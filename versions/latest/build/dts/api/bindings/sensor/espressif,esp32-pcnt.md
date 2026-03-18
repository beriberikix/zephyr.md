---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/sensor/espressif,esp32-pcnt.html
original_path: build/dts/api/bindings/sensor/espressif,esp32-pcnt.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# espressif,esp32-pcnt

Vendor: [Espressif Systems](../../bindings.md#dt-vendor-espressif)

## Description

```text
Espressif's Pulse Counter Mode (PCNT) controller Node

The pulse counter module is designed to count the number of
rising and/or falling edges of an input signal.

The ESP32's PCNT module has 8 independent counting “units” numbered from 0 to 7.
ESP32S2 and ESP32S3 have 4 independent counting “units” numbered from 0 to 3.

Each pulse counter unit has a 16-bit signed counter register.

Each unit has two independent channel: ch0 and ch1 that can be configured
to either increment or decrement the counter.

Each channel has two inputs: a signal input that accepts signal edges
to be detected, as well as a control input that can be used to enable
or disable the signal input.

Each pulse counter unit also features a filter on each of the four inputs,
adding the option to ignore short glitches in the signals.

By combining the usage of both signal and control inputs, a PCNT unit can
act as a quadrature decoder.

Example: Use PCNT to read a rotary-enconder

The mapping between signal and control input and the pin is done through pinctrl:

  &pinctrl {
      pcnt_default: pcnt_default {
          group1 {
              pinmux = <PCNT0_CH0SIG_GPIO14>,
                      <PCNT0_CH0CTRL_GPIO15>;
              bias-pull-up;
          };
      };
  };

Note: Check espressif,esp32-pinctrl.yaml for complete documentation regarding pinctrl.

Use the PCNT node to configure the module:

  &pcnt {
    pinctrl-0 = <&pcnt_default>;
    pinctrl-names = "default";
    status = "okay";
    #address-cells = <1>;
    #size-cells = <0>;
    unit0@0 {
      reg = <0>;
      #address-cells = <1>;
      #size-cells = <0>;
      filter = <100>;
      channelA@0 {
          reg = <0>;
          sig-pos-mode = <2>;
          sig-neg-mode = <1>;
          ctrl-h-mode = <0>;
          ctrl-l-mode = <1>;
      };
    };
  };
```

## Properties

### Top level properties

These property descriptions apply to “espressif,esp32-pcnt”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “espressif,esp32-pcnt” compatible.

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
| `reg` | `int` | ```text The PCNT unit index. The ESP32 has 8 PCNT units. ESP32S2/S3 have 4 PCNT units. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `filter` | `int` | ```text Pulse length (ns) to be ignored ``` |

### Grandchild node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `int` | ```text The PCNT channel index. ```  This property is **required**.  Legal values: `0`, `1`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `sig-pos-mode` | `int` | ```text Define what to do on the positive edge of pulse input. 0 (Default) - Inhibit counter (counter value will not change in this condition). 1 - Increase counter value. 2 - Decrease counter value. ```  Legal values: `0`, `1`, `2` |
| `sig-neg-mode` | `int` | ```text Define what to do on the negative edge of pulse input. 0 (Default) - Inhibit counter (counter value will not change in this condition). 1 - Increase counter value. 2 - Decrease counter value. ```  Legal values: `0`, `1`, `2` |
| `ctrl-h-mode` | `int` | ```text Define what to do when the control input is high. 0 (Default) - Don't change counter mode. 1 - Invert counter mode(increase -> decrease, decrease -> increase). 2 - Control mode: Inhibit counter (counter value will not change in this condition). ```  Legal values: `0`, `1`, `2` |
| `ctrl-l-mode` | `int` | ```text Define what to do when the control input is low. 0 (Default) - Don't change counter mode. 1 - Invert counter mode(increase -> decrease, decrease -> increase). 2 - Control mode: Inhibit counter (counter value will not change in this condition). ```  Legal values: `0`, `1`, `2` |
