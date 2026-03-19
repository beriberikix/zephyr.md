---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbc12__partner__state.html
original_path: doxygen/html/structbc12__partner__state.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bc12\_partner\_state Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [BC1.2 driver APIs](group__b12__interface.md)

BC1.2 detected partner state.
[More...](#details)

`#include <[usb_bc12.h](usb__bc12_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73) | [bc12\_role](#a4da4a226fd933eea17da379687d49acf) |
| union { |  |
| struct { |  |
| enum [bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb)   [type](#adeeb33acadfa0e1a8a57b862dfad97a1) |  |
| int   [current\_ua](#a3a04b815fcc4c283d342b071dda1a0da) |  |
| int   [voltage\_uv](#a1cdea094ae13acbb46fcae6f60ec3a7b) |  |
| } |  |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [pd\_partner\_connected](#a4c1a653bd2393d79680f75afef334ac9) |  |
| } |  |
| }; |  |

## Detailed Description

BC1.2 detected partner state.

Parameters
:   | [bc12\_role](#a4da4a226fd933eea17da379687d49acf) | Current role of the BC1.2 device. |
    | --- | --- |
    | [type](#adeeb33acadfa0e1a8a57b862dfad97a1) | Charging partner type. Valid when [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73 "BC1.2 device role.") is BC12\_PORTABLE\_DEVICE. |
    | current\_ma | Current, in uA, that the charging partner provides. Valid when [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73 "BC1.2 device role.") is BC12\_PORTABLE\_DEVICE. |
    | voltage\_mv | Voltage, in uV, that the charging partner provides. Valid when [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73 "BC1.2 device role.") is BC12\_PORTABLE\_DEVICE. |
    | [pd\_partner\_connected](#a4c1a653bd2393d79680f75afef334ac9) | True if a PD partner is currently connected. Valid when [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73 "BC1.2 device role.") is BC12\_CHARGING\_PORT. |

## Field Documentation

## [◆ ](#a6d0aeca9d22ccb71b19cfb9485927ac5)[union]

| union { ... } [bc12\_partner\_state](structbc12__partner__state.md) |
| --- |

## [◆ ](#a4da4a226fd933eea17da379687d49acf)bc12\_role

| enum [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73) bc12\_partner\_state::bc12\_role |
| --- |

## [◆ ](#a3a04b815fcc4c283d342b071dda1a0da)current\_ua

| int bc12\_partner\_state::current\_ua |
| --- |

## [◆ ](#a4c1a653bd2393d79680f75afef334ac9)pd\_partner\_connected

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bc12\_partner\_state::pd\_partner\_connected |
| --- |

## [◆ ](#adeeb33acadfa0e1a8a57b862dfad97a1)type

| enum [bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb) bc12\_partner\_state::type |
| --- |

## [◆ ](#a1cdea094ae13acbb46fcae6f60ec3a7b)voltage\_uv

| int bc12\_partner\_state::voltage\_uv |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[usb\_bc12.h](usb__bc12_8h_source.md)

- [bc12\_partner\_state](structbc12__partner__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
