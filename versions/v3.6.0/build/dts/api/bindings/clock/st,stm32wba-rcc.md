---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/clock/st,stm32wba-rcc.html
original_path: build/dts/api/bindings/clock/st,stm32wba-rcc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# st,stm32wba-rcc

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32 Reset and Clock controller node.
This node is in charge of system clock ('SYSCLK') source selection and controlling
clocks for AHB (Advanced High Performance) and APB (Advanced Peripheral) bus domains.

Configuring STM32 Reset and Clock controller node:

System clock source should be selected amongst the clock nodes available in "clocks"
node (typically 'clk_hse, clk_hsi', 'pll').
Core clock frequency should also be defined, using "clock-frequency" property.
Note:
        Core clock frequency  = SYSCLK / AHB prescaler
Last, peripheral bus clocks (typically PCLK1, PCLK2, PCLK7) should be configured using
matching prescaler properties.
Here is an example of correctly configured rcc node:
&rcc {
         clocks = <&pll>;                   /* Select pll as SYSCLK source */
         ahb-prescaler = <2>;
         clock-frequency = <DT_FREQ_M(40)>; /* = SYSCLK / AHB prescaler */
         apb1-presacler = <1>;
         apb2-presacler = <1>;
         apb7-presacler = <7>;
}

Specifying a gated clock:

To specify a gated clock, a peripheral should define a "clocks" property encoded
in the following way:
... {
         ...
         clocks = <&rcc STM32_CLOCK_BUS_APB2 0x00000020>;
         ...
}
After the phandle referring to rcc node, the first index specifies the registers of
the bus controlling the peripheral and the second index specifies the bit used to
control the peripheral clock in that bus register.

Specifying an alternate clock source:

Specifying an alternate source clock could be done by adding a clock specifier to the
clock property:
... {
         ...
         clocks = <&rcc STM32_CLOCK_BUS_APB2 0x00000020>,
                      <&rcc STM32_SRC_HSI I2C1_SEL(2)>;
         ...
}
In this example I2C1 device is assigned HSI as clock source.
It is device driver's responsibility to query and use clock source information in
accordance with clock_control API specifications.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**.  Constant value: `2` |
| `clock-frequency` | `int` | ```text default frequency in Hz for clock output (HCLK1) ```  This property is **required**. |
| `ahb-prescaler` | `int` | ```text Common AHB1, AHB2, AHB4 prescaler. Defines actual core clock frequency (HCLK) based on system frequency input. AKA HPRE. The HCLK clocks CPU, AHB1, AHB2, memories and DMA. ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `ahb5-prescaler` | `int` | ```text AHB5 prescaler. Defines actual core clock frequency (HCLK5) based on system frequency input. It is used to limit HCLK5 below 32MHz. Only required when SysClock source is PLL1. AKA HPRE5. ```  Legal values: `1`, `2`, `3`, `4`, `6` |
| `apb1-prescaler` | `int` | This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `apb2-prescaler` | `int` | This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `apb7-prescaler` | `int` | This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `ahb5-div` | `boolean` | ```text AHB5 divider. Applies only when SysClock source is HSI16 or HSE32. When enabled, AHB5 clock is SysClock / 2. When disabled, SysClock is not divided. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32wba-rcc” compatible.

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

- clock cells: bus, bits
