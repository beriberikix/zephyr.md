---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/interrupt-controller/cypress,psoc6-intmux.html
original_path: build/dts/api/bindings/interrupt-controller/cypress,psoc6-intmux.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# cypress,psoc6-intmux

Vendor: [Cypress Semiconductor Corporation](../../bindings.md#dt-vendor-cypress)

## Description

```text
Cypress Interrupt Multiplex

The PSoC-6 Cortex-M0+ NVIC can handle up to 32 interrupts. This means that
user can select up to 32 interrupts sources from the 240 possible vectors
to be processed in the Cortex-M0+ CPU.

At CPU Sub System (CPUSS) there are 8 special registers (intmux[0~7]) to
configure the 32 NVIC lines for Cortex-M0+ CPU. Each register handles up to
4 interrupt sources by grouping intmux channels. These means that each byte
from intmux[0~7] store a 'vector number' which selects the peripheral
interrupt source in the multiplexer. The multiplexer is placed before
Cortex-M0+ NVIC controller. Note that Cortex-M4 have all interrupt sources
directly connected to NVIC and doesn't require any special configuration.

On a general view, the below represents the Interrupt Multiplexer
configuration and how the Cortex-M0+ NVIC sources are organized. Each
channel chX represents a Cortex-M0+ NVIC line and it stores a vector number.
The vector number selects the PSoC-6 peripheral interrupt source for the
Cortex-M0+ NVIC controller line.

intmux[0] = {ch03, ch02, ch01, ch00}
intmux[1] = {ch07, ch06, ch05, ch04}
...
intmux[7] = {ch31, ch30, ch29, ch28}

In practical terms, the Cortex-M0+ requires user to define all NVIC interrupt
sources and the proper NVIC interrupt order. With that, the system configures
the Cortex-M0+ Interrupt Multiplexer and interrupts can be processed.
More information about it at PSoC-6 Architecture Technical Reference Manual,
section CPU Sub System (CPUSS) Registers.

The below fragment configure the GPIO Port 0 to generate an interrupt at
Cortex-M0+ NVIC:

At psoc6.dtsi file the gpio_prt0 peripheral had the interrupt source 2:

gpio_prt0: gpio@40320100 {
  interrupts = <2 1>;
};

In order to enable gpio_prt0 interrupt at Cortex-M0+ an interrupt parent
must be defined at gpio_prt0 node selecting the Interrupt Multiplex Channel.
This can be defined at <board>_m0.dts file:

&gpio_prt0 {
  interrupt-parent = <&intmux_ch20>;
};

The translation of these two definitions is:
       CH   REGS  INT NUM    CH   CH/REG
intmux[20 mod 8] |= 0x02 << (20 mod 4);

These results in Cortex-M0+ NVIC line 20 handling PSoC-6 interrupt source 2.
The interrupt can be enabled/disabled at NVIC at line 20 as usual.

Notes:
1) Multiple definitions will generate multiple interrupts
2) The interrupt sources are shared between Cortex-M0+/M4. This means, they
   can trigger actions in parallel on both processors.
3) User can change priority at Cortex-M0+ NVIC by changing interrupt channels
   at interrupt-parent properties.
4) Only the peripherals used by Cortex-M0+ should be configured.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “cypress,psoc6-intmux” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
