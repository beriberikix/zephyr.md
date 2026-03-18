---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/sensor/adi,adltc2990.html
original_path: build/dts/api/bindings/sensor/adi,adltc2990.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# adi,adltc2990 (on i2c bus)

Vendor: [Analog Devices, Inc.](../../bindings.md#dt-vendor-adi)

## Description

```text
ADLTC2990 Quad I2C Voltage, Current and Temperature Monitor
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `temperature-format` | `int` | ```text Define the temperature format. As per the datasheet, b7 Temperature Format Temperature Reported In; Celsius = 0 (Default), Kelvin = 1 ```  Legal values: `0`, `1` |
| `acquistion-format` | `int` | ```text Define the acquisition format. As per the datasheet, b6 Repeat/Single Repeated Acquisition = 0 (Default), Single Acquisition = 1 ```  Legal values: `0`, `1` |
| `measurement-mode` | `array` | ```text An array of two integers for configuring the chip measurement mode.  The first integer defines the bits 2..0 in the control register. In all cases the internal temperature and supply voltage are measured. In addition the following input measurements are enabled per mode: As per the datasheet, ------------------------------------------- b[2:0] | Mode [2:0] | Mode Description    0   |  0 0 0     | V1, V2, TR2 (Default)    1   |  0 0 1     | V1 – V2, TR2    2   |  0 1 0     | V1 – V2, V3, V4    3   |  0 1 1     | TR1, V3, V4    4   |  1 0 0     | TR1, V3 – V4    5   |  1 0 1     | TR1, TR2    6   |  1 1 0     | V1 – V2, V3 – V4    7   |  1 1 1     | V1, V2, V3, V4 ------------------------------------------- The second integer defines the bits 4..3 in the control register. This allows a subset of the measurements to be enabled: As Per the Datasheet, ------------------------------------------------------------ b[4:3] | Mode [4:3] | Mode Description    0   |  0 0       | Internal Temperature Only (Default)    1   |  0 1       | TR1, V1 or V1 – V2 Only per Mode [2:0]    2   |  1 0       | TR2, V3 or V3 – V4 Only per Mode [2:0]    3   |  1 1       | All Measurements per Mode [2:0] ------------------------------------------------------------ ```  Default value: `[0, 0]` |
| `pins-v1-v2-current-resistor` | `int` | ```text Define the resistor to be used for measuring current in microohms ``` |
| `pin-v1-voltage-divider-resistors` | `array` | ```text Define the resistor to be used for measuring Vout in milliohms ``` |
| `pin-v2-voltage-divider-resistors` | `array` | ```text Define the resistor to be used for measuring Vout in milliohms ``` |
| `pins-v3-v4-current-resistor` | `int` | ```text Define the resistor to be used for measuring current in microohms ``` |
| `pin-v3-voltage-divider-resistors` | `array` | ```text Define the resistor to be used for measuring Vout in milliohms ``` |
| `pin-v4-voltage-divider-resistors` | `array` | ```text Define the resistor to be used for measuring Vout in milliohms ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “adi,adltc2990” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
