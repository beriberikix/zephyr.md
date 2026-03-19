---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__uart__async.html
original_path: doxygen/html/group__uart__async.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Async UART API

[Device Driver APIs](group__io__interfaces.md) » [UART Interface](group__uart__interface.md)

| Data Structures | |
| --- | --- |
| struct | [uart\_event\_tx](structuart__event__tx.md) |
|  | UART TX event data. [More...](structuart__event__tx.md#details) |
| struct | [uart\_event\_rx](structuart__event__rx.md) |
|  | UART RX event data. [More...](structuart__event__rx.md#details) |
| struct | [uart\_event\_rx\_buf](structuart__event__rx__buf.md) |
|  | UART RX buffer released event data. [More...](structuart__event__rx__buf.md#details) |
| struct | [uart\_event\_rx\_stop](structuart__event__rx__stop.md) |
|  | UART RX stopped data. [More...](structuart__event__rx__stop.md#details) |
| struct | [uart\_event](structuart__event.md) |
|  | Structure containing information about current event. [More...](structuart__event.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [uart\_callback\_t](#ga00b7c98a4da3ea3675d0a40c5dacb136)) (const struct [device](structdevice.md) \*dev, struct [uart\_event](structuart__event.md) \*evt, void \*user\_data) |
|  | Define the application callback function signature for [uart\_callback\_set()](#gad33e627ed8729409b14e92453e53459c) function. |

| Enumerations | |
| --- | --- |
| enum | [uart\_event\_type](#gaf0c9513cbafa36d86b4c83f2b6a03dcd) {     [UART\_TX\_DONE](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) , [UART\_TX\_ABORTED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) , [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) , [UART\_RX\_BUF\_REQUEST](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) ,     [UART\_RX\_BUF\_RELEASED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) , [UART\_RX\_DISABLED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) , [UART\_RX\_STOPPED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)   } |
|  | Types of events passed to callback in UART\_ASYNC\_API. [More...](#gaf0c9513cbafa36d86b4c83f2b6a03dcd) |

| Functions | |
| --- | --- |
| static int | [uart\_callback\_set](#gad33e627ed8729409b14e92453e53459c) (const struct [device](structdevice.md) \*dev, [uart\_callback\_t](#ga00b7c98a4da3ea3675d0a40c5dacb136) callback, void \*user\_data) |
|  | Set event handler function. |
| int | [uart\_tx](#gaf99f32ce2e2d9beb32a2f2e5a26320dc) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Send given number of bytes from buffer through UART. |
| int | [uart\_tx\_u16](#gab0ea611cd072fa459a6f1780ce62c9e3) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Send given number of datum from buffer through UART. |
| int | [uart\_tx\_abort](#gaa8a26d3ea685fb98030ea03613be6280) (const struct [device](structdevice.md) \*dev) |
|  | Abort current TX transmission. |
| int | [uart\_rx\_enable](#ga902e18c2a727ed2988e1b6caa6a444b8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Start receiving data through UART. |
| int | [uart\_rx\_enable\_u16](#ga12d91846133351a85fa471fa90f2a0fd) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Start receiving wide data through UART. |
| static int | [uart\_rx\_buf\_rsp](#ga3970fe2818e214b0814ea8b73a816a6a) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Provide receive buffer in response to [UART\_RX\_BUF\_REQUEST](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) event. |
| static int | [uart\_rx\_buf\_rsp\_u16](#ga778bcfc30be853c8d320f295b34c17c0) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Provide wide data receive buffer in response to [UART\_RX\_BUF\_REQUEST](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) event. |
| int | [uart\_rx\_disable](#gafd4753bee51b230091a3c6ddb26ea734) (const struct [device](structdevice.md) \*dev) |
|  | Disable RX. |

## Detailed Description

Since
:   1.14

Version
:   0.8.0

## Typedef Documentation

## [◆ ](#ga00b7c98a4da3ea3675d0a40c5dacb136)uart\_callback\_t

| typedef void(\* uart\_callback\_t) (const struct [device](structdevice.md) \*dev, struct [uart\_event](structuart__event.md) \*evt, void \*user\_data) |
| --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Define the application callback function signature for [uart\_callback\_set()](#gad33e627ed8729409b14e92453e53459c) function.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | evt | Pointer to [uart\_event](structuart__event.md "Structure containing information about current event.") instance. |
    | user\_data | Pointer to data specified by user. |

## Enumeration Type Documentation

## [◆ ](#gaf0c9513cbafa36d86b4c83f2b6a03dcd)uart\_event\_type

| enum [uart\_event\_type](#gaf0c9513cbafa36d86b4c83f2b6a03dcd) |
| --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Types of events passed to callback in UART\_ASYNC\_API.

Receiving:

1. To start receiving, uart\_rx\_enable has to be called with first buffer
2. When receiving starts to current buffer, [UART\_RX\_BUF\_REQUEST](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) will be generated, in response to that user can either:
   - Provide second buffer using uart\_rx\_buf\_rsp, when first buffer is filled, receiving will automatically start to second buffer.
   - Ignore the event, this way when current buffer is filled [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event will be generated and receiving will be stopped.
3. If some data was received and timeout occurred [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event will be generated. It can happen multiples times for the same buffer. RX timeout is counted from last byte received i.e. if no data was received, there won't be any timeout event.
4. [UART\_RX\_BUF\_RELEASED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) event will be generated when the current buffer is no longer used by the driver. It will immediately follow [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event. Depending on the implementation buffer may be released when it is completely or partially filled.
5. If there was second buffer provided, it will become current buffer and we start again at point 2. If no second buffer was specified receiving is stopped and [UART\_RX\_DISABLED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) event is generated. After that whole process can be repeated.

Any time during reception [UART\_RX\_STOPPED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd) event can occur. if there is any data received, [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event will be generated. It will be followed by [UART\_RX\_BUF\_RELEASED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) event for every buffer currently passed to driver and finally by [UART\_RX\_DISABLED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) event.

Receiving can be disabled using uart\_rx\_disable, after calling that function, if there is any data received, [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event will be generated. [UART\_RX\_BUF\_RELEASED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) event will be generated for every buffer currently passed to driver and finally [UART\_RX\_DISABLED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) event will occur.

Transmitting:

1. Transmitting starts by uart\_tx function.
2. If whole buffer was transmitted [UART\_TX\_DONE](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) is generated. If timeout occurred [UART\_TX\_ABORTED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) will be generated.

Transmitting can be aborted using [uart\_tx\_abort](#gaa8a26d3ea685fb98030ea03613be6280), after calling that function [UART\_TX\_ABORTED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) event will be generated.

| Enumerator | |
| --- | --- |
| UART\_TX\_DONE | Whole TX buffer was transmitted. |
| UART\_TX\_ABORTED | Transmitting aborted due to timeout or uart\_tx\_abort call.  When flow control is enabled, there is a possibility that TX transfer won't finish in the allotted time. Some data may have been transferred, information about it can be found in event data. |
| UART\_RX\_RDY | Received data is ready for processing.  This event is generated in the following cases:   - When RX timeout occurred, and data was stored in provided buffer. This can happen multiple times in the same buffer. - When provided buffer is full. - After [uart\_rx\_disable()](#gafd4753bee51b230091a3c6ddb26ea734). - After stopping due to external event ([UART\_RX\_STOPPED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)). |
| UART\_RX\_BUF\_REQUEST | Driver requests next buffer for continuous reception.  This event is triggered when receiving has started for a new buffer, i.e. it's time to provide a next buffer for a seamless switchover to it. For continuous reliable receiving, user should provide another RX buffer in response to this event, using uart\_rx\_buf\_rsp function  If uart\_rx\_buf\_rsp is not called before current buffer is filled up, receiving will stop. |
| UART\_RX\_BUF\_RELEASED | Buffer is no longer used by UART driver. |
| UART\_RX\_DISABLED | RX has been disabled and can be reenabled.  This event is generated whenever receiver has been stopped, disabled or finished its operation and can be enabled again using uart\_rx\_enable |
| UART\_RX\_STOPPED | RX has stopped due to external event.  Reason is one of [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88 "Reception stop reasons."). |

## Function Documentation

## [◆ ](#gad33e627ed8729409b14e92453e53459c)uart\_callback\_set()

| | int uart\_callback\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uart\_callback\_t](#ga00b7c98a4da3ea3675d0a40c5dacb136) | *callback*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Set event handler function.

Since it is mandatory to set callback to use other asynchronous functions, it can be used to detect if the device supports asynchronous API. Remaining API does not have that detection.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | callback | Event handler. |
    | user\_data | Data to pass to event handler function. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If not supported by the device. |
    | -ENOTSUP | If API not enabled. |

## [◆ ](#ga3970fe2818e214b0814ea8b73a816a6a)uart\_rx\_buf\_rsp()

| | int uart\_rx\_buf\_rsp | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Provide receive buffer in response to [UART\_RX\_BUF\_REQUEST](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) event.

Provide pointer to RX buffer, which will be used when current buffer is filled.

Note
:   Providing buffer that is already in usage by driver leads to undefined behavior. Buffer can be reused when it has been released by driver.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | buf | Pointer to receive buffer. |
    | len | Buffer length. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |
    | -EBUSY | Next buffer already set. |
    | -EACCES | Receiver is already disabled (function called too late?). |
    | -errno | Other negative errno value in case of failure. |

## [◆ ](#ga778bcfc30be853c8d320f295b34c17c0)uart\_rx\_buf\_rsp\_u16()

| | int uart\_rx\_buf\_rsp\_u16 | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Provide wide data receive buffer in response to [UART\_RX\_BUF\_REQUEST](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) event.

Provide pointer to RX buffer, which will be used when current buffer is filled.

Note
:   Providing buffer that is already in usage by driver leads to undefined behavior. Buffer can be reused when it has been released by driver.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | buf | Pointer to wide data receive buffer. |
    | len | Buffer length. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If API is not enabled |
    | -EBUSY | Next buffer already set. |
    | -EACCES | Receiver is already disabled (function called too late?). |
    | -errno | Other negative errno value in case of failure. |

## [◆ ](#gafd4753bee51b230091a3c6ddb26ea734)uart\_rx\_disable()

| int uart\_rx\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Disable RX.

[UART\_RX\_BUF\_RELEASED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) event will be generated for every buffer scheduled, after that [UART\_RX\_DISABLED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) event will be generated. Additionally, if there is any pending received data, the [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event for that data will be generated before the [UART\_RX\_BUF\_RELEASED](#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) events.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |
    | -EFAULT | There is no active reception. |
    | -errno | Other negative errno value in case of failure. |

## [◆ ](#ga902e18c2a727ed2988e1b6caa6a444b8)uart\_rx\_enable()

| int uart\_rx\_enable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Start receiving data through UART.

Function sets given buffer as first buffer for receiving and returns immediately. After that event handler, set using [uart\_callback\_set](#gad33e627ed8729409b14e92453e53459c), is called with [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) or [UART\_RX\_BUF\_REQUEST](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) events.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | buf | Pointer to receive buffer. |
    | len | Buffer length. |
    | timeout | Inactivity period after receiving at least a byte which triggers [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event. Given in microseconds. [SYS\_FOREVER\_US](group__timeutil__unit__apis.md#gad8743aaa97d3b2650908020ffb76ef0e "SYS_FOREVER_US") disables timeout. See [uart\_event\_type](#gaf0c9513cbafa36d86b4c83f2b6a03dcd) for details. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |
    | -EBUSY | RX already in progress. |
    | -errno | Other negative errno value in case of failure. |

## [◆ ](#ga12d91846133351a85fa471fa90f2a0fd)uart\_rx\_enable\_u16()

| int uart\_rx\_enable\_u16 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Start receiving wide data through UART.

Function sets given buffer as first buffer for receiving and returns immediately. After that event handler, set using [uart\_callback\_set](#gad33e627ed8729409b14e92453e53459c), is called with [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) or [UART\_RX\_BUF\_REQUEST](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) events.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | buf | Pointer to wide data receive buffer. |
    | len | Buffer length. |
    | timeout | Inactivity period after receiving at least a byte which triggers [UART\_RX\_RDY](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) event. Given in milliseconds. [SYS\_FOREVER\_MS](group__timeutil__unit__apis.md#ga9f9c4c41f62c7578a30209475201efed "SYS_FOREVER_MS") disables timeout. See [uart\_event\_type](#gaf0c9513cbafa36d86b4c83f2b6a03dcd) for details. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |
    | -EBUSY | RX already in progress. |
    | -errno | Other negative errno value in case of failure. |

## [◆ ](#gaf99f32ce2e2d9beb32a2f2e5a26320dc)uart\_tx()

| int uart\_tx | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Send given number of bytes from buffer through UART.

Function returns immediately and event handler, set using [uart\_callback\_set](#gad33e627ed8729409b14e92453e53459c), is called after transfer is finished.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | buf | Pointer to transmit buffer. |
    | len | Length of transmit buffer. |
    | timeout | Timeout in microseconds. Valid only if flow control is enabled. [SYS\_FOREVER\_US](group__timeutil__unit__apis.md#gad8743aaa97d3b2650908020ffb76ef0e "SYS_FOREVER_US") disables timeout. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |
    | -EBUSY | If There is already an ongoing transfer. |
    | -errno | Other negative errno value in case of failure. |

## [◆ ](#gaa8a26d3ea685fb98030ea03613be6280)uart\_tx\_abort()

| int uart\_tx\_abort | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart.h](drivers_2uart_8h.md)>`

Abort current TX transmission.

[UART\_TX\_DONE](#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) event will be generated with amount of data sent.

Parameters
:   | dev | UART device instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |
    | -EFAULT | There is no active transmission. |
    | -errno | Other negative errno value in case of failure. |

## [◆ ](#gab0ea611cd072fa459a6f1780ce62c9e3)uart\_tx\_u16()

| int uart\_tx\_u16 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Send given number of datum from buffer through UART.

Function returns immediately and event handler, set using [uart\_callback\_set](#gad33e627ed8729409b14e92453e53459c), is called after transfer is finished.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | buf | Pointer to wide data transmit buffer. |
    | len | Length of wide data transmit buffer. |
    | timeout | Timeout in milliseconds. Valid only if flow control is enabled. [SYS\_FOREVER\_MS](group__timeutil__unit__apis.md#ga9f9c4c41f62c7578a30209475201efed "SYS_FOREVER_MS") disables timeout. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If API is not enabled. |
    | -EBUSY | If there is already an ongoing transfer. |
    | -errno | Other negative errno value in case of failure. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
