---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/atomic__builtin_8h_source.html
original_path: doxygen/html/atomic__builtin_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

14#include <[zephyr/sys/atomic\_types.h](atomic__types_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20/\* Included from <atomic.h> \*/

21

[ 22](atomic__builtin_8h.md#a6a4a6dea8c56d6a78bc57d87a1f79450)static inline bool [atomic\_cas](atomic__builtin_8h.md#a6a4a6dea8c56d6a78bc57d87a1f79450)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old\_value,

23 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) new\_value)

24{

25 return \_\_atomic\_compare\_exchange\_n(target, &old\_value, new\_value,

26 0, \_\_ATOMIC\_SEQ\_CST,

27 \_\_ATOMIC\_SEQ\_CST);

28}

29

[ 30](atomic__builtin_8h.md#a1ee94308793379944e8e28371e1d135b)static inline bool [atomic\_ptr\_cas](atomic__builtin_8h.md#a1ee94308793379944e8e28371e1d135b)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) old\_value,

31 [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) new\_value)

32{

33 return \_\_atomic\_compare\_exchange\_n(target, &old\_value, new\_value,

34 0, \_\_ATOMIC\_SEQ\_CST,

35 \_\_ATOMIC\_SEQ\_CST);

36}

37

[ 38](atomic__builtin_8h.md#aed809d451c08b151dd8e20db3f12926a)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_add](atomic__builtin_8h.md#aed809d451c08b151dd8e20db3f12926a)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

39{

40 return \_\_atomic\_fetch\_add(target, value, \_\_ATOMIC\_SEQ\_CST);

41}

42

[ 43](atomic__builtin_8h.md#a1283fcb168cc85f65dfcdf973bf47cbb)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_sub](atomic__builtin_8h.md#a1283fcb168cc85f65dfcdf973bf47cbb)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

44{

45 return \_\_atomic\_fetch\_sub(target, value, \_\_ATOMIC\_SEQ\_CST);

46}

47

[ 48](atomic__builtin_8h.md#a66487deb6817076501dd9160537fc06a)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_inc](atomic__builtin_8h.md#a66487deb6817076501dd9160537fc06a)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

49{

50 return [atomic\_add](atomic__builtin_8h.md#aed809d451c08b151dd8e20db3f12926a)(target, 1);

51}

52

[ 53](atomic__builtin_8h.md#a0adecd95c4d47987c404a31e87c1d5c5)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_dec](atomic__builtin_8h.md#a0adecd95c4d47987c404a31e87c1d5c5)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

54{

55 return [atomic\_sub](atomic__builtin_8h.md#a1283fcb168cc85f65dfcdf973bf47cbb)(target, 1);

56}

57

[ 58](atomic__builtin_8h.md#adfe62ad2c8d64b0545b9e31f936bb79b)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_get](atomic__builtin_8h.md#adfe62ad2c8d64b0545b9e31f936bb79b)(const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

59{

60 return \_\_atomic\_load\_n(target, \_\_ATOMIC\_SEQ\_CST);

61}

62

[ 63](atomic__builtin_8h.md#a8efb153bce3bee1616852bda40d12ce5)static inline [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_get](atomic__builtin_8h.md#a8efb153bce3bee1616852bda40d12ce5)(const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target)

64{

65 return \_\_atomic\_load\_n(target, \_\_ATOMIC\_SEQ\_CST);

66}

67

[ 68](atomic__builtin_8h.md#a51f73cb439192f354f36b19018d88a13)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_set](atomic__builtin_8h.md#a51f73cb439192f354f36b19018d88a13)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

69{

70 /\* This builtin, as described by Intel, is not a traditional

71 \* test-and-set operation, but rather an atomic exchange operation. It

72 \* writes value into \*ptr, and returns the previous contents of \*ptr.

73 \*/

74 return \_\_atomic\_exchange\_n(target, value, \_\_ATOMIC\_SEQ\_CST);

75}

76

[ 77](atomic__builtin_8h.md#aa4e97fffda847d0d53b53d79819359a8)static inline [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_set](atomic__builtin_8h.md#aa4e97fffda847d0d53b53d79819359a8)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) value)

78{

79 return \_\_atomic\_exchange\_n(target, value, \_\_ATOMIC\_SEQ\_CST);

80}

81

[ 82](atomic__builtin_8h.md#a45ccf5a7d636206f0673139ac393946f)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_clear](atomic__builtin_8h.md#a45ccf5a7d636206f0673139ac393946f)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

83{

84 return [atomic\_set](atomic__builtin_8h.md#a51f73cb439192f354f36b19018d88a13)(target, 0);

85}

86

[ 87](atomic__builtin_8h.md#a8b511a7b5bccc7bc6b6e13526f87c0f3)static inline [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_clear](atomic__builtin_8h.md#a8b511a7b5bccc7bc6b6e13526f87c0f3)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target)

88{

89 return [atomic\_ptr\_set](atomic__builtin_8h.md#aa4e97fffda847d0d53b53d79819359a8)(target, NULL);

90}

91

[ 92](atomic__builtin_8h.md#ac96691d8703907941e81849b5aea42b4)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_or](atomic__builtin_8h.md#ac96691d8703907941e81849b5aea42b4)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

93{

94 return \_\_atomic\_fetch\_or(target, value, \_\_ATOMIC\_SEQ\_CST);

95}

96

[ 97](atomic__builtin_8h.md#a189eb9d39c3945194e64cdc55ae98deb)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_xor](atomic__builtin_8h.md#a189eb9d39c3945194e64cdc55ae98deb)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

98{

99 return \_\_atomic\_fetch\_xor(target, value, \_\_ATOMIC\_SEQ\_CST);

100}

101

[ 102](atomic__builtin_8h.md#ace9913fc4e103b5a1f27d29e8c12c41c)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_and](atomic__builtin_8h.md#ace9913fc4e103b5a1f27d29e8c12c41c)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

103{

104 return \_\_atomic\_fetch\_and(target, value, \_\_ATOMIC\_SEQ\_CST);

105}

106

[ 107](atomic__builtin_8h.md#aa04dbd054869e89ef234eb35be41798a)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_nand](atomic__builtin_8h.md#aa04dbd054869e89ef234eb35be41798a)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

108{

109 return \_\_atomic\_fetch\_nand(target, value, \_\_ATOMIC\_SEQ\_CST);

110}

111

112#ifdef \_\_cplusplus

113}

114#endif

115

116#endif /\* ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_BUILTIN\_H\_ \*/

[atomic\_dec](atomic__builtin_8h.md#a0adecd95c4d47987c404a31e87c1d5c5)

static atomic\_val\_t atomic\_dec(atomic\_t \*target)

**Definition** atomic\_builtin.h:53

[atomic\_sub](atomic__builtin_8h.md#a1283fcb168cc85f65dfcdf973bf47cbb)

static atomic\_val\_t atomic\_sub(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:43

[atomic\_xor](atomic__builtin_8h.md#a189eb9d39c3945194e64cdc55ae98deb)

static atomic\_val\_t atomic\_xor(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:97

[atomic\_ptr\_cas](atomic__builtin_8h.md#a1ee94308793379944e8e28371e1d135b)

static bool atomic\_ptr\_cas(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t old\_value, atomic\_ptr\_val\_t new\_value)

**Definition** atomic\_builtin.h:30

[atomic\_clear](atomic__builtin_8h.md#a45ccf5a7d636206f0673139ac393946f)

static atomic\_val\_t atomic\_clear(atomic\_t \*target)

**Definition** atomic\_builtin.h:82

[atomic\_set](atomic__builtin_8h.md#a51f73cb439192f354f36b19018d88a13)

static atomic\_val\_t atomic\_set(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:68

[atomic\_inc](atomic__builtin_8h.md#a66487deb6817076501dd9160537fc06a)

static atomic\_val\_t atomic\_inc(atomic\_t \*target)

**Definition** atomic\_builtin.h:48

[atomic\_cas](atomic__builtin_8h.md#a6a4a6dea8c56d6a78bc57d87a1f79450)

static bool atomic\_cas(atomic\_t \*target, atomic\_val\_t old\_value, atomic\_val\_t new\_value)

**Definition** atomic\_builtin.h:22

[atomic\_ptr\_clear](atomic__builtin_8h.md#a8b511a7b5bccc7bc6b6e13526f87c0f3)

static atomic\_ptr\_val\_t atomic\_ptr\_clear(atomic\_ptr\_t \*target)

**Definition** atomic\_builtin.h:87

[atomic\_ptr\_get](atomic__builtin_8h.md#a8efb153bce3bee1616852bda40d12ce5)

static atomic\_ptr\_val\_t atomic\_ptr\_get(const atomic\_ptr\_t \*target)

**Definition** atomic\_builtin.h:63

[atomic\_nand](atomic__builtin_8h.md#aa04dbd054869e89ef234eb35be41798a)

static atomic\_val\_t atomic\_nand(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:107

[atomic\_ptr\_set](atomic__builtin_8h.md#aa4e97fffda847d0d53b53d79819359a8)

static atomic\_ptr\_val\_t atomic\_ptr\_set(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t value)

**Definition** atomic\_builtin.h:77

[atomic\_or](atomic__builtin_8h.md#ac96691d8703907941e81849b5aea42b4)

static atomic\_val\_t atomic\_or(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:92

[atomic\_and](atomic__builtin_8h.md#ace9913fc4e103b5a1f27d29e8c12c41c)

static atomic\_val\_t atomic\_and(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:102

[atomic\_get](atomic__builtin_8h.md#adfe62ad2c8d64b0545b9e31f936bb79b)

static atomic\_val\_t atomic\_get(const atomic\_t \*target)

**Definition** atomic\_builtin.h:58

[atomic\_add](atomic__builtin_8h.md#aed809d451c08b151dd8e20db3f12926a)

static atomic\_val\_t atomic\_add(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic\_builtin.h:38

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
