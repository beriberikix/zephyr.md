---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structshell__uart__async.html
original_path: doxygen/html/structshell__uart__async.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_uart\_async Struct Reference

`#include <[shell_uart.h](shell__uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [shell\_uart\_common](structshell__uart__common.md) | [common](#acb159e579d504b40c574c811c433b307) |
| struct k\_sem | [tx\_sem](#a0d6fa4de1d68adafcf2937e2fdb8119e) |
| struct [uart\_async\_rx](structuart__async__rx.md) | [async\_rx](#a2410eaa1860e6f00ed12ceab5927bbed) |
| struct [uart\_async\_rx\_config](structuart__async__rx__config.md) | [async\_rx\_config](#a96f02b1cd55c7ee2edba7277e105c32d) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [pending\_rx\_req](#a2d13bc10a0150623a10a8e76fb61d526) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_data](#adca67272c56eaebcc1ddde44bb5ec774) [(0 \*(0+[UART\_ASYNC\_RX\_BUF\_OVERHEAD](uart__async__rx_8h.md#ab845a83272799083bf3ecd7a9c8cf2ce)))] |

## Field Documentation

## [◆ ](#a2410eaa1860e6f00ed12ceab5927bbed)async\_rx

| struct [uart\_async\_rx](structuart__async__rx.md) shell\_uart\_async::async\_rx |
| --- |

## [◆ ](#a96f02b1cd55c7ee2edba7277e105c32d)async\_rx\_config

| struct [uart\_async\_rx\_config](structuart__async__rx__config.md) shell\_uart\_async::async\_rx\_config |
| --- |

## [◆ ](#acb159e579d504b40c574c811c433b307)common

| struct [shell\_uart\_common](structshell__uart__common.md) shell\_uart\_async::common |
| --- |

## [◆ ](#a2d13bc10a0150623a10a8e76fb61d526)pending\_rx\_req

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) shell\_uart\_async::pending\_rx\_req |
| --- |

## [◆ ](#adca67272c56eaebcc1ddde44bb5ec774)rx\_data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_uart\_async::rx\_data[(0 \*(0+ [UART\_ASYNC\_RX\_BUF\_OVERHEAD](uart__async__rx_8h.md#ab845a83272799083bf3ecd7a9c8cf2ce)))] |
| --- |

## [◆ ](#a0d6fa4de1d68adafcf2937e2fdb8119e)tx\_sem

| struct k\_sem shell\_uart\_async::tx\_sem |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_uart.h](shell__uart_8h_source.md)

- [shell\_uart\_async](structshell__uart__async.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
