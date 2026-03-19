---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmodem__backend__uart__async.html
original_path: doxygen/html/structmodem__backend__uart__async.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_backend\_uart\_async Struct Reference

`#include <[uart.h](modem_2backend_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [receive\_bufs](#a8e6ff3cae3a79e8b26e67282bb50f5ad) [2] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [receive\_buf\_size](#a85e0e51366bbb2e1d7a72e0b9a0650ee) |
| struct [ring\_buf](structring__buf.md) | [receive\_rb](#ac3909d735bfecac46001f1b289e222a2) |
| struct [k\_spinlock](structk__spinlock.md) | [receive\_rb\_lock](#ab61b263cdbe9bfb796f3dd6ed69b3dea) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [transmit\_buf](#ad05072659c6a38de672fcfa881bab70f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [transmit\_buf\_size](#a7501362bf312cbd6f5b3a67c9edfba50) |
| struct [k\_work](structk__work.md) | [rx\_disabled\_work](#ab98122a94d28b6b5d88e7dbcec6d82df) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [state](#abf5f1dcbf57797ff9d3687331f973b55) |

## Field Documentation

## [◆ ](#a85e0e51366bbb2e1d7a72e0b9a0650ee)receive\_buf\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) modem\_backend\_uart\_async::receive\_buf\_size |
| --- |

## [◆ ](#a8e6ff3cae3a79e8b26e67282bb50f5ad)receive\_bufs

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_backend\_uart\_async::receive\_bufs[2] |
| --- |

## [◆ ](#ac3909d735bfecac46001f1b289e222a2)receive\_rb

| struct [ring\_buf](structring__buf.md) modem\_backend\_uart\_async::receive\_rb |
| --- |

## [◆ ](#ab61b263cdbe9bfb796f3dd6ed69b3dea)receive\_rb\_lock

| struct [k\_spinlock](structk__spinlock.md) modem\_backend\_uart\_async::receive\_rb\_lock |
| --- |

## [◆ ](#ab98122a94d28b6b5d88e7dbcec6d82df)rx\_disabled\_work

| struct [k\_work](structk__work.md) modem\_backend\_uart\_async::rx\_disabled\_work |
| --- |

## [◆ ](#abf5f1dcbf57797ff9d3687331f973b55)state

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) modem\_backend\_uart\_async::state |
| --- |

## [◆ ](#ad05072659c6a38de672fcfa881bab70f)transmit\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_backend\_uart\_async::transmit\_buf |
| --- |

## [◆ ](#a7501362bf312cbd6f5b3a67c9edfba50)transmit\_buf\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) modem\_backend\_uart\_async::transmit\_buf\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/backend/[uart.h](modem_2backend_2uart_8h_source.md)

- [modem\_backend\_uart\_async](structmodem__backend__uart__async.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
