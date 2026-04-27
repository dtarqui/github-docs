## Mini GitHub - Límites

Las siguientes funcionalidades quedan **fuera del alcance** del proyecto:

| ID   | Funcionalidad                | Justificación                                                                                                                                |
| ---- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| L-01 | CI/CD y pipelines            | No se implementarán workflows automáticos, runners ni ejecución de jobs en contenedores. Requeriría un proyecto separado por su complejidad. |
| L-02 | Acceso SSH y claves públicas | El microservicio Git se expondrá únicamente por HTTPS. No se implementará acceso por SSH ni gestión de claves públicas.                      |
| L-03 | Registro de paquetes         | No se publicarán ni consumirán paquetes npm, Maven, Docker o PyPI desde la plataforma.                                                       |
| L-04 | Git LFS y archivos grandes   | Tamaño máximo de repositorio: 100 MB. No se implementará Git Large File Storage.                                                             |
| L-05 | Notificaciones               | No se implementarán notificaciones por email, push, WebSockets ni SSE. Las actualizaciones se verán al recargar o navegar la aplicación.     |
| L-06 | Búsqueda de código           | No habrá indexación ni búsqueda dentro del contenido de archivos. Se permite búsqueda por nombre de repositorio, usuario e issues.           |
| L-07 | Aplicación móvil nativa      | Se implementará como PWA (Progressive Web App) en lugar de app nativa.                                                                       |
| L-08 | Stars en repositorios        | No se implementará la funcionalidad de dar/quitar estrellas a repositorios. Simplifica el modelo de datos y reduce complejidad.              |

### Aclaración: Pull Requests

Los **Pull Requests en flujo básico** (crear PR entre ramas, comentar, aprobar o solicitar cambios y merge) **forman parte del alcance** del producto. Quedan fuera flujos avanzados tipo GitHub (checks automáticos obligatorios, reglas complejas de protección de rama, revisiones en línea densas con sugerencias automáticas).

---
