# Mini GitHub - Modelo de Datos

# Modelo Relacional (SQL)

```sql
-- USERS
CREATE TABLE users (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username          VARCHAR(50)  UNIQUE NOT NULL,
  email             VARCHAR(255) UNIQUE NOT NULL,
  password_hash     VARCHAR(255) NOT NULL,
  avatar_url        VARCHAR(500),
  bio               TEXT,
  location          VARCHAR(100),
  website           VARCHAR(255),
  created_at        TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at        TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
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
CREATE TABLE repositories (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(150) NOT NULL,
  description TEXT,
  is_private BOOLEAN,
  owner_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- PERMISSIONS
CREATE TABLE repository_permissions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  repository_id UUID NOT NULL REFERENCES repositories(id) ON DELETE CASCADE,
  role VARCHAR(50) NOT NULL,

  CONSTRAINT uq_repo_user_role UNIQUE (repository_id, user_id)
);

-- BRANCHES
CREATE TABLE branches (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(100) NOT NULL,
  repository_id UUID NOT NULL REFERENCES repositories(id) ON DELETE CASCADE,
  is_default BOOLEAN DEFAULT false,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- COMMITS
CREATE TABLE commits (
  id VARCHAR(100) PRIMARY KEY,
  message TEXT NOT NULL,
  author_id UUID NOT NULL REFERENCES users(id),
  repository_id UUID NOT NULL REFERENCES repositories(id) ON DELETE CASCADE,
  branch_id UUID REFERENCES branches(id) ON DELETE SET NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- FILES
-- Nota de diseño: el contenido binario se almacena en MinIO/S3.
-- Esta tabla solo guarda metadata y la referencia al objeto en storage.
CREATE TABLE files (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  path VARCHAR(512) NOT NULL,
  storage_key VARCHAR(512) NOT NULL,
  content_type VARCHAR(100),
  size_bytes BIGINT,
  commit_id VARCHAR(100) NOT NULL REFERENCES commits(id) ON DELETE CASCADE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_files_storage_key ON files (storage_key);

-- ISSUES
-- Nota de diseño: repo_id es referencia lógica al repositorio (Repo Service),
-- sin FK física cross-service para respetar database-per-service.
-- La validez de repo_id se verifica en la capa de aplicación.
-- author_id y assignee_id son referencias lógicas a users (Auth Service).
CREATE TABLE issues (
  id           UUID   PRIMARY KEY DEFAULT gen_random_uuid(),
  repo_id      UUID   NOT NULL,
  number       INTEGER     NOT NULL,
  title        VARCHAR(255) NOT NULL,
  body         TEXT,
  state        VARCHAR(20)  NOT NULL DEFAULT 'open',
  author_id    UUID  NOT NULL,
  assignee_id  UUID,
  created_at   TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at   TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  closed_at    TIMESTAMP,

  CONSTRAINT uq_issue_repo_number UNIQUE (repo_id, number),
  CONSTRAINT chk_issue_state CHECK (state IN ('open', 'closed'))
);

CREATE INDEX idx_issues_repo_id    ON issues (repo_id);
CREATE INDEX idx_issues_author_id  ON issues (author_id);
CREATE INDEX idx_issues_state      ON issues (state);

-- LABELS
-- Nota de diseño: repo_id mantiene el mismo criterio de referencia lógica
-- y validación en aplicación que issues.repo_id.
CREATE TABLE labels (
    id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
    repo_id     UUID        NOT NULL,
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

-- PULL REQUESTS
CREATE TABLE pull_requests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  repository_id UUID NOT NULL REFERENCES repositories(id) ON DELETE CASCADE,
  source_branch_id UUID REFERENCES branches(id) ON DELETE SET NULL,
  target_branch_id UUID REFERENCES branches(id) ON DELETE SET NULL,
  author_id UUID NOT NULL REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  description TEXT,
  status VARCHAR(20) NOT NULL DEFAULT 'open',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  merged_at TIMESTAMP,

  CONSTRAINT chk_pr_status CHECK (status IN ('open', 'closed', 'merged'))
);

CREATE INDEX idx_pull_requests_repo_id   ON pull_requests (repository_id);
CREATE INDEX idx_pull_requests_author_id ON pull_requests (author_id);
CREATE INDEX idx_pull_requests_status    ON pull_requests (status);

-- COMMENTS
-- Nota de diseño: author_id es referencia lógica a users (Auth Service).
CREATE TABLE comments (
  id          UUID  PRIMARY KEY DEFAULT gen_random_uuid(),
  body        TEXT  NOT NULL,
  author_id   UUID  NOT NULL,
  issue_id    UUID REFERENCES issues(id) ON DELETE CASCADE,
  pull_request_id UUID REFERENCES pull_requests(id) ON DELETE CASCADE,
  created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT chk_comment_target CHECK (
    (issue_id IS NOT NULL AND pull_request_id IS NULL)
    OR (issue_id IS NULL AND pull_request_id IS NOT NULL)
  )
);

CREATE INDEX idx_comments_issue_id ON comments (issue_id);
CREATE INDEX idx_comments_pull_request_id ON comments (pull_request_id);


-- ORGANIZATIONS
CREATE TABLE organizations (
    id           UUID         NOT NULL DEFAULT gen_random_uuid(),
    name         VARCHAR(50)  NOT NULL,
    display_name VARCHAR(100) NOT NULL,
    description  TEXT,
    avatar_url   VARCHAR(500),
    website      VARCHAR(500),
    visibility   VARCHAR(20)  NOT NULL DEFAULT 'public'
                              CHECK (visibility IN ('public', 'private')),
    owner_id     UUID         NOT NULL,
    created_at   TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at   TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_organizations PRIMARY KEY (id),
    CONSTRAINT uq_org_name UNIQUE (name)
);

CREATE INDEX idx_org_owner ON organizations (owner_id);

-- ORG_MEMBERS
CREATE TABLE org_members (
    organization_id UUID        NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    user_id         UUID        NOT NULL,
    username        VARCHAR(50) NOT NULL,
    avatar_url      VARCHAR(500),
    role            VARCHAR(20) NOT NULL DEFAULT 'member'
                                CHECK (role IN ('owner', 'member')),
    joined_at       TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (organization_id, user_id)
);

CREATE INDEX idx_org_members_username ON org_members (organization_id, username);
CREATE INDEX idx_org_members_user     ON org_members (user_id);

-- TEAMS
CREATE TABLE teams (
    id              UUID        NOT NULL DEFAULT gen_random_uuid(),
    organization_id UUID        NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    name            VARCHAR(50) NOT NULL,
    description     TEXT,
    permission      VARCHAR(20) NOT NULL DEFAULT 'read'
                                CHECK (permission IN ('read', 'write', 'admin')),
    created_at      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id),
    CONSTRAINT uq_team_name_per_org UNIQUE (organization_id, name)
);

CREATE INDEX idx_teams_org ON teams (organization_id);

-- TEAM_MEMBERS

CREATE TABLE team_members (
    team_id    UUID        NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    user_id    UUID        NOT NULL,
    username   VARCHAR(50) NOT NULL,
    avatar_url VARCHAR(500),
    added_at   TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (team_id, user_id)
);

CREATE INDEX idx_team_members_user ON team_members (user_id);

-- TEAM_REPOS
CREATE TABLE team_repos (
    team_id     UUID        NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    repo_id     UUID        NOT NULL,
    repo_name   VARCHAR(100) NOT NULL,
    full_name   VARCHAR(200) NOT NULL,
    permission  VARCHAR(20) NOT NULL DEFAULT 'read'
                            CHECK (permission IN ('read', 'write', 'admin')),
    assigned_at TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (team_id, repo_id)
);

CREATE INDEX idx_team_repos_repo_name ON team_repos (team_id, repo_name);



```

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


REPO SERVICE (PostgreSQL)
  repositories ──< branches
  repositories ──< commits ──< files
  repositories ──< pull_requests

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
