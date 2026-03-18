---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/snippets/nordic-flpr/README.html
original_path: snippets/nordic-flpr/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Nordic FLPR snippet with execution from SRAM (nordic-flpr)

## Overview

This snippet allows users to build Zephyr with the capability to boot Nordic FLPR
(Fast Lightweight Peripheral Processor) from application core.
FLPR code is to be executed from SRAM, so the FLPR image must be built
without the `xip` board variant, or with [`CONFIG_XIP`](../../kconfig.md#CONFIG_XIP "CONFIG_XIP") disabled.
