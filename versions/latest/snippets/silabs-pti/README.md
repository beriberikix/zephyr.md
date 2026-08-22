---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/snippets/silabs-pti/README.html
original_path: snippets/silabs-pti/README.html
---

# Silicon Labs Packet Trace Interface (silabs-pti)

## Overview

This snippet allows users to build Zephyr applications for Silicon Labs Series 2 devices
where radio packets are emitted over the Packet Trace Interface for use by debugging tools.

```shell
west build -S silabs-pti [...]
```

## Requirements

Hardware support for [`silabs,pti`](../../build/dts/api/bindings/debug/silabs%2Cpti.md#std-dtcompatible-silabs-pti).

A pinctrl configuration with nodelabel `pti_default` containing PTI pinout.
