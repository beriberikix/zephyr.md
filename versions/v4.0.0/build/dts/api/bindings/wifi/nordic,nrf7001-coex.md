---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/wifi/nordic,nrf7001-coex.html
original_path: build/dts/api/bindings/wifi/nordic,nrf7001-coex.html
---

# nordic,nrf7001-coex

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
This is a representation of the nRF7001 Wi-Fi chip with COEX interface.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `req-gpios` | `phandle-array` | ```text GPIO of the SOC connected to the PTA's REQUEST pin. ``` |
| `status0-gpios` | `phandle-array` | ```text GPIO of the SOC connected to the PTA's PRIORITY pin. This GPIO is also used to indicate direction (TX/RX). ``` |
| `grant-gpios` | `phandle-array` | ```text GPIO of the SOC connected to the PTA's GRANT pin. ``` |
| `swctrl1-gpios` | `phandle-array` | ```text GPIO of the SOC controlling the Priority (STATUS1) pin (in 4-wire coex case) of the nRF7002 ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf7001-coex” compatible.

(None)
