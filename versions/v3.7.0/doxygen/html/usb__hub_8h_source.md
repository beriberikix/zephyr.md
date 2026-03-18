---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/usb__hub_8h_source.html
original_path: doxygen/html/usb__hub_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_hub.h

[Go to the documentation of this file.](usb__hub_8h.md)

1/\*

2 \* Copyright (c) 2022 Emerson Electric Co.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_USB\_CLASS\_USB\_HUB\_H\_

13#define ZEPHYR\_INCLUDE\_USB\_CLASS\_USB\_HUB\_H\_

14

[ 16](usb__hub_8h.md#a997b8615c74e9aa88f8e273b6a3a61fc)#define USB\_HCFS\_C\_HUB\_LOCAL\_POWER 0x00

[ 17](usb__hub_8h.md#a0b1a392fe6a9e5932158c1cdca43f4bf)#define USB\_HCFS\_C\_HUB\_OVER\_CURRENT 0x01

[ 18](usb__hub_8h.md#ad2d66d4f6f517ea0d3dd76da62742552)#define USB\_HCFS\_PORT\_CONNECTION 0x00

[ 19](usb__hub_8h.md#a5c8ba71161b59bae12afb5dde7728808)#define USB\_HCFS\_PORT\_ENABLE 0x01

[ 20](usb__hub_8h.md#a8cd0227e68d424b758e13f470d838868)#define USB\_HCFS\_PORT\_SUSPEND 0x02

[ 21](usb__hub_8h.md#ae1c71c8da58b67ed5f12f640827b9d77)#define USB\_HCFS\_PORT\_OVER\_CURRENT 0x03

[ 22](usb__hub_8h.md#ae4fd5c849765661c61b4212f0bfe495e)#define USB\_HCFS\_PORT\_RESET 0x04

[ 23](usb__hub_8h.md#a1fe915a2e5569480f4fc24e69f24228c)#define USB\_HCFS\_PORT\_POWER 0x08

[ 24](usb__hub_8h.md#ab3dc8ec69e15379c606e7e58980617ca)#define USB\_HCFS\_PORT\_LOW\_SPEED 0x09

[ 25](usb__hub_8h.md#a75e8cf42cfd77add9f306a20fe6bb14f)#define USB\_HCFS\_C\_PORT\_CONNECTION 0x10

[ 26](usb__hub_8h.md#a71f79a0dbf15b792ffd93305145de316)#define USB\_HCFS\_C\_PORT\_ENABLE 0x11

[ 27](usb__hub_8h.md#a84c40b25ec588b86131300a4dbc765bd)#define USB\_HCFS\_C\_PORT\_SUSPEND 0x12

[ 28](usb__hub_8h.md#aa3273e27d90c343899c4cb1f722c2878)#define USB\_HCFS\_C\_PORT\_OVER\_CURRENT 0x13

[ 29](usb__hub_8h.md#ad53ce209e4472d86b6643c7d391b7f24)#define USB\_HCFS\_C\_PORT\_RESET 0x14

[ 30](usb__hub_8h.md#a94a24ef58ab59d399a0dfa0f0903dfb0)#define USB\_HCFS\_PORT\_TEST 0x15

[ 31](usb__hub_8h.md#a2e049932c995b1fe489c38ed0cf09049)#define USB\_HCFS\_PORT\_INDICATOR 0x16

32

[ 34](usb__hub_8h.md#a91ad2acf2c5316d20738f4d65d68ee14)#define USB\_HCREQ\_GET\_STATUS 0x00

[ 35](usb__hub_8h.md#a3fc30c26205b41f2ca3abeef815917fa)#define USB\_HCREQ\_CLEAR\_FEATURE 0x01

[ 36](usb__hub_8h.md#a7b4f58864afb11d881929e81aa4843bd)#define USB\_HCREQ\_SET\_FEATURE 0x03

[ 37](usb__hub_8h.md#a5c13eb60a311c0bf7c1f5e9fa1f66f2b)#define USB\_HCREQ\_GET\_DESCRIPTOR 0x06

[ 38](usb__hub_8h.md#af632ce62b30de5103c799171d08b0f08)#define USB\_HCREQ\_SET\_DESCRIPTOR 0x07

[ 39](usb__hub_8h.md#a479c4d6fe6691d3cda5d4ba6f868cb2f)#define USB\_HCREQ\_CLEAR\_TT\_BUFFER 0x08

[ 40](usb__hub_8h.md#a09990d8d948aef82115489f60a83250b)#define USB\_HCREQ\_RESET\_TT 0x09

[ 41](usb__hub_8h.md#a4cafe5c744f8e73e1477791c1b64d650)#define USB\_HCREQ\_GET\_TT\_STATE 0x0A

[ 42](usb__hub_8h.md#aacc155cfc273b57e73d2893d1693bfd1)#define USB\_HCREQ\_STOP\_TT 0x0B

43

44#endif /\* ZEPHYR\_INCLUDE\_USB\_CLASS\_USB\_HUB\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_hub.h](usb__hub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
