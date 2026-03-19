---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/atomic__xtensa_8h_source.html
original_path: doxygen/html/atomic__xtensa_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic\_xtensa.h

[Go to the documentation of this file.](atomic__xtensa_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ATOMIC\_XTENSA\_H\_

7#define ZEPHYR\_INCLUDE\_ATOMIC\_XTENSA\_H\_

8

9/\* Included from <zephyr/sys/atomic.h> \*/

10

11/\* Recent GCC versions actually do have working atomics support on

12 \* Xtensa (and so should work with CONFIG\_ATOMIC\_OPERATIONS\_BUILTIN),

13 \* but existing versions of Xtensa's XCC do not. So we define an

14 \* inline implementation here that is more or less identical

15 \*/

16

[ 18](atomic__xtensa_8h.md#a70641cc94157f8d7be8f7fc2ebb72e02)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_get](atomic__xtensa_8h.md#a70641cc94157f8d7be8f7fc2ebb72e02)(const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

19{

20 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) ret;

21

22 /\* Actual Xtensa hardware seems to have only in-order

23 \* pipelines, but the architecture does define a barrier load,

24 \* so use it. There is a matching s32ri instruction, but

25 \* nothing in the Zephyr API requires a barrier store (all the

26 \* atomic write ops have exchange semantics.

27 \*/

28 \_\_asm\_\_ volatile("l32ai %0, %1, 0"

29 : "=r"(ret) : "r"(target) : "memory");

30 return ret;

31}

32

50static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 51](atomic__xtensa_8h.md#a44f4f8164c1db8c54a93d36cb0457339)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [xtensa\_cas](atomic__xtensa_8h.md#a44f4f8164c1db8c54a93d36cb0457339)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*addr, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) oldval,

52 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) newval)

53{

54 \_\_asm\_\_ volatile("wsr %1, SCOMPARE1; s32c1i %0, %2, 0"

55 : "+r"(newval), "+r"(oldval) : "r"(addr) : "memory");

56

57 return newval; /\* got swapped with the old memory by s32c1i \*/

58}

59

61static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 62](atomic__xtensa_8h.md#a6c96fd0f67a7e091035ab989e2cbbfb1)bool [atomic\_cas](atomic__xtensa_8h.md#a6c96fd0f67a7e091035ab989e2cbbfb1)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) oldval, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) newval)

63{

64 return oldval == [xtensa\_cas](atomic__xtensa_8h.md#a44f4f8164c1db8c54a93d36cb0457339)(target, oldval, newval);

65}

66

68static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 69](atomic__xtensa_8h.md#ad949b788f6573e626a03e7b38fbd5645)bool [atomic\_ptr\_cas](atomic__xtensa_8h.md#ad949b788f6573e626a03e7b38fbd5645)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, void \*oldval, void \*newval)

70{

71 return ([atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)) oldval

72 == [xtensa\_cas](atomic__xtensa_8h.md#a44f4f8164c1db8c54a93d36cb0457339)(([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*) target, ([atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)) oldval,

73 ([atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)) newval);

74}

75

76/\* Generates an atomic exchange sequence that swaps the value at

77 \* address "target", whose old value is read to be "cur", with the

78 \* specified expression. Evaluates to the old value which was

79 \* atomically replaced.

80 \*/

81#define Z\_\_GEN\_ATOMXCHG(expr) ({ \

82 atomic\_val\_t res, cur; \

83 do { \

84 cur = \*target; \

85 res = xtensa\_cas(target, cur, (expr)); \

86 } while (res != cur); \

87 res; })

88

90static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 91](atomic__xtensa_8h.md#a5da5d59cfe0071203119b4881c2edf25)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_set](atomic__xtensa_8h.md#a5da5d59cfe0071203119b4881c2edf25)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

92{

93 return Z\_\_GEN\_ATOMXCHG(value);

94}

95

97static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 98](atomic__xtensa_8h.md#a734abed45962c79745a48b6468c499f1)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_add](atomic__xtensa_8h.md#a734abed45962c79745a48b6468c499f1)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

99{

100 return Z\_\_GEN\_ATOMXCHG(cur + value);

101}

102

104static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 105](atomic__xtensa_8h.md#a59692f87d456173352f4ae3f777eb1b6)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_sub](atomic__xtensa_8h.md#a59692f87d456173352f4ae3f777eb1b6)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

106{

107 return Z\_\_GEN\_ATOMXCHG(cur - value);

108}

109

111static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 112](atomic__xtensa_8h.md#a3fe69bb02a07b9445fcab9d8d7e92ea1)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_inc](atomic__xtensa_8h.md#a3fe69bb02a07b9445fcab9d8d7e92ea1)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

113{

114 return Z\_\_GEN\_ATOMXCHG(cur + 1);

115}

116

118static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 119](atomic__xtensa_8h.md#aed9de77ab7834e8e0715fc2dba0c7587)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_dec](atomic__xtensa_8h.md#aed9de77ab7834e8e0715fc2dba0c7587)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

120{

121 return Z\_\_GEN\_ATOMXCHG(cur - 1);

122}

123

[ 125](atomic__xtensa_8h.md#ae81ba87f31b1b2deee0da61697711b48)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_or](atomic__xtensa_8h.md#ae81ba87f31b1b2deee0da61697711b48)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target,

126 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

127{

128 return Z\_\_GEN\_ATOMXCHG(cur | value);

129}

130

[ 132](atomic__xtensa_8h.md#ab9c8fddee80b212bfe3d5da8d8fd09f1)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_xor](atomic__xtensa_8h.md#ab9c8fddee80b212bfe3d5da8d8fd09f1)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target,

133 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

134{

135 return Z\_\_GEN\_ATOMXCHG(cur ^ value);

136}

137

[ 139](atomic__xtensa_8h.md#a41fc4b2cdd3fa7a407c2e28a9be581ac)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_and](atomic__xtensa_8h.md#a41fc4b2cdd3fa7a407c2e28a9be581ac)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target,

140 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

141{

142 return Z\_\_GEN\_ATOMXCHG(cur & value);

143}

144

[ 146](atomic__xtensa_8h.md#acc0cbd2fd07f3d25b6e9366e0c01829a)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_nand](atomic__xtensa_8h.md#acc0cbd2fd07f3d25b6e9366e0c01829a)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target,

147 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

148{

149 return Z\_\_GEN\_ATOMXCHG(~(cur & value));

150}

151

[ 153](atomic__xtensa_8h.md#a6271fb71dfdcdc389f6703d8ffb3f99e)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \*[atomic\_ptr\_get](atomic__xtensa_8h.md#a6271fb71dfdcdc389f6703d8ffb3f99e)(const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target)

154{

155 return (void \*) [atomic\_get](atomic__xtensa_8h.md#a70641cc94157f8d7be8f7fc2ebb72e02)(([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*)target);

156}

157

[ 159](atomic__xtensa_8h.md#a1448d2fb67f55f6084114dfd17f18b5f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \*[atomic\_ptr\_set](atomic__xtensa_8h.md#a1448d2fb67f55f6084114dfd17f18b5f)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, void \*value)

160{

161 return (void \*) [atomic\_set](atomic__xtensa_8h.md#a5da5d59cfe0071203119b4881c2edf25)(([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*) target, ([atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)) value);

162}

163

[ 165](atomic__xtensa_8h.md#a88898c1c167b04955fb276e6f4b0e5f1)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_clear](atomic__xtensa_8h.md#a88898c1c167b04955fb276e6f4b0e5f1)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

166{

167 return [atomic\_set](atomic__xtensa_8h.md#a5da5d59cfe0071203119b4881c2edf25)(target, 0);

168}

169

[ 171](atomic__xtensa_8h.md#af4eeda2b2d7cae6989a1deaa370fc266)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \*[atomic\_ptr\_clear](atomic__xtensa_8h.md#af4eeda2b2d7cae6989a1deaa370fc266)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target)

172{

173 return (void \*) [atomic\_set](atomic__xtensa_8h.md#a5da5d59cfe0071203119b4881c2edf25)(([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*) target, 0);

174}

175

176#endif /\* ZEPHYR\_INCLUDE\_ATOMIC\_XTENSA\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)

atomic\_t atomic\_val\_t

**Definition** atomic\_types.h:16

[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7)

void \* atomic\_ptr\_t

**Definition** atomic\_types.h:17

[atomic\_ptr\_set](atomic__xtensa_8h.md#a1448d2fb67f55f6084114dfd17f18b5f)

static ALWAYS\_INLINE void \* atomic\_ptr\_set(atomic\_ptr\_t \*target, void \*value)

Implementation of atomic\_ptr\_set.

**Definition** atomic\_xtensa.h:159

[atomic\_inc](atomic__xtensa_8h.md#a3fe69bb02a07b9445fcab9d8d7e92ea1)

static ALWAYS\_INLINE atomic\_val\_t atomic\_inc(atomic\_t \*target)

Implementation of atomic\_inc.

**Definition** atomic\_xtensa.h:112

[atomic\_and](atomic__xtensa_8h.md#a41fc4b2cdd3fa7a407c2e28a9be581ac)

static ALWAYS\_INLINE atomic\_val\_t atomic\_and(atomic\_t \*target, atomic\_val\_t value)

Implementation of atomic\_and.

**Definition** atomic\_xtensa.h:139

[xtensa\_cas](atomic__xtensa_8h.md#a44f4f8164c1db8c54a93d36cb0457339)

static ALWAYS\_INLINE atomic\_val\_t xtensa\_cas(atomic\_t \*addr, atomic\_val\_t oldval, atomic\_val\_t newval)

Xtensa specific atomic compare-and-set (CAS).

**Definition** atomic\_xtensa.h:51

[atomic\_sub](atomic__xtensa_8h.md#a59692f87d456173352f4ae3f777eb1b6)

static ALWAYS\_INLINE atomic\_val\_t atomic\_sub(atomic\_t \*target, atomic\_val\_t value)

Implementation of atomic\_sub.

**Definition** atomic\_xtensa.h:105

[atomic\_set](atomic__xtensa_8h.md#a5da5d59cfe0071203119b4881c2edf25)

static ALWAYS\_INLINE atomic\_val\_t atomic\_set(atomic\_t \*target, atomic\_val\_t value)

Implementation of atomic\_set.

**Definition** atomic\_xtensa.h:91

[atomic\_ptr\_get](atomic__xtensa_8h.md#a6271fb71dfdcdc389f6703d8ffb3f99e)

static ALWAYS\_INLINE void \* atomic\_ptr\_get(const atomic\_ptr\_t \*target)

Implementation of atomic\_ptr\_get.

**Definition** atomic\_xtensa.h:153

[atomic\_cas](atomic__xtensa_8h.md#a6c96fd0f67a7e091035ab989e2cbbfb1)

static ALWAYS\_INLINE bool atomic\_cas(atomic\_t \*target, atomic\_val\_t oldval, atomic\_val\_t newval)

Implementation of atomic\_cas.

**Definition** atomic\_xtensa.h:62

[atomic\_get](atomic__xtensa_8h.md#a70641cc94157f8d7be8f7fc2ebb72e02)

static ALWAYS\_INLINE atomic\_val\_t atomic\_get(const atomic\_t \*target)

Implementation of atomic\_get.

**Definition** atomic\_xtensa.h:18

[atomic\_add](atomic__xtensa_8h.md#a734abed45962c79745a48b6468c499f1)

static ALWAYS\_INLINE atomic\_val\_t atomic\_add(atomic\_t \*target, atomic\_val\_t value)

Implementation of atomic\_add.

**Definition** atomic\_xtensa.h:98

[atomic\_clear](atomic__xtensa_8h.md#a88898c1c167b04955fb276e6f4b0e5f1)

static ALWAYS\_INLINE atomic\_val\_t atomic\_clear(atomic\_t \*target)

Implementation of atomic\_clear.

**Definition** atomic\_xtensa.h:165

[atomic\_xor](atomic__xtensa_8h.md#ab9c8fddee80b212bfe3d5da8d8fd09f1)

static ALWAYS\_INLINE atomic\_val\_t atomic\_xor(atomic\_t \*target, atomic\_val\_t value)

Implementation of atomic\_xor.

**Definition** atomic\_xtensa.h:132

[atomic\_nand](atomic__xtensa_8h.md#acc0cbd2fd07f3d25b6e9366e0c01829a)

static ALWAYS\_INLINE atomic\_val\_t atomic\_nand(atomic\_t \*target, atomic\_val\_t value)

Implementation of atomic\_nand.

**Definition** atomic\_xtensa.h:146

[atomic\_ptr\_cas](atomic__xtensa_8h.md#ad949b788f6573e626a03e7b38fbd5645)

static ALWAYS\_INLINE bool atomic\_ptr\_cas(atomic\_ptr\_t \*target, void \*oldval, void \*newval)

Implementation of atomic\_ptr\_cas.

**Definition** atomic\_xtensa.h:69

[atomic\_or](atomic__xtensa_8h.md#ae81ba87f31b1b2deee0da61697711b48)

static ALWAYS\_INLINE atomic\_val\_t atomic\_or(atomic\_t \*target, atomic\_val\_t value)

Implementation of atomic\_or.

**Definition** atomic\_xtensa.h:125

[atomic\_dec](atomic__xtensa_8h.md#aed9de77ab7834e8e0715fc2dba0c7587)

static ALWAYS\_INLINE atomic\_val\_t atomic\_dec(atomic\_t \*target)

Implementation of atomic\_dec.

**Definition** atomic\_xtensa.h:119

[atomic\_ptr\_clear](atomic__xtensa_8h.md#af4eeda2b2d7cae6989a1deaa370fc266)

static ALWAYS\_INLINE void \* atomic\_ptr\_clear(atomic\_ptr\_t \*target)

Implementation of atomic\_ptr\_clear.

**Definition** atomic\_xtensa.h:171

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [atomic\_xtensa.h](atomic__xtensa_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
