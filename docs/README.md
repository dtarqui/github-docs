# GitHub

> Proyecto académico para la materia **Arquitectura en la Nube y Microservicios**

Recreación simplificada de GitHub utilizando arquitectura de microservicios, contenedorización y despliegue en la nube.

*Diseño técnico de Proyecto Github* Ingresar aquí ->  [Github Diseño Tecnico](https://github.com/dtarqui/github-docs/blob/main/docs/semana1/Github%20-%20Dise%C3%B1o%20T%C3%A9cnico.md) 
## Repositorios

| Respositorios                                                                      | Responsable    | Progreso                                                                           |
|------------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------|
| **[Github-users-ms](https://github.com/Savitar465/Github-users-ms.git)**           | Jonas Maidana  | Se agregó docker compose con keycloak y base de datos, se implemento AuthZ y AuthN |
| **[Github-files-ms](https://github.com/Savitar465/Github-files-ms.git)**           | David Rivas    | Repositorio creado con su proyecto smithy respectivo                               |
| **[Github-repository-ms](https://github.com/Savitar465/Github-repository-ms.git)** | Daniel Tarqui  | Repositorio creado con su proyecto smithy respectivo                               |
| **[Github-organizations-ms](https://github.com/dtarqui/Github-organizations-ms)**  | Harold Sanchez | Repositorio creado con su proyecto                                                 |
| **[Github-pullrequests-ms](https://github.com/Savitar465/Github-pullrequests-ms)**   | Jonas Maidana  | Repositorio creado con su proyecto                                                 |
| **[Github-Smithy](https://github.com/Savitar465/Github-Smithy)**           | Equipo         | Proyecto inicial de Smithy que se separará en los diferentes microservicios        |
| **[Github-Cdk](https://github.com/Savitar465/Github-Cdk)**           | Equipo         | En progreso, despliegue de Keycloak en ECS con RDS PostgreSQL y ALB                |
| **[Github-issues-ms](https://github.com/Savitar465/Github-issues-ms.git)**           | Harold Sanchez | Repositorio creado con su proyecto |

> **Nota:** Los roles pueden solaparse según el tamaño del equipo

---
---

## Tabla de Contenidos

- [Descripción](#descripción)
- [Alcances y Límites](#alcances-y-límites)
- [Requisitos Funcionales (RF)](#requisitos-funcionales-rf)
- [Requisitos No Funcionales (RNF)](#requisitos-no-funcionales-rnf)
- [Plan de Trabajo (4 Semanas)](#plan-de-trabajo-4-semanas)
- [Base de Datos](#base-de-datos)
- [API Endpoints](#api-endpoints)
- [Arquitectura](#arquitectura)
- [Stack Tecnológico](#stack-tecnológico)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Microservicios](#microservicios)
- [Diagramas](#diagramas)
- [Instalación y Configuración](#instalación-y-configuración)
- [Despliegue](#despliegue)

---

## Descripción

**GitHub** es una plataforma simplificada de control de versiones y colaboración que permite a los usuarios:

- Crear y gestionar repositorios
- Subir y descargar archivos
- Gestionar issues y seguimiento de problemas
- Colaborar en proyectos

El objetivo principal es demostrar competencias en:

- Diseño de arquitectura de microservicios
- Contenedorización con Docker
- Despliegue en servicios cloud
- Patrones de comunicación entre servicios
- AuthN/AuthZ con OIDC usando Keycloak
- Diseño de contratos API con Smithy

---

## Alcances y Límites

### Alcances (Dentro del Proyecto)

#### Funcionalidades Incluidas

| Módulo            | Alcance                             | Descripción                                                    |
| ----------------- | ----------------------------------- | -------------------------------------------------------------- |
| **Autenticación** | Registro y login con email/password | Sistema completo de autenticación con JWT                      |
| **Autenticación** | OIDC/SSO con Keycloak               | Integración con Keycloak como proveedor principal de identidad |
| **Repositorios**  | CRUD completo                       | Crear, leer, actualizar y eliminar repositorios                |
| **Repositorios**  | Visibilidad                         | Repositorios públicos y privados                               |
| **Archivos**      | Gestión básica                      | Subir, descargar, visualizar y eliminar archivos               |
| **Archivos**      | Navegación                          | Explorador de archivos con estructura de carpetas              |
| **Issues**        | CRUD completo                       | Crear, editar, cerrar y comentar issues                        |
| **Issues**        | Organización                        | Labels y asignación de usuarios                                |
| **Pull Requests** | Gestión básica                      | Crear PRs, revisar con comentarios, aprobar y merge            |
| **Búsqueda**      | Búsqueda básica                     | Buscar repositorios por nombre y usuarios por username         |
| **API**           | Documentación OpenAPI               | Swagger UI para explorar y probar la API REST                  |

#### Arquitectura y Tecnología

| Aspecto               | Alcance                                                                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Microservicios**    | Mínimo 4 servicios independientes y desplegables                                                                            |
| **Contenedorización** | 100% de servicios dockerizados                                                                                              |
| **Orquestación**      | Docker Compose                                                                                                              |
| **Bases de datos**    | Patrón database-per-service implementado                                                                                    |
| **Comunicación interna** | Comunicación servicio a servicio vía gRPC (unario/streaming según caso)                                                |
| **API Gateway**       | Punto único de entrada con autenticación centralizada                                                                       |
| **Cloud**             | Despliegue funcional en al menos un proveedor cloud                                                                         |
| **CI/CD**             | Sin pipeline integrado en el producto (L-01 en Limites.md); despliegue manual o automatización externa al alcance funcional |

#### Entregables Comprometidos

| Entregable            | Descripción                                               |
| --------------------- | --------------------------------------------------------- |
| Código fuente         | Repositorio con todo el código del proyecto               |
| Documentación técnica | README, diagramas de arquitectura, especificación de APIs |
| Docker Compose        | Configuración para levantar todo el sistema localmente    |
| Demo funcional        | Aplicación desplegada y accesible en la nube              |
| Presentación          | Slides y demo en vivo del proyecto                        |

---

### Límites (Fuera del Proyecto)

#### Funcionalidades Excluidas

| Funcionalidad                          | Razón de Exclusión                                                  | Alternativa Implementada                                                   |
| -------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Servidor Git enterprise**            | Alta complejidad operativa (HA, replicación, hardening avanzado)    | Microservicio Git hosteado con soporte básico HTTPS                        |
| **Branch protection avanzada**         | Reglas complejas de protección y políticas obligatorias             | Gestión básica de branches y validaciones mínimas                          |
| **Code review avanzado**               | Comentarios en línea con sugerencias automáticas y flujos complejos | Comentarios en PR e issues (básico)                                        |
| **GitHub Actions / CI en el producto** | Workflows, runners y ejecución de jobs como parte del sistema       | No incluido (L-01); sin CI/CD dentro del alcance funcional del GitHub |
| **Wikis**                              | Feature secundaria                                                  | README del repositorio                                                     |
| **GitHub Pages**                       | Hosting de sitios estáticos                                         | No incluido                                                                |
| **Gists**                              | Snippets de código compartidos                                      | No incluido                                                                |
| **Notificaciones**                     | Email, push, tiempo real, WebSockets, SSE                           | No incluido (L-06); sin subsistema de notificaciones                       |
| **GitHub Copilot / AI features**       | Integración con modelos de IA                                       | No incluido                                                                |
| **Marketplace / Apps**                 | Ecosistema de integraciones                                         | No incluido                                                                |
| **Seguridad avanzada**                 | Escaneo de vulnerabilidades, Dependabot                             | No incluido                                                                |
| **Insights / Analytics**               | Gráficos de contribuciones, traffic                                 | Estadísticas básicas (stars, issues count)                                 |

#### Limitaciones Técnicas

| Limitación                | Descripción                          | Impacto                                          |
| ------------------------- | ------------------------------------ | ------------------------------------------------ |
| **Tamaño de archivos**    | Máximo 10MB por archivo              | Suficiente para código, no para binarios grandes |
| **Almacenamiento total**  | Limitado por tier gratuito del cloud | ~5GB total en el sistema                         |
| **Usuarios concurrentes** | Diseñado para ~100 usuarios          | Demo académica, no producción                    |
| **Disponibilidad**        | No hay SLA definido                  | Puede haber downtime durante desarrollo          |
| **Backups**               | No automatizados                     | Responsabilidad del equipo de desarrollo         |
| **Multi-región**          | Despliegue en una sola región        | Latencia variable según ubicación                |

#### Limitaciones de Seguridad

| Aspecto              | Limitación                                      |
| -------------------- | ----------------------------------------------- |
| **Auditoría**        | No hay logs de auditoría para compliance        |
| **2FA**              | Autenticación de dos factores no implementada   |
| **Encriptación**     | Solo HTTPS en tránsito, no encriptación at-rest |
| **Rate limiting**    | Básico, no protección contra DDoS avanzada      |
| **Secrets scanning** | No se escanean secretos en repositorios         |

#### Limitaciones de Escalabilidad

| Aspecto           | Limitación                        | Solución Futura (No implementada) |
| ----------------- | --------------------------------- | --------------------------------- |
| **Base de datos** | Instancias únicas sin replicación | Réplicas de lectura, sharding     |
| **Storage**       | MinIO single-node                 | Distribución con erasure coding   |

---

### Comparativa: GitHub Propio vs GitHub Real

| Característica       | GitHub Real       | GitHub     | Estado       |
| -------------------- | ----------------- | --------------- | ------------ |
| Usuarios registrados | 100M+             | Demo (~100)     | Simplificado |
| Repositorios         | Ilimitados        | Limitados       | Simplificado |
| Git protocol         | Completo          | Básico (HTTPS)  | Simplificado |
| Push/Pull/Clone      | SSH, HTTPS        | HTTPS (sin SSH) | Simplificado |
| Branches             | Ilimitadas        | Básicas         | Simplificado |
| Commits history      | Completo          | Básico          | Simplificado |
| Pull Requests        | Completo          | Básico          | Simplificado |
| Issues               | Completo          | Básico          | Simplificado |
| Actions (CI/CD)      | Completo          | No incluido     | Excluido     |
| Packages             | Registry completo | No incluido     | Excluido     |
| Projects             | Kanban boards     | No incluido     | Excluido     |
| Discussions          | Foros             | No incluido     | Excluido     |
| Mobile app           | iOS/Android       | No incluido     | Excluido     |
| API                  | REST + GraphQL    | REST básico     | Simplificado |
| Webhooks             | Completo          | No incluido     | Excluido     |

---

### Supuestos y Dependencias

#### Supuestos

| ID     | Supuesto                                                                        |
| ------ | ------------------------------------------------------------------------------- |
| SUP-01 | El equipo tiene conocimientos básicos de Docker y contenedores                  |
| SUP-02 | Se cuenta con acceso a un proveedor cloud con tier gratuito                     |
| SUP-03 | El equipo puede dedicar al menos 20 horas semanales al proyecto                 |
| SUP-04 | Se tiene acceso a GitHub (u homólogo) para el repositorio del código del equipo |
| SUP-05 | Los usuarios del sistema tienen conexión a internet estable                     |

#### Dependencias Externas

| Dependencia     | Tipo                   | Riesgo si no está disponible      |
| --------------- | ---------------------- | --------------------------------- |
| Docker Hub      | Imágenes base          | Medio - se pueden usar mirrors    |
| npm Registry    | Paquetes Node.js (frontend) / Maven Central (backend) | Alto - crítico para el build |
| Proveedor Cloud | Despliegue             | Alto - no hay demo en producción  |
| GitHub          | Repositorio del código | Medio - se puede usar alternativa |
| MinIO/S3        | Almacenamiento         | Alto - archivos no funcionan      |

---

### Criterios de Aceptación del Proyecto

#### Mínimos para Aprobación

| Criterio | Descripción                                              | Verificación                                            |
| -------- | -------------------------------------------------------- | ------------------------------------------------------- |
| CA-01    | Al menos 4 microservicios funcionando                    | `docker-compose ps` muestra 4+ servicios healthy        |
| CA-02    | Registro y login de usuarios operativo                   | Flujo completo en UI sin errores                        |
| CA-03    | CRUD de repositorios funcional                           | Crear, ver, editar, eliminar repos                      |
| CA-04    | Upload/download de archivos                              | Subir archivo y descargarlo exitosamente                |
| CA-05    | Sistema de issues básico                                 | Crear issue, comentar, cerrar                           |
| CA-06    | Desplegado en cloud                                      | URL pública accesible                                   |
| CA-07    | Despliegue del proyecto verificable sin pipeline interno | Evidencia de build/deploy manual o automatizado externo |
| CA-08    | Documentación completa                                   | README, diagramas, API docs                             |

#### Deseables (Valor Agregado)

| Criterio | Descripción                                            |
| -------- | ------------------------------------------------------ |
| CD-01    | SSO con Keycloak funcionando (login federado opcional) |
| CD-02    | Métricas y health checks expuestos                     |
| CD-04    | Tests automatizados (>50% coverage)                    |
| CD-05    | Logs centralizados                                     |

---

## Requisitos Funcionales (RF)

### RF01 - Gestión de Usuarios

| ID     | Requisito                                                               | Prioridad |
| ------ | ----------------------------------------------------------------------- | --------- |
| RF01.1 | El sistema debe permitir el registro de usuarios con email y contraseña | Alta      |
| RF01.2 | El sistema debe permitir autenticación mediante OIDC/SSO con Keycloak   | Alta      |
| RF01.3 | El sistema debe permitir la edición del perfil de usuario               | Media     |
| RF01.4 | El sistema debe permitir la recuperación de contraseña                  | Baja      |

### RF02 - Gestión de Repositorios

| ID     | Requisito                                                       | Prioridad |
| ------ | --------------------------------------------------------------- | --------- |
| RF02.1 | El sistema debe permitir crear repositorios públicos y privados | Alta      |
| RF02.2 | El sistema debe permitir eliminar repositorios propios          | Alta      |
| RF02.3 | El sistema debe permitir editar la información del repositorio  | Media     |
| RF02.4 | El sistema debe mostrar la lista de repositorios del usuario    | Alta      |
| RF02.5 | El sistema debe permitir gestionar branches de repositorios     | Media     |
| RF02.6 | El sistema debe permitir hacer fork de repositorios públicos    | Baja      |

### RF03 - Gestión de Archivos

| ID     | Requisito                                                     | Prioridad |
| ------ | ------------------------------------------------------------- | --------- |
| RF03.1 | El sistema debe permitir subir archivos a un repositorio      | Alta      |
| RF03.2 | El sistema debe permitir descargar archivos de un repositorio | Alta      |
| RF03.3 | El sistema debe mostrar el contenido de archivos de texto     | Alta      |
| RF03.4 | El sistema debe permitir crear carpetas                       | Media     |
| RF03.5 | El sistema debe permitir eliminar archivos                    | Alta      |

### RF04 - Gestión de Issues

| ID     | Requisito                                               | Prioridad |
| ------ | ------------------------------------------------------- | --------- |
| RF04.1 | El sistema debe permitir crear issues en un repositorio | Alta      |
| RF04.2 | El sistema debe permitir asignar labels a los issues    | Media     |
| RF04.3 | El sistema debe permitir comentar en issues             | Alta      |
| RF04.4 | El sistema debe permitir cerrar/reabrir issues          | Alta      |
| RF04.5 | El sistema debe permitir asignar usuarios a issues      | Media     |

### RF05 - Búsqueda

| ID     | Requisito                                               | Prioridad |
| ------ | ------------------------------------------------------- | --------- |
| RF05.1 | El sistema debe permitir buscar repositorios por nombre | Alta      |
| RF05.2 | El sistema debe permitir buscar usuarios                | Media     |

### RF06 - Colaboración

| ID     | Requisito                                                                                                 | Prioridad |
| ------ | --------------------------------------------------------------------------------------------------------- | --------- |
| RF06.1 | El sistema debe permitir gestionar colaboradores de un repositorio con roles (Owner, Developer, Reporter) | Media     |

### RF07 - Pull Requests

| ID     | Requisito                                                                | Prioridad |
| ------ | ------------------------------------------------------------------------ | --------- |
| RF07.1 | El usuario puede crear Pull Requests entre branches                      | Media     |
| RF07.2 | Los reviewers pueden aprobar o solicitar cambios en Pull Requests        | Media     |
| RF07.3 | El sistema debe detectar conflictos antes del merge y bloquear si aplica | Media     |

---

## Requisitos No Funcionales (RNF)

### Arquitectura y Diseño

| ID    | Requisito                                                        | Métrica                             |
| ----- | ---------------------------------------------------------------- | ----------------------------------- |
| RNF01 | El sistema debe implementar arquitectura de microservicios       | Mínimo 5 servicios independientes   |
| RNF02 | Cada microservicio debe tener su propia base de datos            | 1 BD por servicio                   |
| RNF03 | Los servicios deben comunicarse mediante API REST y/o mensajería | 100% de comunicaciones documentadas |

### Contenedorización y Orquestación

| ID    | Requisito                                                 | Métrica                      |
| ----- | --------------------------------------------------------- | ---------------------------- |
| RNF04 | Todos los servicios deben estar contenedorizados          | 100% servicios en Docker     |
| RNF05 | El sistema debe usar Docker Compose para desarrollo local | docker-compose.yml funcional |

### Cloud y Despliegue

| ID    | Requisito                                                                                                         | Métrica                                            |
| ----- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| RNF07 | El sistema debe desplegarse en un proveedor cloud                                                                 | AWS/GCP/Azure                                      |
| RNF08 | Sin pipeline CI/CD integrado en el producto (alineado con L-01); despliegue manual o externo al alcance funcional | Evidencia de despliegue sin workflows en el código |
| RNF09 | El sistema debe tener configuración por variables de entorno                                                      | 0 credenciales hardcodeadas                        |

### Rendimiento y Escalabilidad

| ID    | Requisito                                                   | Métrica                                              |
| ----- | ----------------------------------------------------------- | ---------------------------------------------------- |
| RNF10 | El API Gateway debe responder en menos de 200ms             | p95 < 200ms en pruebas con 100 usuarios concurrentes |
| RNF11 | Los servicios deben poder escalar horizontalmente           | Réplicas configurables                               |
| RNF12 | El sistema debe soportar al menos 100 usuarios concurrentes | Load test k6 exitoso sin errores críticos            |

### Seguridad

| ID    | Requisito                                                 | Métrica                             |
| ----- | --------------------------------------------------------- | ----------------------------------- |
| RNF13 | Todas las comunicaciones externas deben usar HTTPS (TLS 1.3) | 100% endpoints HTTPS             |
| RNF14 | La autenticación debe usar JWT con expiración             | Access token 15m + refresh token 7d |
| RNF15 | Las contraseñas deben almacenarse hasheadas               | bcrypt con salt                     |
| RNF16 | Tokens de acceso con scopes y RBAC por repositorio        | Roles Owner/Developer/Reporter      |
| RNF17 | Cifrado en reposo (AES-256) y en tránsito                 | Datos sensibles cifrados            |
| RNF18 | Aislamiento total entre repositorios privados             | Sin acceso cross-tenant             |

### Usabilidad

| ID    | Requisito                                   | Métrica                        |
| ----- | ------------------------------------------- | ------------------------------ |
| RNF19 | Diseño responsivo y accesible               | Mobile-first, WCAG 2.1 AA      |
| RNF20 | Interfaz funcional en navegadores modernos  | Chrome, Firefox, Safari, Edge  |

### Observabilidad y Mantenibilidad

| ID    | Requisito                                              | Métrica                            |
| ----- | ------------------------------------------------------ | ---------------------------------- |
| RNF21 | El sistema debe tener logging centralizado y estructurado | Logs en formato JSON            |
| RNF22 | El sistema debe exponer métricas de salud (health checks) | Endpoints /health en cada servicio |
| RNF23 | Monitoreo con Prometheus/Grafana                       | Dashboards operativos              |
| RNF24 | Infraestructura como código (Terraform)                | 100% IaC versionado                |
| RNF25 | Despliegues automatizados con rollback (infraestructura del equipo, no feature del producto) | Pipeline de despliegue funcional |
| RNF26 | Ambientes de staging y producción separados            | 2 ambientes mínimo                 |

---

## Plan de Trabajo (4 Semanas)

### Semana 1: Fundamentos y Auth Service

| Día | Tareas                                                          |
| --- | --------------------------------------------------------------- |
| 1-2 | Setup del proyecto, estructura de carpetas, Docker Compose base |
| 3-4 | Auth Service: registro, login, JWT                              |
| 5   | API Gateway básico con routing                                  |
| 6-7 | Frontend: páginas de login/registro                             |

**Entregables:**

- [ ] Estructura del proyecto
- [ ] Auth Service funcionando
- [ ] API Gateway con autenticación
- [ ] UI de autenticación

### Semana 2: Repo Service y Archivos

| Día | Tareas                                                  |
| --- | ------------------------------------------------------- |
| 1-2 | Repo Service: CRUD de repositorios                      |
| 3-4 | Integración con MinIO para archivos                     |
| 5   | Upload/download de archivos                             |
| 6-7 | Frontend: dashboard, crear repo, explorador de archivos |

**Entregables:**

- [ ] CRUD de repositorios
- [ ] Gestión de archivos
- [ ] UI de repositorios

### Semana 3: Issues

| Día | Tareas                        |
| --- | ----------------------------- |
| 1-2 | Issue Service: CRUD de issues |
| 3   | Comentarios en issues         |
| 4-7 | Frontend: issues              |

**Entregables:**

- [ ] Sistema de issues completo
- [ ] UI de issues

### Semana 4: Cloud, Despliegue y Documentación

| Día | Tareas                                                                             |
| --- | ---------------------------------------------------------------------------------- |
| 1-2 | Configuración de infraestructura cloud                                             |
| 3-4 | Preparación de despliegue y validación operativa (sin pipeline CI/CD del producto) |
| 5   | Despliegue en cloud (AWS/GCP/Azure)                                                |
| 6-7 | Testing, documentación, presentación                                               |

**Entregables:**

- [ ] Aplicación desplegada en cloud
- [ ] Despliegue validado (sin pipeline CI/CD del producto)
- [ ] Documentación completa
- [ ] Demo funcional

---

## Base de Datos

### Auth Service - PostgreSQL

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    avatar_url VARCHAR(500),
    bio TEXT,
    location VARCHAR(100),
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- OAuth accounts
CREATE TABLE oauth_accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    provider VARCHAR(50) NOT NULL,
    provider_account_id VARCHAR(255) NOT NULL,
    access_token TEXT,
    refresh_token TEXT,
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(provider, provider_account_id)
);

-- Sessions
CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    token VARCHAR(500) UNIQUE NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Repo Service - PostgreSQL

```sql
-- Repositories
CREATE TABLE repositories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(150) NOT NULL,
    description TEXT,
    is_private BOOLEAN NOT NULL DEFAULT false,
    owner_id UUID NOT NULL,
    default_branch VARCHAR(100) DEFAULT 'main',
    language VARCHAR(50),
    forks_count INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(owner_id, name)
);

-- Repository files (metadata; contenido en MinIO/S3)
CREATE TABLE repo_files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    repository_id UUID NOT NULL REFERENCES repositories(id) ON DELETE CASCADE,
    path VARCHAR(512) NOT NULL,
    storage_key VARCHAR(512) NOT NULL,
    content_type VARCHAR(100),
    size_bytes BIGINT,
    branch VARCHAR(100),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Issue Service - PostgreSQL

```sql
-- Issues table
CREATE TABLE issues (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    repo_id UUID NOT NULL,
    number SERIAL,
    title VARCHAR(255) NOT NULL,
    body TEXT,
    state VARCHAR(20) DEFAULT 'open',
    author_id UUID NOT NULL,
    assignee_id UUID,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    closed_at TIMESTAMP,
    UNIQUE(repo_id, number)
);

-- Labels table
CREATE TABLE labels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    repo_id UUID NOT NULL,
    name VARCHAR(50) NOT NULL,
    color VARCHAR(7) NOT NULL,
    description VARCHAR(255),
    UNIQUE(repo_id, name)
);

-- Issue Labels (many-to-many)
CREATE TABLE issue_labels (
    issue_id UUID REFERENCES issues(id) ON DELETE CASCADE,
    label_id UUID REFERENCES labels(id) ON DELETE CASCADE,
    PRIMARY KEY (issue_id, label_id)
);

-- Comments table
CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    issue_id UUID REFERENCES issues(id) ON DELETE CASCADE,
    author_id UUID NOT NULL,
    body TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## API Endpoints

### Auth Service

| Método | Endpoint                      | Descripción                     |
| ------ | ----------------------------- | ------------------------------- |
| POST   | `/api/auth/register`          | Registrar nuevo usuario         |
| POST   | `/api/auth/login`             | Iniciar sesión                  |
| POST   | `/api/auth/logout`            | Cerrar sesión                   |
| POST   | `/api/auth/refresh`           | Refrescar token                 |
| GET    | `/api/auth/me`                | Obtener usuario actual          |
| GET    | `/api/auth/login/keycloak`    | Iniciar login OIDC con Keycloak |
| GET    | `/api/auth/callback/keycloak` | Callback OIDC de Keycloak       |

Nota: el usuario autenticado se deriva del token Bearer y no desde campos `user_id` enviados por el cliente.

**Ejemplos:**

```bash
# Registro
POST /api/auth/register
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!"
}

# Response
{
  "success": true,
  "data": {
    "user": {
      "id": "uuid",
      "username": "johndoe",
      "email": "john@example.com"
    },
    "token": "eyJhbGciOiJIUzI1NiIs..."
  }
}
```

### Repo Service

| Método | Endpoint                                 | Descripción              |
| ------ | ---------------------------------------- | ------------------------ |
| GET    | `/api/repos`                             | Listar repos del usuario |
| POST   | `/api/repos`                             | Crear repositorio        |
| GET    | `/api/repos/:owner/:repo`                | Obtener repositorio      |
| PATCH  | `/api/repos/:owner/:repo`                | Actualizar repositorio   |
| DELETE | `/api/repos/:owner/:repo`                | Eliminar repositorio     |
| GET    | `/api/repos/:owner/:repo/contents/*path` | Obtener contenido        |
| PUT    | `/api/repos/:owner/:repo/contents/*path` | Subir archivo            |
| DELETE | `/api/repos/:owner/:repo/contents/*path` | Eliminar archivo         |

**Ejemplos:**

```bash
# Crear repositorio
POST /api/repos
{
  "name": "my-project",
  "description": "My awesome project",
  "visibility": "public"
}

# Subir archivo
PUT /api/repos/johndoe/my-project/contents/src/index.js
Content-Type: multipart/form-data
{
  "file": <binary>,
  "message": "Add index.js"
}
```

### Issue Service

| Método | Endpoint                                          | Descripción        |
| ------ | ------------------------------------------------- | ------------------ |
| GET    | `/api/repos/:owner/:repo/issues`                  | Listar issues      |
| POST   | `/api/repos/:owner/:repo/issues`                  | Crear issue        |
| GET    | `/api/repos/:owner/:repo/issues/:number`          | Obtener issue      |
| PATCH  | `/api/repos/:owner/:repo/issues/:number`          | Actualizar issue   |
| GET    | `/api/repos/:owner/:repo/issues/:number/comments` | Listar comentarios |
| POST   | `/api/repos/:owner/:repo/issues/:number/comments` | Crear comentario   |
| GET    | `/api/repos/:owner/:repo/labels`                  | Listar labels      |
| POST   | `/api/repos/:owner/:repo/labels`                  | Crear label        |

**Ejemplos:**

```bash
# Crear issue
POST /api/repos/johndoe/my-project/issues
{
  "title": "Bug: Login not working",
  "body": "When I try to login, I get an error...",
  "labels": ["bug", "high-priority"]
}
```

---

## Arquitectura

### Diagrama de Arquitectura General

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                   CLIENTE                                    │
│                            (React + TypeScript)                              │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │ HTTPS
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                               LOAD BALANCER                                  │
│                            (Nginx / Cloud LB)                                │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                                API GATEWAY                                   │
│                          (Kong / Nginx / AWS ALB)                            │
│  - Enrutamiento de peticiones                                                │
│  - Rate limiting                                                             │
│  - Autenticación JWT                                                         │
│  - Logging centralizado                                                      │
└───────────┬─────────────────┬─────────────────┬───────────────────────────────┘
            │                 │                 │
            ▼                 ▼                 ▼
┌───────────────────┐ ┌───────────────┐ ┌───────────────┐
│   AUTH SERVICE    │ │ REPO SERVICE  │ │ ISSUE SERVICE │
│                   │ │               │ │               │
│ - Registro        │ │ - CRUD repos  │ │ - CRUD issues │
│ - Login/Logout    │ │ - Permisos    │ │ - Comentarios │
│ - JWT tokens      │ │ - Branches    │ │ - Labels      │
│ - OIDC (Keycloak) │ │ - Archivos    │ │ - Asignados   │
│                   │ │               │ │               │
│ Puerto: 8081      │ │ Puerto: 8090  │ │ Puerto: 8084  │
└────────┬──────────┘ └───────┬───────┘ └───────┬───────┘
         │                    │                 │
         ▼                    ▼                 ▼
┌───────────────────┐ ┌───────────────┐ ┌───────────────┐
│    PostgreSQL     │ │  PostgreSQL   │ │  PostgreSQL   │
│   (users, auth)   │ │ (repos, files)│ │   (issues)    │
└───────────────────┘ └───────┬───────┘ └───────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   FILE STORAGE    │
                    │   (MinIO / S3)    │
                    │                   │
                    │ - Archivos repos  │
                    │ - Avatares        │
                    │ - Assets          │
                    └───────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                      INTERNAL SERVICE COMMUNICATION                          │
│                                  (gRPC)                                      │
│                                                                              │
│  Comunicación interna entre servicios:                                       │
│  - Operaciones internas con contratos tipados (Proto)                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Patrón de Arquitectura

| Patrón                   | Descripción                                      |
| ------------------------ | ------------------------------------------------ |
| **Microservicios**       | Cada funcionalidad es un servicio independiente  |
| **API Gateway**          | Punto único de entrada para todas las peticiones |
| **Database per Service** | Cada microservicio tiene su propia base de datos |
| **RPC Interno**          | Comunicación interna tipada con gRPC             |
| **CQRS**                 | Separación de lecturas y escrituras (búsqueda)   |

---

## Stack Tecnológico

### Backend

| Componente        | Tecnología                              | Justificación                                                    |
| ----------------- | --------------------------------------- | ---------------------------------------------------------------- |
| Lenguaje          | Java 25                                 | LTS moderno, records, sealed classes, rendimiento mejorado       |
| Framework         | Spring Boot 4.0.x (issues-ms + organizations-ms: 3.4.5) | Ecosistema maduro, integración nativa con Spring Security |
| Build             | Maven (mvnw wrapper)                    | Gestión de dependencias estándar en el ecosistema Java           |
| Definición de API | Smithy (generación de código)           | Contract-first; genera controllers y DTOs automáticamente        |
| Mapeo de objetos  | MapStruct + Lombok                      | Mapeos en tiempo de compilación, boilerplate reducido            |
| Seguridad         | Keycloak · OAuth2 Resource Server · JWT | SSO estándar, gestión centralizada de identidad                  |
| Documentación     | SpringDoc / Swagger UI                  | Generación automática desde anotaciones Spring MVC               |
| Observabilidad    | Spring Boot Actuator                    | Endpoints `/health`, `/info` y `/metrics` expuestos nativamente  |
| Contenedorización | Docker (eclipse-temurin JRE)            | Imagen base oficial para JVM en contenedores                     |

### Frontend

| Componente  | Tecnología  | Justificación                                          |
| ----------- | ----------- | ------------------------------------------------------ |
| Framework   | Next.js     | SSR/SSG, API Routes nativas, enrutamiento file-based   |
| Lenguaje    | TypeScript  | Tipado estático, menos errores en tiempo de desarrollo |
| Styling     | Tailwind CSS| Utility-first, rápido desarrollo                       |
| HTTP Client | Axios       | Solicitudes HTTP con interceptores y manejo de errores |

### Bases de Datos

| Servicio              | Base de Datos | Justificación                                                        |
| --------------------- | ------------- | -------------------------------------------------------------------- |
| Github-users-ms       | PostgreSQL    | Usuarios, cuentas OAuth y sesiones — datos relacionales ACID         |
| Github-files-ms       | PostgreSQL    | Metadatos de archivos, commits y repos — ACID, pool HikariCP         |
| Github-repository-ms  | MongoDB       | Documentos de repos, branches, colaboradores y estrellas — flexible  |
| Github-issues-ms      | PostgreSQL    | Issues, labels y comentarios (`githubx_issues`) — relaciones complejas ACID |
| Github-organizations-ms| PostgreSQL   | Organizaciones, miembros y equipos — SSL vía env vars para AWS RDS   |
| Github-pullrequests-ms| PostgreSQL    | PRs, revisiones y comentarios en línea — ACID                        |

### Infraestructura

| Componente        | Tecnología             | Justificación                                                 |
| ----------------- | ---------------------- | ------------------------------------------------------------- |
| Contenedores      | Docker                 | Estándar de la industria                                      |
| Orquestación Dev  | Docker Compose         | Simple para desarrollo y producción                           |
| API Gateway       | Kong / Nginx           | Rate limiting, routing                                        |
| Internal RPC      | gRPC                   | Baja latencia y contratos tipados entre servicios             |
| Object Storage    | MinIO / AWS S3         | Almacenamiento de archivos                                    |
| Doc. API          | Swagger UI (OpenAPI 3) | Contrato explícito y pruebas desde el navegador (`/api-docs`) |

### Cloud (elegir uno)

| Proveedor | Servicios a Usar                               |
| --------- | ---------------------------------------------- |
| **AWS**   | EKS, RDS, S3, ECR                 |
| **GCP**   | GKE, Cloud SQL, Cloud Storage     |
| **Azure** | AKS, Azure Database, Blob Storage |

---

## Estructura del Proyecto

El ecosistema está organizado como repositorios Git independientes. La estructura tipo de un microservicio Spring Boot es:

```
Github-<servicio>-ms/
├── pom.xml                        ← Dependencias Maven
├── mvnw / mvnw.cmd                ← Maven wrapper
├── Dockerfile                     ← Build multistage (Smithy + Maven → JRE)
├── .github/
│   └── workflows/                 ← CI/CD GitHub Actions
└── src/
    └── main/
        ├── java/com/githubx/<servicio>/
        │   ├── <Servicio>Application.java
        │   ├── config/            ← SecurityConfig, GrpcConfig, DataSourceConfig
        │   ├── controller/        ← REST controllers (generados por Smithy)
        │   ├── service/           ← Lógica de negocio
        │   ├── repository/        ← Spring Data JPA / MongoDB repositories
        │   ├── entity/            ← Entidades JPA / documentos Mongo
        │   ├── dto/               ← DTOs (generados por Smithy + MapStruct)
        │   ├── mapper/            ← MapStruct mappers
        │   └── grpc/              ← Implementaciones gRPC (XxxServiceImpl)
        ├── proto/                 ← Definiciones Protocol Buffers (.proto)
        └── resources/
            ├── application.yml    ← Configuración base
            ├── application-aws.yml← Perfil producción AWS
            └── schema.sql         ← DDL inicial (organizations-ms y pullrequests-ms)
```

**Repositorios del ecosistema:**

| Repositorio             | Stack / Notas                                                      |
| ----------------------- | ------------------------------------------------------------------ |
| `Github-users-ms`       | Spring Boot 4, Java 25, PostgreSQL, gRPC 9092                      |
| `Github-files-ms`       | Spring Boot 4, Java 25, PostgreSQL, gRPC 9093, perfil aws          |
| `Github-repository-ms`  | Spring Boot 4, Java 25, **MongoDB**, gRPC 9092, integra Git real   |
| `Github-issues-ms`      | Spring Boot **3.4.5**, Java **25**, PostgreSQL (`githubx_issues`), gRPC 9091 |
| `Github-organizations-ms`| Spring Boot **3.4.5**, Java **25**, PostgreSQL + SSL AWS RDS       |
| `Github-pullrequests-ms`| Spring Boot 4, Java 25, PostgreSQL, gRPC 9092                      |
| `Github-front`          | Next.js, TypeScript, Tailwind CSS                                  |
| `Github-Smithy`         | Contrato API (Smithy 2.0), genera OpenAPI + controllers            |
| `Github-Cdk`            | Infraestructura AWS (EKS, RDS, Keycloak) con AWS CDK               |

---

## Microservicios

### 1. Github-users-ms — Gestión de usuarios

**Puertos:** REST `8081` · gRPC `9092`  
**Base de datos:** PostgreSQL (`usuario_database`, schema `usuarios_nuevo`)  
**BD de identidad:** Keycloak (Admin API + Direct Access Grants)

**Responsabilidades:**

- CRUD de usuarios con criterios dinámicos (`SearchSpecification`)
- Gestión completa del ciclo de vida de Keycloak: roles, clientes, permisos
- Login / logout delegado a Keycloak
- Auditoría de transacciones (`TransactionUtil`)

**gRPC:**
- `UserPublicApi` — lectura pública sin autenticación (`GetUser`)
- `UserApi` — operaciones protegidas con JWT: `ListUsers`, `CreateUser`, `EditUser`, `DeleteUser`

**Particularidades:** interceptor gRPC con validación JWT (`GrpcJwtInterceptor`).

---

### 2. Github-files-ms — Gestión de archivos y contenido Git

**Puertos:** REST `8081` (local) / `8080` (contenedor) · gRPC `9093` · Context path: `/api`  
**Base de datos:** PostgreSQL (`github_files_db`) con pool HikariCP

**Responsabilidades:**

- CRUD de archivos y carpetas en repositorios
- Historial de commits y comparación de ramas
- Streaming de contenido de directorios

**Entidades:** `FileEntity`, `CommitEntity`, `CommitFileEntity`, `RepositoryEntity`

**gRPC:**
- `FilePublicApi` — lectura pública: repositorios, archivos, directorios
- `FileApi` — mutaciones protegidas: crear/actualizar/eliminar archivos y carpetas

**Particularidades:** descarga certificado SSL de AWS RDS en el Dockerfile. Soporta perfiles `aws` y `dev`. Tiene directorio `/infra`.

---

### 3. Github-repository-ms — Repositorios, ramas y colaboradores

**Puertos:** REST `8090` · gRPC `9092`  
**Base de datos:** MongoDB (`github_repository_ms`) — único servicio con MongoDB

**Responsabilidades:**

- CRUD de repositorios, forks, ramas (`branches`)
- Colaboradores con roles: `READ`, `WRITE`, `ADMIN`, `OWNER`
- Estrellas (social), comparación entre ramas
- Proxy Git HTTP y gestión de acceso SSH

**Documentos Mongo:** `RepositoryDocument`, `BranchDocument`, `CollaboratorDocument`, `FileEntryDocument`, `StarDocument`

**gRPC:**
- `RepoPublicService` — lectura pública: repositorios, forks, ramas
- `RepoService` — operaciones protegidas (15+ RPCs): crear, actualizar, eliminar, colaboradores, estrellas

**Particularidades:** integra con un servidor Git real (Gitea/Gogs) vía HTTP (`9080`) y SSH (`2222`). El Dockerfile hace build multistage Smithy + Maven. Tiene `docker-compose.yml` propio.

---

### 4. Github-issues-ms — Gestión de issues

**Puertos:** REST `8084` · gRPC `9091`  
**Java:** 25 · **Spring Boot:** 3.4.5  
**Base de datos:** PostgreSQL (`githubx_issues`)

**Responsabilidades:**

- CRUD de issues con filtros opcionales
- Gestión de comentarios (crear, actualizar, eliminar)
- Labels por repositorio

**gRPC:**
- `IssuePublicService` — lectura pública: issues, comentarios, labels
- `IssueService` — operaciones protegidas: crear/actualizar issues y comentarios, crear labels

---

### 5. Github-organizations-ms — Organizaciones y equipos

**Puertos:** REST `8085` · gRPC `9090`  
**Base de datos:** PostgreSQL con SSL vía variables de entorno (`sslmode=verify-full` + `global-bundle.pem` → AWS RDS)  
**Java:** 25 · **Spring Boot:** 3.4.5 (versión diferente a users/files/repo/pullrequests)

**Responsabilidades:**

- CRUD de organizaciones, miembros con roles (`OWNER`, `MEMBER`)
- Equipos (`Team`): miembros, repositorios con permisos (`READ`, `WRITE`, `ADMIN`)

**gRPC:**
- `OrgPublicService` — lectura pública
- `OrgService` — operaciones protegidas (16+ RPCs)

**Particularidades:** tiene `schema.sql` con DDL completo y `smithy-build.json` independiente. Servicio más maduro en configuración de producción (SSL, pool HikariCP bien configurado).

---

### 6. Github-pullrequests-ms — Pull Requests y revisiones

**Puertos:** REST `8082` (local) / `8080` (contenedor) · gRPC `9092` · Context path: `/api`  
**Base de datos:** PostgreSQL (`github_pullrequest_db`)

**Responsabilidades:**

- CRUD de pull requests y revisiones (`APPROVED`, `CHANGES_REQUESTED`, `COMMENTED`)
- Merge con estrategias: `MERGE`, `SQUASH`, `REBASE`
- Comentarios en línea con `file_path` y `line_number`
- Verificación de mergeabilidad y detección de conflictos

**Entidades:** `PullRequestEntity`, `PullRequestReviewEntity`, `PullRequestCommentEntity`, `RepositoryEntity`

**gRPC:**
- `PullRequestPublicService` — lectura pública + verificación de mergeabilidad
- `PullRequestService` — operaciones protegidas: crear, revisar, merge, comentar

**Particularidades:** tiene `schema.sql` con DDL propio. Servicio más completo en lógica de negocio Git.

---

## Diagramas

### Diagrama de Secuencia - Crear Repositorio

```
┌──────┐          ┌───────────┐          ┌─────────────┐          ┌──────────────┐          ┌────────┐
│Client│          │API Gateway│          │Auth Service │          │Repo Service  │          │PostgreSQL│
└──┬───┘          └─────┬─────┘          └──────┬──────┘          └──────┬───────┘          └───┬────┘
   │                    │                       │                        │                      │
   │ POST /api/repos    │                       │                        │                      │
   │ + JWT Token        │                       │                        │                      │
   │───────────────────>│                       │                        │                      │
   │                    │                       │                        │                      │
   │                    │ Validate JWT          │                        │                      │
   │                    │──────────────────────>│                        │                      │
   │                    │                       │                        │                      │
   │                    │ User Data             │                        │                      │
   │                    │<──────────────────────│                        │                      │
   │                    │                       │                        │                      │
   │                    │ Forward Request + User│                        │                      │
   │                    │───────────────────────────────────────────────>│                      │
   │                    │                       │                        │                      │
   │                    │                       │                        │ Insert Repository    │
   │                    │                       │                        │─────────────────────>│
   │                    │                       │                        │                      │
   │                    │                       │                        │ Success              │
   │                    │                       │                        │<─────────────────────│
   │                    │                       │                        │                      │
  │                    │                       │   gRPC call to Search  │                      │
  │                    │                       │   (IndexRepository)    │                      │
  │                    │                       │                        │─────────┐            │
  │                    │                       │                        │         │            │
  │                    │                       │                        │<────────┘            │
   │                    │                       │                        │                      │
   │                    │ Repository Created    │                        │                      │
   │                    │<───────────────────────────────────────────────│                      │
   │                    │                       │                        │                      │
   │ 201 Created        │                       │                        │                      │
   │<───────────────────│                       │                        │                      │
   │                    │                       │                        │                      │
```

---

## Instalación y Configuración

### Prerrequisitos

- Java 25
- Maven 3.9+ (o usar el wrapper `./mvnw`)
- Docker y Docker Compose
- Git
- (Frontend) Node.js 20+ y npm

### Desarrollo Local

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu-usuario/github.git
cd github
```

2. **Configurar variables de entorno**

```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

3. **Compilar y empaquetar un microservicio**

```bash
cd Github-<servicio>-ms
./mvnw clean package -DskipTests
```

4. **Levantar servicios con Docker Compose** (cuando aplica)

```bash
docker-compose up -d
```

5. **Verificar que todos los servicios están corriendo**

```bash
docker-compose ps
```

6. **Acceder a los servicios**

- Github-users-ms: http://localhost:8081
- Github-files-ms: http://localhost:8081/api
- Github-repository-ms: http://localhost:8090
- Github-issues-ms: http://localhost:8084
- Github-organizations-ms: http://localhost:8085
- Github-pullrequests-ms: http://localhost:8082/api
- Swagger UI (por servicio): http://localhost:{puerto}/swagger-ui.html
- Actuator health: http://localhost:{puerto}/actuator/health

### Variables de Entorno

Las variables se inyectan como propiedades de Spring Boot (o mediante variables de entorno del servicio cloud). Cada servicio tiene su `application.yml` con los valores por defecto para desarrollo local.

```env
# Keycloak (común a todos los servicios)
KEYCLOAK_BASE_URL=http://keycloak:8080
KEYCLOAK_REALM=github
KEYCLOAK_CLIENT_ID=github-backend
KEYCLOAK_CLIENT_SECRET=change-me

# Github-users-ms
USERS_DB_URL=jdbc:postgresql://postgres:5432/usuario_database
USERS_DB_USER=postgres
USERS_DB_PASSWORD=change-me
USERS_GRPC_PORT=9092

# Github-files-ms
FILES_DB_URL=jdbc:postgresql://postgres:5432/github_files_db
FILES_DB_USER=postgres
FILES_DB_PASSWORD=change-me
FILES_GRPC_PORT=9093

# Github-repository-ms
REPO_MONGO_URI=mongodb://mongo:27017/github_repository_ms
REPO_GRPC_PORT=9092
GIT_SERVER_HTTP=http://192.168.100.150:9080
GIT_SERVER_SSH=192.168.100.150:2222

# Github-issues-ms
ISSUES_DB_URL=jdbc:postgresql://postgres:5432/githubx_issues
ISSUES_DB_USER=postgres
ISSUES_DB_PASSWORD=change-me
ISSUES_SERVER_PORT=8084
ISSUES_GRPC_PORT=9091

# Github-organizations-ms
ORGS_DB_URL=jdbc:postgresql://rds-host:5432/orgs_db?sslmode=verify-full
ORGS_DB_USER=postgres
ORGS_DB_PASSWORD=change-me
ORGS_SERVER_PORT=8085
ORGS_GRPC_PORT=9090

# Github-pullrequests-ms
PR_DB_URL=jdbc:postgresql://postgres:5432/github_pullrequest_db
PR_DB_USER=postgres
PR_DB_PASSWORD=change-me
PR_GRPC_PORT=9092

# gRPC inter-servicio (addresses)
USERS_GRPC_ADDR=users-service:9092
FILES_GRPC_ADDR=files-service:9093
REPO_GRPC_ADDR=repo-service:9092
ISSUES_GRPC_ADDR=issues-service:9091
ORGS_GRPC_ADDR=orgs-service:9090
PR_GRPC_ADDR=pr-service:9092
```

---

## Despliegue

### Docker Compose (Staging)

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### CI/CD (Fuera del Alcance del Producto)

Para esta implementación de GitHub no se codificará un pipeline CI/CD como funcionalidad del sistema (L-01 en `Limites.md`). No hay workflows, runners ni ejecución de jobs en contenedores dentro del producto.

Cualquier automatización que use el equipo para su propio repositorio de código queda fuera del alcance funcional documentado aquí.

---

## Equipo

| Rol                     | Responsabilidades                |
| ----------------------- | -------------------------------- |
| **Backend Developer 1** | Auth Service, API Gateway        |
| **Backend Developer 2** | Repo Service, File Storage       |
| **Backend Developer 3** | Issue Service, Search Service    |
| **Frontend Developer**  | React App, integración con APIs  |
| **DevOps**              | Docker, CI/CD, Cloud |

> **Nota:** Los roles pueden solaparse según el tamaño del equipo

---

## Licencia

Este proyecto es para fines académicos.

---

## Contacto

- **Materia:** Arquitectura en la Nube y Microservicios
- **Universidad:** [Tu Universidad]
- **Periodo:** [Semestre/Año]
