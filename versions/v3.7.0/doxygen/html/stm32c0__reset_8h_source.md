---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32c0__reset_8h_source.html
original_path: doxygen/html/stm32c0__reset_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32c0\_reset.h

[Go to the documentation of this file.](stm32c0__reset_8h.md)

1/\*

2 \* Copyright (c) 2022 Google Inc

3 \* Copyright (c) Benjamin Björnsson <benjamin.bjornsson@gmail.com>

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32C0\_RESET\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32C0\_RESET\_H\_

10

11#include "[stm32-common.h](stm32-common_8h.md)"

12

13/\* RCC bus reset register offset \*/

[ 14](stm32c0__reset_8h.md#ab41182491ee4576bdff3bc2b8c4d1271)#define STM32\_RESET\_BUS\_IOP 0x24

[ 15](stm32c0__reset_8h.md#a3a527d4f03ed172cd0217eeb28ca5670)#define STM32\_RESET\_BUS\_AHB1 0x28

[ 16](stm32c0__reset_8h.md#af6147c04f9dc0679c14f750afbfdeb17)#define STM32\_RESET\_BUS\_APB1L 0x2C

[ 17](stm32c0__reset_8h.md#a74bf429a826fb31d5d5623a2358e9062)#define STM32\_RESET\_BUS\_APB1H 0x30

18

19#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32C0\_RESET\_H\_ \*/

[stm32-common.h](stm32-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32c0\_reset.h](stm32c0__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
