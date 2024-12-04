#!/bin/bash
# Fecha: 2024-12-04
# Nombre del archivo: auto_commit.sh
# Versión del archivo: V1

# Actualizar la versión en __manifest__.py
python3 update_manifest.py

# Añadir los cambios al índice de git
git add .

# Obtener la nueva versión del manifest
NEW_VERSION=$(grep "'version':" __manifest__.py | awk -F"'" '{print $4}')

# Commit de los cambios con el número de versión
git commit -m "Actualización de versión a $NEW_VERSION"

# Subir los cambios al repositorio
git push
