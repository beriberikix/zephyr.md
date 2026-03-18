---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/video-controls_8h.html
original_path: doxygen/html/video-controls_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video-controls.h File Reference

Public APIs for Video.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](video-controls_8h_source.md)

| Macros | |
| --- | --- |
| Control classes | |
| #define | [VIDEO\_CTRL\_CLASS\_GENERIC](group__video__controls.md#ga21e3872f19c37495e733a8a60cf74b9d)   0x00000000 |
|  | Generic class controls. |
| #define | [VIDEO\_CTRL\_CLASS\_CAMERA](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2)   0x00010000 |
|  | Camera class controls. |
| #define | [VIDEO\_CTRL\_CLASS\_MPEG](group__video__controls.md#ga05599b37f8d9cabd450c49561535ead7)   0x00020000 |
|  | MPEG-compression controls. |
| #define | [VIDEO\_CTRL\_CLASS\_JPEG](group__video__controls.md#gaeba7afc9a30cef1b8a95ca88b23ec057)   0x00030000 |
|  | JPEG-compression controls. |
| #define | [VIDEO\_CTRL\_CLASS\_VENDOR](group__video__controls.md#ga9ec6cd7d3c5d82d5abefcf3a72e4c25b)   0xFFFF0000 |
|  | Vendor-specific class controls. |
| Generic class control IDs | |
| #define | [VIDEO\_CID\_HFLIP](group__video__controls.md#ga59aa47b6f558ef5ae64a67f4a7ac7e31)   ([VIDEO\_CTRL\_CLASS\_GENERIC](group__video__controls.md#ga21e3872f19c37495e733a8a60cf74b9d) + 0) |
|  | Mirror the picture horizontally. |
| #define | [VIDEO\_CID\_VFLIP](group__video__controls.md#ga16651a6825b619399a333ed39e802dfc)   ([VIDEO\_CTRL\_CLASS\_GENERIC](group__video__controls.md#ga21e3872f19c37495e733a8a60cf74b9d) + 1) |
|  | Mirror the picture vertically. |
| Camera class control IDs | |
| #define | [VIDEO\_CID\_CAMERA\_EXPOSURE](group__video__controls.md#gae980f038dfff97ee5b159eeff3f141dc)   ([VIDEO\_CTRL\_CLASS\_CAMERA](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 0) |
| #define | [VIDEO\_CID\_CAMERA\_GAIN](group__video__controls.md#ga4581eedcb07f461f6f7a44a81eb3a2a3)   ([VIDEO\_CTRL\_CLASS\_CAMERA](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 1) |
| #define | [VIDEO\_CID\_CAMERA\_ZOOM](group__video__controls.md#gaad75298a3927f047b29a7505cb63abd1)   ([VIDEO\_CTRL\_CLASS\_CAMERA](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 2) |
| #define | [VIDEO\_CID\_CAMERA\_BRIGHTNESS](group__video__controls.md#ga5d319ac87c6ab1b55942d3dba03633a2)   ([VIDEO\_CTRL\_CLASS\_CAMERA](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 3) |
| #define | [VIDEO\_CID\_CAMERA\_SATURATION](group__video__controls.md#ga8224ea66f4752b6b4dd013deedb25b7c)   ([VIDEO\_CTRL\_CLASS\_CAMERA](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 4) |
| #define | [VIDEO\_CID\_CAMERA\_WHITE\_BAL](group__video__controls.md#ga477ee6f02316a5fdb6d78b46e9c7cb3a)   ([VIDEO\_CTRL\_CLASS\_CAMERA](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 5) |
| #define | [VIDEO\_CID\_CAMERA\_CONTRAST](group__video__controls.md#gab5b1a60e991369f147b80c96859e84d1)   ([VIDEO\_CTRL\_CLASS\_CAMERA](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 6) |
| #define | [VIDEO\_CID\_CAMERA\_COLORBAR](group__video__controls.md#ga768f96e23708c246876dbfd1ea53ff0e)   ([VIDEO\_CTRL\_CLASS\_CAMERA](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 7) |
| #define | [VIDEO\_CID\_CAMERA\_QUALITY](group__video__controls.md#ga374763bc215a167f539f48b89a732d03)   ([VIDEO\_CTRL\_CLASS\_CAMERA](group__video__controls.md#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 8) |

## Detailed Description

Public APIs for Video.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video-controls.h](video-controls_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
