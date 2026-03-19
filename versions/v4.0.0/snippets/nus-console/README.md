---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/snippets/nus-console/README.html
original_path: snippets/nus-console/README.html
---

# NUS Console Snippet (nus-console)

```shell
west build -S nus-console [...]
```

## Overview

This snippet redirects serial console output to a UART over NUS (Bluetooth LE) instance.
The Bluetooth Serial device used shall be configured using [Devicetree](../../build/dts/index.md#devicetree).

## Requirements

Hardware support for:

- [`CONFIG_BT`](../../kconfig.md#CONFIG_BT "CONFIG_BT")
- [`CONFIG_BT_PERIPHERAL`](../../kconfig.md#CONFIG_BT_PERIPHERAL "CONFIG_BT_PERIPHERAL")
- [`CONFIG_BT_ZEPHYR_NUS`](../../kconfig.md#CONFIG_BT_ZEPHYR_NUS "CONFIG_BT_ZEPHYR_NUS")
- [`CONFIG_SERIAL`](../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL")
- [`CONFIG_CONSOLE`](../../kconfig.md#CONFIG_CONSOLE "CONFIG_CONSOLE")
- [`CONFIG_UART_CONSOLE`](../../kconfig.md#CONFIG_UART_CONSOLE "CONFIG_UART_CONSOLE")
