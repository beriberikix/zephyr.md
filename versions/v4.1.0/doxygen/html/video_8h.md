---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/video_8h.html
original_path: doxygen/html/video_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| struct | [video\_driver\_api](structvideo__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [LINE\_COUNT\_HEIGHT](group__video__interface.md#ga59e44ec7c8132f479f1aa71e5b2c6546)   (-1) |
| #define | [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)(a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Four-character-code uniquely identifying the pixel format. |
| #define | [VIDEO\_FOURCC\_FROM\_STR](group__video__pixel__formats.md#gafc6c4cb871f15464f2b7df86d91fd8f3)(str) |
|  | Convert a four-character-string to a four-character-code. |
| Bayer formats (R, G, B channels). | |
| The full color information is spread over multiple pixels. | |
| #define | [VIDEO\_PIX\_FMT\_BGGR8](group__video__pixel__formats.md#ga64ad74bb6c92041a4190614b684ae024)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'A', '8', '1') |
| #define | [VIDEO\_PIX\_FMT\_GBRG8](group__video__pixel__formats.md#gaebdfd9d4230b56f6b8533630356b8793)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'B', 'R', 'G') |
| #define | [VIDEO\_PIX\_FMT\_GRBG8](group__video__pixel__formats.md#ga6b9c8d43406e45927f4e9e94504eae9c)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('G', 'R', 'B', 'G') |
| #define | [VIDEO\_PIX\_FMT\_RGGB8](group__video__pixel__formats.md#ga0c98dc205b724c9e4556e41cc266d80e)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'G', 'B') |
| RGB formats | |
| Per-color (R, G, B) channels. | |
| #define | [VIDEO\_PIX\_FMT\_RGB565X](group__video__pixel__formats.md#gaf3830004bb857fa00a14d0a1209c61a8)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'R') |
|  | 5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0]. |
| #define | [VIDEO\_PIX\_FMT\_RGB565](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('R', 'G', 'B', 'P') |
|  | 5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0]. |
| #define | [VIDEO\_PIX\_FMT\_XRGB32](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('B', 'X', '2', '4') |
|  | The first byte is empty (X) for each pixel. |
| YUV formats | |
| Luminance (Y) and chrominance (U, V) channels. | |
| #define | [VIDEO\_PIX\_FMT\_YUYV](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('Y', 'U', 'Y', 'V') |
|  | There is either a missing channel per pixel, U or V. |
| #define | [VIDEO\_PIX\_FMT\_XYUV32](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('X', 'Y', 'U', 'V') |
|  | The first byte is empty (X) for each pixel. |
| Compressed formats | |
| #define | [VIDEO\_PIX\_FMT\_JPEG](group__video__pixel__formats.md#ga035a13c38c4f123411547e2c40d58bd2)   [VIDEO\_FOURCC](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)('J', 'P', 'E', 'G') |
|  | Both JPEG (single frame) and Motion-JPEG (MJPEG, multiple JPEG frames concatenated). |

| Typedefs | |
| --- | --- |
| typedef int(\* | [video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Set video format. |
| typedef int(\* | [video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Get current video format. |
| typedef int(\* | [video\_api\_set\_frmival\_t](group__video__interface.md#gac69b1ab2877112983b421c650076da89)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Set video frame interval. |
| typedef int(\* | [video\_api\_get\_frmival\_t](group__video__interface.md#gaa7fae28aae3959ea09f9ffc87fa42c7e)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Get current video frame interval. |
| typedef int(\* | [video\_api\_enum\_frmival\_t](group__video__interface.md#gab8bd3f3a430e6872facad2749d7f2240)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie) |
|  | List all supported frame intervals of a given format. |
| typedef int(\* | [video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Enqueue a buffer in the driver’s incoming queue. |
| typedef int(\* | [video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Dequeue a buffer from the driver’s outgoing queue. |
| typedef int(\* | [video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
|  | Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue. |
| typedef int(\* | [video\_api\_set\_stream\_t](group__video__interface.md#ga4293068f01f310a8d9452fb68fb9afa0)) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Start or stop streaming on the video device. |
| typedef int(\* | [video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
|  | Set a video control value. |
| typedef int(\* | [video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
|  | Get a video control value. |
| typedef int(\* | [video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_caps](structvideo__caps.md) \*caps) |
|  | Get capabilities of a video endpoint. |
| typedef int(\* | [video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)) |
|  | Register/Unregister poll signal for buffer events. |

| Enumerations | |
| --- | --- |
| enum | [video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1) { [VIDEO\_FRMIVAL\_TYPE\_DISCRETE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4) = 1 , [VIDEO\_FRMIVAL\_TYPE\_STEPWISE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b) = 2 } |
|  | [video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1 "video_frmival_type enum") enum [More...](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1) |
| enum | [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) { [VIDEO\_EP\_NONE](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7) = -1 , [VIDEO\_EP\_ALL](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9afb3b8e141a5675a7d299b82dca5f36a9) = -2 , [VIDEO\_EP\_IN](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7) = -3 , [VIDEO\_EP\_OUT](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a) = -4 } |
|  | [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9 "video_endpoint_id enum") enum [More...](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) |
| enum | [video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8) { [VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8) , [VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8) , [VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3) } |
|  | video\_event enum [More...](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8) |

| Functions | |
| --- | --- |
| static int | [video\_set\_format](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Set video format. |
| static int | [video\_get\_format](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Get video format. |
| static int | [video\_set\_frmival](group__video__interface.md#ga50149acd5c56d237c5a6988bdf1cc241) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Set video frame interval. |
| static int | [video\_get\_frmival](group__video__interface.md#gaa7a61a51424e0d030b87ec52ceb8dc07) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Get video frame interval. |
| static int | [video\_enum\_frmival](group__video__interface.md#gabd7f2fe113e3ade441a1d6cce66c1cda) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie) |
|  | List video frame intervals. |
| static int | [video\_enqueue](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Enqueue a video buffer. |
| static int | [video\_dequeue](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Dequeue a video buffer. |
| static int | [video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
|  | Flush endpoint buffers. |
| static int | [video\_stream\_start](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0) (const struct [device](structdevice.md) \*dev) |
|  | Start the video device function. |
| static int | [video\_stream\_stop](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48) (const struct [device](structdevice.md) \*dev) |
|  | Stop the video device function. |
| static int | [video\_get\_caps](group__video__interface.md#ga4d5237607c858708380955705a2023bd) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_caps](structvideo__caps.md) \*caps) |
|  | Get the capabilities of a video endpoint. |
| static int | [video\_set\_ctrl](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
|  | Set the value of a control. |
| static int | [video\_get\_ctrl](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
|  | Get the current value of a control. |
| static int | [video\_set\_signal](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)) |
|  | Register/Unregister k\_poll signal for a video endpoint. |
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
| void | [video\_closest\_frmival](group__video__interface.md#ga67a86a3f920332347d8224a3074f6e23) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*match) |
|  | Find the closest match to a frame interval value within a video device. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [video\_bits\_per\_pixel](group__video__pixel__formats.md#gabdbd1b0f40af6663d81402deefdd387f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pixfmt) |
|  | Get number of bits per pixel of a pixel format. |

## Detailed Description

Public APIs for Video.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video.h](video_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
