---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmem__attr__region__t.html
original_path: doxygen/html/structmem__attr__region__t.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_attr\_region\_t Struct Reference

[Memory Management APIs](group__mem__mgmt.md) » [Memory-Attr Interface](group__memory__attr__interface.md)

memory-attr region structure.
[More...](#details)

`#include <[mem_attr.h](mem__attr_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [dt\_name](#a84906ca493441f65f68409f1798e960e) |
|  | Memory node full name. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [dt\_addr](#a0f5363766454ed56fa00152b3bcedadd) |
|  | Memory region physical address. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [dt\_size](#a3931b272d0e7b3ea0ced85888356a2d1) |
|  | Memory region size. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dt\_attr](#ad853fe05ac7015b9229ad49a4ddbb719) |
|  | Memory region attributes. |

## Detailed Description

memory-attr region structure.

This structure represents the data gathered from DT about a memory-region marked with memory attributes.

## Field Documentation

## [◆ ](#a0f5363766454ed56fa00152b3bcedadd)dt\_addr

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) mem\_attr\_region\_t::dt\_addr |
| --- |

Memory region physical address.

## [◆ ](#ad853fe05ac7015b9229ad49a4ddbb719)dt\_attr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mem\_attr\_region\_t::dt\_attr |
| --- |

Memory region attributes.

## [◆ ](#a84906ca493441f65f68409f1798e960e)dt\_name

| const char\* mem\_attr\_region\_t::dt\_name |
| --- |

Memory node full name.

## [◆ ](#a3931b272d0e7b3ea0ced85888356a2d1)dt\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) mem\_attr\_region\_t::dt\_size |
| --- |

Memory region size.

---

The documentation for this struct was generated from the following file:

- zephyr/mem\_mgmt/[mem\_attr.h](mem__attr_8h_source.md)

- [mem\_attr\_region\_t](structmem__attr__region__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
