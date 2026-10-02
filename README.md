# Windwanderer Blog

Dieses Repository enthält den Quellcode für den Windwanderer Blog, basierend auf dem Static Site Generator [Zola](https://www.getzola.org/).

## Bilder optimieren

Um Bilder für das Web zu optimieren (Größe anpassen, Metadaten entfernen, Kompression), gibt es ein Hilfsskript im Ordner `scripts/`.

### Voraussetzungen

Das Skript benötigt [uv](https://docs.astral.sh/uv/) (oder alternativ `pipx`). Die Abhängigkeit `Pillow` wird beim Ausführen automatisch installiert.

### Nutzung

Navigiere in das Hauptverzeichnis des Projekts und führe das Skript mit dem Pfad zum Bilderordner aus:

```bash
uv run scripts/optimize_images.py static/img/DEIN-ORDNER-NAME
```

Optional können die maximale Seitenlänge (Standard: 1600px) und die Qualität (Standard: 85) angepasst werden:

```bash
uv run scripts/optimize_images.py static/img/DEIN-ORDNER-NAME 1200 80
```

Das Skript überschreibt die Originaldateien im angegebenen Ordner mit den optimierten Versionen.

## Newsletter verschicken

Nachdem ein Artikel deployed ist, kann der zugehörige Newsletter direkt aus dem Terminal über [Brevo](https://www.brevo.com/) verschickt werden. Das Skript legt eine Kampagne mit Titel, Header-Bild und Link des Artikels an, schickt eine Test-Mail und versendet nach Bestätigung an die Newsletter-Liste (ID 2).

### Voraussetzungen

Ein Brevo API-Key (Brevo → *SMTP & API* → *API-Keys*), als Umgebungsvariable gesetzt:

```bash
export WINDWANDERER_BREVO_API_KEY=xkeysib-...
```

### Nutzung

```bash
./newsletter.sh content/DEIN-ARTIKEL.md

# oder automatisch den neuesten Artikel (nach Datum)
./newsletter.sh --latest
```

Die Test-Mail geht standardmäßig an `christoph.burgdorf@gmail.com` (muss ein Kontakt in Brevo sein), mit `--test-email` lässt sich eine andere Adresse angeben. Mit `--dry-run` wird nur die Mail als `newsletter-preview.html` erzeugt, ohne Brevo zu kontaktieren. Wird der Versand nicht bestätigt, bleibt die Kampagne als Entwurf in Brevo liegen.
