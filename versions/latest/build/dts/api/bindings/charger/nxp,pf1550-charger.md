---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/charger/nxp,pf1550-charger.html
original_path: build/dts/api/bindings/charger/nxp,pf1550-charger.html
---

# nxp,pf1550-charger

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

Note

An implementation of a driver matching this compatible is available in
[drivers/charger/charger\_pf1550.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/charger_pf1550.c).

## Description

```text
NXP PF1550 battery charger
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `constant-charge-voltage-max-microvolt` | `int` | ```text maximum constant input voltage ```  This property is **required**. |
| `constant-charge-current-max-microamp` | `int` | ```text maximum constant input current ```  This property is **required**. |
| `pf1550,vbus-current-limit-microamp` | `int` | ```text VBUS current limit in microamperes. ```  This property is **required**. |
| `pf1550,system-voltage-min-threshold-microvolt` | `int` | ```text System voltage minimum threshold. ```  This property is **required**.  Legal values: `3500000`, `3700000`, `4300000` |
| `pf1550,thermistor-monitoring-mode` | `string` | ```text Thermistor monitoring mode. Refer to ThrmCfg register description and Table 2 for details. ```  This property is **required**.  Legal values: `'disabled'`, `'thermistor'`, `'JEITA-1'`, `'JEITA-2'` |
| `pf1550,int-gpios` | `phandle-array` | ```text Interrupt pin ```  This property is **required**. |
| `pf1550,led-behaviour` | `string` | ```text Behaviour for charger LED. ```  This property is **required**.  Legal values: `'on-in-charging-flash-in-fault'`, `'flash-in-charging-on-in-fault'`, `'manual-off'` |
| `device-chemistry` | `string` | ```text This describes the chemical technology of the battery. The "lithium-ion" value is a blanket type for all lithium-ion batteries. If the specific chemistry is unknown, this value can be used instead of the precise "lithium-ion-X" options. ```  Legal values: `'nickel-cadmium'`, `'nickel-metal-hydride'`, `'lithium-ion'`, `'lithium-ion-polymer'`, `'lithium-ion-iron-phosphate'`, `'lithium-ion-manganese-oxide'` |
| `ocv-capacity-table-0` | `array` | ```text An array providing the open circuit voltage (OCV) , which is used to look up battery capacity according to current OCV value. The OCV unit is microvolts.  Unlike the linux equivalent this array is required to be 11 elements long, representing the voltages for 0-100% charge in 10% steps. ``` |
| `charge-full-design-microamp-hours` | `int` | ```text battery design capacity ``` |
| `re-charge-voltage-microvolt` | `int` | ```text limit to automatically start charging again ``` |
| `precharge-current-microamp` | `int` | ```text current for pre-charge phase ``` |
| `charge-term-current-microamp` | `int` | ```text current for charge termination phase ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,pf1550-charger” compatible.

(None)
