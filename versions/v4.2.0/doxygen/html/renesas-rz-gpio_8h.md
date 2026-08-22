---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas-rz-gpio_8h.html
original_path: doxygen/html/renesas-rz-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rz-gpio.h File Reference

[Go to the source code of this file.](renesas-rz-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZ\_GPIO\_IOLH\_SHIFT](#afacb3123f587a2129cd1ed472ce2b3e5)   8U |
|  | RZ/A,G,V-specific GPIO Flags The pin driving ability flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows: |
| #define | [RZ\_GPIO\_IOLH\_SET](#a6916bb2358989ef5498e1c87209dd995)(iolh\_val) |
| #define | [RZ\_GPIO\_FILTER\_SHIFT](#aa309713f69b69a9650496f6238380c6d)   10U |
| #define | [RZ\_GPIO\_FILNUM\_SHIFT](#a1f1f1a0433c86dc7f50b368bd258a107)   1U |
| #define | [RZ\_GPIO\_FILCLKSEL\_SHIFT](#abcdbf6cf77765df961496a3698f9102d)   3U |
| #define | [RZ\_GPIO\_FILTER\_SET](#aa905a388dc0ca8b9c532620be7029b8e)(fillonoff, filnum, filclksel) |

## Macro Definition Documentation

## [◆ ](#abcdbf6cf77765df961496a3698f9102d)RZ\_GPIO\_FILCLKSEL\_SHIFT

| #define RZ\_GPIO\_FILCLKSEL\_SHIFT   3U |
| --- |

## [◆ ](#a1f1f1a0433c86dc7f50b368bd258a107)RZ\_GPIO\_FILNUM\_SHIFT

| #define RZ\_GPIO\_FILNUM\_SHIFT   1U |
| --- |

## [◆ ](#aa905a388dc0ca8b9c532620be7029b8e)RZ\_GPIO\_FILTER\_SET

| #define RZ\_GPIO\_FILTER\_SET | ( |  | *fillonoff*, |
| --- | --- | --- | --- |
|  |  |  | *filnum*, |
|  |  |  | *filclksel* ) |

**Value:**

(((fillonoff) | ((filnum) << [RZ\_GPIO\_FILNUM\_SHIFT](#a1f1f1a0433c86dc7f50b368bd258a107)) | \

((filclksel) << [RZ\_GPIO\_FILCLKSEL\_SHIFT](#abcdbf6cf77765df961496a3698f9102d))) \

<< [RZ\_GPIO\_FILTER\_SHIFT](#aa309713f69b69a9650496f6238380c6d))

[RZ\_GPIO\_FILNUM\_SHIFT](#a1f1f1a0433c86dc7f50b368bd258a107)

#define RZ\_GPIO\_FILNUM\_SHIFT

**Definition** renesas-rz-gpio.h:34

[RZ\_GPIO\_FILTER\_SHIFT](#aa309713f69b69a9650496f6238380c6d)

#define RZ\_GPIO\_FILTER\_SHIFT

**Definition** renesas-rz-gpio.h:33

[RZ\_GPIO\_FILCLKSEL\_SHIFT](#abcdbf6cf77765df961496a3698f9102d)

#define RZ\_GPIO\_FILCLKSEL\_SHIFT

**Definition** renesas-rz-gpio.h:35

## [◆ ](#aa309713f69b69a9650496f6238380c6d)RZ\_GPIO\_FILTER\_SHIFT

| #define RZ\_GPIO\_FILTER\_SHIFT   10U |
| --- |

## [◆ ](#a6916bb2358989ef5498e1c87209dd995)RZ\_GPIO\_IOLH\_SET

| #define RZ\_GPIO\_IOLH\_SET | ( |  | *iolh\_val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(iolh\_val << [RZ\_GPIO\_IOLH\_SHIFT](#afacb3123f587a2129cd1ed472ce2b3e5))

[RZ\_GPIO\_IOLH\_SHIFT](#afacb3123f587a2129cd1ed472ce2b3e5)

#define RZ\_GPIO\_IOLH\_SHIFT

RZ/A,G,V-specific GPIO Flags The pin driving ability flags are encoded in the 8 upper bits of gpio\_dt...

**Definition** renesas-rz-gpio.h:29

## [◆ ](#afacb3123f587a2129cd1ed472ce2b3e5)RZ\_GPIO\_IOLH\_SHIFT

| #define RZ\_GPIO\_IOLH\_SHIFT   8U |
| --- |

RZ/A,G,V-specific GPIO Flags The pin driving ability flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:

- Bit 8..9: Pin driving ability value
- Bit 10: Digital Noise Filter ON/OFF
- Bit 11..12: Digital Noise Filter Number value
- Bit 13..14: Digital Noise Filter Clock Selection value example: gpio-consumer { out-gpios = <&port8 2 (GPIO\_PULL\_UP | [RZ\_GPIO\_FILTER\_SET(1, 3, 3)](#aa905a388dc0ca8b9c532620be7029b8e))>; }; gpio-consumer { out-gpios = <&port8 2 (GPIO\_PULL\_UP | [RZ\_GPIO\_IOLH\_SET(2)](#a6916bb2358989ef5498e1c87209dd995))>; };

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [renesas-rz-gpio.h](renesas-rz-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
