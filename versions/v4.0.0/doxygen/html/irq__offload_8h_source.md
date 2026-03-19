---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/irq__offload_8h_source.html
original_path: doxygen/html/irq__offload_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq\_offload.h

[Go to the documentation of this file.](irq__offload_8h.md)

1/\*

2 \* Copyright (c) 2015 Intel corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11#ifndef ZEPHYR\_INCLUDE\_IRQ\_OFFLOAD\_H\_

12#define ZEPHYR\_INCLUDE\_IRQ\_OFFLOAD\_H\_

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 18](irq__offload_8h.md#a5bcf9956ddbf5ea75619f0cef91e1214)typedef void (\*[irq\_offload\_routine\_t](irq__offload_8h.md#a5bcf9956ddbf5ea75619f0cef91e1214))(const void \*parameter);

19

[ 39](irq__offload_8h.md#a429859dd7ac3d88a4b7ae858835847ce)void [irq\_offload](irq__offload_8h.md#a429859dd7ac3d88a4b7ae858835847ce)([irq\_offload\_routine\_t](irq__offload_8h.md#a5bcf9956ddbf5ea75619f0cef91e1214) routine, const void \*parameter);

40

41#ifdef \_\_cplusplus

42}

43#endif

44

45#endif /\* \_SW\_IRQ\_H\_ \*/

[irq\_offload](irq__offload_8h.md#a429859dd7ac3d88a4b7ae858835847ce)

void irq\_offload(irq\_offload\_routine\_t routine, const void \*parameter)

Run a function in interrupt context.

[irq\_offload\_routine\_t](irq__offload_8h.md#a5bcf9956ddbf5ea75619f0cef91e1214)

void(\* irq\_offload\_routine\_t)(const void \*parameter)

**Definition** irq\_offload.h:18

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq\_offload.h](irq__offload_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
