---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/input/st,stmpe811.html
original_path: build/dts/api/bindings/input/st,stmpe811.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# st,stmpe811 (on i2c bus)

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STMPE811 I2C touchscreen controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `int-gpios` | `phandle-array` | ```text Interrupt GPIO. Used by the controller to signal touch data is available. Active low. ``` |
| `screen-width` | `int` | ```text Screen width for scaling the reported coordinates. Default: raw touchscreen resolution. ``` |
| `screen-height` | `int` | ```text Screen height for scaling the reported coordinates. Default: raw touchscreen resolution. ``` |
| `raw-x-min` | `int` | ```text Signed raw X axis start for scaling the reported coordinates. No effect if screen size is not set. ``` |
| `raw-y-min` | `int` | ```text Signed raw Y axis start for scaling the reported coordinates. No effect if screen size is not set. ``` |
| `raw-x-max` | `int` | ```text Raw X axis end for scaling the reported coordinates. No effect if screen size is not set. ``` |
| `raw-y-max` | `int` | ```text Raw Y axis end for scaling the reported coordinates. No effect if screen size is not set. ``` |
| `panel-driver-settling-time-us` | `int` | ```text Panel driver settling time (microseconds). For large panels (> 6"), a capacitor of 10 nF is recommended at the touchscreen terminals for noise filtering. As a general rule, 1-5 nF capacitors require around 500 us settling time, and 5-10 nF need around 1 ms. When a larger capacitor is used, this value should be changed, as it can lead to inaccuracy of the measurement. ```  This property is **required**.  Legal values: `10`, `100`, `500`, `1000`, `5000`, `10000`, `50000`, `100000` |
| `touch-detect-delay-us` | `int` | ```text Touch detect delay (microseconds) is the delay from the activation of the pull-up resistor in the X+ line to the time the device performs touch detection. If no capacitor, or a smaller capacitor is used, this value can be lowered to minimize detection latency, but it could lower the position stability. ```  This property is **required**.  Legal values: `10`, `50`, `100`, `500`, `1000`, `5000`, `10000`, `50000` |
| `touch-average-control` | `int` | ```text Average control (number of samples). This parameter can be set to any of the possible values. Higher values result in more filtering of noise, but also introduce more latency in the touch detection process.  Use cases that require low touch detection latency may benefit from using a lower value for this parameter, at the cost of less noise filtering. ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8` |
| `tracking-index` | `int` | ```text Tracking index determines the minimal distance between the current touch position and the previous touch position. If the distance is shorter than the tracking index, it is discarded. Lowering the tracking index increases the frequency of touch events, but also increases the load on the system. ```  This property is **required**.  Legal values: `0`, `4`, `8`, `16`, `32`, `64`, `92`, `127` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stmpe811” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
