---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/tftp_8h_source.html
original_path: doxygen/html/tftp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tftp.h

[Go to the documentation of this file.](tftp_8h.md)

1/\*

2 \* Copyright (c) 2020 InnBlue

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_NET\_TFTP\_H\_

17#define ZEPHYR\_INCLUDE\_NET\_TFTP\_H\_

18

19#include <[zephyr/kernel.h](kernel_8h.md)>

20#include <[zephyr/net/socket.h](net_2socket_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 32](group__tftp__client.md#ga762c61f0d58a300c91f7577f65574dd5)#define TFTP\_BLOCK\_SIZE 512

33

[ 38](group__tftp__client.md#ga0dbc6adc4cb9be4ea86fce61846c2089)#define TFTP\_HEADER\_SIZE 4

39

[ 41](group__tftp__client.md#ga4387f92c6327823d655d8aa4f1c65beb)#define TFTPC\_MAX\_BUF\_SIZE (TFTP\_BLOCK\_SIZE + TFTP\_HEADER\_SIZE)

42

[ 47](group__tftp__client.md#ga40d1c46aafbf6ea66daa5937ceb1152f)#define TFTPC\_SUCCESS 0

[ 48](group__tftp__client.md#gac8b5e1f02de73c8cd42849ea0229eed2)#define TFTPC\_DUPLICATE\_DATA -1

[ 49](group__tftp__client.md#ga5ac8121d18b8eceffe281281aca1b700)#define TFTPC\_BUFFER\_OVERFLOW -2

[ 50](group__tftp__client.md#ga30ad373e8531ba675165bb61620c9a07)#define TFTPC\_UNKNOWN\_FAILURE -3

[ 51](group__tftp__client.md#ga75729dcb0b640a6fcb2079151cd74f51)#define TFTPC\_REMOTE\_ERROR -4

[ 52](group__tftp__client.md#ga514eaf5d77587b8719801157adf20566)#define TFTPC\_RETRIES\_EXHAUSTED -5

56

[ 61](group__tftp__client.md#ga1ee3d814c6fbaf5570eb5fd9605af7ea)enum [tftp\_evt\_type](group__tftp__client.md#ga1ee3d814c6fbaf5570eb5fd9605af7ea) {

[ 67](group__tftp__client.md#gga1ee3d814c6fbaf5570eb5fd9605af7eaa7bd0226d62c9b49a8381705bc1d5875d) [TFTP\_EVT\_DATA](group__tftp__client.md#gga1ee3d814c6fbaf5570eb5fd9605af7eaa7bd0226d62c9b49a8381705bc1d5875d),

68

[ 74](group__tftp__client.md#gga1ee3d814c6fbaf5570eb5fd9605af7eaa317d58f986f6f2f65b44fdaa5b655eb3) [TFTP\_EVT\_ERROR](group__tftp__client.md#gga1ee3d814c6fbaf5570eb5fd9605af7eaa317d58f986f6f2f65b44fdaa5b655eb3)

75};

76

[ 78](structtftp__data__param.md)struct [tftp\_data\_param](structtftp__data__param.md) {

[ 79](structtftp__data__param.md#a93f666944e8f20bd3a0e1320452913db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data\_ptr](structtftp__data__param.md#a93f666944e8f20bd3a0e1320452913db);

[ 80](structtftp__data__param.md#a704c20ab3177a3d53df21fc9ef64d084) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structtftp__data__param.md#a704c20ab3177a3d53df21fc9ef64d084);

81};

82

[ 84](structtftp__error__param.md)struct [tftp\_error\_param](structtftp__error__param.md) {

[ 85](structtftp__error__param.md#a725f1d2b8b8848febacf4888a0b55611) char \*[msg](structtftp__error__param.md#a725f1d2b8b8848febacf4888a0b55611);

[ 86](structtftp__error__param.md#aa8766ec6c9e92c9383b0dbbafe8a0f43) int [code](structtftp__error__param.md#aa8766ec6c9e92c9383b0dbbafe8a0f43);

87};

88

[ 93](uniontftp__evt__param.md)union [tftp\_evt\_param](uniontftp__evt__param.md) {

[ 95](uniontftp__evt__param.md#a7bec7cd5512f25699fe6b733458e9128) struct [tftp\_data\_param](structtftp__data__param.md) [data](uniontftp__evt__param.md#a7bec7cd5512f25699fe6b733458e9128);

96

[ 98](uniontftp__evt__param.md#a489485b84fa3e559b3065258cabfb205) struct [tftp\_error\_param](structtftp__error__param.md) [error](uniontftp__evt__param.md#a489485b84fa3e559b3065258cabfb205);

99};

100

[ 102](structtftp__evt.md)struct [tftp\_evt](structtftp__evt.md) {

[ 104](structtftp__evt.md#a2d622d9eb3ee0547b47a1330ad9cc412) enum [tftp\_evt\_type](group__tftp__client.md#ga1ee3d814c6fbaf5570eb5fd9605af7ea) [type](structtftp__evt.md#a2d622d9eb3ee0547b47a1330ad9cc412);

105

[ 107](structtftp__evt.md#a37154f19c66ae09a200f4d8d6c2941ca) union [tftp\_evt\_param](uniontftp__evt__param.md) [param](structtftp__evt.md#a37154f19c66ae09a200f4d8d6c2941ca);

108};

109

[ 118](group__tftp__client.md#gafc2d0fd730046b0d3781362263e68ddc)typedef void (\*[tftp\_callback\_t](group__tftp__client.md#gafc2d0fd730046b0d3781362263e68ddc))(const struct [tftp\_evt](structtftp__evt.md) \*evt);

119

[ 127](structtftpc.md)struct [tftpc](structtftpc.md) {

[ 129](structtftpc.md#a8ff9317a6bbdfac895cb1e408ae72cd9) struct [sockaddr](structsockaddr.md) [server](structtftpc.md#a8ff9317a6bbdfac895cb1e408ae72cd9);

130

[ 132](structtftpc.md#a39a04978a6cf3826ef19993989400b60) [tftp\_callback\_t](group__tftp__client.md#gafc2d0fd730046b0d3781362263e68ddc) [callback](structtftpc.md#a39a04978a6cf3826ef19993989400b60);

133

[ 135](structtftpc.md#a23f6f3d19493edbdc050df6d75441f92) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tftp\_buf](structtftpc.md#a23f6f3d19493edbdc050df6d75441f92)[[TFTPC\_MAX\_BUF\_SIZE](group__tftp__client.md#ga4387f92c6327823d655d8aa4f1c65beb)];

136};

137

[ 154](group__tftp__client.md#ga067de19b4089fbd2c2e49e925b73cfb0)int [tftp\_get](group__tftp__client.md#ga067de19b4089fbd2c2e49e925b73cfb0)(struct [tftpc](structtftpc.md) \*client,

155 const char \*remote\_file, const char \*mode);

156

[ 174](group__tftp__client.md#ga692f6a51f2ecd5c3d673ff64f59294b9)int [tftp\_put](group__tftp__client.md#ga692f6a51f2ecd5c3d673ff64f59294b9)(struct [tftpc](structtftpc.md) \*client,

175 const char \*remote\_file, const char \*mode,

176 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*user\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) user\_buf\_size);

177

178#ifdef \_\_cplusplus

179}

180#endif

181

182#endif /\* ZEPHYR\_INCLUDE\_NET\_TFTP\_H\_ \*/

183

[tftp\_get](group__tftp__client.md#ga067de19b4089fbd2c2e49e925b73cfb0)

int tftp\_get(struct tftpc \*client, const char \*remote\_file, const char \*mode)

This function gets data from a "file" on the remote server.

[tftp\_evt\_type](group__tftp__client.md#ga1ee3d814c6fbaf5570eb5fd9605af7ea)

tftp\_evt\_type

TFTP Asynchronous Events notified to the application from the module through the callback registered ...

**Definition** tftp.h:61

[TFTPC\_MAX\_BUF\_SIZE](group__tftp__client.md#ga4387f92c6327823d655d8aa4f1c65beb)

#define TFTPC\_MAX\_BUF\_SIZE

Maximum amount of data that can be sent or received.

**Definition** tftp.h:41

[tftp\_put](group__tftp__client.md#ga692f6a51f2ecd5c3d673ff64f59294b9)

int tftp\_put(struct tftpc \*client, const char \*remote\_file, const char \*mode, const uint8\_t \*user\_buf, uint32\_t user\_buf\_size)

This function puts data to a "file" on the remote server.

[tftp\_callback\_t](group__tftp__client.md#gafc2d0fd730046b0d3781362263e68ddc)

void(\* tftp\_callback\_t)(const struct tftp\_evt \*evt)

TFTP event notification callback registered by the application.

**Definition** tftp.h:118

[TFTP\_EVT\_ERROR](group__tftp__client.md#gga1ee3d814c6fbaf5570eb5fd9605af7eaa317d58f986f6f2f65b44fdaa5b655eb3)

@ TFTP\_EVT\_ERROR

ERROR event when error is received from remote server.

**Definition** tftp.h:74

[TFTP\_EVT\_DATA](group__tftp__client.md#gga1ee3d814c6fbaf5570eb5fd9605af7eaa7bd0226d62c9b49a8381705bc1d5875d)

@ TFTP\_EVT\_DATA

DATA event when data is received from remote server.

**Definition** tftp.h:67

[kernel.h](kernel_8h.md)

Public kernel APIs.

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

[tftp\_data\_param](structtftp__data__param.md)

Parameters for data event.

**Definition** tftp.h:78

[tftp\_data\_param::len](structtftp__data__param.md#a704c20ab3177a3d53df21fc9ef64d084)

uint32\_t len

Length of binary data.

**Definition** tftp.h:80

[tftp\_data\_param::data\_ptr](structtftp__data__param.md#a93f666944e8f20bd3a0e1320452913db)

uint8\_t \* data\_ptr

Pointer to binary data.

**Definition** tftp.h:79

[tftp\_error\_param](structtftp__error__param.md)

Parameters for error event.

**Definition** tftp.h:84

[tftp\_error\_param::msg](structtftp__error__param.md#a725f1d2b8b8848febacf4888a0b55611)

char \* msg

Error message.

**Definition** tftp.h:85

[tftp\_error\_param::code](structtftp__error__param.md#aa8766ec6c9e92c9383b0dbbafe8a0f43)

int code

Error code.

**Definition** tftp.h:86

[tftp\_evt](structtftp__evt.md)

Defines TFTP asynchronous event notified to the application.

**Definition** tftp.h:102

[tftp\_evt::type](structtftp__evt.md#a2d622d9eb3ee0547b47a1330ad9cc412)

enum tftp\_evt\_type type

Identifies the event.

**Definition** tftp.h:104

[tftp\_evt::param](structtftp__evt.md#a37154f19c66ae09a200f4d8d6c2941ca)

union tftp\_evt\_param param

Contains parameters (if any) accompanying the event.

**Definition** tftp.h:107

[tftpc](structtftpc.md)

TFTP client definition to maintain information relevant to the client.

**Definition** tftp.h:127

[tftpc::tftp\_buf](structtftpc.md#a23f6f3d19493edbdc050df6d75441f92)

uint8\_t tftp\_buf[(512+4)]

Buffer for internal usage.

**Definition** tftp.h:135

[tftpc::callback](structtftpc.md#a39a04978a6cf3826ef19993989400b60)

tftp\_callback\_t callback

Event notification callback.

**Definition** tftp.h:132

[tftpc::server](structtftpc.md#a8ff9317a6bbdfac895cb1e408ae72cd9)

struct sockaddr server

Socket address pointing to the remote TFTP server.

**Definition** tftp.h:129

[tftp\_evt\_param](uniontftp__evt__param.md)

Defines event parameters notified along with asynchronous events to the application.

**Definition** tftp.h:93

[tftp\_evt\_param::error](uniontftp__evt__param.md#a489485b84fa3e559b3065258cabfb205)

struct tftp\_error\_param error

Parameters accompanying TFTP\_EVT\_ERROR event.

**Definition** tftp.h:98

[tftp\_evt\_param::data](uniontftp__evt__param.md#a7bec7cd5512f25699fe6b733458e9128)

struct tftp\_data\_param data

Parameters accompanying TFTP\_EVT\_DATA event.

**Definition** tftp.h:95

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [tftp.h](tftp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
