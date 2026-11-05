# Instalar Chécalo · Claude Code

Esta carpeta contiene la herramienta completa, sin resumir sus instrucciones. Usa una de las siguientes opciones. Necesitas Claude Code con acceso a los archivos de tu equipo; adjuntar un ZIP a una conversación sin ese acceso no lo instala.

## 1. Pedir la instalación desde los enlaces

Copia este prompt en un chat nuevo de Claude Code:

```text
Instala para mi usuario la edición Claude Code de Chécalo como plugin completo.

Guía pública: https://github.com/Alanmezaoficial/checalo/blob/main/docs/guia-claude.md
Repositorio: https://github.com/Alanmezaoficial/checalo

Lee la guía. Si estás en Claude Code con acceso a mi equipo, registra el catálogo Alanmezaoficial/checalo e instala checalo@alanmeza-checalo con los comandos admitidos por mi versión. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Conserva también los comandos, agentes y el manifiesto del plugin. Verifica la instalación con la lista de plugins e indica cómo comprobar su activación en una sesión nueva. No ejecutes la skill todavía. Si estás en una conversación sin acceso al equipo o el host no admite este plugin, explica qué necesito sin simular una instalación.
```

## 2. Usar el ZIP descargado

Adjunta el ZIP o señala su ruta local y pega este prompt:

```text
Instala para mi usuario la edición Claude Code de Chécalo del ZIP adjunto checalo-claude-1.0.1.zip, como plugin completo.

Guía pública de apoyo: https://github.com/Alanmezaoficial/checalo/blob/main/docs/guia-claude.md

Localiza el ZIP o pide su ruta local si no puedes acceder al adjunto. Extrae de forma segura la carpeta checalo en una ubicación persistente y lee INSTALAR.md. Esta carpeta incluye .claude-plugin/plugin.json y su catálogo local .claude-plugin/marketplace.json, cuyo source es ./; registra ese catálogo local e instala checalo@alanmeza-checalo. Conserva la carpeta completa, sus scripts, referencias, plantillas, LICENSE y NOTICE. No sustituyas la herramienta por un resumen ni cambies su contenido. Si ya está instalada con ese nombre, detente y dime qué versión encontraste antes de reemplazarla.

Conserva comandos, agentes y recursos del plugin. Valida y consulta la lista de plugins, informa de la ruta y de la comprobación pendiente en una sesión nueva. No ejecutes la skill todavía. Si el host no es compatible o no tiene acceso al equipo, indícalo sin afirmar que quedó instalada.
```

## 3. Instalar manualmente

Con Claude Code instalado y autenticado, abre una terminal y pega estas tres líneas. El catálogo obtiene el plugin completo desde GitHub. No necesita pedirle trabajo a una IA.

```text
claude plugin marketplace add Alanmezaoficial/checalo
claude plugin install checalo@alanmeza-checalo
claude plugin list
```

## Comprobar el resultado

La copia, la aparición en el selector y la ejecución de un encargo son pruebas distintas. Comprueba el selector o la lista de plugins antes de usarla. Guía pública: https://github.com/Alanmezaoficial/checalo/blob/main/docs/guia-claude.md

Se conservan LICENSE, NOTICE y la autoría original. La instalación no autoriza ejecutar proyectos ni publicar servicios.
