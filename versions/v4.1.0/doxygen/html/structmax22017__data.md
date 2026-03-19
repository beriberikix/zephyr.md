---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmax22017__data.html
original_path: doxygen/html/structmax22017__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max22017\_data Struct Reference

`#include <[max22017.h](max22017_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#a0f281976d848ce06e43e39d7c8e555f6) |
| struct [k\_mutex](structk__mutex.md) | [lock](#a996ed1088ac25904049fd500ff20c8d5) |
| struct [k\_work](structk__work.md) | [int\_work](#a3e58c68a77e41a0009ed3b8f314e8a1d) |
| struct [gpio\_callback](structgpio__callback.md) | [callback\_int](#a3404c90326b35195ccce3d502205b0ae) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [crc\_enabled](#afb03a179a5d64e90003f1fb8f4f6100a) |

## Field Documentation

## [◆ ](#a3404c90326b35195ccce3d502205b0ae)callback\_int

| struct [gpio\_callback](structgpio__callback.md) max22017\_data::callback\_int |
| --- |

## [◆ ](#afb03a179a5d64e90003f1fb8f4f6100a)crc\_enabled

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) max22017\_data::crc\_enabled |
| --- |

## [◆ ](#a0f281976d848ce06e43e39d7c8e555f6)dev

| const struct [device](structdevice.md)\* max22017\_data::dev |
| --- |

## [◆ ](#a3e58c68a77e41a0009ed3b8f314e8a1d)int\_work

| struct [k\_work](structk__work.md) max22017\_data::int\_work |
| --- |

## [◆ ](#a996ed1088ac25904049fd500ff20c8d5)lock

| struct [k\_mutex](structk__mutex.md) max22017\_data::lock |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/mfd/[max22017.h](max22017_8h_source.md)

- [max22017\_data](structmax22017__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
