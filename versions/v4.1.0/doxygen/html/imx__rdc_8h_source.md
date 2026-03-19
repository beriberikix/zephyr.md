---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/imx__rdc_8h_source.html
original_path: doxygen/html/imx__rdc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx\_rdc.h

[Go to the documentation of this file.](imx__rdc_8h.md)

1/\*

2 \* Copyright (c) 2018, Diego Sueiro

3 \* Copyright 2024 NXP

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RDC\_IMX\_RDC\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RDC\_IMX\_RDC\_H\_

10

[ 11](imx__rdc_8h.md#aac94244543640603434faa2862eb1eef)#define A7\_DOMAIN\_ID 0

[ 12](imx__rdc_8h.md#a2f961de9f7c100cf1ef6aa65cf40cd4f)#define A9\_DOMAIN\_ID 0

[ 13](imx__rdc_8h.md#ad150e5ccb613174d8aadea285fd99a03)#define A53\_DOMAIN\_ID 0

[ 14](imx__rdc_8h.md#adf4bff1dbb4418d4c9aa2ecb5d8e129a)#define M4\_DOMAIN\_ID 1

[ 15](imx__rdc_8h.md#a926358589743b689f3b9fc11a06c9f52)#define M7\_DOMAIN\_ID 1

16

[ 17](imx__rdc_8h.md#aacbb82ed8695c00e9bfcb0458495c17d)#define RDC\_DOMAIN\_PERM\_NONE (0x0)

[ 18](imx__rdc_8h.md#a29b98390e0431ebd6c92e227c5fda530)#define RDC\_DOMAIN\_PERM\_W (0x1)

[ 19](imx__rdc_8h.md#a95d915525ff5b3873462f00f2f64dedc)#define RDC\_DOMAIN\_PERM\_R (0x2)

[ 20](imx__rdc_8h.md#ad50d355ba8404bbd872a0d6a8ea23f9d)#define RDC\_DOMAIN\_PERM\_RW (RDC\_DOMAIN\_PERM\_W|RDC\_DOMAIN\_PERM\_R)

21

[ 22](imx__rdc_8h.md#a6e2ca7030bfeb01a10d3b66e37f06a03)#define RDC\_DOMAIN\_PERM(domain, perm) (perm << (domain \* 2))

23

[ 24](imx__rdc_8h.md#acdbb0f6700bd61336079152f3e704896)#define RDC\_DT\_VAL(nodelabel) DT\_PROP(DT\_NODELABEL(nodelabel), rdc)

25

26#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RDC\_IMX\_RDC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [rdc](dir_05c3918b97c5e0e97965e827aa660eab.md)
- [imx\_rdc.h](imx__rdc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
