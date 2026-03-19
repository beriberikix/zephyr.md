---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/snippets/rtt-console/README.html
original_path: snippets/rtt-console/README.html
---

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
