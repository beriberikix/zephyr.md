---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/input__touch_8h_source.html
original_path: doxygen/html/input__touch_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_touch.h

[Go to the documentation of this file.](input__touch_8h.md)

1/\*

2 \* Copyright (c) 2024 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_INPUT\_TOUCH\_H\_

7#define ZEPHYR\_INCLUDE\_INPUT\_TOUCH\_H\_

8

17

18#include <[zephyr/input/input.h](input_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 37](structinput__touchscreen__common__config.md)struct [input\_touchscreen\_common\_config](structinput__touchscreen__common__config.md) {

[ 38](structinput__touchscreen__common__config.md#a35b6d8ccd36aa95d46cc24be2f94144b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [screen\_width](structinput__touchscreen__common__config.md#a35b6d8ccd36aa95d46cc24be2f94144b);

[ 39](structinput__touchscreen__common__config.md#ae534425e6069853cb80a3925fce8e2ad) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [screen\_height](structinput__touchscreen__common__config.md#ae534425e6069853cb80a3925fce8e2ad);

[ 40](structinput__touchscreen__common__config.md#a147cc66f165b5bf9e42b591ad77824c5) bool [inverted\_x](structinput__touchscreen__common__config.md#a147cc66f165b5bf9e42b591ad77824c5);

[ 41](structinput__touchscreen__common__config.md#abba0c9353f867287b047635ea358e057) bool [inverted\_y](structinput__touchscreen__common__config.md#abba0c9353f867287b047635ea358e057);

[ 42](structinput__touchscreen__common__config.md#a408e21f2a9e57267d87d24f8a054f999) bool [swapped\_x\_y](structinput__touchscreen__common__config.md#a408e21f2a9e57267d87d24f8a054f999);

43};

44

[ 50](group__touch__events.md#gae19dc2c40a8e14d28db614dfd4c5e32b)#define INPUT\_TOUCH\_DT\_COMMON\_CONFIG\_INIT(node\_id) \

51 { \

52 .screen\_width = DT\_PROP(node\_id, screen\_width), \

53 .screen\_height = DT\_PROP(node\_id, screen\_height), \

54 .inverted\_x = DT\_PROP(node\_id, inverted\_x), \

55 .inverted\_y = DT\_PROP(node\_id, inverted\_y), \

56 .swapped\_x\_y = DT\_PROP(node\_id, swapped\_x\_y) \

57 }

58

[ 64](group__touch__events.md#ga354195b719d526cebd63a061e8dc408b)#define INPUT\_TOUCH\_DT\_INST\_COMMON\_CONFIG\_INIT(inst) \

65 INPUT\_TOUCH\_DT\_COMMON\_CONFIG\_INIT(DT\_DRV\_INST(inst))

66

[ 72](group__touch__events.md#ga0b82cc636a4b686ee2948dc704fd06f0)#define INPUT\_TOUCH\_STRUCT\_CHECK(config) \

73 BUILD\_ASSERT(offsetof(config, common) == 0, \

74 "struct input\_touchscreen\_common\_config must be placed first");

75

[ 84](group__touch__events.md#ga646bb86aa9f942fc3065381bd19e545c)void [input\_touchscreen\_report\_pos](group__touch__events.md#ga646bb86aa9f942fc3065381bd19e545c)(const struct [device](structdevice.md) \*dev,

85 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) y,

86 [k\_timeout\_t](structk__timeout__t.md) timeout);

87

88#ifdef \_\_cplusplus

89}

90#endif

91

93

94#endif /\* ZEPHYR\_INCLUDE\_INPUT\_TOUCH\_H\_ \*/

[input\_touchscreen\_report\_pos](group__touch__events.md#ga646bb86aa9f942fc3065381bd19e545c)

void input\_touchscreen\_report\_pos(const struct device \*dev, uint32\_t x, uint32\_t y, k\_timeout\_t timeout)

Common utility for reporting touchscreen position events.

[input.h](input_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[input\_touchscreen\_common\_config](structinput__touchscreen__common__config.md)

Common touchscreen config.

**Definition** input\_touch.h:37

[input\_touchscreen\_common\_config::inverted\_x](structinput__touchscreen__common__config.md#a147cc66f165b5bf9e42b591ad77824c5)

bool inverted\_x

**Definition** input\_touch.h:40

[input\_touchscreen\_common\_config::screen\_width](structinput__touchscreen__common__config.md#a35b6d8ccd36aa95d46cc24be2f94144b)

uint32\_t screen\_width

**Definition** input\_touch.h:38

[input\_touchscreen\_common\_config::swapped\_x\_y](structinput__touchscreen__common__config.md#a408e21f2a9e57267d87d24f8a054f999)

bool swapped\_x\_y

**Definition** input\_touch.h:42

[input\_touchscreen\_common\_config::inverted\_y](structinput__touchscreen__common__config.md#abba0c9353f867287b047635ea358e057)

bool inverted\_y

**Definition** input\_touch.h:41

[input\_touchscreen\_common\_config::screen\_height](structinput__touchscreen__common__config.md#ae534425e6069853cb80a3925fce8e2ad)

uint32\_t screen\_height

**Definition** input\_touch.h:39

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_touch.h](input__touch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
