---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/xlnx__gem_8h.html
original_path: doxygen/html/xlnx__gem_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xlnx\_gem.h File Reference

[Go to the source code of this file.](xlnx__gem_8h_source.md)

| Macros | |
| --- | --- |
| #define | [XLNX\_GEM\_PHY\_AUTO\_DETECT](#a6f1dc25e8cf23705674ad0bf8a3dd607)   0 |
| #define | [XLNX\_GEM\_MDC\_DIVIDER\_8](#aecfc16f895d5904bb88865654192b6af)   0 /\* cpu\_1x or IOU\_SWITCH\_CLK < 20 MHz \*/ |
| #define | [XLNX\_GEM\_MDC\_DIVIDER\_16](#a2dd7b7b6960988c9adda4e6bb9104d3b)   1 /\* cpu\_1x or IOU\_SWITCH\_CLK 20 - 40 MHz \*/ |
| #define | [XLNX\_GEM\_MDC\_DIVIDER\_32](#a39223a666570e19229337c37affec28a)   2 /\* cpu\_1x or IOU\_SWITCH\_CLK 40 - 80 MHz \*/ |
| #define | [XLNX\_GEM\_MDC\_DIVIDER\_48](#ab161bdaf20281af805fe256aa1420965)   3 /\* cpu\_1x or IOU\_SWITCH\_CLK 80 - 120 MHz \*/ |
| #define | [XLNX\_GEM\_MDC\_DIVIDER\_64](#a299bad98c83526e02e9cbc7b1e20c3e8)   4 /\* cpu\_1x or IOU\_SWITCH\_CLK 120 - 160 MHz \*/ |
| #define | [XLNX\_GEM\_MDC\_DIVIDER\_96](#a903826e931e2f98859a52f3abd6746a5)   5 /\* cpu\_1x or IOU\_SWITCH\_CLK 160 - 240 MHz \*/ |
| #define | [XLNX\_GEM\_MDC\_DIVIDER\_128](#ac0c4600967372762d6c331f050900812)   6 /\* cpu\_1x or IOU\_SWITCH\_CLK 240 - 320 MHz \*/ |
| #define | [XLNX\_GEM\_MDC\_DIVIDER\_224](#afe8f02554a5ec893f1c5aaf9a67e8406)   7 /\* cpu\_1x or IOU\_SWITCH\_CLK 320 - 540 MHz \*/ |
| #define | [XLNX\_GEM\_LINK\_SPEED\_10MBIT](#a36088d09ca9962a60a92988b1a24b129)   1 |
| #define | [XLNX\_GEM\_LINK\_SPEED\_100MBIT](#a9ca8d8dcb4dc9acee911a501b7578f30)   2 |
| #define | [XLNX\_GEM\_LINK\_SPEED\_1GBIT](#a3ab42595d945a7a83be47a6693b8b5f2)   3 |
| #define | [XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_32BIT](#a45ebc16715ede38f89977f402c29a55f)   0 |
| #define | [XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_64BIT](#ac73d8a83557499aec09b759e578e6878)   1 |
| #define | [XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_128BIT](#a0f60f82ee244fd2522e00a1b897f7d49)   2 |
| #define | [XLNX\_GEM\_AMBA\_AHB\_BURST\_SINGLE](#a2ea757d44f3110a20113acb4673bcf43)   1 |
| #define | [XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR4](#a18db46b4e0826fe2b0ba2de2f198c41d)   4 |
| #define | [XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR8](#aaf8ecbfd760ae236aad17ce5ff0ddd91)   8 |
| #define | [XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR16](#af53fba620b18e599bef91a544b638ef1)   16 |
| #define | [XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_1KB](#a9089698903ed9087cc077b6f8b71716e)   0 |
| #define | [XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_2KB](#a7b05fe3ebab46720d425de07fcdb4e59)   1 |
| #define | [XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_4KB](#adec908c6be1fde115f7b5b2317f7e49f)   2 |
| #define | [XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_8KB](#a3782b31ebb12c7c18fe1ae2d1d71525c)   3 |

## Macro Definition Documentation

## [◆ ](#af53fba620b18e599bef91a544b638ef1)XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR16

| #define XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR16   16 |
| --- |

## [◆ ](#a18db46b4e0826fe2b0ba2de2f198c41d)XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR4

| #define XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR4   4 |
| --- |

## [◆ ](#aaf8ecbfd760ae236aad17ce5ff0ddd91)XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR8

| #define XLNX\_GEM\_AMBA\_AHB\_BURST\_INCR8   8 |
| --- |

## [◆ ](#a2ea757d44f3110a20113acb4673bcf43)XLNX\_GEM\_AMBA\_AHB\_BURST\_SINGLE

| #define XLNX\_GEM\_AMBA\_AHB\_BURST\_SINGLE   1 |
| --- |

## [◆ ](#a0f60f82ee244fd2522e00a1b897f7d49)XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_128BIT

| #define XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_128BIT   2 |
| --- |

## [◆ ](#a45ebc16715ede38f89977f402c29a55f)XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_32BIT

| #define XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_32BIT   0 |
| --- |

## [◆ ](#ac73d8a83557499aec09b759e578e6878)XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_64BIT

| #define XLNX\_GEM\_AMBA\_AHB\_DBUS\_WIDTH\_64BIT   1 |
| --- |

## [◆ ](#a9089698903ed9087cc077b6f8b71716e)XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_1KB

| #define XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_1KB   0 |
| --- |

## [◆ ](#a7b05fe3ebab46720d425de07fcdb4e59)XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_2KB

| #define XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_2KB   1 |
| --- |

## [◆ ](#adec908c6be1fde115f7b5b2317f7e49f)XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_4KB

| #define XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_4KB   2 |
| --- |

## [◆ ](#a3782b31ebb12c7c18fe1ae2d1d71525c)XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_8KB

| #define XLNX\_GEM\_HW\_RX\_BUFFER\_SIZE\_8KB   3 |
| --- |

## [◆ ](#a9ca8d8dcb4dc9acee911a501b7578f30)XLNX\_GEM\_LINK\_SPEED\_100MBIT

| #define XLNX\_GEM\_LINK\_SPEED\_100MBIT   2 |
| --- |

## [◆ ](#a36088d09ca9962a60a92988b1a24b129)XLNX\_GEM\_LINK\_SPEED\_10MBIT

| #define XLNX\_GEM\_LINK\_SPEED\_10MBIT   1 |
| --- |

## [◆ ](#a3ab42595d945a7a83be47a6693b8b5f2)XLNX\_GEM\_LINK\_SPEED\_1GBIT

| #define XLNX\_GEM\_LINK\_SPEED\_1GBIT   3 |
| --- |

## [◆ ](#ac0c4600967372762d6c331f050900812)XLNX\_GEM\_MDC\_DIVIDER\_128

| #define XLNX\_GEM\_MDC\_DIVIDER\_128   6 /\* cpu\_1x or IOU\_SWITCH\_CLK 240 - 320 MHz \*/ |
| --- |

## [◆ ](#a2dd7b7b6960988c9adda4e6bb9104d3b)XLNX\_GEM\_MDC\_DIVIDER\_16

| #define XLNX\_GEM\_MDC\_DIVIDER\_16   1 /\* cpu\_1x or IOU\_SWITCH\_CLK 20 - 40 MHz \*/ |
| --- |

## [◆ ](#afe8f02554a5ec893f1c5aaf9a67e8406)XLNX\_GEM\_MDC\_DIVIDER\_224

| #define XLNX\_GEM\_MDC\_DIVIDER\_224   7 /\* cpu\_1x or IOU\_SWITCH\_CLK 320 - 540 MHz \*/ |
| --- |

## [◆ ](#a39223a666570e19229337c37affec28a)XLNX\_GEM\_MDC\_DIVIDER\_32

| #define XLNX\_GEM\_MDC\_DIVIDER\_32   2 /\* cpu\_1x or IOU\_SWITCH\_CLK 40 - 80 MHz \*/ |
| --- |

## [◆ ](#ab161bdaf20281af805fe256aa1420965)XLNX\_GEM\_MDC\_DIVIDER\_48

| #define XLNX\_GEM\_MDC\_DIVIDER\_48   3 /\* cpu\_1x or IOU\_SWITCH\_CLK 80 - 120 MHz \*/ |
| --- |

## [◆ ](#a299bad98c83526e02e9cbc7b1e20c3e8)XLNX\_GEM\_MDC\_DIVIDER\_64

| #define XLNX\_GEM\_MDC\_DIVIDER\_64   4 /\* cpu\_1x or IOU\_SWITCH\_CLK 120 - 160 MHz \*/ |
| --- |

## [◆ ](#aecfc16f895d5904bb88865654192b6af)XLNX\_GEM\_MDC\_DIVIDER\_8

| #define XLNX\_GEM\_MDC\_DIVIDER\_8   0 /\* cpu\_1x or IOU\_SWITCH\_CLK < 20 MHz \*/ |
| --- |

## [◆ ](#a903826e931e2f98859a52f3abd6746a5)XLNX\_GEM\_MDC\_DIVIDER\_96

| #define XLNX\_GEM\_MDC\_DIVIDER\_96   5 /\* cpu\_1x or IOU\_SWITCH\_CLK 160 - 240 MHz \*/ |
| --- |

## [◆ ](#a6f1dc25e8cf23705674ad0bf8a3dd607)XLNX\_GEM\_PHY\_AUTO\_DETECT

| #define XLNX\_GEM\_PHY\_AUTO\_DETECT   0 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [ethernet](dir_206bb9b0b304009ae1ec5beda9489e52.md)
- [xlnx\_gem.h](xlnx__gem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
