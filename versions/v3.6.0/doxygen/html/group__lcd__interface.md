---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__lcd__interface.html
original_path: doxygen/html/group__lcd__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LCD Interface

[Device Driver APIs](group__io__interfaces.md) » [Display Interface](group__display__interface.md)

LCD Interface.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [PANEL\_PIXEL\_FORMAT\_RGB\_888](#ga4775abe39fd68a2d64b4edb649790915)   (0x1 << 0) |
|  | Display pixel formats. |
| #define | [PANEL\_PIXEL\_FORMAT\_MONO01](#ga6712b7424ad89a33e04f66e76d3678ce)   (0x1 << 1) /\* 0=Black 1=White \*/ |
| #define | [PANEL\_PIXEL\_FORMAT\_MONO10](#ga6311ee67721bd6e7209bbdc1b6788eb6)   (0x1 << 2) /\* 1=Black 0=White \*/ |
| #define | [PANEL\_PIXEL\_FORMAT\_ARGB\_8888](#gac86c839997816ecfe501b14d240a6f2a)   (0x1 << 3) |
| #define | [PANEL\_PIXEL\_FORMAT\_RGB\_565](#gad8d20eb4c243e11080d31df41026475b)   (0x1 << 4) |
| #define | [PANEL\_PIXEL\_FORMAT\_BGR\_565](#gabb5f7e341cdd0155e4b7476b81d45d8e)   (0x1 << 5) |

## Detailed Description

LCD Interface.

## Macro Definition Documentation

## [◆ ](#gac86c839997816ecfe501b14d240a6f2a)PANEL\_PIXEL\_FORMAT\_ARGB\_8888

| #define PANEL\_PIXEL\_FORMAT\_ARGB\_8888   (0x1 << 3) |
| --- |

`#include <[panel.h](panel_8h.md)>`

## [◆ ](#gabb5f7e341cdd0155e4b7476b81d45d8e)PANEL\_PIXEL\_FORMAT\_BGR\_565

| #define PANEL\_PIXEL\_FORMAT\_BGR\_565   (0x1 << 5) |
| --- |

`#include <[panel.h](panel_8h.md)>`

## [◆ ](#ga6712b7424ad89a33e04f66e76d3678ce)PANEL\_PIXEL\_FORMAT\_MONO01

| #define PANEL\_PIXEL\_FORMAT\_MONO01   (0x1 << 1) /\* 0=Black 1=White \*/ |
| --- |

`#include <[panel.h](panel_8h.md)>`

## [◆ ](#ga6311ee67721bd6e7209bbdc1b6788eb6)PANEL\_PIXEL\_FORMAT\_MONO10

| #define PANEL\_PIXEL\_FORMAT\_MONO10   (0x1 << 2) /\* 1=Black 0=White \*/ |
| --- |

`#include <[panel.h](panel_8h.md)>`

## [◆ ](#gad8d20eb4c243e11080d31df41026475b)PANEL\_PIXEL\_FORMAT\_RGB\_565

| #define PANEL\_PIXEL\_FORMAT\_RGB\_565   (0x1 << 4) |
| --- |

`#include <[panel.h](panel_8h.md)>`

## [◆ ](#ga4775abe39fd68a2d64b4edb649790915)PANEL\_PIXEL\_FORMAT\_RGB\_888

| #define PANEL\_PIXEL\_FORMAT\_RGB\_888   (0x1 << 0) |
| --- |

`#include <[panel.h](panel_8h.md)>`

Display pixel formats.

Display pixel format enumeration.

These defines must match those present in the [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c "Display pixel formats.") enum. They are required because the enum cannot be reused within devicetree, since enum definitions are not supported by devicetree tooling.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
