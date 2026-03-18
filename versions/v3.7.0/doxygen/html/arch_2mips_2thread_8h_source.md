---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2mips_2thread_8h_source.html
original_path: doxygen/html/arch_2mips_2thread_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2mips_2thread_8h.md)

1/\*

2 \* Copyright (c) 2020 Antony Pavlov <antonynpavlov@gmail.com>

3 \*

4 \* based on include/arch/riscv/thread.h

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

20

21#ifndef ZEPHYR\_INCLUDE\_ARCH\_MIPS\_THREAD\_H\_

22#define ZEPHYR\_INCLUDE\_ARCH\_MIPS\_THREAD\_H\_

23

24#ifndef \_ASMLANGUAGE

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26

27/\*

28 \* The following structure defines the list of registers that need to be

29 \* saved/restored when a cooperative context switch occurs.

30 \*/

31struct \_callee\_saved {

32 unsigned long sp; /\* Stack pointer \*/

33

34 unsigned long s0; /\* saved register \*/

35 unsigned long s1; /\* saved register \*/

36 unsigned long s2; /\* saved register \*/

37 unsigned long s3; /\* saved register \*/

38 unsigned long s4; /\* saved register \*/

39 unsigned long s5; /\* saved register \*/

40 unsigned long s6; /\* saved register \*/

41 unsigned long s7; /\* saved register \*/

42 unsigned long s8; /\* saved register AKA fp \*/

43};

44typedef struct \_callee\_saved \_callee\_saved\_t;

45

46struct \_thread\_arch {

47 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) swap\_return\_value; /\* Return value of z\_swap() \*/

48};

49

50typedef struct \_thread\_arch \_thread\_arch\_t;

51

52#endif /\* \_ASMLANGUAGE \*/

53

54#endif /\* ZEPHYR\_INCLUDE\_ARCH\_MIPS\_THREAD\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [mips](dir_fc8c8ea71cc5b300c3fa15bb05243853.md)
- [thread.h](arch_2mips_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
