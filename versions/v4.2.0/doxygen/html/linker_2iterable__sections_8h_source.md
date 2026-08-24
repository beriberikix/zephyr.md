---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/linker_2iterable__sections_8h_source.html
original_path: doxygen/html/linker_2iterable__sections_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

15/\* clang-format off \*/

16#define Z\_LINK\_ITERABLE(struct\_type) \

17 PLACE\_SYMBOL\_HERE(\_CONCAT(\_##struct\_type, \_list\_start)); \

18 KEEP(\*(SORT\_BY\_NAME(.\_##struct\_type.static.\*))); \

19 PLACE\_SYMBOL\_HERE(\_CONCAT(\_##struct\_type, \_list\_end));

20

21

22#define Z\_LINK\_ITERABLE\_NUMERIC(struct\_type) \

23 PLACE\_SYMBOL\_HERE(\_CONCAT(\_##struct\_type, \_list\_start)); \

24 KEEP(\*(SORT(.\_##struct\_type.static.\*\_?\_\*))); \

25 KEEP(\*(SORT(.\_##struct\_type.static.\*\_??\_\*))); \

26 KEEP(\*(SORT(.\_##struct\_type.static.\*\_???\_\*))); \

27 KEEP(\*(SORT(.\_##struct\_type.static.\*\_????\_\*))); \

28 KEEP(\*(SORT(.\_##struct\_type.static.\*\_?????\_\*))); \

29 PLACE\_SYMBOL\_HERE(\_CONCAT(\_##struct\_type, \_list\_end));

30

31#define Z\_LINK\_ITERABLE\_ALIGNED(struct\_type, align) \

32 . = ALIGN(align); \

33 Z\_LINK\_ITERABLE(struct\_type);

34

35#define Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type) \

36 PLACE\_SYMBOL\_HERE(\_CONCAT(\_##struct\_type, \_list\_start)); \

37 \*(SORT\_BY\_NAME(.\_##struct\_type.static.\*)); \

38 PLACE\_SYMBOL\_HERE(\_CONCAT(\_##struct\_type, \_list\_end));

39/\* clang-format on \*/

40

41#define Z\_LINK\_ITERABLE\_SUBALIGN CONFIG\_LINKER\_ITERABLE\_SUBALIGN

42

[ 57](group__iterable__section__apis.md#gaa83030f309052399a7d1f61c56a0c901)#define ITERABLE\_SECTION\_ROM(struct\_type, subalign) \

58 SECTION\_PROLOGUE(struct\_type##\_area, ,) \

59 { \

60 Z\_LINK\_ITERABLE(struct\_type); \

61 } GROUP\_ROM\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

62

[ 72](group__iterable__section__apis.md#ga2e525d689b958775ad0e1d2c8e61066a)#define ITERABLE\_SECTION\_ROM\_NUMERIC(struct\_type, subalign) \

73 SECTION\_PROLOGUE(struct\_type##\_area, EMPTY,) \

74 { \

75 Z\_LINK\_ITERABLE\_NUMERIC(struct\_type); \

76 } GROUP\_ROM\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

77

[ 90](group__iterable__section__apis.md#gaeecef08064fc4329ba5049f198cbb757)#define ITERABLE\_SECTION\_ROM\_GC\_ALLOWED(struct\_type, subalign) \

91 SECTION\_PROLOGUE(struct\_type##\_area, ,) \

92 { \

93 Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type); \

94 } GROUP\_LINK\_IN(ROMABLE\_REGION)

95

[ 110](group__iterable__section__apis.md#ga50d995ef13e80eb36cfc8556e39056d0)#define ITERABLE\_SECTION\_RAM(struct\_type, subalign) \

111 SECTION\_DATA\_PROLOGUE(struct\_type##\_area, ,) \

112 { \

113 Z\_LINK\_ITERABLE(struct\_type); \

114 } GROUP\_DATA\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

115

[ 125](group__iterable__section__apis.md#gae8ce765d1e5ac0e2ba02e33abdbdb63e)#define ITERABLE\_SECTION\_RAM\_NUMERIC(struct\_type, subalign) \

126 SECTION\_PROLOGUE(struct\_type##\_area, EMPTY,) \

127 { \

128 Z\_LINK\_ITERABLE\_NUMERIC(struct\_type); \

129 } GROUP\_DATA\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

130

[ 143](group__iterable__section__apis.md#gae9ffbe8beed14a543d170e96c39851e5)#define ITERABLE\_SECTION\_RAM\_GC\_ALLOWED(struct\_type, subalign) \

144 SECTION\_DATA\_PROLOGUE(struct\_type##\_area, ,) \

145 { \

146 Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type); \

147 } GROUP\_DATA\_LINK\_IN(RAMABLE\_REGION, ROMABLE\_REGION)

148 /\* end of struct\_section\_apis \*/

152

153#endif /\* INCLUDE\_ZEPHYR\_LINKER\_ITERABLE\_SECTIONS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [iterable\_sections.h](linker_2iterable__sections_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
