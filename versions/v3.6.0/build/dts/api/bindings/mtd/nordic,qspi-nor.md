---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/mtd/nordic,qspi-nor.html
original_path: build/dts/api/bindings/mtd/nordic,qspi-nor.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nordic,qspi-nor (on qspi bus)

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
QSPI NOR flash supporting the JEDEC CFI interface.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `jedec-id` | `uint8-array` | ```text JEDEC ID as manufacturer ID, memory type, memory density ```  This property is **required**. |
| `size` | `int` | ```text The size in bits. Set this or size-in-bytes, but not both. ``` |
| `size-in-bytes` | `int` | ```text The size in bytes. Set this or size, but not both. ``` |
| `quad-enable-requirements` | `string` | ```text Quad Enable Requirements value from JESD216 BFP DW15.  Use NONE if the device detects 1-1-4 and 1-4-4 modes by the instruction.  Use S1B6 if QE is bit 6 of the first status register byte, and can be configured by reading then writing one byte with RDSR and WRSR.  For other fields see the specification. ```  Default value: `S1B6`  Legal values: `'NONE'`, `'S2B1v1'`, `'S1B6'`, `'S2B7'`, `'S2B1v4'`, `'S2B1v5'`, `'S2B1v6'` |
| `readoc` | `string` | ```text Specify the number of data lines and opcode used for reading. If not provided fastread will be selected. ```  Legal values: `'fastread'`, `'read2o'`, `'read2io'`, `'read4o'`, `'read4io'` |
| `writeoc` | `string` | ```text Specify the number of data lines and opcode used for writing. If not provided pp will be selected. ```  Legal values: `'pp'`, `'pp2o'`, `'pp4o'`, `'pp4io'` |
| `address-size-32` | `boolean` | ```text Set to indicate that 32-bit addressing is to be used. If not specified 24-bit addressing will be used. ``` |
| `ppsize-512` | `boolean` | ```text Set to indicate that the write opcode operates on 512-byte pages. If not specified the write opcode operates on 256-byte pages. ``` |
| `sck-delay` | `int` | ```text Number of clock cycles CSn must be asserted before it can go low again, specified in nanoseconds. ``` |
| `rx-delay` | `int` | ```text Number of clock cycles from the rising edge of the SPI clock until the input serial data is sampled. ``` |
| `cpha` | `boolean` | ```text Set to indicate phase starts with asserted half-phase (CPHA=1). For this driver using this property requires also using cpol. ``` |
| `cpol` | `boolean` | ```text Set to indicate clock leading edge is falling (CPOL=1). For this driver using this property requires also using cpha. ``` |
| `sck-frequency` | `int` | ```text Maximum clock speed supported by the device, in Hz. ```  This property is **required**. |
| `requires-ulbpr` | `boolean` | ```text Indicates the device requires the ULBPR (0x98) command.  Some flash chips such as the Microchip SST26VF series have a block protection register that initializes to write-protected.  Use this property to indicate that the BPR must be unlocked before write operations can proceed. ``` |
| `has-dpd` | `boolean` | ```text Indicates the device supports the DPD (0xB9) command.  Use this property to indicate the flash chip supports the Deep Power-Down mode that is entered by command 0xB9 to reduce power consumption below normal standby levels.  Use of this property implies that the RDPD (0xAB) Release from Deep Power Down command is also supported.  (On some chips this command functions as Read Electronic Signature; see t-enter-dpd). ``` |
| `dpd-wakeup-sequence` | `array` | ```text Specifies wakeup durations for devices without RDPD.  Some devices (Macronix MX25R in particular) wake from deep power down by a timed sequence of CSn toggles rather than the RDPD command.  This property specifies three durations measured in nanoseconds, in this order: (1) tDPDD (Delay Time for Release from Deep Power-Down Mode) (2) tCDRP (CSn Toggling Time before Release from Deep Power-Down Mode) (3) tRDP (Recovery Time for Release from Deep Power-Down Mode)  Absence of this property indicates that the RDPD command should be used to wake the chip from Deep Power-Down mode. ``` |
| `t-enter-dpd` | `int` | ```text Duration required to complete the DPD command.  This provides the duration, in nanoseconds, that CSn must be remain deasserted after issuing DPD before the chip will enter deep power down.  If not provided the driver does not enforce a delay. ``` |
| `t-exit-dpd` | `int` | ```text Duration required to complete the RDPD command.  This provides the duration, in nanoseconds, that CSn must be remain deasserted after issuing RDPD before the chip will exit deep power down and be ready to receive additional commands.  If not provided the driver does not enforce a delay. ``` |
| `has-lock` | `int` | ```text Bit mask of bits of the status register that should be cleared on startup.  Some devices from certain vendors power-up with block protect bits set in the status register, which prevent any erase or program operation from working.  Devices that have this behavior need to clear those bits on startup.  However, other devices have non-volatile bits in the status register that should not be cleared.  This value, when present, identifies bits in the status register that should be cleared when the device is initialized. ``` |
| `mxicy,mx25r-power-mode` | `string` | ```text Select to configure flash to use ultra low power mode or high performance mode (L/H switch). The high performance mode has faster write and erase performance, but use more power than ultra low power mode. Only supported on Macronix MX25R Ultra Low Power series. ```  Legal values: `'low-power'`, `'high-performance'` |
| `sfdp-bfp` | `uint8-array` | ```text Contains the 32-bit words in little-endian byte order from the JESD216 Serial Flash Discoverable Parameters Basic Flash Parameters table.  This provides flash-specific configuration information in cases were runtime retrieval of SFDP data is not desired. ``` |
| `enter-4byte-addr` | `int` | ```text Enter 4-Byte Addressing value from JESD216 BFP DW16  This property is ignored if the device is configured to use SFDP data from the sfdp-bfp property (CONFIG_SPI_NOR_SFDP_DEVICETREE) or to read SFDP properties at runtime (CONFIG_SPI_NOR_SFDP_RUNTIME).  For CONFIG_SPI_NOR_SFDP_MINIMAL this is the 8-bit value from bits 31:24 of DW16 identifying ways a device can be placed into 4-byte addressing mode.  If provided as a non-zero value the driver assumes that 4-byte addressing is require to access the full address range, and automatically puts the device into 4-byte address mode when the device is initialized. ``` |
| `page-size` | `int` | ```text Number of bytes in a page from JESD216 BFP DW11  This property is only used in the CONFIG_SPI_NOR_SFDP_MINIMAL configuration. It is ignored if the device is configured to use SFDP data from the sfdp-bfp property (CONFIG_SPI_NOR_SFDP_DEVICETREE) or if the SFDP parameters are read from the device at runtime (CONFIG_SPI_NOR_SFDP_RUNTIME).  The default value is 256 bytes if the value is not specified. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,qspi-nor” compatible.

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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
