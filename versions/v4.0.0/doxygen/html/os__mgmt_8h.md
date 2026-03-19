---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/os__mgmt_8h.html
original_path: doxygen/html/os__mgmt_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

os\_mgmt.h File Reference

[Go to the source code of this file.](os__mgmt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [os\_mgmt\_info\_check](structos__mgmt__info__check.md) |
| struct | [os\_mgmt\_info\_append](structos__mgmt__info__append.md) |

| Macros | |
| --- | --- |
| #define | [OS\_MGMT\_ID\_ECHO](#a24751ec5a8ba224238f484e2048f152a)   0 |
|  | Command IDs for OS management group. |
| #define | [OS\_MGMT\_ID\_CONS\_ECHO\_CTRL](#a0093a8df477e7114ffa195a022851cbe)   1 |
| #define | [OS\_MGMT\_ID\_TASKSTAT](#a067886d5d5d1d8979f93bab61fc2a670)   2 |
| #define | [OS\_MGMT\_ID\_MPSTAT](#aa2918e287d063fb2a82bd87d5c29aba4)   3 |
| #define | [OS\_MGMT\_ID\_DATETIME\_STR](#af4370119858111637ee80af735b0e50c)   4 |
| #define | [OS\_MGMT\_ID\_RESET](#a4447fa2fa0c5f37713f7ef555174e814)   5 |
| #define | [OS\_MGMT\_ID\_MCUMGR\_PARAMS](#a6eb9918c2e6d1564fc362fe3dcdc63d5)   6 |
| #define | [OS\_MGMT\_ID\_INFO](#a0103b1f0d37106c5166b1793c7743513)   7 |
| #define | [OS\_MGMT\_ID\_BOOTLOADER\_INFO](#a142393f94135f1dd91b8cf098e01aa6b)   8 |

| Enumerations | |
| --- | --- |
| enum | [os\_mgmt\_err\_code\_t](#a14dc9256e6585450ea34b13666aa8765) {     [OS\_MGMT\_ERR\_OK](#a14dc9256e6585450ea34b13666aa8765a25f3f37eb72fae4e2a074ee0115014f4) = 0 , [OS\_MGMT\_ERR\_UNKNOWN](#a14dc9256e6585450ea34b13666aa8765a401c167c9780d54de8af0d5a49d07752) , [OS\_MGMT\_ERR\_INVALID\_FORMAT](#a14dc9256e6585450ea34b13666aa8765a8367c0f0a31be507a67a3e981a8d14dd) , [OS\_MGMT\_ERR\_QUERY\_YIELDS\_NO\_ANSWER](#a14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d) ,     [OS\_MGMT\_ERR\_RTC\_NOT\_SET](#a14dc9256e6585450ea34b13666aa8765a654f35347c0a92d45de8c39161c0a517) , [OS\_MGMT\_ERR\_RTC\_COMMAND\_FAILED](#a14dc9256e6585450ea34b13666aa8765a110d57281369d1b5a8c1a1863dcb633a)   } |
|  | Command result codes for OS management group. [More...](#a14dc9256e6585450ea34b13666aa8765) |
| enum | [os\_mgmt\_info\_formats](#a54512f3d774835d1d277872835a3b26f) {     [OS\_MGMT\_INFO\_FORMAT\_KERNEL\_NAME](#a54512f3d774835d1d277872835a3b26faef8107b37da9f80226729774b2b658a0) = BIT(0) , [OS\_MGMT\_INFO\_FORMAT\_NODE\_NAME](#a54512f3d774835d1d277872835a3b26fa5c2b986a7e1c24e319e940193e6333e3) = BIT(1) , [OS\_MGMT\_INFO\_FORMAT\_KERNEL\_RELEASE](#a54512f3d774835d1d277872835a3b26fa16d8270fccec21d7672ce417292114bd) = BIT(2) , [OS\_MGMT\_INFO\_FORMAT\_KERNEL\_VERSION](#a54512f3d774835d1d277872835a3b26fa07febed600a0fb099942b9cc1267e328) = BIT(3) ,     [OS\_MGMT\_INFO\_FORMAT\_BUILD\_DATE\_TIME](#a54512f3d774835d1d277872835a3b26fac5667c4a29bf2c5a0183bae3d963045d) = BIT(4) , [OS\_MGMT\_INFO\_FORMAT\_MACHINE](#a54512f3d774835d1d277872835a3b26fa1d7217a77e0463c984615efa33142848) = BIT(5) , [OS\_MGMT\_INFO\_FORMAT\_PROCESSOR](#a54512f3d774835d1d277872835a3b26fa1279c1778984153bc77c0e34ee6c2082) = BIT(6) , [OS\_MGMT\_INFO\_FORMAT\_HARDWARE\_PLATFORM](#a54512f3d774835d1d277872835a3b26fa19d79c2eba087c14a4d4082d48e77fa5) = BIT(7) ,     [OS\_MGMT\_INFO\_FORMAT\_OPERATING\_SYSTEM](#a54512f3d774835d1d277872835a3b26fa6ccf1e846fb57c9957c5f1698f1fba76) = BIT(8) , [OS\_MGMT\_INFO\_FORMAT\_USER\_CUSTOM\_START](#a54512f3d774835d1d277872835a3b26fa7f409757f5912d9f950b0566896803e2) = BIT(9)   } |

## Macro Definition Documentation

## [◆ ](#a142393f94135f1dd91b8cf098e01aa6b)OS\_MGMT\_ID\_BOOTLOADER\_INFO

| #define OS\_MGMT\_ID\_BOOTLOADER\_INFO   8 |
| --- |

## [◆ ](#a0093a8df477e7114ffa195a022851cbe)OS\_MGMT\_ID\_CONS\_ECHO\_CTRL

| #define OS\_MGMT\_ID\_CONS\_ECHO\_CTRL   1 |
| --- |

## [◆ ](#af4370119858111637ee80af735b0e50c)OS\_MGMT\_ID\_DATETIME\_STR

| #define OS\_MGMT\_ID\_DATETIME\_STR   4 |
| --- |

## [◆ ](#a24751ec5a8ba224238f484e2048f152a)OS\_MGMT\_ID\_ECHO

| #define OS\_MGMT\_ID\_ECHO   0 |
| --- |

Command IDs for OS management group.

## [◆ ](#a0103b1f0d37106c5166b1793c7743513)OS\_MGMT\_ID\_INFO

| #define OS\_MGMT\_ID\_INFO   7 |
| --- |

## [◆ ](#a6eb9918c2e6d1564fc362fe3dcdc63d5)OS\_MGMT\_ID\_MCUMGR\_PARAMS

| #define OS\_MGMT\_ID\_MCUMGR\_PARAMS   6 |
| --- |

## [◆ ](#aa2918e287d063fb2a82bd87d5c29aba4)OS\_MGMT\_ID\_MPSTAT

| #define OS\_MGMT\_ID\_MPSTAT   3 |
| --- |

## [◆ ](#a4447fa2fa0c5f37713f7ef555174e814)OS\_MGMT\_ID\_RESET

| #define OS\_MGMT\_ID\_RESET   5 |
| --- |

## [◆ ](#a067886d5d5d1d8979f93bab61fc2a670)OS\_MGMT\_ID\_TASKSTAT

| #define OS\_MGMT\_ID\_TASKSTAT   2 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a14dc9256e6585450ea34b13666aa8765)os\_mgmt\_err\_code\_t

| enum [os\_mgmt\_err\_code\_t](#a14dc9256e6585450ea34b13666aa8765) |
| --- |

Command result codes for OS management group.

| Enumerator | |
| --- | --- |
| OS\_MGMT\_ERR\_OK | No error, this is implied if there is no ret value in the response. |
| OS\_MGMT\_ERR\_UNKNOWN | Unknown error occurred. |
| OS\_MGMT\_ERR\_INVALID\_FORMAT | The provided format value is not valid. |
| OS\_MGMT\_ERR\_QUERY\_YIELDS\_NO\_ANSWER | Query was not recognized. |
| OS\_MGMT\_ERR\_RTC\_NOT\_SET | RTC is not set. |
| OS\_MGMT\_ERR\_RTC\_COMMAND\_FAILED | RTC command failed. |

## [◆ ](#a54512f3d774835d1d277872835a3b26f)os\_mgmt\_info\_formats

| enum [os\_mgmt\_info\_formats](#a54512f3d774835d1d277872835a3b26f) |
| --- |

| Enumerator | |
| --- | --- |
| OS\_MGMT\_INFO\_FORMAT\_KERNEL\_NAME |  |
| OS\_MGMT\_INFO\_FORMAT\_NODE\_NAME |  |
| OS\_MGMT\_INFO\_FORMAT\_KERNEL\_RELEASE |  |
| OS\_MGMT\_INFO\_FORMAT\_KERNEL\_VERSION |  |
| OS\_MGMT\_INFO\_FORMAT\_BUILD\_DATE\_TIME |  |
| OS\_MGMT\_INFO\_FORMAT\_MACHINE |  |
| OS\_MGMT\_INFO\_FORMAT\_PROCESSOR |  |
| OS\_MGMT\_INFO\_FORMAT\_HARDWARE\_PLATFORM |  |
| OS\_MGMT\_INFO\_FORMAT\_OPERATING\_SYSTEM |  |
| OS\_MGMT\_INFO\_FORMAT\_USER\_CUSTOM\_START |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [os\_mgmt](dir_1a5ff9dfdb0e06a8ce3ba8e3db8b26fb.md)
- [os\_mgmt.h](os__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
