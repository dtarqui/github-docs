# Inventario de imágenes — DevOps e IA (Mini-GitHub)

Estado: **todas las imágenes necesarias están disponibles** en `docs/devops_ia/latex/`.
Este archivo documenta qué contiene cada una (para sus pies de figura en capítulos/anexos).

---

## A. Capturas de la UI en PRODUCCIÓN (evidencia 1B — validación con datos reales)  ✅ disponibles

Producción: `http://github-front-zspshemrjzes-434214445.us-east-1.elb.amazonaws.com`

| Archivo | Qué muestra | Uso sugerido |
|---|---|---|
| `cap_clasificacion_issue.png` | Panel "Clasificación asistida por IA" con los chips `tipo` y `severidad` sugeridos al crear un issue | Anexo E / 09 Validación |
| `cap_resumen_commit.png` | Editor con el campo "Mensaje del commit" rellenado por el resumidor | Anexo E / 09 Validación |
| `cap_issues_labels.png` | Lista de issues con labels `tipo:*` / `severidad:*` aplicadas | Anexo E |

## B. Capturas de consolas / herramientas (evidencia DevOps)  ✅ disponibles

| Archivo | Qué muestra | Uso sugerido |
|---|---|---|
| `cap_swagger_ia.png` | Swagger de los servicios de IA (`/v1/classify`, `/v1/summarize`) | Anexo C |
| `cap_ecs_console.png` | Consola AWS ECS: servicios `github-ecs` en estado RUNNING (incl. los de IA) | Anexo C / D |
| `cap_airflow_dag.png` | Airflow: DAG con el quality gate y el deploy | Anexo D |

---

## C. Figuras generadas por Claude (números/estructura reales)  ✅ disponibles

| Archivo | Contenido | Capítulo |
|---|---|---|
| `fig_clasif_tipo.png` | Métricas por clase — clasificador de tipo (P/R/F1) | 09 |
| `fig_clasif_severidad.png` | Métricas por clase — clasificador de severidad | 09 |
| `fig_distribucion_clases.png` | Distribución/soporte de clases (desbalance) | 09 |
| `fig_resumidor_evolucion.png` | BLEU-4 y ROUGE-L: seq2seq → pointer-generator | 09 |
| `fig_resumidor_lenguaje.png` | BLEU-4 por lenguaje (multilenguaje v3) | 09 |
| `fig_arquitectura.png` | Arquitectura de microservicios (contenedores) | 08 |
| `fig_pipeline_mlops.png` | Pipeline MLOps (Airflow: gate + registry + deploy) | 08 |
| `fig_despliegue_ecs.png` | Despliegue en AWS ECS Fargate (CDK) | 08 |
| `fig_flujo_resumidor.png` | Sistema híbrido en cascada del resumidor | 08 |
| `ishikawa_issues_commits.png` | Diagrama de Ishikawa | Introducción |

---

> Nota: las matrices de confusión y la curva de entrenamiento (que se sugerían generar desde los
> notebooks) se retiraron de la lista por decisión del equipo; no se solicitan.
