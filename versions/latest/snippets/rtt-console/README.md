---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/snippets/rtt-console/README.html
original_path: snippets/rtt-console/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# RTT Console Snippet (rtt-console)

```shell
west build -S rtt-console [...]
```

## Overview

This snippet redirects serial console output to SEGGER RTT.

## Requirements

Hardware support for:

- [`CONFIG_HAS_SEGGER_RTT`](../../kconfig.md#CONFIG_HAS_SEGGER_RTT "CONFIG_HAS_SEGGER_RTT")
- [`CONFIG_CONSOLE`](../../kconfig.md#CONFIG_CONSOLE "CONFIG_CONSOLE")
