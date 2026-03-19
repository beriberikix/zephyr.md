---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/flash__simulator_8h_source.html
original_path: doxygen/html/flash__simulator_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_simulator.h

[Go to the documentation of this file.](flash__simulator_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef \_\_ZEPHYR\_INCLUDE\_DRIVERS\_\_FLASH\_SIMULATOR\_H\_\_

7#define \_\_ZEPHYR\_INCLUDE\_DRIVERS\_\_FLASH\_SIMULATOR\_H\_\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

19

[ 31](flash__simulator_8h.md#a71cca7b794f8e9402d81491c7e93cc3f)\_\_syscall void \*[flash\_simulator\_get\_memory](flash__simulator_8h.md#a71cca7b794f8e9402d81491c7e93cc3f)(const struct [device](structdevice.md) \*dev,

32 size\_t \*mock\_size);

33#ifdef \_\_cplusplus

34}

35#endif

36

37#include <zephyr/syscalls/flash\_simulator.h>

38

39#endif /\* \_\_ZEPHYR\_INCLUDE\_DRIVERS\_\_FLASH\_SIMULATOR\_H\_\_ \*/

[flash\_simulator\_get\_memory](flash__simulator_8h.md#a71cca7b794f8e9402d81491c7e93cc3f)

void \* flash\_simulator\_get\_memory(const struct device \*dev, size\_t \*mock\_size)

Obtain a pointer to the RAM buffer used but by the simulator.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash](dir_b5b0d43e6264d65db716db62f9858e50.md)
- [flash\_simulator.h](flash__simulator_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
