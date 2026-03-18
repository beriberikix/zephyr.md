---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structvideo__caps.html
original_path: doxygen/html/structvideo__caps.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_caps Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

Video format capabilities.
[More...](#details)

`#include <[video.h](video_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [video\_format\_cap](structvideo__format__cap.md) \* | [format\_caps](#adb454a88504d9fd6e40510171a53b185) |
|  | list of video format capabilities (zero terminated). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [min\_vbuf\_count](#a2b2604a36a2f7a5013d9383ab5ef198a) |
|  | minimal count of video buffers to enqueue before being able to start the stream. |

## Detailed Description

Video format capabilities.

Used to describe video endpoint capabilities.

## Field Documentation

## [◆ ](#adb454a88504d9fd6e40510171a53b185)format\_caps

| const struct [video\_format\_cap](structvideo__format__cap.md)\* video\_caps::format\_caps |
| --- |

list of video format capabilities (zero terminated).

## [◆ ](#a2b2604a36a2f7a5013d9383ab5ef198a)min\_vbuf\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) video\_caps::min\_vbuf\_count |
| --- |

minimal count of video buffers to enqueue before being able to start the stream.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_caps](structvideo__caps.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
