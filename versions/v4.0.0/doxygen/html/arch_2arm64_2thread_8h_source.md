---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2arm64_2thread_8h_source.html
original_path: doxygen/html/arch_2arm64_2thread_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2arm64_2thread_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

18

19#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_THREAD\_H\_

20#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_THREAD\_H\_

21

22#ifndef \_ASMLANGUAGE

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24#include <[zephyr/arch/arm64/mm.h](arch_2arm64_2mm_8h.md)>

25

26struct \_callee\_saved {

27 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x19;

28 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x20;

29 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x21;

30 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x22;

31 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x23;

32 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x24;

33 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x25;

34 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x26;

35 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x27;

36 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x28;

37 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x29;

38 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sp\_el0;

39 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sp\_elx;

40 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) lr;

41};

42

43typedef struct \_callee\_saved \_callee\_saved\_t;

44

45struct z\_arm64\_fp\_context {

46 \_\_int128 q0, q1, q2, q3, q4, q5, q6, q7;

47 \_\_int128 q8, q9, q10, q11, q12, q13, q14, q15;

48 \_\_int128 q16, q17, q18, q19, q20, q21, q22, q23;

49 \_\_int128 q24, q25, q26, q27, q28, q29, q30, q31;

50 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fpsr, fpcr;

51};

52

53struct \_thread\_arch {

54#if defined(CONFIG\_USERSPACE) || defined(CONFIG\_ARM64\_STACK\_PROTECTION)

55#if defined(CONFIG\_ARM\_MMU)

56 struct arm\_mmu\_ptables \*ptables;

57#endif

58#if defined(CONFIG\_ARM\_MPU)

59 struct dynamic\_region\_info regions[[ARM64\_MPU\_MAX\_DYNAMIC\_REGIONS](4_2cortex__r_2arm__mpu_8h.md#a6e954e6d9c6117210d857b360bf5fa51)];

60 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) region\_num;

61 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) flushing;

62#endif

63#endif

64#ifdef CONFIG\_ARM64\_SAFE\_EXCEPTION\_STACK

65 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) stack\_limit;

66#endif

67#ifdef CONFIG\_FPU\_SHARING

68 struct z\_arm64\_fp\_context saved\_fp\_context;

69#endif

70 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) exception\_depth;

71};

72

73typedef struct \_thread\_arch \_thread\_arch\_t;

74

75#endif /\* \_ASMLANGUAGE \*/

76

77#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_THREAD\_H\_ \*/

[ARM64\_MPU\_MAX\_DYNAMIC\_REGIONS](4_2cortex__r_2arm__mpu_8h.md#a6e954e6d9c6117210d857b360bf5fa51)

#define ARM64\_MPU\_MAX\_DYNAMIC\_REGIONS

**Definition** arm\_mpu.h:256

[mm.h](arch_2arm64_2mm_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [thread.h](arch_2arm64_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
