---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/pinctrl/infineon,cat1-pinctrl.html
original_path: build/dts/api/bindings/pinctrl/infineon,cat1-pinctrl.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# infineon,cat1-pinctrl

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

## Description

```text
Infineon CAT1 Pinctrl container node

This is a singleton node responsible for controlling the pin function selection
and pin properties. For example, you can use this node to route
UART0 RX to a particular port/pin and enable the pull-up resistor on that
pin.

The node has the 'pinctrl' node label set in SoC's devicetree,
so you can modify it like this:

&pinctrl {
    /* Your modifications go here */
};

Pin configuration can also specify the pin properties, for example the
'bias-pull-up' property. Here is a list of the supported standard pin
properties:
  * bias-high-impedance
  * bias-pull-up
  * bias-pull-down
  * drive-open-drain
  * drive-open-source
  * drive-push-pull   (strong)
  * input-enable      (input-buffer)

Infineon CAT1 SoC's devicetree includes a set of pre-defined pin control
Nodes, which can be found via MPN dtsi.
For example, board cy8cproto_062_4343w uses the CY8C624ABZI_S2D44 part, so
board dts (boards\arm\cy8cproto_062_4343w\cy8cproto_062_4343w.dts) includes MPN dts
(infineon/psoc6/mpns/CY8C624ABZI_S2D44.dtsi).

Each MPN dtsi includes package dtsi (../psoc6_xx/psoc6_xx.yyy-zzz.dtsi),
For example, CY8C624ABZI_S2D44 includes "../psoc6_02/psoc6_02.124-bga.dtsi".

An example of pre-defined pin control from package dtsi (e.g. psoc6_02.124-bga.dtsi):
p3_0_scb2_uart_rx - RX pin UART2 (SCB2) which connected to port3.0

  /omit-if-no-ref/ p3_0_scb2_uart_rx: p3_0_scb2_uart_rx {
        pinmux = <DT_CAT1_PINMUX(3, 0, HSIOM_SEL_ACT_6)>;
  };

Refer to psoc6_02.124-bga.dtsi for the list of all pre-defined pin control nodes.

NOTE1 Pre-defined pin control nodes use macro DT_CAT1_PINMUX to
  initialize pinmux. DT_CAT1_PINMUX has the following input parameters
  DT_CAT1_PINMUX(port_number, pin_number, hsiom),
  hsiom is defined in the HSIOM_SEL_xxx macros in the
  zephyr\include\zephyr\dt-bindings\pinctrl\ifx_cat1-pinctrl.h file.

      You can use DT_CAT1_PINMUX to define your own pin control node:
        &pinctrl {
            my_uart_rx: my_uart_rx {
                pinmux = <DT_CAT1_PINMUX(3, 0, HSIOM_SEL_ACT_6)>;
            };
        };

NOTE2 Pre-defined pin control nodes do not have bias pin configuration.
  The bias configuration can be updated in board-pinctrl.dtsi
  &pinctrl {
    /* Configure pin control Bias mode for uart2 pins */
    p3_1_scb2_uart_tx {
      drive-push-pull;
    };

    p3_0_scb2_uart_rx {
      input-enable;
    };

    p3_2_scb2_uart_rts {
      drive-push-pull;
    };

    p3_3_scb2_uart_cts {
      input-enable;
    };
  };

An example of the usage of pre-defined pin control nodes in your board's DTS file:

  &uart5 {
    pinctrl-0 = <&p5_1_scb5_uart_tx &p5_0_scb5_uart_rx>;
    pinctrl-names = "default";
  };

  /* Configure pin control bias mode for uart5 pins */
  &p5_1_scb5_uart_tx {
    drive-push-pull;
  };

  &p5_0_scb5_uart_rx {
    input-enable;
  };
```

## Properties

### Top level properties

These property descriptions apply to “infineon,cat1-pinctrl”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,cat1-pinctrl” compatible.

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
| `pinmux` | `int` | ```text Encodes port/pin and alternate function. ```  This property is **required**. |
| `bias-high-impedance` | `boolean` | ```text high impedance mode ("third-state", "floating") ``` |
| `bias-pull-up` | `boolean` | ```text enable pull-up resistor ``` |
| `bias-pull-down` | `boolean` | ```text enable pull-down resistor ``` |
| `drive-push-pull` | `boolean` | ```text drive actively high and low ``` |
| `drive-open-drain` | `boolean` | ```text drive with open drain (hardware AND) ``` |
| `drive-open-source` | `boolean` | ```text drive with open source (hardware OR) ``` |
| `input-enable` | `boolean` | ```text enable input on pin (e.g. enable an input buffer, no effect on output) ``` |
