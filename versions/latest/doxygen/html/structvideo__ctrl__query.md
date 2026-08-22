---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvideo__ctrl__query.html
original_path: doxygen/html/structvideo__ctrl__query.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_ctrl\_query Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Controls](group__video__controls.md)

`#include <[zephyr/drivers/video-controls.h](video-controls_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#aa534262295f6bf6816222d32f2b0986a) |
|  | device being queried, application needs to set this field |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#a9444f2b8c981e61ec1b01a498b3d5506) |
|  | control id, application needs to set this field |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [type](#a5a9cc00ce51abb9e3748100dc5d9403e) |
|  | control type |
| const char \* | [name](#a0b2744becc777f7465fd9981c9e639f6) |
|  | control name |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#afc3e9b8a15e2d4eb04b17e0f7cd6a8cb) |
|  | control flags |
| struct [video\_ctrl\_range](structvideo__ctrl__range.md) | [range](#a37ac4deb89a9d5e4b30ff9293301feb5) |
|  | control range |
| union { |  |
| const char \*const \*   [menu](#a56323de13c279c678ffcddc2ea355eea) |  |
| const [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*   [int\_menu](#ad0d74a650e83dece50ca2d46d9e5c750) |  |
| }; |  |
|  | menu if control is of menu type |

## Field Documentation

## [◆ ](#a5eb80d1e5f5973024847f7a49a84d232)[union]

| union { ... } [video\_ctrl\_query](structvideo__ctrl__query.md) |
| --- |

menu if control is of menu type

## [◆ ](#aa534262295f6bf6816222d32f2b0986a)dev

| const struct [device](structdevice.md)\* video\_ctrl\_query::dev |
| --- |

device being queried, application needs to set this field

## [◆ ](#afc3e9b8a15e2d4eb04b17e0f7cd6a8cb)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_ctrl\_query::flags |
| --- |

control flags

## [◆ ](#a9444f2b8c981e61ec1b01a498b3d5506)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_ctrl\_query::id |
| --- |

control id, application needs to set this field

## [◆ ](#ad0d74a650e83dece50ca2d46d9e5c750)int\_menu

| const [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)\* video\_ctrl\_query::int\_menu |
| --- |

## [◆ ](#a56323de13c279c678ffcddc2ea355eea)menu

| const char\* const\* video\_ctrl\_query::menu |
| --- |

## [◆ ](#a0b2744becc777f7465fd9981c9e639f6)name

| const char\* video\_ctrl\_query::name |
| --- |

control name

## [◆ ](#a37ac4deb89a9d5e4b30ff9293301feb5)range

| struct [video\_ctrl\_range](structvideo__ctrl__range.md) video\_ctrl\_query::range |
| --- |

control range

## [◆ ](#a5a9cc00ce51abb9e3748100dc5d9403e)type

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_ctrl\_query::type |
| --- |

control type

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video-controls.h](video-controls_8h_source.md)

- [video\_ctrl\_query](structvideo__ctrl__query.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
