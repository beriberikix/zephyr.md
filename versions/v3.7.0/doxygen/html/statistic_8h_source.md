---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/statistic_8h_source.html
original_path: doxygen/html/statistic_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

statistic.h

[Go to the documentation of this file.](statistic_8h.md)

1

4

5/\*

6 \* Copyright (c) 2023 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_STATISTIC\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_STATISTIC\_H\_

13

14#include <[stdint.h](stdint_8h.md)>

15

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 28](structbt__mesh__statistic.md)struct [bt\_mesh\_statistic](structbt__mesh__statistic.md) {

[ 31](structbt__mesh__statistic.md#a5c8d77c2d32964f0a54420aafff9a4e1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_adv](structbt__mesh__statistic.md#a5c8d77c2d32964f0a54420aafff9a4e1);

[ 33](structbt__mesh__statistic.md#a448c73e05fd8055baaa64532275d9c69) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_loopback](structbt__mesh__statistic.md#a448c73e05fd8055baaa64532275d9c69);

[ 35](structbt__mesh__statistic.md#aa86617d0c3cfa7e2ed7e10e4c3ac8b5c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_proxy](structbt__mesh__statistic.md#aa86617d0c3cfa7e2ed7e10e4c3ac8b5c);

[ 37](structbt__mesh__statistic.md#af7c764c6b702957180d8b74193207a0e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_uknown](structbt__mesh__statistic.md#af7c764c6b702957180d8b74193207a0e);

[ 39](structbt__mesh__statistic.md#a1979c5798d7d015bf4cf0c30716d3e4f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_adv\_relay\_planned](structbt__mesh__statistic.md#a1979c5798d7d015bf4cf0c30716d3e4f);

[ 41](structbt__mesh__statistic.md#a139484340d2bd3fae763b23e91648e0e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_adv\_relay\_succeeded](structbt__mesh__statistic.md#a139484340d2bd3fae763b23e91648e0e);

[ 43](structbt__mesh__statistic.md#a2c47d080eac1050422d36402a9771fa6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_local\_planned](structbt__mesh__statistic.md#a2c47d080eac1050422d36402a9771fa6);

[ 45](structbt__mesh__statistic.md#a9da26f6d5ad7b91b69b95e4d4a70bf71) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_local\_succeeded](structbt__mesh__statistic.md#a9da26f6d5ad7b91b69b95e4d4a70bf71);

[ 47](structbt__mesh__statistic.md#a0f60214d1f2480bc0025415064dd79e8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_friend\_planned](structbt__mesh__statistic.md#a0f60214d1f2480bc0025415064dd79e8);

[ 49](structbt__mesh__statistic.md#aa4d83bb57f86723899bc2fe25342423d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_friend\_succeeded](structbt__mesh__statistic.md#aa4d83bb57f86723899bc2fe25342423d);

50};

51

[ 56](group__bt__mesh__stat.md#ga8c1e9de2f323111ee95d0903b5ecb2fd)void [bt\_mesh\_stat\_get](group__bt__mesh__stat.md#ga8c1e9de2f323111ee95d0903b5ecb2fd)(struct [bt\_mesh\_statistic](structbt__mesh__statistic.md) \*st);

57

[ 60](group__bt__mesh__stat.md#gabe8c893466f24e9b75fe51ae5ea65132)void [bt\_mesh\_stat\_reset](group__bt__mesh__stat.md#gabe8c893466f24e9b75fe51ae5ea65132)(void);

61

62#ifdef \_\_cplusplus

63}

64#endif

68

69#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_STATISTIC\_H\_ \*/

[bt\_mesh\_stat\_get](group__bt__mesh__stat.md#ga8c1e9de2f323111ee95d0903b5ecb2fd)

void bt\_mesh\_stat\_get(struct bt\_mesh\_statistic \*st)

Get mesh frame handling statistic.

[bt\_mesh\_stat\_reset](group__bt__mesh__stat.md#gabe8c893466f24e9b75fe51ae5ea65132)

void bt\_mesh\_stat\_reset(void)

Reset mesh frame handling statistic.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[bt\_mesh\_statistic](structbt__mesh__statistic.md)

The structure that keeps statistics of mesh frames handling.

**Definition** statistic.h:28

[bt\_mesh\_statistic::tx\_friend\_planned](structbt__mesh__statistic.md#a0f60214d1f2480bc0025415064dd79e8)

uint32\_t tx\_friend\_planned

Counter of frames that were initiated to send over friend bearer.

**Definition** statistic.h:47

[bt\_mesh\_statistic::tx\_adv\_relay\_succeeded](structbt__mesh__statistic.md#a139484340d2bd3fae763b23e91648e0e)

uint32\_t tx\_adv\_relay\_succeeded

Counter of frames that succeeded relaying over advertiser bearer.

**Definition** statistic.h:41

[bt\_mesh\_statistic::tx\_adv\_relay\_planned](structbt__mesh__statistic.md#a1979c5798d7d015bf4cf0c30716d3e4f)

uint32\_t tx\_adv\_relay\_planned

Counter of frames that were initiated to relay over advertiser bearer.

**Definition** statistic.h:39

[bt\_mesh\_statistic::tx\_local\_planned](structbt__mesh__statistic.md#a2c47d080eac1050422d36402a9771fa6)

uint32\_t tx\_local\_planned

Counter of frames that were initiated to send over advertiser bearer locally.

**Definition** statistic.h:43

[bt\_mesh\_statistic::rx\_loopback](structbt__mesh__statistic.md#a448c73e05fd8055baaa64532275d9c69)

uint32\_t rx\_loopback

Received frames over loopback.

**Definition** statistic.h:33

[bt\_mesh\_statistic::rx\_adv](structbt__mesh__statistic.md#a5c8d77c2d32964f0a54420aafff9a4e1)

uint32\_t rx\_adv

All received frames passed basic validation and decryption.

**Definition** statistic.h:31

[bt\_mesh\_statistic::tx\_local\_succeeded](structbt__mesh__statistic.md#a9da26f6d5ad7b91b69b95e4d4a70bf71)

uint32\_t tx\_local\_succeeded

Counter of frames that succeeded to send over advertiser bearer locally.

**Definition** statistic.h:45

[bt\_mesh\_statistic::tx\_friend\_succeeded](structbt__mesh__statistic.md#aa4d83bb57f86723899bc2fe25342423d)

uint32\_t tx\_friend\_succeeded

Counter of frames that succeeded to send over friend bearer.

**Definition** statistic.h:49

[bt\_mesh\_statistic::rx\_proxy](structbt__mesh__statistic.md#aa86617d0c3cfa7e2ed7e10e4c3ac8b5c)

uint32\_t rx\_proxy

Received frames over proxy.

**Definition** statistic.h:35

[bt\_mesh\_statistic::rx\_uknown](structbt__mesh__statistic.md#af7c764c6b702957180d8b74193207a0e)

uint32\_t rx\_uknown

Received over unknown interface.

**Definition** statistic.h:37

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [statistic.h](statistic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
