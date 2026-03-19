---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32-gpio_8h_source.html
original_path: doxygen/html/stm32-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32-gpio.h

[Go to the documentation of this file.](stm32-gpio_8h.md)

1/\*

2 \* Copyright (c) 2024 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_STM32\_GPIO\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_STM32\_GPIO\_H\_

9

22

[ 28](group__gpio__interface.md#ga9a05f736e9ee915f591a65a7f6d382d3)#define STM32\_GPIO\_WKUP (1 << 8)

29

31#define STM32\_GPIO\_SPEED\_SHIFT 9

32#define STM32\_GPIO\_SPEED\_MASK 0x3

34

[ 36](group__gpio__interface.md#gaa8d19f48bfea73193ff35c06a6894df6)#define STM32\_GPIO\_LOW\_SPEED (0x0 << STM32\_GPIO\_SPEED\_SHIFT)

37

[ 39](group__gpio__interface.md#gaee4f9eb7cb958d4a55d13029658bdff3)#define STM32\_GPIO\_MEDIUM\_SPEED (0x1 << STM32\_GPIO\_SPEED\_SHIFT)

40

[ 42](group__gpio__interface.md#gac91d2b48bc764131896ebb3b0436dac1)#define STM32\_GPIO\_HIGH\_SPEED (0x2 << STM32\_GPIO\_SPEED\_SHIFT)

43

[ 45](group__gpio__interface.md#gaeff690b8406b0ed24f97bbe8ab4bf31e)#define STM32\_GPIO\_VERY\_HIGH\_SPEED (0x3 << STM32\_GPIO\_SPEED\_SHIFT)

46

48

49#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_STM32\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [stm32-gpio.h](stm32-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
