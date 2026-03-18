---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/pinctrl/ti,cc13xx-cc26xx-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/ti,cc13xx-cc26xx-pinctrl.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ti,cc13xx-cc26xx-pinctrl

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

## Description

```text
TI SimpleLink CC13xx / CC26xx pinctrl node.

Device pin configuration should be placed in the child nodes of this node.
Populate the 'pinmux' field with a pair consisting of a pin number and its IO
functions.

The node has the 'pinctrl' node label set in your SoC's devicetree,
so you can modify it like this:

  &pinctrl {
          /* your modifications go here */
  };

All device pin configurations should be placed in child nodes of the
'pinctrl' node, as in the i2c0 example shown at the end.

Here is a list of
supported standard pin properties:

- bias-disable: Disable pull-up/down.
- bias-pull-down: Enable pull-down resistor.
- bias-pull-up: Enable pull-up resistor.
- drive-open-drain: Output driver is open-drain.
- drive-open-drain: Output driver is open-source.
- drive-strength: Minimum current that can be sourced from the pin.
- input-enable: enable input.
- input-schmitt-enable: enable input schmitt circuit.
- ti,input-edge-detect: enable and configure edge detection interrupts

An example for CC13XX family, include the chip level pinctrl
DTSI file in the board level DTS:

  #include <dt-bindings/pinctrl/cc13xx_cc26xx-pinctrl.h>

We want to configure the I2C pins to open drain, with pullup enabled
and input enabled.

To change a pin's pinctrl default properties add a reference to the
pin in the board's DTS file and set the properties.

  &i2c0 {
    pinctrl-0 = <&i2c0_scl_default &i2c0_sda_default>;
    pinctrl-1 = <&i2c0_scl_sleep &i2c0_sda_sleep>;
    pinctrl-names = "default", "sleep";
  }

The i2c0_scl_default corresponds to the following in the board dts file:

  &pinctrl {
    i2c0_scl_default: i2c0_scl_default {
      pinmux = <4 IOC_PORT_MCU_I2C_MSSCL>;
      bias-pull-up;
      drive-open-drain;
      input-enable;
    };
  };

To configure an input pin with edge detection (e.g. to count pulses):

  &pinctrl {
    gpt0_edge_counter: gpt0_edge_counter {
      pinmux = <15 IOC_PORT_MCU_PORT_EVENT0>;
      input-enable;
      bias-pull-up;
      ti,input-edge-detect = <IOC_RISING_EDGE>;
    };
  };

To configure an output pin (e.g. for PWM output):

  &pinctrl {
    gpt0_pwm: gpt0_pwm {
      pinmux = <16 IOC_PORT_MCU_PORT_EVENT1>;
      bias-disable;
      drive-strength = <8>; /* in mA */
    };
  };
```

## Properties

### Top level properties

These property descriptions apply to “ti,cc13xx-cc26xx-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,cc13xx-cc26xx-pinctrl” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `pinmux` | `array` | ```text CC13XX/CC26XX pin's configuration (IO pin, IO function). ```  This property is **required**. |
| `drive-strength` | `int` | ```text The drive strength controls the minimum output driver strength of an I/O pin configured as an output.   2: min 2 mA (SoC default)   4: min 4 mA   8: min 8 mA for for double drive strength IOs, min 4 mA for normal IOs ```  Default value: `2`  Legal values: `2`, `4`, `8` |
| `ti,input-edge-detect` | `int` | ```text Enables or disables the edge detection interrupt and configures it:   IOC_NO_EDGE: No edge detection (SoC default)   IOC_FALLING_EDGE: Edge detection on falling edge   IOC_RISING_EDGE: Edge detection on rising edge   IOC_BOTH_EDGES: Edge detection on both edges ``` |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `drive-open-source` | `boolean` | ```text drive with open source (hardware OR) ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
| `input-schmitt-enable` | `boolean` | ```text enable schmitt-trigger mode ``` |
