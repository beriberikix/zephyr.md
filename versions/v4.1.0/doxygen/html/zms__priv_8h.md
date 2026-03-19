---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/zms__priv_8h.html
original_path: doxygen/html/zms__priv_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zms\_priv.h File Reference

[Go to the source code of this file.](zms__priv_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [zms\_ate](structzms__ate.md) |
|  | ZMS Allocation Table Entry (ATE) structure. [More...](structzms__ate.md#details) |

| Macros | |
| --- | --- |
| #define | [ADDR\_SECT\_MASK](#a9d825de36817ea93e474a0fe0f171cd3)   [GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)(63, 32) |
| #define | [ADDR\_SECT\_SHIFT](#a4d57ef5332dd6732dc8a774366b8c48b)   32 |
| #define | [ADDR\_OFFS\_MASK](#aa7e50d2939fa8059c2efd455198225fa)   [GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)(31, 0) |
| #define | [SECTOR\_NUM](#a3b4d0b06717099e5f821cd51ce759b7d)(x) |
| #define | [SECTOR\_OFFSET](#ae26b2c8df9b12d757a57414b38e1cac4)(x) |
| #define | [ZMS\_BLOCK\_SIZE](#a9b40fc34a50b2f4ac97fc64fce014f4c)   32 |
| #define | [ZMS\_LOOKUP\_CACHE\_NO\_ADDR](#a2cc4fbfc9a8017246e5b474f5c8c6b42)   [GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)(63, 0) |
| #define | [ZMS\_HEAD\_ID](#a488f392646447c7532b9f84b57c331b4)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [ZMS\_VERSION\_MASK](#a4193db24b2497ae547992eedaa43f6b3)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| #define | [ZMS\_GET\_VERSION](#a7813e55b6ff100cbce70d63cb0a7bd1d)(x) |
| #define | [ZMS\_DEFAULT\_VERSION](#a441f6525635866111d9e859cdcc4ebef)   1 |
| #define | [ZMS\_MAGIC\_NUMBER](#a7b8a825d1d02681d675436d0950c63a2)   0x42 /\* murmur3a hash of "ZMS" (MSB) \*/ |
| #define | [ZMS\_MAGIC\_NUMBER\_MASK](#ae002208bc578d4e4d5a26b04fc4740a6)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 8) |
| #define | [ZMS\_GET\_MAGIC\_NUMBER](#ab9d90629ce189b666ab05ca30f47a38d)(x) |
| #define | [ZMS\_MIN\_ATE\_NUM](#a9331265598a521b8f4abb28b5cea90f6)   5 |
| #define | [ZMS\_INVALID\_SECTOR\_NUM](#a8ce9ad0d1e436bea764bad608ec75e69)   -1 |
| #define | [ZMS\_DATA\_IN\_ATE\_SIZE](#a758c42a254d0e64596c35c7ac644aedc)   8 |

## Macro Definition Documentation

## [◆ ](#aa7e50d2939fa8059c2efd455198225fa)ADDR\_OFFS\_MASK

| #define ADDR\_OFFS\_MASK   [GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)(31, 0) |
| --- |

## [◆ ](#a9d825de36817ea93e474a0fe0f171cd3)ADDR\_SECT\_MASK

| #define ADDR\_SECT\_MASK   [GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)(63, 32) |
| --- |

## [◆ ](#a4d57ef5332dd6732dc8a774366b8c48b)ADDR\_SECT\_SHIFT

| #define ADDR\_SECT\_SHIFT   32 |
| --- |

## [◆ ](#a3b4d0b06717099e5f821cd51ce759b7d)SECTOR\_NUM

| #define SECTOR\_NUM | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([ADDR\_SECT\_MASK](#a9d825de36817ea93e474a0fe0f171cd3), x)

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)

#define FIELD\_GET(mask, value)

**Definition** silabs-pinctrl-siwx91x.h:14

[ADDR\_SECT\_MASK](#a9d825de36817ea93e474a0fe0f171cd3)

#define ADDR\_SECT\_MASK

**Definition** zms\_priv.h:18

## [◆ ](#ae26b2c8df9b12d757a57414b38e1cac4)SECTOR\_OFFSET

| #define SECTOR\_OFFSET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([ADDR\_OFFS\_MASK](#aa7e50d2939fa8059c2efd455198225fa), x)

[ADDR\_OFFS\_MASK](#aa7e50d2939fa8059c2efd455198225fa)

#define ADDR\_OFFS\_MASK

**Definition** zms\_priv.h:20

## [◆ ](#a9b40fc34a50b2f4ac97fc64fce014f4c)ZMS\_BLOCK\_SIZE

| #define ZMS\_BLOCK\_SIZE   32 |
| --- |

## [◆ ](#a758c42a254d0e64596c35c7ac644aedc)ZMS\_DATA\_IN\_ATE\_SIZE

| #define ZMS\_DATA\_IN\_ATE\_SIZE   8 |
| --- |

## [◆ ](#a441f6525635866111d9e859cdcc4ebef)ZMS\_DEFAULT\_VERSION

| #define ZMS\_DEFAULT\_VERSION   1 |
| --- |

## [◆ ](#ab9d90629ce189b666ab05ca30f47a38d)ZMS\_GET\_MAGIC\_NUMBER

| #define ZMS\_GET\_MAGIC\_NUMBER | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([ZMS\_MAGIC\_NUMBER\_MASK](#ae002208bc578d4e4d5a26b04fc4740a6), x)

[ZMS\_MAGIC\_NUMBER\_MASK](#ae002208bc578d4e4d5a26b04fc4740a6)

#define ZMS\_MAGIC\_NUMBER\_MASK

**Definition** zms\_priv.h:37

## [◆ ](#a7813e55b6ff100cbce70d63cb0a7bd1d)ZMS\_GET\_VERSION

| #define ZMS\_GET\_VERSION | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([ZMS\_VERSION\_MASK](#a4193db24b2497ae547992eedaa43f6b3), x)

[ZMS\_VERSION\_MASK](#a4193db24b2497ae547992eedaa43f6b3)

#define ZMS\_VERSION\_MASK

**Definition** zms\_priv.h:33

## [◆ ](#a488f392646447c7532b9f84b57c331b4)ZMS\_HEAD\_ID

| #define ZMS\_HEAD\_ID   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#a8ce9ad0d1e436bea764bad608ec75e69)ZMS\_INVALID\_SECTOR\_NUM

| #define ZMS\_INVALID\_SECTOR\_NUM   -1 |
| --- |

## [◆ ](#a2cc4fbfc9a8017246e5b474f5c8c6b42)ZMS\_LOOKUP\_CACHE\_NO\_ADDR

| #define ZMS\_LOOKUP\_CACHE\_NO\_ADDR   [GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)(63, 0) |
| --- |

## [◆ ](#a7b8a825d1d02681d675436d0950c63a2)ZMS\_MAGIC\_NUMBER

| #define ZMS\_MAGIC\_NUMBER   0x42 /\* murmur3a hash of "ZMS" (MSB) \*/ |
| --- |

## [◆ ](#ae002208bc578d4e4d5a26b04fc4740a6)ZMS\_MAGIC\_NUMBER\_MASK

| #define ZMS\_MAGIC\_NUMBER\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 8) |
| --- |

## [◆ ](#a9331265598a521b8f4abb28b5cea90f6)ZMS\_MIN\_ATE\_NUM

| #define ZMS\_MIN\_ATE\_NUM   5 |
| --- |

## [◆ ](#a4193db24b2497ae547992eedaa43f6b3)ZMS\_VERSION\_MASK

| #define ZMS\_VERSION\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| --- |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [fs](dir_e8230ac05e3aac2b3e0e734457f44f71.md)
- [zms](dir_142391b9069c4c871a5c68dc8690aac3.md)
- [zms\_priv.h](zms__priv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
