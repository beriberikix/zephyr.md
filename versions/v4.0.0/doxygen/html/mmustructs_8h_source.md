---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mmustructs_8h_source.html
original_path: doxygen/html/mmustructs_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

11#include <[zephyr/sys/util.h](sys_2util_8h.md)>

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

[ 28](mmustructs_8h.md#a4a60b63f47f88db455d67c33ef7bb85d)#define ARCH\_DATA\_PAGE\_DIRTY ((uintptr\_t)BIT(6))

[ 29](mmustructs_8h.md#ae76ce742aca8b4ac12907a2bfce98b0e)#define ARCH\_DATA\_PAGE\_LOADED ((uintptr\_t)BIT(0))

[ 30](mmustructs_8h.md#a38cfc7602d259972cdd0b557ab26c2b4)#define ARCH\_DATA\_PAGE\_ACCESSED ((uintptr\_t)BIT(5))

31

32/\* Use an PAT bit for this one since it's never set in a mapped PTE \*/

[ 33](mmustructs_8h.md#a843c53394b00d80b1649a6224557a56a)#define ARCH\_DATA\_PAGE\_NOT\_MAPPED ((uintptr\_t)BIT(7))

34

35/\*

36 \* Special unpaged "location" tags. These are defined as the highest possible

37 \* PTE address values unlikely to conflict with backing store locations.

38 \* As noted in arch\_page\_info\_get(), those values on PAE systems, whose

39 \* pentry\_t is larger than uintptr\_t get truncated.

40 \*/

41#if defined(CONFIG\_X86\_64) || defined(CONFIG\_X86\_PAE)

42#define ARCH\_UNPAGED\_ANON\_ZERO ((uintptr\_t)0x07FFFFFFFFFFF000ULL)

43#define ARCH\_UNPAGED\_ANON\_UNINIT ((uintptr\_t)0x07FFFFFFFFFFE000ULL)

44#else

[ 45](mmustructs_8h.md#a9db83a76d2aaf1f829e12f1c9c4d68c5)#define ARCH\_UNPAGED\_ANON\_ZERO ((uintptr\_t)0xFFFFF000U)

[ 46](mmustructs_8h.md#ab2c364dbdc6958849af03dcfef871852)#define ARCH\_UNPAGED\_ANON\_UNINIT ((uintptr\_t)0xFFFFE000U)

47#endif

48

49/\* Always true with 32-bit page tables, don't enable

50 \* CONFIG\_EXECUTE\_XOR\_WRITE and expect it to work for you

51 \*/

[ 52](mmustructs_8h.md#ab6fb9b9c6c1c968a11ae80bfd70fec26)#define K\_MEM\_PARTITION\_IS\_EXECUTABLE(attr) (((attr) & Z\_X86\_MMU\_XD) == 0)

[ 53](mmustructs_8h.md#a7879968909ce2f0e33763ae1e2fc9d84)#define K\_MEM\_PARTITION\_IS\_WRITABLE(attr) (((attr) & Z\_X86\_MMU\_RW) != 0)

54

55/\* memory partition arch/soc independent attribute \*/

[ 56](mmustructs_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_US | \

57 Z\_X86\_MMU\_XD)

[ 58](mmustructs_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_XD)

[ 59](mmustructs_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO (Z\_X86\_MMU\_US | Z\_X86\_MMU\_XD)

[ 60](mmustructs_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA Z\_X86\_MMU\_XD

61/\* Execution-allowed attributes \*/

[ 62](mmustructs_8h.md#a29db5fb48087c0cae596ff212989ed24)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_US)

[ 63](mmustructs_8h.md#aa0ab658a70fe849f2460638602614b3a)#define K\_MEM\_PARTITION\_P\_RWX\_U\_NA Z\_X86\_MMU\_RW

[ 64](mmustructs_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX Z\_X86\_MMU\_US

[ 65](mmustructs_8h.md#abaedfd0ca98ddfcb6bd84cba94f9cd71)#define K\_MEM\_PARTITION\_P\_RX\_U\_NA (0)

66 /\* memory partition access permission mask \*/

[ 67](mmustructs_8h.md#afc94aaf30fa1dd56ba58d67c07cd2b71)#define K\_MEM\_PARTITION\_PERM\_MASK (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_US | \

68 Z\_X86\_MMU\_XD)

69

70#ifndef \_ASMLANGUAGE

71#include <[zephyr/sys/slist.h](slist_8h.md)>

72

73/\* Page table entry data type at all levels. Defined here due to

74 \* k\_mem\_partition\_attr\_t, eventually move to private x86\_mmu.h

75 \*/

76#if defined(CONFIG\_X86\_64) || defined(CONFIG\_X86\_PAE)

77typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae);

78#else

[ 79](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae);

80#endif

[ 81](mmustructs_8h.md#a2c21ed95c62d70b5abc48fa6d6acb849)typedef [pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae) [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

82

83struct [arch\_mem\_domain](structarch__mem__domain.md) {

84#ifdef CONFIG\_X86\_PAE

85 /\* 4-entry, 32-byte top-level PDPT \*/

86 [pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae) pdpt[4];

87#endif

88 /\* Pointer to top-level structure, either a PML4, PDPT, PD \*/

[ 89](structarch__mem__domain.md#a6807078806451f4512078917e76c52b6) [pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae) \*[ptables](structarch__mem__domain.md#a6807078806451f4512078917e76c52b6);

90

91 /\* Linked list of all active memory domains \*/

92 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structarch__mem__domain.md#a0929bee2d20221e55c0fa05ca321c9d5);

93#ifdef CONFIG\_X86\_PAE

94} \_\_aligned(32);

95#else

96};

97#endif /\* CONFIG\_X86\_PAE \*/

98#endif /\* \_ASMLANGUAGE \*/

99#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_MMU\_H \*/

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[pentry\_t](mmustructs_8h.md#af1ea6e187a2f90056a06f7536a9dc3ae)

uint32\_t pentry\_t

**Definition** mmustructs.h:79

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

**Definition** mmustructs.h:89

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [mmustructs.h](mmustructs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
