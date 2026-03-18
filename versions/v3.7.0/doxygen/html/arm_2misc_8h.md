---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm_2misc_8h.html
original_path: doxygen/html/arm_2misc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

misc.h File Reference

ARM AArch32 public kernel miscellaneous.
[More...](#details)

[Go to the source code of this file.](arm_2misc_8h_source.md)

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_cycle\_get\_32](#a42dcd1878309a82246dbfa26510f868a) (void) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_k\_cycle\_get\_32](#a9ee9f897ec750957de45bf8d43349d5e) (void) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_clock\_cycle\_get\_64](#a25328a181bd0229ef5110c15e8452fc1) (void) |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_k\_cycle\_get\_64](#acc1ed8d949f694a1d39e389334caf971) (void) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_nop](#a0af98dc5138e02248173c30b8f07210f) (void) |

## Detailed Description

ARM AArch32 public kernel miscellaneous.

ARM AArch32-specific kernel miscellaneous interface. Included by [arm/arch.h](arm_2arch_8h.md "ARM AArch32 specific kernel interface header.").

## Function Documentation

## [◆ ](#a9ee9f897ec750957de45bf8d43349d5e)arch\_k\_cycle\_get\_32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_k\_cycle\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acc1ed8d949f694a1d39e389334caf971)arch\_k\_cycle\_get\_64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_k\_cycle\_get\_64 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0af98dc5138e02248173c30b8f07210f)arch\_nop()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_nop | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a42dcd1878309a82246dbfa26510f868a)sys\_clock\_cycle\_get\_32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_clock\_cycle\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a25328a181bd0229ef5110c15e8452fc1)sys\_clock\_cycle\_get\_64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_clock\_cycle\_get\_64 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [misc.h](arm_2misc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
