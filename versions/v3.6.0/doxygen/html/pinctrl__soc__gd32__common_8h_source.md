---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pinctrl__soc__gd32__common_8h_source.html
original_path: doxygen/html/pinctrl__soc__gd32__common_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_soc\_gd32\_common.h

[Go to the documentation of this file.](pinctrl__soc__gd32__common_8h.md)

1/\*

2 \* Copyright (c) 2021 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_SOC\_GD32\_COMMON\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_SOC\_GD32\_COMMON\_H\_

14

15#include <[zephyr/devicetree.h](devicetree_8h.md)>

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17

18#ifdef CONFIG\_PINCTRL\_GD32\_AF

19#include <dt-bindings/pinctrl/gd32-af.h>

20#else

21#include <dt-bindings/pinctrl/gd32-afio.h>

22#endif /\* CONFIG\_PINCTRL\_GD32\_AF \*/

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

29

42typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pinctrl\_soc\_pin\_t;

43

51#define Z\_PINCTRL\_STATE\_PIN\_INIT(node\_id, prop, idx) \

52 (DT\_PROP\_BY\_IDX(node\_id, prop, idx) | \

53 ((GD32\_PUPD\_PULLUP \* DT\_PROP(node\_id, bias\_pull\_up)) \

54 << GD32\_PUPD\_POS) | \

55 ((GD32\_PUPD\_PULLDOWN \* DT\_PROP(node\_id, bias\_pull\_down)) \

56 << GD32\_PUPD\_POS) | \

57 ((GD32\_OTYPE\_OD \* DT\_PROP(node\_id, drive\_open\_drain)) \

58 << GD32\_OTYPE\_POS) | \

59 (DT\_ENUM\_IDX(node\_id, slew\_rate) << GD32\_OSPEED\_POS)),

60

67#define Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, prop) \

68 {DT\_FOREACH\_CHILD\_VARGS(DT\_PHANDLE(node\_id, prop), \

69 DT\_FOREACH\_PROP\_ELEM, pinmux, \

70 Z\_PINCTRL\_STATE\_PIN\_INIT)}

71

73

78

[ 80](pinctrl__soc__gd32__common_8h.md#a6d65e0d22b11faef8c661c1f64698085)#define GD32\_PUPD\_NONE 0U

[ 82](pinctrl__soc__gd32__common_8h.md#af4c1b103266889ab30f5c83e2936892d)#define GD32\_PUPD\_PULLUP 1U

[ 84](pinctrl__soc__gd32__common_8h.md#a04dd91ec07a12774db8f4b5835c47d39)#define GD32\_PUPD\_PULLDOWN 2U

85

87

92

[ 94](pinctrl__soc__gd32__common_8h.md#ac0a262538fd3143987bf9abc17804db6)#define GD32\_OTYPE\_PP 0U

[ 96](pinctrl__soc__gd32__common_8h.md#af6ce59bcdd18128905acc9982fa20bdd)#define GD32\_OTYPE\_OD 1U

97

99

105

106#ifdef CONFIG\_PINCTRL\_GD32\_AF

108#define GD32\_OSPEED\_2MHZ 0U

109#if defined(CONFIG\_SOC\_SERIES\_GD32F3X0) || \

110 defined(CONFIG\_SOC\_SERIES\_GD32A50X) || \

111 defined(CONFIG\_SOC\_SERIES\_GD32L23X)

113#define GD32\_OSPEED\_10MHZ 1U

115#define GD32\_OSPEED\_50MHZ 3U

116#else

118#define GD32\_OSPEED\_25MHZ 1U

120#define GD32\_OSPEED\_50MHZ 2U

122#define GD32\_OSPEED\_MAX 3U

123#endif

124

125#else /\* CONFIG\_PINCTRL\_GD32\_AF \*/

[ 127](pinctrl__soc__gd32__common_8h.md#a9ebb7800a833966707ae14cf62b8acce)#define GD32\_OSPEED\_10MHZ 0U

[ 129](pinctrl__soc__gd32__common_8h.md#aac13ae160bc3d73661a4b8ca100cb013)#define GD32\_OSPEED\_2MHZ 1U

[ 131](pinctrl__soc__gd32__common_8h.md#a177ba012fcf27e7a635f1148a63dd51c)#define GD32\_OSPEED\_50MHZ 2U

[ 133](pinctrl__soc__gd32__common_8h.md#a93145148efe045ec2df4ecebb91ebd8d)#define GD32\_OSPEED\_MAX 3U

134#endif /\* CONFIG\_PINCTRL\_GD32\_AF \*/

135

137

150

[ 152](pinctrl__soc__gd32__common_8h.md#aaf70ca09229da5704f8178fd12587efc)#define GD32\_PUPD\_MSK 0x3U

[ 154](pinctrl__soc__gd32__common_8h.md#a57dc4bab7677e156ba09bbb655135104)#define GD32\_PUPD\_POS 29U

[ 156](pinctrl__soc__gd32__common_8h.md#a76f8f5d1fe9a6e255463918e3865d616)#define GD32\_OTYPE\_MSK 0x1U

[ 158](pinctrl__soc__gd32__common_8h.md#a5bb9edb771fae4128fa78e1743d73c70)#define GD32\_OTYPE\_POS 28U

[ 160](pinctrl__soc__gd32__common_8h.md#a7f8504427d9138b30b600f023cd653e3)#define GD32\_OSPEED\_MSK 0x3U

[ 162](pinctrl__soc__gd32__common_8h.md#a9662e875d2fea130c2027a3b0d84e4ef)#define GD32\_OSPEED\_POS 26U

163

165

[ 171](pinctrl__soc__gd32__common_8h.md#aa92c3af616f86950a0c2182670532f60)#define GD32\_PUPD\_GET(pincfg) \

172 (((pincfg) >> GD32\_PUPD\_POS) & GD32\_PUPD\_MSK)

173

[ 179](pinctrl__soc__gd32__common_8h.md#ab818f40b6797fdcbcaec0e8e60a81479)#define GD32\_OTYPE\_GET(pincfg) \

180 (((pincfg) >> GD32\_OTYPE\_POS) & GD32\_OTYPE\_MSK)

181

[ 187](pinctrl__soc__gd32__common_8h.md#a786b5e81f3643ffcc0f27bbbe467401b)#define GD32\_OSPEED\_GET(pincfg) \

188 (((pincfg) >> GD32\_OSPEED\_POS) & GD32\_OSPEED\_MSK)

189

190#ifdef \_\_cplusplus

191}

192#endif

193

194#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_PINCTRL\_SOC\_GD32\_COMMON\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl](dir_c0bb3bf986f9412b3a6b9d85dc06c157.md)
- [pinctrl\_soc\_gd32\_common.h](pinctrl__soc__gd32__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
