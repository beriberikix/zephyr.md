---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/video-controls_8h_source.html
original_path: doxygen/html/video-controls_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

24#include <[zephyr/kernel.h](kernel_8h.md)>

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

[ 54](group__video__controls.md#ga762a6c2b0fb032b9ebdfeff5ed15c3de)#define VIDEO\_CID\_POWER\_LINE\_FREQUENCY (VIDEO\_CTRL\_CLASS\_GENERIC + 2)

[ 56](group__video__controls.md#ga6f6eaed7defdbb5f440874c7c6d0a6eb)#define VIDEO\_CID\_PIXEL\_RATE (VIDEO\_CTRL\_CLASS\_GENERIC + 3)

57

[ 58](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a)enum [video\_power\_line\_frequency](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a) {

[ 59](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93) = 0,

[ 60](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10) = 1,

[ 61](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796) = 2,

[ 62](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0) = 3,

63};

64

68

[ 73](group__video__controls.md#gae980f038dfff97ee5b159eeff3f141dc)#define VIDEO\_CID\_CAMERA\_EXPOSURE (VIDEO\_CTRL\_CLASS\_CAMERA + 0)

[ 74](group__video__controls.md#ga4581eedcb07f461f6f7a44a81eb3a2a3)#define VIDEO\_CID\_CAMERA\_GAIN (VIDEO\_CTRL\_CLASS\_CAMERA + 1)

[ 75](group__video__controls.md#gaad75298a3927f047b29a7505cb63abd1)#define VIDEO\_CID\_CAMERA\_ZOOM (VIDEO\_CTRL\_CLASS\_CAMERA + 2)

[ 76](group__video__controls.md#ga5d319ac87c6ab1b55942d3dba03633a2)#define VIDEO\_CID\_CAMERA\_BRIGHTNESS (VIDEO\_CTRL\_CLASS\_CAMERA + 3)

[ 77](group__video__controls.md#ga8224ea66f4752b6b4dd013deedb25b7c)#define VIDEO\_CID\_CAMERA\_SATURATION (VIDEO\_CTRL\_CLASS\_CAMERA + 4)

[ 78](group__video__controls.md#ga477ee6f02316a5fdb6d78b46e9c7cb3a)#define VIDEO\_CID\_CAMERA\_WHITE\_BAL (VIDEO\_CTRL\_CLASS\_CAMERA + 5)

[ 79](group__video__controls.md#gab5b1a60e991369f147b80c96859e84d1)#define VIDEO\_CID\_CAMERA\_CONTRAST (VIDEO\_CTRL\_CLASS\_CAMERA + 6)

[ 80](group__video__controls.md#ga982ebf66843d84a39e1697642d2289be)#define VIDEO\_CID\_CAMERA\_TEST\_PATTERN (VIDEO\_CTRL\_CLASS\_CAMERA + 7)

[ 81](group__video__controls.md#ga374763bc215a167f539f48b89a732d03)#define VIDEO\_CID\_CAMERA\_QUALITY (VIDEO\_CTRL\_CLASS\_CAMERA + 8)

[ 82](group__video__controls.md#ga41d092d9852933708e033273db4b72c2)#define VIDEO\_CID\_CAMERA\_HUE (VIDEO\_CTRL\_CLASS\_CAMERA + 9)

86

87#ifdef \_\_cplusplus

88}

89#endif

90

91/\* Controls \*/

92

96

97#endif /\* ZEPHYR\_INCLUDE\_VIDEO\_H\_ \*/

[device.h](device_8h.md)

[video\_power\_line\_frequency](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a)

video\_power\_line\_frequency

**Definition** video-controls.h:58

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED

**Definition** video-controls.h:59

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO

**Definition** video-controls.h:62

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ

**Definition** video-controls.h:61

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ

**Definition** video-controls.h:60

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video-controls.h](video-controls_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
