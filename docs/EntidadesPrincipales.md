# Mini GitHub - Entidades Principales y Modelo de Datos

## Descripción del Sistema

El sistema a desarrollar es una plataforma web tipo “Mini GitHub” que permitirá:

- Gestión de usuarios
- Creación de repositorios Git
- Control de acceso a repositorios
- Manejo básico de ramas y commits
- Visualización de archivos
- Colaboración mediante Issues y Pull Requests

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

| Entidad | Servicio | Base de Datos |
|---|---|---|
| `users` | Auth Service | PostgreSQL |
| `oauth_accounts` | Auth Service | PostgreSQL |
| `sessions` | Auth Service | PostgreSQL |
| `repositories` | Repo Service | MongoDB |
| `files` | Repo Service | MongoDB |
| `stars` | Repo Service | MongoDB |
| `issues` | Issue Service | PostgreSQL |
| `labels` | Issue Service | PostgreSQL |
| `issue_labels` | Issue Service | PostgreSQL |
| `comments` | Issue Service | PostgreSQL |

---

## User (Usuario)

Representa a los usuarios registrados en la plataforma.
**Servicio:** Auth Service | **Base de datos:** PostgreSQL (`auth_db`)

| Campo | Tipo |
|------|------|
| Id | UUID (PK) |
| Username | VARCHAR(50) UNIQUE NOT NULL |
| Email | VARCHAR(255) UNIQUE NOT NULL |
| PasswordHash | VARCHAR(255) NOT NULL — bcrypt con salt |
| avatar_url | VARCHAR(500) |
| bio | TEXT |
| location | VARCHAR(100) |
| website | VARCHAR(255) |
| CreatedAt | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |
| updated_at | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |

---

## OAuthAccount (Cuenta OAuth)

Vincula cuentas externas (GitHub, Google) a un usuario local.  
**Servicio:** Auth Service | **Base de datos:** PostgreSQL (`auth_db`)

| Campo | Tipo |
|------|------|
| id | UUID (PK) |
| user_id | UUID (FK → users) ON DELETE CASCADE |
| provider | VARCHAR(50) — 'github' \| 'google' |
| provider_account_id | VARCHAR(255) NOT NULL |
| access_token | TEXT |
| refresh_token | TEXT |
| expires_at | TIMESTAMP |
| created_at | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |

---

## Session (Sesión)

Gestiona los tokens JWT activos para control de sesiones.  
**Servicio:** Auth Service | **Base de datos:** PostgreSQL (`auth_db`)

| Campo | Tipo |
|------|------|
| id | UUID (PK) |
| user_id | UUID (FK → users) ON DELETE CASCADE |
| token | VARCHAR(500) UNIQUE NOT NULL |
| expires_at | TIMESTAMP NOT NULL |
| created_at | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |

---


## Repository (Repositorio)

Representa un repositorio Git creado por un usuario.

| Campo | Tipo |
|------|------|
| Id | INT (PK) |
| Name | VARCHAR |
| Description | TEXT |
| IsPrivate | BIT |
| OwnerId | INT (FK → User) |
| CreatedAt | DATETIME |

---

## RepositoryPermission (Permisos)

Define los niveles de acceso de los usuarios a un repositorio.

| Campo | Tipo |
|------|------|
| Id | INT (PK) |
| UserId | INT (FK → User) |
| RepositoryId | INT (FK → Repository) |
| Role | VARCHAR (Owner, Write, Read) |

---

## Branch (Rama)

Representa las ramas dentro de un repositorio.

| Campo | Tipo |
|------|------|
| Id | INT (PK) |
| Name | VARCHAR |
| RepositoryId | INT (FK) |
| IsDefault | BIT |

---

## Commit

Representa los commits realizados en el repositorio.

| Campo | Tipo |
|------|------|
| Id | VARCHAR (PK) |
| Message | TEXT |
| AuthorId | INT (FK → User) |
| RepositoryId | INT (FK) |
| BranchId | INT (FK) |
| CreatedAt | DATETIME |

---

## File (Archivo)

Representa los archivos versionados en un commit.

| Campo | Tipo |
|------|------|
| Id | INT (PK) |
| Path | VARCHAR |
| Content | TEXT |
| CommitId | VARCHAR (FK → Commit) |

---

## PullRequest (Solicitud de Cambio)

Permite proponer cambios entre ramas.

| Campo | Tipo |
|------|------|
| Id | INT (PK) |
| Title | VARCHAR |
| Description | TEXT |
| SourceBranchId | INT |
| TargetBranchId | INT |
| AuthorId | INT |
| Status | VARCHAR (Open, Closed, Merged) |

---

## Issue (Incidencia)

Permite registrar tareas, bugs o mejoras.
**Servicio:** Issue Service | **Base de datos:** PostgreSQL (`issues_db`)

| Campo | Tipo |
|------|------|
| Id | UUID (PK) |
| repo_id | VARCHAR(50) NOT NULL — ID del repo (Mongo ObjectId como texto o postgres) |
| number | INTEGER NOT NULL — número secuencial por repo |
| Title | VARCHAR(255) NOT NULL |
| body | TEXT |
| state | VARCHAR(20) NOT NULL DEFAULT 'open' — 'open' \| 'closed' |
| Description | TEXT |
| RepositoryId | INT |
| AuthorId | INT |
| Status | VARCHAR (Open, Closed) |
| assignee_id | UUID — user_id de Auth Service (nullable) |
| created_at | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |
| updated_at | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |
| closed_at | TIMESTAMP |

---

## Label (Etiqueta)

Etiquetas reutilizables dentro de un repositorio (bug, feature, etc.).  
**Servicio:** Issue Service | **Base de datos:** PostgreSQL (`issues_db`)

| Campo | Tipo |
|------|------|
| id | UUID (PK) |
| repo_id | VARCHAR(50) NOT NULL |
| name | VARCHAR(50) NOT NULL |
| color | CHAR(7) NOT NULL — "#ff0000" |
| description | VARCHAR(255) |

---

## IssueLabel (Relación Issue-Etiqueta N:M)

**Servicio:** Issue Service | **Base de datos:** PostgreSQL (`issues_db`)

| Campo | Tipo |
|------|------|
| issue_id | UUID (FK → issues) ON DELETE CASCADE |
| label_id | UUID (FK → labels) ON DELETE CASCADE |

---

## Comment (Comentario)

Permite comentar en Issues y Pull Requests.

| Campo | Tipo |
|------|------|
| Id | UUID (PK) |
| body | TEXT NOT NULL |
| AuthorId | UUID NOT NULL — user_id de Auth Service |
| IssueId | UUID (FK → issues) ON DELETE CASCADE |
| PullRequestId | INT (NULLABLE) |
| CreatedAt | DATETIME |
| updated_at | TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP |

---

# Relaciones entre Entidades

```

User ──< Repository
User ──< RepositoryPermission >── Repository

Repository ──< Branch
Branch ──< Commit
Commit ──< File

Repository ──< Issue ──< Comment
Repository ──< PullRequest ──< Comment

User ──< OAuthAccount
User ──< Session

Repository ──< Star
Issue >──< Label (via IssueLabel)

````

---

# Modelo Relacional (SQL)

```sql
-- USERS
Users (
  Id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  Username          VARCHAR(50)  UNIQUE NOT NULL,
  Email             VARCHAR(255) UNIQUE NOT NULL,
  PasswordHash      VARCHAR(255) NOT NULL,
  avatar_url        VARCHAR(500),
  bio               TEXT,
  location          VARCHAR(100),
  website           VARCHAR(255),
  CreatedAt         TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP 
   updated_at       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email    ON users (email);

-- OAUTH ACCOUNTS
CREATE TABLE oauth_accounts (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id             UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    provider            VARCHAR(50)  NOT NULL,
    provider_account_id VARCHAR(255) NOT NULL,
    access_token        TEXT,
    refresh_token       TEXT,
    expires_at          TIMESTAMP,
    created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uq_oauth_provider UNIQUE (provider, provider_account_id)
);

CREATE INDEX idx_oauth_user_id ON oauth_accounts (user_id);

-- SESSIONS
CREATE TABLE sessions (
    id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id    UUID        NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    token      VARCHAR(500) UNIQUE NOT NULL,
    expires_at TIMESTAMP   NOT NULL,
    created_at TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_sessions_user_id    ON sessions (user_id);
CREATE INDEX idx_sessions_expires_at ON sessions (expires_at);

-- REPOSITORIES
Repositories (
  Id INT PRIMARY KEY,
  Name VARCHAR(150),
  Description TEXT,
  IsPrivate BIT,
  OwnerId INT,
  CreatedAt DATETIME,
  FOREIGN KEY (OwnerId) REFERENCES Users(Id)
);

-- PERMISSIONS
RepositoryPermissions (
  Id INT PRIMARY KEY,
  UserId INT,
  RepositoryId INT,
  Role VARCHAR(50),
  FOREIGN KEY (UserId) REFERENCES Users(Id),
  FOREIGN KEY (RepositoryId) REFERENCES Repositories(Id)
);

-- BRANCHES
Branches (
  Id INT PRIMARY KEY,
  Name VARCHAR(100),
  RepositoryId INT,
  IsDefault BIT,
  FOREIGN KEY (RepositoryId) REFERENCES Repositories(Id)
);

-- COMMITS
Commits (
  Id VARCHAR(100) PRIMARY KEY,
  Message TEXT,
  AuthorId INT,
  RepositoryId INT,
  BranchId INT,
  CreatedAt DATETIME,
  FOREIGN KEY (AuthorId) REFERENCES Users(Id),
  FOREIGN KEY (RepositoryId) REFERENCES Repositories(Id),
  FOREIGN KEY (BranchId) REFERENCES Branches(Id)
);

-- FILES
Files (
  Id INT PRIMARY KEY,
  Path VARCHAR(255),
  Content TEXT,
  CommitId VARCHAR(100),
  FOREIGN KEY (CommitId) REFERENCES Commits(Id)
);

-- PULL REQUESTS
PullRequests (
  Id INT PRIMARY KEY,
  Title VARCHAR(150),
  Description TEXT,
  SourceBranchId INT,
  TargetBranchId INT,
  AuthorId INT,
  Status VARCHAR(50)
);

-- ISSUES
Issues (
  Id           UUID   PRIMARY KEY DEFAULT gen_random_uuid(),
  repo_id      VARCHAR(50) NOT NULL,
  number       INTEGER     NOT NULL,
  Title        VARCHAR(255) NOT NULL,
  body         TEXT,
  state        VARCHAR(20)  NOT NULL DEFAULT 'open',
  Description  TEXT,
  RepositoryId INT,
  AuthorId     UUID  NOT NULL,,
  Status       VARCHAR(50)
  assignee_id UUID,
    created_at  TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    closed_at   TIMESTAMP,

    CONSTRAINT uq_issue_repo_number UNIQUE (repo_id, number),
    CONSTRAINT chk_issue_state CHECK (state IN ('open', 'closed'))
);

CREATE INDEX idx_issues_repo_id    ON issues (repo_id);
CREATE INDEX idx_issues_author_id  ON issues (author_id);
CREATE INDEX idx_issues_state      ON issues (state);

-- LABELS
CREATE TABLE labels (
    id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    repo_id     VARCHAR(50) NOT NULL,
    name        VARCHAR(50) NOT NULL,
    color       CHAR(7)     NOT NULL,
    description VARCHAR(255),

    CONSTRAINT uq_label_repo_name UNIQUE (repo_id, name)
);

CREATE INDEX idx_labels_repo_id ON labels (repo_id);

-- ISSUE_LABELS (N:M)
CREATE TABLE issue_labels (
    issue_id UUID NOT NULL REFERENCES issues(id) ON DELETE CASCADE,
    label_id UUID NOT NULL REFERENCES labels(id) ON DELETE CASCADE,

    PRIMARY KEY (issue_id, label_id)
);

-- COMMENTS
Comments (
  Id          UUID  PRIMARY KEY DEFAULT gen_random_uuid(),
  body        TEXT  NOT NULL,
  AuthorId    UUID  NOT NULL,
  IssueId     UUID  NOT NULL REFERENCES issues(id) ON DELETE CASCADE,
  PullRequestId INT NULL,
  CreatedAt DATETIME,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_comments_issue_id ON comments (issue_id);
````

# Diagrama de Relaciones (por servicio)

```
AUTH SERVICE (PostgreSQL)
┌──────────┐       ┌─────────────────┐       ┌──────────┐
│  users   │──┐    │  oauth_accounts │       │ sessions │
│──────────│  └───►│─────────────────│       │──────────│
│ id (PK)  │       │ id (PK)         │       │ id (PK)  │
│ username │       │ user_id (FK)    │       │ user_id  │
│ email    │       │ provider        │       │ token    │
│ ...      │◄──────│ ...             │       │ ...      │
└──────────┘       └─────────────────┘       └──────────┘


ISSUE SERVICE (PostgreSQL)
┌──────────┐       ┌──────────────┐       ┌──────────┐
│  issues  │──┐    │ issue_labels │──┐    │  labels  │
│──────────│  └───►│──────────────│  └───►│──────────│
│ id (PK)  │       │ issue_id(FK) │       │ id (PK)  │
│ repo_id  │       │ label_id(FK) │       │ repo_id  │
│ number   │       └──────────────┘       │ name     │
│ state    │                              │ color    │
│ ...      │       ┌──────────────┐       └──────────┘
└──────────┘◄──────│   comments   │
                   │──────────────│
                   │ id (PK)      │
                   │ issue_id(FK) │
                   │ author_id    │
                   │ body         │
                   └──────────────┘
```