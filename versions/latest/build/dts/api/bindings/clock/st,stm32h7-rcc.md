---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/clock/st,stm32h7-rcc.html
original_path: build/dts/api/bindings/clock/st,stm32h7-rcc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# st,stm32h7-rcc

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32 Reset and Clock controller node for STM32H7 devices
This node is in charge of system clock ('SYSCLK') source selection and
System Clock Generation.

Configuring STM32 Reset and Clock controller node:

System clock source should be selected amongst the clock nodes available in "clocks"
node (typically 'clk_hse, clk_csi', 'pll', ...).
As part of this node configuration, SYSCLK frequency should also be defined, using
"clock-frequency" property.
Last, bus clocks (typically HCLK, PCLK1, PCLK2) should be configured using matching
prescaler properties.
Here is an example of correctly configured rcc node:
&rcc {
         clocks = <&pll>;  /* Set pll as SYSCLK source */
         clock-frequency = <DT_FREQ_M(480)>; /* SYSCLK runs at 480MHz */
         d1cpre = <1>;
         hpre = <1>;
         d1ppre = <1>;
         d2ppre1 = <1>;
         d2ppre2 = <1>;
         d3ppre = <1>;
}

Confere st,stm32-rcc binding for information about domain clocks configuration.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**.  Constant value: `2` |
| `clock-frequency` | `int` | ```text default frequency in Hz for clock output ```  This property is **required**. |
| `d1cpre` | `int` | ```text D1 Domain, CPU1 clock prescaler. Sets a HCLK frequency (feeding Cortex-M Systick) lower than SYSCLK frequency (actual core frequency). Zephyr doesn't make a difference today between these two clocks. Changing this prescaler is not allowed until it is made possible to use them independently in Zephyr clock subsystem. ```  This property is **required**.  Legal values: `1` |
| `hpre` | `int` | ```text D2 domain, CPU2 core clock and AHB(1/2/3/4) peripheral prescaler ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16`, `64`, `128`, `256`, `512` |
| `d1ppre` | `int` | ```text D1 domain, APB3 peripheral prescaler ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `d2ppre1` | `int` | ```text D2 domain, APB1 peripheral prescaler ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `d2ppre2` | `int` | ```text D2 domain, APB2 peripheral prescaler ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `d3ppre` | `int` | ```text D3 domain, APB4 peripheral prescaler ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32h7-rcc” compatible.

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
