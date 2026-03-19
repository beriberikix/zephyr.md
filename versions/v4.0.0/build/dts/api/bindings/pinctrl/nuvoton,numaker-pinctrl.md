---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/nuvoton,numaker-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/nuvoton,numaker-pinctrl.html
---

# nuvoton,numaker-pinctrl

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

Note

An implementation of a driver matching this compatible is available in
[drivers/pinctrl/pinctrl\_numaker.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_numaker.c).

## Description

```text
Pin controller is responsible for controlling pin function
selection and pin properties. For example, for example you can
use this node to set UART0 RX as pin PB12 to fulfill SYS_GPB_MFP3_PB12MFP_UART0_RXD.

The node has the 'pinctrl' node label set in your SoC's devicetree,
so you can modify it like this:

  &pinctrl {
          /* your modifications go here */
  };

All device pin configurations should be placed in child nodes of the
'pinctrl' node, as shown in this example:

  &pinctrl {
    /* configuration for the uart0 "default" state */
    uart0_default: uart0_default {
        /* configure PB13 as UART0 TX and PB12 as UART0 RX */
      group0 {
        pinmux = <PB12MFP_UART0_RXD>, <PB13MFP_UART0_TXD>;
      };
    };
  };

To link pin configurations with a device, use a pinctrl-N property for some
number N, like this example you could place in your board's DTS file:

  #include "board-pinctrl.dtsi"

  &uart0 {
      pinctrl-0 = <&uart0_default>;
      pinctrl-names = "default";
  };
```

## Properties

### Top level properties

These property descriptions apply to “nuvoton,numaker-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nuvoton,numaker-pinctrl” compatible.

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

### Grandchild node properties

| Name | Type | Details |
| --- | --- | --- |
| `pinmux` | `array` | ```text An array of pins sharing the same group properties. The pins should be defined using pre-defined macros or, alternatively, using NVT_PINMUX macros depending on the pinmux model used by the SoC series. ```  This property is **required**. |
| `drive-strength` | `string` | ```text Set the driving strength of a pin. Hardware default configuration is low and it's enough to drive most components, like as LED, CAN transceiver and so on. ```  Default value: `low`  Legal values: `'low'`, `'fast'` |
| `slew-rate` | `string` | ```text Set the speed of a pin. This setting effectively limits the slew rate of the output signal. Hardware default configuration is low. Fast slew rate could support fast speed pins, like as SPI CLK up to 50MHz. ```  Default value: `low`  Legal values: `'low'`, `'high'`, `'fast'` |
| `digital-path-disable` | `boolean` | ```text disable digital path on a pin. ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `input-schmitt-enable` | `boolean` | ```text enable schmitt-trigger mode ``` |
