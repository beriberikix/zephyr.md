---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/pwm/nxp,s32-emios-pwm.html
original_path: build/dts/api/bindings/pwm/nxp,s32-emios-pwm.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nxp,s32-emios-pwm

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
NXP S32 eMIOS PWM node for S32 SoCs. Each channel in eMIOS can be configured
to use for PWM operation. There are several PWM modes supported by this module,
some modes only support on channels that have internal counter, some modes
require to use a reference timebase from a master bus.

For example to configuring eMIOS instance 0 with:
  - Channel 0 for mode OPWFMB
  - Channel 1 for mode OPWMB
  - Channel 2 for mode OPWMCB with deadtime inserted at leading edge
  - Channel 3 for mode SAIC, use internal timebase with input filter = 2 eMIOS clock

  emios0_pwm: pwm {
    pwm_0 {
      channel = <0>;
      pwm-mode = "OPWFMB";
      prescaler = <8>;
      period = <65534>;
      duty-cycle = <32768>;
      polarity = "ACTIVE_HIGH";
    };

    pwm_1 {
      channel = <1>;
      master-bus = <&emios1_bus_a>;
      pwm-mode = "OPWMB";
      duty-cycle = <32768>;
      phase-shift = <100>;
      polarity = "ACTIVE_LOW";
    };

    pwm_2 {
      channel = <2>;
      master-bus = <&emios1_bus_b>;
      pwm-mode = "OPWMCB_LEAD_EDGE";
      duty-cycle = <32768>;
      dead-time = <100>;
      polarity = "ACTIVE_LOW";
    };

    pwm_3 {
      channel = <3>;
      pwm-mode = "SAIC";
      prescaler = <8>;
      input-filter = <2>;
    };
  };

OPWMB and OPWMCB modes use reference timebase, the master bus is chosen over
phandle 'master-bus'. For OPWMB mode, PWM's period is master bus's period and
is 2 * master bus's period - 2 for OPWMCB mode. Please notice that the devicetree
node for master bus should be enabled and configured for using, please see
'nxp,s32-emios' bindings.
```

## Properties

### Top level properties

These property descriptions apply to “nxp,s32-emios-pwm”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `#pwm-cells` | `int` | ```text Number of items to expect in a pwm specifier ```  This property is **required**.  Constant value: `3` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,s32-emios-pwm” compatible.

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
| `channel` | `int` | ```text eMIOS PWM channel ```  This property is **required**. |
| `master-bus` | `phandle` | ```text A phandle to master-bus node that will be used as external timebase for current channel, this can be bypassed if internal counter is used for PWM operation. A master bus must be used exclusively, such as if is used as a timebase for a channel in SAIC mode, do not use that master bus as a timebase for generate PWM pulse. ``` |
| `pwm-mode` | `string` | ```text Select PWM mode: - OPWFMB: provides waveforms with variable duty cycle and frequency,           this mode uses internal counter.  - OPWMB:  generate pulses with programmable leading and trailing           edge placement. The period is determined by period of           an external counter driven in MCB Up Mode. Changing PWM period           at runtime will impact to all channels share the same timebase.           The new period and cycle take effect in next period boundary.  - OPWMCB: generates a center aligned PWM with dead time insertion to the           leading or trailing edge. The period is determined by period of           an external counter driven in MCB Up Down Mode. Changing PWM period           at runtime will impact to all channels share the same timebase,           The new period and cycle take effect in next period boundary.  - SAIC: single action input capture mode, the eMIOS captures events as soon as         they occur. The value of latest captured event is stored and can be read         by software. ```  This property is **required**.  Legal values: `'OPWFMB'`, `'OPWMB'`, `'OPWMCB_TRAIL_EDGE'`, `'OPWMCB_LEAD_EDGE'`, `'SAIC'` |
| `polarity` | `string` | ```text Output polarity for PWM channel. ```  Legal values: `'ACTIVE_LOW'`, `'ACTIVE_HIGH'` |
| `duty-cycle` | `int` | ```text Duty-cycle (in ticks) for PWM channel at boot time. ``` |
| `period` | `int` | ```text Period (in ticks) for OPWFMB at boot time. Period for the rest of PWM mode depends on period's master bus. Must be in range [2 ... 65535]. ``` |
| `freeze` | `boolean` | ```text Freeze individual internal counter when the chip enters Debug mode. ``` |
| `prescaler-src` | `string` | ```text Select clock source for internal counter prescaler. ```  Default value: `PRESCALED_CLOCK`  Legal values: `'PRESCALED_CLOCK'`, `'MODULE_CLOCK'` |
| `prescaler` | `int` | ```text The clock divider for internal counter prescaler. ```  Legal values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16` |
| `dead-time` | `int` | ```text Dead time (in ticks) for PWM channel in OPWMCB mode. ``` |
| `phase-shift` | `int` | ```text Phase Shift (in ticks) for PWM channel in OPWMB mode. ``` |
| `input-filter` | `int` | ```text Select the minimum input pulse width, in filter clock cycles that can pass through the input filter. The filter latency - the difference in time between the input and the response is three clock edges. Default 0 means the filter is bypassed. The clock source for programmable input filter is eMIOS clock. ```  Legal values: `0`, `2`, `4`, `8`, `16` |

## Specifier cell names

- pwm cells: channel, period, flags
