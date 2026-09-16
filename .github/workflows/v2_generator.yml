name: Generar Catálogos V2 Automáticamente

on:
  push:
    paths:
      - "API's/*.json" # Solo se ejecuta si modificaste los catálogos

jobs:
  minify-catalogs:
    runs-on: ubuntu-latest
    permissions:
      contents: write # Permiso para que el robot pueda guardar los V2

    steps:
      - name: Descargar el código
        uses: actions/checkout@v4

      - name: Instalar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Ejecutar el Script de Compresión
        run: |
          python scripts/minify_catalogs.py "API's/db.json" "API's/db_v2.json"
          python scripts/minify_catalogs.py "API's/dbseries2.json" "API's/dbseries_v2.json"
          python scripts/minify_catalogs.py "API's/anime.json" "API's/anime_v2.json"

      - name: Subir (Commit) los archivos V2 generados
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "🤖 Auto-generados los catálogos V2 (Ultra-Ligeros)"
          file_pattern: "API's/*_v2.json"
