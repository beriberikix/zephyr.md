---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rpi__pico__clock_8h_source.html
original_path: doxygen/html/rpi__pico__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi\_pico\_clock.h

[Go to the documentation of this file.](rpi__pico__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Andrei-Edward Popa

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RPI\_PICO\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RPI\_PICO\_CLOCK\_H\_

8

[ 9](rpi__pico__clock_8h.md#a466e4913a0890f6d06decf7fe912a8d6)#define RPI\_PICO\_PLL\_SYS 0

[ 10](rpi__pico__clock_8h.md#a32863224d85037e237d6ba1d6f526349)#define RPI\_PICO\_PLL\_USB 1

[ 11](rpi__pico__clock_8h.md#ac641d50669b0c5a5932ba47754f997f2)#define RPI\_PICO\_PLL\_COUNT 2

12

[ 13](rpi__pico__clock_8h.md#ac64aeeb93c3df085cdba8088c7e71643)#define RPI\_PICO\_GPIN\_0 0

[ 14](rpi__pico__clock_8h.md#a6f6f6655d1e43da01b19f676da7eba9f)#define RPI\_PICO\_GPIN\_1 1

[ 15](rpi__pico__clock_8h.md#a0c1f6d136e18501a33806da47b4fbd74)#define RPI\_PICO\_GPIN\_COUNT 2

16

[ 17](rpi__pico__clock_8h.md#ad69d8a2bad53c6d014daaf080459785f)#define RPI\_PICO\_CLKID\_CLK\_GPOUT0 0

[ 18](rpi__pico__clock_8h.md#a4ff53626cd36bd222c4fd03fa2a1cd7c)#define RPI\_PICO\_CLKID\_CLK\_GPOUT1 1

[ 19](rpi__pico__clock_8h.md#ad56ce5dde45a27c349e97060fe81b877)#define RPI\_PICO\_CLKID\_CLK\_GPOUT2 2

[ 20](rpi__pico__clock_8h.md#adc9f3183caef9040a3e217b8ad373aa4)#define RPI\_PICO\_CLKID\_CLK\_GPOUT3 3

[ 21](rpi__pico__clock_8h.md#a3209f2d463248e9eaecf91bfad06221c)#define RPI\_PICO\_CLKID\_CLK\_REF 4

[ 22](rpi__pico__clock_8h.md#aa6925acbb797026caccb78c0bb0c64c5)#define RPI\_PICO\_CLKID\_CLK\_SYS 5

[ 23](rpi__pico__clock_8h.md#aa0e2c91d4ad02985c075c9206d1be314)#define RPI\_PICO\_CLKID\_CLK\_PERI 6

[ 24](rpi__pico__clock_8h.md#a791f267cb9b1fc36e024dd7c0d72b9c5)#define RPI\_PICO\_CLKID\_CLK\_USB 7

[ 25](rpi__pico__clock_8h.md#a34360769303719d99776e50019050d5f)#define RPI\_PICO\_CLKID\_CLK\_ADC 8

[ 26](rpi__pico__clock_8h.md#a54693a90319dedf8a7c7c0bad0f087e7)#define RPI\_PICO\_CLKID\_CLK\_RTC 9

27

[ 28](rpi__pico__clock_8h.md#afa64692c1c8e8c28970fd9c88a8a1adf)#define RPI\_PICO\_CLKID\_PLL\_SYS 10

[ 29](rpi__pico__clock_8h.md#aec02ce9014d772f07ba4e25d825e61a0)#define RPI\_PICO\_CLKID\_PLL\_USB 11

[ 30](rpi__pico__clock_8h.md#ace2c7bd1defff7594766ad67416ed524)#define RPI\_PICO\_CLKID\_XOSC 12

[ 31](rpi__pico__clock_8h.md#a942f1316a463d6a10d4edf88176915f2)#define RPI\_PICO\_CLKID\_ROSC 13

[ 32](rpi__pico__clock_8h.md#af74becbd25d5e91d0034236b30c13b73)#define RPI\_PICO\_CLKID\_ROSC\_PH 14

[ 33](rpi__pico__clock_8h.md#a5da8c9643f9505364e73f1ea44555939)#define RPI\_PICO\_CLKID\_GPIN0 15

[ 34](rpi__pico__clock_8h.md#a668080f8aaa30b302a2eb92c11320533)#define RPI\_PICO\_CLKID\_GPIN1 16

35

[ 36](rpi__pico__clock_8h.md#a4b34aea0ef551dbdc54a321ebb891866)#define RPI\_PICO\_ROSC\_RANGE\_RESET 0xAA0

[ 37](rpi__pico__clock_8h.md#ac095e9944a07e06b48bc2bce646afac1)#define RPI\_PICO\_ROSC\_RANGE\_LOW 0xFA4

[ 38](rpi__pico__clock_8h.md#afeca2ad3fbf43ff038e7d8b334de8217)#define RPI\_PICO\_ROSC\_RANGE\_MEDIUM 0xFA5

[ 39](rpi__pico__clock_8h.md#a109f4ccc6aca6fc3fdf31be5817e779c)#define RPI\_PICO\_ROSC\_RANGE\_HIGH 0xFA7

[ 40](rpi__pico__clock_8h.md#ab8e87bc64fecf6db1ff6124be82b9120)#define RPI\_PICO\_ROSC\_RANGE\_TOOHIGH 0xFA6

41

[ 42](rpi__pico__clock_8h.md#a610d24203e8b6b6d69a37ee38c26b2d2)#define RPI\_PICO\_CLOCK\_COUNT 10

43

44#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RPI\_PICO\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [rpi\_pico\_clock.h](rpi__pico__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
