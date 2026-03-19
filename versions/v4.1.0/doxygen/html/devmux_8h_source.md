---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/devmux_8h_source.html
original_path: doxygen/html/devmux_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

devmux.h

[Go to the documentation of this file.](devmux_8h.md)

1/\*

2 \* Copyright (c) 2023, Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef INCLUDE\_ZEPHYR\_DRIVERS\_MISC\_DEVMUX\_H\_

13#define INCLUDE\_ZEPHYR\_DRIVERS\_MISC\_DEVMUX\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16

17#include <[zephyr/device.h](device_8h.md)>

18#include <[zephyr/kernel.h](kernel_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

55

[ 65](group__demux__interface.md#gafd3635aa5bd36c41832a4eb31cd122ca)\_\_syscall int [devmux\_select\_get](group__demux__interface.md#gafd3635aa5bd36c41832a4eb31cd122ca)(const struct [device](structdevice.md) \*dev);

66

[ 78](group__demux__interface.md#ga895dad09fcd98c8731f9ae784b018e0a)\_\_syscall int [devmux\_select\_set](group__demux__interface.md#ga895dad09fcd98c8731f9ae784b018e0a)(struct [device](structdevice.md) \*dev, size\_t index);

79

83

84#ifdef \_\_cplusplus

85}

86#endif

87

88#include <zephyr/syscalls/devmux.h>

89

90#endif /\* INCLUDE\_ZEPHYR\_DRIVERS\_MISC\_DEVMUX\_H\_ \*/

[device.h](device_8h.md)

[devmux\_select\_set](group__demux__interface.md#ga895dad09fcd98c8731f9ae784b018e0a)

int devmux\_select\_set(struct device \*dev, size\_t index)

Set the selection of a devmux device.

[devmux\_select\_get](group__demux__interface.md#gafd3635aa5bd36c41832a4eb31cd122ca)

int devmux\_select\_get(const struct device \*dev)

Get the current selection of a devmux device.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [devmux](dir_f5d1e1250050ed799930adfc7b07539c.md)
- [devmux.h](devmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
