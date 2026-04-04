## Mini GitHub - Requerimientos Funcionales

### RF01 — Gestión de Usuarios

| ID     | Requerimiento                                                                                                                    |
| ------ | -------------------------------------------------------------------------------------------------------------------------------- |
| RF01.1 | El sistema debe permitir el registro de usuarios con email y contraseña.                                                         |
| RF01.2 | El sistema debe permitir autenticación OIDC/SSO mediante Keycloak con federación de identidades (GitHub, Google, usuario local). |
| RF01.3 | El sistema debe permitir la edición del perfil de usuario.                                                                       |
| RF01.4 | El sistema debe permitir la recuperación de contraseña.                                                                          |

### RF02 — Gestión de Repositorios Git

| ID     | Requerimiento                                                    |
| ------ | ---------------------------------------------------------------- |
| RF02.1 | El sistema debe permitir crear repositorios públicos y privados. |
| RF02.2 | El sistema debe permitir eliminar repositorios propios.          |
| RF02.3 | El sistema debe permitir editar la información del repositorio.  |
| RF02.4 | El sistema debe mostrar la lista de repositorios del usuario.    |
| RF02.5 | El sistema debe gestionar branches de repositorios.              |
| RF02.6 | El sistema debe permitir hacer fork de repositorios públicos.    |

### RF03 — Gestión de Archivos

| ID     | Requerimiento                                                  |
| ------ | -------------------------------------------------------------- |
| RF03.1 | El sistema debe permitir subir archivos a un repositorio.      |
| RF03.2 | El sistema debe permitir descargar archivos de un repositorio. |
| RF03.3 | El sistema debe mostrar el contenido de archivos de texto.     |
| RF03.4 | El sistema debe permitir crear carpetas.                       |
| RF03.5 | El sistema debe permitir eliminar archivos.                    |

### RF04 — Gestión de Issues

| ID     | Requerimiento                                                                |
| ------ | ---------------------------------------------------------------------------- |
| RF04.1 | El sistema debe permitir crear issues en un repositorio con título y cuerpo. |
| RF04.2 | El sistema debe permitir asignar labels y usuarios a los issues.             |
| RF04.3 | El sistema debe permitir comentar en issues.                                 |
| RF04.4 | El sistema debe permitir cerrar y reabrir issues.                            |

### RF05 — Búsqueda

| ID     | Requerimiento                                            |
| ------ | -------------------------------------------------------- |
| RF05.1 | El sistema debe permitir buscar repositorios por nombre. |
| RF05.2 | El sistema debe permitir buscar usuarios.                |

### RF06 — Colaboración

| ID     | Requerimiento                                                                                           |
| ------ | ------------------------------------------------------------------------------------------------------- |
| RF06.1 | El sistema debe permitir dar "star" a repositorios.                                                     |
| RF06.2 | El sistema debe poder gestionar colaboradores de un repositorio con roles (Owner, Developer, Reporter). |

### RF07 — Pull Requests

| ID     | Requerimiento                                                                       |
| ------ | ----------------------------------------------------------------------------------- |
| RF07.1 | El usuario puede crear un Pull Request entre dos branches con título y descripción. |
| RF07.2 | Los reviewers pueden aprobar o solicitar cambios en un Pull Request.                |
| RF07.3 | El sistema detecta conflictos de merge y los reporta antes de ejecutar el merge.    |

---
