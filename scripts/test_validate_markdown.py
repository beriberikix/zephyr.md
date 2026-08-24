#!/usr/bin/env python3
"""Tests for validate_markdown. Stdlib only: run with `python3 scripts/test_validate_markdown.py`."""

from __future__ import annotations

import unittest
from pathlib import Path

import validate_markdown as V

FRONT_MATTER = (
    "---\n"
    "version: v1\n"
    "source_url: https://example.com/a.html\n"
    "original_path: a.html\n"
    "---\n\n"
)
PATH = Path("t.md")


def link_kinds(body: str) -> list[str]:
    return [issue.kind for issue in V.check_links(PATH, FRONT_MATTER + body)]


class LinkScanningTests(unittest.TestCase):
    def assert_kinds(self, body: str, expected: list[str]) -> None:
        self.assertEqual(link_kinds(body), expected, body)

    def test_external_html_url_is_not_an_internal_link(self):
        # Regression: the flat regex reported these as unresolved internal links.
        self.assert_kinds("[Docs](https://ex.com/a/index.html)", [])

    def test_nested_link_is_reported_as_nested(self):
        self.assert_kinds(
            "[L]([https://ex.com/a.html](https://ex.com/a.html))", ["nested-link"]
        )

    def test_unresolved_internal_html_is_an_error(self):
        self.assert_kinds("[Env](../develop/env_vars.html)", ["unresolved-html"])
        self.assert_kinds("[Env](../develop/env_vars.html#envvar-PATH)", ["unresolved-html"])

    def test_resolved_markdown_link_passes(self):
        self.assert_kinds("[Env](../develop/env_vars.md#envvar-PATH)", [])

    def test_label_containing_brackets(self):
        self.assert_kinds("[foo [1] bar](../a.html)", ["unresolved-html"])
        self.assert_kinds("[foo [1] bar](../a.md)", [])

    def test_image_link(self):
        self.assert_kinds("![alt](../img/a.html)", ["unresolved-html"])

    def test_parenthesis_inside_url(self):
        self.assert_kinds("[W](https://en.wikipedia.org/wiki/A_(b).html)", [])

    def test_angle_bracket_target(self):
        self.assert_kinds("[E](<../develop/env vars.html>)", ["unresolved-html"])

    def test_target_with_title(self):
        self.assert_kinds('[E](../a.html "Title")', ["unresolved-html"])
        self.assert_kinds('[E](../a.md "Title")', [])

    def test_code_is_ignored(self):
        self.assert_kinds("```\n[x](y.html)\n```", [])
        self.assert_kinds("~~~\n[x](y.html)\n~~~", [])
        self.assert_kinds("Use `[x](y.html)` here", [])

    def test_non_path_targets_are_skipped(self):
        self.assert_kinds("[T](#section)", [])
        self.assert_kinds("[M](mailto:a@b.com)", [])
        self.assert_kinds("[P](//ex.com/a.html)", [])

    def test_links_nested_in_a_label_are_scanned(self):
        # Sphinx renders a clickable figure as an image inside a link. Both
        # targets are real links and both must be checked.
        self.assert_kinds(
            "[![alt](../_images/a.jpg)](../_images/a.jpg)",
            ["unresolved-asset", "unresolved-asset"],
        )
        self.assert_kinds(
            "[![alt](../_images/a.jpg)](https://ex.com/a.jpg)", ["unresolved-asset"]
        )
        self.assert_kinds("[![alt](../a.html)](../b.html)", ["unresolved-html", "unresolved-html"])

    def test_relative_asset_links_are_errors(self):
        # Only Markdown is generated here, so these resolve to nothing.
        self.assert_kinds("![pinout](../../_images/board.jpg)", ["unresolved-asset"])
        self.assert_kinds("[diagram](../_images/arch.svg)", ["unresolved-asset"])
        self.assert_kinds("[archive](../_downloads/demo.zip)", ["unresolved-asset"])

    def test_absolute_asset_links_are_fine(self):
        self.assert_kinds(
            "![pinout](https://docs.zephyrproject.org/4.2.0/_images/board.jpg)", []
        )

    def test_extensionless_relative_links_are_left_alone(self):
        self.assert_kinds("[dir](../some/target)", [])

    def test_html_extension_reported_once(self):
        # Must be unresolved-html, not also unresolved-asset.
        self.assert_kinds("[Env](../develop/env_vars.html)", ["unresolved-html"])

    def test_html_must_be_the_extension(self):
        # ".htmlx" is not HTML, so it is not an unresolved-html finding. It is
        # still not Markdown, so it is reported as an asset instead.
        self.assert_kinds("[X](../a.htmlx)", ["unresolved-asset"])
        self.assert_kinds("[X](../a.md?src=b.html)", [])

    def test_escaped_brackets_are_not_links(self):
        self.assert_kinds(r"\[not a link\](../a.html)", [])
        self.assert_kinds("just [brackets] and (parens)", [])

    def test_multiple_links_on_one_line(self):
        self.assert_kinds(
            "[a](../x.html) and [b](../y.html)", ["unresolved-html", "unresolved-html"]
        )

    def test_line_numbers_account_for_front_matter(self):
        issues = V.check_links(PATH, FRONT_MATTER + "line one\n\n[E](../a.html)")
        self.assertEqual([i.line for i in issues], [9])


class FrontMatterTests(unittest.TestCase):
    def assert_kinds(self, text: str, expected: list[str]) -> None:
        self.assertEqual([i.kind for i in V.check_front_matter(PATH, text)], expected)

    def test_valid(self):
        self.assert_kinds(FRONT_MATTER + "body", [])

    def test_absent(self):
        self.assert_kinds("# Title\n", ["front-matter"])

    def test_missing_keys(self):
        self.assert_kinds("---\nversion: v1\n---\n\nx", ["front-matter", "front-matter"])

    def test_unterminated(self):
        self.assert_kinds("---\nversion: v1\n", ["front-matter"])

    def test_key_must_start_the_line(self):
        # "myversion:" must not satisfy the "version:" requirement.
        self.assert_kinds(
            "---\nmyversion: v1\nsource_url: x\noriginal_path: y\n---\n\nx", ["front-matter"]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
