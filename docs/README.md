# GitHub

> Proyecto académico para la materia **Arquitectura en la Nube y Microservicios**

Recreación simplificada de GitHub utilizando arquitectura de microservicios, contenedorización y despliegue en la nube.

*Diseño técnico de Proyecto Github* Ingresar aquí ->  [Github Diseño Tecnico](https://github.com/dtarqui/github-docs/blob/main/docs/semana1/Github%20-%20Dise%C3%B1o%20T%C3%A9cnico.md) 

---

## Tabla de Contenidos

- [Descripción](#descripción)
- [Alcances y Límites](#alcances-y-límites)
- [Arquitectura](#arquitectura)
- [Requisitos Funcionales (RF)](#requisitos-funcionales-rf)
- [Requisitos No Funcionales (RNF)](#requisitos-no-funcionales-rnf)
- [Stack Tecnológico](#stack-tecnológico)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Microservicios](#microservicios)
- [Base de Datos](#base-de-datos)
- [API Endpoints](#api-endpoints)
- [Diagramas](#diagramas)
- [Instalación y Configuración](#instalación-y-configuración)
- [Despliegue](#despliegue)
- [Plan de Trabajo (4 Semanas)](#plan-de-trabajo-4-semanas)

---

## Descripción

**Mini-GitHub** es una plataforma simplificada de control de versiones y colaboración que permite a los usuarios:

- Crear y gestionar repositorios
- Subir y descargar archivos
- Gestionar issues y seguimiento de problemas
- Colaborar en proyectos

El objetivo principal es demostrar competencias en:

- Diseño de arquitectura de microservicios
- Contenedorización con Docker
- Orquestación con Kubernetes
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
| **Orquestación**      | Docker Compose (desarrollo) + Kubernetes (producción)                                                                       |
| **Bases de datos**    | Patrón database-per-service implementado                                                                                    |
| **Mensajería**        | Comunicación asíncrona entre servicios via RabbitMQ                                                                         |
| **Caché/Sesiones**    | Redis para caché y sesiones de aplicación                                                                                   |
| **API Gateway**       | Punto único de entrada con autenticación centralizada                                                                       |
| **Cloud**             | Despliegue funcional en al menos un proveedor cloud                                                                         |
| **CI/CD**             | Sin pipeline integrado en el producto (L-01 en Limites.md); despliegue manual o automatización externa al alcance funcional |

#### Entregables Comprometidos

| Entregable            | Descripción                                               |
| --------------------- | --------------------------------------------------------- |
| Código fuente         | Repositorio con todo el código del proyecto               |
| Documentación técnica | README, diagramas de arquitectura, especificación de APIs |
| Docker Compose        | Configuración para levantar todo el sistema localmente    |
| Manifiestos K8s       | Archivos YAML para despliegue en Kubernetes               |
| Demo funcional        | Aplicación desplegada y accesible en la nube              |
| Presentación          | Slides y demo en vivo del proyecto                        |

---

### Límites (Fuera del Proyecto)

#### Funcionalidades Excluidas

| Funcionalidad                          | Razón de Exclusión                                                  | Alternativa Implementada                                                   |
| -------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Servidor Git enterprise**            | Alta complejidad operativa (HA, replicación, hardening avanzado)    | Microservicio Git hosteado con soporte básico HTTPS                        |
| **Diff y merge de código**             | Algoritmos complejos de comparación de texto                        | Visualización de contenido sin comparación                                 |
| **Branch protection avanzada**         | Reglas complejas de protección y políticas obligatorias             | Gestión básica de branches y validaciones mínimas                          |
| **Code review avanzado**               | Comentarios en línea con sugerencias automáticas y flujos complejos | Comentarios en PR e issues (básico)                                        |
| **GitHub Actions / CI en el producto** | Workflows, runners y ejecución de jobs como parte del sistema       | No incluido (L-01); sin CI/CD dentro del alcance funcional del Mini-GitHub |
| **Wikis**                              | Feature secundaria                                                  | README del repositorio                                                     |
| **GitHub Pages**                       | Hosting de sitios estáticos                                         | No incluido                                                                |
| **Gists**                              | Snippets de código compartidos                                      | No incluido                                                                |
| **Organizaciones**                     | Gestión de equipos y permisos complejos                             | Solo usuarios individuales                                                 |
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
| **Caché**         | Redis single-node                 | Redis Cluster                     |
| **Búsqueda**      | Elasticsearch single-node         | Cluster con múltiples nodos       |
| **Storage**       | MinIO single-node                 | Distribución con erasure coding   |

---

### Comparativa: Mini-GitHub vs GitHub Real

| Característica       | GitHub Real       | Mini-GitHub     | Estado       |
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
| npm Registry    | Paquetes Node.js       | Alto - crítico para el build      |
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
| CD-02    | Búsqueda con Elasticsearch                             |
| CD-03    | Métricas y health checks expuestos                     |
| CD-04    | Tests automatizados (>50% coverage)                    |
| CD-05    | Logs centralizados                                     |
| CD-06    | Kubernetes con auto-scaling configurado                |

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
│                          (Kong / Express Gateway)                            │
│  - Enrutamiento de peticiones                                                │
│  - Rate limiting                                                             │
│  - Autenticación JWT                                                         │
│  - Logging centralizado                                                      │
└───────────┬─────────────────┬─────────────────┬─────────────────┬───────────┘
            │                 │                 │                 │
            ▼                 ▼                 ▼                 ▼
┌───────────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────────┐
│   AUTH SERVICE    │ │ REPO SERVICE  │ │ ISSUE SERVICE │ │  SEARCH SERVICE   │
│                   │ │               │ │               │ │                   │
│ - Registro        │ │ - CRUD repos  │ │ - CRUD issues │ │ - Elasticsearch   │
│ - Login/Logout    │ │ - Permisos    │ │ - Comentarios │ │ - Indexación      │
│ - JWT tokens      │ │ - Branches    │ │ - Labels      │ │ - Búsqueda repos  │
│ - OIDC (Keycloak) │ │ - Archivos    │ │ - Asignados   │ │ - Búsqueda código │
│                   │ │               │ │               │ │                   │
│ Puerto: 3001      │ │ Puerto: 3002  │ │ Puerto: 3003  │ │ Puerto: 3004      │
└────────┬──────────┘ └───────┬───────┘ └───────┬───────┘ └─────────┬─────────┘
         │                    │                 │                   │
         ▼                    ▼                 ▼                   ▼
┌───────────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────────┐
│    PostgreSQL     │ │  PostgreSQL   │ │  PostgreSQL   │ │  Elasticsearch    │
│   (users, auth)   │ │ (repos, files)│ │   (issues)    │ │    (índices)      │
└───────────────────┘ └───────┬───────┘ └───────────────┘ └───────────────────┘
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
│                           MESSAGE BROKER                                     │
│                         (RabbitMQ + Redis)                                   │
│                                                                              │
│  Comunicación asíncrona entre servicios:                                     │
│  - Eventos de creación de repos                                              │
│  - Indexación de búsqueda                                                    │
│  Redis se usa para caché/sesiones (no como broker principal de eventos).     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Patrón de Arquitectura

| Patrón                   | Descripción                                      |
| ------------------------ | ------------------------------------------------ |
| **Microservicios**       | Cada funcionalidad es un servicio independiente  |
| **API Gateway**          | Punto único de entrada para todas las peticiones |
| **Database per Service** | Cada microservicio tiene su propia base de datos |
| **Event-Driven**         | Comunicación asíncrona mediante eventos          |
| **CQRS**                 | Separación de lecturas y escrituras (búsqueda)   |

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
| RNF06 | El sistema debe poder desplegarse en Kubernetes           | Manifiestos K8s completos    |

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
| RNF24 | Infraestructura como código (Terraform/Kubernetes)     | 100% IaC versionado                |
| RNF25 | Despliegues automatizados con rollback (infraestructura del equipo, no feature del producto) | Pipeline de despliegue funcional |
| RNF26 | Ambientes de staging y producción separados            | 2 ambientes mínimo                 |

---

## Stack Tecnológico

### Backend

| Componente    | Tecnología            | Justificación                                           |
| ------------- | --------------------- | ------------------------------------------------------- |
| Lenguaje      | Node.js (TypeScript)  | Ecosistema maduro, async nativo                         |
| Framework     | Express.js / Fastify  | Ligero, flexible, gran comunidad                        |
| ORM SQL       | Prisma                | Type-safe, migraciones automáticas (Auth, Repo, Issues) |
| Validación    | Zod / Joi             | Validación de schemas                                   |
| Autenticación | Keycloak (OIDC) + JWT | SSO estandar, gestion centralizada de identidad         |

### Frontend

| Componente       | Tecnología              | Justificación                    |
| ---------------- | ----------------------- | -------------------------------- |
| Framework        | React 18                | Componentes, hooks, ecosistema   |
| Lenguaje         | TypeScript              | Tipado estático, menos errores   |
| State Management | Zustand / Redux Toolkit | Simple y escalable               |
| Styling          | Tailwind CSS            | Utility-first, rápido desarrollo |
| HTTP Client      | Axios / TanStack Query  | Caché, reintentos, estados       |
| Routing          | React Router v6         | Estándar de la industria         |

### Bases de Datos

| Servicio       | Base de Datos | Justificación                                  |
| -------------- | ------------- | ---------------------------------------------- |
| Auth Service   | PostgreSQL    | Datos relacionales, ACID                       |
| Repo Service   | PostgreSQL    | Metadatos y relaciones ACID; blobs en MinIO/S3 |
| Issue Service  | PostgreSQL    | Relaciones complejas                           |
| Search Service | Elasticsearch | Full-text search optimizado                    |
| Caché          | Redis         | Sesiones, caché, pub/sub                       |

### Infraestructura

| Componente        | Tecnología             | Justificación                                                 |
| ----------------- | ---------------------- | ------------------------------------------------------------- |
| Contenedores      | Docker                 | Estándar de la industria                                      |
| Orquestación Dev  | Docker Compose         | Simple para desarrollo                                        |
| Orquestación Prod | Kubernetes             | Escalabilidad, auto-healing                                   |
| API Gateway       | Kong / Nginx           | Rate limiting, routing                                        |
| Message Broker    | RabbitMQ               | Mensajería confiable                                          |
| Object Storage    | MinIO / AWS S3         | Almacenamiento de archivos                                    |
| Doc. API          | Swagger UI (OpenAPI 3) | Contrato explícito y pruebas desde el navegador (`/api-docs`) |

### Cloud (elegir uno)

| Proveedor | Servicios a Usar                               |
| --------- | ---------------------------------------------- |
| **AWS**   | EKS, RDS, S3, ElastiCache, ECR                 |
| **GCP**   | GKE, Cloud SQL, Cloud Storage, Memorystore     |
| **Azure** | AKS, Azure Database, Blob Storage, Azure Cache |

---

## Estructura del Proyecto

```
mini-github/
├── README.md
├── docker-compose.yml
├── docker-compose.prod.yml
├── .env.example
├── .gitignore
│
├── docs/
│   ├── architecture.md
│   ├── api-specification.md
│   ├── database-schemas.md
│   └── deployment-guide.md
│
├── infrastructure/
│   ├── kubernetes/
│   │   ├── namespace.yaml
│   │   ├── configmaps/
│   │   │   └── app-config.yaml
│   │   ├── secrets/
│   │   │   └── app-secrets.yaml
│   │   ├── deployments/
│   │   │   ├── api-gateway.yaml
│   │   │   ├── auth-service.yaml
│   │   │   ├── repo-service.yaml
│   │   │   ├── issue-service.yaml
│   │   │   └── search-service.yaml
│   │   ├── services/
│   │   │   ├── api-gateway-svc.yaml
│   │   │   ├── auth-service-svc.yaml
│   │   │   ├── repo-service-svc.yaml
│   │   │   ├── issue-service-svc.yaml
│   │   │   └── search-service-svc.yaml
│   │   └── ingress/
│   │       └── ingress.yaml
│   │
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── modules/
│           ├── eks/
│           ├── rds/
│           └── s3/
│
├── services/
│   │
│   ├── api-gateway/
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── src/
│   │       ├── index.ts
│   │       ├── config/
│   │       │   └── gateway.config.ts
│   │       ├── middleware/
│   │       │   ├── auth.middleware.ts
│   │       │   ├── rateLimit.middleware.ts
│   │       │   └── logging.middleware.ts
│   │       └── routes/
│   │           └── proxy.routes.ts
│   │
│   ├── auth-service/
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── prisma/
│   │   │   ├── schema.prisma
│   │   │   └── migrations/
│   │   └── src/
│   │       ├── index.ts
│   │       ├── config/
│   │       │   └── database.ts
│   │       ├── controllers/
│   │       │   └── auth.controller.ts
│   │       ├── services/
│   │       │   └── auth.service.ts
│   │       ├── repositories/
│   │       │   └── user.repository.ts
│   │       ├── middleware/
│   │       │   └── validate.middleware.ts
│   │       ├── routes/
│   │       │   └── auth.routes.ts
│   │       ├── schemas/
│   │       │   └── auth.schema.ts
│   │       ├── utils/
│   │       │   ├── jwt.utils.ts
│   │       │   └── password.utils.ts
│   │       └── types/
│   │           └── auth.types.ts
│   │
│   ├── repo-service/
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── src/
│   │       ├── index.ts
│   │       ├── config/
│   │       │   ├── database.ts
│   │       │   └── storage.ts
│   │       ├── controllers/
│   │       │   ├── repo.controller.ts
│   │       │   └── file.controller.ts
│   │       ├── services/
│   │       │   ├── repo.service.ts
│   │       │   └── file.service.ts
│   │       ├── repositories/
│   │       │   └── repo.repository.ts
│   │       ├── routes/
│   │       │   ├── repo.routes.ts
│   │       │   └── file.routes.ts
│   │       ├── models/
│   │       │   ├── repo.model.ts
│   │       │   └── file.model.ts
│   │       └── types/
│   │           └── repo.types.ts
│   │
│   ├── issue-service/
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   ├── prisma/
│   │   │   ├── schema.prisma
│   │   │   └── migrations/
│   │   └── src/
│   │       ├── index.ts
│   │       ├── config/
│   │       │   └── database.ts
│   │       ├── controllers/
│   │       │   ├── issue.controller.ts
│   │       │   └── comment.controller.ts
│   │       ├── services/
│   │       │   ├── issue.service.ts
│   │       │   └── comment.service.ts
│   │       ├── repositories/
│   │       │   ├── issue.repository.ts
│   │       │   └── comment.repository.ts
│   │       ├── routes/
│   │       │   └── issue.routes.ts
│   │       └── types/
│   │           └── issue.types.ts
│   │
│   └── search-service/
│       ├── Dockerfile
│       ├── package.json
│       ├── tsconfig.json
│       └── src/
│           ├── index.ts
│           ├── config/
│           │   └── elasticsearch.ts
│           ├── controllers/
│           │   └── search.controller.ts
│           ├── services/
│           │   └── search.service.ts
│           ├── routes/
│           │   └── search.routes.ts
│           └── consumers/
│               └── indexer.consumer.ts
│
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── index.html
│   └── src/
│       ├── main.tsx
│       ├── App.tsx
│       ├── vite-env.d.ts
│       ├── assets/
│       │   └── logo.svg
│       ├── components/
│       │   ├── common/
│       │   │   ├── Button.tsx
│       │   │   ├── Input.tsx
│       │   │   ├── Modal.tsx
│       │   │   └── Navbar.tsx
│       │   ├── auth/
│       │   │   ├── LoginForm.tsx
│       │   │   └── RegisterForm.tsx
│       │   ├── repo/
│       │   │   ├── RepoCard.tsx
│       │   │   ├── RepoList.tsx
│       │   │   ├── FileExplorer.tsx
│       │   │   └── FileViewer.tsx
│       │   └── issue/
│       │       ├── IssueCard.tsx
│       │       ├── IssueList.tsx
│       │       └── IssueForm.tsx
│       ├── pages/
│       │   ├── Home.tsx
│       │   ├── Login.tsx
│       │   ├── Register.tsx
│       │   ├── Dashboard.tsx
│       │   ├── RepoView.tsx
│       │   ├── RepoCreate.tsx
│       │   ├── IssueView.tsx
│       │   └── Profile.tsx
│       ├── hooks/
│       │   ├── useAuth.ts
│       │   ├── useRepos.ts
│       │   └── useIssues.ts
│       ├── services/
│       │   ├── api.ts
│       │   ├── auth.service.ts
│       │   ├── repo.service.ts
│       │   └── issue.service.ts
│       ├── store/
│       │   ├── index.ts
│       │   ├── authSlice.ts
│       │   └── repoSlice.ts
│       ├── types/
│       │   ├── auth.types.ts
│       │   ├── repo.types.ts
│       │   └── issue.types.ts
│       └── utils/
│           ├── constants.ts
│           └── helpers.ts
│
├── shared/
│   └── types/
│       ├── api.types.ts
│       └── events.types.ts
│
└── .github/
    └── workflows/
        ├── ci.yml
        ├── cd-staging.yml
        └── cd-production.yml
```

---

## Microservicios

### 1. API Gateway (Puerto 3000)

**Responsabilidades:**

- Punto único de entrada
- Enrutamiento de peticiones
- Autenticación/Autorización
- Rate limiting
- Logging centralizado
- CORS handling

**Tecnologías:** Express.js, http-proxy-middleware

### 2. Auth Service (Puerto 3001)

**Responsabilidades:**

- Registro de usuarios
- Login/Logout
- Generación y validación de JWT
- Integración OIDC/SSO con Keycloak
- Gestión de sesiones

**Base de datos:** PostgreSQL

**Eventos que emite:**

- `user.created`
- `user.updated`
- `user.deleted`

### 3. Repo Service (Puerto 3002)

**Responsabilidades:**

- CRUD de repositorios
- Gestión de archivos
- Control de permisos
- Gestión de branches (básico)
- Forks

**Base de datos:** PostgreSQL (`repos_db`) + MinIO (archivos)

**Eventos que emite:**

- `repo.created`
- `repo.updated`
- `repo.deleted`
- `file.uploaded`

### 4. Issue Service (Puerto 3003)

**Responsabilidades:**

- CRUD de issues
- Gestión de comentarios
- Labels y milestones
- Asignación de usuarios

**Base de datos:** PostgreSQL

**Eventos que emite:**

- `issue.created`
- `issue.updated`
- `issue.closed`
- `comment.created`

### 5. Search Service (Puerto 3004)

**Responsabilidades:**

- Indexación de repositorios
- Búsqueda full-text
- Filtrado y ordenamiento
- Sugerencias

**Base de datos:** Elasticsearch

**Eventos que consume:**

- `repo.created`
- `repo.updated`
- `repo.deleted`

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

### Search Service

| Método | Endpoint                      | Descripción         |
| ------ | ----------------------------- | ------------------- |
| GET    | `/api/search/repositories?q=` | Buscar repositorios |
| GET    | `/api/search/users?q=`        | Buscar usuarios     |
| GET    | `/api/search/issues?q=`       | Buscar issues       |

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
   │                    │                       │      Emit: repo.created│                      │
   │                    │                       │        (to RabbitMQ)   │                      │
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

### Diagrama de Despliegue - Kubernetes

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                    KUBERNETES CLUSTER                                    │
│                                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────────────────┐    │
│  │                              INGRESS CONTROLLER                                  │    │
│  │                                 (nginx-ingress)                                  │    │
│  └───────────────────────────────────────┬─────────────────────────────────────────┘    │
│                                          │                                               │
│  ┌───────────────────────────────────────┴─────────────────────────────────────────┐    │
│  │                               NAMESPACE: mini-github                             │    │
│  │                                                                                  │    │
│  │   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐             │    │
│  │   │   API Gateway   │    │   API Gateway   │    │   API Gateway   │             │    │
│  │   │   (Pod 1)       │    │   (Pod 2)       │    │   (Pod 3)       │             │    │
│  │   └────────┬────────┘    └────────┬────────┘    └────────┬────────┘             │    │
│  │            │                      │                      │                       │    │
│  │            └──────────────────────┼──────────────────────┘                       │    │
│  │                                   │                                              │    │
│  │                    ┌──────────────┴──────────────┐                               │    │
│  │                    │      Service: api-gateway   │                               │    │
│  │                    │      (ClusterIP)            │                               │    │
│  │                    └──────────────┬──────────────┘                               │    │
│  │                                   │                                              │    │
│  │   ┌───────────────────────────────┼───────────────────────────────┐              │    │
│  │   │                               │                               │              │    │
│  │   ▼                               ▼                               ▼              │    │
│  │ ┌─────────────┐             ┌─────────────┐             ┌─────────────┐          │    │
│  │ │Auth Service │             │Repo Service │             │Issue Service│          │    │
│  │ │ Deployment  │             │ Deployment  │             │ Deployment  │          │    │
│  │ │ replicas: 2 │             │ replicas: 3 │             │ replicas: 2 │          │    │
│  │ └──────┬──────┘             └──────┬──────┘             └──────┬──────┘          │    │
│  │        │                           │                           │                 │    │
│  │        ▼                           ▼                           ▼                 │    │
│  │ ┌─────────────┐             ┌─────────────┐             ┌─────────────┐          │    │
│  │ │  Service    │             │  Service    │             │  Service    │          │    │
│  │ │ ClusterIP   │             │ ClusterIP   │             │ ClusterIP   │          │    │
│  │ └─────────────┘             └─────────────┘             └─────────────┘          │    │
│  │                                                                                  │    │
│  └──────────────────────────────────────────────────────────────────────────────────┘    │
│                                                                                          │
│  ┌──────────────────────────────────────────────────────────────────────────────────┐   │
│  │                              NAMESPACE: databases                                 │   │
│  │                                                                                   │   │
│  │   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐                │   │
│  │   │   PostgreSQL    │   │   PostgreSQL    │   │  Elasticsearch  │                │   │
│  │   │ (auth / issues) │   │    (repos_db)   │   │   (índices)     │                │   │
│  │   │   StatefulSet   │   │   StatefulSet   │   │   StatefulSet   │                │   │
│  │   └────────┬────────┘   └────────┬────────┘   └────────┬────────┘                │   │
│  │            │                     │                     │                          │   │
│  │            ▼                     ▼                     ▼                          │   │
│  │   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐                │   │
│  │   │  PVC: 10Gi      │   │  PVC: 20Gi      │   │  PVC: 10Gi      │                │   │
│  │   │  (SSD)          │   │  (SSD)          │   │  (SSD)          │                │   │
│  │   └─────────────────┘   └─────────────────┘   └─────────────────┘                │   │
│  │                                                                                   │   │
│  └───────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                          │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Instalación y Configuración

### Prerrequisitos

- Node.js 18+
- Docker y Docker Compose
- Git
- (Opcional) kubectl y acceso a cluster Kubernetes

### Desarrollo Local

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu-usuario/mini-github.git
cd mini-github
```

2. **Configurar variables de entorno**

```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

3. **Levantar servicios con Docker Compose**

```bash
docker-compose up -d
```

4. **Verificar que todos los servicios están corriendo**

```bash
docker-compose ps
```

5. **Acceder a la aplicación**

- Frontend: http://localhost:3000
- API Gateway: http://localhost:8080
- RabbitMQ Management: http://localhost:15672
- MinIO Console: http://localhost:9001

### Variables de Entorno

```env
# General
NODE_ENV=development
LOG_LEVEL=debug

# API Gateway
API_GATEWAY_PORT=8080
JWT_SECRET=your-super-secret-jwt-key

# Keycloak (SSO/OIDC)
KEYCLOAK_BASE_URL=http://keycloak:8080
KEYCLOAK_REALM=mini-github
KEYCLOAK_CLIENT_ID=mini-github-web
KEYCLOAK_CLIENT_SECRET=change-me

# Auth Service
AUTH_SERVICE_PORT=3001
AUTH_DATABASE_URL=postgresql://user:pass@postgres:5432/auth_db

# Repo Service
REPO_SERVICE_PORT=3002
REPO_DATABASE_URL=postgresql://user:pass@postgres:5432/repos_db
MINIO_ENDPOINT=minio
MINIO_PORT=9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin

# Issue Service
ISSUE_SERVICE_PORT=3003
ISSUE_DATABASE_URL=postgresql://user:pass@postgres:5432/issues_db

# Search Service
SEARCH_SERVICE_PORT=3004
ELASTICSEARCH_URL=http://elasticsearch:9200

# RabbitMQ
RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672

# Redis
REDIS_URL=redis://redis:6379
```

---

## Despliegue

### Docker Compose (Staging)

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Kubernetes

1. **Crear namespace**

```bash
kubectl apply -f infrastructure/kubernetes/namespace.yaml
```

2. **Aplicar ConfigMaps y Secrets**

```bash
kubectl apply -f infrastructure/kubernetes/configmaps/
kubectl apply -f infrastructure/kubernetes/secrets/
```

3. **Desplegar servicios**

```bash
kubectl apply -f infrastructure/kubernetes/deployments/
kubectl apply -f infrastructure/kubernetes/services/
```

4. **Configurar Ingress**

```bash
kubectl apply -f infrastructure/kubernetes/ingress/
```

### CI/CD (Fuera del Alcance del Producto)

Para esta implementación de Mini-GitHub no se codificará un pipeline CI/CD como funcionalidad del sistema (L-01 en `Limites.md`). No hay workflows, runners ni ejecución de jobs en contenedores dentro del producto.

Cualquier automatización que use el equipo para su propio repositorio de código queda fuera del alcance funcional documentado aquí.

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

### Semana 3: Issues y Búsqueda

| Día | Tareas                           |
| --- | -------------------------------- |
| 1-2 | Issue Service: CRUD de issues    |
| 3   | Comentarios en issues            |
| 4-5 | Search Service con Elasticsearch |
| 6-7 | Frontend: issues, búsqueda       |

**Entregables:**

- [ ] Sistema de issues completo
- [ ] Búsqueda funcionando
- [ ] UI de issues y búsqueda

### Semana 4: Cloud, Despliegue y Documentación

| Día | Tareas                                                                             |
| --- | ---------------------------------------------------------------------------------- |
| 1-2 | Manifiestos Kubernetes                                                             |
| 3-4 | Preparación de despliegue y validación operativa (sin pipeline CI/CD del producto) |
| 5   | Despliegue en cloud (AWS/GCP/Azure)                                                |
| 6-7 | Testing, documentación, presentación                                               |

**Entregables:**

- [ ] Aplicación desplegada en cloud
- [ ] Despliegue validado (sin pipeline CI/CD del producto)
- [ ] Documentación completa
- [ ] Demo funcional

---

## Equipo

| Rol                     | Responsabilidades                |
| ----------------------- | -------------------------------- |
| **Backend Developer 1** | Auth Service, API Gateway        |
| **Backend Developer 2** | Repo Service, File Storage       |
| **Backend Developer 3** | Issue Service, Search Service    |
| **Frontend Developer**  | React App, integración con APIs  |
| **DevOps**              | Docker, Kubernetes, CI/CD, Cloud |

> **Nota:** Los roles pueden solaparse según el tamaño del equipo

---

## Licencia

Este proyecto es para fines académicos.

---

## Contacto

- **Materia:** Arquitectura en la Nube y Microservicios
- **Universidad:** [Tu Universidad]
- **Periodo:** [Semestre/Año]
