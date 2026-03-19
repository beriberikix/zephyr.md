---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/clock/st,stm32-rcc.html
original_path: build/dts/api/bindings/clock/st,stm32-rcc.html
---

# st,stm32-rcc

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32 Reset and Clock controller node.
This node is in charge of system clock ('SYSCLK') source selection and controlling
clocks for AHB (Advanced High Performance) and APB (Advanced Peripheral) bus domains.

Configuring STM32 Reset and Clock controller node:

System clock source should be selected amongst the clock nodes available in "clocks"
node (typically 'clk_hse, clk_hsi', 'pll', ...).
Core clock frequency should also be defined, using "clock-frequency" property.
Note:
        Core clock frequency  = SYSCLK / AHB prescaler
Last, peripheral bus clocks (typically PCLK1, PCLK2) should be configured using matching
prescaler properties.
Here is an example of correctly configured rcc node:
&rcc {
         clocks = <&pll>;  /* Select 80MHz pll as SYSCLK source */
         ahb-prescaler = <2>;
         clock-frequency = <DT_FREQ_M(40)>; /* = SYSCLK / AHB prescaler */
         apb1-presacler = <1>;
         apb2-presacler = <1>;
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
The gated clock is required when accessing to the peripheral controller is needed
(generally for configuring the device). If dual clock domain is not used, it is
also used for peripheral operation.

Specifying a domain clock source:

Specifying a domain source clock could be done by adding a clock specifier to the
clock property:
... {
         ...
         clocks = <&rcc STM32_CLOCK_BUS_APB2 0x00000020>,
                      <&rcc STM32_SRC_HSI I2C1_SEL(2)>;
         ...
}
In this example, I2C1 device is assigned HSI as domain clock source.
Domain clock is independent from the bus/gated clock and allows access to the device's
register while the gated clock is off. As it doesn't feed the peripheral's controller, it
allows peripheral operation, but can't be used for peripheral configuration.
It is peripheral driver's responsibility to query and use clock source information in
accordance with clock_control API specifications.

Since the peripheral subsystem rate is dictated by the clock used for peripheral
operation, same clock should be used in calls to `clock_control_get_rate()`

Note 1: No additional specifier means gating clock is also the clock source (ie
        'PCLK/PCLK1/PCLK2' depending on the device). There is no need to add a second
        cell to explicitly set it.
Note 2: Default peripheral clock configuration (ie the one provided in *.dsti files)
        should be the one matching SoC reset state. Confere reference manual to check
        what is the reset value of the clock source for each peripheral.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**.  Constant value: `2` |
| `clock-frequency` | `int` | ```text default frequency in Hz for clock output ```  This property is **required**. |
| `ahb-prescaler` | `int` | ```text AHB prescaler. Defines actual core clock frequency (HCLK) based on system frequency input. The HCLK clocks CPU, AHB, memories and DMA. ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16`, `64`, `128`, `256`, `512` |
| `apb1-prescaler` | `int` | This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `apb2-prescaler` | `int` | This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `undershoot-prevention` | `boolean` | ```text On some parts, it could be required to set up highest core frequencies (>80MHz) in two steps in order to prevent undershoot. This is done by applying an intermediate AHB prescaler before switching System Clock source to PLL. Once done, prescaler is set back to expected value. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-rcc” compatible.

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

- clock cells: bus, bits
