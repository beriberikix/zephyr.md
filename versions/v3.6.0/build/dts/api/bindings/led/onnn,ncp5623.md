---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/led/onnn,ncp5623.html
original_path: build/dts/api/bindings/led/onnn,ncp5623.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# onnn,ncp5623 (on i2c bus)

Vendor: [ON Semiconductor Corp.](../../bindings.md#dt-vendor-onnn)

## Description

```text
NCP5623 Triple Output I2C Controlled RGB LED driver

The LED_SHELL application can be used for testing

The following example defines a single RGB LED in the ncp5623 DT node

ncp5623c@39 {
  compatible = "onnn,ncp5623";
  reg = <0x39>;

  led_0 {
    label = "RGB LED";
    index = <0>;
    color-mapping =
      <LED_COLOR_ID_RED>,
      <LED_COLOR_ID_GREEN>,
      <LED_COLOR_ID_BLUE>;
  };
};

The following example defines three single-channel LEDs in the ncp5623 DT node

ncp5623c@39 {
  compatible = "onnn,ncp5623";
  reg = <0x39>;

  led_0 {
    label = "RED LED";
    index = <0>;
    color-mapping =
      <LED_COLOR_ID_RED>;
  };

  led_1 {
    label = "GREEN LED";
    index = <1>;
    color-mapping =
      <LED_COLOR_ID_GREEN>;
  };

  led_2 {
    label = "BLUE LED";
    index = <2>;
    color-mapping =
      <LED_COLOR_ID_BLUE>;
  };
};
```

## Properties

### Top level properties

These property descriptions apply to “onnn,ncp5623”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “onnn,ncp5623” compatible.

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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `label` | `string` | ```text Human readable string describing the LED ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `index` | `int` | ```text Index of the LED on a controller. It can be used by drivers or applications to map a logical LED to its real position on the controller. For example, this allows to handle boards where the LEDs in an array/strip are not wired following the LED order of the controller. ```  This property is **required**. |
| `color-mapping` | `array` | ```text Channel to color mapping of a multicolor LED. If a LED supports several colors, then the color-mapping property can be used to describe how the hardware channels and the colors are mapped.  For example the channel to color mapping of RGB LEDs would be     color-mapping =         <LED_COLOR_ID_RED>,         <LED_COLOR_ID_GREEN>,         <LED_COLOR_ID_BLUE>; ```  This property is **required**. |
