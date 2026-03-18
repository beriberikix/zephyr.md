---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mmustructs_8h_source.html
original_path: doxygen/html/mmustructs_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mmustructs.h

[Go to the documentation of this file.](mmustructs_8h.md)

1/\*

2 \* Copyright (c) 2011-2014 Wind River Systems, Inc.

3 \* Copyright (c) 2020 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_MMU\_H

9#define ZEPHYR\_INCLUDE\_ARCH\_X86\_MMU\_H

10

11#include <[zephyr/sys/util.h](util_8h.md)>

12

13/\*

14 \* K\_MEM\_PARTITION\_\* defines

15 \*

16 \* Slated for removal when virtual memory is implemented, memory

17 \* mapping APIs will replace memory domains.

18 \*/

19#define Z\_X86\_MMU\_RW BIT64(1)

20#define Z\_X86\_MMU\_US BIT64(2)

21#if defined(CONFIG\_X86\_PAE) || defined(CONFIG\_X86\_64)

22#define Z\_X86\_MMU\_XD BIT64(63)

23#else

24#define Z\_X86\_MMU\_XD 0

25#endif

26

27/\* For these we'll just use the same bits in the PTE \*/

[ 28](group__arch-mmu.md#ga4a60b63f47f88db455d67c33ef7bb85d)#define ARCH\_DATA\_PAGE\_DIRTY ((uintptr\_t)BIT(6))

[ 29](group__arch-mmu.md#gae76ce742aca8b4ac12907a2bfce98b0e)#define ARCH\_DATA\_PAGE\_LOADED ((uintptr\_t)BIT(0))

[ 30](group__arch-mmu.md#ga38cfc7602d259972cdd0b557ab26c2b4)#define ARCH\_DATA\_PAGE\_ACCESSED ((uintptr\_t)BIT(5))

31

32/\* Use an PAT bit for this one since it's never set in a mapped PTE \*/

[ 33](group__arch-mmu.md#ga843c53394b00d80b1649a6224557a56a)#define ARCH\_DATA\_PAGE\_NOT\_MAPPED ((uintptr\_t)BIT(7))

34

35/\* Always true with 32-bit page tables, don't enable

36 \* CONFIG\_EXECUTE\_XOR\_WRITE and expect it to work for you

37 \*/

[ 38](mmustructs_8h.md#ab6fb9b9c6c1c968a11ae80bfd70fec26)#define K\_MEM\_PARTITION\_IS\_EXECUTABLE(attr) (((attr) & Z\_X86\_MMU\_XD) == 0)

[ 39](mmustructs_8h.md#a7879968909ce2f0e33763ae1e2fc9d84)#define K\_MEM\_PARTITION\_IS\_WRITABLE(attr) (((attr) & Z\_X86\_MMU\_RW) != 0)

40

41/\* memory partition arch/soc independent attribute \*/

[ 42](mmustructs_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_US | \

43 Z\_X86\_MMU\_XD)

[ 44](mmustructs_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_XD)

[ 45](mmustructs_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO (Z\_X86\_MMU\_US | Z\_X86\_MMU\_XD)

[ 46](mmustructs_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA Z\_X86\_MMU\_XD

47/\* Execution-allowed attributes \*/

[ 48](mmustructs_8h.md#a29db5fb48087c0cae596ff212989ed24)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_US)

[ 49](mmustructs_8h.md#aa0ab658a70fe849f2460638602614b3a)#define K\_MEM\_PARTITION\_P\_RWX\_U\_NA Z\_X86\_MMU\_RW

[ 50](mmustructs_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX Z\_X86\_MMU\_US

[ 51](mmustructs_8h.md#abaedfd0ca98ddfcb6bd84cba94f9cd71)#define K\_MEM\_PARTITION\_P\_RX\_U\_NA (0)

52 /\* memory partition access permission mask \*/

[ 53](mmustructs_8h.md#afc94aaf30fa1dd56ba58d67c07cd2b71)#define K\_MEM\_PARTITION\_PERM\_MASK (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_US | \

54 Z\_X86\_MMU\_XD)

55

56#ifndef \_ASMLANGUAGE

57#include <[zephyr/sys/slist.h](slist_8h.md)>

58

59/\* Page table entry data type at all levels. Defined here due to

60 \* k\_mem\_partition\_attr\_t, eventually move to private x86\_mmu.h

61 \*/

62#if defined(CONFIG\_X86\_64) || defined(CONFIG\_X86\_PAE)

63typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae);

64#else

[ 65](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae);

66#endif

[ 67](mmustructs_8h.md#a2c21ed95c62d70b5abc48fa6d6acb849)typedef [pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae) [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

68

69struct [arch\_mem\_domain](structarch__mem__domain.md) {

70#ifdef CONFIG\_X86\_PAE

71 /\* 4-entry, 32-byte top-level PDPT \*/

72 [pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae) pdpt[4];

73#endif

74 /\* Pointer to top-level structure, either a PML4, PDPT, PD \*/

[ 75](structarch__mem__domain.md#a6807078806451f4512078917e76c52b6) [pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae) \*[ptables](structarch__mem__domain.md#a6807078806451f4512078917e76c52b6);

76

77 /\* Linked list of all active memory domains \*/

78 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structarch__mem__domain.md#a0929bee2d20221e55c0fa05ca321c9d5);

79#ifdef CONFIG\_X86\_PAE

80} \_\_aligned(32);

81#else

82};

83#endif /\* CONFIG\_X86\_PAE \*/

84#endif /\* \_ASMLANGUAGE \*/

85#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_MMU\_H \*/

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae)

uint32\_t pentry\_t

**Definition** mmustructs.h:65

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[arch\_mem\_domain](structarch__mem__domain.md)

**Definition** arch.h:46

[arch\_mem\_domain::node](structarch__mem__domain.md#a0929bee2d20221e55c0fa05ca321c9d5)

sys\_snode\_t node

**Definition** arch.h:50

[arch\_mem\_domain::ptables](structarch__mem__domain.md#a6807078806451f4512078917e76c52b6)

pentry\_t \* ptables

**Definition** mmustructs.h:75

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [mmustructs.h](mmustructs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
