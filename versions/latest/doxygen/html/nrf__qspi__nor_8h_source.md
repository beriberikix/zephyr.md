---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nrf__qspi__nor_8h_source.html
original_path: doxygen/html/nrf__qspi__nor_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_qspi\_nor.h

[Go to the documentation of this file.](nrf__qspi__nor_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_NRF\_QSPI\_NOR\_H\_\_

8#define \_\_ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_NRF\_QSPI\_NOR\_H\_\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 32](nrf__qspi__nor_8h.md#abfe75f149d6a54c7fefe9d3a2ed21ea3)\_\_syscall void [nrf\_qspi\_nor\_xip\_enable](nrf__qspi__nor_8h.md#abfe75f149d6a54c7fefe9d3a2ed21ea3)(const struct [device](structdevice.md) \*dev, bool enable);

33

34#ifdef \_\_cplusplus

35}

36#endif

37

38#include <syscalls/nrf\_qspi\_nor.h>

39

40#endif /\* \_\_ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_NRF\_QSPI\_NOR\_H\_\_ \*/

[nrf\_qspi\_nor\_xip\_enable](nrf__qspi__nor_8h.md#abfe75f149d6a54c7fefe9d3a2ed21ea3)

void nrf\_qspi\_nor\_xip\_enable(const struct device \*dev, bool enable)

Specifies whether XIP (execute in place) operation should be possible.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash](dir_b5b0d43e6264d65db716db62f9858e50.md)
- [nrf\_qspi\_nor.h](nrf__qspi__nor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
