---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__rbtree__apis.html
original_path: doxygen/html/group__rbtree__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Balanced Red/Black Tree

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Balanced Red/Black Tree implementation.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [rbnode](structrbnode.md) |
|  | Balanced red/black tree node structure. [More...](structrbnode.md#details) |
| struct | [rbtree](structrbtree.md) |
|  | Balanced red/black tree structure. [More...](structrbtree.md#details) |

| Macros | |
| --- | --- |
| #define | [RB\_FOR\_EACH](#gaa0a518139442a69865881f6b460b03df)(tree, node) |
|  | Walk a tree in-order without recursing. |
| #define | [RB\_FOR\_EACH\_CONTAINER](#gab03a8af066d5110cda6b7522f342b168)(tree, node, field) |
|  | Loop over rbtree with implicit container field logic. |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [rb\_lessthan\_t](#ga6c22a3d4a917b0a2e4328eb9df8e8615)) (struct [rbnode](structrbnode.md) \*a, struct [rbnode](structrbnode.md) \*b) |
|  | Red/black tree comparison predicate. |
| typedef void(\* | [rb\_visit\_t](#ga27e6996e6ed57aabb2791662960beca0)) (struct [rbnode](structrbnode.md) \*node, void \*cookie) |
|  | Prototype for node visitor callback. |

| Functions | |
| --- | --- |
| void | [rb\_insert](#ga6b2c6d796f333fb03e316afc42336ecf) (struct [rbtree](structrbtree.md) \*tree, struct [rbnode](structrbnode.md) \*node) |
|  | Insert node into tree. |
| void | [rb\_remove](#ga8de6504411a0dbd8f4a43e9e18c53919) (struct [rbtree](structrbtree.md) \*tree, struct [rbnode](structrbnode.md) \*node) |
|  | Remove node from tree. |
| static struct [rbnode](structrbnode.md) \* | [rb\_get\_min](#ga2fe1a6028e972155acc0cc72429d8dec) (struct [rbtree](structrbtree.md) \*tree) |
|  | Returns the lowest-sorted member of the tree. |
| static struct [rbnode](structrbnode.md) \* | [rb\_get\_max](#ga031fd9abf8ae98fe0c7519465df522f6) (struct [rbtree](structrbtree.md) \*tree) |
|  | Returns the highest-sorted member of the tree. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [rb\_contains](#ga918cb502c4b636f49a73906735612b91) (struct [rbtree](structrbtree.md) \*tree, struct [rbnode](structrbnode.md) \*node) |
|  | Returns true if the given node is part of the tree. |
| static void | [rb\_walk](#ga79e7c341ee876f1e6f6adaf8b1162995) (struct [rbtree](structrbtree.md) \*tree, [rb\_visit\_t](#ga27e6996e6ed57aabb2791662960beca0) visit\_fn, void \*cookie) |
|  | Walk/enumerate a rbtree. |

## Detailed Description

Balanced Red/Black Tree implementation.

This implements an intrusive balanced tree that guarantees O(log2(N)) runtime for all operations and amortized O(1) behavior for creation and destruction of whole trees. The algorithms and naming are conventional per existing academic and didactic implementations, c.f.:

[https://en.wikipedia.org/wiki/Red%E2%80%93black\_tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)

The implementation is size-optimized to prioritize runtime memory usage. The data structure is intrusive, which is to say the [rbnode](structrbnode.md "rbnode") handle is intended to be placed in a separate struct, in the same way as with other such structures (e.g. Zephyr's [Doubly-linked list](group__doubly-linked-list__apis.md "Doubly-linked list")), and requires no data pointer to be stored in the node. The color bit is unioned with a pointer (fairly common for such libraries). Most notably, there is no "parent" pointer stored in the node, the upper structure of the tree being generated dynamically via a stack as the tree is recursed. So the overall memory overhead of a node is just two pointers, identical with a doubly-linked list.

## Macro Definition Documentation

## [◆ ](#gaa0a518139442a69865881f6b460b03df)RB\_FOR\_EACH

| #define RB\_FOR\_EACH | ( |  | *tree*, |
| --- | --- | --- | --- |
|  |  |  | *node* ) |

`#include <[rb.h](rb_8h.md)>`

**Value:**

for (struct \_rb\_foreach \_\_f = \_RB\_FOREACH\_INIT(tree, node); \

((node) = z\_rb\_foreach\_next((tree), &\_\_f)); \

)

Walk a tree in-order without recursing.

While [rb\_walk()](#ga79e7c341ee876f1e6f6adaf8b1162995) is very simple, recursing on the C stack can be clumsy for some purposes and on some architectures wastes significant memory in stack frames. This macro implements a non-recursive "foreach" loop that can iterate directly on the tree, at a moderate cost in code size.

Note that the resulting loop is not safe against modifications to the tree. Changes to the tree structure during the loop will produce incorrect results, as nodes may be skipped or duplicated. Unlike linked lists, no \_SAFE variant exists.

Note also that the macro expands its arguments multiple times, so they should not be expressions with side effects.

Parameters
:   | tree | A pointer to a struct rbtree to walk |
    | --- | --- |
    | node | The symbol name of a local struct rbnode\* variable to use as the iterator |

## [◆ ](#gab03a8af066d5110cda6b7522f342b168)RB\_FOR\_EACH\_CONTAINER

| #define RB\_FOR\_EACH\_CONTAINER | ( |  | *tree*, |
| --- | --- | --- | --- |
|  |  |  | *node*, |
|  |  |  | *field* ) |

`#include <[rb.h](rb_8h.md)>`

**Value:**

for (struct \_rb\_foreach \_\_f = \_RB\_FOREACH\_INIT(tree, node); \

({struct [rbnode](structrbnode.md) \*n = z\_rb\_foreach\_next(tree, &\_\_f); \

(node) = n ? [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(n, \_\_typeof\_\_(\*(node)), \

field) : [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4); (node); }) != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4); \

)

[CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)

#define CONTAINER\_OF(ptr, type, field)

Get a pointer to a structure containing the element.

**Definition** util.h:284

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[rbnode](structrbnode.md)

Balanced red/black tree node structure.

**Definition** rb.h:58

Loop over rbtree with implicit container field logic.

As for [RB\_FOR\_EACH()](#gaa0a518139442a69865881f6b460b03df), but "node" can have an arbitrary type containing a struct rbnode.

Parameters
:   | tree | A pointer to a struct rbtree to walk |
    | --- | --- |
    | node | The symbol name of a local iterator |
    | field | The field name of a struct rbnode inside node |

## Typedef Documentation

## [◆ ](#ga6c22a3d4a917b0a2e4328eb9df8e8615)rb\_lessthan\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* rb\_lessthan\_t) (struct [rbnode](structrbnode.md) \*a, struct [rbnode](structrbnode.md) \*b) |
| --- |

`#include <[rb.h](rb_8h.md)>`

Red/black tree comparison predicate.

Compares the two nodes and returns true if node A is strictly less than B according to the tree's sorting criteria, false otherwise.

Note that during insert, the new node being inserted will always be "A", where "B" is the existing node within the tree against which it is being compared. This trait can be used (with care!) to implement "most/least recently added" semantics between nodes which would otherwise compare as equal.

## [◆ ](#ga27e6996e6ed57aabb2791662960beca0)rb\_visit\_t

| typedef void(\* rb\_visit\_t) (struct [rbnode](structrbnode.md) \*node, void \*cookie) |
| --- |

`#include <[rb.h](rb_8h.md)>`

Prototype for node visitor callback.

Parameters
:   | node | Node being visited |
    | --- | --- |
    | cookie | User-specified data |

## Function Documentation

## [◆ ](#ga918cb502c4b636f49a73906735612b91)rb\_contains()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) rb\_contains | ( | struct [rbtree](structrbtree.md) \* | *tree*, |
| --- | --- | --- | --- |
|  |  | struct [rbnode](structrbnode.md) \* | *node* ) |

`#include <[rb.h](rb_8h.md)>`

Returns true if the given node is part of the tree.

Note that this does not internally dereference the node pointer (though the tree's lessthan callback might!), it just tests it for equality with items in the tree. So it's feasible to use this to implement a "set" construct by simply testing the pointer value itself.

## [◆ ](#ga031fd9abf8ae98fe0c7519465df522f6)rb\_get\_max()

| | struct [rbnode](structrbnode.md) \* rb\_get\_max | ( | struct [rbtree](structrbtree.md) \* | *tree* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rb.h](rb_8h.md)>`

Returns the highest-sorted member of the tree.

## [◆ ](#ga2fe1a6028e972155acc0cc72429d8dec)rb\_get\_min()

| | struct [rbnode](structrbnode.md) \* rb\_get\_min | ( | struct [rbtree](structrbtree.md) \* | *tree* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rb.h](rb_8h.md)>`

Returns the lowest-sorted member of the tree.

## [◆ ](#ga6b2c6d796f333fb03e316afc42336ecf)rb\_insert()

| void rb\_insert | ( | struct [rbtree](structrbtree.md) \* | *tree*, |
| --- | --- | --- | --- |
|  |  | struct [rbnode](structrbnode.md) \* | *node* ) |

`#include <[rb.h](rb_8h.md)>`

Insert node into tree.

## [◆ ](#ga8de6504411a0dbd8f4a43e9e18c53919)rb\_remove()

| void rb\_remove | ( | struct [rbtree](structrbtree.md) \* | *tree*, |
| --- | --- | --- | --- |
|  |  | struct [rbnode](structrbnode.md) \* | *node* ) |

`#include <[rb.h](rb_8h.md)>`

Remove node from tree.

## [◆ ](#ga79e7c341ee876f1e6f6adaf8b1162995)rb\_walk()

| | void rb\_walk | ( | struct [rbtree](structrbtree.md) \* | *tree*, | | --- | --- | --- | --- | |  |  | [rb\_visit\_t](#ga27e6996e6ed57aabb2791662960beca0) | *visit\_fn*, | |  |  | void \* | *cookie* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rb.h](rb_8h.md)>`

Walk/enumerate a rbtree.

Very simple recursive enumeration. Low code size, but requiring a separate function can be clumsy for the user and there is no way to break out of the loop early. See RB\_FOR\_EACH for an iterative implementation.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
