---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/mtd/andestech,qspi-nor.html
original_path: build/dts/api/bindings/mtd/andestech,qspi-nor.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# andestech,qspi-nor

Vendor: [Andes Technology Corporation](../../bindings.md#dt-vendor-andestech)

## Description

```text
Properties supporting Zephyr qspi-nor flash driver control of flash memories using the standard M25P80-based command set.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `jedec-id` | `uint8-array` | ```text JEDEC ID as manufacturer ID, memory type, memory density ``` |
| `size` | `int` | ```text flash capacity in bits ``` |
| `sfdp-bfp` | `uint8-array` | ```text Contains the 32-bit words in little-endian byte order from the JESD216 Serial Flash Discoverable Parameters Basic Flash Parameters table.  This provides flash-specific configuration information in cases were runtime retrieval of SFDP data is not desired. ``` |
| `quad-enable-requirements` | `string` | ```text Quad Enable Requirements value from JESD216 BFP DW15.  Use NONE if the device detects 1-1-4 and 1-4-4 modes by the instruction.  Use S1B6 if QE is bit 6 of the first status register byte, and can be configured by reading then writing one byte with RDSR and WRSR.  For other fields see the specification. ```  Legal values: `'NONE'`, `'S2B1v1'`, `'S1B6'`, `'S2B7'`, `'S2B1v4'`, `'S2B1v5'`, `'S2B1v6'` |
| `enter-4byte-addr` | `int` | ```text Enter 4-Byte Addressing value from JESD216 BFP DW16  This property is ignored if the device is configured to use SFDP data from the sfdp-bfp property (CONFIG_SPI_NOR_SFDP_DEVICETREE) or to read SFDP properties at runtime (CONFIG_SPI_NOR_SFDP_RUNTIME).  For CONFIG_SPI_NOR_SFDP_MINIMAL this is the 8-bit value from bits 31:24 of DW16 identifying ways a device can be placed into 4-byte addressing mode.  If provided as a non-zero value the driver assumes that 4-byte addressing is require to access the full address range, and automatically puts the device into 4-byte address mode when the device is initialized. ``` |
| `page-size` | `int` | ```text Number of bytes in a page from JESD216 BFP DW11  This property is only used in the CONFIG_SPI_NOR_SFDP_MINIMAL configuration. It is ignored if the device is configured to use SFDP data from the sfdp-bfp property (CONFIG_SPI_NOR_SFDP_DEVICETREE) or if the SFDP parameters are read from the device at runtime (CONFIG_SPI_NOR_SFDP_RUNTIME).  The default value is 256 bytes if the value is not specified. ``` |
| `requires-ulbpr` | `boolean` | ```text Indicates the device requires the ULBPR (0x98) command.  Some flash chips such as the Microchip SST26VF series have a block protection register that initializes to write-protected.  Use this property to indicate that the BPR must be unlocked before write operations can proceed. ``` |
| `has-dpd` | `boolean` | ```text Indicates the device supports the DPD (0xB9) command.  Use this property to indicate the flash chip supports the Deep Power-Down mode that is entered by command 0xB9 to reduce power consumption below normal standby levels.  Use of this property implies that the RDPD (0xAB) Release from Deep Power Down command is also supported.  (On some chips this command functions as Read Electronic Signature; see t-enter-dpd). ``` |
| `dpd-wakeup-sequence` | `array` | ```text Specifies wakeup durations for devices without RDPD.  Some devices (Macronix MX25R in particular) wake from deep power down by a timed sequence of CSn toggles rather than the RDPD command.  This property specifies three durations measured in nanoseconds, in this order: (1) tDPDD (Delay Time for Release from Deep Power-Down Mode) (2) tCDRP (CSn Toggling Time before Release from Deep Power-Down Mode) (3) tRDP (Recovery Time for Release from Deep Power-Down Mode)  Absence of this property indicates that the RDPD command should be used to wake the chip from Deep Power-Down mode. ``` |
| `t-enter-dpd` | `int` | ```text Duration required to complete the DPD command.  This provides the duration, in nanoseconds, that CSn must be remain deasserted after issuing DPD before the chip will enter deep power down.  If not provided the driver does not enforce a delay. ``` |
| `t-exit-dpd` | `int` | ```text Duration required to complete the RDPD command.  This provides the duration, in nanoseconds, that CSn must be remain deasserted after issuing RDPD before the chip will exit deep power down and be ready to receive additional commands.  If not provided the driver does not enforce a delay. ``` |
| `has-lock` | `int` | ```text Bit mask of bits of the status register that should be cleared on startup.  Some devices from certain vendors power-up with block protect bits set in the status register, which prevent any erase or program operation from working.  Devices that have this behavior need to clear those bits on startup.  However, other devices have non-volatile bits in the status register that should not be cleared.  This value, when present, identifies bits in the status register that should be cleared when the device is initialized. ``` |
| `mxicy,mx25r-power-mode` | `string` | ```text Select to configure flash to use ultra low power mode or high performance mode (L/H switch). The high performance mode has faster write and erase performance, but use more power than ultra low power mode. Only supported on Macronix MX25R Ultra Low Power series. ```  Legal values: `'low-power'`, `'high-performance'` |
| `wp-gpios` | `phandle-array` | ```text WPn pin ``` |
| `hold-gpios` | `phandle-array` | ```text HOLDn pin ``` |
| `reset-gpios` | `phandle-array` | ```text RESETn pin ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “andestech,qspi-nor” compatible.

(None)
