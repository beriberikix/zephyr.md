---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/snippets/nordic-flpr-xip/README.html
original_path: snippets/nordic-flpr-xip/README.html
---

# Nordic FLPR snippet with execution in place (nordic-flpr-xip)

## Overview

This snippet allows users to build Zephyr with the capability to boot Nordic FLPR
(Fast Lightweight Peripheral Processor) from application core.
FLPR code is to be executed from RRAM, so the FLPR image must be built
for the `xip` board variant, or with [`CONFIG_XIP`](../../kconfig.md#CONFIG_XIP "CONFIG_XIP") enabled.
