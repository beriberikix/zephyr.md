---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__can__isotp.html
original_path: doxygen/html/group__can__isotp.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CAN ISO-TP Protocol

[Connectivity](group__connectivity.md)

CAN ISO-TP Protocol.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [isotp\_msg\_id](structisotp__msg__id.md) |
|  | ISO-TP message id struct. [More...](structisotp__msg__id.md#details) |
| struct | [isotp\_fc\_opts](structisotp__fc__opts.md) |
|  | ISO-TP frame control options struct. [More...](structisotp__fc__opts.md#details) |

| Macros | |
| --- | --- |
| #define | [ISOTP\_N\_OK](#gab7daaebbc303665beb2946ce077d5312)   0 |
|  | Completed successfully. |
| #define | [ISOTP\_N\_TIMEOUT\_A](#ga8298423e96932f94308f3064755d18fb)   -1 |
|  | Ar/As has timed out. |
| #define | [ISOTP\_N\_TIMEOUT\_BS](#ga9e525bb24928a2656e7cd2842b306553)   -2 |
|  | Reception of next FC has timed out. |
| #define | [ISOTP\_N\_TIMEOUT\_CR](#ga77b802df46c66ed6002f143b57f73b7a)   -3 |
|  | Cr has timed out. |
| #define | [ISOTP\_N\_WRONG\_SN](#ga9caa5677a171e1bd0be06ebb6b006046)   -4 |
|  | Unexpected sequence number. |
| #define | [ISOTP\_N\_INVALID\_FS](#ga99312831df8e1822f02b41e3fccc0661)   -5 |
|  | Invalid flow status received. |
| #define | [ISOTP\_N\_UNEXP\_PDU](#ga45e3bfdd3948be6ccb3daec5db412b78)   -6 |
|  | Unexpected PDU received. |
| #define | [ISOTP\_N\_WFT\_OVRN](#gad6bcb7b6fb8ab30da1a4ddeabe3e3178)   -7 |
|  | Maximum number of WAIT flowStatus PDUs exceeded. |
| #define | [ISOTP\_N\_BUFFER\_OVERFLW](#ga1b8e6b35a637b5f98e7a2ab4270efd41)   -8 |
|  | FlowStatus OVFLW PDU was received. |
| #define | [ISOTP\_N\_ERROR](#ga0805646e65d39a9e2f15e110720887ca)   -9 |
|  | General error. |
| #define | [ISOTP\_NO\_FREE\_FILTER](#gaf0624cd5e7d12e94f4a739bc47ee0361)   -10 |
|  | Implementation specific errors. |
| #define | [ISOTP\_NO\_NET\_BUF\_LEFT](#ga901f61175e228a70c2f882bc999caea6)   -11 |
|  | No net buffer left to allocate. |
| #define | [ISOTP\_NO\_BUF\_DATA\_LEFT](#gaed5270f0ee489128adb8c2ea481c6c77)   -12 |
|  | Not sufficient space in the buffer left for the data. |
| #define | [ISOTP\_NO\_CTX\_LEFT](#gac5cb1fafeb8aa5cf9fe1695612671c7d)   -13 |
|  | No context buffer left to allocate. |
| #define | [ISOTP\_RECV\_TIMEOUT](#gaa3e873d4a80ee128f1858520874f93b6)   -14 |
|  | Timeout for recv. |
| #define | [ISOTP\_FIXED\_ADDR\_SA\_POS](#gaedb0e7330d19b1cdc380c0b36cabf2f5)   (CONFIG\_ISOTP\_FIXED\_ADDR\_SA\_POS) |
|  | Position of fixed source address (SA). |
| #define | [ISOTP\_FIXED\_ADDR\_SA\_MASK](#ga2a9cbfd95bae05a9f7433f3b1c58689e)   (CONFIG\_ISOTP\_FIXED\_ADDR\_SA\_MASK) |
|  | Mask to obtain fixed source address (SA). |
| #define | [ISOTP\_FIXED\_ADDR\_TA\_POS](#ga2b64d4dffde99159ae5120586364e1c6)   (CONFIG\_ISOTP\_FIXED\_ADDR\_TA\_POS) |
|  | Position of fixed target address (TA). |
| #define | [ISOTP\_FIXED\_ADDR\_TA\_MASK](#ga5d5415982e04e506c9b045bfbe2be337)   (CONFIG\_ISOTP\_FIXED\_ADDR\_TA\_MASK) |
|  | Mask to obtain fixed target address (TA). |
| #define | [ISOTP\_FIXED\_ADDR\_PRIO\_POS](#ga29f8806889f4e41c1529c35a56ee98a9)   (CONFIG\_ISOTP\_FIXED\_ADDR\_PRIO\_POS) |
|  | Position of priority in fixed addressing mode. |
| #define | [ISOTP\_FIXED\_ADDR\_PRIO\_MASK](#gab5dc33148923e7cd58b438a8906d1ace)   (CONFIG\_ISOTP\_FIXED\_ADDR\_PRIO\_MASK) |
|  | Mask for priority in fixed addressing mode. |
| #define | [ISOTP\_FIXED\_ADDR\_RX\_MASK](#gac27b3210cb754b4621c54923696bfe2d)   (CONFIG\_ISOTP\_FIXED\_ADDR\_RX\_MASK) |
|  | CAN filter RX mask to match any priority and source address (SA). |

| Typedefs | |
| --- | --- |
| typedef void(\* | [isotp\_tx\_callback\_t](#gad4f9c0d3f847d453ea662128db2603bb)) (int error\_nr, void \*arg) |
|  | Transmission callback. |

| Functions | |
| --- | --- |
| int | [isotp\_bind](#ga725696a26c3bdc0c99e3c4e611a897f9) (struct isotp\_recv\_ctx \*rctx, const struct [device](structdevice.md) \*can\_dev, const struct [isotp\_msg\_id](structisotp__msg__id.md) \*rx\_addr, const struct [isotp\_msg\_id](structisotp__msg__id.md) \*tx\_addr, const struct [isotp\_fc\_opts](structisotp__fc__opts.md) \*opts, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Bind an address to a receiving context. |
| void | [isotp\_unbind](#ga622293da5564203bf6dcb993410d21ba) (struct isotp\_recv\_ctx \*rctx) |
|  | Unbind a context from the interface. |
| int | [isotp\_recv](#ga79c9cad7f39802c5c80af743717e22c6) (struct isotp\_recv\_ctx \*rctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Read out received data from fifo. |
| int | [isotp\_recv\_net](#ga4fb0ef794b7c4104d6e6b17bc68e09d8) (struct isotp\_recv\_ctx \*rctx, struct [net\_buf](structnet__buf.md) \*\*buffer, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get the net buffer on data reception. |
| int | [isotp\_send](#ga3723fae583a1d7deabc2deee475ba756) (struct isotp\_send\_ctx \*sctx, const struct [device](structdevice.md) \*can\_dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [isotp\_msg\_id](structisotp__msg__id.md) \*tx\_addr, const struct [isotp\_msg\_id](structisotp__msg__id.md) \*rx\_addr, [isotp\_tx\_callback\_t](#gad4f9c0d3f847d453ea662128db2603bb) complete\_cb, void \*cb\_arg) |
|  | Send data. |

| ISO-TP message ID flags | |
| --- | --- |
|  | |
| #define | [ISOTP\_MSG\_EXT\_ADDR](#ga903d326b3bfb05151b9d5d0a0ace59b9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Message uses ISO-TP extended addressing (first payload byte of CAN frame). |
| #define | [ISOTP\_MSG\_FIXED\_ADDR](#ga998ae9b1645485f567e692bfbaa50cbe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Message uses ISO-TP fixed addressing (according to SAE J1939). |
| #define | [ISOTP\_MSG\_IDE](#ga16935466c1a543c03d11b71b8944d0b8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Message uses extended (29-bit) CAN ID. |
| #define | [ISOTP\_MSG\_FDF](#ga70b485a2e576b1b0fec2cc8037215bd9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Message uses CAN FD format (FDF). |
| #define | [ISOTP\_MSG\_BRS](#ga9275708b5afba61c8b5c98c718ec4635)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Message uses CAN FD Baud Rate Switch (BRS). |

## Detailed Description

CAN ISO-TP Protocol.

## Macro Definition Documentation

## [◆ ](#gab5dc33148923e7cd58b438a8906d1ace)ISOTP\_FIXED\_ADDR\_PRIO\_MASK

| #define ISOTP\_FIXED\_ADDR\_PRIO\_MASK   (CONFIG\_ISOTP\_FIXED\_ADDR\_PRIO\_MASK) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Mask for priority in fixed addressing mode.

## [◆ ](#ga29f8806889f4e41c1529c35a56ee98a9)ISOTP\_FIXED\_ADDR\_PRIO\_POS

| #define ISOTP\_FIXED\_ADDR\_PRIO\_POS   (CONFIG\_ISOTP\_FIXED\_ADDR\_PRIO\_POS) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Position of priority in fixed addressing mode.

## [◆ ](#gac27b3210cb754b4621c54923696bfe2d)ISOTP\_FIXED\_ADDR\_RX\_MASK

| #define ISOTP\_FIXED\_ADDR\_RX\_MASK   (CONFIG\_ISOTP\_FIXED\_ADDR\_RX\_MASK) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

CAN filter RX mask to match any priority and source address (SA).

## [◆ ](#ga2a9cbfd95bae05a9f7433f3b1c58689e)ISOTP\_FIXED\_ADDR\_SA\_MASK

| #define ISOTP\_FIXED\_ADDR\_SA\_MASK   (CONFIG\_ISOTP\_FIXED\_ADDR\_SA\_MASK) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Mask to obtain fixed source address (SA).

## [◆ ](#gaedb0e7330d19b1cdc380c0b36cabf2f5)ISOTP\_FIXED\_ADDR\_SA\_POS

| #define ISOTP\_FIXED\_ADDR\_SA\_POS   (CONFIG\_ISOTP\_FIXED\_ADDR\_SA\_POS) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Position of fixed source address (SA).

## [◆ ](#ga5d5415982e04e506c9b045bfbe2be337)ISOTP\_FIXED\_ADDR\_TA\_MASK

| #define ISOTP\_FIXED\_ADDR\_TA\_MASK   (CONFIG\_ISOTP\_FIXED\_ADDR\_TA\_MASK) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Mask to obtain fixed target address (TA).

## [◆ ](#ga2b64d4dffde99159ae5120586364e1c6)ISOTP\_FIXED\_ADDR\_TA\_POS

| #define ISOTP\_FIXED\_ADDR\_TA\_POS   (CONFIG\_ISOTP\_FIXED\_ADDR\_TA\_POS) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Position of fixed target address (TA).

## [◆ ](#ga9275708b5afba61c8b5c98c718ec4635)ISOTP\_MSG\_BRS

| #define ISOTP\_MSG\_BRS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Message uses CAN FD Baud Rate Switch (BRS).

Only valid in combination with [ISOTP\_MSG\_FDF](#ga70b485a2e576b1b0fec2cc8037215bd9).

## [◆ ](#ga903d326b3bfb05151b9d5d0a0ace59b9)ISOTP\_MSG\_EXT\_ADDR

| #define ISOTP\_MSG\_EXT\_ADDR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Message uses ISO-TP extended addressing (first payload byte of CAN frame).

## [◆ ](#ga70b485a2e576b1b0fec2cc8037215bd9)ISOTP\_MSG\_FDF

| #define ISOTP\_MSG\_FDF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Message uses CAN FD format (FDF).

## [◆ ](#ga998ae9b1645485f567e692bfbaa50cbe)ISOTP\_MSG\_FIXED\_ADDR

| #define ISOTP\_MSG\_FIXED\_ADDR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Message uses ISO-TP fixed addressing (according to SAE J1939).

Only valid in combination with [ISOTP\_MSG\_IDE](#ga16935466c1a543c03d11b71b8944d0b8).

## [◆ ](#ga16935466c1a543c03d11b71b8944d0b8)ISOTP\_MSG\_IDE

| #define ISOTP\_MSG\_IDE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Message uses extended (29-bit) CAN ID.

## [◆ ](#ga1b8e6b35a637b5f98e7a2ab4270efd41)ISOTP\_N\_BUFFER\_OVERFLW

| #define ISOTP\_N\_BUFFER\_OVERFLW   -8 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

FlowStatus OVFLW PDU was received.

## [◆ ](#ga0805646e65d39a9e2f15e110720887ca)ISOTP\_N\_ERROR

| #define ISOTP\_N\_ERROR   -9 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

General error.

## [◆ ](#ga99312831df8e1822f02b41e3fccc0661)ISOTP\_N\_INVALID\_FS

| #define ISOTP\_N\_INVALID\_FS   -5 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Invalid flow status received.

## [◆ ](#gab7daaebbc303665beb2946ce077d5312)ISOTP\_N\_OK

| #define ISOTP\_N\_OK   0 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Completed successfully.

## [◆ ](#ga8298423e96932f94308f3064755d18fb)ISOTP\_N\_TIMEOUT\_A

| #define ISOTP\_N\_TIMEOUT\_A   -1 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Ar/As has timed out.

## [◆ ](#ga9e525bb24928a2656e7cd2842b306553)ISOTP\_N\_TIMEOUT\_BS

| #define ISOTP\_N\_TIMEOUT\_BS   -2 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Reception of next FC has timed out.

## [◆ ](#ga77b802df46c66ed6002f143b57f73b7a)ISOTP\_N\_TIMEOUT\_CR

| #define ISOTP\_N\_TIMEOUT\_CR   -3 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Cr has timed out.

## [◆ ](#ga45e3bfdd3948be6ccb3daec5db412b78)ISOTP\_N\_UNEXP\_PDU

| #define ISOTP\_N\_UNEXP\_PDU   -6 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Unexpected PDU received.

## [◆ ](#gad6bcb7b6fb8ab30da1a4ddeabe3e3178)ISOTP\_N\_WFT\_OVRN

| #define ISOTP\_N\_WFT\_OVRN   -7 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Maximum number of WAIT flowStatus PDUs exceeded.

## [◆ ](#ga9caa5677a171e1bd0be06ebb6b006046)ISOTP\_N\_WRONG\_SN

| #define ISOTP\_N\_WRONG\_SN   -4 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Unexpected sequence number.

## [◆ ](#gaed5270f0ee489128adb8c2ea481c6c77)ISOTP\_NO\_BUF\_DATA\_LEFT

| #define ISOTP\_NO\_BUF\_DATA\_LEFT   -12 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Not sufficient space in the buffer left for the data.

## [◆ ](#gac5cb1fafeb8aa5cf9fe1695612671c7d)ISOTP\_NO\_CTX\_LEFT

| #define ISOTP\_NO\_CTX\_LEFT   -13 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

No context buffer left to allocate.

## [◆ ](#gaf0624cd5e7d12e94f4a739bc47ee0361)ISOTP\_NO\_FREE\_FILTER

| #define ISOTP\_NO\_FREE\_FILTER   -10 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Implementation specific errors.

Can't bind or send because the CAN device has no filter left

## [◆ ](#ga901f61175e228a70c2f882bc999caea6)ISOTP\_NO\_NET\_BUF\_LEFT

| #define ISOTP\_NO\_NET\_BUF\_LEFT   -11 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

No net buffer left to allocate.

## [◆ ](#gaa3e873d4a80ee128f1858520874f93b6)ISOTP\_RECV\_TIMEOUT

| #define ISOTP\_RECV\_TIMEOUT   -14 |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Timeout for recv.

## Typedef Documentation

## [◆ ](#gad4f9c0d3f847d453ea662128db2603bb)isotp\_tx\_callback\_t

| typedef void(\* isotp\_tx\_callback\_t) (int error\_nr, void \*arg) |
| --- |

`#include <[isotp.h](isotp_8h.md)>`

Transmission callback.

This callback is called when a transmission is completed.

Parameters
:   | error\_nr | ISOTP\_N\_OK on success, ISOTP\_N\_\* on error |
    | --- | --- |
    | arg | Callback argument passed to the send function |

## Function Documentation

## [◆ ](#ga725696a26c3bdc0c99e3c4e611a897f9)isotp\_bind()

| int isotp\_bind | ( | struct isotp\_recv\_ctx \* | *rctx*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *can\_dev*, |
|  |  | const struct [isotp\_msg\_id](structisotp__msg__id.md) \* | *rx\_addr*, |
|  |  | const struct [isotp\_msg\_id](structisotp__msg__id.md) \* | *tx\_addr*, |
|  |  | const struct [isotp\_fc\_opts](structisotp__fc__opts.md) \* | *opts*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[isotp.h](isotp_8h.md)>`

Bind an address to a receiving context.

This function binds an RX and TX address combination to an RX context. When data arrives from the specified address, it is buffered and can be read by calling isotp\_recv. When calling this routine, a filter is applied in the CAN device, and the context is initialized. The context must be valid until calling unbind.

Parameters
:   | rctx | Context to store the internal states. |
    | --- | --- |
    | can\_dev | The CAN device to be used for sending and receiving. |
    | rx\_addr | Identifier for incoming data. |
    | tx\_addr | Identifier for FC frames. |
    | opts | Flow control options. |
    | timeout | Timeout for FF SF buffer allocation. |

Return values
:   | [ISOTP\_N\_OK](#gab7daaebbc303665beb2946ce077d5312) | on success |
    | --- | --- |
    | [ISOTP\_NO\_FREE\_FILTER](#gaf0624cd5e7d12e94f4a739bc47ee0361) | if CAN device has no filters left. |

## [◆ ](#ga79c9cad7f39802c5c80af743717e22c6)isotp\_recv()

| int isotp\_recv | ( | struct isotp\_recv\_ctx \* | *rctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[isotp.h](isotp_8h.md)>`

Read out received data from fifo.

This function reads the data from the receive FIFO of the context. It blocks if the FIFO is empty. If an error occurs, the function returns a negative number and leaves the data buffer unchanged.

Parameters
:   | rctx | Context that is already bound. |
    | --- | --- |
    | data | Pointer to a buffer where the data is copied to. |
    | len | Size of the buffer. |
    | timeout | Timeout for incoming data. |

Return values
:   | Number | of bytes copied on success |
    | --- | --- |
    | [ISOTP\_RECV\_TIMEOUT](#gaa3e873d4a80ee128f1858520874f93b6) | when "timeout" timed out |
    | ISOTP\_N\_\* | on error |

## [◆ ](#ga4fb0ef794b7c4104d6e6b17bc68e09d8)isotp\_recv\_net()

| int isotp\_recv\_net | ( | struct isotp\_recv\_ctx \* | *rctx*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \*\* | *buffer*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[isotp.h](isotp_8h.md)>`

Get the net buffer on data reception.

This function reads incoming data into net-buffers. It blocks until the entire packet is received, BS is reached, or an error occurred. If BS was zero, the data is in a single [net\_buf](structnet__buf.md "Network buffer representation."). Otherwise, the data is fragmented in chunks of BS size. The net-buffers are referenced and must be freed with net\_buf\_unref after the data is processed.

Parameters
:   | rctx | Context that is already bound. |
    | --- | --- |
    | buffer | Pointer where the [net\_buf](structnet__buf.md "Network buffer representation.") pointer is written to. |
    | timeout | Timeout for incoming data. |

Return values
:   | Remaining | data length for this transfer if BS > 0, 0 for BS = 0 |
    | --- | --- |
    | [ISOTP\_RECV\_TIMEOUT](#gaa3e873d4a80ee128f1858520874f93b6) | when "timeout" timed out |
    | ISOTP\_N\_\* | on error |

## [◆ ](#ga3723fae583a1d7deabc2deee475ba756)isotp\_send()

| int isotp\_send | ( | struct isotp\_send\_ctx \* | *sctx*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *can\_dev*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const struct [isotp\_msg\_id](structisotp__msg__id.md) \* | *tx\_addr*, |
|  |  | const struct [isotp\_msg\_id](structisotp__msg__id.md) \* | *rx\_addr*, |
|  |  | [isotp\_tx\_callback\_t](#gad4f9c0d3f847d453ea662128db2603bb) | *complete\_cb*, |
|  |  | void \* | *cb\_arg* ) |

`#include <[isotp.h](isotp_8h.md)>`

Send data.

This function is used to send data to a peer that listens to the tx\_addr. An internal work-queue is used to transfer the segmented data. Data and context must be valid until the transmission has finished. If a complete\_cb is given, this function is non-blocking, and the callback is called on completion with the return value as a parameter.

Parameters
:   | sctx | Context to store the internal states. |
    | --- | --- |
    | can\_dev | The CAN device to be used for sending and receiving. |
    | data | Data to be sent. |
    | len | Length of the data to be sent. |
    | rx\_addr | Identifier for FC frames. |
    | tx\_addr | Identifier for outgoing frames the receiver listens on. |
    | complete\_cb | Function called on completion or NULL. |
    | cb\_arg | Argument passed to the complete callback. |

Return values
:   | [ISOTP\_N\_OK](#gab7daaebbc303665beb2946ce077d5312) | on success |
    | --- | --- |
    | ISOTP\_N\_\* | on error |

## [◆ ](#ga622293da5564203bf6dcb993410d21ba)isotp\_unbind()

| void isotp\_unbind | ( | struct isotp\_recv\_ctx \* | *rctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[isotp.h](isotp_8h.md)>`

Unbind a context from the interface.

This function removes the binding from isotp\_bind. The filter is detached from the CAN device, and if a transmission is ongoing, buffers are freed. The context can be discarded safely after calling this function.

Parameters
:   | rctx | Context that should be unbound. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
