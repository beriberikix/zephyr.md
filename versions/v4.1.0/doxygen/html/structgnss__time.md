---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structgnss__time.html
original_path: doxygen/html/structgnss__time.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss\_time Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GNSS Interface](group__gnss__interface.md)

GNSS time data structure.
[More...](#details)

`#include <[gnss.h](gnss_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [hour](#a5c8a280736741d8d07dacba30d48ed6f) |
|  | Hour [0, 23]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [minute](#a3e8b96861e45cc2a6222961e92ab62f5) |
|  | Minute [0, 59]. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [millisecond](#a2ab6b41452491ec34966fda0ddbdd9da) |
|  | Millisecond [0, 60999]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [month\_day](#a766744149009588f83cca930ef53ff10) |
|  | Day of month [1, 31]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [month](#a1c6730dc08cd3dfb48aee08154f5f2de) |
|  | Month [1, 12]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [century\_year](#a4daa514f38a7b7d88bf49cb5d664b2ac) |
|  | Year [0, 99]. |

## Detailed Description

GNSS time data structure.

## Field Documentation

## [◆ ](#a4daa514f38a7b7d88bf49cb5d664b2ac)century\_year

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gnss\_time::century\_year |
| --- |

Year [0, 99].

## [◆ ](#a5c8a280736741d8d07dacba30d48ed6f)hour

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gnss\_time::hour |
| --- |

Hour [0, 23].

## [◆ ](#a2ab6b41452491ec34966fda0ddbdd9da)millisecond

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) gnss\_time::millisecond |
| --- |

Millisecond [0, 60999].

## [◆ ](#a3e8b96861e45cc2a6222961e92ab62f5)minute

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gnss\_time::minute |
| --- |

Minute [0, 59].

## [◆ ](#a1c6730dc08cd3dfb48aee08154f5f2de)month

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gnss\_time::month |
| --- |

Month [1, 12].

## [◆ ](#a766744149009588f83cca930ef53ff10)month\_day

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gnss\_time::month\_day |
| --- |

Day of month [1, 31].

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gnss.h](gnss_8h_source.md)

- [gnss\_time](structgnss__time.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
