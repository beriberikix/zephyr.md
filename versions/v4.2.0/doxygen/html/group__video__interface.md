---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__video__interface.html
original_path: doxygen/html/group__video__interface.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Video Interface

[Device Driver APIs](group__io__interfaces.md)

Video Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Video pixel formats](group__video__pixel__formats.md) |
|  | The '|' characters separate the pixels or logical blocks, and spaces separate the bytes. |

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
| struct | [video\_selection\_target](structvideo__selection__target.md) |
|  | Video selection target enum. [More...](structvideo__selection__target.md#details) |

| Macros | |
| --- | --- |
| #define | [LINE\_COUNT\_HEIGHT](#ga59e44ec7c8132f479f1aa71e5b2c6546)   (-1) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [video\_api\_format\_t](#ga964b301e45a42aa78799a1d9c9297ab1)) (const struct [device](structdevice.md) \*dev, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Function pointer type for video\_set/get\_format(). |
| typedef int(\* | [video\_api\_frmival\_t](#gaf63180944041a9e934c9f7567bdc1b88)) (const struct [device](structdevice.md) \*dev, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Function pointer type for video\_set/get\_frmival(). |
| typedef int(\* | [video\_api\_enum\_frmival\_t](#ga026c9a4531a125339e69b81f75343555)) (const struct [device](structdevice.md) \*dev, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie) |
|  | List all supported frame intervals of a given format. |
| typedef int(\* | [video\_api\_enqueue\_t](#gae6849a22140b3507bab219b579bc3d40)) (const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Enqueue a buffer in the driver’s incoming queue. |
| typedef int(\* | [video\_api\_dequeue\_t](#ga4265087c8faf62bbc36e88c0587022a1)) (const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Dequeue a buffer from the driver’s outgoing queue. |
| typedef int(\* | [video\_api\_flush\_t](#ga990ba001531c7300a06ca02d64c31eaa)) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
|  | Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue. |
| typedef int(\* | [video\_api\_set\_stream\_t](#gacda90bacb17a53e0bd11e5bfd37be57a)) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable, enum [video\_buf\_type](#gad386b2994b56844ebe713f156b9dfe4e) type) |
|  | Start or stop streaming on the video device. |
| typedef int(\* | [video\_api\_ctrl\_t](#ga522b4027fc6f22bf59f4face3c97e303)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cid) |
|  | Set/Get a video control value. |
| typedef int(\* | [video\_api\_get\_caps\_t](#ga070cb5f5bf35b98e2e7dda3378114780)) (const struct [device](structdevice.md) \*dev, struct [video\_caps](structvideo__caps.md) \*caps) |
|  | Get capabilities of a video endpoint. |
| typedef int(\* | [video\_api\_set\_signal\_t](#gad5aacb1386785a3587d41844c7854f83)) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Register/Unregister poll signal for buffer events. |
| typedef int(\* | [video\_api\_selection\_t](#gab4d2eb34f8ccc95fa6dcda7848f4408a)) (const struct [device](structdevice.md) \*dev, struct [video\_selection](structvideo__selection.md) \*sel) |
|  | Get/Set video selection (crop / compose). |

| Enumerations | |
| --- | --- |
| enum | [video\_buf\_type](#gad386b2994b56844ebe713f156b9dfe4e) { [VIDEO\_BUF\_TYPE\_INPUT](#ggad386b2994b56844ebe713f156b9dfe4ea20b003de365a7e2c32bba889ae78a3a1) , [VIDEO\_BUF\_TYPE\_OUTPUT](#ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083) } |
|  | [video\_buf\_type](#gad386b2994b56844ebe713f156b9dfe4e) enum [More...](#gad386b2994b56844ebe713f156b9dfe4e) |
| enum | [video\_frmival\_type](#ga6abf1fc9c35cf1d1648cde7616e7cad1) { [VIDEO\_FRMIVAL\_TYPE\_DISCRETE](#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4) = 1 , [VIDEO\_FRMIVAL\_TYPE\_STEPWISE](#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b) = 2 } |
|  | [video\_frmival\_type](#ga6abf1fc9c35cf1d1648cde7616e7cad1) enum [More...](#ga6abf1fc9c35cf1d1648cde7616e7cad1) |
| enum | [video\_signal\_result](#ga0f50f287c4075e992fbab6d8a990d7a8) { [VIDEO\_BUF\_DONE](#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8) , [VIDEO\_BUF\_ABORTED](#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8) , [VIDEO\_BUF\_ERROR](#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3) } |
|  | video\_event enum [More...](#ga0f50f287c4075e992fbab6d8a990d7a8) |
| enum | [video\_selection\_target](#gae375c0586e3505632cc69348935c9b54) {     [VIDEO\_SEL\_TGT\_CROP](#ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17) , [VIDEO\_SEL\_TGT\_CROP\_BOUND](#ggae375c0586e3505632cc69348935c9b54ab1b1302e553daefb9c1017e0bed9d8f1) , [VIDEO\_SEL\_TGT\_NATIVE\_SIZE](#ggae375c0586e3505632cc69348935c9b54a7536f3626e44f03775f09a1813ec8b20) , [VIDEO\_SEL\_TGT\_COMPOSE](#ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49) ,     [VIDEO\_SEL\_TGT\_COMPOSE\_BOUND](#ggae375c0586e3505632cc69348935c9b54a038df16bad455f389f5c24fc91c8bd4f)   } |

| Functions | |
| --- | --- |
| static int | [video\_set\_format](#gab93c2cb09bf5b0629b665cc4a079e3cd) (const struct [device](structdevice.md) \*dev, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Set video format. |
| static int | [video\_get\_format](#gad4a5849af21d20197169f0557329fdc1) (const struct [device](structdevice.md) \*dev, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Get video format. |
| static int | [video\_set\_frmival](#gac7a047582183dcdc4fed58ef9b9b4a84) (const struct [device](structdevice.md) \*dev, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Set video frame interval. |
| static int | [video\_get\_frmival](#gaf5a5bcd6e05d38a55a296b8290c3e0aa) (const struct [device](structdevice.md) \*dev, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Get video frame interval. |
| static int | [video\_enum\_frmival](#ga8141d7cb665fd975c4f852e40ba408e8) (const struct [device](structdevice.md) \*dev, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie) |
|  | List video frame intervals. |
| static int | [video\_enqueue](#gaca3d87049c7631f2edbbb673da94836a) (const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Enqueue a video buffer. |
| static int | [video\_dequeue](#ga45967c58a8cb6c18eac5b3ee3f1061f1) (const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Dequeue a video buffer. |
| static int | [video\_flush](#gaa670ffe1b3025ac48f132b4cac89693b) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
|  | Flush endpoint buffers. |
| static int | [video\_stream\_start](#ga835bb485fcf906cc5b27529a0fe218d3) (const struct [device](structdevice.md) \*dev, enum [video\_buf\_type](#gad386b2994b56844ebe713f156b9dfe4e) type) |
|  | Start the video device function. |
| static int | [video\_stream\_stop](#gaa8965272b3f2a7f6692b56ff569f190f) (const struct [device](structdevice.md) \*dev, enum [video\_buf\_type](#gad386b2994b56844ebe713f156b9dfe4e) type) |
|  | Stop the video device function. |
| static int | [video\_get\_caps](#ga903c7fff276274c9f3a9ac88be02cba2) (const struct [device](structdevice.md) \*dev, struct [video\_caps](structvideo__caps.md) \*caps) |
|  | Get the capabilities of a video endpoint. |
| int | [video\_set\_ctrl](#ga1cce17a3dfc881a1080708c7bc417aac) (const struct [device](structdevice.md) \*dev, struct [video\_control](structvideo__control.md) \*control) |
|  | Set the value of a control. |
| int | [video\_get\_ctrl](#ga71853c720e6df1def4c945e23d103298) (const struct [device](structdevice.md) \*dev, struct [video\_control](structvideo__control.md) \*control) |
|  | Get the current value of a control. |
| int | [video\_query\_ctrl](#ga8813a656a66adc6bfb10fb7f27194898) (struct [video\_ctrl\_query](structvideo__ctrl__query.md) \*cq) |
|  | Query information about a control. |
| void | [video\_print\_ctrl](#ga2bff04c6abc344350d6b0036289a701e) (const struct [video\_ctrl\_query](structvideo__ctrl__query.md) \*const cq) |
|  | Print all the information of a control. |
| static int | [video\_set\_signal](#gac67404c76cbd6183aee59f3b8243652b) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Register/Unregister k\_poll signal for a video endpoint. |
| static int | [video\_set\_selection](#ga21f2e7d6b5ec0c50ceeee580c6272613) (const struct [device](structdevice.md) \*dev, struct [video\_selection](structvideo__selection.md) \*sel) |
|  | Set video selection (crop/compose). |
| static int | [video\_get\_selection](#ga917889d41696ab12c92475b85caec13f) (const struct [device](structdevice.md) \*dev, struct [video\_selection](structvideo__selection.md) \*sel) |
|  | Get video selection (crop/compose). |
| struct [video\_buffer](structvideo__buffer.md) \* | [video\_buffer\_aligned\_alloc](#ga195914c7f03f2241702c77d41d1ab750) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate aligned video buffer. |
| struct [video\_buffer](structvideo__buffer.md) \* | [video\_buffer\_alloc](#gaee6eb26310a40d3f18161b3567f9e0a9) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate video buffer. |
| void | [video\_buffer\_release](#gad2661653db019b673153001b2c61b10f) (struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Release a video buffer. |
| int | [video\_format\_caps\_index](#gadbf59fd2d77b3d164cacf56bd4ae81ce) (const struct [video\_format\_cap](structvideo__format__cap.md) \*fmts, const struct [video\_format](structvideo__format.md) \*fmt, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*idx) |
|  | Search for a format that matches in a list of capabilities. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [video\_frmival\_nsec](#ga6b3c7456b2527cc441a100ff50787dc2) (const struct [video\_frmival](structvideo__frmival.md) \*frmival) |
|  | Compute the difference between two frame intervals. |
| void | [video\_closest\_frmival\_stepwise](#gad11314e82e9207449b3c0b29fdc830d0) (const struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) \*stepwise, const struct [video\_frmival](structvideo__frmival.md) \*desired, struct [video\_frmival](structvideo__frmival.md) \*match) |
|  | Find the closest match to a frame interval value within a stepwise frame interval. |
| void | [video\_closest\_frmival](#gaeeb67898719f094787d4157e8ce13209) (const struct [device](structdevice.md) \*dev, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*match) |
|  | Find the closest match to a frame interval value within a video device. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [video\_get\_csi\_link\_freq](#ga41e450607b4dc062fac682728ec7a79d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bpp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lane\_nb) |
|  | Return the link-frequency advertised by a device. |

| MIPI CSI2 Data-types | |
| --- | --- |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_NULL](#ga59d6f35198b6412a9aa78c094ecfaa19)   0x10 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_BLANKING](#gaede52c3391311b7cf931665afdeed720)   0x11 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_EMBEDDED\_8](#ga2b16d411ffcbcc7e74fa6aa2966b4b0d)   0x12 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV420\_8](#gab8001106ce7c91573012a895a4b3f1a8)   0x18 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV420\_10](#ga65dac1b59e00cb26e9af9e39663b20f0)   0x19 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV420\_CSPS\_8](#ga9c40ffb7a4042dd9d149e960eeddd14e)   0x1c |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV420\_CSPS\_10](#gad1d445cd3b576e4c7062f0a06f8dc71e)   0x1d |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV422\_8](#ga18dac33c3f8afd80e08d69ed78aee5a9)   0x1e |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_YUV422\_10](#ga4b530659596536d30168161139cc46fb)   0x1f |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RGB444](#ga04efc97a4dab0af7c7266ab104b8d626)   0x20 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RGB555](#ga351c2045810bb786d8232162f47fee7d)   0x21 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RGB565](#gad5f04e5dd3d5e0c5f67c64e28cd91c56)   0x22 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RGB666](#gaa452375e0454fa314eb140bac3c07e67)   0x23 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RGB888](#ga0d637375f7bf081967135139a8f6c5b6)   0x24 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW6](#gad251376f21a56d05742fcb68d228a677)   0x28 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW7](#ga384e8203e1bb7208a4bcb1e4931a929b)   0x29 |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW8](#ga6d3881edac75ba2c12185dc119311945)   0x2a |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW10](#ga64a52402a6883cb1b23a5524418528a9)   0x2b |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW12](#gadadb66f582b5e014336e29c1dafc3631)   0x2c |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_RAW14](#ga2ad6b8870c5dca6a8d19b1f80d83b81b)   0x2d |
| #define | [VIDEO\_MIPI\_CSI2\_DT\_USER](#ga98885f3584261947dd2b325bf12b2f3d)(n) |

## Detailed Description

Video Interface.

Since
:   2.1

Version
:   1.1.0

## Macro Definition Documentation

## [◆ ](#ga59e44ec7c8132f479f1aa71e5b2c6546)LINE\_COUNT\_HEIGHT

| #define LINE\_COUNT\_HEIGHT   (-1) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#gaede52c3391311b7cf931665afdeed720)VIDEO\_MIPI\_CSI2\_DT\_BLANKING

| #define VIDEO\_MIPI\_CSI2\_DT\_BLANKING   0x11 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga2b16d411ffcbcc7e74fa6aa2966b4b0d)VIDEO\_MIPI\_CSI2\_DT\_EMBEDDED\_8

| #define VIDEO\_MIPI\_CSI2\_DT\_EMBEDDED\_8   0x12 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga59d6f35198b6412a9aa78c094ecfaa19)VIDEO\_MIPI\_CSI2\_DT\_NULL

| #define VIDEO\_MIPI\_CSI2\_DT\_NULL   0x10 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga64a52402a6883cb1b23a5524418528a9)VIDEO\_MIPI\_CSI2\_DT\_RAW10

| #define VIDEO\_MIPI\_CSI2\_DT\_RAW10   0x2b |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#gadadb66f582b5e014336e29c1dafc3631)VIDEO\_MIPI\_CSI2\_DT\_RAW12

| #define VIDEO\_MIPI\_CSI2\_DT\_RAW12   0x2c |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga2ad6b8870c5dca6a8d19b1f80d83b81b)VIDEO\_MIPI\_CSI2\_DT\_RAW14

| #define VIDEO\_MIPI\_CSI2\_DT\_RAW14   0x2d |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#gad251376f21a56d05742fcb68d228a677)VIDEO\_MIPI\_CSI2\_DT\_RAW6

| #define VIDEO\_MIPI\_CSI2\_DT\_RAW6   0x28 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga384e8203e1bb7208a4bcb1e4931a929b)VIDEO\_MIPI\_CSI2\_DT\_RAW7

| #define VIDEO\_MIPI\_CSI2\_DT\_RAW7   0x29 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga6d3881edac75ba2c12185dc119311945)VIDEO\_MIPI\_CSI2\_DT\_RAW8

| #define VIDEO\_MIPI\_CSI2\_DT\_RAW8   0x2a |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga04efc97a4dab0af7c7266ab104b8d626)VIDEO\_MIPI\_CSI2\_DT\_RGB444

| #define VIDEO\_MIPI\_CSI2\_DT\_RGB444   0x20 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga351c2045810bb786d8232162f47fee7d)VIDEO\_MIPI\_CSI2\_DT\_RGB555

| #define VIDEO\_MIPI\_CSI2\_DT\_RGB555   0x21 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#gad5f04e5dd3d5e0c5f67c64e28cd91c56)VIDEO\_MIPI\_CSI2\_DT\_RGB565

| #define VIDEO\_MIPI\_CSI2\_DT\_RGB565   0x22 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#gaa452375e0454fa314eb140bac3c07e67)VIDEO\_MIPI\_CSI2\_DT\_RGB666

| #define VIDEO\_MIPI\_CSI2\_DT\_RGB666   0x23 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga0d637375f7bf081967135139a8f6c5b6)VIDEO\_MIPI\_CSI2\_DT\_RGB888

| #define VIDEO\_MIPI\_CSI2\_DT\_RGB888   0x24 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga98885f3584261947dd2b325bf12b2f3d)VIDEO\_MIPI\_CSI2\_DT\_USER

| #define VIDEO\_MIPI\_CSI2\_DT\_USER | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

**Value:**

(0x30 + (n))

## [◆ ](#ga65dac1b59e00cb26e9af9e39663b20f0)VIDEO\_MIPI\_CSI2\_DT\_YUV420\_10

| #define VIDEO\_MIPI\_CSI2\_DT\_YUV420\_10   0x19 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#gab8001106ce7c91573012a895a4b3f1a8)VIDEO\_MIPI\_CSI2\_DT\_YUV420\_8

| #define VIDEO\_MIPI\_CSI2\_DT\_YUV420\_8   0x18 |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#gad1d445cd3b576e4c7062f0a06f8dc71e)VIDEO\_MIPI\_CSI2\_DT\_YUV420\_CSPS\_10

| #define VIDEO\_MIPI\_CSI2\_DT\_YUV420\_CSPS\_10   0x1d |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga9c40ffb7a4042dd9d149e960eeddd14e)VIDEO\_MIPI\_CSI2\_DT\_YUV420\_CSPS\_8

| #define VIDEO\_MIPI\_CSI2\_DT\_YUV420\_CSPS\_8   0x1c |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga4b530659596536d30168161139cc46fb)VIDEO\_MIPI\_CSI2\_DT\_YUV422\_10

| #define VIDEO\_MIPI\_CSI2\_DT\_YUV422\_10   0x1f |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## [◆ ](#ga18dac33c3f8afd80e08d69ed78aee5a9)VIDEO\_MIPI\_CSI2\_DT\_YUV422\_8

| #define VIDEO\_MIPI\_CSI2\_DT\_YUV422\_8   0x1e |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

## Typedef Documentation

## [◆ ](#ga522b4027fc6f22bf59f4face3c97e303)video\_api\_ctrl\_t

| typedef int(\* video\_api\_ctrl\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cid) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Set/Get a video control value.

Parameters
:   | dev | Pointer to the device structure. |
    | --- | --- |
    | cid | Id of the control to set/get its value. |

## [◆ ](#ga4265087c8faf62bbc36e88c0587022a1)video\_api\_dequeue\_t

| typedef int(\* video\_api\_dequeue\_t) (const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Dequeue a buffer from the driver’s outgoing queue.

See [video\_dequeue()](#ga45967c58a8cb6c18eac5b3ee3f1061f1) for argument descriptions.

## [◆ ](#gae6849a22140b3507bab219b579bc3d40)video\_api\_enqueue\_t

| typedef int(\* video\_api\_enqueue\_t) (const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*buf) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Enqueue a buffer in the driver’s incoming queue.

See [video\_enqueue()](#gaca3d87049c7631f2edbbb673da94836a) for argument descriptions.

## [◆ ](#ga026c9a4531a125339e69b81f75343555)video\_api\_enum\_frmival\_t

| typedef int(\* video\_api\_enum\_frmival\_t) (const struct [device](structdevice.md) \*dev, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

List all supported frame intervals of a given format.

See [video\_enum\_frmival()](#ga8141d7cb665fd975c4f852e40ba408e8) for argument descriptions.

## [◆ ](#ga990ba001531c7300a06ca02d64c31eaa)video\_api\_flush\_t

| typedef int(\* video\_api\_flush\_t) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue.

See [video\_flush()](#gaa670ffe1b3025ac48f132b4cac89693b) for argument descriptions.

## [◆ ](#ga964b301e45a42aa78799a1d9c9297ab1)video\_api\_format\_t

| typedef int(\* video\_api\_format\_t) (const struct [device](structdevice.md) \*dev, struct [video\_format](structvideo__format.md) \*fmt) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Function pointer type for video\_set/get\_format().

See video\_set/get\_format() for argument descriptions.

## [◆ ](#gaf63180944041a9e934c9f7567bdc1b88)video\_api\_frmival\_t

| typedef int(\* video\_api\_frmival\_t) (const struct [device](structdevice.md) \*dev, struct [video\_frmival](structvideo__frmival.md) \*frmival) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Function pointer type for video\_set/get\_frmival().

See video\_set/get\_frmival() for argument descriptions.

## [◆ ](#ga070cb5f5bf35b98e2e7dda3378114780)video\_api\_get\_caps\_t

| typedef int(\* video\_api\_get\_caps\_t) (const struct [device](structdevice.md) \*dev, struct [video\_caps](structvideo__caps.md) \*caps) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Get capabilities of a video endpoint.

See [video\_get\_caps()](#ga903c7fff276274c9f3a9ac88be02cba2) for argument descriptions.

## [◆ ](#gab4d2eb34f8ccc95fa6dcda7848f4408a)video\_api\_selection\_t

| typedef int(\* video\_api\_selection\_t) (const struct [device](structdevice.md) \*dev, struct [video\_selection](structvideo__selection.md) \*sel) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Get/Set video selection (crop / compose).

See [video\_set\_selection](#ga21f2e7d6b5ec0c50ceeee580c6272613) and [video\_get\_selection](#ga917889d41696ab12c92475b85caec13f) for argument descriptions.

## [◆ ](#gad5aacb1386785a3587d41844c7854f83)video\_api\_set\_signal\_t

| typedef int(\* video\_api\_set\_signal\_t) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Register/Unregister poll signal for buffer events.

See [video\_set\_signal()](#gac67404c76cbd6183aee59f3b8243652b) for argument descriptions.

## [◆ ](#gacda90bacb17a53e0bd11e5bfd37be57a)video\_api\_set\_stream\_t

| typedef int(\* video\_api\_set\_stream\_t) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable, enum [video\_buf\_type](#gad386b2994b56844ebe713f156b9dfe4e) type) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Start or stop streaming on the video device.

Start (enable == true) or stop (enable == false) streaming on the video device.

Parameters
:   | dev | Pointer to the device structure. |
    | --- | --- |
    | enable | If true, start streaming, otherwise stop streaming. |
    | type | The type of the buffers stream to start or stop. |

Return values
:   | 0 | on success, otherwise a negative errno code. |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#gad386b2994b56844ebe713f156b9dfe4e)video\_buf\_type

| enum [video\_buf\_type](#gad386b2994b56844ebe713f156b9dfe4e) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

[video\_buf\_type](#gad386b2994b56844ebe713f156b9dfe4e) enum

Supported video buffer types of a video device. The direction (input or output) is defined from the device's point of view. Devices like cameras support only output type, encoders support only input types while m2m devices like ISP, PxP support both input and output types.

| Enumerator | |
| --- | --- |
| VIDEO\_BUF\_TYPE\_INPUT | input buffer type |
| VIDEO\_BUF\_TYPE\_OUTPUT | output buffer type |

## [◆ ](#ga6abf1fc9c35cf1d1648cde7616e7cad1)video\_frmival\_type

| enum [video\_frmival\_type](#ga6abf1fc9c35cf1d1648cde7616e7cad1) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

[video\_frmival\_type](#ga6abf1fc9c35cf1d1648cde7616e7cad1) enum

Supported frame interval type of a video device.

| Enumerator | |
| --- | --- |
| VIDEO\_FRMIVAL\_TYPE\_DISCRETE | discrete frame interval type |
| VIDEO\_FRMIVAL\_TYPE\_STEPWISE | stepwise frame interval type |

## [◆ ](#gae375c0586e3505632cc69348935c9b54)video\_selection\_target

| enum video\_selection\_target |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

| Enumerator | |
| --- | --- |
| VIDEO\_SEL\_TGT\_CROP | Current crop setting. |
| VIDEO\_SEL\_TGT\_CROP\_BOUND | Crop bound (aka the maximum crop achievable). |
| VIDEO\_SEL\_TGT\_NATIVE\_SIZE | Native size of the input frame. |
| VIDEO\_SEL\_TGT\_COMPOSE | Current compose setting. |
| VIDEO\_SEL\_TGT\_COMPOSE\_BOUND | Compose bound (aka the maximum compose achievable). |

## [◆ ](#ga0f50f287c4075e992fbab6d8a990d7a8)video\_signal\_result

| enum [video\_signal\_result](#ga0f50f287c4075e992fbab6d8a990d7a8) |
| --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

video\_event enum

Identify video event.

| Enumerator | |
| --- | --- |
| VIDEO\_BUF\_DONE |  |
| VIDEO\_BUF\_ABORTED |  |
| VIDEO\_BUF\_ERROR |  |

## Function Documentation

## [◆ ](#ga195914c7f03f2241702c77d41d1ab750)video\_buffer\_aligned\_alloc()

| struct [video\_buffer](structvideo__buffer.md) \* video\_buffer\_aligned\_alloc | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Allocate aligned video buffer.

Parameters
:   | size | Size of the video buffer (in bytes). |
    | --- | --- |
    | align | Alignment of the requested memory, must be a power of two. |
    | timeout | Timeout duration or K\_NO\_WAIT |

Return values
:   | pointer | to allocated video buffer |
    | --- | --- |

## [◆ ](#gaee6eb26310a40d3f18161b3567f9e0a9)video\_buffer\_alloc()

| struct [video\_buffer](structvideo__buffer.md) \* video\_buffer\_alloc | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Allocate video buffer.

Parameters
:   | size | Size of the video buffer (in bytes). |
    | --- | --- |
    | timeout | Timeout duration or K\_NO\_WAIT |

Return values
:   | pointer | to allocated video buffer |
    | --- | --- |

## [◆ ](#gad2661653db019b673153001b2c61b10f)video\_buffer\_release()

| void video\_buffer\_release | ( | struct [video\_buffer](structvideo__buffer.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Release a video buffer.

Parameters
:   | buf | Pointer to the video buffer to release. |
    | --- | --- |

## [◆ ](#gaeeb67898719f094787d4157e8ce13209)video\_closest\_frmival()

| void video\_closest\_frmival | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [video\_frmival\_enum](structvideo__frmival__enum.md) \* | *match* ) |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Find the closest match to a frame interval value within a video device.

To compute the closest match, fill `match` with the following fields:

- `match->format` to the [video\_format](structvideo__format.md "video_format") of interest.
- `match->type` to [VIDEO\_FRMIVAL\_TYPE\_DISCRETE](#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4).
- `match->discrete` to the desired frame interval.

The result will be loaded into `match`, with the following fields set:

- `match->discrete` to the value of the closest frame interval.
- `match->index` to the index of the closest frame interval.

Parameters
:   | dev | Video device to query. |
    | --- | --- |
    | match | Frame interval enumerator with the query, and loaded with the result. |

## [◆ ](#gad11314e82e9207449b3c0b29fdc830d0)video\_closest\_frmival\_stepwise()

| void video\_closest\_frmival\_stepwise | ( | const struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) \* | *stepwise*, |
| --- | --- | --- | --- |
|  |  | const struct [video\_frmival](structvideo__frmival.md) \* | *desired*, |
|  |  | struct [video\_frmival](structvideo__frmival.md) \* | *match* ) |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Find the closest match to a frame interval value within a stepwise frame interval.

Parameters
:   | stepwise | The stepwise frame interval range to search |
    | --- | --- |
    | desired | The frame interval for which find the closest match |
    | match | The resulting frame interval closest to `desired` |

## [◆ ](#ga45967c58a8cb6c18eac5b3ee3f1061f1)video\_dequeue()

| | int video\_dequeue | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [video\_buffer](structvideo__buffer.md) \*\* | *buf*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Dequeue a video buffer.

Dequeue a filled (capturing) or displayed (output) buffer from the driver’s endpoint outgoing queue.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | buf | Pointer a video buffer pointer. |
    | timeout | Timeout |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -EIO | General input / output error. |

## [◆ ](#gaca3d87049c7631f2edbbb673da94836a)video\_enqueue()

| | int video\_enqueue | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [video\_buffer](structvideo__buffer.md) \* | *buf* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Enqueue a video buffer.

Enqueue an empty (capturing) or filled (output) video buffer in the driver’s endpoint incoming queue.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | buf | Pointer to the video buffer. |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -EIO | General input / output error. |

## [◆ ](#ga8141d7cb665fd975c4f852e40ba408e8)video\_enum\_frmival()

| | int video\_enum\_frmival | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [video\_frmival\_enum](structvideo__frmival__enum.md) \* | *fie* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

List video frame intervals.

List all supported video frame intervals of a given format.

Applications should fill the pixelformat, width and height fields of the [video\_frmival\_enum](structvideo__frmival__enum.md "Video frame interval enumeration structure.") struct first to form a query. Then, the index field is used to iterate through the supported frame intervals list.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | fie | Pointer to a video frame interval enumeration struct. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If API is not implemented. |
    | -EINVAL | If parameters are invalid. |
    | -EIO | General input / output error. |

## [◆ ](#gaa670ffe1b3025ac48f132b4cac89693b)video\_flush()

| | int video\_flush | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *cancel* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Flush endpoint buffers.

A call to flush finishes when all endpoint buffers have been moved from incoming queue to outgoing queue. Either because canceled or fully processed through the video function.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | cancel | If true, cancel buffer processing instead of waiting for completion. |

Return values
:   | 0 | Is successful, -ERRNO code otherwise. |
    | --- | --- |

## [◆ ](#gadbf59fd2d77b3d164cacf56bd4ae81ce)video\_format\_caps\_index()

| int video\_format\_caps\_index | ( | const struct [video\_format\_cap](structvideo__format__cap.md) \* | *fmts*, |
| --- | --- | --- | --- |
|  |  | const struct [video\_format](structvideo__format.md) \* | *fmt*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *idx* ) |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Search for a format that matches in a list of capabilities.

Parameters
:   | fmts | The format capability list to search. |
    | --- | --- |
    | fmt | The format to find in the list. |
    | idx | The pointer to a number of the first format that matches. |

Returns
:   0 when a format is found.
:   -ENOENT when no matching format is found.

## [◆ ](#ga6b3c7456b2527cc441a100ff50787dc2)video\_frmival\_nsec()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) video\_frmival\_nsec | ( | const struct [video\_frmival](structvideo__frmival.md) \* | *frmival* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Compute the difference between two frame intervals.

Parameters
:   | frmival | Frame interval to turn into microseconds. |
    | --- | --- |

Returns
:   The frame interval value in microseconds.

## [◆ ](#ga903c7fff276274c9f3a9ac88be02cba2)video\_get\_caps()

| | int video\_get\_caps | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [video\_caps](structvideo__caps.md) \* | *caps* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Get the capabilities of a video endpoint.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | caps | Pointer to the [video\_caps](structvideo__caps.md "Video format capabilities.") struct to fill. |

Return values
:   | 0 | Is successful, -ERRNO code otherwise. |
    | --- | --- |

## [◆ ](#ga41e450607b4dc062fac682728ec7a79d)video\_get\_csi\_link\_freq()

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) video\_get\_csi\_link\_freq | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bpp*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *lane\_nb* ) |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Return the link-frequency advertised by a device.

Device exposing a CSI link should advertise at least one of the following two controls:

- [VIDEO\_CID\_LINK\_FREQ](group__video__controls.md#ga2142e2819c445b70d82067a3cfb193c8 "VIDEO_CID_LINK_FREQ")
- [VIDEO\_CID\_PIXEL\_RATE](group__video__controls.md#ga6f6eaed7defdbb5f440874c7c6d0a6eb "VIDEO_CID_PIXEL_RATE")

At first the helper will try read the [VIDEO\_CID\_LINK\_FREQ](group__video__controls.md#ga2142e2819c445b70d82067a3cfb193c8 "VIDEO_CID_LINK_FREQ") and if not available will approximate the link-frequency from the [VIDEO\_CID\_PIXEL\_RATE](group__video__controls.md#ga6f6eaed7defdbb5f440874c7c6d0a6eb "VIDEO_CID_PIXEL_RATE") value, taking into consideration the bits per pixel of the format and the number of lanes.

Parameters
:   | dev | Video device to query. |
    | --- | --- |
    | bpp | Amount of bits per pixel of the pixel format produced by the device |
    | lane\_nb | Number of CSI-2 lanes used |

## [◆ ](#ga71853c720e6df1def4c945e23d103298)video\_get\_ctrl()

| int video\_get\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [video\_control](structvideo__control.md) \* | *control* ) |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Get the current value of a control.

This retrieve the value of a video control, value type depends on control ID, and must be interpreted accordingly.

Parameters
:   | dev | Pointer to the device structure. |
    | --- | --- |
    | control | Pointer to the video control struct. |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -ENOTSUP | If format is not supported. |
    | -EIO | General input / output error. |

## [◆ ](#gad4a5849af21d20197169f0557329fdc1)video\_get\_format()

| | int video\_get\_format | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [video\_format](structvideo__format.md) \* | *fmt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Get video format.

Get video device current video format.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | fmt | Pointer to video format struct. |

Return values
:   | pointer | to video format |
    | --- | --- |

## [◆ ](#gaf5a5bcd6e05d38a55a296b8290c3e0aa)video\_get\_frmival()

| | int video\_get\_frmival | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [video\_frmival](structvideo__frmival.md) \* | *frmival* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Get video frame interval.

Get current frame interval of the video device.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | frmival | Pointer to a video frame interval struct. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If API is not implemented. |
    | -EINVAL | If parameters are invalid. |
    | -EIO | General input / output error. |

## [◆ ](#ga917889d41696ab12c92475b85caec13f)video\_get\_selection()

| | int video\_get\_selection | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [video\_selection](structvideo__selection.md) \* | *sel* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Get video selection (crop/compose).

Retrieve the current settings related to the crop and compose of the video device. This can also be used to read the native size of the input stream of the video device. This function can be used to read crop / compose capabilities of the device prior to performing configuration via the [video\_set\_selection](#ga21f2e7d6b5ec0c50ceeee580c6272613) api.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | sel | Pointer to a video selection structure, `type` and `target` set by the caller |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -ENOTSUP | If format is not supported. |
    | -EIO | General input / output error. |

## [◆ ](#ga2bff04c6abc344350d6b0036289a701e)video\_print\_ctrl()

| void video\_print\_ctrl | ( | const struct [video\_ctrl\_query](structvideo__ctrl__query.md) \*const | *cq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Print all the information of a control.

Print all the information of a control including its name, type, flag, range, menu (if any) and current value, i.e. by invoking the [video\_get\_ctrl()](#ga71853c720e6df1def4c945e23d103298), in a human readble format.

Parameters
:   | cq | Pointer to the control query struct. |
    | --- | --- |

## [◆ ](#ga8813a656a66adc6bfb10fb7f27194898)video\_query\_ctrl()

| int video\_query\_ctrl | ( | struct [video\_ctrl\_query](structvideo__ctrl__query.md) \* | *cq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Query information about a control.

Applications set the id field of the query structure, the function fills the rest of this structure. It is possible to enumerate base class controls (i.e., VIDEO\_CID\_BASE + x) by calling this function with successive id values starting from VIDEO\_CID\_BASE up to and exclusive VIDEO\_CID\_LASTP1. The function may return -ENOTSUP if a control in this range is not supported. Applications can also enumerate private controls by starting at VIDEO\_CID\_PRIVATE\_BASE and incrementing the id until the driver returns -ENOTSUP. For other control classes, it's a bit more difficult. Hence, the best way to enumerate all kinds of device's supported controls is to iterate with VIDEO\_CTRL\_FLAG\_NEXT\_CTRL.

Parameters
:   | cq | Pointer to the control query struct. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If the control id is invalid. |
    | -ENOTSUP | If the control id is not supported. |

## [◆ ](#ga1cce17a3dfc881a1080708c7bc417aac)video\_set\_ctrl()

| int video\_set\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [video\_control](structvideo__control.md) \* | *control* ) |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Set the value of a control.

This set the value of a video control, value type depends on control ID, and must be interpreted accordingly.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | control | Pointer to the video control struct. |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -ENOTSUP | If format is not supported. |
    | -EIO | General input / output error. |

## [◆ ](#gab93c2cb09bf5b0629b665cc4a079e3cd)video\_set\_format()

| | int video\_set\_format | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [video\_format](structvideo__format.md) \* | *fmt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Set video format.

Configure video device with a specific format.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | fmt | Pointer to a video format struct. |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -ENOTSUP | If format is not supported. |
    | -EIO | General input / output error. |

## [◆ ](#gac7a047582183dcdc4fed58ef9b9b4a84)video\_set\_frmival()

| | int video\_set\_frmival | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [video\_frmival](structvideo__frmival.md) \* | *frmival* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Set video frame interval.

Configure video device with a specific frame interval.

Drivers must not return an error solely because the requested interval doesn’t match the device capabilities. They must instead modify the interval to match what the hardware can provide.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | frmival | Pointer to a video frame interval struct. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If API is not implemented. |
    | -EINVAL | If parameters are invalid. |
    | -EIO | General input / output error. |

## [◆ ](#ga21f2e7d6b5ec0c50ceeee580c6272613)video\_set\_selection()

| | int video\_set\_selection | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [video\_selection](structvideo__selection.md) \* | *sel* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Set video selection (crop/compose).

Configure the optional crop and compose feature of a video device. Crop is first applied on the input frame, and the result of that crop is applied to the compose. The result of the compose (width/height) is equal to the format width/height given to the [video\_set\_format](#gab93c2cb09bf5b0629b665cc4a079e3cd) function.

Some targets are inter-dependents. For instance, setting a [VIDEO\_SEL\_TGT\_CROP](#ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17) will reset [VIDEO\_SEL\_TGT\_COMPOSE](#ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49) to the same size.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | sel | Pointer to a video selection structure |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -ENOTSUP | If format is not supported. |
    | -EIO | General input / output error. |

## [◆ ](#gac67404c76cbd6183aee59f3b8243652b)video\_set\_signal()

| | int video\_set\_signal | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Register/Unregister k\_poll signal for a video endpoint.

Register a poll signal to the endpoint, which will be signaled on frame completion (done, aborted, error). Registering a NULL poll signal unregisters any previously registered signal.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | sig | Pointer to [k\_poll\_signal](structk__poll__signal.md) |

Return values
:   | 0 | Is successful, -ERRNO code otherwise. |
    | --- | --- |

## [◆ ](#ga835bb485fcf906cc5b27529a0fe218d3)video\_stream\_start()

| | int video\_stream\_start | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [video\_buf\_type](#gad386b2994b56844ebe713f156b9dfe4e) | *type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Start the video device function.

video\_stream\_start is called to enter ‘streaming’ state (capture, output...). The driver may receive buffers with [video\_enqueue()](#gaca3d87049c7631f2edbbb673da94836a) before video\_stream\_start is called. If driver/device needs a minimum number of buffers before being able to start streaming, then driver set the min\_vbuf\_count to the related endpoint capabilities.

Parameters
:   | dev | Pointer to the device structure. |
    | --- | --- |
    | type | The type of the buffers stream to start. |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#gaa8965272b3f2a7f6692b56ff569f190f)video\_stream\_stop()

| | int video\_stream\_stop | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [video\_buf\_type](#gad386b2994b56844ebe713f156b9dfe4e) | *type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/video.h](video_8h.md)>`

Stop the video device function.

On video\_stream\_stop, driver must stop any transactions or wait until they finish.

Parameters
:   | dev | Pointer to the device structure. |
    | --- | --- |
    | type | The type of the buffers stream to stop. |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EIO | General input / output error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
