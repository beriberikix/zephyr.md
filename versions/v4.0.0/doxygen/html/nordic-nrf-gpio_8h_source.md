---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nordic-nrf-gpio_8h_source.html
original_path: doxygen/html/nordic-nrf-gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nordic-nrf-gpio.h

[Go to the documentation of this file.](nordic-nrf-gpio_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NRF\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NRF\_GPIO\_H\_

8

15

38

41#define NRF\_GPIO\_DRIVE\_MSK 0x0300U

43

[ 45](group__gpio__interface__nrf.md#ga00ce8b0f371e41899b0379adc4647036)#define NRF\_GPIO\_DRIVE\_S0 (0U << 8U)

[ 47](group__gpio__interface__nrf.md#gaa21a50e68b9018384dc7b409673cd047)#define NRF\_GPIO\_DRIVE\_H0 (1U << 8U)

[ 49](group__gpio__interface__nrf.md#ga5909d23af54ccd8bea797e0f74871cb3)#define NRF\_GPIO\_DRIVE\_S1 (0U << 9U)

[ 51](group__gpio__interface__nrf.md#ga8adac513c62dfc12b9f4d7272d73a99f)#define NRF\_GPIO\_DRIVE\_H1 (1U << 9U)

[ 53](group__gpio__interface__nrf.md#ga0b03a6717cc2e5d57aba54379188a884)#define NRF\_GPIO\_DRIVE\_S0S1 (NRF\_GPIO\_DRIVE\_S0 | NRF\_GPIO\_DRIVE\_S1)

[ 55](group__gpio__interface__nrf.md#ga43697400db8d8cba4dd4bbaaae59a551)#define NRF\_GPIO\_DRIVE\_S0H1 (NRF\_GPIO\_DRIVE\_S0 | NRF\_GPIO\_DRIVE\_H1)

[ 57](group__gpio__interface__nrf.md#ga4426bd906d7e2965f53e21a246ec0bbc)#define NRF\_GPIO\_DRIVE\_H0S1 (NRF\_GPIO\_DRIVE\_H0 | NRF\_GPIO\_DRIVE\_S1)

[ 59](group__gpio__interface__nrf.md#ga905a8813a86d8cf1087a47eadc089987)#define NRF\_GPIO\_DRIVE\_H0H1 (NRF\_GPIO\_DRIVE\_H0 | NRF\_GPIO\_DRIVE\_H1)

60

62

64

65#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_NORDIC\_NRF\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nordic-nrf-gpio.h](nordic-nrf-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
