---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm_2cortex__a__r_2cpu_8h_source.html
original_path: doxygen/html/arm_2cortex__a__r_2cpu_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu.h

[Go to the documentation of this file.](arm_2cortex__a__r_2cpu_8h.md)

1/\*

2 \* Copyright (c) 2018 Lexmark International, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_CPU\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_CPU\_H\_

9

10#if defined(CONFIG\_ARM\_MPU)

11#include <[zephyr/arch/arm/cortex\_a\_r/mpu.h](arm_2cortex__a__r_2mpu_8h.md)>

12#endif

13

14/\*

15 \* SCTLR register bit assignments

16 \*/

[ 17](arm_2cortex__a__r_2cpu_8h.md#aa78d7bae99df2480a96055226477b726)#define SCTLR\_MPU\_ENABLE (1 << 0)

18

[ 19](arm_2cortex__a__r_2cpu_8h.md#a7b9e6e5e6ca9a4011ff55154df4d2e6e)#define MODE\_USR 0x10

[ 20](arm_2cortex__a__r_2cpu_8h.md#a2d95aed11b5420eb0d67884b39e984f4)#define MODE\_FIQ 0x11

[ 21](arm_2cortex__a__r_2cpu_8h.md#ae3e562974dac9a93ece87414925c8c7e)#define MODE\_IRQ 0x12

[ 22](arm_2cortex__a__r_2cpu_8h.md#a9266f9bd89f1bccd0b3b5e8825ab654c)#define MODE\_SVC 0x13

[ 23](arm_2cortex__a__r_2cpu_8h.md#a75f8757e1d238418b64ef59fc09e5e94)#define MODE\_ABT 0x17

[ 24](arm_2cortex__a__r_2cpu_8h.md#a6557422114a234fff334a90634283b02)#define MODE\_HYP 0x1a

[ 25](arm_2cortex__a__r_2cpu_8h.md#aade1410afb684e0540924f289ba68f23)#define MODE\_UND 0x1b

[ 26](arm_2cortex__a__r_2cpu_8h.md#ac5fe4951d03afe9d7e282e754b655f7e)#define MODE\_SYS 0x1f

[ 27](arm_2cortex__a__r_2cpu_8h.md#aba2b187200eec47c5fc32655e296783d)#define MODE\_MASK 0x1f

28

[ 29](arm_2cortex__a__r_2cpu_8h.md#a9368e9f279fd5b52f0ef708d907e0fa2)#define E\_BIT (1 << 9)

[ 30](arm_2cortex__a__r_2cpu_8h.md#ae59e66b2ffaf088f18f894088f53205b)#define A\_BIT (1 << 8)

[ 31](arm_2cortex__a__r_2cpu_8h.md#aee2152981b17e0fd7752a41c038f42ad)#define I\_BIT (1 << 7)

[ 32](arm_2cortex__a__r_2cpu_8h.md#a96123c0224b549def3a8fd4cc5530e43)#define F\_BIT (1 << 6)

[ 33](arm_2cortex__a__r_2cpu_8h.md#ace344d543daa81e5cbfbba5fabb29d27)#define T\_BIT (1 << 5)

34

[ 35](arm_2cortex__a__r_2cpu_8h.md#a5c62a691b1161751afa302c0aa64f85d)#define HIVECS (1 << 13)

36

[ 37](arm_2cortex__a__r_2cpu_8h.md#aa0976c383cc1d77799a4bea364fda464)#define CPACR\_NA (0U)

[ 38](arm_2cortex__a__r_2cpu_8h.md#a436351855fd50865506e3e24fd161d39)#define CPACR\_FA (3U)

39

[ 40](arm_2cortex__a__r_2cpu_8h.md#aeeb8aaad6fa5d13fe4802c6f69308faf)#define CPACR\_CP10(r) (r << 20)

[ 41](arm_2cortex__a__r_2cpu_8h.md#a25e830ab98f6c2992b5b4e2dddb74ca4)#define CPACR\_CP11(r) (r << 22)

42

[ 43](arm_2cortex__a__r_2cpu_8h.md#a814e21f8d57ac2486be3c095f159215f)#define FPEXC\_EN (1 << 30)

44

[ 45](arm_2cortex__a__r_2cpu_8h.md#a093fac404bee8f2ffcfab117b6348345)#define DFSR\_DOMAIN\_SHIFT (4)

[ 46](arm_2cortex__a__r_2cpu_8h.md#a8a9af346b603e05f05f7ea99c8104bdf)#define DFSR\_DOMAIN\_MASK (0xf)

[ 47](arm_2cortex__a__r_2cpu_8h.md#a4ff165c22368a07195d60b49d52c2790)#define DFSR\_FAULT\_4\_MASK (1 << 10)

[ 48](arm_2cortex__a__r_2cpu_8h.md#ab82fe44d3e94935526b7400b00e06f77)#define DFSR\_WRITE\_MASK (1 << 11)

[ 49](arm_2cortex__a__r_2cpu_8h.md#aaefa716c9eed67bff548d67fd319fa63)#define DFSR\_AXI\_SLAVE\_MASK (1 << 12)

50

51/\* Armv8-R AArch32 architecture profile \*/

[ 52](arm_2cortex__a__r_2cpu_8h.md#a2d4fcd4a7bb1c87080f5795d0f531703)#define VBAR\_MASK (0xFFFFFFE0U)

[ 53](arm_2cortex__a__r_2cpu_8h.md#a223e38830566f400f6d592a6bb7dd361)#define SCTLR\_M\_BIT BIT(0)

[ 54](arm_2cortex__a__r_2cpu_8h.md#ad9dc6fc20549b11dc1b2cc5ed02d5ee7)#define SCTLR\_A\_BIT BIT(1)

[ 55](arm_2cortex__a__r_2cpu_8h.md#a752ac38bb53a96c6749fbfc09a1fb88d)#define SCTLR\_C\_BIT BIT(2)

[ 56](arm_2cortex__a__r_2cpu_8h.md#ac9fd86e6613531ab567031f4c02a2900)#define SCTLR\_I\_BIT BIT(12)

57

58/\* Hyp System Control Register \*/

[ 59](arm_2cortex__a__r_2cpu_8h.md#a419c15bf37a7aaea28a4bea82b8c4421)#define HSCTLR\_RES1 (BIT(29) | BIT(28) | BIT(23) | \

60 BIT(22) | BIT(18) | BIT(16) | \

61 BIT(11) | BIT(4) | BIT(3))

62

63/\* Hyp Auxiliary Control Register \*/

[ 64](arm_2cortex__a__r_2cpu_8h.md#a367fbf6725426a0cb44a01cd7d3bbac4)#define HACTLR\_CPUACTLR BIT(0)

[ 65](arm_2cortex__a__r_2cpu_8h.md#af6034c7fd77f1096314b8753ddd83621)#define HACTLR\_CDBGDCI BIT(1)

[ 66](arm_2cortex__a__r_2cpu_8h.md#a6161c9da01ec5a54597681bc187e2c40)#define HACTLR\_FLASHIFREGIONR BIT(7)

[ 67](arm_2cortex__a__r_2cpu_8h.md#a054011b021f935829db1fe81688a2efa)#define HACTLR\_PERIPHPREGIONR BIT(8)

[ 68](arm_2cortex__a__r_2cpu_8h.md#ada072a55f7ba6970e29472d7ca78d967)#define HACTLR\_QOSR\_BIT BIT(9)

[ 69](arm_2cortex__a__r_2cpu_8h.md#a7d34434117254b1745ff62a40f850455)#define HACTLR\_BUSTIMEOUTR\_BIT BIT(10)

[ 70](arm_2cortex__a__r_2cpu_8h.md#a4f2b59b38069f9b4ddcd879bd666a9df)#define HACTLR\_INTMONR\_BIT BIT(12)

[ 71](arm_2cortex__a__r_2cpu_8h.md#ae245fc7db7d6db0279d6da680de1981f)#define HACTLR\_ERR\_BIT BIT(13)

72

[ 73](arm_2cortex__a__r_2cpu_8h.md#aa417d6d641a116d5e2d3eaf6a56b1cc8)#define HACTLR\_INIT (HACTLR\_ERR\_BIT | HACTLR\_INTMONR\_BIT | \

74 HACTLR\_BUSTIMEOUTR\_BIT | HACTLR\_QOSR\_BIT | \

75 HACTLR\_PERIPHPREGIONR | HACTLR\_FLASHIFREGIONR | \

76 HACTLR\_CDBGDCI | HACTLR\_CPUACTLR)

77/\* ARMv8 Timer \*/

[ 78](arm_2cortex__a__r_2cpu_8h.md#a0001886233fa8459922ad8338eba1dc8)#define CNTV\_CTL\_ENABLE\_BIT BIT(0)

[ 79](arm_2cortex__a__r_2cpu_8h.md#a382fbb7831e299acfd89e9f03c08aebb)#define CNTV\_CTL\_IMASK\_BIT BIT(1)

80

81/\* Interrupt Controller System Register Enable Register \*/

[ 82](arm_2cortex__a__r_2cpu_8h.md#a581240d06f8f27d299a303941934d0a9)#define ICC\_SRE\_ELx\_SRE\_BIT BIT(0)

[ 83](arm_2cortex__a__r_2cpu_8h.md#a54ea5ad3d9d0c66c5787b4c10feaeffb)#define ICC\_SRE\_ELx\_DFB\_BIT BIT(1)

[ 84](arm_2cortex__a__r_2cpu_8h.md#a6464acd03121adf32b11764b8e16a59f)#define ICC\_SRE\_ELx\_DIB\_BIT BIT(2)

[ 85](arm_2cortex__a__r_2cpu_8h.md#a89642941ffefc853013b0f92cc80f131)#define ICC\_SRE\_EL3\_EN\_BIT BIT(3)

86

87/\* MPIDR \*/

[ 88](arm_2cortex__a__r_2cpu_8h.md#a9bce40a5c0fceea5298a899b174c3e1c)#define MPIDR\_AFFLVL\_MASK (0xff)

89

[ 90](arm_2cortex__a__r_2cpu_8h.md#a7a2087ca83455cf2759a5aee220105e2)#define MPIDR\_AFF0\_SHIFT (0)

[ 91](arm_2cortex__a__r_2cpu_8h.md#a3a7ffd9f7a014257a725513d531edab2)#define MPIDR\_AFF1\_SHIFT (8)

[ 92](arm_2cortex__a__r_2cpu_8h.md#a61d65102667e48cb00b7f9133dcd60f2)#define MPIDR\_AFF2\_SHIFT (16)

93

[ 94](arm_2cortex__a__r_2cpu_8h.md#a35278aa57b0b98cd0cb541cfea58b177)#define MPIDR\_AFFLVL(mpidr, aff\_level) \

95 (((mpidr) >> MPIDR\_AFF##aff\_level##\_SHIFT) & MPIDR\_AFFLVL\_MASK)

96

[ 97](arm_2cortex__a__r_2cpu_8h.md#a958d9c5f047f5dc318ecf4b171a68949)#define GET\_MPIDR() read\_sysreg(mpidr)

[ 98](arm_2cortex__a__r_2cpu_8h.md#a850e9ad6314a72da4ef5ff09d5e1e024)#define MPIDR\_TO\_CORE(mpidr) MPIDR\_AFFLVL(mpidr, 0)

99

100/\* ICC SGI macros \*/

[ 101](arm_2cortex__a__r_2cpu_8h.md#aef12617a687736364283ba5fc45eb29a)#define SGIR\_TGT\_MASK (0xffff)

[ 102](arm_2cortex__a__r_2cpu_8h.md#a54fd53204f64c9081d7c0c9fc3209c37)#define SGIR\_AFF1\_SHIFT (16)

[ 103](arm_2cortex__a__r_2cpu_8h.md#afcb9746b2d5edfd88af4af2759c931d7)#define SGIR\_AFF2\_SHIFT (32)

[ 104](arm_2cortex__a__r_2cpu_8h.md#ac4364d68d92dd7b7e1bb7ffac6e81eef)#define SGIR\_AFF3\_SHIFT (48)

[ 105](arm_2cortex__a__r_2cpu_8h.md#aaebf9f7f5e67965fac91a7eb0336f3e4)#define SGIR\_AFF\_MASK (0xff)

[ 106](arm_2cortex__a__r_2cpu_8h.md#a9bd0096ceb2f20d31173b61127dc5bd3)#define SGIR\_INTID\_SHIFT (24)

[ 107](arm_2cortex__a__r_2cpu_8h.md#a6e5a1e0b98322addaa87188e4d9a03f1)#define SGIR\_INTID\_MASK (0xf)

[ 108](arm_2cortex__a__r_2cpu_8h.md#a0a9ae05724f25a9f9e55e664823eeb6b)#define SGIR\_IRM\_SHIFT (40)

[ 109](arm_2cortex__a__r_2cpu_8h.md#a31c2a71ebf8c2e296f0c8417012ca7f4)#define SGIR\_IRM\_MASK (0x1)

[ 110](arm_2cortex__a__r_2cpu_8h.md#a410f4b9c7089a847d01bc6592335871f)#define SGIR\_IRM\_TO\_AFF (0)

111

[ 112](arm_2cortex__a__r_2cpu_8h.md#a2df77921af208fb2202cb6d03a9ea004)#define GICV3\_SGIR\_VALUE(\_aff3, \_aff2, \_aff1, \_intid, \_irm, \_tgt) \

113 ((((uint64\_t) (\_aff3) & SGIR\_AFF\_MASK) << SGIR\_AFF3\_SHIFT) | \

114 (((uint64\_t) (\_irm) & SGIR\_IRM\_MASK) << SGIR\_IRM\_SHIFT) | \

115 (((uint64\_t) (\_aff2) & SGIR\_AFF\_MASK) << SGIR\_AFF2\_SHIFT) | \

116 (((\_intid) & SGIR\_INTID\_MASK) << SGIR\_INTID\_SHIFT) | \

117 (((\_aff1) & SGIR\_AFF\_MASK) << SGIR\_AFF1\_SHIFT) | \

118 ((\_tgt) & SGIR\_TGT\_MASK))

119

120#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_CPU\_H\_ \*/

[mpu.h](arm_2cortex__a__r_2mpu_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [cpu.h](arm_2cortex__a__r_2cpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
