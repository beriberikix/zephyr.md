---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/snippets/rtt-tracing/README.html
original_path: snippets/rtt-tracing/README.html
---

# SystemView RTT Tracing Snippet (rtt-tracing)

```shell
west build -S rtt-tracing [...]
```

## Overview

This snippet enables SEGGER SystemView RTT support with the tracing subsystem.

## Requirements

Hardware support for:

- [`CONFIG_HAS_SEGGER_RTT`](../../kconfig.md#CONFIG_HAS_SEGGER_RTT "CONFIG_HAS_SEGGER_RTT")
