---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl__soc__bflb__common_8h_source.html
original_path: doxygen/html/pinctrl__soc__bflb__common_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_soc\_bflb\_common.h

[Go to the documentation of this file.](pinctrl__soc__bflb__common_8h.md)

1/\*

2 \* Copyright (c) 2021-2025 Gerson Fernando Budke <nandojve@gmail.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_SOC\_BFLB\_COMMON\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_SOC\_BFLB\_COMMON\_H\_

14

15#include <[zephyr/devicetree.h](devicetree_8h.md)>

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17

18/\* clang-format off \*/

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

25

45typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d);

46

54#define Z\_PINCTRL\_STATE\_PIN\_INIT(node\_id, prop, idx) \

55 ((DT\_PROP\_BY\_IDX(node\_id, prop, idx)) \

56 | (DT\_PROP(node\_id, bias\_pull\_up) << BFLB\_PINMUX\_PULL\_UP\_POS) \

57 | (DT\_PROP(node\_id, bias\_pull\_down) << BFLB\_PINMUX\_PULL\_DOWN\_POS) \

58 | (DT\_PROP(node\_id, output\_enable) << BFLB\_PINMUX\_OE\_POS) \

59 | (DT\_PROP(node\_id, input\_schmitt\_enable) << BFLB\_PINMUX\_SMT\_POS) \

60 | (DT\_ENUM\_IDX(node\_id, drive\_strength) << BFLB\_PINMUX\_DRIVER\_STRENGTH\_POS) \

61 ),

62

69#define Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, prop) \

70 {DT\_FOREACH\_CHILD\_VARGS(DT\_PHANDLE(node\_id, prop), \

71 DT\_FOREACH\_PROP\_ELEM, pinmux, \

72 Z\_PINCTRL\_STATE\_PIN\_INIT)}

73

75

76#ifdef \_\_cplusplus

77}

78#endif

79

80/\* clang-format on \*/

81

82#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_SOC\_BFLB\_COMMON\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[types.h](include_2zephyr_2types_8h.md)

[pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d)

struct pinctrl\_soc\_pin pinctrl\_soc\_pin\_t

Type for R-Car pin.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl](dir_c0bb3bf986f9412b3a6b9d85dc06c157.md)
- [pinctrl\_soc\_bflb\_common.h](pinctrl__soc__bflb__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
