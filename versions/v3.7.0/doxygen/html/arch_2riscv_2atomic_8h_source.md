---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2riscv_2atomic_8h_source.html
original_path: doxygen/html/arch_2riscv_2atomic_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic.h

[Go to the documentation of this file.](arch_2riscv_2atomic_8h.md)

1

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ATOMIC\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ATOMIC\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

13/\* The standard RISC-V atomic-instruction extension, "A", specifies

14 \* the number of instructions that atomically read-modify-write memory,

15 \* which RISC-V harts should support in order to synchronise harts

16 \* running in the same memory space. This is the subset of RISC-V

17 \* atomic-instructions not present in atomic\_builtin.h file.

18 \*/

19

20#ifdef CONFIG\_64BIT

21static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_swap](arch_2riscv_2atomic_8h.md#ad7b411811c56512edd93b23c5aa5a503)(const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) newval)

22{

23 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) ret;

24

25 \_\_asm\_\_ volatile("amoswap.d.aq %0, %1, %2"

26 : "=r"(ret)

27 : "r"(newval), "A"(\*target)

28 : "memory");

29

30 return ret;

31}

32

33static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_max](arch_2riscv_2atomic_8h.md#aebee55ea9e302b35ddb4555c726c8482)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

34{

35 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) ret;

36

37 \_\_asm\_\_ volatile("amomax.d.aq %0, %1, %2"

38 : "=r"(ret)

39 : "r"(value), "A"(\*target)

40 : "memory");

41

42 return ret;

43}

44

45static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_min](arch_2riscv_2atomic_8h.md#a9fdddd559afa2918ad69fafe91782df1)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

46{

47 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) ret;

48

49 \_\_asm\_\_ volatile("amomin.d.aq %0, %1, %2"

50 : "=r"(ret)

51 : "r"(value), "A"(\*target)

52 : "memory");

53

54 return ret;

55}

56

57static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_maxu](arch_2riscv_2atomic_8h.md#a51405da00fee2c1f894bab41e9c62386)(unsigned long \*target, unsigned long value)

58{

59 unsigned long ret;

60

61 \_\_asm\_\_ volatile("amomaxu.d.aq %0, %1, %2"

62 : "=r"(ret)

63 : "r"(value), "A"(\*target)

64 : "memory");

65

66 return ret;

67}

68

69static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_minu](arch_2riscv_2atomic_8h.md#af165e862d4fd1219838fd209fab3ef7c)(unsigned long \*target, unsigned long value)

70{

71 unsigned long ret;

72

73 \_\_asm\_\_ volatile("amominu.d.aq %0, %1, %2"

74 : "=r"(ret)

75 : "r"(value), "A"(\*target)

76 : "memory");

77

78 return ret;

79}

80

81#else

82

[ 83](arch_2riscv_2atomic_8h.md#ad7b411811c56512edd93b23c5aa5a503)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_swap](arch_2riscv_2atomic_8h.md#ad7b411811c56512edd93b23c5aa5a503)(const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) newval)

84{

85 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) ret;

86

87 \_\_asm\_\_ volatile("amoswap.w.aq %0, %1, %2"

88 : "=r"(ret)

89 : "r"(newval), "A"(\*target)

90 : "memory");

91

92 return ret;

93}

94

[ 95](arch_2riscv_2atomic_8h.md#aebee55ea9e302b35ddb4555c726c8482)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_max](arch_2riscv_2atomic_8h.md#aebee55ea9e302b35ddb4555c726c8482)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

96{

97 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) ret;

98

99 \_\_asm\_\_ volatile("amomax.w.aq %0, %1, %2"

100 : "=r"(ret)

101 : "r"(value), "A"(\*target)

102 : "memory");

103

104 return ret;

105}

106

[ 107](arch_2riscv_2atomic_8h.md#a9fdddd559afa2918ad69fafe91782df1)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_min](arch_2riscv_2atomic_8h.md#a9fdddd559afa2918ad69fafe91782df1)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value)

108{

109 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) ret;

110

111 \_\_asm\_\_ volatile("amomin.w.aq %0, %1, %2"

112 : "=r"(ret)

113 : "r"(value), "A"(\*target)

114 : "memory");

115

116 return ret;

117}

118

[ 119](arch_2riscv_2atomic_8h.md#a51405da00fee2c1f894bab41e9c62386)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned long [atomic\_maxu](arch_2riscv_2atomic_8h.md#a51405da00fee2c1f894bab41e9c62386)(unsigned long \*target, unsigned long value)

120{

121 unsigned long ret;

122

123 \_\_asm\_\_ volatile("amomaxu.w.aq %0, %1, %2"

124 : "=r"(ret)

125 : "r"(value), "A"(\*target)

126 : "memory");

127

128 return ret;

129}

130

[ 131](arch_2riscv_2atomic_8h.md#af165e862d4fd1219838fd209fab3ef7c)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned long [atomic\_minu](arch_2riscv_2atomic_8h.md#af165e862d4fd1219838fd209fab3ef7c)(unsigned long \*target, unsigned long value)

132{

133 unsigned long ret;

134

135 \_\_asm\_\_ volatile("amominu.w.aq %0, %1, %2"

136 : "=r"(ret)

137 : "r"(value), "A"(\*target)

138 : "memory");

139

140 return ret;

141}

142

143#endif /\* CONFIG\_64BIT \*/

144

145#ifdef \_\_cplusplus

146}

147#endif

148

149#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ATOMIC\_H\_ \*/

[atomic\_maxu](arch_2riscv_2atomic_8h.md#a51405da00fee2c1f894bab41e9c62386)

static ALWAYS\_INLINE unsigned long atomic\_maxu(unsigned long \*target, unsigned long value)

**Definition** atomic.h:119

[atomic\_min](arch_2riscv_2atomic_8h.md#a9fdddd559afa2918ad69fafe91782df1)

static ALWAYS\_INLINE atomic\_val\_t atomic\_min(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic.h:107

[atomic\_swap](arch_2riscv_2atomic_8h.md#ad7b411811c56512edd93b23c5aa5a503)

static ALWAYS\_INLINE atomic\_val\_t atomic\_swap(const atomic\_t \*target, atomic\_val\_t newval)

Copyright (c) 2024 NextSilicon SPDX-License-Identifier: Apache-2.0.

**Definition** atomic.h:83

[atomic\_max](arch_2riscv_2atomic_8h.md#aebee55ea9e302b35ddb4555c726c8482)

static ALWAYS\_INLINE atomic\_val\_t atomic\_max(atomic\_t \*target, atomic\_val\_t value)

**Definition** atomic.h:95

[atomic\_minu](arch_2riscv_2atomic_8h.md#af165e862d4fd1219838fd209fab3ef7c)

static ALWAYS\_INLINE unsigned long atomic\_minu(unsigned long \*target, unsigned long value)

**Definition** atomic.h:131

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)

atomic\_t atomic\_val\_t

**Definition** atomic\_types.h:16

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [atomic.h](arch_2riscv_2atomic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
