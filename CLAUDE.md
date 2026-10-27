# CLAUDE.md

## Who this is for
Zarin Sabah Teresa ("Teresa", she/her). B.Sc. in ICT, Institute of Information Technology, Jahangirnagar University (2019–2024, CGPA 3.76/4.00). Research done: deep learning for skin lesion classification and segmentation (undergraduate research project).

**Goal:** apply to graduate programs (MS/PhD), primarily in the USA but not limited to it.

**Deadline: December 15** (application materials).

## Current state / to-do
1. **Master CV** — draft first; every other document derives from it.
2. **2–3 R&D projects / project ideas** to present (portfolio + application talking points).
3. **Application writing:** SOP (statement of purpose), LOR (letters of recommendation — Teresa requests them; we can draft a recommender brief/bullet sheet, not forge letters), and writing samples.
4. **Online presence:** GitHub and LinkedIn are essentially empty — make them presentable (README profile, pinned repos, clean LinkedIn headline/About/Experience).
5. **Research motivation** — still undecided. Teresa is drawn to the "easier"/human-centered side of IT and **qualitative research** (e.g. HCI, social computing, user studies, digital health/accessibility). Brainstorm and narrow this down; don't assume a direction.

## Working rules
- **Never fabricate** experience, publications, grades, awards, or recommender statements. Only use facts Teresa has given or that are already in this repo; mark gaps as `TODO(Teresa): ...` and ask.
- Her research interest is tentative — present options with trade-offs, then let her choose.
- Tailor documents to US grad admissions conventions (1–2 page CV, 1–2 page SOP unless a program says otherwise, program-specific faculty fit).
- Keep drafts as plain Markdown in a `docs/` folder (e.g. `docs/cv.md`, `docs/sop.md`, `docs/projects.md`, `docs/research-motivation.md`); export to PDF/DOCX only when asked.

## Portfolio website (this repo)
Plain static site, no build step, deployed by GitHub Pages from `master`.
- `index.html` — all content; Home and Courses views, hash-routed (`#/home`, `#/projects`, `#/courses`)
- `assets/css/style.css` — light/dark themes via CSS variables
- `assets/js/main.js` — theme toggle, routing, avatar hover effect
- Preview: `python3 -m http.server` → http://localhost:8000
- Keep it dependency-free. The Projects page currently holds three **concept** projects (labeled "Concept", not built — see `docs/projects.md`); never present them as completed work or add results/metrics. Publications only with real content.
- Active branch for the rewrite: `refactor-static` (not yet merged to `master`).

## Commands
- Run Claude Code without permission prompts: `claude --dangerously-skip-permissions` (also noted in `claude-important-commands.txt`)
