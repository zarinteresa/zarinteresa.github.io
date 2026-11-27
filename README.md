# zarinteresa.github.io

Personal website of Zarin Sabah Teresa. Plain HTML/CSS/JS served by GitHub Pages.

- `src/pages/*.html` – page content (home, projects, courses, cv). **Edit these.**
- `tools/build.py` – stamps the shared header, meta tags and JSON-LD onto each page and writes
  `index.html`, `projects/`, `courses/`, `cv/`, `404.html` and `sitemap.xml`. Run `python3 tools/build.py`
  after any edit, and commit the generated files.
- `assets/` – CSS, JS (theme toggle, avatar effect, redirect for old `#/` links), images, CV PDF.
- `.nojekyll` – serve files as-is.

Preview locally: `python3 -m http.server` then open http://localhost:8000
