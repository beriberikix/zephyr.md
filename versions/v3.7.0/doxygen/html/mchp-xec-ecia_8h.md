---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mchp-xec-ecia_8h.html
original_path: doxygen/html/mchp-xec-ecia_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mchp-xec-ecia.h File Reference

[Go to the source code of this file.](mchp-xec-ecia_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MCHP\_XEC\_ECIA](#ac1daa9f5e1b5764f0748577ee60550d3)(g, gb, na, nd) |
| #define | [MCHP\_XEC\_ECIA\_GIRQ](#a6fee82b914dc9f73392586224f0708e7)(e) |
| #define | [MCHP\_XEC\_ECIA\_GIRQ\_POS](#a32c0b5e661fbee763a496b3b06eae34a)(e) |
| #define | [MCHP\_XEC\_ECIA\_NVIC\_AGGR](#a9099e944648c0d8b6946b2092f872122)(e) |
| #define | [MCHP\_XEC\_ECIA\_NVIC\_DIRECT](#a1efb0ece73d7b15da7cdc316c162bc3a)(e) |

## Macro Definition Documentation

## [◆ ](#ac1daa9f5e1b5764f0748577ee60550d3)MCHP\_XEC\_ECIA

| #define MCHP\_XEC\_ECIA | ( |  | *g*, |
| --- | --- | --- | --- |
|  |  |  | *gb*, |
|  |  |  | *na*, |
|  |  |  | *nd* ) |

**Value:**

(((g) & 0x1f) + (((gb) & 0x1f) << 8) + (((na) & 0xff) << 16) + \

(((nd) & 0xff) << 24))

## [◆ ](#a6fee82b914dc9f73392586224f0708e7)MCHP\_XEC\_ECIA\_GIRQ

| #define MCHP\_XEC\_ECIA\_GIRQ | ( |  | *e* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((e) & 0x1f)

## [◆ ](#a32c0b5e661fbee763a496b3b06eae34a)MCHP\_XEC\_ECIA\_GIRQ\_POS

| #define MCHP\_XEC\_ECIA\_GIRQ\_POS | ( |  | *e* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((e) >> 8) & 0x1f)

## [◆ ](#a9099e944648c0d8b6946b2092f872122)MCHP\_XEC\_ECIA\_NVIC\_AGGR

| #define MCHP\_XEC\_ECIA\_NVIC\_AGGR | ( |  | *e* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((e) >> 16) & 0xff)

## [◆ ](#a1efb0ece73d7b15da7cdc316c162bc3a)MCHP\_XEC\_ECIA\_NVIC\_DIRECT

| #define MCHP\_XEC\_ECIA\_NVIC\_DIRECT | ( |  | *e* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((e) >> 24) & 0xff)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [mchp-xec-ecia.h](mchp-xec-ecia_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
