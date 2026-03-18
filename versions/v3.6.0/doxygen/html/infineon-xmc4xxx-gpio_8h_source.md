---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/infineon-xmc4xxx-gpio_8h_source.html
original_path: doxygen/html/infineon-xmc4xxx-gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

infineon-xmc4xxx-gpio.h

[Go to the documentation of this file.](infineon-xmc4xxx-gpio_8h.md)

1/\*

2 \* Copyright (c) 2022 Schlumberger

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_INFINEON\_XMC4XXX\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_INFINEON\_XMC4XXX\_GPIO\_H\_

8

[ 9](infineon-xmc4xxx-gpio_8h.md#a0204cbd6c151fcea59199b1c4e007eaf)#define XMC4XXX\_GPIO\_DS\_POS 9

[ 10](infineon-xmc4xxx-gpio_8h.md#a766a7c07cd178b9373fec28745b1e077)#define XMC4XXX\_GPIO\_DS\_MASK 0xf

11

12/\* GPIO driver will use XMC\_GPIO\_OUTPUT\_STRENGTH\_STRONG\_MEDIUM\_EDGE if DS is unset \*/

[ 13](infineon-xmc4xxx-gpio_8h.md#ab820bfc6577c45c88b59260531d078d3)#define XMC4XXX\_GPIO\_DS\_STRONG\_SHARP\_EDGE (0x1 << XMC4XXX\_GPIO\_DS\_POS)

[ 14](infineon-xmc4xxx-gpio_8h.md#a6a21bcff48f4e8a4acede963a534fb95)#define XMC4XXX\_GPIO\_DS\_STRONG\_MEDIUM\_EDGE (0x2 << XMC4XXX\_GPIO\_DS\_POS)

[ 15](infineon-xmc4xxx-gpio_8h.md#a07e14898ba2a322edf9729054832c1a9)#define XMC4XXX\_GPIO\_DS\_STRONG\_SOFT\_EDGE (0x3 << XMC4XXX\_GPIO\_DS\_POS)

[ 16](infineon-xmc4xxx-gpio_8h.md#aa81ddd8894b2f3a1e991b5d95ac81a7f)#define XMC4XXX\_GPIO\_DS\_STRONG\_SLOW\_EDGE (0x4 << XMC4XXX\_GPIO\_DS\_POS)

[ 17](infineon-xmc4xxx-gpio_8h.md#af725ddf9a1dfaf02d478cdcf94132a24)#define XMC4XXX\_GPIO\_DS\_MEDIUM (0x5 << XMC4XXX\_GPIO\_DS\_POS)

18/\* values 5, 6 not set in xmc4\_gpio.h \*/

[ 19](infineon-xmc4xxx-gpio_8h.md#a5c307c3181d3094cadb68766b318b3e5)#define XMC4XXX\_GPIO\_DS\_WEAK (0x8 << XMC4XXX\_GPIO\_DS\_POS)

20

[ 21](infineon-xmc4xxx-gpio_8h.md#a52bb9df6ed1e4ead550ceefe1b96a5b3)#define XMC4XXX\_GPIO\_GET\_DS(flags) ((flags >> XMC4XXX\_GPIO\_DS\_POS) & XMC4XXX\_GPIO\_DS\_MASK)

22

23#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_INFINEON\_XMC4XXX\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [infineon-xmc4xxx-gpio.h](infineon-xmc4xxx-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
