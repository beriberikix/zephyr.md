---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__br__discovery__param.html
original_path: doxygen/html/structbt__br__discovery__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_br\_discovery\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

BR/EDR discovery parameters.
[More...](#details)

`#include <[bluetooth.h](bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [length](#a3087af0c5a264d50a27395d974f99e1e) |
|  | Maximum length of the discovery in units of 1.28 seconds. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [limited](#ac02d03f8cfdf4ad7aee3178e871cc105) |
|  | True if limited discovery procedure is to be used. |

## Detailed Description

BR/EDR discovery parameters.

## Field Documentation

## [◆ ](#a3087af0c5a264d50a27395d974f99e1e)length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_br\_discovery\_param::length |
| --- |

Maximum length of the discovery in units of 1.28 seconds.

Valid range is 0x01 - 0x30.

## [◆ ](#ac02d03f8cfdf4ad7aee3178e871cc105)limited

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_br\_discovery\_param::limited |
| --- |

True if limited discovery procedure is to be used.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_8h_source.md)

- [bt\_br\_discovery\_param](structbt__br__discovery__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
