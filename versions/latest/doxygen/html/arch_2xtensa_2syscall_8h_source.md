---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arch_2xtensa_2syscall_8h_source.html
original_path: doxygen/html/arch_2xtensa_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

33/\* When syscall assembly is executed, the EPC points to the syscall

34 \* instruction, and we have to manually advance it so we will

35 \* return to the instruction after syscall to continue execution.

36 \* However, with zero-overhead loops and the syscall instruction is

37 \* the last instruction, this simple addition does not work as it

38 \* would point past the loop and would have skipped the loop.

39 \* Because of this, syscall entrance would need to look at the loop

40 \* registers and set the PC back to the beginning of loop if we are

41 \* still looping. Assuming most of the syscalls are not inside

42 \* loops, the extra handling code consumes quite a few cycles.

43 \* To workaround this, simply adds a nop after syscall so we no

44 \* longer have to deal with loops at syscall entrance, and that

45 \* a nop is faster than all the code to manipulate loop registers.

46 \*/

47#ifdef XCHAL\_HAVE\_LOOPS

48#define XTENSA\_SYSCALL\_ASM "syscall; nop;"

49#else

[ 50](arch_2xtensa_2syscall_8h.md#ae894ee9b6b190499380248043b461434)#define XTENSA\_SYSCALL\_ASM "syscall"

51#endif

52

53#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

54[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) xtensa\_syscall\_helper\_args\_6([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

55 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

56 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

57 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

58

59[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) xtensa\_syscall\_helper\_args\_5([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

60 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

61 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

62

63[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) xtensa\_syscall\_helper\_args\_4([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

64 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

65 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id);

66

67#define SYSINL ALWAYS\_INLINE

68#else

[ 69](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741)#define SYSINL inline

70#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

71

80

81

[ 82](arch_2xtensa_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

83 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

84 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

85 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

86{

87#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

88 return xtensa\_syscall\_helper\_args\_6(arg1, arg2, arg3, arg4, arg5, arg6, call\_id);

89#else

90 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

91 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

92 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

93 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

94 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

95 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a8 \_\_asm\_\_("%a8") = arg5;

96 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a9 \_\_asm\_\_("%a9") = arg6;

97

98 \_\_asm\_\_ volatile([XTENSA\_SYSCALL\_ASM](arch_2xtensa_2syscall_8h.md#ae894ee9b6b190499380248043b461434)

99 : "=r" (a2)

100 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

101 "r" (a5), "r" (a8), "r" (a9)

102 : "memory");

103

104 return a2;

105#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

106}

107

[ 108](arch_2xtensa_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

109 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

110 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

111{

112#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

113 return xtensa\_syscall\_helper\_args\_5(arg1, arg2, arg3, arg4, arg5, call\_id);

114#else

115 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

116 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

117 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

118 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

119 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

120 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a8 \_\_asm\_\_("%a8") = arg5;

121

122 \_\_asm\_\_ volatile([XTENSA\_SYSCALL\_ASM](arch_2xtensa_2syscall_8h.md#ae894ee9b6b190499380248043b461434)

123 : "=r" (a2)

124 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

125 "r" (a5), "r" (a8)

126 : "memory");

127

128 return a2;

129#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

130}

131

[ 132](arch_2xtensa_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)static [SYSINL](arch_2xtensa_2syscall_8h.md#a33d81dc0242dff05fdc92eb508224741) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

133 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

134 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

135{

136#ifdef CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER

137 return xtensa\_syscall\_helper\_args\_4(arg1, arg2, arg3, arg4, call\_id);

138#else

139 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

140 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

141 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

142 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

143 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a5 \_\_asm\_\_("%a5") = arg4;

144

145 \_\_asm\_\_ volatile([XTENSA\_SYSCALL\_ASM](arch_2xtensa_2syscall_8h.md#ae894ee9b6b190499380248043b461434)

146 : "=r" (a2)

147 : "r" (a2), "r" (a6), "r" (a3), "r" (a4),

148 "r" (a5)

149 : "memory");

150

151 return a2;

152#endif /\* CONFIG\_XTENSA\_SYSCALL\_USE\_HELPER \*/

153}

154

[ 155](arch_2xtensa_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

156 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

157{

158 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

159 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

160 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

161 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a4 \_\_asm\_\_("%a4") = arg3;

162

163 \_\_asm\_\_ volatile([XTENSA\_SYSCALL\_ASM](arch_2xtensa_2syscall_8h.md#ae894ee9b6b190499380248043b461434)

164 : "=r" (a2)

165 : "r" (a2), "r" (a6), "r" (a3), "r" (a4)

166 : "memory");

167

168 return a2;

169}

170

[ 171](arch_2xtensa_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

172 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

173{

174 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

175 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

176 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a3 \_\_asm\_\_("%a3") = arg2;

177

178 \_\_asm\_\_ volatile([XTENSA\_SYSCALL\_ASM](arch_2xtensa_2syscall_8h.md#ae894ee9b6b190499380248043b461434)

179 : "=r" (a2)

180 : "r" (a2), "r" (a6), "r" (a3)

181 : "memory");

182

183 return a2;

184}

185

[ 186](arch_2xtensa_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

187{

188 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

189 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a6 \_\_asm\_\_("%a6") = arg1;

190

191 \_\_asm\_\_ volatile([XTENSA\_SYSCALL\_ASM](arch_2xtensa_2syscall_8h.md#ae894ee9b6b190499380248043b461434)

192 : "=r" (a2)

193 : "r" (a2), "r" (a6)

194 : "memory");

195

196 return a2;

197}

198

[ 199](arch_2xtensa_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

200{

201 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) a2 \_\_asm\_\_("%a2") = call\_id;

202

203 \_\_asm\_\_ volatile([XTENSA\_SYSCALL\_ASM](arch_2xtensa_2syscall_8h.md#ae894ee9b6b190499380248043b461434)

204 : "=r" (a2)

205 : "r" (a2)

206 : "memory");

207

208 return a2;

209}

210

211/\*

212 \* There is no easy (or generic) way to figure out if a thread is runnining

213 \* in un-privileged mode. Reading the current ring (PS.CRING) is a privileged

214 \* instruction and not thread local storage is not available in xcc.

215 \*/

[ 216](arch_2xtensa_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)static inline bool [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)(void)

217{

218#if XCHAL\_HAVE\_THREADPTR

219 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) thread;

220

221 \_\_asm\_\_ volatile(

222 "rur.THREADPTR %0\n\t"

223 : "=a" (thread)

224 );

225#ifdef CONFIG\_THREAD\_LOCAL\_STORAGE

226 extern Z\_THREAD\_LOCAL [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) is\_user\_mode;

227

228 if (!thread) {

229 return false;

230 }

231

232 return is\_user\_mode != 0;

233#else

234 return !!thread;

235#endif

236

237#else /\* XCHAL\_HAVE\_THREADPTR \*/

238 extern bool xtensa\_is\_user\_context(void);

239

240 return xtensa\_is\_user\_context();

241#endif /\* XCHAL\_HAVE\_THREADPTR \*/

242}

243

244#undef SYSINL

245

246#ifdef \_\_cplusplus

247}

248#endif

249

250#endif /\* \_ASMLANGUAGE \*/

251#endif /\* CONFIG\_USERSPACE \*/

252#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_SYSCALL\_H\_ \*/

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

**Definition** syscall.h:69

[XTENSA\_SYSCALL\_ASM](arch_2xtensa_2syscall_8h.md#ae894ee9b6b190499380248043b461434)

#define XTENSA\_SYSCALL\_ASM

**Definition** syscall.h:50

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
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
