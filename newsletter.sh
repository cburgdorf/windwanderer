#!/bin/sh

# Sends the newsletter for a blog post via Brevo.
# Usage: ./newsletter.sh --latest  or  ./newsletter.sh content/mein-artikel.md

cd "$(dirname "$0")" || exit 1
uv run scripts/send_newsletter.py "$@"
