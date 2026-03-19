---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/spi/xlnx,xps-spi-2.00.a.html
original_path: build/dts/api/bindings/spi/xlnx,xps-spi-2.00.a.html
---

# xlnx,xps-spi-2.00.a

Vendor: [Xilinx](../../bindings.md#dt-vendor-xlnx)

Note

An implementation of a driver matching this compatible is available in
[drivers/spi/spi\_xlnx\_axi\_quadspi.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_xlnx_axi_quadspi.c).

## Description

These nodes are “spi” bus nodes.

```text
Xilinx AXI Quad SPI IP node
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `xlnx,num-ss-bits` | `int` | ```text Number of slave select bits implemented ```  This property is **required**.  Legal values: `1`, `2`, `3`, `4` |
| `xlnx,num-transfer-bits` | `int` | ```text Number of bits per transfer ```  This property is **required**.  Legal values: `8`, `16`, `32` |
| `xlnx,startup-block` | `boolean` | ```text Indicates the core is instantiated with the STARTUP block option, as is typically used when interfacing with the FPGA's configuration flash device. In this configuration the SPI clock is routed through the STARTUP block rather than normal signal routing. In this case, a workaround is required to issue a dummy transaction to the SPI flash device to ensure the STARTUP block is disengaged and allow the SPI core to control the CCLK line properly. The dummy READ_ID transaction will be issued to chip select 0. ``` |
| `fifo-size` | `int` | ```text FIFO size configured in SPI core. 0 indicates no FIFO. If not specified, 0 is assumed. Used to optimize TX/RX read handling. If the FIFO size is 0, the driver will check for FIFO full/empty after every word. ``` |
| `clock-frequency` | `int` | ```text Clock frequency the SPI peripheral is being driven at, in Hz. ``` |
| `cs-gpios` | `phandle-array` | ```text An array of chip select GPIOs to use. Each element in the array specifies a GPIO. The index in the array corresponds to the child node that the CS gpio controls.  Example:    spi@... {           cs-gpios = <&gpio0 23 GPIO_ACTIVE_LOW>,                         <&gpio1 10 GPIO_ACTIVE_LOW>,                         ...;            spi-device@0 {                   reg = <0>;                   ...           };           spi-device@1 {                   reg = <1>;                   ...           };           ...   };  The child node "spi-device@0" specifies a SPI device with chip select controller gpio0, pin 23, and devicetree GPIO flags GPIO_ACTIVE_LOW. Similarly, "spi-device@1" has CS GPIO controller gpio1, pin 10, and flags GPIO_ACTIVE_LOW. Additional devices can be configured in the same way.  If unsure about the flags cell, GPIO_ACTIVE_LOW is generally a safe choice for a typical "CSn" pin. GPIO_ACTIVE_HIGH may be used if intervening hardware inverts the signal to the peripheral device or the line itself is active high.  If this property is not defined, no chip select GPIOs are set. SPI controllers with dedicated CS pins do not need to define the cs-gpios property. ``` |
| `overrun-character` | `int` | ```text The overrun character (ORC) is used when all bytes from the TX buffer are sent, but the transfer continues due to RX. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “xlnx,xps-spi-2.00.a” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
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
