---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/serial_8h_source.html
original_path: doxygen/html/serial_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

serial.h

[Go to the documentation of this file.](serial_8h.md)

1/\*

2 \* Copyright Runtime.io 2018. All rights reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_MGMT\_SERIAL\_H\_

8#define ZEPHYR\_INCLUDE\_MGMT\_SERIAL\_H\_

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](serial_8h.md#a67c8df024da7e6ff3ceaa06fc0b9b168)#define MCUMGR\_SERIAL\_HDR\_PKT 0x0609

[ 17](serial_8h.md#a133a20780bbcd019b00c57d9e6da2884)#define MCUMGR\_SERIAL\_HDR\_FRAG 0x0414

[ 18](serial_8h.md#a33ba8e4d44edccce44101888d69eea18)#define MCUMGR\_SERIAL\_MAX\_FRAME 127

19

[ 20](serial_8h.md#aa54b69e1d1440f957e0a5f7946487871)#define MCUMGR\_SERIAL\_HDR\_PKT\_1 (MCUMGR\_SERIAL\_HDR\_PKT >> 8)

[ 21](serial_8h.md#a09386427eb67c2e07535b79eb8ca9fbc)#define MCUMGR\_SERIAL\_HDR\_PKT\_2 (MCUMGR\_SERIAL\_HDR\_PKT & 0xff)

[ 22](serial_8h.md#a1edd532f85b7037096b2033b70ea5985)#define MCUMGR\_SERIAL\_HDR\_FRAG\_1 (MCUMGR\_SERIAL\_HDR\_FRAG >> 8)

[ 23](serial_8h.md#a50ca5a231808ab473ea1d2fe89fd53f2)#define MCUMGR\_SERIAL\_HDR\_FRAG\_2 (MCUMGR\_SERIAL\_HDR\_FRAG & 0xff)

24

[ 28](structmcumgr__serial__rx__ctxt.md)struct [mcumgr\_serial\_rx\_ctxt](structmcumgr__serial__rx__ctxt.md) {

29 /\* Contains the partially- or fully-received mcumgr request. Data

30 \* stored in this buffer has already been base64-decoded.

31 \*/

[ 32](structmcumgr__serial__rx__ctxt.md#a5fdf2dd95185a49806c1900184c7bdfc) struct [net\_buf](structnet__buf.md) \*[nb](structmcumgr__serial__rx__ctxt.md#a5fdf2dd95185a49806c1900184c7bdfc);

33

34 /\* Length of full packet, as read from header. \*/

[ 35](structmcumgr__serial__rx__ctxt.md#a4ded2b7748334b0f3166f4c18cd1d6b0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pkt\_len](structmcumgr__serial__rx__ctxt.md#a4ded2b7748334b0f3166f4c18cd1d6b0);

36};

37

[ 46](serial_8h.md#a49006881d527ebba84948a913a83c17e)typedef int (\*[mcumgr\_serial\_tx\_cb](serial_8h.md#a49006881d527ebba84948a913a83c17e))(const void \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), int [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

47

[ 67](serial_8h.md#aa510a98df8b01ccf5bae8eacc9c59078)struct [net\_buf](structnet__buf.md) \*[mcumgr\_serial\_process\_frag](serial_8h.md#aa510a98df8b01ccf5bae8eacc9c59078)(

68 struct [mcumgr\_serial\_rx\_ctxt](structmcumgr__serial__rx__ctxt.md) \*rx\_ctxt,

69 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*frag, int frag\_len);

70

[ 80](serial_8h.md#aca191e14700f0c2da9643e7daa582867)int [mcumgr\_serial\_tx\_pkt](serial_8h.md#aca191e14700f0c2da9643e7daa582867)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), int [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38), [mcumgr\_serial\_tx\_cb](serial_8h.md#a49006881d527ebba84948a913a83c17e) cb);

81

82#ifdef \_\_cplusplus

83}

84#endif

85

86#endif

[types.h](include_2zephyr_2types_8h.md)

[mcumgr\_serial\_tx\_cb](serial_8h.md#a49006881d527ebba84948a913a83c17e)

int(\* mcumgr\_serial\_tx\_cb)(const void \*data, int len)

Transmits a chunk of raw response data.

**Definition** serial.h:46

[mcumgr\_serial\_process\_frag](serial_8h.md#aa510a98df8b01ccf5bae8eacc9c59078)

struct net\_buf \* mcumgr\_serial\_process\_frag(struct mcumgr\_serial\_rx\_ctxt \*rx\_ctxt, const uint8\_t \*frag, int frag\_len)

Processes an mcumgr request fragment received over a serial transport.

[mcumgr\_serial\_tx\_pkt](serial_8h.md#aca191e14700f0c2da9643e7daa582867)

int mcumgr\_serial\_tx\_pkt(const uint8\_t \*data, int len, mcumgr\_serial\_tx\_cb cb)

Encodes and transmits an mcumgr packet over serial.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[mcumgr\_serial\_rx\_ctxt](structmcumgr__serial__rx__ctxt.md)

Maintains state for an incoming mcumgr request packet.

**Definition** serial.h:28

[mcumgr\_serial\_rx\_ctxt::pkt\_len](structmcumgr__serial__rx__ctxt.md#a4ded2b7748334b0f3166f4c18cd1d6b0)

uint16\_t pkt\_len

**Definition** serial.h:35

[mcumgr\_serial\_rx\_ctxt::nb](structmcumgr__serial__rx__ctxt.md#a5fdf2dd95185a49806c1900184c7bdfc)

struct net\_buf \* nb

**Definition** serial.h:32

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** buf.h:936

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** buf.h:939

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [serial.h](serial_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
