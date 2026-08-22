---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas-rza2m-gpio_8h.html
original_path: doxygen/html/renesas-rza2m-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rza2m-gpio.h File Reference

[Go to the source code of this file.](renesas-rza2m-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZA2M\_GPIO\_DRIVE\_NORMAL](#a382c4b325a6e8d1b55175ab528aa1d65)   (0U << 8U) |
|  | RZ/A2M specific GPIO Flags. |
| #define | [RZA2M\_GPIO\_DRIVE\_HIGH](#a18c5f0126b0a08699e6ef7f39cebc034)   (1U << 8U) |
|  | High drive. |

## Macro Definition Documentation

## [◆ ](#a18c5f0126b0a08699e6ef7f39cebc034)RZA2M\_GPIO\_DRIVE\_HIGH

| #define RZA2M\_GPIO\_DRIVE\_HIGH   (1U << 8U) |
| --- |

High drive.

## [◆ ](#a382c4b325a6e8d1b55175ab528aa1d65)RZA2M\_GPIO\_DRIVE\_NORMAL

| #define RZA2M\_GPIO\_DRIVE\_NORMAL   (0U << 8U) |
| --- |

RZ/A2M specific GPIO Flags.

The drive flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:

- Bit 8: Drive strength Normal drive

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [renesas-rza2m-gpio.h](renesas-rza2m-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
