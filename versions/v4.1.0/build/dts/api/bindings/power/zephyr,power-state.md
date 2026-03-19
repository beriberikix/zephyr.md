---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/power/zephyr,power-state.html
original_path: build/dts/api/bindings/power/zephyr,power-state.html
---

# zephyr,power-state

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

## Description

```text
Properties for power management state
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `power-state-name` | `string` | ```text indicates a power state ```  This property is **required**.  Legal values: `'active'`, `'runtime-idle'`, `'suspend-to-idle'`, `'standby'`, `'suspend-to-ram'`, `'suspend-to-disk'`, `'soft-off'` |
| `substate-id` | `int` | ```text Platform specific identification. ``` |
| `min-residency-us` | `int` | ```text Minimum residency duration in microseconds. It is the minimum time for a given idle state to be worthwhile energywise. It includes the time to enter in this state. ``` |
| `exit-latency-us` | `int` | ```text Worst case latency in microseconds required to exit the idle state. ``` |
| `zephyr,pm-device-disabled` | `boolean` | ```text Disable system managed device power management for this state. When set, the power management subsystem will not suspend devices before entering this state. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “zephyr,power-state” compatible.

(None)
