---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__video__interface.html
original_path: doxygen/html/group__video__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| #define | [video\_fourcc](#gabeacdd211927e893561446fd7299ab08)(a, b, c, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [video\_api\_set\_format\_t](#gaf6e1ac05a51ae9afaf2569311853ee18)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Set video format. |
| typedef int(\* | [video\_api\_get\_format\_t](#ga7c85f21c1e1839bce84bbce3e339903d)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Get current video format. |
| typedef int(\* | [video\_api\_enqueue\_t](#ga161a0320e7e84935f809d6460064c0fe)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Enqueue a buffer in the driver’s incoming queue. |
| typedef int(\* | [video\_api\_dequeue\_t](#ga16c82da50c6024d36b65fd1c6f33721d)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Dequeue a buffer from the driver’s outgoing queue. |
| typedef int(\* | [video\_api\_flush\_t](#gad308f355cd9d5a5d56bd0c81d31626db)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
|  | Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue. |
| typedef int(\* | [video\_api\_stream\_start\_t](#ga06fe3e6bfed2d817c5c239161d8a777e)) (const struct [device](structdevice.md) \*dev) |
|  | Start the capture or output process. |
| typedef int(\* | [video\_api\_stream\_stop\_t](#ga5e8564970bd5cc3b57ee23ff223460bd)) (const struct [device](structdevice.md) \*dev) |
|  | Stop the capture or output process. |
| typedef int(\* | [video\_api\_set\_ctrl\_t](#gad392294a57d6fb191058cf852a5adc8a)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
|  | Set a video control value. |
| typedef int(\* | [video\_api\_get\_ctrl\_t](#gaa0779e606de3ec27e1e9230cd13a090c)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
|  | Get a video control value. |
| typedef int(\* | [video\_api\_get\_caps\_t](#gad4a0c666d5534f9daed7d3c9a00c1312)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_caps](structvideo__caps.md) \*caps) |
|  | Get capabilities of a video endpoint. |
| typedef int(\* | [video\_api\_set\_signal\_t](#ga9d08347300d2e3c8dc7ae01d2902d321)) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [k\_poll\_signal](structk__poll__signal.md) \*signal) |
|  | Register/Unregister poll signal for buffer events. |

| Enumerations | |
| --- | --- |
| enum | [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) { [VIDEO\_EP\_NONE](#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7) , [VIDEO\_EP\_ANY](#ggafa3d076a1324ea54b5c5ec7806cb2ef9a450d124253f8463114b851b1e51960fb) , [VIDEO\_EP\_IN](#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7) , [VIDEO\_EP\_OUT](#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a) } |
|  | [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) enum [More...](#gafa3d076a1324ea54b5c5ec7806cb2ef9) |
| enum | [video\_signal\_result](#ga0f50f287c4075e992fbab6d8a990d7a8) { [VIDEO\_BUF\_DONE](#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8) , [VIDEO\_BUF\_ABORTED](#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8) , [VIDEO\_BUF\_ERROR](#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3) } |
|  | video\_event enum [More...](#ga0f50f287c4075e992fbab6d8a990d7a8) |

| Functions | |
| --- | --- |
| static int | [video\_set\_format](#gae38df95199e41ac197b9754824b2bd29) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Set video format. |
| static int | [video\_get\_format](#gac0964bd0b57c6be5e773a21af0438edc) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
|  | Get video format. |
| static int | [video\_enqueue](#gac19d14a5875d48c96bd66a8bb65e8a51) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Enqueue a video buffer. |
| static int | [video\_dequeue](#ga9862024c9b07855609ea2078680c9afd) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Dequeue a video buffer. |
| static int | [video\_flush](#gae5e6256ab799ca1cbbac4987b82bb145) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
|  | Flush endpoint buffers. |
| static int | [video\_stream\_start](#ga7145a18ad5e3e5d74398c89c00ea19f0) (const struct [device](structdevice.md) \*dev) |
|  | Start the video device function. |
| static int | [video\_stream\_stop](#ga6464dede55777c9082e85d6af43a4d48) (const struct [device](structdevice.md) \*dev) |
|  | Stop the video device function. |
| static int | [video\_get\_caps](#ga4d5237607c858708380955705a2023bd) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_caps](structvideo__caps.md) \*caps) |
|  | Get the capabilities of a video endpoint. |
| static int | [video\_set\_ctrl](#ga87873a4612cfbd2cb62595dec15cb77e) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
|  | Set the value of a control. |
| static int | [video\_get\_ctrl](#ga664122e82da802f1dff8b5c30e158acd) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
|  | Get the current value of a control. |
| static int | [video\_set\_signal](#gab38a9f956f5d5452fc6e0c0f1bf382be) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [k\_poll\_signal](structk__poll__signal.md) \*signal) |
|  | Register/Unregister k\_poll signal for a video endpoint. |
| struct [video\_buffer](structvideo__buffer.md) \* | [video\_buffer\_alloc](#ga8454f5568e24cf7b8a59dde765b4a804) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate video buffer. |
| void | [video\_buffer\_release](#gad2661653db019b673153001b2c61b10f) (struct [video\_buffer](structvideo__buffer.md) \*buf) |
|  | Release a video buffer. |

## Detailed Description

Video Interface.

## Macro Definition Documentation

## [◆ ](#gabeacdd211927e893561446fd7299ab08)video\_fourcc

| #define video\_fourcc | ( |  | *a*, |
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

## Typedef Documentation

## [◆ ](#ga16c82da50c6024d36b65fd1c6f33721d)video\_api\_dequeue\_t

| typedef int(\* video\_api\_dequeue\_t) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
| --- |

`#include <[video.h](video_8h.md)>`

Dequeue a buffer from the driver’s outgoing queue.

See [video\_dequeue()](#ga9862024c9b07855609ea2078680c9afd) for argument descriptions.

## [◆ ](#ga161a0320e7e84935f809d6460064c0fe)video\_api\_enqueue\_t

| typedef int(\* video\_api\_enqueue\_t) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_buffer](structvideo__buffer.md) \*buf) |
| --- |

`#include <[video.h](video_8h.md)>`

Enqueue a buffer in the driver’s incoming queue.

See [video\_enqueue()](#gac19d14a5875d48c96bd66a8bb65e8a51) for argument descriptions.

## [◆ ](#gad308f355cd9d5a5d56bd0c81d31626db)video\_api\_flush\_t

| typedef int(\* video\_api\_flush\_t) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) cancel) |
| --- |

`#include <[video.h](video_8h.md)>`

Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue.

See [video\_flush()](#gae5e6256ab799ca1cbbac4987b82bb145) for argument descriptions.

## [◆ ](#gad4a0c666d5534f9daed7d3c9a00c1312)video\_api\_get\_caps\_t

| typedef int(\* video\_api\_get\_caps\_t) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_caps](structvideo__caps.md) \*caps) |
| --- |

`#include <[video.h](video_8h.md)>`

Get capabilities of a video endpoint.

See [video\_get\_caps()](#ga4d5237607c858708380955705a2023bd) for argument descriptions.

## [◆ ](#gaa0779e606de3ec27e1e9230cd13a090c)video\_api\_get\_ctrl\_t

| typedef int(\* video\_api\_get\_ctrl\_t) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
| --- |

`#include <[video.h](video_8h.md)>`

Get a video control value.

See [video\_get\_ctrl()](#ga664122e82da802f1dff8b5c30e158acd) for argument descriptions.

## [◆ ](#ga7c85f21c1e1839bce84bbce3e339903d)video\_api\_get\_format\_t

| typedef int(\* video\_api\_get\_format\_t) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
| --- |

`#include <[video.h](video_8h.md)>`

Get current video format.

See [video\_get\_format()](#gac0964bd0b57c6be5e773a21af0438edc) for argument descriptions.

## [◆ ](#gad392294a57d6fb191058cf852a5adc8a)video\_api\_set\_ctrl\_t

| typedef int(\* video\_api\_set\_ctrl\_t) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cid, void \*value) |
| --- |

`#include <[video.h](video_8h.md)>`

Set a video control value.

See [video\_set\_ctrl()](#ga87873a4612cfbd2cb62595dec15cb77e) for argument descriptions.

## [◆ ](#gaf6e1ac05a51ae9afaf2569311853ee18)video\_api\_set\_format\_t

| typedef int(\* video\_api\_set\_format\_t) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [video\_format](structvideo__format.md) \*fmt) |
| --- |

`#include <[video.h](video_8h.md)>`

Set video format.

See [video\_set\_format()](#gae38df95199e41ac197b9754824b2bd29) for argument descriptions.

## [◆ ](#ga9d08347300d2e3c8dc7ae01d2902d321)video\_api\_set\_signal\_t

| typedef int(\* video\_api\_set\_signal\_t) (const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, struct [k\_poll\_signal](structk__poll__signal.md) \*signal) |
| --- |

`#include <[video.h](video_8h.md)>`

Register/Unregister poll signal for buffer events.

See [video\_set\_signal()](#gab38a9f956f5d5452fc6e0c0f1bf382be) for argument descriptions.

## [◆ ](#ga06fe3e6bfed2d817c5c239161d8a777e)video\_api\_stream\_start\_t

| typedef int(\* video\_api\_stream\_start\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[video.h](video_8h.md)>`

Start the capture or output process.

See [video\_stream\_start()](#ga7145a18ad5e3e5d74398c89c00ea19f0) for argument descriptions.

## [◆ ](#ga5e8564970bd5cc3b57ee23ff223460bd)video\_api\_stream\_stop\_t

| typedef int(\* video\_api\_stream\_stop\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[video.h](video_8h.md)>`

Stop the capture or output process.

See [video\_stream\_stop()](#ga6464dede55777c9082e85d6af43a4d48) for argument descriptions.

## Enumeration Type Documentation

## [◆ ](#gafa3d076a1324ea54b5c5ec7806cb2ef9)video\_endpoint\_id

| enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) |
| --- |

`#include <[video.h](video_8h.md)>`

[video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) enum

Identify the video device endpoint.

| Enumerator | |
| --- | --- |
| VIDEO\_EP\_NONE |  |
| VIDEO\_EP\_ANY |  |
| VIDEO\_EP\_IN |  |
| VIDEO\_EP\_OUT |  |

## [◆ ](#ga0f50f287c4075e992fbab6d8a990d7a8)video\_signal\_result

| enum [video\_signal\_result](#ga0f50f287c4075e992fbab6d8a990d7a8) |
| --- |

`#include <[video.h](video_8h.md)>`

video\_event enum

Identify video event.

| Enumerator | |
| --- | --- |
| VIDEO\_BUF\_DONE |  |
| VIDEO\_BUF\_ABORTED |  |
| VIDEO\_BUF\_ERROR |  |

## Function Documentation

## [◆ ](#ga8454f5568e24cf7b8a59dde765b4a804)video\_buffer\_alloc()

| struct [video\_buffer](structvideo__buffer.md) \* video\_buffer\_alloc | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Allocate video buffer.

Parameters
:   | size | Size of the video buffer. |
    | --- | --- |

Return values
:   | pointer | to allocated video buffer |
    | --- | --- |

## [◆ ](#gad2661653db019b673153001b2c61b10f)video\_buffer\_release()

| void video\_buffer\_release | ( | struct [video\_buffer](structvideo__buffer.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Release a video buffer.

Parameters
:   | buf | Pointer to the video buffer to release. |
    | --- | --- |

## [◆ ](#ga9862024c9b07855609ea2078680c9afd)video\_dequeue()

| | int video\_dequeue | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) | *ep*, | |  |  | struct [video\_buffer](structvideo__buffer.md) \*\* | *buf*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Dequeue a video buffer.

Dequeue a filled (capturing) or displayed (output) buffer from the driver’s endpoint outgoing queue.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ep | Endpoint ID. |
    | buf | Pointer a video buffer pointer. |
    | timeout | Timeout |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -EIO | General input / output error. |

## [◆ ](#gac19d14a5875d48c96bd66a8bb65e8a51)video\_enqueue()

| | int video\_enqueue | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) | *ep*, | |  |  | struct [video\_buffer](structvideo__buffer.md) \* | *buf* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Enqueue a video buffer.

Enqueue an empty (capturing) or filled (output) video buffer in the driver’s endpoint incoming queue.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ep | Endpoint ID. |
    | buf | Pointer to the video buffer. |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -EIO | General input / output error. |

## [◆ ](#gae5e6256ab799ca1cbbac4987b82bb145)video\_flush()

| | int video\_flush | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) | *ep*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *cancel* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Flush endpoint buffers.

A call to flush finishes when all endpoint buffers have been moved from incoming queue to outgoing queue. Either because canceled or fully processed through the video function.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ep | Endpoint ID. |
    | cancel | If true, cancel buffer processing instead of waiting for completion. |

Return values
:   | 0 | Is successful, -ERRNO code otherwise. |
    | --- | --- |

## [◆ ](#ga4d5237607c858708380955705a2023bd)video\_get\_caps()

| | int video\_get\_caps | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) | *ep*, | |  |  | struct [video\_caps](structvideo__caps.md) \* | *caps* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Get the capabilities of a video endpoint.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ep | Endpoint ID. |
    | caps | Pointer to the [video\_caps](structvideo__caps.md "Video format capabilities.") struct to fill. |

Return values
:   | 0 | Is successful, -ERRNO code otherwise. |
    | --- | --- |

## [◆ ](#ga664122e82da802f1dff8b5c30e158acd)video\_get\_ctrl()

| | int video\_get\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *cid*, | |  |  | void \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Get the current value of a control.

This retrieve the value of a video control, value type depends on control ID, and must be interpreted accordingly.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | cid | Control ID. |
    | value | Pointer to the control value. |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -ENOTSUP | If format is not supported. |
    | -EIO | General input / output error. |

## [◆ ](#gac0964bd0b57c6be5e773a21af0438edc)video\_get\_format()

| | int video\_get\_format | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) | *ep*, | |  |  | struct [video\_format](structvideo__format.md) \* | *fmt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Get video format.

Get video device current video format.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ep | Endpoint ID. |
    | fmt | Pointer to video format struct. |

Return values
:   | pointer | to video format |
    | --- | --- |

## [◆ ](#ga87873a4612cfbd2cb62595dec15cb77e)video\_set\_ctrl()

| | int video\_set\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *cid*, | |  |  | void \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Set the value of a control.

This set the value of a video control, value type depends on control ID, and must be interpreted accordingly.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | cid | Control ID. |
    | value | Pointer to the control value. |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -ENOTSUP | If format is not supported. |
    | -EIO | General input / output error. |

## [◆ ](#gae38df95199e41ac197b9754824b2bd29)video\_set\_format()

| | int video\_set\_format | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) | *ep*, | |  |  | struct [video\_format](structvideo__format.md) \* | *fmt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Set video format.

Configure video device with a specific format.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ep | Endpoint ID. |
    | fmt | Pointer to a video format struct. |

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EINVAL | If parameters are invalid. |
    | -ENOTSUP | If format is not supported. |
    | -EIO | General input / output error. |

## [◆ ](#gab38a9f956f5d5452fc6e0c0f1bf382be)video\_set\_signal()

| | int video\_set\_signal | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [video\_endpoint\_id](#gafa3d076a1324ea54b5c5ec7806cb2ef9) | *ep*, | |  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *signal* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Register/Unregister k\_poll signal for a video endpoint.

Register a poll signal to the endpoint, which will be signaled on frame completion (done, aborted, error). Registering a NULL poll signal unregisters any previously registered signal.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ep | Endpoint ID. |
    | signal | Pointer to [k\_poll\_signal](structk__poll__signal.md) |

Return values
:   | 0 | Is successful, -ERRNO code otherwise. |
    | --- | --- |

## [◆ ](#ga7145a18ad5e3e5d74398c89c00ea19f0)video\_stream\_start()

| | int video\_stream\_start | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Start the video device function.

video\_stream\_start is called to enter ‘streaming’ state (capture, output...). The driver may receive buffers with [video\_enqueue()](#gac19d14a5875d48c96bd66a8bb65e8a51) before video\_stream\_start is called. If driver/device needs a minimum number of buffers before being able to start streaming, then driver set the min\_vbuf\_count to the related endpoint capabilities.

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#ga6464dede55777c9082e85d6af43a4d48)video\_stream\_stop()

| | int video\_stream\_stop | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[video.h](video_8h.md)>`

Stop the video device function.

On video\_stream\_stop, driver must stop any transactions or wait until they finish.

Return values
:   | 0 | Is successful. |
    | --- | --- |
    | -EIO | General input / output error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
