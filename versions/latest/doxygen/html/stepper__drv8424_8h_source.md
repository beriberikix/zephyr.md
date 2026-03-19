---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stepper__drv8424_8h_source.html
original_path: doxygen/html/stepper__drv8424_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper\_drv8424.h

[Go to the documentation of this file.](stepper__drv8424_8h.md)

1

7

8/\*

9 \* SPDX-FileCopyrightText: Copyright (c) 2024 Navimatix GmbH

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14#include <[stdint.h](stdint_8h.md)>

15#include <[zephyr/drivers/stepper.h](stepper_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 29](stepper__drv8424_8h.md#af25c14a3f91974bd689755989dc962d0)int [drv8424\_microstep\_recovery](stepper__drv8424_8h.md#af25c14a3f91974bd689755989dc962d0)(const struct [device](structdevice.md) \*dev);

30

31#ifdef \_\_cplusplus

32}

33#endif

[stdint.h](stdint_8h.md)

[stepper.h](stepper_8h.md)

Public API for Stepper Driver.

[drv8424\_microstep\_recovery](stepper__drv8424_8h.md#af25c14a3f91974bd689755989dc962d0)

int drv8424\_microstep\_recovery(const struct device \*dev)

After microstep setter fails, attempt to recover into previous state.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper](dir_975614d18b9dbb5293fe20c1ce7c38bb.md)
- [stepper\_drv8424.h](stepper__drv8424_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
