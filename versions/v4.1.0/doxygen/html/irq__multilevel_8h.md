---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/irq__multilevel_8h.html
original_path: doxygen/html/irq__multilevel_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq\_multilevel.h File Reference

Public interface for multi-level interrupts.
[More...](#details)

`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](irq__multilevel_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IRQ\_TO\_L2](#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)(irq) |
|  | Preprocessor macro to convert irq from level 1 to level 2 format. |
| #define | [IRQ\_TO\_L3](#a1aa1eaa367e7c8baa250900de4eb0daf)(irq) |
|  | Preprocessor macro to convert irq from level 1 to level 3 format. |

| Functions | |
| --- | --- |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_get\_level](#a45afd68784e71521606e489d965b1c13) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Return IRQ level This routine returns the interrupt level number of the provided interrupt. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_from\_level\_2](#a4022e57572b3bffb694bf25eef090cec) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Return the 2nd level interrupt number. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_to\_level\_2](#a79eb4433215c271fa61b9352855f93ca) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Converts irq from level 1 to level 2 format. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_parent\_level\_2](#ab1a4c5a542e4ad472dba609829c34bc4) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Returns the parent IRQ of the level 2 raw IRQ number. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_from\_level\_3](#a401e5249731398fdec30f8e51437f2fb) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Return the 3rd level interrupt number. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_to\_level\_3](#a3b8df71a84ac972b89eb37684dcc7072) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Converts irq from level 1 to level 3 format. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_parent\_level\_3](#ae11c8cb9a832a5a8f514a52a12f133c4) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Returns the parent IRQ of the level 3 raw IRQ number. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_from\_level](#a07a9a77e0d09a05f81d73da2d3f3388a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int level) |
|  | Return the interrupt number for a given level. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_to\_level](#ae91094e0be680803d7bd79739029e390) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int level) |
|  | Converts irq from level 1 to a given level. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_parent\_level](#a8f22ab28ed1da7312fcd716eea59e400) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int level) |
|  | Returns the parent IRQ of the given level raw IRQ number. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_get\_intc\_irq](#a9fb52147e972ee981050b47758dca73d) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Returns the parent interrupt controller IRQ of the given IRQ number. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_increment](#a4b5e1b801ea817b0432a5c5e74f6bff7) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int val) |
|  | Increments the multilevel-encoded *irq* by *val*. |

| Variables | |
| --- | --- |
| Size of \_z\_irq\_t must equal to | [uint32\_t](#a6b77d32212a1febe3b9e3366eb84580e) |

## Detailed Description

Public interface for multi-level interrupts.

## Macro Definition Documentation

## [◆ ](#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)IRQ\_TO\_L2

| #define IRQ\_TO\_L2 | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((irq + 1) << CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS)

Preprocessor macro to convert irq from level 1 to level 2 format.

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |

Returns
:   2nd level IRQ number

## [◆ ](#a1aa1eaa367e7c8baa250900de4eb0daf)IRQ\_TO\_L3

| #define IRQ\_TO\_L3 | ( |  | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((irq + 1) << (CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS))

Preprocessor macro to convert irq from level 1 to level 3 format.

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |

Returns
:   3rd level IRQ number

## Function Documentation

## [◆ ](#a07a9a77e0d09a05f81d73da2d3f3388a)irq\_from\_level()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_from\_level | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *level* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Return the interrupt number for a given level.

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |
    | level | IRQ level |

Returns
:   IRQ number in the level

## [◆ ](#a4022e57572b3bffb694bf25eef090cec)irq\_from\_level\_2()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_from\_level\_2 | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Return the 2nd level interrupt number.

This routine returns the second level irq number of the zephyr irq number passed in

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |

Returns
:   2nd level IRQ number

## [◆ ](#a401e5249731398fdec30f8e51437f2fb)irq\_from\_level\_3()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_from\_level\_3 | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Return the 3rd level interrupt number.

This routine returns the third level irq number of the zephyr irq number passed in

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |

Returns
:   3rd level IRQ number

## [◆ ](#a9fb52147e972ee981050b47758dca73d)irq\_get\_intc\_irq()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_get\_intc\_irq | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Returns the parent interrupt controller IRQ of the given IRQ number.

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |

Returns
:   IRQ of the interrupt controller

## [◆ ](#a45afd68784e71521606e489d965b1c13)irq\_get\_level()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_get\_level | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Return IRQ level This routine returns the interrupt level number of the provided interrupt.

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |

Returns
:   1 if IRQ level 1, 2 if IRQ level 2, 3 if IRQ level 3

## [◆ ](#a4b5e1b801ea817b0432a5c5e74f6bff7)irq\_increment()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_increment | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Increments the multilevel-encoded *irq* by *val*.

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |
    | val | Amount to increment |

Returns
:   *irq* incremented by *val*

## [◆ ](#a8f22ab28ed1da7312fcd716eea59e400)irq\_parent\_level()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_parent\_level | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *level* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Returns the parent IRQ of the given level raw IRQ number.

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |
    | level | IRQ level |

Returns
:   IRQ parent of the given level

## [◆ ](#ab1a4c5a542e4ad472dba609829c34bc4)irq\_parent\_level\_2()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_parent\_level\_2 | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Returns the parent IRQ of the level 2 raw IRQ number.

The parent of a 2nd level interrupt is in the 1st byte

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |

Returns
:   2nd level IRQ parent

## [◆ ](#ae11c8cb9a832a5a8f514a52a12f133c4)irq\_parent\_level\_3()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_parent\_level\_3 | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Returns the parent IRQ of the level 3 raw IRQ number.

The parent of a 3rd level interrupt is in the 2nd byte

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |

Returns
:   3rd level IRQ parent

## [◆ ](#ae91094e0be680803d7bd79739029e390)irq\_to\_level()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_to\_level | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *level* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Converts irq from level 1 to a given level.

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |
    | level | IRQ level |

Returns
:   Converted IRQ number in the level

## [◆ ](#a79eb4433215c271fa61b9352855f93ca)irq\_to\_level\_2()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_to\_level\_2 | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Converts irq from level 1 to level 2 format.

This routine converts the input into the level 2 irq number format

Note
:   Values >= 0xFF are invalid

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |

Returns
:   2nd level IRQ number

## [◆ ](#a3b8df71a84ac972b89eb37684dcc7072)irq\_to\_level\_3()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_to\_level\_3 | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Converts irq from level 1 to level 3 format.

This routine converts the input into the level 3 irq number format

Note
:   Values >= 0xFF are invalid

Parameters
:   | irq | IRQ number in its zephyr format |
    | --- | --- |

Returns
:   3rd level IRQ number

## Variable Documentation

## [◆ ](#a6b77d32212a1febe3b9e3366eb84580e)uint32\_t

| Size of \_z\_irq\_t must equal to [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq\_multilevel.h](irq__multilevel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
