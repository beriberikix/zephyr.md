---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xtensa__mmu_8h_source.html
original_path: doxygen/html/xtensa__mmu_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xtensa\_mmu.h

[Go to the documentation of this file.](xtensa__mmu_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[stdint.h](stdint_8h.md)>

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_MMU\_H

10#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_MMU\_H

11

17

22

[ 24](group__xtensa__mmu__apis.md#ga0583957e9dcbf2c85154ac8994e14b3a)#define XTENSA\_MMU\_PERM\_X BIT(0)

25

[ 27](group__xtensa__mmu__apis.md#ga485ae34d7a65229418abb6019a9be5df)#define XTENSA\_MMU\_PERM\_W BIT(1)

28

[ 30](group__xtensa__mmu__apis.md#ga4193becf070dca661418f9d57516ae15)#define XTENSA\_MMU\_PERM\_WX (XTENSA\_MMU\_PERM\_W | XTENSA\_MMU\_PERM\_X)

31

[ 33](group__xtensa__mmu__apis.md#gad45f01becd63452801d0ec1889f366ae)#define XTENSA\_MMU\_CACHED\_WB BIT(2)

34

[ 36](group__xtensa__mmu__apis.md#gaf103854e82190435afc12cc6e84b91fc)#define XTENSA\_MMU\_CACHED\_WT BIT(3)

37

41

46

[ 47](group__xtensa__mmu__apis.md#ga58f790e348e5e1c4a3962a134cfb505f)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

48

[ 49](group__xtensa__mmu__apis.md#gab6fb9b9c6c1c968a11ae80bfd70fec26)#define K\_MEM\_PARTITION\_IS\_EXECUTABLE(attr) (((attr) & XTENSA\_MMU\_PERM\_X) != 0)

[ 50](group__xtensa__mmu__apis.md#ga7879968909ce2f0e33763ae1e2fc9d84)#define K\_MEM\_PARTITION\_IS\_WRITABLE(attr) (((attr) & XTENSA\_MMU\_PERM\_W) != 0)

[ 51](group__xtensa__mmu__apis.md#gae68645bc9363200e1cadffb770fe6a20)#define K\_MEM\_PARTITION\_IS\_USER(attr) (((attr) & XTENSA\_MMU\_MAP\_USER) != 0)

52

53/\* Read-Write access permission attributes \*/

[ 54](group__xtensa__mmu__apis.md#ga9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW \

55 ((k\_mem\_partition\_attr\_t) {XTENSA\_MMU\_PERM\_W | XTENSA\_MMU\_MAP\_USER})

[ 56](group__xtensa__mmu__apis.md#ga3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA \

57 ((k\_mem\_partition\_attr\_t) {0})

[ 58](group__xtensa__mmu__apis.md#ga708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO \

59 ((k\_mem\_partition\_attr\_t) {XTENSA\_MMU\_MAP\_USER})

[ 60](group__xtensa__mmu__apis.md#ga706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA \

61 ((k\_mem\_partition\_attr\_t) {0})

[ 62](group__xtensa__mmu__apis.md#ga73bc6803ccf24aad395089a4395bd22f)#define K\_MEM\_PARTITION\_P\_NA\_U\_NA \

63 ((k\_mem\_partition\_attr\_t) {0})

64

65/\* Execution-allowed attributes \*/

[ 66](group__xtensa__mmu__apis.md#ga78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX \

67 ((k\_mem\_partition\_attr\_t) {XTENSA\_MMU\_PERM\_X})

68

72

[ 78](group__xtensa__mmu__apis.md#ga37dfdbbf3a5830d0745944d9e1668da1)#define XTENSA\_MMU\_MAP\_USER BIT(4)

79

[ 90](group__xtensa__mmu__apis.md#gaf3036aabe1539acf75d72f8f8e4eb123)#define XTENSA\_MMU\_MAP\_SHARED BIT(30)

91

[ 95](structxtensa__mmu__range.md)struct [xtensa\_mmu\_range](structxtensa__mmu__range.md) {

[ 97](structxtensa__mmu__range.md#add09f00df98ae5c63084824dc070ef09) const char \*[name](structxtensa__mmu__range.md#add09f00df98ae5c63084824dc070ef09);

98

[ 100](structxtensa__mmu__range.md#ac525faa02c8886265e4118ce7cd80744) const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [start](structxtensa__mmu__range.md#ac525faa02c8886265e4118ce7cd80744);

101

[ 103](structxtensa__mmu__range.md#abc812bf633710dee5a8dcb19c522ad3f) const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [end](structxtensa__mmu__range.md#abc812bf633710dee5a8dcb19c522ad3f);

104

[ 106](structxtensa__mmu__range.md#ac0ff0bdc3091d2bd8d1b48b8a383a9a5) const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attrs](structxtensa__mmu__range.md#ac0ff0bdc3091d2bd8d1b48b8a383a9a5);

107};

108

114extern const struct [xtensa\_mmu\_range](structxtensa__mmu__range.md) [xtensa\_soc\_mmu\_ranges](group__xtensa__mmu__apis.md#gaf61e45b5fd46c1bf38d5172d7f27f2f3)[];

115

117extern int [xtensa\_soc\_mmu\_ranges\_num](group__xtensa__mmu__apis.md#ga57a61711ec5a6613304469392f33c749);

118

[ 124](group__xtensa__mmu__apis.md#ga4647e8c6102df87952ca82b76f3c13a5)void [xtensa\_mmu\_init](group__xtensa__mmu__apis.md#ga4647e8c6102df87952ca82b76f3c13a5)(void);

125

[ 134](group__xtensa__mmu__apis.md#gab6335d894a19734cab891fa85919a123)void [xtensa\_mmu\_reinit](group__xtensa__mmu__apis.md#gab6335d894a19734cab891fa85919a123)(void);

135

[ 146](group__xtensa__mmu__apis.md#gad1cf0320ec5ebd2936b7141582f99004)void [xtensa\_mmu\_tlb\_ipi](group__xtensa__mmu__apis.md#gad1cf0320ec5ebd2936b7141582f99004)(void);

147

[ 154](group__xtensa__mmu__apis.md#ga4aacd525656e5e12063785d6e51c71aa)void [xtensa\_mmu\_tlb\_shootdown](group__xtensa__mmu__apis.md#ga4aacd525656e5e12063785d6e51c71aa)(void);

155

159

160#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_MMU\_H \*/

[xtensa\_mmu\_init](group__xtensa__mmu__apis.md#ga4647e8c6102df87952ca82b76f3c13a5)

void xtensa\_mmu\_init(void)

Initialize hardware MMU.

[xtensa\_mmu\_tlb\_shootdown](group__xtensa__mmu__apis.md#ga4aacd525656e5e12063785d6e51c71aa)

void xtensa\_mmu\_tlb\_shootdown(void)

Invalidate cache to page tables and flush TLBs.

[xtensa\_soc\_mmu\_ranges\_num](group__xtensa__mmu__apis.md#ga57a61711ec5a6613304469392f33c749)

int xtensa\_soc\_mmu\_ranges\_num

Number of SoC additional memory regions.

[xtensa\_mmu\_reinit](group__xtensa__mmu__apis.md#gab6335d894a19734cab891fa85919a123)

void xtensa\_mmu\_reinit(void)

Re-initialize hardware MMU.

[xtensa\_mmu\_tlb\_ipi](group__xtensa__mmu__apis.md#gad1cf0320ec5ebd2936b7141582f99004)

void xtensa\_mmu\_tlb\_ipi(void)

Tell other processors to flush TLBs.

[xtensa\_soc\_mmu\_ranges](group__xtensa__mmu__apis.md#gaf61e45b5fd46c1bf38d5172d7f27f2f3)

const struct xtensa\_mmu\_range xtensa\_soc\_mmu\_ranges[]

Additional memory regions required by SoC.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:143

[xtensa\_mmu\_range](structxtensa__mmu__range.md)

Struct used to map a memory region.

**Definition** xtensa\_mmu.h:95

[xtensa\_mmu\_range::end](structxtensa__mmu__range.md#abc812bf633710dee5a8dcb19c522ad3f)

const uint32\_t end

End address of the memory region.

**Definition** xtensa\_mmu.h:103

[xtensa\_mmu\_range::attrs](structxtensa__mmu__range.md#ac0ff0bdc3091d2bd8d1b48b8a383a9a5)

const uint32\_t attrs

Attributes for the memory region.

**Definition** xtensa\_mmu.h:106

[xtensa\_mmu\_range::start](structxtensa__mmu__range.md#ac525faa02c8886265e4118ce7cd80744)

const uint32\_t start

Start address of the memory region.

**Definition** xtensa\_mmu.h:100

[xtensa\_mmu\_range::name](structxtensa__mmu__range.md#add09f00df98ae5c63084824dc070ef09)

const char \* name

Name of the memory region.

**Definition** xtensa\_mmu.h:97

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [xtensa\_mmu.h](xtensa__mmu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
