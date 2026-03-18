---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__socket__can.html
original_path: doxygen/html/group__socket__can.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Core Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

SocketCAN library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [sockaddr\_can](structsockaddr__can.md) |
|  | struct [sockaddr\_can](structsockaddr__can.md "struct sockaddr_can - The sockaddr structure for CAN sockets") - The sockaddr structure for CAN sockets [More...](structsockaddr__can.md#details) |
| struct | [socketcan\_frame](structsocketcan__frame.md) |
|  | CAN frame for Linux SocketCAN compatibility. [More...](structsocketcan__frame.md#details) |
| struct | [socketcan\_filter](structsocketcan__filter.md) |
|  | CAN filter for Linux SocketCAN compatibility. [More...](structsocketcan__filter.md#details) |

| Macros | |
| --- | --- |
| #define | [CAN\_RAW](#ga57682d9a1e4f4d90943dbaa683582bf5)   1 |
| #define | [SOL\_CAN\_BASE](#ga844d9f6f282d8e95d264f6340a0018fa)   100 |
| #define | [SOL\_CAN\_RAW](#gad981aa82a29d828882a2fb4c35c1cdd7)   ([SOL\_CAN\_BASE](#ga844d9f6f282d8e95d264f6340a0018fa) + [CAN\_RAW](#ga57682d9a1e4f4d90943dbaa683582bf5)) |
| #define | [SOCKETCAN\_MAX\_DLEN](#ga3ec3e39a63684e78a52cf9160c82c257)   8U |
| #define | [CAN\_MTU](#ga7d1f583cdc56ead407496713f3f22ac8)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [socketcan\_frame](structsocketcan__frame.md))) |
| #define | [CANFD\_BRS](#gace1d124719f8eac5f59788811c4afaf4)   0x01 /\* bit rate switch (second bitrate for payload data) \*/ |
| #define | [CANFD\_ESI](#gacfc1bf4466d32189a1708b4351df0794)   0x02 /\* error [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) indicator of the transmitting node \*/ |
| #define | [CANFD\_FDF](#ga409cae306f00226ef192320f4f01f51c)   0x04 /\* mark CAN FD for dual use of struct canfd\_frame \*/ |

| Enumerations | |
| --- | --- |
| enum | { [CAN\_RAW\_FILTER](#gga0878a39c728876bf39637e284a5b132ba1650b3e04298c36834ffa7dca117443a) = 1 } |

| Functions | |
| --- | --- |
| static void | [socketcan\_to\_can\_frame](#gaccedf1d7bf2131797e53a16dc93cd7e1) (const struct [socketcan\_frame](structsocketcan__frame.md) \*sframe, struct [can\_frame](structcan__frame.md) \*zframe) |
|  | Translate a *[socketcan\_frame](structsocketcan__frame.md "CAN frame for Linux SocketCAN compatibility.")* struct to a *[can\_frame](structcan__frame.md "CAN frame structure.")* struct. |
| static void | [socketcan\_from\_can\_frame](#ga49ffbe49124fdc472946fd0978f9a6d5) (const struct [can\_frame](structcan__frame.md) \*zframe, struct [socketcan\_frame](structsocketcan__frame.md) \*sframe) |
|  | Translate a *[can\_frame](structcan__frame.md "CAN frame structure.")* struct to a *[socketcan\_frame](structsocketcan__frame.md "CAN frame for Linux SocketCAN compatibility.")* struct. |
| static void | [socketcan\_to\_can\_filter](#ga040c4882d349cdc3c568f3580e823cba) (const struct [socketcan\_filter](structsocketcan__filter.md) \*sfilter, struct [can\_filter](structcan__filter.md) \*zfilter) |
|  | Translate a *[socketcan\_filter](structsocketcan__filter.md "CAN filter for Linux SocketCAN compatibility.")* struct to a *[can\_filter](structcan__filter.md "CAN filter structure.")* struct. |
| static void | [socketcan\_from\_can\_filter](#gaf5cee7f0d6385c6fc4736e9399ed06b3) (const struct [can\_filter](structcan__filter.md) \*zfilter, struct [socketcan\_filter](structsocketcan__filter.md) \*sfilter) |
|  | Translate a *[can\_filter](structcan__filter.md "CAN filter structure.")* struct to a *[socketcan\_filter](structsocketcan__filter.md "CAN filter for Linux SocketCAN compatibility.")* struct. |

| Linux SocketCAN compatibility | |
| --- | --- |
| The following structures and functions provide compatibility with the CAN frame and CAN filter formats used by Linux SocketCAN. | |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [socketcan\_id\_t](#ga35a7941726d1e22defd8c3098391ca8e) |
|  | CAN Identifier structure for Linux SocketCAN compatibility. |

## Detailed Description

SocketCAN library.

SocketCAN utilities.

## Macro Definition Documentation

## [◆ ](#ga7d1f583cdc56ead407496713f3f22ac8)CAN\_MTU

| #define CAN\_MTU   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [socketcan\_frame](structsocketcan__frame.md))) |
| --- |

`#include <[socketcan.h](socketcan_8h.md)>`

## [◆ ](#ga57682d9a1e4f4d90943dbaa683582bf5)CAN\_RAW

| #define CAN\_RAW   1 |
| --- |

`#include <[socketcan.h](socketcan_8h.md)>`

## [◆ ](#gace1d124719f8eac5f59788811c4afaf4)CANFD\_BRS

| #define CANFD\_BRS   0x01 /\* bit rate switch (second bitrate for payload data) \*/ |
| --- |

`#include <[socketcan.h](socketcan_8h.md)>`

## [◆ ](#gacfc1bf4466d32189a1708b4351df0794)CANFD\_ESI

| #define CANFD\_ESI   0x02 /\* error [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) indicator of the transmitting node \*/ |
| --- |

`#include <[socketcan.h](socketcan_8h.md)>`

## [◆ ](#ga409cae306f00226ef192320f4f01f51c)CANFD\_FDF

| #define CANFD\_FDF   0x04 /\* mark CAN FD for dual use of struct canfd\_frame \*/ |
| --- |

`#include <[socketcan.h](socketcan_8h.md)>`

## [◆ ](#ga3ec3e39a63684e78a52cf9160c82c257)SOCKETCAN\_MAX\_DLEN

| #define SOCKETCAN\_MAX\_DLEN   8U |
| --- |

`#include <[socketcan.h](socketcan_8h.md)>`

## [◆ ](#ga844d9f6f282d8e95d264f6340a0018fa)SOL\_CAN\_BASE

| #define SOL\_CAN\_BASE   100 |
| --- |

`#include <[socketcan.h](socketcan_8h.md)>`

## [◆ ](#gad981aa82a29d828882a2fb4c35c1cdd7)SOL\_CAN\_RAW

| #define SOL\_CAN\_RAW   ([SOL\_CAN\_BASE](#ga844d9f6f282d8e95d264f6340a0018fa) + [CAN\_RAW](#ga57682d9a1e4f4d90943dbaa683582bf5)) |
| --- |

`#include <[socketcan.h](socketcan_8h.md)>`

## Typedef Documentation

## [◆ ](#ga35a7941726d1e22defd8c3098391ca8e)socketcan\_id\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [socketcan\_id\_t](#ga35a7941726d1e22defd8c3098391ca8e) |
| --- |

`#include <[socketcan.h](socketcan_8h.md)>`

CAN Identifier structure for Linux SocketCAN compatibility.

The fields in this type are:

+------+--------------------------------------------------------------+

| Bits | Description |

+======+==============================================================+

| 0-28 | CAN identifier (11/29 bit) |

+------+--------------------------------------------------------------+

| 29 | Error message frame flag (0 = data frame, 1 = error message) |

+------+--------------------------------------------------------------+

| 30 | Remote transmission request flag (1 = RTR frame) |

+------+--------------------------------------------------------------+

| 31 | Frame format flag (0 = standard 11 bit, 1 = extended 29 bit) |

+------+--------------------------------------------------------------+

## Enumeration Type Documentation

## [◆ ](#ga0878a39c728876bf39637e284a5b132b)anonymous enum

| anonymous enum |
| --- |

`#include <[socketcan.h](socketcan_8h.md)>`

| Enumerator | |
| --- | --- |
| CAN\_RAW\_FILTER |  |

## Function Documentation

## [◆ ](#gaf5cee7f0d6385c6fc4736e9399ed06b3)socketcan\_from\_can\_filter()

| | void socketcan\_from\_can\_filter | ( | const struct [can\_filter](structcan__filter.md) \* | *zfilter*, | | --- | --- | --- | --- | |  |  | struct [socketcan\_filter](structsocketcan__filter.md) \* | *sfilter* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socketcan_utils.h](socketcan__utils_8h.md)>`

Translate a *[can\_filter](structcan__filter.md "CAN filter structure.")* struct to a *[socketcan\_filter](structsocketcan__filter.md "CAN filter for Linux SocketCAN compatibility.")* struct.

Parameters
:   | zfilter | Pointer to [can\_filter](structcan__filter.md "CAN filter structure.") struct. |
    | --- | --- |
    | sfilter | Pointer to [socketcan\_filter](structsocketcan__filter.md "CAN filter for Linux SocketCAN compatibility.") struct. |

## [◆ ](#ga49ffbe49124fdc472946fd0978f9a6d5)socketcan\_from\_can\_frame()

| | void socketcan\_from\_can\_frame | ( | const struct [can\_frame](structcan__frame.md) \* | *zframe*, | | --- | --- | --- | --- | |  |  | struct [socketcan\_frame](structsocketcan__frame.md) \* | *sframe* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socketcan_utils.h](socketcan__utils_8h.md)>`

Translate a *[can\_frame](structcan__frame.md "CAN frame structure.")* struct to a *[socketcan\_frame](structsocketcan__frame.md "CAN frame for Linux SocketCAN compatibility.")* struct.

Parameters
:   | zframe | Pointer to [can\_frame](structcan__frame.md "CAN frame structure.") struct. |
    | --- | --- |
    | sframe | Pointer to [socketcan\_frame](structsocketcan__frame.md "CAN frame for Linux SocketCAN compatibility.") struct. |

## [◆ ](#ga040c4882d349cdc3c568f3580e823cba)socketcan\_to\_can\_filter()

| | void socketcan\_to\_can\_filter | ( | const struct [socketcan\_filter](structsocketcan__filter.md) \* | *sfilter*, | | --- | --- | --- | --- | |  |  | struct [can\_filter](structcan__filter.md) \* | *zfilter* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socketcan_utils.h](socketcan__utils_8h.md)>`

Translate a *[socketcan\_filter](structsocketcan__filter.md "CAN filter for Linux SocketCAN compatibility.")* struct to a *[can\_filter](structcan__filter.md "CAN filter structure.")* struct.

Parameters
:   | sfilter | Pointer to [socketcan\_filter](structsocketcan__filter.md "CAN filter for Linux SocketCAN compatibility.") struct. |
    | --- | --- |
    | zfilter | Pointer to [can\_filter](structcan__filter.md "CAN filter structure.") struct. |

## [◆ ](#gaccedf1d7bf2131797e53a16dc93cd7e1)socketcan\_to\_can\_frame()

| | void socketcan\_to\_can\_frame | ( | const struct [socketcan\_frame](structsocketcan__frame.md) \* | *sframe*, | | --- | --- | --- | --- | |  |  | struct [can\_frame](structcan__frame.md) \* | *zframe* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socketcan_utils.h](socketcan__utils_8h.md)>`

Translate a *[socketcan\_frame](structsocketcan__frame.md "CAN frame for Linux SocketCAN compatibility.")* struct to a *[can\_frame](structcan__frame.md "CAN frame structure.")* struct.

Parameters
:   | sframe | Pointer to sockecan\_frame struct. |
    | --- | --- |
    | zframe | Pointer to [can\_frame](structcan__frame.md "CAN frame structure.") struct. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
