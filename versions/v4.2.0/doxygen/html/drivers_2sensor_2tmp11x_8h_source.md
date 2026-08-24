---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2sensor_2tmp11x_8h_source.html
original_path: doxygen/html/drivers_2sensor_2tmp11x_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmp11x.h

[Go to the documentation of this file.](drivers_2sensor_2tmp11x_8h.md)

1/\*

2 \* Copyright (c) 2021 Innoseis B.V

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMP11X\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMP11X\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

12#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

13

[ 14](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9)enum [sensor\_attribute\_tmp\_11x](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9) {

[ 16](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9aeb6e8af036fe3a8081504b62f30fb591) [SENSOR\_ATTR\_TMP11X\_ONE\_SHOT\_MODE](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9aeb6e8af036fe3a8081504b62f30fb591) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 18](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9a423099eda7d8c3cd7e3712bf9b4ce024) [SENSOR\_ATTR\_TMP11X\_SHUTDOWN\_MODE](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9a423099eda7d8c3cd7e3712bf9b4ce024),

[ 20](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9a001d3256c1daf5275e414bd5a01bd8cb) [SENSOR\_ATTR\_TMP11X\_CONTINUOUS\_CONVERSION\_MODE](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9a001d3256c1daf5275e414bd5a01bd8cb),

21};

22

[ 23](drivers_2sensor_2tmp11x_8h.md#abb06ab7fe6ab207f5b9d77521bef218f)#define EEPROM\_TMP11X\_SIZE (4 \* sizeof(uint16\_t))

24

[ 25](drivers_2sensor_2tmp11x_8h.md#ae08f7c30e516b4b8f36a6ad1883830cf)int [tmp11x\_eeprom\_read](drivers_2sensor_2tmp11x_8h.md#ae08f7c30e516b4b8f36a6ad1883830cf)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data,

26 size\_t len);

27

[ 28](drivers_2sensor_2tmp11x_8h.md#abc253a269051ae0aeec8061a050922c9)int [tmp11x\_eeprom\_write](drivers_2sensor_2tmp11x_8h.md#abc253a269051ae0aeec8061a050922c9)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

29 const void \*data, size\_t len);

30

31#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMP11X\_H\_ \*/

[device.h](device_8h.md)

[sensor\_attribute\_tmp\_11x](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9)

sensor\_attribute\_tmp\_11x

**Definition** tmp11x.h:14

[SENSOR\_ATTR\_TMP11X\_CONTINUOUS\_CONVERSION\_MODE](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9a001d3256c1daf5275e414bd5a01bd8cb)

@ SENSOR\_ATTR\_TMP11X\_CONTINUOUS\_CONVERSION\_MODE

Turn on continuous conversion.

**Definition** tmp11x.h:20

[SENSOR\_ATTR\_TMP11X\_SHUTDOWN\_MODE](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9a423099eda7d8c3cd7e3712bf9b4ce024)

@ SENSOR\_ATTR\_TMP11X\_SHUTDOWN\_MODE

Shutdown the sensor.

**Definition** tmp11x.h:18

[SENSOR\_ATTR\_TMP11X\_ONE\_SHOT\_MODE](drivers_2sensor_2tmp11x_8h.md#a30cbd49ad5c7286d23453ce6f1167ee9aeb6e8af036fe3a8081504b62f30fb591)

@ SENSOR\_ATTR\_TMP11X\_ONE\_SHOT\_MODE

Turn on power saving/one shot mode.

**Definition** tmp11x.h:16

[tmp11x\_eeprom\_write](drivers_2sensor_2tmp11x_8h.md#abc253a269051ae0aeec8061a050922c9)

int tmp11x\_eeprom\_write(const struct device \*dev, off\_t offset, const void \*data, size\_t len)

[tmp11x\_eeprom\_read](drivers_2sensor_2tmp11x_8h.md#ae08f7c30e516b4b8f36a6ad1883830cf)

int tmp11x\_eeprom\_read(const struct device \*dev, off\_t offset, void \*data, size\_t len)

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:372

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tmp11x.h](drivers_2sensor_2tmp11x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
