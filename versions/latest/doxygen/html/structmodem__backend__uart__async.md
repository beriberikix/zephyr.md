---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmodem__backend__uart__async.html
original_path: doxygen/html/structmodem__backend__uart__async.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_backend\_uart\_async Struct Reference

`#include <[zephyr/modem/backend/uart.h](modem_2backend_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [modem\_backend\_uart\_async\_common](structmodem__backend__uart__async__common.md) | [common](#a8c186bed442db94aa84bf76ad3253fc2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [receive\_bufs](#a8e6ff3cae3a79e8b26e67282bb50f5ad) [2] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [receive\_buf\_size](#a85e0e51366bbb2e1d7a72e0b9a0650ee) |
| struct [ring\_buf](structring__buf.md) | [receive\_rb](#ac3909d735bfecac46001f1b289e222a2) |
| struct [k\_spinlock](structk__spinlock.md) | [receive\_rb\_lock](#ab61b263cdbe9bfb796f3dd6ed69b3dea) |

## Field Documentation

## [◆ ](#a8c186bed442db94aa84bf76ad3253fc2)common

| struct [modem\_backend\_uart\_async\_common](structmodem__backend__uart__async__common.md) modem\_backend\_uart\_async::common |
| --- |

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

---

The documentation for this struct was generated from the following file:

- zephyr/modem/backend/[uart.h](modem_2backend_2uart_8h_source.md)

- [modem\_backend\_uart\_async](structmodem__backend__uart__async.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
