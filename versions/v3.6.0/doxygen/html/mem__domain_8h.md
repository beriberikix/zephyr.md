---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mem__domain_8h.html
original_path: doxygen/html/mem__domain_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_domain.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/sys/dlist.h](dlist_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/kernel/thread.h](kernel_2thread_8h_source.md)>`

[Go to the source code of this file.](mem__domain_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [k\_mem\_partition](structk__mem__partition.md) |
|  | Memory Partition. [More...](structk__mem__partition.md#details) |
| struct | [k\_mem\_domain](structk__mem__domain.md) |
|  | Memory Domain. [More...](structk__mem__domain.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_MEM\_PARTITION\_DEFINE](group__mem__domain__apis.md#ga4360fd595cb3fe3a10b58c12ae2b7ece)(name, start, size, attr) |
|  | Statically declare a memory partition. |

| Functions | |
| --- | --- |
| int | [k\_mem\_domain\_init](group__mem__domain__apis.md#ga8a987bc85c02925685fe87213fe26c5a) (struct [k\_mem\_domain](structk__mem__domain.md) \*domain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_parts, struct [k\_mem\_partition](structk__mem__partition.md) \*parts[]) |
|  | Initialize a memory domain. |
| int | [k\_mem\_domain\_add\_partition](group__mem__domain__apis.md#ga07da0cf76f8db54373b88d40be63b138) (struct [k\_mem\_domain](structk__mem__domain.md) \*domain, struct [k\_mem\_partition](structk__mem__partition.md) \*part) |
|  | Add a memory partition into a memory domain. |
| int | [k\_mem\_domain\_remove\_partition](group__mem__domain__apis.md#gada4f8ce609d6b720ee88e11544555fc2) (struct [k\_mem\_domain](structk__mem__domain.md) \*domain, struct [k\_mem\_partition](structk__mem__partition.md) \*part) |
|  | Remove a memory partition from a memory domain. |
| int | [k\_mem\_domain\_add\_thread](group__mem__domain__apis.md#ga7b4d6148d9375f020a268961d5afde2d) (struct [k\_mem\_domain](structk__mem__domain.md) \*domain, [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Add a thread into a memory domain. |

| Variables | |
| --- | --- |
| struct [k\_mem\_domain](structk__mem__domain.md) | [k\_mem\_domain\_default](group__mem__domain__apis.md#ga3613abdb546a66059fa3f621a2ebd41a) |
|  | Default memory domain. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [app\_memory](dir_a5c66281f93d933ad709643c33992dc2.md)
- [mem\_domain.h](mem__domain_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
