---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/sensor/vishay,vcnl36825t.html
original_path: build/dts/api/bindings/sensor/vishay,vcnl36825t.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# vishay,vcnl36825t (on i2c bus)

Vendor: [Vishay Intertechnology, Inc](../../bindings.md#dt-vendor-vishay)

## Description

```text
VCNL36825T proximity and ambient light sensor.  See datasheet at
https://www.vishay.com/docs/84274/vcnl36825t.pdf
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `operation-mode` | `string` | ```text Mode of operation. - "auto": the sensor performs sampling continuously, - "force": the sampling is performed on every fetch command.  Defaults to sensor reset value. ```  Default value: `auto`  Legal values: `'auto'`, `'force'` |
| `measurement-period` | `int` | ```text Measurement period of the sensors in ms. Higher values yield lower power consumption. Note:   - [10, 80] ms only if low power mode is inactive   - [80, 320] ms only in low power mode  Defaults to 40 ms which is supported in both normal and low-power mode. ```  Default value: `40`  Legal values: `10`, `20`, `40`, `80`, `160`, `320` |
| `proximity-it` | `string` | ```text Proximity integration time in T. Defaults to sensor reset value. ```  Default value: `1`  Legal values: `'1'`, `'1.5'`, `'2'`, `'2.5'`, `'3'`, `'3.5'`, `'4'`, `'8'` |
| `proximity-itb` | `int` | ```text Duration of the proximity integration time T in us. Defaults to sensor reset value. ```  Default value: `25`  Legal values: `25`, `50` |
| `multi-pulse` | `int` | ```text Number of pulses per single measurement. Higher values increase accuracy and power consumption. Defaults to sensor reset value. ```  Default value: `1`  Legal values: `1`, `2`, `4`, `8` |
| `laser-current` | `int` | ```text Current used by the laser during measurement periods. Defaults to minimum allowed value. ```  Default value: `10`  Legal values: `10`, `12`, `14`, `16`, `18`, `20` |
| `low-power` | `boolean` | ```text Activate low power mode. This allows to increase the measurement period up to 320 ms. ``` |
| `high-gain` | `boolean` | ```text Activate the high gain mode. ``` |
| `sunlight-cancellation` | `boolean` | ```text Activate sunlight cancellation. ``` |
| `high-dynamic-output` | `boolean` | ```text Activate 16bit high dynamic output mode. Cannot be used with threshold interrupt. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “vishay,vcnl36825t” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
