---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structuart__async__rx.html
original_path: doxygen/html/structuart__async__rx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_async\_rx Struct Reference

UART asynchronous RX helper structure.
[More...](#details)

`#include <[uart_async_rx.h](uart__async__rx_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [uart\_async\_rx\_config](structuart__async__rx__config.md) \* | [config](#abbe20b7426175d7436470f6a26bb578e) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [pending\_bytes](#a1150d2c365330c4d87a22b44412611f6) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [free\_buf\_cnt](#a15510449c58841c7294e0359a92bf4d0) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [buf\_len](#a85ea611224160caee86767b4910e17d9) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [drv\_buf\_idx](#ac782b9465c3766d5217676a3a97a963b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rd\_buf\_idx](#a9a192c4f08f6d946bb562a9bbba8f196) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rd\_idx](#ad75410820beef5a612f602d3017df5f6) |

## Detailed Description

UART asynchronous RX helper structure.

## Field Documentation

## [◆ ](#a85ea611224160caee86767b4910e17d9)buf\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uart\_async\_rx::buf\_len |
| --- |

## [◆ ](#abbe20b7426175d7436470f6a26bb578e)config

| const struct [uart\_async\_rx\_config](structuart__async__rx__config.md)\* uart\_async\_rx::config |
| --- |

## [◆ ](#ac782b9465c3766d5217676a3a97a963b)drv\_buf\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uart\_async\_rx::drv\_buf\_idx |
| --- |

## [◆ ](#a15510449c58841c7294e0359a92bf4d0)free\_buf\_cnt

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) uart\_async\_rx::free\_buf\_cnt |
| --- |

## [◆ ](#a1150d2c365330c4d87a22b44412611f6)pending\_bytes

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) uart\_async\_rx::pending\_bytes |
| --- |

## [◆ ](#a9a192c4f08f6d946bb562a9bbba8f196)rd\_buf\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uart\_async\_rx::rd\_buf\_idx |
| --- |

## [◆ ](#ad75410820beef5a612f602d3017df5f6)rd\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uart\_async\_rx::rd\_idx |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/serial/[uart\_async\_rx.h](uart__async__rx_8h_source.md)

- [uart\_async\_rx](structuart__async__rx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
