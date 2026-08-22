---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvideo__control.html
original_path: doxygen/html/structvideo__control.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_control Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Controls](group__video__controls.md)

Video control structure.
[More...](#details)

`#include <[zephyr/drivers/video-controls.h](video-controls_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#a9ff5d90ec4ccb2b23dbd84c0eacdad75) |
|  | control id |
| union { |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [val](#a9068d0a2e351688a9077e607042a4ed3) |  |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)   [val64](#ab0504077a3dcc37f5781a54baeb1e65f) |  |
| }; |  |
|  | control value |

## Detailed Description

Video control structure.

Used to get/set a video control.

See also
:   video\_ctrl for the struct used in the driver implementation

## Field Documentation

## [◆ ](#a3719fb43329e574ae075b944ba5106bb)[union]

| union { ... } [video\_control](structvideo__control.md) |
| --- |

control value

## [◆ ](#a9ff5d90ec4ccb2b23dbd84c0eacdad75)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_control::id |
| --- |

control id

## [◆ ](#a9068d0a2e351688a9077e607042a4ed3)val

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) video\_control::val |
| --- |

## [◆ ](#ab0504077a3dcc37f5781a54baeb1e65f)val64

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) video\_control::val64 |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video-controls.h](video-controls_8h_source.md)

- [video\_control](structvideo__control.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
