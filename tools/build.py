#!/usr/bin/env python3
"""Build the static pages from src/. No dependencies.

Edit page content in src/pages/*.html, page titles/descriptions in PAGES below,
then run:  python3 tools/build.py
It writes index.html, projects/index.html, courses/index.html, cv/index.html,
404.html and sitemap.xml. Commit the generated files: GitHub Pages serves them as-is.
"""
import datetime
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://zarinteresa.github.io"
NAME = "Zarin Sabah Teresa"
TODAY = datetime.date.today().isoformat()

PAGES = [
    # (key, url path, output file, <title>, meta description)
    ("home", "/", "index.html",
     f"{NAME} | ICT graduate, HCI and health informatics",
     f"{NAME}: B.Sc. in ICT, Jahangirnagar University. Interested in HCI, digital mental health, "
     "women-centered computing and health informatics."),
    ("projects", "/projects/", "projects/index.html",
     f"Projects and research plans | {NAME}",
     f"Projects and research plans by {NAME}: Angel Wing, a houseplant care app in development, "
     "and two research concepts in accessibility and privacy."),
    ("courses", "/courses/", "courses/index.html",
     f"Coursework | {NAME}",
     f"Undergraduate coursework of {NAME}, B.Sc. in Information and Communication Technology, "
     "Jahangirnagar University (2019 to 2024)."),
    ("cv", "/cv/", "cv/index.html",
     f"CV | {NAME}",
     f"CV of {NAME}: education, research on skin lesion analysis, projects, teaching, "
     "leadership and community service. Download the PDF."),
]
NAV = [("home", "/", "Home"), ("projects", "/projects/", "Projects"),
       ("courses", "/courses/", "Courses"), ("cv", "/cv/", "CV")]

PERSON = {
    "@context": "https://schema.org",
    "@type": "ProfilePage",
    "url": SITE + "/",
    "mainEntity": {
        "@type": "Person",
        "name": NAME,
        "url": SITE + "/",
        "image": SITE + "/assets/img/avatar.jpg",
        "description": "B.Sc. in Information and Communication Technology, Jahangirnagar University. "
                       "Interested in human-computer interaction and health informatics.",
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "Jahangirnagar University",
                     "url": "https://www.juniv.edu"},
        "knowsAbout": ["Human-Computer Interaction", "Digital Mental Health",
                       "Women-Centered Computing", "Health Informatics", "Mobile Health",
                       "Applied Machine Learning"],
        "sameAs": ["https://github.com/zarinteresa", "https://www.linkedin.com/in/zteresa"],
    },
}

HEAD = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="{name}">
  <meta name="google-site-verification" content="Z8w7jApubOW_Wm3F71XZFdB7NtA5iTuq6Iqc0Dke5SE">
  {robots}<link rel="canonical" href="{url}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="{name}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{site}/assets/img/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{name}: HCI and health informatics">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <script>
    try {{ var t = localStorage.getItem('theme'); if (t) document.documentElement.dataset.theme = t; }} catch (e) {{}}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap"></noscript>
  <link rel="stylesheet" href="/assets/css/style.css">
{jsonld}</head>
<body>
<main>
  <header class="profile">
    <div class="avatar" id="avatar">
      <span class="ring ring--yellow"></span>
      <span class="ring ring--pink"></span>
      <span class="ring ring--blue"></span>
      <img src="/assets/img/avatar-360.jpg" alt="Portrait of {name}" width="180" height="180">
    </div>
    {name_tag}
    <p class="affil">B.Sc. in Information and Communication Technology<br>Jahangirnagar University</p>
    <nav class="icons" aria-label="Social links">
      <a href="mailto:zarin.teresa10@gmail.com" aria-label="Email"><svg viewBox="0 0 24 24"><path d="M3 5h18v14H3z M3 6l9 7 9-7"/></svg></a>
      <a href="https://github.com/zarinteresa" aria-label="GitHub" target="_blank" rel="noopener"><svg viewBox="0 0 24 24"><path d="M9 19c-4 1.5-4-2-6-2m12 4v-3.5a3 3 0 0 0-.8-2.3c2.800-.3 5.800-1.400 5.800-6.200a4.800 4.800 0 0 0-1.300-3.300 4.500 4.500 0 0 0-.1-3.300s-1.100-.3-3.500 1.300a12 12 0 0 0-6.200 0C6.500 2.800 5.400 3.100 5.400 3.100a4.500 4.500 0 0 0-.1 3.300A4.800 4.800 0 0 0 4 9.700c0 4.800 3 5.900 5.800 6.200a3 3 0 0 0-.8 2.300V21"/></svg></a>
      <a href="https://www.linkedin.com/in/zteresa" aria-label="LinkedIn" target="_blank" rel="noopener"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z M2 9h4v12H2z M4 2a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"/></svg></a>
    </nav>
    <nav aria-label="Site">
      <ul class="nav">
{nav}
        <li><button id="theme-toggle" type="button" aria-label="Toggle dark mode">◐</button></li>
      </ul>
    </nav>
  </header>

  <div class="content">
    <section id="{key}" class="page">
{body}
    </section>
  </div>
  <footer>© {year} {name}</footer>
</main>
<script src="/assets/js/main.js"></script>
</body>
</html>
"""


def render(key, path, title, desc, body, robots=""):
    active = ' class="active" aria-current="page"'
    nav = "\n".join(
        f'        <li><a href="{href}"{active if k == key else ""}>{label}</a></li>'
        for k, href, label in NAV)
    jsonld = ""
    if key == "home":
        jsonld = ('  <script type="application/ld+json">\n'
                  + json.dumps(PERSON, indent=2, ensure_ascii=False) + "\n  </script>\n")
    name_tag = f"<h1>{NAME}</h1>" if key == "home" else f'<p class="name">{NAME}</p>'
    body = "\n".join(("      " + line) if line.strip() else "" for line in body.rstrip().split("\n"))
    return HEAD.format(title=html.escape(title), desc=html.escape(desc), name=NAME, site=SITE,
                       url=SITE + path, og_type="profile" if key == "home" else "website",
                       robots=robots, jsonld=jsonld, name_tag=name_tag, nav=nav, key=key,
                       body=body, year=datetime.date.today().year)


def main():
    for key, path, out, title, desc in PAGES:
        body = (ROOT / "src/pages" / f"{key}.html").read_text()
        target = ROOT / out
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(key, path, title, desc, body))
        print("wrote", out)

    notfound = ('<h1 class="page-title">Page not found</h1>\n'
                '<p>This page doesn\'t exist. Go to the <a href="/">home page</a>.</p>')
    (ROOT / "404.html").write_text(render(
        "404", "/404.html", f"Page not found | {NAME}", f"Page not found on {NAME}'s website.",
        notfound, robots='<meta name="robots" content="noindex">\n  '))
    print("wrote 404.html")

    urls = [SITE + p for _, p, *_ in PAGES] + [SITE + "/assets/Zarin_Sabah_Teresa_CV.pdf"]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sitemap += [f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls]
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    main()
