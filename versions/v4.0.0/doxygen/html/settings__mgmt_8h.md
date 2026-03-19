---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/settings__mgmt_8h.html
original_path: doxygen/html/settings__mgmt_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_mgmt.h File Reference

[Go to the source code of this file.](settings__mgmt_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SETTINGS\_MGMT\_ID\_READ\_WRITE](#aff2f915e03116c35567dfa3b61353e34)   0 |
|  | Command IDs for settings management group. |
| #define | [SETTINGS\_MGMT\_ID\_DELETE](#a1c3751a9b7a6b267f78fcc8b2b8954fb)   1 |
| #define | [SETTINGS\_MGMT\_ID\_COMMIT](#a85687e53d63edfe4d3bd55988d863e9d)   2 |
| #define | [SETTINGS\_MGMT\_ID\_LOAD\_SAVE](#a3add3a2acfcd23eb7af5df404378050c)   3 |

| Enumerations | |
| --- | --- |
| enum | [settings\_mgmt\_ret\_code\_t](#afb39b95aec3183531602aa6964ceb1cc) {     [SETTINGS\_MGMT\_ERR\_OK](#afb39b95aec3183531602aa6964ceb1ccab337460951137340ebdd8fa85d929a8f) = 0 , [SETTINGS\_MGMT\_ERR\_UNKNOWN](#afb39b95aec3183531602aa6964ceb1cca47500e585ffceef9e05006f8298e825d) , [SETTINGS\_MGMT\_ERR\_KEY\_TOO\_LONG](#afb39b95aec3183531602aa6964ceb1cca89805202eb970bdb3689067884c71a28) , [SETTINGS\_MGMT\_ERR\_KEY\_NOT\_FOUND](#afb39b95aec3183531602aa6964ceb1ccacb9f7104664f9be3d7b56bbfcbabf32f) ,     [SETTINGS\_MGMT\_ERR\_READ\_NOT\_SUPPORTED](#afb39b95aec3183531602aa6964ceb1cca93c1c519a357196a5186bf1fdaf18ae2) , [SETTINGS\_MGMT\_ERR\_ROOT\_KEY\_NOT\_FOUND](#afb39b95aec3183531602aa6964ceb1cca4ebaa41c929542cc39f32c418b406a55) , [SETTINGS\_MGMT\_ERR\_WRITE\_NOT\_SUPPORTED](#afb39b95aec3183531602aa6964ceb1cca18928efa693757f2bf564b049a9d799b) , [SETTINGS\_MGMT\_ERR\_DELETE\_NOT\_SUPPORTED](#afb39b95aec3183531602aa6964ceb1ccaacb2dafde9aed9953c5764597463762d)   } |
|  | Command result codes for settings management group. [More...](#afb39b95aec3183531602aa6964ceb1cc) |

## Macro Definition Documentation

## [◆ ](#a85687e53d63edfe4d3bd55988d863e9d)SETTINGS\_MGMT\_ID\_COMMIT

| #define SETTINGS\_MGMT\_ID\_COMMIT   2 |
| --- |

## [◆ ](#a1c3751a9b7a6b267f78fcc8b2b8954fb)SETTINGS\_MGMT\_ID\_DELETE

| #define SETTINGS\_MGMT\_ID\_DELETE   1 |
| --- |

## [◆ ](#a3add3a2acfcd23eb7af5df404378050c)SETTINGS\_MGMT\_ID\_LOAD\_SAVE

| #define SETTINGS\_MGMT\_ID\_LOAD\_SAVE   3 |
| --- |

## [◆ ](#aff2f915e03116c35567dfa3b61353e34)SETTINGS\_MGMT\_ID\_READ\_WRITE

| #define SETTINGS\_MGMT\_ID\_READ\_WRITE   0 |
| --- |

Command IDs for settings management group.

## Enumeration Type Documentation

## [◆ ](#afb39b95aec3183531602aa6964ceb1cc)settings\_mgmt\_ret\_code\_t

| enum [settings\_mgmt\_ret\_code\_t](#afb39b95aec3183531602aa6964ceb1cc) |
| --- |

Command result codes for settings management group.

| Enumerator | |
| --- | --- |
| SETTINGS\_MGMT\_ERR\_OK | No error, this is implied if there is no ret value in the response. |
| SETTINGS\_MGMT\_ERR\_UNKNOWN | Unknown error occurred. |
| SETTINGS\_MGMT\_ERR\_KEY\_TOO\_LONG | The provided key name is too long to be used. |
| SETTINGS\_MGMT\_ERR\_KEY\_NOT\_FOUND | The provided key name does not exist. |
| SETTINGS\_MGMT\_ERR\_READ\_NOT\_SUPPORTED | The provided key name does not support being read. |
| SETTINGS\_MGMT\_ERR\_ROOT\_KEY\_NOT\_FOUND | The provided root key name does not exist. |
| SETTINGS\_MGMT\_ERR\_WRITE\_NOT\_SUPPORTED | The provided key name does not support being written. |
| SETTINGS\_MGMT\_ERR\_DELETE\_NOT\_SUPPORTED | The provided key name does not support being deleted. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [settings\_mgmt](dir_f7c37d3a1c1d534b483feb4fbb3dbf95.md)
- [settings\_mgmt.h](settings__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
