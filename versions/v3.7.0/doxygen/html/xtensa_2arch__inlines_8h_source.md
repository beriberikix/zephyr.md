---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/xtensa_2arch__inlines_8h_source.html
original_path: doxygen/html/xtensa_2arch__inlines_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_inlines.h

[Go to the documentation of this file.](xtensa_2arch__inlines_8h.md)

1/\*

2 \* Copyright (c) 2016 Cadence Design Systems, Inc.

3 \* Copyright (c) 2019 Stephanos Ioannidis <root@stephanos.io>

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_ARCH\_INLINES\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_ARCH\_INLINES\_H\_

10

11#ifndef \_ASMLANGUAGE

12

13#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

14#include <zephyr/zsr.h>

15

[ 23](xtensa_2arch__inlines_8h.md#ad745bdf9b93a9019a1d373e9f50a35e5)#define XTENSA\_RSR(sr) \

24 ({uint32\_t v; \

25 \_\_asm\_\_ volatile ("rsr." sr " %0" : "=a"(v)); \

26 v; })

27

[ 34](xtensa_2arch__inlines_8h.md#a319bd616dfbeb56398294bcb9f7a0fdd)#define XTENSA\_WSR(sr, v) \

35 do { \

36 \_\_asm\_\_ volatile ("wsr." sr " %0" : : "r"(v)); \

37 } while (false)

38

[ 46](xtensa_2arch__inlines_8h.md#aa297de6c2736557e7076e496ce25ec23)#define XTENSA\_RUR(ur) \

47 ({uint32\_t v; \

48 \_\_asm\_\_ volatile ("rur." ur " %0" : "=a"(v)); \

49 v; })

50

[ 57](xtensa_2arch__inlines_8h.md#a22be7315733dd413f1c3253faa2e78da)#define XTENSA\_WUR(ur, v) \

58 do { \

59 \_\_asm\_\_ volatile ("wur." ur " %0" : : "r"(v)); \

60 } while (false)

61

[ 63](xtensa_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \*[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)(void)

64{

65 \_cpu\_t \*cpu;

66

67 cpu = (\_cpu\_t \*)[XTENSA\_RSR](xtensa_2arch__inlines_8h.md#ad745bdf9b93a9019a1d373e9f50a35e5)(ZSR\_CPU\_STR);

68

69 return cpu;

70}

71

[ 73](xtensa_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)(void)

74{

75 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prid;

76

77 \_\_asm\_\_ volatile("rsr %0, PRID" : "=r"(prid));

78 return prid;

79}

80

81#ifdef CONFIG\_SOC\_HAS\_RUNTIME\_NUM\_CPUS

82extern unsigned int soc\_num\_cpus;

83#endif

84

[ 86](xtensa_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)(void)

87{

88#ifdef CONFIG\_SOC\_HAS\_RUNTIME\_NUM\_CPUS

89 return soc\_num\_cpus;

90#else

91 return CONFIG\_MP\_MAX\_NUM\_CPUS;

92#endif

93}

94

95#endif /\* !\_ASMLANGUAGE \*/

96

97#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_ARCH\_INLINES\_H\_ \*/

[arch\_curr\_cpu](arc_2arch__inlines_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)

static ALWAYS\_INLINE \_cpu\_t \* arch\_curr\_cpu(void)

**Definition** arch\_inlines.h:17

[arch\_proc\_id](arc_2arch__inlines_8h.md#a4bf4475c062f66961e183d17fd4c22d3)

static ALWAYS\_INLINE uint32\_t arch\_proc\_id(void)

**Definition** arch\_inlines.h:30

[arch\_num\_cpus](arc_2arch__inlines_8h.md#a83c8ae933b0ec7d067569f17125c6a2c)

static ALWAYS\_INLINE unsigned int arch\_num\_cpus(void)

**Definition** arch\_inlines.h:39

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[kernel\_structs.h](kernel__structs_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[XTENSA\_RSR](xtensa_2arch__inlines_8h.md#ad745bdf9b93a9019a1d373e9f50a35e5)

#define XTENSA\_RSR(sr)

Read a special register.

**Definition** arch\_inlines.h:23

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [arch\_inlines.h](xtensa_2arch__inlines_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
