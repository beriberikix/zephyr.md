---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mpsc__packet_8h_source.html
original_path: doxygen/html/mpsc__packet_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc\_packet.h

[Go to the documentation of this file.](mpsc__packet_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_SYS\_MPSC\_PACKET\_H\_

7#define ZEPHYR\_INCLUDE\_SYS\_MPSC\_PACKET\_H\_

8

9#include <[string.h](string_8h.md)>

10#include <[stdint.h](stdint_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 25](group__mpsc__packet.md#gadb02a97032e41897ae6644a23d163849)#define MPSC\_PBUF\_HDR\_BITS 2

26

[ 32](group__mpsc__packet.md#ga643932633f40ecdcfb9120662221d828)#define MPSC\_PBUF\_HDR \

33 uint32\_t valid: 1; \

34 uint32\_t busy: 1

35

[ 37](structmpsc__pbuf__hdr.md)struct [mpsc\_pbuf\_hdr](structmpsc__pbuf__hdr.md) {

[ 38](structmpsc__pbuf__hdr.md#a83666ac11d7c4271186b67966c3729b4) [MPSC\_PBUF\_HDR](group__mpsc__packet.md#ga643932633f40ecdcfb9120662221d828);

[ 39](structmpsc__pbuf__hdr.md#a7a19c1ed5035b095160e946fd989e1c6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data](structmpsc__pbuf__hdr.md#a7a19c1ed5035b095160e946fd989e1c6): 32 - [MPSC\_PBUF\_HDR\_BITS](group__mpsc__packet.md#gadb02a97032e41897ae6644a23d163849);

40};

41

[ 43](structmpsc__pbuf__skip.md)struct [mpsc\_pbuf\_skip](structmpsc__pbuf__skip.md) {

[ 44](structmpsc__pbuf__skip.md#a71106c8d9ec492ef788973996c9cba15) [MPSC\_PBUF\_HDR](group__mpsc__packet.md#ga643932633f40ecdcfb9120662221d828);

[ 45](structmpsc__pbuf__skip.md#af28d9ee25b93377519f625edd14d4078) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structmpsc__pbuf__skip.md#af28d9ee25b93377519f625edd14d4078): 32 - [MPSC\_PBUF\_HDR\_BITS](group__mpsc__packet.md#gadb02a97032e41897ae6644a23d163849);

46};

47

[ 49](unionmpsc__pbuf__generic.md)union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) {

[ 50](unionmpsc__pbuf__generic.md#af06ded46d485a33c73d12c4a32205554) struct [mpsc\_pbuf\_hdr](structmpsc__pbuf__hdr.md) [hdr](unionmpsc__pbuf__generic.md#af06ded46d485a33c73d12c4a32205554);

[ 51](unionmpsc__pbuf__generic.md#a52bbb3c2d0de9dc08680e7f901a43689) struct [mpsc\_pbuf\_skip](structmpsc__pbuf__skip.md) [skip](unionmpsc__pbuf__generic.md#a52bbb3c2d0de9dc08680e7f901a43689);

[ 52](unionmpsc__pbuf__generic.md#ac3d909bd2d28794c4db2d75ffbb7ec04) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw](unionmpsc__pbuf__generic.md#ac3d909bd2d28794c4db2d75ffbb7ec04);

53};

54

58

59#ifdef \_\_cplusplus

60}

61#endif

62

63#endif /\* ZEPHYR\_INCLUDE\_SYS\_MPSC\_PACKET\_H\_ \*/

[MPSC\_PBUF\_HDR](group__mpsc__packet.md#ga643932633f40ecdcfb9120662221d828)

#define MPSC\_PBUF\_HDR

Header that must be added to the first word in each packet.

**Definition** mpsc\_packet.h:32

[MPSC\_PBUF\_HDR\_BITS](group__mpsc__packet.md#gadb02a97032e41897ae6644a23d163849)

#define MPSC\_PBUF\_HDR\_BITS

Number of bits in the first word which are used by the buffer.

**Definition** mpsc\_packet.h:25

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[string.h](string_8h.md)

[mpsc\_pbuf\_hdr](structmpsc__pbuf__hdr.md)

Generic packet header.

**Definition** mpsc\_packet.h:37

[mpsc\_pbuf\_hdr::data](structmpsc__pbuf__hdr.md#a7a19c1ed5035b095160e946fd989e1c6)

uint32\_t data

**Definition** mpsc\_packet.h:39

[mpsc\_pbuf\_skip](structmpsc__pbuf__skip.md)

Skip packet used internally by the packet buffer.

**Definition** mpsc\_packet.h:43

[mpsc\_pbuf\_skip::len](structmpsc__pbuf__skip.md#af28d9ee25b93377519f625edd14d4078)

uint32\_t len

**Definition** mpsc\_packet.h:45

[mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md)

Generic packet header.

**Definition** mpsc\_packet.h:49

[mpsc\_pbuf\_generic::skip](unionmpsc__pbuf__generic.md#a52bbb3c2d0de9dc08680e7f901a43689)

struct mpsc\_pbuf\_skip skip

**Definition** mpsc\_packet.h:51

[mpsc\_pbuf\_generic::raw](unionmpsc__pbuf__generic.md#ac3d909bd2d28794c4db2d75ffbb7ec04)

uint32\_t raw

**Definition** mpsc\_packet.h:52

[mpsc\_pbuf\_generic::hdr](unionmpsc__pbuf__generic.md#af06ded46d485a33c73d12c4a32205554)

struct mpsc\_pbuf\_hdr hdr

**Definition** mpsc\_packet.h:50

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mpsc\_packet.h](mpsc__packet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
