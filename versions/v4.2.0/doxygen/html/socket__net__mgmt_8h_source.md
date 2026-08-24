---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/socket__net__mgmt_8h_source.html
original_path: doxygen/html/socket__net__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

33

35

36/\* Protocols of the protocol family PF\_NET\_MGMT \*/

37#define NET\_MGMT\_EVENT\_PROTO 0x01

38

39/\* Socket NET\_MGMT options \*/

40#define SOL\_NET\_MGMT\_BASE 100

41#define SOL\_NET\_MGMT\_RAW (SOL\_NET\_MGMT\_BASE + 1)

42

44

49

[ 51](group__socket__net__mgmt.md#ga3d81f8a1f284a6ab2ac0a0a42a5dc793)#define SO\_NET\_MGMT\_ETHERNET\_SET\_QAV\_PARAM 1

52

[ 54](group__socket__net__mgmt.md#ga6cf79af1501bdcce6e559f7636c1a2d3)#define SO\_NET\_MGMT\_ETHERNET\_GET\_QAV\_PARAM 2

55 /\* for @name \*/

57

[ 76](structsockaddr__nm.md)struct [sockaddr\_nm](structsockaddr__nm.md) {

[ 78](structsockaddr__nm.md#af6d556718e643c9083c790e1e797eedf) [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [nm\_family](structsockaddr__nm.md#af6d556718e643c9083c790e1e797eedf);

79

[ 81](structsockaddr__nm.md#a79727f415488b6e548c48a556692a330) int [nm\_ifindex](structsockaddr__nm.md#a79727f415488b6e548c48a556692a330);

82

[ 86](structsockaddr__nm.md#ad3299cf4df378026cc40ee10f5abcba1) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [nm\_pid](structsockaddr__nm.md#ad3299cf4df378026cc40ee10f5abcba1);

87

[ 89](structsockaddr__nm.md#a90207ab0ca1b7ed30e97156b83671598) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [nm\_mask](structsockaddr__nm.md#a90207ab0ca1b7ed30e97156b83671598);

90};

91

92

[ 96](structnet__mgmt__msghdr.md)struct [net\_mgmt\_msghdr](structnet__mgmt__msghdr.md) {

[ 98](structnet__mgmt__msghdr.md#a6867379b1ab13c504ee9884cc386c05e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nm\_msg\_version](structnet__mgmt__msghdr.md#a6867379b1ab13c504ee9884cc386c05e);

99

[ 101](structnet__mgmt__msghdr.md#ad7f4caefa6b3d8d93a480cd8210d7a4d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nm\_msg\_len](structnet__mgmt__msghdr.md#ad7f4caefa6b3d8d93a480cd8210d7a4d);

102

[ 104](structnet__mgmt__msghdr.md#a09e1bc6f985b8fcc3397aa447b1d8e94) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nm\_msg](structnet__mgmt__msghdr.md#a09e1bc6f985b8fcc3397aa447b1d8e94)[];

105};

106

[ 116](group__socket__net__mgmt.md#ga8ae9629a7869b3214f8b2f72aef545ee)#define NET\_MGMT\_SOCKET\_VERSION\_1 0x0001

117

121

122#ifdef \_\_cplusplus

123}

124#endif

125

126#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_NET\_MGMT\_H\_ \*/

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:168

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

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[net\_mgmt\_msghdr](structnet__mgmt__msghdr.md)

Each network management message is prefixed with this header.

**Definition** socket\_net\_mgmt.h:96

[net\_mgmt\_msghdr::nm\_msg](structnet__mgmt__msghdr.md#a09e1bc6f985b8fcc3397aa447b1d8e94)

uint8\_t nm\_msg[]

The actual message data follows.

**Definition** socket\_net\_mgmt.h:104

[net\_mgmt\_msghdr::nm\_msg\_version](structnet__mgmt__msghdr.md#a6867379b1ab13c504ee9884cc386c05e)

uint32\_t nm\_msg\_version

Network management version.

**Definition** socket\_net\_mgmt.h:98

[net\_mgmt\_msghdr::nm\_msg\_len](structnet__mgmt__msghdr.md#ad7f4caefa6b3d8d93a480cd8210d7a4d)

uint32\_t nm\_msg\_len

Length of the data.

**Definition** socket\_net\_mgmt.h:101

[sockaddr\_nm](structsockaddr__nm.md)

struct sockaddr\_nm - The sockaddr structure for NET\_MGMT sockets

**Definition** socket\_net\_mgmt.h:76

[sockaddr\_nm::nm\_ifindex](structsockaddr__nm.md#a79727f415488b6e548c48a556692a330)

int nm\_ifindex

Network interface related to this address.

**Definition** socket\_net\_mgmt.h:81

[sockaddr\_nm::nm\_mask](structsockaddr__nm.md#a90207ab0ca1b7ed30e97156b83671598)

uint64\_t nm\_mask

net\_mgmt mask

**Definition** socket\_net\_mgmt.h:89

[sockaddr\_nm::nm\_pid](structsockaddr__nm.md#ad3299cf4df378026cc40ee10f5abcba1)

uintptr\_t nm\_pid

Thread id or similar that is used to separate the different sockets.

**Definition** socket\_net\_mgmt.h:86

[sockaddr\_nm::nm\_family](structsockaddr__nm.md#af6d556718e643c9083c790e1e797eedf)

sa\_family\_t nm\_family

AF\_NET\_MGMT address family.

**Definition** socket\_net\_mgmt.h:78

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_net\_mgmt.h](socket__net__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
