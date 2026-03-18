---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__flagged-single-linked-list__apis.html
original_path: doxygen/html/group__flagged-single-linked-list__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Flagged Single-linked list

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Flagged single-linked list implementation.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [SYS\_SFLIST\_FOR\_EACH\_NODE](#gaa3e9a3eeef7ecca012b0926fb2758c01)(\_\_sl, \_\_sn) |
|  | Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_sn should not be removed. |
| #define | [SYS\_SFLIST\_ITERATE\_FROM\_NODE](#ga0470a27a54ed20eec35baa6cacd6a5ff)(\_\_sl, \_\_sn) |
|  | Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_sn should not be removed. |
| #define | [SYS\_SFLIST\_FOR\_EACH\_NODE\_SAFE](#gabe867ebba43f1f0ebd2441147a9e3d3d)(\_\_sl, \_\_sn, \_\_sns) |
|  | Provide the primitive to safely iterate on a list Note: \_\_sn can be removed, it will not break the loop. |
| #define | [SYS\_SFLIST\_CONTAINER](#ga68dae6db03b52bc27777a2b8c274a852)(\_\_ln, \_\_cn, \_\_n) |
|  | Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes. |
| #define | [SYS\_SFLIST\_PEEK\_HEAD\_CONTAINER](#ga2c339b75ed80f3a94b0419ac73f18682)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek container of the list head. |
| #define | [SYS\_SFLIST\_PEEK\_TAIL\_CONTAINER](#ga73760da17d0daefe655bbd750a3ce3e8)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek container of the list tail. |
| #define | [SYS\_SFLIST\_PEEK\_NEXT\_CONTAINER](#ga0ba4b870acea3a10a1be066fb1d769c8)(\_\_cn, \_\_n) |
|  | Provide the primitive to peek the next container. |
| #define | [SYS\_SFLIST\_FOR\_EACH\_CONTAINER](#ga1db228cdfd8004738fc6c4d2430be0cc)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached. |
| #define | [SYS\_SFLIST\_FOR\_EACH\_CONTAINER\_SAFE](#ga6b33a7b2be024c0e243f5bbccf900e81)(\_\_sl, \_\_cn, \_\_cns, \_\_n) |
|  | Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop. |
| #define | [SYS\_SFLIST\_STATIC\_INIT](#ga892d5c9ce2d89b04f0ce15a88eefed71)(ptr\_to\_list) |
|  | Statically initialize a flagged single-linked list. |
| #define | [SYS\_SFLIST\_FLAGS\_MASK](#ga46e57329036b76ab03267d2e9258d5c2)   0x3UL |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [unative\_t](#ga5f0d5529e0d52d1a0d3c9594fadff48c) |
| typedef struct \_sfnode | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) |
|  | Flagged single-linked list node structure. |
| typedef struct \_sflist | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) |
|  | Flagged single-linked list structure. |

| Functions | |
| --- | --- |
| static void | [sys\_sflist\_init](#ga9597045ad20485fd88a0fec83fe1ffe1) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Initialize a list. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sys\_sfnode\_flags\_get](#ga0e258c1faa3cbaee48c29e8f2c11132b) ([sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Fetch flags value for a particular sfnode. |
| static [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_peek\_head](#ga6c993728bebb604f966cdc944939642e) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Peek the first node from the list. |
| static [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_peek\_tail](#gabf278ac7912180fc50a25c0ebddc093c) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Peek the last node from the list. |
| static void | [sys\_sfnode\_init](#gae56469b67ad7a92363d04ac726e326ea) ([sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Initialize an sflist node. |
| static void | [sys\_sfnode\_flags\_set](#ga85d82a3a5927f79a5f5655cb3405ce95) ([sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set flags value for an sflist node. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_sflist\_is\_empty](#gac506235a9df89a7a52631e9990ceaad5) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Test if the given list is empty. |
| static [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_peek\_next\_no\_check](#gaa67d15dd4fb28dbbc64f4b0e8e21455e) ([sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Peek the next node from current node, node is not NULL. |
| static [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_peek\_next](#ga514b41f1af89f3f08e216cfede7d5605) ([sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Peek the next node from current node. |
| static void | [sys\_sflist\_prepend](#ga824ff283c821b6f392ebd81516b65712) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Prepend a node to the given list. |
| static void | [sys\_sflist\_append](#ga77733972e39b7db9fc3dcc998261fb2d) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Append a node to the given list. |
| static void | [sys\_sflist\_append\_list](#gaaf9512d6c4432f34347771c9887e678a) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list, void \*head, void \*tail) |
|  | Append a list to the given list. |
| static void | [sys\_sflist\_merge\_sflist](#ga6c68678fceb6127a34760fb04ddef8b0) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list\_to\_append) |
|  | merge two sflists, appending the second one to the first |
| static void | [sys\_sflist\_insert](#ga8983c5704eb149b0941f1fb19f79b8c1) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*prev, [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Insert a node to the given list. |
| static [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_get\_not\_empty](#ga065a7968e8082b65f9344a6331b424fc) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Fetch and remove the first node of the given list. |
| static [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_get](#ga124d4dbb8d6d554071cb5eac2585b4ac) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Fetch and remove the first node of the given list. |
| static void | [sys\_sflist\_remove](#ga66c716ef7495fcb04ea60aac340dc5ed) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*prev\_node, [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Remove a node. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_sflist\_find\_and\_remove](#gad66348fe7677cca76a547e09c8354322) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Find and remove a node from a list. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_sflist\_len](#gaa2d7de9f2366bf638c409b34c26aa871) ([sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Compute the size of the given list in O(n) time. |

## Detailed Description

Flagged single-linked list implementation.

Similar to [Single-linked list](group__single-linked-list__apis.md "Single-linked list") with the added ability to define two bits of user "flags" for each node. They can be accessed and modified using the [sys\_sfnode\_flags\_get()](#ga0e258c1faa3cbaee48c29e8f2c11132b) and [sys\_sfnode\_flags\_set()](#ga85d82a3a5927f79a5f5655cb3405ce95) APIs.

Flagged single-linked list implementation using inline macros/functions. This API is not thread safe, and thus if a list is used across threads, calls to functions must be protected with synchronization primitives.

## Macro Definition Documentation

## [◆ ](#ga68dae6db03b52bc27777a2b8c274a852)SYS\_SFLIST\_CONTAINER

| #define SYS\_SFLIST\_CONTAINER | ( |  | *\_\_ln*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[sflist.h](sflist_8h.md)>`

**Value:**

Z\_GENLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n)

Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes.

Parameters
:   | \_\_ln | A pointer on a [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) to get its container |
    | --- | --- |
    | \_\_cn | Container struct type pointer |
    | \_\_n | The field name of [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct |

## [◆ ](#ga46e57329036b76ab03267d2e9258d5c2)SYS\_SFLIST\_FLAGS\_MASK

| #define SYS\_SFLIST\_FLAGS\_MASK   0x3UL |
| --- |

`#include <[sflist.h](sflist_8h.md)>`

## [◆ ](#ga1db228cdfd8004738fc6c4d2430be0cc)SYS\_SFLIST\_FOR\_EACH\_CONTAINER

| #define SYS\_SFLIST\_FOR\_EACH\_CONTAINER | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[sflist.h](sflist_8h.md)>`

**Value:**

Z\_GENLIST\_FOR\_EACH\_CONTAINER(sflist, \_\_sl, \_\_cn, \_\_n)

Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_SFLIST_FOR_EACH_CONTAINER(l, c, n) {
    <user code>
}
```

Parameters
:   | \_\_sl | A pointer on a [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) to iterate on |
    | --- | --- |
    | \_\_cn | A pointer to peek each entry of the list |
    | \_\_n | The field name of [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct |

## [◆ ](#ga6b33a7b2be024c0e243f5bbccf900e81)SYS\_SFLIST\_FOR\_EACH\_CONTAINER\_SAFE

| #define SYS\_SFLIST\_FOR\_EACH\_CONTAINER\_SAFE | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_cns*, |
|  |  |  | *\_\_n* ) |

`#include <[sflist.h](sflist_8h.md)>`

**Value:**

Z\_GENLIST\_FOR\_EACH\_CONTAINER\_SAFE(sflist, \_\_sl, \_\_cn, \_\_cns, \_\_n)

Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_SFLIST_FOR_EACH_NODE_SAFE(l, c, cn, n) {
    <user code>
}
```

Parameters
:   | \_\_sl | A pointer on a [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) to iterate on |
    | --- | --- |
    | \_\_cn | A pointer to peek each entry of the list |
    | \_\_cns | A pointer for the loop to run safely |
    | \_\_n | The field name of [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct |

## [◆ ](#gaa3e9a3eeef7ecca012b0926fb2758c01)SYS\_SFLIST\_FOR\_EACH\_NODE

| #define SYS\_SFLIST\_FOR\_EACH\_NODE | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_sn* ) |

`#include <[sflist.h](sflist_8h.md)>`

**Value:**

Z\_GENLIST\_FOR\_EACH\_NODE(sflist, \_\_sl, \_\_sn)

Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_sn should not be removed.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_SFLIST_FOR_EACH_NODE(l, n) {
    <user code>
}
```

This and other SYS\_SFLIST\_\*() macros are not thread safe.

Parameters
:   | \_\_sl | A pointer on a [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) to iterate on |
    | --- | --- |
    | \_\_sn | A [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) pointer to peek each node of the list |

## [◆ ](#gabe867ebba43f1f0ebd2441147a9e3d3d)SYS\_SFLIST\_FOR\_EACH\_NODE\_SAFE

| #define SYS\_SFLIST\_FOR\_EACH\_NODE\_SAFE | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_sn*, |
|  |  |  | *\_\_sns* ) |

`#include <[sflist.h](sflist_8h.md)>`

**Value:**

Z\_GENLIST\_FOR\_EACH\_NODE\_SAFE(sflist, \_\_sl, \_\_sn, \_\_sns)

Provide the primitive to safely iterate on a list Note: \_\_sn can be removed, it will not break the loop.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_SFLIST_FOR_EACH_NODE_SAFE(l, n, s) {
    <user code>
}
```

This and other SYS\_SFLIST\_\*() macros are not thread safe.

Parameters
:   | \_\_sl | A pointer on a [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) to iterate on |
    | --- | --- |
    | \_\_sn | A [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) pointer to peek each node of the list |
    | \_\_sns | A [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) pointer for the loop to run safely |

## [◆ ](#ga0470a27a54ed20eec35baa6cacd6a5ff)SYS\_SFLIST\_ITERATE\_FROM\_NODE

| #define SYS\_SFLIST\_ITERATE\_FROM\_NODE | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_sn* ) |

`#include <[sflist.h](sflist_8h.md)>`

**Value:**

Z\_GENLIST\_ITERATE\_FROM\_NODE(sflist, \_\_sl, \_\_sn)

Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_sn should not be removed.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_SFLIST_ITERATE_FROM_NODE(l, n) {
    <user code>
}
```

Like [SYS\_SFLIST\_FOR\_EACH\_NODE()](#gaa3e9a3eeef7ecca012b0926fb2758c01), but \_\_dn already contains a node in the list where to start searching for the next entry from. If NULL, it starts from the head.

This and other SYS\_SFLIST\_\*() macros are not thread safe.

Parameters
:   | \_\_sl | A pointer on a [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) to iterate on |
    | --- | --- |
    | \_\_sn | A [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) pointer to peek each node of the list it contains the starting node, or NULL to start from the head |

## [◆ ](#ga2c339b75ed80f3a94b0419ac73f18682)SYS\_SFLIST\_PEEK\_HEAD\_CONTAINER

| #define SYS\_SFLIST\_PEEK\_HEAD\_CONTAINER | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[sflist.h](sflist_8h.md)>`

**Value:**

Z\_GENLIST\_PEEK\_HEAD\_CONTAINER(sflist, \_\_sl, \_\_cn, \_\_n)

Provide the primitive to peek container of the list head.

Parameters
:   | \_\_sl | A pointer on a [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) to peek |
    | --- | --- |
    | \_\_cn | Container struct type pointer |
    | \_\_n | The field name of [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct |

## [◆ ](#ga0ba4b870acea3a10a1be066fb1d769c8)SYS\_SFLIST\_PEEK\_NEXT\_CONTAINER

| #define SYS\_SFLIST\_PEEK\_NEXT\_CONTAINER | ( |  | *\_\_cn*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_n* ) |

`#include <[sflist.h](sflist_8h.md)>`

**Value:**

Z\_GENLIST\_PEEK\_NEXT\_CONTAINER(sflist, \_\_cn, \_\_n)

Provide the primitive to peek the next container.

Parameters
:   | \_\_cn | Container struct type pointer |
    | --- | --- |
    | \_\_n | The field name of [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct |

## [◆ ](#ga73760da17d0daefe655bbd750a3ce3e8)SYS\_SFLIST\_PEEK\_TAIL\_CONTAINER

| #define SYS\_SFLIST\_PEEK\_TAIL\_CONTAINER | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[sflist.h](sflist_8h.md)>`

**Value:**

Z\_GENLIST\_PEEK\_TAIL\_CONTAINER(sflist, \_\_sl, \_\_cn, \_\_n)

Provide the primitive to peek container of the list tail.

Parameters
:   | \_\_sl | A pointer on a [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) to peek |
    | --- | --- |
    | \_\_cn | Container struct type pointer |
    | \_\_n | The field name of [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct |

## [◆ ](#ga892d5c9ce2d89b04f0ce15a88eefed71)SYS\_SFLIST\_STATIC\_INIT

| #define SYS\_SFLIST\_STATIC\_INIT | ( |  | *ptr\_to\_list* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

**Value:**

{NULL, NULL}

Statically initialize a flagged single-linked list.

Parameters
:   | ptr\_to\_list | A pointer on the list to initialize |
    | --- | --- |

## Typedef Documentation

## [◆ ](#ga9e7f835170787303732c805dc7375f66)sys\_sflist\_t

| typedef struct \_sflist [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) |
| --- |

`#include <[sflist.h](sflist_8h.md)>`

Flagged single-linked list structure.

## [◆ ](#ga02dabbe35036cbc11fbbefa99a129cc7)sys\_sfnode\_t

| typedef struct \_sfnode [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) |
| --- |

`#include <[sflist.h](sflist_8h.md)>`

Flagged single-linked list node structure.

## [◆ ](#ga5f0d5529e0d52d1a0d3c9594fadff48c)unative\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unative\_t](#ga5f0d5529e0d52d1a0d3c9594fadff48c) |
| --- |

`#include <[sflist.h](sflist_8h.md)>`

## Function Documentation

## [◆ ](#ga77733972e39b7db9fc3dcc998261fb2d)sys\_sflist\_append()

| | void sys\_sflist\_append | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Append a node to the given list.

This and other sys\_sflist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | node | A pointer on the node to append |

## [◆ ](#gaaf9512d6c4432f34347771c9887e678a)sys\_sflist\_append\_list()

| | void sys\_sflist\_append\_list | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list*, | | --- | --- | --- | --- | |  |  | void \* | *head*, | |  |  | void \* | *tail* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Append a list to the given list.

Append a singly-linked, NULL-terminated list consisting of nodes containing the pointer to the next node as the first element of a node, to *list*. This and other sys\_sflist\_\*() functions are not thread safe.

FIXME: Why are the element parameters void \*?

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | head | A pointer to the first element of the list to append |
    | tail | A pointer to the last element of the list to append |

## [◆ ](#gad66348fe7677cca76a547e09c8354322)sys\_sflist\_find\_and\_remove()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_sflist\_find\_and\_remove | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Find and remove a node from a list.

This and other sys\_sflist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | node | A pointer on the node to remove from the list |

Returns
:   true if node was removed

## [◆ ](#ga124d4dbb8d6d554071cb5eac2585b4ac)sys\_sflist\_get()

| | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* sys\_sflist\_get | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Fetch and remove the first node of the given list.

This and other sys\_sflist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |

Returns
:   A pointer to the first node of the list (or NULL if empty)

## [◆ ](#ga065a7968e8082b65f9344a6331b424fc)sys\_sflist\_get\_not\_empty()

| | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* sys\_sflist\_get\_not\_empty | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Fetch and remove the first node of the given list.

List must be known to be non-empty. This and other sys\_sflist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |

Returns
:   A pointer to the first node of the list

## [◆ ](#ga9597045ad20485fd88a0fec83fe1ffe1)sys\_sflist\_init()

| | void sys\_sflist\_init | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Initialize a list.

Parameters
:   | list | A pointer on the list to initialize |
    | --- | --- |

## [◆ ](#ga8983c5704eb149b0941f1fb19f79b8c1)sys\_sflist\_insert()

| | void sys\_sflist\_insert | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *prev*, | |  |  | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Insert a node to the given list.

This and other sys\_sflist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | prev | A pointer on the previous node |
    | node | A pointer on the node to insert |

## [◆ ](#gac506235a9df89a7a52631e9990ceaad5)sys\_sflist\_is\_empty()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_sflist\_is\_empty | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Test if the given list is empty.

Parameters
:   | list | A pointer on the list to test |
    | --- | --- |

Returns
:   a boolean, true if it's empty, false otherwise

## [◆ ](#gaa2d7de9f2366bf638c409b34c26aa871)sys\_sflist\_len()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_sflist\_len | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Compute the size of the given list in O(n) time.

Parameters
:   | list | A pointer on the list |
    | --- | --- |

Returns
:   an integer equal to the size of the list, or 0 if empty

## [◆ ](#ga6c68678fceb6127a34760fb04ddef8b0)sys\_sflist\_merge\_sflist()

| | void sys\_sflist\_merge\_sflist | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list\_to\_append* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

merge two sflists, appending the second one to the first

When the operation is completed, the appending list is empty. This and other sys\_sflist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | list\_to\_append | A pointer to the list to append. |

## [◆ ](#ga6c993728bebb604f966cdc944939642e)sys\_sflist\_peek\_head()

| | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* sys\_sflist\_peek\_head | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Peek the first node from the list.

Parameters
:   | list | A point on the list to peek the first node from |
    | --- | --- |

Returns
:   A pointer on the first node of the list (or NULL if none)

## [◆ ](#ga514b41f1af89f3f08e216cfede7d5605)sys\_sflist\_peek\_next()

| | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* sys\_sflist\_peek\_next | ( | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *node* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Peek the next node from current node.

Parameters
:   | node | A pointer on the node where to peek the next node |
    | --- | --- |

Returns
:   a pointer on the next node (or NULL if none)

## [◆ ](#gaa67d15dd4fb28dbbc64f4b0e8e21455e)sys\_sflist\_peek\_next\_no\_check()

| | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* sys\_sflist\_peek\_next\_no\_check | ( | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *node* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Peek the next node from current node, node is not NULL.

Faster then [sys\_sflist\_peek\_next()](#ga514b41f1af89f3f08e216cfede7d5605) if node is known not to be NULL.

Parameters
:   | node | A pointer on the node where to peek the next node |
    | --- | --- |

Returns
:   a pointer on the next node (or NULL if none)

## [◆ ](#gabf278ac7912180fc50a25c0ebddc093c)sys\_sflist\_peek\_tail()

| | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* sys\_sflist\_peek\_tail | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Peek the last node from the list.

Parameters
:   | list | A point on the list to peek the last node from |
    | --- | --- |

Returns
:   A pointer on the last node of the list (or NULL if none)

## [◆ ](#ga824ff283c821b6f392ebd81516b65712)sys\_sflist\_prepend()

| | void sys\_sflist\_prepend | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Prepend a node to the given list.

This and other sys\_sflist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | node | A pointer on the node to prepend |

## [◆ ](#ga66c716ef7495fcb04ea60aac340dc5ed)sys\_sflist\_remove()

| | void sys\_sflist\_remove | ( | [sys\_sflist\_t](#ga9e7f835170787303732c805dc7375f66) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *prev\_node*, | |  |  | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Remove a node.

This and other sys\_sflist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | prev\_node | A pointer on the previous node (can be NULL, which means the node is the list's head) |
    | node | A pointer on the node to remove |

## [◆ ](#ga0e258c1faa3cbaee48c29e8f2c11132b)sys\_sfnode\_flags\_get()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sys\_sfnode\_flags\_get | ( | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *node* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Fetch flags value for a particular sfnode.

Parameters
:   | node | A pointer to the node to fetch flags from |
    | --- | --- |

Returns
:   The value of flags, which will be between 0 and 3

## [◆ ](#ga85d82a3a5927f79a5f5655cb3405ce95)sys\_sfnode\_flags\_set()

| | void sys\_sfnode\_flags\_set | ( | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *node*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Set flags value for an sflist node.

Set a flags value for this slist node, which can be a value between 0 and 3. These flags will persist even if the node is moved around within a list, removed, or transplanted to a different slist.

Parameters
:   | node | A pointer to the node to set the flags on |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | A value between 0 and 3 to set the flags value |

## [◆ ](#gae56469b67ad7a92363d04ac726e326ea)sys\_sfnode\_init()

| | void sys\_sfnode\_init | ( | [sys\_sfnode\_t](#ga02dabbe35036cbc11fbbefa99a129cc7) \* | *node*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[sflist.h](sflist_8h.md)>`

Initialize an sflist node.

Set an initial flags value for this slist node, which can be a value between 0 and 3. These flags will persist even if the node is moved around within a list, removed, or transplanted to a different slist.

This is ever so slightly faster than [sys\_sfnode\_flags\_set()](#ga85d82a3a5927f79a5f5655cb3405ce95) and should only be used on a node that hasn't been added to any list.

Parameters
:   | node | A pointer to the node to set the flags on |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | A value between 0 and 3 to set the flags value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
