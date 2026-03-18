---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/linker_2iterable__sections_8h_source.html
original_path: doxygen/html/linker_2iterable__sections_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iterable\_sections.h

[Go to the documentation of this file.](linker_2iterable__sections_8h.md)

1/\*

2 \* Copyright (C) 2020, Intel Corporation

3 \* Copyright (C) 2023, Nordic Semiconductor ASA

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef INCLUDE\_ZEPHYR\_LINKER\_ITERABLE\_SECTIONS\_H\_

8#define INCLUDE\_ZEPHYR\_LINKER\_ITERABLE\_SECTIONS\_H\_

9

14

15#define Z\_LINK\_ITERABLE(struct\_type) \

16 \_CONCAT(\_##struct\_type, \_list\_start) = .; \

17 KEEP(\*(SORT\_BY\_NAME(.\_##struct\_type.static.\*))); \

18 \_CONCAT(\_##struct\_type, \_list\_end) = .

19

20#define Z\_LINK\_ITERABLE\_NUMERIC(struct\_type) \

21 \_CONCAT(\_##struct\_type, \_list\_start) = .; \

22 KEEP(\*(SORT(.\_##struct\_type.static.\*\_?\_\*))); \

23 KEEP(\*(SORT(.\_##struct\_type.static.\*\_??\_\*))); \

24 \_CONCAT(\_##struct\_type, \_list\_end) = .

25

26#define Z\_LINK\_ITERABLE\_ALIGNED(struct\_type, align) \

27 . = ALIGN(align); \

28 Z\_LINK\_ITERABLE(struct\_type);

29

30#define Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type) \

31 \_CONCAT(\_##struct\_type, \_list\_start) = .; \

32 \*(SORT\_BY\_NAME(.\_##struct\_type.static.\*)); \

33 \_CONCAT(\_##struct\_type, \_list\_end) = .

34

[ 49](group__iterable__section__apis.md#gaa83030f309052399a7d1f61c56a0c901)#define ITERABLE\_SECTION\_ROM(struct\_type, subalign) \

50 SECTION\_PROLOGUE(struct\_type##\_area,,SUBALIGN(subalign)) \

51 { \

52 Z\_LINK\_ITERABLE(struct\_type); \

53 } GROUP\_ROM\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

54

[ 64](group__iterable__section__apis.md#ga2e525d689b958775ad0e1d2c8e61066a)#define ITERABLE\_SECTION\_ROM\_NUMERIC(struct\_type, subalign) \

65 SECTION\_PROLOGUE(struct\_type##\_area, EMPTY, SUBALIGN(subalign)) \

66 { \

67 Z\_LINK\_ITERABLE\_NUMERIC(struct\_type); \

68 } GROUP\_ROM\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

69

[ 82](group__iterable__section__apis.md#gaeecef08064fc4329ba5049f198cbb757)#define ITERABLE\_SECTION\_ROM\_GC\_ALLOWED(struct\_type, subalign) \

83 SECTION\_PROLOGUE(struct\_type##\_area,,SUBALIGN(subalign)) \

84 { \

85 Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type); \

86 } GROUP\_LINK\_IN(ROMABLE\_REGION)

87

[ 102](group__iterable__section__apis.md#ga50d995ef13e80eb36cfc8556e39056d0)#define ITERABLE\_SECTION\_RAM(struct\_type, subalign) \

103 SECTION\_DATA\_PROLOGUE(struct\_type##\_area,,SUBALIGN(subalign)) \

104 { \

105 Z\_LINK\_ITERABLE(struct\_type); \

106 } GROUP\_DATA\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

107

[ 117](group__iterable__section__apis.md#gae8ce765d1e5ac0e2ba02e33abdbdb63e)#define ITERABLE\_SECTION\_RAM\_NUMERIC(struct\_type, subalign) \

118 SECTION\_PROLOGUE(struct\_type##\_area, EMPTY, SUBALIGN(subalign)) \

119 { \

120 Z\_LINK\_ITERABLE\_NUMERIC(struct\_type); \

121 } GROUP\_DATA\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

122

[ 135](group__iterable__section__apis.md#gae9ffbe8beed14a543d170e96c39851e5)#define ITERABLE\_SECTION\_RAM\_GC\_ALLOWED(struct\_type, subalign) \

136 SECTION\_DATA\_PROLOGUE(struct\_type##\_area,,SUBALIGN(subalign)) \

137 { \

138 Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type); \

139 } GROUP\_DATA\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

140 /\* end of struct\_section\_apis \*/

144

145#endif /\* INCLUDE\_ZEPHYR\_LINKER\_ITERABLE\_SECTIONS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [iterable\_sections.h](linker_2iterable__sections_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
