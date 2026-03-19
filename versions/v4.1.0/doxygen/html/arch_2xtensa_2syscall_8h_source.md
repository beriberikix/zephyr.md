---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arch_2xtensa_2syscall_8h_source.html
original_path: doxygen/html/arch_2xtensa_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

34[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) xtensa\_syscall\_helper\_args\_6([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

35 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

36 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

37 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

38

39[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) xtensa\_syscall\_helper\_args\_5([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

40 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

41 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

42

43[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) xtensa\_syscall\_helper\_args\_4([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

44 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

45 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

46

47#define SYSINL ALWAYS\_INLINE

48#else

[ 49](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741)#define SYSINL inline

50#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

51

60

61

[ 62](arch_2xtensa_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

63 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

64 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

65 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

66{

67#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

68 return xtensa\_syscall\_helper\_args\_6(arg1, arg2, arg3, arg4, arg5, arg6, call\_id);

69#else

70 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

71 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

72 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

73 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

74 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

75 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a8 \_\_asm\_\_("%a8") = arg5;

76 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a9 \_\_asm\_\_("%a9") = arg6;

77

78 \_\_asm\_\_ volatile("syscall\n\t"

79 : "=r" (a2)

80 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

81 "r" (a5), "r" (a8), "r" (a9)

82 : "memory");

83

84 return a2;

85#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

86}

87

[ 88](arch_2xtensa_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

89 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

90 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

91{

92#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

93 return xtensa\_syscall\_helper\_args\_5(arg1, arg2, arg3, arg4, arg5, call\_id);

94#else

95 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

96 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

97 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

98 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

99 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

100 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a8 \_\_asm\_\_("%a8") = arg5;

101

102 \_\_asm\_\_ volatile("syscall\n\t"

103 : "=r" (a2)

104 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

105 "r" (a5), "r" (a8)

106 : "memory");

107

108 return a2;

109#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

110}

111

[ 112](arch_2xtensa_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

113 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

114 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

115{

116#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

117 return xtensa\_syscall\_helper\_args\_4(arg1, arg2, arg3, arg4, call\_id);

118#else

119 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

120 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

121 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

122 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

123 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

124

125 \_\_asm\_\_ volatile("syscall\n\t"

126 : "=r" (a2)

127 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

128 "r" (a5)

129 : "memory");

130

131 return a2;

132#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

133}

134

[ 135](arch_2xtensa_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

136 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

137{

138 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

139 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

140 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

141 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

142

143 \_\_asm\_\_ volatile("syscall\n\t"

144 : "=r" (a2)

145 : "r" (a2), "r" (a6), "r" (a3), "r" (a4)

146 : "memory");

147

148 return a2;

149}

150

[ 151](arch_2xtensa_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

152 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

153{

154 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

155 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

156 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

157

158 \_\_asm\_\_ volatile("syscall\n\t"

159 : "=r" (a2)

160 : "r" (a2), "r" (a6), "r" (a3)

161 : "memory");

162

163 return a2;

164}

165

[ 166](arch_2xtensa_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

167{

168 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

169 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

170

171 \_\_asm\_\_ volatile("syscall\n\t"

172 : "=r" (a2)

173 : "r" (a2), "r" (a6)

174 : "memory");

175

176 return a2;

177}

178

[ 179](arch_2xtensa_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

180{

181 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

182

183 \_\_asm\_\_ volatile("syscall\n\t"

184 : "=r" (a2)

185 : "r" (a2)

186 : "memory");

187

188 return a2;

189}

190

191/\*

192 \* There is no easy (or generic) way to figure out if a thread is runnining

193 \* in un-privileged mode. Reading the current ring (PS.CRING) is a privileged

194 \* instruction and not thread local storage is not available in xcc.

195 \*/

[ 196](arch_2xtensa_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)static inline bool [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)(void)

197{

198#if XCHAL\_HAVE\_THREADPTR

199 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) thread;

200

201 \_\_asm\_\_ volatile(

202 "rur.THREADPTR %0\n\t"

203 : "=a" (thread)

204 );

205#ifdef CONFIG\_THREAD\_LOCAL\_STORAGE

206 extern Z\_THREAD\_LOCAL [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) is\_user\_mode;

207

208 if (!thread) {

209 return false;

210 }

211

212 return is\_user\_mode != 0;

213#else

214 return !!thread;

215#endif

216

217#else /\* XCHAL\_HAVE\_THREADPTR \*/

218 extern bool xtensa\_is\_user\_context(void);

219

220 return xtensa\_is\_user\_context();

221#endif /\* XCHAL\_HAVE\_THREADPTR \*/

222}

223

224#undef SYSINL

225

226#ifdef \_\_cplusplus

227}

228#endif

229

230#endif /\* \_ASMLANGUAGE \*/

231#endif /\* CONFIG\_USERSPACE \*/

232#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_SYSCALL\_H\_ \*/

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

**Definition** syscall.h:49

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
