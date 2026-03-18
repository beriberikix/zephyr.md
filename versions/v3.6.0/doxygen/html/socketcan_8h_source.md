---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/socketcan_8h_source.html
original_path: doxygen/html/socketcan_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socketcan.h

[Go to the documentation of this file.](socketcan_8h.md)

1

6

7/\*

8 \* Copyright (c) 2019 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKETCAN\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_SOCKETCAN\_H\_

15

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

18#include <[zephyr/net/net\_if.h](net__if_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

30

31/\* Protocols of the protocol family PF\_CAN \*/

[ 32](group__socket__can.md#ga57682d9a1e4f4d90943dbaa683582bf5)#define CAN\_RAW 1

33

34/\* SocketCAN options \*/

[ 35](group__socket__can.md#ga844d9f6f282d8e95d264f6340a0018fa)#define SOL\_CAN\_BASE 100

[ 36](group__socket__can.md#gad981aa82a29d828882a2fb4c35c1cdd7)#define SOL\_CAN\_RAW (SOL\_CAN\_BASE + CAN\_RAW)

37

38enum {

[ 39](group__socket__can.md#gga0878a39c728876bf39637e284a5b132ba1650b3e04298c36834ffa7dca117443a) [CAN\_RAW\_FILTER](group__socket__can.md#gga0878a39c728876bf39637e284a5b132ba1650b3e04298c36834ffa7dca117443a) = 1,

40};

41

42/\* SocketCAN MTU size compatible with Linux \*/

43#ifdef CONFIG\_CAN\_FD\_MODE

44#define SOCKETCAN\_MAX\_DLEN 64U

45#define CANFD\_MTU (sizeof(struct socketcan\_frame))

46#define CAN\_MTU (CANFD\_MTU - 56U)

47#else /\* CONFIG\_CAN\_FD\_MODE \*/

[ 48](group__socket__can.md#ga3ec3e39a63684e78a52cf9160c82c257)#define SOCKETCAN\_MAX\_DLEN 8U

[ 49](group__socket__can.md#ga7d1f583cdc56ead407496713f3f22ac8)#define CAN\_MTU (sizeof(struct socketcan\_frame))

50#endif /\* !CONFIG\_CAN\_FD\_MODE \*/

51

52/\* CAN FD specific flags from Linux Kernel (include/uapi/linux/can.h) \*/

[ 53](group__socket__can.md#gace1d124719f8eac5f59788811c4afaf4)#define CANFD\_BRS 0x01 /\* bit rate switch (second bitrate for payload data) \*/

[ 54](group__socket__can.md#gacfc1bf4466d32189a1708b4351df0794)#define CANFD\_ESI 0x02 /\* error state indicator of the transmitting node \*/

[ 55](group__socket__can.md#ga409cae306f00226ef192320f4f01f51c)#define CANFD\_FDF 0x04 /\* mark CAN FD for dual use of struct canfd\_frame \*/

56

[ 61](structsockaddr__can.md)struct [sockaddr\_can](structsockaddr__can.md) {

[ 62](structsockaddr__can.md#ae9d8c789193e516c282a707d5a118ebc) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [can\_family](structsockaddr__can.md#ae9d8c789193e516c282a707d5a118ebc);

[ 63](structsockaddr__can.md#af1586f4d4c039a7941f07c0d746a73a7) int [can\_ifindex](structsockaddr__can.md#af1586f4d4c039a7941f07c0d746a73a7);

64};

65

74

[ 96](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e);

97

[ 101](structsocketcan__frame.md)struct [socketcan\_frame](structsocketcan__frame.md) {

[ 103](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6) [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) [can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6);

[ 105](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731);

[ 107](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d);

109 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) res0; /\* reserved/padding. \*/

110 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) res1; /\* reserved/padding. \*/

112

[ 114](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623)[[SOCKETCAN\_MAX\_DLEN](group__socket__can.md#ga3ec3e39a63684e78a52cf9160c82c257)];

115};

116

[ 122](structsocketcan__filter.md)struct [socketcan\_filter](structsocketcan__filter.md) {

[ 124](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47) [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) [can\_id](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47);

[ 126](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9) [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) [can\_mask](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9);

[ 128](structsocketcan__filter.md#a84abbc2f8a18bfe2d53cacf582f9fa10) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structsocketcan__filter.md#a84abbc2f8a18bfe2d53cacf582f9fa10);

129};

130

132

136

137#ifdef \_\_cplusplus

138}

139#endif

140

141#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKETCAN\_H\_ \*/

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e)

uint32\_t socketcan\_id\_t

CAN Identifier structure for Linux SocketCAN compatibility.

**Definition** socketcan.h:96

[SOCKETCAN\_MAX\_DLEN](group__socket__can.md#ga3ec3e39a63684e78a52cf9160c82c257)

#define SOCKETCAN\_MAX\_DLEN

**Definition** socketcan.h:48

[CAN\_RAW\_FILTER](group__socket__can.md#gga0878a39c728876bf39637e284a5b132ba1650b3e04298c36834ffa7dca117443a)

@ CAN\_RAW\_FILTER

**Definition** socketcan.h:39

[types.h](include_2zephyr_2types_8h.md)

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[sockaddr\_can](structsockaddr__can.md)

struct sockaddr\_can - The sockaddr structure for CAN sockets

**Definition** socketcan.h:61

[sockaddr\_can::can\_family](structsockaddr__can.md#ae9d8c789193e516c282a707d5a118ebc)

sa\_family\_t can\_family

**Definition** socketcan.h:62

[sockaddr\_can::can\_ifindex](structsockaddr__can.md#af1586f4d4c039a7941f07c0d746a73a7)

int can\_ifindex

**Definition** socketcan.h:63

[socketcan\_filter](structsocketcan__filter.md)

CAN filter for Linux SocketCAN compatibility.

**Definition** socketcan.h:122

[socketcan\_filter::can\_mask](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9)

socketcan\_id\_t can\_mask

The mask applied to can\_id for matching.

**Definition** socketcan.h:126

[socketcan\_filter::flags](structsocketcan__filter.md#a84abbc2f8a18bfe2d53cacf582f9fa10)

uint8\_t flags

Additional flags for FD frame filter.

**Definition** socketcan.h:128

[socketcan\_filter::can\_id](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47)

socketcan\_id\_t can\_id

The CAN identifier to match.

**Definition** socketcan.h:124

[socketcan\_frame](structsocketcan__frame.md)

CAN frame for Linux SocketCAN compatibility.

**Definition** socketcan.h:101

[socketcan\_frame::can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6)

socketcan\_id\_t can\_id

32-bit CAN ID + EFF/RTR/ERR flags.

**Definition** socketcan.h:103

[socketcan\_frame::data](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623)

uint8\_t data[8U]

The payload data.

**Definition** socketcan.h:114

[socketcan\_frame::len](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731)

uint8\_t len

Frame payload length in bytes.

**Definition** socketcan.h:105

[socketcan\_frame::flags](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d)

uint8\_t flags

Additional flags for CAN FD.

**Definition** socketcan.h:107

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socketcan.h](socketcan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
