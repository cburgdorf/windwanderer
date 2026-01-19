# Windwanderer Blog

Dieses Repository enthält den Quellcode für den Windwanderer Blog, basierend auf dem Static Site Generator [Zola](https://www.getzola.org/).

## Bilder optimieren

Um Bilder für das Web zu optimieren (Größe anpassen, Metadaten entfernen, Kompression), gibt es ein Hilfsskript im Ordner `scripts/`.

### Voraussetzungen

Das Skript benötigt Python 3 und die Bibliothek `Pillow`.
Falls noch nicht installiert, kann Pillow so installiert werden:

```bash
pip install Pillow
```

### Nutzung

Navigiere in das Hauptverzeichnis des Projekts und führe das Skript mit dem Pfad zum Bilderordner aus:

```bash
python3 scripts/optimize_images.py static/img/DEIN-ORDNER-NAME
```

Optional können die maximale Seitenlänge (Standard: 1600px) und die Qualität (Standard: 85) angepasst werden:

```bash
python3 scripts/optimize_images.py static/img/DEIN-ORDNER-NAME 1200 80
```

Das Skript überschreibt die Originaldateien im angegebenen Ordner mit den optimierten Versionen.
