---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__usbd__uvc.html
original_path: doxygen/html/group__usbd__uvc.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB Video Class (UVC) device API

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

USB Video Class (UVC) device API.
[More...](#details)

| Functions | |
| --- | --- |
| void | [uvc\_set\_video\_dev](#gac4caf401c52d9a3755ace3e8dfa884a3) (const struct [device](structdevice.md) \*uvc\_dev, const struct [device](structdevice.md) \*video\_dev) |
|  | Set the video device that a UVC instance will use. |

## Detailed Description

USB Video Class (UVC) device API.

Since
:   4.2

Version
:   0.1.0

See also
:   uvc: "Universal Serial Bus Device Class Definition for Video Devices" Document Release 1.5 (August 9, 2012)

## Function Documentation

## [◆ ](#gac4caf401c52d9a3755ace3e8dfa884a3)uvc\_set\_video\_dev()

| void uvc\_set\_video\_dev | ( | const struct [device](structdevice.md) \* | *uvc\_dev*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *video\_dev* ) |

`#include <[zephyr/usb/class/usbd_uvc.h](usbd__uvc_8h.md)>`

Set the video device that a UVC instance will use.

It will query its supported controls, formats and frame rates, and use this information to generate USB descriptors sent to the host.

At runtime, it will forward all USB controls from the host to this device.

Note
:   This function must be called before [usbd\_enable](group__usbd__api.md#ga1a40fc13129e9218ca63ab3ca70d8d68 "usbd_enable").

Parameters
:   | uvc\_dev | The UVC device |
    | --- | --- |
    | video\_dev | The video device that this UVC instance controls |

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
