---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structgnss__data.html
original_path: doxygen/html/structgnss__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss\_data Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GNSS Interface](group__gnss__interface.md)

GNSS data structure.
[More...](#details)

`#include <[gnss.h](gnss_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [navigation\_data](structnavigation__data.md) | [nav\_data](#a2470031921179cb30172441163d80052) |
|  | Navigation data acquired. |
| struct [gnss\_info](structgnss__info.md) | [info](#a78155e6d2c981b9121b2ee42c1700988) |
|  | GNSS info when navigation data was acquired. |
| struct [gnss\_time](structgnss__time.md) | [utc](#ae6bfc0c6a53901963a1d20bad025fb99) |
|  | UTC time when data was acquired. |

## Detailed Description

GNSS data structure.

## Field Documentation

## [◆ ](#a78155e6d2c981b9121b2ee42c1700988)info

| struct [gnss\_info](structgnss__info.md) gnss\_data::info |
| --- |

GNSS info when navigation data was acquired.

## [◆ ](#a2470031921179cb30172441163d80052)nav\_data

| struct [navigation\_data](structnavigation__data.md) gnss\_data::nav\_data |
| --- |

Navigation data acquired.

## [◆ ](#ae6bfc0c6a53901963a1d20bad025fb99)utc

| struct [gnss\_time](structgnss__time.md) gnss\_data::utc |
| --- |

UTC time when data was acquired.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gnss.h](gnss_8h_source.md)

- [gnss\_data](structgnss__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
