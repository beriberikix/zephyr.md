---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/video-controls_8h_source.html
original_path: doxygen/html/video-controls_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video-controls.h

[Go to the documentation of this file.](video-controls_8h.md)

1

6

7/\*

8 \* Copyright (c) 2019 Linaro Limited.

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_VIDEO\_CONTROLS\_H\_

13#define ZEPHYR\_INCLUDE\_VIDEO\_CONTROLS\_H\_

14

21

22#include <[zephyr/device.h](device_8h.md)>

23#include <stddef.h>

24#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 36](group__video__controls.md#ga21e3872f19c37495e733a8a60cf74b9d)#define VIDEO\_CTRL\_CLASS\_GENERIC 0x00000000

[ 37](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2)#define VIDEO\_CTRL\_CLASS\_CAMERA 0x00010000

[ 38](group__video__controls.md#ga05599b37f8d9cabd450c49561535ead7)#define VIDEO\_CTRL\_CLASS\_MPEG 0x00020000

[ 39](group__video__controls.md#gaeba7afc9a30cef1b8a95ca88b23ec057)#define VIDEO\_CTRL\_CLASS\_JPEG 0x00030000

[ 40](group__video__controls.md#ga9ec6cd7d3c5d82d5abefcf3a72e4c25b)#define VIDEO\_CTRL\_CLASS\_VENDOR 0xFFFF0000

44

[ 50](group__video__controls.md#ga59aa47b6f558ef5ae64a67f4a7ac7e31)#define VIDEO\_CID\_HFLIP (VIDEO\_CTRL\_CLASS\_GENERIC + 0)

[ 52](group__video__controls.md#ga16651a6825b619399a333ed39e802dfc)#define VIDEO\_CID\_VFLIP (VIDEO\_CTRL\_CLASS\_GENERIC + 1)

56

[ 61](group__video__controls.md#gae980f038dfff97ee5b159eeff3f141dc)#define VIDEO\_CID\_CAMERA\_EXPOSURE (VIDEO\_CTRL\_CLASS\_CAMERA + 0)

[ 62](group__video__controls.md#ga4581eedcb07f461f6f7a44a81eb3a2a3)#define VIDEO\_CID\_CAMERA\_GAIN (VIDEO\_CTRL\_CLASS\_CAMERA + 1)

[ 63](group__video__controls.md#gaad75298a3927f047b29a7505cb63abd1)#define VIDEO\_CID\_CAMERA\_ZOOM (VIDEO\_CTRL\_CLASS\_CAMERA + 2)

[ 64](group__video__controls.md#ga5d319ac87c6ab1b55942d3dba03633a2)#define VIDEO\_CID\_CAMERA\_BRIGHTNESS (VIDEO\_CTRL\_CLASS\_CAMERA + 3)

[ 65](group__video__controls.md#ga8224ea66f4752b6b4dd013deedb25b7c)#define VIDEO\_CID\_CAMERA\_SATURATION (VIDEO\_CTRL\_CLASS\_CAMERA + 4)

[ 66](group__video__controls.md#ga477ee6f02316a5fdb6d78b46e9c7cb3a)#define VIDEO\_CID\_CAMERA\_WHITE\_BAL (VIDEO\_CTRL\_CLASS\_CAMERA + 5)

[ 67](group__video__controls.md#gab5b1a60e991369f147b80c96859e84d1)#define VIDEO\_CID\_CAMERA\_CONTRAST (VIDEO\_CTRL\_CLASS\_CAMERA + 6)

[ 68](group__video__controls.md#ga768f96e23708c246876dbfd1ea53ff0e)#define VIDEO\_CID\_CAMERA\_COLORBAR (VIDEO\_CTRL\_CLASS\_CAMERA + 7)

[ 69](group__video__controls.md#ga374763bc215a167f539f48b89a732d03)#define VIDEO\_CID\_CAMERA\_QUALITY (VIDEO\_CTRL\_CLASS\_CAMERA + 8)

73

74#ifdef \_\_cplusplus

75}

76#endif

77

78/\* Controls \*/

79

80

84

85#endif /\* ZEPHYR\_INCLUDE\_VIDEO\_H\_ \*/

[device.h](device_8h.md)

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video-controls.h](video-controls_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
