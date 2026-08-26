#!/usr/bin/env python3
"""Validate generated Zephyr Markdown: front matter and resolved internal links.

Replaces a single regex sweep that could not see nesting, ignored code fences, and
stopped at the first problem. Uses stdlib only so CI needs no extra dependencies.
"""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
import urllib.error
import urllib.request
from bisect import bisect_right
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path, PurePosixPath
from typing import Iterator, NamedTuple

REQUIRED_FRONT_MATTER_KEYS = ("version", "source_url", "original_path")

# Targets we never resolve locally; anything else is treated as a repo-relative path.
EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "tel:", "ftp://", "data:")

FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
MAX_REPORTED = 50

# Absolute targets are checked only when explicitly asked for, since it needs
# the network and upstream sites rate-limit.
CHECKABLE_SCHEMES = ("http://", "https://")
USER_AGENT = "zephyr-md-link-check"


class Issue(NamedTuple):
    path: Path
    line: int
    kind: str
    detail: str


class Link(NamedTuple):
    line: int
    label: str
    target_raw: str


def mask_code(text: str) -> str:
    """Blank out fenced blocks and inline code, preserving offsets and line numbers.

    Masked characters become spaces so that link scanning skips code samples while
    reported line numbers still match the real file.
    """
    out: list[str] = []
    fence: str | None = None

    for line in text.splitlines(keepends=True):
        stripped = line.rstrip("\n")
        match = FENCE_RE.match(stripped)

        if match:
            token = match.group(1)
            if fence is None:
                fence = token[0]
            elif token[0] == fence:
                fence = None
            out.append(" " * len(stripped) + line[len(stripped):])
            continue

        if fence is not None:
            out.append(" " * len(stripped) + line[len(stripped):])
            continue

        out.append(mask_inline_code(stripped) + line[len(stripped):])

    return "".join(out)


INLINE_CODE_RE = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")


def mask_inline_code(line: str) -> str:
    """Blank inline code spans, matching a backtick run with an equal-length run."""
    if "`" not in line:
        return line
    return INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), line)


def scan_links(text: str) -> Iterator[Link]:
    """Yield inline links, matching brackets and parens by depth rather than by regex.

    Handles labels that themselves contain brackets and targets that contain parens,
    both of which a flat regex mis-parses.
    """
    line_starts = build_line_index(text)
    length = len(text)
    i = text.find("[")

    while i != -1 and i < length:
        if i > 0 and text[i - 1] == "\\":
            i = text.find("[", i + 1)
            continue

        label_end = match_delimiter(text, i, "[", "]")
        if label_end is None or label_end + 1 >= length or text[label_end + 1] != "(":
            i = text.find("[", i + 1)
            continue

        target_end = match_delimiter(text, label_end + 1, "(", ")")
        if target_end is None:
            i = text.find("[", i + 1)
            continue

        yield Link(
            line=bisect_right(line_starts, i),
            label=text[i + 1:label_end],
            target_raw=text[label_end + 2:target_end],
        )
        # Resume just inside this link rather than past it: a label can hold a
        # link of its own, as Sphinx's clickable figures do with
        # "[![alt](image)](image)", and the inner target needs checking too.
        i = text.find("[", i + 1)


def build_line_index(text: str) -> list[int]:
    """Offsets at which each line starts, for O(log n) offset-to-line lookup."""
    starts = [0]
    offset = text.find("\n")
    while offset != -1:
        starts.append(offset + 1)
        offset = text.find("\n", offset + 1)
    return starts


def match_delimiter(text: str, start: int, open_char: str, close_char: str) -> int | None:
    """Return the index closing the delimiter opened at `start`, or None."""
    depth = 0
    i = start
    length = len(text)

    while i < length:
        char = text[i]
        if char == "\\":
            i += 2
            continue
        if char == "\n" and text.startswith("\n\n", i):
            return None
        if char == open_char:
            depth += 1
        elif char == close_char:
            depth -= 1
            if depth == 0:
                return i
        i += 1

    return None


def split_target(target_raw: str) -> str:
    """Extract the destination from a link target, dropping any title."""
    target = target_raw.strip()

    if target.startswith("<"):
        end = target.find(">")
        if end != -1:
            return target[1:end].strip()

    # A title is whitespace-separated and quoted; a bare space otherwise belongs to
    # the destination only in malformed input, which other checks catch.
    for quote in ('"', "'", "("):
        marker = target.find(f" {quote}")
        if marker != -1:
            target = target[:marker]

    return target.strip()


def check_front_matter(path: Path, text: str) -> list[Issue]:
    if not text.startswith("---\n"):
        return [Issue(path, 1, "front-matter", "missing opening '---' delimiter")]

    end = text.find("\n---\n", 3)
    if end == -1:
        return [Issue(path, 1, "front-matter", "missing closing '---' delimiter")]

    block = text[4:end + 1]
    issues = []
    for key in REQUIRED_FRONT_MATTER_KEYS:
        if not re.search(rf"^{re.escape(key)}:", block, re.MULTILINE):
            issues.append(Issue(path, 1, "front-matter", f"missing required key '{key}:'"))
    return issues


def check_links(path: Path, text: str, known: set[str] | None = None) -> list[Issue]:
    issues = []

    for link in scan_links(mask_code(text)):
        if "](" in link.target_raw:
            issues.append(Issue(
                path, link.line, "nested-link",
                f"link target contains another link: [{truncate(link.label)}]"
                f"({truncate(link.target_raw)})",
            ))
            continue

        target = split_target(link.target_raw)
        if not target or target.startswith("#"):
            continue
        if target.startswith(EXTERNAL_SCHEMES) or target.startswith("//"):
            continue

        path_part = target.split("#", 1)[0].split("?", 1)[0]
        if path_part.endswith((".html", ".htm")):
            issues.append(Issue(
                path, link.line, "unresolved-html",
                f"internal link still points at HTML: {truncate(target)}",
            ))
            continue

        # Only Markdown is generated into this repository. A relative link to
        # anything else -- an image, an archive -- resolves to a file that was
        # never written, so it must have been rewritten to the published docs.
        suffix = PurePosixPath(path_part).suffix.lower()
        if suffix and suffix != ".md":
            issues.append(Issue(
                path, link.line, "unresolved-asset",
                f"relative link to a non-Markdown file: {truncate(target)}",
            ))
            continue

        # A well-formed link to a file that was never written is still broken.
        if known is not None and suffix == ".md":
            resolved = posixpath.normpath(
                posixpath.join(path.parent.as_posix(), path_part)
            )
            if resolved not in known:
                issues.append(Issue(
                    path, link.line, "dangling-link",
                    f"link target does not exist: {truncate(path_part)}",
                ))

    return issues


def collect_urls(path: Path, text: str) -> Iterator[tuple[str, int]]:
    """Yield (url, line) for each absolute http(s) target on the page."""
    for link in scan_links(mask_code(text)):
        if "](" in link.target_raw:
            continue
        target = split_target(link.target_raw)
        if target.startswith(CHECKABLE_SCHEMES):
            yield target.split("#", 1)[0], link.line


def classify_status(status: int) -> str | None:
    """Return a complaint for a status worth reporting, else None.

    401/403 mean the target exists but will not serve a robot, which says
    nothing about whether the link is right, so they are not failures.
    """
    if status in (401, 403):
        return None
    if status == 404 or status == 410:
        return f"HTTP {status}"
    if status >= 400:
        return f"HTTP {status}"
    return None


def probe_url(url: str, timeout: float) -> str | None:
    """Return a complaint if the URL does not resolve, else None."""
    request = urllib.request.Request(
        url, method="HEAD", headers={"User-Agent": USER_AGENT}
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return classify_status(response.status)
    except urllib.error.HTTPError as exc:
        # Some hosts reject HEAD outright; retry once with GET before believing it.
        if exc.code in (405, 501):
            try:
                get = urllib.request.Request(
                    url, headers={"User-Agent": USER_AGENT}
                )
                with urllib.request.urlopen(get, timeout=timeout) as response:
                    return classify_status(response.status)
            except Exception as retry_exc:  # noqa: BLE001 - reported, not raised
                return f"{type(retry_exc).__name__}"
        return classify_status(exc.code)
    except Exception as exc:  # noqa: BLE001 - network errors are the point here
        return f"{type(exc).__name__}"


def check_urls(
    first_seen: dict[str, tuple[Path, int]], workers: int, timeout: float
) -> list[Issue]:
    """Probe each unique URL once and attribute failures to where it first appears."""
    urls = sorted(first_seen)
    if not urls:
        return []

    with ThreadPoolExecutor(max_workers=workers) as pool:
        complaints = list(pool.map(lambda u: probe_url(u, timeout), urls))

    issues = []
    for url, complaint in zip(urls, complaints):
        if complaint is None:
            continue
        path, line = first_seen[url]
        issues.append(Issue(path, line, "broken-url", f"{complaint}: {truncate(url)}"))
    return sorted(issues, key=lambda i: (i.path.as_posix(), i.line))


def truncate(value: str, limit: int = 120) -> str:
    value = " ".join(value.split())
    return value if len(value) <= limit else value[:limit - 1] + "…"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path("versions"))
    parser.add_argument(
        "--strict-links",
        action="store_true",
        help="treat dangling internal links as errors instead of warnings",
    )
    parser.add_argument(
        "--check-urls",
        action="store_true",
        help="also verify that absolute http(s) links resolve (needs network; "
             "each unique URL is probed once)",
    )
    parser.add_argument(
        "--url-workers",
        type=int,
        default=16,
        help="parallel requests when --check-urls is set (default: 16)",
    )
    parser.add_argument(
        "--url-timeout",
        type=float,
        default=10.0,
        help="per-request timeout in seconds when --check-urls is set (default: 10)",
    )
    parser.add_argument(
        "--warn-nested-links",
        action="store_true",
        help="downgrade nested/malformed links to warnings (escape hatch for a new "
             "upstream shape the converter cannot yet collapse)",
    )
    args = parser.parse_args()

    if not args.root.is_dir():
        print(f"error: not a directory: {args.root}", file=sys.stderr)
        return 1

    files = sorted(args.root.rglob("*.md"))
    if not files:
        print(f"error: no markdown files found in {args.root}/", file=sys.stderr)
        return 1

    known = {p.as_posix() for p in files}

    issues: list[Issue] = []
    first_seen: dict[str, tuple[Path, int]] = {}
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        issues.extend(check_front_matter(path, text))
        issues.extend(check_links(path, text, known))
        if args.check_urls:
            for url, line in collect_urls(path, text):
                first_seen.setdefault(url, (path, line))

    if args.check_urls:
        print(f"Probing {len(first_seen)} unique absolute links...", flush=True)
        issues.extend(check_urls(first_seen, args.url_workers, args.url_timeout))

    # Upstream Doxygen links a handful of pages it never generates; those targets
    # are missing from the published docs too, so a dangling link is reported but
    # does not fail the build unless asked.
    soft = {"dangling-link"} if not args.strict_links else set()
    if args.warn_nested_links:
        soft.add("nested-link")
    warnings = [i for i in issues if i.kind in soft]
    errors = [i for i in issues if i not in warnings]

    report("warning", warnings)
    report("error", errors)

    print(f"Checked {len(files)} markdown files: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


def report(level: str, issues: list[Issue]) -> None:
    if not issues:
        return

    stream = sys.stderr if level == "error" else sys.stdout
    for issue in issues[:MAX_REPORTED]:
        print(f"{level}: {issue.path}:{issue.line}: [{issue.kind}] {issue.detail}", file=stream)

    if len(issues) > MAX_REPORTED:
        print(f"{level}: ... and {len(issues) - MAX_REPORTED} more", file=stream)


if __name__ == "__main__":
    raise SystemExit(main())
