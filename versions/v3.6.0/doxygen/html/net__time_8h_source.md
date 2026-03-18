---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__time_8h_source.html
original_path: doxygen/html/net__time_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_time.h

[Go to the documentation of this file.](net__time_8h.md)

1/\*

2 \* Copyright (c) 2023 Zephyr Project

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

20

21#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_TIME\_H\_

22#define ZEPHYR\_INCLUDE\_NET\_NET\_TIME\_H\_

23

24/\* Include required for NSEC\_PER\_\* constants. \*/

25#include <[zephyr/sys\_clock.h](include_2zephyr_2sys__clock_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 101](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56);

102

[ 104](group__net__time.md#ga38c90d968fc905093de2db057e6fa199)#define NET\_TIME\_MAX INT64\_MAX

105

[ 107](group__net__time.md#ga732cb69409953ce0ce08991179afe718)#define NET\_TIME\_MIN INT64\_MIN

108

[ 110](group__net__time.md#gabcd93249b790bea7ed6f8aab9ebe568a)#define NET\_TIME\_SEC\_MAX (NET\_TIME\_MAX / NSEC\_PER\_SEC)

111

[ 113](group__net__time.md#ga1fe8655623f0db550f7ae501b161940b)#define NET\_TIME\_SEC\_MIN (NET\_TIME\_MIN / NSEC\_PER\_SEC)

114

115#ifdef \_\_cplusplus

116}

117#endif

118

122

123#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_TIME\_H\_ \*/

[net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)

int64\_t net\_time\_t

Any occurrence of net\_time\_t specifies a concept of nanosecond resolution scalar time span,...

**Definition** net\_time.h:101

[sys\_clock.h](include_2zephyr_2sys__clock_8h.md)

Variables needed for system clock.

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_time.h](net__time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
