---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ioapic_8h_source.html
original_path: doxygen/html/ioapic_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ioapic.h

[Go to the documentation of this file.](ioapic_8h.md)

1/\* ioapic.h - public IOAPIC APIs \*/

2

3/\*

4 \* Copyright (c) 2012-2015 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_IOAPIC\_H\_

10#define ZEPHYR\_INCLUDE\_DRIVERS\_IOAPIC\_H\_

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16/\*

17 \* Redirection table entry bits: lower 32 bit

18 \* Used as flags argument in ioapic\_irq\_set

19 \*/

20

[ 21](ioapic_8h.md#afe15b2cc2000b86362e9fb0026ec4f32)#define IOAPIC\_INT\_MASK 0x00010000

[ 22](ioapic_8h.md#ac66c78294836c1327cbbf6bd5111282a)#define IOAPIC\_TRIGGER\_MASK 0x00008000

[ 23](ioapic_8h.md#afee8dca23363d2f9b785a21f6b5c4080)#define IOAPIC\_LEVEL 0x00008000

[ 24](ioapic_8h.md#a1d4cfd6f7d4aba0bc773e4d53333bb1d)#define IOAPIC\_EDGE 0x00000000

[ 25](ioapic_8h.md#a850d24fefdc5a1b0f92922a504eb43b5)#define IOAPIC\_REMOTE 0x00004000

[ 26](ioapic_8h.md#a3d009fe11441cfd8ad68f91d764f447e)#define IOAPIC\_POLARITY\_MASK 0x00002000

[ 27](ioapic_8h.md#a23ec31db6b36b64ad0d04c3caf2815f2)#define IOAPIC\_LOW 0x00002000

[ 28](ioapic_8h.md#a1677a4eb3aab3bea022e9ea2bf547888)#define IOAPIC\_HIGH 0x00000000

[ 29](ioapic_8h.md#af9cdfb74e72ef22f3c51f7b9a8b3afe9)#define IOAPIC\_LOGICAL 0x00000800

[ 30](ioapic_8h.md#aa4ef248efabc134ecad5f00fa34fa456)#define IOAPIC\_PHYSICAL 0x00000000

[ 31](ioapic_8h.md#a1d1756d4b243d2235d58ffa2caf4e5fc)#define IOAPIC\_DELIVERY\_MODE\_MASK 0x00000700

[ 32](ioapic_8h.md#af84ed8737d1822ded039bb975b8f5bc9)#define IOAPIC\_FIXED 0x00000000

[ 33](ioapic_8h.md#add788ae14ffab1b56a831c2a39d2a617)#define IOAPIC\_LOWEST 0x00000100

[ 34](ioapic_8h.md#aa01949d30064c45959fdfefcedd916f1)#define IOAPIC\_SMI 0x00000200

[ 35](ioapic_8h.md#a3e2f1930e2f92cff455b98b76c6c4397)#define IOAPIC\_NMI 0x00000400

[ 36](ioapic_8h.md#a16099bc753e03fdf31f6aa35f01cf2fa)#define IOAPIC\_INIT 0x00000500

[ 37](ioapic_8h.md#aeff81f0a6186d2b188c7109baa670c52)#define IOAPIC\_EXTINT 0x00000700

38

39#ifndef \_ASMLANGUAGE

40[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_ioapic\_num\_rtes(void);

41void z\_ioapic\_irq\_enable(unsigned int irq);

42void z\_ioapic\_irq\_disable(unsigned int irq);

43void z\_ioapic\_int\_vec\_set(unsigned int irq, unsigned int vector);

44void z\_ioapic\_irq\_set(unsigned int irq, unsigned int vector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

45#endif /\* \_ASMLANGUAGE \*/

46

47#ifdef \_\_cplusplus

48}

49#endif

50

51#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_IOAPIC\_H\_ \*/

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [ioapic.h](ioapic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
