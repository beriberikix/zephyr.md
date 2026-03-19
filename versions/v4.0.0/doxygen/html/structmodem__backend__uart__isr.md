---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmodem__backend__uart__isr.html
original_path: doxygen/html/structmodem__backend__uart__isr.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_backend\_uart\_isr Struct Reference

`#include <[uart.h](modem_2backend_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [ring\_buf](structring__buf.md) | [receive\_rdb](#afacd3e6c890a30188987e6cffae03981) [2] |
| struct [ring\_buf](structring__buf.md) | [transmit\_rb](#a69aa3fbffb2bfbd8d5ca16effb8f4f17) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [transmit\_buf\_len](#a4d270cc8e2260c349c588109a3c4ddae) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [receive\_buf\_len](#a2c50ecd1dad68ee2aa2ad57b1b746831) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [receive\_rdb\_used](#ac7a373618e4dc5dfda02bbc9d09a11a3) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [transmit\_buf\_put\_limit](#a3b0413caf39e82a52e2bbab6ba42ac3b) |

## Field Documentation

## [◆ ](#a2c50ecd1dad68ee2aa2ad57b1b746831)receive\_buf\_len

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) modem\_backend\_uart\_isr::receive\_buf\_len |
| --- |

## [◆ ](#afacd3e6c890a30188987e6cffae03981)receive\_rdb

| struct [ring\_buf](structring__buf.md) modem\_backend\_uart\_isr::receive\_rdb[2] |
| --- |

## [◆ ](#ac7a373618e4dc5dfda02bbc9d09a11a3)receive\_rdb\_used

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modem\_backend\_uart\_isr::receive\_rdb\_used |
| --- |

## [◆ ](#a4d270cc8e2260c349c588109a3c4ddae)transmit\_buf\_len

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) modem\_backend\_uart\_isr::transmit\_buf\_len |
| --- |

## [◆ ](#a3b0413caf39e82a52e2bbab6ba42ac3b)transmit\_buf\_put\_limit

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) modem\_backend\_uart\_isr::transmit\_buf\_put\_limit |
| --- |

## [◆ ](#a69aa3fbffb2bfbd8d5ca16effb8f4f17)transmit\_rb

| struct [ring\_buf](structring__buf.md) modem\_backend\_uart\_isr::transmit\_rb |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/backend/[uart.h](modem_2backend_2uart_8h_source.md)

- [modem\_backend\_uart\_isr](structmodem__backend__uart__isr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
