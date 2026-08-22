---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structvideo__buffer.html
original_path: doxygen/html/structvideo__buffer.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_buffer Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

Video buffer structure.
[More...](#details)

`#include <[zephyr/drivers/video.h](video_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [driver\_data](#ab184d528487042650af105eb7d37381e) |
|  | Pointer to driver specific data. |
| enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) | [type](#a46dd9bd9398ff74e4f9859a07b9c48af) |
|  | type of the buffer |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buffer](#a6a62d7a50c717dc6bc85e2d8f6ae95e3) |
|  | pointer to the start of the buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [index](#acb948f9f124f9f2bfe9b19b44af60854) |
|  | index of the buffer, optionally set by the application |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [size](#a3f040775c683c91740c8bda5c96e621b) |
|  | size of the buffer in bytes. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [bytesused](#a17505a283ab5ef65047b798cb49aa9e1) |
|  | number of bytes occupied by the valid data in the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timestamp](#af5c1abf09e0047334e03afbc64226eba) |
|  | time reference in milliseconds at which the last data byte was actually received for input endpoints or to be consumed for output endpoints. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [line\_offset](#abe25963ea5e42d6fe42de1f21b554b87) |
|  | Line offset within frame this buffer represents, from the beginning of the frame. |

## Detailed Description

Video buffer structure.

Represent a video frame.

## Field Documentation

## [◆ ](#a6a62d7a50c717dc6bc85e2d8f6ae95e3)buffer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* video\_buffer::buffer |
| --- |

pointer to the start of the buffer.

## [◆ ](#a17505a283ab5ef65047b798cb49aa9e1)bytesused

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_buffer::bytesused |
| --- |

number of bytes occupied by the valid data in the buffer.

## [◆ ](#ab184d528487042650af105eb7d37381e)driver\_data

| void\* video\_buffer::driver\_data |
| --- |

Pointer to driver specific data.

## [◆ ](#acb948f9f124f9f2bfe9b19b44af60854)index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) video\_buffer::index |
| --- |

index of the buffer, optionally set by the application

## [◆ ](#abe25963ea5e42d6fe42de1f21b554b87)line\_offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) video\_buffer::line\_offset |
| --- |

Line offset within frame this buffer represents, from the beginning of the frame.

This offset is given in pixels, so [line\_offset](#abe25963ea5e42d6fe42de1f21b554b87) \* pitch provides offset from the start of the frame in bytes.

## [◆ ](#a3f040775c683c91740c8bda5c96e621b)size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_buffer::size |
| --- |

size of the buffer in bytes.

## [◆ ](#af5c1abf09e0047334e03afbc64226eba)timestamp

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_buffer::timestamp |
| --- |

time reference in milliseconds at which the last data byte was actually received for input endpoints or to be consumed for output endpoints.

## [◆ ](#a46dd9bd9398ff74e4f9859a07b9c48af)type

| enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) video\_buffer::type |
| --- |

type of the buffer

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_buffer](structvideo__buffer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
