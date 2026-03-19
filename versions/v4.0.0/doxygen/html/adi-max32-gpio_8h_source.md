---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/adi-max32-gpio_8h_source.html
original_path: doxygen/html/adi-max32-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adi-max32-gpio.h

[Go to the documentation of this file.](adi-max32-gpio_8h.md)

1/\*

2 \* Copyright (c) 2023-2024 Analog Devices, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ADI\_MAX32\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ADI\_MAX32\_GPIO\_H\_

8

15

43

[ 45](group__gpio__interface__max32.md#ga267d4548e80843b5b5678d2050cbef73)#define MAX32\_GPIO\_VSEL\_POS (8U)

[ 46](group__gpio__interface__max32.md#ga57b502aa34453a1af1eb5103221c5bde)#define MAX32\_GPIO\_VSEL\_MASK (0x01U << MAX32\_GPIO\_VSEL\_POS)

[ 47](group__gpio__interface__max32.md#ga476d2376c91da2a1cf1bdfd0a7a95198)#define MAX32\_GPIO\_VSEL\_VDDIO (0U << MAX32\_GPIO\_VSEL\_POS)

[ 48](group__gpio__interface__max32.md#ga964594ce9114dc57a9e50e416e948147)#define MAX32\_GPIO\_VSEL\_VDDIOH (1U << MAX32\_GPIO\_VSEL\_POS)

49

[ 51](group__gpio__interface__max32.md#ga8f42437e9d5cbc3bb2d9d58fee643bc5)#define MAX32\_GPIO\_DRV\_STRENGTH\_POS (9U)

[ 52](group__gpio__interface__max32.md#gaefce80e7ae44c9f9397e3b4f02a59893)#define MAX32\_GPIO\_DRV\_STRENGTH\_MASK (0x03U << MAX32\_GPIO\_DRV\_STRENGTH\_POS)

[ 53](group__gpio__interface__max32.md#gaf783f2b803f4772b5bf4c83f616b8a8a)#define MAX32\_GPIO\_DRV\_STRENGTH\_0 (0U << MAX32\_GPIO\_DRV\_STRENGTH\_POS)

[ 54](group__gpio__interface__max32.md#ga2e0abcd63dbbef23c2368be433c1909d)#define MAX32\_GPIO\_DRV\_STRENGTH\_1 (1U << MAX32\_GPIO\_DRV\_STRENGTH\_POS)

[ 55](group__gpio__interface__max32.md#gae7199008d9e034361d80355651128fdd)#define MAX32\_GPIO\_DRV\_STRENGTH\_2 (2U << MAX32\_GPIO\_DRV\_STRENGTH\_POS)

[ 56](group__gpio__interface__max32.md#gacf1c36bc17e552528ef20d4a8ae67f36)#define MAX32\_GPIO\_DRV\_STRENGTH\_3 (3U << MAX32\_GPIO\_DRV\_STRENGTH\_POS)

57

[ 59](group__gpio__interface__max32.md#gad20918791adf470f4421a2cbc1c7beaf)#define MAX32\_GPIO\_WEAK\_PULL\_UP\_POS (10U)

[ 60](group__gpio__interface__max32.md#gac3a2881b03a0e130c0dc174a7aad5b04)#define MAX32\_GPIO\_WEAK\_PULL\_UP (1U << MAX32\_GPIO\_WEAK\_PULL\_UP\_POS)

[ 62](group__gpio__interface__max32.md#ga81dd2d4a0dbd87b5346c65e608f5ea45)#define MAX32\_GPIO\_WEAK\_PULL\_DOWN\_POS (11U)

[ 63](group__gpio__interface__max32.md#gaa2a5bc76ccfd583c11ee5f18015871be)#define MAX32\_GPIO\_WEAK\_PULL\_DOWN (1U << MAX32\_GPIO\_WEAK\_PULL\_DOWN\_POS)

64

66

68

69#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_ADI\_MAX32\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [adi-max32-gpio.h](adi-max32-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
