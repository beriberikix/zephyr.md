---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmodem__backend__uart.html
original_path: doxygen/html/structmodem__backend__uart.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_backend\_uart Struct Reference

`#include <[uart.h](modem_2backend_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [uart](#a26f3331f0ae7d9384f369ae50694090d) |
| struct modem\_pipe | [pipe](#af7e0483a6398b6893ac4693e2bc12f31) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [receive\_ready\_work](#a369c5fd2072e42f5eedfe03a5d312ec6) |
| struct [k\_work](structk__work.md) | [transmit\_idle\_work](#aafd345ff47cc51a9e1100604a51f6b2d) |
| union { |  |
| struct [modem\_backend\_uart\_isr](structmodem__backend__uart__isr.md)   [isr](#a812165945d6a4aba4fd6bc5ba26b3082) |  |
| struct [modem\_backend\_uart\_async](structmodem__backend__uart__async.md)   [async](#a387327d6378834136fe6a0e80cec7337) |  |
| }; |  |

## Field Documentation

## [◆ ](#aa0880365ddedbc3e9ee3bc37a70a740e)[union]

| union { ... } [modem\_backend\_uart](structmodem__backend__uart.md) |
| --- |

## [◆ ](#a387327d6378834136fe6a0e80cec7337)async

| struct [modem\_backend\_uart\_async](structmodem__backend__uart__async.md) modem\_backend\_uart::async |
| --- |

## [◆ ](#a812165945d6a4aba4fd6bc5ba26b3082)isr

| struct [modem\_backend\_uart\_isr](structmodem__backend__uart__isr.md) modem\_backend\_uart::isr |
| --- |

## [◆ ](#af7e0483a6398b6893ac4693e2bc12f31)pipe

| struct modem\_pipe modem\_backend\_uart::pipe |
| --- |

## [◆ ](#a369c5fd2072e42f5eedfe03a5d312ec6)receive\_ready\_work

| struct [k\_work\_delayable](structk__work__delayable.md) modem\_backend\_uart::receive\_ready\_work |
| --- |

## [◆ ](#aafd345ff47cc51a9e1100604a51f6b2d)transmit\_idle\_work

| struct [k\_work](structk__work.md) modem\_backend\_uart::transmit\_idle\_work |
| --- |

## [◆ ](#a26f3331f0ae7d9384f369ae50694090d)uart

| const struct [device](structdevice.md)\* modem\_backend\_uart::uart |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/backend/[uart.h](modem_2backend_2uart_8h_source.md)

- [modem\_backend\_uart](structmodem__backend__uart.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
