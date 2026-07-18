# Apéndice E — Integración en el frontend

La plataforma consume ambos modelos desde el frontend (Next.js / React) mediante una capa de
servicio dedicada y dos componentes de interfaz, presentando las predicciones como **sugerencias
editables**.

## E.1 Capa de servicio (`ai.ts`)

Un módulo `src/lib/services/ai.ts` centraliza el acceso a los dos modelos. En el navegador usa
rutas relativas que el servidor de Next.js reenvía a los servicios (evitando CORS), y adjunta el
*token* JWT del usuario:

Tabla: Capa de servicio — funciones, endpoints y salidas de los modelos.

| Función | Endpoint (relativo) | Destino real | Salida |
|---|---|---|---|
| `classifyIssue(title, body)` | `POST /ai-classifier/v1/classify` | `:8095` | `{ tipo, severidad, confianza_tipo }` |
| `summarizeDiff(diff)` | `POST /ai-summarizer/v1/summarize` | `:8096` | `{ resumen }` |

Ante un servicio no disponible, la interfaz degrada con un mensaje de error sin romper el
formulario.

## E.2 Modelo 1 en la UI — clasificación de issues

En el formulario de creación de issue, un botón **"Sugerir tipo y severidad"** invoca
`classifyIssue`. El resultado se muestra como dos *chips* de color: el **tipo** (con su porcentaje
de confianza) y la **severidad**. Un botón **"Aplicar como labels"** convierte la sugerencia en
etiquetas `tipo:<x>` y `severidad:<y>` (creándolas en el repositorio si no existen). La sugerencia
es **editable**: el usuario puede quitar o cambiar las labels; la IA no modifica el título ni la
descripción.

## E.3 Modelo 2 en la UI — resumen de commit

En el editor de archivos, un botón **"Sugerir mensaje"** construye el *diff* del cambio, invoca
`summarizeDiff` y **rellena el campo del mensaje de commit** con el texto generado. El usuario
puede editarlo libremente antes de confirmar; el mensaje final se propaga al *commit* real.

## E.4 Configuración

Las URLs de los servicios de IA se inyectan por variables de entorno en tiempo de *build*
(`NEXT_PUBLIC_CLASSIFIER_API_URL` → `:8095`, `NEXT_PUBLIC_SUMMARIZER_API_URL` → `:8096`) y se
enrutan mediante *rewrites* de Next.js (`/ai-classifier/*`, `/ai-summarizer/*`). En despliegue,
el frontend alcanza los servicios de IA por Service Discovery dentro de la VPC.

*(Las capturas de estas pantallas en producción se incluyen en el Apéndice F.)*
