---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structshell__uart__int__driven.html
original_path: doxygen/html/structshell__uart__int__driven.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_uart\_int\_driven Struct Reference

`#include <[shell_uart.h](shell__uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [shell\_uart\_common](structshell__uart__common.md) | [common](#a524615d1e41ed52429a3f1541f39f977) |
| struct [ring\_buf](structring__buf.md) | [tx\_ringbuf](#a308d6b1f53e1c58a6368e9c11a7fedce) |
| struct [ring\_buf](structring__buf.md) | [rx\_ringbuf](#aa099ed76b8ca37637588609fdfbf469d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_buf](#a29fe5ca8668a6db73f5478bad912f37a) [0] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_buf](#aec5209bcb1b41935934f1638f80d676c) [0] |
| struct k\_timer | [dtr\_timer](#ad0ca48ecfcc0c333e3854b656b89b3d3) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [tx\_busy](#ad685a823847bdc230071e1898ebf9562) |

## Field Documentation

## [◆ ](#a524615d1e41ed52429a3f1541f39f977)common

| struct [shell\_uart\_common](structshell__uart__common.md) shell\_uart\_int\_driven::common |
| --- |

## [◆ ](#ad0ca48ecfcc0c333e3854b656b89b3d3)dtr\_timer

| struct k\_timer shell\_uart\_int\_driven::dtr\_timer |
| --- |

## [◆ ](#aec5209bcb1b41935934f1638f80d676c)rx\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_uart\_int\_driven::rx\_buf[0] |
| --- |

## [◆ ](#aa099ed76b8ca37637588609fdfbf469d)rx\_ringbuf

| struct [ring\_buf](structring__buf.md) shell\_uart\_int\_driven::rx\_ringbuf |
| --- |

## [◆ ](#a29fe5ca8668a6db73f5478bad912f37a)tx\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_uart\_int\_driven::tx\_buf[0] |
| --- |

## [◆ ](#ad685a823847bdc230071e1898ebf9562)tx\_busy

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) shell\_uart\_int\_driven::tx\_busy |
| --- |

## [◆ ](#a308d6b1f53e1c58a6368e9c11a7fedce)tx\_ringbuf

| struct [ring\_buf](structring__buf.md) shell\_uart\_int\_driven::tx\_ringbuf |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_uart.h](shell__uart_8h_source.md)

- [shell\_uart\_int\_driven](structshell__uart__int__driven.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
