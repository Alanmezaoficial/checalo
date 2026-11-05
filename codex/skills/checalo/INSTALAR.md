# Instalar Chécalo · Codex

Esta carpeta contiene la herramienta completa, sin resumir sus instrucciones. Usa una de las siguientes opciones. Necesitas Codex con acceso a los archivos de tu equipo; adjuntar un ZIP a una conversación sin ese acceso no lo instala.

## 1. Pedir la instalación desde los enlaces

Copia este prompt en un chat nuevo de Codex:

```text
Instala para mi usuario la edición Codex de Chécalo.

Skill: https://github.com/Alanmezaoficial/checalo/tree/main/codex/skills/checalo
Guía pública: https://github.com/Alanmezaoficial/checalo/blob/main/docs/guia-codex.md
Repositorio: https://github.com/Alanmezaoficial/checalo

Lee la guía y usa skill-installer si está disponible, indicando la ruta codex/skills/checalo y la carpeta personal de skills que detecta esta versión de Codex. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Comprueba que SKILL.md y todos sus recursos quedaron instalados. Indica la ruta final y cómo comprobar que aparece en el selector. No inicies un proyecto ni ejecutes la skill todavía. Si no tienes acceso a archivos o a GitHub, explica qué falta sin afirmar que la instalaste.
```

## 2. Usar el ZIP descargado

Adjunta el ZIP o señala su ruta local y pega este prompt:

```text
Instala para mi usuario la edición Codex de Chécalo que adjunto en el ZIP checalo-codex-1.0.1.zip.

Guía pública de apoyo: https://github.com/Alanmezaoficial/checalo/blob/main/docs/guia-codex.md

Localiza el ZIP adjunto o su archivo local accesible, revisa su estructura y extrae de forma segura la carpeta checalo. Copia esa carpeta completa a la ubicación personal de skills que detecta mi Codex. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Comprueba SKILL.md y la integridad de los archivos copiados, indica la ruta final y cómo comprobar el selector. No ejecutes la skill todavía. Si el ZIP no es accesible desde este chat, pídeme su ruta local; no uses una descarga de la edición Claude.
```

## 3. Instalar manualmente

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

## Comprobar el resultado

La copia, la aparición en el selector y la ejecución de un encargo son pruebas distintas. Comprueba el selector o la lista de plugins antes de usarla. Guía pública: https://github.com/Alanmezaoficial/checalo/blob/main/docs/guia-codex.md

Se conservan LICENSE, NOTICE y la autoría original. La instalación no autoriza ejecutar proyectos ni publicar servicios.
