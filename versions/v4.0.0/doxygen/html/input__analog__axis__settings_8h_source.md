---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/input__analog__axis__settings_8h_source.html
original_path: doxygen/html/input__analog__axis__settings_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_analog\_axis\_settings.h

[Go to the documentation of this file.](input__analog__axis__settings_8h.md)

1/\*

2 \* Copyright 2023 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_INPUT\_ANALOG\_AXIS\_SETTINGS\_H\_

8#define ZEPHYR\_INCLUDE\_INPUT\_ANALOG\_AXIS\_SETTINGS\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[zephyr/device.h](device_8h.md)>

12

17

[ 29](group__input__analog__axis.md#ga56973ef7c7a465defdb7bd2934c86778)int [analog\_axis\_calibration\_save](group__input__analog__axis.md#ga56973ef7c7a465defdb7bd2934c86778)(const struct [device](structdevice.md) \*dev);

30

32

33#endif /\* ZEPHYR\_INCLUDE\_INPUT\_ANALOG\_AXIS\_SETTINGS\_H\_ \*/

[device.h](device_8h.md)

[analog\_axis\_calibration\_save](group__input__analog__axis.md#ga56973ef7c7a465defdb7bd2934c86778)

int analog\_axis\_calibration\_save(const struct device \*dev)

Save the calibration data.

[stdint.h](stdint_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_analog\_axis\_settings.h](input__analog__axis__settings_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
