#!/usr/bin/env -S pipx run
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Creates a Brevo email campaign for a blog post, sends a test email and,
after confirmation, sends the campaign to the newsletter list.
"""
import argparse
import base64
import glob
import html
import json
import os
import re
import sys
import tomllib
import unicodedata
import urllib.error
import urllib.request

BASE_URL = "https://windwanderer.xyz"
API_URL = "https://api.brevo.com/v3"
LIST_ID = 2
TEST_EMAIL = "christoph.burgdorf@gmail.com"
SENDER = {"name": "windwanderer", "email": "hello@windwanderer.xyz"}
MONTHS = ["Januar", "Februar", "März", "April", "Mai", "Juni",
          "Juli", "August", "September", "Oktober", "November", "Dezember"]


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def split_post(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    match = re.match(r"\+\+\+\n(.*?)\n\+\+\+\n(.*)", raw, re.S)
    if not match:
        sys.exit(f"Error: No TOML front matter found in {path}")
    return tomllib.loads(match.group(1)), match.group(2)


def read_front_matter(path):
    return split_post(path)[0]


def teaser_paragraphs(body):
    """Plain-text paragraphs of everything before <!-- more -->."""
    if "<!-- more -->" not in body:
        return []
    teaser = body.split("<!-- more -->")[0]
    teaser = re.sub(r"\{\{.*?\}\}", "", teaser, flags=re.S)        # shortcodes
    teaser = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", teaser)     # links and images
    teaser = re.sub(r"[*_`]+", "", teaser)                          # emphasis
    paragraphs = [" ".join(p.split()) for p in re.split(r"\n\s*\n", teaser)]
    return [p for p in paragraphs if p]


def find_latest_post():
    content_dir = os.path.join(os.path.dirname(__file__), "..", "content")
    posts = [
        (meta["date"], path)
        for path in glob.glob(os.path.join(content_dir, "*.md"))
        if not os.path.basename(path).startswith("_")
        and "date" in (meta := read_front_matter(path))
        and not meta.get("draft", False)
    ]
    if not posts:
        sys.exit("Error: No posts found.")
    return max(posts)[1]


def read_post(path):
    meta, body = split_post(path)
    extra = meta.get("extra", {})
    image = extra.get("social_img") or extra.get("header_img")
    if not image:
        sys.exit("Error: The post has no header_img or social_img.")
    slug = meta.get("slug") or slugify(os.path.splitext(os.path.basename(path))[0])
    return {
        "title": meta["title"],
        "date": meta.get("date"),
        "teaser": teaser_paragraphs(body),
        "url": f"{BASE_URL}/{slug}/",
        "image": BASE_URL + "/" + image.lstrip("/"),
    }


def check_online(url):
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request) as response:
            return response.status == 200
    except urllib.error.HTTPError:
        return False


def build_html(post):
    title = html.escape(post["title"])
    url = html.escape(post["url"])
    image = html.escape(post["image"])
    date = post["date"]
    eyebrow = "Neuer Blogartikel"
    if date:
        eyebrow += f" &middot; {date.day}. {MONTHS[date.month - 1]} {date.year}"
    preheader = html.escape(post["teaser"][0]) if post["teaser"] else ""

    accent = "#0085A1"
    serif = "font-family:Lora,Georgia,'Times New Roman',serif;"
    sans = "font-family:'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif;"
    teaser = "".join(
        f'<p style="{serif}margin:0 0 18px;font-size:18px;line-height:1.65;color:#333333;">{html.escape(p)}</p>'
        for p in post["teaser"]
    )
    small = f"{sans}margin:0;font-size:13px;line-height:1.6;color:#8a8f98;"

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css?family=Lora:400,700|Open+Sans:400,800" rel="stylesheet">
  <style>
    @media (max-width: 620px) {{
      .content {{ padding: 28px 22px 8px !important; }}
      .title {{ font-size: 26px !important; }}
    }}
  </style>
</head>
<body style="margin:0;padding:0;background-color:#f1f3f4;">
  <div style="display:none;max-height:0;overflow:hidden;opacity:0;">{preheader}</div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f1f3f4;">
    <tr><td align="center" style="padding:28px 12px;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">
        <tr><td align="center" style="padding:0 0 20px;">
          <a href="https://windwanderer.xyz/" style="{sans}font-size:14px;font-weight:800;letter-spacing:4px;text-transform:uppercase;color:#212529;text-decoration:none;">Wind Wanderer</a>
        </td></tr>
        <tr><td style="background-color:#ffffff;border-radius:10px;overflow:hidden;">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
            <tr><td>
              <a href="{url}"><img src="{image}" alt="{title}" width="600" style="display:block;width:100%;max-width:600px;height:auto;border:0;border-radius:10px 10px 0 0;"></a>
            </td></tr>
            <tr><td class="content" style="padding:36px 44px 12px;">
              <p style="{sans}margin:0 0 12px;font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:{accent};">{eyebrow}</p>
              <h1 class="title" style="{sans}margin:0 0 22px;font-size:30px;line-height:1.25;font-weight:800;color:#212529;">
                <a href="{url}" style="color:#212529;text-decoration:none;">{title}</a>
              </h1>
              {teaser}
            </td></tr>
            <tr><td align="center" style="padding:8px 44px 40px;">
              <table role="presentation" cellpadding="0" cellspacing="0"><tr>
                <td style="background-color:{accent};border-radius:6px;">
                  <a href="{url}" style="{sans}display:inline-block;padding:14px 34px;font-size:16px;font-weight:800;color:#ffffff;text-decoration:none;">Weiterlesen &rarr;</a>
                </td>
              </tr></table>
            </td></tr>
          </table>
        </td></tr>
        <tr><td align="center" style="padding:26px 20px 8px;">
          <p style="{serif}margin:0 0 18px;font-size:16px;font-style:italic;color:#555555;">Liebe Grüße von Bord,<br>Elvira, Christoph &amp; Eric</p>
          <p style="{small}">Du bekommst diese Mail an {{{{contact.EMAIL}}}}, weil du den Newsletter von <a href="https://windwanderer.xyz/" style="color:#8a8f98;">windwanderer.xyz</a> abonniert hast.</p>
          <p style="{small}margin-top:6px;"><a href="{{{{ unsubscribe }}}}" style="color:#8a8f98;text-decoration:underline;">Newsletter abbestellen</a></p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
"""


def resolve_api_key(key):
    """Accept a plain REST key (xkeysib-...) or an MCP key that wraps one in base64 JSON."""
    if key.startswith("xkeysib-"):
        return key
    try:
        decoded = json.loads(base64.b64decode(key + "=" * (-len(key) % 4)))
    except ValueError:
        return key
    if isinstance(decoded, dict):
        for value in decoded.values():
            if isinstance(value, str) and value.startswith("xkeysib-"):
                return value
    return key


def api(method, path, api_key, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request(
        API_URL + path,
        data=data,
        method=method,
        headers={"api-key": api_key, "accept": "application/json", "content-type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"Brevo API error ({method} {path}): {e.code} {e.read().decode()}")


def main():
    parser = argparse.ArgumentParser(description="Send the newsletter for a blog post via Brevo.")
    post_group = parser.add_mutually_exclusive_group(required=True)
    post_group.add_argument("post", nargs="?", help="Path to the post, e.g. content/mein-artikel.md")
    post_group.add_argument("--latest", action="store_true", help="Use the post with the most recent date")
    parser.add_argument("--test-email", default=TEST_EMAIL, help="Recipient of the test email")
    parser.add_argument("--dry-run", action="store_true", help="Only write the email HTML to newsletter-preview.html")
    args = parser.parse_args()

    post = read_post(find_latest_post() if args.latest else args.post)
    email_html = build_html(post)
    print(f"Titel: {post['title']}\nURL:   {post['url']}\nBild:  {post['image']}")

    if args.dry_run:
        with open("newsletter-preview.html", "w", encoding="utf-8") as f:
            f.write(email_html)
        print("Vorschau geschrieben: newsletter-preview.html")
        return

    api_key = os.environ.get("WINDWANDERER_BREVO_API_KEY", "").strip()
    if not api_key:
        sys.exit("Error: Please set WINDWANDERER_BREVO_API_KEY.")
    api_key = resolve_api_key(api_key)

    for url in (post["url"], post["image"]):
        if not check_online(url):
            sys.exit(f"Error: {url} is not online yet. Deploy the post first.")

    campaign = api("POST", "/emailCampaigns", api_key, {
        "name": f"Blogartikel: {post['title']}",
        "subject": f"Neuer Blogartikel: {post['title']}",
        "previewText": post["teaser"][0][:150] if post["teaser"] else "",
        "sender": SENDER,
        "htmlContent": email_html,
        "recipients": {"listIds": [LIST_ID]},
    })
    campaign_id = campaign["id"]
    print(f"Kampagne {campaign_id} angelegt.")

    api("POST", f"/emailCampaigns/{campaign_id}/sendTest", api_key, {"emailTo": [args.test_email]})
    print(f"Test-Mail an {args.test_email} verschickt.")

    try:
        answer = input(f"An alle Empfänger der Liste {LIST_ID} senden? (j/n) ")
    except EOFError:
        answer = ""
    if answer.strip().lower() != "j":
        print("Nicht gesendet. Die Kampagne liegt als Entwurf in Brevo.")
        return

    api("POST", f"/emailCampaigns/{campaign_id}/sendNow", api_key)
    print("Newsletter wird verschickt.")


if __name__ == "__main__":
    main()
