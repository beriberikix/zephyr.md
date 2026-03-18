---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__single-linked-list__apis.html
original_path: doxygen/html/group__single-linked-list__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Single-linked list

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Single-linked list implementation.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [SYS\_SLIST\_FOR\_EACH\_NODE](#gaf32ac0f222186e497d3f6180b6c26352)(\_\_sl, \_\_sn) |
|  | Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_sn should not be removed. |
| #define | [SYS\_SLIST\_ITERATE\_FROM\_NODE](#ga1740075b07ec67635c1934dcbe1b5cee)(\_\_sl, \_\_sn) |
|  | Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_sn should not be removed. |
| #define | [SYS\_SLIST\_FOR\_EACH\_NODE\_SAFE](#gad6f1014e26d6cf9925d00b4f53076116)(\_\_sl, \_\_sn, \_\_sns) |
|  | Provide the primitive to safely iterate on a list Note: \_\_sn can be removed, it will not break the loop. |
| #define | [SYS\_SLIST\_CONTAINER](#ga07e4257835751e18a6c06bfa5f9c25e8)(\_\_ln, \_\_cn, \_\_n) |
|  | Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes. |
| #define | [SYS\_SLIST\_PEEK\_HEAD\_CONTAINER](#ga8fdb1e6baa7ba061dc1bd35f73a2fff1)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek container of the list head. |
| #define | [SYS\_SLIST\_PEEK\_TAIL\_CONTAINER](#ga709c87e180d48c782c1583d7fb7629b3)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek container of the list tail. |
| #define | [SYS\_SLIST\_PEEK\_NEXT\_CONTAINER](#ga5d1c9ee21f75da485ba12aa56471e699)(\_\_cn, \_\_n) |
|  | Provide the primitive to peek the next container. |
| #define | [SYS\_SLIST\_FOR\_EACH\_CONTAINER](#gacd97d2f1044c0560d96c9f9a6f26d2f6)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached. |
| #define | [SYS\_SLIST\_FOR\_EACH\_CONTAINER\_SAFE](#gacf3aaf32a6a3389229b548588c6d655e)(\_\_sl, \_\_cn, \_\_cns, \_\_n) |
|  | Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop. |
| #define | [SYS\_SLIST\_STATIC\_INIT](#ga7f4710125f45643b7acdaa58dbfff225)(ptr\_to\_list) |
|  | Statically initialize a single-linked list. |

| Typedefs | |
| --- | --- |
| typedef struct \_snode | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) |
|  | Single-linked list node structure. |
| typedef struct \_slist | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) |
|  | Single-linked list structure. |

| Functions | |
| --- | --- |
| static void | [sys\_slist\_init](#ga913aea7661b4ab3b4b50a8efc0d70428) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Initialize a list. |
| static [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_peek\_head](#ga1af7fbf228545d591ef8961fa5f6a8f1) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Peek the first node from the list. |
| static [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_peek\_tail](#ga49975721fa11c48000669d2c4ec0877f) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Peek the last node from the list. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_slist\_is\_empty](#ga7d729bbb7bba57c5784ad0d2c341670a) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Test if the given list is empty. |
| static [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_peek\_next\_no\_check](#ga58d001a256f28278f0e7c0b96b9cc492) ([sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Peek the next node from current node, node is not NULL. |
| static [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_peek\_next](#ga729cbf8cafdbc34261db9274195ac5df) ([sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Peek the next node from current node. |
| static void | [sys\_slist\_prepend](#gac962e3ec8440e4adb2ba6682dbf186ff) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Prepend a node to the given list. |
| static void | [sys\_slist\_append](#ga829fd7b6f1944dc38e10685e861e62b5) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Append a node to the given list. |
| static void | [sys\_slist\_append\_list](#gaaf7393c6bbf6d5cbd303173d95269481) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list, void \*head, void \*tail) |
|  | Append a list to the given list. |
| static void | [sys\_slist\_merge\_slist](#ga0c00bbb3dc6903f386fdb1e37fdd3b66) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list\_to\_append) |
|  | merge two slists, appending the second one to the first |
| static void | [sys\_slist\_insert](#gadcbef5c013861fdfd325bae357c37b85) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*prev, [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Insert a node to the given list. |
| static [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_get\_not\_empty](#ga036a65b86f101a7867a83cdd1617ba33) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Fetch and remove the first node of the given list. |
| static [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_get](#ga497d7e9069c08e25a03ebc212ef8bbb3) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Fetch and remove the first node of the given list. |
| static void | [sys\_slist\_remove](#gaee6957483d4fbe3b824f7a495d56030f) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*prev\_node, [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Remove a node. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_slist\_find\_and\_remove](#ga296560229ffdfd0054c9c7b0602825a6) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Find and remove a node from a list. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_slist\_find](#gaca24163d9f029c1b78e4637349d2ef92) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*node, [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*\*prev) |
|  | Find if a node is already linked in a singly linked list. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_slist\_len](#ga02a4d013fa37aca2943effe3afa0567b) ([sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Compute the size of the given list in O(n) time. |

## Detailed Description

Single-linked list implementation.

Single-linked list implementation using inline macros/functions. This API is not thread safe, and thus if a list is used across threads, calls to functions must be protected with synchronization primitives.

## Macro Definition Documentation

## [◆ ](#ga07e4257835751e18a6c06bfa5f9c25e8)SYS\_SLIST\_CONTAINER

| #define SYS\_SLIST\_CONTAINER | ( |  | *\_\_ln*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[slist.h](slist_8h.md)>`

**Value:**

Z\_GENLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n)

Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes.

Parameters
:   | \_\_ln | A pointer on a sys\_node\_t to get its container |
    | --- | --- |
    | \_\_cn | Container struct type pointer |
    | \_\_n | The field name of sys\_node\_t within the container struct |

## [◆ ](#gacd97d2f1044c0560d96c9f9a6f26d2f6)SYS\_SLIST\_FOR\_EACH\_CONTAINER

| #define SYS\_SLIST\_FOR\_EACH\_CONTAINER | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[slist.h](slist_8h.md)>`

**Value:**

Z\_GENLIST\_FOR\_EACH\_CONTAINER(slist, \_\_sl, \_\_cn, \_\_n)

Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_SLIST_FOR_EACH_CONTAINER(l, c, n) {
    <user code>
}
```

Parameters
:   | \_\_sl | A pointer on a [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) to iterate on |
    | --- | --- |
    | \_\_cn | A pointer to peek each entry of the list |
    | \_\_n | The field name of sys\_node\_t within the container struct |

## [◆ ](#gacf3aaf32a6a3389229b548588c6d655e)SYS\_SLIST\_FOR\_EACH\_CONTAINER\_SAFE

| #define SYS\_SLIST\_FOR\_EACH\_CONTAINER\_SAFE | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_cns*, |
|  |  |  | *\_\_n* ) |

`#include <[slist.h](slist_8h.md)>`

**Value:**

Z\_GENLIST\_FOR\_EACH\_CONTAINER\_SAFE(slist, \_\_sl, \_\_cn, \_\_cns, \_\_n)

Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_SLIST_FOR_EACH_NODE_SAFE(l, c, cn, n) {
    <user code>
}
```

Parameters
:   | \_\_sl | A pointer on a [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) to iterate on |
    | --- | --- |
    | \_\_cn | A pointer to peek each entry of the list |
    | \_\_cns | A pointer for the loop to run safely |
    | \_\_n | The field name of sys\_node\_t within the container struct |

## [◆ ](#gaf32ac0f222186e497d3f6180b6c26352)SYS\_SLIST\_FOR\_EACH\_NODE

| #define SYS\_SLIST\_FOR\_EACH\_NODE | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_sn* ) |

`#include <[slist.h](slist_8h.md)>`

**Value:**

Z\_GENLIST\_FOR\_EACH\_NODE(slist, \_\_sl, \_\_sn)

Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_sn should not be removed.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_SLIST_FOR_EACH_NODE(l, n) {
    <user code>
}
```

This and other SYS\_SLIST\_\*() macros are not thread safe.

Parameters
:   | \_\_sl | A pointer on a [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) to iterate on |
    | --- | --- |
    | \_\_sn | A [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) pointer to peek each node of the list |

## [◆ ](#gad6f1014e26d6cf9925d00b4f53076116)SYS\_SLIST\_FOR\_EACH\_NODE\_SAFE

| #define SYS\_SLIST\_FOR\_EACH\_NODE\_SAFE | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_sn*, |
|  |  |  | *\_\_sns* ) |

`#include <[slist.h](slist_8h.md)>`

**Value:**

Z\_GENLIST\_FOR\_EACH\_NODE\_SAFE(slist, \_\_sl, \_\_sn, \_\_sns)

Provide the primitive to safely iterate on a list Note: \_\_sn can be removed, it will not break the loop.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_SLIST_FOR_EACH_NODE_SAFE(l, n, s) {
    <user code>
}
```

This and other SYS\_SLIST\_\*() macros are not thread safe.

Parameters
:   | \_\_sl | A pointer on a [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) to iterate on |
    | --- | --- |
    | \_\_sn | A [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) pointer to peek each node of the list |
    | \_\_sns | A [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) pointer for the loop to run safely |

## [◆ ](#ga1740075b07ec67635c1934dcbe1b5cee)SYS\_SLIST\_ITERATE\_FROM\_NODE

| #define SYS\_SLIST\_ITERATE\_FROM\_NODE | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_sn* ) |

`#include <[slist.h](slist_8h.md)>`

**Value:**

Z\_GENLIST\_ITERATE\_FROM\_NODE(slist, \_\_sl, \_\_sn)

Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_sn should not be removed.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_SLIST_ITERATE_FROM_NODE(l, n) {
    <user code>
}
```

Like [SYS\_SLIST\_FOR\_EACH\_NODE()](#gaf32ac0f222186e497d3f6180b6c26352), but \_\_dn already contains a node in the list where to start searching for the next entry from. If NULL, it starts from the head.

This and other SYS\_SLIST\_\*() macros are not thread safe.

Parameters
:   | \_\_sl | A pointer on a [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) to iterate on |
    | --- | --- |
    | \_\_sn | A [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) pointer to peek each node of the list it contains the starting node, or NULL to start from the head |

## [◆ ](#ga8fdb1e6baa7ba061dc1bd35f73a2fff1)SYS\_SLIST\_PEEK\_HEAD\_CONTAINER

| #define SYS\_SLIST\_PEEK\_HEAD\_CONTAINER | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[slist.h](slist_8h.md)>`

**Value:**

Z\_GENLIST\_PEEK\_HEAD\_CONTAINER(slist, \_\_sl, \_\_cn, \_\_n)

Provide the primitive to peek container of the list head.

Parameters
:   | \_\_sl | A pointer on a [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) to peek |
    | --- | --- |
    | \_\_cn | Container struct type pointer |
    | \_\_n | The field name of sys\_node\_t within the container struct |

## [◆ ](#ga5d1c9ee21f75da485ba12aa56471e699)SYS\_SLIST\_PEEK\_NEXT\_CONTAINER

| #define SYS\_SLIST\_PEEK\_NEXT\_CONTAINER | ( |  | *\_\_cn*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_n* ) |

`#include <[slist.h](slist_8h.md)>`

**Value:**

Z\_GENLIST\_PEEK\_NEXT\_CONTAINER(slist, \_\_cn, \_\_n)

Provide the primitive to peek the next container.

Parameters
:   | \_\_cn | Container struct type pointer |
    | --- | --- |
    | \_\_n | The field name of sys\_node\_t within the container struct |

## [◆ ](#ga709c87e180d48c782c1583d7fb7629b3)SYS\_SLIST\_PEEK\_TAIL\_CONTAINER

| #define SYS\_SLIST\_PEEK\_TAIL\_CONTAINER | ( |  | *\_\_sl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[slist.h](slist_8h.md)>`

**Value:**

Z\_GENLIST\_PEEK\_TAIL\_CONTAINER(slist, \_\_sl, \_\_cn, \_\_n)

Provide the primitive to peek container of the list tail.

Parameters
:   | \_\_sl | A pointer on a [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) to peek |
    | --- | --- |
    | \_\_cn | Container struct type pointer |
    | \_\_n | The field name of sys\_node\_t within the container struct |

## [◆ ](#ga7f4710125f45643b7acdaa58dbfff225)SYS\_SLIST\_STATIC\_INIT

| #define SYS\_SLIST\_STATIC\_INIT | ( |  | *ptr\_to\_list* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

**Value:**

{NULL, NULL}

Statically initialize a single-linked list.

Parameters
:   | ptr\_to\_list | A pointer on the list to initialize |
    | --- | --- |

## Typedef Documentation

## [◆ ](#ga44658c336b634c03938a251cdc8134f8)sys\_slist\_t

| typedef struct \_slist [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) |
| --- |

`#include <[slist.h](slist_8h.md)>`

Single-linked list structure.

## [◆ ](#ga69bf43aad81e3ee2d55250c59b857493)sys\_snode\_t

| typedef struct \_snode [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) |
| --- |

`#include <[slist.h](slist_8h.md)>`

Single-linked list node structure.

## Function Documentation

## [◆ ](#ga829fd7b6f1944dc38e10685e861e62b5)sys\_slist\_append()

| | void sys\_slist\_append | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Append a node to the given list.

This and other sys\_slist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | node | A pointer on the node to append |

## [◆ ](#gaaf7393c6bbf6d5cbd303173d95269481)sys\_slist\_append\_list()

| | void sys\_slist\_append\_list | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list*, | | --- | --- | --- | --- | |  |  | void \* | *head*, | |  |  | void \* | *tail* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Append a list to the given list.

Append a singly-linked, NULL-terminated list consisting of nodes containing the pointer to the next node as the first element of a node, to *list*. This and other sys\_slist\_\*() functions are not thread safe.

FIXME: Why are the element parameters void \*?

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | head | A pointer to the first element of the list to append |
    | tail | A pointer to the last element of the list to append |

## [◆ ](#gaca24163d9f029c1b78e4637349d2ef92)sys\_slist\_find()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_slist\_find | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | *node*, | |  |  | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \*\* | *prev* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Find if a node is already linked in a singly linked list.

This and other sys\_slist\_\*() functions are not thread safe.

Parameters
:   |  | list | A pointer to the list to check |
    | --- | --- | --- |
    |  | node | A pointer to the node to search in the list |
    | [out] | prev | A pointer to the previous node |

Returns
:   true if node was found in the list, false otherwise

## [◆ ](#ga296560229ffdfd0054c9c7b0602825a6)sys\_slist\_find\_and\_remove()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_slist\_find\_and\_remove | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Find and remove a node from a list.

This and other sys\_slist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | node | A pointer on the node to remove from the list |

Returns
:   true if node was removed

## [◆ ](#ga497d7e9069c08e25a03ebc212ef8bbb3)sys\_slist\_get()

| | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* sys\_slist\_get | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Fetch and remove the first node of the given list.

This and other sys\_slist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |

Returns
:   A pointer to the first node of the list (or NULL if empty)

## [◆ ](#ga036a65b86f101a7867a83cdd1617ba33)sys\_slist\_get\_not\_empty()

| | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* sys\_slist\_get\_not\_empty | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Fetch and remove the first node of the given list.

List must be known to be non-empty. This and other sys\_slist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |

Returns
:   A pointer to the first node of the list

## [◆ ](#ga913aea7661b4ab3b4b50a8efc0d70428)sys\_slist\_init()

| | void sys\_slist\_init | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Initialize a list.

Parameters
:   | list | A pointer on the list to initialize |
    | --- | --- |

## [◆ ](#gadcbef5c013861fdfd325bae357c37b85)sys\_slist\_insert()

| | void sys\_slist\_insert | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | *prev*, | |  |  | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Insert a node to the given list.

This and other sys\_slist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | prev | A pointer on the previous node |
    | node | A pointer on the node to insert |

## [◆ ](#ga7d729bbb7bba57c5784ad0d2c341670a)sys\_slist\_is\_empty()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_slist\_is\_empty | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Test if the given list is empty.

Parameters
:   | list | A pointer on the list to test |
    | --- | --- |

Returns
:   a boolean, true if it's empty, false otherwise

## [◆ ](#ga02a4d013fa37aca2943effe3afa0567b)sys\_slist\_len()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_slist\_len | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Compute the size of the given list in O(n) time.

Parameters
:   | list | A pointer on the list |
    | --- | --- |

Returns
:   an integer equal to the size of the list, or 0 if empty

## [◆ ](#ga0c00bbb3dc6903f386fdb1e37fdd3b66)sys\_slist\_merge\_slist()

| | void sys\_slist\_merge\_slist | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list\_to\_append* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

merge two slists, appending the second one to the first

When the operation is completed, the appending list is empty. This and other sys\_slist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | list\_to\_append | A pointer to the list to append. |

## [◆ ](#ga1af7fbf228545d591ef8961fa5f6a8f1)sys\_slist\_peek\_head()

| | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* sys\_slist\_peek\_head | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Peek the first node from the list.

Parameters
:   | list | A point on the list to peek the first node from |
    | --- | --- |

Returns
:   A pointer on the first node of the list (or NULL if none)

## [◆ ](#ga729cbf8cafdbc34261db9274195ac5df)sys\_slist\_peek\_next()

| | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* sys\_slist\_peek\_next | ( | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | *node* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Peek the next node from current node.

Parameters
:   | node | A pointer on the node where to peek the next node |
    | --- | --- |

Returns
:   a pointer on the next node (or NULL if none)

## [◆ ](#ga58d001a256f28278f0e7c0b96b9cc492)sys\_slist\_peek\_next\_no\_check()

| | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* sys\_slist\_peek\_next\_no\_check | ( | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | *node* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Peek the next node from current node, node is not NULL.

Faster then [sys\_slist\_peek\_next()](#ga729cbf8cafdbc34261db9274195ac5df) if node is known not to be NULL.

Parameters
:   | node | A pointer on the node where to peek the next node |
    | --- | --- |

Returns
:   a pointer on the next node (or NULL if none)

## [◆ ](#ga49975721fa11c48000669d2c4ec0877f)sys\_slist\_peek\_tail()

| | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* sys\_slist\_peek\_tail | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Peek the last node from the list.

Parameters
:   | list | A point on the list to peek the last node from |
    | --- | --- |

Returns
:   A pointer on the last node of the list (or NULL if none)

## [◆ ](#gac962e3ec8440e4adb2ba6682dbf186ff)sys\_slist\_prepend()

| | void sys\_slist\_prepend | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Prepend a node to the given list.

This and other sys\_slist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | node | A pointer on the node to prepend |

## [◆ ](#gaee6957483d4fbe3b824f7a495d56030f)sys\_slist\_remove()

| | void sys\_slist\_remove | ( | [sys\_slist\_t](#ga44658c336b634c03938a251cdc8134f8) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | *prev\_node*, | |  |  | [sys\_snode\_t](#ga69bf43aad81e3ee2d55250c59b857493) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[slist.h](slist_8h.md)>`

Remove a node.

This and other sys\_slist\_\*() functions are not thread safe.

Parameters
:   | list | A pointer on the list to affect |
    | --- | --- |
    | prev\_node | A pointer on the previous node (can be NULL, which means the node is the list's head) |
    | node | A pointer on the node to remove |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
