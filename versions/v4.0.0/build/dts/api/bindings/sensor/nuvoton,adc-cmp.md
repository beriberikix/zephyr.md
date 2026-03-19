---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/sensor/nuvoton,adc-cmp.html
original_path: build/dts/api/bindings/sensor/nuvoton,adc-cmp.html
---

# nuvoton,adc-cmp

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/nuvoton/nuvoton\_adc\_cmp\_npcx/adc\_cmp\_npcx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nuvoton/nuvoton_adc_cmp_npcx/adc_cmp_npcx.c).

## Description

```text
This will perform signal comparison with threshold established.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `threshold-mv` | `int` | ```text Value in millivolts present on ADC data as threshold assert. ``` |
| `comparison` | `string` | ```text Determines the condition to be met between ADC data and threshold assert value that will trigger comparator event. ```  Legal values: `'ADC_CMP_NPCX_GREATER'`, `'ADC_CMP_NPCX_LESS_OR_EQUAL'` |
| `thr-sel` | `string` | ```text Determines the register for threshold control and event. ```  Legal values: `'ADC_CMP_NPCX_THRCTL1'`, `'ADC_CMP_NPCX_THRCTL2'`, `'ADC_CMP_NPCX_THRCTL3'`, `'ADC_CMP_NPCX_THRCTL4'`, `'ADC_CMP_NPCX_THRCTL5'`, `'ADC_CMP_NPCX_THRCTL6'` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nuvoton,adc-cmp” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `io-channels` | `phandle-array` | ```text ADC channel that will perform measurement. ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
