# Repositorios del Ecosistema GitHub

Este documento centraliza los repositorios oficiales del ecosistema y su uso recomendado.

## Índice de repositorios

| Categoría       | Repositorio             | Propósito                                                                | Enlace                                                                        |
| --------------- | ----------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Documentación   | github-docs             | Documentación funcional/técnica del proyecto y entregables escritos.     | [github-docs](https://github.com/dtarqui/github-docs)                         |
| Contratos API   | Github-Smithy           | Contrato API (Smithy), generación OpenAPI y evidencia de `smithy build`. | [Github-Smithy](https://github.com/Savitar465/Github-Smithy)                  |
| Infraestructura | Github-Cdk              | Infraestructura cloud de referencia (EKS/RDS/Keycloak).                  | [Github-Cdk](https://github.com/Savitar465/Github-Cdk)                        |
| Microservicio   | Github-git              | Servicio de Git (server).                                                | [Github-git](https://github.com/dtarqui/Github-git)                           |
| Microservicio   | Github-files-ms         | Gestión de archivos y contenido.                                         | [Github-files-ms](https://github.com/Savitar465/Github-files-ms)              |
| Microservicio   | Github-issues-ms        | Gestión de issues.                                                       | [Github-issues-ms](https://github.com/Savitar465/Github-issues-ms)            |
| Microservicio   | Github-organizations-ms | Gestión de organizaciones y miembros/roles por organización.             | [Github-organizations-ms](https://github.com/dtarqui/Github-organizations-ms) |
| Microservicio   | Github-pull-requests-ms | Gestión de pull requests y flujo de revisión/merge.                      | [Github-pull-requests-ms](https://github.com/dtarqui/Github-pull-requests-ms) |
| Microservicio   | Github-repository-ms    | Gestión de repositorios y metadatos.                                     | [Github-repository-ms](https://github.com/Savitar465/Github-repository-ms)    |
| Microservicio   | Github-users-ms         | Gestión de usuarios (autenticación/perfil).                              | [Github-users-ms](https://github.com/Savitar465/Github-users-ms)              |
| Frontend        | Github-front            | Interfaz de usuario del proyecto GitHub.                                 | [Github-front](https://github.com/Savitar465/Github-front)                    |

## Uso recomendado en entregables

- Para referencias de contrato API y build, usar Github-Smithy.
- Para referencias de arquitectura/documentación, usar github-docs.
- Para referencias de infraestructura AWS, usar Github-Cdk.
- Para gestión de organizaciones, usar Github-organizations-ms.
- Para flujo de pull requests, usar Github-pull-requests-ms.
- Para gestión de usuarios, usar Github-users-ms.
- Para operaciones de archivos, usar Github-files-ms.
- Para gestión de repositorios, usar Github-repository-ms.
- Para interfaz de usuario, usar Github-front.
