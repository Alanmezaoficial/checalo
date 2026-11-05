# Actualizar Chécalo desde su fuente

1. Lee `upstream.lock.json` y obtén el siguiente commit original en una carpeta distinta.
2. Compara con la base fijada, no con una carpeta instalada modificada a mano.
3. Claude integra procedimientos compatibles del original y adapta nombres/rutas. Codex conserva su base y aplica solo mejoras compatibles; no hereda variables, permisos ni herramientas exclusivas de Claude.
4. Mantén avisos actuales e históricos. Registra cada cambio propio y cualquier comportamiento que difiera.
5. Ejecuta las pruebas del paquete, referencias, validación de metadatos y extracción. En Súbelo ejecuta también `scripts/sync_cowork_plugin.py --check`.
6. Prueba instalación en una carpeta nueva. Comprueba el selector y un encargo real en el host disponible; los hosts no ejecutados siguen pendientes.
7. Registra el nuevo SHA original y versión derivada. Guarda respaldo de cambios propios antes de actualizar tu copia instalada. No actualices las instalaciones anteriores con otros nombres.

No se hace `git pull` sobre una instalación para intentar resolver conflictos automáticamente. El paquete se publica solo después de revisar sus archivos y el destino.
