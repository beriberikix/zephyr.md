---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/sensor/st,stm32-temp-cal.html
original_path: build/dts/api/bindings/sensor/st,stm32-temp-cal.html
---

# st,stm32-temp-cal

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/st/stm32\_temp/stm32\_temp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/st/stm32_temp/stm32_temp.c).

## Description

```text
STM32 family TEMP node for production calibrated sensors with two calibration temperatures.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `ts-cal2-addr` | `int` | ```text Address of TS_CAL2 calibration parameter ```  This property is **required**. |
| `ts-cal2-temp` | `int` | ```text Temperature at which TS_CAL2 has been measured (TS_CAL2_TEMP) ```  This property is **required**. |
| `ts-cal1-addr` | `int` | ```text Address of TS_CAL1 calibration parameter ```  This property is **required**. |
| `ts-cal1-temp` | `int` | ```text Temperature at which TS_CAL1 has been measured (TS_CAL2_TEMP) ```  This property is **required**. |
| `ts-cal-vrefanalog` | `int` | ```text Analog voltage reference (Vref+) voltage with which temperature sensor calibration parameters have been measured ```  This property is **required**. |
| `ts-cal-resolution` | `int` | ```text ADC resolution used for measuring calibration data  This is usually equal to the ADC's native resolution.  Most series have a 12-bit ADC, but 14-bit and 16-bit also exists on e.g., STM32U5 and STM32H7 (16) series. ```  Default value: `12`  Legal values: `12`, `14`, `16` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-temp-cal” compatible.

| Name | Type | Details |
| --- | --- | --- |
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
| `io-channels` | `phandle-array` | ```text IO channels specifiers ```  This property is **required**. |
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
