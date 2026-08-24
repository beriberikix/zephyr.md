---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvideo__rect.html
original_path: doxygen/html/structvideo__rect.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_rect Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

Description of a rectangle area.
[More...](#details)

`#include <[zephyr/drivers/video.h](video_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [left](#a94da5de0a4cc682556acd00fc05a8ea5) |
|  | left offset of selection rectangle |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [top](#a769fd3843bcb11211eccdd766d09d83a) |
|  | top offset of selection rectangle |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [width](#a26403179cc6d65ff6c07a4b31b1a5050) |
|  | width of selection rectangle |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [height](#a57d79483c9fc9bd800437160bd30664d) |
|  | height of selection rectangle |

## Detailed Description

Description of a rectangle area.

Used for crop/compose and possibly within drivers as well

## Field Documentation

## [◆ ](#a57d79483c9fc9bd800437160bd30664d)height

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_rect::height |
| --- |

height of selection rectangle

## [◆ ](#a94da5de0a4cc682556acd00fc05a8ea5)left

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_rect::left |
| --- |

left offset of selection rectangle

## [◆ ](#a769fd3843bcb11211eccdd766d09d83a)top

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_rect::top |
| --- |

top offset of selection rectangle

## [◆ ](#a26403179cc6d65ff6c07a4b31b1a5050)width

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_rect::width |
| --- |

width of selection rectangle

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_rect](structvideo__rect.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
