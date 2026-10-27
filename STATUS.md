# STATUS — When AI Gets It Wrong

Built: 2026-10-27 · Owner: Asdale Dynamics, LLC

## What was built

A complete beginner's manual for verifying AI answers calmly — delivered
as readable Markdown and a self-contained static HTML site. Warm,
plain-English, local-first, no jargon, no fear.

- **`docs/` — 12 Markdown pages (the source of truth):**
  - `index.md` — start-here intro ("confident is not the same as
    correct"), the verify-before-you-trust calm promise, the route
    table, and the companion rules vs. *The Spot Fake Media Guide*
    (media side there) and *The AI Scam Safety Guide* (money side
    there) — cross-referenced by name, never re-taught.
  - `01` why models hallucinate: prediction-not-lookup in plain
    English, the trained-in helpfulness reflex, and four gap types
    (knowledge, freshness, precision, source) plus sycophancy.
  - `02` the mistake taxonomy: a twelve-row table (fabricated fact,
    stale fact, numeric slip, invented citation, mangled quote, entity
    confusion, overreach, sycophantic flip, scope error, procedure
    drift, missing "I don't know", compounding) with what each looks
    like, why it happens, and its cheap catch, plus a high/low-risk
    table.
  - `03` high-stakes vs. low-stakes asks — the one-question stakes test
    ("who pays if wrong?"), a four-row sort with real examples, and the
    common gray zones resolved.
  - `04` the verify-before-you-trust habit: load-bearing details, the
    four-step loop (assign row → isolate → check by type → trust
    forward), the two fastest checks, and what the habit is *not*.
  - `05` cross-checking with real sources: the evidence ranking
    (primary source down), the five targeted checks (landing page,
    exact-quote search, own arithmetic, trust the screen, date
    labels), the three-source bar, and the dead-link caution.
  - `06` a second local opinion: why two models work (disagreement is a
    detector; agreement never a seal), cloud-vs-local trade-off table,
    Ollama/LM Studio/Jan setup path, the three-minute comparison
    ritual, privacy notes, and the correlated-error honesty limits.
  - `07` what never to delegate: law, medicine, money (plus official
    records and relaying to others) — what AI may freely help with in
    each, the shared blacklist logic, and the "prepare vs. decide"
    line.
  - `08` when it was wrong: the four-rung recovery ladder (contain,
    diagnose once, repair the loop, restore proportion) and fix-
    forward habits.
  - `09` spot-the-hallucination drills: five practice scenes (invented
    history, medical background, fake citation, stale procedure,
    agreeable echo) with expandable answers, plus how to grow your own
    drill set.
  - `checklist.md` — printable verification checklist (34 checkboxes,
    print button, print-friendly CSS).
  - `glossary.md` — 20 plain-English terms, alphabetical, with chapter
    pointers.
- **`build.py`** — stdlib-only Markdown → static HTML builder (headings
  with anchors, lists, task lists, tables, quotes, code fences,
  callouts, expandable `<details>` answers, inline formatting, `.md` →
  `.html` link rewriting, prev/next nav, shared header/footer). After
  every build it runs an internal link/anchor checker and exits
  non-zero on any problem.
- **`assets/`** — hand-written `style.css` (calm paper theme, responsive,
  print rules) and `favicon.svg` (checked answer). No external assets,
  no CDN, no fetched fonts, no JavaScript beyond one optional print
  button.
- **`site/`** — generated output (gitignored; rebuild with
  `python3 build.py`).
- **`tests/test_build.py`** — 37 tests: converter units (including the
  callout/details extensions and error cases), end-to-end build into a
  temp dir, page/anchor resolution, footer copyright checks,
  README/License checks, taxonomy-table and drill-details checks,
  both companion guides referenced by name, never-delegate chapter
  content, local-first assertions, and a secret-shaped-string scan of
  repo files.
- **`LICENSE`** — MIT with the exact line `Copyright (c) 2026 Asdale
  Dynamics, LLC`; **`README.md`** credits Asdale Dynamics, LLC (both
  test-asserted).

## How to run it

```bash
python3 build.py                          # build site/ + link check
python3 -m unittest discover -s tests -v  # run the 37 tests
```

Then open `site/index.html` in any browser. Everything works offline;
`site/` is self-contained. Python 3.10+ (developed on 3.13); no packages
to install.

## Verification results

- `python3 build.py` → **Built 14 files** (12 HTML pages + style.css +
  favicon.svg); **link check OK: 12 pages, all 202 hrefs resolve**
  (internal links and anchors).
- `python3 -m unittest discover -s tests` → **Ran 37 tests … OK**.
- Every built page parses as well-formed HTML (tag-balance check via
  Python's `html.parser`); nav carries all 12 chapters on every page;
  the checklist renders 34 tasks; the five drill answers render as
  hidden `<details>`; the taxonomy table renders 12 body rows.
- All docs proofread for stray non-ASCII characters (found none beyond
  intended typographic quotes/dashes/arrows).
- `LICENSE` contains the exact line `Copyright (c) 2026 Asdale
  Dynamics, LLC`; `README.md` credits Asdale Dynamics, LLC; every page
  footer carries the same copyright line (all three test-asserted).
- Git: initialized on `main`, single plain commit (`Add When AI Gets It
  Wrong guide: manual, build, tests`) by the existing git identity
  (Dylan Asdale), no co-author trailers, no remote, nothing pushed.
  `site/` is gitignored by design (regenerable output).

## Known gaps

- **Drills are prose, not live samples.** The five practice scenes show
  the *shape* of wrong answers rather than shipping real model outputs —
  deliberate (nothing here should be chased down by readers expecting it
  to exist), but a future edition could add a "make-your-own-samples"
  companion pack.
- **Stakes are the reader's to assign.** The row-1–4 test maps the
  reader's life, so it is judgment-based by design; the guide teaches
  the judgment calls but cannot make them automatically.
- **Local-AI setup changes** — Ollama/LM Studio/Jan UIs and model names
  evolve; chapter 06 teaches the shape (small model, different family,
  fresh chat, compare load-bearing details) rather than click-paths.
- **English only**; a large-print/translated variant could widen reach.
- **No websearch/writeback claims**: the guide assumes plain chat
  models; grounded/search-enabled tools change the freshness risk but
  not the checking habit — a possible future chapter.
- Education only — never legal, medical, or financial advice; specific
  situations are handed to licensed humans by design (chapter 07).
