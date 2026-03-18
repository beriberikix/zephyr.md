---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2xtensa_2syscall_8h_source.html
original_path: doxygen/html/arch_2xtensa_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

27#include <xtensa/config/core-isa.h>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

33#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

34[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) xtensa\_syscall\_helper([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

35 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

36 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

37 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

38

39#define SYSINL ALWAYS\_INLINE

40#else

[ 41](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741)#define SYSINL inline

42#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

43

52

[ 53](arch_2xtensa_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

54 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

55 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

56 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

57{

58#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

59 return xtensa\_syscall\_helper(arg1, arg2, arg3, arg4, arg5, arg6, call\_id);

60#else

61 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

62 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

63 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

64 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

65 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

66 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a8 \_\_asm\_\_("%a8") = arg5;

67 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a9 \_\_asm\_\_("%a9") = arg6;

68

69 \_\_asm\_\_ volatile("syscall\n\t"

70 : "=r" (a2)

71 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

72 "r" (a5), "r" (a8), "r" (a9)

73 : "memory");

74

75 return a2;

76#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

77}

78

[ 79](arch_2xtensa_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

80 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

81 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

82{

83#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

84 return xtensa\_syscall\_helper(arg1, arg2, arg3, arg4, arg5, 0, call\_id);

85#else

86 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

87 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

88 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

89 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

90 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

91 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a8 \_\_asm\_\_("%a8") = arg5;

92

93 \_\_asm\_\_ volatile("syscall\n\t"

94 : "=r" (a2)

95 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

96 "r" (a5), "r" (a8)

97 : "memory");

98

99 return a2;

100#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

101}

102

[ 103](arch_2xtensa_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

104 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

105 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

106{

107#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

108 return xtensa\_syscall\_helper(arg1, arg2, arg3, arg4, 0, 0, call\_id);

109#else

110 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

111 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

112 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

113 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

114 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

115

116 \_\_asm\_\_ volatile("syscall\n\t"

117 : "=r" (a2)

118 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

119 "r" (a5)

120 : "memory");

121

122 return a2;

123#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

124}

125

[ 126](arch_2xtensa_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

127 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

128{

129#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

130 return xtensa\_syscall\_helper(arg1, arg2, arg3, 0, 0, 0, call\_id);

131#else

132 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

133 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

134 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

135 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

136

137 \_\_asm\_\_ volatile("syscall\n\t"

138 : "=r" (a2)

139 : "r" (a2), "r" (a6), "r" (a3), "r" (a4)

140 : "memory");

141

142 return a2;

143#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

144}

145

[ 146](arch_2xtensa_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

147 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

148{

149#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

150 return xtensa\_syscall\_helper(arg1, arg2, 0, 0, 0, 0, call\_id);

151#else

152 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

153 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

154 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

155

156 \_\_asm\_\_ volatile("syscall\n\t"

157 : "=r" (a2)

158 : "r" (a2), "r" (a6), "r" (a3)

159 : "memory");

160

161 return a2;

162#endif

163}

164

[ 165](arch_2xtensa_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1,

166 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

167{

168#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

169 return xtensa\_syscall\_helper(arg1, 0, 0, 0, 0, 0, call\_id);

170#else

171 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

172 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

173

174 \_\_asm\_\_ volatile("syscall\n\t"

175 : "=r" (a2)

176 : "r" (a2), "r" (a6)

177 : "memory");

178

179 return a2;

180#endif

181}

182

[ 183](arch_2xtensa_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

184{

185#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

186 return xtensa\_syscall\_helper(0, 0, 0, 0, 0, 0, call\_id);

187#else

188 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

189

190 \_\_asm\_\_ volatile("syscall\n\t"

191 : "=r" (a2)

192 : "r" (a2)

193 : "memory");

194

195 return a2;

196#endif

197}

198

199/\*

200 \* There is no easy (or generic) way to figure out if a thread is runnining

201 \* in un-privileged mode. Reading the current ring (PS.CRING) is a privileged

202 \* instruction and not thread local storage is not available in xcc.

203 \*/

[ 204](arch_2xtensa_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)static inline bool [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)(void)

205{

206#if XCHAL\_HAVE\_THREADPTR

207 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) thread;

208

209 \_\_asm\_\_ volatile(

210 "rur.THREADPTR %0\n\t"

211 : "=a" (thread)

212 );

213#ifdef CONFIG\_THREAD\_LOCAL\_STORAGE

214 extern \_\_thread [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) is\_user\_mode;

215

216 if (!thread) {

217 return false;

218 }

219

220 return is\_user\_mode != 0;

221#else

222 return !!thread;

223#endif

224

225#else /\* XCHAL\_HAVE\_THREADPTR \*/

226 extern bool xtensa\_is\_user\_context(void);

227

228 return xtensa\_is\_user\_context();

229#endif /\* XCHAL\_HAVE\_THREADPTR \*/

230}

231

232#undef SYSINL

233

234#ifdef \_\_cplusplus

235}

236#endif

237

238#endif /\* \_ASMLANGUAGE \*/

239#endif /\* CONFIG\_USERSPACE \*/

240#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_SYSCALL\_H\_ \*/

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

**Definition** syscall.h:41

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
