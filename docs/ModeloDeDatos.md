# Mini GitHub - Modelo de Datos

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
---

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