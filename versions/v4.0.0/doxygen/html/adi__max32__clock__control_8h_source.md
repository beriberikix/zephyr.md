---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/adi__max32__clock__control_8h_source.html
original_path: doxygen/html/adi__max32__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adi\_max32\_clock\_control.h

[Go to the documentation of this file.](adi__max32__clock__control_8h.md)

1/\*

2 \* Copyright (c) 2023-2024 Analog Devices, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ADI\_MAX32\_CLOCK\_CONTROL\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ADI\_MAX32\_CLOCK\_CONTROL\_H\_

9

10#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

11

12#include <[zephyr/dt-bindings/clock/adi\_max32\_clock.h](adi__max32__clock_8h.md)>

13

14#include <wrap\_max32\_sys.h>

15

17

[ 18](structmax32__perclk.md)struct [max32\_perclk](structmax32__perclk.md) {

[ 19](structmax32__perclk.md#aef1b470aa172b72c180b1cb2a700c459) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bus](structmax32__perclk.md#aef1b470aa172b72c180b1cb2a700c459);

[ 20](structmax32__perclk.md#a10dd006d4c09983c0947a07eb9085348) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bit](structmax32__perclk.md#a10dd006d4c09983c0947a07eb9085348);

21

22 /\* Peripheral clock source:

23 \* Can be (see: adi\_max32\_clock.h file):

24 \*

25 \* ADI\_MAX32\_PRPH\_CLK\_SRC\_PCLK

26 \* ADI\_MAX32\_PRPH\_CLK\_SRC\_EXTCLK

27 \* ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO

28 \* ADI\_MAX32\_PRPH\_CLK\_SRC\_ERFO

29 \* ADI\_MAX32\_PRPH\_CLK\_SRC\_ERTCO

30 \* ADI\_MAX32\_PRPH\_CLK\_SRC\_INRO

31 \* ADI\_MAX32\_PRPH\_CLK\_SRC\_ISO

32 \* ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO\_DIV8

33 \*/

[ 34](structmax32__perclk.md#a02bb20153ff5e67ad9a7dbc5a45c646c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_src](structmax32__perclk.md#a02bb20153ff5e67ad9a7dbc5a45c646c);

35};

36

[ 38](adi__max32__clock__control_8h.md#a41eab4d492a019700d1e1d4714932cd9)#define ADI\_MAX32\_SYSCLK\_PRESCALER DT\_PROP\_OR(DT\_NODELABEL(gcr), sysclk\_prescaler, 1)

39

[ 40](adi__max32__clock__control_8h.md#a31a7fbb2f0c1ce1f5b9899b49b6324ec)#define ADI\_MAX32\_CLK\_IPO\_FREQ DT\_PROP(DT\_NODELABEL(clk\_ipo), clock\_frequency)

[ 41](adi__max32__clock__control_8h.md#a56a549a210a78cb99f019f85fa15807b)#define ADI\_MAX32\_CLK\_ERFO\_FREQ DT\_PROP(DT\_NODELABEL(clk\_erfo), clock\_frequency)

[ 42](adi__max32__clock__control_8h.md#ae5e0473609734b17bcdd2ce6f4e7a63a)#define ADI\_MAX32\_CLK\_IBRO\_FREQ DT\_PROP(DT\_NODELABEL(clk\_ibro), clock\_frequency)

[ 43](adi__max32__clock__control_8h.md#ace96ad0d7564ad0fe326992257686820)#define ADI\_MAX32\_CLK\_ISO\_FREQ DT\_PROP\_OR(DT\_NODELABEL(clk\_iso), clock\_frequency, 0)

[ 44](adi__max32__clock__control_8h.md#abb3947e441021737ca566e89fd56cb0c)#define ADI\_MAX32\_CLK\_INRO\_FREQ DT\_PROP(DT\_NODELABEL(clk\_inro), clock\_frequency)

[ 45](adi__max32__clock__control_8h.md#a664282617e29d44f951a48da1ac1ae9d)#define ADI\_MAX32\_CLK\_ERTCO\_FREQ DT\_PROP(DT\_NODELABEL(clk\_ertco), clock\_frequency)

46/\* External clock may not be defined so \_OR is used \*/

[ 47](adi__max32__clock__control_8h.md#a158271c4ced07ddeda9e677f7fd028c7)#define ADI\_MAX32\_CLK\_EXTCLK\_FREQ DT\_PROP\_OR(DT\_NODELABEL(clk\_extclk), clock\_frequency, 0)

48

[ 49](adi__max32__clock__control_8h.md#a1de5a43e10f129609662765dc2ebac24)#define DT\_GCR\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(gcr))

50

51#if DT\_SAME\_NODE(DT\_GCR\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_ipo))

52#define ADI\_MAX32\_SYSCLK\_SRC ADI\_MAX32\_CLK\_IPO

53#define ADI\_MAX32\_SYSCLK\_FREQ (ADI\_MAX32\_CLK\_IPO\_FREQ / ADI\_MAX32\_SYSCLK\_PRESCALER)

54#endif

55#if DT\_SAME\_NODE(DT\_GCR\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_erfo))

56#define ADI\_MAX32\_SYSCLK\_SRC ADI\_MAX32\_CLK\_ERFO

57#define ADI\_MAX32\_SYSCLK\_FREQ (ADI\_MAX32\_CLK\_ERFO\_FREQ / ADI\_MAX32\_SYSCLK\_PRESCALER)

58#endif

59#if DT\_SAME\_NODE(DT\_GCR\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_ibro))

60#define ADI\_MAX32\_SYSCLK\_SRC ADI\_MAX32\_CLK\_IBRO

61#define ADI\_MAX32\_SYSCLK\_FREQ (ADI\_MAX32\_CLK\_IBRO\_FREQ / ADI\_MAX32\_SYSCLK\_PRESCALER)

62#endif

63#if DT\_SAME\_NODE(DT\_GCR\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_iso))

64#define ADI\_MAX32\_SYSCLK\_SRC ADI\_MAX32\_CLK\_ISO

65#define ADI\_MAX32\_SYSCLK\_FREQ (ADI\_MAX32\_CLK\_ISO\_FREQ / ADI\_MAX32\_SYSCLK\_PRESCALER)

66#endif

67#if DT\_SAME\_NODE(DT\_GCR\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_inro))

68#define ADI\_MAX32\_SYSCLK\_SRC ADI\_MAX32\_CLK\_INRO

69#define ADI\_MAX32\_SYSCLK\_FREQ (ADI\_MAX32\_CLK\_INRO\_FREQ / ADI\_MAX32\_SYSCLK\_PRESCALER)

70#endif

71#if DT\_SAME\_NODE(DT\_GCR\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_ertco))

72#define ADI\_MAX32\_SYSCLK\_SRC ADI\_MAX32\_CLK\_ERTCO

73#define ADI\_MAX32\_SYSCLK\_FREQ (ADI\_MAX32\_CLK\_ERTCO\_FREQ / ADI\_MAX32\_SYSCLK\_PRESCALER)

74#endif

75#if DT\_SAME\_NODE(DT\_GCR\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_extclk))

76#define ADI\_MAX32\_SYSCLK\_SRC ADI\_MAX32\_CLK\_EXTCLK

77#define ADI\_MAX32\_SYSCLK\_FREQ (ADI\_MAX32\_CLK\_EXTCLK\_FREQ / ADI\_MAX32\_SYSCLK\_PRESCALER)

78#endif

79

80#ifndef ADI\_MAX32\_SYSCLK\_SRC

[ 81](adi__max32__clock__control_8h.md#a21d5bba4fce8bf21105689ae8ea96216)#define ADI\_MAX32\_SYSCLK\_SRC ADI\_MAX32\_CLK\_IPO

[ 82](adi__max32__clock__control_8h.md#ac82b515b2268a26b19b69972fc113e1c)#define ADI\_MAX32\_SYSCLK\_FREQ (ADI\_MAX32\_CLK\_IPO\_FREQ / ADI\_MAX32\_SYSCLK\_PRESCALER)

83#endif

84

[ 85](adi__max32__clock__control_8h.md#a4e3ca6232db9220b60f17d1dca74627f)#define ADI\_MAX32\_PCLK\_FREQ (ADI\_MAX32\_SYSCLK\_FREQ / 2)

86

[ 87](adi__max32__clock__control_8h.md#abc5b92548642b17cb955d1f6b1949726)#define ADI\_MAX32\_GET\_PRPH\_CLK\_FREQ(clk\_src) \

88 ((clk\_src) == ADI\_MAX32\_PRPH\_CLK\_SRC\_PCLK ? ADI\_MAX32\_PCLK\_FREQ \

89 : (clk\_src) == ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO ? ADI\_MAX32\_CLK\_IBRO\_FREQ \

90 : (clk\_src) == ADI\_MAX32\_PRPH\_CLK\_SRC\_ERFO ? ADI\_MAX32\_CLK\_ERFO\_FREQ \

91 : (clk\_src) == ADI\_MAX32\_PRPH\_CLK\_SRC\_ERTCO ? ADI\_MAX32\_CLK\_ERTCO\_FREQ \

92 : (clk\_src) == ADI\_MAX32\_PRPH\_CLK\_SRC\_INRO ? ADI\_MAX32\_CLK\_INRO\_FREQ \

93 : (clk\_src) == ADI\_MAX32\_PRPH\_CLK\_SRC\_ISO ? ADI\_MAX32\_CLK\_ISO\_FREQ \

94 : (clk\_src) == ADI\_MAX32\_PRPH\_CLK\_SRC\_IBRO\_DIV8 ? (ADI\_MAX32\_CLK\_IBRO\_FREQ / 8) \

95 : (clk\_src) == ADI\_MAX32\_PRPH\_CLK\_SRC\_EXTCLK ? ADI\_MAX32\_CLK\_EXTCLK\_FREQ \

96 : 0)

97

98#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ADI\_MAX32\_CLOCK\_CONTROL\_H\_ \*/

[adi\_max32\_clock.h](adi__max32__clock_8h.md)

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[max32\_perclk](structmax32__perclk.md)

Driver structure definition.

**Definition** adi\_max32\_clock\_control.h:18

[max32\_perclk::clk\_src](structmax32__perclk.md#a02bb20153ff5e67ad9a7dbc5a45c646c)

uint32\_t clk\_src

**Definition** adi\_max32\_clock\_control.h:34

[max32\_perclk::bit](structmax32__perclk.md#a10dd006d4c09983c0947a07eb9085348)

uint32\_t bit

**Definition** adi\_max32\_clock\_control.h:20

[max32\_perclk::bus](structmax32__perclk.md#aef1b470aa172b72c180b1cb2a700c459)

uint32\_t bus

**Definition** adi\_max32\_clock\_control.h:19

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [adi\_max32\_clock\_control.h](adi__max32__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
