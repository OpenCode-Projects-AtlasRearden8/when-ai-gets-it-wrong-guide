# When AI Gets It Wrong

Confident is not the same as correct — explained like a friend would. A
beginner's manual for calm verification of AI answers:

- **why models hallucinate** — the plain-English mechanism (prediction,
  not lookup; helpfulness over hedging; sycophancy) and four gap types,
- a **mistake taxonomy** — twelve recurring error types with what each
  looks like, why it happens, and the cheap check that catches it,
- the **stakes test** — one question ("if this is wrong, who pays?")
  that sorts every ask into skim-it, check-it, or never-delegate,
- the **verify-before-you-trust habit** — find the load-bearing details,
  check those, let the rest be pleasant; minutes, not hours,
- **cross-checking with real sources** — primary sources, exact-quote
  searches, your own arithmetic, the three-source bar, and why a nice
  link is not a source,
- a **second local opinion** — running a different model on your own
  computer (Ollama / LM Studio / Jan), private and offline, with the
  honest limits of two agreeing models,
- **what never to delegate** — law, medicine, and money, where AI
  prepares you for the professional and never gets the final word,
- **recovery** — what to do when you already believed a wrong answer:
  contain, diagnose once, fix forward, forgive,
- five **spot-the-hallucination drills**, a printable **verification
  checklist**, and a plain-English **glossary**.

The theme throughout: calm triage, not paranoia. Most AI answers deserve
zero checking — and the habit exists so the ones that matter never sneak
past.

## Companions, not repeats

This guide is the **answers side** of a set with two siblings, and the
three are deliberately built not to re-teach each other:

- ***The Spot Fake Media Guide*** — the **media side**: AI-made images,
  cloned voices, deepfake video, fake screenshots.
- ***The AI Scam Safety Guide*** — the **money side**: scam messages,
  fake listings, cloned-voice calls, payment recovery.
- **Here** — the **answers side**: when an AI chatbot's *own answer* is
  fabricated, stale, miscounted, or fake-sourced, and how to verify
  before you trust.

All three cross-reference each other by name (in prose, never by fragile
links across repos) and share the same calm motto family: pause, match
effort to stakes, "unresolved" is allowed.

## Who's behind it

Written and maintained by **Asdale Dynamics, LLC** as part of its
beginner-friendly guide series — the same spirit behind the book *The
Massive AI Manual*: plain English, step by step, warm, never
condescending, never alarmist. Education only — never legal, medical, or
financial advice.

## Read it

The Markdown "source of truth" lives in [`docs/`](docs/). Build the static
site and open it in any browser:

```bash
python3 build.py
```

That generates `site/` — a self-contained static HTML site with no
external dependencies, no analytics, no cookies, and no JavaScript
requirement (one optional print button for the checklist). Open
`site/index.html` to start reading. Everything works offline.

## Test it

```bash
python3 -m unittest discover -s tests -v
```

The suite covers the Markdown-to-HTML converter (headings, anchors,
lists, task lists, tables, quotes, code fences, callouts, expandable
details, inline formatting, link rewriting), an end-to-end build into a
temporary directory, internal link and anchor checking, the required
copyright line in every page footer, the mistake-taxonomy table and
drills, and a scan for secret-shaped strings in repo files.

`build.py` also verifies every internal link and anchor after each build
and exits non-zero on a problem, so a broken cross-reference can't ship
quietly.

## Repo layout

```
docs/          12 Markdown pages (the source of truth)
assets/        style.css + favicon.svg (copied into the site at build)
build.py       stdlib-only Markdown → static HTML builder + link checker
tests/         unittest suite (converter + end-to-end + repo checks)
site/          generated output (not committed; run python3 build.py)
```

## License

MIT — see [`LICENSE`](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.
