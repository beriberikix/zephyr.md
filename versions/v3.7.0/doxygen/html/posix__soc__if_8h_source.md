---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/posix__soc__if_8h_source.html
original_path: doxygen/html/posix__soc__if_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

posix\_soc\_if.h

[Go to the documentation of this file.](posix__soc__if_8h.md)

1/\*

2 \* Copyright (c) 2017 Oticon A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_POSIX\_POSIX\_SOC\_IF\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_POSIX\_POSIX\_SOC\_IF\_H\_

8

9/\*

10 \* This file lists the functions the POSIX architecture core expects the

11 \* SOC or board will provide

12 \*

13 \* All functions listed here must be provided by the implementation of the SOC

14 \* or all its boards

15 \*/

16

17#include <[zephyr/arch/posix/posix\_trace.h](posix__trace_8h.md)>

18#include "soc\_irq.h" /\* Must exist and define \_ARCH\_IRQ/ISR\_\* macros \*/

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](posix__soc__if_8h.md#a924db5712e0c7e6b3595dfc723281329)void [posix\_halt\_cpu](posix__soc__if_8h.md#a924db5712e0c7e6b3595dfc723281329)(void);

[ 25](posix__soc__if_8h.md#a400f264c1c3a8838c589577b287d42a0)void [posix\_atomic\_halt\_cpu](posix__soc__if_8h.md#a400f264c1c3a8838c589577b287d42a0)(unsigned int imask);

26

[ 27](posix__soc__if_8h.md#a05199832c06ba854431bbdbfe2302918)void [posix\_irq\_enable](posix__soc__if_8h.md#a05199832c06ba854431bbdbfe2302918)(unsigned int irq);

[ 28](posix__soc__if_8h.md#a2d1cbc3efb24d49b151ad9506e1132c7)void [posix\_irq\_disable](posix__soc__if_8h.md#a2d1cbc3efb24d49b151ad9506e1132c7)(unsigned int irq);

[ 29](posix__soc__if_8h.md#ad2d42fd9f28c04e0b37c4f34ed0dd711)int [posix\_irq\_is\_enabled](posix__soc__if_8h.md#ad2d42fd9f28c04e0b37c4f34ed0dd711)(unsigned int irq);

[ 30](posix__soc__if_8h.md#a53106413853e29d1eeebbf1b5c4d36a5)unsigned int [posix\_irq\_lock](posix__soc__if_8h.md#a53106413853e29d1eeebbf1b5c4d36a5)(void);

[ 31](posix__soc__if_8h.md#abf80b27ff517e32514e952c53e6c67c6)void [posix\_irq\_unlock](posix__soc__if_8h.md#abf80b27ff517e32514e952c53e6c67c6)(unsigned int key);

[ 32](posix__soc__if_8h.md#a18ad9bcd5676c282e5527e746550dfbb)void [posix\_irq\_full\_unlock](posix__soc__if_8h.md#a18ad9bcd5676c282e5527e746550dfbb)(void);

[ 33](posix__soc__if_8h.md#af6eefac1419bea5bca9a3c1ce48bcf0e)int [posix\_get\_current\_irq](posix__soc__if_8h.md#af6eefac1419bea5bca9a3c1ce48bcf0e)(void);

[ 34](posix__soc__if_8h.md#a8aa652da8beecd80c6036e1ad6f8fddd)void [posix\_sw\_set\_pending\_IRQ](posix__soc__if_8h.md#a8aa652da8beecd80c6036e1ad6f8fddd)(unsigned int IRQn);

[ 35](posix__soc__if_8h.md#aa26107cfff573cc9028b321a62684c46)void [posix\_sw\_clear\_pending\_IRQ](posix__soc__if_8h.md#aa26107cfff573cc9028b321a62684c46)(unsigned int IRQn);

36#ifdef CONFIG\_IRQ\_OFFLOAD

37void posix\_irq\_offload(void (\*routine)(const void \*), const void \*parameter);

38#endif

39

40#ifdef \_\_cplusplus

41}

42#endif

43

44#endif /\* ZEPHYR\_INCLUDE\_ARCH\_POSIX\_POSIX\_SOC\_IF\_H\_ \*/

[posix\_irq\_enable](posix__soc__if_8h.md#a05199832c06ba854431bbdbfe2302918)

void posix\_irq\_enable(unsigned int irq)

[posix\_irq\_full\_unlock](posix__soc__if_8h.md#a18ad9bcd5676c282e5527e746550dfbb)

void posix\_irq\_full\_unlock(void)

[posix\_irq\_disable](posix__soc__if_8h.md#a2d1cbc3efb24d49b151ad9506e1132c7)

void posix\_irq\_disable(unsigned int irq)

[posix\_atomic\_halt\_cpu](posix__soc__if_8h.md#a400f264c1c3a8838c589577b287d42a0)

void posix\_atomic\_halt\_cpu(unsigned int imask)

[posix\_irq\_lock](posix__soc__if_8h.md#a53106413853e29d1eeebbf1b5c4d36a5)

unsigned int posix\_irq\_lock(void)

[posix\_sw\_set\_pending\_IRQ](posix__soc__if_8h.md#a8aa652da8beecd80c6036e1ad6f8fddd)

void posix\_sw\_set\_pending\_IRQ(unsigned int IRQn)

[posix\_halt\_cpu](posix__soc__if_8h.md#a924db5712e0c7e6b3595dfc723281329)

void posix\_halt\_cpu(void)

[posix\_sw\_clear\_pending\_IRQ](posix__soc__if_8h.md#aa26107cfff573cc9028b321a62684c46)

void posix\_sw\_clear\_pending\_IRQ(unsigned int IRQn)

[posix\_irq\_unlock](posix__soc__if_8h.md#abf80b27ff517e32514e952c53e6c67c6)

void posix\_irq\_unlock(unsigned int key)

[posix\_irq\_is\_enabled](posix__soc__if_8h.md#ad2d42fd9f28c04e0b37c4f34ed0dd711)

int posix\_irq\_is\_enabled(unsigned int irq)

[posix\_get\_current\_irq](posix__soc__if_8h.md#af6eefac1419bea5bca9a3c1ce48bcf0e)

int posix\_get\_current\_irq(void)

[posix\_trace.h](posix__trace_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [posix](dir_2eaa0886f2679378503a1f6e740c4205.md)
- [posix\_soc\_if.h](posix__soc__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
