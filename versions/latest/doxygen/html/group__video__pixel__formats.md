---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__video__pixel__formats.html
original_path: doxygen/html/group__video__pixel__formats.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Video pixel formats

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

The '|' characters separate the pixels or logical blocks, and spaces separate the bytes.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)(a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Four-character-code uniquely identifying the pixel format. |
| #define | [VIDEO\_FOURCC\_FROM\_STR](#gafc6c4cb871f15464f2b7df86d91fd8f3)(str) |
|  | Convert a four-character-string to a four-character-code. |
| #define | [VIDEO\_FOURCC\_TO\_STR](#gacd3805f57633c3db8c6adcd87384bd5c)(fourcc) |
|  | Convert a four-character-code to a four-character-string. |

| Functions | |
| --- | --- |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [video\_bits\_per\_pixel](#gabdbd1b0f40af6663d81402deefdd387f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pixfmt) |
|  | Get number of bits per pixel of a pixel format. |

| Bayer formats (R, G, B channels). | |
| --- | --- |
| The full color information is spread over multiple pixels.  When the format includes more than 8-bit per pixel, a strategy becomes needed to pack the bits over multiple bytes, as illustrated for each format.  The number above the 'R', 'r', 'G', 'g', 'B', 'b' are hints about which pixel number the following bits belong to. | |
| #define | [VIDEO\_PIX\_FMT\_SBGGR8](#gabc0205ce5c6426051fdec88d92f123e3)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'A', '8', '1') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG8](#gaa9edb9c562fc3c86b61e071970fae60d)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', 'R', 'G') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG8](#ga19d8dc905695229097dffe659f2a806e)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'R', 'B', 'G') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB8](#gabf0dde810e75d37823891ed03811482c)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'G', 'B') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR10P](#ga3751a8dce1c7459df06f83cd09449b5d)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'B', 'A', 'A') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG10P](#gad69ab9041428488051bdb45f42ad4271)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'G', 'A', 'A') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG10P](#gaa28c6306a3ed44a0e50c16e0eac86688)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'g', 'A', 'A') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB10P](#ga604d2f3501407546aa924e2fdb37be2f)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'R', 'A', 'A') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR12P](#gab5b5375f050d039e05032c77ac838b31)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'B', 'C', 'C') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG12P](#gaecedece3398a6e2f62c20c2eb3f6d3c2)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'G', 'C', 'C') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG12P](#ga02d91ebf4b5150d5fa437bb3a7a6e872)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'g', 'C', 'C') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB12P](#ga348c15cc77c728fdac773d58341cbc1d)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'R', 'C', 'C') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR14P](#gac3413c36b3ce91e5658cd0f973c1f3d7)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'B', 'E', 'E') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG14P](#ga89eb47d1dd60794781ee91cb5ae199ad)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'G', 'E', 'E') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG14P](#gae06f742e31a62295d3ee16af8eec1b06)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'g', 'E', 'E') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB14P](#ga66646a639518285810335a70337277d7)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'R', 'E', 'E') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR10](#ga0b55190a343fe891bdbb7b148e7feeae)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'G', '1', '0') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG10](#ga8e0f47c16483b14b45a593e9e542a987)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '0') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG10](#ga011cc337bc54480d1e11c3e6833ae398)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'A', '1', '0') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB10](#ga249cbf808658dab777a705fd9deb2986)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '0') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR12](#gaa2d7712f655dfcb3c74b4f4ec9941402)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'G', '1', '2') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG12](#gaa3df9d0af327e609b25e050a4362c2e2)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '2') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG12](#gaf18e6647596613e07ec3c651574b08ba)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'A', '1', '2') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB12](#ga7b167f2b6a147d325a685825274cd2f2)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '2') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR14](#ga403f40a7e15319365c6ca8f3f5f19d21)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'G', '1', '4') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG14](#ga6c98a7066d7d3bdd8fce3d3651772153)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '4') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG14](#gaf58481956952b13b071b1a68541b9c21)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'R', '1', '4') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB14](#gaa6e4c240372e53db8ea3472cc456af58)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '4') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR16](#gae096669643176203199270317dc3449d)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'Y', 'R', '2') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG16](#ga7f00eb633dd312ea89097edc82dc8f0c)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '6') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG16](#ga4269984ce806e64ba5ccd41c1429769a)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'R', '1', '6') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB16](#ga4f31b5d397868e952d53022c6c8e5823)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '6') |

| Grayscale formats | |
| --- | --- |
| Luminance (Y) channel only, in various bit depth and packing.  When the format includes more than 8-bit per pixel, a strategy becomes needed to pack the bits over multiple bytes, as illustrated for each format.  The number above the 'Y', 'y' are hints about which pixel number the following bits belong to. | |
| #define | [VIDEO\_PIX\_FMT\_GREY](#gaa3af19adaf282b83a6c16f265a4260dc)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'R', 'E', 'Y') |
|  | Same as Y8 (8-bit luma-only) following the standard FOURCC naming, or L8 in some graphics libraries. |
| #define | [VIDEO\_PIX\_FMT\_Y10P](#ga502df4612995fc39e03d6de3ec675159)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '0', 'P') |
| #define | [VIDEO\_PIX\_FMT\_Y12P](#ga263e6553a77d00bc509c1b270efebb0b)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '2', 'P') |
| #define | [VIDEO\_PIX\_FMT\_Y14P](#gada0124aad9c10d403966b1e3851cd968)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '4', 'P') |
| #define | [VIDEO\_PIX\_FMT\_Y10](#ga0506f2c8aa1a82f02fc9383d99b43bc3)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '0', ' ') |
|  | Little endian, with the 6 most significant bits set to Zero. |
| #define | [VIDEO\_PIX\_FMT\_Y12](#ga166b2144cec4b4f92fadda30e81b7d22)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '2', ' ') |
|  | Little endian, with the 4 most significant bits set to Zero. |
| #define | [VIDEO\_PIX\_FMT\_Y14](#ga7d9379f19abcbac17bad3d6359a42d9d)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '4', ' ') |
|  | Little endian, with the 2 most significant bits set to Zero. |
| #define | [VIDEO\_PIX\_FMT\_Y16](#gaa65fe8bd917dd2fe95fa87530fc3055f)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '6', ' ') |
|  | Little endian. |

| RGB formats | |
| --- | --- |
| Per-color (R, G, B) channels. | |
| #define | [VIDEO\_PIX\_FMT\_RGB565X](#gaf3830004bb857fa00a14d0a1209c61a8)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'R') |
|  | 5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0]. |
| #define | [VIDEO\_PIX\_FMT\_RGB565](#gaf009d0eb7dbdb3bfd8883da03478c1ec)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'P') |
|  | 5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0]. |
| #define | [VIDEO\_PIX\_FMT\_BGR24](#gaf1f8775bbdd0508c4e21a58dfcfc362d)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'G', 'R', '3') |
|  | 24 bit RGB format with 8 bit per component |
| #define | [VIDEO\_PIX\_FMT\_RGB24](#ga03e6be04b23b9735c96231eebc687158)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', '3') |
|  | 24 bit RGB format with 8 bit per component |
| #define | [VIDEO\_PIX\_FMT\_ARGB32](#ga5cd54fb54967a80576082cadd5941670)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'A', '2', '4') |
| #define | [VIDEO\_PIX\_FMT\_ABGR32](#gaffb650a5f9b2b03890283ecfe95aee04)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('A', 'R', '2', '4') |
| #define | [VIDEO\_PIX\_FMT\_RGBA32](#ga8ee1e3b82eeeb02188157aa4b4b5d842)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('A', 'B', '2', '4') |
| #define | [VIDEO\_PIX\_FMT\_BGRA32](#ga515e379bc7f59a8062f3e2a5980b0626)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'A', '2', '4') |
| #define | [VIDEO\_PIX\_FMT\_XRGB32](#ga8be24c04210f8818d75082bd710db8b1)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'X', '2', '4') |
|  | The first byte is empty (X) for each pixel. |

| YUV formats | |
| --- | --- |
| Luminance (Y) and chrominance (U, V) channels. | |
| #define | [VIDEO\_PIX\_FMT\_YUYV](#gad186d3166acec11c893ae57a0ae68f11)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', 'U', 'Y', 'V') |
|  | There is either a missing channel per pixel, U or V. |
| #define | [VIDEO\_PIX\_FMT\_YVYU](#ga299af047675a110c109cee954f55fca6)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', 'V', 'Y', 'U') |
| #define | [VIDEO\_PIX\_FMT\_VYUY](#ga63c825ce5dc6c863d355195fde40acb1)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('V', 'Y', 'U', 'Y') |
| #define | [VIDEO\_PIX\_FMT\_UYVY](#gadca3ee56c798cf05b63cbfc87af98ce3)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('U', 'Y', 'V', 'Y') |
| #define | [VIDEO\_PIX\_FMT\_XYUV32](#ga017bcbec587314f569d6d0e4fbdda351)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('X', 'Y', 'U', 'V') |
|  | The first byte is empty (X) for each pixel. |

| Compressed formats | |
| --- | --- |
| #define | [VIDEO\_PIX\_FMT\_JPEG](#ga035a13c38c4f123411547e2c40d58bd2)   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('J', 'P', 'E', 'G') |
|  | Both JPEG (single frame) and Motion-JPEG (MJPEG, multiple JPEG frames concatenated). |

## Detailed Description

The '|' characters separate the pixels or logical blocks, and spaces separate the bytes.

The uppercase letter represents the most significant bit. The lowercase letters represent the rest of the bits.

## Macro Definition Documentation

## [◆ ](#gafb9e36597c39face52cd0c010df20951)VIDEO\_FOURCC

| #define VIDEO\_FOURCC | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | *c*, |
|  |  |  | *[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)* ) |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

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

`#include <[zephyr/drivers/video.h](video_8h.md)>`

**Value:**

[VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)((str)[0], (str)[1], (str)[2], (str)[3])

[VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)

#define VIDEO\_FOURCC(a, b, c, d)

Four-character-code uniquely identifying the pixel format.

**Definition** video.h:1002

Convert a four-character-string to a four-character-code.

Convert a string literal or variable into a four-character-code as defined by [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951).

Parameters
:   | str | String to be converted |
    | --- | --- |

Returns
:   Four-character-code.

## [◆ ](#gacd3805f57633c3db8c6adcd87384bd5c)VIDEO\_FOURCC\_TO\_STR

| #define VIDEO\_FOURCC\_TO\_STR | ( |  | *fourcc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

**Value:**

((char[]){ \

(char)((fourcc) & 0xFF), \

(char)(((fourcc) >> 8) & 0xFF), \

(char)(((fourcc) >> 16) & 0xFF), \

(char)(((fourcc) >> 24) & 0xFF), \

'\0' \

})

Convert a four-character-code to a four-character-string.

Convert a four-character code as defined by [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951) into a string that can be used anywhere, such as in debug logs with the s print formatter.

Parameters
:   | fourcc | The 32-bit four-character-code integer to be converted, in CPU-native endinaness. |
    | --- | --- |

Returns
:   Four-character-string built out of it.

## [◆ ](#gaffb650a5f9b2b03890283ecfe95aee04)VIDEO\_PIX\_FMT\_ABGR32

| #define VIDEO\_PIX\_FMT\_ABGR32   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('A', 'R', '2', '4') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| Bbbbbbbb Gggggggg Rrrrrrrr Aaaaaaaa | ...

## [◆ ](#ga5cd54fb54967a80576082cadd5941670)VIDEO\_PIX\_FMT\_ARGB32

| #define VIDEO\_PIX\_FMT\_ARGB32   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'A', '2', '4') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| Aaaaaaaa Rrrrrrrr Gggggggg Bbbbbbbb | ...

## [◆ ](#gaf1f8775bbdd0508c4e21a58dfcfc362d)VIDEO\_PIX\_FMT\_BGR24

| #define VIDEO\_PIX\_FMT\_BGR24   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'G', 'R', '3') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

24 bit RGB format with 8 bit per component

| Bbbbbbbb Gggggggg Rggggggg | ...

## [◆ ](#ga515e379bc7f59a8062f3e2a5980b0626)VIDEO\_PIX\_FMT\_BGRA32

| #define VIDEO\_PIX\_FMT\_BGRA32   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'A', '2', '4') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| Aaaaaaaa Bbbbbbbb Gggggggg Rrrrrrrr | ...

## [◆ ](#gaa3af19adaf282b83a6c16f265a4260dc)VIDEO\_PIX\_FMT\_GREY

| #define VIDEO\_PIX\_FMT\_GREY   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'R', 'E', 'Y') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Same as Y8 (8-bit luma-only) following the standard FOURCC naming, or L8 in some graphics libraries.

0 1 2 3

| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | ...

## [◆ ](#ga035a13c38c4f123411547e2c40d58bd2)VIDEO\_PIX\_FMT\_JPEG

| #define VIDEO\_PIX\_FMT\_JPEG   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('J', 'P', 'E', 'G') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Both JPEG (single frame) and Motion-JPEG (MJPEG, multiple JPEG frames concatenated).

## [◆ ](#ga03e6be04b23b9735c96231eebc687158)VIDEO\_PIX\_FMT\_RGB24

| #define VIDEO\_PIX\_FMT\_RGB24   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', '3') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

24 bit RGB format with 8 bit per component

| Rggggggg Gggggggg Bbbbbbbb | ...

## [◆ ](#gaf009d0eb7dbdb3bfd8883da03478c1ec)VIDEO\_PIX\_FMT\_RGB565

| #define VIDEO\_PIX\_FMT\_RGB565   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'P') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0].

This 16-bit integer is then packed in little endian format over two bytes:

7......0 15.....8

| gggBbbbb RrrrrGgg | ...

## [◆ ](#gaf3830004bb857fa00a14d0a1209c61a8)VIDEO\_PIX\_FMT\_RGB565X

| #define VIDEO\_PIX\_FMT\_RGB565X   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'R') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0].

This 16-bit integer is then packed in big endian format over two bytes:

15.....8 7......0

| RrrrrGgg gggBbbbb | ...

## [◆ ](#ga8ee1e3b82eeeb02188157aa4b4b5d842)VIDEO\_PIX\_FMT\_RGBA32

| #define VIDEO\_PIX\_FMT\_RGBA32   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('A', 'B', '2', '4') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| Rrrrrrrr Gggggggg Bbbbbbbb Aaaaaaaa | ...

## [◆ ](#ga0b55190a343fe891bdbb7b148e7feeae)VIDEO\_PIX\_FMT\_SBGGR10

| #define VIDEO\_PIX\_FMT\_SBGGR10   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'G', '1', '0') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| bbbbbbbb 000000Bb | gggggggg 000000Gg | bbbbbbbb 000000Bb | gggggggg 000000Gg | ...

| gggggggg 000000Gg | rrrrrrrr 000000Rr | gggggggg 000000Gg | rrrrrrrr 000000Rr | ...

## [◆ ](#ga3751a8dce1c7459df06f83cd09449b5d)VIDEO\_PIX\_FMT\_SBGGR10P

| #define VIDEO\_PIX\_FMT\_SBGGR10P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'B', 'A', 'A') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3 3 2 1 0

| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ggbbggbb | ...

| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | rrggrrgg | ...

## [◆ ](#gaa2d7712f655dfcb3c74b4f4ec9941402)VIDEO\_PIX\_FMT\_SBGGR12

| #define VIDEO\_PIX\_FMT\_SBGGR12   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'G', '1', '2') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | ...

| gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | ...

## [◆ ](#gab5b5375f050d039e05032c77ac838b31)VIDEO\_PIX\_FMT\_SBGGR12P

| #define VIDEO\_PIX\_FMT\_SBGGR12P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'B', 'C', 'C') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 1 0 2 3 3 2

| Bbbbbbbb | Gggggggg | ggggbbbb | Bbbbbbbb | Gggggggg | ggggbbbb | ...

| Gggggggg | Rrrrrrrr | rrrrgggg | Gggggggg | Rrrrrrrr | rrrrgggg | ...

## [◆ ](#ga403f40a7e15319365c6ca8f3f5f19d21)VIDEO\_PIX\_FMT\_SBGGR14

| #define VIDEO\_PIX\_FMT\_SBGGR14   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'G', '1', '4') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | ...

| gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | ...

## [◆ ](#gac3413c36b3ce91e5658cd0f973c1f3d7)VIDEO\_PIX\_FMT\_SBGGR14P

| #define VIDEO\_PIX\_FMT\_SBGGR14P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'B', 'E', 'E') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3 1 0 2 1 3 2

| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ggbbbbbb bbbbgggg ggggggbb | ...

| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | rrgggggg ggggrrrr rrrrrrgg | ...

## [◆ ](#gae096669643176203199270317dc3449d)VIDEO\_PIX\_FMT\_SBGGR16

| #define VIDEO\_PIX\_FMT\_SBGGR16   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'Y', 'R', '2') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | ...

| gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | ...

## [◆ ](#gabc0205ce5c6426051fdec88d92f123e3)VIDEO\_PIX\_FMT\_SBGGR8

| #define VIDEO\_PIX\_FMT\_SBGGR8   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'A', '8', '1') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3

| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ...

| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | ...

## [◆ ](#ga8e0f47c16483b14b45a593e9e542a987)VIDEO\_PIX\_FMT\_SGBRG10

| #define VIDEO\_PIX\_FMT\_SGBRG10   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '0') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| gggggggg 000000Gg | bbbbbbbb 000000Bb | gggggggg 000000Gg | bbbbbbbb 000000Bb | ...

| rrrrrrrr 000000Rr | gggggggg 000000Gg | rrrrrrrr 000000Rr | gggggggg 000000Gg | ...

## [◆ ](#gad69ab9041428488051bdb45f42ad4271)VIDEO\_PIX\_FMT\_SGBRG10P

| #define VIDEO\_PIX\_FMT\_SGBRG10P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'G', 'A', 'A') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3 3 2 1 0

| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | bbggbbgg | ...

| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ggrrggrr | ...

## [◆ ](#gaa3df9d0af327e609b25e050a4362c2e2)VIDEO\_PIX\_FMT\_SGBRG12

| #define VIDEO\_PIX\_FMT\_SGBRG12   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '2') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | ...

| rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | ...

## [◆ ](#gaecedece3398a6e2f62c20c2eb3f6d3c2)VIDEO\_PIX\_FMT\_SGBRG12P

| #define VIDEO\_PIX\_FMT\_SGBRG12P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'G', 'C', 'C') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 1 0 2 3 3 2

| Gggggggg | Bbbbbbbb | bbbbgggg | Gggggggg | Bbbbbbbb | bbbbgggg | ...

| Rrrrrrrr | Gggggggg | ggggrrrr | Rrrrrrrr | Gggggggg | ggggrrrr | ...

## [◆ ](#ga6c98a7066d7d3bdd8fce3d3651772153)VIDEO\_PIX\_FMT\_SGBRG14

| #define VIDEO\_PIX\_FMT\_SGBRG14   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '4') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | ...

| rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | ...

## [◆ ](#ga89eb47d1dd60794781ee91cb5ae199ad)VIDEO\_PIX\_FMT\_SGBRG14P

| #define VIDEO\_PIX\_FMT\_SGBRG14P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'G', 'E', 'E') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3 1 0 2 1 3 2

| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | bbgggggg ggggbbbb bbbbbbgg | ...

| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ggrrrrrr rrrrgggg ggggggrr | ...

## [◆ ](#ga7f00eb633dd312ea89097edc82dc8f0c)VIDEO\_PIX\_FMT\_SGBRG16

| #define VIDEO\_PIX\_FMT\_SGBRG16   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '6') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | ...

| rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | ...

## [◆ ](#gaa9edb9c562fc3c86b61e071970fae60d)VIDEO\_PIX\_FMT\_SGBRG8

| #define VIDEO\_PIX\_FMT\_SGBRG8   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'B', 'R', 'G') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3

| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | ...

| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ...

## [◆ ](#ga011cc337bc54480d1e11c3e6833ae398)VIDEO\_PIX\_FMT\_SGRBG10

| #define VIDEO\_PIX\_FMT\_SGRBG10   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'A', '1', '0') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| gggggggg 000000Gg | rrrrrrrr 000000Rr | gggggggg 000000Gg | rrrrrrrr 000000Rr | ...

| bbbbbbbb 000000Bb | gggggggg 000000Gg | bbbbbbbb 000000Bb | gggggggg 000000Gg | ...

## [◆ ](#gaa28c6306a3ed44a0e50c16e0eac86688)VIDEO\_PIX\_FMT\_SGRBG10P

| #define VIDEO\_PIX\_FMT\_SGRBG10P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'g', 'A', 'A') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3 3 2 1 0

| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | rrggrrgg | ...

| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ggbbggbb | ...

## [◆ ](#gaf18e6647596613e07ec3c651574b08ba)VIDEO\_PIX\_FMT\_SGRBG12

| #define VIDEO\_PIX\_FMT\_SGRBG12   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'A', '1', '2') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | ...

| bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | ...

## [◆ ](#ga02d91ebf4b5150d5fa437bb3a7a6e872)VIDEO\_PIX\_FMT\_SGRBG12P

| #define VIDEO\_PIX\_FMT\_SGRBG12P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'g', 'C', 'C') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 1 0 2 3 3 2

| Gggggggg | Rrrrrrrr | rrrrgggg | Gggggggg | Rrrrrrrr | rrrrgggg | ...

| Bbbbbbbb | Gggggggg | ggggbbbb | Bbbbbbbb | Gggggggg | ggggbbbb | ...

## [◆ ](#gaf58481956952b13b071b1a68541b9c21)VIDEO\_PIX\_FMT\_SGRBG14

| #define VIDEO\_PIX\_FMT\_SGRBG14   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'R', '1', '4') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | ...

| bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | ...

## [◆ ](#gae06f742e31a62295d3ee16af8eec1b06)VIDEO\_PIX\_FMT\_SGRBG14P

| #define VIDEO\_PIX\_FMT\_SGRBG14P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'g', 'E', 'E') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3 1 0 2 1 3 2

| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | rrgggggg ggggrrrr rrrrrrgg | ...

| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ggbbbbbb bbbbgggg ggggggbb | ...

## [◆ ](#ga4269984ce806e64ba5ccd41c1429769a)VIDEO\_PIX\_FMT\_SGRBG16

| #define VIDEO\_PIX\_FMT\_SGRBG16   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'R', '1', '6') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | ...

| bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | ...

## [◆ ](#ga19d8dc905695229097dffe659f2a806e)VIDEO\_PIX\_FMT\_SGRBG8

| #define VIDEO\_PIX\_FMT\_SGRBG8   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('G', 'R', 'B', 'G') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3

| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | ...

| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ...

## [◆ ](#ga249cbf808658dab777a705fd9deb2986)VIDEO\_PIX\_FMT\_SRGGB10

| #define VIDEO\_PIX\_FMT\_SRGGB10   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '0') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| rrrrrrrr 000000Rr | gggggggg 000000Gg | rrrrrrrr 000000Rr | gggggggg 000000Gg | ...

| gggggggg 000000Gg | bbbbbbbb 000000Bb | gggggggg 000000Gg | bbbbbbbb 000000Bb | ...

## [◆ ](#ga604d2f3501407546aa924e2fdb37be2f)VIDEO\_PIX\_FMT\_SRGGB10P

| #define VIDEO\_PIX\_FMT\_SRGGB10P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'R', 'A', 'A') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3 3 2 1 0

| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ggrrggrr | ...

| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | bbggbbgg | ...

## [◆ ](#ga7b167f2b6a147d325a685825274cd2f2)VIDEO\_PIX\_FMT\_SRGGB12

| #define VIDEO\_PIX\_FMT\_SRGGB12   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '2') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | ...

| gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | ...

## [◆ ](#ga348c15cc77c728fdac773d58341cbc1d)VIDEO\_PIX\_FMT\_SRGGB12P

| #define VIDEO\_PIX\_FMT\_SRGGB12P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'R', 'C', 'C') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 1 0 2 3 3 2

| Rrrrrrrr | Gggggggg | ggggrrrr | Rrrrrrrr | Gggggggg | ggggrrrr | ...

| Gggggggg | Bbbbbbbb | bbbbgggg | Gggggggg | Bbbbbbbb | bbbbgggg | ...

## [◆ ](#gaa6e4c240372e53db8ea3472cc456af58)VIDEO\_PIX\_FMT\_SRGGB14

| #define VIDEO\_PIX\_FMT\_SRGGB14   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '4') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | ...

| gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | ...

## [◆ ](#ga66646a639518285810335a70337277d7)VIDEO\_PIX\_FMT\_SRGGB14P

| #define VIDEO\_PIX\_FMT\_SRGGB14P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('p', 'R', 'E', 'E') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3 1 0 2 1 3 2

| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ggrrrrrr rrrrgggg ggggggrr | ...

| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | bbgggggg ggggbbbb bbbbbbgg | ...

## [◆ ](#ga4f31b5d397868e952d53022c6c8e5823)VIDEO\_PIX\_FMT\_SRGGB16

| #define VIDEO\_PIX\_FMT\_SRGGB16   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '6') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | ...

| gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | ...

## [◆ ](#gabf0dde810e75d37823891ed03811482c)VIDEO\_PIX\_FMT\_SRGGB8

| #define VIDEO\_PIX\_FMT\_SRGGB8   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'G', 'B') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3

| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ...

| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | ...

## [◆ ](#gadca3ee56c798cf05b63cbfc87af98ce3)VIDEO\_PIX\_FMT\_UYVY

| #define VIDEO\_PIX\_FMT\_UYVY   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('U', 'Y', 'V', 'Y') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| Uuuuuuuu Yyyyyyyy | Vvvvvvvv Yyyyyyyy | ...

## [◆ ](#ga63c825ce5dc6c863d355195fde40acb1)VIDEO\_PIX\_FMT\_VYUY

| #define VIDEO\_PIX\_FMT\_VYUY   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('V', 'Y', 'U', 'Y') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| Vvvvvvvv Yyyyyyyy | Uuuuuuuu Yyyyyyyy | ...

## [◆ ](#ga8be24c04210f8818d75082bd710db8b1)VIDEO\_PIX\_FMT\_XRGB32

| #define VIDEO\_PIX\_FMT\_XRGB32   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('B', 'X', '2', '4') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

The first byte is empty (X) for each pixel.

| Xxxxxxxx Rrrrrrrr Gggggggg Bbbbbbbb | ...

## [◆ ](#ga017bcbec587314f569d6d0e4fbdda351)VIDEO\_PIX\_FMT\_XYUV32

| #define VIDEO\_PIX\_FMT\_XYUV32   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('X', 'Y', 'U', 'V') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

The first byte is empty (X) for each pixel.

| Xxxxxxxx Yyyyyyyy Uuuuuuuu Vvvvvvvv | ...

## [◆ ](#ga0506f2c8aa1a82f02fc9383d99b43bc3)VIDEO\_PIX\_FMT\_Y10

| #define VIDEO\_PIX\_FMT\_Y10   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '0', ' ') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Little endian, with the 6 most significant bits set to Zero.

0 1 2 3

| yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | ...

| yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | ...

## [◆ ](#ga502df4612995fc39e03d6de3ec675159)VIDEO\_PIX\_FMT\_Y10P

| #define VIDEO\_PIX\_FMT\_Y10P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '0', 'P') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3 3 2 1 0

| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | yyyyyyyy | ...

## [◆ ](#ga166b2144cec4b4f92fadda30e81b7d22)VIDEO\_PIX\_FMT\_Y12

| #define VIDEO\_PIX\_FMT\_Y12   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '2', ' ') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Little endian, with the 4 most significant bits set to Zero.

0 1 2 3

| yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | ...

| yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | ...

## [◆ ](#ga263e6553a77d00bc509c1b270efebb0b)VIDEO\_PIX\_FMT\_Y12P

| #define VIDEO\_PIX\_FMT\_Y12P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '2', 'P') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 1 0 2 3 3 2

| Yyyyyyyy | Yyyyyyyy | yyyyyyyy | Yyyyyyyy | Yyyyyyyy | yyyyyyyy | ...

| Yyyyyyyy | Yyyyyyyy | yyyyyyyy | Yyyyyyyy | Yyyyyyyy | yyyyyyyy | ...

## [◆ ](#ga7d9379f19abcbac17bad3d6359a42d9d)VIDEO\_PIX\_FMT\_Y14

| #define VIDEO\_PIX\_FMT\_Y14   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '4', ' ') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Little endian, with the 2 most significant bits set to Zero.

0 1 2 3

| yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | ...

| yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | ...

## [◆ ](#gada0124aad9c10d403966b1e3851cd968)VIDEO\_PIX\_FMT\_Y14P

| #define VIDEO\_PIX\_FMT\_Y14P   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '4', 'P') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

0 1 2 3 1 0 2 1 3 2

| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | yyyyyyyy yyyyyyyy yyyyyyyy | ...

| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | yyyyyyyy yyyyyyyy yyyyyyyy | ...

## [◆ ](#gaa65fe8bd917dd2fe95fa87530fc3055f)VIDEO\_PIX\_FMT\_Y16

| #define VIDEO\_PIX\_FMT\_Y16   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', '1', '6', ' ') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Little endian.

0 1 2 3

| yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | ...

| yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | ...

## [◆ ](#gad186d3166acec11c893ae57a0ae68f11)VIDEO\_PIX\_FMT\_YUYV

| #define VIDEO\_PIX\_FMT\_YUYV   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', 'U', 'Y', 'V') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

There is either a missing channel per pixel, U or V.

The value is to be averaged over 2 pixels to get the value of individual pixel.

| Yyyyyyyy Uuuuuuuu | Yyyyyyyy Vvvvvvvv | ...

## [◆ ](#ga299af047675a110c109cee954f55fca6)VIDEO\_PIX\_FMT\_YVYU

| #define VIDEO\_PIX\_FMT\_YVYU   [VIDEO\_FOURCC](#gafb9e36597c39face52cd0c010df20951)('Y', 'V', 'Y', 'U') |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| Yyyyyyyy Vvvvvvvv | Yyyyyyyy Uuuuuuuu | ...

## Function Documentation

## [◆ ](#gabdbd1b0f40af6663d81402deefdd387f)video\_bits\_per\_pixel()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int video\_bits\_per\_pixel | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pixfmt* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Get number of bits per pixel of a pixel format.

Parameters
:   | pixfmt | FourCC pixel format value ([Video pixel formats](group__video__pixel__formats.md "Video pixel formats")). |
    | --- | --- |

Return values
:   | 0 | if the format is unhandled or if it is variable number of bits |
    | --- | --- |
    | bit | size of one pixel for this format |

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
