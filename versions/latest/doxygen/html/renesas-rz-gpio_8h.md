---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas-rz-gpio_8h.html
original_path: doxygen/html/renesas-rz-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rz-gpio.h File Reference

[Go to the source code of this file.](renesas-rz-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZG3S\_GPIO\_IOLH\_SHIFT](#a50350917566913f95cdc02a843bdbb0f)   7U |
|  | RZ G3S specific GPIO Flags The pin driving ability flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows: |
| #define | [RZG3S\_GPIO\_IOLH\_SET](#ac52f50ae237947ab33ee0490ef7cefa2)(iolh\_val) |
| #define | [RZG3S\_GPIO\_FILTER\_SHIFT](#a0cb876606c6b3540026074f8ebdf12b5)   9U |
| #define | [RZG3S\_GPIO\_FILNUM\_SHIFT](#a8780a0482bc050ad51ba807f2de8bb34)   1U |
| #define | [RZG3S\_GPIO\_FILCLKSEL\_SHIFT](#a203b3330bbf774fa6b892c9d5e2d3421)   3U |
| #define | [RZG3S\_GPIO\_FILTER\_SET](#a618c746bd23b346a7c9edda84e3d75e1)(fillonoff, filnum, filclksel) |

## Macro Definition Documentation

## [◆ ](#a203b3330bbf774fa6b892c9d5e2d3421)RZG3S\_GPIO\_FILCLKSEL\_SHIFT

| #define RZG3S\_GPIO\_FILCLKSEL\_SHIFT   3U |
| --- |

## [◆ ](#a8780a0482bc050ad51ba807f2de8bb34)RZG3S\_GPIO\_FILNUM\_SHIFT

| #define RZG3S\_GPIO\_FILNUM\_SHIFT   1U |
| --- |

## [◆ ](#a618c746bd23b346a7c9edda84e3d75e1)RZG3S\_GPIO\_FILTER\_SET

| #define RZG3S\_GPIO\_FILTER\_SET | ( |  | *fillonoff*, |
| --- | --- | --- | --- |
|  |  |  | *filnum*, |
|  |  |  | *filclksel* ) |

**Value:**

(((fillonoff) | ((filnum) << [RZG3S\_GPIO\_FILNUM\_SHIFT](#a8780a0482bc050ad51ba807f2de8bb34)) | \

((filclksel) << [RZG3S\_GPIO\_FILCLKSEL\_SHIFT](#a203b3330bbf774fa6b892c9d5e2d3421))) \

<< [RZG3S\_GPIO\_FILTER\_SHIFT](#a0cb876606c6b3540026074f8ebdf12b5))

[RZG3S\_GPIO\_FILTER\_SHIFT](#a0cb876606c6b3540026074f8ebdf12b5)

#define RZG3S\_GPIO\_FILTER\_SHIFT

**Definition** renesas-rz-gpio.h:33

[RZG3S\_GPIO\_FILCLKSEL\_SHIFT](#a203b3330bbf774fa6b892c9d5e2d3421)

#define RZG3S\_GPIO\_FILCLKSEL\_SHIFT

**Definition** renesas-rz-gpio.h:35

[RZG3S\_GPIO\_FILNUM\_SHIFT](#a8780a0482bc050ad51ba807f2de8bb34)

#define RZG3S\_GPIO\_FILNUM\_SHIFT

**Definition** renesas-rz-gpio.h:34

## [◆ ](#a0cb876606c6b3540026074f8ebdf12b5)RZG3S\_GPIO\_FILTER\_SHIFT

| #define RZG3S\_GPIO\_FILTER\_SHIFT   9U |
| --- |

## [◆ ](#ac52f50ae237947ab33ee0490ef7cefa2)RZG3S\_GPIO\_IOLH\_SET

| #define RZG3S\_GPIO\_IOLH\_SET | ( |  | *iolh\_val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(iolh\_val << [RZG3S\_GPIO\_IOLH\_SHIFT](#a50350917566913f95cdc02a843bdbb0f))

[RZG3S\_GPIO\_IOLH\_SHIFT](#a50350917566913f95cdc02a843bdbb0f)

#define RZG3S\_GPIO\_IOLH\_SHIFT

RZ G3S specific GPIO Flags The pin driving ability flags are encoded in the 8 upper bits of gpio\_dt\_f...

**Definition** renesas-rz-gpio.h:29

## [◆ ](#a50350917566913f95cdc02a843bdbb0f)RZG3S\_GPIO\_IOLH\_SHIFT

| #define RZG3S\_GPIO\_IOLH\_SHIFT   7U |
| --- |

RZ G3S specific GPIO Flags The pin driving ability flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:

- Bit 9..8: Pin driving ability value
- Bit 11..10: Digital Noise Filter Clock Selection value
- Bit 13..12: Digital Noise Filter Number value
- Bit 14: Digital Noise Filter ON/OFF example: gpio-consumer { out-gpios = <&port8 2 (GPIO\_PULL\_UP | [RZG3S\_GPIO\_FILTER\_SET(1, 3, 3)](#a618c746bd23b346a7c9edda84e3d75e1))>; }; gpio-consumer { out-gpios = <&port8 2 (GPIO\_PULL\_UP | [RZG3S\_GPIO\_IOLH\_SET(2)](#ac52f50ae237947ab33ee0490ef7cefa2))>; };

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [renesas-rz-gpio.h](renesas-rz-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
