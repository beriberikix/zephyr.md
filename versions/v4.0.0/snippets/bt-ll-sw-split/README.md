---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/snippets/bt-ll-sw-split/README.html
original_path: snippets/bt-ll-sw-split/README.html
---

# Zephyr Bluetooth LE Controller (bt-ll-sw-split)

You can build with this snippet by following the instructions in [the snippets usage page](../../build/snippets/using.md#using-snippets).
When building with `west`, you can do:

```shell
west build -S bt-ll-sw-split [...]
```

## Overview

This selects the Zephyr Bluetooth LE Controller.

## Requirements

Hardware support for:

- [`CONFIG_BT`](../../kconfig.md#CONFIG_BT "CONFIG_BT")
- [`CONFIG_BT_CTLR`](../../kconfig.md#CONFIG_BT_CTLR "CONFIG_BT_CTLR")
