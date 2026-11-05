---
title: 'Chécalo · Edición Codex'
---

# Chécalo

Entiende los riesgos antes de publicar. Esta guía te acompaña desde la preparación hasta el resultado y señala qué necesita comprobarse en tu entorno.

## Empieza por aquí: tres formas de instalar

Elige solo una opción. La instalación conserva la herramienta completa con sus referencias y scripts. Usa Codex en un entorno con acceso a archivos.

### 1. Copia un prompt con los enlaces · recomendado

Copia el bloque completo, pégalo en un chat nuevo de Codex y deja que prepare la instalación. La guía enlazada es pública en GitHub: no necesita iniciar sesión en el Bunker.

```text
Instala para mi usuario la edición Codex de Chécalo.

Skill: https://github.com/Alanmezaoficial/checalo/tree/main/codex/skills/checalo
Guía pública: https://github.com/Alanmezaoficial/checalo/blob/main/docs/guia-codex.md
Repositorio: https://github.com/Alanmezaoficial/checalo

Lee la guía y usa skill-installer si está disponible, indicando la ruta codex/skills/checalo y la carpeta personal de skills que detecta esta versión de Codex. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Comprueba que SKILL.md y todos sus recursos quedaron instalados. Indica la ruta final y cómo comprobar que aparece en el selector. No inicies un proyecto ni ejecutes la skill todavía. Si no tienes acceso a archivos o a GitHub, explica qué falta sin afirmar que la instalaste.
```

### 2. Descarga el ZIP y acompáñalo con este prompt

En la ficha de esta edición, pulsa Descargar ZIP. Adjunta el archivo a un chat de Codex o indica su ruta local si el host no admite ese adjunto; después pega el bloque. Descargar o adjuntar el archivo sin pedir la instalación no lo instala. Cada ZIP incluye INSTALAR.md con estas instrucciones.

```text
Instala para mi usuario la edición Codex de Chécalo que adjunto en el ZIP checalo-codex-1.0.1.zip.

Guía pública de apoyo: https://github.com/Alanmezaoficial/checalo/blob/main/docs/guia-codex.md

Localiza el ZIP adjunto o su archivo local accesible, revisa su estructura y extrae de forma segura la carpeta checalo. Copia esa carpeta completa a la ubicación personal de skills que detecta mi Codex. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Comprueba SKILL.md y la integridad de los archivos copiados, indica la ruta final y cómo comprobar el selector. No ejecutes la skill todavía. Si el ZIP no es accesible desde este chat, pídeme su ruta local; no uses una descarga de la edición Claude.
```

<details>
<summary>3. Prefiero instalar manualmente · Windows · PowerShell</summary>

Descarga el ZIP de esta edición. En Windows, abre PowerShell y pega el bloque completo. Busca el archivo en Descargas; si lo guardaste en otra carpeta, cambia solo zipPath. No necesita pedirle trabajo a una IA.

```powershell
$zipPath = Join-Path $env:USERPROFILE 'Downloads\checalo-codex-1.0.1.zip'
$skillsRoot = Join-Path $env:USERPROFILE '.agents\skills'
$destination = Join-Path $skillsRoot 'checalo'
if (!(Test-Path -LiteralPath $zipPath -PathType Leaf)) { throw 'No encuentro el ZIP en Descargas. Ajusta zipPath a su ubicación.' }
if (Test-Path -LiteralPath $destination) { throw 'La skill ya existe. Revisa su versión antes de actualizar.' }
$staging = Join-Path ([System.IO.Path]::GetTempPath()) ('manos-instalar-' + [guid]::NewGuid().ToString('N'))
Expand-Archive -LiteralPath $zipPath -DestinationPath $staging
$source = Join-Path $staging 'checalo'
if (!(Test-Path -LiteralPath (Join-Path $source 'SKILL.md') -PathType Leaf)) { throw 'El ZIP no tiene la estructura esperada.' }
New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null
Copy-Item -LiteralPath $source -Destination $destination -Recurse
foreach ($file in Get-ChildItem -LiteralPath $source -File -Recurse) {
  $relative = $file.FullName.Substring($source.Length + 1)
  $copy = Join-Path $destination $relative
  if ((Get-FileHash -LiteralPath $file.FullName).Hash -ne (Get-FileHash -LiteralPath $copy).Hash) { throw ('Copia distinta: ' + $relative) }
}
Write-Output ('Archivos instalados y comprobados en: ' + $destination)
```

</details>

### Confirma que quedó disponible

Abre el selector de skills en una sesión nueva y busca Chécalo. Si no aparece, reinicia Codex. Si la carpeta existe pero no aparece en el selector, informa de ambas cosas; no son la misma prueba.

Las secciones siguientes explican requisitos y alternativas con más detalle.

## Antes de instalar

Necesitas Codex con acceso al sistema de archivos del equipo y una carpeta de trabajo. La biblioteca está en el apartado ChatGPT, pero este paquete está preparado para Codex: descargarlo desde un teléfono no lo instala en tu computadora ni lo habilita en todas las modalidades de ChatGPT.

La skill utiliza las herramientas que estén disponibles en esa sesión. Python es necesario para los helpers incluidos; las tareas del proyecto pueden necesitar Node, Git u otro runtime. No se necesita una clave de API para leer estas instrucciones ni se incluye ninguna.

## Obtener desde GitHub

El [repositorio público](https://github.com/Alanmezaoficial/checalo) incluye ambas ediciones. Si tienes Git, puedes obtenerlo en una carpeta nueva:

```text
git clone https://github.com/Alanmezaoficial/checalo.git
cd checalo
```

También puedes descargar el ZIP desde **Code → Download ZIP** en GitHub. Antes de copiar, abre la raíz que contiene `claude/` y `codex/`.

## Instala una copia con nombre propio

Descomprime el repositorio preparado. Abre PowerShell en su raíz, donde están `claude/` y `codex/`. Este comando copia únicamente la skill nueva y se detiene si ya existe ese destino:

```powershell
$source = (Resolve-Path '.\codex\skills\checalo').Path
$destination = Join-Path $env:USERPROFILE '.agents\skills\checalo'
if (Test-Path -LiteralPath $destination) { throw 'El destino ya existe; revisa su versión antes de actualizar.' }
New-Item -ItemType Directory -Path (Split-Path -Parent $destination) -Force | Out-Null
Copy-Item -LiteralPath $source -Destination $destination -Recurse
```

Si descargaste el ZIP de la edición Codex en lugar del repositorio completo, su carpeta superior ya se llama `checalo`: copia esa carpeta completa a `.agents/skills` de tu usuario. Deben quedar `SKILL.md`, sus recursos y `agents/openai.yaml` dentro de ella. Conserva `LICENSE` y `NOTICE`. Las instalaciones anteriores con otros nombres pueden seguir presentes.

## Verifica antes de encargar trabajo

Comprueba que existe `$env:USERPROFILE\.agents\skills\checalo\SKILL.md`. Inicia una sesión nueva de Codex y selecciona la skill; en CLI/extensión puedes escribir `$checalo` o abrir `/skills`. Si no aparece, reinicia el host y revisa la carpeta: no debe haber un nivel adicional `checalo/checalo`.

La presencia del archivo comprueba la copia; verla en el selector comprueba descubrimiento; completar un encargo comprueba ese recorrido. Son verificaciones distintas. Nuestro registro separa extracción/copia verificadas de la activación en una sesión nueva, que queda pendiente si el host no se probó.

## Empieza por una carpeta concreta

Imagina que tienes una página lista para enseñar. Antes de compartirla, Chécalo puede revisar el código, los archivos de configuración y las dependencias disponibles, y ordenar lo que encuentre por prioridad.

```text
$checalo Audita esta carpeta local sin modificar el código. Explica el alcance, las herramientas utilizadas y lo que no puedas comprobar.
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
