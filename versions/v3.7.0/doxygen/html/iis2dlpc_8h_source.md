---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/iis2dlpc_8h_source.html
original_path: doxygen/html/iis2dlpc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iis2dlpc.h

[Go to the documentation of this file.](iis2dlpc_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_IIS2DLPC\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_IIS2DLPC\_H\_

8

9/\* power-modes \*/

[ 10](iis2dlpc_8h.md#a1e1c2a12612d55d0d1a60e6df5cc3050)#define IIS2DLPC\_DT\_LP\_M1 0

[ 11](iis2dlpc_8h.md#a52571a5d3d8e7a042a442f8d8b55029e)#define IIS2DLPC\_DT\_LP\_M2 1

[ 12](iis2dlpc_8h.md#ada77b7def23ffce8089c4773204a5ed0)#define IIS2DLPC\_DT\_LP\_M3 2

[ 13](iis2dlpc_8h.md#aa39b8641e427747eb81ab276b30447f9)#define IIS2DLPC\_DT\_LP\_M4 3

[ 14](iis2dlpc_8h.md#a623fd5c18feaac196c33265ea84aa0e8)#define IIS2DLPC\_DT\_HP\_MODE 4

15

16/\* Filter bandwidth \*/

[ 17](iis2dlpc_8h.md#abf53338af02c9036850d61f4942123fe)#define IIS2DLPC\_DT\_FILTER\_BW\_ODR\_DIV\_2 0

[ 18](iis2dlpc_8h.md#a24ba2864f9a1c76f73636ab40ce977cc)#define IIS2DLPC\_DT\_FILTER\_BW\_ODR\_DIV\_4 1

[ 19](iis2dlpc_8h.md#ae701e403e5b068c4188bf6ecebc5e088)#define IIS2DLPC\_DT\_FILTER\_BW\_ODR\_DIV\_10 2

[ 20](iis2dlpc_8h.md#ab453a45f6561c03f6c2657b025fb8280)#define IIS2DLPC\_DT\_FILTER\_BW\_ODR\_DIV\_20 3

21

22/\* Tap mode \*/

[ 23](iis2dlpc_8h.md#a52c4b179f307100adfbe341dcc8756b1)#define IIS2DLPC\_DT\_SINGLE\_TAP 0

[ 24](iis2dlpc_8h.md#ae49fca709c40c78ae3001454d2277761)#define IIS2DLPC\_DT\_SINGLE\_DOUBLE\_TAP 1

25

26/\* Free-Fall threshold \*/

[ 27](iis2dlpc_8h.md#a31b120d2c9f9271f6d6c0e6270d6869c)#define IIS2DLPC\_DT\_FF\_THRESHOLD\_156\_mg 0

[ 28](iis2dlpc_8h.md#aa03f24ea0546d41d75b7b27980ec4a03)#define IIS2DLPC\_DT\_FF\_THRESHOLD\_219\_mg 1

[ 29](iis2dlpc_8h.md#aa97f60a94b60643bf8fd53ba93a213b5)#define IIS2DLPC\_DT\_FF\_THRESHOLD\_250\_mg 2

[ 30](iis2dlpc_8h.md#a6958c72e3b6a4202c2e393802f44c045)#define IIS2DLPC\_DT\_FF\_THRESHOLD\_312\_mg 3

[ 31](iis2dlpc_8h.md#a368134487e769d5b6a9a8c43caf75fb4)#define IIS2DLPC\_DT\_FF\_THRESHOLD\_344\_mg 4

[ 32](iis2dlpc_8h.md#a189b31dc699c5c7698289502d1d4a2c2)#define IIS2DLPC\_DT\_FF\_THRESHOLD\_406\_mg 5

[ 33](iis2dlpc_8h.md#abb23c1eaaa0b82d566e3c6fb24b4bf75)#define IIS2DLPC\_DT\_FF\_THRESHOLD\_469\_mg 6

[ 34](iis2dlpc_8h.md#a84b6e0ed1a646f349e7e166e18ef3b5d)#define IIS2DLPC\_DT\_FF\_THRESHOLD\_500\_mg 7

35

36/\* wakeup duration \*/

[ 37](iis2dlpc_8h.md#ad369d4265e7542856d5ccd052fcb3025)#define IIS2DLPC\_DT\_WAKEUP\_1\_ODR 0

[ 38](iis2dlpc_8h.md#ad7f6fb74463c30e726dc34ef9462993c)#define IIS2DLPC\_DT\_WAKEUP\_2\_ODR 1

[ 39](iis2dlpc_8h.md#ad3f89e84420074c53fc9e13a30f116a8)#define IIS2DLPC\_DT\_WAKEUP\_3\_ODR 2

[ 40](iis2dlpc_8h.md#a651cadb8f638381169876dbd5291714a)#define IIS2DLPC\_DT\_WAKEUP\_4\_ODR 3

41

42#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ST\_IIS2DLPC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [iis2dlpc.h](iis2dlpc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
