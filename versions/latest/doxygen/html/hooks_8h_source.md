---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hooks_8h_source.html
original_path: doxygen/html/hooks_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hooks.h

[Go to the documentation of this file.](hooks_8h.md)

1/\*

2 \* Copyright (c) 2024 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_PLATFORM\_PLATFORM\_H\_

7#define ZEPHYR\_INCLUDE\_PLATFORM\_PLATFORM\_H\_

8

21

22

[ 29](hooks_8h.md#ad6e8df1eefd1add03ad8379802bd989e)void [soc\_reset\_hook](hooks_8h.md#ad6e8df1eefd1add03ad8379802bd989e)(void);

30

[ 37](hooks_8h.md#adc333ec5f401d3d8311a496736bd1aa4)void [soc\_prep\_hook](hooks_8h.md#adc333ec5f401d3d8311a496736bd1aa4)(void);

38

[ 45](hooks_8h.md#a5ee95ec1991b2083210194fe485b3a02)void [soc\_early\_init\_hook](hooks_8h.md#a5ee95ec1991b2083210194fe485b3a02)(void);

46

[ 53](hooks_8h.md#ad3d12da84a31f3d4db5621635f5df687)void [soc\_late\_init\_hook](hooks_8h.md#ad3d12da84a31f3d4db5621635f5df687)(void);

54

[ 61](hooks_8h.md#aed3aa074849066c29086ea37f8f9ef8a)void [soc\_per\_core\_init\_hook](hooks_8h.md#aed3aa074849066c29086ea37f8f9ef8a)(void);

62

[ 70](hooks_8h.md#a684e5461ecf7657b5ab646cdb9e41a51)void [board\_early\_init\_hook](hooks_8h.md#a684e5461ecf7657b5ab646cdb9e41a51)(void);

71

[ 79](hooks_8h.md#adc6098773fbea0f7ba1575f4a47649b1)void [board\_late\_init\_hook](hooks_8h.md#adc6098773fbea0f7ba1575f4a47649b1)(void);

80

81#endif

[soc\_early\_init\_hook](hooks_8h.md#a5ee95ec1991b2083210194fe485b3a02)

void soc\_early\_init\_hook(void)

SoC hook executed before the kernel and devices are initialized.

[board\_early\_init\_hook](hooks_8h.md#a684e5461ecf7657b5ab646cdb9e41a51)

void board\_early\_init\_hook(void)

Board hook executed before the kernel starts.

[soc\_late\_init\_hook](hooks_8h.md#ad3d12da84a31f3d4db5621635f5df687)

void soc\_late\_init\_hook(void)

SoC hook executed after the kernel and devices are initialized.

[soc\_reset\_hook](hooks_8h.md#ad6e8df1eefd1add03ad8379802bd989e)

void soc\_reset\_hook(void)

SoC hook executed at the beginning of the reset vector.

[soc\_prep\_hook](hooks_8h.md#adc333ec5f401d3d8311a496736bd1aa4)

void soc\_prep\_hook(void)

SoC hook executed after the reset vector.

[board\_late\_init\_hook](hooks_8h.md#adc6098773fbea0f7ba1575f4a47649b1)

void board\_late\_init\_hook(void)

Board hook executed after the kernel starts.

[soc\_per\_core\_init\_hook](hooks_8h.md#aed3aa074849066c29086ea37f8f9ef8a)

void soc\_per\_core\_init\_hook(void)

SoC per-core initialization.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [platform](dir_0ba13cd2a44aeab16da188d21efe06c8.md)
- [hooks.h](hooks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
