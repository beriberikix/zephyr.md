---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sys__bitops_8h_source.html
original_path: doxygen/html/sys__bitops_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_bitops.h

[Go to the documentation of this file.](sys__bitops_8h.md)

1/\*

2 \* Copyright (c) 2020, Wind River Systems, Inc.

3 \* Copyright (c) 2017, Oticon A/S

4 \* Copyright (c) 2020, Synopsys

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9/\* Memory bits manipulation functions in non-arch-specific C code \*/

10

11#ifndef ZEPHYR\_INCLUDE\_ARCH\_COMMON\_SYS\_BITOPS\_H\_

12#define ZEPHYR\_INCLUDE\_ARCH\_COMMON\_SYS\_BITOPS\_H\_

13

14#ifndef \_ASMLANGUAGE

15

16#include <[zephyr/toolchain.h](toolchain_8h.md)>

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](sys__bitops_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_set\_bit](sys__bitops_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

25{

26 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) temp = \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr;

27

28 \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr = temp | (1 << bit);

29}

30

[ 31](sys__bitops_8h.md#a3a7b18493a4a34f82c9409453277265d)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_clear\_bit](sys__bitops_8h.md#a3a7b18493a4a34f82c9409453277265d)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

32{

33 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) temp = \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr;

34

35 \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr = temp & ~(1 << bit);

36}

37

[ 38](sys__bitops_8h.md#a43a2682b576dd69995dfdd203134f2a6)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_test\_bit](sys__bitops_8h.md#a43a2682b576dd69995dfdd203134f2a6)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

39{

40 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) temp = \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr;

41

42 return temp & (1 << bit);

43}

44

[ 45](sys__bitops_8h.md#aed49e233b8996739c7c7cefcfee7aada)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_set\_bits](sys__bitops_8h.md#aed49e233b8996739c7c7cefcfee7aada)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int mask)

46{

47 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) temp = \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr;

48

49 \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr = temp | mask;

50}

51

[ 52](sys__bitops_8h.md#a5b18d9541a6688f5e405741d27608834)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_clear\_bits](sys__bitops_8h.md#a5b18d9541a6688f5e405741d27608834)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int mask)

53{

54 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) temp = \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr;

55

56 \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr = temp & ~mask;

57}

58

59static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 60](sys__bitops_8h.md#a486594e16aa5d5a12e61eefb37418cd2) void [sys\_bitfield\_set\_bit](x86_2arch_8h.md#a185a9d6bf53f3e815f6385c3f500f4fc)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

61{

62 /\* Doing memory offsets in terms of 32-bit values to prevent

63 \* alignment issues

64 \*/

65 [sys\_set\_bit](sys__bitops_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)(addr + ((bit >> 5) << 2), bit & 0x1F);

66}

67

68static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 69](sys__bitops_8h.md#ad82b2448d5695f2f8ea4fc03bdb761f1) void [sys\_bitfield\_clear\_bit](x86_2arch_8h.md#a7167fa52e3fb5416c93527fea091c446)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

70{

71 [sys\_clear\_bit](sys__bitops_8h.md#a3a7b18493a4a34f82c9409453277265d)(addr + ((bit >> 5) << 2), bit & 0x1F);

72}

73

74static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 75](sys__bitops_8h.md#a355852406186b130c32d398b1896649a) int [sys\_bitfield\_test\_bit](x86_2arch_8h.md#a6547612936cc24eae4ff0217ea654c4d)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

76{

77 return [sys\_test\_bit](sys__bitops_8h.md#a43a2682b576dd69995dfdd203134f2a6)(addr + ((bit >> 5) << 2), bit & 0x1F);

78}

79

80static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 81](sys__bitops_8h.md#a036f93e32f1d1cc34cb2df3193650d48) int [sys\_test\_and\_set\_bit](sys__bitops_8h.md#a036f93e32f1d1cc34cb2df3193650d48)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

82{

83 int ret;

84

85 ret = [sys\_test\_bit](sys__bitops_8h.md#a43a2682b576dd69995dfdd203134f2a6)(addr, bit);

86 [sys\_set\_bit](sys__bitops_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)(addr, bit);

87

88 return ret;

89}

90

91static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 92](sys__bitops_8h.md#accf2bc65402198dda9d43ccd788163c6) int [sys\_test\_and\_clear\_bit](sys__bitops_8h.md#accf2bc65402198dda9d43ccd788163c6)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

93{

94 int ret;

95

96 ret = [sys\_test\_bit](sys__bitops_8h.md#a43a2682b576dd69995dfdd203134f2a6)(addr, bit);

97 [sys\_clear\_bit](sys__bitops_8h.md#a3a7b18493a4a34f82c9409453277265d)(addr, bit);

98

99 return ret;

100}

101

102static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 103](sys__bitops_8h.md#aa078b28e73f6416ae2865e2e807a6da5) int [sys\_bitfield\_test\_and\_set\_bit](x86_2arch_8h.md#aa770dbc8057ea68ed43b5eac0db9b390)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

104{

105 int ret;

106

107 ret = [sys\_bitfield\_test\_bit](x86_2arch_8h.md#a6547612936cc24eae4ff0217ea654c4d)(addr, bit);

108 [sys\_bitfield\_set\_bit](x86_2arch_8h.md#a185a9d6bf53f3e815f6385c3f500f4fc)(addr, bit);

109

110 return ret;

111}

112

113static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 114](sys__bitops_8h.md#a7c2f80fff262e362cb7daf8c10065136) int [sys\_bitfield\_test\_and\_clear\_bit](x86_2arch_8h.md#ab27f26cae6ce9e528d078fd49b9b4952)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

115{

116 int ret;

117

118 ret = [sys\_bitfield\_test\_bit](x86_2arch_8h.md#a6547612936cc24eae4ff0217ea654c4d)(addr, bit);

119 [sys\_bitfield\_clear\_bit](x86_2arch_8h.md#a7167fa52e3fb5416c93527fea091c446)(addr, bit);

120

121 return ret;

122}

123

124#ifdef \_\_cplusplus

125}

126#endif

127

128#endif /\* \_ASMLANGUAGE \*/

129

130#endif /\* ZEPHYR\_INCLUDE\_ARCH\_COMMON\_SYS\_BITOPS\_H\_ \*/

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[sys\_io.h](sys_2sys__io_8h.md)

[mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d)

uintptr\_t mem\_addr\_t

**Definition** sys\_io.h:21

[sys\_test\_and\_set\_bit](sys__bitops_8h.md#a036f93e32f1d1cc34cb2df3193650d48)

static ALWAYS\_INLINE int sys\_test\_and\_set\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** sys\_bitops.h:81

[sys\_set\_bit](sys__bitops_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)

static ALWAYS\_INLINE void sys\_set\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** sys\_bitops.h:24

[sys\_clear\_bit](sys__bitops_8h.md#a3a7b18493a4a34f82c9409453277265d)

static ALWAYS\_INLINE void sys\_clear\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** sys\_bitops.h:31

[sys\_test\_bit](sys__bitops_8h.md#a43a2682b576dd69995dfdd203134f2a6)

static ALWAYS\_INLINE int sys\_test\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** sys\_bitops.h:38

[sys\_clear\_bits](sys__bitops_8h.md#a5b18d9541a6688f5e405741d27608834)

static ALWAYS\_INLINE void sys\_clear\_bits(mem\_addr\_t addr, unsigned int mask)

Masking the designated bits from addr to 0.

**Definition** sys\_bitops.h:52

[sys\_test\_and\_clear\_bit](sys__bitops_8h.md#accf2bc65402198dda9d43ccd788163c6)

static ALWAYS\_INLINE int sys\_test\_and\_clear\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** sys\_bitops.h:92

[sys\_set\_bits](sys__bitops_8h.md#aed49e233b8996739c7c7cefcfee7aada)

static ALWAYS\_INLINE void sys\_set\_bits(mem\_addr\_t addr, unsigned int mask)

Masking the designated bits from addr to 1.

**Definition** sys\_bitops.h:45

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[sys\_bitfield\_set\_bit](x86_2arch_8h.md#a185a9d6bf53f3e815f6385c3f500f4fc)

#define sys\_bitfield\_set\_bit

**Definition** arch.h:208

[sys\_bitfield\_test\_bit](x86_2arch_8h.md#a6547612936cc24eae4ff0217ea654c4d)

#define sys\_bitfield\_test\_bit

**Definition** arch.h:210

[sys\_bitfield\_clear\_bit](x86_2arch_8h.md#a7167fa52e3fb5416c93527fea091c446)

#define sys\_bitfield\_clear\_bit

**Definition** arch.h:209

[sys\_bitfield\_test\_and\_set\_bit](x86_2arch_8h.md#aa770dbc8057ea68ed43b5eac0db9b390)

#define sys\_bitfield\_test\_and\_set\_bit

**Definition** arch.h:211

[sys\_bitfield\_test\_and\_clear\_bit](x86_2arch_8h.md#ab27f26cae6ce9e528d078fd49b9b4952)

#define sys\_bitfield\_test\_and\_clear\_bit

**Definition** arch.h:212

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [sys\_bitops.h](sys__bitops_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
