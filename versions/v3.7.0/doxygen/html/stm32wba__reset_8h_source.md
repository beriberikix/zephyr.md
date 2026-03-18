---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32wba__reset_8h_source.html
original_path: doxygen/html/stm32wba__reset_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32wba\_reset.h

[Go to the documentation of this file.](stm32wba__reset_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32WBA\_RESET\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32WBA\_RESET\_H\_

9

10#include "[stm32-common.h](stm32-common_8h.md)"

11

12/\* RCC bus reset register offset \*/

[ 13](stm32wba__reset_8h.md#a3a527d4f03ed172cd0217eeb28ca5670)#define STM32\_RESET\_BUS\_AHB1 0x60

[ 14](stm32wba__reset_8h.md#a0abdd5105ad8f47103e5905294bc503e)#define STM32\_RESET\_BUS\_AHB2 0x64

[ 15](stm32wba__reset_8h.md#ab3c50488687aae8e2e1deb2624f5221c)#define STM32\_RESET\_BUS\_AHB4 0x6C

[ 16](stm32wba__reset_8h.md#a46ea9f7abcdf8026c74ffc5afb842819)#define STM32\_RESET\_BUS\_AHB5 0x70

[ 17](stm32wba__reset_8h.md#af6147c04f9dc0679c14f750afbfdeb17)#define STM32\_RESET\_BUS\_APB1L 0x74

[ 18](stm32wba__reset_8h.md#a74bf429a826fb31d5d5623a2358e9062)#define STM32\_RESET\_BUS\_APB1H 0x78

[ 19](stm32wba__reset_8h.md#adb41bde903446da14725436f08119509)#define STM32\_RESET\_BUS\_APB2 0x7C

[ 20](stm32wba__reset_8h.md#a4badc13a5b56e220326ad22d9a60b583)#define STM32\_RESET\_BUS\_APB7 0x80

21

22#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_STM32WBA\_RESET\_H\_ \*/

[stm32-common.h](stm32-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [stm32wba\_reset.h](stm32wba__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
