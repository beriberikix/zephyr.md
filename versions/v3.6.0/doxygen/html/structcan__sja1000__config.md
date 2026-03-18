---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcan__sja1000__config.html
original_path: doxygen/html/structcan__sja1000__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sjw](#ad97c09a6e2c0dfea93eccca8bcaa0100) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [phase\_seg1](#a3bce305b1aaaf5a8054650a91d54042d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [phase\_seg2](#ae8bb3785595e09033ae93b57262dbef1) |
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

## [◆ ](#a3bce305b1aaaf5a8054650a91d54042d)phase\_seg1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_sja1000\_config::phase\_seg1 |
| --- |

## [◆ ](#ae8bb3785595e09033ae93b57262dbef1)phase\_seg2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_sja1000\_config::phase\_seg2 |
| --- |

## [◆ ](#a7db8fc3fbb3dfdb95d6f4d5999ec5646)read\_reg

| [can\_sja1000\_read\_reg\_t](can__sja1000_8h.md#a62d5b661f7b39f84f93a9597d2371341) can\_sja1000\_config::read\_reg |
| --- |

## [◆ ](#ad97c09a6e2c0dfea93eccca8bcaa0100)sjw

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_sja1000\_config::sjw |
| --- |

## [◆ ](#ab7a864dc361c9b4a9b5917df7566c403)write\_reg

| [can\_sja1000\_write\_reg\_t](can__sja1000_8h.md#a7f71e5009721c00f2d6821a7db4c49cb) can\_sja1000\_config::write\_reg |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_sja1000.h](can__sja1000_8h_source.md)

- [can\_sja1000\_config](structcan__sja1000__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
