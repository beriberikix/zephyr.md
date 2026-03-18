---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2nios2_2thread_8h_source.html
original_path: doxygen/html/arch_2nios2_2thread_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2nios2_2thread_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

18

19#ifndef ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_THREAD\_H\_

20#define ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_THREAD\_H\_

21

22#ifndef \_ASMLANGUAGE

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24

25struct \_callee\_saved {

26 /\* General purpose callee-saved registers \*/

27 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r16;

28 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r17;

29 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r18;

30 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r19;

31 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r20;

32 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r21;

33 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r22;

34 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r23;

35

36 /\* Normally used for the frame pointer but also a general purpose

37 \* register if frame pointers omitted

38 \*/

39 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r28;

40

41 /\* Return address \*/

42 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ra;

43

44 /\* Stack pointer \*/

45 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sp;

46

47 /\* IRQ status before irq\_lock() and call to z\_swap() \*/

48 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) key;

49

50 /\* Return value of z\_swap() \*/

51 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retval;

52};

53

54typedef struct \_callee\_saved \_callee\_saved\_t;

55

56struct \_thread\_arch {

57 /\* nothing for now \*/

58};

59

60typedef struct \_thread\_arch \_thread\_arch\_t;

61

62#endif /\* \_ASMLANGUAGE \*/

63

64#endif /\* ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_THREAD\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [nios2](dir_bcfa142ae77c1ee311b7ef8e30037d11.md)
- [thread.h](arch_2nios2_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
