---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2xtensa_2syscall_8h_source.html
original_path: doxygen/html/arch_2xtensa_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h

[Go to the documentation of this file.](arch_2xtensa_2syscall_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_SYSCALL\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_SYSCALL\_H\_

18

19#ifdef CONFIG\_USERSPACE

20#ifndef \_ASMLANGUAGE

21

22#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

23#include <[stdbool.h](stdbool_8h.md)>

24#include <[zephyr/linker/sections.h](sections_8h.md)>

25#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

31#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

32[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) xtensa\_syscall\_helper([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

33 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

34 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

35 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

36

37#define SYSINL ALWAYS\_INLINE

38#else

[ 39](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741)#define SYSINL inline

40#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

41

50

[ 51](arch_2xtensa_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

52 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

53 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

54 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

55{

56#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

57 return xtensa\_syscall\_helper(arg1, arg2, arg3, arg4, arg5, arg6, call\_id);

58#else

59 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

60 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

61 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

62 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

63 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

64 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a8 \_\_asm\_\_("%a8") = arg5;

65 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a9 \_\_asm\_\_("%a9") = arg6;

66

67 \_\_asm\_\_ volatile("syscall\n\t"

68 : "=r" (a2)

69 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

70 "r" (a5), "r" (a8), "r" (a9)

71 : "memory");

72

73 return a2;

74#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

75}

76

[ 77](arch_2xtensa_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

78 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

79 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

80{

81#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

82 return xtensa\_syscall\_helper(arg1, arg2, arg3, arg4, arg5, 0, call\_id);

83#else

84 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

85 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

86 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

87 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

88 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

89 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a8 \_\_asm\_\_("%a8") = arg5;

90

91 \_\_asm\_\_ volatile("syscall\n\t"

92 : "=r" (a2)

93 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

94 "r" (a5), "r" (a8)

95 : "memory");

96

97 return a2;

98#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

99}

100

[ 101](arch_2xtensa_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

102 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

103 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

104{

105#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

106 return xtensa\_syscall\_helper(arg1, arg2, arg3, arg4, 0, 0, call\_id);

107#else

108 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

109 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

110 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

111 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

112 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

113

114 \_\_asm\_\_ volatile("syscall\n\t"

115 : "=r" (a2)

116 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

117 "r" (a5)

118 : "memory");

119

120 return a2;

121#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

122}

123

[ 124](arch_2xtensa_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

125 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

126{

127#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

128 return xtensa\_syscall\_helper(arg1, arg2, arg3, 0, 0, 0, call\_id);

129#else

130 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

131 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

132 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

133 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

134

135 \_\_asm\_\_ volatile("syscall\n\t"

136 : "=r" (a2)

137 : "r" (a2), "r" (a6), "r" (a3), "r" (a4)

138 : "memory");

139

140 return a2;

141#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

142}

143

[ 144](arch_2xtensa_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

145 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

146{

147#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

148 return xtensa\_syscall\_helper(arg1, arg2, 0, 0, 0, 0, call\_id);

149#else

150 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

151 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

152 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

153

154 \_\_asm\_\_ volatile("syscall\n\t"

155 : "=r" (a2)

156 : "r" (a2), "r" (a6), "r" (a3)

157 : "memory");

158

159 return a2;

160#endif

161}

162

[ 163](arch_2xtensa_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1,

164 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

165{

166#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

167 return xtensa\_syscall\_helper(arg1, 0, 0, 0, 0, 0, call\_id);

168#else

169 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

170 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

171

172 \_\_asm\_\_ volatile("syscall\n\t"

173 : "=r" (a2)

174 : "r" (a2), "r" (a6)

175 : "memory");

176

177 return a2;

178#endif

179}

180

[ 181](arch_2xtensa_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

182{

183#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

184 return xtensa\_syscall\_helper(0, 0, 0, 0, 0, 0, call\_id);

185#else

186 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

187

188 \_\_asm\_\_ volatile("syscall\n\t"

189 : "=r" (a2)

190 : "r" (a2)

191 : "memory");

192

193 return a2;

194#endif

195}

196

197/\*

198 \* There is no easy (or generic) way to figure out if a thread is runnining

199 \* in un-privileged mode. Reading the currrent ring (PS.CRING) is a privileged

200 \* instruction and not thread local storage is not available in xcc.

201 \*/

[ 202](arch_2xtensa_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)static inline bool [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)(void)

203{

204 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) thread;

205

206 \_\_asm\_\_ volatile(

207 "rur.THREADPTR %0\n\t"

208 : "=a" (thread)

209 );

210#ifdef CONFIG\_THREAD\_LOCAL\_STORAGE

211 extern \_\_thread [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) is\_user\_mode;

212

213 if (!thread) {

214 return false;

215 }

216

217 return is\_user\_mode != 0;

218#else

219 return !!thread;

220#endif

221}

222

223#undef SYSINL

224

225#ifdef \_\_cplusplus

226}

227#endif

228

229#endif /\* \_ASMLANGUAGE \*/

230#endif /\* CONFIG\_USERSPACE \*/

231#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_SYSCALL\_H\_ \*/

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

[SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741)

#define SYSINL

**Definition** syscall.h:39

[types.h](include_2zephyr_2types_8h.md)

[sections.h](sections_8h.md)

Definitions of various linker Sections.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [syscall.h](arch_2xtensa_2syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
