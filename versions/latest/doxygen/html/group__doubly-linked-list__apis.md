---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__doubly-linked-list__apis.html
original_path: doxygen/html/group__doubly-linked-list__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Doubly-linked list

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Doubly-linked list implementation.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [SYS\_DLIST\_FOR\_EACH\_NODE](#ga3788b5bbd11acc885e7378800a8cf974)(\_\_dl, \_\_dn) |
|  | Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_dn should not be removed. |
| #define | [SYS\_DLIST\_ITERATE\_FROM\_NODE](#ga2bda6ba927f32e1d0b71ad63781b9909)(\_\_dl, \_\_dn) |
|  | Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_dn should not be removed. |
| #define | [SYS\_DLIST\_FOR\_EACH\_NODE\_SAFE](#ga21c5c7dc311eaba99f00fb2eeca736d9)(\_\_dl, \_\_dn, \_\_dns) |
|  | Provide the primitive to safely iterate on a list Note: \_\_dn can be removed, it will not break the loop. |
| #define | [SYS\_DLIST\_CONTAINER](#ga33a8bf65e8095e3b4dcee0b005b79170)(\_\_dn, \_\_cn, \_\_n) |
|  | Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes. |
| #define | [SYS\_DLIST\_PEEK\_HEAD\_CONTAINER](#ga6dc66f3e84d3b79fef461d30b56a0f7c)(\_\_dl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek container of the list head. |
| #define | [SYS\_DLIST\_PEEK\_NEXT\_CONTAINER](#gaffb72234c90286ecf382b93d4db50a19)(\_\_dl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek the next container. |
| #define | [SYS\_DLIST\_FOR\_EACH\_CONTAINER](#gaf9eeb36eef731248c2f57c603feb1b20)(\_\_dl, \_\_cn, \_\_n) |
|  | Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached. |
| #define | [SYS\_DLIST\_FOR\_EACH\_CONTAINER\_SAFE](#gaf07e09986c950b0dd1a0c89d4348f858)(\_\_dl, \_\_cn, \_\_cns, \_\_n) |
|  | Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop. |
| #define | [SYS\_DLIST\_STATIC\_INIT](#ga3681d4600f9cbd9237ea9ce6f67e508d)(ptr\_to\_list) |
|  | Static initializer for a doubly-linked list. |

| Typedefs | |
| --- | --- |
| typedef struct \_dnode | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) |
|  | Doubly-linked list structure. |
| typedef struct \_dnode | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) |
|  | Doubly-linked list node structure. |

| Functions | |
| --- | --- |
| static void | [sys\_dlist\_init](#gaf05dbc7d7250990b971796300aaf6c53) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | initialize list to its empty state |
| static void | [sys\_dnode\_init](#gadf15b39af330221921d24505280e7a32) ([sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | initialize node to its state when not in a list |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dnode\_is\_linked](#gac725da0c7e65c126a96a9405af84ca41) (const [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | check if a node is a member of any list |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_is\_head](#ga78a2c3d2272ee91578eafbfba3840af4) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | check if a node is the list's head |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_is\_tail](#ga38b8cad6cd6535c8ddc65d623fa967db) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | check if a node is the list's tail |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_is\_empty](#gaaa314b62d8d271071d5603075a961766) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | check if the list is empty |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_has\_multiple\_nodes](#ga05b1ed491829b98de0200eca523b7829) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | check if more than one node present |
| static [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_head](#ga6fc11e4682311b6b368d849e1e421183) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get a reference to the head item in the list |
| static [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_head\_not\_empty](#ga7196173f9d59400b52163c2850a22fee) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get a reference to the head item in the list |
| static [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_next\_no\_check](#ga84863ceb4ef678a9d3500d0e876e6afb) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the next item in the list, node is not NULL |
| static [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_next](#ga76366019520dc4c2ce2735cf747c1a22) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the next item in the list |
| static [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_prev\_no\_check](#ga806259b974b7ea6e42feaeab3987f140) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the previous item in the list, node is not NULL |
| static [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_prev](#ga23b9f6a10a14c08ccf1fbb7d8518fc43) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the previous item in the list |
| static [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_tail](#gac84d0d3aade5677f7840f51f3c65c095) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get a reference to the tail item in the list |
| static void | [sys\_dlist\_append](#ga119cb342faf37cd4e97e6361c7ecabe3) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | add node to tail of list |
| static void | [sys\_dlist\_prepend](#ga6f21ba50e0de93f54bfefeaabe0c767f) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | add node to head of list |
| static void | [sys\_dlist\_insert](#ga94987670c6afd5eabeb9957bb065a071) ([sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*successor, [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | Insert a node into a list. |
| static void | [sys\_dlist\_insert\_at](#ga667cee0bdd59d8ca3fc82a5bca2bcd48) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node, int(\*cond)([sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node, void \*data), void \*data) |
|  | insert node at position |
| static void | [sys\_dlist\_remove](#ga06f88befada25820fba01d2019970e4e) ([sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | remove a specific node from a list |
| static [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_get](#ga3032394541494771f980e7642ecbc287) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get the first node in a list |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_dlist\_len](#ga9418e906cc333b6a57b092487592c563) ([sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | Compute the size of the given list in O(n) time. |

## Detailed Description

Doubly-linked list implementation.

Doubly-linked list implementation using inline macros/functions. This API is not thread safe, and thus if a list is used across threads, calls to functions must be protected with synchronization primitives.

The lists are expected to be initialized such that both the head and tail pointers point to the list itself. Initializing the lists in such a fashion simplifies the adding and removing of nodes to/from the list.

## Macro Definition Documentation

## [◆ ](#ga33a8bf65e8095e3b4dcee0b005b79170)SYS\_DLIST\_CONTAINER

| #define SYS\_DLIST\_CONTAINER | ( |  | *\_\_dn*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[dlist.h](dlist_8h.md)>`

**Value:**

((\_\_dn != NULL) ? [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(\_\_dn, \_\_typeof\_\_(\*\_\_cn), \_\_n) : NULL)

[CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)

#define CONTAINER\_OF(ptr, type, field)

Get a pointer to a structure containing the element.

**Definition** util.h:265

Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes.

Parameters
:   | \_\_dn | A pointer on a [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) to get its container |
    | --- | --- |
    | \_\_cn | Container struct type pointer |
    | \_\_n | The field name of [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) within the container struct |

## [◆ ](#gaf9eeb36eef731248c2f57c603feb1b20)SYS\_DLIST\_FOR\_EACH\_CONTAINER

| #define SYS\_DLIST\_FOR\_EACH\_CONTAINER | ( |  | *\_\_dl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[dlist.h](dlist_8h.md)>`

**Value:**

for (\_\_cn = [SYS\_DLIST\_PEEK\_HEAD\_CONTAINER](#ga6dc66f3e84d3b79fef461d30b56a0f7c)(\_\_dl, \_\_cn, \_\_n); \

\_\_cn != NULL; \

\_\_cn = [SYS\_DLIST\_PEEK\_NEXT\_CONTAINER](#gaffb72234c90286ecf382b93d4db50a19)(\_\_dl, \_\_cn, \_\_n))

[SYS\_DLIST\_PEEK\_HEAD\_CONTAINER](#ga6dc66f3e84d3b79fef461d30b56a0f7c)

#define SYS\_DLIST\_PEEK\_HEAD\_CONTAINER(\_\_dl, \_\_cn, \_\_n)

Provide the primitive to peek container of the list head.

**Definition** dlist.h:142

[SYS\_DLIST\_PEEK\_NEXT\_CONTAINER](#gaffb72234c90286ecf382b93d4db50a19)

#define SYS\_DLIST\_PEEK\_NEXT\_CONTAINER(\_\_dl, \_\_cn, \_\_n)

Provide the primitive to peek the next container.

**Definition** dlist.h:152

Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_DLIST_FOR_EACH_CONTAINER(l, c, n) {
    <user code>
}
```

Parameters
:   | \_\_dl | A pointer on a [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) to iterate on |
    | --- | --- |
    | \_\_cn | A container struct type pointer to peek each entry of the list |
    | \_\_n | The field name of [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) within the container struct |

## [◆ ](#gaf07e09986c950b0dd1a0c89d4348f858)SYS\_DLIST\_FOR\_EACH\_CONTAINER\_SAFE

| #define SYS\_DLIST\_FOR\_EACH\_CONTAINER\_SAFE | ( |  | *\_\_dl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_cns*, |
|  |  |  | *\_\_n* ) |

`#include <[dlist.h](dlist_8h.md)>`

**Value:**

for (\_\_cn = [SYS\_DLIST\_PEEK\_HEAD\_CONTAINER](#ga6dc66f3e84d3b79fef461d30b56a0f7c)(\_\_dl, \_\_cn, \_\_n), \

\_\_cns = [SYS\_DLIST\_PEEK\_NEXT\_CONTAINER](#gaffb72234c90286ecf382b93d4db50a19)(\_\_dl, \_\_cn, \_\_n); \

\_\_cn != NULL; \_\_cn = \_\_cns, \

\_\_cns = [SYS\_DLIST\_PEEK\_NEXT\_CONTAINER](#gaffb72234c90286ecf382b93d4db50a19)(\_\_dl, \_\_cn, \_\_n))

Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_DLIST_FOR_EACH_CONTAINER_SAFE(l, c, cn, n) {
    <user code>
}
```

Parameters
:   | \_\_dl | A pointer on a [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) to iterate on |
    | --- | --- |
    | \_\_cn | A container struct type pointer to peek each entry of the list |
    | \_\_cns | A container struct type pointer for the loop to run safely |
    | \_\_n | The field name of [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) within the container struct |

## [◆ ](#ga3788b5bbd11acc885e7378800a8cf974)SYS\_DLIST\_FOR\_EACH\_NODE

| #define SYS\_DLIST\_FOR\_EACH\_NODE | ( |  | *\_\_dl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_dn* ) |

`#include <[dlist.h](dlist_8h.md)>`

**Value:**

for (\_\_dn = [sys\_dlist\_peek\_head](#ga6fc11e4682311b6b368d849e1e421183)(\_\_dl); \_\_dn != NULL; \

\_\_dn = [sys\_dlist\_peek\_next](#ga76366019520dc4c2ce2735cf747c1a22)(\_\_dl, \_\_dn))

[sys\_dlist\_peek\_head](#ga6fc11e4682311b6b368d849e1e421183)

static sys\_dnode\_t \* sys\_dlist\_peek\_head(sys\_dlist\_t \*list)

get a reference to the head item in the list

**Definition** dlist.h:303

[sys\_dlist\_peek\_next](#ga76366019520dc4c2ce2735cf747c1a22)

static sys\_dnode\_t \* sys\_dlist\_peek\_next(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

get a reference to the next item in the list

**Definition** dlist.h:350

Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_dn should not be removed.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_DLIST_FOR_EACH_NODE(l, n) {
    <user code>
}
```

This and other SYS\_DLIST\_\*() macros are not thread safe.

Parameters
:   | \_\_dl | A pointer on a [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) to iterate on |
    | --- | --- |
    | \_\_dn | A [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) pointer to peek each node of the list |

## [◆ ](#ga21c5c7dc311eaba99f00fb2eeca736d9)SYS\_DLIST\_FOR\_EACH\_NODE\_SAFE

| #define SYS\_DLIST\_FOR\_EACH\_NODE\_SAFE | ( |  | *\_\_dl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_dn*, |
|  |  |  | *\_\_dns* ) |

`#include <[dlist.h](dlist_8h.md)>`

**Value:**

for (\_\_dn = [sys\_dlist\_peek\_head](#ga6fc11e4682311b6b368d849e1e421183)(\_\_dl), \

\_\_dns = [sys\_dlist\_peek\_next](#ga76366019520dc4c2ce2735cf747c1a22)(\_\_dl, \_\_dn); \

\_\_dn != NULL; \_\_dn = \_\_dns, \

\_\_dns = [sys\_dlist\_peek\_next](#ga76366019520dc4c2ce2735cf747c1a22)(\_\_dl, \_\_dn))

Provide the primitive to safely iterate on a list Note: \_\_dn can be removed, it will not break the loop.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_DLIST_FOR_EACH_NODE_SAFE(l, n, s) {
    <user code>
}
```

This and other SYS\_DLIST\_\*() macros are not thread safe.

Parameters
:   | \_\_dl | A pointer on a [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) to iterate on |
    | --- | --- |
    | \_\_dn | A [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) pointer to peek each node of the list |
    | \_\_dns | A [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) pointer for the loop to run safely |

## [◆ ](#ga2bda6ba927f32e1d0b71ad63781b9909)SYS\_DLIST\_ITERATE\_FROM\_NODE

| #define SYS\_DLIST\_ITERATE\_FROM\_NODE | ( |  | *\_\_dl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_dn* ) |

`#include <[dlist.h](dlist_8h.md)>`

**Value:**

for (\_\_dn = \_\_dn ? [sys\_dlist\_peek\_next\_no\_check](#ga84863ceb4ef678a9d3500d0e876e6afb)(\_\_dl, \_\_dn) \

: [sys\_dlist\_peek\_head](#ga6fc11e4682311b6b368d849e1e421183)(\_\_dl); \

\_\_dn != NULL; \

\_\_dn = [sys\_dlist\_peek\_next](#ga76366019520dc4c2ce2735cf747c1a22)(\_\_dl, \_\_dn))

[sys\_dlist\_peek\_next\_no\_check](#ga84863ceb4ef678a9d3500d0e876e6afb)

static sys\_dnode\_t \* sys\_dlist\_peek\_next\_no\_check(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

get a reference to the next item in the list, node is not NULL

**Definition** dlist.h:334

Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_dn should not be removed.

User *MUST* add the loop statement curly braces enclosing its own code:

```
SYS_DLIST_ITERATE_FROM_NODE(l, n) {
    <user code>
}
```

Like [SYS\_DLIST\_FOR\_EACH\_NODE()](#ga3788b5bbd11acc885e7378800a8cf974), but \_\_dn already contains a node in the list where to start searching for the next entry from. If NULL, it starts from the head.

This and other SYS\_DLIST\_\*() macros are not thread safe.

Parameters
:   | \_\_dl | A pointer on a [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) to iterate on |
    | --- | --- |
    | \_\_dn | A [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) pointer to peek each node of the list; it contains the starting node, or NULL to start from the head |

## [◆ ](#ga6dc66f3e84d3b79fef461d30b56a0f7c)SYS\_DLIST\_PEEK\_HEAD\_CONTAINER

| #define SYS\_DLIST\_PEEK\_HEAD\_CONTAINER | ( |  | *\_\_dl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[dlist.h](dlist_8h.md)>`

**Value:**

[SYS\_DLIST\_CONTAINER](#ga33a8bf65e8095e3b4dcee0b005b79170)([sys\_dlist\_peek\_head](#ga6fc11e4682311b6b368d849e1e421183)(\_\_dl), \_\_cn, \_\_n)

[SYS\_DLIST\_CONTAINER](#ga33a8bf65e8095e3b4dcee0b005b79170)

#define SYS\_DLIST\_CONTAINER(\_\_dn, \_\_cn, \_\_n)

Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL point...

**Definition** dlist.h:133

Provide the primitive to peek container of the list head.

Parameters
:   | \_\_dl | A pointer on a [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) to peek |
    | --- | --- |
    | \_\_cn | Container struct type pointer |
    | \_\_n | The field name of [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) within the container struct |

## [◆ ](#gaffb72234c90286ecf382b93d4db50a19)SYS\_DLIST\_PEEK\_NEXT\_CONTAINER

| #define SYS\_DLIST\_PEEK\_NEXT\_CONTAINER | ( |  | *\_\_dl*, |
| --- | --- | --- | --- |
|  |  |  | *\_\_cn*, |
|  |  |  | *\_\_n* ) |

`#include <[dlist.h](dlist_8h.md)>`

**Value:**

((\_\_cn != NULL) ? \

SYS\_DLIST\_CONTAINER([sys\_dlist\_peek\_next](#ga76366019520dc4c2ce2735cf747c1a22)(\_\_dl, &(\_\_cn->\_\_n)), \

\_\_cn, \_\_n) : NULL)

Provide the primitive to peek the next container.

Parameters
:   | \_\_dl | A pointer on a [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) to peek |
    | --- | --- |
    | \_\_cn | Container struct type pointer |
    | \_\_n | The field name of [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) within the container struct |

## [◆ ](#ga3681d4600f9cbd9237ea9ce6f67e508d)SYS\_DLIST\_STATIC\_INIT

| #define SYS\_DLIST\_STATIC\_INIT | ( |  | *ptr\_to\_list* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

**Value:**

{ {(ptr\_to\_list)}, {(ptr\_to\_list)} }

Static initializer for a doubly-linked list.

## Typedef Documentation

## [◆ ](#gaa03f9557215b486fee1039dd4c07e683)sys\_dlist\_t

| typedef struct \_dnode [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) |
| --- |

`#include <[dlist.h](dlist_8h.md)>`

Doubly-linked list structure.

## [◆ ](#ga57fdb936802a617d16c00ab08cd2ad98)sys\_dnode\_t

| typedef struct \_dnode [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) |
| --- |

`#include <[dlist.h](dlist_8h.md)>`

Doubly-linked list node structure.

## Function Documentation

## [◆ ](#ga119cb342faf37cd4e97e6361c7ecabe3)sys\_dlist\_append()

| | void sys\_dlist\_append | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

add node to tail of list

This and other sys\_dlist\_\*() functions are not thread safe.

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |
    | node | the element to append |

## [◆ ](#ga3032394541494771f980e7642ecbc287)sys\_dlist\_get()

| | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* sys\_dlist\_get | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

get the first node in a list

This and other sys\_dlist\_\*() functions are not thread safe.

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |

Returns
:   the first node in the list, NULL if list is empty

## [◆ ](#ga05b1ed491829b98de0200eca523b7829)sys\_dlist\_has\_multiple\_nodes()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_dlist\_has\_multiple\_nodes | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

check if more than one node present

This and other sys\_dlist\_\*() functions are not thread safe.

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |

Returns
:   true if multiple nodes, false otherwise

## [◆ ](#gaf05dbc7d7250990b971796300aaf6c53)sys\_dlist\_init()

| | void sys\_dlist\_init | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

initialize list to its empty state

Parameters
:   | list | the doubly-linked list |
    | --- | --- |

## [◆ ](#ga94987670c6afd5eabeb9957bb065a071)sys\_dlist\_insert()

| | void sys\_dlist\_insert | ( | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *successor*, | | --- | --- | --- | --- | |  |  | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

Insert a node into a list.

Insert a node before a specified node in a dlist.

Parameters
:   | successor | the position before which "node" will be inserted |
    | --- | --- |
    | node | the element to insert |

## [◆ ](#ga667cee0bdd59d8ca3fc82a5bca2bcd48)sys\_dlist\_insert\_at()

| | void sys\_dlist\_insert\_at | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node*, | |  |  | int(\* | *cond*)([sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \*node, void \*data), | |  |  | void \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

insert node at position

Insert a node in a location depending on a external condition. The cond() function checks if the node is to be inserted *before* the current node against which it is checked. This and other sys\_dlist\_\*() functions are not thread safe.

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |
    | node | the element to insert |
    | cond | a function that determines if the current node is the correct insert point |
    | data | parameter to cond() |

## [◆ ](#gaaa314b62d8d271071d5603075a961766)sys\_dlist\_is\_empty()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_dlist\_is\_empty | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

check if the list is empty

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |

Returns
:   true if empty, false otherwise

## [◆ ](#ga78a2c3d2272ee91578eafbfba3840af4)sys\_dlist\_is\_head()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_dlist\_is\_head | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

check if a node is the list's head

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |
    | node | the node to check |

Returns
:   true if node is the head, false otherwise

## [◆ ](#ga38b8cad6cd6535c8ddc65d623fa967db)sys\_dlist\_is\_tail()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_dlist\_is\_tail | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

check if a node is the list's tail

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |
    | node | the node to check |

Returns
:   true if node is the tail, false otherwise

## [◆ ](#ga9418e906cc333b6a57b092487592c563)sys\_dlist\_len()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sys\_dlist\_len | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

Compute the size of the given list in O(n) time.

Parameters
:   | list | A pointer on the list |
    | --- | --- |

Returns
:   an integer equal to the size of the list, or 0 if empty

## [◆ ](#ga6fc11e4682311b6b368d849e1e421183)sys\_dlist\_peek\_head()

| | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* sys\_dlist\_peek\_head | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

get a reference to the head item in the list

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |

Returns
:   a pointer to the head element, NULL if list is empty

## [◆ ](#ga7196173f9d59400b52163c2850a22fee)sys\_dlist\_peek\_head\_not\_empty()

| | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* sys\_dlist\_peek\_head\_not\_empty | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

get a reference to the head item in the list

The list must be known to be non-empty.

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |

Returns
:   a pointer to the head element

## [◆ ](#ga76366019520dc4c2ce2735cf747c1a22)sys\_dlist\_peek\_next()

| | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* sys\_dlist\_peek\_next | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

get a reference to the next item in the list

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |
    | node | the node from which to get the next element in the list |

Returns
:   a pointer to the next element from a node, NULL if node is the tail or NULL (when node comes from reading the head of an empty list).

## [◆ ](#ga84863ceb4ef678a9d3500d0e876e6afb)sys\_dlist\_peek\_next\_no\_check()

| | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* sys\_dlist\_peek\_next\_no\_check | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

get a reference to the next item in the list, node is not NULL

Faster than [sys\_dlist\_peek\_next()](#ga76366019520dc4c2ce2735cf747c1a22) if node is known not to be NULL.

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |
    | node | the node from which to get the next element in the list |

Returns
:   a pointer to the next element from a node, NULL if node is the tail

## [◆ ](#ga23b9f6a10a14c08ccf1fbb7d8518fc43)sys\_dlist\_peek\_prev()

| | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* sys\_dlist\_peek\_prev | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

get a reference to the previous item in the list

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |
    | node | the node from which to get the previous element in the list |

Returns
:   a pointer to the previous element from a node, NULL if node is the tail or NULL (when node comes from reading the head of an empty list).

## [◆ ](#ga806259b974b7ea6e42feaeab3987f140)sys\_dlist\_peek\_prev\_no\_check()

| | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* sys\_dlist\_peek\_prev\_no\_check | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

get a reference to the previous item in the list, node is not NULL

Faster than [sys\_dlist\_peek\_prev()](#ga23b9f6a10a14c08ccf1fbb7d8518fc43) if node is known not to be NULL.

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |
    | node | the node from which to get the previous element in the list |

Returns
:   a pointer to the previous element from a node, NULL if node is the tail

## [◆ ](#gac84d0d3aade5677f7840f51f3c65c095)sys\_dlist\_peek\_tail()

| | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* sys\_dlist\_peek\_tail | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

get a reference to the tail item in the list

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |

Returns
:   a pointer to the tail element, NULL if list is empty

## [◆ ](#ga6f21ba50e0de93f54bfefeaabe0c767f)sys\_dlist\_prepend()

| | void sys\_dlist\_prepend | ( | [sys\_dlist\_t](#gaa03f9557215b486fee1039dd4c07e683) \* | *list*, | | --- | --- | --- | --- | |  |  | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

add node to head of list

This and other sys\_dlist\_\*() functions are not thread safe.

Parameters
:   | list | the doubly-linked list to operate on |
    | --- | --- |
    | node | the element to append |

## [◆ ](#ga06f88befada25820fba01d2019970e4e)sys\_dlist\_remove()

| | void sys\_dlist\_remove | ( | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

remove a specific node from a list

The list is implicit from the node. The node must be part of a list. This and other sys\_dlist\_\*() functions are not thread safe.

Parameters
:   | node | the node to remove |
    | --- | --- |

## [◆ ](#gadf15b39af330221921d24505280e7a32)sys\_dnode\_init()

| | void sys\_dnode\_init | ( | [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

initialize node to its state when not in a list

Parameters
:   | node | the node |
    | --- | --- |

## [◆ ](#gac725da0c7e65c126a96a9405af84ca41)sys\_dnode\_is\_linked()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_dnode\_is\_linked | ( | const [sys\_dnode\_t](#ga57fdb936802a617d16c00ab08cd2ad98) \* | *node* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dlist.h](dlist_8h.md)>`

check if a node is a member of any list

Parameters
:   | node | the node |
    | --- | --- |

Returns
:   true if node is linked into a list, false if it is not

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
