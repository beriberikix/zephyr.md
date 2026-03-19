---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/input/pixart,pat912x.html
original_path: build/dts/api/bindings/input/pixart,pat912x.html
---

# pixart,pat912x (on i2c bus)

Vendor: [PixArt Imaging Inc.](../../bindings.md#dt-vendor-pixart)

Note

An implementation of a driver matching this compatible is available in
[drivers/input/input\_pat912x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/input_pat912x.c).

## Description

```text
PAT9125EL Miniature Optical Navigation Chip
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `motion-gpios` | `phandle-array` | ```text GPIO connected to the motion pin, active low. ```  This property is **required**. |
| `zephyr,axis-x` | `int` | ```text The input code for the X axis to report for the device, typically any of INPUT_REL_*. No report produced for the device X axis if unspecified. ``` |
| `zephyr,axis-y` | `int` | ```text The input code for the Y axis to report for the device, typically any of INPUT_REL_*. No report produced for the device Y axis if unspecified. ``` |
| `res-x-cpi` | `int` | ```text CPI resolution for the X axis, range 0 to 1275, rounded down to the closest supported value in increments of 5. ``` |
| `res-y-cpi` | `int` | ```text CPI resolution for the Y axis, range 0 to 1275, rounded down to the closest supported value in increments of 5. ``` |
| `invert-x` | `boolean` | ```text Invert X axis values. ``` |
| `invert-y` | `boolean` | ```text Invert Y axis values. ``` |
| `sleep1-enable` | `boolean` | ```text Enable sleep1 mode. ``` |
| `sleep2-enable` | `boolean` | ```text Enable sleep2 mode, only valid if sleep1 is also enabled. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “pixart,pat912x” compatible.

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
