---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ambiq-apollo5-pinctrl_8h_source.html
original_path: doxygen/html/ambiq-apollo5-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ambiq-apollo5-pinctrl.h

[Go to the documentation of this file.](ambiq-apollo5-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2025 Ambiq Micro Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_APOLLO5\_PINCTRL\_H\_\_

8#define \_\_APOLLO5\_PINCTRL\_H\_\_

9

[ 10](ambiq-apollo5-pinctrl_8h.md#a8c22bac02781bdc9237a2c7938d78038)#define APOLLO5\_ALT\_FUNC\_POS 0

[ 11](ambiq-apollo5-pinctrl_8h.md#ac35ff7ac7e5d9288dcab2c51413fb1fa)#define APOLLO5\_ALT\_FUNC\_MASK 0xf

12

[ 13](ambiq-apollo5-pinctrl_8h.md#a7d03a9ca93525a57900dd019f950f34d)#define APOLLO5\_PIN\_NUM\_POS 4

[ 14](ambiq-apollo5-pinctrl_8h.md#aedbb28a1b3dca93f8ce798a14365ffda)#define APOLLO5\_PIN\_NUM\_MASK 0xff

15

[ 16](ambiq-apollo5-pinctrl_8h.md#a2111c8a6e9540311d67885ad557f9d7b)#define APOLLO5\_PINMUX(pin\_num, alt\_func) \

17 (pin\_num << APOLLO5\_PIN\_NUM\_POS | \

18 alt\_func << APOLLO5\_ALT\_FUNC\_POS)

19

20#endif /\* \_\_APOLLO5\_PINCTRL\_H\_\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ambiq-apollo5-pinctrl.h](ambiq-apollo5-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
