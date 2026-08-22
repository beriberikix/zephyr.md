---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/input/vishay,vs1838b.html
original_path: build/dts/api/bindings/input/vishay,vs1838b.html
---

# vishay,vs1838b

Vendor: [Vishay Intertechnology, Inc](../../bindings.md#dt-vendor-vishay)

Note

An implementation of a driver matching this compatible is available in
[drivers/input/input\_vs1838b.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/input_vs1838b.c).

## Description

```text
Vishay VS1838B infrared receiver
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `data-gpios` | `phandle-array` | ```text GPIO used to transmit the received data. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “vishay,vs1838b” compatible.

(None)
