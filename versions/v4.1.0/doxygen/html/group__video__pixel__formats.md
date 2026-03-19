---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__video__pixel__formats.html
original_path: doxygen/html/group__video__pixel__formats.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Video pixel formats

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

The | characters separate the pixels, and spaces separate the bytes.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)(a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Four-character-code uniquely identifying the pixel format. |
| #define | [VIDEO\_FOURCC\_FROM\_STR](#gafc6c4cb871f15464f2b7df86d91fd8f3)(str) |
|  | Convert a four-character-string to a four-character-code. |

| Functions | |
| --- | --- |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [video\_bits\_per\_pixel](#gabdbd1b0f40af6663d81402deefdd387f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pixfmt) |
|  | Get number of bits per pixel of a pixel format. |

| Bayer formats (R, G, B channels). | |
| --- | --- |
| The full color information is spread over multiple pixels. | |
| #define | [VIDEO\_PIX\_FMT\_BGGR8](#ga64ad74bb6c92041a4190614b684ae024)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'A', '8', '1') |
| #define | [VIDEO\_PIX\_FMT\_GBRG8](#gaebdfd9d4230b56f6b8533630356b8793)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', 'R', 'G') |
| #define | [VIDEO\_PIX\_FMT\_GRBG8](#ga6b9c8d43406e45927f4e9e94504eae9c)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'R', 'B', 'G') |
| #define | [VIDEO\_PIX\_FMT\_RGGB8](#ga0c98dc205b724c9e4556e41cc266d80e)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'G', 'B') |

| RGB formats | |
| --- | --- |
| Per-color (R, G, B) channels. | |
| #define | [VIDEO\_PIX\_FMT\_RGB565X](#gaf3830004bb857fa00a14d0a1209c61a8)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'R') |
|  | 5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0]. |
| #define | [VIDEO\_PIX\_FMT\_RGB565](#gaf009d0eb7dbdb3bfd8883da03478c1ec)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'P') |
|  | 5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0]. |
| #define | [VIDEO\_PIX\_FMT\_XRGB32](#ga8be24c04210f8818d75082bd710db8b1)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'X', '2', '4') |
|  | The first byte is empty (X) for each pixel. |

| YUV formats | |
| --- | --- |
| Luminance (Y) and chrominance (U, V) channels. | |
| #define | [VIDEO\_PIX\_FMT\_YUYV](#gad186d3166acec11c893ae57a0ae68f11)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', 'U', 'Y', 'V') |
|  | There is either a missing channel per pixel, U or V. |
| #define | [VIDEO\_PIX\_FMT\_XYUV32](#ga017bcbec587314f569d6d0e4fbdda351)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('X', 'Y', 'U', 'V') |
|  | The first byte is empty (X) for each pixel. |

| Compressed formats | |
| --- | --- |
| #define | [VIDEO\_PIX\_FMT\_JPEG](#ga035a13c38c4f123411547e2c40d58bd2)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('J', 'P', 'E', 'G') |
|  | Both JPEG (single frame) and Motion-JPEG (MJPEG, multiple JPEG frames concatenated). |

## Detailed Description

The | characters separate the pixels, and spaces separate the bytes.

The uppercase letter represents the most significant bit. The lowercase letters represent the rest of the bits.

## Macro Definition Documentation

## [◆ ](#gafb9e36597c39face52cd0c010df20951)VIDEO\_FOURCC

| #define VIDEO\_FOURCC | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | *c*, |
|  |  |  | *[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)* ) |

`#include <[video.h](video_8h.md)>`

**Value:**

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(a) | (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(b) << 8) | (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(c) << 16) | (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) << 24))

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Four-character-code uniquely identifying the pixel format.

## [◆ ](#gafc6c4cb871f15464f2b7df86d91fd8f3)VIDEO\_FOURCC\_FROM\_STR

| #define VIDEO\_FOURCC\_FROM\_STR | ( |  | *str* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

**Value:**

[VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)((str)[0], (str)[1], (str)[2], (str)[3])

[VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)

#define VIDEO\_FOURCC(a, b, c, d)

Four-character-code uniquely identifying the pixel format.

**Definition** video.h:822

Convert a four-character-string to a four-character-code.

Convert a string literal or variable into a four-character-code as defined by [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951).

Parameters
:   | str | String to be converted |
    | --- | --- |

Returns
:   Four-character-code.

## [◆ ](#ga64ad74bb6c92041a4190614b684ae024)VIDEO\_PIX\_FMT\_BGGR8

| #define VIDEO\_PIX\_FMT\_BGGR8   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'A', '8', '1') |
| --- |

`#include <[video.h](video_8h.md)>`

```
* | Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ...
* | Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | ...
*
```

## [◆ ](#gaebdfd9d4230b56f6b8533630356b8793)VIDEO\_PIX\_FMT\_GBRG8

| #define VIDEO\_PIX\_FMT\_GBRG8   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', 'R', 'G') |
| --- |

`#include <[video.h](video_8h.md)>`

```
* | Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | ...
* | Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ...
*
```

## [◆ ](#ga6b9c8d43406e45927f4e9e94504eae9c)VIDEO\_PIX\_FMT\_GRBG8

| #define VIDEO\_PIX\_FMT\_GRBG8   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'R', 'B', 'G') |
| --- |

`#include <[video.h](video_8h.md)>`

```
* | Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | ...
* | Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ...
*
```

## [◆ ](#ga035a13c38c4f123411547e2c40d58bd2)VIDEO\_PIX\_FMT\_JPEG

| #define VIDEO\_PIX\_FMT\_JPEG   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('J', 'P', 'E', 'G') |
| --- |

`#include <[video.h](video_8h.md)>`

Both JPEG (single frame) and Motion-JPEG (MJPEG, multiple JPEG frames concatenated).

## [◆ ](#gaf009d0eb7dbdb3bfd8883da03478c1ec)VIDEO\_PIX\_FMT\_RGB565

| #define VIDEO\_PIX\_FMT\_RGB565   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'P') |
| --- |

`#include <[video.h](video_8h.md)>`

5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0].

This 16-bit integer is then packed in little endian format over two bytes:

```
*   7......0 15.....8
* | gggBbbbb RrrrrGgg | ...
*
```

## [◆ ](#gaf3830004bb857fa00a14d0a1209c61a8)VIDEO\_PIX\_FMT\_RGB565X

| #define VIDEO\_PIX\_FMT\_RGB565X   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'R') |
| --- |

`#include <[video.h](video_8h.md)>`

5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0].

This 16-bit integer is then packed in big endian format over two bytes:

```
*   15.....8 7......0
* | RrrrrGgg gggBbbbb | ...
*
```

## [◆ ](#ga0c98dc205b724c9e4556e41cc266d80e)VIDEO\_PIX\_FMT\_RGGB8

| #define VIDEO\_PIX\_FMT\_RGGB8   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'G', 'B') |
| --- |

`#include <[video.h](video_8h.md)>`

```
* | Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ...
* | Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | ...
*
```

## [◆ ](#ga8be24c04210f8818d75082bd710db8b1)VIDEO\_PIX\_FMT\_XRGB32

| #define VIDEO\_PIX\_FMT\_XRGB32   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'X', '2', '4') |
| --- |

`#include <[video.h](video_8h.md)>`

The first byte is empty (X) for each pixel.

```
* | Xxxxxxxx Rrrrrrrr Gggggggg Bbbbbbbb | ...
*
```

## [◆ ](#ga017bcbec587314f569d6d0e4fbdda351)VIDEO\_PIX\_FMT\_XYUV32

| #define VIDEO\_PIX\_FMT\_XYUV32   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('X', 'Y', 'U', 'V') |
| --- |

`#include <[video.h](video_8h.md)>`

The first byte is empty (X) for each pixel.

```
* | Xxxxxxxx Yyyyyyyy Uuuuuuuu Vvvvvvvv | ...
*
```

## [◆ ](#gad186d3166acec11c893ae57a0ae68f11)VIDEO\_PIX\_FMT\_YUYV

| #define VIDEO\_PIX\_FMT\_YUYV   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', 'U', 'Y', 'V') |
| --- |

`#include <[video.h](video_8h.md)>`

There is either a missing channel per pixel, U or V.

The value is to be averaged over 2 pixels to get the value of individual pixel.

```
* | Yyyyyyyy Uuuuuuuu | Yyyyyyyy Vvvvvvvv | ...
*
```

## Function Documentation

## [◆ ](#gabdbd1b0f40af6663d81402deefdd387f)video\_bits\_per\_pixel()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int video\_bits\_per\_pixel | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pixfmt* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Get number of bits per pixel of a pixel format.

Parameters
:   | pixfmt | FourCC pixel format value ([Video pixel formats](group__video__pixel__formats.md "Video pixel formats")). |
    | --- | --- |

Return values
:   | 0 | if the format is unhandled or if it is variable number of bits |
    | --- | --- |
    | bit | size of one pixel for this format |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
