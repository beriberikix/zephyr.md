---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/socketcan_8h.html
original_path: doxygen/html/socketcan_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socketcan.h File Reference

SocketCAN definitions.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`

[Go to the source code of this file.](socketcan_8h_source.md)

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
| #define | [CAN\_RAW](group__socket__can.md#ga57682d9a1e4f4d90943dbaa683582bf5)   1 |
|  | Protocols of the protocol family PF\_CAN. |
| #define | [SOCKETCAN\_MAX\_DLEN](group__socket__can.md#ga3ec3e39a63684e78a52cf9160c82c257)   8U |
|  | SocketCAN max data length. |
| #define | [CAN\_MTU](group__socket__can.md#ga7d1f583cdc56ead407496713f3f22ac8)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [socketcan\_frame](structsocketcan__frame.md))) |
|  | CAN frame MTU. |
| #define | [CANFD\_BRS](group__socket__can.md#gace1d124719f8eac5f59788811c4afaf4)   0x01 |
|  | Bit rate switch (second bitrate for payload data). |
| #define | [CANFD\_ESI](group__socket__can.md#gacfc1bf4466d32189a1708b4351df0794)   0x02 |
|  | Error state indicator of the transmitting node. |
| #define | [CANFD\_FDF](group__socket__can.md#ga409cae306f00226ef192320f4f01f51c)   0x04 |
|  | Mark CAN FD for dual use of struct canfd\_frame. |

| Typedefs | |
| --- | --- |
| Linux SocketCAN compatibility | |
| The following structures and functions provide compatibility with the CAN frame and CAN filter formats used by Linux SocketCAN. | |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) |
|  | CAN Identifier structure for Linux SocketCAN compatibility. |

## Detailed Description

SocketCAN definitions.

Definitions for SocketCAN support.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socketcan.h](socketcan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
