---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mem__attr_8h.html
original_path: doxygen/html/mem__attr_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_attr.h File Reference

`#include <stddef.h>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/dt-bindings/memory-attr/memory-attr.h](memory-attr_8h_source.md)>`

[Go to the source code of this file.](mem__attr_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mem\_attr\_region\_t](structmem__attr__region__t.md) |
|  | memory-attr region structure. [More...](structmem__attr__region__t.md#details) |

| Macros | |
| --- | --- |
| #define | [DT\_MEMORY\_ATTR\_FOREACH\_STATUS\_OKAY\_NODE](group__memory__attr__interface.md#ga316e41444a0db6bb78ec0c1c4bdc832b)(fn) |
|  | Invokes `fn` for every status okay node in the tree with property zephyr,memory-attr. |

| Functions | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [mem\_attr\_get\_regions](group__memory__attr__interface.md#gadcf93c67fe564d65064f5f6175d7089f) (const struct [mem\_attr\_region\_t](structmem__attr__region__t.md) \*\*region) |
|  | Get the list of memory regions. |
| int | [mem\_attr\_check\_buf](group__memory__attr__interface.md#gac599eafdb0be231c0105b05eb76b657b) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) attr) |
|  | Check if a buffer has correct size and attributes. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mem\_mgmt](dir_5ee27bc867ccb4004a26ac2b9a5fc96f.md)
- [mem\_attr.h](mem__attr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
