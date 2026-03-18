---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.html
original_path: doxygen/html/include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu.h File Reference

[Go to the source code of this file.](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SCTLR\_MPU\_ENABLE](#aa78d7bae99df2480a96055226477b726)   (1 << 0) |
| #define | [MODE\_USR](#a7b9e6e5e6ca9a4011ff55154df4d2e6e)   0x10 |
| #define | [MODE\_FIQ](#a2d95aed11b5420eb0d67884b39e984f4)   0x11 |
| #define | [MODE\_IRQ](#ae3e562974dac9a93ece87414925c8c7e)   0x12 |
| #define | [MODE\_SVC](#a9266f9bd89f1bccd0b3b5e8825ab654c)   0x13 |
| #define | [MODE\_ABT](#a75f8757e1d238418b64ef59fc09e5e94)   0x17 |
| #define | [MODE\_HYP](#a6557422114a234fff334a90634283b02)   0x1a |
| #define | [MODE\_UND](#aade1410afb684e0540924f289ba68f23)   0x1b |
| #define | [MODE\_SYS](#ac5fe4951d03afe9d7e282e754b655f7e)   0x1f |
| #define | [MODE\_MASK](#aba2b187200eec47c5fc32655e296783d)   0x1f |
| #define | [A\_BIT](#ae59e66b2ffaf088f18f894088f53205b)   (1 << 8) |
| #define | [I\_BIT](#aee2152981b17e0fd7752a41c038f42ad)   (1 << 7) |
| #define | [F\_BIT](#a96123c0224b549def3a8fd4cc5530e43)   (1 << 6) |
| #define | [T\_BIT](#ace344d543daa81e5cbfbba5fabb29d27)   (1 << 5) |
| #define | [HIVECS](#a5c62a691b1161751afa302c0aa64f85d)   (1 << 13) |
| #define | [CPACR\_NA](#aa0976c383cc1d77799a4bea364fda464)   (0U) |
| #define | [CPACR\_FA](#a436351855fd50865506e3e24fd161d39)   (3U) |
| #define | [CPACR\_CP10](#aeeb8aaad6fa5d13fe4802c6f69308faf)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
| #define | [CPACR\_CP11](#a25e830ab98f6c2992b5b4e2dddb74ca4)([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
| #define | [FPEXC\_EN](#a814e21f8d57ac2486be3c095f159215f)   (1 << 30) |
| #define | [DFSR\_DOMAIN\_SHIFT](#a093fac404bee8f2ffcfab117b6348345)   (4) |
| #define | [DFSR\_DOMAIN\_MASK](#a8a9af346b603e05f05f7ea99c8104bdf)   (0xf) |
| #define | [DFSR\_FAULT\_4\_MASK](#a4ff165c22368a07195d60b49d52c2790)   (1 << 10) |
| #define | [DFSR\_WRITE\_MASK](#ab82fe44d3e94935526b7400b00e06f77)   (1 << 11) |
| #define | [DFSR\_AXI\_SLAVE\_MASK](#aaefa716c9eed67bff548d67fd319fa63)   (1 << 12) |
| #define | [VBAR\_MASK](#a2d4fcd4a7bb1c87080f5795d0f531703)   (0xFFFFFFE0U) |
| #define | [SCTLR\_M\_BIT](#a223e38830566f400f6d592a6bb7dd361)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [SCTLR\_A\_BIT](#ad9dc6fc20549b11dc1b2cc5ed02d5ee7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [SCTLR\_C\_BIT](#a752ac38bb53a96c6749fbfc09a1fb88d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [SCTLR\_I\_BIT](#ac9fd86e6613531ab567031f4c02a2900)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [HSCTLR\_RES1](#a419c15bf37a7aaea28a4bea82b8c4421) |
| #define | [HACTLR\_CPUACTLR](#a367fbf6725426a0cb44a01cd7d3bbac4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [HACTLR\_CDBGDCI](#af6034c7fd77f1096314b8753ddd83621)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [HACTLR\_FLASHIFREGIONR](#a6161c9da01ec5a54597681bc187e2c40)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [HACTLR\_PERIPHPREGIONR](#a054011b021f935829db1fe81688a2efa)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [HACTLR\_QOSR\_BIT](#ada072a55f7ba6970e29472d7ca78d967)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [HACTLR\_BUSTIMEOUTR\_BIT](#a7d34434117254b1745ff62a40f850455)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [HACTLR\_INTMONR\_BIT](#a4f2b59b38069f9b4ddcd879bd666a9df)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [HACTLR\_ERR\_BIT](#ae245fc7db7d6db0279d6da680de1981f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| #define | [HACTLR\_INIT](#aa417d6d641a116d5e2d3eaf6a56b1cc8) |
| #define | [CNTV\_CTL\_ENABLE\_BIT](#a0001886233fa8459922ad8338eba1dc8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [CNTV\_CTL\_IMASK\_BIT](#a382fbb7831e299acfd89e9f03c08aebb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ICC\_SRE\_ELx\_SRE\_BIT](#a581240d06f8f27d299a303941934d0a9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ICC\_SRE\_ELx\_DFB\_BIT](#a54ea5ad3d9d0c66c5787b4c10feaeffb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ICC\_SRE\_ELx\_DIB\_BIT](#a6464acd03121adf32b11764b8e16a59f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [ICC\_SRE\_EL3\_EN\_BIT](#a89642941ffefc853013b0f92cc80f131)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [MPIDR\_AFFLVL\_MASK](#a9bce40a5c0fceea5298a899b174c3e1c)   (0xff) |
| #define | [MPIDR\_AFF0\_SHIFT](#a7a2087ca83455cf2759a5aee220105e2)   (0) |
| #define | [MPIDR\_AFF1\_SHIFT](#a3a7ffd9f7a014257a725513d531edab2)   (8) |
| #define | [MPIDR\_AFF2\_SHIFT](#a61d65102667e48cb00b7f9133dcd60f2)   (16) |
| #define | [MPIDR\_AFFLVL](#a35278aa57b0b98cd0cb541cfea58b177)(mpidr, aff\_level) |
| #define | [GET\_MPIDR](#a958d9c5f047f5dc318ecf4b171a68949)() |
| #define | [MPIDR\_TO\_CORE](#a850e9ad6314a72da4ef5ff09d5e1e024)(mpidr) |
| #define | [SGIR\_TGT\_MASK](#aef12617a687736364283ba5fc45eb29a)   (0xffff) |
| #define | [SGIR\_AFF1\_SHIFT](#a54fd53204f64c9081d7c0c9fc3209c37)   (16) |
| #define | [SGIR\_AFF2\_SHIFT](#afcb9746b2d5edfd88af4af2759c931d7)   (32) |
| #define | [SGIR\_AFF3\_SHIFT](#ac4364d68d92dd7b7e1bb7ffac6e81eef)   (48) |
| #define | [SGIR\_AFF\_MASK](#aaebf9f7f5e67965fac91a7eb0336f3e4)   (0xff) |
| #define | [SGIR\_INTID\_SHIFT](#a9bd0096ceb2f20d31173b61127dc5bd3)   (24) |
| #define | [SGIR\_INTID\_MASK](#a6e5a1e0b98322addaa87188e4d9a03f1)   (0xf) |
| #define | [SGIR\_IRM\_SHIFT](#a0a9ae05724f25a9f9e55e664823eeb6b)   (40) |
| #define | [SGIR\_IRM\_MASK](#a31c2a71ebf8c2e296f0c8417012ca7f4)   (0x1) |
| #define | [SGIR\_IRM\_TO\_AFF](#a410f4b9c7089a847d01bc6592335871f)   (0) |
| #define | [GICV3\_SGIR\_VALUE](#a2df77921af208fb2202cb6d03a9ea004)(\_aff3, \_aff2, \_aff1, \_intid, \_irm, \_tgt) |

## Macro Definition Documentation

## [◆ ](#ae59e66b2ffaf088f18f894088f53205b)A\_BIT

| #define A\_BIT   (1 << 8) |
| --- |

## [◆ ](#a0001886233fa8459922ad8338eba1dc8)CNTV\_CTL\_ENABLE\_BIT

| #define CNTV\_CTL\_ENABLE\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a382fbb7831e299acfd89e9f03c08aebb)CNTV\_CTL\_IMASK\_BIT

| #define CNTV\_CTL\_IMASK\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#aeeb8aaad6fa5d13fe4802c6f69308faf)CPACR\_CP10

| #define CPACR\_CP10 | ( |  | *[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) << 20)

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

## [◆ ](#a25e830ab98f6c2992b5b4e2dddb74ca4)CPACR\_CP11

| #define CPACR\_CP11 | ( |  | *[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) << 22)

## [◆ ](#a436351855fd50865506e3e24fd161d39)CPACR\_FA

| #define CPACR\_FA   (3U) |
| --- |

## [◆ ](#aa0976c383cc1d77799a4bea364fda464)CPACR\_NA

| #define CPACR\_NA   (0U) |
| --- |

## [◆ ](#aaefa716c9eed67bff548d67fd319fa63)DFSR\_AXI\_SLAVE\_MASK

| #define DFSR\_AXI\_SLAVE\_MASK   (1 << 12) |
| --- |

## [◆ ](#a8a9af346b603e05f05f7ea99c8104bdf)DFSR\_DOMAIN\_MASK

| #define DFSR\_DOMAIN\_MASK   (0xf) |
| --- |

## [◆ ](#a093fac404bee8f2ffcfab117b6348345)DFSR\_DOMAIN\_SHIFT

| #define DFSR\_DOMAIN\_SHIFT   (4) |
| --- |

## [◆ ](#a4ff165c22368a07195d60b49d52c2790)DFSR\_FAULT\_4\_MASK

| #define DFSR\_FAULT\_4\_MASK   (1 << 10) |
| --- |

## [◆ ](#ab82fe44d3e94935526b7400b00e06f77)DFSR\_WRITE\_MASK

| #define DFSR\_WRITE\_MASK   (1 << 11) |
| --- |

## [◆ ](#a96123c0224b549def3a8fd4cc5530e43)F\_BIT

| #define F\_BIT   (1 << 6) |
| --- |

## [◆ ](#a814e21f8d57ac2486be3c095f159215f)FPEXC\_EN

| #define FPEXC\_EN   (1 << 30) |
| --- |

## [◆ ](#a958d9c5f047f5dc318ecf4b171a68949)GET\_MPIDR

| #define GET\_MPIDR | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[read\_sysreg](cortex__a__r_2lib__helpers_8h.md#abf4f1c14ffe7c2d5b2bfa605615e676d)(mpidr)

[read\_sysreg](cortex__a__r_2lib__helpers_8h.md#abf4f1c14ffe7c2d5b2bfa605615e676d)

#define read\_sysreg(reg)

**Definition** lib\_helpers.h:100

## [◆ ](#a2df77921af208fb2202cb6d03a9ea004)GICV3\_SGIR\_VALUE

| #define GICV3\_SGIR\_VALUE | ( |  | *\_aff3*, |
| --- | --- | --- | --- |
|  |  |  | *\_aff2*, |
|  |  |  | *\_aff1*, |
|  |  |  | *\_intid*, |
|  |  |  | *\_irm*, |
|  |  |  | *\_tgt* ) |

**Value:**

(((([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) (\_aff3) & [SGIR\_AFF\_MASK](#aaebf9f7f5e67965fac91a7eb0336f3e4)) << [SGIR\_AFF3\_SHIFT](#ac4364d68d92dd7b7e1bb7ffac6e81eef)) | \

((([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) (\_irm) & [SGIR\_IRM\_MASK](#a31c2a71ebf8c2e296f0c8417012ca7f4)) << [SGIR\_IRM\_SHIFT](#a0a9ae05724f25a9f9e55e664823eeb6b)) | \

((([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) (\_aff2) & [SGIR\_AFF\_MASK](#aaebf9f7f5e67965fac91a7eb0336f3e4)) << [SGIR\_AFF2\_SHIFT](#afcb9746b2d5edfd88af4af2759c931d7)) | \

(((\_intid) & [SGIR\_INTID\_MASK](#a6e5a1e0b98322addaa87188e4d9a03f1)) << [SGIR\_INTID\_SHIFT](#a9bd0096ceb2f20d31173b61127dc5bd3)) | \

(((\_aff1) & [SGIR\_AFF\_MASK](#aaebf9f7f5e67965fac91a7eb0336f3e4)) << [SGIR\_AFF1\_SHIFT](#a54fd53204f64c9081d7c0c9fc3209c37)) | \

((\_tgt) & [SGIR\_TGT\_MASK](#aef12617a687736364283ba5fc45eb29a)))

[SGIR\_IRM\_SHIFT](#a0a9ae05724f25a9f9e55e664823eeb6b)

#define SGIR\_IRM\_SHIFT

**Definition** cpu.h:107

[SGIR\_IRM\_MASK](#a31c2a71ebf8c2e296f0c8417012ca7f4)

#define SGIR\_IRM\_MASK

**Definition** cpu.h:108

[SGIR\_AFF1\_SHIFT](#a54fd53204f64c9081d7c0c9fc3209c37)

#define SGIR\_AFF1\_SHIFT

**Definition** cpu.h:101

[SGIR\_INTID\_MASK](#a6e5a1e0b98322addaa87188e4d9a03f1)

#define SGIR\_INTID\_MASK

**Definition** cpu.h:106

[SGIR\_INTID\_SHIFT](#a9bd0096ceb2f20d31173b61127dc5bd3)

#define SGIR\_INTID\_SHIFT

**Definition** cpu.h:105

[SGIR\_AFF\_MASK](#aaebf9f7f5e67965fac91a7eb0336f3e4)

#define SGIR\_AFF\_MASK

**Definition** cpu.h:104

[SGIR\_AFF3\_SHIFT](#ac4364d68d92dd7b7e1bb7ffac6e81eef)

#define SGIR\_AFF3\_SHIFT

**Definition** cpu.h:103

[SGIR\_TGT\_MASK](#aef12617a687736364283ba5fc45eb29a)

#define SGIR\_TGT\_MASK

**Definition** cpu.h:100

[SGIR\_AFF2\_SHIFT](#afcb9746b2d5edfd88af4af2759c931d7)

#define SGIR\_AFF2\_SHIFT

**Definition** cpu.h:102

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

## [◆ ](#a7d34434117254b1745ff62a40f850455)HACTLR\_BUSTIMEOUTR\_BIT

| #define HACTLR\_BUSTIMEOUTR\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#af6034c7fd77f1096314b8753ddd83621)HACTLR\_CDBGDCI

| #define HACTLR\_CDBGDCI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a367fbf6725426a0cb44a01cd7d3bbac4)HACTLR\_CPUACTLR

| #define HACTLR\_CPUACTLR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ae245fc7db7d6db0279d6da680de1981f)HACTLR\_ERR\_BIT

| #define HACTLR\_ERR\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

## [◆ ](#a6161c9da01ec5a54597681bc187e2c40)HACTLR\_FLASHIFREGIONR

| #define HACTLR\_FLASHIFREGIONR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#aa417d6d641a116d5e2d3eaf6a56b1cc8)HACTLR\_INIT

| #define HACTLR\_INIT |
| --- |

**Value:**

([HACTLR\_ERR\_BIT](#ae245fc7db7d6db0279d6da680de1981f) | [HACTLR\_INTMONR\_BIT](#a4f2b59b38069f9b4ddcd879bd666a9df) | \

[HACTLR\_BUSTIMEOUTR\_BIT](#a7d34434117254b1745ff62a40f850455) | [HACTLR\_QOSR\_BIT](#ada072a55f7ba6970e29472d7ca78d967) | \

[HACTLR\_PERIPHPREGIONR](#a054011b021f935829db1fe81688a2efa) | [HACTLR\_FLASHIFREGIONR](#a6161c9da01ec5a54597681bc187e2c40) | \

[HACTLR\_CDBGDCI](#af6034c7fd77f1096314b8753ddd83621) | [HACTLR\_CPUACTLR](#a367fbf6725426a0cb44a01cd7d3bbac4))

[HACTLR\_PERIPHPREGIONR](#a054011b021f935829db1fe81688a2efa)

#define HACTLR\_PERIPHPREGIONR

**Definition** cpu.h:66

[HACTLR\_CPUACTLR](#a367fbf6725426a0cb44a01cd7d3bbac4)

#define HACTLR\_CPUACTLR

**Definition** cpu.h:63

[HACTLR\_INTMONR\_BIT](#a4f2b59b38069f9b4ddcd879bd666a9df)

#define HACTLR\_INTMONR\_BIT

**Definition** cpu.h:69

[HACTLR\_FLASHIFREGIONR](#a6161c9da01ec5a54597681bc187e2c40)

#define HACTLR\_FLASHIFREGIONR

**Definition** cpu.h:65

[HACTLR\_BUSTIMEOUTR\_BIT](#a7d34434117254b1745ff62a40f850455)

#define HACTLR\_BUSTIMEOUTR\_BIT

**Definition** cpu.h:68

[HACTLR\_QOSR\_BIT](#ada072a55f7ba6970e29472d7ca78d967)

#define HACTLR\_QOSR\_BIT

**Definition** cpu.h:67

[HACTLR\_ERR\_BIT](#ae245fc7db7d6db0279d6da680de1981f)

#define HACTLR\_ERR\_BIT

**Definition** cpu.h:70

[HACTLR\_CDBGDCI](#af6034c7fd77f1096314b8753ddd83621)

#define HACTLR\_CDBGDCI

**Definition** cpu.h:64

## [◆ ](#a4f2b59b38069f9b4ddcd879bd666a9df)HACTLR\_INTMONR\_BIT

| #define HACTLR\_INTMONR\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#a054011b021f935829db1fe81688a2efa)HACTLR\_PERIPHPREGIONR

| #define HACTLR\_PERIPHPREGIONR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#ada072a55f7ba6970e29472d7ca78d967)HACTLR\_QOSR\_BIT

| #define HACTLR\_QOSR\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#a5c62a691b1161751afa302c0aa64f85d)HIVECS

| #define HIVECS   (1 << 13) |
| --- |

## [◆ ](#a419c15bf37a7aaea28a4bea82b8c4421)HSCTLR\_RES1

| #define HSCTLR\_RES1 |
| --- |

**Value:**

([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) | \

BIT(22) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) | \

BIT(11) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3))

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

## [◆ ](#aee2152981b17e0fd7752a41c038f42ad)I\_BIT

| #define I\_BIT   (1 << 7) |
| --- |

## [◆ ](#a89642941ffefc853013b0f92cc80f131)ICC\_SRE\_EL3\_EN\_BIT

| #define ICC\_SRE\_EL3\_EN\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a54ea5ad3d9d0c66c5787b4c10feaeffb)ICC\_SRE\_ELx\_DFB\_BIT

| #define ICC\_SRE\_ELx\_DFB\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a6464acd03121adf32b11764b8e16a59f)ICC\_SRE\_ELx\_DIB\_BIT

| #define ICC\_SRE\_ELx\_DIB\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a581240d06f8f27d299a303941934d0a9)ICC\_SRE\_ELx\_SRE\_BIT

| #define ICC\_SRE\_ELx\_SRE\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a75f8757e1d238418b64ef59fc09e5e94)MODE\_ABT

| #define MODE\_ABT   0x17 |
| --- |

## [◆ ](#a2d95aed11b5420eb0d67884b39e984f4)MODE\_FIQ

| #define MODE\_FIQ   0x11 |
| --- |

## [◆ ](#a6557422114a234fff334a90634283b02)MODE\_HYP

| #define MODE\_HYP   0x1a |
| --- |

## [◆ ](#ae3e562974dac9a93ece87414925c8c7e)MODE\_IRQ

| #define MODE\_IRQ   0x12 |
| --- |

## [◆ ](#aba2b187200eec47c5fc32655e296783d)MODE\_MASK

| #define MODE\_MASK   0x1f |
| --- |

## [◆ ](#a9266f9bd89f1bccd0b3b5e8825ab654c)MODE\_SVC

| #define MODE\_SVC   0x13 |
| --- |

## [◆ ](#ac5fe4951d03afe9d7e282e754b655f7e)MODE\_SYS

| #define MODE\_SYS   0x1f |
| --- |

## [◆ ](#aade1410afb684e0540924f289ba68f23)MODE\_UND

| #define MODE\_UND   0x1b |
| --- |

## [◆ ](#a7b9e6e5e6ca9a4011ff55154df4d2e6e)MODE\_USR

| #define MODE\_USR   0x10 |
| --- |

## [◆ ](#a7a2087ca83455cf2759a5aee220105e2)MPIDR\_AFF0\_SHIFT

| #define MPIDR\_AFF0\_SHIFT   (0) |
| --- |

## [◆ ](#a3a7ffd9f7a014257a725513d531edab2)MPIDR\_AFF1\_SHIFT

| #define MPIDR\_AFF1\_SHIFT   (8) |
| --- |

## [◆ ](#a61d65102667e48cb00b7f9133dcd60f2)MPIDR\_AFF2\_SHIFT

| #define MPIDR\_AFF2\_SHIFT   (16) |
| --- |

## [◆ ](#a35278aa57b0b98cd0cb541cfea58b177)MPIDR\_AFFLVL

| #define MPIDR\_AFFLVL | ( |  | *mpidr*, |
| --- | --- | --- | --- |
|  |  |  | *aff\_level* ) |

**Value:**

(((mpidr) >> MPIDR\_AFF##aff\_level##\_SHIFT) & [MPIDR\_AFFLVL\_MASK](#a9bce40a5c0fceea5298a899b174c3e1c))

[MPIDR\_AFFLVL\_MASK](#a9bce40a5c0fceea5298a899b174c3e1c)

#define MPIDR\_AFFLVL\_MASK

**Definition** cpu.h:87

## [◆ ](#a9bce40a5c0fceea5298a899b174c3e1c)MPIDR\_AFFLVL\_MASK

| #define MPIDR\_AFFLVL\_MASK   (0xff) |
| --- |

## [◆ ](#a850e9ad6314a72da4ef5ff09d5e1e024)MPIDR\_TO\_CORE

| #define MPIDR\_TO\_CORE | ( |  | *mpidr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[MPIDR\_AFFLVL](#a35278aa57b0b98cd0cb541cfea58b177)(mpidr, 0)

[MPIDR\_AFFLVL](#a35278aa57b0b98cd0cb541cfea58b177)

#define MPIDR\_AFFLVL(mpidr, aff\_level)

**Definition** cpu.h:93

## [◆ ](#ad9dc6fc20549b11dc1b2cc5ed02d5ee7)SCTLR\_A\_BIT

| #define SCTLR\_A\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a752ac38bb53a96c6749fbfc09a1fb88d)SCTLR\_C\_BIT

| #define SCTLR\_C\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#ac9fd86e6613531ab567031f4c02a2900)SCTLR\_I\_BIT

| #define SCTLR\_I\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#a223e38830566f400f6d592a6bb7dd361)SCTLR\_M\_BIT

| #define SCTLR\_M\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#aa78d7bae99df2480a96055226477b726)SCTLR\_MPU\_ENABLE

| #define SCTLR\_MPU\_ENABLE   (1 << 0) |
| --- |

## [◆ ](#a54fd53204f64c9081d7c0c9fc3209c37)SGIR\_AFF1\_SHIFT

| #define SGIR\_AFF1\_SHIFT   (16) |
| --- |

## [◆ ](#afcb9746b2d5edfd88af4af2759c931d7)SGIR\_AFF2\_SHIFT

| #define SGIR\_AFF2\_SHIFT   (32) |
| --- |

## [◆ ](#ac4364d68d92dd7b7e1bb7ffac6e81eef)SGIR\_AFF3\_SHIFT

| #define SGIR\_AFF3\_SHIFT   (48) |
| --- |

## [◆ ](#aaebf9f7f5e67965fac91a7eb0336f3e4)SGIR\_AFF\_MASK

| #define SGIR\_AFF\_MASK   (0xff) |
| --- |

## [◆ ](#a6e5a1e0b98322addaa87188e4d9a03f1)SGIR\_INTID\_MASK

| #define SGIR\_INTID\_MASK   (0xf) |
| --- |

## [◆ ](#a9bd0096ceb2f20d31173b61127dc5bd3)SGIR\_INTID\_SHIFT

| #define SGIR\_INTID\_SHIFT   (24) |
| --- |

## [◆ ](#a31c2a71ebf8c2e296f0c8417012ca7f4)SGIR\_IRM\_MASK

| #define SGIR\_IRM\_MASK   (0x1) |
| --- |

## [◆ ](#a0a9ae05724f25a9f9e55e664823eeb6b)SGIR\_IRM\_SHIFT

| #define SGIR\_IRM\_SHIFT   (40) |
| --- |

## [◆ ](#a410f4b9c7089a847d01bc6592335871f)SGIR\_IRM\_TO\_AFF

| #define SGIR\_IRM\_TO\_AFF   (0) |
| --- |

## [◆ ](#aef12617a687736364283ba5fc45eb29a)SGIR\_TGT\_MASK

| #define SGIR\_TGT\_MASK   (0xffff) |
| --- |

## [◆ ](#ace344d543daa81e5cbfbba5fabb29d27)T\_BIT

| #define T\_BIT   (1 << 5) |
| --- |

## [◆ ](#a2d4fcd4a7bb1c87080f5795d0f531703)VBAR\_MASK

| #define VBAR\_MASK   (0xFFFFFFE0U) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [cpu.h](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
