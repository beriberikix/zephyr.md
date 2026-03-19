---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/uart__async__rx_8h.html
original_path: doxygen/html/uart__async__rx_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_async\_rx.h File Reference

Helper module for receiving using UART Asynchronous API.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](uart__async__rx_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [uart\_async\_rx\_buf](structuart__async__rx__buf.md) |
| struct | [uart\_async\_rx](structuart__async__rx.md) |
|  | UART asynchronous RX helper structure. [More...](structuart__async__rx.md#details) |
| struct | [uart\_async\_rx\_config](structuart__async__rx__config.md) |
|  | UART asynchronous RX helper configuration structure. [More...](structuart__async__rx__config.md#details) |

| Macros | |
| --- | --- |
| #define | [UART\_ASYNC\_RX\_BUF\_OVERHEAD](#ab845a83272799083bf3ecd7a9c8cf2ce)   offsetof(struct [uart\_async\_rx\_buf](structuart__async__rx__buf.md), buffer) |
|  | Get amount of space dedicated for managing each buffer state. |

| Functions | |
| --- | --- |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [uart\_async\_rx\_get\_buf\_len](#a9e51885811653d21e0e8712b09ef800d) (struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx) |
|  | Get RX buffer length. |
| int | [uart\_async\_rx\_init](#a8daddb05f11ad43c8c4510a4312cf38f) (struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx, const struct [uart\_async\_rx\_config](structuart__async__rx__config.md) \*config) |
|  | Initialize the helper instance. |
| void | [uart\_async\_rx\_reset](#ad551b1684437c8ab48c0708fb5b0d1f6) (struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx) |
|  | Reset state of the helper instance. |
| void | [uart\_async\_rx\_on\_rdy](#acca21c43fa833b4789edbc1bc92bab2b) (struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Indicate received data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [uart\_async\_rx\_buf\_req](#a1eede7070affe966616148924ba2c519) (struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx) |
|  | Get next RX buffer. |
| void | [uart\_async\_rx\_on\_buf\_rel](#a2064f3d760adb4cf6912caf12f7a54cc) (struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf) |
|  | Indicate that buffer is no longer used by the UART driver. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [uart\_async\_rx\_data\_claim](#a8d5ed81dfa4c067f173249744b25561e) (struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Claim received data for processing. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [uart\_async\_rx\_data\_consume](#a1ac0b3ee0e1840177d07c4fbcbd635df) (struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Consume claimed data. |

## Detailed Description

Helper module for receiving using UART Asynchronous API.

## Macro Definition Documentation

## [◆ ](#ab845a83272799083bf3ecd7a9c8cf2ce)UART\_ASYNC\_RX\_BUF\_OVERHEAD

| #define UART\_ASYNC\_RX\_BUF\_OVERHEAD   offsetof(struct [uart\_async\_rx\_buf](structuart__async__rx__buf.md), buffer) |
| --- |

Get amount of space dedicated for managing each buffer state.

User buffer provided during the initialization is split into chunks and each chunk has overhead. This overhead can be used to calculate actual space used for UART data.

Returns
:   Overhead space in bytes.

## Function Documentation

## [◆ ](#a1eede7070affe966616148924ba2c519)uart\_async\_rx\_buf\_req()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* uart\_async\_rx\_buf\_req | ( | struct [uart\_async\_rx](structuart__async__rx.md) \* | *async\_rx* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get next RX buffer.

Returned pointer shall be provided to [uart\_rx\_buf\_rsp](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a "uart_rx_buf_rsp") or [uart\_rx\_enable](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8 "uart_rx_enable"). If null is returned that indicates that there are no available buffers since all buffers are used by the driver or contain not consumed data.

Parameters
:   | async\_rx | Pointer to the helper instance. |
    | --- | --- |

Returns
:   Pointer to the next RX buffer or null if no buffer available.

## [◆ ](#a8d5ed81dfa4c067f173249744b25561e)uart\_async\_rx\_data\_claim()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) uart\_async\_rx\_data\_claim | ( | struct [uart\_async\_rx](structuart__async__rx.md) \* | *async\_rx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

Claim received data for processing.

Helper module works in the zero copy mode. It provides a pointer to the buffer that was directly used by the UART driver. Since received data is spread across multiple buffers there is no possibility to read all data at once. It can only be consumed in chunks. After data is processed, [uart\_async\_rx\_data\_consume](#a1ac0b3ee0e1840177d07c4fbcbd635df) is used to indicate that data is consumed.

Parameters
:   | async\_rx | Pointer to the helper instance. |
    | --- | --- |
    | data | Location where address to the buffer is written. Untouched if no data to claim. |
    | length | Amount of requested data. |

Returns
:   Amount valid of data in the `data` buffer. 0 is returned when there is no data.

## [◆ ](#a1ac0b3ee0e1840177d07c4fbcbd635df)uart\_async\_rx\_data\_consume()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) uart\_async\_rx\_data\_consume | ( | struct [uart\_async\_rx](structuart__async__rx.md) \* | *async\_rx*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

Consume claimed data.

It pairs with [uart\_async\_rx\_data\_claim](#a8d5ed81dfa4c067f173249744b25561e).

Parameters
:   | async\_rx | Pointer to the helper instance. |
    | --- | --- |
    | length | Amount of data to consume. It must be less or equal than amount of claimed data. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If there are free buffers in the pool after data got consumed. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If there are no free buffers. |

## [◆ ](#a9e51885811653d21e0e8712b09ef800d)uart\_async\_rx\_get\_buf\_len()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uart\_async\_rx\_get\_buf\_len | ( | struct [uart\_async\_rx](structuart__async__rx.md) \* | *async\_rx* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get RX buffer length.

Parameters
:   | async\_rx | Pointer to the helper instance. |
    | --- | --- |

Returns
:   Buffer length.

## [◆ ](#a8daddb05f11ad43c8c4510a4312cf38f)uart\_async\_rx\_init()

| int uart\_async\_rx\_init | ( | struct [uart\_async\_rx](structuart__async__rx.md) \* | *async\_rx*, |
| --- | --- | --- | --- |
|  |  | const struct [uart\_async\_rx\_config](structuart__async__rx__config.md) \* | *config* ) |

Initialize the helper instance.

Parameters
:   | async\_rx | Pointer to the helper instance. |
    | --- | --- |
    | config | Configuration. Must be persistent. |

Return values
:   | 0 | on successful initialization. |
    | --- | --- |

## [◆ ](#a2064f3d760adb4cf6912caf12f7a54cc)uart\_async\_rx\_on\_buf\_rel()

| void uart\_async\_rx\_on\_buf\_rel | ( | struct [uart\_async\_rx](structuart__async__rx.md) \* | *async\_rx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf* ) |

Indicate that buffer is no longer used by the UART driver.

Function shall be called on [UART\_RX\_BUF\_RELEASED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48 "UART_RX_BUF_RELEASED") event.

Parameters
:   | async\_rx | Pointer to the helper instance. |
    | --- | --- |
    | buf | Buffer pointer received in the UART driver event. |

## [◆ ](#acca21c43fa833b4789edbc1bc92bab2b)uart\_async\_rx\_on\_rdy()

| void uart\_async\_rx\_on\_rdy | ( | struct [uart\_async\_rx](structuart__async__rx.md) \* | *async\_rx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

Indicate received data.

Function shall be called from [UART\_RX\_RDY](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7 "UART_RX_RDY") context.

Parameters
:   | async\_rx | Pointer to the helper instance. |
    | --- | --- |
    | buffer | Buffer received in the UART driver event. |
    | length | Length received in the UART driver event. |

## [◆ ](#ad551b1684437c8ab48c0708fb5b0d1f6)uart\_async\_rx\_reset()

| void uart\_async\_rx\_reset | ( | struct [uart\_async\_rx](structuart__async__rx.md) \* | *async\_rx* | ) |  |
| --- | --- | --- | --- | --- | --- |

Reset state of the helper instance.

Helper can be reset after RX abort to discard all received data and bring the helper to its initial state.

Parameters
:   | async\_rx | Pointer to the helper instance. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [serial](dir_19e6ea47bd3dc215ff4232c3392e0b57.md)
- [uart\_async\_rx.h](uart__async__rx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
