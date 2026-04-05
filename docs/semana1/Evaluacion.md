# Evaluación de Github - Diseño Técnico vs Rubrica Parte 1 (Reevaluación)

Fecha: 2026-04-05
Documento evaluado: [docs/semana1/Github - Diseño Técnico.md](docs/semana1/Github%20-%20Diseño%20Técnico.md)
Rúbrica base: [docs/semana1/Rubrica_Parte1.md](docs/semana1/Rubrica_Parte1.md)

## Resultado Ejecutivo

Estimación actual: 19.0 / 20 (sin penalizaciones).

Estado de la reevaluación:

- Documento de diseño fuerte y coherente con la rúbrica en secciones A y B.
- La única brecha de alto impacto sigue siendo evidencia verificable de Smithy en este workspace.

Mejoras verificadas en esta reevaluación:

- Se incorporó AuthN completo con flujo OIDC + PKCE y claims de token en [docs/semana1/Github - Diseño Técnico.md](docs/semana1/Github%20-%20Diseño%20Técnico.md#L464).
- Se incorporó AuthZ con RBAC y mapeo scopes -> operaciones en [docs/semana1/Github - Diseño Técnico.md](docs/semana1/Github%20-%20Diseño%20Técnico.md#L499).
- Se formalizó versionado REST en `/v1` en [docs/semana1/Github - Diseño Técnico.md](docs/semana1/Github%20-%20Diseño%20Técnico.md#L106).

Brecha principal restante para puntaje máximo:

- Evidencia verificable del modelo Smithy y ejecución de `smithy build` (C1).

## Falencias Actuales (Priorizadas)

1. Crítica: falta evidencia entregable de Smithy en este workspace.
- Evidencia: no se encontraron archivos `.smithy` en el workspace de documentación.
- Impacto: C1 puede bajar fuertemente si el evaluador no ve modelo + build funcionando.
- Qué falta: enlace/commit del repo `Github-Smithy` + evidencia de `smithy build` exitoso.

2. Media: C3 depende de evidencia en el modelo, no solo en documento.
- Evidencia documental existe en [docs/semana1/Github - Diseño Técnico.md](docs/semana1/Github%20-%20Diseño%20Técnico.md#L100), [docs/semana1/Github - Diseño Técnico.md](docs/semana1/Github%20-%20Diseño%20Técnico.md#L142) y [docs/semana1/Github - Diseño Técnico.md](docs/semana1/Github%20-%20Diseño%20Técnico.md#L518), pero la rúbrica pide traits/errores Smithy concretos.
- Impacto: si no se demuestra en `.smithy`, C3 puede bajar de Excelente/Bueno a Suficiente.

3. Media-baja: trazabilidad de entregables externos aún no consolidada en un anexo de evidencias.
- Falta un bloque final con links directos a repo Smithy, comando build, captura/log y hash/commit.
- Impacto: riesgo de evaluación subjetiva por falta de evidencia rápida.

## Evaluación por Criterio (Estimación Actual)

### Sección A — Documento de Diseño (8 pts)

- A1 Requisitos funcionales: 2.0 / 2.0
- A2 Requisitos no funcionales: 2.0 / 2.0
- A3 Entidades y modelo de datos: 2.0 / 2.0
- A4 Alto nivel y diagramas: 2.0 / 2.0

Subtotal A: 8.0 / 8.0

### Sección B — AuthZ/AuthN (6 pts)

- B1 Flujo AuthN OIDC: 2.0 / 2.0
- B2 Modelo AuthZ: 2.0 / 2.0
- B3 Integración SSO y seguridad de tokens: 2.0 / 2.0

Subtotal B: 6.0 / 6.0

### Sección C — API REST con Smithy (6 pts)

- C1 Correctitud/completitud Smithy: 1.3 / 2.0 (brecha por evidencia local/build)
- C2 Diseño REST de recursos: 2.0 / 2.0
- C3 Seguridad y manejo de errores API: 1.7 / 2.0 (documentado, pero falta confirmación en modelo Smithy)

Subtotal C: 5.0 / 6.0

Total estimado: 19.0 / 20

Nota de confianza:

- Alta en A y B (evidencia completa en documento).
- Media en C por ausencia de artefacto Smithy en este workspace de evaluación.

## Qué Debemos Mejorar para Llegar a la Nota Máxima

1. Cerrar C1 con evidencia técnica completa
- Adjuntar referencia explícita al repositorio Smithy.
- Listar ubicación de recursos y operaciones principales.
- Incluir evidencia de `smithy build` sin errores (log o captura + fecha + commit).

2. Cerrar C3 con evidencia de seguridad/errores en Smithy
- Mostrar uso de `@httpBearerAuth` en el modelo.
- Mostrar estructuras de error (`@error("client")`, `@error("server")`) y códigos HTTP asociados.
- Mostrar al menos 2 traits de validación (`@required`, `@length`, `@pattern`, etc.).

3. Mejorar evaluabilidad (formato entrega)
- Agregar sección breve “Evidencias de cumplimiento de rúbrica” con links directos y commit IDs.

## Qué Falta (Concreto y Accionable)

- [ ] Link a repo `Github-Smithy` con commit/tag de la entrega.
- [ ] Evidencia de `smithy build` exitoso (texto o captura).
- [ ] Tabla corta de operaciones Smithy por recurso (Auth, Repo, Issue, Search).
- [ ] Evidencia de traits de seguridad/validación/errores en el modelo.
- [ ] Verificación final de que no hay secretos en repositorios entregados.

## Plan de Cierre para 20/20

1. Subir evidencia Smithy (30-45 min).
2. Añadir anexo de evidencias al documento (15-20 min).
3. Hacer revisión cruzada final con checklist de rúbrica (15 min).

## Veredicto de Reevaluación

El documento está técnicamente fuerte y listo para nota alta. La diferencia entre 19 y 20 depende de una sola condición: mostrar evidencia verificable del modelo Smithy y de `smithy build` exitoso en la entrega.

## Conclusión

El documento técnico está en nivel alto y ya cumple muy bien A y B. Para asegurar 20/20, solo falta cerrar la evidencia verificable del modelo Smithy y su build en la entrega final.
