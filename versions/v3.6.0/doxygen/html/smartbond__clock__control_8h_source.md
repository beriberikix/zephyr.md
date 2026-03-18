---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/smartbond__clock__control_8h_source.html
original_path: doxygen/html/smartbond__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smartbond\_clock\_control.h

[Go to the documentation of this file.](smartbond__clock__control_8h.md)

1/\*

2 \* Copyright (c) 2023 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_SMARTBOND\_CLOCK\_CONTROL\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_SMARTBOND\_CLOCK\_CONTROL\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 21](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83)enum [smartbond\_clock](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83) {

22 /\* Not a clock, used for error case only \*/

[ 23](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a89ea767c0399e9325736b661b7c5d298) [SMARTBOND\_CLK\_NONE](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a89ea767c0399e9325736b661b7c5d298),

[ 24](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a16fb9df64c8f3921272f0fe93f9ed6c7) [SMARTBOND\_CLK\_RC32K](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a16fb9df64c8f3921272f0fe93f9ed6c7),

[ 25](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83aa4fb1618d90efc7580dd3f89e7ef9036) [SMARTBOND\_CLK\_RCX](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83aa4fb1618d90efc7580dd3f89e7ef9036),

[ 26](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83ae1a24769cf389312fbf1554cc4404c99) [SMARTBOND\_CLK\_XTAL32K](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83ae1a24769cf389312fbf1554cc4404c99),

[ 27](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a683e5cf10c55857edb78c547dd02a7e3) [SMARTBOND\_CLK\_RC32M](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a683e5cf10c55857edb78c547dd02a7e3),

[ 28](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a372e528a85ba9f8a7c2c1b90c54f77ab) [SMARTBOND\_CLK\_XTAL32M](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a372e528a85ba9f8a7c2c1b90c54f77ab),

[ 29](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a1ac03107185f01fbcd9f12733a1d89b3) [SMARTBOND\_CLK\_PLL96M](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a1ac03107185f01fbcd9f12733a1d89b3),

[ 30](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a21bab67b1cf51a9784fbcdea997134fe) [SMARTBOND\_CLK\_DIVN\_32M](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a21bab67b1cf51a9784fbcdea997134fe),

[ 31](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83afde13daa39fdbe4048ba2f1459027258) [SMARTBOND\_CLK\_HCLK](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83afde13daa39fdbe4048ba2f1459027258),

[ 32](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a6abb5210f065753cbfa1fbd74d7562a7) [SMARTBOND\_CLK\_LP\_CLK](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a6abb5210f065753cbfa1fbd74d7562a7),

[ 33](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83ad10e9e43712650502a7f92479071c297) [SMARTBOND\_CLK\_SYS\_CLK](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83ad10e9e43712650502a7f92479071c297),

34};

35

42int z\_smartbond\_select\_sys\_clk(enum [smartbond\_clock](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83) sys\_clk);

43

50int z\_smartbond\_select\_lp\_clk(enum [smartbond\_clock](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83) lp\_clk);

51

52#ifdef \_\_cplusplus

53}

54#endif

55

56#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_SMARTBOND\_CLOCK\_CONTROL\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[device.h](device_8h.md)

[smartbond\_clock](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83)

smartbond\_clock

Smartbond clocks.

**Definition** smartbond\_clock\_control.h:21

[SMARTBOND\_CLK\_RC32K](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a16fb9df64c8f3921272f0fe93f9ed6c7)

@ SMARTBOND\_CLK\_RC32K

**Definition** smartbond\_clock\_control.h:24

[SMARTBOND\_CLK\_PLL96M](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a1ac03107185f01fbcd9f12733a1d89b3)

@ SMARTBOND\_CLK\_PLL96M

**Definition** smartbond\_clock\_control.h:29

[SMARTBOND\_CLK\_DIVN\_32M](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a21bab67b1cf51a9784fbcdea997134fe)

@ SMARTBOND\_CLK\_DIVN\_32M

**Definition** smartbond\_clock\_control.h:30

[SMARTBOND\_CLK\_XTAL32M](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a372e528a85ba9f8a7c2c1b90c54f77ab)

@ SMARTBOND\_CLK\_XTAL32M

**Definition** smartbond\_clock\_control.h:28

[SMARTBOND\_CLK\_RC32M](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a683e5cf10c55857edb78c547dd02a7e3)

@ SMARTBOND\_CLK\_RC32M

**Definition** smartbond\_clock\_control.h:27

[SMARTBOND\_CLK\_LP\_CLK](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a6abb5210f065753cbfa1fbd74d7562a7)

@ SMARTBOND\_CLK\_LP\_CLK

**Definition** smartbond\_clock\_control.h:32

[SMARTBOND\_CLK\_NONE](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83a89ea767c0399e9325736b661b7c5d298)

@ SMARTBOND\_CLK\_NONE

**Definition** smartbond\_clock\_control.h:23

[SMARTBOND\_CLK\_RCX](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83aa4fb1618d90efc7580dd3f89e7ef9036)

@ SMARTBOND\_CLK\_RCX

**Definition** smartbond\_clock\_control.h:25

[SMARTBOND\_CLK\_SYS\_CLK](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83ad10e9e43712650502a7f92479071c297)

@ SMARTBOND\_CLK\_SYS\_CLK

**Definition** smartbond\_clock\_control.h:33

[SMARTBOND\_CLK\_XTAL32K](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83ae1a24769cf389312fbf1554cc4404c99)

@ SMARTBOND\_CLK\_XTAL32K

**Definition** smartbond\_clock\_control.h:26

[SMARTBOND\_CLK\_HCLK](smartbond__clock__control_8h.md#a951aa7e2fb999ade4f6c404ce9570a83afde13daa39fdbe4048ba2f1459027258)

@ SMARTBOND\_CLK\_HCLK

**Definition** smartbond\_clock\_control.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [smartbond\_clock\_control.h](smartbond__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
