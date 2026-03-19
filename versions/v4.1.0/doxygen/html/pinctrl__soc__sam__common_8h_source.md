---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pinctrl__soc__sam__common_8h_source.html
original_path: doxygen/html/pinctrl__soc__sam__common_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_soc\_sam\_common.h

[Go to the documentation of this file.](pinctrl__soc__sam__common_8h.md)

1/\*

2 \* Copyright (c) 2022, Gerson Fernando Budke <nandojve@gmail.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_SOC\_SAM\_COMMON\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_SOC\_SAM\_COMMON\_H\_

14

15#include <[zephyr/devicetree.h](devicetree_8h.md)>

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17#include <dt-bindings/pinctrl/atmel\_sam\_pinctrl.h>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

24

32typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d);

33

41#if defined(CONFIG\_SOC\_FAMILY\_ATMEL\_SAM)

42#define Z\_PINCTRL\_STATE\_PIN\_INIT(node\_id, prop, idx) \

43 ((DT\_PROP\_BY\_IDX(node\_id, prop, idx) << SAM\_PINCTRL\_PINMUX\_POS) \

44 | (DT\_PROP(node\_id, bias\_pull\_up) << SAM\_PINCTRL\_PULLUP\_POS) \

45 | (DT\_PROP(node\_id, bias\_pull\_down) << SAM\_PINCTRL\_PULLDOWN\_POS) \

46 | (DT\_PROP(node\_id, drive\_open\_drain) << SAM\_PINCTRL\_OPENDRAIN\_POS) \

47 ),

48#else /\* CONFIG\_SOC\_FAMILY\_ATMEL\_SAM0 \*/

49#define Z\_PINCTRL\_STATE\_PIN\_INIT(node\_id, prop, idx) \

50 ((DT\_PROP\_BY\_IDX(node\_id, prop, idx) << SAM\_PINCTRL\_PINMUX\_POS) \

51 | (DT\_PROP(node\_id, bias\_pull\_up) << SAM\_PINCTRL\_PULLUP\_POS) \

52 | (DT\_PROP(node\_id, bias\_pull\_down) << SAM\_PINCTRL\_PULLDOWN\_POS) \

53 | (DT\_PROP(node\_id, input\_enable) << SAM\_PINCTRL\_INPUTENABLE\_POS) \

54 | (DT\_PROP(node\_id, output\_enable) << SAM\_PINCTRL\_OUTPUTENABLE\_POS) \

55 | (DT\_ENUM\_IDX(node\_id, drive\_strength) << SAM\_PINCTRL\_DRIVESTRENGTH\_POS)\

56 ),

57#endif

58

65#define Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, prop) \

66 {DT\_FOREACH\_CHILD\_VARGS(DT\_PHANDLE(node\_id, prop), \

67 DT\_FOREACH\_PROP\_ELEM, pinmux, \

68 Z\_PINCTRL\_STATE\_PIN\_INIT)}

69

71

72

79

[ 80](pinctrl__soc__sam__common_8h.md#a966bab3a458ab5d74319cd296f25f756)#define SAM\_PINCTRL\_FLAGS\_DEFAULT (0U)

[ 81](pinctrl__soc__sam__common_8h.md#ae42a8c43d997c40238c0cb3af2855ea8)#define SAM\_PINCTRL\_FLAGS\_POS (0U)

[ 82](pinctrl__soc__sam__common_8h.md#a47928c213072d5e26923570e8ef14bd9)#define SAM\_PINCTRL\_FLAGS\_MASK (0x3F << SAM\_PINCTRL\_FLAGS\_POS)

[ 83](pinctrl__soc__sam__common_8h.md#aea986207fa829b606d47d4919a1fb515)#define SAM\_PINCTRL\_FLAG\_MASK (1U)

[ 84](pinctrl__soc__sam__common_8h.md#a60ca2e906d19a30ac9168163301491c0)#define SAM\_PINCTRL\_PULLUP\_POS (SAM\_PINCTRL\_FLAGS\_POS)

[ 85](pinctrl__soc__sam__common_8h.md#a72052ca63d8cac12fdb6314dc9db7f12)#define SAM\_PINCTRL\_PULLUP (1U << SAM\_PINCTRL\_PULLUP\_POS)

[ 86](pinctrl__soc__sam__common_8h.md#a3d1ff6f736aed51318196736067db4c9)#define SAM\_PINCTRL\_PULLDOWN\_POS (SAM\_PINCTRL\_PULLUP\_POS + 1U)

[ 87](pinctrl__soc__sam__common_8h.md#ac39a6835941c340ee1bb0fb71bb34c9c)#define SAM\_PINCTRL\_PULLDOWN (1U << SAM\_PINCTRL\_PULLDOWN\_POS)

[ 88](pinctrl__soc__sam__common_8h.md#af23ac8ff95ef934f2d8dd6f3727ef5fc)#define SAM\_PINCTRL\_OPENDRAIN\_POS (SAM\_PINCTRL\_PULLDOWN\_POS + 1U)

[ 89](pinctrl__soc__sam__common_8h.md#a41a3c21a35fbe8baaea766ffeb56d6ea)#define SAM\_PINCTRL\_OPENDRAIN (1U << SAM\_PINCTRL\_OPENDRAIN\_POS)

[ 90](pinctrl__soc__sam__common_8h.md#a32af1969f02a3f5ac5c92f19258c6b71)#define SAM\_PINCTRL\_INPUTENABLE\_POS (SAM\_PINCTRL\_OPENDRAIN\_POS + 1U)

[ 91](pinctrl__soc__sam__common_8h.md#a354e8d543c70ab5affdffeda7c0e84d9)#define SAM\_PINCTRL\_INPUTENABLE (1U << SAM\_PINCTRL\_INPUTENABLE\_POS)

[ 92](pinctrl__soc__sam__common_8h.md#a078ce2bd47b20adc4d31756373a343a1)#define SAM\_PINCTRL\_OUTPUTENABLE\_POS (SAM\_PINCTRL\_INPUTENABLE\_POS + 1U)

[ 93](pinctrl__soc__sam__common_8h.md#a3d0d020327f4ce53c3e8a705551e01bf)#define SAM\_PINCTRL\_OUTPUTENABLE (1U << SAM\_PINCTRL\_OUTPUTENABLE\_POS)

[ 94](pinctrl__soc__sam__common_8h.md#a984860553e4a824427b86ab627e9e48a)#define SAM\_PINCTRL\_DRIVESTRENGTH\_POS (SAM\_PINCTRL\_OUTPUTENABLE\_POS + 1U)

[ 95](pinctrl__soc__sam__common_8h.md#a510309503bbe70010329b11748f94b23)#define SAM\_PINCTRL\_DRIVESTRENGTH (1U << SAM\_PINCTRL\_DRIVESTRENGTH\_POS)

96

98

[ 105](pinctrl__soc__sam__common_8h.md#ac0d76820e58e8d0ef6a65663ccd488d4)#define SAM\_PINCTRL\_FLAG\_GET(pincfg, pos) \

106 (((pincfg) >> pos) & SAM\_PINCTRL\_FLAG\_MASK)

107

[ 108](pinctrl__soc__sam__common_8h.md#a65850f6768e47ce900ab6ae615764570)#define SAM\_PINCTRL\_FLAGS\_GET(pincfg) \

109 (((pincfg) >> SAM\_PINCTRL\_FLAGS\_POS) & SAM\_PINCTRL\_FLAGS\_MASK)

110

111#ifdef \_\_cplusplus

112}

113#endif

114

115#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_SOC\_SAM\_COMMON\_H\_ \*/

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
- [pinctrl\_soc\_sam\_common.h](pinctrl__soc__sam__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
