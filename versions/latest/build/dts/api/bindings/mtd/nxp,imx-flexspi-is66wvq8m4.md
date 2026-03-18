---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/mtd/nxp,imx-flexspi-is66wvq8m4.html
original_path: build/dts/api/bindings/mtd/nxp,imx-flexspi-is66wvq8m4.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nxp,imx-flexspi-is66wvq8m4 (on spi bus)

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
ISSI IS66WVQ8M4 pSRAM on NXP FlexSPI bus
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `jedec-id` | `uint8-array` | ```text JEDEC ID as manufacturer ID, memory type, memory density ``` |
| `size` | `int` | ```text flash capacity in bits ``` |
| `sfdp-bfp` | `uint8-array` | ```text Contains the 32-bit words in little-endian byte order from the JESD216 Serial Flash Discoverable Parameters Basic Flash Parameters table.  This provides flash-specific configuration information in cases were runtime retrieval of SFDP data is not desired. ``` |
| `quad-enable-requirements` | `string` | ```text Quad Enable Requirements value from JESD216 BFP DW15.  Use NONE if the device detects 1-1-4 and 1-4-4 modes by the instruction.  Use S1B6 if QE is bit 6 of the first status register byte, and can be configured by reading then writing one byte with RDSR and WRSR.  For other fields see the specification. ```  Legal values: `'NONE'`, `'S2B1v1'`, `'S1B6'`, `'S2B7'`, `'S2B1v4'`, `'S2B1v5'`, `'S2B1v6'` |
| `enter-4byte-addr` | `int` | ```text Enter 4-Byte Addressing value from JESD216 BFP DW16  This property is ignored if the device is configured to use SFDP data from the sfdp-bfp property (CONFIG_SPI_NOR_SFDP_DEVICETREE) or to read SFDP properties at runtime (CONFIG_SPI_NOR_SFDP_RUNTIME).  For CONFIG_SPI_NOR_SFDP_MINIMAL this is the 8-bit value from bits 31:24 of DW16 identifying ways a device can be placed into 4-byte addressing mode.  If provided as a non-zero value the driver assumes that 4-byte addressing is require to access the full address range, and automatically puts the device into 4-byte address mode when the device is initialized. ``` |
| `page-size` | `int` | ```text Number of bytes in a page from JESD216 BFP DW11  This property is only used in the CONFIG_SPI_NOR_SFDP_MINIMAL configuration. It is ignored if the device is configured to use SFDP data from the sfdp-bfp property (CONFIG_SPI_NOR_SFDP_DEVICETREE) or if the SFDP parameters are read from the device at runtime (CONFIG_SPI_NOR_SFDP_RUNTIME).  The default value is 256 bytes if the value is not specified. ``` |
| `cs-interval-unit` | `int` | ```text Chip select interval units, in serial clock cycles. See the CSINTERVALUNIT field in registers FLASHA1CR0 through FLASHB2CR0. The default corresponds to the reset value of the register field. ```  Default value: `1`  Legal values: `1`, `256` |
| `cs-interval` | `int` | ```text Minimum interval between chip select deassertion and assertion. See the CSINTERVAL field in registers FLASHA1CR0 through FLASHB2CR0. The default corresponds to the reset value of the register field. ``` |
| `cs-setup-time` | `int` | ```text Chip select setup time, in serial clock cycles. See the TCSS field in registers FLASHA1CR0 through FLASHB2CR0. The default corresponds to the reset value of the register field. ```  Default value: `3` |
| `cs-hold-time` | `int` | ```text Chip select hold time, in serial clock cycles. See the TCSH field in registers FLASHA1CR0 through FLASHB2CR0. The default corresponds to the reset value of the register field. ```  Default value: `3` |
| `data-valid-time` | `int` | ```text Data valid time, in nanoseconds. See the registers DLLACR through DLLBCR. ``` |
| `column-space` | `int` | ```text Column address bit width. Set to zero if the flash does not support column address. See the CAS field in registers FLASHA1CR0 through FLASHB2CR0. The default corresponds to the reset value of the register field. ``` |
| `word-addressable` | `boolean` | ```text Don't transmit the least significant address bit when the flash is word addressable. See the WA field in registers FLASHA1CR0 through FLASHB2CR0. ``` |
| `ahb-write-wait-unit` | `int` | ```text AHB write wait interval units, in AHB clock cycles. See the AWRWAITUNIT field in registers FLASHA1CR2 through FLASHB2CR2. The default corresponds to the reset value of the register field. ```  Default value: `2`  Legal values: `2`, `8`, `32`, `128`, `512`, `2048`, `8192`, `32768` |
| `ahb-write-wait-interval` | `int` | ```text Time to wait between AHB triggered command sequences. See the AWRWAIT field in registers FLASHA1CR2 through FLASHB2CR2. The default corresponds to the reset value of the register field. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,imx-flexspi-is66wvq8m4” compatible.

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
