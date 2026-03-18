---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/slist_8h.html
original_path: doxygen/html/slist_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

slist.h File Reference

`#include <stddef.h>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include "[list_gen.h](list__gen_8h_source.md)"`

[Go to the source code of this file.](slist_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SYS\_SLIST\_FOR\_EACH\_NODE](group__single-linked-list__apis.md#gaf32ac0f222186e497d3f6180b6c26352)(\_\_sl, \_\_sn) |
|  | Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_sn should not be removed. |
| #define | [SYS\_SLIST\_ITERATE\_FROM\_NODE](group__single-linked-list__apis.md#ga1740075b07ec67635c1934dcbe1b5cee)(\_\_sl, \_\_sn) |
|  | Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_sn should not be removed. |
| #define | [SYS\_SLIST\_FOR\_EACH\_NODE\_SAFE](group__single-linked-list__apis.md#gad6f1014e26d6cf9925d00b4f53076116)(\_\_sl, \_\_sn, \_\_sns) |
|  | Provide the primitive to safely iterate on a list Note: \_\_sn can be removed, it will not break the loop. |
| #define | [SYS\_SLIST\_CONTAINER](group__single-linked-list__apis.md#ga07e4257835751e18a6c06bfa5f9c25e8)(\_\_ln, \_\_cn, \_\_n) |
|  | Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes. |
| #define | [SYS\_SLIST\_PEEK\_HEAD\_CONTAINER](group__single-linked-list__apis.md#ga8fdb1e6baa7ba061dc1bd35f73a2fff1)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek container of the list head. |
| #define | [SYS\_SLIST\_PEEK\_TAIL\_CONTAINER](group__single-linked-list__apis.md#ga709c87e180d48c782c1583d7fb7629b3)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek container of the list tail. |
| #define | [SYS\_SLIST\_PEEK\_NEXT\_CONTAINER](group__single-linked-list__apis.md#ga5d1c9ee21f75da485ba12aa56471e699)(\_\_cn, \_\_n) |
|  | Provide the primitive to peek the next container. |
| #define | [SYS\_SLIST\_FOR\_EACH\_CONTAINER](group__single-linked-list__apis.md#gacd97d2f1044c0560d96c9f9a6f26d2f6)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached. |
| #define | [SYS\_SLIST\_FOR\_EACH\_CONTAINER\_SAFE](group__single-linked-list__apis.md#gacf3aaf32a6a3389229b548588c6d655e)(\_\_sl, \_\_cn, \_\_cns, \_\_n) |
|  | Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop. |
| #define | [SYS\_SLIST\_STATIC\_INIT](group__single-linked-list__apis.md#ga7f4710125f45643b7acdaa58dbfff225)(ptr\_to\_list) |
|  | Statically initialize a single-linked list. |

| Typedefs | |
| --- | --- |
| typedef struct \_snode | [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) |
|  | Single-linked list node structure. |
| typedef struct \_slist | [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) |
|  | Single-linked list structure. |

| Functions | |
| --- | --- |
| static void | [sys\_slist\_init](group__single-linked-list__apis.md#ga913aea7661b4ab3b4b50a8efc0d70428) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Initialize a list. |
| static [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_peek\_head](group__single-linked-list__apis.md#ga1af7fbf228545d591ef8961fa5f6a8f1) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Peek the first node from the list. |
| static [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_peek\_tail](group__single-linked-list__apis.md#ga49975721fa11c48000669d2c4ec0877f) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Peek the last node from the list. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_slist\_is\_empty](group__single-linked-list__apis.md#ga7d729bbb7bba57c5784ad0d2c341670a) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Test if the given list is empty. |
| static [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_peek\_next\_no\_check](group__single-linked-list__apis.md#ga58d001a256f28278f0e7c0b96b9cc492) ([sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Peek the next node from current node, node is not NULL. |
| static [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_peek\_next](group__single-linked-list__apis.md#ga729cbf8cafdbc34261db9274195ac5df) ([sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Peek the next node from current node. |
| static void | [sys\_slist\_prepend](group__single-linked-list__apis.md#gac962e3ec8440e4adb2ba6682dbf186ff) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Prepend a node to the given list. |
| static void | [sys\_slist\_append](group__single-linked-list__apis.md#ga829fd7b6f1944dc38e10685e861e62b5) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Append a node to the given list. |
| static void | [sys\_slist\_append\_list](group__single-linked-list__apis.md#gaaf7393c6bbf6d5cbd303173d95269481) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, void \*head, void \*tail) |
|  | Append a list to the given list. |
| static void | [sys\_slist\_merge\_slist](group__single-linked-list__apis.md#ga0c00bbb3dc6903f386fdb1e37fdd3b66) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list\_to\_append) |
|  | merge two slists, appending the second one to the first |
| static void | [sys\_slist\_insert](group__single-linked-list__apis.md#gadcbef5c013861fdfd325bae357c37b85) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*prev, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Insert a node to the given list. |
| static [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_get\_not\_empty](group__single-linked-list__apis.md#ga036a65b86f101a7867a83cdd1617ba33) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Fetch and remove the first node of the given list. |
| static [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \* | [sys\_slist\_get](group__single-linked-list__apis.md#ga497d7e9069c08e25a03ebc212ef8bbb3) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Fetch and remove the first node of the given list. |
| static void | [sys\_slist\_remove](group__single-linked-list__apis.md#gaee6957483d4fbe3b824f7a495d56030f) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*prev\_node, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Remove a node. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_slist\_find\_and\_remove](group__single-linked-list__apis.md#ga296560229ffdfd0054c9c7b0602825a6) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node) |
|  | Find and remove a node from a list. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_slist\_len](group__single-linked-list__apis.md#ga02a4d013fa37aca2943effe3afa0567b) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Compute the size of the given list in O(n) time. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [slist.h](slist_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
