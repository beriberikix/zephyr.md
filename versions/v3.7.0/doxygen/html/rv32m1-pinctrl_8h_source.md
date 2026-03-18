---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rv32m1-pinctrl_8h_source.html
original_path: doxygen/html/rv32m1-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rv32m1-pinctrl.h

[Go to the documentation of this file.](rv32m1-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2022 Henrik Brix Andersen <henrik@brixandersen.dk>

3 \* Copyright (c) 2022 NXP

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_RV32M1\_PINCTRL\_

8#define \_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_RV32M1\_PINCTRL\_

9

[ 17](rv32m1-pinctrl_8h.md#adc4ef31269f0084e7551566b199093df)#define RV32M1\_MUX(port, pin, mux) \

18 (((((port) - 'A') & 0xF) << 28) | \

19 (((pin) & 0x3F) << 22) | \

20 (((mux) & 0x7) << 8))

21

22#endif /\* \_ZEPHYR\_DT\_BINDINGS\_PINCTRL\_RV32M1\_PINCTRL\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [rv32m1-pinctrl.h](rv32m1-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
