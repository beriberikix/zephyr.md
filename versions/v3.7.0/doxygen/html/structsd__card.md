---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsd__card.html
original_path: doxygen/html/structsd__card.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sd\_card Struct Reference

SD card structure.
[More...](#details)

`#include <[sd.h](sd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [sdhc](#afabeaa207f2f5caaec8cfedac6b35661) |
|  | SD host controller for card. |
| struct [sdhc\_io](structsdhc__io.md) | [bus\_io](#a875b7081a3e647b782cdb835372f5029) |
|  | Current bus I/O props for SDHC. |
| enum [sd\_voltage](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d) | [card\_voltage](#ae8e85d2fc44a97b42247d87a5c2aafdf) |
|  | Card signal voltage. |
| struct [k\_mutex](structk__mutex.md) | [lock](#aba2501397066d0930691c40778405aa7) |
|  | card mutex |
| struct [sdhc\_host\_props](structsdhc__host__props.md) | [host\_props](#a9f597007072d3af5b70ea5cc2a4cbd29) |
|  | SDHC host properties. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ocr](#a856e7ea75577c62be17dc5d8c99908f4) |
|  | Raw card OCR content. |
| struct [sd\_switch\_caps](structsd__switch__caps.md) | [switch\_caps](#a03eac55046f7222c97d60fa919e3cae9) |
|  | SD switch capabilities. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [num\_io](#a17a021db8aa3a8ad224e422f3854eafc): 3 |
|  | I/O function count. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [relative\_addr](#a1db9545598f0eb6b6440e63d4941d2ab) |
|  | Card relative address. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [block\_count](#acdcfdaab67d284ef3a8ee3202fd7a538) |
|  | Number of blocks in SD card. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [block\_size](#a3d29b73f029af5182475c2a2d365173b) |
|  | SD block size. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sd\_version](#a5a9a627df5daf23b468ce705bf5f5f81) |
|  | SD specification version. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [card\_speed](#a8beccfe60fc714c159528fbd2c122b16) |
|  | Card timing mode. |
| enum [card\_status](sd_8h.md#a52167aac735d93085a5eebc6f50e1bba) | [status](#a03d7be3154dcd881df60921681a4f308) |
|  | Card status. |
| enum [card\_type](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14) | [type](#a798acb1bb9495d1009a23f139d269108) |
|  | Card type. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#ad5d6e798ae8b04d829fb8131f6cb1ccf) |
|  | Card flags. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bus\_width](#a38383b8f5c1f9bff1537f407fbec9faf) |
|  | Desired bus width. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cccr\_flags](#ab122e442ab3ba5078c99a98a861ec908) |
|  | SDIO CCCR data. |
| struct [sdio\_func](structsdio__func.md) | [func0](#a93986ee5db729d9931b4ababe41c303a) |
|  | Function 0 common card data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [card\_buffer](#a81c9ec36c79e77599c10163455c86e7c) [CONFIG\_SD\_BUFFER\_SIZE] |

## Detailed Description

SD card structure.

This structure is used by the subsystem to track an individual SD device connected to the system. The application may access these fields, but use caution when changing values.

## Field Documentation

## [◆ ](#acdcfdaab67d284ef3a8ee3202fd7a538)block\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sd\_card::block\_count |
| --- |

Number of blocks in SD card.

## [◆ ](#a3d29b73f029af5182475c2a2d365173b)block\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sd\_card::block\_size |
| --- |

SD block size.

## [◆ ](#a875b7081a3e647b782cdb835372f5029)bus\_io

| struct [sdhc\_io](structsdhc__io.md) sd\_card::bus\_io |
| --- |

Current bus I/O props for SDHC.

## [◆ ](#a38383b8f5c1f9bff1537f407fbec9faf)bus\_width

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_card::bus\_width |
| --- |

Desired bus width.

## [◆ ](#a81c9ec36c79e77599c10163455c86e7c)card\_buffer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_card::card\_buffer[CONFIG\_SD\_BUFFER\_SIZE] |
| --- |

## [◆ ](#a8beccfe60fc714c159528fbd2c122b16)card\_speed

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_card::card\_speed |
| --- |

Card timing mode.

## [◆ ](#ae8e85d2fc44a97b42247d87a5c2aafdf)card\_voltage

| enum [sd\_voltage](group__sdhc__interface.md#ga34041edf280f125b8500809226b3de5d) sd\_card::card\_voltage |
| --- |

Card signal voltage.

## [◆ ](#ab122e442ab3ba5078c99a98a861ec908)cccr\_flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sd\_card::cccr\_flags |
| --- |

SDIO CCCR data.

## [◆ ](#ad5d6e798ae8b04d829fb8131f6cb1ccf)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sd\_card::flags |
| --- |

Card flags.

## [◆ ](#a93986ee5db729d9931b4ababe41c303a)func0

| struct [sdio\_func](structsdio__func.md) sd\_card::func0 |
| --- |

Function 0 common card data.

## [◆ ](#a9f597007072d3af5b70ea5cc2a4cbd29)host\_props

| struct [sdhc\_host\_props](structsdhc__host__props.md) sd\_card::host\_props |
| --- |

SDHC host properties.

## [◆ ](#aba2501397066d0930691c40778405aa7)lock

| struct [k\_mutex](structk__mutex.md) sd\_card::lock |
| --- |

card mutex

## [◆ ](#a17a021db8aa3a8ad224e422f3854eafc)num\_io

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sd\_card::num\_io |
| --- |

I/O function count.

0 for SD cards

## [◆ ](#a856e7ea75577c62be17dc5d8c99908f4)ocr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sd\_card::ocr |
| --- |

Raw card OCR content.

## [◆ ](#a1db9545598f0eb6b6440e63d4941d2ab)relative\_addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sd\_card::relative\_addr |
| --- |

Card relative address.

## [◆ ](#a5a9a627df5daf23b468ce705bf5f5f81)sd\_version

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_card::sd\_version |
| --- |

SD specification version.

## [◆ ](#afabeaa207f2f5caaec8cfedac6b35661)sdhc

| const struct [device](structdevice.md)\* sd\_card::sdhc |
| --- |

SD host controller for card.

## [◆ ](#a03d7be3154dcd881df60921681a4f308)status

| enum [card\_status](sd_8h.md#a52167aac735d93085a5eebc6f50e1bba) sd\_card::status |
| --- |

Card status.

## [◆ ](#a03eac55046f7222c97d60fa919e3cae9)switch\_caps

| struct [sd\_switch\_caps](structsd__switch__caps.md) sd\_card::switch\_caps |
| --- |

SD switch capabilities.

## [◆ ](#a798acb1bb9495d1009a23f139d269108)type

| enum [card\_type](sd_8h.md#aee707e2ff5691dbdefd9341a18de7b14) sd\_card::type |
| --- |

Card type.

---

The documentation for this struct was generated from the following file:

- zephyr/sd/[sd.h](sd_8h_source.md)

- [sd\_card](structsd__card.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
