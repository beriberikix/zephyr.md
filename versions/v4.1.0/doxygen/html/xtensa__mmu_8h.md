---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xtensa__mmu_8h.html
original_path: doxygen/html/xtensa__mmu_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xtensa\_mmu.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](xtensa__mmu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [xtensa\_mmu\_range](structxtensa__mmu__range.md) |
|  | Struct used to map a memory region. [More...](structxtensa__mmu__range.md#details) |

| Macros | |
| --- | --- |
| #define | [XTENSA\_MMU\_MAP\_USER](group__xtensa__mmu__apis.md#ga37dfdbbf3a5830d0745944d9e1668da1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Software only bit to indicate a memory region can be accessed by user thread(s). |
| #define | [XTENSA\_MMU\_MAP\_SHARED](group__xtensa__mmu__apis.md#gaf3036aabe1539acf75d72f8f8e4eb123)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30) |
|  | Software only bit to indicate a memory region is shared by all threads. |
| Memory region permission and caching mode. | |
| #define | [XTENSA\_MMU\_PERM\_X](group__xtensa__mmu__apis.md#ga0583957e9dcbf2c85154ac8994e14b3a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Memory region is executable. |
| #define | [XTENSA\_MMU\_PERM\_W](group__xtensa__mmu__apis.md#ga485ae34d7a65229418abb6019a9be5df)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Memory region is writable. |
| #define | [XTENSA\_MMU\_PERM\_WX](group__xtensa__mmu__apis.md#ga4193becf070dca661418f9d57516ae15)   ([XTENSA\_MMU\_PERM\_W](group__xtensa__mmu__apis.md#ga485ae34d7a65229418abb6019a9be5df) | [XTENSA\_MMU\_PERM\_X](group__xtensa__mmu__apis.md#ga0583957e9dcbf2c85154ac8994e14b3a)) |
|  | Memory region is both executable and writable. |
| #define | [XTENSA\_MMU\_CACHED\_WB](group__xtensa__mmu__apis.md#gad45f01becd63452801d0ec1889f366ae)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Memory region has write-back cache. |
| #define | [XTENSA\_MMU\_CACHED\_WT](group__xtensa__mmu__apis.md#gaf103854e82190435afc12cc6e84b91fc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Memory region has write-through cache. |

| Functions | |
| --- | --- |
| void | [xtensa\_mmu\_init](group__xtensa__mmu__apis.md#ga4647e8c6102df87952ca82b76f3c13a5) (void) |
|  | Initialize hardware MMU. |
| void | [xtensa\_mmu\_reinit](group__xtensa__mmu__apis.md#gab6335d894a19734cab891fa85919a123) (void) |
|  | Re-initialize hardware MMU. |
| void | [xtensa\_mmu\_tlb\_ipi](group__xtensa__mmu__apis.md#gad1cf0320ec5ebd2936b7141582f99004) (void) |
|  | Tell other processors to flush TLBs. |
| void | [xtensa\_mmu\_tlb\_shootdown](group__xtensa__mmu__apis.md#ga4aacd525656e5e12063785d6e51c71aa) (void) |
|  | Invalidate cache to page tables and flush TLBs. |

| Variables | |
| --- | --- |
| const struct [xtensa\_mmu\_range](structxtensa__mmu__range.md) | [xtensa\_soc\_mmu\_ranges](group__xtensa__mmu__apis.md#gaf61e45b5fd46c1bf38d5172d7f27f2f3) [] |
|  | Additional memory regions required by SoC. |
| int | [xtensa\_soc\_mmu\_ranges\_num](group__xtensa__mmu__apis.md#ga57a61711ec5a6613304469392f33c749) |
|  | Number of SoC additional memory regions. |

| Memory domain and partitions | |
| --- | --- |
| #define | [K\_MEM\_PARTITION\_IS\_EXECUTABLE](group__xtensa__mmu__apis.md#gab6fb9b9c6c1c968a11ae80bfd70fec26)(attr) |
| #define | [K\_MEM\_PARTITION\_IS\_WRITABLE](group__xtensa__mmu__apis.md#ga7879968909ce2f0e33763ae1e2fc9d84)(attr) |
| #define | [K\_MEM\_PARTITION\_IS\_USER](group__xtensa__mmu__apis.md#gae68645bc9363200e1cadffb770fe6a20)(attr) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](group__xtensa__mmu__apis.md#ga9b7cc3c51f518517031d76807470aa10)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MMU\_PERM\_W](group__xtensa__mmu__apis.md#ga485ae34d7a65229418abb6019a9be5df) | [XTENSA\_MMU\_MAP\_USER](group__xtensa__mmu__apis.md#ga37dfdbbf3a5830d0745944d9e1668da1)}) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](group__xtensa__mmu__apis.md#ga3c52d13e42a66beb72d088ac56388951)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {0}) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](group__xtensa__mmu__apis.md#ga708338371e91b5a3f2d44f9ae48849db)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MMU\_MAP\_USER](group__xtensa__mmu__apis.md#ga37dfdbbf3a5830d0745944d9e1668da1)}) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](group__xtensa__mmu__apis.md#ga706eaa9c515f1cc859d97ef8455b2f2f)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {0}) |
| #define | [K\_MEM\_PARTITION\_P\_NA\_U\_NA](group__xtensa__mmu__apis.md#ga73bc6803ccf24aad395089a4395bd22f)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {0}) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX](group__xtensa__mmu__apis.md#ga78f9b21aa8b5c894db28328f5a1e2641)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MMU\_PERM\_X](group__xtensa__mmu__apis.md#ga0583957e9dcbf2c85154ac8994e14b3a)}) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_mem\_partition\_attr\_t](group__xtensa__mmu__apis.md#ga58f790e348e5e1c4a3962a134cfb505f) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [xtensa\_mmu.h](xtensa__mmu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
