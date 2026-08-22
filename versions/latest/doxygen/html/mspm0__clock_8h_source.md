---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mspm0__clock_8h_source.html
original_path: doxygen/html/mspm0__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspm0\_clock.h

[Go to the documentation of this file.](mspm0__clock_8h.md)

1/\*

2 \* Copyright 2025 Texas Instruments Inc.

3 \* Copyright 2025 Linumiz

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MSPM0\_CLOCK\_H

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MSPM0\_CLOCK\_H

10

[ 11](mspm0__clock_8h.md#a546f50fc3a86ada7e34d3c5b78526e5e)#define MSPM0\_CLOCK(clk, bit) ((clk << 8) | bit)

12

13/\* Peripheral clock source selection register mask \*/

[ 14](mspm0__clock_8h.md#a35877f69e306437ad9c8bea5ce455e11)#define MSPM0\_CLOCK\_PERIPH\_REG\_MASK(X) (X & 0xFF)

15

16/\* Clock references \*/

[ 17](mspm0__clock_8h.md#a7df45c402fe047a5b5742c1dda57c6b5)#define MSPM0\_CLOCK\_SYSOSC MSPM0\_CLOCK(0x0, 0x0)

[ 18](mspm0__clock_8h.md#a1eef26082f2c6a8bf57cfb33a8ae7bca)#define MSPM0\_CLOCK\_LFCLK MSPM0\_CLOCK(0x1, 0x2)

[ 19](mspm0__clock_8h.md#a3a35970f45fab5f68466339e14a5dcb1)#define MSPM0\_CLOCK\_MFCLK MSPM0\_CLOCK(0x2, 0x4)

[ 20](mspm0__clock_8h.md#a86b9a5c73fae48eace61eaddb94a7309)#define MSPM0\_CLOCK\_BUSCLK MSPM0\_CLOCK(0x3, 0x8)

[ 21](mspm0__clock_8h.md#a9b1175ca378a2e7cfcda5f1ed0c0759a)#define MSPM0\_CLOCK\_ULPCLK MSPM0\_CLOCK(0x4, 0x8)

[ 22](mspm0__clock_8h.md#aa8a1076dd4b533aa15b2ee838047546c)#define MSPM0\_CLOCK\_MCLK MSPM0\_CLOCK(0x5, 0x8)

[ 23](mspm0__clock_8h.md#aa4b3c20657ab23b60f249d1f459829fd)#define MSPM0\_CLOCK\_MFPCLK MSPM0\_CLOCK(0x6, 0x0)

[ 24](mspm0__clock_8h.md#abb0965a9382c3e85ec418ac911766094)#define MSPM0\_CLOCK\_CANCLK MSPM0\_CLOCK(0x7, 0x0)

[ 25](mspm0__clock_8h.md#ad2a34eb409acbd0a2058434cdcf3c40c)#define MSPM0\_CLOCK\_CLK\_OUT MSPM0\_CLOCK(0x8, 0x0)

26

27#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [mspm0\_clock.h](mspm0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
