---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stepper__drv84xx_8h_source.html
original_path: doxygen/html/stepper__drv84xx_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper\_drv84xx.h

[Go to the documentation of this file.](stepper__drv84xx_8h.md)

1

7

8/\*

9 \* SPDX-FileCopyrightText: Copyright (c) 2024 Navimatix GmbH

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_DRV84XX\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_DRV84XX\_H\_

16

17#include <[stdint.h](stdint_8h.md)>

18#include <[zephyr/drivers/stepper.h](stepper_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 32](stepper__drv84xx_8h.md#aee40af14c8f26a7df237e9be0597942e)int [drv84xx\_microstep\_recovery](stepper__drv84xx_8h.md#aee40af14c8f26a7df237e9be0597942e)(const struct [device](structdevice.md) \*dev);

33

34#ifdef \_\_cplusplus

35}

36#endif

37

38#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_DRV84XX\_H\_ \*/

[stdint.h](stdint_8h.md)

[stepper.h](stepper_8h.md)

Public API for Stepper Driver.

[drv84xx\_microstep\_recovery](stepper__drv84xx_8h.md#aee40af14c8f26a7df237e9be0597942e)

int drv84xx\_microstep\_recovery(const struct device \*dev)

After microstep setter fails, attempt to recover into previous state.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper](dir_975614d18b9dbb5293fe20c1ce7c38bb.md)
- [stepper\_drv84xx.h](stepper__drv84xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
