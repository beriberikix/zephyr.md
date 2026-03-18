---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/pinctrl-ra-common_8h_source.html
original_path: doxygen/html/pinctrl-ra-common_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-ra-common.h

[Go to the documentation of this file.](pinctrl-ra-common_8h.md)

1/\*

2 \* Copyright (c) 2023 TOKITA Hiroshi <tokita.hiroshi@fujitsu.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RA\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RA\_COMMON\_H\_

9

[ 10](pinctrl-ra-common_8h.md#a113d98d5dece049c593a5aef12437d75)#define PORT4\_POS 29

[ 11](pinctrl-ra-common_8h.md#a6f0d2254afbdaa587e24fc3da5e01ec7)#define PORT4\_MASK 0x1

[ 12](pinctrl-ra-common_8h.md#a36b3cbcfdb0dc8773bd2075f03b7af21)#define PSEL\_POS 24

[ 13](pinctrl-ra-common_8h.md#a08e7257d70d4cddfec8fe57461aef1f7)#define PSEL\_MASK 0x5

[ 14](pinctrl-ra-common_8h.md#ab9a807cc315af3fc52903b357fe4def0)#define PORT\_POS 21

[ 15](pinctrl-ra-common_8h.md#a753dc0d0821793f46a32babcf2087a82)#define PORT\_MASK 0x7

[ 16](pinctrl-ra-common_8h.md#a34af731a37775b8da8f1c63a2e6186e3)#define PIN\_POS 17

[ 17](pinctrl-ra-common_8h.md#a838ccdbc9c7ae5cfc5ec5328f1fd7404)#define PIN\_MASK 0xF

[ 18](pinctrl-ra-common_8h.md#a301c04edbd1a0282380fdaa5af14ad55)#define OPT\_POS 0

[ 19](pinctrl-ra-common_8h.md#af44b6097b3ff3bd26acb0dee9a571374)#define OPT\_MASK 0x1B000

20

[ 21](pinctrl-ra-common_8h.md#a90dffe4222a204ce3d83db055af089a1)#define RA\_PINCFG\_GPIO 0x00000

[ 22](pinctrl-ra-common_8h.md#a200abb246b5840ee429b5ffdd76fe35c)#define RA\_PINCFG\_FUNC 0x10000

[ 23](pinctrl-ra-common_8h.md#aab0068f1482f166541504b8bc2958cf4)#define RA\_PINCFG\_ANALOG 0x08000

24

[ 25](pinctrl-ra-common_8h.md#a10cac511c82da4ae64ef387f5d08183e)#define RA\_PINCFG(port, pin, psel, opt) \

26 ((((psel)&PSEL\_MASK) << PSEL\_POS) | (((pin)&PIN\_MASK) << PIN\_POS) | \

27 (((port)&PORT\_MASK) << PORT\_POS) | ((((port) >> 3) & PORT4\_MASK) << PORT4\_POS) | \

28 (((opt)&OPT\_MASK) << OPT\_POS))

29

30#if RA\_SOC\_PINS >= 40

31#define RA\_PINCFG\_\_40(port, pin, psel, opt) RA\_PINCFG(port, pin, psel, opt)

32#endif

33

34#if RA\_SOC\_PINS >= 48

35#define RA\_PINCFG\_\_48(port, pin, psel, opt) RA\_PINCFG(port, pin, psel, opt)

36#endif

37

38#if RA\_SOC\_PINS >= 64

39#define RA\_PINCFG\_\_64(port, pin, psel, opt) RA\_PINCFG(port, pin, psel, opt)

40#endif

41

42#if RA\_SOC\_PINS >= 100

43#define RA\_PINCFG\_100(port, pin, psel, opt) RA\_PINCFG(port, pin, psel, opt)

44#endif

45

46#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-ra-common.h](pinctrl-ra-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
