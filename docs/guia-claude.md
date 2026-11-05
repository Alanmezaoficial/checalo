---
title: 'Chécalo · Edición Claude'
---

# Chécalo

Entiende los riesgos antes de publicar. Esta guía te acompaña desde la preparación hasta el resultado y señala qué necesita comprobarse en tu entorno.

## Antes de instalar

La edición principal necesita **Claude Code**, no solo una conversación en claude.ai. Debes tenerlo instalado, autenticado y con acceso a la carpeta del proyecto. Las herramientas del proyecto y las CLIs de alojamiento se obtienen aparte cuando hagan falta. No hay credenciales ni cuentas incluidas.

Se conserva el flujo original de Claude y su resolución de recursos. En Súbelo, el original principal declara macOS/Linux y WSL2 para Windows. Un paquete que se puede descomprimir en Windows no demuestra que todos sus comandos POSIX funcionen en PowerShell.

## Instalar desde GitHub

El [repositorio público](https://github.com/Alanmezaoficial/checalo) contiene el catálogo y las dos ediciones. Dentro de una sesión de Claude Code:

```text
/plugin marketplace add Alanmezaoficial/checalo
/plugin install checalo@alanmeza-checalo
/plugin list
```

El nombre después de `@` corresponde al catálogo de este repositorio, distinto en cada skill. Instalarlo registra el plugin en tu entorno; comprueba después el comando indicado abajo y ejecuta un encargo pequeño. La publicación del repositorio no sustituye esa prueba del host.

## Prueba el plugin local

Descomprime el repositorio preparado y abre una terminal en su raíz. Para cargar el plugin solo durante esa sesión:

```text
claude --plugin-dir ./claude
```

Para registrarlo mediante su catálogo local:

```text
claude plugin validate .
claude plugin validate ./claude
claude plugin marketplace add .
claude plugin install checalo@alanmeza-checalo
claude plugin list
```

Los comandos de catálogo cambian la configuración local de Claude; ejecútalos cuando quieras instalar. No utilizan un repositorio público. Si descargaste solo el ZIP Claude, descomprímelo y usa `claude --plugin-dir` con su carpeta superior: el catálogo está en el repositorio completo.

## Comprueba qué se cargó

Abre el menú de skills/comandos y busca `/checalo:checalo`. El prefijo es el nombre del plugin. Si copias solo el `SKILL.md`, faltarán sus referencias; conserva la carpeta completa. No mezcles la instalación como plugin con una copia parcial en `~/.claude/skills`.

Validar el manifiesto, instalarlo y ejecutar un encargo son tres pasos diferentes. Los JSON/YAML y recursos de esta edición se revisan localmente; la instalación y el flujo conversacional en Claude Code o Cowork no se presentan como probados si no se abrió ese host.

## Empieza por una carpeta concreta

Imagina que tienes una página lista para enseñar. Antes de compartirla, Chécalo puede revisar el código, los archivos de configuración y las dependencias disponibles, y ordenar lo que encuentre por prioridad.

```text
/checalo:checalo Audita esta carpeta local sin modificar el código. Explica el alcance, las herramientas utilizadas y lo que no puedas comprobar.
```

Indica la ruta si no es la carpeta actual. Si trabajas en Windows y contiene espacios, escribe la ruta completa entre comillas. Nunca pegues contraseñas para que el auditor las «revise».

## Qué revisa

Tiene un flujo principal: reconocimiento, cinco carriles de análisis y consolidación del informe. Los carriles cubren dependencias, patrones de código, secretos, configuración/infraestructura y cadena de suministro/CI. Las 14 referencias ayudan a revisar lenguajes, autenticación, criptografía, logs y otros temas cuando aplican.

Semgrep, Trivy, Gitleaks y las herramientas de los gestores de paquetes son opcionales. Si no están disponibles, la revisión puede continuar con una cobertura distinta; el informe debe decir qué no se ejecutó. Una lectura manual de versiones no equivale a consultar una base de vulnerabilidades.

## Variantes reales

No hay una edición rápida o brownfield independiente. La cobertura se ajusta al tamaño del proyecto: completa en uno pequeño, dirigida en uno mediano y priorizada en uno muy grande. Esos niveles no son skills adicionales ni garantizan leer todos los archivos.

El escáner de secretos sí tiene opciones propias para su uso técnico:

```text
python scripts/scan_secrets.py --help
python scripts/scan_secrets.py "ruta al proyecto" --json
python scripts/scan_secrets.py "ruta al proyecto" --summary
python scripts/check_lockfiles.py "ruta al proyecto"
```

Ejecuta esos ejemplos desde la carpeta instalada de la skill y sustituye `python` por el intérprete disponible. En Windows puede ser `py -3` o una ruta absoluta. Son helpers: ejecutar ambos no equivale a completar los cinco carriles.

`--staged-only` revisa los archivos del índice Git de la carpeta actual. No instala un hook y no debe ejecutarse sobre otro repositorio por accidente. Con coincidencias normales el escáner termina con código 1; en staged puede terminar con 2. Lee el JSON antes de interpretar el código como avería.

## Qué te pedirá y qué entrega

Necesita la carpeta autorizada, exclusiones relevantes y el objetivo de la revisión. Detecta el stack y las herramientas disponibles. Entrega un Markdown con hallazgos ubicados, severidad, confianza, evidencia sin valores de credenciales, impacto, propuestas de corrección y límites de cobertura.

Claude conserva la ubicación de reporte en el Escritorio definida por su flujo; Codex usa `outputs/security` en el workspace. Si el Escritorio está redirigido por OneDrive, comprueba la ruta real. El informe no debe escribirse sobre un archivo existente sin resolver ese conflicto.

## Del informe a una corrección

Primero lee el impacto y las prioridades. Después puedes encargar una corrección explícita:

```text
Lee el informe de Chécalo. Corrige los hallazgos altos que afecten a esta página con cambios mínimos y vuelve a comprobarlos. Conserva los archivos y funciones ajenos al problema.
```

Esto es un nuevo encargo. La auditoría sola no edita código, instala paquetes ni ejecuta la aplicación. Un puntaje cero resume lo revisado y no certifica ausencia de vulnerabilidades.

## Diferencias entre ediciones

Claude mantiene la coordinación de sus cinco subagentes según el flujo original. Codex usa los recursos y la concurrencia realmente disponibles; puede trabajar por tandas o en la tarea principal. La nueva protección del escáner se aplica a ambas: informa tipo, archivo y línea sin emitir el resto de la línea, donde podría existir otra credencial.

## Problemas frecuentes

- **No se encuentra Python:** comprueba el intérprete antes de concluir que la skill falla. No hace falta instalar todos los escáneres externos para leer el código.
- **Hay muchas coincidencias de prueba:** revisa contexto y controles; una regex no confirma explotabilidad.
- **Falta el lockfile:** explica qué gestor usa el proyecto; no generes uno durante una auditoría de lectura.
- **Piden una clave de API para revisar:** estos helpers locales no necesitan una. Las herramientas externas tienen requisitos propios.

## Mantener esta edición

Antes de actualizar guarda una copia de tu carpeta instalada y de cualquier cambio propio. Revisa `upstream.lock.json`, `CHANGELOG.md` y `docs/actualizar-desde-original.md` en el repositorio preparado. Compara la siguiente revisión en otra carpeta; no uses un reemplazo completo para integrar cambios pequeños.

Actualiza solo la edición que utilizas. Comprueba referencias y extracción, vuelve a instalar en un destino aislado y después ejecuta un encargo representativo. Las actualizaciones de estas skills y las versiones del proyecto que estás construyendo son trabajos distintos.

## Autoría y comprobaciones

Adaptación y documentación de **Alanmeza.ai**, sobre los proyectos originales de **Enrique Rocha / Hainrixz** y, en Chécalo, **Cyber Neo Contributors**. Se conservan MIT, `LICENSE`, `NOTICE` y los avisos de procedencia. Consulta el registro de validación de esta edición para distinguir scripts probados, copia instalada y host conversacional pendiente.
