---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/haptics/ti,drv2605.html
original_path: build/dts/api/bindings/haptics/ti,drv2605.html
---

# ti,drv2605 (on i2c bus)

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

Note

An implementation of a driver matching this compatible is available in
[drivers/haptics/drv2605.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/haptics/drv2605.c).

## Description

```text
DRV2605 Haptic Driver for ERM and LRA with built-in library and smart-loop
architecture.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `actuator-mode` | `string` | This property is **required**.  Legal values: `'ERM'`, `'LRA'` |
| `feedback-brake-factor` | `string` | ```text Selects the feedback gain ratio between braking gain and driving gain. According to the datasheet, a value of 2 ("3X") is valid for most actuators. ```  Default value: `3X`  Legal values: `'1X'`, `'2X'`, `'3X'`, `'4X'`, `'6X'`, `'8X'`, `'16X'`, `'DISABLED'` |
| `loop-gain` | `string` | ```text Selects a loop gain for the feedback control. According to the datasheet, a value of 2 ("HIGH") is valid for most actuators. ```  Default value: `HIGH`  Legal values: `'LOW'`, `'MEDIUM'`, `'HIGH'`, `'VERY_HIGH'` |
| `vib-rated-mv` | `int` | ```text Sets the reference voltage for full-scale output during closed-loop operation. The default value is inherited from ti,drv260x.yaml in Linux. ```  Default value: `3200` |
| `vib-overdrive-mv` | `int` | ```text Sets a clamp so that the automatic overdrive is bounded. The default value is inherited from ti,drv260x.yaml in Linux. ```  Default value: `3200` |
| `en-gpios` | `phandle-array` | ```text GPIO to enable and disable the device. ``` |
| `in-trig-gpios` | `phandle-array` | ```text GPIO to trigger ROM waveforms or drive an input signal. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,drv2605” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text device address on i2c bus ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
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
