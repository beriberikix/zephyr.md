---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/charger/maxim,max20335-charger.html
original_path: build/dts/api/bindings/charger/maxim,max20335-charger.html
---

# maxim,max20335-charger

Vendor: [Maxim Integrated Products](../../bindings.md#dt-vendor-maxim)

Note

An implementation of a driver matching this compatible is available in
[drivers/charger/charger\_max20335.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/charger_max20335.c).

## Description

```text
Maxim MAX20335 battery charger
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `constant-charge-voltage-max-microvolt` | `int` | ```text maximum constant input voltage ```  This property is **required**.  Legal values: `4050000`, `4100000`, `4150000`, `4200000`, `4250000`, `4300000`, `4350000`, `4400000`, `4450000`, `4500000`, `4550000`, `4600000` |
| `chgin-to-sys-current-limit-microamp` | `int` | ```text CHGIN to SYS path current limitter configuration. Refer to ILimCntl register description for details. ```  This property is **required**.  Legal values: `0`, `100000`, `500000`, `1000000` |
| `system-voltage-min-threshold-microvolt` | `int` | ```text System voltage minimum threshold. When SYS path voltage drops to this level, the charger current is reduced to prevent battery damage. ```  This property is **required**.  Legal values: `3600000`, `3700000`, `3800000`, `3900000`, `4000000`, `4100000`, `4200000`, `4300000` |
| `re-charge-threshold-microvolt` | `int` | ```text Recharge threshold in relation to BatReg. Refer to ChgCntlA register description for details. ```  This property is **required**.  Legal values: `70000`, `120000`, `170000`, `220000` |
| `thermistor-monitoring-mode` | `string` | ```text Thermistor monitoring mode. Refer to ThrmCfg register description and Table 2 for details. ```  This property is **required**.  Legal values: `'disabled'`, `'thermistor'`, `'JEITA-1'`, `'JEITA-2'` |
| `int-gpios` | `phandle-array` | ```text Interrupt pin ```  This property is **required**. |
| `device-chemistry` | `string` | ```text This describes the chemical technology of the battery. The "lithium-ion" value is a blanket type for all lithium-ion batteries. If the specific chemistry is unknown, this value can be used instead of the precise "lithium-ion-X" options. ```  Legal values: `'nickel-cadmium'`, `'nickel-metal-hydride'`, `'lithium-ion'`, `'lithium-ion-polymer'`, `'lithium-ion-iron-phosphate'`, `'lithium-ion-manganese-oxide'` |
| `ocv-capacity-table-0` | `array` | ```text An array providing the open circuit voltage (OCV) , which is used to look up battery capacity according to current OCV value. The OCV unit is microvolts.  Unlike the linux equivalent this array is required to be 11 elements long, representing the voltages for 0-100% charge in 10% steps. ``` |
| `charge-full-design-microamp-hours` | `int` | ```text battery design capacity ``` |
| `re-charge-voltage-microvolt` | `int` | ```text limit to automatically start charging again ``` |
| `precharge-current-microamp` | `int` | ```text current for pre-charge phase ``` |
| `charge-term-current-microamp` | `int` | ```text current for charge termination phase ``` |
| `constant-charge-current-max-microamp` | `int` | ```text maximum constant input current ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “maxim,max20335-charger” compatible.

(None)
