---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dlist_8h.html
original_path: doxygen/html/dlist_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dlist.h File Reference

`#include <stddef.h>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](dlist_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SYS\_DLIST\_FOR\_EACH\_NODE](group__doubly-linked-list__apis.md#ga3788b5bbd11acc885e7378800a8cf974)(\_\_dl, \_\_dn) |
|  | Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_dn should not be removed. |
| #define | [SYS\_DLIST\_ITERATE\_FROM\_NODE](group__doubly-linked-list__apis.md#ga2bda6ba927f32e1d0b71ad63781b9909)(\_\_dl, \_\_dn) |
|  | Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_dn should not be removed. |
| #define | [SYS\_DLIST\_FOR\_EACH\_NODE\_SAFE](group__doubly-linked-list__apis.md#ga21c5c7dc311eaba99f00fb2eeca736d9)(\_\_dl, \_\_dn, \_\_dns) |
|  | Provide the primitive to safely iterate on a list Note: \_\_dn can be removed, it will not break the loop. |
| #define | [SYS\_DLIST\_CONTAINER](group__doubly-linked-list__apis.md#ga33a8bf65e8095e3b4dcee0b005b79170)(\_\_dn, \_\_cn, \_\_n) |
|  | Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes. |
| #define | [SYS\_DLIST\_PEEK\_HEAD\_CONTAINER](group__doubly-linked-list__apis.md#ga6dc66f3e84d3b79fef461d30b56a0f7c)(\_\_dl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek container of the list head. |
| #define | [SYS\_DLIST\_PEEK\_NEXT\_CONTAINER](group__doubly-linked-list__apis.md#gaffb72234c90286ecf382b93d4db50a19)(\_\_dl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek the next container. |
| #define | [SYS\_DLIST\_FOR\_EACH\_CONTAINER](group__doubly-linked-list__apis.md#gaf9eeb36eef731248c2f57c603feb1b20)(\_\_dl, \_\_cn, \_\_n) |
|  | Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached. |
| #define | [SYS\_DLIST\_FOR\_EACH\_CONTAINER\_SAFE](group__doubly-linked-list__apis.md#gaf07e09986c950b0dd1a0c89d4348f858)(\_\_dl, \_\_cn, \_\_cns, \_\_n) |
|  | Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop. |
| #define | [SYS\_DLIST\_STATIC\_INIT](group__doubly-linked-list__apis.md#ga3681d4600f9cbd9237ea9ce6f67e508d)(ptr\_to\_list) |
|  | Static initializer for a doubly-linked list. |

| Typedefs | |
| --- | --- |
| typedef struct \_dnode | [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) |
|  | Doubly-linked list structure. |
| typedef struct \_dnode | [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) |
|  | Doubly-linked list node structure. |

| Functions | |
| --- | --- |
| static void | [sys\_dlist\_init](group__doubly-linked-list__apis.md#gaf05dbc7d7250990b971796300aaf6c53) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | initialize list to its empty state |
| static void | [sys\_dnode\_init](group__doubly-linked-list__apis.md#gadf15b39af330221921d24505280e7a32) ([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | initialize node to its state when not in a list |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dnode\_is\_linked](group__doubly-linked-list__apis.md#gac725da0c7e65c126a96a9405af84ca41) (const [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | check if a node is a member of any list |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_is\_head](group__doubly-linked-list__apis.md#ga78a2c3d2272ee91578eafbfba3840af4) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | check if a node is the list's head |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_is\_tail](group__doubly-linked-list__apis.md#ga38b8cad6cd6535c8ddc65d623fa967db) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | check if a node is the list's tail |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | check if the list is empty |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_has\_multiple\_nodes](group__doubly-linked-list__apis.md#ga05b1ed491829b98de0200eca523b7829) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | check if more than one node present |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_head](group__doubly-linked-list__apis.md#ga6fc11e4682311b6b368d849e1e421183) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get a reference to the head item in the list |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_head\_not\_empty](group__doubly-linked-list__apis.md#ga7196173f9d59400b52163c2850a22fee) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get a reference to the head item in the list |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_next\_no\_check](group__doubly-linked-list__apis.md#ga84863ceb4ef678a9d3500d0e876e6afb) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the next item in the list, node is not NULL |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_next](group__doubly-linked-list__apis.md#ga76366019520dc4c2ce2735cf747c1a22) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the next item in the list |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_prev\_no\_check](group__doubly-linked-list__apis.md#ga806259b974b7ea6e42feaeab3987f140) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the previous item in the list, node is not NULL |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_prev](group__doubly-linked-list__apis.md#ga23b9f6a10a14c08ccf1fbb7d8518fc43) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the previous item in the list |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_tail](group__doubly-linked-list__apis.md#gac84d0d3aade5677f7840f51f3c65c095) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get a reference to the tail item in the list |
| static void | [sys\_dlist\_append](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | add node to tail of list |
| static void | [sys\_dlist\_prepend](group__doubly-linked-list__apis.md#ga6f21ba50e0de93f54bfefeaabe0c767f) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | add node to head of list |
| static void | [sys\_dlist\_insert](group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071) ([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*successor, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | Insert a node into a list. |
| static void | [sys\_dlist\_insert\_at](group__doubly-linked-list__apis.md#ga667cee0bdd59d8ca3fc82a5bca2bcd48) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node, int(\*cond)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node, void \*data), void \*data) |
|  | insert node at position |
| static void | [sys\_dlist\_remove](group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e) ([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | remove a specific node from a list |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_get](group__doubly-linked-list__apis.md#ga3032394541494771f980e7642ecbc287) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get the first node in a list |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_dlist\_len](group__doubly-linked-list__apis.md#ga9418e906cc333b6a57b092487592c563) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | Compute the size of the given list in O(n) time. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [dlist.h](dlist_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
