---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/socketcan_8h_source.html
original_path: doxygen/html/socketcan_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

32

[ 34](group__socket__can.md#ga57682d9a1e4f4d90943dbaa683582bf5)#define CAN\_RAW 1

35

37

38/\* SocketCAN options \*/

39#define SOL\_CAN\_BASE 100

40#define SOL\_CAN\_RAW (SOL\_CAN\_BASE + CAN\_RAW)

41

42enum {

43 CAN\_RAW\_FILTER = 1,

44};

45

47

48/\* SocketCAN MTU size compatible with Linux \*/

49#ifdef CONFIG\_CAN\_FD\_MODE

51#define SOCKETCAN\_MAX\_DLEN 64U

53#define CANFD\_MTU (sizeof(struct socketcan\_frame))

55#define CAN\_MTU (CANFD\_MTU - 56U)

56#else /\* CONFIG\_CAN\_FD\_MODE \*/

[ 58](group__socket__can.md#ga3ec3e39a63684e78a52cf9160c82c257)#define SOCKETCAN\_MAX\_DLEN 8U

[ 60](group__socket__can.md#ga7d1f583cdc56ead407496713f3f22ac8)#define CAN\_MTU (sizeof(struct socketcan\_frame))

61#endif /\* !CONFIG\_CAN\_FD\_MODE \*/

62

63/\* CAN FD specific flags from Linux Kernel (include/uapi/linux/can.h) \*/

[ 64](group__socket__can.md#gace1d124719f8eac5f59788811c4afaf4)#define CANFD\_BRS 0x01

[ 65](group__socket__can.md#gacfc1bf4466d32189a1708b4351df0794)#define CANFD\_ESI 0x02

[ 66](group__socket__can.md#ga409cae306f00226ef192320f4f01f51c)#define CANFD\_FDF 0x04

67

[ 72](structsockaddr__can.md)struct [sockaddr\_can](structsockaddr__can.md) {

[ 73](structsockaddr__can.md#ae9d8c789193e516c282a707d5a118ebc) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [can\_family](structsockaddr__can.md#ae9d8c789193e516c282a707d5a118ebc);

[ 74](structsockaddr__can.md#af1586f4d4c039a7941f07c0d746a73a7) int [can\_ifindex](structsockaddr__can.md#af1586f4d4c039a7941f07c0d746a73a7);

75};

76

85

[ 107](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e);

108

[ 112](structsocketcan__frame.md)struct [socketcan\_frame](structsocketcan__frame.md) {

[ 114](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6) [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) [can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6);

[ 116](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731);

[ 118](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d);

120 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) res0; /\* reserved/padding. \*/

121 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) res1; /\* reserved/padding. \*/

123

[ 125](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623)[[SOCKETCAN\_MAX\_DLEN](group__socket__can.md#ga3ec3e39a63684e78a52cf9160c82c257)];

126};

127

[ 133](structsocketcan__filter.md)struct [socketcan\_filter](structsocketcan__filter.md) {

[ 135](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47) [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) [can\_id](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47);

[ 137](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9) [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) [can\_mask](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9);

[ 139](structsocketcan__filter.md#a84abbc2f8a18bfe2d53cacf582f9fa10) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structsocketcan__filter.md#a84abbc2f8a18bfe2d53cacf582f9fa10);

140};

141

143

147

148#ifdef \_\_cplusplus

149}

150#endif

151

152#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKETCAN\_H\_ \*/

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:168

[socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e)

uint32\_t socketcan\_id\_t

CAN Identifier structure for Linux SocketCAN compatibility.

**Definition** socketcan.h:107

[SOCKETCAN\_MAX\_DLEN](group__socket__can.md#ga3ec3e39a63684e78a52cf9160c82c257)

#define SOCKETCAN\_MAX\_DLEN

SocketCAN max data length.

**Definition** socketcan.h:58

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

**Definition** socketcan.h:72

[sockaddr\_can::can\_family](structsockaddr__can.md#ae9d8c789193e516c282a707d5a118ebc)

sa\_family\_t can\_family

Address family.

**Definition** socketcan.h:73

[sockaddr\_can::can\_ifindex](structsockaddr__can.md#af1586f4d4c039a7941f07c0d746a73a7)

int can\_ifindex

SocketCAN network interface index.

**Definition** socketcan.h:74

[socketcan\_filter](structsocketcan__filter.md)

CAN filter for Linux SocketCAN compatibility.

**Definition** socketcan.h:133

[socketcan\_filter::can\_mask](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9)

socketcan\_id\_t can\_mask

The mask applied to can\_id for matching.

**Definition** socketcan.h:137

[socketcan\_filter::flags](structsocketcan__filter.md#a84abbc2f8a18bfe2d53cacf582f9fa10)

uint8\_t flags

Additional flags for FD frame filter.

**Definition** socketcan.h:139

[socketcan\_filter::can\_id](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47)

socketcan\_id\_t can\_id

The CAN identifier to match.

**Definition** socketcan.h:135

[socketcan\_frame](structsocketcan__frame.md)

CAN frame for Linux SocketCAN compatibility.

**Definition** socketcan.h:112

[socketcan\_frame::can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6)

socketcan\_id\_t can\_id

32-bit CAN ID + EFF/RTR/ERR flags.

**Definition** socketcan.h:114

[socketcan\_frame::data](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623)

uint8\_t data[8U]

The payload data.

**Definition** socketcan.h:125

[socketcan\_frame::len](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731)

uint8\_t len

Frame payload length in bytes.

**Definition** socketcan.h:116

[socketcan\_frame::flags](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d)

uint8\_t flags

Additional flags for CAN FD.

**Definition** socketcan.h:118

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socketcan.h](socketcan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
