---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/renesas-rzt2m-gpio_8h.html
original_path: doxygen/html/renesas-rzt2m-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-rzt2m-gpio.h File Reference

`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](renesas-rzt2m-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)   8 |
| #define | [RZT2M\_GPIO\_DRIVE\_MASK](#a16ed0517a7b43d606ea0849ebb2d96a7)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)([RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f) + 2, [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)) |
| #define | [RZT2M\_GPIO\_DRIVE\_LOW](#a0e2542438d2c829d6509399314a01682)   (0U << [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)) |
|  | Select GPIO pin drive strength. |
| #define | [RZT2M\_GPIO\_DRIVE\_MIDDLE](#a683f1d1fc91e508793141734caaef335)   (1U << [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)) |
| #define | [RZT2M\_GPIO\_DRIVE\_HIGH](#a814748063a20fe7d971e19d6e296eb59)   (2U << [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)) |
| #define | [RZT2M\_GPIO\_DRIVE\_ULTRA\_HIGH](#a2b60d89adec85b941aa8d7963233aafb)   (3U << [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)) |
| #define | [RZT2M\_GPIO\_SCHMITT\_TRIGGER\_OFFSET](#a0536626285ce7ba19c1a8baf57365902)   10 |
| #define | [RZT2M\_GPIO\_SCHMITT\_TRIGGER\_MASK](#a5650f1078ef92c15174bf2ce8c7e6f08)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([RZT2M\_GPIO\_SCHMITT\_TRIGGER\_OFFSET](#a0536626285ce7ba19c1a8baf57365902)) |
| #define | [RZT2M\_GPIO\_SCHMITT\_TRIGGER](#ac2d2e1cef0fa53eb0ce6f7dcb32cb4ef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([RZT2M\_GPIO\_SCHMITT\_TRIGGER\_OFFSET](#a0536626285ce7ba19c1a8baf57365902)) |
|  | Enable GPIO pin schmitt trigger. |
| #define | [RZT2M\_GPIO\_SLEW\_RATE\_OFFSET](#a4f3e3fb225e921d3405c189b87980a16)   11 |
| #define | [RZT2M\_GPIO\_SLEW\_RATE\_MASK](#a595d6e02f3fd2168deb2fe06f6d00f7d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([RZT2M\_GPIO\_SLEW\_RATE\_OFFSET](#a4f3e3fb225e921d3405c189b87980a16)) |
| #define | [RZT2M\_GPIO\_SLEW\_RATE\_SLOW](#a2f754f8752b7c42ee89286725b2be4bb)   0U |
|  | Select GPIO pin slew rate. |
| #define | [RZT2M\_GPIO\_SLEW\_RATE\_FAST](#a752db650514faa34a43bf14a70746dac)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([RZT2M\_GPIO\_SLEW\_RATE\_OFFSET](#a4f3e3fb225e921d3405c189b87980a16)) |

## Macro Definition Documentation

## [◆ ](#a814748063a20fe7d971e19d6e296eb59)RZT2M\_GPIO\_DRIVE\_HIGH

| #define RZT2M\_GPIO\_DRIVE\_HIGH   (2U << [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)) |
| --- |

## [◆ ](#a0e2542438d2c829d6509399314a01682)RZT2M\_GPIO\_DRIVE\_LOW

| #define RZT2M\_GPIO\_DRIVE\_LOW   (0U << [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)) |
| --- |

Select GPIO pin drive strength.

## [◆ ](#a16ed0517a7b43d606ea0849ebb2d96a7)RZT2M\_GPIO\_DRIVE\_MASK

| #define RZT2M\_GPIO\_DRIVE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)([RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f) + 2, [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)) |
| --- |

## [◆ ](#a683f1d1fc91e508793141734caaef335)RZT2M\_GPIO\_DRIVE\_MIDDLE

| #define RZT2M\_GPIO\_DRIVE\_MIDDLE   (1U << [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)) |
| --- |

## [◆ ](#a8fdc883e48d39eb950e47c8a7433630f)RZT2M\_GPIO\_DRIVE\_OFFSET

| #define RZT2M\_GPIO\_DRIVE\_OFFSET   8 |
| --- |

## [◆ ](#a2b60d89adec85b941aa8d7963233aafb)RZT2M\_GPIO\_DRIVE\_ULTRA\_HIGH

| #define RZT2M\_GPIO\_DRIVE\_ULTRA\_HIGH   (3U << [RZT2M\_GPIO\_DRIVE\_OFFSET](#a8fdc883e48d39eb950e47c8a7433630f)) |
| --- |

## [◆ ](#ac2d2e1cef0fa53eb0ce6f7dcb32cb4ef)RZT2M\_GPIO\_SCHMITT\_TRIGGER

| #define RZT2M\_GPIO\_SCHMITT\_TRIGGER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([RZT2M\_GPIO\_SCHMITT\_TRIGGER\_OFFSET](#a0536626285ce7ba19c1a8baf57365902)) |
| --- |

Enable GPIO pin schmitt trigger.

## [◆ ](#a5650f1078ef92c15174bf2ce8c7e6f08)RZT2M\_GPIO\_SCHMITT\_TRIGGER\_MASK

| #define RZT2M\_GPIO\_SCHMITT\_TRIGGER\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([RZT2M\_GPIO\_SCHMITT\_TRIGGER\_OFFSET](#a0536626285ce7ba19c1a8baf57365902)) |
| --- |

## [◆ ](#a0536626285ce7ba19c1a8baf57365902)RZT2M\_GPIO\_SCHMITT\_TRIGGER\_OFFSET

| #define RZT2M\_GPIO\_SCHMITT\_TRIGGER\_OFFSET   10 |
| --- |

## [◆ ](#a752db650514faa34a43bf14a70746dac)RZT2M\_GPIO\_SLEW\_RATE\_FAST

| #define RZT2M\_GPIO\_SLEW\_RATE\_FAST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([RZT2M\_GPIO\_SLEW\_RATE\_OFFSET](#a4f3e3fb225e921d3405c189b87980a16)) |
| --- |

## [◆ ](#a595d6e02f3fd2168deb2fe06f6d00f7d)RZT2M\_GPIO\_SLEW\_RATE\_MASK

| #define RZT2M\_GPIO\_SLEW\_RATE\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([RZT2M\_GPIO\_SLEW\_RATE\_OFFSET](#a4f3e3fb225e921d3405c189b87980a16)) |
| --- |

## [◆ ](#a4f3e3fb225e921d3405c189b87980a16)RZT2M\_GPIO\_SLEW\_RATE\_OFFSET

| #define RZT2M\_GPIO\_SLEW\_RATE\_OFFSET   11 |
| --- |

## [◆ ](#a2f754f8752b7c42ee89286725b2be4bb)RZT2M\_GPIO\_SLEW\_RATE\_SLOW

| #define RZT2M\_GPIO\_SLEW\_RATE\_SLOW   0U |
| --- |

Select GPIO pin slew rate.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [renesas-rzt2m-gpio.h](renesas-rzt2m-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
