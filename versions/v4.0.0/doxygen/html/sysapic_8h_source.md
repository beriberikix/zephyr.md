---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sysapic_8h_source.html
original_path: doxygen/html/sysapic_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sysapic.h

[Go to the documentation of this file.](sysapic_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SYSAPIC\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SYSAPIC\_H\_

9

10#include <[zephyr/drivers/interrupt\_controller/loapic.h](loapic_8h.md)>

11

[ 12](sysapic_8h.md#afffc88f34c930a5af21baadb445f9c71)#define IRQ\_TRIGGER\_EDGE IOAPIC\_EDGE

[ 13](sysapic_8h.md#afa859e1b2648a338573252756f6df69b)#define IRQ\_TRIGGER\_LEVEL IOAPIC\_LEVEL

14

[ 15](sysapic_8h.md#a1f706a68a6c632a0a3ad761eaa0092ee)#define IRQ\_POLARITY\_HIGH IOAPIC\_HIGH

[ 16](sysapic_8h.md#a90a856442e76f43799d24ca853d8a04b)#define IRQ\_POLARITY\_LOW IOAPIC\_LOW

17

18#ifndef \_ASMLANGUAGE

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20

[ 21](sysapic_8h.md#ad0fac43b50900ad4e2b2d1e1876fc36d)#define LOAPIC\_IRQ\_COUNT 6 /\* Default to LOAPIC\_TIMER to LOAPIC\_ERROR \*/

22

23void z\_irq\_controller\_irq\_config(unsigned int vector, unsigned int irq,

24 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

25

26int z\_irq\_controller\_isr\_vector\_get(void);

27

28static inline void z\_irq\_controller\_eoi(void)

29{

30 [x86\_write\_loapic](loapic_8h.md#a884390389c9c7cef65801bba00395e4d)([LOAPIC\_EOI](loapic_8h.md#a5cc8ffe88a717189312314661d489e52), 0);

31}

32

33#endif /\* \_ASMLANGUAGE \*/

34

35#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SYSAPIC\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[loapic.h](loapic_8h.md)

[LOAPIC\_EOI](loapic_8h.md#a5cc8ffe88a717189312314661d489e52)

#define LOAPIC\_EOI

**Definition** loapic.h:23

[x86\_write\_loapic](loapic_8h.md#a884390389c9c7cef65801bba00395e4d)

static void x86\_write\_loapic(unsigned int reg, uint32\_t val)

Write 32-bit value to the local APIC using the default mode.

**Definition** loapic.h:147

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [sysapic.h](sysapic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
