---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/charger/maxim,max20335-charger.html
original_path: build/dts/api/bindings/charger/maxim,max20335-charger.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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
| `re-charge-voltage-microvolt` | `int` | ```text limit to automatically start charging again ``` |
| `precharge-current-microamp` | `int` | ```text current for pre-charge phase ``` |
| `charge-term-current-microamp` | `int` | ```text current for charge termination phase ``` |
| `constant-charge-current-max-microamp` | `int` | ```text maximum constant input current ``` |
| `constant-charge-voltage-max-microvolt` | `int` | ```text maximum constant input voltage ```  This property is **required**.  Legal values: `4050000`, `4100000`, `4150000`, `4200000`, `4250000`, `4300000`, `4350000`, `4400000`, `4450000`, `4500000`, `4550000`, `4600000` |
| `chgin-to-sys-current-limit-microamp` | `int` | ```text CHGIN to SYS path current limitter configuration. Refer to ILimCntl register description for details. ```  This property is **required**.  Legal values: `0`, `100000`, `500000`, `1000000` |
| `system-voltage-min-threshold-microvolt` | `int` | ```text System voltage minimum threshold. When SYS path voltage drops to this level, the charger current is reduced to prevent battery damage. ```  This property is **required**.  Legal values: `3600000`, `3700000`, `3800000`, `3900000`, `4000000`, `4100000`, `4200000`, `4300000` |
| `re-charge-threshold-microvolt` | `int` | ```text Recharge threshold in relation to BatReg. Refer to ChgCntlA register description for details. ```  This property is **required**.  Legal values: `70000`, `120000`, `170000`, `220000` |
| `thermistor-monitoring-mode` | `string` | ```text Thermistor monitoring mode. Refer to ThrmCfg register description and Table 2 for details. ```  This property is **required**.  Legal values: `'disabled'`, `'thermistor'`, `'JEITA-1'`, `'JEITA-2'` |
| `int-gpios` | `phandle-array` | ```text Interrupt pin ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “maxim,max20335-charger” compatible.

(None)
