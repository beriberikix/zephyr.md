---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas-rztn-gpio_8h.html
original_path: doxygen/html/renesas-rztn-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rztn-gpio.h File Reference

[Go to the source code of this file.](renesas-rztn-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZTN\_GPIO\_DRCTL\_SHIFT](#a398f7ed2fd6c066ab26045493681af0f)   8U |
|  | RZTN specific GPIO Flags The pin driving ability flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows: |
| #define | [RZTN\_GPIO\_SCHMITT\_TRIG\_SHIFT](#a5ab9e01109972081f1979e0c02984629)   4U |
| #define | [RZTN\_GPIO\_SLEW\_RATE\_SHIFT](#a8f596a5b412bc8a744a762e0cfc31b9d)   5U |
| #define | [RZTN\_GPIO\_DRCTL\_SET](#a74666258b9d1c0bc26c00cc30bbfb489)(drive\_ability, schmitt\_trig, slew\_rate) |

## Macro Definition Documentation

## [◆ ](#a74666258b9d1c0bc26c00cc30bbfb489)RZTN\_GPIO\_DRCTL\_SET

| #define RZTN\_GPIO\_DRCTL\_SET | ( |  | *drive\_ability*, |
| --- | --- | --- | --- |
|  |  |  | *schmitt\_trig*, |
|  |  |  | *slew\_rate* ) |

**Value:**

(((drive\_ability) | ((schmitt\_trig) << [RZTN\_GPIO\_SCHMITT\_TRIG\_SHIFT](#a5ab9e01109972081f1979e0c02984629)) | \

((slew\_rate) << [RZTN\_GPIO\_SLEW\_RATE\_SHIFT](#a8f596a5b412bc8a744a762e0cfc31b9d))) \

<< [RZTN\_GPIO\_DRCTL\_SHIFT](#a398f7ed2fd6c066ab26045493681af0f))

[RZTN\_GPIO\_DRCTL\_SHIFT](#a398f7ed2fd6c066ab26045493681af0f)

#define RZTN\_GPIO\_DRCTL\_SHIFT

RZTN specific GPIO Flags The pin driving ability flags are encoded in the 8 upper bits of gpio\_dt\_fla...

**Definition** renesas-rztn-gpio.h:28

[RZTN\_GPIO\_SCHMITT\_TRIG\_SHIFT](#a5ab9e01109972081f1979e0c02984629)

#define RZTN\_GPIO\_SCHMITT\_TRIG\_SHIFT

**Definition** renesas-rztn-gpio.h:29

[RZTN\_GPIO\_SLEW\_RATE\_SHIFT](#a8f596a5b412bc8a744a762e0cfc31b9d)

#define RZTN\_GPIO\_SLEW\_RATE\_SHIFT

**Definition** renesas-rztn-gpio.h:30

## [◆ ](#a398f7ed2fd6c066ab26045493681af0f)RZTN\_GPIO\_DRCTL\_SHIFT

| #define RZTN\_GPIO\_DRCTL\_SHIFT   8U |
| --- |

RZTN specific GPIO Flags The pin driving ability flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:

- Bit 9..8: Driving ability control
- Bit 12: Schmitt trigger control
- Bit 13: Slew rate control Example: Driving ability control: Middle Schmitt trigger control: Enabled Slew rate control: Slow gpio-consumer { out-gpios = <&port8 2 (GPIO\_PULL\_UP | RZTN\_GPIO\_CFG\_SET(1, 1, 0))>; };

## [◆ ](#a5ab9e01109972081f1979e0c02984629)RZTN\_GPIO\_SCHMITT\_TRIG\_SHIFT

| #define RZTN\_GPIO\_SCHMITT\_TRIG\_SHIFT   4U |
| --- |

## [◆ ](#a8f596a5b412bc8a744a762e0cfc31b9d)RZTN\_GPIO\_SLEW\_RATE\_SHIFT

| #define RZTN\_GPIO\_SLEW\_RATE\_SHIFT   5U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [renesas-rztn-gpio.h](renesas-rztn-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
