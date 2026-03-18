---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structk__obj__type.html
original_path: doxygen/html/structk__obj__type.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_obj\_type Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Object Core APIs](group__obj__core__apis.md)

Object type structure.
[More...](#details)

`#include <[obj_core.h](obj__core_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a96995171db1f9e3927058b2f4f22fb41) |
|  | Node within list of object types. |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [list](#ac00f591b7d19a0e2d43b167793ef0f29) |
|  | List of objects of this object type. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#acf48ce26b12ef2f1584b4d32f2b2b712) |
|  | Unique type ID. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [obj\_core\_offset](#a39824fdc4dd042e1742c4d966b068a61) |
|  | Offset to obj\_core field. |

## Detailed Description

Object type structure.

## Field Documentation

## [◆ ](#acf48ce26b12ef2f1584b4d32f2b2b712)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_obj\_type::id |
| --- |

Unique type ID.

## [◆ ](#ac00f591b7d19a0e2d43b167793ef0f29)list

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) k\_obj\_type::list |
| --- |

List of objects of this object type.

## [◆ ](#a96995171db1f9e3927058b2f4f22fb41)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) k\_obj\_type::node |
| --- |

Node within list of object types.

## [◆ ](#a39824fdc4dd042e1742c4d966b068a61)obj\_core\_offset

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_obj\_type::obj\_core\_offset |
| --- |

Offset to obj\_core field.

---

The documentation for this struct was generated from the following file:

- zephyr/kernel/[obj\_core.h](obj__core_8h_source.md)

- [k\_obj\_type](structk__obj__type.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
