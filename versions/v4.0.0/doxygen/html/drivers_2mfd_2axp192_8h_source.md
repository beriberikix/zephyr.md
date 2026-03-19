---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2mfd_2axp192_8h_source.html
original_path: doxygen/html/drivers_2mfd_2axp192_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

axp192.h

[Go to the documentation of this file.](drivers_2mfd_2axp192_8h.md)

1/\*

2 \* Copyright (c) 2023 Martin Kiepfer

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AXP192\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AXP192\_H\_

9

10#include <stddef.h>

11#include <[stdint.h](stdint_8h.md)>

12

13#include <[zephyr/device.h](device_8h.md)>

14#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

[ 23](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249)enum [axp192\_gpio\_func](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249) {

[ 24](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ab8eee3f4b6ce22594b90d7e49e4927df) [AXP192\_GPIO\_FUNC\_INPUT](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ab8eee3f4b6ce22594b90d7e49e4927df) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 25](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249af1c2244571c0a3b12c0ae94c583c1a4b) [AXP192\_GPIO\_FUNC\_OUTPUT\_OD](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249af1c2244571c0a3b12c0ae94c583c1a4b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 26](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a8d006f1e4284057f5b952b236729c5f5) [AXP192\_GPIO\_FUNC\_OUTPUT\_LOW](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a8d006f1e4284057f5b952b236729c5f5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 27](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ae9f961ad84c38f3315e3cdb25ede9328) [AXP192\_GPIO\_FUNC\_LDO](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ae9f961ad84c38f3315e3cdb25ede9328) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 28](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ab3a2622cccb9ec1cdf22ddd5ac75ae6a) [AXP192\_GPIO\_FUNC\_ADC](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ab3a2622cccb9ec1cdf22ddd5ac75ae6a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 29](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a2634f857f19e03ab8337780025c25579) [AXP192\_GPIO\_FUNC\_PWM](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a2634f857f19e03ab8337780025c25579) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 30](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a69c1f986672389305a3000b83a12417f) [AXP192\_GPIO\_FUNC\_FLOAT](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a69c1f986672389305a3000b83a12417f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 31](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a5955f43848da067d9134790f9fe1c240) [AXP192\_GPIO\_FUNC\_CHARGE\_CTL](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a5955f43848da067d9134790f9fe1c240) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 32](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ad16e246ca71f2e865cccf1b4ad2f9286) [AXP192\_GPIO\_FUNC\_INVALID](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ad16e246ca71f2e865cccf1b4ad2f9286)

33};

34

[ 38](drivers_2mfd_2axp192_8h.md#a61d7d88bead4733fedcbfb70f8ada464)#define AXP192\_GPIO\_FUNC\_VALID(func) (func < AXP192\_GPIO\_FUNC\_INVALID)

39

[ 43](drivers_2mfd_2axp192_8h.md#a0df71981c80a3c46e168287c39df88ee)#define AXP192\_GPIO\_MAX\_NUM 6U

44

62

[ 78](group__mdf__interface__axp192.md#ga61c3f46791f4efa08ee45fc85dc32c81)int [mfd\_axp192\_gpio\_func\_ctrl](group__mdf__interface__axp192.md#ga61c3f46791f4efa08ee45fc85dc32c81)(const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*client\_dev,

79 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, enum [axp192\_gpio\_func](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249) func);

80

[ 91](group__mdf__interface__axp192.md#ga29db6e44c801fecfa1df2d9da93c2e0b)int [mfd\_axp192\_gpio\_func\_get](group__mdf__interface__axp192.md#ga29db6e44c801fecfa1df2d9da93c2e0b)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, enum [axp192\_gpio\_func](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249) \*func);

92

[ 105](group__mdf__interface__axp192.md#ga8db91c44adbf8ca6f727e2deb0aa96dd)int [mfd\_axp192\_gpio\_pd\_ctrl](group__mdf__interface__axp192.md#ga8db91c44adbf8ca6f727e2deb0aa96dd)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, bool enable);

106

[ 118](group__mdf__interface__axp192.md#gabdacd1e10bacf9f0393beb65327eaeea)int [mfd\_axp192\_gpio\_pd\_get](group__mdf__interface__axp192.md#gabdacd1e10bacf9f0393beb65327eaeea)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, bool \*enabled);

119

[ 128](group__mdf__interface__axp192.md#gaa12241d0655122f05da06dc506d2a5c0)int [mfd\_axp192\_gpio\_read\_port](group__mdf__interface__axp192.md#gaa12241d0655122f05da06dc506d2a5c0)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value);

129

[ 139](group__mdf__interface__axp192.md#ga7570c8657918c15c71fddca264bce10e)int [mfd\_axp192\_gpio\_write\_port](group__mdf__interface__axp192.md#ga7570c8657918c15c71fddca264bce10e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask);

140

144

145#ifdef \_\_cplusplus

146}

147#endif

148

149#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AXP192\_H\_ \*/

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[axp192\_gpio\_func](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249)

axp192\_gpio\_func

GPIO function type.

**Definition** axp192.h:23

[AXP192\_GPIO\_FUNC\_PWM](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a2634f857f19e03ab8337780025c25579)

@ AXP192\_GPIO\_FUNC\_PWM

**Definition** axp192.h:29

[AXP192\_GPIO\_FUNC\_CHARGE\_CTL](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a5955f43848da067d9134790f9fe1c240)

@ AXP192\_GPIO\_FUNC\_CHARGE\_CTL

**Definition** axp192.h:31

[AXP192\_GPIO\_FUNC\_FLOAT](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a69c1f986672389305a3000b83a12417f)

@ AXP192\_GPIO\_FUNC\_FLOAT

**Definition** axp192.h:30

[AXP192\_GPIO\_FUNC\_OUTPUT\_LOW](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249a8d006f1e4284057f5b952b236729c5f5)

@ AXP192\_GPIO\_FUNC\_OUTPUT\_LOW

**Definition** axp192.h:26

[AXP192\_GPIO\_FUNC\_ADC](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ab3a2622cccb9ec1cdf22ddd5ac75ae6a)

@ AXP192\_GPIO\_FUNC\_ADC

**Definition** axp192.h:28

[AXP192\_GPIO\_FUNC\_INPUT](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ab8eee3f4b6ce22594b90d7e49e4927df)

@ AXP192\_GPIO\_FUNC\_INPUT

**Definition** axp192.h:24

[AXP192\_GPIO\_FUNC\_INVALID](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ad16e246ca71f2e865cccf1b4ad2f9286)

@ AXP192\_GPIO\_FUNC\_INVALID

**Definition** axp192.h:32

[AXP192\_GPIO\_FUNC\_LDO](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249ae9f961ad84c38f3315e3cdb25ede9328)

@ AXP192\_GPIO\_FUNC\_LDO

**Definition** axp192.h:27

[AXP192\_GPIO\_FUNC\_OUTPUT\_OD](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249af1c2244571c0a3b12c0ae94c583c1a4b)

@ AXP192\_GPIO\_FUNC\_OUTPUT\_OD

**Definition** axp192.h:25

[mfd\_axp192\_gpio\_func\_get](group__mdf__interface__axp192.md#ga29db6e44c801fecfa1df2d9da93c2e0b)

int mfd\_axp192\_gpio\_func\_get(const struct device \*dev, uint8\_t gpio, enum axp192\_gpio\_func \*func)

Read out current configuration of a specific GPIO pin.

[mfd\_axp192\_gpio\_func\_ctrl](group__mdf__interface__axp192.md#ga61c3f46791f4efa08ee45fc85dc32c81)

int mfd\_axp192\_gpio\_func\_ctrl(const struct device \*dev, const struct device \*client\_dev, uint8\_t gpio, enum axp192\_gpio\_func func)

Request a GPIO pin to be configured to a specific function.

[mfd\_axp192\_gpio\_write\_port](group__mdf__interface__axp192.md#ga7570c8657918c15c71fddca264bce10e)

int mfd\_axp192\_gpio\_write\_port(const struct device \*dev, uint8\_t value, uint8\_t mask)

Write GPIO port.

[mfd\_axp192\_gpio\_pd\_ctrl](group__mdf__interface__axp192.md#ga8db91c44adbf8ca6f727e2deb0aa96dd)

int mfd\_axp192\_gpio\_pd\_ctrl(const struct device \*dev, uint8\_t gpio, bool enable)

Enable pull-down on specified GPIO pin.

[mfd\_axp192\_gpio\_read\_port](group__mdf__interface__axp192.md#gaa12241d0655122f05da06dc506d2a5c0)

int mfd\_axp192\_gpio\_read\_port(const struct device \*dev, uint8\_t \*value)

Read GPIO port.

[mfd\_axp192\_gpio\_pd\_get](group__mdf__interface__axp192.md#gabdacd1e10bacf9f0393beb65327eaeea)

int mfd\_axp192\_gpio\_pd\_get(const struct device \*dev, uint8\_t gpio, bool \*enabled)

Read out the current pull-down configuration of a specific GPIO.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [axp192.h](drivers_2mfd_2axp192_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
