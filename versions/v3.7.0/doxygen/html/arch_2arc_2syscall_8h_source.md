---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2arc_2syscall_8h_source.html
original_path: doxygen/html/arch_2arc_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h

[Go to the documentation of this file.](arch_2arc_2syscall_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_SYSCALL\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_SYSCALL\_H\_

18

19#define \_TRAP\_S\_CALL\_RUNTIME\_EXCEPT 2

20#define \_TRAP\_S\_CALL\_SYSTEM\_CALL 3

21

22#ifdef CONFIG\_USERSPACE

23#ifndef \_ASMLANGUAGE

24

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[stdbool.h](stdbool_8h.md)>

27

28#ifdef CONFIG\_ISA\_ARCV2

29#include <[zephyr/arch/arc/v2/aux\_regs.h](aux__regs_8h.md)>

30#endif

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35/\* Syscall invocation macros. arc-specific machine constraints used to ensure

36 \* args land in the proper registers. Currently, they are all stub functions

37 \* just for enabling CONFIG\_USERSPACE on arc w/o errors.

38 \*/

39

[ 40](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

41 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

42 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

43 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

44{

45 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

46 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

47 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

48 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r3 \_\_asm\_\_("r3") = arg4;

49 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r4 \_\_asm\_\_("r4") = arg5;

50 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r5 \_\_asm\_\_("r5") = arg6;

51 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

52

53 compiler\_barrier();

54

55 \_\_asm\_\_ volatile(

56 "trap\_s %[trap\_s\_id]\n"

57 : "=r"(ret)

58 : [trap\_s\_id] "i" (\_TRAP\_S\_CALL\_SYSTEM\_CALL),

59 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

60 "r" (r4), "r" (r5), "r" (r6));

61

62 return ret;

63}

64

[ 65](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

66 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

67 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5,

68 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

69{

70 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

71 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

72 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

73 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r3 \_\_asm\_\_("r3") = arg4;

74 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r4 \_\_asm\_\_("r4") = arg5;

75 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

76

77 compiler\_barrier();

78

79 \_\_asm\_\_ volatile(

80 "trap\_s %[trap\_s\_id]\n"

81 : "=r"(ret)

82 : [trap\_s\_id] "i" (\_TRAP\_S\_CALL\_SYSTEM\_CALL),

83 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

84 "r" (r4), "r" (r6));

85

86 return ret;

87}

88

[ 89](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

90 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

91 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

92{

93 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

94 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

95 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

96 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r3 \_\_asm\_\_("r3") = arg4;

97 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

98

99 compiler\_barrier();

100

101 \_\_asm\_\_ volatile(

102 "trap\_s %[trap\_s\_id]\n"

103 : "=r"(ret)

104 : [trap\_s\_id] "i" (\_TRAP\_S\_CALL\_SYSTEM\_CALL),

105 "r" (ret), "r" (r1), "r" (r2), "r" (r3),

106 "r" (r6));

107

108 return ret;

109}

110

[ 111](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

112 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3,

113 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

114{

115 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

116 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

117 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r2 \_\_asm\_\_("r2") = arg3;

118 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

119

120 compiler\_barrier();

121

122 \_\_asm\_\_ volatile(

123 "trap\_s %[trap\_s\_id]\n"

124 : "=r"(ret)

125 : [trap\_s\_id] "i" (\_TRAP\_S\_CALL\_SYSTEM\_CALL),

126 "r" (ret), "r" (r1), "r" (r2), "r" (r6));

127

128 return ret;

129}

130

[ 131](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

132 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

133{

134 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

135 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r1 \_\_asm\_\_("r1") = arg2;

136 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

137

138 compiler\_barrier();

139

140 \_\_asm\_\_ volatile(

141 "trap\_s %[trap\_s\_id]\n"

142 : "=r"(ret)

143 : [trap\_s\_id] "i" (\_TRAP\_S\_CALL\_SYSTEM\_CALL),

144 "r" (ret), "r" (r1), "r" (r6));

145

146 return ret;

147}

148

[ 149](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

150{

151 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0") = arg1;

152 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

153

154 compiler\_barrier();

155

156 \_\_asm\_\_ volatile(

157 "trap\_s %[trap\_s\_id]\n"

158 : "=r"(ret)

159 : [trap\_s\_id] "i" (\_TRAP\_S\_CALL\_SYSTEM\_CALL),

160 "r" (ret), "r" (r6));

161

162 return ret;

163}

164

[ 165](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

166{

167 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret \_\_asm\_\_("r0");

168 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r6 \_\_asm\_\_("r6") = call\_id;

169

170 compiler\_barrier();

171

172 \_\_asm\_\_ volatile(

173 "trap\_s %[trap\_s\_id]\n"

174 : "=r"(ret)

175 : [trap\_s\_id] "i" (\_TRAP\_S\_CALL\_SYSTEM\_CALL),

176 "r" (ret), "r" (r6));

177

178 return ret;

179}

180

[ 181](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)static inline bool [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)(void)

182{

183 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status;

184

185 compiler\_barrier();

186

187 \_\_asm\_\_ volatile("lr %0, [%[status32]]\n"

188 : "=r"(status)

189 : [status32] "i" (\_ARC\_V2\_STATUS32));

190

191 return !(status & \_ARC\_V2\_STATUS32\_US) ? true : false;

192}

193

194#ifdef \_\_cplusplus

195}

196#endif

197

198#endif /\* \_ASMLANGUAGE \*/

199#endif /\* CONFIG\_USERSPACE \*/

200#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_SYSCALL\_H\_ \*/

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

[aux\_regs.h](aux__regs_8h.md)

ARCv2 auxiliary registers definitions.

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
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [syscall.h](arch_2arc_2syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
