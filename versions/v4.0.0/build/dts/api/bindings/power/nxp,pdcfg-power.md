---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/power/nxp,pdcfg-power.html
original_path: build/dts/api/bindings/power/nxp,pdcfg-power.html
---

# nxp,pdcfg-power

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
Properties for NXP power management through the PDCFG register
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `deep-sleep-config` | `array` | ```text An array of values written to the PDSLEEPCFG registers that controls the power to various blocks while the CPU is in deep sleep mode. These values are programmed to the sleep configuration registers before entering deep sleep mode. ``` |
| `power-state-name` | `string` | ```text indicates a power state ```  This property is **required**.  Legal values: `'active'`, `'runtime-idle'`, `'suspend-to-idle'`, `'standby'`, `'suspend-to-ram'`, `'suspend-to-disk'`, `'soft-off'` |
| `substate-id` | `int` | ```text Platform specific identification. ``` |
| `min-residency-us` | `int` | ```text Minimum residency duration in microseconds. It is the minimum time for a given idle state to be worthwhile energywise. It includes the time to enter in this state. ``` |
| `exit-latency-us` | `int` | ```text Worst case latency in microseconds required to exit the idle state. ``` |
| `zephyr,pm-device-disabled` | `boolean` | ```text Disable system managed device power management for this state. When set, the power management subsystem will not suspend devices before entering this state. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,pdcfg-power” compatible.

(None)
