# Historias de Usuario — Mini-GitHub

## Tabla de Contenidos

- [Épica 1: Autenticación y Gestión de Usuarios](#épica-1-autenticación-y-gestión-de-usuarios)
- [Épica 2: Gestión de Repositorios](#épica-2-gestión-de-repositorios)
- [Épica 3: Operaciones Git y Archivos](#épica-3-operaciones-git-y-archivos)
- [Épica 4: Colaboración](#épica-4-colaboración)
- [Épica 5: Búsqueda y Notificaciones](#épica-5-búsqueda-y-notificaciones)
- [Épica 6: Documentación y Calidad](#épica-6-documentación-y-calidad)

---

## Épica 1: Autenticación y Gestión de Usuarios

### HU-01: Registro de nuevos usuarios

> **Como** visitante del sitio
> **Quiero** poder crear una cuenta con mi email y una contraseña
> **Para** acceder a la plataforma y gestionar repositorios

**Criterios de aceptación:**

- [ ] Formulario con campos: email, contraseña, confirmar contraseña.
- [ ] Validación de formato de email y fortaleza de contraseña.
- [ ] Envío de email de bienvenida o confirmación (según flujo definido).
- [ ] Almacenamiento seguro de contraseñas (hash + salt).
- [ ] Redirección al dashboard tras registro exitoso.

**Checklist de tareas:**

- [ ] Diseñar interfaz de registro (HTML/CSS/React).
- [ ] Crear endpoint `POST /api/auth/register` en backend.
- [ ] Implementar validaciones de entrada (email único, contraseña segura).
- [ ] Configurar hashing de contraseñas con bcrypt.
- [ ] Generar y almacenar JWT al finalizar registro.
- [ ] Implementar email de bienvenida (opcional).
- [ ] Escribir pruebas unitarias e integración.

---

### HU-02: Inicio de sesión con email y contraseña

> **Como** usuario registrado
> **Quiero** iniciar sesión con mi email y contraseña
> **Para** acceder a mi cuenta y usar la plataforma

**Criterios de aceptación:**

- [ ] Formulario de login con email y contraseña.
- [ ] Validación de credenciales.
- [ ] Generación de token JWT al autenticarse.
- [ ] Almacenamiento seguro del token en frontend (httpOnly cookie o localStorage con medidas de seguridad).
- [ ] Manejo de errores (credenciales incorrectas, cuenta no confirmada).

**Checklist de tareas:**

- [ ] Crear endpoint `POST /api/auth/login`.
- [ ] Verificar contraseña contra hash almacenado.
- [ ] Generar JWT con expiración.
- [ ] Configurar interceptor en frontend para adjuntar token.
- [ ] Implementar redirección a dashboard tras login.
- [ ] Manejar errores 401/403.
- [ ] Agregar opción de "recordarme".

---

### HU-03: Autenticación con SSO vía Keycloak con federación de proveedores

> **Como** usuario
> **Quiero** poder iniciar sesión mediante SSO a través de Keycloak usando mi cuenta de GitHub, Google o credenciales locales
> **Para** acceder sin tener que recordar otra contraseña y poder usar más de una forma de autenticación

**Criterios de aceptación:**

- [ ] Botón "Login with SSO" en la pantalla de acceso.
- [ ] Keycloak muestra opciones para: usuario/contraseña local, login con GitHub, login con Google.
- [ ] Federación de identidades de GitHub y Google configurada en el realm de Keycloak.
- [ ] Redirección al servidor Keycloak y callback de retorno con token OIDC.
- [ ] Creación automática de usuario local si no existe (a partir del perfil federado).
- [ ] Generación de JWT de la plataforma tras autenticación OIDC exitosa.

**Checklist de tareas:**

- [ ] Configurar realm y cliente en Keycloak.
- [ ] Registrar y configurar identity providers: GitHub OAuth, Google OAuth en Keycloak.
- [ ] Configurar variables de entorno (`KEYCLOAK_URL`, `CLIENT_ID`, `CLIENT_SECRET`, `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`).
- [ ] Implementar endpoint `/api/auth/sso` y callback `/api/auth/sso/callback`.
- [ ] Crear lógica de callback y creación/actualización de usuario local.
- [ ] Generar JWT de la plataforma y redirigir al frontend con token.
- [ ] Agregar botón de SSO en frontend que redirija a pantalla de login de Keycloak.
- [ ] Probar flujo completo en entorno local y producción (usuario local, GitHub, Google).

---

### HU-04: Recuperación de contraseña

> **Como** usuario
> **Quiero** poder restablecer mi contraseña si la olvidé
> **Para** recuperar el acceso a mi cuenta

**Criterios de aceptación:**

- [ ] Enlace "Olvidé mi contraseña" en login.
- [ ] Formulario para ingresar email.
- [ ] Envío de email con enlace único y temporal.
- [ ] Formulario para nueva contraseña.
- [ ] Actualización segura de la contraseña.

**Checklist de tareas:**

- [ ] Crear endpoint `POST /api/auth/forgot-password`.
- [ ] Generar token único con expiración (ej. 1 hora).
- [ ] Configurar servicio de envío de emails (nodemailer, SendGrid, etc.).
- [ ] Diseñar plantilla de email de recuperación.
- [ ] Crear endpoint `POST /api/auth/reset-password/:token`.
- [ ] Validar token y actualizar contraseña.
- [ ] Agregar interfaz de recuperación en frontend.

---

### HU-05: Edición de perfil de usuario

> **Como** usuario autenticado
> **Quiero** poder editar mi nombre, avatar y otros datos de perfil
> **Para** personalizar mi cuenta

**Criterios de aceptación:**

- [ ] Página de perfil con datos actuales.
- [ ] Campos editables: nombre completo, avatar (URL o subida), biografía.
- [ ] Validación de datos.
- [ ] Persistencia de cambios.

**Checklist de tareas:**

- [ ] Crear endpoint `GET /api/users/me` para obtener perfil.
- [ ] Crear endpoint `PUT /api/users/me` para actualizar perfil.
- [ ] Implementar subida de avatar a cloud storage (ej. AWS S3).
- [ ] Diseñar interfaz de perfil en frontend.
- [ ] Manejar carga de imagen y previsualización.
- [ ] Probar actualización de datos.

---

## Épica 2: Gestión de Repositorios

### HU-06: Crear repositorio nuevo

> **Como** usuario autenticado
> **Quiero** crear un repositorio nuevo, eligiendo nombre, descripción y visibilidad (público/privado)
> **Para** empezar a versionar mi código

**Criterios de aceptación:**

- [ ] Formulario con nombre, descripción opcional, selector público/privado.
- [ ] Creación de repositorio vacío en el sistema.
- [ ] Inicialización con README opcional.
- [ ] Redirección a la página del repositorio.

**Checklist de tareas:**

- [ ] Crear endpoint `POST /api/repos`.
- [ ] Validar nombre único por usuario.
- [ ] Crear estructura de base de datos para repositorio.
- [ ] Generar carpeta física o estructura en sistema de archivos (si aplica).
- [ ] Agregar opción "Inicializar con README" en frontend.
- [ ] Mostrar nuevo repositorio en lista.

---

### HU-07: Listar repositorios del usuario

> **Como** usuario autenticado
> **Quiero** ver una lista de todos mis repositorios
> **Para** acceder rápidamente a ellos

**Criterios de aceptación:**

- [ ] Vista con tarjetas o tabla de repositorios.
- [ ] Mostrar nombre, descripción, visibilidad, fecha de creación.
- [ ] Enlace a cada repositorio.
- [ ] Filtro por públicos/privados.

**Checklist de tareas:**

- [ ] Crear endpoint `GET /api/repos?user=me`.
- [ ] Implementar paginación.
- [ ] Diseñar componente de lista en frontend.
- [ ] Agregar buscador local por nombre.
- [ ] Manejar estados de carga y vacío.

---

### HU-08: Editar información de repositorio

> **Como** usuario propietario de un repositorio
> **Quiero** poder editar la descripción, visibilidad y otros metadatos
> **Para** mantener la información actualizada

**Criterios de aceptación:**

- [ ] Página de configuración del repositorio.
- [ ] Campos editables: descripción, visibilidad (público/privado).
- [ ] Confirmación de cambios.
- [ ] Validación de permisos (solo owner).

**Checklist de tareas:**

- [ ] Crear endpoint `PATCH /api/repos/:repoId`.
- [ ] Verificar que el usuario sea owner.
- [ ] Actualizar campos en base de datos.
- [ ] Diseñar formulario de edición en frontend.
- [ ] Mostrar mensajes de éxito/error.

---

### HU-10: Hacer fork de un repositorio público

> **Como** usuario
> **Quiero** hacer fork de un repositorio público para tener mi propia copia
> **Para** trabajar en el proyecto de forma independiente

**Criterios de aceptación:**

- [ ] Botón "Fork" visible en repositorios públicos.
- [ ] Creación de copia exacta del repositorio con nuevo dueño (el usuario).
- [ ] Mantener referencia al repositorio original (upstream).
- [ ] El fork aparece en la lista de repositorios del usuario.
- [ ] Cambios en el fork no afectan al original.

**Checklist de tareas:**

- [ ] Crear endpoint `POST /api/repos/:repoId/fork`.
- [ ] Validar que el repositorio sea público.
- [ ] Copiar estructura del repositorio (metadata, files, issues, labels).
- [ ] Asignar nuevo owner al fork (usuario autenticado).
- [ ] Almacenar referencia al repositorio padre en la BD.
- [ ] Agregar botón de fork en UI del repositorio.
- [ ] Mostrar badge "forked from <original repo>" en la página del fork.
- [ ] Redirigir al usuario al fork creado.

---

### HU-10: Eliminar repositorio

> **Como** usuario propietario
> **Quiero** eliminar un repositorio que ya no necesito
> **Para** mantener limpia mi cuenta

**Criterios de aceptación:**

- [ ] Botón de eliminar en configuración.
- [ ] Confirmación con diálogo de advertencia.
- [ ] Eliminación física del repositorio y sus datos.
- [ ] Redirección a dashboard.

**Checklist de tareas:**

- [ ] Crear endpoint `DELETE /api/repos/:repoId`.
- [ ] Verificar permisos de owner.
- [ ] Eliminar registros de BD y archivos asociados.
- [ ] Agregar modal de confirmación en frontend.
- [ ] Manejar eliminación en cascada (commits, branches, etc.).

---

## Épica 3: Operaciones Git y Archivos

### HU-11: Clonar repositorio vía HTTPS

> **Como** usuario
> **Quiero** clonar un repositorio remoto usando HTTPS con mis credenciales o token
> **Para** trabajar localmente con Git

**Criterios de aceptación:**

- [ ] URL HTTPS visible en repositorio.
- [ ] Autenticación vía usuario/contraseña o token personal.
- [ ] Soporte para `git clone` desde cliente externo.
- [ ] Generación de token personal en perfil.

**Checklist de tareas:**

- [ ] Configurar servidor Git (ej. usando git-http-backend o libgit2).
- [ ] Implementar autenticación HTTP básica o token.
- [ ] Crear endpoint para generar tokens personales.
- [ ] Probar clonación con Git CLI.
- [ ] Documentar URL y método de autenticación.

---

### HU-12: Push/Pull vía HTTPS

> **Como** usuario
> **Quiero** hacer push y pull de cambios usando HTTPS
> **Para** sincronizar mi trabajo local con el servidor

**Criterios de aceptación:**

- [ ] Autenticación requerida para push.
- [ ] Validación de permisos según rol (owner/developer).
- [ ] Actualización correcta de branches y commits.
- [ ] Rechazo de pushes que violen reglas (ej. no fast-forward).

**Checklist de tareas:**

- [ ] Configurar recepción de pushes en backend.
- [ ] Implementar actualización de referencias Git.
- [ ] Registrar commits y cambios en base de datos.
- [ ] Manejar errores comunes (conflictos, falta de permisos).
- [ ] Probar flujo completo con Git local.

---

### HU-13: Navegación de archivos y carpetas

> **Como** usuario
> **Quiero** explorar la estructura de archivos y carpetas de un repositorio desde el navegador
> **Para** visualizar el contenido sin necesidad de clonar

**Criterios de aceptación:**

- [ ] Vista de árbol de directorios.
- [ ] Navegación por carpetas.
- [ ] Listado de archivos con íconos por tipo.
- [ ] Visualización del contenido de archivos de texto.

**Checklist de tareas:**

- [ ] Crear endpoint `GET /api/repos/:repoId/contents?path=...`.
- [ ] Leer estructura desde el repositorio Git.
- [ ] Renderizar árbol de archivos en frontend.
- [ ] Implementar visualizador de texto con resaltado de sintaxis.
- [ ] Manejar archivos binarios con mensaje adecuado.

---

### HU-14: Subir archivos directamente desde la web

> **Como** usuario
> **Quiero** subir archivos nuevos a un repositorio sin usar Git
> **Para** agregar documentos rápidamente

**Criterios de aceptación:**

- [ ] Botón "Subir archivo" en vista del repositorio.
- [ ] Selector de archivo y opción de mensaje de commit.
- [ ] Commit automático en la rama actual.
- [ ] Actualización de la vista después de subir.

**Checklist de tareas:**

- [ ] Crear endpoint `POST /api/repos/:repoId/upload`.
- [ ] Recibir archivo y metadata (ruta, mensaje commit).
- [ ] Realizar commit en el repositorio Git.
- [ ] Manejar archivos grandes (hasta límite).
- [ ] Diseñar UI de subida con progreso.

---

### HU-15: Eliminar archivos desde la web

> **Como** usuario
> **Quiero** eliminar archivos de un repositorio desde el navegador
> **Para** remover contenido obsoleto

**Criterios de aceptación:**

- [ ] Botón de eliminar junto a cada archivo.
- [ ] Confirmación y mensaje de commit.
- [ ] Commit de eliminación.
- [ ] Actualización de la vista.

**Checklist de tareas:**

- [ ] Crear endpoint `DELETE /api/repos/:repoId/contents`.
- [ ] Validar ruta y existencia.
- [ ] Generar commit de eliminación.
- [ ] Agregar interfaz en frontend.
- [ ] Probar eliminación y restauración.

---

### HU-16: Descargar archivos del repositorio

> **Como** usuario
> **Quiero** descargar archivos individuales o el repositorio completo como ZIP
> **Para** obtener el contenido sin necesidad de usar Git

**Criterios de aceptación:**

- [ ] Botón "Descargar" en vista de archivo individual.
- [ ] Opción "Descargar ZIP" en página principal del repositorio.
- [ ] Descarga respeta la rama seleccionada.
- [ ] Archivos binarios se descargan correctamente.

**Checklist de tareas:**

- [ ] Crear endpoint `GET /api/repos/:repoId/download?path=...` para archivo individual.
- [ ] Crear endpoint `GET /api/repos/:repoId/archive?ref=branch` para ZIP completo.
- [ ] Generar archivo ZIP dinámicamente desde el repositorio Git.
- [ ] Agregar botones de descarga en frontend.
- [ ] Manejar archivos grandes con streaming.
- [ ] Probar descarga en diferentes navegadores.

---

### HU-17: Crear carpetas en el repositorio

> **Como** usuario
> **Quiero** crear carpetas nuevas en el repositorio desde la interfaz web
> **Para** organizar mi código sin usar Git

**Criterios de aceptación:**

- [ ] Botón "Nueva carpeta" en vista del repositorio.
- [ ] Formulario con nombre de carpeta y mensaje de commit.
- [ ] Validación de nombre (sin caracteres especiales).
- [ ] Commit automático con archivo placeholder (.gitkeep).
- [ ] Actualización de la vista tras crear.

**Checklist de tareas:**

- [ ] Crear endpoint `POST /api/repos/:repoId/folders`.
- [ ] Validar nombre de carpeta.
- [ ] Crear carpeta con archivo .gitkeep (Git no permite carpetas vacías).
- [ ] Generar commit automático.
- [ ] Diseñar modal de creación en frontend.
- [ ] Manejar errores (carpeta existente, permisos).

---

### HU-18: Ver historial de commits

> **Como** usuario
> **Quiero** ver el historial de commits de un repositorio con fecha, autor y mensaje
> **Para** entender la evolución del código

**Criterios de aceptación:**

- [ ] Página de historial de commits accesible desde el repositorio.
- [ ] Lista paginada de commits con: hash, autor, fecha, mensaje.
- [ ] Filtro por rama.
- [ ] Enlace para ver el diff de cada commit.
- [ ] Avatar del autor junto al commit.

**Checklist de tareas:**

- [ ] Crear endpoint `GET /api/repos/:repoId/commits?branch=...&page=...`.
- [ ] Obtener commits desde el repositorio Git.
- [ ] Implementar paginación.
- [ ] Crear endpoint `GET /api/repos/:repoId/commits/:sha` para detalle.
- [ ] Diseñar vista de historial en frontend.
- [ ] Mostrar diff de cada commit al hacer clic.
- [ ] Integrar avatares de usuarios.

---

### HU-19: Gestión de branches

> **Como** usuario
> **Quiero** ver, crear y cambiar entre branches
> **Para** organizar mi trabajo en paralelo

**Criterios de aceptación:**

- [ ] Listado de branches.
- [ ] Crear nueva branch desde otra existente.
- [ ] Cambiar branch activa (para navegación).
- [ ] Eliminar branch (si no es default).

**Checklist de tareas:**

- [ ] Endpoint `GET /api/repos/:repoId/branches`.
- [ ] Endpoint `POST /api/repos/:repoId/branches` para crear.
- [ ] Endpoint `DELETE /api/repos/:repoId/branches/:branch` para eliminar.
- [ ] UI de selector de branch en frontend.
- [ ] Actualizar navegación según branch seleccionada.

---

## Épica 4: Colaboración

### HU-20: Gestión de colaboradores con roles

> **Como** owner de un repositorio
> **Quiero** invitar a otros usuarios con roles específicos (Developer, Reporter)
> **Para** controlar quién puede escribir o solo leer

**Criterios de aceptación:**

- [ ] Búsqueda de usuarios por email/username.
- [ ] Asignación de rol: Owner, Developer, Reporter.
- [ ] Permisos por rol:
  - **Owner:** acceso total.
  - **Developer:** subir archivos, crear issues, comentar.
  - **Reporter:** solo lectura.
- [ ] Listado de colaboradores.

**Checklist de tareas:**

- [ ] Endpoint `GET /api/repos/:repoId/collaborators`.
- [ ] Endpoint `POST /api/repos/:repoId/collaborators` para invitar.
- [ ] Endpoint `PATCH /api/repos/:repoId/collaborators/:userId` para cambiar rol.
- [ ] Middleware de autorización basado en rol.
- [ ] UI de gestión de colaboradores.

---

### HU-21: Dar estrella a repositorios

> **Como** usuario
> **Quiero** marcar repositorios como favoritos
> **Para** seguirlos o destacarlos

**Criterios de aceptación:**

- [ ] Botón de estrella en página del repo.
- [ ] Contador de estrellas.
- [ ] Lista de repositorios destacados en perfil.

**Checklist de tareas:**

- [ ] Endpoint `POST /api/repos/:repoId/star`.
- [ ] Endpoint `DELETE /api/repos/:repoId/star`.
- [ ] Contar estrellas en entidad repositorio.
- [ ] UI con estado activo/inactivo.
- [ ] Lista de repositorios marcados en dashboard.

---

## Épica 5: Búsqueda y Notificaciones

### HU-22: Buscar repositorios por nombre

> **Como** usuario
> **Quiero** buscar repositorios públicos por su nombre
> **Para** descubrir proyectos

**Criterios de aceptación:**

- [ ] Campo de búsqueda en navbar.
- [ ] Resultados paginados.
- [ ] Mostrar nombre, descripción, estrellas.
- [ ] Enlace a repositorio.

**Checklist de tareas:**

- [ ] Endpoint `GET /api/search/repositories?q=...`.
- [ ] Indexar nombres y descripciones.
- [ ] Implementar búsqueda case-insensitive.
- [ ] UI de resultados con ordenamiento.
- [ ] Manejar búsqueda vacía.

---

### HU-23: Buscar usuarios

> **Como** usuario
> **Quiero** buscar otros usuarios por nombre de usuario
> **Para** encontrar colaboradores

**Criterios de aceptación:**

- [ ] Búsqueda en navbar o página dedicada.
- [ ] Mostrar avatar, nombre, username.
- [ ] Enlace al perfil.

**Checklist de tareas:**

- [ ] Endpoint `GET /api/search/users?q=...`.
- [ ] Indexar usuarios.
- [ ] UI de resultados.
- [ ] Integrar con invitación a colaboradores.

---

### HU-24: Notificaciones por email

> **Como** usuario
> **Quiero** recibir correos cuando ocurran eventos clave (PR creado, revisión, merge)
> **Para** mantenerme informado sin estar en la plataforma

**Criterios de aceptación:**

- [ ] Configuración de preferencias de notificaciones.
- [ ] Envío de emails para:
  - PR creado donde soy reviewer o propietario.
  - Comentario en PR que sigo.
  - Merge completado.
  - Invitación a colaborador.
- [ ] Plantillas de email claras.

**Checklist de tareas:**

- [ ] Configurar servicio de emails.
- [ ] Escuchar eventos del sistema (event sourcing).
- [ ] Crear cola de envío para no bloquear.
- [ ] Diseñar plantillas HTML.
- [ ] Implementar configuración de preferencias por usuario.
- [ ] Pruebas de entrega.

---

## Épica 6: Documentación y Calidad

### HU-25: Documentación de API con Swagger

> **Como** desarrollador que integra con la plataforma
> **Quiero** tener una documentación interactiva de la API
> **Para** entender cómo consumir los endpoints

**Criterios de aceptación:**

- [ ] Swagger UI disponible en `/api-docs`.
- [ ] Todos los endpoints documentados con parámetros, respuestas, ejemplos.
- [ ] Autenticación JWT soportada en Swagger.

**Checklist de tareas:**

- [ ] Configurar Swagger (OpenAPI 3.0).
- [ ] Anotar todos los controladores con descripciones.
- [ ] Documentar esquemas de datos.
- [ ] Agregar botón de autorización para JWT.
- [ ] Validar que documentación esté actualizada.

---

### HU-26: Interfaz como Progressive Web App (PWA)

> **Como** usuario
> **Quiero** poder instalar la aplicación en mi dispositivo móvil
> **Para** acceder como si fuera una app nativa

**Criterios de aceptación:**

- [ ] `manifest.json` configurado.
- [ ] Service worker para caché básico.
- [ ] Funcionalidad offline limitada.
- [ ] Íconos y splash screen.

**Checklist de tareas:**

- [ ] Generar `manifest.json`.
- [ ] Registrar service worker.
- [ ] Cachear assets estáticos.
- [ ] Probar instalación en Android/iOS.
- [ ] Configurar estrategia de caché.

---

_26 historias de usuario · 6 épicas_
