---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gpio__emul_8h_source.html
original_path: doxygen/html/gpio__emul_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_emul.h

[Go to the documentation of this file.](gpio__emul_8h.md)

1/\*

2 \* Copyright (c) 2020 Friedt Professional Engineering Services, Inc

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_EMUL\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_EMUL\_H\_

14

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

45

[ 56](group__gpio__emul.md#gaa7eae6a0f85d0f0fb6a8aa41329f4709)int [gpio\_emul\_input\_set\_masked](group__gpio__emul.md#gaa7eae6a0f85d0f0fb6a8aa41329f4709)(const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins,

57 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) values);

58

[ 69](group__gpio__emul.md#ga3962e337bc22e532f2c181724621fcf8)static inline int [gpio\_emul\_input\_set](group__gpio__emul.md#ga3962e337bc22e532f2c181724621fcf8)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin,

70 int value)

71{

72 return [gpio\_emul\_input\_set\_masked](group__gpio__emul.md#gaa7eae6a0f85d0f0fb6a8aa41329f4709)(port, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin), value ? [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin) : 0);

73}

74

[ 85](group__gpio__emul.md#gaa6e4c5c2c53d421e9635c0a977172205)int [gpio\_emul\_output\_get\_masked](group__gpio__emul.md#gaa6e4c5c2c53d421e9635c0a977172205)(const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins,

86 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*values);

87

[ 97](group__gpio__emul.md#gaa62613aa6eb442d2c4e436893316124f)static inline int [gpio\_emul\_output\_get](group__gpio__emul.md#gaa62613aa6eb442d2c4e436893316124f)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin)

98{

99 int ret;

100 [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) values;

101

102 ret = [gpio\_emul\_output\_get\_masked](group__gpio__emul.md#gaa6e4c5c2c53d421e9635c0a977172205)(port, [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin), &values);

103 if (ret == 0) {

104 ret = (values & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(pin)) ? 1 : 0;

105 }

106

107 return ret;

108}

109

[ 122](group__gpio__emul.md#ga86bd5ff4f557e4d520a4f760fb74cdd5)int [gpio\_emul\_flags\_get](group__gpio__emul.md#ga86bd5ff4f557e4d520a4f760fb74cdd5)(const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

123

127

128#ifdef \_\_cplusplus

129}

130#endif

131

132#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_EMUL\_H\_ \*/

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[gpio\_emul\_input\_set](group__gpio__emul.md#ga3962e337bc22e532f2c181724621fcf8)

static int gpio\_emul\_input\_set(const struct device \*port, gpio\_pin\_t pin, int value)

Modify the value of one emulated GPIO input pin.

**Definition** gpio\_emul.h:69

[gpio\_emul\_flags\_get](group__gpio__emul.md#ga86bd5ff4f557e4d520a4f760fb74cdd5)

int gpio\_emul\_flags\_get(const struct device \*port, gpio\_pin\_t pin, gpio\_flags\_t \*flags)

Get flags for a given emulated GPIO pin.

[gpio\_emul\_output\_get](group__gpio__emul.md#gaa62613aa6eb442d2c4e436893316124f)

static int gpio\_emul\_output\_get(const struct device \*port, gpio\_pin\_t pin)

Read the value of one emulated GPIO output pin.

**Definition** gpio\_emul.h:97

[gpio\_emul\_output\_get\_masked](group__gpio__emul.md#gaa6e4c5c2c53d421e9635c0a977172205)

int gpio\_emul\_output\_get\_masked(const struct device \*port, gpio\_port\_pins\_t pins, gpio\_port\_value\_t \*values)

Read the value of one or more emulated GPIO output pins.

[gpio\_emul\_input\_set\_masked](group__gpio__emul.md#gaa7eae6a0f85d0f0fb6a8aa41329f4709)

int gpio\_emul\_input\_set\_masked(const struct device \*port, gpio\_port\_pins\_t pins, gpio\_port\_value\_t values)

Modify the values of one or more emulated GPIO input pins.

[gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)

uint8\_t gpio\_pin\_t

Provides a type to hold a GPIO pin index.

**Definition** gpio.h:254

[gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e)

uint32\_t gpio\_flags\_t

Provides a type to hold GPIO configuration flags.

**Definition** gpio.h:274

[gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)

uint32\_t gpio\_port\_pins\_t

Identifies a set of pins associated with a port.

**Definition** gpio.h:233

[gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693)

uint32\_t gpio\_port\_value\_t

Provides values for a set of pins associated with a port.

**Definition** gpio.h:246

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_emul.h](gpio__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
