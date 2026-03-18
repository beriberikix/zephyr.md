---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__video__controls.html
original_path: doxygen/html/group__video__controls.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Video Controls

[Device Driver APIs](group__io__interfaces.md)

Video controls.
[More...](#details)

| Control classes | |
| --- | --- |
| #define | [VIDEO\_CTRL\_CLASS\_GENERIC](#ga21e3872f19c37495e733a8a60cf74b9d)   0x00000000 |
|  | Generic class controls. |
| #define | [VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2)   0x00010000 |
|  | Camera class controls. |
| #define | [VIDEO\_CTRL\_CLASS\_MPEG](#ga05599b37f8d9cabd450c49561535ead7)   0x00020000 |
|  | MPEG-compression controls. |
| #define | [VIDEO\_CTRL\_CLASS\_JPEG](#gaeba7afc9a30cef1b8a95ca88b23ec057)   0x00030000 |
|  | JPEG-compression controls. |
| #define | [VIDEO\_CTRL\_CLASS\_VENDOR](#ga9ec6cd7d3c5d82d5abefcf3a72e4c25b)   0xFFFF0000 |
|  | Vendor-specific class controls. |

| Generic class control IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_HFLIP](#ga59aa47b6f558ef5ae64a67f4a7ac7e31)   ([VIDEO\_CTRL\_CLASS\_GENERIC](#ga21e3872f19c37495e733a8a60cf74b9d) + 0) |
|  | Mirror the picture horizontally. |
| #define | [VIDEO\_CID\_VFLIP](#ga16651a6825b619399a333ed39e802dfc)   ([VIDEO\_CTRL\_CLASS\_GENERIC](#ga21e3872f19c37495e733a8a60cf74b9d) + 1) |
|  | Mirror the picture vertically. |

| Camera class control IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_CAMERA\_EXPOSURE](#gae980f038dfff97ee5b159eeff3f141dc)   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 0) |
| #define | [VIDEO\_CID\_CAMERA\_GAIN](#ga4581eedcb07f461f6f7a44a81eb3a2a3)   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 1) |
| #define | [VIDEO\_CID\_CAMERA\_ZOOM](#gaad75298a3927f047b29a7505cb63abd1)   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 2) |
| #define | [VIDEO\_CID\_CAMERA\_BRIGHTNESS](#ga5d319ac87c6ab1b55942d3dba03633a2)   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 3) |
| #define | [VIDEO\_CID\_CAMERA\_SATURATION](#ga8224ea66f4752b6b4dd013deedb25b7c)   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 4) |
| #define | [VIDEO\_CID\_CAMERA\_WHITE\_BAL](#ga477ee6f02316a5fdb6d78b46e9c7cb3a)   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 5) |
| #define | [VIDEO\_CID\_CAMERA\_CONTRAST](#gab5b1a60e991369f147b80c96859e84d1)   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 6) |
| #define | [VIDEO\_CID\_CAMERA\_COLORBAR](#ga768f96e23708c246876dbfd1ea53ff0e)   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 7) |
| #define | [VIDEO\_CID\_CAMERA\_QUALITY](#ga374763bc215a167f539f48b89a732d03)   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 8) |

## Detailed Description

Video controls.

## Macro Definition Documentation

## [◆ ](#ga5d319ac87c6ab1b55942d3dba03633a2)VIDEO\_CID\_CAMERA\_BRIGHTNESS

| #define VIDEO\_CID\_CAMERA\_BRIGHTNESS   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 3) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga768f96e23708c246876dbfd1ea53ff0e)VIDEO\_CID\_CAMERA\_COLORBAR

| #define VIDEO\_CID\_CAMERA\_COLORBAR   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 7) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

## [◆ ](#gab5b1a60e991369f147b80c96859e84d1)VIDEO\_CID\_CAMERA\_CONTRAST

| #define VIDEO\_CID\_CAMERA\_CONTRAST   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 6) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

## [◆ ](#gae980f038dfff97ee5b159eeff3f141dc)VIDEO\_CID\_CAMERA\_EXPOSURE

| #define VIDEO\_CID\_CAMERA\_EXPOSURE   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 0) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga4581eedcb07f461f6f7a44a81eb3a2a3)VIDEO\_CID\_CAMERA\_GAIN

| #define VIDEO\_CID\_CAMERA\_GAIN   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 1) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga374763bc215a167f539f48b89a732d03)VIDEO\_CID\_CAMERA\_QUALITY

| #define VIDEO\_CID\_CAMERA\_QUALITY   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 8) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga8224ea66f4752b6b4dd013deedb25b7c)VIDEO\_CID\_CAMERA\_SATURATION

| #define VIDEO\_CID\_CAMERA\_SATURATION   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 4) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga477ee6f02316a5fdb6d78b46e9c7cb3a)VIDEO\_CID\_CAMERA\_WHITE\_BAL

| #define VIDEO\_CID\_CAMERA\_WHITE\_BAL   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 5) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

## [◆ ](#gaad75298a3927f047b29a7505cb63abd1)VIDEO\_CID\_CAMERA\_ZOOM

| #define VIDEO\_CID\_CAMERA\_ZOOM   ([VIDEO\_CTRL\_CLASS\_CAMERA](#gaf08fd11d488f66ac7e7a56c6caf2d6a2) + 2) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga59aa47b6f558ef5ae64a67f4a7ac7e31)VIDEO\_CID\_HFLIP

| #define VIDEO\_CID\_HFLIP   ([VIDEO\_CTRL\_CLASS\_GENERIC](#ga21e3872f19c37495e733a8a60cf74b9d) + 0) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

Mirror the picture horizontally.

## [◆ ](#ga16651a6825b619399a333ed39e802dfc)VIDEO\_CID\_VFLIP

| #define VIDEO\_CID\_VFLIP   ([VIDEO\_CTRL\_CLASS\_GENERIC](#ga21e3872f19c37495e733a8a60cf74b9d) + 1) |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

Mirror the picture vertically.

## [◆ ](#gaf08fd11d488f66ac7e7a56c6caf2d6a2)VIDEO\_CTRL\_CLASS\_CAMERA

| #define VIDEO\_CTRL\_CLASS\_CAMERA   0x00010000 |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

Camera class controls.

## [◆ ](#ga21e3872f19c37495e733a8a60cf74b9d)VIDEO\_CTRL\_CLASS\_GENERIC

| #define VIDEO\_CTRL\_CLASS\_GENERIC   0x00000000 |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

Generic class controls.

## [◆ ](#gaeba7afc9a30cef1b8a95ca88b23ec057)VIDEO\_CTRL\_CLASS\_JPEG

| #define VIDEO\_CTRL\_CLASS\_JPEG   0x00030000 |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

JPEG-compression controls.

## [◆ ](#ga05599b37f8d9cabd450c49561535ead7)VIDEO\_CTRL\_CLASS\_MPEG

| #define VIDEO\_CTRL\_CLASS\_MPEG   0x00020000 |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

MPEG-compression controls.

## [◆ ](#ga9ec6cd7d3c5d82d5abefcf3a72e4c25b)VIDEO\_CTRL\_CLASS\_VENDOR

| #define VIDEO\_CTRL\_CLASS\_VENDOR   0xFFFF0000 |
| --- |

`#include <[video-controls.h](video-controls_8h.md)>`

Vendor-specific class controls.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
