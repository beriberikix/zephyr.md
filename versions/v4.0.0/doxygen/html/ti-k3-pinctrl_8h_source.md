---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ti-k3-pinctrl_8h_source.html
original_path: doxygen/html/ti-k3-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ti-k3-pinctrl.h

[Go to the documentation of this file.](ti-k3-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2023 Enphase Energy

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_TI\_K3\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_TI\_K3\_PINCTRL\_H\_

9

[ 10](ti-k3-pinctrl_8h.md#a0febfbc566c3728115a03bb7f7dc620e)#define PULLUDEN\_SHIFT 16

[ 11](ti-k3-pinctrl_8h.md#ad24bec783f5c84d6e82a34141b0d057a)#define PULLTYPESEL\_SHIFT 17

[ 12](ti-k3-pinctrl_8h.md#aa96a5ff81411950a5661202b443142ca)#define RXACTIVE\_SHIFT 18

13

[ 14](ti-k3-pinctrl_8h.md#a768319530a87153b9804251bdc3b9e4d)#define PULL\_DISABLE (1 << PULLUDEN\_SHIFT)

[ 15](ti-k3-pinctrl_8h.md#acaca8fc3aa06bcd710d33c74ec8bff40)#define PULL\_ENABLE (0 << PULLUDEN\_SHIFT)

16

[ 17](ti-k3-pinctrl_8h.md#aca4f67c0077925f24ea1f6b26e313271)#define PULL\_UP ((1 << PULLTYPESEL\_SHIFT) | PULL\_ENABLE)

[ 18](ti-k3-pinctrl_8h.md#ab47362632d6cd744f764880731de5704)#define PULL\_DOWN ((0 << PULLTYPESEL\_SHIFT) | PULL\_ENABLE)

19

[ 20](ti-k3-pinctrl_8h.md#a6ad4c7f924e24241629dc10ed6b433f9)#define INPUT\_ENABLE (1 << RXACTIVE\_SHIFT)

[ 21](ti-k3-pinctrl_8h.md#a40984b9ac260aa5f3467e55a91cfff30)#define INPUT\_DISABLE (0 << RXACTIVE\_SHIFT)

22

23/\* Only the following macros are intended be used in DTS files \*/

24

[ 25](ti-k3-pinctrl_8h.md#a16f6fcf4256a279427eb2c243c9e0bd5)#define PIN\_OUTPUT (INPUT\_DISABLE | PULL\_DISABLE)

[ 26](ti-k3-pinctrl_8h.md#abfd6c5cdc843d33ebddee7b244931fc3)#define PIN\_OUTPUT\_PULLUP (INPUT\_DISABLE | PULL\_UP)

[ 27](ti-k3-pinctrl_8h.md#a8c5881bfb4d468fa634c8bec1d68595c)#define PIN\_OUTPUT\_PULLDOWN (INPUT\_DISABLE | PULL\_DOWN)

[ 28](ti-k3-pinctrl_8h.md#a5a94a90bd5b33109a2e3832760bc5da1)#define PIN\_INPUT (INPUT\_ENABLE | PULL\_DISABLE)

[ 29](ti-k3-pinctrl_8h.md#a06f998fe6be04b6a8d278b150790d436)#define PIN\_INPUT\_PULLUP (INPUT\_ENABLE | PULL\_UP)

[ 30](ti-k3-pinctrl_8h.md#a3ce1576f1da81ea2f6c492b8f8cd5350)#define PIN\_INPUT\_PULLDOWN (INPUT\_ENABLE | PULL\_DOWN)

31

[ 32](ti-k3-pinctrl_8h.md#adf2868df9ec8ecdd15e89b8a33a1fdbc)#define MUX\_MODE\_0 0

[ 33](ti-k3-pinctrl_8h.md#a7efdf57cf0a9ef6847bd3e62b42ab771)#define MUX\_MODE\_1 1

[ 34](ti-k3-pinctrl_8h.md#ac2c88f4a9d2752f06cb925ca4993a35e)#define MUX\_MODE\_2 2

[ 35](ti-k3-pinctrl_8h.md#a018dca77be29b23eface983280b1812f)#define MUX\_MODE\_3 3

[ 36](ti-k3-pinctrl_8h.md#ad0ff0ccc1b0b38c49a842c565aa6c0b8)#define MUX\_MODE\_4 4

[ 37](ti-k3-pinctrl_8h.md#a6192dc972d0c7712a06be2d47205c558)#define MUX\_MODE\_5 5

[ 38](ti-k3-pinctrl_8h.md#a9a5bcfce0779373f2ed0f0dd645a9703)#define MUX\_MODE\_6 6

[ 39](ti-k3-pinctrl_8h.md#a97074809f50f00264fd33793d4d0b647)#define MUX\_MODE\_7 7

[ 40](ti-k3-pinctrl_8h.md#a0c6c56a47585b1fe1233139689c519de)#define MUX\_MODE\_8 8

[ 41](ti-k3-pinctrl_8h.md#aa951dab323d11eb1059ed1f278f7730d)#define MUX\_MODE\_9 9

[ 42](ti-k3-pinctrl_8h.md#aebfc9715ee7edf771cb23da2b0028a11)#define MUX\_MODE\_10 10

[ 43](ti-k3-pinctrl_8h.md#a052beac6cdfccce06bb16f447e54db92)#define MUX\_MODE\_11 11

[ 44](ti-k3-pinctrl_8h.md#a1213893060e171293e0484324a6e20ab)#define MUX\_MODE\_12 12

[ 45](ti-k3-pinctrl_8h.md#aa436ee60756d56a9a5f451cdb0dae3c5)#define MUX\_MODE\_13 13

[ 46](ti-k3-pinctrl_8h.md#afa386486189b7027f7ac93a9e2fa2614)#define MUX\_MODE\_14 14

47

[ 48](ti-k3-pinctrl_8h.md#a95cac03e59fecc4cb31762747913dddf)#define K3\_PINMUX(offset, value, mux\_mode) (((offset) & 0x1fff)) ((value) | (mux\_mode))

49

50#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_TI\_K3\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ti-k3-pinctrl.h](ti-k3-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
