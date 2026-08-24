---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/it51xxx__pwm_8h_source.html
original_path: doxygen/html/it51xxx__pwm_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

it51xxx\_pwm.h

[Go to the documentation of this file.](it51xxx__pwm_8h.md)

1/\*

2 \* Copyright (c) 2025 ITE Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PWM\_IT51XXX\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PWM\_IT51XXX\_H\_

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10

11/\* PWM prescaler references \*/

[ 12](it51xxx__pwm_8h.md#a98aaba2e733ce20cd59eeadc33663965)#define PWM\_PRESCALER\_C4 1

[ 13](it51xxx__pwm_8h.md#a15fa229af614107078c43d887c985520)#define PWM\_PRESCALER\_C6 2

[ 14](it51xxx__pwm_8h.md#a784a4aa1339416ac435615ec74742ca9)#define PWM\_PRESCALER\_C7 3

15

16/\* PWM channel references \*/

[ 17](it51xxx__pwm_8h.md#a9b43cbcd1d148602c21fa850bebefbdc)#define PWM\_CHANNEL\_0 0

[ 18](it51xxx__pwm_8h.md#a1da821e350e2e57c46bb73d60256e537)#define PWM\_CHANNEL\_1 1

[ 19](it51xxx__pwm_8h.md#a90a3351d5ed724d6970eb50970e12df3)#define PWM\_CHANNEL\_2 2

[ 20](it51xxx__pwm_8h.md#ad7ecaad6ade54bca69bac60bb39b3d23)#define PWM\_CHANNEL\_3 3

[ 21](it51xxx__pwm_8h.md#a7695e0811561c98657a24fb828b7dd80)#define PWM\_CHANNEL\_4 4

[ 22](it51xxx__pwm_8h.md#a45c3365cad7dbd63b7db5881a287ca78)#define PWM\_CHANNEL\_5 5

[ 23](it51xxx__pwm_8h.md#abbce1e1eeae1747443dcea1259f99384)#define PWM\_CHANNEL\_6 6

[ 24](it51xxx__pwm_8h.md#aefd382e2874b5ecac051e5f0129199b0)#define PWM\_CHANNEL\_7 7

25

26/\*

27 \* Provides a type to hold PWM configuration flags.

28 \*

29 \* The upper 8 bits are reserved for SoC specific flags.

30 \* Output open-drain flag [ 8 ]

31 \*/

[ 32](it51xxx__pwm_8h.md#a7250e9763907d112155feca0f89f107f)#define PWM\_IT51XXX\_OPEN\_DRAIN BIT(8)

33

34#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PWM\_IT51XXX\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pwm](dir_ff747911c88ea6a5644735057b122c0d.md)
- [it51xxx\_pwm.h](it51xxx__pwm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
