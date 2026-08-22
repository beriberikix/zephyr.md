---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mfd__maxq10xx_8h_source.html
original_path: doxygen/html/mfd__maxq10xx_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mfd\_maxq10xx.h

[Go to the documentation of this file.](mfd__maxq10xx_8h.md)

1/\*

2 \* Copyright (c) 2025 Vogl Electronic GmbH

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_MAXQ10XX\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_MAXQ10XX\_H\_

8

9#include <[zephyr/device.h](device_8h.md)>

10#include <[zephyr/kernel.h](kernel_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 24](mfd__maxq10xx_8h.md#afab2fb34feb7d84e42caea6021dd1ed9)struct [k\_sem](structk__sem.md) \*[mfd\_maxq10xx\_get\_lock](mfd__maxq10xx_8h.md#afab2fb34feb7d84e42caea6021dd1ed9)(const struct [device](structdevice.md) \*dev);

25

26

27#ifdef \_\_cplusplus

28}

29#endif

30

31#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_MAXQ10XX\_H\_ \*/

[device.h](device_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[mfd\_maxq10xx\_get\_lock](mfd__maxq10xx_8h.md#afab2fb34feb7d84e42caea6021dd1ed9)

struct k\_sem \* mfd\_maxq10xx\_get\_lock(const struct device \*dev)

Get the semaphore reference for a MAXQ1xx instance.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[k\_sem](structk__sem.md)

Semaphore structure.

**Definition** kernel.h:3275

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [mfd\_maxq10xx.h](mfd__maxq10xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
