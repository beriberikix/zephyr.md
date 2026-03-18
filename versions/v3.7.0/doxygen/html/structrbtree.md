---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structrbtree.html
original_path: doxygen/html/structrbtree.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rbtree Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [Balanced Red/Black Tree](group__rbtree__apis.md)

Balanced red/black tree structure.
[More...](#details)

`#include <[rb.h](rb_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [rbnode](structrbnode.md) \* | [root](#abd0a6e986acba39f103cb66fb1c3bd3b) |
|  | Root node of the tree. |
| [rb\_lessthan\_t](group__rbtree__apis.md#ga6c22a3d4a917b0a2e4328eb9df8e8615) | [lessthan\_fn](#aed5a31980a5cd818b91fd14ccf8bcd75) |
|  | Comparison function for nodes in the tree. |

## Detailed Description

Balanced red/black tree structure.

## Field Documentation

## [◆ ](#aed5a31980a5cd818b91fd14ccf8bcd75)lessthan\_fn

| [rb\_lessthan\_t](group__rbtree__apis.md#ga6c22a3d4a917b0a2e4328eb9df8e8615) rbtree::lessthan\_fn |
| --- |

Comparison function for nodes in the tree.

## [◆ ](#abd0a6e986acba39f103cb66fb1c3bd3b)root

| struct [rbnode](structrbnode.md)\* rbtree::root |
| --- |

Root node of the tree.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[rb.h](rb_8h_source.md)

- [rbtree](structrbtree.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
