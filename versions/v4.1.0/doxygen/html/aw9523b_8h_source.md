---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/aw9523b_8h_source.html
original_path: doxygen/html/aw9523b_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

aw9523b.h

[Go to the documentation of this file.](aw9523b_8h.md)

1/\*

2 \* Copyright (c) 2024 TOKITA Hiroshi

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AW9523B\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AW9523B\_H\_

9

10struct k\_sem;

11struct [device](structdevice.md);

12

[ 13](aw9523b_8h.md#a1f7aa80f94e817243c025fa69a93e7a2)#define AW9523B\_REG\_INPUT0 0x00

[ 14](aw9523b_8h.md#afbf23b8ce14c96dc50ce317138f98867)#define AW9523B\_REG\_INPUT1 0x01

[ 15](aw9523b_8h.md#a3341e3bac373ce220a8b7a9629bb1229)#define AW9523B\_REG\_OUTPUT0 0x02

[ 16](aw9523b_8h.md#af419d7d29c16ff1dbb47bc2854d02403)#define AW9523B\_REG\_OUTPUT1 0x03

[ 17](aw9523b_8h.md#a3fd2c20478daa9e54029d676b7ed051a)#define AW9523B\_REG\_CONFIG0 0x04

[ 18](aw9523b_8h.md#a9a02d43d60c3810d73a2d7e06dd88580)#define AW9523B\_REG\_CONFIG1 0x05

[ 19](aw9523b_8h.md#a89ce2c5b1ec5b7210f6eb6312c03f77e)#define AW9523B\_REG\_INT0 0x06

[ 20](aw9523b_8h.md#a08dff7582b4c9a07e87d205aec180686)#define AW9523B\_REG\_INT1 0x07

[ 21](aw9523b_8h.md#a2688498eed938ad419d1a43c06244615)#define AW9523B\_REG\_ID 0x10

[ 22](aw9523b_8h.md#a3e7e0c602b6d81e104432e939a413509)#define AW9523B\_REG\_CTL 0x11

[ 23](aw9523b_8h.md#a388713ac651192a7e5538a658ebbb255)#define AW9523B\_REG\_MODE0 0x12

[ 24](aw9523b_8h.md#a47c3f456cfc9bc72c1c9ef2ba306bc12)#define AW9523B\_REG\_MODE1 0x13

[ 25](aw9523b_8h.md#af3d0173aa8962a759591d5c4bbdf5db8)#define AW9523B\_REG\_DIM0 0x20

[ 26](aw9523b_8h.md#a9c7923f5e3f3b896fa3afec9b99f17d4)#define AW9523B\_REG\_DIM1 0x21

[ 27](aw9523b_8h.md#a4d5196fca641d6a6c0278f231b6b3f8e)#define AW9523B\_REG\_DIM2 0x22

[ 28](aw9523b_8h.md#ad960cb044ea73b219f93c4f2def11079)#define AW9523B\_REG\_DIM3 0x23

[ 29](aw9523b_8h.md#aa0a9852cf4b26dcd116af3de93158a5c)#define AW9523B\_REG\_DIM4 0x24

[ 30](aw9523b_8h.md#ae2e0b10772f2c930688be2d7ad5ef255)#define AW9523B\_REG\_DIM5 0x25

[ 31](aw9523b_8h.md#ac023a04ddfa03d53215fc7a5c810a9a0)#define AW9523B\_REG\_DIM6 0x26

[ 32](aw9523b_8h.md#aac1a4aa90e1bfee50e908ae635cb99b3)#define AW9523B\_REG\_DIM7 0x27

[ 33](aw9523b_8h.md#a2dbf73306042bbe13377c740d0d9ad1b)#define AW9523B\_REG\_DIM8 0x28

[ 34](aw9523b_8h.md#a4aa914a5e2333d96b95ff8dd98726c16)#define AW9523B\_REG\_DIM9 0x29

[ 35](aw9523b_8h.md#a0eda894e55d4489b459f56ab7e7b74fc)#define AW9523B\_REG\_DIM10 0x2A

[ 36](aw9523b_8h.md#a11c877cc36271eae10e5f5f30c64a808)#define AW9523B\_REG\_DIM11 0x2B

[ 37](aw9523b_8h.md#a7e639b7be7e076fad8c575764e7e78d0)#define AW9523B\_REG\_DIM12 0x2C

[ 38](aw9523b_8h.md#a9da30c63370af2093cdd75f027683f48)#define AW9523B\_REG\_DIM13 0x2D

[ 39](aw9523b_8h.md#ac1d4112c86997da487ee4b6f54b46622)#define AW9523B\_REG\_DIM14 0x2E

[ 40](aw9523b_8h.md#a2fa5cb9c3c9342c268c3781ba7936a5f)#define AW9523B\_REG\_DIM15 0x2F

[ 41](aw9523b_8h.md#aae1c0f21390b157b8484aab1a53a0a40)#define AW9523B\_REG\_SW\_RSTN 0x7F

42

[ 43](aw9523b_8h.md#a3a9fc514a7f53f404543683787ca83ce)struct k\_sem \*[aw9523b\_get\_lock](aw9523b_8h.md#a3a9fc514a7f53f404543683787ca83ce)(const struct [device](structdevice.md) \*dev);

44

45#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AW9523B\_H\_ \*/

[aw9523b\_get\_lock](aw9523b_8h.md#a3a9fc514a7f53f404543683787ca83ce)

struct k\_sem \* aw9523b\_get\_lock(const struct device \*dev)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [aw9523b.h](aw9523b_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
