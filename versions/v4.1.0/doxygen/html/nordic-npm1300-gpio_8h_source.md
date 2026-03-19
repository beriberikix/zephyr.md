---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nordic-npm1300-gpio_8h_source.html
original_path: doxygen/html/nordic-npm1300-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nordic-npm1300-gpio.h

[Go to the documentation of this file.](nordic-npm1300-gpio_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM1300\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM1300\_GPIO\_H\_

8

24

30

33#define NPM1300\_GPIO\_DRIVE\_MSK 0x0100U

35

[ 37](group__gpio__interface__npm1300.md#ga722f82469c3c9cd88ab50c6bb75e9645)#define NPM1300\_GPIO\_DRIVE\_1MA (0U << 8U)

[ 39](group__gpio__interface__npm1300.md#ga8b8b6263b00bf56fc9d486f8d542d56d)#define NPM1300\_GPIO\_DRIVE\_6MA (1U << 8U)

40

42

48

51#define NPM1300\_GPIO\_DEBOUNCE\_MSK 0x0200U

53

[ 55](group__gpio__interface__npm1300.md#gaacaf730223621e60b83f47680d132b73)#define NPM1300\_GPIO\_DEBOUNCE\_OFF (0U << 9U)

[ 57](group__gpio__interface__npm1300.md#ga668319bb806733e3ded7026b76e8461d)#define NPM1300\_GPIO\_DEBOUNCE\_ON (1U << 9U)

58

60

66

69#define NPM1300\_GPIO\_WDT\_RESET\_MSK 0x0400U

71

[ 73](group__gpio__interface__npm1300.md#gad8117ab46f3c11c72f200ef36d99571e)#define NPM1300\_GPIO\_WDT\_RESET\_OFF (0U << 10U)

[ 75](group__gpio__interface__npm1300.md#ga34d42db564731b044d43d7732d872510)#define NPM1300\_GPIO\_WDT\_RESET\_ON (1U << 10U)

76

78

84

87#define NPM1300\_GPIO\_PWRLOSSWARN\_MSK 0x0800U

89

[ 91](group__gpio__interface__npm1300.md#ga982a2ede317e91f66d1ba8924d5f0d03)#define NPM1300\_GPIO\_PWRLOSSWARN\_OFF (0U << 11U)

[ 93](group__gpio__interface__npm1300.md#ga20d4345e30291bee82b6a63f0a1f8d40)#define NPM1300\_GPIO\_PWRLOSSWARN\_ON (1U << 11U)

94

96

98

99#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM1300\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nordic-npm1300-gpio.h](nordic-npm1300-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
