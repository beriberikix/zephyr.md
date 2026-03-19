---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nxp-s32-gpio_8h.html
original_path: doxygen/html/nxp-s32-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp-s32-gpio.h File Reference

[Go to the source code of this file.](nxp-s32-gpio_8h_source.md)

| Macros | |
| --- | --- |
| NXP S32 GPIO interrupt controller routing flags | |
| NXP S32 GPIO specific flags  The driver flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:   - Bit 8: Interrupt controller to which the respective GPIO interrupt is routed.   NXP S32 GPIO interrupt controller routing flags | |
| #define | [NXP\_S32\_GPIO\_INT\_WKPU](#a2e1b254b390cdd2ca038ff4e930680f5)   (0x1U << NXP\_S32\_GPIO\_INT\_CONTROLLER\_POS) |
|  | Interrupt routed to the WKPU controller. |

## Macro Definition Documentation

## [◆ ](#a2e1b254b390cdd2ca038ff4e930680f5)NXP\_S32\_GPIO\_INT\_WKPU

| #define NXP\_S32\_GPIO\_INT\_WKPU   (0x1U << NXP\_S32\_GPIO\_INT\_CONTROLLER\_POS) |
| --- |

Interrupt routed to the WKPU controller.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [nxp-s32-gpio.h](nxp-s32-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
