---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2arm_2syscall_8h_source.html
original_path: doxygen/html/arch_2arm_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h

[Go to the documentation of this file.](arch_2arm_2syscall_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_SYSCALL\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_SYSCALL\_H\_

18

19#define \_SVC\_CALL\_CONTEXT\_SWITCH 0

20#define \_SVC\_CALL\_IRQ\_OFFLOAD 1

21#define \_SVC\_CALL\_RUNTIME\_EXCEPT 2

22#define \_SVC\_CALL\_SYSTEM\_CALL 3

23

24#ifdef CONFIG\_USERSPACE

25#ifndef \_ASMLANGUAGE

26

27#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

28#include <[stdbool.h](stdbool_8h.md)>

29#include <[zephyr/arch/arm/misc.h](arm_2misc_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

35

36/\* Syscall invocation macros. arm-specific machine constraints used to ensure

37 \* args land in the proper registers.

38 \*/

[ 39](arch_2arm_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

40 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

41 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

42 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

43{

44 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

45 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

46 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

47 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r3 \_\_asm\_\_("r3") = arg4;

48 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r4 \_\_asm\_\_("r4") = arg5;

49 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r5 \_\_asm\_\_("r5") = arg6;

50 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

51

52 \_\_asm\_\_ volatile("svc %[svid]\n"

53 : "=r"(ret), "=r"(r1), "=r"(r2), "=r"(r3)

54 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

55 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

56 "r" (r4), "r" (r5), "r" (r6)

57 : "r8", "memory", "ip");

58

59 return ret;

60}

61

[ 62](arch_2arm_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

63 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

64 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5,

65 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

66{

67 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

68 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

69 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

70 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r3 \_\_asm\_\_("r3") = arg4;

71 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r4 \_\_asm\_\_("r4") = arg5;

72 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

73

74 \_\_asm\_\_ volatile("svc %[svid]\n"

75 : "=r"(ret), "=r"(r1), "=r"(r2), "=r"(r3)

76 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

77 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

78 "r" (r4), "r" (r6)

79 : "r8", "memory", "ip");

80

81 return ret;

82}

83

[ 84](arch_2arm_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

85 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

86 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

87{

88 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

89 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

90 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

91 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r3 \_\_asm\_\_("r3") = arg4;

92 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

93

94 \_\_asm\_\_ volatile("svc %[svid]\n"

95 : "=r"(ret), "=r"(r1), "=r"(r2), "=r"(r3)

96 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

97 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

98 "r" (r6)

99 : "r8", "memory", "ip");

100

101 return ret;

102}

103

[ 104](arch_2arm_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

105 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3,

106 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

107{

108 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

109 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

110 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

111 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

112

113 \_\_asm\_\_ volatile("svc %[svid]\n"

114 : "=r"(ret), "=r"(r1), "=r"(r2)

115 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

116 "r" (ret), "r" (r1), "r" (r2), "r" (r6)

117 : "r8", "memory", "r3", "ip");

118

119 return ret;

120}

121

[ 122](arch_2arm_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

123 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

124{

125 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

126 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

127 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

128

129 \_\_asm\_\_ volatile("svc %[svid]\n"

130 : "=r"(ret), "=r"(r1)

131 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

132 "r" (ret), "r" (r1), "r" (r6)

133 : "r8", "memory", "r2", "r3", "ip");

134

135 return ret;

136}

137

[ 138](arch_2arm_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1,

139 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

140{

141 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

142 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

143

144 \_\_asm\_\_ volatile("svc %[svid]\n"

145 : "=r"(ret)

146 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

147 "r" (ret), "r" (r6)

148 : "r8", "memory", "r1", "r2", "r3", "ip");

149 return ret;

150}

151

[ 152](arch_2arm_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

153{

154 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0");

155 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

156

157 \_\_asm\_\_ volatile("svc %[svid]\n"

158 : "=r"(ret)

159 : [svid] "i" (\_SVC\_CALL\_SYSTEM\_CALL),

160 "r" (ret), "r" (r6)

161 : "r8", "memory", "r1", "r2", "r3", "ip");

162

163 return ret;

164}

165

[ 166](arch_2arm_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)static inline bool [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)(void)

167{

168#if defined(CONFIG\_CPU\_CORTEX\_M)

169 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value;

170

171 /\* check for handler mode \*/

172 \_\_asm\_\_ volatile("mrs %0, IPSR\n\t" : "=r"(value));

173 if (value) {

174 return false;

175 }

176#endif

177

178 return z\_arm\_thread\_is\_in\_user\_mode();

179}

180

181#ifdef \_\_cplusplus

182}

183#endif

184

185#endif /\* \_ASMLANGUAGE \*/

186#endif /\* CONFIG\_USERSPACE \*/

187#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_SYSCALL\_H\_ \*/

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

[misc.h](arm_2misc_8h.md)

ARM AArch32 public kernel miscellaneous.

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [syscall.h](arch_2arm_2syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
