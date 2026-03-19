---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__time_8h_source.html
original_path: doxygen/html/net__time_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

22

23#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_TIME\_H\_

24#define ZEPHYR\_INCLUDE\_NET\_NET\_TIME\_H\_

25

26/\* Include required for NSEC\_PER\_\* constants. \*/

27#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 103](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56);

104

[ 106](group__net__time.md#ga38c90d968fc905093de2db057e6fa199)#define NET\_TIME\_MAX INT64\_MAX

107

[ 109](group__net__time.md#ga732cb69409953ce0ce08991179afe718)#define NET\_TIME\_MIN INT64\_MIN

110

[ 112](group__net__time.md#gabcd93249b790bea7ed6f8aab9ebe568a)#define NET\_TIME\_SEC\_MAX (NET\_TIME\_MAX / NSEC\_PER\_SEC)

113

[ 115](group__net__time.md#ga1fe8655623f0db550f7ae501b161940b)#define NET\_TIME\_SEC\_MIN (NET\_TIME\_MIN / NSEC\_PER\_SEC)

116

117#ifdef \_\_cplusplus

118}

119#endif

120

124

125#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_TIME\_H\_ \*/

[net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)

int64\_t net\_time\_t

Any occurrence of net\_time\_t specifies a concept of nanosecond resolution scalar time span,...

**Definition** net\_time.h:103

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[sys\_clock.h](sys__clock_8h.md)

Variables needed for system clock.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_time.h](net__time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
