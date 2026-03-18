---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__clock__control__litex__interface.html
original_path: doxygen/html/group__clock__control__litex__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LiteX Clock Control driver interface

[Device Driver APIs](group__io__interfaces.md) » [Clock Control Interface](group__clock__control__interface.md)

LiteX Clock Control driver interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [litex\_clk\_setup](structlitex__clk__setup.md) |
|  | Structure for interfacing with clock control API. [More...](structlitex__clk__setup.md#details) |

| Macros | |
| --- | --- |
| #define | [MMCM](#ga9b1e322b8de40ff6226e14932ef2b879)   [DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clock0) |
| #define | [NCLKOUT](#ga6accac6cf4c18a252888165efb14e637)   [DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)([MMCM](#ga9b1e322b8de40ff6226e14932ef2b879), clock\_output\_names) |

## Detailed Description

LiteX Clock Control driver interface.

LiteX Clock Control driver interface

## Macro Definition Documentation

## [◆ ](#ga9b1e322b8de40ff6226e14932ef2b879)MMCM

| #define MMCM   [DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(clock0) |
| --- |

`#include <[clock_control_litex.h](clock__control__litex_8h.md)>`

## [◆ ](#ga6accac6cf4c18a252888165efb14e637)NCLKOUT

| #define NCLKOUT   [DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)([MMCM](#ga9b1e322b8de40ff6226e14932ef2b879), clock\_output\_names) |
| --- |

`#include <[clock_control_litex.h](clock__control__litex_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
