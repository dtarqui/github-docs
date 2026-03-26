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

## User (Usuario)

Representa a los usuarios registrados en la plataforma.

| Campo | Tipo |
|------|------|
| Id | INT (PK) |
| Username | VARCHAR |
| Email | VARCHAR |
| PasswordHash | VARCHAR |
| CreatedAt | DATETIME |

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

| Campo | Tipo |
|------|------|
| Id | INT (PK) |
| Title | VARCHAR |
| Description | TEXT |
| RepositoryId | INT |
| AuthorId | INT |
| Status | VARCHAR (Open, Closed) |

---

## Comment (Comentario)

Permite comentar en Issues y Pull Requests.

| Campo | Tipo |
|------|------|
| Id | INT (PK) |
| Content | TEXT |
| AuthorId | INT |
| IssueId | INT (NULLABLE) |
| PullRequestId | INT (NULLABLE) |
| CreatedAt | DATETIME |

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

````

---

# Modelo Relacional (SQL)

```sql
-- USERS
Users (
  Id INT PRIMARY KEY,
  Username VARCHAR(100),
  Email VARCHAR(150),
  PasswordHash VARCHAR(255),
  CreatedAt DATETIME
);

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
  Id INT PRIMARY KEY,
  Title VARCHAR(150),
  Description TEXT,
  RepositoryId INT,
  AuthorId INT,
  Status VARCHAR(50)
);

-- COMMENTS
Comments (
  Id INT PRIMARY KEY,
  Content TEXT,
  AuthorId INT,
  IssueId INT NULL,
  PullRequestId INT NULL,
  CreatedAt DATETIME
);
````

