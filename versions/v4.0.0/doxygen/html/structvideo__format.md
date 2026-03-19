---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structvideo__format.html
original_path: doxygen/html/structvideo__format.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_format Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

Video format structure.
[More...](#details)

`#include <[video.h](video_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pixelformat](#adb8bf2c8d59125c050cdfe160c30f5ef) |
|  | FourCC pixel format value ([Video pixel formats](group__video__pixel__formats.md "Video pixel formats")). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [width](#a7b0cc009ac03437e7e3e86b45545b693) |
|  | frame width in pixels. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [height](#a0e71fa7a0abd7740d5245021ba1acbb0) |
|  | frame height in pixels. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pitch](#aa4cd70933938ec6f52175232cf403ef6) |
|  | line stride. |

## Detailed Description

Video format structure.

Used to configure frame format.

## Field Documentation

## [◆ ](#a0e71fa7a0abd7740d5245021ba1acbb0)height

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_format::height |
| --- |

frame height in pixels.

## [◆ ](#aa4cd70933938ec6f52175232cf403ef6)pitch

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_format::pitch |
| --- |

line stride.

This is the number of bytes that needs to be added to the address in the first pixel of a row in order to go to the address of the first pixel of the next row (>=width).

## [◆ ](#adb8bf2c8d59125c050cdfe160c30f5ef)pixelformat

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_format::pixelformat |
| --- |

FourCC pixel format value ([Video pixel formats](group__video__pixel__formats.md "Video pixel formats")).

## [◆ ](#a7b0cc009ac03437e7e3e86b45545b693)width

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_format::width |
| --- |

frame width in pixels.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_format](structvideo__format.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
