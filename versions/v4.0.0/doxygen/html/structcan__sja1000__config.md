---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcan__sja1000__config.html
original_path: doxygen/html/structcan__sja1000__config.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_sja1000\_config Struct Reference

SJA1000 driver internal configuration structure.
[More...](#details)

`#include <[can_sja1000.h](can__sja1000_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct can\_driver\_config | [common](#a5f6b844c34defd6d63149629843e9dbb) |
| [can\_sja1000\_read\_reg\_t](can__sja1000_8h.md#a62d5b661f7b39f84f93a9597d2371341) | [read\_reg](#a7db8fc3fbb3dfdb95d6f4d5999ec5646) |
| [can\_sja1000\_write\_reg\_t](can__sja1000_8h.md#a7f71e5009721c00f2d6821a7db4c49cb) | [write\_reg](#ab7a864dc361c9b4a9b5917df7566c403) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ocr](#a7949f91e0d855d701771ff4f59669b42) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cdr](#a66f62e4f7efadf3b0454173e3795886d) |
| const void \* | [custom](#a31b21d7556a6c7d176cc955029310400) |

## Detailed Description

SJA1000 driver internal configuration structure.

## Field Documentation

## [◆ ](#a66f62e4f7efadf3b0454173e3795886d)cdr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_sja1000\_config::cdr |
| --- |

## [◆ ](#a5f6b844c34defd6d63149629843e9dbb)common

| const struct can\_driver\_config can\_sja1000\_config::common |
| --- |

## [◆ ](#a31b21d7556a6c7d176cc955029310400)custom

| const void\* can\_sja1000\_config::custom |
| --- |

## [◆ ](#a7949f91e0d855d701771ff4f59669b42)ocr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_sja1000\_config::ocr |
| --- |

## [◆ ](#a7db8fc3fbb3dfdb95d6f4d5999ec5646)read\_reg

| [can\_sja1000\_read\_reg\_t](can__sja1000_8h.md#a62d5b661f7b39f84f93a9597d2371341) can\_sja1000\_config::read\_reg |
| --- |

## [◆ ](#ab7a864dc361c9b4a9b5917df7566c403)write\_reg

| [can\_sja1000\_write\_reg\_t](can__sja1000_8h.md#a7f71e5009721c00f2d6821a7db4c49cb) can\_sja1000\_config::write\_reg |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_sja1000.h](can__sja1000_8h_source.md)

- [can\_sja1000\_config](structcan__sja1000__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
