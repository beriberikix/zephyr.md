---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/usbd__uvc_8h_source.html
original_path: doxygen/html/usbd__uvc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_uvc.h

[Go to the documentation of this file.](usbd__uvc_8h.md)

1/\*

2 \* Copyright (c) 2025 tinyVision.ai Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_UVC\_H

13#define ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_UVC\_H

14

15#include <[zephyr/device.h](device_8h.md)>

16

27

[ 41](group__usbd__uvc.md#gac4caf401c52d9a3755ace3e8dfa884a3)void [uvc\_set\_video\_dev](group__usbd__uvc.md#gac4caf401c52d9a3755ace3e8dfa884a3)(const struct [device](structdevice.md) \*uvc\_dev, const struct [device](structdevice.md) \*video\_dev);

42

46

47#endif /\* ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_UVC\_H \*/

[device.h](device_8h.md)

[uvc\_set\_video\_dev](group__usbd__uvc.md#gac4caf401c52d9a3755ace3e8dfa884a3)

void uvc\_set\_video\_dev(const struct device \*uvc\_dev, const struct device \*video\_dev)

Set the video device that a UVC instance will use.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_uvc.h](usbd__uvc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
