#!/usr/bin/env python3
"""Convert Zephyr Sphinx HTML output to versioned Markdown with YAML front matter."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

import yaml
from bs4 import BeautifulSoup
from bs4.element import Tag
from markdownify import MarkdownConverter


DEFAULT_MAIN_SELECTORS = [
    "div[role='main']",
    "article",
    "main",
    "div.document",
    "div.body",
    "div[role='document']",
]

DEFAULT_STRIP_SELECTORS = [
    "script",
    "style",
    "noscript",
    "header",
    "footer",
    "nav",
    "div[role='navigation']",
    "div[role='search']",
    "div[role='complementary']",
    ".wy-nav-side",
    ".wy-side-nav-search",
    ".wy-breadcrumbs",
    ".rst-footer-buttons",
    ".related",
    ".sphinxsidebar",
    ".toctree-wrapper",
    ".headerlink",
]

CODE_LANGUAGE_MAP = {
    "bash": "shell",
    "sh": "shell",
    "console": "shell",
    "shell-session": "shell",
    "none": "text",
    "default": "text",
}


class ZephyrMarkdownConverter(MarkdownConverter):
    """Custom markdown converter that rewrites internal HTML links to Markdown."""

    def convert_a(self, el: Tag, text: str, parent_tags: Iterable[str]) -> str:  # type: ignore[override]
        href = (el.get("href") or "").strip()
        if not href:
            return text

        parsed = urlparse(href)
        is_external = parsed.scheme in {"http", "https", "mailto", "tel"} or href.startswith("//")
        if is_external:
            return f"[{text}]({href})"

        if href.startswith("#"):
            return f"[{text}]({href})"

        path_part, anchor = _split_anchor(href)

        if path_part.endswith(".html"):
            path_part = f"{path_part[:-5]}.md"
        elif path_part.endswith("/"):
            path_part = f"{path_part}index.md"

        new_href = path_part
        if anchor:
            new_href = f"{new_href}#{anchor}" if new_href else f"#{anchor}"

        title = (el.get("title") or "").strip()
        title_part = f' "{title}"' if title else ""
        return f"[{text}]({new_href}{title_part})"


def _split_anchor(link: str) -> tuple[str, str]:
    if "#" not in link:
        return link, ""
    path, anchor = link.split("#", 1)
    return path, anchor


def detect_code_language(pre_tag: Tag) -> str | None:
    """Detect code language from Sphinx/pygments classes around <pre>."""
    candidates: list[str] = []

    for source in (pre_tag, pre_tag.parent, pre_tag.parent.parent if pre_tag.parent else None):
        if source is None or not isinstance(source, Tag):
            continue

        classes = source.get("class", [])
        for cls in classes:
            if cls.startswith("highlight-"):
                candidates.append(cls.replace("highlight-", "", 1))
            elif cls.startswith("language-"):
                candidates.append(cls.replace("language-", "", 1))
            elif cls.startswith("lang-"):
                candidates.append(cls.replace("lang-", "", 1))

        data_language = source.get("data-language")
        if data_language:
            candidates.append(str(data_language))

    for candidate in candidates:
        normalized = CODE_LANGUAGE_MAP.get(candidate.lower(), candidate.lower())
        if normalized:
            return normalized

    return None


def extract_main_content(soup: BeautifulSoup, selectors: list[str]) -> Tag:
    for selector in selectors:
        found = soup.select_one(selector)
        if found:
            return found

    if soup.body:
        return soup.body
    return soup


def strip_noise(root: Tag, selectors: list[str]) -> None:
    for selector in selectors:
        for node in root.select(selector):
            node.decompose()


def normalize_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def build_front_matter(version: str, source_url: str, original_path: str) -> str:
    payload = {
        "version": version,
        "source_url": source_url,
        "original_path": original_path,
    }
    return "---\n" + yaml.safe_dump(payload, sort_keys=False).strip() + "\n---\n\n"


def compute_source_url(base_source_url: str, relative_html_path: str) -> str:
    base = base_source_url.rstrip("/")
    rel = relative_html_path.replace("\\", "/")
    return f"{base}/{rel}"


def convert_html_file(
    html_file: Path,
    html_root: Path,
    output_root: Path,
    version: str,
    base_source_url: str,
    main_selectors: list[str],
    strip_selectors: list[str],
) -> tuple[Path, str]:
    relative_html = html_file.relative_to(html_root).as_posix()
    relative_md = relative_html[:-5] + ".md"
    output_file = output_root / relative_md

    soup = BeautifulSoup(html_file.read_text(encoding="utf-8", errors="ignore"), "lxml")
    content_root = extract_main_content(soup, main_selectors)
    strip_noise(content_root, strip_selectors)

    converter = ZephyrMarkdownConverter(
        heading_style="ATX",
        bullets="-",
        code_language_callback=detect_code_language,
        table_infer_header=True,
    )
    markdown_body = converter.convert_soup(content_root)
    markdown_body = normalize_markdown(markdown_body)

    source_url = compute_source_url(base_source_url, relative_html)
    front_matter = build_front_matter(version, source_url, relative_html)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(front_matter + markdown_body, encoding="utf-8")
    return output_file, relative_html


def find_html_files(root: Path) -> list[Path]:
    html_files = [
        path
        for path in root.rglob("*.html")
        if "_static" not in path.parts and "_sources" not in path.parts
    ]
    return sorted(html_files)


def copy_latest(version_output_dir: Path, latest_dir: Path) -> None:
    if latest_dir.exists():
        shutil.rmtree(latest_dir)
    shutil.copytree(version_output_dir, latest_dir)


def write_manifest(version_output_dir: Path, version: str, converted: list[dict[str, str]]) -> None:
    manifest = {
        "version": version,
        "total_files": len(converted),
        "files": converted,
    }
    manifest_path = version_output_dir / "_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-html-root", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--version", required=True)
    parser.add_argument("--base-source-url", required=True)
    parser.add_argument("--main-selector", action="append", default=[])
    parser.add_argument("--strip-selector", action="append", default=[])
    parser.add_argument("--latest-dir", type=Path)
    parser.add_argument("--clean", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    html_root: Path = args.input_html_root
    output_root: Path = args.output_root

    if not html_root.exists():
        raise FileNotFoundError(f"Input HTML root not found: {html_root}")

    if args.clean and output_root.exists():
        shutil.rmtree(output_root)

    output_root.mkdir(parents=True, exist_ok=True)

    main_selectors = args.main_selector or DEFAULT_MAIN_SELECTORS
    strip_selectors = args.strip_selector or DEFAULT_STRIP_SELECTORS

    html_files = find_html_files(html_root)
    if not html_files:
        raise RuntimeError(f"No HTML files found in {html_root}")

    converted_files: list[dict[str, str]] = []
    for html_file in html_files:
        output_file, original_html = convert_html_file(
            html_file=html_file,
            html_root=html_root,
            output_root=output_root,
            version=args.version,
            base_source_url=args.base_source_url,
            main_selectors=main_selectors,
            strip_selectors=strip_selectors,
        )
        converted_files.append(
            {
                "original_path": original_html,
                "markdown_path": output_file.relative_to(output_root).as_posix(),
            }
        )

    write_manifest(output_root, args.version, converted_files)

    if args.latest_dir:
        copy_latest(output_root, args.latest_dir)

    print(f"Converted {len(converted_files)} HTML files for {args.version} into {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
