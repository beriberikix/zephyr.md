---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpi-pico-rp2350a-pinctrl_8h_source.html
original_path: doxygen/html/rpi-pico-rp2350a-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi-pico-rp2350a-pinctrl.h

[Go to the documentation of this file.](rpi-pico-rp2350a-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2024, Andrew Featherstone

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_RP2350A\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_RP2350A\_PINCTRL\_H\_

9

10#include "[rpi-pico-rp2350-pinctrl-common.h](rpi-pico-rp2350-pinctrl-common_8h.md)"

11

12/\* ADC channel allocations differ between the RP2350A and RP2350B.

13 \* Refer to Table 1115 in the datasheet.

14 \*/

[ 15](rpi-pico-rp2350a-pinctrl_8h.md#a6ab3748b716a2c39ff7e0e78afec3bdf)#define ADC\_CH0\_P26 RP2XXX\_PINMUX(26, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

[ 16](rpi-pico-rp2350a-pinctrl_8h.md#a237c44c257ad8b0c7d15bca6f83e2b75)#define ADC\_CH1\_P27 RP2XXX\_PINMUX(27, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

[ 17](rpi-pico-rp2350a-pinctrl_8h.md#a8bf50dbc36c4a534e26159c8a961a18c)#define ADC\_CH2\_P28 RP2XXX\_PINMUX(28, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

[ 18](rpi-pico-rp2350a-pinctrl_8h.md#ad2ab3e2ede7b0c85b17387eddbbc97ed)#define ADC\_CH3\_P29 RP2XXX\_PINMUX(29, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

19

20#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_RP2350A\_PINCTRL\_H\_ \*/

[rpi-pico-rp2350-pinctrl-common.h](rpi-pico-rp2350-pinctrl-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [rpi-pico-rp2350a-pinctrl.h](rpi-pico-rp2350a-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
