---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/bluetooth/ambiq,bt-hci-spi.html
original_path: build/dts/api/bindings/bluetooth/ambiq,bt-hci-spi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ambiq,bt-hci-spi

Vendor: [Ambiq Micro, Inc.](../../bindings.md#dt-vendor-ambiq)

## Description

```text
Bluetooth module that uses Ambiq's Bluetooth Host Controller Interface SPI
driver (e.g. Apollo4 Blue Plus).
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `irq-gpios` | `phandle-array` | ```text This irq gpio is used to indicate there is packet ready to send to host from controller. ``` |
| `reset-gpios` | `phandle-array` | ```text This reset gpio is used to reset the Bluetooth controller. ``` |
| `clkreq-gpios` | `phandle-array` | ```text This clkreq gpio is used to send the XO32MHz clock request to host from controller. The host needs to enable XO32MHz when receiving low to high edge interrupts and disable XO32MHz when receiving high to low edge interrupts. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ambiq,bt-hci-spi” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
