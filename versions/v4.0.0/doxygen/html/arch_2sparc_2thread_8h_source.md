---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2sparc_2thread_8h_source.html
original_path: doxygen/html/arch_2sparc_2thread_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2sparc_2thread_8h.md)

1/\*

2 \* Copyright (c) 2019-2020 Cobham Gaisler AB

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

18

19#ifndef ZEPHYR\_INCLUDE\_ARCH\_SPARC\_THREAD\_H\_

20#define ZEPHYR\_INCLUDE\_ARCH\_SPARC\_THREAD\_H\_

21

22#ifndef \_ASMLANGUAGE

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24

25/\*

26 \* The following structure defines the list of registers that need to be

27 \* saved/restored when a cooperative context switch occurs.

28 \*/

29struct \_callee\_saved {

30 /\* y register used by mul/div \*/

31 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) y;

32

33 /\* processor status register \*/

34 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) psr;

35

36 /\*

37 \* local registers

38 \*

39 \* Using uint64\_t l0\_and\_l1 will put everything in this structure on a

40 \* double word boundary which allows us to use double word loads and

41 \* stores safely in the context switch.

42 \*/

43 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) l0\_and\_l1;

44 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) l2;

45 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) l3;

46 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) l4;

47 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) l5;

48 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) l6;

49 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) l7;

50

51 /\* input registers \*/

52 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i0;

53 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i1;

54 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i2;

55 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i3;

56 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i4;

57 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i5;

58 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i6; /\* frame pointer \*/

59 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i7;

60

61 /\* output registers \*/

62 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) o6; /\* stack pointer \*/

63 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) o7;

64

65};

66typedef struct \_callee\_saved \_callee\_saved\_t;

67

68struct \_thread\_arch {

69 /\* empty \*/

70};

71

72typedef struct \_thread\_arch \_thread\_arch\_t;

73

74#endif /\* \_ASMLANGUAGE \*/

75

76#endif /\* ZEPHYR\_INCLUDE\_ARCH\_SPARC\_THREAD\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [sparc](dir_0b6b538994b3c7630127059eac21a61b.md)
- [thread.h](arch_2sparc_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
