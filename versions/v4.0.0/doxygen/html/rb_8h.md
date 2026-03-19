---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/rb_8h.html
original_path: doxygen/html/rb_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rb.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <alloca.h>`

[Go to the source code of this file.](rb_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [rbnode](structrbnode.md) |
|  | Balanced red/black tree node structure. [More...](structrbnode.md#details) |
| struct | [rbtree](structrbtree.md) |
|  | Balanced red/black tree structure. [More...](structrbtree.md#details) |

| Macros | |
| --- | --- |
| #define | [RB\_FOR\_EACH](group__rbtree__apis.md#gaa0a518139442a69865881f6b460b03df)(tree, node) |
|  | Walk a tree in-order without recursing. |
| #define | [RB\_FOR\_EACH\_CONTAINER](group__rbtree__apis.md#gab03a8af066d5110cda6b7522f342b168)(tree, node, field) |
|  | Loop over rbtree with implicit container field logic. |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [rb\_lessthan\_t](group__rbtree__apis.md#ga6c22a3d4a917b0a2e4328eb9df8e8615)) (struct [rbnode](structrbnode.md) \*a, struct [rbnode](structrbnode.md) \*b) |
|  | Red/black tree comparison predicate. |
| typedef void(\* | [rb\_visit\_t](group__rbtree__apis.md#ga27e6996e6ed57aabb2791662960beca0)) (struct [rbnode](structrbnode.md) \*node, void \*cookie) |
|  | Prototype for node visitor callback. |

| Functions | |
| --- | --- |
| void | [rb\_insert](group__rbtree__apis.md#ga6b2c6d796f333fb03e316afc42336ecf) (struct [rbtree](structrbtree.md) \*tree, struct [rbnode](structrbnode.md) \*node) |
|  | Insert node into tree. |
| void | [rb\_remove](group__rbtree__apis.md#ga8de6504411a0dbd8f4a43e9e18c53919) (struct [rbtree](structrbtree.md) \*tree, struct [rbnode](structrbnode.md) \*node) |
|  | Remove node from tree. |
| static struct [rbnode](structrbnode.md) \* | [rb\_get\_min](group__rbtree__apis.md#ga2fe1a6028e972155acc0cc72429d8dec) (struct [rbtree](structrbtree.md) \*tree) |
|  | Returns the lowest-sorted member of the tree. |
| static struct [rbnode](structrbnode.md) \* | [rb\_get\_max](group__rbtree__apis.md#ga031fd9abf8ae98fe0c7519465df522f6) (struct [rbtree](structrbtree.md) \*tree) |
|  | Returns the highest-sorted member of the tree. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [rb\_contains](group__rbtree__apis.md#ga918cb502c4b636f49a73906735612b91) (struct [rbtree](structrbtree.md) \*tree, struct [rbnode](structrbnode.md) \*node) |
|  | Returns true if the given node is part of the tree. |
| static void | [rb\_walk](group__rbtree__apis.md#ga79e7c341ee876f1e6f6adaf8b1162995) (struct [rbtree](structrbtree.md) \*tree, [rb\_visit\_t](group__rbtree__apis.md#ga27e6996e6ed57aabb2791662960beca0) visit\_fn, void \*cookie) |
|  | Walk/enumerate a rbtree. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [rb.h](rb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
