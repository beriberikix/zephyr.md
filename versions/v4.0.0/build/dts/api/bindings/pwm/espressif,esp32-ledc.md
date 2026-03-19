---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pwm/espressif,esp32-ledc.html
original_path: build/dts/api/bindings/pwm/espressif,esp32-ledc.html
---

# espressif,esp32-ledc

Vendor: [Espressif Systems](../../bindings.md#dt-vendor-espressif)

Note

An implementation of a driver matching this compatible is available in
[drivers/pwm/pwm\_led\_esp32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/pwm_led_esp32.c).

## Description

```text
Espressif's LEDC controller Node

The LEDC controller is primarily designed to control the intensity of LEDs, although it can be
used to generate PWM signals for other purposes as well.

The mapping between the channel and GPIO is done through pinctrl

  &ledc0 {
    pinctrl-0 = <&ledc0_default>;
    pinctrl-names = "default";
  }

The 'ledc0_default' node state is defined in <board>-pinctrl.dtsi.

  ledc0_default: ledc0_default {
          group1 {
                  pinmux = <LEDC_CH0_GPIO0>,
                           <LEDC_CH1_GPIO2>,
                           <LEDC_CH2_GPIO4>;
                  output-enable;
          };
  };

If another GPIO mapping is desired, check if <board>-pinctrl.dtsi already have it defined,
otherwise, define the required mapping at your own application folder into a custom
<board>.overlay file.
The 'pinmux' property uses a macro defined in
https://github.com/zephyrproject-rtos/hal_espressif/tree/zephyr/include/dt-bindings/pinctrl
Before including a new node, check if the desired mapping is available according to the SoC.

As an example, the 'ledc0_custom' state below illustrates an alternate mapping using another set
of channels and pins in a custom overlay file.

  &pinctrl {

          ledc0_custom:  ledc0_custom {
                  group1 {
                          pinmux = <LEDC_CH0_GPIO0>,
                                   <LEDC_CH9_GPIO2>,
                                   <LEDC_CH10_GPIO4>;
                          output-enable;
                  };
           };

  };

Use the child bindings to configure the desired channel:

  &ledc0 {
    pinctrl-0 = <&ledc0_custom>;
    pinctrl-names = "default";
    status = "okay";
    #address-cells = <1>;
    #size-cells = <0>;
    channel0@0 {
      reg = <0x0>;
      timer = <0>;
    };
    channel9@9 {
      reg = <0x9>;
      timer = <0>;
    };
    channel10@a {
      reg = <0xa>;
      timer = <1>;
    };
  };

  Note: The channel's 'reg' property defines the ID of the channel. It must match the channel used
    in the 'pinmux'.
```

## Properties

### Top level properties

These property descriptions apply to “espressif,esp32-ledc”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#pwm-cells` | `int` | ```text Number of items to expect in a pwm specifier ```  This property is **required**.  Constant value: `3` |
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
may apply to the “espressif,esp32-ledc” compatible.

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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `int` | ```text The ESP32 has 8 low speed channel and 8 high speed channels. The low speed channel are mapped from channel 0 to 7, and the high speed are mapped from channel 8 to 15.  High speed channels are only available in the ESP32 SoC. ESP32S2 and ESP32S3 have 8 available channels, and ESP32C3 has 6. In these SoCs there is no differentiation between low or high speed. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `timer` | `int` | ```text Timer selection. For maximum flexibility, the high-speed as well as the low-speed channels can be driven from one of four high-speed/low-speed timers. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |

## Specifier cell names

- pwm cells: channel, period, flags
