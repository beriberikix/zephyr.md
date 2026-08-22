---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/uart__bridge_8h_source.html
original_path: doxygen/html/uart__bridge_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_bridge.h

[Go to the documentation of this file.](uart__bridge_8h.md)

1/\*

2 \* Copyright 2025 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/device.h](device_8h.md)>

8

[ 18](uart__bridge_8h.md#a05e43f34092fbbe84c868e6ec8966313)void [uart\_bridge\_settings\_update](uart__bridge_8h.md#a05e43f34092fbbe84c868e6ec8966313)(const struct [device](structdevice.md) \*dev,

19 const struct [device](structdevice.md) \*bridge\_dev);

[device.h](device_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[uart\_bridge\_settings\_update](uart__bridge_8h.md#a05e43f34092fbbe84c868e6ec8966313)

void uart\_bridge\_settings\_update(const struct device \*dev, const struct device \*bridge\_dev)

Update the hardware port settings on a uart bridge.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart](dir_eceb547fc512cd90b0f2ab20ab1dbc9a.md)
- [uart\_bridge.h](uart__bridge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
