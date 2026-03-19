---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__le__oob.html
original_path: doxygen/html/structbt__le__oob.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_oob Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

LE Out of Band information.
[More...](#details)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#a17cfed7683efbf5b5954847d655d7424) |
|  | LE address. |
| struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) | [le\_sc\_data](#a80ccd4ab120a880adfff9aba3b19b4fd) |
|  | LE Secure Connections pairing Out of Band data. |

## Detailed Description

LE Out of Band information.

## Field Documentation

## [◆ ](#a17cfed7683efbf5b5954847d655d7424)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_le\_oob::addr |
| --- |

LE address.

If privacy is enabled this is a Resolvable Private Address.

## [◆ ](#a80ccd4ab120a880adfff9aba3b19b4fd)le\_sc\_data

| struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) bt\_le\_oob::le\_sc\_data |
| --- |

LE Secure Connections pairing Out of Band data.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_oob](structbt__le__oob.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
