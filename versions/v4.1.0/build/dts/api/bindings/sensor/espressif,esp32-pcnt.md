---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/sensor/espressif,esp32-pcnt.html
original_path: build/dts/api/bindings/sensor/espressif,esp32-pcnt.html
---

# espressif,esp32-pcnt

Vendor: [Espressif Systems](../../bindings.md#dt-vendor-espressif)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/espressif/pcnt\_esp32/pcnt\_esp32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/espressif/pcnt_esp32/pcnt_esp32.c).

## Description

```text
ESP32 Pulse Counter (PCNT)

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
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `dmas` | `phandle-array` | ```text DMA channel specifiers relevant to the device. ``` |
| `dma-names` | `string-array` | ```text Optional names given to the DMA channel specifiers in the "dmas" property. ``` |
| `io-channels` | `phandle-array` | ```text IO channel specifiers relevant to the device. ``` |
| `io-channel-names` | `string-array` | ```text Optional names given to the IO channel specifiers in the "io-channels" property. ``` |
| `mboxes` | `phandle-array` | ```text Mailbox / IPM channel specifiers relevant to the device. ``` |
| `mbox-names` | `string-array` | ```text Optional names given to the mbox specifiers in the "mboxes" property. ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers relevant to the device. ``` |
| `power-domain-names` | `string-array` | ```text Optional names given to the power domain specifiers in the "power-domains" property. ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

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
