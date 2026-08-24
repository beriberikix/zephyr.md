---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mspm0-pinctrl_8h_source.html
original_path: doxygen/html/mspm0-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspm0-pinctrl.h

[Go to the documentation of this file.](mspm0-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2025 Texas Instruments

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_MSPM0\_DT\_BINDINGS\_PINCTRL\_H\_

8#define \_MSPM0\_DT\_BINDINGS\_PINCTRL\_H\_

9

[ 10](mspm0-pinctrl_8h.md#a7bc7b96a754e425dd773b864eb0181be)#define MSP\_PORT\_INDEX\_BY\_NAME(x) ((x == "PORTA") ? 0 : 1)

11

[ 12](mspm0-pinctrl_8h.md#aed042e160fbf0499081e08f32b485ccc)#define MSPM0\_PIN\_FUNCTION\_ANALOG (0x00000000)

[ 13](mspm0-pinctrl_8h.md#aafceb12e339618d1282aa7300507d9a5)#define MSPM0\_PIN\_FUNCTION\_GPIO (0x00000001)

[ 14](mspm0-pinctrl_8h.md#a2d119d2da878acd9ebac10c6d0cc7c80)#define MSPM0\_PIN\_FUNCTION\_2 (0x00000002)

[ 15](mspm0-pinctrl_8h.md#a4cdd8ded8a55c33f3b586152d64b2621)#define MSPM0\_PIN\_FUNCTION\_3 (0x00000003)

[ 16](mspm0-pinctrl_8h.md#a897c32ff405a8c4eeaaffed7a6c69d5a)#define MSPM0\_PIN\_FUNCTION\_4 (0x00000004)

[ 17](mspm0-pinctrl_8h.md#ab6ec2101ebc8d171852da5c72a9e6ff1)#define MSPM0\_PIN\_FUNCTION\_5 (0x00000005)

[ 18](mspm0-pinctrl_8h.md#a4891b06c78d726a4806ea7f8c18d2bbc)#define MSPM0\_PIN\_FUNCTION\_6 (0x00000006)

[ 19](mspm0-pinctrl_8h.md#af2b0ea70556adb258d70cbb7274dce12)#define MSPM0\_PIN\_FUNCTION\_7 (0x00000007)

[ 20](mspm0-pinctrl_8h.md#a250cc53f70b280ed5a909f5b968f2c0b)#define MSPM0\_PIN\_FUNCTION\_8 (0x00000008)

[ 21](mspm0-pinctrl_8h.md#affb9f84a279ac6ec00f153d024282b05)#define MSPM0\_PIN\_FUNCTION\_9 (0x00000009)

[ 22](mspm0-pinctrl_8h.md#a974860da2ed7b0ad8835edf35fc3fa71)#define MSPM0\_PIN\_FUNCTION\_10 (0x0000000A)

23

24/\* Creates a concatenation of the correct pin function based on the pin control

25 \* management register offset and the function suffix.

26 \*/

[ 27](mspm0-pinctrl_8h.md#a6d8c1db9082542af49cc37dce3d02720)#define MSP\_PINMUX(pincm, function) (((pincm - 1) << 0x10) | function)

28

29#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [mspm0-pinctrl.h](mspm0-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
