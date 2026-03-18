---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ht16k33_8h_source.html
original_path: doxygen/html/ht16k33_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ht16k33.h

[Go to the documentation of this file.](ht16k33_8h.md)

1/\*

2 \* Copyright (c) 2019 Henrik Brix Andersen <henrik@brixandersen.dk>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LED\_HT16K33\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_LED\_HT16K33\_H\_

10

11#include <[zephyr/drivers/kscan.h](kscan_8h.md)>

12

[ 23](ht16k33_8h.md#a0d8df2d688f589651ce4231f301b98ae)int [ht16k33\_register\_keyscan\_callback](ht16k33_8h.md#a0d8df2d688f589651ce4231f301b98ae)(const struct [device](structdevice.md) \*parent,

24 const struct [device](structdevice.md) \*child,

25 [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback);

26

27#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LED\_HT16K33\_H\_ \*/

[kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480)

void(\* kscan\_callback\_t)(const struct device \*dev, uint32\_t row, uint32\_t column, bool pressed)

Keyboard scan callback called when user press/release a key on a matrix keyboard.

**Definition** kscan.h:44

[ht16k33\_register\_keyscan\_callback](ht16k33_8h.md#a0d8df2d688f589651ce4231f301b98ae)

int ht16k33\_register\_keyscan\_callback(const struct device \*parent, const struct device \*child, kscan\_callback\_t callback)

Register a HT16K33 keyscan device to be notified of relevant keyscan events by the keyscan interrupt ...

[kscan.h](kscan_8h.md)

Public API for Keyboard scan matrix devices.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led](dir_c34d419ad899f160d883f47e8e6b2aca.md)
- [ht16k33.h](ht16k33_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
