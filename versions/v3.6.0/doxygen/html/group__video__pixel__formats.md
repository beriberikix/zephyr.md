---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__video__pixel__formats.html
original_path: doxygen/html/group__video__pixel__formats.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Video pixel formats

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

| Bayer formats | |
| --- | --- |
| #define | [VIDEO\_PIX\_FMT\_BGGR8](#ga64ad74bb6c92041a4190614b684ae024)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('B', 'G', 'G', 'R') /\* 8 BGBG.. GRGR.. \*/ |
|  | BGGR8 pixel format. |
| #define | [VIDEO\_PIX\_FMT\_GBRG8](#gaebdfd9d4230b56f6b8533630356b8793)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('G', 'B', 'R', 'G') /\* 8 GBGB.. RGRG.. \*/ |
|  | GBRG8 pixel format. |
| #define | [VIDEO\_PIX\_FMT\_GRBG8](#ga6b9c8d43406e45927f4e9e94504eae9c)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('G', 'R', 'B', 'G') /\* 8 GRGR.. BGBG.. \*/ |
|  | GRBG8 pixel format. |
| #define | [VIDEO\_PIX\_FMT\_RGGB8](#ga0c98dc205b724c9e4556e41cc266d80e)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('R', 'G', 'G', 'B') /\* 8 RGRG.. GBGB.. \*/ |
|  | RGGB8 pixel format. |

| RGB formats | |
| --- | --- |
| #define | [VIDEO\_PIX\_FMT\_RGB565](#gaf009d0eb7dbdb3bfd8883da03478c1ec)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('R', 'G', 'B', 'P') /\* 16 RGB-5-6-5 \*/ |
|  | RGB565 pixel format. |

| YUV formats | |
| --- | --- |
| #define | [VIDEO\_PIX\_FMT\_YUYV](#gad186d3166acec11c893ae57a0ae68f11)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('Y', 'U', 'Y', 'V') /\* 16 Y0-Cb0 Y1-Cr0 \*/ |
|  | YUYV pixel format. |

| JPEG formats | |
| --- | --- |
| #define | [VIDEO\_PIX\_FMT\_JPEG](#ga035a13c38c4f123411547e2c40d58bd2)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('J', 'P', 'E', 'G') /\* 8 JPEG \*/ |
|  | JPEG pixel format. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga64ad74bb6c92041a4190614b684ae024)VIDEO\_PIX\_FMT\_BGGR8

| #define VIDEO\_PIX\_FMT\_BGGR8   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('B', 'G', 'G', 'R') /\* 8 BGBG.. GRGR.. \*/ |
| --- |

`#include <[video.h](video_8h.md)>`

BGGR8 pixel format.

## [◆ ](#gaebdfd9d4230b56f6b8533630356b8793)VIDEO\_PIX\_FMT\_GBRG8

| #define VIDEO\_PIX\_FMT\_GBRG8   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('G', 'B', 'R', 'G') /\* 8 GBGB.. RGRG.. \*/ |
| --- |

`#include <[video.h](video_8h.md)>`

GBRG8 pixel format.

## [◆ ](#ga6b9c8d43406e45927f4e9e94504eae9c)VIDEO\_PIX\_FMT\_GRBG8

| #define VIDEO\_PIX\_FMT\_GRBG8   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('G', 'R', 'B', 'G') /\* 8 GRGR.. BGBG.. \*/ |
| --- |

`#include <[video.h](video_8h.md)>`

GRBG8 pixel format.

## [◆ ](#ga035a13c38c4f123411547e2c40d58bd2)VIDEO\_PIX\_FMT\_JPEG

| #define VIDEO\_PIX\_FMT\_JPEG   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('J', 'P', 'E', 'G') /\* 8 JPEG \*/ |
| --- |

`#include <[video.h](video_8h.md)>`

JPEG pixel format.

## [◆ ](#gaf009d0eb7dbdb3bfd8883da03478c1ec)VIDEO\_PIX\_FMT\_RGB565

| #define VIDEO\_PIX\_FMT\_RGB565   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('R', 'G', 'B', 'P') /\* 16 RGB-5-6-5 \*/ |
| --- |

`#include <[video.h](video_8h.md)>`

RGB565 pixel format.

## [◆ ](#ga0c98dc205b724c9e4556e41cc266d80e)VIDEO\_PIX\_FMT\_RGGB8

| #define VIDEO\_PIX\_FMT\_RGGB8   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('R', 'G', 'G', 'B') /\* 8 RGRG.. GBGB.. \*/ |
| --- |

`#include <[video.h](video_8h.md)>`

RGGB8 pixel format.

## [◆ ](#gad186d3166acec11c893ae57a0ae68f11)VIDEO\_PIX\_FMT\_YUYV

| #define VIDEO\_PIX\_FMT\_YUYV   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('Y', 'U', 'Y', 'V') /\* 16 Y0-Cb0 Y1-Cr0 \*/ |
| --- |

`#include <[video.h](video_8h.md)>`

YUYV pixel format.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
