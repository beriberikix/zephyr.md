---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/shared__multi__heap_8h.html
original_path: doxygen/html/shared__multi__heap_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shared\_multi\_heap.h File Reference

Public API for Shared Multi-Heap framework.
[More...](#details)

[Go to the source code of this file.](shared__multi__heap_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shared\_multi\_heap\_region](structshared__multi__heap__region.md) |
|  | SMH region struct. [More...](structshared__multi__heap__region.md#details) |

| Macros | |
| --- | --- |
| #define | [MAX\_SHARED\_MULTI\_HEAP\_ATTR](group__shared__multi__heap.md#gae582ce2dfaaf9554d43aab717c85c17c)   [SMH\_REG\_ATTR\_NUM](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4a0a41317e94fcdf459708be4a78b74c91) |
|  | Maximum number of standard attributes. |

| Enumerations | |
| --- | --- |
| enum | [shared\_multi\_heap\_attr](group__shared__multi__heap.md#ga11861c5c373f9e5d81496ae1be7df1d4) { [SMH\_REG\_ATTR\_CACHEABLE](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4afb2e0bb04859ff231dee953279b8bf3a) , [SMH\_REG\_ATTR\_NON\_CACHEABLE](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4a2625b9b8aea429ab748f9e39d55f0dff) , [SMH\_REG\_ATTR\_NUM](group__shared__multi__heap.md#gga11861c5c373f9e5d81496ae1be7df1d4a0a41317e94fcdf459708be4a78b74c91) } |
|  | SMH region attributes enumeration type. [More...](group__shared__multi__heap.md#ga11861c5c373f9e5d81496ae1be7df1d4) |

| Functions | |
| --- | --- |
| int | [shared\_multi\_heap\_pool\_init](group__shared__multi__heap.md#ga5b7f09666e3eac051b4c4942572f9ca3) (void) |
|  | Init the pool. |
| void \* | [shared\_multi\_heap\_alloc](group__shared__multi__heap.md#ga8cd3d321f5ae516cd55812d304289971) (enum [shared\_multi\_heap\_attr](group__shared__multi__heap.md#ga11861c5c373f9e5d81496ae1be7df1d4) attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate memory from the memory shared multi-heap pool. |
| void \* | [shared\_multi\_heap\_aligned\_alloc](group__shared__multi__heap.md#ga328b199253da06ed724e9b0157167ede) (enum [shared\_multi\_heap\_attr](group__shared__multi__heap.md#ga11861c5c373f9e5d81496ae1be7df1d4) attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Allocate aligned memory from the memory shared multi-heap pool. |
| void | [shared\_multi\_heap\_free](group__shared__multi__heap.md#gab968bf26483d22939aaa7c2b1b6743ad) (void \*block) |
|  | Free memory from the shared multi-heap pool. |
| int | [shared\_multi\_heap\_add](group__shared__multi__heap.md#ga086362a2a8fce827a246039ef8757cc5) (struct [shared\_multi\_heap\_region](structshared__multi__heap__region.md) \*region, void \*user\_data) |
|  | Add an heap region to the shared multi-heap pool. |

## Detailed Description

Public API for Shared Multi-Heap framework.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [multi\_heap](dir_bbf885d0562205ffed4d60b82c4fd442.md)
- [shared\_multi\_heap.h](shared__multi__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
