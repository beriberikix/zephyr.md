---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pwm/infineon,xmc4xxx-ccu8-pwm.html
original_path: build/dts/api/bindings/pwm/infineon,xmc4xxx-ccu8-pwm.html
---

# infineon,xmc4xxx-ccu8-pwm

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

Note

An implementation of a driver matching this compatible is available in
[drivers/pwm/pwm\_xmc4xxx\_ccu8.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/pwm_xmc4xxx_ccu8.c).

## Description

```text
Infineon XMC4XXX PWM Capture Compare Unit 8 (CCU8) module

The PWM CCU8 module can automatically generate a high-side
and a low-side PWM signal, where the two signals are complementary
to each other.

The module supports adding a dead time between the high-side and
low-side PWM signals.

The dead time ensures that there is a delay before the PWM state
transitions from 0 to 1, preventing the high-side and low-side
switches from being on simultaneously.

There are two CCU8 modules with DTS node labels: pwm_ccu80 and
pwm_ccu81. Each module has four slices, and each slice has
two channels. A channel consists of a corresponding high-side
and low-side PWM signal.

The CCU8 modules use the CCU clock source. Each slice applies
a separate prescaler to divide the clock. The clock divider is
defined by the 'slice-prescaler' property. Additionally, each
slice has a dead time prescaler, which divides the slice clock
for the dead time counter.

Device tree example:
A node can define a 'pwm' field, usually referenced in a 'pwms'
property, where the entries include the PWM module phandle,
channel number, pulse period (in nanoseconds or set using
PWM_XX() macros), and a channel
flag (PWM_POLARITY_NORMAL/PWM_POLARITY_INVERTED).

The 'pwm_ccu8' node must define the following fields:
&pwm_ccu80 {
        slice-prescaler = <15 15 15 15>;
        slice-deadtime-prescaler = <3 3 3 3>;
        channel-deadtime-high = <0 0 0 0 PWM_MSEC(100) 0 0 0>;
        channel-deadtime-low = <0 0 0 0 PWM_MSEC(100) 0 0 0>;
        pinctrl-0 = <&pwm_out_p5_9_ccu80_ch4_high &pwm_out_p0_0_ccu80_ch4_low>;
        pinctrl-names = "default";
};

This will configure channel 4 with a 100msec deadtime on the high
and low side PWM signals.

Another node can reference the PWM as follows:
&test_node {
   ...
   pwms = <&pwm_ccu80 0 PWM_SEC(1) PWM_POLARITY_NORMAL>;
   ...
};

The 'pwm_out_p{PORT}_{PIN}_ccu8{MODULE_IDX}_ch{CHANNEL_IDX}_{HIGH_LOW}'
format is used for CCU8 pinctrl nodes. 'MODULE_IDX' and 'CHANNEL_IDX'
refer to a specific 'pwm_ccu8x' module and channel, respectively.
'PORT/PIN' defines the GPIO that the channel connects to.
'HIGH_LOW' indicates whether the pin is for the high or low-side signal.

It's not necessary to specify both the high and low pinctrls. Only the low-side
signal can, for example, be used as PWM, but note that the duty cycle of the
low signal will be (1 - duty) as set via the API.

Note that a slice has two channels. Channels 0/1 are in slice 0,
channels 2/3 are in slice 1, and so on. Each channel can have its own
duty cycle and high/low dead times. But the pulse duration applies to
both channels. Thus, when using the PWM control api to modify the pulse width
on a channel 0, it will also be updated for channel 1 since they are
in the same slice.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `slice-prescaler` | `array` | ```text Defines the clock divider for each slice. The entry in the array will divide CCU clock by (2 << value). The range for the prescaler values is [0, 15]. Reducing prescaler value will improve resolution but decrease the maximum period. ```  This property is **required**. |
| `slice-deadtime-prescaler` | `array` | ```text Defines the clock divider for dead time counter for each slice. The range for the values is [0, 3]. Reducing prescaler value will improve dead time resolution but decrease the maximum dead time. ```  This property is **required**. |
| `channel-deadtime-high` | `array` | ```text Defines the dead time in nanoseconds for the high-side PWM signal for each channel. ```  This property is **required**. |
| `channel-deadtime-low` | `array` | ```text Defines the dead time in nanoseconds for the low-side PWM signal for each channel. ```  This property is **required**. |
| `#pwm-cells` | `int` | ```text Number of items to expect in a pwm specifier ```  This property is **required**.  Constant value: `3` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,xmc4xxx-ccu8-pwm” compatible.

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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

## Specifier cell names

- pwm cells: channel, period, flags
