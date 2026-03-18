---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/socket__net__mgmt_8h_source.html
original_path: doxygen/html/socket__net__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_net\_mgmt.h

[Go to the documentation of this file.](socket__net__mgmt_8h.md)

1

6

7/\*

8 \* Copyright (c) 2019 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_NET\_MGMT\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_NET\_MGMT\_H\_

15

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

18#include <[zephyr/net/net\_if.h](net__if_8h.md)>

19#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

31

32/\* Protocols of the protocol family PF\_NET\_MGMT \*/

[ 33](group__socket__net__mgmt.md#gab2d2105917cbbeaed6c31b0c763da855)#define NET\_MGMT\_EVENT\_PROTO 0x01

34

35/\* Socket NET\_MGMT options \*/

[ 36](group__socket__net__mgmt.md#ga89dc8c08d137eab552835fdba3d32cb7)#define SOL\_NET\_MGMT\_BASE 100

[ 37](group__socket__net__mgmt.md#gadf2e70bb146e100d4546ab281f67741f)#define SOL\_NET\_MGMT\_RAW (SOL\_NET\_MGMT\_BASE + 1)

38

[ 57](structsockaddr__nm.md)struct [sockaddr\_nm](structsockaddr__nm.md) {

[ 59](structsockaddr__nm.md#af6d556718e643c9083c790e1e797eedf) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [nm\_family](structsockaddr__nm.md#af6d556718e643c9083c790e1e797eedf);

60

[ 62](structsockaddr__nm.md#a79727f415488b6e548c48a556692a330) int [nm\_ifindex](structsockaddr__nm.md#a79727f415488b6e548c48a556692a330);

63

[ 67](structsockaddr__nm.md#ad3299cf4df378026cc40ee10f5abcba1) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [nm\_pid](structsockaddr__nm.md#ad3299cf4df378026cc40ee10f5abcba1);

68

[ 70](structsockaddr__nm.md#ac46ee5b5a9b3a04a53a8ae6e0f640a83) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nm\_mask](structsockaddr__nm.md#ac46ee5b5a9b3a04a53a8ae6e0f640a83);

71};

72

73

[ 77](structnet__mgmt__msghdr.md)struct [net\_mgmt\_msghdr](structnet__mgmt__msghdr.md) {

[ 79](structnet__mgmt__msghdr.md#a6867379b1ab13c504ee9884cc386c05e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nm\_msg\_version](structnet__mgmt__msghdr.md#a6867379b1ab13c504ee9884cc386c05e);

80

[ 82](structnet__mgmt__msghdr.md#ad7f4caefa6b3d8d93a480cd8210d7a4d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nm\_msg\_len](structnet__mgmt__msghdr.md#ad7f4caefa6b3d8d93a480cd8210d7a4d);

83

[ 85](structnet__mgmt__msghdr.md#a09e1bc6f985b8fcc3397aa447b1d8e94) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nm\_msg](structnet__mgmt__msghdr.md#a09e1bc6f985b8fcc3397aa447b1d8e94)[];

86};

87

[ 97](group__socket__net__mgmt.md#ga8ae9629a7869b3214f8b2f72aef545ee)#define NET\_MGMT\_SOCKET\_VERSION\_1 0x0001

98

102

103#ifdef \_\_cplusplus

104}

105#endif

106

107#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_NET\_MGMT\_H\_ \*/

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[types.h](include_2zephyr_2types_8h.md)

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[net\_mgmt\_msghdr](structnet__mgmt__msghdr.md)

Each network management message is prefixed with this header.

**Definition** socket\_net\_mgmt.h:77

[net\_mgmt\_msghdr::nm\_msg](structnet__mgmt__msghdr.md#a09e1bc6f985b8fcc3397aa447b1d8e94)

uint8\_t nm\_msg[]

The actual message data follows.

**Definition** socket\_net\_mgmt.h:85

[net\_mgmt\_msghdr::nm\_msg\_version](structnet__mgmt__msghdr.md#a6867379b1ab13c504ee9884cc386c05e)

uint32\_t nm\_msg\_version

Network management version.

**Definition** socket\_net\_mgmt.h:79

[net\_mgmt\_msghdr::nm\_msg\_len](structnet__mgmt__msghdr.md#ad7f4caefa6b3d8d93a480cd8210d7a4d)

uint32\_t nm\_msg\_len

Length of the data.

**Definition** socket\_net\_mgmt.h:82

[sockaddr\_nm](structsockaddr__nm.md)

struct sockaddr\_nm - The sockaddr structure for NET\_MGMT sockets

**Definition** socket\_net\_mgmt.h:57

[sockaddr\_nm::nm\_ifindex](structsockaddr__nm.md#a79727f415488b6e548c48a556692a330)

int nm\_ifindex

Network interface related to this address.

**Definition** socket\_net\_mgmt.h:62

[sockaddr\_nm::nm\_mask](structsockaddr__nm.md#ac46ee5b5a9b3a04a53a8ae6e0f640a83)

uint32\_t nm\_mask

net\_mgmt mask

**Definition** socket\_net\_mgmt.h:70

[sockaddr\_nm::nm\_pid](structsockaddr__nm.md#ad3299cf4df378026cc40ee10f5abcba1)

uintptr\_t nm\_pid

Thread id or similar that is used to separate the different sockets.

**Definition** socket\_net\_mgmt.h:67

[sockaddr\_nm::nm\_family](structsockaddr__nm.md#af6d556718e643c9083c790e1e797eedf)

sa\_family\_t nm\_family

AF\_NET\_MGMT address family.

**Definition** socket\_net\_mgmt.h:59

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_net\_mgmt.h](socket__net__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
