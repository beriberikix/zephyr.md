---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/charger/maxim,max20335-charger.html
original_path: build/dts/api/bindings/charger/maxim,max20335-charger.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# maxim,max20335-charger

Vendor: [Maxim Integrated Products](../../bindings.md#dt-vendor-maxim)

## Description

```text
Maxim MAX20335 battery charger
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `constant-charge-current-max-microamp` | `int` | ```text maximum constant input current ```  This property is **required**. |
| `constant-charge-voltage-max-microvolt` | `int` | ```text maximum constant input voltage ```  This property is **required**. |
| `precharge-current-microamp` | `int` | ```text current for pre-charge phase ``` |
| `charge-term-current-microamp` | `int` | ```text current for charge termination phase ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “maxim,max20335-charger” compatible.

(None)
