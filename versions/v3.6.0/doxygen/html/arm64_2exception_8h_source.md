---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arm64_2exception_8h_source.html
original_path: doxygen/html/arm64_2exception_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](arm64_2exception_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_EXCEPTION\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_EXCEPTION\_H\_

16

17/\* for assembler, only works with constants \*/

18

19#ifdef \_ASMLANGUAGE

20#else

21#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27struct \_\_esf {

28 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x0;

29 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x1;

30 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x2;

31 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x3;

32 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x4;

33 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x5;

34 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x6;

35 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x7;

36 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x8;

37 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x9;

38 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x10;

39 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x11;

40 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x12;

41 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x13;

42 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x14;

43 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x15;

44 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x16;

45 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x17;

46 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x18;

47 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) lr;

48 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) spsr;

49 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) elr;

50#ifdef CONFIG\_ARM64\_ENABLE\_FRAME\_POINTER

51 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) fp;

52#endif

53#ifdef CONFIG\_ARM64\_SAFE\_EXCEPTION\_STACK

54 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sp;

55#endif

56} \_\_aligned(16);

57

58typedef struct \_\_esf z\_arch\_esf\_t;

59

60#ifdef \_\_cplusplus

61}

62#endif

63

64#endif /\* \_ASMLANGUAGE \*/

65

66#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_EXCEPTION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [exception.h](arm64_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
