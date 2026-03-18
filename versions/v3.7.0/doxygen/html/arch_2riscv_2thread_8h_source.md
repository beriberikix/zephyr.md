---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2riscv_2thread_8h_source.html
original_path: doxygen/html/arch_2riscv_2thread_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2riscv_2thread_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

18

19#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_THREAD\_H\_

20#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_THREAD\_H\_

21

22#ifndef \_ASMLANGUAGE

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24

25/\*

26 \* The following structure defines the list of registers that need to be

27 \* saved/restored when a context switch occurs.

28 \*/

29struct \_callee\_saved {

30 unsigned long sp; /\* Stack pointer, (x2 register) \*/

31 unsigned long ra; /\* return address \*/

32

33 unsigned long s0; /\* saved register/frame pointer \*/

34 unsigned long s1; /\* saved register \*/

35#if !defined(CONFIG\_RISCV\_ISA\_RV32E)

36 unsigned long s2; /\* saved register \*/

37 unsigned long s3; /\* saved register \*/

38 unsigned long s4; /\* saved register \*/

39 unsigned long s5; /\* saved register \*/

40 unsigned long s6; /\* saved register \*/

41 unsigned long s7; /\* saved register \*/

42 unsigned long s8; /\* saved register \*/

43 unsigned long s9; /\* saved register \*/

44 unsigned long s10; /\* saved register \*/

45 unsigned long s11; /\* saved register \*/

46#endif

47};

48typedef struct \_callee\_saved \_callee\_saved\_t;

49

50#if !defined(RV\_FP\_TYPE)

51#ifdef CONFIG\_CPU\_HAS\_FPU\_DOUBLE\_PRECISION

52#define RV\_FP\_TYPE uint64\_t

53#else

[ 54](arch_2riscv_2thread_8h.md#a94fb796ff93ddd2633c9cc48d9bc1214)#define RV\_FP\_TYPE uint32\_t

55#endif

56#endif

57

58struct z\_riscv\_fp\_context {

59 [RV\_FP\_TYPE](arch_2riscv_2thread_8h.md#a94fb796ff93ddd2633c9cc48d9bc1214) fa0, fa1, fa2, fa3, fa4, fa5, fa6, fa7;

60 [RV\_FP\_TYPE](arch_2riscv_2thread_8h.md#a94fb796ff93ddd2633c9cc48d9bc1214) ft0, ft1, ft2, ft3, ft4, ft5, ft6, ft7, ft8, ft9, ft10, ft11;

61 [RV\_FP\_TYPE](arch_2riscv_2thread_8h.md#a94fb796ff93ddd2633c9cc48d9bc1214) fs0, fs1, fs2, fs3, fs4, fs5, fs6, fs7, fs8, fs9, fs10, fs11;

62 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fcsr;

63};

64typedef struct z\_riscv\_fp\_context z\_riscv\_fp\_context\_t;

65

[ 66](arch_2riscv_2thread_8h.md#ad37c7fba59f9d64bc2b4d154c274e007)#define PMP\_M\_MODE\_SLOTS 8 /\* 8 is plenty enough for m-mode \*/

67

68struct \_thread\_arch {

69#ifdef CONFIG\_FPU\_SHARING

70 struct z\_riscv\_fp\_context saved\_fp\_context;

71 bool fpu\_recently\_used;

72 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) exception\_depth;

73#endif

74#ifdef CONFIG\_USERSPACE

75 unsigned long priv\_stack\_start;

76 unsigned long u\_mode\_pmpaddr\_regs[CONFIG\_PMP\_SLOTS];

77 unsigned long u\_mode\_pmpcfg\_regs[CONFIG\_PMP\_SLOTS / sizeof(unsigned long)];

78 unsigned int u\_mode\_pmp\_domain\_offset;

79 unsigned int u\_mode\_pmp\_end\_index;

80 unsigned int u\_mode\_pmp\_update\_nr;

81#endif

82#ifdef CONFIG\_PMP\_STACK\_GUARD

83 unsigned int m\_mode\_pmp\_end\_index;

84 unsigned long m\_mode\_pmpaddr\_regs[[PMP\_M\_MODE\_SLOTS](arch_2riscv_2thread_8h.md#ad37c7fba59f9d64bc2b4d154c274e007)];

85 unsigned long m\_mode\_pmpcfg\_regs[[PMP\_M\_MODE\_SLOTS](arch_2riscv_2thread_8h.md#ad37c7fba59f9d64bc2b4d154c274e007) / sizeof(unsigned long)];

86#endif

87};

88

89typedef struct \_thread\_arch \_thread\_arch\_t;

90

91#endif /\* \_ASMLANGUAGE \*/

92

93#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RISCV\_THREAD\_H\_ \*/

[RV\_FP\_TYPE](arch_2riscv_2thread_8h.md#a94fb796ff93ddd2633c9cc48d9bc1214)

#define RV\_FP\_TYPE

**Definition** thread.h:54

[PMP\_M\_MODE\_SLOTS](arch_2riscv_2thread_8h.md#ad37c7fba59f9d64bc2b4d154c274e007)

#define PMP\_M\_MODE\_SLOTS

**Definition** thread.h:66

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [thread.h](arch_2riscv_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
