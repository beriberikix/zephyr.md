---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/spi/microchip,xec-qmspi-ldma.html
original_path: build/dts/api/bindings/spi/microchip,xec-qmspi-ldma.html
---

# microchip,xec-qmspi-ldma

Vendor: [Microchip Technology Inc.](../../bindings.md#dt-vendor-microchip)

Note

An implementation of a driver matching this compatible is available in
[drivers/spi/spi\_xec\_qmspi\_ldma.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_xec_qmspi_ldma.c).

## Description

These nodes are “spi” bus nodes.

```text
Microchip XEC QMSPI controller with local DMA
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `girqs` | `array` | ```text An array of integers encoding each interrupt signal connection. This information includes the aggregated GIRQ number, GIRQ bit position, aggregated GIRQ NVIC connection, and direct NVIC connection of the GIRQ bit. ```  This property is **required**. |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `lines` | `int` | ```text QMSPI data lines 1, 2, or 4. 1 data line is full-duplex MOSI and MISO or half-duplex on MOSI only. Lines set to 2 or 4 indicate dual or quad I/O modes. Defaults to 1 for full duplex driver's support for full-duplex spi. ```  Legal values: `1`, `2`, `4` |
| `chip-select` | `int` | ```text Use QMSPI CS0# or CS1#. Port 0 supports both chip selects. Ports 1 and 2 implement CS0# only. Defaults to CS0#. ``` |
| `dcsckon` | `int` | ```text Delay in QMSPI main clocks from CS# assertion to first clock edge. If not present use hardware default value. Refer to chip documentation for QMSPI input clock frequency. ``` |
| `dckcsoff` | `int` | ```text Delay in QMSPI main clocks from last clock edge to CS# de-assertion. If not present use hardware default value. Refer to chip documentation for QMSPI input clock frequency. ``` |
| `dldh` | `int` | ```text Delay in QMSPI main clocks from CS# de-assertion to driving HOLD# and WP#. If not present use hardware default value. Refer to chip documentation for QMSPI input clock frequency. ``` |
| `dcsda` | `int` | ```text Delay in QMSPI main clocks from CS# de-assertion to CS# assertion. If not present use hardware default value. Refer to chip documentation for QMSPI input clock frequency. ``` |
| `cs1-freq` | `int` | ```text Allows different frequencies for CS#0 and CS1# devices. This applies to ports implementing CS1#. ``` |
| `tctradj` | `int` | ```text An optional signed 8-bit value for adjusting the QMSPI control signal timing tap. ``` |
| `tsckadj` | `int` | ```text An optional signed 8-bit value for adjusting the QMSPI clock signal timing tap. ``` |
| `clock-frequency` | `int` | ```text Clock frequency the SPI peripheral is being driven at, in Hz. ``` |
| `cs-gpios` | `phandle-array` | ```text An array of chip select GPIOs to use. Each element in the array specifies a GPIO. The index in the array corresponds to the child node that the CS gpio controls.  Example:    spi@... {           cs-gpios = <&gpio0 23 GPIO_ACTIVE_LOW>,                         <&gpio1 10 GPIO_ACTIVE_LOW>,                         ...;            spi-device@0 {                   reg = <0>;                   ...           };           spi-device@1 {                   reg = <1>;                   ...           };           ...   };  The child node "spi-device@0" specifies a SPI device with chip select controller gpio0, pin 23, and devicetree GPIO flags GPIO_ACTIVE_LOW. Similarly, "spi-device@1" has CS GPIO controller gpio1, pin 10, and flags GPIO_ACTIVE_LOW. Additional devices can be configured in the same way.  If unsure about the flags cell, GPIO_ACTIVE_LOW is generally a safe choice for a typical "CSn" pin. GPIO_ACTIVE_HIGH may be used if intervening hardware inverts the signal to the peripheral device or the line itself is active high.  If this property is not defined, no chip select GPIOs are set. SPI controllers with dedicated CS pins do not need to define the cs-gpios property. ``` |
| `overrun-character` | `int` | ```text The overrun character (ORC) is used when all bytes from the TX buffer are sent, but the transfer continues due to RX. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “microchip,xec-qmspi-ldma” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clock-names` | `string-array` | ```text name of each clock ``` |
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
