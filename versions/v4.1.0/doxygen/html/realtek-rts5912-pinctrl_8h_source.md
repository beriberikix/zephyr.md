---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/realtek-rts5912-pinctrl_8h_source.html
original_path: doxygen/html/realtek-rts5912-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

realtek-rts5912-pinctrl.h

[Go to the documentation of this file.](realtek-rts5912-pinctrl_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \*

4 \* Copyright (c) 2024 Realtek Semiconductor Corporation, SIBG-SD7

5 \* Author: Lin Yu-Cheng <lin\_yu\_cheng@realtek.com>

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_REALTEK\_RTS5912\_PINCTRL\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_REALTEK\_RTS5912\_PINCTRL\_H\_

10

11#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

12

[ 13](realtek-rts5912-pinctrl_8h.md#acaf6fce01a1687b4286a749ead4ca90c)#define REALTEK\_RTS5912\_GPIO\_INOUT BIT(0) /\* IN/OUT : 0 input 1 output \*/

[ 14](realtek-rts5912-pinctrl_8h.md#a37c9b457ded69e287ac79d93d75392f1)#define REALTEK\_RTS5912\_GPIO\_PINON BIT(1) /\* Input\_detect : 1 enable 0 disable \*/

[ 15](realtek-rts5912-pinctrl_8h.md#af6ac5662dc1122df9934acdfda1a972f)#define REALTEK\_RTS5912\_GPIO\_VOLT BIT(2) /\* Pin Volt : 1 1.8V 0 3.3V \*/

[ 16](realtek-rts5912-pinctrl_8h.md#aa068c89b25e53c56cebaa2c292f0d496)#define REALTEK\_RTS5912\_FUNC0 0 /\* GPIO mode \*/

[ 17](realtek-rts5912-pinctrl_8h.md#a320f452117e29ea363d8e92791d11a62)#define REALTEK\_RTS5912\_FUNC1 BIT(8) /\* Function mode use BIT0~2 \*/

[ 18](realtek-rts5912-pinctrl_8h.md#a0f1aeb726f327dd57aa91fcd68fb96e7)#define REALTEK\_RTS5912\_FUNC2 BIT(9)

[ 19](realtek-rts5912-pinctrl_8h.md#a1cf29b9a5799e9ecc455e8f304114574)#define REALTEK\_RTS5912\_FUNC3 ((BIT(8)) | (BIT(9)))

[ 20](realtek-rts5912-pinctrl_8h.md#a2f9db2ea5d8996c5374eb1c314f2b206)#define REALTEK\_RTS5912\_FUNC4 BIT(10)

21

[ 22](realtek-rts5912-pinctrl_8h.md#ad919b2c55c39409ce55e61c9a6c4b517)#define REALTEK\_RTS5912\_INPUT\_OUTPUT\_POS 0

[ 23](realtek-rts5912-pinctrl_8h.md#a126ef964f014695a4ba2bb12f80df4b7)#define REALTEK\_RTS5912\_INPUT\_DETECTION\_POS 1

[ 24](realtek-rts5912-pinctrl_8h.md#a129d1a2771427bf45ebe1d68b86d1f52)#define REALTEK\_RTS5912\_VOLTAGE\_POS 2

[ 25](realtek-rts5912-pinctrl_8h.md#af2020d8bbae4e24b4e5f48ce1f4fc7f1)#define REALTEK\_RTS5912\_DRV\_STR\_POS 11

[ 26](realtek-rts5912-pinctrl_8h.md#af5aa6f81b75e84553e31401a798266f5)#define REALTEK\_RTS5912\_SLEW\_RATE\_POS 12

[ 27](realtek-rts5912-pinctrl_8h.md#af8faf52c5ea35defe026cb4f6cc95cdc)#define REALTEK\_RTS5912\_PD\_POS 13

[ 28](realtek-rts5912-pinctrl_8h.md#ae3fc4f59fc38de4f3380b13eab30842d)#define REALTEK\_RTS5912\_PU\_POS 14

[ 29](realtek-rts5912-pinctrl_8h.md#ac89f34fde098b5df324b3ed69f108aec)#define REALTEK\_RTS5912\_SCHMITTER\_POS 15

[ 30](realtek-rts5912-pinctrl_8h.md#ab4802986241c477ce74d7ab082ef9ff3)#define REALTEK\_RTS5912\_TYPE\_POS 16

[ 31](realtek-rts5912-pinctrl_8h.md#a67f5fb84972d53406c8c9e440815fe60)#define REALTEK\_RTS5912\_HIGH\_LOW\_POS 17

32

[ 33](realtek-rts5912-pinctrl_8h.md#ab00c925ffba481594ed7216d41efa52a)#define REALTEK\_RTS5912\_GPIO\_HIGH\_POS 18

[ 34](realtek-rts5912-pinctrl_8h.md#a7524cfe0cc5990bf5bc835d030deaf11)#define REALTEK\_RTS5912\_GPIO\_HIGH\_MSK 0x3f

[ 35](realtek-rts5912-pinctrl_8h.md#a3f09fb1e1ad93e1fc1189ad5babbc533)#define REALTEK\_RTS5912\_GPIO\_LOW\_POS 3

[ 36](realtek-rts5912-pinctrl_8h.md#a9cbb1539029aa9b58ffedb4b3ede0e93)#define REALTEK\_RTS5912\_GPIO\_LOW\_MSK 0x1f

37

[ 38](realtek-rts5912-pinctrl_8h.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)#define FUNC0 REALTEK\_RTS5912\_FUNC0

[ 39](realtek-rts5912-pinctrl_8h.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)#define FUNC1 REALTEK\_RTS5912\_FUNC1

[ 40](realtek-rts5912-pinctrl_8h.md#a0e8023a25dd46655b8eda5b0476ba169)#define FUNC2 REALTEK\_RTS5912\_FUNC2

[ 41](realtek-rts5912-pinctrl_8h.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)#define FUNC3 REALTEK\_RTS5912\_FUNC3

[ 42](realtek-rts5912-pinctrl_8h.md#a769e96bef0ce818be7aa2cb0a0a67753)#define FUNC4 REALTEK\_RTS5912\_FUNC4

43

[ 44](realtek-rts5912-pinctrl_8h.md#aa3e9ea3bc9606018c92e70d6728c8594)#define REALTEK\_RTS5912\_PINMUX(n, f) \

45 (((((n) >> 5) & REALTEK\_RTS5912\_GPIO\_HIGH\_MSK) << REALTEK\_RTS5912\_GPIO\_HIGH\_POS) | \

46 (((n) & REALTEK\_RTS5912\_GPIO\_LOW\_MSK) << REALTEK\_RTS5912\_GPIO\_LOW\_POS) | (f))

47

48#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_REALTEK\_RTS5912\_PINCTRL\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [realtek-rts5912-pinctrl.h](realtek-rts5912-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
