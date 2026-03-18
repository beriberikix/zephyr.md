---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/tmp116_8h_source.html
original_path: doxygen/html/tmp116_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmp116.h

[Go to the documentation of this file.](tmp116_8h.md)

1/\*

2 \* Copyright (c) 2021 Innoseis B.V

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMP116\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMP116\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

12

[ 13](tmp116_8h.md#a8729d146265e4f402928085f46c49d33)#define EEPROM\_TMP116\_SIZE (4 \* sizeof(uint16\_t))

14

[ 15](tmp116_8h.md#abfc6372f2d640f921b237fe14f18b73b)int [tmp116\_eeprom\_read](tmp116_8h.md#abfc6372f2d640f921b237fe14f18b73b)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data,

16 size\_t len);

17

[ 18](tmp116_8h.md#ab740cbdd946d5df162621f2309822810)int [tmp116\_eeprom\_write](tmp116_8h.md#ab740cbdd946d5df162621f2309822810)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

19 const void \*data, size\_t len);

20

21#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMP116\_H\_ \*/

[device.h](device_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[tmp116\_eeprom\_write](tmp116_8h.md#ab740cbdd946d5df162621f2309822810)

int tmp116\_eeprom\_write(const struct device \*dev, off\_t offset, const void \*data, size\_t len)

[tmp116\_eeprom\_read](tmp116_8h.md#abfc6372f2d640f921b237fe14f18b73b)

int tmp116\_eeprom\_read(const struct device \*dev, off\_t offset, void \*data, size\_t len)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tmp116.h](tmp116_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
