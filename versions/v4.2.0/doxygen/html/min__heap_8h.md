---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/min__heap_8h.html
original_path: doxygen/html/min__heap_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

min\_heap.h File Reference

`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](min__heap_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [min\_heap](structmin__heap.md) |
|  | min-heap data structure with user-provided comparator. [More...](structmin__heap.md#details) |

| Macros | |
| --- | --- |
| #define | [MIN\_HEAP\_DEFINE](group__min__heap__apis.md#ga2363fb8ce4cd36e21ae5100e62d450c4)(name, cap, elem\_sz, align, cmp\_func) |
|  | Define a min-heap instance. |
| #define | [MIN\_HEAP\_DEFINE\_STATIC](group__min__heap__apis.md#gab4b10202a0a9f63608061b2ce35d902c)(name, cap, elem\_sz, align, cmp\_func) |
|  | Define a statically allocated and aligned min-heap instance. |
| #define | [MIN\_HEAP\_FOREACH](group__min__heap__apis.md#ga73c54e30b56717ee7498141488504137)(heap, node\_var) |
|  | Iterate over each node in the heap. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [min\_heap\_cmp\_t](group__min__heap__apis.md#ga638b9c8b6023ec281b1adcb9ca6ba814)) (const void \*a, const void \*b) |
|  | Comparator function type for min-heap ordering. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [min\_heap\_eq\_t](group__min__heap__apis.md#gab17087bc7c433bb85e94d4c88ad4ffbb)) (const void \*node, const void \*other) |
|  | Equality function for finding a node in the heap. |

| Functions | |
| --- | --- |
| void | [min\_heap\_init](group__min__heap__apis.md#ga675aa066413418b51e2210331f5d352b) (struct [min\_heap](structmin__heap.md) \*heap, void \*storage, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cap, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) elem\_size, [min\_heap\_cmp\_t](group__min__heap__apis.md#ga638b9c8b6023ec281b1adcb9ca6ba814) cmp) |
|  | Initialize a min-heap instance at runtime. |
| int | [min\_heap\_push](group__min__heap__apis.md#ga4cb5ee2bf40ab6f1ba557f8fa3927ba3) (struct [min\_heap](structmin__heap.md) \*heap, const void \*item) |
|  | Push an element into the min-heap. |
| void \* | [min\_heap\_peek](group__min__heap__apis.md#ga022a40c2cd09b925118a157ba05bfc2f) (const struct [min\_heap](structmin__heap.md) \*heap) |
|  | Peek at the top element of the min-heap. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [min\_heap\_remove](group__min__heap__apis.md#gab65afad260840bff650977b137404c7c) (struct [min\_heap](structmin__heap.md) \*heap, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) id, void \*out\_buf) |
|  | Remove a specific element from the min-heap. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [min\_heap\_is\_empty](group__min__heap__apis.md#ga808c35eebd9e18aadeba4f5b2a4db827) (struct [min\_heap](structmin__heap.md) \*heap) |
|  | Check if the min heap is empty. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [min\_heap\_pop](group__min__heap__apis.md#gacd04b6cd038669e229c69f60c25af9e0) (struct [min\_heap](structmin__heap.md) \*heap, void \*out\_buf) |
|  | Remove and return the highest priority element in the heap. |
| void \* | [min\_heap\_find](group__min__heap__apis.md#ga246f404f179c6c4c8ebeec6e15b2e3c2) (struct [min\_heap](structmin__heap.md) \*heap, [min\_heap\_eq\_t](group__min__heap__apis.md#gab17087bc7c433bb85e94d4c88ad4ffbb) eq, const void \*other, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*out\_id) |
|  | Search for a node in the heap matching a condition. |
| static void \* | [min\_heap\_get\_element](group__min__heap__apis.md#gac0f633e80405d5e47f8bd8eb09d952c6) (const struct [min\_heap](structmin__heap.md) \*heap, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) index) |
|  | Get a pointer to the element at the specified index. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [min\_heap.h](min__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
