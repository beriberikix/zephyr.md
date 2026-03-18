---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/adc_2gd32f3x0_8h_source.html
original_path: doxygen/html/adc_2gd32f3x0_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32f3x0.h

[Go to the documentation of this file.](adc_2gd32f3x0_8h.md)

1/\*

2 \* Copyright 2022 BrainCo Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_GD32F3X0\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_GD32F3X0\_H\_

8

9/\*

10 \* ADC clock and prescaler definition refer from rcu\_adc\_clock\_enum which

11 \* defined at GD32F3X0 RCU HAL.

12 \*/

[ 13](adc_2gd32f3x0_8h.md#a1cf9783335d0fdeacb1f1b59c98c8a84)#define GD32\_RCU\_ADCCK\_IRC28M\_DIV2 0

[ 14](adc_2gd32f3x0_8h.md#a43f5922d4cd744f19656417d1e5eaf95)#define GD32\_RCU\_ADCCK\_IRC28M 1

[ 15](adc_2gd32f3x0_8h.md#aa606e7561c9640ea5492e1a62c36b8df)#define GD32\_RCU\_ADCCK\_APB2\_DIV2 2

[ 16](adc_2gd32f3x0_8h.md#a07f10a1e5dbe5c36b33d0a795459ef5b)#define GD32\_RCU\_ADCCK\_AHB\_DIV3 3

[ 17](adc_2gd32f3x0_8h.md#a91d2211d1b8f39f3c6d9d9f0920b91e9)#define GD32\_RCU\_ADCCK\_APB2\_DIV4 4

[ 18](adc_2gd32f3x0_8h.md#aa816f5c64beb8882aeaf466fe50ae5a6)#define GD32\_RCU\_ADCCK\_AHB\_DIV5 5

[ 19](adc_2gd32f3x0_8h.md#aeb7f63a54bca06853c5217d7951cf77d)#define GD32\_RCU\_ADCCK\_APB2\_DIV6 6

[ 20](adc_2gd32f3x0_8h.md#a1bd584741364be703bfc4f9535cc7bcc)#define GD32\_RCU\_ADCCK\_AHB\_DIV7 7

[ 21](adc_2gd32f3x0_8h.md#a5445e6ca3a57c0b2a8175cc4bd229a44)#define GD32\_RCU\_ADCCK\_APB2\_DIV8 8

[ 22](adc_2gd32f3x0_8h.md#af9c5c3db7389513415fd1a7adc7a2209)#define GD32\_RCU\_ADCCK\_AHB\_DIV9 9

23

24#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_GD32F3X0\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [gd32f3x0.h](adc_2gd32f3x0_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
