#!/usr/bin/env python3
"""Tests for validate_markdown. Stdlib only: run with `python3 scripts/test_validate_markdown.py`."""

from __future__ import annotations

import unittest
from unittest import mock
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


class DanglingLinkTests(unittest.TestCase):
    """A well-formed link to a file that was never written is still broken."""

    def check(self, body: str, known: list[str]) -> list[str]:
        return [
            i.kind
            for i in V.check_links(Path("versions/v1/a/b.md"), FRONT_MATTER + body, set(known))
        ]

    def test_existing_target_passes(self):
        self.assertEqual(self.check("[x](../c/d.md)", ["versions/v1/c/d.md"]), [])

    def test_missing_target_is_reported(self):
        self.assertEqual(self.check("[x](../c/d.md)", []), ["dangling-link"])

    def test_percent_encoded_name_does_not_match_literal_file(self):
        # The regression that shipped 87k broken links: pages are written under
        # their literal names, links arrived percent-encoded.
        self.assertEqual(
            self.check("[x](../cpu/espressif%2Criscv.md)",
                       ["versions/v1/cpu/espressif,riscv.md"]),
            ["dangling-link"],
        )
        self.assertEqual(
            self.check("[x](../cpu/espressif,riscv.md)",
                       ["versions/v1/cpu/espressif,riscv.md"]),
            [],
        )

    def test_anchor_is_ignored_when_resolving(self):
        self.assertEqual(self.check("[x](../c/d.md#frag)", ["versions/v1/c/d.md"]), [])

    def test_disabled_when_no_index_supplied(self):
        self.assertEqual([i.kind for i in V.check_links(PATH, FRONT_MATTER + "[x](../c/d.md)")], [])


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


class CollectUrls(unittest.TestCase):
    def urls(self, body):
        return [u for u, _ in V.collect_urls(Path("versions/v1/a.md"), body)]

    def test_picks_up_absolute_links(self):
        self.assertEqual(
            self.urls("see [x](https://example.com/a) and [y](http://example.org)"),
            ["https://example.com/a", "http://example.org"],
        )

    def test_skips_relative_and_anchors(self):
        self.assertEqual(self.urls("[a](b.md) [c](#frag) [d](mailto:x@y.z)"), [])

    def test_drops_the_fragment(self):
        # The fragment never reaches the server, so probing it would be noise.
        self.assertEqual(self.urls("[a](https://example.com/p#sec)"), ["https://example.com/p"])

    def test_ignores_code_blocks(self):
        self.assertEqual(self.urls("```\n[a](https://example.com)\n```\n"), [])

    def test_descends_into_labels(self):
        # A clickable figure is "[![alt](image)](page)": both targets are real
        # and both deserve probing, so the label is not a dead end.
        self.assertEqual(
            sorted(self.urls("[![alt](https://x.com/i.png)](https://y.com/p)")),
            ["https://x.com/i.png", "https://y.com/p"],
        )

    def test_skips_malformed_targets(self):
        # Nesting inside the *target* is the broken shape check_links reports as
        # nested-link; probing the mangled result would be noise.
        self.assertEqual(self.urls("[a](https://x.com](https://y.com)"), [])

    def test_reports_line_numbers(self):
        found = list(V.collect_urls(Path("a.md"), "one\ntwo\n[x](https://example.com)\n"))
        self.assertEqual(found, [("https://example.com", 3)])


class ClassifyStatus(unittest.TestCase):
    def test_success_is_silent(self):
        for status in (200, 204, 301, 302):
            self.assertIsNone(V.classify_status(status))

    def test_missing_is_reported(self):
        self.assertEqual(V.classify_status(404), "HTTP 404")
        self.assertEqual(V.classify_status(410), "HTTP 410")

    def test_auth_walls_are_not_failures(self):
        # The page exists; it just will not serve a robot. Reporting these
        # would bury real breakage under noise from sites that block crawlers.
        self.assertIsNone(V.classify_status(401))
        self.assertIsNone(V.classify_status(403))

    def test_server_errors_are_reported(self):
        self.assertEqual(V.classify_status(500), "HTTP 500")


class CheckUrlsAttribution(unittest.TestCase):
    def test_failure_is_attributed_to_first_occurrence(self):
        first_seen = {"https://gone.example": (Path("versions/v1/a.md"), 7)}
        with mock.patch.object(V, "probe_url", return_value="HTTP 404"):
            issues = V.check_urls(first_seen, workers=2, timeout=1.0)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].kind, "broken-url")
        self.assertEqual(issues[0].line, 7)
        self.assertIn("gone.example", issues[0].detail)

    def test_healthy_urls_produce_nothing(self):
        first_seen = {"https://ok.example": (Path("a.md"), 1)}
        with mock.patch.object(V, "probe_url", return_value=None):
            self.assertEqual(V.check_urls(first_seen, workers=2, timeout=1.0), [])

    def test_each_unique_url_is_probed_once(self):
        first_seen = {f"https://e{i}.example": (Path("a.md"), i) for i in range(5)}
        with mock.patch.object(V, "probe_url", return_value=None) as probe:
            V.check_urls(first_seen, workers=4, timeout=1.0)
        self.assertEqual(probe.call_count, 5)

    def test_no_urls_makes_no_requests(self):
        with mock.patch.object(V, "probe_url") as probe:
            self.assertEqual(V.check_urls({}, workers=4, timeout=1.0), [])
        probe.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
