---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/isotp_8h.html
original_path: doxygen/html/isotp_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

isotp.h File Reference

Public API for ISO-TP (ISO 15765-2:2016).
[More...](#details)

`#include <[zephyr/drivers/can.h](drivers_2can_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/buf.h](net_2buf_8h_source.md)>`

[Go to the source code of this file.](isotp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [isotp\_msg\_id](structisotp__msg__id.md) |
|  | ISO-TP message id struct. [More...](structisotp__msg__id.md#details) |
| struct | [isotp\_fc\_opts](structisotp__fc__opts.md) |
|  | ISO-TP frame control options struct. [More...](structisotp__fc__opts.md#details) |

| Macros | |
| --- | --- |
| #define | [ISOTP\_N\_OK](group__can__isotp.md#gab7daaebbc303665beb2946ce077d5312)   0 |
|  | Completed successfully. |
| #define | [ISOTP\_N\_TIMEOUT\_A](group__can__isotp.md#ga8298423e96932f94308f3064755d18fb)   -1 |
|  | Ar/As has timed out. |
| #define | [ISOTP\_N\_TIMEOUT\_BS](group__can__isotp.md#ga9e525bb24928a2656e7cd2842b306553)   -2 |
|  | Reception of next FC has timed out. |
| #define | [ISOTP\_N\_TIMEOUT\_CR](group__can__isotp.md#ga77b802df46c66ed6002f143b57f73b7a)   -3 |
|  | Cr has timed out. |
| #define | [ISOTP\_N\_WRONG\_SN](group__can__isotp.md#ga9caa5677a171e1bd0be06ebb6b006046)   -4 |
|  | Unexpected sequence number. |
| #define | [ISOTP\_N\_INVALID\_FS](group__can__isotp.md#ga99312831df8e1822f02b41e3fccc0661)   -5 |
|  | Invalid flow status received. |
| #define | [ISOTP\_N\_UNEXP\_PDU](group__can__isotp.md#ga45e3bfdd3948be6ccb3daec5db412b78)   -6 |
|  | Unexpected PDU received. |
| #define | [ISOTP\_N\_WFT\_OVRN](group__can__isotp.md#gad6bcb7b6fb8ab30da1a4ddeabe3e3178)   -7 |
|  | Maximum number of WAIT flowStatus PDUs exceeded. |
| #define | [ISOTP\_N\_BUFFER\_OVERFLW](group__can__isotp.md#ga1b8e6b35a637b5f98e7a2ab4270efd41)   -8 |
|  | FlowStatus OVFLW PDU was received. |
| #define | [ISOTP\_N\_ERROR](group__can__isotp.md#ga0805646e65d39a9e2f15e110720887ca)   -9 |
|  | General error. |
| #define | [ISOTP\_NO\_FREE\_FILTER](group__can__isotp.md#gaf0624cd5e7d12e94f4a739bc47ee0361)   -10 |
|  | Implementation specific errors. |
| #define | [ISOTP\_NO\_NET\_BUF\_LEFT](group__can__isotp.md#ga901f61175e228a70c2f882bc999caea6)   -11 |
|  | No net buffer left to allocate. |
| #define | [ISOTP\_NO\_BUF\_DATA\_LEFT](group__can__isotp.md#gaed5270f0ee489128adb8c2ea481c6c77)   -12 |
|  | Not sufficient space in the buffer left for the data. |
| #define | [ISOTP\_NO\_CTX\_LEFT](group__can__isotp.md#gac5cb1fafeb8aa5cf9fe1695612671c7d)   -13 |
|  | No context buffer left to allocate. |
| #define | [ISOTP\_RECV\_TIMEOUT](group__can__isotp.md#gaa3e873d4a80ee128f1858520874f93b6)   -14 |
|  | Timeout for recv. |
| #define | [ISOTP\_FIXED\_ADDR\_SA\_POS](group__can__isotp.md#gaedb0e7330d19b1cdc380c0b36cabf2f5)   (CONFIG\_ISOTP\_FIXED\_ADDR\_SA\_POS) |
|  | Position of fixed source address (SA). |
| #define | [ISOTP\_FIXED\_ADDR\_SA\_MASK](group__can__isotp.md#ga2a9cbfd95bae05a9f7433f3b1c58689e)   (CONFIG\_ISOTP\_FIXED\_ADDR\_SA\_MASK) |
|  | Mask to obtain fixed source address (SA). |
| #define | [ISOTP\_FIXED\_ADDR\_TA\_POS](group__can__isotp.md#ga2b64d4dffde99159ae5120586364e1c6)   (CONFIG\_ISOTP\_FIXED\_ADDR\_TA\_POS) |
|  | Position of fixed target address (TA). |
| #define | [ISOTP\_FIXED\_ADDR\_TA\_MASK](group__can__isotp.md#ga5d5415982e04e506c9b045bfbe2be337)   (CONFIG\_ISOTP\_FIXED\_ADDR\_TA\_MASK) |
|  | Mask to obtain fixed target address (TA). |
| #define | [ISOTP\_FIXED\_ADDR\_PRIO\_POS](group__can__isotp.md#ga29f8806889f4e41c1529c35a56ee98a9)   (CONFIG\_ISOTP\_FIXED\_ADDR\_PRIO\_POS) |
|  | Position of priority in fixed addressing mode. |
| #define | [ISOTP\_FIXED\_ADDR\_PRIO\_MASK](group__can__isotp.md#gab5dc33148923e7cd58b438a8906d1ace)   (CONFIG\_ISOTP\_FIXED\_ADDR\_PRIO\_MASK) |
|  | Mask for priority in fixed addressing mode. |
| #define | [ISOTP\_FIXED\_ADDR\_RX\_MASK](group__can__isotp.md#gac27b3210cb754b4621c54923696bfe2d)   (CONFIG\_ISOTP\_FIXED\_ADDR\_RX\_MASK) |
|  | CAN filter RX mask to match any priority and source address (SA). |
| ISO-TP message ID flags | |
|  | |
| #define | [ISOTP\_MSG\_EXT\_ADDR](group__can__isotp.md#ga903d326b3bfb05151b9d5d0a0ace59b9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Message uses ISO-TP extended addressing (first payload byte of CAN frame). |
| #define | [ISOTP\_MSG\_FIXED\_ADDR](group__can__isotp.md#ga998ae9b1645485f567e692bfbaa50cbe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Message uses ISO-TP fixed addressing (according to SAE J1939). |
| #define | [ISOTP\_MSG\_IDE](group__can__isotp.md#ga16935466c1a543c03d11b71b8944d0b8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Message uses extended (29-bit) CAN ID. |
| #define | [ISOTP\_MSG\_FDF](group__can__isotp.md#ga70b485a2e576b1b0fec2cc8037215bd9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Message uses CAN FD format (FDF). |
| #define | [ISOTP\_MSG\_BRS](group__can__isotp.md#ga9275708b5afba61c8b5c98c718ec4635)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Message uses CAN FD Baud Rate Switch (BRS). |

| Typedefs | |
| --- | --- |
| typedef void(\* | [isotp\_tx\_callback\_t](group__can__isotp.md#gad4f9c0d3f847d453ea662128db2603bb)) (int error\_nr, void \*arg) |
|  | Transmission callback. |

| Functions | |
| --- | --- |
| int | [isotp\_bind](group__can__isotp.md#ga725696a26c3bdc0c99e3c4e611a897f9) (struct isotp\_recv\_ctx \*rctx, const struct [device](structdevice.md) \*can\_dev, const struct [isotp\_msg\_id](structisotp__msg__id.md) \*rx\_addr, const struct [isotp\_msg\_id](structisotp__msg__id.md) \*tx\_addr, const struct [isotp\_fc\_opts](structisotp__fc__opts.md) \*opts, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Bind an address to a receiving context. |
| void | [isotp\_unbind](group__can__isotp.md#ga622293da5564203bf6dcb993410d21ba) (struct isotp\_recv\_ctx \*rctx) |
|  | Unbind a context from the interface. |
| int | [isotp\_recv](group__can__isotp.md#ga79c9cad7f39802c5c80af743717e22c6) (struct isotp\_recv\_ctx \*rctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Read out received data from fifo. |
| int | [isotp\_recv\_net](group__can__isotp.md#ga4fb0ef794b7c4104d6e6b17bc68e09d8) (struct isotp\_recv\_ctx \*rctx, struct [net\_buf](structnet__buf.md) \*\*buffer, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get the net buffer on data reception. |
| int | [isotp\_send](group__can__isotp.md#ga3723fae583a1d7deabc2deee475ba756) (struct isotp\_send\_ctx \*sctx, const struct [device](structdevice.md) \*can\_dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [isotp\_msg\_id](structisotp__msg__id.md) \*tx\_addr, const struct [isotp\_msg\_id](structisotp__msg__id.md) \*rx\_addr, [isotp\_tx\_callback\_t](group__can__isotp.md#gad4f9c0d3f847d453ea662128db2603bb) complete\_cb, void \*cb\_arg) |
|  | Send data. |

## Detailed Description

Public API for ISO-TP (ISO 15765-2:2016).

ISO-TP is a transport protocol for CAN (Controller Area Network)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [canbus](dir_7890c2fc429c7c0e4d7e0cd7b89129f9.md)
- [isotp.h](isotp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
