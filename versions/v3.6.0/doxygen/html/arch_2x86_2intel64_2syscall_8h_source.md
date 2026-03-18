---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2x86_2intel64_2syscall_8h_source.html
original_path: doxygen/html/arch_2x86_2intel64_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h

[Go to the documentation of this file.](arch_2x86_2intel64_2syscall_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_SYSCALL\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_SYSCALL\_H\_

18

19#ifdef CONFIG\_USERSPACE

20#ifndef \_ASMLANGUAGE

21

22#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

23#include <[stdbool.h](stdbool_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

29/\*

30 \* x86\_64 System V calling convention:

31 \* First six arguments passed in via RDI, RSI, RDX, RCX, R8, R9

32 \* We'll use RAX for the call\_id, and the return value

33 \*

34 \* Arrange registers so that they are in-place as much as possible when

35 \* doing the system call. Because RCX get overwritten by the CPU, put arg 4

36 \* in r10 instead.

37 \*

38 \* SYSCALL instruction stores return address in RCX and RFLAGS in R11. RIP is

39 \* loaded from LSTAR MSR, masks RFLAGS with the low 32 bits of EFER.SFMASK. CS

40 \* and SS are loaded from values derived from bits 47:32 of STAR MSR (+0

41 \* for CS, +8 for SS)

42 \*

43 \* SYSRET loads RIP from RCX and RFLAGS from r11. CS and SS are set with

44 \* values derived from STAR MSR bits 63:48 (+8 for CS, +16 for SS)

45 \*

46 \* The kernel is in charge of not clobbering across the system call

47 \* the remaining registers: RBX, RBP, R12-R15, SIMD/FPU, and any unused

48 \* argument registers.

49 \*/

[ 50](arch_2x86_2intel64_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

51 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

52 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

53 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

54{

55 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rax \_\_asm\_\_("%rax") = call\_id;

56 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rdi \_\_asm\_\_("%rdi") = arg1;

57 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rsi \_\_asm\_\_("%rsi") = arg2;

58 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rdx \_\_asm\_\_("%rdx") = arg3;

59 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) r10 \_\_asm\_\_("%r10") = arg4; /\* RCX unavailable \*/

60 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) r8 \_\_asm\_\_("%r8") = arg5;

61 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) r9 \_\_asm\_\_("%r9") = arg6;

62

63 \_\_asm\_\_ volatile("syscall\n\t"

64 : "=r" (rax)

65 : "r" (rax), "r" (rdi), "r" (rsi), "r" (rdx),

66 "r" (r10), "r" (r8), "r" (r9)

67 : "memory", "rcx", "r11");

68

69 return rax;

70}

71

[ 72](arch_2x86_2intel64_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

73 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

74 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5,

75 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

76{

77 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rax \_\_asm\_\_("%rax") = call\_id;

78 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rdi \_\_asm\_\_("%rdi") = arg1;

79 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rsi \_\_asm\_\_("%rsi") = arg2;

80 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rdx \_\_asm\_\_("%rdx") = arg3;

81 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) r10 \_\_asm\_\_("%r10") = arg4; /\* RCX unavailable \*/

82 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) r8 \_\_asm\_\_("%r8") = arg5;

83

84 \_\_asm\_\_ volatile("syscall\n\t"

85 : "=r" (rax)

86 : "r" (rax), "r" (rdi), "r" (rsi), "r" (rdx),

87 "r" (r10), "r" (r8)

88 : "memory", "rcx", "r11");

89

90 return rax;

91}

92

[ 93](arch_2x86_2intel64_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

94 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

95 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

96{

97 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rax \_\_asm\_\_("%rax") = call\_id;

98 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rdi \_\_asm\_\_("%rdi") = arg1;

99 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rsi \_\_asm\_\_("%rsi") = arg2;

100 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rdx \_\_asm\_\_("%rdx") = arg3;

101 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) r10 \_\_asm\_\_("%r10") = arg4; /\* RCX unavailable \*/

102

103 \_\_asm\_\_ volatile("syscall\n\t"

104 : "=r" (rax)

105 : "r" (rax), "r" (rdi), "r" (rsi), "r" (rdx),

106 "r" (r10)

107 : "memory", "rcx", "r11");

108

109 return rax;

110}

111

[ 112](arch_2x86_2intel64_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

113 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3,

114 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

115{

116 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rax \_\_asm\_\_("%rax") = call\_id;

117 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rdi \_\_asm\_\_("%rdi") = arg1;

118 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rsi \_\_asm\_\_("%rsi") = arg2;

119 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rdx \_\_asm\_\_("%rdx") = arg3;

120

121 \_\_asm\_\_ volatile("syscall\n\t"

122 : "=r" (rax)

123 : "r" (rax), "r" (rdi), "r" (rsi), "r" (rdx)

124 : "memory", "rcx", "r11");

125

126 return rax;

127}

128

[ 129](arch_2x86_2intel64_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

130 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

131

132{

133 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rax \_\_asm\_\_("%rax") = call\_id;

134 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rdi \_\_asm\_\_("%rdi") = arg1;

135 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rsi \_\_asm\_\_("%rsi") = arg2;

136

137 \_\_asm\_\_ volatile("syscall\n\t"

138 : "=r" (rax)

139 : "r" (rax), "r" (rdi), "r" (rsi)

140 : "memory", "rcx", "r11");

141

142 return rax;

143}

144

[ 145](arch_2x86_2intel64_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1,

146 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

147{

148 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rax \_\_asm\_\_("%rax") = call\_id;

149 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rdi \_\_asm\_\_("%rdi") = arg1;

150

151 \_\_asm\_\_ volatile("syscall\n\t"

152 : "=r" (rax)

153 : "r" (rax), "r" (rdi)

154 : "memory", "rcx", "r11");

155

156 return rax;

157}

158

[ 159](arch_2x86_2intel64_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

160{

161 register [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) rax \_\_asm\_\_("%rax") = call\_id;

162

163 \_\_asm\_\_ volatile("syscall\n\t"

164 : "=r" (rax)

165 : "r" (rax)

166 : "memory", "rcx", "r11");

167

168 return rax;

169}

170

[ 171](arch_2x86_2intel64_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)static inline bool [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)(void)

172{

173 int cs;

174

175 \_\_asm\_\_ volatile ("mov %%cs, %[cs\_val]" : [cs\_val] "=r" (cs));

176

177 return (cs & 0x3) != 0;

178}

179

180#ifdef \_\_cplusplus

181}

182#endif

183

184#endif /\* \_ASMLANGUAGE \*/

185#endif /\* CONFIG\_USERSPACE \*/

186#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_SYSCALL\_H\_ \*/

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

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [intel64](dir_1abf87bed33eaf4508c3178cbd4d6168.md)
- [syscall.h](arch_2x86_2intel64_2syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
