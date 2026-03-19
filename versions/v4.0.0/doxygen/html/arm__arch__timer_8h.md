---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm__arch__timer_8h.html
original_path: doxygen/html/arm__arch__timer_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_arch\_timer.h File Reference

`#include <[zephyr/dt-bindings/interrupt-controller/arm-gic.h](arm-gic_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](arm__arch__timer_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42)   [DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(0, arm\_armv8\_timer) |
| #define | [ARM\_TIMER\_SECURE\_IRQ](#ab20a2e64d841b305054bb1e5463de625)   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 0, irq) |
| #define | [ARM\_TIMER\_NON\_SECURE\_IRQ](#a62df9aa2725c6cc49641bad7eddedfb2)   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 1, irq) |
| #define | [ARM\_TIMER\_VIRTUAL\_IRQ](#a22468e93135e790458d9c2bfd493c070)   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 2, irq) |
| #define | [ARM\_TIMER\_HYP\_IRQ](#abb6827272e664d5f0ebc05efaacf4a8c)   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 3, irq) |
| #define | [ARM\_TIMER\_SECURE\_PRIO](#a10a91fd36630255fb88f08558b96be7a) |
| #define | [ARM\_TIMER\_NON\_SECURE\_PRIO](#a48f3d216ea1166a40f7c5ab333e269b8) |
| #define | [ARM\_TIMER\_VIRTUAL\_PRIO](#acafac307be9d89ff4ebb72ab23c75ac6) |
| #define | [ARM\_TIMER\_HYP\_PRIO](#a5b8a919fcfd8e4346aca7eefa382a1f0) |
| #define | [ARM\_TIMER\_SECURE\_FLAGS](#ab43f20d1d6d366b921817c2c463c5025)   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 0, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| #define | [ARM\_TIMER\_NON\_SECURE\_FLAGS](#a7852b4d22a08d2bef99c14495daff57a)   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 1, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| #define | [ARM\_TIMER\_VIRTUAL\_FLAGS](#a373af60653667562ca2ca950c45e4b20)   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 2, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| #define | [ARM\_TIMER\_HYP\_FLAGS](#a9c6a0c6b52a600627958024cf80929de)   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 3, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |

## Macro Definition Documentation

## [◆ ](#a9c6a0c6b52a600627958024cf80929de)ARM\_TIMER\_HYP\_FLAGS

| #define ARM\_TIMER\_HYP\_FLAGS   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 3, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

## [◆ ](#abb6827272e664d5f0ebc05efaacf4a8c)ARM\_TIMER\_HYP\_IRQ

| #define ARM\_TIMER\_HYP\_IRQ   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 3, irq) |
| --- |

## [◆ ](#a5b8a919fcfd8e4346aca7eefa382a1f0)ARM\_TIMER\_HYP\_PRIO

| #define ARM\_TIMER\_HYP\_PRIO |
| --- |

**Value:**

[DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 3,\

priority)

[ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42)

#define ARM\_TIMER\_NODE

**Definition** arm\_arch\_timer.h:14

[DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)

#define DT\_IRQ\_BY\_IDX(node\_id, idx, cell)

Get a value within an interrupt specifier at an index.

**Definition** devicetree.h:2650

## [◆ ](#aea7a05797c3c8202e22fbde7784e6f42)ARM\_TIMER\_NODE

| #define ARM\_TIMER\_NODE   [DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(0, arm\_armv8\_timer) |
| --- |

## [◆ ](#a7852b4d22a08d2bef99c14495daff57a)ARM\_TIMER\_NON\_SECURE\_FLAGS

| #define ARM\_TIMER\_NON\_SECURE\_FLAGS   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 1, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

## [◆ ](#a62df9aa2725c6cc49641bad7eddedfb2)ARM\_TIMER\_NON\_SECURE\_IRQ

| #define ARM\_TIMER\_NON\_SECURE\_IRQ   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 1, irq) |
| --- |

## [◆ ](#a48f3d216ea1166a40f7c5ab333e269b8)ARM\_TIMER\_NON\_SECURE\_PRIO

| #define ARM\_TIMER\_NON\_SECURE\_PRIO |
| --- |

**Value:**

[DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 1,\

priority)

## [◆ ](#ab43f20d1d6d366b921817c2c463c5025)ARM\_TIMER\_SECURE\_FLAGS

| #define ARM\_TIMER\_SECURE\_FLAGS   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 0, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

## [◆ ](#ab20a2e64d841b305054bb1e5463de625)ARM\_TIMER\_SECURE\_IRQ

| #define ARM\_TIMER\_SECURE\_IRQ   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 0, irq) |
| --- |

## [◆ ](#a10a91fd36630255fb88f08558b96be7a)ARM\_TIMER\_SECURE\_PRIO

| #define ARM\_TIMER\_SECURE\_PRIO |
| --- |

**Value:**

[DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 0,\

priority)

## [◆ ](#a373af60653667562ca2ca950c45e4b20)ARM\_TIMER\_VIRTUAL\_FLAGS

| #define ARM\_TIMER\_VIRTUAL\_FLAGS   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 2, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

## [◆ ](#a22468e93135e790458d9c2bfd493c070)ARM\_TIMER\_VIRTUAL\_IRQ

| #define ARM\_TIMER\_VIRTUAL\_IRQ   [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 2, irq) |
| --- |

## [◆ ](#acafac307be9d89ff4ebb72ab23c75ac6)ARM\_TIMER\_VIRTUAL\_PRIO

| #define ARM\_TIMER\_VIRTUAL\_PRIO |
| --- |

**Value:**

[DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([ARM\_TIMER\_NODE](#aea7a05797c3c8202e22fbde7784e6f42), 2,\

priority)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [timer](dir_21cf19e3c466cbc66f61aa827c3fd772.md)
- [arm\_arch\_timer.h](arm__arch__timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
