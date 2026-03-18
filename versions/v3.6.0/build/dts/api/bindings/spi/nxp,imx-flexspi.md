---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/spi/nxp,imx-flexspi.html
original_path: build/dts/api/bindings/spi/nxp,imx-flexspi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nxp,imx-flexspi

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

These nodes are “spi” bus nodes.

```text
NXP FlexSPI controller
```

## Properties

### Top level properties

These property descriptions apply to “nxp,imx-flexspi”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `ahb-bufferable` | `boolean` | ```text Enable AHB bufferable write access by setting register field AHBCR[BUFFERABLEEN]. ``` |
| `ahb-cacheable` | `boolean` | ```text Enable AHB cacheable read access by setting register field AHBCR[CACHEABLEEN]. ``` |
| `ahb-prefetch` | `boolean` | ```text Enable AHB read prefetch by setting register field AHBCR[PREFETCHEN]. ``` |
| `ahb-read-addr-opt` | `boolean` | ```text Remove burst start address alignment limitation by setting register field AHBCR[READADDROPT]. ``` |
| `combination-mode` | `boolean` | ```text Combine port A and port B data pins to support octal mode access by setting register field MCR0[COMBINATIONEN]. ``` |
| `sck-differential-clock` | `boolean` | ```text Enable/disable SCKB pad use as SCKA differential clock output, when enabled, Port B flash access is not available. ``` |
| `rx-clock-source` | `int` | ```text Source clock for flash read. See the RXCLKSRC field in register MCR0. The default corresponds to the reset value of the register field. ```  Legal values: `0`, `1`, `2`, `3` |
| `rx-buffer-config` | `array` | ```text Array of tuples to configure AHB RX buffers. Format is the following: <prefetch priority master_id buf_size>. Pass multiple tuples to configure multiple RX buffers (up to maximum supported by SOC). The tuple fields correspond to the following register bitfields: prefetch: AHBRXBUFxCRx[PREFETCH] priority: AHBRXBUFxCRx[PRIORITY] master_id: AHBRXBUFxCRx[MSTRID] buf_size: AHBRXBUFxCRx[BUFSZ] ``` |
| `clock-frequency` | `int` | ```text Clock frequency the SPI peripheral is being driven at, in Hz. ``` |
| `cs-gpios` | `phandle-array` | ```text An array of chip select GPIOs to use. Each element in the array specifies a GPIO. The index in the array corresponds to the child node that the CS gpio controls.  Example:    spi@... {           cs-gpios = <&gpio0 23 GPIO_ACTIVE_LOW>,                         <&gpio1 10 GPIO_ACTIVE_LOW>,                         ...;            spi-device@0 {                   reg = <0>;                   ...           };           spi-device@1 {                   reg = <1>;                   ...           };           ...   };  The child node "spi-device@0" specifies a SPI device with chip select controller gpio0, pin 23, and devicetree GPIO flags GPIO_ACTIVE_LOW. Similarly, "spi-device@1" has CS GPIO controller gpio1, pin 10, and flags GPIO_ACTIVE_LOW. Additional devices can be configured in the same way.  If unsure about the flags cell, GPIO_ACTIVE_LOW is generally a safe choice for a typical "CSn" pin. GPIO_ACTIVE_HIGH may be used if intervening hardware inverts the signal to the peripheral device or the line itself is active high.  If this property is not defined, no chip select GPIOs are set. SPI controllers with dedicated CS pins do not need to define the cs-gpios property. ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,imx-flexspi” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `cs-interval-unit` | `int` | ```text Chip select interval units, in serial clock cycles. See the CSINTERVALUNIT field in registers FLASHA1CR0 through FLASHB2CR0. The default corresponds to the reset value of the register field. ```  Default value: `1`  Legal values: `1`, `256` |
| `cs-interval` | `int` | ```text Minimum interval between chip select deassertion and assertion. See the CSINTERVAL field in registers FLASHA1CR0 through FLASHB2CR0. The default corresponds to the reset value of the register field. ``` |
| `cs-setup-time` | `int` | ```text Chip select setup time, in serial clock cycles. See the TCSS field in registers FLASHA1CR0 through FLASHB2CR0. The default corresponds to the reset value of the register field. ```  Default value: `3` |
| `cs-hold-time` | `int` | ```text Chip select hold time, in serial clock cycles. See the TCSH field in registers FLASHA1CR0 through FLASHB2CR0. The default corresponds to the reset value of the register field. ```  Default value: `3` |
| `data-valid-time` | `int` | ```text Data valid time, in nanoseconds. See the registers DLLACR through DLLBCR. ``` |
| `column-space` | `int` | ```text Column address bit width. Set to zero if the flash does not support column address. See the CAS field in registers FLASHA1CR0 through FLASHB2CR0. The default corresponds to the reset value of the register field. ``` |
| `word-addressable` | `boolean` | ```text Don't transmit the least significant address bit when the flash is word addressable. See the WA field in registers FLASHA1CR0 through FLASHB2CR0. ``` |
| `ahb-write-wait-unit` | `int` | ```text AHB write wait interval units, in AHB clock cycles. See the AWRWAITUNIT field in registers FLASHA1CR2 through FLASHB2CR2. The default corresponds to the reset value of the register field. ```  Default value: `2`  Legal values: `2`, `8`, `32`, `128`, `512`, `2048`, `8192`, `32768` |
| `ahb-write-wait-interval` | `int` | ```text Time to wait between AHB triggered command sequences. See the AWRWAIT field in registers FLASHA1CR2 through FLASHB2CR2. The default corresponds to the reset value of the register field. ``` |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
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
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `jedec-id` | `uint8-array` | ```text JEDEC ID as manufacturer ID, memory type, memory density ``` |
| `size` | `int` | ```text flash capacity in bits ``` |
| `sfdp-bfp` | `uint8-array` | ```text Contains the 32-bit words in little-endian byte order from the JESD216 Serial Flash Discoverable Parameters Basic Flash Parameters table.  This provides flash-specific configuration information in cases were runtime retrieval of SFDP data is not desired. ``` |
| `quad-enable-requirements` | `string` | ```text Quad Enable Requirements value from JESD216 BFP DW15.  Use NONE if the device detects 1-1-4 and 1-4-4 modes by the instruction.  Use S1B6 if QE is bit 6 of the first status register byte, and can be configured by reading then writing one byte with RDSR and WRSR.  For other fields see the specification. ```  Legal values: `'NONE'`, `'S2B1v1'`, `'S1B6'`, `'S2B7'`, `'S2B1v4'`, `'S2B1v5'`, `'S2B1v6'` |
| `enter-4byte-addr` | `int` | ```text Enter 4-Byte Addressing value from JESD216 BFP DW16  This property is ignored if the device is configured to use SFDP data from the sfdp-bfp property (CONFIG_SPI_NOR_SFDP_DEVICETREE) or to read SFDP properties at runtime (CONFIG_SPI_NOR_SFDP_RUNTIME).  For CONFIG_SPI_NOR_SFDP_MINIMAL this is the 8-bit value from bits 31:24 of DW16 identifying ways a device can be placed into 4-byte addressing mode.  If provided as a non-zero value the driver assumes that 4-byte addressing is require to access the full address range, and automatically puts the device into 4-byte address mode when the device is initialized. ``` |
| `page-size` | `int` | ```text Number of bytes in a page from JESD216 BFP DW11  This property is only used in the CONFIG_SPI_NOR_SFDP_MINIMAL configuration. It is ignored if the device is configured to use SFDP data from the sfdp-bfp property (CONFIG_SPI_NOR_SFDP_DEVICETREE) or if the SFDP parameters are read from the device at runtime (CONFIG_SPI_NOR_SFDP_RUNTIME).  The default value is 256 bytes if the value is not specified. ``` |
