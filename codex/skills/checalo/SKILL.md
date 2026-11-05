---
name: checalo
description: Audita defensivamente la seguridad de un proyecto local autorizado y genera un reporte priorizado, sin modificar el código. Revisa dependencias, patrones SAST, secretos, autenticación, criptografía, configuración, infraestructura, supply chain y CI/CD. Úsala cuando el usuario pida auditoría de seguridad, buscar vulnerabilidades o revisar un proyecto antes de publicarlo. No la uses para atacar sistemas remotos, explotar vulnerabilidades ni corregir archivos sin una petición posterior explícita.
---

# Chécalo para Codex

Realiza una auditoría defensiva, basada en evidencia, del código que el usuario puso en alcance. Esta adaptación conserva el proyecto MIT de Hainrixz; consulta [LICENSE](LICENSE).

## Contrato de seguridad

- Solo audita proyectos locales o repositorios expresamente autorizados por el usuario.
- Mantén el proyecto objetivo en modo lectura. No edites, borres, instales paquetes ni ejecutes la aplicación.
- No ejecutes exploits, fuzzing agresivo, escaneos de red ni pruebas contra producción.
- No ejecutes variantes con `--fix` ni herramientas que actualicen lockfiles.
- Nunca reproduzcas valores de secretos. Redacta como `abcd…wxyz` o informa solo tipo, archivo y línea.
- La única escritura permitida es el reporte en `./outputs/security/` del workspace activo.
- Una auditoría puntual no demuestra ausencia de vulnerabilidades. Declara cobertura y limitaciones.

## Entrada y reconocimiento

Resuelve la ruta indicada por el usuario o usa el directorio actual. Confirma que existe y calcula la raíz absoluta.

1. Detecta lenguajes, frameworks, gestores de paquetes, Docker/IaC y CI/CD por archivos manifiesto.
2. Cuenta archivos excluyendo `.git`, dependencias, caches y artefactos generados.
3. Clasifica cobertura: completa (<1.000 archivos), dirigida (1.000–10.000) o rutas críticas (>10.000).
4. Descubre herramientas opcionales sin instalarlas: Semgrep, Trivy, Gitleaks, `npm audit`, `pip-audit`, `cargo audit`.
5. En Windows usa `Get-Command` o `where.exe` y el intérprete Python disponible; en macOS/Linux usa `command -v`. No asumas que existe `python3`.

Antes del análisis, informa stack, tamaño, cobertura planeada y herramientas disponibles.

## Referencias

Carga solo las que apliquen:

- Siempre: [OWASP](references/owasp-top-10.md), [CWE](references/cwe-top-25.md), [secretos](references/secrets-patterns.md), [criptografía](references/crypto-patterns.md), [errores](references/error-handling-patterns.md), [logging](references/logging-patterns.md) y [plantilla](references/report-template.md).
- JavaScript/TypeScript: [lang-javascript.md](references/lang-javascript.md).
- Python: [lang-python.md](references/lang-python.md).
- Web/auth: [web-security-patterns.md](references/web-security-patterns.md) y [auth-authz-patterns.md](references/auth-authz-patterns.md).
- Docker/IaC: [iac-docker.md](references/iac-docker.md).
- CI/CD: [cicd-security.md](references/cicd-security.md).
- Dependencias: [supply-chain.md](references/supply-chain.md).

## Cinco carriles de análisis

Ejecuta los cinco. Para repositorios medianos o grandes, usa subagentes de colaboración cuando estén disponibles porque los carriles son independientes. Respeta el límite real de concurrencia: reparte cinco carriles entre los subagentes disponibles y la tarea principal, o ejecútalos por tandas. Todos reciben la ruta absoluta, alcance, exclusiones y el contrato de solo lectura.

1. **SCA:** vulnerabilidades de dependencias mediante herramientas disponibles. Si una herramienta necesita red, solicita el permiso correspondiente. Registra CVE/advisory, paquete, versión afectada y versión corregida.
2. **SAST:** inyección SQL/comandos/código, XSS, SSRF, traversal, deserialización, redirecciones, validación de entrada y controles cercanos. Verifica contexto para reducir falsos positivos.
3. **Secretos y auth:** ejecuta [scripts/scan_secrets.py](scripts/scan_secrets.py), revisa `.gitignore`, sesiones, cookies, JWT, autorización por objeto/tenant y rutas administrativas. No incluyas los valores encontrados.
4. **Configuración e infraestructura:** cabeceras, CORS/CSP, debug, errores, Docker, IaC, permisos, exposición de puertos, logs y observabilidad.
5. **Supply chain y CI/CD:** ejecuta [scripts/check_lockfiles.py](scripts/check_lockfiles.py); revisa lockfiles, pinning, registries, acciones sin SHA, permisos del pipeline, eventos peligrosos y manejo de secretos.

No presentes coincidencias de regex como vulnerabilidades confirmadas: lee de 5 a 10 líneas de contexto y busca controles compensatorios.

## Formato de hallazgos

Cada hallazgo debe incluir:

- ID `CN-###`, severidad y confianza;
- CWE y OWASP cuando apliquen;
- ruta relativa y línea exacta;
- evidencia mínima, con secretos redactados;
- impacto y escenario de abuso realista;
- corrección específica y prueba de regresión sugerida;
- fuente de la evidencia: herramienta o revisión manual.

Severidad:

- Critical: RCE, bypass de autenticación, secreto productivo confirmado o exploit activo.
- High: inyección explotable, escalada de privilegios o CVE grave alcanzable.
- Medium: exposición condicionada, configuración débil o defensa faltante con impacto limitado.
- Low/Info: endurecimiento o riesgo de baja explotabilidad.

Usa el puntaje de riesgo del upstream solo como resumen heurístico: `min(100, critical*25 + high*10 + medium*3 + low)`. No lo presentes como CVSS.

## Reporte y salida

Fusiona y deduplica por archivo, línea y CWE; conserva la mayor severidad y enriquece la evidencia. Escribe:

`./outputs/security/checalo-report-<proyecto>-<AAAA-MM-DD>.md`

El reporte debe incluir resumen ejecutivo, conteos, tres prioridades, hallazgos por severidad, dependencias, supply chain, cobertura, archivos omitidos, herramientas usadas, duración y limitaciones. Si no hay hallazgos, enumera qué se comprobó.

Al entregar, muestra la ruta absoluta, el riesgo, los tres hallazgos principales y qué no pudo verificarse. No corrijas nada hasta que el usuario lo pida. Si pide remediación, aplica cambios mínimos con pruebas, empezando por Critical y High, y vuelve a ejecutar la auditoría relevante.

## Compatibilidad del ejecutor

Esta edición dirige a Codex con las herramientas expuestas en la sesión. Los nombres de capacidades heredados en ejemplos no registran APIs ni permisos de Claude. Para datos de OpenAI consulta OpenAI Docs; para Anthropic u otro proveedor consulta sus fuentes oficiales, sin cambiar el proveedor elegido por el proyecto. La documentación técnica con fecha es una caché histórica: verifica los datos cambiantes antes de usarlos.
