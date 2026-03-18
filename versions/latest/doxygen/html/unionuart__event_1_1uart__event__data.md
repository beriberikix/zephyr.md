---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/unionuart__event_1_1uart__event__data.html
original_path: doxygen/html/unionuart__event_1_1uart__event__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_event::uart\_event\_data Union Reference

Event data.
[More...](#details)

`#include <[uart.h](drivers_2uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [uart\_event\_tx](structuart__event__tx.md) | [tx](#a79fb6b799d5574c6aa38a211e020035f) |
|  | [UART\_TX\_DONE](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4 "Whole TX buffer was transmitted.") and [UART\_TX\_ABORTED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1 "Transmitting aborted due to timeout or uart_tx_abort call.") events data. |
| struct [uart\_event\_rx](structuart__event__rx.md) | [rx](#afac00624290b8fe5cf7b59516567b972) |
|  | [UART\_RX\_RDY](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7 "Received data is ready for processing.") event data. |
| struct [uart\_event\_rx\_buf](structuart__event__rx__buf.md) | [rx\_buf](#ac03cdaeccba5f693337fa19299101863) |
|  | [UART\_RX\_BUF\_RELEASED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48 "Buffer is no longer used by UART driver.") event data. |
| struct [uart\_event\_rx\_stop](structuart__event__rx__stop.md) | [rx\_stop](#aad7488a2a3d91cea0ea874a08d7b88f6) |
|  | [UART\_RX\_STOPPED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd "RX has stopped due to external event.") event data. |

## Detailed Description

Event data.

## Field Documentation

## [◆ ](#afac00624290b8fe5cf7b59516567b972)rx

| struct [uart\_event\_rx](structuart__event__rx.md) uart\_event::uart\_event\_data::rx |
| --- |

[UART\_RX\_RDY](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7 "Received data is ready for processing.") event data.

## [◆ ](#ac03cdaeccba5f693337fa19299101863)rx\_buf

| struct [uart\_event\_rx\_buf](structuart__event__rx__buf.md) uart\_event::uart\_event\_data::rx\_buf |
| --- |

[UART\_RX\_BUF\_RELEASED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48 "Buffer is no longer used by UART driver.") event data.

## [◆ ](#aad7488a2a3d91cea0ea874a08d7b88f6)rx\_stop

| struct [uart\_event\_rx\_stop](structuart__event__rx__stop.md) uart\_event::uart\_event\_data::rx\_stop |
| --- |

[UART\_RX\_STOPPED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd "RX has stopped due to external event.") event data.

## [◆ ](#a79fb6b799d5574c6aa38a211e020035f)tx

| struct [uart\_event\_tx](structuart__event__tx.md) uart\_event::uart\_event\_data::tx |
| --- |

[UART\_TX\_DONE](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4 "Whole TX buffer was transmitted.") and [UART\_TX\_ABORTED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1 "Transmitting aborted due to timeout or uart_tx_abort call.") events data.

---

The documentation for this union was generated from the following file:

- zephyr/drivers/[uart.h](drivers_2uart_8h_source.md)

- [uart\_event](structuart__event.md)
- [uart\_event\_data](unionuart__event_1_1uart__event__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
