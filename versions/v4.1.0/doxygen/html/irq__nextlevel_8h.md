---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/irq__nextlevel_8h.html
original_path: doxygen/html/irq__nextlevel_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq\_nextlevel.h File Reference

Public interface for configuring interrupts.
[More...](#details)

[Go to the source code of this file.](irq__nextlevel_8h_source.md)

| Functions | |
| --- | --- |
| static void | [irq\_enable\_next\_level](#a335d42cf95c25ab8564475c4b4c3ead9) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Enable an IRQ in the next level. |
| static void | [irq\_disable\_next\_level](#ad694fcad4c3fba0d2794cdc34ddcd1bb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Disable an IRQ in the next level. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_is\_enabled\_next\_level](#aa7178acd1058940b83c7c7500217bc01) (const struct [device](structdevice.md) \*dev) |
|  | Get IRQ enable state. |
| static void | [irq\_set\_priority\_next\_level](#af41789f946ebb445f4a402009ed2e8bb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set IRQ priority. |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq\_line\_is\_enabled\_next\_level](#a7e0e5fe59eae08878a8f243dd9301633) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Get IRQ line enable state. |

## Detailed Description

Public interface for configuring interrupts.

## Function Documentation

## [◆ ](#ad694fcad4c3fba0d2794cdc34ddcd1bb)irq\_disable\_next\_level()

| | void irq\_disable\_next\_level | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Disable an IRQ in the next level.

This routine disables interrupts present in the interrupt controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | irq | IRQ to be disabled. |

## [◆ ](#a335d42cf95c25ab8564475c4b4c3ead9)irq\_enable\_next\_level()

| | void irq\_enable\_next\_level | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Enable an IRQ in the next level.

This routine enables interrupts present in the interrupt controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | irq | IRQ to be enabled. |

## [◆ ](#aa7178acd1058940b83c7c7500217bc01)irq\_is\_enabled\_next\_level()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_is\_enabled\_next\_level | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get IRQ enable state.

This routine indicates if any interrupts are enabled in the interrupt controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   interrupt enable state, true or false

## [◆ ](#a7e0e5fe59eae08878a8f243dd9301633)irq\_line\_is\_enabled\_next\_level()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_line\_is\_enabled\_next\_level | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Get IRQ line enable state.

Query if a particular IRQ line is enabled.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | irq | IRQ line to be queried. |

Returns
:   interrupt enable state, true or false

## [◆ ](#af41789f946ebb445f4a402009ed2e8bb)irq\_set\_priority\_next\_level()

| | void irq\_set\_priority\_next\_level | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *prio*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Set IRQ priority.

This routine indicates if any interrupts are enabled in the interrupt controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | irq | IRQ to be disabled. |
    | prio | priority for irq in the interrupt controller. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | controller specific flags. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq\_nextlevel.h](irq__nextlevel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
