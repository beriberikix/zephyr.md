---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ffs_8h_source.html
original_path: doxygen/html/ffs_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ffs.h

[Go to the documentation of this file.](ffs_8h.md)

1/\*

2 \* Copyright (c) 2015, Wind River Systems, Inc.

3 \* Copyright (c) 2017, Oticon A/S

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_COMMON\_FFS\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_COMMON\_FFS\_H\_

10

11#ifndef \_ASMLANGUAGE

12

13#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

30

[ 31](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op)

32{

33 if (op == 0) {

34 return 0;

35 }

36

37 return 32 - \_\_builtin\_clz(op);

38}

39

40

52

[ 53](ffs_8h.md#a860b01217c1d5eb5f416272c3b719113)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [find\_lsb\_set](ffs_8h.md#a860b01217c1d5eb5f416272c3b719113)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op)

54{

55#ifdef CONFIG\_TOOLCHAIN\_HAS\_BUILTIN\_FFS

56 return \_\_builtin\_ffs(op);

57

58#else

59 /\*

60 \* Toolchain does not have \_\_builtin\_ffs().

61 \* Need to do this manually.

62 \*/

63 int bit;

64

65 if (op == 0) {

66 return 0;

67 }

68

69 for (bit = 0; bit < 32; bit++) {

70 if ((op & (1 << bit)) != 0) {

71 return (bit + 1);

72 }

73 }

74

75 /\*

76 \* This should never happen but we need to keep

77 \* compiler happy.

78 \*/

79 return 0;

80#endif /\* CONFIG\_TOOLCHAIN\_HAS\_BUILTIN\_FFS \*/

81}

82

83#ifdef \_\_cplusplus

84}

85#endif

86

87#endif /\* \_ASMLANGUAGE \*/

88

89#endif /\* ZEPHYR\_INCLUDE\_ARCH\_COMMON\_FFS\_H\_ \*/

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)

static ALWAYS\_INLINE unsigned int find\_msb\_set(uint32\_t op)

find most significant bit set in a 32-bit word

**Definition** ffs.h:31

[find\_lsb\_set](ffs_8h.md#a860b01217c1d5eb5f416272c3b719113)

static ALWAYS\_INLINE unsigned int find\_lsb\_set(uint32\_t op)

find least significant bit set in a 32-bit word

**Definition** ffs.h:53

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [ffs.h](ffs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
