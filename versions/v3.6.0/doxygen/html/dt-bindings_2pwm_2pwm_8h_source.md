---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dt-bindings_2pwm_2pwm_8h_source.html
original_path: doxygen/html/dt-bindings_2pwm_2pwm_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pwm.h

[Go to the documentation of this file.](dt-bindings_2pwm_2pwm_8h.md)

1/\*

2 \* Copyright (c) 2019 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PWM\_PWM\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PWM\_PWM\_H\_

8

15

22

[ 24](group__pwm__interface.md#ga17f20d628bcc81d5023c39e4cdfad405)#define PWM\_NSEC(x) (x)

[ 26](group__pwm__interface.md#ga368f28c8daaee25e546484bd908e675e)#define PWM\_USEC(x) (PWM\_NSEC(x) \* 1000UL)

[ 28](group__pwm__interface.md#ga1cccc226a23866dd2dcac9467ff3af0e)#define PWM\_MSEC(x) (PWM\_USEC(x) \* 1000UL)

[ 30](group__pwm__interface.md#ga4da4565d4dbded0efb640bd538cba3c2)#define PWM\_SEC(x) (PWM\_MSEC(x) \* 1000UL)

[ 32](group__pwm__interface.md#ga4a5edbee48c4a5706cf75524aef2364a)#define PWM\_HZ(x) (PWM\_SEC(1UL) / (x))

[ 34](group__pwm__interface.md#gaf846cf23d31d14296e0cbc1f82a530f4)#define PWM\_KHZ(x) (PWM\_HZ((x) \* 1000UL))

35

37

[ 47](group__pwm__interface.md#ga2c706bbada711f383d7b42f09dace861)#define PWM\_POLARITY\_NORMAL (0 << 0)

48

[ 50](group__pwm__interface.md#ga930c0ab50f81aeb571af9747947d7fae)#define PWM\_POLARITY\_INVERTED (1 << 0)

51

53#define PWM\_POLARITY\_MASK 0x1

56

58

59#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PWM\_PWM\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pwm](dir_ff747911c88ea6a5644735057b122c0d.md)
- [pwm.h](dt-bindings_2pwm_2pwm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
