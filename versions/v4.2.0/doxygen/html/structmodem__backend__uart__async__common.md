---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmodem__backend__uart__async__common.html
original_path: doxygen/html/structmodem__backend__uart__async__common.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_backend\_uart\_async\_common Struct Reference

`#include <[zephyr/modem/backend/uart.h](modem_2backend_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [transmit\_buf](#a41f85b18c22fc678ce06b5ea42dd052a) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [transmit\_buf\_size](#a37c79230e6f796fa12dfc4eed5e94fcc) |
| struct [k\_work](structk__work.md) | [rx\_disabled\_work](#a3996a268ebdeefec160ed80d122ce533) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [state](#a4e542d2880b320f3b843fc3813c0fd0f) |

## Field Documentation

## [◆ ](#a3996a268ebdeefec160ed80d122ce533)rx\_disabled\_work

| struct [k\_work](structk__work.md) modem\_backend\_uart\_async\_common::rx\_disabled\_work |
| --- |

## [◆ ](#a4e542d2880b320f3b843fc3813c0fd0f)state

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) modem\_backend\_uart\_async\_common::state |
| --- |

## [◆ ](#a41f85b18c22fc678ce06b5ea42dd052a)transmit\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_backend\_uart\_async\_common::transmit\_buf |
| --- |

## [◆ ](#a37c79230e6f796fa12dfc4eed5e94fcc)transmit\_buf\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) modem\_backend\_uart\_async\_common::transmit\_buf\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/backend/[uart.h](modem_2backend_2uart_8h_source.md)

- [modem\_backend\_uart\_async\_common](structmodem__backend__uart__async__common.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
