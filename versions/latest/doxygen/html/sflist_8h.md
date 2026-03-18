---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sflist_8h.html
original_path: doxygen/html/sflist_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sflist.h File Reference

`#include <stddef.h>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include "[list_gen.h](list__gen_8h_source.md)"`

[Go to the source code of this file.](sflist_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SYS\_SFLIST\_FOR\_EACH\_NODE](group__flagged-single-linked-list__apis.md#gaa3e9a3eeef7ecca012b0926fb2758c01)(\_\_sl, \_\_sn) |
|  | Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_sn should not be removed. |
| #define | [SYS\_SFLIST\_ITERATE\_FROM\_NODE](group__flagged-single-linked-list__apis.md#ga0470a27a54ed20eec35baa6cacd6a5ff)(\_\_sl, \_\_sn) |
|  | Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_sn should not be removed. |
| #define | [SYS\_SFLIST\_FOR\_EACH\_NODE\_SAFE](group__flagged-single-linked-list__apis.md#gabe867ebba43f1f0ebd2441147a9e3d3d)(\_\_sl, \_\_sn, \_\_sns) |
|  | Provide the primitive to safely iterate on a list Note: \_\_sn can be removed, it will not break the loop. |
| #define | [SYS\_SFLIST\_CONTAINER](group__flagged-single-linked-list__apis.md#ga68dae6db03b52bc27777a2b8c274a852)(\_\_ln, \_\_cn, \_\_n) |
|  | Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes. |
| #define | [SYS\_SFLIST\_PEEK\_HEAD\_CONTAINER](group__flagged-single-linked-list__apis.md#ga2c339b75ed80f3a94b0419ac73f18682)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek container of the list head. |
| #define | [SYS\_SFLIST\_PEEK\_TAIL\_CONTAINER](group__flagged-single-linked-list__apis.md#ga73760da17d0daefe655bbd750a3ce3e8)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to peek container of the list tail. |
| #define | [SYS\_SFLIST\_PEEK\_NEXT\_CONTAINER](group__flagged-single-linked-list__apis.md#ga0ba4b870acea3a10a1be066fb1d769c8)(\_\_cn, \_\_n) |
|  | Provide the primitive to peek the next container. |
| #define | [SYS\_SFLIST\_FOR\_EACH\_CONTAINER](group__flagged-single-linked-list__apis.md#ga1db228cdfd8004738fc6c4d2430be0cc)(\_\_sl, \_\_cn, \_\_n) |
|  | Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached. |
| #define | [SYS\_SFLIST\_FOR\_EACH\_CONTAINER\_SAFE](group__flagged-single-linked-list__apis.md#ga6b33a7b2be024c0e243f5bbccf900e81)(\_\_sl, \_\_cn, \_\_cns, \_\_n) |
|  | Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop. |
| #define | [SYS\_SFLIST\_STATIC\_INIT](group__flagged-single-linked-list__apis.md#ga892d5c9ce2d89b04f0ce15a88eefed71)(ptr\_to\_list) |
|  | Statically initialize a flagged single-linked list. |
| #define | [SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2)   0x3UL |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [unative\_t](group__flagged-single-linked-list__apis.md#ga5f0d5529e0d52d1a0d3c9594fadff48c) |
| typedef struct \_sfnode | [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) |
|  | Flagged single-linked list node structure. |
| typedef struct \_sflist | [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) |
|  | Flagged single-linked list structure. |

| Functions | |
| --- | --- |
| static void | [sys\_sflist\_init](group__flagged-single-linked-list__apis.md#ga9597045ad20485fd88a0fec83fe1ffe1) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Initialize a list. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sys\_sfnode\_flags\_get](group__flagged-single-linked-list__apis.md#ga0e258c1faa3cbaee48c29e8f2c11132b) ([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Fetch flags value for a particular sfnode. |
| static [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_peek\_head](group__flagged-single-linked-list__apis.md#ga6c993728bebb604f966cdc944939642e) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Peek the first node from the list. |
| static [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_peek\_tail](group__flagged-single-linked-list__apis.md#gabf278ac7912180fc50a25c0ebddc093c) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Peek the last node from the list. |
| static void | [sys\_sfnode\_init](group__flagged-single-linked-list__apis.md#gae56469b67ad7a92363d04ac726e326ea) ([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Initialize an sflist node. |
| static void | [sys\_sfnode\_flags\_set](group__flagged-single-linked-list__apis.md#ga85d82a3a5927f79a5f5655cb3405ce95) ([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set flags value for an sflist node. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#gac506235a9df89a7a52631e9990ceaad5) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Test if the given list is empty. |
| static [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_peek\_next\_no\_check](group__flagged-single-linked-list__apis.md#gaa67d15dd4fb28dbbc64f4b0e8e21455e) ([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Peek the next node from current node, node is not NULL. |
| static [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_peek\_next](group__flagged-single-linked-list__apis.md#ga514b41f1af89f3f08e216cfede7d5605) ([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Peek the next node from current node. |
| static void | [sys\_sflist\_prepend](group__flagged-single-linked-list__apis.md#ga824ff283c821b6f392ebd81516b65712) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Prepend a node to the given list. |
| static void | [sys\_sflist\_append](group__flagged-single-linked-list__apis.md#ga77733972e39b7db9fc3dcc998261fb2d) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Append a node to the given list. |
| static void | [sys\_sflist\_append\_list](group__flagged-single-linked-list__apis.md#gaaf9512d6c4432f34347771c9887e678a) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, void \*head, void \*tail) |
|  | Append a list to the given list. |
| static void | [sys\_sflist\_merge\_sflist](group__flagged-single-linked-list__apis.md#ga6c68678fceb6127a34760fb04ddef8b0) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list\_to\_append) |
|  | merge two sflists, appending the second one to the first |
| static void | [sys\_sflist\_insert](group__flagged-single-linked-list__apis.md#ga8983c5704eb149b0941f1fb19f79b8c1) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*prev, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Insert a node to the given list. |
| static [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_get\_not\_empty](group__flagged-single-linked-list__apis.md#ga065a7968e8082b65f9344a6331b424fc) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Fetch and remove the first node of the given list. |
| static [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \* | [sys\_sflist\_get](group__flagged-single-linked-list__apis.md#ga124d4dbb8d6d554071cb5eac2585b4ac) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Fetch and remove the first node of the given list. |
| static void | [sys\_sflist\_remove](group__flagged-single-linked-list__apis.md#ga66c716ef7495fcb04ea60aac340dc5ed) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*prev\_node, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Remove a node. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_sflist\_find\_and\_remove](group__flagged-single-linked-list__apis.md#gad66348fe7677cca76a547e09c8354322) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node) |
|  | Find and remove a node from a list. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_sflist\_len](group__flagged-single-linked-list__apis.md#gaa2d7de9f2366bf638c409b34c26aa871) ([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list) |
|  | Compute the size of the given list in O(n) time. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [sflist.h](sflist_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
