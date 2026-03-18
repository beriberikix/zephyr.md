---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/cortex__a__r_2lib__helpers_8h_source.html
original_path: doxygen/html/cortex__a__r_2lib__helpers_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lib\_helpers.h

[Go to the documentation of this file.](cortex__a__r_2lib__helpers_8h.md)

1/\*

2 \* Copyright (c) 2022 IoT.bzh

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*

6 \* Armv8-R AArch32 architecture helpers.

7 \*

8 \*/

9

10#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_LIB\_HELPERS\_H\_

11#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_LIB\_HELPERS\_H\_

12

13#ifndef \_ASMLANGUAGE

14

15#include <[stdint.h](stdint_8h.md)>

16

[ 17](cortex__a__r_2lib__helpers_8h.md#a8bd3d2e84fbd96daba2f99d0c318bf5c)#define read\_sysreg32(op1, CRn, CRm, op2) \

18({ \

19 uint32\_t val; \

20 \_\_asm\_\_ volatile ("mrc p15, " #op1 ", %0, c" #CRn ", c" \

21 #CRm ", " #op2 : "=r" (val) :: "memory"); \

22 val; \

23})

24

[ 25](cortex__a__r_2lib__helpers_8h.md#a2334d77203a5d5db697773ef588839c2)#define write\_sysreg32(val, op1, CRn, CRm, op2) \

26({ \

27 \_\_asm\_\_ volatile ("mcr p15, " #op1 ", %0, c" #CRn ", c" \

28 #CRm ", " #op2 :: "r" (val) : "memory"); \

29})

30

[ 31](cortex__a__r_2lib__helpers_8h.md#a292c132843b32eae185818aeddb1cd48)#define read\_sysreg64(op1, CRm) \

32({ \

33 uint64\_t val; \

34 \_\_asm\_\_ volatile ("mrrc p15, " #op1 ", %Q0, %R0, c" \

35 #CRm : "=r" (val) :: "memory"); \

36 val; \

37})

38

[ 39](cortex__a__r_2lib__helpers_8h.md#a596118b721eb1e3184b351a2b4383485)#define write\_sysreg64(val, op1, CRm) \

40({ \

41 \_\_asm\_\_ volatile ("mcrr p15, " #op1 ", %Q0, %R0, c" \

42 #CRm :: "r" (val) : "memory"); \

43})

44

[ 45](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)#define MAKE\_REG\_HELPER(reg, op1, CRn, CRm, op2) \

46 static ALWAYS\_INLINE uint32\_t read\_##reg(void) \

47 { \

48 return read\_sysreg32(op1, CRn, CRm, op2); \

49 } \

50 static ALWAYS\_INLINE void write\_##reg(uint32\_t val) \

51 { \

52 write\_sysreg32(val, op1, CRn, CRm, op2); \

53 }

54

[ 55](cortex__a__r_2lib__helpers_8h.md#aecef30202db40ce61d5ebb5bf4907971)#define MAKE\_REG64\_HELPER(reg, op1, CRm) \

56 static ALWAYS\_INLINE uint64\_t read\_##reg(void) \

57 { \

58 return read\_sysreg64(op1, CRm); \

59 } \

60 static ALWAYS\_INLINE void write\_##reg(uint64\_t val) \

61 { \

62 write\_sysreg64(val, op1, CRm); \

63 }

64

[ 65](cortex__a__r_2lib__helpers_8h.md#a7c1906a10ebfe46fc20b8ded1a838f2c)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(mpuir, 0, 0, 0, 4);

[ 66](cortex__a__r_2lib__helpers_8h.md#a91b417a13806edaa706288547de78ca7)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(mpidr, 0, 0, 0, 5);

[ 67](cortex__a__r_2lib__helpers_8h.md#aadf14247e4ae2390a06c7c198a4ee064)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(sctlr, 0, 1, 0, 0);

[ 68](cortex__a__r_2lib__helpers_8h.md#a5067072ffc6359b9a0e990d60a87cb90)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(prselr, 0, 6, 2, 1);

[ 69](cortex__a__r_2lib__helpers_8h.md#a49d03d7caeb4025cfbe60974c42e1221)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(prbar, 0, 6, 3, 0);

[ 70](cortex__a__r_2lib__helpers_8h.md#ab98fe50c068572436318524d47b39e8f)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(prlar, 0, 6, 3, 1);

[ 71](cortex__a__r_2lib__helpers_8h.md#aff11460b159e63e224c49c1010a6e1f0)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(mair0, 0, 10, 2, 0);

[ 72](cortex__a__r_2lib__helpers_8h.md#ab9cc0f92c805971f92aa7e7ecb6c2a2f)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(vbar, 0, 12, 0, 0);

[ 73](cortex__a__r_2lib__helpers_8h.md#a260cf183f5aa1745e5439626e9480f48)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(cntv\_ctl, 0, 14, 3, 1);

[ 74](cortex__a__r_2lib__helpers_8h.md#ad3d02a5e9e30eac6fb4a6be8b08110c8)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(ctr, 0, 0, 0, 1);

[ 75](cortex__a__r_2lib__helpers_8h.md#af410cde5864b6e4997a31e2162e4873d)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(tpidruro, 0, 13, 0, 3);

[ 76](cortex__a__r_2lib__helpers_8h.md#aa15690fa7f43f5699611f07cd07b52aa)[MAKE\_REG64\_HELPER](cortex__a__r_2lib__helpers_8h.md#aecef30202db40ce61d5ebb5bf4907971)([ICC\_SGI1R](include_2zephyr_2arch_2arm64_2cpu_8h.md#ae36e32afe169a9173e3294a807af3234), 0, 12);

[ 77](cortex__a__r_2lib__helpers_8h.md#aadc1c2db15fb0074e0acfb554cb26d8b)[MAKE\_REG64\_HELPER](cortex__a__r_2lib__helpers_8h.md#aecef30202db40ce61d5ebb5bf4907971)(cntvct, 1, 14);

[ 78](cortex__a__r_2lib__helpers_8h.md#ae286bdd594c272fb2493e838ca927975)[MAKE\_REG64\_HELPER](cortex__a__r_2lib__helpers_8h.md#aecef30202db40ce61d5ebb5bf4907971)(cntv\_cval, 3, 14);

79

80/\*

81 \* GIC v3 compatibility macros:

82 \* ARMv8 AArch32 profile has no mention of

83 \* ELx in the register names.

84 \* We define them anyway to reuse the GICv3 driver

85 \* made for AArch64.

86 \*/

87

88/\* ICC\_PMR \*/

[ 89](cortex__a__r_2lib__helpers_8h.md#aa8c18af48a651032f050ac9218066030)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)([ICC\_PMR\_EL1](include_2zephyr_2arch_2arm64_2cpu_8h.md#a569e3c45407957f8e9b6786441dd1954), 0, 4, 6, 0);

90/\* ICC\_IAR1 \*/

[ 91](cortex__a__r_2lib__helpers_8h.md#a8162a3562d7c787b977c21ae15c30301)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)([ICC\_IAR1\_EL1](include_2zephyr_2arch_2arm64_2cpu_8h.md#a35f0be43473c740c83e32af88e2d0625), 0, 12, 12, 0);

92/\* ICC\_EOIR1 \*/

[ 93](cortex__a__r_2lib__helpers_8h.md#a309e98780104b76bb98ab5b1dbf867ac)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)([ICC\_EOIR1\_EL1](include_2zephyr_2arch_2arm64_2cpu_8h.md#a5dbe3c5dfb9ff381fac5c1a004116592), 0, 12, 12, 1);

94/\* ICC\_SRE \*/

[ 95](cortex__a__r_2lib__helpers_8h.md#adb4c0847f09d9601162f53b5870f573a)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)([ICC\_SRE\_EL1](include_2zephyr_2arch_2arm64_2cpu_8h.md#a178411409386d40d5927250161b2c3d3), 0, 12, 12, 5);

96/\* ICC\_IGRPEN1 \*/

[ 97](cortex__a__r_2lib__helpers_8h.md#afa5bbc906e90bd7a522ea4f96be14bc0)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)([ICC\_IGRPEN1\_EL1](include_2zephyr_2arch_2arm64_2cpu_8h.md#aeb7f0f2d77b8c2015a23e12982e35a01), 0, 12, 12, 7);

98

[ 99](cortex__a__r_2lib__helpers_8h.md#adfcf211009c840e6f89530db728f9047)#define write\_sysreg(val, reg) write\_##reg(val)

[ 100](cortex__a__r_2lib__helpers_8h.md#abf4f1c14ffe7c2d5b2bfa605615e676d)#define read\_sysreg(reg) read\_##reg()

101

[ 102](cortex__a__r_2lib__helpers_8h.md#a544cc6885da9c2a5fb66a2a788d2ae41)#define sev() \_\_asm\_\_ volatile("sev" : : : "memory")

[ 103](cortex__a__r_2lib__helpers_8h.md#aa97b536857f20cc5b809240da5c6b0b4)#define wfe() \_\_asm\_\_ volatile("wfe" : : : "memory")

104

105#endif /\* !\_ASMLANGUAGE \*/

106#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_LIB\_HELPERS\_H\_ \*/

[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)

#define MAKE\_REG\_HELPER(reg, op1, CRn, CRm, op2)

**Definition** lib\_helpers.h:45

[MAKE\_REG64\_HELPER](cortex__a__r_2lib__helpers_8h.md#aecef30202db40ce61d5ebb5bf4907971)

#define MAKE\_REG64\_HELPER(reg, op1, CRm)

**Definition** lib\_helpers.h:55

[ICC\_SRE\_EL1](include_2zephyr_2arch_2arm64_2cpu_8h.md#a178411409386d40d5927250161b2c3d3)

#define ICC\_SRE\_EL1

**Definition** cpu.h:146

[ICC\_IAR1\_EL1](include_2zephyr_2arch_2arm64_2cpu_8h.md#a35f0be43473c740c83e32af88e2d0625)

#define ICC\_IAR1\_EL1

**Definition** cpu.h:158

[ICC\_PMR\_EL1](include_2zephyr_2arch_2arm64_2cpu_8h.md#a569e3c45407957f8e9b6786441dd1954)

#define ICC\_PMR\_EL1

**Definition** cpu.h:151

[ICC\_EOIR1\_EL1](include_2zephyr_2arch_2arm64_2cpu_8h.md#a5dbe3c5dfb9ff381fac5c1a004116592)

#define ICC\_EOIR1\_EL1

**Definition** cpu.h:160

[ICC\_SGI1R](include_2zephyr_2arch_2arm64_2cpu_8h.md#ae36e32afe169a9173e3294a807af3234)

#define ICC\_SGI1R

**Definition** cpu.h:145

[ICC\_IGRPEN1\_EL1](include_2zephyr_2arch_2arm64_2cpu_8h.md#aeb7f0f2d77b8c2015a23e12982e35a01)

#define ICC\_IGRPEN1\_EL1

**Definition** cpu.h:144

[stdint.h](stdint_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [lib\_helpers.h](cortex__a__r_2lib__helpers_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
