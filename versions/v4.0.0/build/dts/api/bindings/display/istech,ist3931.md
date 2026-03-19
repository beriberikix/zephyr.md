---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/display/istech,ist3931.html
original_path: build/dts/api/bindings/display/istech,ist3931.html
---

# istech,ist3931 (on i2c bus)

Vendor: [Integrated Solutions Technology Inc.](../../bindings.md#dt-vendor-istech)

Note

An implementation of a driver matching this compatible is available in
[drivers/display/display\_ist3931.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/display_ist3931.c).

## Description

```text
IST3931 65x132 display controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `reset-gpios` | `phandle-array` | ```text RESET pin.  The RESET pin of IST3931 is active low. If connected directly the MCU pin should be configured as active low. ```  This property is **required**. |
| `x-offset` | `int` | ```text The column offset in pixels of the LCD to the controller memory ```  This property is **required**. |
| `y-offset` | `int` | ```text The row offset in pixels of the LCD to the controller memory ```  This property is **required**. |
| `voltage-converter` | `boolean` | ```text Internal voltage converter circuits will be enabled if true ``` |
| `voltage-follower` | `boolean` | ```text Internal voltage follower circuits will be enabled if true ``` |
| `lcd-bias` | `int` | ```text LCD bias ratio of the voltage required for driving the LCD ```  This property is **required**. |
| `lcd-ct` | `int` | ```text reference voltage V0= [0.7+CT*0.005]/Bias at 24 degree Celsius ```  This property is **required**. |
| `duty-ratio` | `int` | ```text Com_1~COM_N is select, N=Duty-ratio. ```  This property is **required**. |
| `frame-control` | `int` | ```text Frame-control of row frequency and frame frequency. Row frequency = 3X10^6/ Frame-control Frame frequency = Row frequency / Duty-ratio ```  This property is **required**. |
| `reverse-com-output` | `boolean` | ```text Common Output Mode Select, the output mode will be COM_1->COM_N if set to 0 ``` |
| `reverse-seg-driver` | `boolean` | ```text Defines the relationship between RAM column address and segment driver. the mapping will be SEG1->SEG132 if set to 0 ``` |
| `e-force-on` | `boolean` | ```text turn on whole LCD points regardless of display RAM ``` |
| `reverse-ram-lcd` | `boolean` | ```text Reverse the lit and unlit display relation between RAM bit data and LCD cell ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `height` | `int` | ```text Height of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |
| `width` | `int` | ```text Width of the panel driven by the controller, with the units in pixels. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “istech,ist3931” compatible.

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
