# Zephyr Documentation to Markdown Pipeline

This repository contains automation that builds Zephyr RTOS documentation for selected release tags and converts rendered Sphinx HTML into versioned Markdown for LLM/RAG use.

## Output Layout

Generated documentation is committed to:

- `versions/{tag}/...`
- `versions/latest/...`
- `versions/versions.json`

Each Markdown file includes YAML front matter:

- `version`
- `source_url`
- `original_path`

## Manual Run

Use the `Sync Zephyr Docs` workflow (`.github/workflows/sync.yml`) with inputs:

- `tags`: comma-separated tags, for example `v3.5.0,v3.6.0`
- `source_url_template`: default `https://docs.zephyrproject.org/{version}`
- `zephyr_repo`: default `https://github.com/zephyrproject-rtos/zephyr.git`

The workflow can also run automatically on tag pushes matching `v*`.

## Converter Script

`scripts/convert.py` converts Zephyr Sphinx HTML to Markdown by:

- Crawling all HTML files under an input root
- Extracting main content (`div[role='main']`, `article`, `main` fallback)
- Removing navigation/search/footer noise
- Rewriting internal links from `.html` to `.md`
- Preserving tables and fenced code blocks with language hints
- Injecting required YAML front matter metadata

### Local Usage

```bash
python3 -m pip install -r scripts/requirements-convert.txt
python3 scripts/convert.py \
  --input-html-root /path/to/doc/_build/html \
  --output-root versions/v3.6.0 \
  --version v3.6.0 \
  --base-source-url https://docs.zephyrproject.org/3.6.0 \
  --clean
```
