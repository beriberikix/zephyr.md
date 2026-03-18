---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/video_8h.html
original_path: doxygen/html/video_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video.h File Reference

Public APIs for Video.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/drivers/video-controls.h](video-controls_8h_source.md)>`

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
| struct | [video\_driver\_api](structvideo__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)(a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
| Bayer formats | |
| #define | [VIDEO\_PIX\_FMT\_BGGR8](group__video__pixel__formats.md#ga64ad74bb6c92041a4190614b684ae024)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('B', 'G', 'G', 'R') /\* 8 BGBG.. GRGR.. \*/ |
|  | BGGR8 pixel format. |
| #define | [VIDEO\_PIX\_FMT\_GBRG8](group__video__pixel__formats.md#gaebdfd9d4230b56f6b8533630356b8793)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('G', 'B', 'R', 'G') /\* 8 GBGB.. RGRG.. \*/ |
|  | GBRG8 pixel format. |
| #define | [VIDEO\_PIX\_FMT\_GRBG8](group__video__pixel__formats.md#ga6b9c8d43406e45927f4e9e94504eae9c)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('G', 'R', 'B', 'G') /\* 8 GRGR.. BGBG.. \*/ |
|  | GRBG8 pixel format. |
| #define | [VIDEO\_PIX\_FMT\_RGGB8](group__video__pixel__formats.md#ga0c98dc205b724c9e4556e41cc266d80e)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('R', 'G', 'G', 'B') /\* 8 RGRG.. GBGB.. \*/ |
|  | RGGB8 pixel format. |
| RGB formats | |
| #define | [VIDEO\_PIX\_FMT\_RGB565](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('R', 'G', 'B', 'P') /\* 16 RGB-5-6-5 \*/ |
|  | RGB565 pixel format. |
| YUV formats | |
| #define | [VIDEO\_PIX\_FMT\_YUYV](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('Y', 'U', 'Y', 'V') /\* 16 Y0-Cb0 Y1-Cr0 \*/ |
|  | YUYV pixel format. |
| JPEG formats | |
| #define | [VIDEO\_PIX\_FMT\_JPEG](group__video__pixel__formats.md#ga035a13c38c4f123411547e2c40d58bd2)   [video\_fourcc](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)('J', 'P', 'E', 'G') /\* 8 JPEG \*/ |
|  | JPEG pixel format. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Set video format. |
| typedef int(\* | [video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Get current video format. |
| typedef int(\* | [video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Enqueue a buffer in the driver’s incoming queue. |
| typedef int(\* | [video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Dequeue a buffer from the driver’s outgoing queue. |
| typedef int(\* | [video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
|  | Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue. |
| typedef int(\* | [video\_api\_stream\_start\_t](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e)) (const struct [device](structdevice.md) \*dev) |
|  | Start the capture or output process. |
| typedef int(\* | [video\_api\_stream\_stop\_t](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd)) (const struct [device](structdevice.md) \*dev) |
|  | Stop the capture or output process. |
| typedef int(\* | [video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
|  | Set a video control value. |
| typedef int(\* | [video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
|  | Get a video control value. |
| typedef int(\* | [video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_caps](structvideo__caps.md) \*caps) |
|  | Get capabilities of a video endpoint. |
| typedef int(\* | [video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [k\_poll\_signal](structk__poll__signal.md) \*signal) |
|  | Register/Unregister poll signal for buffer events. |

| Enumerations | |
| --- | --- |
| enum | [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) { [VIDEO\_EP\_NONE](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7) , [VIDEO\_EP\_ANY](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a450d124253f8463114b851b1e51960fb) , [VIDEO\_EP\_IN](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7) , [VIDEO\_EP\_OUT](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a) } |
|  | [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9 "video_endpoint_id enum") enum [More...](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) |
| enum | [video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8) { [VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8) , [VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8) , [VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3) } |
|  | video\_event enum [More...](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8) |

| Functions | |
| --- | --- |
| static int | [video\_set\_format](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Set video format. |
| static int | [video\_get\_format](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Get video format. |
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
| static int | [video\_set\_signal](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [k\_poll\_signal](structk__poll__signal.md) \*signal) |
|  | Register/Unregister k\_poll signal for a video endpoint. |
| struct [video\_buffer](structvideo__buffer.md) \* | [video\_buffer\_alloc](group__video__interface.md#ga8454f5568e24cf7b8a59dde765b4a804) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate video buffer. |
| void | [video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f) (struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Release a video buffer. |

## Detailed Description

Public APIs for Video.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video.h](video_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
