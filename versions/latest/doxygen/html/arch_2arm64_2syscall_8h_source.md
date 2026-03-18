---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2arm64_2syscall_8h_source.html
original_path: doxygen/html/arch_2arm64_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h

[Go to the documentation of this file.](arch_2arm64_2syscall_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_SYSCALL\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_SYSCALL\_H\_

18

19#define \_SVC\_CALL\_IRQ\_OFFLOAD 1

20#define \_SVC\_CALL\_RUNTIME\_EXCEPT 2

21#define \_SVC\_CALL\_SYSTEM\_CALL 3

22

23#ifdef CONFIG\_USERSPACE

24#ifndef \_ASMLANGUAGE

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <[stdbool.h](stdbool_8h.md)>

28#include <[zephyr/arch/arm64/lib\_helpers.h](4_2lib__helpers_8h.md)>

29#include <[zephyr/arch/arm64/tpidrro\_el0.h](tpidrro__el0_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

35/\*

36 \* Syscall invocation macros. arm-specific machine constraints used to ensure

37 \* args land in the proper registers.

38 \*/

[ 39](arch_2arm64_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

40 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

41 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

42 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

43{

44 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret \_\_asm\_\_("x0") = arg1;

45 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r1 \_\_asm\_\_("x1") = arg2;

46 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r2 \_\_asm\_\_("x2") = arg3;

47 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r3 \_\_asm\_\_("x3") = arg4;

48 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r4 \_\_asm\_\_("x4") = arg5;

49 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r5 \_\_asm\_\_("x5") = arg6;

50 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r8 \_\_asm\_\_("x8") = call\_id;

51

52 \_\_asm\_\_ volatile("svc %[svid]\n"

53 : "=r"(ret)

54 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

55 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

56 "r" (r4), "r" (r5), "r" (r8)

57 : "memory");

58

59 return ret;

60}

61

[ 62](arch_2arm64_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

63 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

64 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5,

65 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

66{

67 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret \_\_asm\_\_("x0") = arg1;

68 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r1 \_\_asm\_\_("x1") = arg2;

69 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r2 \_\_asm\_\_("x2") = arg3;

70 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r3 \_\_asm\_\_("x3") = arg4;

71 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r4 \_\_asm\_\_("x4") = arg5;

72 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r8 \_\_asm\_\_("x8") = call\_id;

73

74 \_\_asm\_\_ volatile("svc %[svid]\n"

75 : "=r"(ret)

76 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

77 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

78 "r" (r4), "r" (r8)

79 : "memory");

80

81 return ret;

82}

83

[ 84](arch_2arm64_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

85 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

86 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

87{

88 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret \_\_asm\_\_("x0") = arg1;

89 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r1 \_\_asm\_\_("x1") = arg2;

90 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r2 \_\_asm\_\_("x2") = arg3;

91 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r3 \_\_asm\_\_("x3") = arg4;

92 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r8 \_\_asm\_\_("x8") = call\_id;

93

94 \_\_asm\_\_ volatile("svc %[svid]\n"

95 : "=r"(ret)

96 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

97 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

98 "r" (r8)

99 : "memory");

100

101 return ret;

102}

103

[ 104](arch_2arm64_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

105 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3,

106 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

107{

108 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret \_\_asm\_\_("x0") = arg1;

109 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r1 \_\_asm\_\_("x1") = arg2;

110 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r2 \_\_asm\_\_("x2") = arg3;

111 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r8 \_\_asm\_\_("x8") = call\_id;

112

113 \_\_asm\_\_ volatile("svc %[svid]\n"

114 : "=r"(ret)

115 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

116 "r" (ret), "r" (r1), "r" (r2), "r" (r8)

117 : "memory");

118

119 return ret;

120}

121

[ 122](arch_2arm64_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

123 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

124{

125 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret \_\_asm\_\_("x0") = arg1;

126 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r1 \_\_asm\_\_("x1") = arg2;

127 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r8 \_\_asm\_\_("x8") = call\_id;

128

129 \_\_asm\_\_ volatile("svc %[svid]\n"

130 : "=r"(ret)

131 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

132 "r" (ret), "r" (r1), "r" (r8)

133 : "memory");

134

135 return ret;

136}

137

[ 138](arch_2arm64_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1,

139 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

140{

141 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret \_\_asm\_\_("x0") = arg1;

142 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r8 \_\_asm\_\_("x8") = call\_id;

143

144 \_\_asm\_\_ volatile("svc %[svid]\n"

145 : "=r"(ret)

146 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

147 "r" (ret), "r" (r8)

148 : "memory");

149 return ret;

150}

151

[ 152](arch_2arm64_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

153{

154 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret \_\_asm\_\_("x0");

155 register [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r8 \_\_asm\_\_("x8") = call\_id;

156

157 \_\_asm\_\_ volatile("svc %[svid]\n"

158 : "=r"(ret)

159 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

160 "r" (ret), "r" (r8)

161 : "memory");

162

163 return ret;

164}

165

[ 166](arch_2arm64_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)static inline bool [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)(void)

167{

168 return ([read\_tpidrro\_el0](4_2lib__helpers_8h.md#a5d96400189d120420955eec6d7229490)() & [TPIDRROEL0\_IN\_EL0](tpidrro__el0_8h.md#a7350edf399cb3e4a9cf63010bf3954b7)) != 0;

169}

170

171#ifdef \_\_cplusplus

172}

173#endif

174

175#endif /\* \_ASMLANGUAGE \*/

176#endif /\* CONFIG\_USERSPACE \*/

177

178#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_SYSCALL\_H\_ \*/

[lib\_helpers.h](4_2lib__helpers_8h.md)

[read\_tpidrro\_el0](4_2lib__helpers_8h.md#a5d96400189d120420955eec6d7229490)

static ALWAYS\_INLINE uint64\_t read\_tpidrro\_el0(void)

**Definition** lib\_helpers.h:75

[arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)

static uintptr\_t arch\_syscall\_invoke4(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t arg4, uintptr\_t call\_id)

**Definition** syscall.h:89

[arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)

static uintptr\_t arch\_syscall\_invoke2(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t call\_id)

**Definition** syscall.h:131

[arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)

static uintptr\_t arch\_syscall\_invoke1(uintptr\_t arg1, uintptr\_t call\_id)

**Definition** syscall.h:149

[arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)

static uintptr\_t arch\_syscall\_invoke0(uintptr\_t call\_id)

**Definition** syscall.h:165

[arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)

static bool arch\_is\_user\_context(void)

**Definition** syscall.h:181

[arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)

static uintptr\_t arch\_syscall\_invoke5(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t arg4, uintptr\_t arg5, uintptr\_t call\_id)

**Definition** syscall.h:65

[arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)

static uintptr\_t arch\_syscall\_invoke3(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t call\_id)

**Definition** syscall.h:111

[arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)

static uintptr\_t arch\_syscall\_invoke6(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t arg4, uintptr\_t arg5, uintptr\_t arg6, uintptr\_t call\_id)

**Definition** syscall.h:40

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[tpidrro\_el0.h](tpidrro__el0_8h.md)

tpidrro\_el0 bits allocation

[TPIDRROEL0\_IN\_EL0](tpidrro__el0_8h.md#a7350edf399cb3e4a9cf63010bf3954b7)

#define TPIDRROEL0\_IN\_EL0

**Definition** tpidrro\_el0.h:20

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [syscall.h](arch_2arm64_2syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
