---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__obj__core.html
original_path: doxygen/html/structk__obj__core.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_obj\_core Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Object Core APIs](group__obj__core__apis.md)

Object core structure.
[More...](#details)

`#include <[obj_core.h](obj__core_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a3ef8e436efe8b8daefef44c649222407) |
|  | Object node within object type's list. |
| struct [k\_obj\_type](structk__obj__type.md) \* | [type](#ad08bd00d9d7f4d331ed0775514e766b5) |
|  | Object type to which object belongs. |

## Detailed Description

Object core structure.

## Field Documentation

## [◆ ](#a3ef8e436efe8b8daefef44c649222407)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) k\_obj\_core::node |
| --- |

Object node within object type's list.

## [◆ ](#ad08bd00d9d7f4d331ed0775514e766b5)type

| struct [k\_obj\_type](structk__obj__type.md)\* k\_obj\_core::type |
| --- |

Object type to which object belongs.

---

The documentation for this struct was generated from the following file:

- zephyr/kernel/[obj\_core.h](obj__core_8h_source.md)

- [k\_obj\_core](structk__obj__core.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
