---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/linker_2iterable__sections_8h_source.html
original_path: doxygen/html/linker_2iterable__sections_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

24 KEEP(\*(SORT(.\_##struct\_type.static.\*\_???\_\*))); \

25 KEEP(\*(SORT(.\_##struct\_type.static.\*\_????\_\*))); \

26 KEEP(\*(SORT(.\_##struct\_type.static.\*\_?????\_\*))); \

27 \_CONCAT(\_##struct\_type, \_list\_end) = .

28

29#define Z\_LINK\_ITERABLE\_ALIGNED(struct\_type, align) \

30 . = ALIGN(align); \

31 Z\_LINK\_ITERABLE(struct\_type);

32

33#define Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type) \

34 \_CONCAT(\_##struct\_type, \_list\_start) = .; \

35 \*(SORT\_BY\_NAME(.\_##struct\_type.static.\*)); \

36 \_CONCAT(\_##struct\_type, \_list\_end) = .

37

38#define Z\_LINK\_ITERABLE\_SUBALIGN CONFIG\_LINKER\_ITERABLE\_SUBALIGN

39

[ 54](group__iterable__section__apis.md#gaa83030f309052399a7d1f61c56a0c901)#define ITERABLE\_SECTION\_ROM(struct\_type, subalign) \

55 SECTION\_PROLOGUE(struct\_type##\_area,,SUBALIGN(subalign)) \

56 { \

57 Z\_LINK\_ITERABLE(struct\_type); \

58 } GROUP\_ROM\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

59

[ 69](group__iterable__section__apis.md#ga2e525d689b958775ad0e1d2c8e61066a)#define ITERABLE\_SECTION\_ROM\_NUMERIC(struct\_type, subalign) \

70 SECTION\_PROLOGUE(struct\_type##\_area, EMPTY, SUBALIGN(subalign)) \

71 { \

72 Z\_LINK\_ITERABLE\_NUMERIC(struct\_type); \

73 } GROUP\_ROM\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

74

[ 87](group__iterable__section__apis.md#gaeecef08064fc4329ba5049f198cbb757)#define ITERABLE\_SECTION\_ROM\_GC\_ALLOWED(struct\_type, subalign) \

88 SECTION\_PROLOGUE(struct\_type##\_area,,SUBALIGN(subalign)) \

89 { \

90 Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type); \

91 } GROUP\_LINK\_IN(ROMABLE\_REGION)

92

[ 107](group__iterable__section__apis.md#ga50d995ef13e80eb36cfc8556e39056d0)#define ITERABLE\_SECTION\_RAM(struct\_type, subalign) \

108 SECTION\_DATA\_PROLOGUE(struct\_type##\_area,,SUBALIGN(subalign)) \

109 { \

110 Z\_LINK\_ITERABLE(struct\_type); \

111 } GROUP\_DATA\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

112

[ 122](group__iterable__section__apis.md#gae8ce765d1e5ac0e2ba02e33abdbdb63e)#define ITERABLE\_SECTION\_RAM\_NUMERIC(struct\_type, subalign) \

123 SECTION\_PROLOGUE(struct\_type##\_area, EMPTY, SUBALIGN(subalign)) \

124 { \

125 Z\_LINK\_ITERABLE\_NUMERIC(struct\_type); \

126 } GROUP\_DATA\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

127

[ 140](group__iterable__section__apis.md#gae9ffbe8beed14a543d170e96c39851e5)#define ITERABLE\_SECTION\_RAM\_GC\_ALLOWED(struct\_type, subalign) \

141 SECTION\_DATA\_PROLOGUE(struct\_type##\_area,,SUBALIGN(subalign)) \

142 { \

143 Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type); \

144 } GROUP\_DATA\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

145 /\* end of struct\_section\_apis \*/

149

150#endif /\* INCLUDE\_ZEPHYR\_LINKER\_ITERABLE\_SECTIONS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [iterable\_sections.h](linker_2iterable__sections_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
