---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structvideo__frmival__enum.html
original_path: doxygen/html/structvideo__frmival__enum.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_frmival\_enum Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

Video frame interval enumeration structure.
[More...](#details)

`#include <[video.h](video_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [index](#a7654ce36fd942885b193da57579d88ed) |
|  | frame interval index during enumeration |
| const struct [video\_format](structvideo__format.md) \* | [format](#a8c103777cd5db24a2197ef994b8d008d) |
|  | video format for which the query is made |
| enum [video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1) | [type](#aec62b54ed1152d6b3ea80c24ce7624f7) |
|  | frame interval type the device supports |
| union { |  |
| struct [video\_frmival](structvideo__frmival.md)   [discrete](#af22ef303cdc75fd48b698ff72b57354c) |  |
| struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md)   [stepwise](#aa3fda4e99646bff1d902198437982124) |  |
| }; |  |
|  | the actual frame interval |

## Detailed Description

Video frame interval enumeration structure.

Used to describe the supported video frame intervals of a given video format.

## Field Documentation

## [◆ ](#abc899c4c0372fceb52f1afcc408b2815)[union]

| union { ... } [video\_frmival\_enum](structvideo__frmival__enum.md) |
| --- |

the actual frame interval

## [◆ ](#af22ef303cdc75fd48b698ff72b57354c)discrete

| struct [video\_frmival](structvideo__frmival.md) video\_frmival\_enum::discrete |
| --- |

## [◆ ](#a8c103777cd5db24a2197ef994b8d008d)format

| const struct [video\_format](structvideo__format.md)\* video\_frmival\_enum::format |
| --- |

video format for which the query is made

## [◆ ](#a7654ce36fd942885b193da57579d88ed)index

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_frmival\_enum::index |
| --- |

frame interval index during enumeration

## [◆ ](#aa3fda4e99646bff1d902198437982124)stepwise

| struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) video\_frmival\_enum::stepwise |
| --- |

## [◆ ](#aec62b54ed1152d6b3ea80c24ce7624f7)type

| enum [video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1) video\_frmival\_enum::type |
| --- |

frame interval type the device supports

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_frmival\_enum](structvideo__frmival__enum.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
