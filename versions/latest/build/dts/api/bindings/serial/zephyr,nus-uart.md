---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/serial/zephyr,nus-uart.html
original_path: build/dts/api/bindings/serial/zephyr,nus-uart.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# zephyr,nus-uart

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

## Description

```text
UART over NUS (Bluetooth LE)
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `tx-fifo-size` | `int` | ```text Size of the virtual UART TX FIFO ```  Default value: `1024` |
| `rx-fifo-size` | `int` | ```text Size of the virtual UART RX FIFO ```  Default value: `1024` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,nus-uart” compatible.

(None)
