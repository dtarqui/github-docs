# Mini GitHub - Entidades Principales

## Descripción del Sistema

El sistema a desarrollar es una plataforma web tipo “Mini GitHub” que permitirá:

- Gestión de usuarios
- Creación de repositorios Git
- Control de acceso a repositorios
- Subida, descarga y visualización de archivos
- Colaboración mediante Issues y comentarios

El sistema será implementado con Git como motor externo.

---

# Alcance del Modelo de Datos

El modelo de datos se enfoca en:

- Representar la estructura lógica del sistema
- Almacenar metadata
- Soportar funcionalidades básicas de colaboración

---

# Entidades Principales

## Tabla de Entidades por Servicio

| Entidad          | Servicio      | Base de Datos |
| ---------------- | ------------- | ------------- |
| `users`          | Auth Service  | PostgreSQL    |
| `oauth_accounts` | Auth Service  | PostgreSQL    |
| `sessions`       | Auth Service  | PostgreSQL    |
| `repositories`   | Repo Service  | PostgreSQL    |
| `files`          | Repo Service  | PostgreSQL    |
| `stars`          | Repo Service  | PostgreSQL    |
| `issues`         | Issue Service | PostgreSQL    |
| `labels`         | Issue Service | PostgreSQL    |
| `issue_labels`   | Issue Service | PostgreSQL    |
| `comments`       | Issue Service | PostgreSQL    |

---

## User (Usuario)

Representa a los usuarios registrados en la plataforma.
**Servicio:** Auth Service | **Base de datos:** PostgreSQL (`auth_db`)

| Campo        | Tipo                                         |
| ------------ | -------------------------------------------- |
| Id           | UUID (PK)                                    |
| Username     | VARCHAR(50) UNIQUE NOT NULL                  |
| Email        | VARCHAR(255) UNIQUE NOT NULL                 |
| PasswordHash | VARCHAR(255) NOT NULL — bcrypt con salt      |
| avatar_url   | VARCHAR(500)                                 |
| bio          | TEXT                                         |
| location     | VARCHAR(100)                                 |
| website      | VARCHAR(255)                                 |
| CreatedAt    | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |
| updated_at   | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |

---

## OAuthAccount (Cuenta OAuth)

Vincula cuentas externas (GitHub, Google) a un usuario local.  
**Servicio:** Auth Service | **Base de datos:** PostgreSQL (`auth_db`)

| Campo               | Tipo                                         |
| ------------------- | -------------------------------------------- |
| id                  | UUID (PK)                                    |
| user_id             | UUID (FK → users) ON DELETE CASCADE          |
| provider            | VARCHAR(50) — 'github' \| 'google'           |
| provider_account_id | VARCHAR(255) NOT NULL                        |
| access_token        | TEXT                                         |
| refresh_token       | TEXT                                         |
| expires_at          | TIMESTAMP                                    |
| created_at          | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |

---

## Session (Sesión)

Gestiona los tokens JWT activos para control de sesiones.  
**Servicio:** Auth Service | **Base de datos:** PostgreSQL (`auth_db`)

| Campo      | Tipo                                         |
| ---------- | -------------------------------------------- |
| id         | UUID (PK)                                    |
| user_id    | UUID (FK → users) ON DELETE CASCADE          |
| token      | VARCHAR(500) UNIQUE NOT NULL                 |
| expires_at | TIMESTAMP NOT NULL                           |
| created_at | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |

---

## Repository (Repositorio)

Representa un repositorio Git creado por un usuario.  
**Servicio:** Repo Service | **Base de datos:** PostgreSQL (`repos_db`)

| Campo       | Tipo                                         |
| ----------- | -------------------------------------------- |
| Id          | UUID (PK)                                    |
| Name        | VARCHAR(150) NOT NULL                        |
| Description | TEXT                                         |
| IsPrivate   | BOOLEAN NOT NULL DEFAULT false               |
| OwnerId     | UUID (FK → users)                            |
| CreatedAt   | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |

---

## RepositoryPermission (Permisos)

Define los niveles de acceso de los usuarios a un repositorio.  
**Servicio:** Repo Service | **Base de datos:** PostgreSQL (`repos_db`)

| Campo        | Tipo                                         |
| ------------ | -------------------------------------------- |
| Id           | UUID (PK)                                    |
| UserId       | UUID (FK → users)                            |
| RepositoryId | UUID (FK → repositories)                     |
| Role         | VARCHAR(50) NOT NULL (Owner, Write, Read)    |

---

## Branch (Rama)

Representa las ramas dentro de un repositorio.  
**Servicio:** Repo Service | **Base de datos:** PostgreSQL (`repos_db`)

| Campo        | Tipo                                         |
| ------------ | -------------------------------------------- |
| Id           | UUID (PK)                                    |
| Name         | VARCHAR(100) NOT NULL                        |
| RepositoryId | UUID (FK → repositories)                     |
| IsDefault    | BOOLEAN NOT NULL DEFAULT false               |

---

## Commit

Representa los commits realizados en el repositorio.  
**Servicio:** Repo Service | **Base de datos:** PostgreSQL (`repos_db`)

| Campo        | Tipo                                         |
| ------------ | -------------------------------------------- |
| Id           | VARCHAR(100) (PK)                            |
| Message      | TEXT NOT NULL                                |
| AuthorId     | UUID (FK → users)                            |
| RepositoryId | UUID (FK → repositories)                   |
| BranchId     | UUID (FK → branches)                         |
| CreatedAt    | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |

---

## File (Archivo)

Representa los archivos versionados en un commit.  
**Servicio:** Repo Service | **Base de datos:** PostgreSQL (`repos_db`)

| Campo    | Tipo                                         |
| -------- | -------------------------------------------- |
| Id       | UUID (PK)                                    |
| Path     | VARCHAR(255) NOT NULL                        |
| Content  | TEXT                                         |
| CommitId | VARCHAR(100) (FK → commits)                  |

---

## PullRequest (Solicitud de Cambio)

Permite proponer cambios entre ramas.

| Campo          | Tipo                           |
| -------------- | ------------------------------ |
| Id             | UUID (PK)                      |
| RepositoryId   | UUID (FK → Repository)         |
| SourceBranchId | UUID                           |
| TargetBranchId | UUID                           |
| AuthorId       | UUID                           |
| Title          | VARCHAR                        |
| Description    | TEXT                           |
| Status         | VARCHAR (Open, Closed, Merged) |
| CreatedAt      | TIMESTAMP                      |

---

## Issue (Incidencia)

Permite registrar tareas, bugs o mejoras.
**Servicio:** Issue Service | **Base de datos:** PostgreSQL (`issues_db`)

| Campo       | Tipo                                                           |
| ----------- | -------------------------------------------------------------- |
| id          | UUID (PK)                                                      |
| repo_id     | UUID NOT NULL — identificador del repositorio (Issue Service; referencia lógica al repo) |
| number      | INTEGER NOT NULL — número secuencial por repo                  |
| title       | VARCHAR(255) NOT NULL                                          |
| body        | TEXT                                                           |
| state       | VARCHAR(20) NOT NULL DEFAULT 'open' — 'open' \| 'closed'       |
| author_id   | UUID NOT NULL — user_id de Auth Service                        |
| assignee_id | UUID — user_id de Auth Service (nullable)                      |
| created_at  | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                   |
| updated_at  | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                   |
| closed_at   | TIMESTAMP                                                      |

---

## Label (Etiqueta)

Etiquetas reutilizables dentro de un repositorio (bug, feature, etc.).  
**Servicio:** Issue Service | **Base de datos:** PostgreSQL (`issues_db`)

| Campo       | Tipo                         |
| ----------- | ---------------------------- |
| id          | UUID (PK)                    |
| repo_id     | UUID NOT NULL                |
| name        | VARCHAR(50) NOT NULL         |
| color       | CHAR(7) NOT NULL — "#ff0000" |
| description | VARCHAR(255)                 |

---

## IssueLabel (Relación Issue-Etiqueta N:M)

**Servicio:** Issue Service | **Base de datos:** PostgreSQL (`issues_db`)

| Campo    | Tipo                                 |
| -------- | ------------------------------------ |
| issue_id | UUID (FK → issues) ON DELETE CASCADE |
| label_id | UUID (FK → labels) ON DELETE CASCADE |

---

## Comment (Comentario)

Permite comentar en Issues y Pull Requests.

| Campo         | Tipo                                                   |
| ------------- | ------------------------------------------------------ |
| Id            | UUID (PK)                                              |
| body          | TEXT NOT NULL                                          |
| AuthorId      | UUID NOT NULL — user_id de Auth Service                |
| IssueId       | UUID (FK → issues) ON DELETE CASCADE                   |
| PullRequestId | UUID (FK → pull_requests) ON DELETE CASCADE (nullable) |
| CreatedAt     | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP           |
| updated_at    | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP           |

---

## Star (Estrella)

Registra que un usuario marcó un repositorio como favorito.  
**Servicio:** Repo Service | **Base de datos:** PostgreSQL (`repos_db`)

| Campo      | Tipo                                         |
| ---------- | -------------------------------------------- |
| id         | UUID (PK)                                    |
| repo_id    | UUID (FK → repositories)                     |
| user_id    | UUID NOT NULL — user_id de Auth Service      |
| created_at | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |

---

# Relaciones entre Entidades

```

User ──< Repository
User ──< RepositoryPermission >── Repository

Repository ──< Issue ──< Comment
Repository ──< PullRequest ──< Comment

User ──< OAuthAccount
User ──< Session

Repository ──< Star
Issue >──< Label (via IssueLabel)

```
