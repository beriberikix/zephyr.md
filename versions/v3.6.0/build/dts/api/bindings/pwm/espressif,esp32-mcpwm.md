---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/pwm/espressif,esp32-mcpwm.html
original_path: build/dts/api/bindings/pwm/espressif,esp32-mcpwm.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# espressif,esp32-mcpwm

Vendor: [Espressif Systems](../../bindings.md#dt-vendor-espressif)

## Description

```text
Espressif's Motor Control Pulse Width Modulator (MCPWM) controller Node

The MCPWM peripheral is intended for motor and power control.
It provides six PWM outputs that can be set up to operate in several topologies

ESP32 contains two MCPWM peripherals: MCPWM0 and MCPWM1

Each MCPWM peripheral has one clock divider (prescaler), three PWM timers, three PWM operators,
and a capture module.

Every PWM operator has two PWM outputs: PWMxA and PWMxB. They can work independently, in symmetric
and asymmetric configuration. MCPWMxA and MCPWMxB will share the same timer, thus having the same
operating frequency.

The driver currently always use the timer x for operator x. Timer 0 will use operator 0 for
PWM0A/B.
Timer 1 will use operator 1 for PWM1A/B, and so on.

Mapping channel ID:
Channel 0 -> Timer 0, Operator 0, output PWM0A
Channel 1 -> Timer 0, Operator 0, output PWM0B
Channel 2 -> Timer 1, Operator 1, output PWM1A
Channel 3 -> Timer 1, Operator 1, output PWM1B
Channel 4 -> Timer 2, Operator 2, output PWM2A
Channel 5 -> Timer 2, Operator 2, output PWM2B
Channel 6 -> Capture 0
Channel 7 -> Capture 1
Channel 8 -> Capture 2

Example: Use PWM0A output and capture 0:

pwm_loopback_0 {
  compatible = "test-pwm-loopback";
  pwms = <&mcpwm0 0 0 PWM_POLARITY_NORMAL>, #Channel 0 -> Output PWM0A
         <&mcpwm0 6 0 PWM_POLARITY_NORMAL>; #Channel 6 -> Capture 0;
};

The mapping between the output PWMxA/B or CaptureX and GPIO is done through pinctrl:

  &mcpwm0 {
    pinctrl-0 = <&mcpwm0_default>;
    pinctrl-names = "default";
  }

The 'mcpwm0_default' node is defined inside the pinctrl node.

  &pinctrl {
    mcpwm0_default: mcpwm0_default {
      group1 {
        pinmux = <MCPWM0_OUT0A_GPIO0>,
          <MCPWM0_OUT0B_GPIO2>,
          <MCPWM0_OUT1A_GPIO4>;
        output-enable;
      };
      group2 {
        pinmux = <MCPWM0_CAP0_GPIO5>;
      };
    };
  };

Note: Check espressif,esp32-pinctrl.yaml for complete documentation regarding pinctrl.

Use the prescale-timerX property to configure the timers:

  &mcpwm0 {
    pinctrl-0 = <&mcpwm0_default>;
    pinctrl-names = "default";
    prescale = <255>;
    prescale-timer0 = <103>;
    prescale-timer1 = <0>;
    prescale-timer2 = <255>;
    status = "okay";
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `prescale` | `int` | ```text 8 bit timer prescale for the global clock. Period of PWM_clk = 6.25ns * (PWM_CLK_PRESCALE + 1). ```  This property is **required**. |
| `#pwm-cells` | `int` | ```text Number of items to expect in a pwm specifier ```  This property is **required**.  Constant value: `3` |
| `prescale-timer0` | `int` | ```text 8 bit timer prescale for timer 0. Period of PT0_clk = Period of PWM_clk * (PWM_TIMER0_PRESCALE + 1). ``` |
| `prescale-timer1` | `int` | ```text 8 bit timer prescale for timer 1. Period of PT1_clk = Period of PWM_clk * (PWM_TIMER1_PRESCALE + 1). ``` |
| `prescale-timer2` | `int` | ```text 8 bit timer prescale for timer 2. Period of PT2_clk = Period of PWM_clk * (PWM_TIMER2_PRESCALE + 1). ``` |
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
may apply to the “espressif,esp32-mcpwm” compatible.

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

## Specifier cell names

- pwm cells: channel, period, flags
