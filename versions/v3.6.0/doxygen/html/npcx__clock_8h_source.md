---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/npcx__clock_8h_source.html
original_path: doxygen/html/npcx__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npcx\_clock.h

[Go to the documentation of this file.](npcx__clock_8h.md)

1/\*

2 \* Copyright (c) 2020 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NPCX\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NPCX\_CLOCK\_H\_

8

9/\* clock bus references \*/

[ 10](npcx__clock_8h.md#a9f3fc618897763975a65f66c619854ac)#define NPCX\_CLOCK\_BUS\_FREERUN 0

[ 11](npcx__clock_8h.md#a382491652e75bde69fbac082e3402913)#define NPCX\_CLOCK\_BUS\_LFCLK 1

[ 12](npcx__clock_8h.md#a0425fca091b81a5b9d1052a7d34b4de4)#define NPCX\_CLOCK\_BUS\_OSC 2

[ 13](npcx__clock_8h.md#ab2bc8744b107a91a609f76f9efc57866)#define NPCX\_CLOCK\_BUS\_FIU 3

[ 14](npcx__clock_8h.md#aef0bb3e64c85a87af7006b81616fbeac)#define NPCX\_CLOCK\_BUS\_CORE 4

[ 15](npcx__clock_8h.md#aa8598937aaed8d93dba381bfc407af6e)#define NPCX\_CLOCK\_BUS\_APB1 5

[ 16](npcx__clock_8h.md#acf61d3dd0d38a2052effd4d86e3d1cd9)#define NPCX\_CLOCK\_BUS\_APB2 6

[ 17](npcx__clock_8h.md#a652de72b9824db8f2c8401c337cd8ca0)#define NPCX\_CLOCK\_BUS\_APB3 7

[ 18](npcx__clock_8h.md#afb9bea70ff6783393a846602fa04ccf2)#define NPCX\_CLOCK\_BUS\_APB4 8

[ 19](npcx__clock_8h.md#a4cdc44708ecbbe475c641f90e165da46)#define NPCX\_CLOCK\_BUS\_AHB6 9

[ 20](npcx__clock_8h.md#ac7df6df2fba5420e5d5f2c6752b0eb36)#define NPCX\_CLOCK\_BUS\_FMCLK 10

[ 21](npcx__clock_8h.md#a1be6f0a37effd6c311efa0c6d0de09a8)#define NPCX\_CLOCK\_BUS\_FIU0 NPCX\_CLOCK\_BUS\_FIU

[ 22](npcx__clock_8h.md#a6ec4f8868b227546318d4fe54f7c020f)#define NPCX\_CLOCK\_BUS\_FIU1 11

23

24/\* clock enable/disable references \*/

[ 25](npcx__clock_8h.md#a3cfc03c2f2b22b58bfaa62f8e753050f)#define NPCX\_PWDWN\_CTL1 0

[ 26](npcx__clock_8h.md#a2253e4b15af7daf3ff65d90ba86c421c)#define NPCX\_PWDWN\_CTL2 1

[ 27](npcx__clock_8h.md#afcd2d828dadff9fb0d76a20519bc5e79)#define NPCX\_PWDWN\_CTL3 2

[ 28](npcx__clock_8h.md#a4019557265432cccae4e51784f0ad727)#define NPCX\_PWDWN\_CTL4 3

[ 29](npcx__clock_8h.md#ac18e443a37a88218a4224e0eab242ba2)#define NPCX\_PWDWN\_CTL5 4

[ 30](npcx__clock_8h.md#ab3a1cbb76c0157237f668a1e33a61f1d)#define NPCX\_PWDWN\_CTL6 5

[ 31](npcx__clock_8h.md#a9134426b5250e98c1a5e81b7cf0a4c2a)#define NPCX\_PWDWN\_CTL7 6

[ 32](npcx__clock_8h.md#a635ddd778df9d5c850c88ce6257b8443)#define NPCX\_PWDWN\_CTL8 7

[ 33](npcx__clock_8h.md#a7fccea2270c428253610ebd8df38e851)#define NPCX\_PWDWN\_CTL\_COUNT 8

34

35#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NPCX\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [npcx\_clock.h](npcx__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
