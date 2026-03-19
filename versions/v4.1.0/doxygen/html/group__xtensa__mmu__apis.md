---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__xtensa__mmu__apis.html
original_path: doxygen/html/group__xtensa__mmu__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Xtensa Memory Management Unit (MMU) APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md) » [Xtensa APIs](group__xtensa__apis.md)

| Data Structures | |
| --- | --- |
| struct | [xtensa\_mmu\_range](structxtensa__mmu__range.md) |
|  | Struct used to map a memory region. [More...](structxtensa__mmu__range.md#details) |

| Macros | |
| --- | --- |
| #define | [XTENSA\_MMU\_MAP\_USER](#ga37dfdbbf3a5830d0745944d9e1668da1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Software only bit to indicate a memory region can be accessed by user thread(s). |
| #define | [XTENSA\_MMU\_MAP\_SHARED](#gaf3036aabe1539acf75d72f8f8e4eb123)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30) |
|  | Software only bit to indicate a memory region is shared by all threads. |

| Functions | |
| --- | --- |
| void | [xtensa\_mmu\_init](#ga4647e8c6102df87952ca82b76f3c13a5) (void) |
|  | Initialize hardware MMU. |
| void | [xtensa\_mmu\_reinit](#gab6335d894a19734cab891fa85919a123) (void) |
|  | Re-initialize hardware MMU. |
| void | [xtensa\_mmu\_tlb\_ipi](#gad1cf0320ec5ebd2936b7141582f99004) (void) |
|  | Tell other processors to flush TLBs. |
| void | [xtensa\_mmu\_tlb\_shootdown](#ga4aacd525656e5e12063785d6e51c71aa) (void) |
|  | Invalidate cache to page tables and flush TLBs. |

| Variables | |
| --- | --- |
| const struct [xtensa\_mmu\_range](structxtensa__mmu__range.md) | [xtensa\_soc\_mmu\_ranges](#gaf61e45b5fd46c1bf38d5172d7f27f2f3) [] |
|  | Additional memory regions required by SoC. |
| int | [xtensa\_soc\_mmu\_ranges\_num](#ga57a61711ec5a6613304469392f33c749) |
|  | Number of SoC additional memory regions. |

| Memory domain and partitions | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_mem\_partition\_attr\_t](#ga58f790e348e5e1c4a3962a134cfb505f) |
| #define | [K\_MEM\_PARTITION\_IS\_EXECUTABLE](#gab6fb9b9c6c1c968a11ae80bfd70fec26)(attr) |
| #define | [K\_MEM\_PARTITION\_IS\_WRITABLE](#ga7879968909ce2f0e33763ae1e2fc9d84)(attr) |
| #define | [K\_MEM\_PARTITION\_IS\_USER](#gae68645bc9363200e1cadffb770fe6a20)(attr) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](#ga9b7cc3c51f518517031d76807470aa10)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MMU\_PERM\_W](#ga485ae34d7a65229418abb6019a9be5df) | [XTENSA\_MMU\_MAP\_USER](#ga37dfdbbf3a5830d0745944d9e1668da1)}) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](#ga3c52d13e42a66beb72d088ac56388951)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {0}) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](#ga708338371e91b5a3f2d44f9ae48849db)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MMU\_MAP\_USER](#ga37dfdbbf3a5830d0745944d9e1668da1)}) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](#ga706eaa9c515f1cc859d97ef8455b2f2f)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {0}) |
| #define | [K\_MEM\_PARTITION\_P\_NA\_U\_NA](#ga73bc6803ccf24aad395089a4395bd22f)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {0}) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX](#ga78f9b21aa8b5c894db28328f5a1e2641)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MMU\_PERM\_X](#ga0583957e9dcbf2c85154ac8994e14b3a)}) |

| Memory region permission and caching mode. | |
| --- | --- |
| #define | [XTENSA\_MMU\_PERM\_X](#ga0583957e9dcbf2c85154ac8994e14b3a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Memory region is executable. |
| #define | [XTENSA\_MMU\_PERM\_W](#ga485ae34d7a65229418abb6019a9be5df)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Memory region is writable. |
| #define | [XTENSA\_MMU\_PERM\_WX](#ga4193becf070dca661418f9d57516ae15)   ([XTENSA\_MMU\_PERM\_W](#ga485ae34d7a65229418abb6019a9be5df) | [XTENSA\_MMU\_PERM\_X](#ga0583957e9dcbf2c85154ac8994e14b3a)) |
|  | Memory region is both executable and writable. |
| #define | [XTENSA\_MMU\_CACHED\_WB](#gad45f01becd63452801d0ec1889f366ae)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Memory region has write-back cache. |
| #define | [XTENSA\_MMU\_CACHED\_WT](#gaf103854e82190435afc12cc6e84b91fc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Memory region has write-through cache. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gab6fb9b9c6c1c968a11ae80bfd70fec26)K\_MEM\_PARTITION\_IS\_EXECUTABLE

| #define K\_MEM\_PARTITION\_IS\_EXECUTABLE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

**Value:**

(((attr) & [XTENSA\_MMU\_PERM\_X](#ga0583957e9dcbf2c85154ac8994e14b3a)) != 0)

[XTENSA\_MMU\_PERM\_X](#ga0583957e9dcbf2c85154ac8994e14b3a)

#define XTENSA\_MMU\_PERM\_X

Memory region is executable.

**Definition** xtensa\_mmu.h:24

## [◆ ](#gae68645bc9363200e1cadffb770fe6a20)K\_MEM\_PARTITION\_IS\_USER

| #define K\_MEM\_PARTITION\_IS\_USER | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

**Value:**

(((attr) & [XTENSA\_MMU\_MAP\_USER](#ga37dfdbbf3a5830d0745944d9e1668da1)) != 0)

[XTENSA\_MMU\_MAP\_USER](#ga37dfdbbf3a5830d0745944d9e1668da1)

#define XTENSA\_MMU\_MAP\_USER

Software only bit to indicate a memory region can be accessed by user thread(s).

**Definition** xtensa\_mmu.h:78

## [◆ ](#ga7879968909ce2f0e33763ae1e2fc9d84)K\_MEM\_PARTITION\_IS\_WRITABLE

| #define K\_MEM\_PARTITION\_IS\_WRITABLE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

**Value:**

(((attr) & [XTENSA\_MMU\_PERM\_W](#ga485ae34d7a65229418abb6019a9be5df)) != 0)

[XTENSA\_MMU\_PERM\_W](#ga485ae34d7a65229418abb6019a9be5df)

#define XTENSA\_MMU\_PERM\_W

Memory region is writable.

**Definition** xtensa\_mmu.h:27

## [◆ ](#ga73bc6803ccf24aad395089a4395bd22f)K\_MEM\_PARTITION\_P\_NA\_U\_NA

| #define K\_MEM\_PARTITION\_P\_NA\_U\_NA   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {0}) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

## [◆ ](#ga706eaa9c515f1cc859d97ef8455b2f2f)K\_MEM\_PARTITION\_P\_RO\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {0}) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

## [◆ ](#ga708338371e91b5a3f2d44f9ae48849db)K\_MEM\_PARTITION\_P\_RO\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MMU\_MAP\_USER](#ga37dfdbbf3a5830d0745944d9e1668da1)}) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

## [◆ ](#ga3c52d13e42a66beb72d088ac56388951)K\_MEM\_PARTITION\_P\_RW\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {0}) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

## [◆ ](#ga9b7cc3c51f518517031d76807470aa10)K\_MEM\_PARTITION\_P\_RW\_U\_RW

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MMU\_PERM\_W](#ga485ae34d7a65229418abb6019a9be5df) | [XTENSA\_MMU\_MAP\_USER](#ga37dfdbbf3a5830d0745944d9e1668da1)}) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

## [◆ ](#ga78f9b21aa8b5c894db28328f5a1e2641)K\_MEM\_PARTITION\_P\_RX\_U\_RX

| #define K\_MEM\_PARTITION\_P\_RX\_U\_RX   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MMU\_PERM\_X](#ga0583957e9dcbf2c85154ac8994e14b3a)}) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

## [◆ ](#gad45f01becd63452801d0ec1889f366ae)XTENSA\_MMU\_CACHED\_WB

| #define XTENSA\_MMU\_CACHED\_WB   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Memory region has write-back cache.

## [◆ ](#gaf103854e82190435afc12cc6e84b91fc)XTENSA\_MMU\_CACHED\_WT

| #define XTENSA\_MMU\_CACHED\_WT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Memory region has write-through cache.

## [◆ ](#gaf3036aabe1539acf75d72f8f8e4eb123)XTENSA\_MMU\_MAP\_SHARED

| #define XTENSA\_MMU\_MAP\_SHARED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Software only bit to indicate a memory region is shared by all threads.

This BIT tells the mapping code whether the memory region should be shared between all threads. That is not used in the HW, it is just for the implementation.

The PTE mapping this memory will use an ASID that is set in the ring 4 spot in RASID.

## [◆ ](#ga37dfdbbf3a5830d0745944d9e1668da1)XTENSA\_MMU\_MAP\_USER

| #define XTENSA\_MMU\_MAP\_USER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Software only bit to indicate a memory region can be accessed by user thread(s).

This BIT tells the mapping code which ring PTE entries to use.

## [◆ ](#ga485ae34d7a65229418abb6019a9be5df)XTENSA\_MMU\_PERM\_W

| #define XTENSA\_MMU\_PERM\_W   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Memory region is writable.

## [◆ ](#ga4193becf070dca661418f9d57516ae15)XTENSA\_MMU\_PERM\_WX

| #define XTENSA\_MMU\_PERM\_WX   ([XTENSA\_MMU\_PERM\_W](#ga485ae34d7a65229418abb6019a9be5df) | [XTENSA\_MMU\_PERM\_X](#ga0583957e9dcbf2c85154ac8994e14b3a)) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Memory region is both executable and writable.

## [◆ ](#ga0583957e9dcbf2c85154ac8994e14b3a)XTENSA\_MMU\_PERM\_X

| #define XTENSA\_MMU\_PERM\_X   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Memory region is executable.

## Typedef Documentation

## [◆ ](#ga58f790e348e5e1c4a3962a134cfb505f)k\_mem\_partition\_attr\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_mem\_partition\_attr\_t |
| --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

## Function Documentation

## [◆ ](#ga4647e8c6102df87952ca82b76f3c13a5)xtensa\_mmu\_init()

| void xtensa\_mmu\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Initialize hardware MMU.

This initializes the MMU hardware and setup the memory regions at boot.

## [◆ ](#gab6335d894a19734cab891fa85919a123)xtensa\_mmu\_reinit()

| void xtensa\_mmu\_reinit | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Re-initialize hardware MMU.

This configures the MMU hardware when the cpu lost context and has re-started.

It assumes that the page table is already created and accessible in memory.

## [◆ ](#gad1cf0320ec5ebd2936b7141582f99004)xtensa\_mmu\_tlb\_ipi()

| void xtensa\_mmu\_tlb\_ipi | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Tell other processors to flush TLBs.

This sends IPI to other processors to telling them to invalidate cache to page tables and flush TLBs. This is needed when one processor is updating page tables that may affect threads running on other processors.

Note
:   This needs to be implemented in the SoC layer.

## [◆ ](#ga4aacd525656e5e12063785d6e51c71aa)xtensa\_mmu\_tlb\_shootdown()

| void xtensa\_mmu\_tlb\_shootdown | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Invalidate cache to page tables and flush TLBs.

This invalidates cache to all page tables and flush TLBs as they may have been modified by other processors.

## Variable Documentation

## [◆ ](#gaf61e45b5fd46c1bf38d5172d7f27f2f3)xtensa\_soc\_mmu\_ranges

| | const struct [xtensa\_mmu\_range](structxtensa__mmu__range.md) xtensa\_soc\_mmu\_ranges[] | | --- | | extern |
| --- | --- | --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Additional memory regions required by SoC.

These memory regions will be setup by MMU initialization code at boot.

## [◆ ](#ga57a61711ec5a6613304469392f33c749)xtensa\_soc\_mmu\_ranges\_num

| | int xtensa\_soc\_mmu\_ranges\_num | | --- | | extern |
| --- | --- | --- |

`#include <[xtensa_mmu.h](xtensa__mmu_8h.md)>`

Number of SoC additional memory regions.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
