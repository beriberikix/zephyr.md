---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/adc__cmp__npcx_8h_source.html
original_path: doxygen/html/adc__cmp__npcx_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc\_cmp\_npcx.h

[Go to the documentation of this file.](adc__cmp__npcx_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_ADC\_CMP\_NPCX\_H\_

8#define \_ADC\_CMP\_NPCX\_H\_

9

[ 10](adc__cmp__npcx_8h.md#a803a31c01dab5a6417a38f2863d63cd8)enum [adc\_cmp\_npcx\_comparison](adc__cmp__npcx_8h.md#a803a31c01dab5a6417a38f2863d63cd8) {

[ 11](adc__cmp__npcx_8h.md#a803a31c01dab5a6417a38f2863d63cd8ab7687952bf7767dabd362415527291ec) [ADC\_CMP\_NPCX\_GREATER](adc__cmp__npcx_8h.md#a803a31c01dab5a6417a38f2863d63cd8ab7687952bf7767dabd362415527291ec),

[ 12](adc__cmp__npcx_8h.md#a803a31c01dab5a6417a38f2863d63cd8ad82416068bf2542ecbab7eda11c3305a) [ADC\_CMP\_NPCX\_LESS\_OR\_EQUAL](adc__cmp__npcx_8h.md#a803a31c01dab5a6417a38f2863d63cd8ad82416068bf2542ecbab7eda11c3305a),

13};

14

15/\* Supported ADC threshold controllers in NPCX series \*/

[ 16](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7b)enum [npcx\_adc\_cmp\_thrctl](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7b) {

[ 17](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba3b32fe6061c4f4665a3f3dd4dc6b4149) [ADC\_CMP\_NPCX\_THRCTL1](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba3b32fe6061c4f4665a3f3dd4dc6b4149),

[ 18](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba28c3ea89d01af5cbfadf01631ba80e22) [ADC\_CMP\_NPCX\_THRCTL2](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba28c3ea89d01af5cbfadf01631ba80e22),

[ 19](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba6e1d82b3799b3935ea08cb1f89fb43d9) [ADC\_CMP\_NPCX\_THRCTL3](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba6e1d82b3799b3935ea08cb1f89fb43d9),

[ 20](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7bad82720ff653bdd33c357da0c4800ff77) [ADC\_CMP\_NPCX\_THRCTL4](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7bad82720ff653bdd33c357da0c4800ff77),

[ 21](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7bac1e7062cf13413c88f988a0d8035e7c0) [ADC\_CMP\_NPCX\_THRCTL5](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7bac1e7062cf13413c88f988a0d8035e7c0),

[ 22](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba757400fdc6537af47fa7f5fb0de4c98f) [ADC\_CMP\_NPCX\_THRCTL6](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba757400fdc6537af47fa7f5fb0de4c98f),

[ 23](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba645e1aa2db79ebd6f4cbcb8d7ba3ec18) [ADC\_CMP\_NPCX\_THRCTL\_COUNT](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba645e1aa2db79ebd6f4cbcb8d7ba3ec18),

24};

25

[ 26](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018a)enum [adc\_cmp\_npcx\_sensor\_attribute](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018a) {

[ 27](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018aa8a66a89764bff1e455273a02da29903d) [SENSOR\_ATTR\_LOWER\_VOLTAGE\_THRESH](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018aa8a66a89764bff1e455273a02da29903d) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 28](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018aaaaadca90015c5516321259b8921cedc3) [SENSOR\_ATTR\_UPPER\_VOLTAGE\_THRESH](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018aaaaadca90015c5516321259b8921cedc3),

29};

30

31#endif /\* \_ADC\_CMP\_NPCX\_H\_ \*/

[adc\_cmp\_npcx\_comparison](adc__cmp__npcx_8h.md#a803a31c01dab5a6417a38f2863d63cd8)

adc\_cmp\_npcx\_comparison

**Definition** adc\_cmp\_npcx.h:10

[ADC\_CMP\_NPCX\_GREATER](adc__cmp__npcx_8h.md#a803a31c01dab5a6417a38f2863d63cd8ab7687952bf7767dabd362415527291ec)

@ ADC\_CMP\_NPCX\_GREATER

**Definition** adc\_cmp\_npcx.h:11

[ADC\_CMP\_NPCX\_LESS\_OR\_EQUAL](adc__cmp__npcx_8h.md#a803a31c01dab5a6417a38f2863d63cd8ad82416068bf2542ecbab7eda11c3305a)

@ ADC\_CMP\_NPCX\_LESS\_OR\_EQUAL

**Definition** adc\_cmp\_npcx.h:12

[adc\_cmp\_npcx\_sensor\_attribute](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018a)

adc\_cmp\_npcx\_sensor\_attribute

**Definition** adc\_cmp\_npcx.h:26

[SENSOR\_ATTR\_LOWER\_VOLTAGE\_THRESH](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018aa8a66a89764bff1e455273a02da29903d)

@ SENSOR\_ATTR\_LOWER\_VOLTAGE\_THRESH

**Definition** adc\_cmp\_npcx.h:27

[SENSOR\_ATTR\_UPPER\_VOLTAGE\_THRESH](adc__cmp__npcx_8h.md#a87c321b131ecec52103cc63b22c0018aaaaadca90015c5516321259b8921cedc3)

@ SENSOR\_ATTR\_UPPER\_VOLTAGE\_THRESH

**Definition** adc\_cmp\_npcx.h:28

[npcx\_adc\_cmp\_thrctl](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7b)

npcx\_adc\_cmp\_thrctl

**Definition** adc\_cmp\_npcx.h:16

[ADC\_CMP\_NPCX\_THRCTL2](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba28c3ea89d01af5cbfadf01631ba80e22)

@ ADC\_CMP\_NPCX\_THRCTL2

**Definition** adc\_cmp\_npcx.h:18

[ADC\_CMP\_NPCX\_THRCTL1](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba3b32fe6061c4f4665a3f3dd4dc6b4149)

@ ADC\_CMP\_NPCX\_THRCTL1

**Definition** adc\_cmp\_npcx.h:17

[ADC\_CMP\_NPCX\_THRCTL\_COUNT](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba645e1aa2db79ebd6f4cbcb8d7ba3ec18)

@ ADC\_CMP\_NPCX\_THRCTL\_COUNT

**Definition** adc\_cmp\_npcx.h:23

[ADC\_CMP\_NPCX\_THRCTL3](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba6e1d82b3799b3935ea08cb1f89fb43d9)

@ ADC\_CMP\_NPCX\_THRCTL3

**Definition** adc\_cmp\_npcx.h:19

[ADC\_CMP\_NPCX\_THRCTL6](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7ba757400fdc6537af47fa7f5fb0de4c98f)

@ ADC\_CMP\_NPCX\_THRCTL6

**Definition** adc\_cmp\_npcx.h:22

[ADC\_CMP\_NPCX\_THRCTL5](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7bac1e7062cf13413c88f988a0d8035e7c0)

@ ADC\_CMP\_NPCX\_THRCTL5

**Definition** adc\_cmp\_npcx.h:21

[ADC\_CMP\_NPCX\_THRCTL4](adc__cmp__npcx_8h.md#ab327195533e735ea950e56aca63b0a7bad82720ff653bdd33c357da0c4800ff77)

@ ADC\_CMP\_NPCX\_THRCTL4

**Definition** adc\_cmp\_npcx.h:20

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:350

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [adc\_cmp\_npcx.h](adc__cmp__npcx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
