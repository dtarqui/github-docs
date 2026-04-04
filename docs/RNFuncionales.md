## Mini GitHub - Requerimientos No Funcionales

### Arquitectura y Diseño

| ID    | Requerimiento                                                     |
| ----- | ----------------------------------------------------------------- |
| RNF01 | El sistema debe implementar arquitectura de microservicios.       |
| RNF02 | Cada microservicio debe tener su propia base de datos.            |
| RNF03 | Los servicios deben comunicarse mediante API REST y/o mensajería. |

### Contenedorización y Orquestación

| ID    | Requerimiento                                              |
| ----- | ---------------------------------------------------------- |
| RNF04 | Todos los servicios deben estar contenedorizados.          |
| RNF05 | El sistema debe usar Docker Compose para desarrollo local. |
| RNF06 | El sistema debe poder desplegarse en Kubernetes.           |

### Cloud y Despliegue

| ID    | Requerimiento                                                   |
| ----- | --------------------------------------------------------------- |
| RNF07 | El sistema debe desplegarse en un proveedor cloud.              |
| RNF08 | No se implementará pipeline CI/CD como parte del producto (workflows, runners ni ejecución de jobs en contenedores; coherente con L-01). El despliegue puede ser manual o con herramientas externas al alcance funcional. |
| RNF09 | El sistema debe tener configuración por variables de entorno.   |

### Rendimiento y Escalabilidad

| ID    | Requerimiento                                                |
| ----- | ------------------------------------------------------------ |
| RNF10 | El API Gateway debe responder en menos de 100ms.             |
| RNF11 | Los servicios deben poder escalar horizontalmente.           |
| RNF12 | El sistema debe soportar al menos 100 usuarios concurrentes. |

### Seguridad

| ID    | Requerimiento                                                 |
| ----- | ------------------------------------------------------------- |
| RNF13 | Todas las comunicaciones externas deben usar HTTPS (TLS 1.3). |
| RNF14 | La autenticación debe usar JWT con expiración.                |
| RNF15 | Las contraseñas deben almacenarse hasheadas.                  |
| RNF16 | Tokens de acceso con scopes y RBAC por repositorio.           |
| RNF17 | Cifrado en reposo (AES-256) y en tránsito.                    |
| RNF18 | Aislamiento total entre repositorios privados.                |

### Usabilidad

| ID    | Requerimiento                                   |
| ----- | ----------------------------------------------- |
| RNF19 | Diseño responsivo y accesible.                  |
| RNF20 | Interfaz funcional en navegadores web modernos. |

### Observabilidad y Mantenibilidad

| ID    | Requerimiento                                              |
| ----- | ---------------------------------------------------------- |
| RNF21 | El sistema debe tener logging centralizado y estructurado. |
| RNF22 | El sistema debe exponer métricas de salud (health checks). |
| RNF23 | Monitoreo con Prometheus/Grafana.                          |
| RNF24 | Infraestructura como código (Terraform/Kubernetes).        |
| RNF25 | Despliegues automatizados con rollback.                    |
| RNF26 | Ambientes de staging y producción separados.               |

---
