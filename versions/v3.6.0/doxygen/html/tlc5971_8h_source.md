---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/tlc5971_8h_source.html
original_path: doxygen/html/tlc5971_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tlc5971.h

[Go to the documentation of this file.](tlc5971_8h.md)

1/\*

2 \* Copyright (c) 2022 Esco Medical ApS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LED\_STRIP\_TLC5971\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_LED\_STRIP\_TLC5971\_H\_

9

[ 13](tlc5971_8h.md#aee75c4832a72869ca6e2960c726ed707)#define TLC5971\_GLOBAL\_BRIGHTNESS\_CONTROL\_MAX 127

14

[ 25](tlc5971_8h.md#acc0ab1f6ae658de98d043e49291abea4)int [tlc5971\_set\_global\_brightness](tlc5971_8h.md#acc0ab1f6ae658de98d043e49291abea4)(const struct [device](structdevice.md) \*dev, struct [led\_rgb](structled__rgb.md) pixel);

26

27#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LED\_STRIP\_TLC5971\_H\_ \*/

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[led\_rgb](structled__rgb.md)

Color value for a single RGB LED.

**Definition** led\_strip.h:38

[tlc5971\_set\_global\_brightness](tlc5971_8h.md#acc0ab1f6ae658de98d043e49291abea4)

int tlc5971\_set\_global\_brightness(const struct device \*dev, struct led\_rgb pixel)

Set the global brightness control levels for the tlc5971 strip.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led\_strip](dir_ffa26527181ee514263f5645af64c462.md)
- [tlc5971.h](tlc5971_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
