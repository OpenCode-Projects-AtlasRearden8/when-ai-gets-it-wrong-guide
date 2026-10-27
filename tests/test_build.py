"""Tests for When AI Gets It Wrong.

Run with:  python3 -m unittest discover -s tests -v

Covers the Markdown-to-HTML converter (including the ::: callout and
:::details extensions), an end-to-end build: every page renders, every
internal link and anchor resolves, the required copyright line appears in
every footer, the mistake-taxonomy table renders, checkbox checklists
render, drill answers are hidden details, and no secret- or API-key-shaped
strings appear anywhere in the repo.

Copyright (c) 2026 Asdale Dynamics, LLC - MIT License
"""

from __future__ import annotations

import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build  # noqa: E402

DOCS = sorted((ROOT / "docs").glob("*.md"))
COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"


# ---------------------------------------------------------------------------
# Converter unit tests
# ---------------------------------------------------------------------------

class InlineTests(unittest.TestCase):
    def test_bold_italic_code(self):
        self.assertEqual(build.inline("a **b** *c* `d`"),
                         "a <strong>b</strong> <em>c</em> <code>d</code>")

    def test_code_span_protected_from_markup(self):
        self.assertEqual(build.inline("`*x*`"), "<code>*x*</code>")

    def test_link_to_md_rewritten(self):
        self.assertEqual(build.inline("[a](05-cross-checking-with-real-sources.md)"),
                         '<a href="05-cross-checking-with-real-sources.html">a</a>')
        self.assertEqual(build.inline("[a](05-cross-checking-with-real-sources.md#x)"),
                         '<a href="05-cross-checking-with-real-sources.html#x">a</a>')

    def test_external_link_target_blank(self):
        out = build.inline("[f](https://contentcredentials.org/verify)")
        self.assertIn('target="_blank"', out)
        self.assertIn('rel="noopener"', out)

    def test_html_escaped(self):
        self.assertEqual(build.inline("a < b"), "a &lt; b")


class BlockTests(unittest.TestCase):
    def test_heading_gets_anchor(self):
        out = build.md_to_html("## The Stakes Test")
        self.assertIn('<h2 id="the-stakes-test">', out)

    def test_paragraph_wrapping(self):
        self.assertEqual(build.md_to_html("first\nsecond"),
                         "<p>first second</p>")

    def test_bullet_list_with_tasks(self):
        out = build.md_to_html("- [ ] one\n- [x] two\n- plain")
        self.assertEqual(out.count('class="task"'), 2)
        self.assertEqual(out.count(" checked"), 1)
        self.assertIn("<li>plain</li>", out)

    def test_nested_list(self):
        out = build.md_to_html("- a\n  - a1\n- b")
        self.assertIn("<ul>", out)
        self.assertIn("<li>a1</li>", out)
        self.assertIn("<li>b</li>", out)

    def test_ordered_list(self):
        out = build.md_to_html("1. one\n2. two")
        self.assertTrue(out.startswith("<ol>"))
        self.assertIn("<li>one</li>", out)

    def test_table(self):
        out = build.md_to_html(
            "| a | b |\n| --- | --- |\n| 1 | **2** |")
        self.assertIn("<thead><tr><th>a</th><th>b</th></tr></thead>", out)
        self.assertIn("<td><strong>2</strong></td>", out)

    def test_blockquote_renders_inner(self):
        out = build.md_to_html("> **Bold** note")
        self.assertIn("<blockquote>", out)
        self.assertIn("<strong>Bold</strong>", out)

    def test_fenced_code_escapes(self):
        out = build.md_to_html("```\na <tag>\n```")
        self.assertIn("<pre><code>", out)
        self.assertIn("a &lt;tag&gt;", out)

    def test_horizontal_rule(self):
        self.assertIn("<hr>", build.md_to_html("---"))

    def test_slugify(self):
        self.assertEqual(build.slugify("High-Stakes vs. Low-Stakes Asks"),
                         "high-stakes-vs-low-stakes-asks")

    def test_callout_renders(self):
        out = build.md_to_html(":::note Watch out\nBody line.\n:::")
        self.assertIn('<aside class="callout note">', out)
        self.assertIn('<p class="callout-kicker">Watch out</p>', out)
        self.assertIn("<p>Body line.</p>", out)

    def test_details_renders(self):
        out = build.md_to_html(":::details Answer\n**Hidden** words.\n:::")
        self.assertIn("<details>", out)
        self.assertIn("<summary>Answer</summary>", out)
        self.assertIn("<strong>Hidden</strong>", out)

    def test_unclosed_details_raises(self):
        with self.assertRaises(ValueError):
            build.md_to_html(":::details Answer\nnever closed")

    def test_stray_closer_raises(self):
        with self.assertRaises(ValueError):
            build.md_to_html(":::")


# ---------------------------------------------------------------------------
# End-to-end build tests
# ---------------------------------------------------------------------------

class BuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name) / "site"
        cls.files = build.build(cls.out)
        cls.pages = {p["slug"]: p for p in build.read_pages()}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def _read(self, name: str) -> str:
        return (self.out / name).read_text(encoding="utf-8")

    def test_expected_pages_built(self):
        self.assertIn("index.html", self.files)
        for md in DOCS:
            self.assertIn(md.stem + ".html", self.files)
        self.assertIn("style.css", self.files)
        self.assertIn("favicon.svg", self.files)

    def test_required_chapters_present(self):
        for required in ("01", "02", "03", "04", "05", "06", "07", "08", "09"):
            matches = [s for s in self.pages if s.startswith(required + "-")]
            self.assertTrue(matches, f"chapter {required} missing from docs/")

    def test_special_pages_present(self):
        for slug in ("checklist", "glossary"):
            self.assertIn(slug, self.pages)

    def test_footer_copyright(self):
        for f in self.files:
            if f.endswith(".html"):
                self.assertIn(COPYRIGHT, self._read(f))

    def test_readme_credits_company(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", readme)

    def test_license_exact_copyright_line(self):
        lic = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", lic)

    def test_nav_covers_all_pages(self):
        index = self._read("index.html")
        for slug, page in self.pages.items():
            self.assertIn(f'{page["file"]}"', index)

    def test_prevnext_links_resolve(self):
        for f in self.files:
            if not f.endswith(".html"):
                continue
            for _, href in re.findall(r'class="(prev|next)" href="([^"]+)"',
                                      self._read(f)):
                self.assertIn(href, self.files, f"bad prev/next in {f}")

    def test_internal_md_links_resolve_to_pages_and_anchors(self):
        link = re.compile(r"\[([^\]]+)\]\(([A-Za-z0-9._/-]+\.md(#[A-Za-z0-9-]+)?)\)")
        for md in DOCS:
            text = md.read_text(encoding="utf-8")
            for _, url, _ in link.findall(text):
                base, _, anchor = url.partition("#")
                slug = base.replace(".md", "")
                self.assertIn(slug, self.pages,
                              f"{md.name}: broken link -> {url}")
                if anchor:
                    target_html = self._read(slug + ".html")
                    self.assertIn(f'id="{anchor}"',
                                  target_html,
                                  f"{md.name}: missing anchor {url}")

    def test_checkbox_checklist_renders(self):
        checklist = next(p for p in self.pages.values() if p["slug"] == "checklist")
        self.assertIn('class="task"', checklist["body"])
        self.assertIn("<input", checklist["body"])
        self.assertGreater(checklist["body"].count("<input"), 20)

    def test_print_button_on_checklist_only(self):
        self.assertIn("print-button", self._read("checklist.html"))
        for slug, page in self.pages.items():
            if slug != "checklist":
                self.assertNotIn("print-button", page["body"])

    def test_drill_answers_are_hidden_details(self):
        drills = next(p for p in self.pages.values() if p["slug"].startswith("09-"))
        self.assertGreaterEqual(drills["body"].count("<details>"), 5)

    def test_mistake_taxonomy_table_renders(self):
        taxonomy = next(p for p in self.pages.values() if p["slug"].startswith("02-"))
        self.assertIn("<table>", taxonomy["body"])
        self.assertIn("Fabricated fact", taxonomy["body"].replace("<strong>", "").replace("</strong>", ""))
        # The taxonomy table has a row for each of twelve mistake types.
        rows = re.findall(r"<tr>", taxonomy["body"])
        self.assertGreaterEqual(len(rows), 13)  # header + 12 taxonomy rows

    def test_companion_guides_referenced_not_linked(self):
        # Cross-references to the two sibling guides stay prose (no fragile
        # relative links into sibling repos).
        for p in self.pages.values():
            self.assertNotIn('href="../', p["body"])
        body_all = "".join(p["body"] for p in self.pages.values())
        self.assertIn("Spot Fake Media Guide", body_all)
        self.assertIn("AI Scam Safety Guide", body_all)

    def test_never_delegate_chapter_lists_top_three(self):
        nd = next(p for p in self.pages.values() if p["slug"].startswith("07-"))
        text = re.sub(r"<[^>]+>", " ", nd["body"])
        for domain in ("Law", "Medicine", "Money"):
            self.assertIn(domain, text)

    def test_second_local_opinion_mentions_tools(self):
        loc = next(p for p in self.pages.values() if p["slug"].startswith("06-"))
        self.assertIn("Ollama", loc["body"])
        self.assertIn("LM Studio", loc["body"])

    def test_no_secrets_in_repo_files(self):
        secret_patterns = [
            re.compile(p, re.I) for p in (
                r"sk-[a-z0-9]{16,}", r"ghp_[a-z0-9]{20,}", r"github_pat_",
                r"xox[bp]-", r"AKIA[A-Z0-9]{12,}", r"-----BEGIN [A-Z ]*PRIVATE KEY",
                r"api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9]{12,}",
                r"secret[_-]?key\s*[:=]\s*['\"][A-Za-z0-9]{12,}",
            )
        ]
        for path in list(ROOT.rglob("*")):
            if (not path.is_file()
                    or "__pycache__" in path.parts
                    or path == ROOT / "tests" / "test_build.py"
                    or path.name == "favicon.svg"
                    or path.parent.name == "site"
                    or ".git" in path.parts):
                continue
            if path.suffix in {".md", ".py", ".css", ".txt", ".cfg", ".html"}:
                try:
                    content = path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                for pat in secret_patterns:
                    self.assertIsNone(pat.search(content),
                                      f"secret-shaped string in {path}")

    def test_site_is_local_first(self):
        # No CDN/external assets referenced by any built page.
        for f in self.files:
            if f.endswith(".html"):
                page = self._read(f)
                self.assertNotIn('src="http', page)
                self.assertNotIn('href="http' + 's://cdn', page)


if __name__ == "__main__":
    unittest.main()
