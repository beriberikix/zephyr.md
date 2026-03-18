---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/intel-ioapic_8h_source.html
original_path: doxygen/html/intel-ioapic_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intel-ioapic.h

[Go to the documentation of this file.](intel-ioapic_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_INTEL\_IOAPIC\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_INTEL\_IOAPIC\_H\_

8

[ 9](intel-ioapic_8h.md#a296e915831223a614a6ea87dbe7735e7)#define IRQ\_TYPE\_LEVEL 0x00008000

[ 10](intel-ioapic_8h.md#aff68b0efbc719bc28f0d56c9ba8607bc)#define IRQ\_TYPE\_EDGE 0x00000000

[ 11](intel-ioapic_8h.md#a76dfa18a4a8be7f8b930115b7a9ffc93)#define IRQ\_TYPE\_LOW 0x00002000

[ 12](intel-ioapic_8h.md#aeb89171ec61787d7a3ced80b30af4359)#define IRQ\_TYPE\_HIGH 0x00000000

[ 13](intel-ioapic_8h.md#a0c6b1b5a78c465e429a9a5633601d231)#define IRQ\_DELIVERY\_LOWEST 0x00000100

[ 14](intel-ioapic_8h.md#a19034e9b2fe534947855ad074cd5962b)#define IRQ\_DELIVERY\_FIXED 0x00000000

15

16/\*

17 \* for most device interrupts, lowest priority delivery is preferred

18 \* since this ensures only one CPU gets the interrupt in SMP systems.

19 \*/

[ 20](intel-ioapic_8h.md#a980bab4b0502b138f5fa8af9ca9833b4)#define IRQ\_TYPE\_LOWEST\_EDGE\_RISING (IRQ\_DELIVERY\_LOWEST | IRQ\_TYPE\_EDGE | IRQ\_TYPE\_HIGH)

[ 21](intel-ioapic_8h.md#a5a136f30dc5cb9f1b696751903b3fadd)#define IRQ\_TYPE\_LOWEST\_EDGE\_FALLING (IRQ\_DELIVERY\_LOWEST | IRQ\_TYPE\_EDGE | IRQ\_TYPE\_LOW)

[ 22](intel-ioapic_8h.md#a9083a377fa943731dc24733933bae5d6)#define IRQ\_TYPE\_LOWEST\_LEVEL\_HIGH (IRQ\_DELIVERY\_LOWEST | IRQ\_TYPE\_LEVEL | IRQ\_TYPE\_HIGH)

[ 23](intel-ioapic_8h.md#a15c26d56a818f5340c36117a429282a8)#define IRQ\_TYPE\_LOWEST\_LEVEL\_LOW (IRQ\_DELIVERY\_LOWEST | IRQ\_TYPE\_LEVEL | IRQ\_TYPE\_LOW)

24

25/\* for interrupts that want to be delivered to all CPUs, e.g. HPET \*/

[ 26](intel-ioapic_8h.md#af1a9700940385a6aa6c9ff93fa834436)#define IRQ\_TYPE\_FIXED\_EDGE\_RISING (IRQ\_DELIVERY\_FIXED | IRQ\_TYPE\_EDGE | IRQ\_TYPE\_HIGH)

[ 27](intel-ioapic_8h.md#a7f62c57495f357ec336cba12f1a12d61)#define IRQ\_TYPE\_FIXED\_EDGE\_FALLING (IRQ\_DELIVERY\_FIXED | IRQ\_TYPE\_EDGE | IRQ\_TYPE\_LOW)

[ 28](intel-ioapic_8h.md#a9a2bb018c589784edf36b204ba2daf48)#define IRQ\_TYPE\_FIXED\_LEVEL\_HIGH (IRQ\_DELIVERY\_FIXED | IRQ\_TYPE\_LEVEL | IRQ\_TYPE\_HIGH)

[ 29](intel-ioapic_8h.md#ab570a690df9e89e8a38e257ce32e9801)#define IRQ\_TYPE\_FIXED\_LEVEL\_LOW (IRQ\_DELIVERY\_FIXED | IRQ\_TYPE\_LEVEL | IRQ\_TYPE\_LOW)

30

31#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [intel-ioapic.h](intel-ioapic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
