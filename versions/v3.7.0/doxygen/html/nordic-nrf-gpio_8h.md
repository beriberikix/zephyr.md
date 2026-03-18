---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nordic-nrf-gpio_8h.html
original_path: doxygen/html/nordic-nrf-gpio_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nordic-nrf-gpio.h File Reference

[Go to the source code of this file.](nordic-nrf-gpio_8h_source.md)

| Macros | |
| --- | --- |
| nRF GPIO drive flags | |
| nRF GPIO drive flags  Standard (S) or High (H) drive modes can be applied to both pin levels, 0 or   1. High drive mode will increase current capabilities of the pin (refer to each SoC reference manual).   When the pin is configured to operate in open-drain mode (wired-and), the drive mode can only be selected for the 0 level (1 is disconnected). Similarly, when the pin is configured to operate in open-source mode (wired-or), the drive mode can only be set for the 1 level (0 is disconnected).  The drive flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:   - Bit 8: Drive mode for '0' (0=Standard, 1=High) - Bit 9: Drive mode for '1' (0=Standard, 1=High) | |
| #define | [NRF\_GPIO\_DRIVE\_S0](group__gpio__interface__nrf.md#ga00ce8b0f371e41899b0379adc4647036)   (0U << 8U) |
|  | Standard drive for '0' (default, used with GPIO\_OPEN\_DRAIN). |
| #define | [NRF\_GPIO\_DRIVE\_H0](group__gpio__interface__nrf.md#gaa21a50e68b9018384dc7b409673cd047)   (1U << 8U) |
|  | High drive for '0' (used with GPIO\_OPEN\_DRAIN). |
| #define | [NRF\_GPIO\_DRIVE\_S1](group__gpio__interface__nrf.md#ga5909d23af54ccd8bea797e0f74871cb3)   (0U << 9U) |
|  | Standard drive for '1' (default, used with GPIO\_OPEN\_SOURCE). |
| #define | [NRF\_GPIO\_DRIVE\_H1](group__gpio__interface__nrf.md#ga8adac513c62dfc12b9f4d7272d73a99f)   (1U << 9U) |
|  | High drive for '1' (used with GPIO\_OPEN\_SOURCE). |
| #define | [NRF\_GPIO\_DRIVE\_S0S1](group__gpio__interface__nrf.md#ga0b03a6717cc2e5d57aba54379188a884)   ([NRF\_GPIO\_DRIVE\_S0](group__gpio__interface__nrf.md#ga00ce8b0f371e41899b0379adc4647036) | [NRF\_GPIO\_DRIVE\_S1](group__gpio__interface__nrf.md#ga5909d23af54ccd8bea797e0f74871cb3)) |
|  | Standard drive for '0' and '1' (default). |
| #define | [NRF\_GPIO\_DRIVE\_S0H1](group__gpio__interface__nrf.md#ga43697400db8d8cba4dd4bbaaae59a551)   ([NRF\_GPIO\_DRIVE\_S0](group__gpio__interface__nrf.md#ga00ce8b0f371e41899b0379adc4647036) | [NRF\_GPIO\_DRIVE\_H1](group__gpio__interface__nrf.md#ga8adac513c62dfc12b9f4d7272d73a99f)) |
|  | Standard drive for '0' and high for '1'. |
| #define | [NRF\_GPIO\_DRIVE\_H0S1](group__gpio__interface__nrf.md#ga4426bd906d7e2965f53e21a246ec0bbc)   ([NRF\_GPIO\_DRIVE\_H0](group__gpio__interface__nrf.md#gaa21a50e68b9018384dc7b409673cd047) | [NRF\_GPIO\_DRIVE\_S1](group__gpio__interface__nrf.md#ga5909d23af54ccd8bea797e0f74871cb3)) |
|  | High drive for '0' and standard for '1'. |
| #define | [NRF\_GPIO\_DRIVE\_H0H1](group__gpio__interface__nrf.md#ga905a8813a86d8cf1087a47eadc089987)   ([NRF\_GPIO\_DRIVE\_H0](group__gpio__interface__nrf.md#gaa21a50e68b9018384dc7b409673cd047) | [NRF\_GPIO\_DRIVE\_H1](group__gpio__interface__nrf.md#ga8adac513c62dfc12b9f4d7272d73a99f)) |
|  | High drive for '0' and '1'. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nordic-nrf-gpio.h](nordic-nrf-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
