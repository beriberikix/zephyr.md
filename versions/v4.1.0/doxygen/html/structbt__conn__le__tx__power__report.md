---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__conn__le__tx__power__report.html
original_path: doxygen/html/structbt__conn__le__tx__power__report.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_tx\_power\_report Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

LE Transmit Power Reporting Structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reason](#aa5606925229784af8ae90542432cf200) |
|  | Reason for Transmit power reporting, as documented in Core Spec. |
| enum [bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190) | [phy](#a5b1f67537fbe945f2f258b47082723b4) |
|  | Phy of Transmit power reporting. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power\_level](#ace830ddb7ae662c9759babed87f1b6f3) |
|  | Transmit power level. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_power\_level\_flag](#ae7a4f77c6f7af1a459896d25cf661eb8) |
|  | Bit 0: Transmit power level is at minimum level. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [delta](#a7c681c7b9f77d994b2de1febea7c5dc9) |
|  | Change in transmit power level. |

## Detailed Description

LE Transmit Power Reporting Structure.

## Field Documentation

## [◆ ](#a7c681c7b9f77d994b2de1febea7c5dc9)delta

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_conn\_le\_tx\_power\_report::delta |
| --- |

Change in transmit power level.

- 0xXX - Change in transmit power level (positive indicates increased power, negative indicates decreased power, zero indicates unchanged) Units: dB
- 0x7F - Change is not available or is out of range.

## [◆ ](#a5b1f67537fbe945f2f258b47082723b4)phy

| enum [bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190) bt\_conn\_le\_tx\_power\_report::phy |
| --- |

Phy of Transmit power reporting.

## [◆ ](#aa5606925229784af8ae90542432cf200)reason

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_tx\_power\_report::reason |
| --- |

Reason for Transmit power reporting, as documented in Core Spec.

Version 5.4 Vol. 4, Part E, 7.7.65.33.

## [◆ ](#ace830ddb7ae662c9759babed87f1b6f3)tx\_power\_level

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_conn\_le\_tx\_power\_report::tx\_power\_level |
| --- |

Transmit power level.

- 0xXX - Transmit power level
  - Range: -127 to 20
  - Units: dBm
- 0x7E - Remote device is not managing power levels on this PHY.
- 0x7F - Transmit power level is not available

## [◆ ](#ae7a4f77c6f7af1a459896d25cf661eb8)tx\_power\_level\_flag

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_tx\_power\_report::tx\_power\_level\_flag |
| --- |

Bit 0: Transmit power level is at minimum level.

Bit 1: Transmit power level is at maximum level.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_tx\_power\_report](structbt__conn__le__tx__power__report.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
