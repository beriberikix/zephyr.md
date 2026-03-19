---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/snippets/cdc-acm-console/README.html
original_path: snippets/cdc-acm-console/README.html
---

# CDC-ACM Console Snippet (cdc-acm-console)

```shell
west build -S cdc-acm-console [...]
```

## Overview

This snippet redirects serial console output to a CDC ACM UART. The USB device
which should be used is configured using [Devicetree](../../build/dts/index.md#devicetree).

## Requirements

Hardware support for:

- [`CONFIG_USB_DEVICE_STACK`](../../kconfig.md#CONFIG_USB_DEVICE_STACK "CONFIG_USB_DEVICE_STACK")
- [`CONFIG_SERIAL`](../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL")
- [`CONFIG_CONSOLE`](../../kconfig.md#CONFIG_CONSOLE "CONFIG_CONSOLE")
- [`CONFIG_UART_CONSOLE`](../../kconfig.md#CONFIG_UART_CONSOLE "CONFIG_UART_CONSOLE")
- [`CONFIG_UART_LINE_CTRL`](../../kconfig.md#CONFIG_UART_LINE_CTRL "CONFIG_UART_LINE_CTRL")

A devicetree node with node label `zephyr_udc0` that points to an enabled USB
device node with driver support. This should look roughly like this in
[your devicetree](../../build/dts/howtos.md#get-devicetree-outputs):

```dts
zephyr_udc0: usbd@deadbeef {
     compatible = "vnd,usb-device";
     /* ... */
};
```
