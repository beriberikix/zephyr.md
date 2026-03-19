---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mmu_2arm__mmu_8h.html
original_path: doxygen/html/mmu_2arm__mmu_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mmu.h File Reference

[Go to the source code of this file.](mmu_2arm__mmu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arm\_mmu\_region](structarm__mmu__region.md) |
| struct | [arm\_mmu\_config](structarm__mmu__config.md) |

| Macros | |
| --- | --- |
| #define | [MT\_STRONGLY\_ORDERED](#aef13623eed6a774294ff117f0f1260d3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [MT\_DEVICE](#ab0d5bcaf320e734ca524c213bb950de1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [MT\_NORMAL](#a8b006dab179dfa8965dcef3ac302746d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [MT\_MASK](#aea34d2f5ddb576d5d54a82fa63778ce1)   0x7 |
| #define | [MPERM\_R](#a798d4c3b727dc70d39bdce4485e75b63)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [MPERM\_W](#a3a8f3c247e82832a527c9998daddab51)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [MPERM\_X](#a18d392d8f4282d5e0f4b7b4950667a10)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [MPERM\_UNPRIVILEGED](#abcbc3a051ff2302bfcf9496220f572b1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [MATTR\_NON\_SECURE](#a8a5663c1705ebc0fed3165acedee100b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [MATTR\_NON\_GLOBAL](#a674920d803fe277dd364d324bd9de3d3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [MATTR\_SHARED](#a61a894a354c54f67395d0e9293e4cf31)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [MATTR\_CACHE\_OUTER\_WB\_WA](#a67253d34ae4dc883c58116c1354f3e2d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [MATTR\_CACHE\_OUTER\_WT\_nWA](#a47edb43bfd4a767ed8365d78aca9d4a6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [MATTR\_CACHE\_OUTER\_WB\_nWA](#a875777d8e87e20dc861d0439ddfcfd19)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [MATTR\_CACHE\_INNER\_WB\_WA](#aefd9b92f9576e6565d02cd1902d97d33)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| #define | [MATTR\_CACHE\_INNER\_WT\_nWA](#a21ace71b252adcf3ef4903c28feb9254)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| #define | [MATTR\_CACHE\_INNER\_WB\_nWA](#aa864871d6a9bcd964b356d16d284e6fa)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| #define | [MATTR\_MAY\_MAP\_L1\_SECTION](#afa2923609302c3ae56b387ae2cc7d28f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| #define | [MMU\_REGION\_ENTRY](#a7ab46a0bcc5d7f2645f98067ed78ac8f)(\_name, \_base\_pa, \_base\_va, \_size, \_attrs) |
| #define | [MMU\_REGION\_FLAT\_ENTRY](#a7a9f450388792a5c053dd227207d255f)(name, adr, sz, attrs) |
| #define | [MMU\_REGION\_DT\_FLAT\_ENTRY](#a345c9537de9d7439c853b7f5c275d0cf)(node\_id, attrs) |
| #define | [MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY](#a3266a39e2c823047ab9a9162be60daf4)(compat, attr) |

| Variables | |
| --- | --- |
| const struct [arm\_mmu\_config](structarm__mmu__config.md) | [mmu\_config](#afb6753aab93fd940c3fc43c11a908216) |

## Macro Definition Documentation

## [◆ ](#aa864871d6a9bcd964b356d16d284e6fa)MATTR\_CACHE\_INNER\_WB\_nWA

| #define MATTR\_CACHE\_INNER\_WB\_nWA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

## [◆ ](#aefd9b92f9576e6565d02cd1902d97d33)MATTR\_CACHE\_INNER\_WB\_WA

| #define MATTR\_CACHE\_INNER\_WB\_WA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

## [◆ ](#a21ace71b252adcf3ef4903c28feb9254)MATTR\_CACHE\_INNER\_WT\_nWA

| #define MATTR\_CACHE\_INNER\_WT\_nWA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

## [◆ ](#a875777d8e87e20dc861d0439ddfcfd19)MATTR\_CACHE\_OUTER\_WB\_nWA

| #define MATTR\_CACHE\_OUTER\_WB\_nWA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#a67253d34ae4dc883c58116c1354f3e2d)MATTR\_CACHE\_OUTER\_WB\_WA

| #define MATTR\_CACHE\_OUTER\_WB\_WA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#a47edb43bfd4a767ed8365d78aca9d4a6)MATTR\_CACHE\_OUTER\_WT\_nWA

| #define MATTR\_CACHE\_OUTER\_WT\_nWA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#afa2923609302c3ae56b387ae2cc7d28f)MATTR\_MAY\_MAP\_L1\_SECTION

| #define MATTR\_MAY\_MAP\_L1\_SECTION   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| --- |

## [◆ ](#a674920d803fe277dd364d324bd9de3d3)MATTR\_NON\_GLOBAL

| #define MATTR\_NON\_GLOBAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#a8a5663c1705ebc0fed3165acedee100b)MATTR\_NON\_SECURE

| #define MATTR\_NON\_SECURE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a61a894a354c54f67395d0e9293e4cf31)MATTR\_SHARED

| #define MATTR\_SHARED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#a3266a39e2c823047ab9a9162be60daf4)MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY

| #define MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY | ( |  | *compat*, |
| --- | --- | --- | --- |
|  |  |  | *attr* ) |

**Value:**

[DT\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga99cf30d6cf4847ed99ba7d81ad2b49d0)(compat, \

[MMU\_REGION\_DT\_FLAT\_ENTRY](#a345c9537de9d7439c853b7f5c275d0cf), attr)

[DT\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga99cf30d6cf4847ed99ba7d81ad2b49d0)

#define DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn,...)

Invokes fn for each status okay node of a compatible with multiple arguments.

**Definition** devicetree.h:3408

[MMU\_REGION\_DT\_FLAT\_ENTRY](#a345c9537de9d7439c853b7f5c275d0cf)

#define MMU\_REGION\_DT\_FLAT\_ENTRY(node\_id, attrs)

**Definition** arm\_mmu.h:86

## [◆ ](#a345c9537de9d7439c853b7f5c275d0cf)MMU\_REGION\_DT\_FLAT\_ENTRY

| #define MMU\_REGION\_DT\_FLAT\_ENTRY | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *attrs* ) |

**Value:**

[MMU\_REGION\_FLAT\_ENTRY](#a7a9f450388792a5c053dd227207d255f)([DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)(node\_id), \

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id), \

[DT\_REG\_SIZE](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)(node\_id), \

attrs),

[DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)

#define DT\_NODE\_FULL\_NAME(node\_id)

Get a devicetree node's name with unit-address as a string literal.

**Definition** devicetree.h:520

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2433

[DT\_REG\_SIZE](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)

#define DT\_REG\_SIZE(node\_id)

Get a node's (only) register block size.

**Definition** devicetree.h:2454

[MMU\_REGION\_FLAT\_ENTRY](#a7a9f450388792a5c053dd227207d255f)

#define MMU\_REGION\_FLAT\_ENTRY(name, adr, sz, attrs)

**Definition** arm\_mmu.h:67

## [◆ ](#a7ab46a0bcc5d7f2645f98067ed78ac8f)MMU\_REGION\_ENTRY

| #define MMU\_REGION\_ENTRY | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_base\_pa*, |
|  |  |  | *\_base\_va*, |
|  |  |  | *\_size*, |
|  |  |  | *\_attrs* ) |

**Value:**

{\

.name = \_name, \

.base\_pa = \_base\_pa, \

.base\_va = \_base\_va, \

.size = \_size, \

.attrs = \_attrs, \

}

## [◆ ](#a7a9f450388792a5c053dd227207d255f)MMU\_REGION\_FLAT\_ENTRY

| #define MMU\_REGION\_FLAT\_ENTRY | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *adr*, |
|  |  |  | *sz*, |
|  |  |  | *attrs* ) |

**Value:**

[MMU\_REGION\_ENTRY](#a7ab46a0bcc5d7f2645f98067ed78ac8f)(name, adr, adr, sz, attrs)

[MMU\_REGION\_ENTRY](#a7ab46a0bcc5d7f2645f98067ed78ac8f)

#define MMU\_REGION\_ENTRY(\_name, \_base\_pa, \_base\_va, \_size, \_attrs)

**Definition** arm\_mmu.h:58

## [◆ ](#a798d4c3b727dc70d39bdce4485e75b63)MPERM\_R

| #define MPERM\_R   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#abcbc3a051ff2302bfcf9496220f572b1)MPERM\_UNPRIVILEGED

| #define MPERM\_UNPRIVILEGED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a3a8f3c247e82832a527c9998daddab51)MPERM\_W

| #define MPERM\_W   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a18d392d8f4282d5e0f4b7b4950667a10)MPERM\_X

| #define MPERM\_X   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#ab0d5bcaf320e734ca524c213bb950de1)MT\_DEVICE

| #define MT\_DEVICE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#aea34d2f5ddb576d5d54a82fa63778ce1)MT\_MASK

| #define MT\_MASK   0x7 |
| --- |

## [◆ ](#a8b006dab179dfa8965dcef3ac302746d)MT\_NORMAL

| #define MT\_NORMAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#aef13623eed6a774294ff117f0f1260d3)MT\_STRONGLY\_ORDERED

| #define MT\_STRONGLY\_ORDERED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## Variable Documentation

## [◆ ](#afb6753aab93fd940c3fc43c11a908216)mmu\_config

| | const struct [arm\_mmu\_config](structarm__mmu__config.md) mmu\_config | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mmu](dir_f6f11dc85c806d5d35780c9904432735.md)
- [arm\_mmu.h](mmu_2arm__mmu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
