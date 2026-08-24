---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/dlist_8h.html
original_path: doxygen/html/dlist_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_is\_head](group__doubly-linked-list__apis.md#gafc47ac9ba916c585cf527deb9df4ada2) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, const [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | check if a node is the list's head |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_is\_tail](group__doubly-linked-list__apis.md#ga336288dfb1d6293567743018171090a4) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, const [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | check if a node is the list's tail |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaa44b9aa0cf3910e5f2884c3cd6b0b01e) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | check if the list is empty |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_dlist\_has\_multiple\_nodes](group__doubly-linked-list__apis.md#ga397bae1a777af7b008e9d24fe7dd6608) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | check if more than one node present |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_head](group__doubly-linked-list__apis.md#ga07567e9c1baeb92577daf39134b83568) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get a reference to the head item in the list |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_head\_not\_empty](group__doubly-linked-list__apis.md#ga6be5281719ce432fe1b34be64bbdfcfb) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get a reference to the head item in the list |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_next\_no\_check](group__doubly-linked-list__apis.md#ga12be5af77a8941913d8ba0e4cbd97122) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, const [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the next item in the list, node is not NULL |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_next](group__doubly-linked-list__apis.md#ga6aa98dd8c6365fa74956ee182b71b2d0) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, const [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the next item in the list |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_prev\_no\_check](group__doubly-linked-list__apis.md#ga569062ce6e6d6280c9e77f88fa6a45cb) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, const [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the previous item in the list, node is not NULL |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_prev](group__doubly-linked-list__apis.md#gababe826faee8b081dbe09cfad4556a4e) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, const [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | get a reference to the previous item in the list |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_peek\_tail](group__doubly-linked-list__apis.md#gae8b78bea092edc49afeb2d481e36dc86) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get a reference to the tail item in the list |
| static void | [sys\_dlist\_append](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | add node to tail of list |
| static void | [sys\_dlist\_prepend](group__doubly-linked-list__apis.md#ga6f21ba50e0de93f54bfefeaabe0c767f) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | add node to head of list |
| static void | [sys\_dlist\_insert](group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071) ([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*successor, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | Insert a node into a list. |
| static void | [sys\_dlist\_insert\_at](group__doubly-linked-list__apis.md#ga667cee0bdd59d8ca3fc82a5bca2bcd48) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node, int(\*cond)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node, void \*data), void \*data) |
|  | insert node at position |
| static void | [sys\_dlist\_dequeue](group__doubly-linked-list__apis.md#gadf588e086301e31d70c4fc8de4b9d499) ([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | remove a specific node from a list |
| static void | [sys\_dlist\_remove](group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e) ([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node) |
|  | remove a specific node from a list |
| static [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \* | [sys\_dlist\_get](group__doubly-linked-list__apis.md#ga3032394541494771f980e7642ecbc287) ([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | get the first node in a list |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_dlist\_len](group__doubly-linked-list__apis.md#ga6797f138ad66cfb5ee7918bb12869eac) (const [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list) |
|  | Compute the size of the given list in O(n) time. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [dlist.h](dlist_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
