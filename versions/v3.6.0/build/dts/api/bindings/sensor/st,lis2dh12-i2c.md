---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/sensor/st,lis2dh12-i2c.html
original_path: build/dts/api/bindings/sensor/st,lis2dh12-i2c.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# st,lis2dh12 (on i2c bus)

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STMicroelectronics LIS2DH12 3-axis accelerometer
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `irq-gpios` | `phandle-array` | ```text The INT1 and (optional) INT2 signal connections.  These signals are active-high as produced by the sensor. ``` |
| `int1-gpio-config` | `int` | ```text Select the interrupt configuration for INT1 gpio.  The default of 0 is the most common situation to avoid multiple interrupts to be triggered by same event.  - 0 # LIS2DH_DT_GPIO_INT_EDGE - 1 # LIS2DH_DT_GPIO_INT_EDGE_RISING - 2 # LIS2DH_DT_GPIO_INT_EDGE_FALLING - 3 # LIS2DH_DT_GPIO_INT_LEVEL_HIGH - 4 # LIS2DH_DT_GPIO_INT_LEVEL_LOW ```  Legal values: `0`, `1`, `2`, `3`, `4` |
| `int2-gpio-config` | `int` | ```text Select the interrupt configuration for INT2 gpio.  The default of 0 is the most common situation to avoid multiple interrupts to be triggered by same event.  - 0 # LIS2DH_DT_GPIO_INT_EDGE - 1 # LIS2DH_DT_GPIO_INT_EDGE_RISING - 2 # LIS2DH_DT_GPIO_INT_EDGE_FALLING - 3 # LIS2DH_DT_GPIO_INT_LEVEL_HIGH - 4 # LIS2DH_DT_GPIO_INT_LEVEL_LOW ```  Legal values: `0`, `1`, `2`, `3`, `4` |
| `disconnect-sdo-sa0-pull-up` | `boolean` | ```text Indicates the device driver should disconnect SDO/SA0 pull-up during device initialization (e.g. to save current leakage). Note that only subset of devices supported by this binding have SDO/SA0 pull-up (e.g. LIS2DH12, LIS3DH). ``` |
| `anym-on-int1` | `boolean` | ```text Indicates that the device driver should use interrupt 1 for any movement. This is for boards that only have one interrupt line connected from the sensor to the processor. ``` |
| `anym-no-latch` | `boolean` | ```text Disable the latching of interrupts for any movement. ``` |
| `anym-mode` | `int` | ```text Select the interrupt mode for any movement.  The default of 0 is the power-on-reset value.  - 0 # LIS2DH_DT_ANYM_OR_COMBINATION - 1 # LIS2DH_DT_ANYM_6D_MOVEMENT - 2 # LIS2DH_DT_ANYM_AND_COMBINATION - 3 # LIS2DH_DT_ANYM_6D_POSITION ```  Legal values: `0`, `1`, `2`, `3` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,lis2dh12” compatible.

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
