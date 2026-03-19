---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pinctrl/xlnx,pinctrl-zynq.html
original_path: build/dts/api/bindings/pinctrl/xlnx,pinctrl-zynq.html
---

# xlnx,pinctrl-zynq

Vendor: [Xilinx](../../bindings.md#dt-vendor-xlnx)

Note

An implementation of a driver matching this compatible is available in
[drivers/pinctrl/pinctrl\_xlnx\_zynq.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_xlnx_zynq.c).

## Description

```text
Xilinx Zynq-7000 SoC series pinctrl node. This node will define pin multiplexing and
configurations in groups. Each group within the pinctrl node defines the pin multiplexing and
configuration for a peripheral, and each subgroup in the pin group defines all the pins for that
peripheral with the same configuration properties. Pins are selected either by named pin groups
(e.g. groups = "uart1_10_grp") or by named pins (e.g. pins = "MIO49") or a combination of
these. The remaining properties set configuration values for those pins.

Here is an example for UART1 pins:

#include <zephyr/dt-bindings/pinctrl/pinctrl-zynq.h>

&pinctrl0 {
  pinctrl_uart1_default: uart1-default {
    mux {
      groups = "uart1_10_grp";
      function = "uart1";
    };

    conf {
      groups = "uart1_10_grp";
      slew-rate = <IO_SPEED_SLOW>;
      power-source = <IO_STANDARD_LVCMOS18>;
    };

    conf-rx {
      pins = "MIO49";
      bias-high-impedance;
    };

    conf-tx {
      pins = "MIO48";
      bias-disable;
    };
  };
};

See the Xilinx Zynq-7000 SoC Technical Reference Manual (UG585) for further details on pin
multiplexing and configuration options.
```

## Properties

### Top level properties

These property descriptions apply to “xlnx,pinctrl-zynq”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `syscon` | `phandle` | ```text phandle to the System Level Control Registers (SLCR). ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “xlnx,pinctrl-zynq” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Base address and size of the System Level Control Registers (SLCR) space. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `groups` | `string-array` | ```text Specify list of pin groups to select for this configuration node.  Valid pin groups are "ethernet0_0_grp", "ethernet1_0_grp", "mdio0_0_grp," "mdio1_0_grp", "qspi0_0_grp", "qspi1_0_grp", "qspi_fbclk," "qspi_cs1_grp", "spi0_0_grp", "spi0_1_grp", "spi0_2_grp," "spi0_0_ss0", "spi0_0_ss1", "spi0_0_ss2", "spi0_1_ss0," "spi0_1_ss1", "spi0_1_ss2", "spi0_2_ss0", "spi0_2_ss1," "spi0_2_ss2", "spi1_0_grp", "spi1_1_grp", "spi1_2_grp," "spi1_3_grp", "spi1_0_ss0", "spi1_0_ss1", "spi1_0_ss2," "spi1_1_ss0", "spi1_1_ss1", "spi1_1_ss2", "spi1_2_ss0," "spi1_2_ss1", "spi1_2_ss2", "spi1_3_ss0", "spi1_3_ss1," "spi1_3_ss2", "sdio0_0_grp", "sdio0_1_grp", "sdio0_2_grp," "sdio1_0_grp", "sdio1_1_grp", "sdio1_2_grp", "sdio1_3_grp," "sdio0_emio_wp", "sdio0_emio_cd", "sdio1_emio_wp," "sdio1_emio_cd", "smc0_nor", "smc0_nor_cs1_grp," "smc0_nor_addr25_grp", "smc0_nand", "can0_0_grp", "can0_1_grp," "can0_2_grp", "can0_3_grp", "can0_4_grp", "can0_5_grp," "can0_6_grp", "can0_7_grp", "can0_8_grp", "can0_9_grp," "can0_10_grp", "can1_0_grp", "can1_1_grp", "can1_2_grp," "can1_3_grp", "can1_4_grp", "can1_5_grp", "can1_6_grp," "can1_7_grp", "can1_8_grp", "can1_9_grp", "can1_10_grp," "can1_11_grp", "uart0_0_grp", "uart0_1_grp", "uart0_2_grp," "uart0_3_grp", "uart0_4_grp", "uart0_5_grp", "uart0_6_grp," "uart0_7_grp", "uart0_8_grp", "uart0_9_grp", "uart0_10_grp," "uart1_0_grp", "uart1_1_grp", "uart1_2_grp", "uart1_3_grp," "uart1_4_grp", "uart1_5_grp", "uart1_6_grp", "uart1_7_grp," "uart1_8_grp", "uart1_9_grp", "uart1_10_grp", "uart1_11_grp," "i2c0_0_grp", "i2c0_1_grp", "i2c0_2_grp", "i2c0_3_grp," "i2c0_4_grp", "i2c0_5_grp", "i2c0_6_grp", "i2c0_7_grp," "i2c0_8_grp", "i2c0_9_grp", "i2c0_10_grp", "i2c1_0_grp," "i2c1_1_grp", "i2c1_2_grp", "i2c1_3_grp", "i2c1_4_grp," "i2c1_5_grp", "i2c1_6_grp", "i2c1_7_grp", "i2c1_8_grp," "i2c1_9_grp", "i2c1_10_grp", "ttc0_0_grp", "ttc0_1_grp," "ttc0_2_grp", "ttc1_0_grp", "ttc1_1_grp", "ttc1_2_grp," "swdt0_0_grp", "swdt0_1_grp", "swdt0_2_grp", "swdt0_3_grp," "swdt0_4_grp", "gpio0_0_grp", "gpio0_1_grp", "gpio0_2_grp," "gpio0_3_grp", "gpio0_4_grp", "gpio0_5_grp", "gpio0_6_grp," "gpio0_7_grp", "gpio0_8_grp", "gpio0_9_grp", "gpio0_10_grp," "gpio0_11_grp", "gpio0_12_grp", "gpio0_13_grp", "gpio0_14_grp," "gpio0_15_grp", "gpio0_16_grp", "gpio0_17_grp", "gpio0_18_grp," "gpio0_19_grp", "gpio0_20_grp", "gpio0_21_grp", "gpio0_22_grp," "gpio0_23_grp", "gpio0_24_grp", "gpio0_25_grp", "gpio0_26_grp," "gpio0_27_grp", "gpio0_28_grp", "gpio0_29_grp", "gpio0_30_grp," "gpio0_31_grp", "gpio0_32_grp", "gpio0_33_grp", "gpio0_34_grp," "gpio0_35_grp", "gpio0_36_grp", "gpio0_37_grp", "gpio0_38_grp," "gpio0_39_grp", "gpio0_40_grp", "gpio0_41_grp", "gpio0_42_grp," "gpio0_43_grp", "gpio0_44_grp", "gpio0_45_grp", "gpio0_46_grp," "gpio0_47_grp", "gpio0_48_grp", "gpio0_49_grp", "gpio0_50_grp," "gpio0_51_grp", "gpio0_52_grp", "gpio0_53_grp", "usb0_0_grp," "usb1_0_grp"  Pin groups are combined with pin names (see pins) to form the full list of pins to select. ``` |
| `pins` | `string-array` | ```text Specify list of pin names to select for this configuration node. Valid pin names are "MIO0" to "MIO53".  Pin names are combined with pin groups (see groups) to form the full list of pins to select. ``` |
| `function` | `string` | ```text Specify the alternative function to be configured for the given pin groups. Sets the L3_SEL, L2_SEL, L1_SEL, and L0_SEL fields in the MIO_PIN_xx SLCR register. ```  Legal values: `'ethernet0'`, `'ethernet1'`, `'mdio0'`, `'mdio1'`, `'qspi0'`, `'qspi1'`, `'qspi_fbclk'`, `'qspi_cs1'`, `'spi0'`, `'spi0_ss'`, `'spi1'`, `'spi1_ss'`, `'sdio0'`, `'sdio0_pc'`, `'sdio0_cd'`, `'sdio0_wp'`, `'sdio1'`, `'sdio1_pc'`, `'sdio1_cd'`, `'sdio1_wp'`, `'smc0_nor'`, `'smc0_nor_cs1'`, `'smc0_nor_addr25'`, `'smc0_nand'`, `'can0'`, `'can1'`, `'uart0'`, `'uart1'`, `'i2c0'`, `'i2c1'`, `'ttc0'`, `'ttc1'`, `'swdt0'`, `'gpio0'`, `'usb0'`, `'usb1'` |
| `bias-disable` | `boolean` | ```text Disable any IO buffer pin bias. Clears the PULLUP and TRI_ENABLE fields in the MIO_PIN_xx SLCR register. ``` |
| `bias-high-impedance` | `boolean` | ```text Enables tri-state on IO buffer pin. Sets the TRI_ENABLE field in the MIO_PIN_xx SLCR register. ``` |
| `bias-pull-up` | `boolean` | ```text Enables pull-up on IO buffer pin. Sets the PULLUP field in the MIO_PIN_xx SLCR register. ``` |
| `low-power-enable` | `boolean` | ```text Disable HSTL input buffer to save power when it is an output-only. Applicable when power-source (IO_Type) is HSTL. Sets the DisableRcvr field in the MIO_PIN_xx SLCR register. ``` |
| `low-power-disable` | `boolean` | ```text Enable HSTL input buffer. Applicable when the power-souce (IO_Type) is HSTL. Clears the DisableRcvr field in the MIO_PIN_xx SLCR register. ``` |
| `power-source` | `int` | ```text IO buffer type. Sets the IO_Type field in the MIO_PIN_xx SLCR register. The IO_STANDARD_* macros are defined in pinctrl-zynq.h.  1 or IO_STANDARD_LVCMOS18 2 or IO_STANDARD_LVCMOS25 3 or IO_STANDARD_LVCMOS33 4 or IO_STANDARD_HSTL ```  Legal values: `1`, `2`, `3`, `4` |
| `slew-rate` | `int` | ```text IO buffer edge rate. Applicable when the power-source (IO_type) is LVCMOS18, LVCMOS25, or LVCMOS33. Sets the Speed field in the MIO_PIN_xx SLCR register. The IO_SPEED_* macros are defined in pinctrl-zynq.h.  0 or IO_SPEED_SLOW 1 or IO_SPEED_FAST ```  Legal values: `0`, `1` |
