---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/atomic__builtin_8h_source.html
original_path: doxygen/html/atomic__builtin_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic\_builtin.h

[Go to the documentation of this file.](atomic__builtin_8h.md)

1/\* atomic operations \*/

2

3/\*

4 \* Copyright (c) 1997-2015, Wind River Systems, Inc.

5 \* Copyright (c) 2023 Nordic Semiconductor ASA

6 \*

7 \* SPDX-License-Identifier: Apache-2.0

8 \*/

9

10#ifndef ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_BUILTIN\_H\_

11#define ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_BUILTIN\_H\_

12

13#include <[stdbool.h](stdbool_8h.md)>

14#include <stddef.h>

15#include <[zephyr/sys/atomic\_types.h](atomic__types_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21/\* Included from <atomic.h> \*/

22

[ 23](atomic__builtin_8h.md#a6a4a6dea8c56d6a78bc57d87a1f79450)static inline bool [atomic\_cas](atomic__builtin_8h.md#a6a4a6dea8c56d6a78bc57d87a1f79450)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old\_value,

24 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) new\_value)

25{

26 return \_\_atomic\_compare\_exchange\_n(target, &old\_value, new\_value,

27 0, \_\_ATOMIC\_SEQ\_CST,

28 \_\_ATOMIC\_SEQ\_CST);

29}

30

[ 31](atomic__builtin_8h.md#a1ee94308793379944e8e28371e1d135b)static inline bool [atomic\_ptr\_cas](atomic__builtin_8h.md#a1ee94308793379944e8e28371e1d135b)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) old\_value,

32 [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) new\_value)

33{

34 return \_\_atomic\_compare\_exchange\_n(target, &old\_value, new\_value,

35 0, \_\_ATOMIC\_SEQ\_CST,

36 \_\_ATOMIC\_SEQ\_CST);

37}

38

[ 39](atomic__builtin_8h.md#aed809d451c08b151dd8e20db3f12926a)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_add](atomic__builtin_8h.md#aed809d451c08b151dd8e20db3f12926a)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

40{

41 return \_\_atomic\_fetch\_add(target, value, \_\_ATOMIC\_SEQ\_CST);

42}

43

[ 44](atomic__builtin_8h.md#a1283fcb168cc85f65dfcdf973bf47cbb)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_sub](atomic__builtin_8h.md#a1283fcb168cc85f65dfcdf973bf47cbb)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

45{

46 return \_\_atomic\_fetch\_sub(target, value, \_\_ATOMIC\_SEQ\_CST);

47}

48

[ 49](atomic__builtin_8h.md#a66487deb6817076501dd9160537fc06a)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_inc](atomic__builtin_8h.md#a66487deb6817076501dd9160537fc06a)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

50{

51 return [atomic\_add](atomic__builtin_8h.md#aed809d451c08b151dd8e20db3f12926a)(target, 1);

52}

53

[ 54](atomic__builtin_8h.md#a0adecd95c4d47987c404a31e87c1d5c5)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_dec](atomic__builtin_8h.md#a0adecd95c4d47987c404a31e87c1d5c5)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

55{

56 return [atomic\_sub](atomic__builtin_8h.md#a1283fcb168cc85f65dfcdf973bf47cbb)(target, 1);

57}

58

[ 59](atomic__builtin_8h.md#adfe62ad2c8d64b0545b9e31f936bb79b)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_get](atomic__builtin_8h.md#adfe62ad2c8d64b0545b9e31f936bb79b)(const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

60{

61 return \_\_atomic\_load\_n(target, \_\_ATOMIC\_SEQ\_CST);

62}

63

[ 64](atomic__builtin_8h.md#a8efb153bce3bee1616852bda40d12ce5)static inline [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_get](atomic__builtin_8h.md#a8efb153bce3bee1616852bda40d12ce5)(const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target)

65{

66 return \_\_atomic\_load\_n(target, \_\_ATOMIC\_SEQ\_CST);

67}

68

[ 69](atomic__builtin_8h.md#a51f73cb439192f354f36b19018d88a13)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_set](atomic__builtin_8h.md#a51f73cb439192f354f36b19018d88a13)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

70{

71 /\* This builtin, as described by Intel, is not a traditional

72 \* test-and-set operation, but rather an atomic exchange operation. It

73 \* writes value into \*ptr, and returns the previous contents of \*ptr.

74 \*/

75 return \_\_atomic\_exchange\_n(target, value, \_\_ATOMIC\_SEQ\_CST);

76}

77

[ 78](atomic__builtin_8h.md#aa4e97fffda847d0d53b53d79819359a8)static inline [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_set](atomic__builtin_8h.md#aa4e97fffda847d0d53b53d79819359a8)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) value)

79{

80 return \_\_atomic\_exchange\_n(target, value, \_\_ATOMIC\_SEQ\_CST);

81}

82

[ 83](atomic__builtin_8h.md#a45ccf5a7d636206f0673139ac393946f)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_clear](atomic__builtin_8h.md#a45ccf5a7d636206f0673139ac393946f)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

84{

85 return [atomic\_set](atomic__builtin_8h.md#a51f73cb439192f354f36b19018d88a13)(target, 0);

86}

87

[ 88](atomic__builtin_8h.md#a8b511a7b5bccc7bc6b6e13526f87c0f3)static inline [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_clear](atomic__builtin_8h.md#a8b511a7b5bccc7bc6b6e13526f87c0f3)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target)

89{

90 return [atomic\_ptr\_set](atomic__builtin_8h.md#aa4e97fffda847d0d53b53d79819359a8)(target, NULL);

91}

92

[ 93](atomic__builtin_8h.md#ac96691d8703907941e81849b5aea42b4)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_or](atomic__builtin_8h.md#ac96691d8703907941e81849b5aea42b4)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

94{

95 return \_\_atomic\_fetch\_or(target, value, \_\_ATOMIC\_SEQ\_CST);

96}

97

[ 98](atomic__builtin_8h.md#a189eb9d39c3945194e64cdc55ae98deb)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_xor](atomic__builtin_8h.md#a189eb9d39c3945194e64cdc55ae98deb)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

99{

100 return \_\_atomic\_fetch\_xor(target, value, \_\_ATOMIC\_SEQ\_CST);

101}

102

[ 103](atomic__builtin_8h.md#ace9913fc4e103b5a1f27d29e8c12c41c)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_and](atomic__builtin_8h.md#ace9913fc4e103b5a1f27d29e8c12c41c)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

104{

105 return \_\_atomic\_fetch\_and(target, value, \_\_ATOMIC\_SEQ\_CST);

106}

107

[ 108](atomic__builtin_8h.md#aa04dbd054869e89ef234eb35be41798a)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_nand](atomic__builtin_8h.md#aa04dbd054869e89ef234eb35be41798a)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

109{

110 return \_\_atomic\_fetch\_nand(target, value, \_\_ATOMIC\_SEQ\_CST);

111}

112

113#ifdef \_\_cplusplus

114}

115#endif

116

117#endif /\* ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_BUILTIN\_H\_ \*/

[atomic\_dec](atomic__builtin_8h.md#a0adecd95c4d47987c404a31e87c1d5c5)

static atomic\_val\_t atomic\_dec(atomic\_t \*target)

**Definition** atomic\_builtin.h:54

[atomic\_sub](atomic__builtin_8h.md#a1283fcb168cc85f65dfcdf973bf47cbb)

static atomic\_val\_t atomic\_sub(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:44

[atomic\_xor](atomic__builtin_8h.md#a189eb9d39c3945194e64cdc55ae98deb)

static atomic\_val\_t atomic\_xor(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:98

[atomic\_ptr\_cas](atomic__builtin_8h.md#a1ee94308793379944e8e28371e1d135b)

static bool atomic\_ptr\_cas(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t old\_value, atomic\_ptr\_val\_t new\_value)

**Definition** atomic\_builtin.h:31

[atomic\_clear](atomic__builtin_8h.md#a45ccf5a7d636206f0673139ac393946f)

static atomic\_val\_t atomic\_clear(atomic\_t \*target)

**Definition** atomic\_builtin.h:83

[atomic\_set](atomic__builtin_8h.md#a51f73cb439192f354f36b19018d88a13)

static atomic\_val\_t atomic\_set(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:69

[atomic\_inc](atomic__builtin_8h.md#a66487deb6817076501dd9160537fc06a)

static atomic\_val\_t atomic\_inc(atomic\_t \*target)

**Definition** atomic\_builtin.h:49

[atomic\_cas](atomic__builtin_8h.md#a6a4a6dea8c56d6a78bc57d87a1f79450)

static bool atomic\_cas(atomic\_t \*target, atomic\_val\_t old\_value, atomic\_val\_t new\_value)

**Definition** atomic\_builtin.h:23

[atomic\_ptr\_clear](atomic__builtin_8h.md#a8b511a7b5bccc7bc6b6e13526f87c0f3)

static atomic\_ptr\_val\_t atomic\_ptr\_clear(atomic\_ptr\_t \*target)

**Definition** atomic\_builtin.h:88

[atomic\_ptr\_get](atomic__builtin_8h.md#a8efb153bce3bee1616852bda40d12ce5)

static atomic\_ptr\_val\_t atomic\_ptr\_get(const atomic\_ptr\_t \*target)

**Definition** atomic\_builtin.h:64

[atomic\_nand](atomic__builtin_8h.md#aa04dbd054869e89ef234eb35be41798a)

static atomic\_val\_t atomic\_nand(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:108

[atomic\_ptr\_set](atomic__builtin_8h.md#aa4e97fffda847d0d53b53d79819359a8)

static atomic\_ptr\_val\_t atomic\_ptr\_set(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t value)

**Definition** atomic\_builtin.h:78

[atomic\_or](atomic__builtin_8h.md#ac96691d8703907941e81849b5aea42b4)

static atomic\_val\_t atomic\_or(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:93

[atomic\_and](atomic__builtin_8h.md#ace9913fc4e103b5a1f27d29e8c12c41c)

static atomic\_val\_t atomic\_and(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:103

[atomic\_get](atomic__builtin_8h.md#adfe62ad2c8d64b0545b9e31f936bb79b)

static atomic\_val\_t atomic\_get(const atomic\_t \*target)

**Definition** atomic\_builtin.h:59

[atomic\_add](atomic__builtin_8h.md#aed809d451c08b151dd8e20db3f12926a)

static atomic\_val\_t atomic\_add(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:39

[atomic\_types.h](atomic__types_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)

atomic\_t atomic\_val\_t

**Definition** atomic\_types.h:16

[atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4)

atomic\_ptr\_t atomic\_ptr\_val\_t

**Definition** atomic\_types.h:18

[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7)

void \* atomic\_ptr\_t

**Definition** atomic\_types.h:17

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [atomic\_builtin.h](atomic__builtin_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
