---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/pinctrl/gd,gd32-pinctrl-afio.html
original_path: build/dts/api/bindings/pinctrl/gd,gd32-pinctrl-afio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# gd,gd32-pinctrl-afio

Vendor: [GigaDevice Semiconductor](../../bindings.md#dt-vendor-gd)

## Description

```text
The GD32 pin controller (AFIO model) is a singleton node responsible for
controlling pin function selection and pin properties. For example, you can
use this node to route USART0 RX to pin PA10 and enable the pull-up resistor
on the pin. Remapping is also supported.

The node has the 'pinctrl' node label set in your SoC's devicetree,
so you can modify it like this:

  &pinctrl {
          /* your modifications go here */
  };

All device pin configurations should be placed in child nodes of the
'pinctrl' node, as shown in this example:

  /* You can put this in places like a board-pinctrl.dtsi file in
   * your board directory, or a devicetree overlay in your application.
   */

  /* include pre-defined combinations for the SoC variant used by the board */
  #include <dt-bindings/pinctrl/gd32f403z(k-i-g-e-c-b)xx-pinctrl.h>

  &pinctrl {
    /* configuration for the usart0 "default" state */
    usart0_default: usart0_default {
      /* group 1 */
      group1 {
        /* configure PA9 as USART0 TX and PA11 as USART0 CTS (no remap) */
        pinmux = <USART0_TX_PA9_NORMP>, <USART0_CTS_PA11_NORMP>;
      };
      /* group 2 */
      group2 {
        /* configure PA10 as USART0 RX and PA12 as USART0 RTS (no remap) */
        pinmux = <USART0_RX_PA10_NORMP>, <USART0_RTS_PA12_NORMP>;
        /* both PA10 and PA12 have pull-up enabled */
        bias-pull-up;
      };

    /* configuration for the usart0 "sleep" state */
    usart0_sleep: usart0_sleep {
      /* group 1 */
      group1 {
        /* configure PA9, PA10, PA11 and PA12 in analog mode */
        pinmux = <ANALOG_PA9>, <ANALOG_PA10>, <ANALOG_PA12>, <ANALOG_PA11>;
      };
    };

The 'usart0_default' child node encodes the pin configurations for a
particular state of a device; in this case, the default (that is, active)
state. Similarly, 'usart0_sleep' child node encodes the pin configurations
for the sleep state (used in device low power mode). Note that analog mode
is used for low power states because it disconnects the pin pull-up/down
resistor, schmitt trigger, and output buffer.

As shown, pin configurations are organized in groups within each child node.
Each group can specify a list of pin function selections in the 'pinmux'
property.

A group can also specify shared pin properties common to all the specified
pins, such as the 'bias-pull-up' property in group 2. Here is a list of
supported standard pin properties:

- drive-push-pull: Push-pull drive mode (default, not required). Only
  applies for GPIO_IN mode.
- drive-open-drain: Open-drain drive mode. Only applies for GPIO_IN mode.
- bias-disable: Disable pull-up/down (default, not required). Only applies
  for GPIO_IN mode.
- bias-pull-up: Enable pull-up resistor. Only applies for GPIO_IN mode.
- bias-pull-down: Enable pull-down resistor. Only applies for GPIO_IN mode.
- slew-rate: Set the maximum speed (and so the slew-rate) of the output
  signal (default: 2MHz). Only applies for ALTERNATE mode.

Note that drive and bias options are mutually exclusive.

Peripherals that are remappable will have their pre-defined macros suffixed
with the remap option being selected, for example:

  - CAN0_RX_PA11_NORMP: No remap
  - CAN0_RX_PB8_PRMP: Partial remap
  - CAN0_RX_PD0_FRMP: Full remap

It is important that **ALL** pinmux entries share the same remap. For
example:

  &pinctrl {
    can0_default: can0_default {
      group1 {
        pinmux = <CAN0_RX_PD0_FRMP>, <CAN0_TX_PD1_FRMP>;
        /*                    ^^^^                ^^^^           */
        /* CAN0 pins are remapped choosing the full remap option */
      };
    };
  };

To link pin configurations with a device, use a pinctrl-N property for some
number N, like this example you could place in your board's DTS file:

   #include "board-pinctrl.dtsi"

   &usart0 {
         pinctrl-0 = <&usart0_default>;
         pinctrl-1 = <&usart0_sleep>;
         pinctrl-names = "default", "sleep";
   };
```

## Properties

### Top level properties

These property descriptions apply to “gd,gd32-pinctrl-afio”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “gd,gd32-pinctrl-afio” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |

### Grandchild node properties

| Name | Type | Details |
| --- | --- | --- |
| `slew-rate` | `string` | ```text Set the maximum speed of a pin. This setting effectively limits the slew rate of the output signal. Defaults to "max-speed-2mhz", the SoC default. The max-speed-highest option may not be available on all SoC variants. If selected and not available the 50 MHz maximum speed will be used instead. Note that usage of max-speed-highest may require enabling the I/O compensation cell (refer to the gd,gd32-afio binding for more details). ```  Default value: `max-speed-2mhz`  Legal values: `'max-speed-10mhz'`, `'max-speed-2mhz'`, `'max-speed-50mhz'`, `'max-speed-highest'` |
| `pinmux` | `array` | ```text An array of pins sharing the same group properties. The pins should be defined using pre-defined macros or, alternatively, using the GD32_PINMUX_AF or GD32_PINMUX_AFIO utility macros depending on the pinmux model used by the SoC series. ```  This property is **required**. |
| `bias-disable` | `boolean` | ```text disable any pin bias ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
