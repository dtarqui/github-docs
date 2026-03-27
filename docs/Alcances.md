# MINI-GITHUB — Documento de Alcances
> Arquitectura en la Nube y Microservicios

Este documento define los alcances, límites y requerimientos del proyecto Mini-GitHub, una plataforma simplificada de control de versiones basada en arquitectura de microservicios.

---

## Tabla de Contenidos

- [1. Alcances](#1-alcances)
- [2. Límites](#2-límites)
- [3. Requerimientos Funcionales](#3-requerimientos-funcionales)
- [4. Requerimientos No Funcionales](#4-requerimientos-no-funcionales)

---

## 1. Alcances

El proyecto incluye las siguientes funcionalidades:

- **Autenticación:** Registro, login con email/contraseña, JWT y recuperación de contraseña.
- **Gestión de usuarios y equipos:** Roles básicos (Owner, Developer, Reporter) para control de acceso a repositorios.
- **Repositorios Git:** Crear, clonar, push/pull via HTTPS, navegación de archivos y visualización de commits.
- **Branches y merge:** Gestión básica de ramas con detección de conflictos antes de ejecutar el merge.
- **Pull Requests:** Crear PRs entre branches, revisión con comentarios, aprobación y merge.
- **Notificaciones por email:** Alertas en eventos clave como PRs creados, revisiones, merge completados e invitaciones a colaboradores.
- **API REST documentada:** Endpoints documentados con Swagger UI.

---

## 2. Límites

Las siguientes funcionalidades quedan **fuera del alcance** del proyecto:

| ID | Funcionalidad | Justificación |
|----|---------------|---------------|
| L-01 | CI/CD y pipelines | No se implementarán workflows automáticos, runners ni ejecución de jobs en contenedores. Requeriría un proyecto separado por su complejidad. |
| L-02 | Acceso SSH y claves públicas | Solo se soportará clonación y push via HTTPS con usuario/contraseña o token personal. |
| L-03 | Organizaciones y equipos avanzados | No existirá el concepto de organización. Solo repositorios personales con colaboradores individuales. |
| L-04 | Registro de paquetes | No se publicarán ni consumirán paquetes npm, Maven, Docker o PyPI desde la plataforma. |
| L-05 | Git LFS y archivos grandes | Tamaño máximo de repositorio: 100 MB. No se implementará Git Large File Storage. |
| L-06 | Notificaciones en tiempo real | Sin WebSockets ni push notifications. Las actualizaciones se verán al recargar la página. Solo notificaciones por email. |
| L-07 | Búsqueda de código | No habrá indexación ni búsqueda dentro del contenido de archivos. Solo búsqueda por nombre de repositorio. |
| L-08 | Aplicación móvil nativa | Se implementará como PWA (Progressive Web App) en lugar de app nativa. |

---

## 3. Requerimientos Funcionales

### RF01 — Gestión de Usuarios

| ID | Requerimiento |
|----|---------------|
| RF01.1 | El sistema debe permitir el registro de usuarios con email y contraseña. |
| RF01.2 | El sistema debe permitir autenticación mediante OAuth (GitHub/Google). |
| RF01.3 | El sistema debe permitir la edición del perfil de usuario. |
| RF01.4 | El sistema debe permitir la recuperación de contraseña. |

### RF02 — Gestión de Repositorios Git

| ID | Requerimiento |
|----|---------------|
| RF02.1 | El sistema debe permitir crear repositorios públicos y privados. |
| RF02.2 | El sistema debe permitir eliminar repositorios propios. |
| RF02.3 | El sistema debe permitir editar la información del repositorio. |
| RF02.4 | El sistema debe mostrar la lista de repositorios del usuario. |
| RF02.5 | El sistema debe gestionar branches de repositorios. |

### RF03 — Gestión de Archivos

| ID | Requerimiento |
|----|---------------|
| RF03.1 | El sistema debe permitir subir archivos a un repositorio. |
| RF03.2 | El sistema debe permitir descargar archivos de un repositorio. |
| RF03.3 | El sistema debe mostrar el contenido de archivos de texto. |
| RF03.4 | El sistema debe permitir crear carpetas. |
| RF03.5 | El sistema debe permitir eliminar archivos. |

### RF04 — Pull Requests

| ID | Requerimiento |
|----|---------------|
| RF04.1 | El usuario puede crear un Pull Request entre dos branches con título y descripción. El PR incluye lista de commits y diff completo de los cambios. |
| RF04.2 | Los reviewers pueden aprobar o solicitar cambios en un PR. |
| RF04.3 | El sistema detecta conflictos de merge y los reporta antes de ejecutar el merge. Si hay conflictos, el merge queda bloqueado. |

### RF05 — Búsqueda

| ID | Requerimiento |
|----|---------------|
| RF05.1 | El sistema debe permitir buscar repositorios por nombre. |
| RF05.2 | El sistema debe permitir buscar usuarios. |

### RF06 — Colaboración

| ID | Requerimiento |
|----|---------------|
| RF06.1 | El sistema debe permitir dar "star" a repositorios. |
| RF06.2 | El sistema debe poder gestionar equipos con roles. |
| RF06.3 | El sistema debe mostrar el autor de cada commit. |

---

## 4. Requerimientos No Funcionales

### Arquitectura y Diseño

| ID | Requerimiento |
|----|---------------|
| RNF01 | El sistema debe implementar arquitectura de microservicios. |
| RNF02 | Cada microservicio debe tener su propia base de datos. |
| RNF03 | Los servicios deben comunicarse mediante API REST y/o mensajería. |

### Contenedorización y Orquestación

| ID | Requerimiento |
|----|---------------|
| RNF04 | Todos los servicios deben estar contenedorizados. |
| RNF05 | El sistema debe usar Docker Compose para desarrollo local. |
| RNF06 | El sistema debe poder desplegarse en Kubernetes. |

### Cloud y Despliegue

| ID | Requerimiento |
|----|---------------|
| RNF07 | El sistema debe desplegarse en un proveedor cloud. |
| RNF08 | Debe existir un pipeline CI/CD para el despliegue del proyecto. |
| RNF09 | El sistema debe tener configuración por variables de entorno. |

### Rendimiento y Escalabilidad

| ID | Requerimiento |
|----|---------------|
| RNF10 | El API Gateway debe responder en menos de 100ms. |
| RNF11 | Los servicios deben poder escalar horizontalmente. |
| RNF12 | El sistema debe soportar al menos 100 usuarios concurrentes. |

### Seguridad

| ID | Requerimiento |
|----|---------------|
| RNF13 | Todas las comunicaciones externas deben usar HTTPS (TLS 1.3). |
| RNF14 | La autenticación debe usar JWT con expiración. |
| RNF15 | Las contraseñas deben almacenarse hasheadas. |
| RNF16 | Tokens de acceso con scopes y RBAC por repositorio. |
| RNF17 | Cifrado en reposo (AES-256) y en tránsito. |
| RNF18 | Aislamiento total entre repositorios privados. |

### Usabilidad

| ID | Requerimiento |
|----|---------------|
| RNF19 | Diseño responsivo y accesible. |
| RNF20 | Interfaz funcional en navegadores web modernos. |

### Observabilidad y Mantenibilidad

| ID | Requerimiento |
|----|---------------|
| RNF21 | El sistema debe tener logging centralizado y estructurado. |
| RNF22 | El sistema debe exponer métricas de salud (health checks). |
| RNF23 | Monitoreo con Prometheus/Grafana. |
| RNF24 | Infraestructura como código (Terraform/Kubernetes). |
| RNF25 | Despliegues automatizados con rollback. |
| RNF26 | Ambientes de staging y producción separados. |

---

*Fin del documento*
