---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/nordic-npm13xx-gpio_8h_source.html
original_path: doxygen/html/nordic-npm13xx-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nordic-npm13xx-gpio.h

[Go to the documentation of this file.](nordic-npm13xx-gpio_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM13XX\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM13XX\_GPIO\_H\_

8

24

30

33#define NPM13XX\_GPIO\_DRIVE\_MSK 0x0100U

35

[ 37](group__gpio__interface__npm13xx.md#ga6a747e318dbdecb394e6c97055cf7d3b)#define NPM13XX\_GPIO\_DRIVE\_1MA (0U << 8U)

[ 39](group__gpio__interface__npm13xx.md#ga29c65d6c81acd6c6474a8d5463d30312)#define NPM13XX\_GPIO\_DRIVE\_6MA (1U << 8U)

40

42

48

51#define NPM13XX\_GPIO\_DEBOUNCE\_MSK 0x0200U

53

[ 55](group__gpio__interface__npm13xx.md#ga94b628f01bd35ef5a8c4be5810853d8a)#define NPM13XX\_GPIO\_DEBOUNCE\_OFF (0U << 9U)

[ 57](group__gpio__interface__npm13xx.md#ga37203fc635db945392c25ba5eddb42ad)#define NPM13XX\_GPIO\_DEBOUNCE\_ON (1U << 9U)

58

60

66

69#define NPM13XX\_GPIO\_WDT\_RESET\_MSK 0x0400U

71

[ 73](group__gpio__interface__npm13xx.md#ga7e835aa905fce6b9bd88f6c113ad8fbd)#define NPM13XX\_GPIO\_WDT\_RESET\_OFF (0U << 10U)

[ 75](group__gpio__interface__npm13xx.md#gac17073bd2d8bda878c0cf7307276efcb)#define NPM13XX\_GPIO\_WDT\_RESET\_ON (1U << 10U)

76

78

84

87#define NPM13XX\_GPIO\_PWRLOSSWARN\_MSK 0x0800U

89

[ 91](group__gpio__interface__npm13xx.md#ga8aa4cab9a6961ca60a14e1cae448376e)#define NPM13XX\_GPIO\_PWRLOSSWARN\_OFF (0U << 11U)

[ 93](group__gpio__interface__npm13xx.md#gae774196d9a4258da3d849899de5b744b)#define NPM13XX\_GPIO\_PWRLOSSWARN\_ON (1U << 11U)

94

96

98

99#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NPM13XX\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nordic-npm13xx-gpio.h](nordic-npm13xx-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
