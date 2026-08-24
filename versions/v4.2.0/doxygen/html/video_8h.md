---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/video_8h.html
original_path: doxygen/html/video_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video.h File Reference

Public APIs for Video.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](video_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [video\_format](structvideo__format.md) |
|  | Video format structure. [More...](structvideo__format.md#details) |
| struct | [video\_format\_cap](structvideo__format__cap.md) |
|  | Video format capability. [More...](structvideo__format__cap.md#details) |
| struct | [video\_caps](structvideo__caps.md) |
|  | Video format capabilities. [More...](structvideo__caps.md#details) |
| struct | [video\_buffer](structvideo__buffer.md) |
|  | Video buffer structure. [More...](structvideo__buffer.md#details) |
| struct | [video\_frmival](structvideo__frmival.md) |
|  | Video frame interval structure. [More...](structvideo__frmival.md#details) |
| struct | [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) |
|  | Video frame interval stepwise structure. [More...](structvideo__frmival__stepwise.md#details) |
| struct | [video\_frmival\_enum](structvideo__frmival__enum.md) |
|  | Video frame interval enumeration structure. [More...](structvideo__frmival__enum.md#details) |
| struct | [video\_rect](structvideo__rect.md) |
|  | Description of a rectangle area. [More...](structvideo__rect.md#details) |
| struct | [video\_selection](structvideo__selection.md) |
|  | Video selection (crop / compose) structure. [More...](structvideo__selection.md#details) |
| struct | [video\_driver\_api](structvideo__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [LINE\_COUNT\_HEIGHT](group__video__interface.md#ga59e44ec7c8132f479f1aa71e5b2c6546)   (-1) |
| #define | [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)(a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Four-character-code uniquely identifying the pixel format. |
| #define | [VIDEO\_FOURCC\_FROM\_STR](group__video__pixel__formats.md#gafc6c4cb871f15464f2b7df86d91fd8f3)(str) |
|  | Convert a four-character-string to a four-character-code. |
| #define | [VIDEO\_FOURCC\_TO\_STR](group__video__pixel__formats.md#gacd3805f57633c3db8c6adcd87384bd5c)(fourcc) |
|  | Convert a four-character-code to a four-character-string. |
| Bayer formats (R, G, B channels). | |
| The full color information is spread over multiple pixels.  When the format includes more than 8-bit per pixel, a strategy becomes needed to pack the bits over multiple bytes, as illustrated for each format.  The number above the 'R', 'r', 'G', 'g', 'B', 'b' are hints about which pixel number the following bits belong to. | |
| #define | [VIDEO\_PIX\_FMT\_SBGGR8](group__video__pixel__formats.md#gabc0205ce5c6426051fdec88d92f123e3)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'A', '8', '1') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG8](group__video__pixel__formats.md#gaa9edb9c562fc3c86b61e071970fae60d)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'B', 'R', 'G') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG8](group__video__pixel__formats.md#ga19d8dc905695229097dffe659f2a806e)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'R', 'B', 'G') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB8](group__video__pixel__formats.md#gabf0dde810e75d37823891ed03811482c)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'G', 'B') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR10P](group__video__pixel__formats.md#ga3751a8dce1c7459df06f83cd09449b5d)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'B', 'A', 'A') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG10P](group__video__pixel__formats.md#gad69ab9041428488051bdb45f42ad4271)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'G', 'A', 'A') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG10P](group__video__pixel__formats.md#gaa28c6306a3ed44a0e50c16e0eac86688)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'g', 'A', 'A') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB10P](group__video__pixel__formats.md#ga604d2f3501407546aa924e2fdb37be2f)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'R', 'A', 'A') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR12P](group__video__pixel__formats.md#gab5b5375f050d039e05032c77ac838b31)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'B', 'C', 'C') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG12P](group__video__pixel__formats.md#gaecedece3398a6e2f62c20c2eb3f6d3c2)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'G', 'C', 'C') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG12P](group__video__pixel__formats.md#ga02d91ebf4b5150d5fa437bb3a7a6e872)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'g', 'C', 'C') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB12P](group__video__pixel__formats.md#ga348c15cc77c728fdac773d58341cbc1d)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'R', 'C', 'C') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR14P](group__video__pixel__formats.md#gac3413c36b3ce91e5658cd0f973c1f3d7)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'B', 'E', 'E') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG14P](group__video__pixel__formats.md#ga89eb47d1dd60794781ee91cb5ae199ad)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'G', 'E', 'E') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG14P](group__video__pixel__formats.md#gae06f742e31a62295d3ee16af8eec1b06)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'g', 'E', 'E') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB14P](group__video__pixel__formats.md#ga66646a639518285810335a70337277d7)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('p', 'R', 'E', 'E') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR10](group__video__pixel__formats.md#ga0b55190a343fe891bdbb7b148e7feeae)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'G', '1', '0') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG10](group__video__pixel__formats.md#ga8e0f47c16483b14b45a593e9e542a987)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '0') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG10](group__video__pixel__formats.md#ga011cc337bc54480d1e11c3e6833ae398)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'A', '1', '0') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB10](group__video__pixel__formats.md#ga249cbf808658dab777a705fd9deb2986)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '0') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR12](group__video__pixel__formats.md#gaa2d7712f655dfcb3c74b4f4ec9941402)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'G', '1', '2') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG12](group__video__pixel__formats.md#gaa3df9d0af327e609b25e050a4362c2e2)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '2') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG12](group__video__pixel__formats.md#gaf18e6647596613e07ec3c651574b08ba)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'A', '1', '2') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB12](group__video__pixel__formats.md#ga7b167f2b6a147d325a685825274cd2f2)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '2') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR14](group__video__pixel__formats.md#ga403f40a7e15319365c6ca8f3f5f19d21)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'G', '1', '4') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG14](group__video__pixel__formats.md#ga6c98a7066d7d3bdd8fce3d3651772153)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '4') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG14](group__video__pixel__formats.md#gaf58481956952b13b071b1a68541b9c21)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'R', '1', '4') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB14](group__video__pixel__formats.md#gaa6e4c240372e53db8ea3472cc456af58)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '4') |
| #define | [VIDEO\_PIX\_FMT\_SBGGR16](group__video__pixel__formats.md#gae096669643176203199270317dc3449d)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'Y', 'R', '2') |
| #define | [VIDEO\_PIX\_FMT\_SGBRG16](group__video__pixel__formats.md#ga7f00eb633dd312ea89097edc82dc8f0c)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'B', '1', '6') |
| #define | [VIDEO\_PIX\_FMT\_SGRBG16](group__video__pixel__formats.md#ga4269984ce806e64ba5ccd41c1429769a)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'R', '1', '6') |
| #define | [VIDEO\_PIX\_FMT\_SRGGB16](group__video__pixel__formats.md#ga4f31b5d397868e952d53022c6c8e5823)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', '1', '6') |
| Grayscale formats | |
| Luminance (Y) channel only, in various bit depth and packing.  When the format includes more than 8-bit per pixel, a strategy becomes needed to pack the bits over multiple bytes, as illustrated for each format.  The number above the 'Y', 'y' are hints about which pixel number the following bits belong to. | |
| #define | [VIDEO\_PIX\_FMT\_GREY](group__video__pixel__formats.md#gaa3af19adaf282b83a6c16f265a4260dc)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'R', 'E', 'Y') |
|  | Same as Y8 (8-bit luma-only) following the standard FOURCC naming, or L8 in some graphics libraries. |
| #define | [VIDEO\_PIX\_FMT\_Y10P](group__video__pixel__formats.md#ga502df4612995fc39e03d6de3ec675159)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('Y', '1', '0', 'P') |
| #define | [VIDEO\_PIX\_FMT\_Y12P](group__video__pixel__formats.md#ga263e6553a77d00bc509c1b270efebb0b)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('Y', '1', '2', 'P') |
| #define | [VIDEO\_PIX\_FMT\_Y14P](group__video__pixel__formats.md#gada0124aad9c10d403966b1e3851cd968)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('Y', '1', '4', 'P') |
| #define | [VIDEO\_PIX\_FMT\_Y10](group__video__pixel__formats.md#ga0506f2c8aa1a82f02fc9383d99b43bc3)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('Y', '1', '0', ' ') |
|  | Little endian, with the 6 most significant bits set to Zero. |
| #define | [VIDEO\_PIX\_FMT\_Y12](group__video__pixel__formats.md#ga166b2144cec4b4f92fadda30e81b7d22)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('Y', '1', '2', ' ') |
|  | Little endian, with the 4 most significant bits set to Zero. |
| #define | [VIDEO\_PIX\_FMT\_Y14](group__video__pixel__formats.md#ga7d9379f19abcbac17bad3d6359a42d9d)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('Y', '1', '4', ' ') |
|  | Little endian, with the 2 most significant bits set to Zero. |
| #define | [VIDEO\_PIX\_FMT\_Y16](group__video__pixel__formats.md#gaa65fe8bd917dd2fe95fa87530fc3055f)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('Y', '1', '6', ' ') |
|  | Little endian. |
| RGB formats | |
| Per-color (R, G, B) channels. | |
| #define | [VIDEO\_PIX\_FMT\_RGB565X](group__video__pixel__formats.md#gaf3830004bb857fa00a14d0a1209c61a8)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'R') |
|  | 5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0]. |
| #define | [VIDEO\_PIX\_FMT\_RGB565](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'P') |
|  | 5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0]. |
| #define | [VIDEO\_PIX\_FMT\_BGR24](group__video__pixel__formats.md#gaf1f8775bbdd0508c4e21a58dfcfc362d)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'G', 'R', '3') |
|  | 24 bit RGB format with 8 bit per component |
| #define | [VIDEO\_PIX\_FMT\_RGB24](group__video__pixel__formats.md#ga03e6be04b23b9735c96231eebc687158)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', '3') |
|  | 24 bit RGB format with 8 bit per component |
| #define | [VIDEO\_PIX\_FMT\_ARGB32](group__video__pixel__formats.md#ga5cd54fb54967a80576082cadd5941670)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'A', '2', '4') |
| #define | [VIDEO\_PIX\_FMT\_ABGR32](group__video__pixel__formats.md#gaffb650a5f9b2b03890283ecfe95aee04)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('A', 'R', '2', '4') |
| #define | [VIDEO\_PIX\_FMT\_RGBA32](group__video__pixel__formats.md#ga8ee1e3b82eeeb02188157aa4b4b5d842)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('A', 'B', '2', '4') |
| #define | [VIDEO\_PIX\_FMT\_BGRA32](group__video__pixel__formats.md#ga515e379bc7f59a8062f3e2a5980b0626)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'A', '2', '4') |
| #define | [VIDEO\_PIX\_FMT\_XRGB32](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'X', '2', '4') |
|  | The first byte is empty (X) for each pixel. |
| YUV formats | |
| Luminance (Y) and chrominance (U, V) channels. | |
| #define | [VIDEO\_PIX\_FMT\_YUYV](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('Y', 'U', 'Y', 'V') |
|  | There is either a missing channel per pixel, U or V. |
| #define | [VIDEO\_PIX\_FMT\_YVYU](group__video__pixel__formats.md#ga299af047675a110c109cee954f55fca6)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('Y', 'V', 'Y', 'U') |
| #define | [VIDEO\_PIX\_FMT\_VYUY](group__video__pixel__formats.md#ga63c825ce5dc6c863d355195fde40acb1)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('V', 'Y', 'U', 'Y') |
| #define | [VIDEO\_PIX\_FMT\_UYVY](group__video__pixel__formats.md#gadca3ee56c798cf05b63cbfc87af98ce3)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('U', 'Y', 'V', 'Y') |
| #define | [VIDEO\_PIX\_FMT\_XYUV32](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('X', 'Y', 'U', 'V') |
|  | The first byte is empty (X) for each pixel. |
| Compressed formats | |
| #define | [VIDEO\_PIX\_FMT\_JPEG](group__video__pixel__formats.md#ga035a13c38c4f123411547e2c40d58bd2)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('J', 'P', 'E', 'G') |
|  | Both JPEG (single frame) and Motion-JPEG (MJPEG, multiple JPEG frames concatenated). |
| MIPI CSI2 Data-types | |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_NULL](group__video__interface.md#ga59d6f35198b6412a9aa78c094ecfaa19)   0x10 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_BLANKING](group__video__interface.md#gaede52c3391311b7cf931665afdeed720)   0x11 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_EMBEDDED\_8](group__video__interface.md#ga2b16d411ffcbcc7e74fa6aa2966b4b0d)   0x12 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV420\_8](group__video__interface.md#gab8001106ce7c91573012a895a4b3f1a8)   0x18 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV420\_10](group__video__interface.md#ga65dac1b59e00cb26e9af9e39663b20f0)   0x19 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV420\_CSPS\_8](group__video__interface.md#ga9c40ffb7a4042dd9d149e960eeddd14e)   0x1c |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV420\_CSPS\_10](group__video__interface.md#gad1d445cd3b576e4c7062f0a06f8dc71e)   0x1d |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV422\_8](group__video__interface.md#ga18dac33c3f8afd80e08d69ed78aee5a9)   0x1e |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV422\_10](group__video__interface.md#ga4b530659596536d30168161139cc46fb)   0x1f |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RGB444](group__video__interface.md#ga04efc97a4dab0af7c7266ab104b8d626)   0x20 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RGB555](group__video__interface.md#ga351c2045810bb786d8232162f47fee7d)   0x21 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RGB565](group__video__interface.md#gad5f04e5dd3d5e0c5f67c64e28cd91c56)   0x22 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RGB666](group__video__interface.md#gaa452375e0454fa314eb140bac3c07e67)   0x23 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RGB888](group__video__interface.md#ga0d637375f7bf081967135139a8f6c5b6)   0x24 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW6](group__video__interface.md#gad251376f21a56d05742fcb68d228a677)   0x28 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW7](group__video__interface.md#ga384e8203e1bb7208a4bcb1e4931a929b)   0x29 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW8](group__video__interface.md#ga6d3881edac75ba2c12185dc119311945)   0x2a |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW10](group__video__interface.md#ga64a52402a6883cb1b23a5524418528a9)   0x2b |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW12](group__video__interface.md#gadadb66f582b5e014336e29c1dafc3631)   0x2c |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW14](group__video__interface.md#ga2ad6b8870c5dca6a8d19b1f80d83b81b)   0x2d |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_USER](group__video__interface.md#ga98885f3584261947dd2b325bf12b2f3d)(n) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [video\_api\_format\_t](group__video__interface.md#ga964b301e45a42aa78799a1d9c9297ab1)) (const struct [device](structdevice.md) \*dev, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Function pointer type for video\_set/get\_format(). |
| typedef int(\* | [video\_api\_frmival\_t](group__video__interface.md#gaf63180944041a9e934c9f7567bdc1b88)) (const struct [device](structdevice.md) \*dev, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Function pointer type for video\_set/get\_frmival(). |
| typedef int(\* | [video\_api\_enum\_frmival\_t](group__video__interface.md#ga026c9a4531a125339e69b81f75343555)) (const struct [device](structdevice.md) \*dev, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie) |
|  | List all supported frame intervals of a given format. |
| typedef int(\* | [video\_api\_enqueue\_t](group__video__interface.md#gae6849a22140b3507bab219b579bc3d40)) (const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Enqueue a buffer in the driver’s incoming queue. |
| typedef int(\* | [video\_api\_dequeue\_t](group__video__interface.md#ga4265087c8faf62bbc36e88c0587022a1)) (const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Dequeue a buffer from the driver’s outgoing queue. |
| typedef int(\* | [video\_api\_flush\_t](group__video__interface.md#ga990ba001531c7300a06ca02d64c31eaa)) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
|  | Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue. |
| typedef int(\* | [video\_api\_set\_stream\_t](group__video__interface.md#gacda90bacb17a53e0bd11e5bfd37be57a)) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable, enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) type) |
|  | Start or stop streaming on the video device. |
| typedef int(\* | [video\_api\_ctrl\_t](group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cid) |
|  | Set/Get a video control value. |
| typedef int(\* | [video\_api\_get\_caps\_t](group__video__interface.md#ga070cb5f5bf35b98e2e7dda3378114780)) (const struct [device](structdevice.md) \*dev, struct [video\_caps](structvideo__caps.md) \*caps) |
|  | Get capabilities of a video endpoint. |
| typedef int(\* | [video\_api\_set\_signal\_t](group__video__interface.md#gad5aacb1386785a3587d41844c7854f83)) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Register/Unregister poll signal for buffer events. |
| typedef int(\* | [video\_api\_selection\_t](group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a)) (const struct [device](structdevice.md) \*dev, struct [video\_selection](structvideo__selection.md) \*sel) |
|  | Get/Set video selection (crop / compose). |

| Enumerations | |
| --- | --- |
| enum | [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) { [VIDEO\_BUF\_TYPE\_INPUT](group__video__interface.md#ggad386b2994b56844ebe713f156b9dfe4ea20b003de365a7e2c32bba889ae78a3a1) , [VIDEO\_BUF\_TYPE\_OUTPUT](group__video__interface.md#ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083) } |
|  | [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e "video_buf_type enum") enum [More...](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) |
| enum | [video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1) { [VIDEO\_FRMIVAL\_TYPE\_DISCRETE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4) = 1 , [VIDEO\_FRMIVAL\_TYPE\_STEPWISE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b) = 2 } |
|  | [video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1 "video_frmival_type enum") enum [More...](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1) |
| enum | [video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8) { [VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8) , [VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8) , [VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3) } |
|  | video\_event enum [More...](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8) |
| enum | [video\_selection\_target](group__video__interface.md#gae375c0586e3505632cc69348935c9b54) {     [VIDEO\_SEL\_TGT\_CROP](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17) , [VIDEO\_SEL\_TGT\_CROP\_BOUND](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54ab1b1302e553daefb9c1017e0bed9d8f1) , [VIDEO\_SEL\_TGT\_NATIVE\_SIZE](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a7536f3626e44f03775f09a1813ec8b20) , [VIDEO\_SEL\_TGT\_COMPOSE](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49) ,     [VIDEO\_SEL\_TGT\_COMPOSE\_BOUND](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a038df16bad455f389f5c24fc91c8bd4f)   } |

| Functions | |
| --- | --- |
| static int | [video\_set\_format](group__video__interface.md#gab93c2cb09bf5b0629b665cc4a079e3cd) (const struct [device](structdevice.md) \*dev, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Set video format. |
| static int | [video\_get\_format](group__video__interface.md#gad4a5849af21d20197169f0557329fdc1) (const struct [device](structdevice.md) \*dev, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Get video format. |
| static int | [video\_set\_frmival](group__video__interface.md#gac7a047582183dcdc4fed58ef9b9b4a84) (const struct [device](structdevice.md) \*dev, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Set video frame interval. |
| static int | [video\_get\_frmival](group__video__interface.md#gaf5a5bcd6e05d38a55a296b8290c3e0aa) (const struct [device](structdevice.md) \*dev, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Get video frame interval. |
| static int | [video\_enum\_frmival](group__video__interface.md#ga8141d7cb665fd975c4f852e40ba408e8) (const struct [device](structdevice.md) \*dev, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie) |
|  | List video frame intervals. |
| static int | [video\_enqueue](group__video__interface.md#gaca3d87049c7631f2edbbb673da94836a) (const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Enqueue a video buffer. |
| static int | [video\_dequeue](group__video__interface.md#ga45967c58a8cb6c18eac5b3ee3f1061f1) (const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Dequeue a video buffer. |
| static int | [video\_flush](group__video__interface.md#gaa670ffe1b3025ac48f132b4cac89693b) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
|  | Flush endpoint buffers. |
| static int | [video\_stream\_start](group__video__interface.md#ga835bb485fcf906cc5b27529a0fe218d3) (const struct [device](structdevice.md) \*dev, enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) type) |
|  | Start the video device function. |
| static int | [video\_stream\_stop](group__video__interface.md#gaa8965272b3f2a7f6692b56ff569f190f) (const struct [device](structdevice.md) \*dev, enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) type) |
|  | Stop the video device function. |
| static int | [video\_get\_caps](group__video__interface.md#ga903c7fff276274c9f3a9ac88be02cba2) (const struct [device](structdevice.md) \*dev, struct [video\_caps](structvideo__caps.md) \*caps) |
|  | Get the capabilities of a video endpoint. |
| int | [video\_set\_ctrl](group__video__interface.md#ga1cce17a3dfc881a1080708c7bc417aac) (const struct [device](structdevice.md) \*dev, struct [video\_control](structvideo__control.md) \*control) |
|  | Set the value of a control. |
| int | [video\_get\_ctrl](group__video__interface.md#ga71853c720e6df1def4c945e23d103298) (const struct [device](structdevice.md) \*dev, struct [video\_control](structvideo__control.md) \*control) |
|  | Get the current value of a control. |
| int | [video\_query\_ctrl](group__video__interface.md#ga8813a656a66adc6bfb10fb7f27194898) (struct [video\_ctrl\_query](structvideo__ctrl__query.md) \*cq) |
|  | Query information about a control. |
| void | [video\_print\_ctrl](group__video__interface.md#ga2bff04c6abc344350d6b0036289a701e) (const struct [video\_ctrl\_query](structvideo__ctrl__query.md) \*const cq) |
|  | Print all the information of a control. |
| static int | [video\_set\_signal](group__video__interface.md#gac67404c76cbd6183aee59f3b8243652b) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Register/Unregister k\_poll signal for a video endpoint. |
| static int | [video\_set\_selection](group__video__interface.md#ga21f2e7d6b5ec0c50ceeee580c6272613) (const struct [device](structdevice.md) \*dev, struct [video\_selection](structvideo__selection.md) \*sel) |
|  | Set video selection (crop/compose). |
| static int | [video\_get\_selection](group__video__interface.md#ga917889d41696ab12c92475b85caec13f) (const struct [device](structdevice.md) \*dev, struct [video\_selection](structvideo__selection.md) \*sel) |
|  | Get video selection (crop/compose). |
| struct [video\_buffer](structvideo__buffer.md) \* | [video\_buffer\_aligned\_alloc](group__video__interface.md#ga195914c7f03f2241702c77d41d1ab750) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate aligned video buffer. |
| struct [video\_buffer](structvideo__buffer.md) \* | [video\_buffer\_alloc](group__video__interface.md#gaee6eb26310a40d3f18161b3567f9e0a9) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate video buffer. |
| void | [video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f) (struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Release a video buffer. |
| int | [video\_format\_caps\_index](group__video__interface.md#gadbf59fd2d77b3d164cacf56bd4ae81ce) (const struct [video\_format\_cap](structvideo__format__cap.md) \*fmts, const struct [video\_format](structvideo__format.md) \*fmt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*idx) |
|  | Search for a format that matches in a list of capabilities. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [video\_frmival\_nsec](group__video__interface.md#ga6b3c7456b2527cc441a100ff50787dc2) (const struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Compute the difference between two frame intervals. |
| void | [video\_closest\_frmival\_stepwise](group__video__interface.md#gad11314e82e9207449b3c0b29fdc830d0) (const struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) \*stepwise, const struct [video\_frmival](structvideo__frmival.md) \*desired, struct [video\_frmival](structvideo__frmival.md) \*match) |
|  | Find the closest match to a frame interval value within a stepwise frame interval. |
| void | [video\_closest\_frmival](group__video__interface.md#gaeeb67898719f094787d4157e8ce13209) (const struct [device](structdevice.md) \*dev, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*match) |
|  | Find the closest match to a frame interval value within a video device. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [video\_get\_csi\_link\_freq](group__video__interface.md#ga41e450607b4dc062fac682728ec7a79d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bpp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lane\_nb) |
|  | Return the link-frequency advertised by a device. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [video\_bits\_per\_pixel](group__video__pixel__formats.md#gabdbd1b0f40af6663d81402deefdd387f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pixfmt) |
|  | Get number of bits per pixel of a pixel format. |

## Detailed Description

Public APIs for Video.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video.h](video_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
