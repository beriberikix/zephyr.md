---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structvideo__frmival.html
original_path: doxygen/html/structvideo__frmival.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_frmival Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

Video frame interval structure.
[More...](#details)

`#include <[video.h](video_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [numerator](#a57ee282f01da0f1ef1db2558d777631c) |
|  | numerator of the frame interval |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [denominator](#aba4a6700ea733c3b07ee6445856c580a) |
|  | denominator of the frame interval |

## Detailed Description

Video frame interval structure.

Used to describe a video frame interval.

## Field Documentation

## [◆ ](#aba4a6700ea733c3b07ee6445856c580a)denominator

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_frmival::denominator |
| --- |

denominator of the frame interval

## [◆ ](#a57ee282f01da0f1ef1db2558d777631c)numerator

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) video\_frmival::numerator |
| --- |

numerator of the frame interval

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_frmival](structvideo__frmival.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
