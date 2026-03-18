---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/snippets/nordic-ppr-xip/README.html
original_path: snippets/nordic-ppr-xip/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Nordic boot PPR snippet with execution in place (nordic-ppr-xip)

## Overview

This snippet allows users to build Zephyr with the capability to boot Nordic PPR
(Peripheral Processor) from another core. PPR code is to be executed from MRAM,
so the PPR image must be built for the `xip` board variant, or with
[`CONFIG_XIP`](../../kconfig.md#CONFIG_XIP "CONFIG_XIP") enabled.
