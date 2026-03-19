---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm_2cortex__m_2cpu_8h_source.html
original_path: doxygen/html/arm_2cortex__m_2cpu_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu.h

[Go to the documentation of this file.](arm_2cortex__m_2cpu_8h.md)

1/\*

2 \* Copyright (c) 2015, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_CORTEX\_M\_CPU\_H

8#define \_CORTEX\_M\_CPU\_H

9

10#ifdef \_ASMLANGUAGE

11

12#define \_SCS\_BASE\_ADDR \_PPB\_INT\_SCS

13

14/\* ICSR defines \*/

15#define \_SCS\_ICSR (\_SCS\_BASE\_ADDR + 0xd04)

16#define \_SCS\_ICSR\_PENDSV (1 << 28)

17#define \_SCS\_ICSR\_UNPENDSV (1 << 27)

18#define \_SCS\_ICSR\_RETTOBASE (1 << 11)

19

20#define \_SCS\_MPU\_CTRL (\_SCS\_BASE\_ADDR + 0xd94)

21

22/\* CONTROL defines \*/

23#define \_CONTROL\_FPCA\_Msk (1 << 2)

24

25/\* EXC\_RETURN defines \*/

26#define \_EXC\_RETURN\_SPSEL\_Msk (1 << 2)

27#define \_EXC\_RETURN\_FTYPE\_Msk (1 << 4)

28

29#else

30#include <[stdint.h](stdint_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

36/\* CP10 Access Bits \*/

[ 37](arm_2cortex__m_2cpu_8h.md#a65fa7b1d26e122d7466d09d023dd03f5)#define CPACR\_CP10\_Pos 20U

[ 38](arm_2cortex__m_2cpu_8h.md#aae47418d3f6f6596d74427d671db4568)#define CPACR\_CP10\_Msk (3UL << CPACR\_CP10\_Pos)

[ 39](arm_2cortex__m_2cpu_8h.md#ab98d9a7803e01c9419a1b3db46ea1add)#define CPACR\_CP10\_NO\_ACCESS (0UL << CPACR\_CP10\_Pos)

[ 40](arm_2cortex__m_2cpu_8h.md#aae2814998733c5960397fe122e1fd171)#define CPACR\_CP10\_PRIV\_ACCESS (1UL << CPACR\_CP10\_Pos)

[ 41](arm_2cortex__m_2cpu_8h.md#a92b527c3d4f14132baac8726ab4df091)#define CPACR\_CP10\_RESERVED (2UL << CPACR\_CP10\_Pos)

[ 42](arm_2cortex__m_2cpu_8h.md#a9206df98746982fe6644162f551d7dfa)#define CPACR\_CP10\_FULL\_ACCESS (3UL << CPACR\_CP10\_Pos)

43

44/\* CP11 Access Bits \*/

[ 45](arm_2cortex__m_2cpu_8h.md#aedc603d4d2e20473426cf237efdf0a0f)#define CPACR\_CP11\_Pos 22U

[ 46](arm_2cortex__m_2cpu_8h.md#a48424c4ebf99120abe4887ca5f6445eb)#define CPACR\_CP11\_Msk (3UL << CPACR\_CP11\_Pos)

[ 47](arm_2cortex__m_2cpu_8h.md#a8994c5fdf0730b06c7a11846151eaa5f)#define CPACR\_CP11\_NO\_ACCESS (0UL << CPACR\_CP11\_Pos)

[ 48](arm_2cortex__m_2cpu_8h.md#abcb053930af36f899c8d079fa80cbb6a)#define CPACR\_CP11\_PRIV\_ACCESS (1UL << CPACR\_CP11\_Pos)

[ 49](arm_2cortex__m_2cpu_8h.md#a8318babac72e1f7ee52b60cbf0c5975d)#define CPACR\_CP11\_RESERVED (2UL << CPACR\_CP11\_Pos)

[ 50](arm_2cortex__m_2cpu_8h.md#a45e50725e2027dda6cbc5ca350d5d177)#define CPACR\_CP11\_FULL\_ACCESS (3UL << CPACR\_CP11\_Pos)

51

52#ifdef CONFIG\_PM\_S2RAM

53

54struct \_\_cpu\_context {

55 /\* GPRs are saved onto the stack \*/

56 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) msp;

57 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) msplim;

58 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) psp;

59 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) psplim;

60 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) apsr;

61 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ipsr;

62 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) epsr;

63 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) primask;

64 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) faultmask;

65 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) basepri;

66 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) control;

67};

68

69typedef struct \_\_cpu\_context \_cpu\_context\_t;

70

71#endif /\* CONFIG\_PM\_S2RAM \*/

72

73#ifdef \_\_cplusplus

74}

75#endif

76

77#endif /\* \_ASMLANGUAGE \*/

78

79#endif /\* \_CORTEX\_M\_CPU\_H \*/

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_m](dir_d27032cbfb87610ee5132d2bc57d6588.md)
- [cpu.h](arm_2cortex__m_2cpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
