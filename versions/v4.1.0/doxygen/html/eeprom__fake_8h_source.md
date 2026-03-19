---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/eeprom__fake_8h_source.html
original_path: doxygen/html/eeprom__fake_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eeprom\_fake.h

[Go to the documentation of this file.](eeprom__fake_8h.md)

1/\*

2 \* Copyright (c) 2022 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_EEPROM\_FAKE\_EEPROM\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_EEPROM\_FAKE\_EEPROM\_H\_

9

10#include <[zephyr/drivers/eeprom.h](eeprom_8h.md)>

11#include <[zephyr/fff.h](fff_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 17](eeprom__fake_8h.md#a1cb054262963a6627153371a2acfe402)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_eeprom\_read, const struct [device](structdevice.md) \*, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f), void \*, size\_t);

18

[ 19](eeprom__fake_8h.md#aed5eb663ecbf3ca11fd70257c9e36613)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_eeprom\_write, const struct [device](structdevice.md) \*, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f), const void \*, size\_t);

20

[ 21](eeprom__fake_8h.md#ac45f5d2518a923c2c95f490f73b997cc)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(size\_t, fake\_eeprom\_size, const struct [device](structdevice.md) \*);

22

[ 23](eeprom__fake_8h.md#a800769bebaa15f0430dd66078ea0c413)size\_t [fake\_eeprom\_size\_delegate](eeprom__fake_8h.md#a800769bebaa15f0430dd66078ea0c413)(const struct [device](structdevice.md) \*dev);

24

25#ifdef \_\_cplusplus

26}

27#endif

28

29#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_EEPROM\_FAKE\_EEPROM\_H\_ \*/

[eeprom.h](eeprom_8h.md)

Public API for EEPROM drivers.

[fake\_eeprom\_size\_delegate](eeprom__fake_8h.md#a800769bebaa15f0430dd66078ea0c413)

size\_t fake\_eeprom\_size\_delegate(const struct device \*dev)

[fff.h](fff_8h.md)

[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)

#define DECLARE\_FAKE\_VALUE\_FUNC(...)

**Definition** fff.h:8684

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [eeprom](dir_af342b5e759e5b1b2dac755f05d42ced.md)
- [eeprom\_fake.h](eeprom__fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
