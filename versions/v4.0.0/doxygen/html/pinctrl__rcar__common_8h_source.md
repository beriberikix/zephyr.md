---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pinctrl__rcar__common_8h_source.html
original_path: doxygen/html/pinctrl__rcar__common_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_rcar\_common.h

[Go to the documentation of this file.](pinctrl__rcar__common_8h.md)

1/\*

2 \* Copyright (c) 2023 IoT.bzh

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*

6 \*/

7

8#ifndef ZEPHYR\_SOC\_ARM\_RENESAS\_RCAR\_COMMON\_PINCTRL\_SOC\_H\_

9#define ZEPHYR\_SOC\_ARM\_RENESAS\_RCAR\_COMMON\_PINCTRL\_SOC\_H\_

10

11#include <[zephyr/devicetree.h](devicetree_8h.md)>

12#include <[zephyr/dt-bindings/pinctrl/renesas/pinctrl-rcar-common.h](pinctrl-rcar-common_8h.md)>

13#include <[stdint.h](stdint_8h.md)>

14#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

15

[ 16](structrcar__pin__func.md)struct [rcar\_pin\_func](structrcar__pin__func.md) {

[ 17](structrcar__pin__func.md#abc0b9a433a3b0e00da4a5fe733c31c7d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bank](structrcar__pin__func.md#abc0b9a433a3b0e00da4a5fe733c31c7d):5; /\* bank number 0 - 18 \*/

[ 18](structrcar__pin__func.md#acf66a4904ab66054f9f8c0f680157481) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [shift](structrcar__pin__func.md#acf66a4904ab66054f9f8c0f680157481):5; /\* bit shift 0 - 28 \*/

[ 19](structrcar__pin__func.md#aeafc3b430ee3137afdc362027c6b058c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [func](structrcar__pin__func.md#aeafc3b430ee3137afdc362027c6b058c):4; /\* choice from 0x0 to 0xF \*/

20};

21

[ 23](pinctrl__rcar__common_8h.md#a8ac73177e56465acd4376645a2fd89b1)#define RCAR\_PIN\_FLAGS\_PULL\_SET BIT(0)

[ 25](pinctrl__rcar__common_8h.md#acdaea04a569eaec56c706bd311e1cadd)#define RCAR\_PIN\_FLAGS\_PUEN BIT(1)

[ 27](pinctrl__rcar__common_8h.md#a6df27aa417055266a299e964bb92fd44)#define RCAR\_PIN\_FLAGS\_PUD BIT(2)

[ 29](pinctrl__rcar__common_8h.md#aabcc781206d861b19d24bd82ad1150b0)#define RCAR\_PIN\_FLAGS\_FUNC\_SET BIT(3)

[ 31](pinctrl__rcar__common_8h.md#a44b7efa931db5d11e5b7c9cb8a94bbf9)#define RCAR\_PIN\_FLAGS\_FUNC\_DUMMY BIT(4)

32

[ 33](pinctrl__rcar__common_8h.md#a5ac9cbd536534bf5e4edb3b76f0a2f60)#define RCAR\_PIN\_PULL\_UP (RCAR\_PIN\_FLAGS\_PULL\_SET | RCAR\_PIN\_FLAGS\_PUEN | RCAR\_PIN\_FLAGS\_PUD)

[ 34](pinctrl__rcar__common_8h.md#a53d33b579bb9c498fdd09ed9bb35c0e1)#define RCAR\_PIN\_PULL\_DOWN (RCAR\_PIN\_FLAGS\_PULL\_SET | RCAR\_PIN\_FLAGS\_PUEN)

[ 35](pinctrl__rcar__common_8h.md#a6d4c259adbd0cd5fd6065fdd4a57cda7)#define RCAR\_PIN\_PULL\_DISABLE RCAR\_PIN\_FLAGS\_PULL\_SET

36

[ 38](structpinctrl__soc__pin.md)typedef struct [pinctrl\_soc\_pin](structpinctrl__soc__pin.md) {

[ 39](structpinctrl__soc__pin.md#a0a2ceae237c3321a4ce1a3dd7a031322) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pin](structpinctrl__soc__pin.md#a0a2ceae237c3321a4ce1a3dd7a031322);

[ 40](structpinctrl__soc__pin.md#aa1e68145488d654ab03e114c3f9949a9) struct [rcar\_pin\_func](structrcar__pin__func.md) [func](structpinctrl__soc__pin.md#aa1e68145488d654ab03e114c3f9949a9);

[ 41](structpinctrl__soc__pin.md#a8e7c595f1e24e227da45a2b5d5fad501) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structpinctrl__soc__pin.md#a8e7c595f1e24e227da45a2b5d5fad501);

[ 42](structpinctrl__soc__pin.md#a0784ff8fd0192c54997ab5841153c82b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [drive\_strength](structpinctrl__soc__pin.md#a0784ff8fd0192c54997ab5841153c82b);

[ 43](structpinctrl__soc__pin.md#a37e11e6cc80fdd3cedbbbee555e062ae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [voltage](structpinctrl__soc__pin.md#a37e11e6cc80fdd3cedbbbee555e062ae);

[ 44](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d)} [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d);

45

[ 46](pinctrl__rcar__common_8h.md#af89135625acaec60f328c703a7d1823b)#define RCAR\_IPSR(node\_id) DT\_PROP\_BY\_IDX(node\_id, pin, 1)

[ 47](pinctrl__rcar__common_8h.md#a2c260d5b989251d6dc533f835df76772)#define RCAR\_HAS\_IPSR(node\_id) DT\_PROP\_HAS\_IDX(node\_id, pin, 1)

48

49/\* Offsets are defined in dt-bindings pinctrl-rcar-common.h \*/

[ 50](pinctrl__rcar__common_8h.md#a7f0e2d8e2d84035326685c1e2c56d181)#define RCAR\_PIN\_FUNC(node\_id) \

51 { \

52 ((RCAR\_IPSR(node\_id) >> 10U) & 0x1FU), \

53 ((RCAR\_IPSR(node\_id) >> 4U) & 0x1FU), \

54 ((RCAR\_IPSR(node\_id) & 0xFU)) \

55 }

56

[ 57](pinctrl__rcar__common_8h.md#a718e93760aba13e5c883ce133760e197)#define RCAR\_PIN\_IS\_FUNC\_DUMMY(node\_id) \

58 ((((RCAR\_IPSR(node\_id) >> 10U) & 0x1FU) == 0x1F) && \

59 (((RCAR\_IPSR(node\_id) >> 4U) & 0x1FU) == 0x1F) && \

60 ((RCAR\_IPSR(node\_id) & 0xFU) == 0xF))

61

[ 62](pinctrl__rcar__common_8h.md#ab94ca6630b8bddbf7325b5ae01ee969d)#define RCAR\_PIN\_FLAGS(node\_id) \

63 DT\_PROP(node\_id, bias\_pull\_up) \* RCAR\_PIN\_PULL\_UP | \

64 DT\_PROP(node\_id, bias\_pull\_down) \* RCAR\_PIN\_PULL\_DOWN | \

65 DT\_PROP(node\_id, bias\_disable) \* RCAR\_PIN\_PULL\_DISABLE | \

66 RCAR\_HAS\_IPSR(node\_id) \* RCAR\_PIN\_FLAGS\_FUNC\_SET | \

67 RCAR\_PIN\_IS\_FUNC\_DUMMY(node\_id) \* RCAR\_PIN\_FLAGS\_FUNC\_DUMMY

68

[ 69](pinctrl__rcar__common_8h.md#a3f524c2e190008ea866d3e9e114a5f18)#define RCAR\_DT\_PIN(node\_id) \

70 { \

71 .pin = DT\_PROP\_BY\_IDX(node\_id, pin, 0), \

72 .func = COND\_CODE\_1(RCAR\_HAS\_IPSR(node\_id), \

73 (RCAR\_PIN\_FUNC(node\_id)), {0}), \

74 .flags = RCAR\_PIN\_FLAGS(node\_id), \

75 .drive\_strength = \

76 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, drive\_strength), \

77 (DT\_PROP(node\_id, drive\_strength)), (0)), \

78 .voltage = COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, \

79 power\_source), \

80 (DT\_PROP(node\_id, power\_source)), \

81 (PIN\_VOLTAGE\_NONE)), \

82 },

83

91#define Z\_PINCTRL\_STATE\_PIN\_INIT(node\_id, state\_prop, idx) \

92 RCAR\_DT\_PIN(DT\_PROP\_BY\_IDX(node\_id, state\_prop, idx))

93

100#define Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, prop) \

101 { DT\_FOREACH\_PROP\_ELEM(node\_id, prop, Z\_PINCTRL\_STATE\_PIN\_INIT) }

102

[ 103](structpfc__drive__reg__field.md)struct [pfc\_drive\_reg\_field](structpfc__drive__reg__field.md) {

[ 104](structpfc__drive__reg__field.md#a39e89d41227063647a0bbdc881a49b30) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pin](structpfc__drive__reg__field.md#a39e89d41227063647a0bbdc881a49b30);

[ 105](structpfc__drive__reg__field.md#a8cfedc171cbedd9c8dd24930e800c2c1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [offset](structpfc__drive__reg__field.md#a8cfedc171cbedd9c8dd24930e800c2c1);

[ 106](structpfc__drive__reg__field.md#a7d65f9710f1ca64d162e50fc63cbd45c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [size](structpfc__drive__reg__field.md#a7d65f9710f1ca64d162e50fc63cbd45c);

107};

108

[ 109](structpfc__drive__reg.md)struct [pfc\_drive\_reg](structpfc__drive__reg.md) {

[ 110](structpfc__drive__reg.md#ab9ae8bee56ea46c08ede93f67d1c520c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reg](structpfc__drive__reg.md#ab9ae8bee56ea46c08ede93f67d1c520c);

[ 111](structpfc__drive__reg.md#a92e5c3d645c3a1278f6e0b1afed677f4) const struct [pfc\_drive\_reg\_field](structpfc__drive__reg__field.md) [fields](structpfc__drive__reg.md#a92e5c3d645c3a1278f6e0b1afed677f4)[8];

112};

113

[ 114](structpfc__bias__reg.md)struct [pfc\_bias\_reg](structpfc__bias__reg.md) {

[ 115](structpfc__bias__reg.md#af52bea8a971a9d529b88de56a96ba2f6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [puen](structpfc__bias__reg.md#af52bea8a971a9d529b88de56a96ba2f6);

[ 116](structpfc__bias__reg.md#ad5b3f9a184e18852279224bc8bd410f1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pud](structpfc__bias__reg.md#ad5b3f9a184e18852279224bc8bd410f1);

[ 117](structpfc__bias__reg.md#ab3762934173a1c25c7c31ed04694d276) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pins](structpfc__bias__reg.md#ab3762934173a1c25c7c31ed04694d276)[32];

118};

119

[ 126](pinctrl__rcar__common_8h.md#af231b8fe5b02c023bf068b8c7565d4c4)#define RCAR\_IS\_GP\_PIN(pin) (pin < PIN\_NOGPSR\_START)

127

128#endif /\* ZEPHYR\_SOC\_ARM\_RENESAS\_RCAR\_COMMON\_PINCTRL\_SOC\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[pinctrl-rcar-common.h](pinctrl-rcar-common_8h.md)

[pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d)

struct pinctrl\_soc\_pin pinctrl\_soc\_pin\_t

Type for R-Car pin.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[pfc\_bias\_reg](structpfc__bias__reg.md)

**Definition** pinctrl\_rcar\_common.h:114

[pfc\_bias\_reg::pins](structpfc__bias__reg.md#ab3762934173a1c25c7c31ed04694d276)

const uint16\_t pins[32]

Pull-up/down or pull-down control register.

**Definition** pinctrl\_rcar\_common.h:117

[pfc\_bias\_reg::pud](structpfc__bias__reg.md#ad5b3f9a184e18852279224bc8bd410f1)

uint32\_t pud

Pull-enable or pull-up control register.

**Definition** pinctrl\_rcar\_common.h:116

[pfc\_bias\_reg::puen](structpfc__bias__reg.md#af52bea8a971a9d529b88de56a96ba2f6)

uint32\_t puen

**Definition** pinctrl\_rcar\_common.h:115

[pfc\_drive\_reg\_field](structpfc__drive__reg__field.md)

**Definition** pinctrl\_rcar\_common.h:103

[pfc\_drive\_reg\_field::pin](structpfc__drive__reg__field.md#a39e89d41227063647a0bbdc881a49b30)

uint16\_t pin

**Definition** pinctrl\_rcar\_common.h:104

[pfc\_drive\_reg\_field::size](structpfc__drive__reg__field.md#a7d65f9710f1ca64d162e50fc63cbd45c)

uint8\_t size

**Definition** pinctrl\_rcar\_common.h:106

[pfc\_drive\_reg\_field::offset](structpfc__drive__reg__field.md#a8cfedc171cbedd9c8dd24930e800c2c1)

uint8\_t offset

**Definition** pinctrl\_rcar\_common.h:105

[pfc\_drive\_reg](structpfc__drive__reg.md)

**Definition** pinctrl\_rcar\_common.h:109

[pfc\_drive\_reg::fields](structpfc__drive__reg.md#a92e5c3d645c3a1278f6e0b1afed677f4)

const struct pfc\_drive\_reg\_field fields[8]

**Definition** pinctrl\_rcar\_common.h:111

[pfc\_drive\_reg::reg](structpfc__drive__reg.md#ab9ae8bee56ea46c08ede93f67d1c520c)

uint32\_t reg

**Definition** pinctrl\_rcar\_common.h:110

[pinctrl\_soc\_pin](structpinctrl__soc__pin.md)

Type for R-Car pin.

**Definition** pinctrl\_rcar\_common.h:38

[pinctrl\_soc\_pin::drive\_strength](structpinctrl__soc__pin.md#a0784ff8fd0192c54997ab5841153c82b)

uint8\_t drive\_strength

**Definition** pinctrl\_rcar\_common.h:42

[pinctrl\_soc\_pin::pin](structpinctrl__soc__pin.md#a0a2ceae237c3321a4ce1a3dd7a031322)

uint16\_t pin

**Definition** pinctrl\_rcar\_common.h:39

[pinctrl\_soc\_pin::voltage](structpinctrl__soc__pin.md#a37e11e6cc80fdd3cedbbbee555e062ae)

uint8\_t voltage

**Definition** pinctrl\_rcar\_common.h:43

[pinctrl\_soc\_pin::flags](structpinctrl__soc__pin.md#a8e7c595f1e24e227da45a2b5d5fad501)

uint8\_t flags

**Definition** pinctrl\_rcar\_common.h:41

[pinctrl\_soc\_pin::func](structpinctrl__soc__pin.md#aa1e68145488d654ab03e114c3f9949a9)

struct rcar\_pin\_func func

**Definition** pinctrl\_rcar\_common.h:40

[rcar\_pin\_func](structrcar__pin__func.md)

**Definition** pinctrl\_rcar\_common.h:16

[rcar\_pin\_func::bank](structrcar__pin__func.md#abc0b9a433a3b0e00da4a5fe733c31c7d)

uint8\_t bank

**Definition** pinctrl\_rcar\_common.h:17

[rcar\_pin\_func::shift](structrcar__pin__func.md#acf66a4904ab66054f9f8c0f680157481)

uint8\_t shift

**Definition** pinctrl\_rcar\_common.h:18

[rcar\_pin\_func::func](structrcar__pin__func.md#aeafc3b430ee3137afdc362027c6b058c)

uint8\_t func

**Definition** pinctrl\_rcar\_common.h:19

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl](dir_c0bb3bf986f9412b3a6b9d85dc06c157.md)
- [pinctrl\_rcar\_common.h](pinctrl__rcar__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
