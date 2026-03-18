---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/pwm/infineon,xmc4xxx-ccu4-pwm.html
original_path: build/dts/api/bindings/pwm/infineon,xmc4xxx-ccu4-pwm.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# infineon,xmc4xxx-ccu4-pwm

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

## Description

```text
Infineon XMC4XXX PWM Capture Compare Unit 4 (CCU4) module

The are four CCU4 modules with dts node labels:
pwm_ccu40, pwm_ccu41, pwm_ccu42, pwm_ccu43.
Each module has four slices and each slice has one channel.
A channel is connected to a particular gpio pin, which are defined
using pinctrl in:
dts/arm/infineon/xmc4xxx_xxx-pinctrl.dtsi

The CCU4 modules uses the CCU clock source. Each slice applies a separate
prescalar which divides the clock.

Device tree example:
A node can define a 'pwm' field, usually referenced in a 'pwms'
property, where the entries include the PWM module phandle,
channel number, pulse period (in nanoseconds or set using
PWM_XX() macros), and a channela
flag (PWM_POLARITY_NORMAL/PWM_POLARITY_INVERTED).

The pwm ccu4 node must define the slice-prescaler values and the pinctrl nodes:
&pwm_ccu40 {
    slice-prescaler = <15 15 15 15>;
    pinctrl-0 = <&pwm_out_p1_1_ccu40_ch2>;
    pinctrl-names = "default";
};

Another node can reference the PWM as follows:
&test_node {
   ...
   pwms = <&pwm_ccu40 0 PWM_SEC(1) PWM_POLARITY_NORMAL>;
   ...
};

The user must also explicitly set pinctrl properties.
The pin should be configured with drive-push-pull bool option and hwctrl should be set
to disabled. The drive-strength field can be set to any of the supported values:
&pwm_out_p1_1_ccu40_ch2 {
    drive-strength = "strong-medium-edge";
    drive-push-pull;
    hwctrl = "disabled";
};

The CCU4 pinctrl nodes have a node labels in the format
pwm_out_p{PORT}_{PIN}_ccu4{MODULE_IDX}_ch{CHANNEL_IDX}, where MODULE_IDX and
CHANNEL_IDX refers to specific pwm_ccu4x module and channel, respectively.
PORT/PIN pair defines what gpio the channel connects to.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `slice-prescaler` | `array` | ```text Defines the clock divider for each channel. The entry in the array will divide CCU clock by (2 << value). The range for the prescaler values is [0, 15]. Reducing prescaler value will improve resolution but decrease the maximum period. ```  This property is **required**. |
| `#pwm-cells` | `int` | ```text Number of items to expect in a pwm specifier ```  This property is **required**.  Constant value: `3` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,xmc4xxx-ccu4-pwm” compatible.

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

## Specifier cell names

- pwm cells: channel, period, flags
