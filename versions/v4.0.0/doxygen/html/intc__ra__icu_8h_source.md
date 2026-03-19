---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/intc__ra__icu_8h_source.html
original_path: doxygen/html/intc__ra__icu_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_ra\_icu.h

[Go to the documentation of this file.](intc__ra__icu_8h.md)

1/\*

2 \* Copyright (c) 2023 TOKITA Hiroshi <tokita.hiroshi@fujitsu.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/dt-bindings/interrupt-controller/renesas-ra-icu.h](renesas-ra-icu_8h.md)>

8

9#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RA\_ICU\_H\_

[ 10](intc__ra__icu_8h.md#a28f51943d0ae322da596758f4134a7b6)#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RA\_ICU\_H\_

11

[ 12](intc__ra__icu_8h.md#a1811342f456c5d4ea6d84b22fabb6c91)#define RA\_ICU\_FLAG\_EVENT\_OFFSET 8

[ 13](intc__ra__icu_8h.md#a1e1233fb119146e36c549b816f6b495a)#define RA\_ICU\_FLAG\_EVENT\_MASK (BIT\_MASK(8) << RA\_ICU\_FLAG\_EVENT\_OFFSET)

[ 14](intc__ra__icu_8h.md#add34bc98468f4e6dd02308b5a285d8e7)#define RA\_ICU\_FLAG\_INTCFG\_OFFSET 16

[ 15](intc__ra__icu_8h.md#a3956755910b2fb1bcb1e0fe747853b4d)#define RA\_ICU\_FLAG\_INTCFG\_MASK (BIT\_MASK(8) << RA\_ICU\_FLAG\_INTCFG\_OFFSET)

16

[ 17](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207e)enum [icu\_irq\_mode](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207e) {

[ 18](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432) [ICU\_FALLING](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432),

[ 19](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3) [ICU\_RISING](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3),

[ 20](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650) [ICU\_BOTH\_EDGE](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650),

[ 21](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4) [ICU\_LOW\_LEVEL](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4),

22};

23

[ 24](intc__ra__icu_8h.md#aebf359fac4cee1cc97b3ef726fb2c8b9)typedef void (\*[ra\_isr\_handler](intc__ra__icu_8h.md#aebf359fac4cee1cc97b3ef726fb2c8b9))(const void \*);

25

[ 26](intc__ra__icu_8h.md#a10a9501f6a1e51173851ebc569d50ecb)extern void [ra\_icu\_clear\_int\_flag](intc__ra__icu_8h.md#a10a9501f6a1e51173851ebc569d50ecb)(unsigned int irqn);

27

[ 28](intc__ra__icu_8h.md#a012a14c9b65ef744eed4c854d5376e07)extern int [ra\_icu\_query\_available\_irq](intc__ra__icu_8h.md#a012a14c9b65ef744eed4c854d5376e07)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event);

[ 29](intc__ra__icu_8h.md#ad2f7c4299dced5b919bcc310abea17bd)extern int [ra\_icu\_query\_exists\_irq](intc__ra__icu_8h.md#ad2f7c4299dced5b919bcc310abea17bd)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event);

30

[ 31](intc__ra__icu_8h.md#af30844ef3589626f9e200f11c821c07e)extern void [ra\_icu\_query\_irq\_config](intc__ra__icu_8h.md#af30844ef3589626f9e200f11c821c07e)(unsigned int irq, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*intcfg, [ra\_isr\_handler](intc__ra__icu_8h.md#aebf359fac4cee1cc97b3ef726fb2c8b9) \*pisr,

32 const void \*\*cbarg);

33

[ 34](intc__ra__icu_8h.md#ad854b5c872869e0d982f8af4279ae81f)extern int [ra\_icu\_irq\_connect\_dynamic](intc__ra__icu_8h.md#ad854b5c872869e0d982f8af4279ae81f)(unsigned int irq, unsigned int priority,

35 void (\*routine)(const void \*parameter), const void \*parameter,

36 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

37

[ 38](intc__ra__icu_8h.md#aba7fd8b061cc37d1525bf07b6aeae2f1)extern int [ra\_icu\_irq\_disconnect\_dynamic](intc__ra__icu_8h.md#aba7fd8b061cc37d1525bf07b6aeae2f1)(unsigned int irq, unsigned int priority,

39 void (\*routine)(const void \*parameter),

40 const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

41

42#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RA\_ICU\_H\_ \*/

[ra\_icu\_query\_available\_irq](intc__ra__icu_8h.md#a012a14c9b65ef744eed4c854d5376e07)

int ra\_icu\_query\_available\_irq(uint32\_t event)

[ra\_icu\_clear\_int\_flag](intc__ra__icu_8h.md#a10a9501f6a1e51173851ebc569d50ecb)

void ra\_icu\_clear\_int\_flag(unsigned int irqn)

[ra\_icu\_irq\_disconnect\_dynamic](intc__ra__icu_8h.md#aba7fd8b061cc37d1525bf07b6aeae2f1)

int ra\_icu\_irq\_disconnect\_dynamic(unsigned int irq, unsigned int priority, void(\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)

[ra\_icu\_query\_exists\_irq](intc__ra__icu_8h.md#ad2f7c4299dced5b919bcc310abea17bd)

int ra\_icu\_query\_exists\_irq(uint32\_t event)

[ra\_icu\_irq\_connect\_dynamic](intc__ra__icu_8h.md#ad854b5c872869e0d982f8af4279ae81f)

int ra\_icu\_irq\_connect\_dynamic(unsigned int irq, unsigned int priority, void(\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)

[icu\_irq\_mode](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207e)

icu\_irq\_mode

**Definition** intc\_ra\_icu.h:17

[ICU\_RISING](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3)

@ ICU\_RISING

**Definition** intc\_ra\_icu.h:19

[ICU\_BOTH\_EDGE](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650)

@ ICU\_BOTH\_EDGE

**Definition** intc\_ra\_icu.h:20

[ICU\_LOW\_LEVEL](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4)

@ ICU\_LOW\_LEVEL

**Definition** intc\_ra\_icu.h:21

[ICU\_FALLING](intc__ra__icu_8h.md#aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432)

@ ICU\_FALLING

**Definition** intc\_ra\_icu.h:18

[ra\_isr\_handler](intc__ra__icu_8h.md#aebf359fac4cee1cc97b3ef726fb2c8b9)

void(\* ra\_isr\_handler)(const void \*)

**Definition** intc\_ra\_icu.h:24

[ra\_icu\_query\_irq\_config](intc__ra__icu_8h.md#af30844ef3589626f9e200f11c821c07e)

void ra\_icu\_query\_irq\_config(unsigned int irq, uint32\_t \*intcfg, ra\_isr\_handler \*pisr, const void \*\*cbarg)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[renesas-ra-icu.h](renesas-ra-icu_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_ra\_icu.h](intc__ra__icu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
