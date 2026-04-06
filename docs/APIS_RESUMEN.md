# Resumen REST
Formato por endpoint: metodo + ruta, body de ejemplo cuando aplica, y tipo de respuesta principal (2xx).

## AuthAccountApi

_GitHub Auth Account API_

```txt
POST /v1/auth/logout -> No Content
descripcion: Invalida el token JWT activo.

GET /v1/auth/me -> UserDTO
descripcion: Devuelve el perfil del usuario autenticado derivado del JWT. RF01.3

POST /v1/auth/refresh -> AuthTokenDTO
descripcion: Renueva el access token antes de su expiracion. RNF14

GET /v1/users/{username} -> UserDTO
descripcion: Devuelve el perfil publico de un usuario por su username. RF05.2

PATCH /v1/users/me -> UserDTO
descripcion: Actualiza bio, avatar, location y website del usuario. RF01.3
body: {
  "avatarUrl": string
  "bio": string
  "location": string
  "website": string
}

```

## AuthPublicApi

_GitHub Auth Public API_

```txt
POST /v1/auth/forgot-password
descripcion: Envia email con enlace temporal de recuperacion. RF01.4
body: {
  "email": string
}

POST /v1/auth/login -> LoginResponseBody
descripcion: Autentica con email y contrasena, retorna JWT. RF01.1
body: {
  "email": string
  "password": string
}

GET /v1/auth/oauth/{provider} -> InitiateOAuthBody
descripcion: Inicia flujo OAuth con el proveedor indicado (github | google). RF01.2

GET /v1/auth/oauth/{provider}/callback -> LoginResponseBody
descripcion: Callback del proveedor OAuth. Crea usuario si no existe y emite JWT. RF01.2

POST /v1/auth/register -> RegisterResponseBody
descripcion: Registra un nuevo usuario con email y contrasena. RF01.1
body: {
  "username": string
  "email": string
  "password": string
  "confirmPassword": string
}

POST /v1/auth/reset-password/{token}
descripcion: Cambia la contrasena usando el token de recuperacion. RF01.4
body: {
  "newPassword": string
  "confirmPassword": string
}

```

## FilesApi

_GitHub Files API_

```txt
GET /v1/repos/{owner}/{repo}/commits -> ListCommitsBody
descripcion: Lista el historial de commits del repositorio. HU-18

GET /v1/repos/{owner}/{repo}/commits/{sha} -> GetCommitBody
descripcion: Obtiene el detalle de un commit específico. HU-18

GET /v1/repos/{owner}/{repo}/commits/{sha}/diff -> GetCommitDiffOutputPayload
descripcion: Obtiene el diff de un commit en formato texto. HU-18

GET /v1/repos/{owner}/{repo}/compare/{baseBranch}/{headBranch} -> CompareDTO
descripcion: Compara dos branches mostrando commits y archivos cambiados. HU-20

GET /v1/repos/{owner}/{repo}/contents -> GetFileContentBody
descripcion: Lista el contenido de una ruta del repositorio usando query path. HU-13

GET /v1/repos/{owner}/{repo}/contents/{filePath+} -> GetFileContentBody
descripcion: Obtiene el contenido de un archivo o lista el contenido de un directorio. RF03.3

PUT /v1/repos/{owner}/{repo}/contents/{filePath+} -> FileOperationResponse
descripcion: Sube un archivo al repositorio (create/update por path). RF03.1
body: {
  "content": string
  "message": string
  "branch": string
  "author": Identity
  "committer": Identity
}

PATCH /v1/repos/{owner}/{repo}/contents/{filePath+} -> FileOperationResponse
descripcion: Actualiza un archivo existente en el repositorio. RF03.1
body: {
  "sha": string
  "content": string
  "message": string
  "branch": string
  "fromPath": string
  "author": Identity
  "committer": Identity
}

DELETE /v1/repos/{owner}/{repo}/contents/{filePath+} -> DeleteFileResponseBody
descripcion: Elimina un archivo generando un commit de borrado. RF03.5

GET /v1/repos/{owner}/{repo}/download -> GetRawFileOutputPayload
descripcion: Descarga un archivo individual del repositorio. RF03.2

POST /v1/repos/{owner}/{repo}/folders -> FileOperationResponse
descripcion: Crea una carpeta nueva con .gitkeep. RF03.4
body: {
  "path": string
  "message": string
  "branch": string
}

```

## IssueApi

_GitHub Issue API_

```txt
GET /v1/repos/{owner}/{repo}/issues -> ListIssuesBody
descripcion: Lista los issues de un repositorio con filtros opcionales.

POST /v1/repos/{owner}/{repo}/issues -> IssueDTO
descripcion: Crea un issue en el repositorio.
body: {
  "title": string
  "body": string
  "labels": string[]
  "assignee": string
}

GET /v1/repos/{owner}/{repo}/issues/{issueNumber} -> IssueDTO
descripcion: Obtiene un issue por su número secuencial.

PATCH /v1/repos/{owner}/{repo}/issues/{issueNumber} -> IssueDTO
descripcion: Actualiza título, body, estado, assignee o labels.
body: {
  "title": string
  "body": string
  "state": IssueState
  "assignee": string
  "labels": string[]
}

GET /v1/repos/{owner}/{repo}/issues/{issueNumber}/comments -> ListIssueCommentsBody
descripcion: Lista los comentarios de un issue.

POST /v1/repos/{owner}/{repo}/issues/{issueNumber}/comments -> CommentDTO
descripcion: Agrega un comentario a un issue.
body: {
  "body": string
}

GET /v1/repos/{owner}/{repo}/labels -> ListLabelsBody
descripcion: Lista los labels disponibles en el repositorio.

POST /v1/repos/{owner}/{repo}/labels -> LabelDTO
descripcion: Crea un label nuevo en el repositorio.
body: {
  "name": string
  "color": string
  "description": string
}

GET /v1/repos/{owner}/{repo}/pulls -> ListPullRequestsBody
descripcion: Lista los Pull Requests del repositorio.

POST /v1/repos/{owner}/{repo}/pulls -> PullRequestDTO
descripcion: Crea un Pull Request entre dos ramas.
body: {
  "title": string
  "description": string
  "sourceBranch": string
  "targetBranch": string
}

GET /v1/repos/{owner}/{repo}/pulls/{prNumber} -> PullRequestDTO
descripcion: Obtiene el detalle de un PR.

GET /v1/repos/{owner}/{repo}/pulls/{prNumber}/comments -> ListPullRequestCommentsBody
descripcion: Lista historial de comentarios de un PR.

POST /v1/repos/{owner}/{repo}/pulls/{prNumber}/comments -> PullRequestCommentDTO
descripcion: Agrega un comentario general o por línea a un PR.
body: {
  "body": string
  "filePath": string
  "lineNumber": number
}

POST /v1/repos/{owner}/{repo}/pulls/{prNumber}/merge -> PullRequestDTO
descripcion: Ejecuta el merge de un PR aprobado y sin conflictos.
body: {
  "strategy": MergeStrategy
  "commitMessage": string
}

GET /v1/repos/{owner}/{repo}/pulls/{prNumber}/mergeability -> PullRequestMergeabilityDTO
descripcion: Evalúa conflictos y mergeabilidad de un PR antes del merge.

PATCH /v1/repos/{owner}/{repo}/pulls/{prNumber}/review -> PullRequestDTO
descripcion: Aprueba o solicita cambios en un PR.
body: {
  "decision": ReviewDecision
  "comment": string
}

```

## IssueCommentsApi

_GitHub Issue Comments API_

```txt
GET /v1/repos/{owner}/{repo}/issues/comments -> ListIssueCommentsBody
descripcion: Lista comentarios de issues a nivel repositorio.

GET /v1/repos/{owner}/{repo}/issues/comments/{commentId} -> CommentDTO
descripcion: Obtiene un comentario de issue por su ID.

PATCH /v1/repos/{owner}/{repo}/issues/comments/{commentId} -> CommentDTO
descripcion: Actualiza el cuerpo de un comentario de issue.
body: {
  "body": string
}

DELETE /v1/repos/{owner}/{repo}/issues/comments/{commentId} -> No Content
descripcion: Elimina un comentario de issue por su ID.

```

## OrgApi

_GitHub Organization API_

```txt
POST /v1/orgs -> OrganizationDTO
descripcion: Crea una nueva organización. El usuario autenticado queda como owner.
body: {
  "name": string
  "displayName": string
  "description": string
  "website": string
  "visibility": OrgVisibility
}

PATCH /v1/orgs/{orgName} -> OrganizationDTO
descripcion: Actualiza los datos de la organización. Solo el owner puede hacerlo.
body: {
  "displayName": string
  "description": string
  "website": string
  "avatarUrl": string
  "visibility": OrgVisibility
}

DELETE /v1/orgs/{orgName} -> No Content
descripcion: Elimina la organización y todos sus equipos y repositorios. Solo el owner puede hacerlo.

GET /v1/orgs/{orgName}/members -> ListOrgMembersBody
descripcion: Lista todos los miembros de la organización con sus roles.

POST /v1/orgs/{orgName}/members -> OrgMemberDTO
descripcion: Invita a un usuario a unirse a la organización con un rol.
body: {
  "username": string
  "role": OrgMemberRole
}

PATCH /v1/orgs/{orgName}/members/{username} -> OrgMemberDTO
descripcion: Cambia el rol de un miembro dentro de la organización.
body: {
  "role": OrgMemberRole
}

DELETE /v1/orgs/{orgName}/members/{username} -> No Content
descripcion: Elimina a un miembro de la organización y de todos sus equipos.

GET /v1/orgs/{orgName}/teams -> ListOrgTeamsBody
descripcion: Lista todos los equipos de la organización.

POST /v1/orgs/{orgName}/teams -> TeamDTO
descripcion: Crea un nuevo equipo dentro de la organización con un nivel de permisos.
body: {
  "name": string
  "description": string
  "permission": TeamPermission
}

GET /v1/orgs/{orgName}/teams/{teamId} -> TeamDTO
descripcion: Obtiene los datos de un equipo específico.

PATCH /v1/orgs/{orgName}/teams/{teamId} -> TeamDTO
descripcion: Actualiza el nombre, descripción o permisos de un equipo.
body: {
  "name": string
  "description": string
  "permission": TeamPermission
}

DELETE /v1/orgs/{orgName}/teams/{teamId} -> No Content
descripcion: Elimina un equipo de la organización.

GET /v1/orgs/{orgName}/teams/{teamId}/members -> ListTeamMembersBody
descripcion: Lista los miembros de un equipo.

PUT /v1/orgs/{orgName}/teams/{teamId}/members/{username} -> No Content
descripcion: Agrega a un miembro de la organización a un equipo.

DELETE /v1/orgs/{orgName}/teams/{teamId}/members/{username} -> No Content
descripcion: Elimina a un miembro de un equipo (no lo elimina de la organización).

GET /v1/orgs/{orgName}/teams/{teamId}/repos -> ListTeamReposBody
descripcion: Lista los repositorios que tiene asignados un equipo.

PUT /v1/orgs/{orgName}/teams/{teamId}/repos/{repoName} -> No Content
descripcion: Asigna un repositorio de la organización a un equipo con permisos específicos.
body: {
  "permission": TeamPermission
}

DELETE /v1/orgs/{orgName}/teams/{teamId}/repos/{repoName} -> No Content
descripcion: Quita el acceso de un equipo a un repositorio.

GET /v1/user/orgs -> ListMyOrganizationsBody
descripcion: Lista las organizaciones a las que pertenece el usuario autenticado.

```

## OrgPublicApi

_GitHub Organization Public API_

```txt
GET /v1/orgs/{orgName} -> OrganizationDTO
descripcion: Obtiene los datos públicos de una organización.

GET /v1/orgs/{orgName}/repos -> ListOrgReposBody
descripcion: Lista todos los repositorios que pertenecen a la organización.

```

## RepoApi

_GitHub Repo API_

```txt
GET /v1/repos -> ListRepositoriesBody
descripcion: Lista los repositorios del usuario autenticado.

POST /v1/repos -> RepositoryDTO
descripcion: Crea un repositorio nuevo para el usuario autenticado.
body: {
  "name": string
  "description": string
  "visibility": RepoVisibility
  "initWithReadme": boolean
  "language": string
}

GET /v1/repos/{owner}/{repo} -> RepositoryDTO
descripcion: Obtiene los datos de un repositorio.

PATCH /v1/repos/{owner}/{repo} -> RepositoryDTO
descripcion: Actualiza descripción, visibilidad u opciones del repositorio. Solo el owner.
body: {
  "description": string
  "visibility": RepoVisibility
  "hasIssues": boolean
  "language": string
}

DELETE /v1/repos/{owner}/{repo} -> No Content
descripcion: Elimina el repositorio y todos sus datos. Solo el owner.

GET /v1/repos/{owner}/{repo}/archive
descripcion: Descarga el repositorio completo en ZIP.

GET /v1/repos/{owner}/{repo}/branches -> ListBranchesBody
descripcion: Lista todas las ramas del repositorio.

POST /v1/repos/{owner}/{repo}/branches -> BranchDTO
descripcion: Crea una rama nueva a partir de otra existente.
body: {
  "name": string
  "fromBranch": string
}

GET /v1/repos/{owner}/{repo}/branches/{branch} -> BranchDTO
descripcion: Obtiene el detalle de una rama específica.

DELETE /v1/repos/{owner}/{repo}/branches/{branch} -> No Content
descripcion: Elimina una rama (no puede ser la rama por defecto).

GET /v1/repos/{owner}/{repo}/collaborators -> ListCollaboratorsBody
descripcion: Lista colaboradores y sus roles.

POST /v1/repos/{owner}/{repo}/collaborators -> CollaboratorDTO
descripcion: Invita a un colaborador con un rol.
body: {
  "username": string
  "role": CollaboratorRole
}

GET /v1/repos/{owner}/{repo}/collaborators/{collaboratorUsername} -> CollaboratorDTO
descripcion: Obtiene detalle de un colaborador específico.

PUT /v1/repos/{owner}/{repo}/collaborators/{collaboratorUsername} -> No Content
descripcion: Agrega o confirma un colaborador por username.

PATCH /v1/repos/{owner}/{repo}/collaborators/{collaboratorUsername} -> CollaboratorDTO
descripcion: Cambia el rol de un colaborador existente.
body: {
  "role": CollaboratorRole
}

DELETE /v1/repos/{owner}/{repo}/collaborators/{collaboratorUsername} -> No Content
descripcion: Elimina un colaborador del repositorio.

GET /v1/repos/{owner}/{repo}/contents/{filePath+} -> GetRepoContentsBody
descripcion: Lista archivos y carpetas de una ruta del repositorio.

PUT /v1/repos/{owner}/{repo}/contents/{filePath+} -> FileEntryDTO
descripcion: Sube o actualiza un archivo en el repositorio.
body: {
  "content": string
  "message": string
  "branch": string
}

DELETE /v1/repos/{owner}/{repo}/contents/{filePath+} -> No Content
descripcion: Elimina un archivo generando un commit de borrado.

GET /v1/repos/{owner}/{repo}/forks -> ListRepositoryForksBody
descripcion: Lista los forks de un repositorio.

POST /v1/repos/{owner}/{repo}/forks -> RepositoryDTO
descripcion: Crea un fork de un repositorio público en la cuenta del usuario autenticado.
body: {
  "name": string
  "targetOwner": string
}

PUT /v1/repos/{owner}/{repo}/star -> No Content
descripcion: Da estrella a un repositorio.

DELETE /v1/repos/{owner}/{repo}/star -> No Content
descripcion: Quita la estrella de un repositorio.

PUT /v1/user/starred/{owner}/{repo} -> No Content
descripcion: Da estrella a un repositorio con ruta.

DELETE /v1/user/starred/{owner}/{repo} -> No Content
descripcion: Quita estrella a un repositorio con ruta.

```

## SearchApi

_GitHub Search API_

```txt
GET /v1/search/issues -> SearchIssuesBody
descripcion: Busca issues en repositorios accesibles por el usuario.

GET /v1/search/repositories -> SearchRepositoriesBody
descripcion: Busca repositorios públicos por nombre, descripción o lenguaje. RF05.1

GET /v1/search/users -> SearchUsersBody
descripcion: Busca usuarios por username. RF05.2

```

