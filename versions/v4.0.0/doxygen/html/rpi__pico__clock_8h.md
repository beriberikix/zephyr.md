---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/rpi__pico__clock_8h.html
original_path: doxygen/html/rpi__pico__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi\_pico\_clock.h File Reference

[Go to the source code of this file.](rpi__pico__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RPI\_PICO\_PLL\_SYS](#a466e4913a0890f6d06decf7fe912a8d6)   0 |
| #define | [RPI\_PICO\_PLL\_USB](#a32863224d85037e237d6ba1d6f526349)   1 |
| #define | [RPI\_PICO\_PLL\_COUNT](#ac641d50669b0c5a5932ba47754f997f2)   2 |
| #define | [RPI\_PICO\_GPIN\_0](#ac64aeeb93c3df085cdba8088c7e71643)   0 |
| #define | [RPI\_PICO\_GPIN\_1](#a6f6f6655d1e43da01b19f676da7eba9f)   1 |
| #define | [RPI\_PICO\_GPIN\_COUNT](#a0c1f6d136e18501a33806da47b4fbd74)   2 |
| #define | [RPI\_PICO\_CLKID\_CLK\_GPOUT0](#ad69d8a2bad53c6d014daaf080459785f)   0 |
| #define | [RPI\_PICO\_CLKID\_CLK\_GPOUT1](#a4ff53626cd36bd222c4fd03fa2a1cd7c)   1 |
| #define | [RPI\_PICO\_CLKID\_CLK\_GPOUT2](#ad56ce5dde45a27c349e97060fe81b877)   2 |
| #define | [RPI\_PICO\_CLKID\_CLK\_GPOUT3](#adc9f3183caef9040a3e217b8ad373aa4)   3 |
| #define | [RPI\_PICO\_CLKID\_CLK\_REF](#a3209f2d463248e9eaecf91bfad06221c)   4 |
| #define | [RPI\_PICO\_CLKID\_CLK\_SYS](#aa6925acbb797026caccb78c0bb0c64c5)   5 |
| #define | [RPI\_PICO\_CLKID\_CLK\_PERI](#aa0e2c91d4ad02985c075c9206d1be314)   6 |
| #define | [RPI\_PICO\_CLKID\_CLK\_USB](#a791f267cb9b1fc36e024dd7c0d72b9c5)   7 |
| #define | [RPI\_PICO\_CLKID\_CLK\_ADC](#a34360769303719d99776e50019050d5f)   8 |
| #define | [RPI\_PICO\_CLKID\_CLK\_RTC](#a54693a90319dedf8a7c7c0bad0f087e7)   9 |
| #define | [RPI\_PICO\_CLKID\_PLL\_SYS](#afa64692c1c8e8c28970fd9c88a8a1adf)   10 |
| #define | [RPI\_PICO\_CLKID\_PLL\_USB](#aec02ce9014d772f07ba4e25d825e61a0)   11 |
| #define | [RPI\_PICO\_CLKID\_XOSC](#ace2c7bd1defff7594766ad67416ed524)   12 |
| #define | [RPI\_PICO\_CLKID\_ROSC](#a942f1316a463d6a10d4edf88176915f2)   13 |
| #define | [RPI\_PICO\_CLKID\_ROSC\_PH](#af74becbd25d5e91d0034236b30c13b73)   14 |
| #define | [RPI\_PICO\_CLKID\_GPIN0](#a5da8c9643f9505364e73f1ea44555939)   15 |
| #define | [RPI\_PICO\_CLKID\_GPIN1](#a668080f8aaa30b302a2eb92c11320533)   16 |
| #define | [RPI\_PICO\_ROSC\_RANGE\_RESET](#a4b34aea0ef551dbdc54a321ebb891866)   0xAA0 |
| #define | [RPI\_PICO\_ROSC\_RANGE\_LOW](#ac095e9944a07e06b48bc2bce646afac1)   0xFA4 |
| #define | [RPI\_PICO\_ROSC\_RANGE\_MEDIUM](#afeca2ad3fbf43ff038e7d8b334de8217)   0xFA5 |
| #define | [RPI\_PICO\_ROSC\_RANGE\_HIGH](#a109f4ccc6aca6fc3fdf31be5817e779c)   0xFA7 |
| #define | [RPI\_PICO\_ROSC\_RANGE\_TOOHIGH](#ab8e87bc64fecf6db1ff6124be82b9120)   0xFA6 |
| #define | [RPI\_PICO\_CLOCK\_COUNT](#a610d24203e8b6b6d69a37ee38c26b2d2)   10 |

## Macro Definition Documentation

## [◆ ](#a34360769303719d99776e50019050d5f)RPI\_PICO\_CLKID\_CLK\_ADC

| #define RPI\_PICO\_CLKID\_CLK\_ADC   8 |
| --- |

## [◆ ](#ad69d8a2bad53c6d014daaf080459785f)RPI\_PICO\_CLKID\_CLK\_GPOUT0

| #define RPI\_PICO\_CLKID\_CLK\_GPOUT0   0 |
| --- |

## [◆ ](#a4ff53626cd36bd222c4fd03fa2a1cd7c)RPI\_PICO\_CLKID\_CLK\_GPOUT1

| #define RPI\_PICO\_CLKID\_CLK\_GPOUT1   1 |
| --- |

## [◆ ](#ad56ce5dde45a27c349e97060fe81b877)RPI\_PICO\_CLKID\_CLK\_GPOUT2

| #define RPI\_PICO\_CLKID\_CLK\_GPOUT2   2 |
| --- |

## [◆ ](#adc9f3183caef9040a3e217b8ad373aa4)RPI\_PICO\_CLKID\_CLK\_GPOUT3

| #define RPI\_PICO\_CLKID\_CLK\_GPOUT3   3 |
| --- |

## [◆ ](#aa0e2c91d4ad02985c075c9206d1be314)RPI\_PICO\_CLKID\_CLK\_PERI

| #define RPI\_PICO\_CLKID\_CLK\_PERI   6 |
| --- |

## [◆ ](#a3209f2d463248e9eaecf91bfad06221c)RPI\_PICO\_CLKID\_CLK\_REF

| #define RPI\_PICO\_CLKID\_CLK\_REF   4 |
| --- |

## [◆ ](#a54693a90319dedf8a7c7c0bad0f087e7)RPI\_PICO\_CLKID\_CLK\_RTC

| #define RPI\_PICO\_CLKID\_CLK\_RTC   9 |
| --- |

## [◆ ](#aa6925acbb797026caccb78c0bb0c64c5)RPI\_PICO\_CLKID\_CLK\_SYS

| #define RPI\_PICO\_CLKID\_CLK\_SYS   5 |
| --- |

## [◆ ](#a791f267cb9b1fc36e024dd7c0d72b9c5)RPI\_PICO\_CLKID\_CLK\_USB

| #define RPI\_PICO\_CLKID\_CLK\_USB   7 |
| --- |

## [◆ ](#a5da8c9643f9505364e73f1ea44555939)RPI\_PICO\_CLKID\_GPIN0

| #define RPI\_PICO\_CLKID\_GPIN0   15 |
| --- |

## [◆ ](#a668080f8aaa30b302a2eb92c11320533)RPI\_PICO\_CLKID\_GPIN1

| #define RPI\_PICO\_CLKID\_GPIN1   16 |
| --- |

## [◆ ](#afa64692c1c8e8c28970fd9c88a8a1adf)RPI\_PICO\_CLKID\_PLL\_SYS

| #define RPI\_PICO\_CLKID\_PLL\_SYS   10 |
| --- |

## [◆ ](#aec02ce9014d772f07ba4e25d825e61a0)RPI\_PICO\_CLKID\_PLL\_USB

| #define RPI\_PICO\_CLKID\_PLL\_USB   11 |
| --- |

## [◆ ](#a942f1316a463d6a10d4edf88176915f2)RPI\_PICO\_CLKID\_ROSC

| #define RPI\_PICO\_CLKID\_ROSC   13 |
| --- |

## [◆ ](#af74becbd25d5e91d0034236b30c13b73)RPI\_PICO\_CLKID\_ROSC\_PH

| #define RPI\_PICO\_CLKID\_ROSC\_PH   14 |
| --- |

## [◆ ](#ace2c7bd1defff7594766ad67416ed524)RPI\_PICO\_CLKID\_XOSC

| #define RPI\_PICO\_CLKID\_XOSC   12 |
| --- |

## [◆ ](#a610d24203e8b6b6d69a37ee38c26b2d2)RPI\_PICO\_CLOCK\_COUNT

| #define RPI\_PICO\_CLOCK\_COUNT   10 |
| --- |

## [◆ ](#ac64aeeb93c3df085cdba8088c7e71643)RPI\_PICO\_GPIN\_0

| #define RPI\_PICO\_GPIN\_0   0 |
| --- |

## [◆ ](#a6f6f6655d1e43da01b19f676da7eba9f)RPI\_PICO\_GPIN\_1

| #define RPI\_PICO\_GPIN\_1   1 |
| --- |

## [◆ ](#a0c1f6d136e18501a33806da47b4fbd74)RPI\_PICO\_GPIN\_COUNT

| #define RPI\_PICO\_GPIN\_COUNT   2 |
| --- |

## [◆ ](#ac641d50669b0c5a5932ba47754f997f2)RPI\_PICO\_PLL\_COUNT

| #define RPI\_PICO\_PLL\_COUNT   2 |
| --- |

## [◆ ](#a466e4913a0890f6d06decf7fe912a8d6)RPI\_PICO\_PLL\_SYS

| #define RPI\_PICO\_PLL\_SYS   0 |
| --- |

## [◆ ](#a32863224d85037e237d6ba1d6f526349)RPI\_PICO\_PLL\_USB

| #define RPI\_PICO\_PLL\_USB   1 |
| --- |

## [◆ ](#a109f4ccc6aca6fc3fdf31be5817e779c)RPI\_PICO\_ROSC\_RANGE\_HIGH

| #define RPI\_PICO\_ROSC\_RANGE\_HIGH   0xFA7 |
| --- |

## [◆ ](#ac095e9944a07e06b48bc2bce646afac1)RPI\_PICO\_ROSC\_RANGE\_LOW

| #define RPI\_PICO\_ROSC\_RANGE\_LOW   0xFA4 |
| --- |

## [◆ ](#afeca2ad3fbf43ff038e7d8b334de8217)RPI\_PICO\_ROSC\_RANGE\_MEDIUM

| #define RPI\_PICO\_ROSC\_RANGE\_MEDIUM   0xFA5 |
| --- |

## [◆ ](#a4b34aea0ef551dbdc54a321ebb891866)RPI\_PICO\_ROSC\_RANGE\_RESET

| #define RPI\_PICO\_ROSC\_RANGE\_RESET   0xAA0 |
| --- |

## [◆ ](#ab8e87bc64fecf6db1ff6124be82b9120)RPI\_PICO\_ROSC\_RANGE\_TOOHIGH

| #define RPI\_PICO\_ROSC\_RANGE\_TOOHIGH   0xFA6 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [rpi\_pico\_clock.h](rpi__pico__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
