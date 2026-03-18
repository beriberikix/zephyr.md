---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/pwm_2max31790_8h_source.html
original_path: doxygen/html/pwm_2max31790_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max31790.h

[Go to the documentation of this file.](pwm_2max31790_8h.md)

1/\*

2 \* Copyright (c) 2023 SILA Embedded Solutions GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PWM\_MAX31790\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_PWM\_MAX31790\_H\_

9

19#define PWM\_MAX31790\_FLAG\_RPM\_MODE\_POS 8

20#define PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_POS 9

21#define PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_POS 12

22#define PWM\_MAX31790\_FLAG\_SPIN\_UP\_POS 15

24

[ 34](pwm_2max31790_8h.md#a49d4bcb7f5c77aa1489e54957f32433a)#define PWM\_MAX31790\_FLAG\_RPM\_MODE (1 << PWM\_MAX31790\_FLAG\_RPM\_MODE\_POS)

[ 42](pwm_2max31790_8h.md#a98b4a27f06adbc3f7011f8e22c29d28f)#define PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_1 (0 << PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_POS)

[ 43](pwm_2max31790_8h.md#a98f86024db6a17a04def84bafd87f5b9)#define PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_2 (1 << PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_POS)

[ 44](pwm_2max31790_8h.md#a77105f041235cc0189c43ddece06f220)#define PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_4 (2 << PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_POS)

[ 45](pwm_2max31790_8h.md#a0fb4a86a4cd1ed5582f025d35f82c148)#define PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_8 (3 << PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_POS)

[ 46](pwm_2max31790_8h.md#a28bc19a81c2ea6b910a84cd622bcea05)#define PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_16 (4 << PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_POS)

[ 47](pwm_2max31790_8h.md#a79d0de4ba831f2b1df823550bc813578)#define PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_32 (5 << PWM\_MAX31790\_FLAG\_SPEED\_RANGE\_POS)

[ 54](pwm_2max31790_8h.md#a9030b924200302e3b03295d540e71df1)#define PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_0 (0 << PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_POS)

[ 55](pwm_2max31790_8h.md#ad0cf273c9627e5491438ce4827184e2d)#define PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_1 (1 << PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_POS)

[ 56](pwm_2max31790_8h.md#ab49c21cba041885bc5e2c67f5decf994)#define PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_2 (2 << PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_POS)

[ 57](pwm_2max31790_8h.md#a4e3772d1a9d1a4b79b66fa016d681106)#define PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_3 (3 << PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_POS)

[ 58](pwm_2max31790_8h.md#a04e3d5b3adcefb3152090707a1affcf0)#define PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_4 (4 << PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_POS)

[ 59](pwm_2max31790_8h.md#a8bd18ed522d33db5d7a3b0f02b8b9e39)#define PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_5 (5 << PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_POS)

[ 60](pwm_2max31790_8h.md#a83447dea9e822dae8f9838ace497fc55)#define PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_6 (6 << PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_POS)

[ 61](pwm_2max31790_8h.md#a40371ed8f761964573be18c33db2c759)#define PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_7 (7 << PWM\_MAX31790\_FLAG\_PWM\_RATE\_OF\_CHANGE\_POS)

[ 68](pwm_2max31790_8h.md#a2b7c056ec08e8add71a422d9cc610c98)#define PWM\_MAX31790\_FLAG\_SPIN\_UP (1 << PWM\_MAX31790\_FLAG\_SPIN\_UP\_POS)

70

71#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PWM\_MAX31790\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pwm](dir_be6d7cea606f8787ce461c788254eca9.md)
- [max31790.h](pwm_2max31790_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
