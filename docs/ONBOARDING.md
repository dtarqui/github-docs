# Onboarding — Ecosistema "Mini-GitHub" (arquitectura real)

> **Propósito.** Mapa técnico de **lo que el código realmente hace hoy**, a partir de una lectura archivo por archivo de los 11 repositorios. Es complementario —y en varios puntos divergente— de los documentos de diseño (`semana1/Github - Diseño Técnico.md`, `README.md`, `ModeloDeDatos.md`). Cuando diseño y código difieren, este documento describe el **código**.
>
> **Fecha de la lectura:** 2026-06-21. **Alcance:** `Github-users-ms`, `Github-repository-ms`, `Github-files-ms`, `Github-issues-ms`, `Github-pullrequest-ms`, `Github-organizations-ms`, `Github-front`, `Github-git`, `Github-Cdk`, `Github-Smithy`, `github-docs`.

---

## 1. La idea en una frase

Plataforma **contract-first** (Smithy → OpenAPI/proto): un **frontend Next.js** habla con **microservicios Java/Spring** (cada uno con su propia BD), autenticados por **JWT de Keycloak**, que se comunican por **REST + gRPC**, y delegan el Git real a un **servidor Git** por SSH/HTTP.

---

## 2. Tabla maestra de servicios (realidad del código)

| Servicio | Stack real | BD | HTTP | gRPC | Auth | Estado |
|---|---|---|---|---|---|---|
| **users-ms** | Java 25 · Spring Boot 4.0.6 | PostgreSQL (espejo de Keycloak) | 8081 | 9092 | Keycloak (delega identidad) | Funcional |
| **repository-ms** | Java 25 · Spring Boot 4.0.5 | **MongoDB** | 8090 | 9092 | JWT Keycloak | Funcional (authz floja) |
| **files-ms** | Java 25 · Spring Boot 4.0.6 | PostgreSQL (**blobs Base64**) | 8084 `/api` | — | **Ninguna** (anuncia JWT, no lo implementa) | Funcional |
| **issues-ms** | Java 17 · Spring Boot 3.4.5 | PostgreSQL | 8091 | 9091 | JWT Keycloak | Funcional |
| **pullrequest-ms** | Java 25 · Spring Boot 4.0.6 | PostgreSQL | 8082 `/api` | 9092 | JWT Keycloak | Funcional (gRPC merge roto) |
| **organizations-ms** | Java 17 · Spring Boot 3.4.5 | PostgreSQL | 8085 | 9090 | JWT Keycloak | Parcial (stubs a users/repos) |
| **git server** | Ubuntu · SSH + Apache `git-http-backend` | FS (repos bare) | 80 (int) / 22 SSH | — | Hook `git-auth` → repository-ms | Funcional |
| **front** | Next.js 16 · React 19 · TS · Tailwind | — | 3000 | — | OIDC/PKCE + ROPC + mock | Funcional |
| **Github-Cdk** | TypeScript · AWS CDK v2 | — | — | — | — | Keycloak stack **desconectado** |
| **Search Service** | — | Elasticsearch (solo diseño) | 3004 | — | — | **NO existe** |

> El diseño asumía Node.js+TS y PostgreSQL en todos lados; la realidad es **Java/Spring en todo el backend**, con **MongoDB** en repository-ms y **sin Search, sin MinIO, sin Redis, sin RabbitMQ, sin API Gateway**.

---

## 3. Mapa de comunicación real

```
                         ┌──────────────┐
   Browser ──HTTPS──►    │ front (3000) │  Next.js, JWT en localStorage
                         └──────┬───────┘
        (no hay API Gateway real; el front llama a cada MS por rewrites de Next)
   ┌───────────┬───────────┬─────────┴────┬────────────┬─────────────┐
   ▼           ▼           ▼              ▼            ▼             ▼
 users(8081) repos(8090) files(8084)  issues(8091) pulls(8082)  orgs(8085)
   │           │                                       │
   │ Keycloak  │ gRPC/REST                             │ REST
   ▼ (admin +  ▼                                       ▼
  Keycloak)  git-server ◄── git-auth /internal/ssh-access   pulls──►repos (merge real)
             (SSH 2222 / Apache 80)                    orgs──►(users/repos: STUB)
```

- **No hay API Gateway implementado** (el diseño lo pone como pieza central). El front apunta directo a cada microservicio vía *rewrites* de Next.
- **repository-ms es el hub Git:** crea/borra repos bare, hace push/clone con JGit, y autoriza el acceso SSH (`GET /internal/ssh-access`) que consulta el `git-auth` del servidor Git.
- **pullrequest-ms → repository-ms** (REST `POST /repos/{owner}/{repo}/merge`) para el merge real de ramas.
- **organizations-ms** está pensado para llamar a users/repos, pero esas integraciones son **stubs** (genera UUIDs aleatorios; `listOrgRepos` devuelve vacío).
- **gRPC interno** existe en 5 servicios pero su uso real entre servicios es mínimo; ningún servicio indexa en un Search.

---

## 4. Mapa de puertos

| Puerto | Servicio | Notas |
|---|---|---|
| 3000 | front (Next.js) | dev y Docker |
| 8081 / 9092 | users-ms | HTTP / gRPC |
| 8082 / 9092 | pullrequest-ms | HTTP context-path `/api` |
| 8084 / — | files-ms | HTTP context-path `/api`, sin gRPC |
| 8085 / 9090 | organizations-ms | (Dockerfile expone 8083 por error) |
| 8090 / 9092 | repository-ms | gRPC 9092 no expuesto en Dockerfile |
| 8091 / 9091 | issues-ms | (Dockerfile expone 8080 por error) |
| 22 (2222 host) / 80 | git-server | SSH externo / Apache interno |

> Los `EXPOSE` de varios Dockerfiles **no coinciden** con el puerto real de la app. El front tiene además variables de puerto inconsistentes entre `.env`, `.env.example` y los rewrites (ORG: 8083 vs 8085; ISSUES: 8091 vs 8085).

---

## 5. Resumen por servicio

### users-ms (Auth) — Java/Spring Boot 4 · PostgreSQL · 8081/9092
- **Rol:** identidad. **Delega todo a Keycloak**: el login es un `grant_type=password` contra Keycloak; no emite tokens propios ni hashea contraseñas. La tabla `usuarios` (schema `usuarios_nuevo`) es un **espejo** cuya PK es el UUID de Keycloak.
- **API:** REST `/v1/users` (CRUD + `/search` dinámico por `Specification`), passthrough `/v1/keycloak/*`, auth por filtros de Spring Security (`/v1/auth/login|logout`). gRPC `UserApi`/`UserPublicApi`. Roles ADMIN/USER_MANAGER/VIEWER (`@PreAuthorize`).
- **Riesgos:** `.env` con secretos reales (password RDS + 2 client secrets Keycloak); **edit/delete NO se propagan a Keycloak** (desincroniza BD↔Keycloak); stack traces en respuestas de error; README/docs heredados de otro proyecto ("Inspire").
- **Archivos clave:** `config/security/SecurityConfig.java`, `config/security/KeycloakLoginFilter.java`, `service/implementacion/{AuthServiceImpl,UserServiceImpl,KeycloakServiceImpl}.java`, `model/User.java`, `src/main/proto/user_service.proto`.

### repository-ms (Repo) — Java/Spring Boot 4 · MongoDB · 8090/9092
- **Rol:** metadatos de repos + orquestador del git-server (JGit). Colecciones: `repositories`, `branches`, `collaborators`, `file_entries`, `stars`. Búsqueda = regex sobre Mongo (no Elasticsearch).
- **API:** REST Smithy (repos, branches, collaborators, contents, social/stars, forks) + gRPC dual (público/privado). Proxy Git `/{owner}/{repo}.git/**`. Gate `GET /internal/ssh-access`. Integra organizations-ms para mezclar colaboradores de equipos.
- **Roles:** READ/WRITE/ADMIN/MAINTAIN (no Owner/Developer/Reporter del diseño).
- **Riesgo crítico:** el `AccessService` correcto **solo se aplica al canal SSH**; las **mutaciones y lecturas HTTP/gRPC no validan ownership** → cualquiera puede borrar repos ajenos y **leer repos privados sin auth**. Además: fork con `ownerId` aleatorio, borrado sin cascada en Mongo, clona el repo entero por request (lento), rompe en Windows (`PosixFilePermissions`), `MICROSERVICE_AUTH_TOKEN` con default `some-secret-token`.
- **Archivos clave:** `service/git/AccessServiceImpl.java`, `service/implementacion/RepositoryServiceImpl.java`, `controller/InternalController.java`, `grpc/`, `config/SecurityConfig.java`.

### files-ms (Files) — Java/Spring Boot 4 · PostgreSQL · 8084/api
- **Rol:** contenido de archivos, commits, diffs, comparar ramas. **Sin MinIO/S3**: el contenido va **Base64 en `files.content`**. El SHA no es el de Git real; `patch` siempre `null` (los diffs salen vacíos).
- **API:** REST Smithy (`contents`, `download`, `folders`, `commits`, `compare`). **Sin gRPC.**
- **Riesgos:** **sin autenticación implementada** (endpoints abiertos pese a anunciar JWT), **sin saneo de path-traversal `..`**, secretos en `.env`/`application-aws.yaml`. Solapa funcionalidad de "contents"/commits con repository-ms (ambigüedad sobre la fuente de verdad). `RepositoryService` interno es código no alcanzable desde la API.
- **Archivos clave:** `service/implementacion/{FileServiceImpl,CommitServiceImpl}.java`, `delegate/V1ApiDelegateImpl.java`, `model/FileEntity.java`, `src/main/resources/schema.sql`.

### issues-ms (Issues) — Java/Spring Boot 3.4.5 · PostgreSQL · 8091/9091
- **Rol:** issues, labels (N:M), comentarios. `repo_id` = string `"owner/repo"` (referencia lógica, no validada). Numeración `MAX(number)+1` por repo.
- **API:** REST `/v1/repos/{o}/{r}/{issues,labels}` + comentarios; gRPC dual. Triggers SQL para `comments_count`/`updated_at`.
- **Riesgos:** **race condition** en numeración (sin lock/secuencia); labels inexistentes ignorados en silencio; **no hay PRs aquí** (contradice el modelo de datos del diseño, que ubicaba PR en Issue Service); Java 25 (pom) vs JDK 17 (Docker/CI); triggers no se aplican con `ddl-auto: update`; comentarios solo de issues (sin la "exclusión mutua issue/PR" del diseño).
- **Archivos clave:** `service/implementacion/IssueServiceImpl.java`, `schema.sql`, `controller/`, `src/main/openapi/IssueApi.json`, `src/main/proto/issue_service.proto`.

### pullrequest-ms (PRs) — Java/Spring Boot 4 · PostgreSQL · 8082/api
- **Rol:** PRs, reviews, comentarios, merge. **Microservicio independiente** (el diseño lo ponía dentro de issues). Mantiene réplica local de `repositories` (lazy-sync desde repository-ms).
- **Lógica de merge:** PR abierto → sin conflictos → ≥1 review `APPROVED` → 0 `CHANGES_REQUESTED` → **merge real delegado a repository-ms** (REST). BD propia `github_pullrequest_db`.
- **Riesgos:** **gRPC `MergePullRequest` no compila** (6 args vs 7) y **tests desfasados** → la integración de merge se añadió sin actualizar gRPC/tests; **sin autorización de dominio** (cualquier autenticado mergea/revisa/cierra cualquier PR); `hasConflicts`/`commitsCount` nunca se calculan (la detección de conflictos es un flag muerto); `mergeBranches` usa `/repos/...` sin `/v1`.
- **Archivos clave:** `service/implementacion/PullRequestServiceImpl.java`, `client/RepositoryApiClient.java`, `delegate/V1ApiDelegateImpl.java`, `schema.sql`.

### organizations-ms (Orgs) — Java/Spring Boot 3.4.5 · PostgreSQL · 8085/9090
- **Rol:** orgs, members, teams, team-members, team-repos. Completo **dentro de su BD**, pero las integraciones con users y repos son **stubs** (`addOrgMember`/`addTeamRepo` generan UUID aleatorio; `listOrgRepos` vacío; `collaborators` siempre vacío en `getRepoAccess`).
- **API:** REST `/v1/orgs/**`, `/v1/user/orgs`, `/v1/repos/{o}/{r}/access/teams` (extra fuera de contrato) + gRPC dual.
- **Riesgos:** rol `DEVELOPER` es **código muerto** (authz solo distingue owner exacto vs miembro); fuga de orgs privadas en `GET /v1/orgs/{name}`; Smithy desconectado del build (usa `OrgApi.json`); secretos en `.env`; Java 25 vs JDK 17; falta README; `IllegalStateException` (sin auth) → 500/INTERNAL en vez de 401.
- **Archivos clave:** `service/implementacion/*ServiceImpl.java`, `controller/`, `src/main/openapi/OrgApi.json`, `src/main/proto/org_service.proto`, `schema.sql`.

### git-server — Ubuntu · SSH + Apache · 22/80
- **Rol:** almacén de repos bare. **SSH (2222 host)** es el canal con clientes, con hook `git-auth` que delega la autorización a repository-ms (`/internal/ssh-access`). **Apache `git-http-backend` (80)** es interno, **sin auth** (lo proxea repository-ms). Sin TLS propio.
- **Riesgos:** `git-admin.cgi` permite crear/borrar repos e **inyectar claves SSH** con token opcional y **sin saneo de path-traversal**, y el puerto 80 **sí se publica** en dev (`9080:80`) pese a la doc → cadena de explotación grave. `git-auth` tampoco sanea `..` en el path del repo. Contradice el diseño "HTTPS sin SSH".
- **Aciertos:** `sshd_config` muy endurecido; usuario `git` con `git-shell`; `manage-repo.sh` sí valida nombres.
- **Archivos clave:** `git-auth`, `git-admin.cgi`, `start.sh`, `manage-repo.sh`, `Dockerfile`, `docker-compose.yml`.

### front — Next.js 16 · React 19 · TS · 3000
- **Rol:** SPA completa (repos, archivos, commits, PRs, issues, orgs, teams). 3 modos de auth: **OIDC/PKCE Keycloak**, ROPC (`grant_type=password`), y **mock `demo/demo`** (flag).
- **Riesgos:** **JWT en `localStorage`** (XSS), **sin guards server-side** (no hay `middleware.ts`), puertos/URLs inconsistentes entre `.env`/README/rewrites, logging que filtra tokens, ELB Keycloak público en `.env`, `/dashboard` con datos mock, `users-api` cae a mock ante errores.
- **Archivos clave:** `src/lib/auth/auth-context.tsx`, `src/lib/api/repository-api.ts`, `next.config.ts`, `.env`/`.env.example`, `src/app/layout.tsx`.

### Github-Cdk — AWS CDK v2 · TS
- **Rol:** infraestructura. Tiene el `KeycloakStack` completo (VPC sin NAT + EKS v1.29 + RDS PostgreSQL + manifiestos Keycloak), **pero está comentado** en `bin/github-cdk.ts`; por defecto solo despliega un ejercicio S3→Lambda→DynamoDB.
- **Riesgos:** passwords en texto plano (`unsafePlainText`); nodos EKS y control plane en subredes públicas (`PUBLIC_AND_PRIVATE`); SG de RDS abre 5432 a toda la VPC; scripts `synth:*`/`deploy:*` rotos (apuntan a `bin/*` inexistentes); `S3StaticWebsiteStack` con bucket público; dependencia `cdk-rds-sql` huérfana.
- **Archivos clave:** `bin/github-cdk.ts`, `config/app-config.ts`, `lib/stacks/keycloak-stack.ts`, `lib/constructs/{network,cluster,database,keycloak}/`.

---

## 6. Modelo de datos (database-per-service)

| BD | Motor | Tablas / colecciones |
|---|---|---|
| auth | PostgreSQL | `usuarios` (espejo Keycloak) |
| repository | **MongoDB** | repositories, branches, collaborators, file_entries, stars |
| files | PostgreSQL | repositories, files (content Base64), commits, commit_files |
| issues | PostgreSQL | issues, labels, issue_labels, issue_comments |
| pullrequest | PostgreSQL | repositories (réplica), pull_requests, pull_request_reviews, pull_request_comments |
| organizations | PostgreSQL | organizations, org_members, teams, team_members, team_repos |

El patrón `database-per-service` **se cumple**, con referencias lógicas por UUID/string (`repo_id = "owner/repo"`) y **sin FK cross-service** — pero **nadie valida esas referencias** (issues no comprueba que el repo exista, orgs inventa los IDs de users/repos, etc.).

---

## 7. Divergencias diseño ↔ implementación

| Diseño dice | Realidad |
|---|---|
| Node.js + TS + Prisma | Java + Spring Boot en todo el backend |
| PostgreSQL en todos | repository-ms usa MongoDB |
| MinIO/S3 para blobs | Base64 en PostgreSQL (files-ms); bare repos en git-server |
| PR dentro de Issue Service | Microservicio PR independiente (`github_pullrequest_db`) |
| Files dentro de Repo Service | Microservicio Files independiente (solapa con repo-ms) |
| Search Service + Elasticsearch | No existe; búsqueda = regex/LIKE local |
| Redis (caché/sesiones) | No se usa |
| API Gateway central | No implementado (front llama directo) |
| Roles Owner/Developer/Reporter | repos: READ/WRITE/ADMIN · users: ADMIN/USER_MANAGER/VIEWER · orgs: owner/member (developer muerto) |
| "HTTPS sin SSH" para Git | SSH es el canal principal; HTTP interno sin auth |
| gRPC para indexación a Search | gRPC existe pero casi no se usa entre servicios |

---

## 8. Hallazgos transversales

### Seguridad (patrón sistémico)
1. **Secretos reales commiteados en `.env`** en users, files, issues, organizations, repository y front (password RDS `githubPass123`, client secrets de Keycloak, ELB público). *Acción: rotar y purgar del historial.*
2. **Autorización de dominio ausente o incompleta:** repository-ms, files-ms y pullrequest-ms permiten operar sobre recursos ajenos con solo estar autenticado (o sin auth alguna, en files-ms).
3. **Repos privados expuestos** (repository-ms: lecturas en `permitAll`, sin chequeo de visibilidad).
4. **git-admin.cgi explotable** (inyección de claves SSH, sin saneo de path, token opcional, puerto publicado en dev).
5. **front:** JWT en `localStorage`, sin guards server-side, modo mock activable por flag.

### Calidad / consistencia
- **Java 25 (pom) vs JDK 17 (Docker/CI)** en issues-ms y organizations-ms → build inconsistente.
- **`EXPOSE` de Dockerfiles no coinciden** con los puertos reales en casi todos.
- **README/docs son plantillas heredadas** desconectadas del código (users, repository, organizations).
- **`ddl-auto: update` + `schema.sql`/triggers** → doble fuente de esquema; triggers que no se aplican.
- **gRPC no expuesto** en varios Dockerfiles aunque el servicio lo levanta.
- **Rutas sin `/v1`** en algunos endpoints (repository-ms compare/merge; pullrequest-ms merge a repos).

---

## 9. Cómo levantar el sistema (estado para la demo)

No hay un `docker-compose` raíz que orqueste todo (cada repo trae el suyo). Para una demo habría que: levantar **Keycloak + PostgreSQL + MongoDB**, configurar el realm de Keycloak, arrancar los 6 microservicios + git-server, y el front apuntando a los puertos correctos.

**Bloqueadores conocidos:**
- Puertos/URLs inconsistentes front↔back.
- gRPC de merge que no compila en pullrequest-ms (el merge por REST sí funciona).
- Integraciones stub en organizations-ms (members/repos con IDs ficticios).
- `Search` inexistente (el front no lo usa, así que no bloquea).
- `KeycloakStack` de CDK comentado (despliegue cloud no operativo por defecto).

---

## 10. Convención de contrato (Smithy)

El servicio agregador `com.githubx#GitHubApi` (`Github-Smithy/model/service.smithy`) reúne ~80 operaciones de los dominios auth, repo, files, issue, pullrequest, search y organization bajo prefijo `/v1`. Cada microservicio consume su porción del modelo (algunos generan controllers/DTOs Spring desde Smithy vía Gradle; otros usan un `OrgApi.json`/`IssueApi.json` exportado y desconectan el Smithy del build). El inventario de endpoints REST está en `APIS_RESUMEN.md`.
