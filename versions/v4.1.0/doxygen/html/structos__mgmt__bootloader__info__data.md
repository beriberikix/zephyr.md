---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structos__mgmt__bootloader__info__data.html
original_path: doxygen/html/structos__mgmt__bootloader__info__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

os\_mgmt\_bootloader\_info\_data Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md) » [MCUmgr os\_mgmt callback API](group__mcumgr__callback__api__os__mgmt.md)

Structure provided in the [MGMT\_EVT\_OP\_OS\_MGMT\_BOOTLOADER\_INFO](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf "Callback when a bootloader info command has been received, data is os_mgmt_bootloader_info_data().") notification callback: This callback function is used to add new fields to the bootloader info response.
[More...](#details)

`#include <[os_mgmt_callbacks.h](os__mgmt__callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| zcbor\_state\_t \* | [zse](#a0509ede3b6d0b40c0b93700a738f54cf) |
|  | The zcbor encoder which is currently being used to output group information, additional fields to the group can be added using this. |
| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | [decoded](#a19db05235f5b818dfc7e479265beee71) |
|  | Contains the number of decoded parameters. |
| struct zcbor\_string \* | [query](#add73c66753d7b66713e9fdac8a1f951f) |
|  | Contains the value of the query parameter. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | [has\_output](#a2629ccb5b8ecc9da25bed2d0ec695938) |
|  | Must be set to true to indicate a response has been added, otherwise will return the [OS\_MGMT\_ERR\_QUERY\_YIELDS\_NO\_ANSWER](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d "Query was not recognized.") error. |

## Detailed Description

Structure provided in the [MGMT\_EVT\_OP\_OS\_MGMT\_BOOTLOADER\_INFO](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf "Callback when a bootloader info command has been received, data is os_mgmt_bootloader_info_data().") notification callback: This callback function is used to add new fields to the bootloader info response.

## Field Documentation

## [◆ ](#a19db05235f5b818dfc7e479265beee71)decoded

| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)\* os\_mgmt\_bootloader\_info\_data::decoded |
| --- |

Contains the number of decoded parameters.

## [◆ ](#a2629ccb5b8ecc9da25bed2d0ec695938)has\_output

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)\* os\_mgmt\_bootloader\_info\_data::has\_output |
| --- |

Must be set to true to indicate a response has been added, otherwise will return the [OS\_MGMT\_ERR\_QUERY\_YIELDS\_NO\_ANSWER](os__mgmt_8h.md#a14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d "Query was not recognized.") error.

## [◆ ](#add73c66753d7b66713e9fdac8a1f951f)query

| struct zcbor\_string\* os\_mgmt\_bootloader\_info\_data::query |
| --- |

Contains the value of the query parameter.

## [◆ ](#a0509ede3b6d0b40c0b93700a738f54cf)zse

| zcbor\_state\_t\* os\_mgmt\_bootloader\_info\_data::zse |
| --- |

The zcbor encoder which is currently being used to output group information, additional fields to the group can be added using this.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/os\_mgmt/[os\_mgmt\_callbacks.h](os__mgmt__callbacks_8h_source.md)

- [os\_mgmt\_bootloader\_info\_data](structos__mgmt__bootloader__info__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
