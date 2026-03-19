---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pwm__fake_8h_source.html
original_path: doxygen/html/pwm__fake_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pwm\_fake.h

[Go to the documentation of this file.](pwm__fake_8h.md)

1/\*

2 \* Copyright (c) 2024, Kickmaker

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef INCLUDE\_DRIVERS\_PWM\_PWM\_FAKE\_H\_

8#define INCLUDE\_DRIVERS\_PWM\_PWM\_FAKE\_H\_

9

10#include <[zephyr/drivers/pwm.h](drivers_2pwm_8h.md)>

11#include <[zephyr/fff.h](fff_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 17](pwm__fake_8h.md#a97f4dc2d1a09b5152fa79c5b6bf3591a)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_pwm\_set\_cycles, const struct [device](structdevice.md) \*, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f),

18 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f), [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0));

19

20#ifdef \_\_cplusplus

21}

22#endif

23

24#endif /\* INCLUDE\_DRIVERS\_PWM\_PWM\_FAKE\_H\_ \*/

[pwm.h](drivers_2pwm_8h.md)

Public PWM Driver APIs.

[fff.h](fff_8h.md)

[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)

#define DECLARE\_FAKE\_VALUE\_FUNC(...)

**Definition** fff.h:8684

[pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0)

uint16\_t pwm\_flags\_t

Provides a type to hold PWM configuration flags.

**Definition** pwm.h:81

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pwm](dir_be6d7cea606f8787ce461c788254eca9.md)
- [pwm\_fake.h](pwm__fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
