---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structvideo__caps.html
original_path: doxygen/html/structvideo__caps.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [min\_line\_count](#a3ab95e55cd093f2414937a1916ef7f52) |
|  | Denotes minimum line count of a video buffer that this endpoint can fill or process. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [max\_line\_count](#a51a059da1f30cac333ad6aad4c37d739) |
|  | Denotes maximum line count of a video buffer that this endpoint can fill or process. |

## Detailed Description

Video format capabilities.

Used to describe video endpoint capabilities.

## Field Documentation

## [◆ ](#adb454a88504d9fd6e40510171a53b185)format\_caps

| const struct [video\_format\_cap](structvideo__format__cap.md)\* video\_caps::format\_caps |
| --- |

list of video format capabilities (zero terminated).

## [◆ ](#a51a059da1f30cac333ad6aad4c37d739)max\_line\_count

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) video\_caps::max\_line\_count |
| --- |

Denotes maximum line count of a video buffer that this endpoint can fill or process.

Similar constraints to [min\_line\_count](#a3ab95e55cd093f2414937a1916ef7f52), but [LINE\_COUNT\_HEIGHT](group__video__interface.md#ga59e44ec7c8132f479f1aa71e5b2c6546) indicates that the endpoint will never fill or process more than a full video frame in one video buffer.

## [◆ ](#a3ab95e55cd093f2414937a1916ef7f52)min\_line\_count

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) video\_caps::min\_line\_count |
| --- |

Denotes minimum line count of a video buffer that this endpoint can fill or process.

Each line is expected to consume the number of bytes the selected video format's pitch uses, so the video buffer must be at least pitch \* [min\_line\_count](#a3ab95e55cd093f2414937a1916ef7f52) bytes. [LINE\_COUNT\_HEIGHT](group__video__interface.md#ga59e44ec7c8132f479f1aa71e5b2c6546) is a special value, indicating the endpoint only supports video buffers with at least enough bytes to store a full video frame

## [◆ ](#a2b2604a36a2f7a5013d9383ab5ef198a)min\_vbuf\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) video\_caps::min\_vbuf\_count |
| --- |

minimal count of video buffers to enqueue before being able to start the stream.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_caps](structvideo__caps.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
