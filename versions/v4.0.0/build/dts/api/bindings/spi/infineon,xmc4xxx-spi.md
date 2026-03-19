---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/spi/infineon,xmc4xxx-spi.html
original_path: build/dts/api/bindings/spi/infineon,xmc4xxx-spi.html
---

# infineon,xmc4xxx-spi

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

Note

An implementation of a driver matching this compatible is available in
[drivers/spi/spi\_xmc4xxx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_xmc4xxx.c).

## Description

These nodes are “spi” bus nodes.

```text
INFINEON XMC4XXX SPI controller
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `miso-src` | `string` | ```text Connects the SPI miso line (USIC DX0 input) to a specific GPIO pin. The USIC DX0 input is a multiplexer which connects to different GPIO pins. Refer to the XMC4XXX reference manual for the GPIO pin/mux mappings. DX0G is the loopback input line. ```  This property is **required**.  Legal values: `'DX0A'`, `'DX0B'`, `'DX0C'`, `'DX0D'`, `'DX0E'`, `'DX0F'`, `'DX0G'` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
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
may apply to the “infineon,xmc4xxx-spi” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text IRQ number and priority to use for interrupt driven SPI. If DMA is not used (enabled using option CONFIG_SPI_XMC4XXX_DMA) then only one, for receiving, labelled with "rx" needs to be set. When using DMA, two interrupts labelled "tx" and "rx" must be set. Each USIC must use a certain interrupt range: USIC0 = [84, 89] USIC1 = [90, 95] USIC2 = [96, 101] ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `dmas` | `phandle-array` | ```text Optional TX & RX dma specifiers.  The dmas are referenced in the USIC/SPI node using the following syntax: dmas = <&dma1 1 0 XMC4XXX_SET_CONFIG(10,6)>, <&dma1 2 0 XMC4XXX_SET_CONFIG(11,6)>; where the first entry is for the TX, and the second for RX.  The parameters in the dma entry are: dma device phandle, dma channel, dma priority (0 is lowest and 7 is highest), and an opaque entry for the dma line routing parameters set by the macro XMC4XXX_SET_CONFIG(line, request_source). Use the following steps to properly select parameters line, request_source: 1. Select a dma device and a free dma channel. 1. Select a free dma line. dma0 device can only connect to lines [0, 7] and    dma1 can connect to lines [8, 11]. 2. For a given interrupt, calculate the service request (SR) number. Note the following    simple mapping: in USIC0 interrupt 84->SR0, interrupt 85->SR1, ... etc.    In USIC1, interrupt 90->SR0, 91->SR1, etc. 3. Select request_source from Table "DMA Request Source Selection" in XMC4XXX reference    manual.  For example, say we select interrupt 85 on USIC0, dma0, channel 3, priority 4, and line 7. The interrupt would map to SR1. From Table "DMA Request Source Selection", request_source would need to be set to 10 and the dts entry would be: dma = <&dma0 3 4 XMC4XXX_SET_CONFIG(7,10) ... >; ``` |
| `dma-names` | `string-array` | ```text Required if the dmas property exists. Should be set to "tx" and "rx" to match the dmas property.  For example    dma-names = "tx", "rx"; ``` |
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
