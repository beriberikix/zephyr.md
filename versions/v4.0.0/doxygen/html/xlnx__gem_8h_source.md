---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/xlnx__gem_8h_source.html
original_path: doxygen/html/xlnx__gem_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xlnx\_gem.h

[Go to the documentation of this file.](xlnx__gem_8h.md)

1/\*

2 \* Copyright (c) 2021-2022, Weidmueller Interface GmbH & Co. KG

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ETHERNET\_XLNX\_GEM\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ETHERNET\_XLNX\_GEM\_H\_

8

9/\* PHY auto-detection alias \*/

[ 10](xlnx__gem_8h.md#a6f1dc25e8cf23705674ad0bf8a3dd607)#define XLNX\_GEM\_PHY\_AUTO\_DETECT 0

11

12/\*

13 \* MDC divider values

14 \*

15 \* According to the ZynqMP's gem.network\_config register documentation (UG1087),

16 \* divider /32 is the reset value. The network\_config[mdc\_clock\_division]

17 \* documentation in UG1087 is likely wrong (copied directly from the Zynq-7000),

18 \* as it claims that the MDC clock division is applied to the cpu\_1x clock

19 \* which the UltraScale doesn't have. Contradicting information is provided in

20 \* the UltraScale TRM (UG1085), which mentions in chapter 34, section "Configure

21 \* the PHY", p. 1074, that the MDC clock division is applied to the IOU\_SWITCH\_CLK.

22 \* Xilinx's emacps driver doesn't (or no longer does) limit the range of dividers

23 \* on the UltraScale compared to the Zynq-7000.

24 \* -> Contrary to earlier revisions of this driver, all dividers are available

25 \* to both the UltraScale and the Zynq-7000.

26 \*/

27

[ 28](xlnx__gem_8h.md#aecfc16f895d5904bb88865654192b6af)#define XLNX\_GEM\_MDC\_DIVIDER\_8 0 /\* cpu\_1x or IOU\_SWITCH\_CLK < 20 MHz \*/

[ 29](xlnx__gem_8h.md#a2dd7b7b6960988c9adda4e6bb9104d3b)#define XLNX\_GEM\_MDC\_DIVIDER\_16 1 /\* cpu\_1x or IOU\_SWITCH\_CLK 20 - 40 MHz \*/

[ 30](xlnx__gem_8h.md#a39223a666570e19229337c37affec28a)#define XLNX\_GEM\_MDC\_DIVIDER\_32 2 /\* cpu\_1x or IOU\_SWITCH\_CLK 40 - 80 MHz \*/

[ 31](xlnx__gem_8h.md#ab161bdaf20281af805fe256aa1420965)#define XLNX\_GEM\_MDC\_DIVIDER\_48 3 /\* cpu\_1x or IOU\_SWITCH\_CLK 80 - 120 MHz \*/

[ 32](xlnx__gem_8h.md#a299bad98c83526e02e9cbc7b1e20c3e8)#define XLNX\_GEM\_MDC\_DIVIDER\_64 4 /\* cpu\_1x or IOU\_SWITCH\_CLK 120 - 160 MHz \*/

[ 33](xlnx__gem_8h.md#a903826e931e2f98859a52f3abd6746a5)#define XLNX\_GEM\_MDC\_DIVIDER\_96 5 /\* cpu\_1x or IOU\_SWITCH\_CLK 160 - 240 MHz \*/

[ 34](xlnx__gem_8h.md#ac0c4600967372762d6c331f050900812)#define XLNX\_GEM\_MDC\_DIVIDER\_128 6 /\* cpu\_1x or IOU\_SWITCH\_CLK 240 - 320 MHz \*/

[ 35](xlnx__gem_8h.md#afe8f02554a5ec893f1c5aaf9a67e8406)#define XLNX\_GEM\_MDC\_DIVIDER\_224 7 /\* cpu\_1x or IOU\_SWITCH\_CLK 320 - 540 MHz \*/

36

37/\* Link speed values \*/

[ 38](xlnx__gem_8h.md#a36088d09ca9962a60a92988b1a24b129)#define XLNX\_GEM\_LINK\_SPEED\_10MBIT 1

[ 39](xlnx__gem_8h.md#a9ca8d8dcb4dc9acee911a501b7578f30)#define XLNX\_GEM\_LINK\_SPEED\_100MBIT 2

[ 40](xlnx__gem_8h.md#a3ab42595d945a7a83be47a6693b8b5f2)#define XLNX\_GEM\_LINK\_SPEED\_1GBIT 3

41

42/\* AMBA AHB data bus width \*/

[ 43](xlnx__gem_8h.md#a45ebc16715ede38f89977f402c29a55f)#define XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_32BIT 0

[ 44](xlnx__gem_8h.md#ac73d8a83557499aec09b759e578e6878)#define XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_64BIT 1

[ 45](xlnx__gem_8h.md#a0f60f82ee244fd2522e00a1b897f7d49)#define XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_128BIT 2

46

47/\* AMBA AHB burst length \*/

[ 48](xlnx__gem_8h.md#a2ea757d44f3110a20113acb4673bcf43)#define XLNX\_GEM\_AMBA\_AHB\_BURST\_SINGLE 1

[ 49](xlnx__gem_8h.md#a18db46b4e0826fe2b0ba2de2f198c41d)#define XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR4 4

[ 50](xlnx__gem_8h.md#aaf8ecbfd760ae236aad17ce5ff0ddd91)#define XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR8 8

[ 51](xlnx__gem_8h.md#af53fba620b18e599bef91a544b638ef1)#define XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR16 16

52

53/\* Hardware RX buffer size \*/

[ 54](xlnx__gem_8h.md#a9089698903ed9087cc077b6f8b71716e)#define XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_1KB 0

[ 55](xlnx__gem_8h.md#a7b05fe3ebab46720d425de07fcdb4e59)#define XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_2KB 1

[ 56](xlnx__gem_8h.md#adec908c6be1fde115f7b5b2317f7e49f)#define XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_4KB 2

[ 57](xlnx__gem_8h.md#a3782b31ebb12c7c18fe1ae2d1d71525c)#define XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_8KB 3

58

59#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ETHERNET\_XLNX\_GEM\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [ethernet](dir_206bb9b0b304009ae1ec5beda9489e52.md)
- [xlnx\_gem.h](xlnx__gem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
