---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2x86_2ia32_2syscall_8h_source.html
original_path: doxygen/html/arch_2x86_2ia32_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h

[Go to the documentation of this file.](arch_2x86_2ia32_2syscall_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_SYSCALL\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_SYSCALL\_H\_

18

[ 19](arch_2x86_2ia32_2syscall_8h.md#a719fbb690b1312f487003392d29970b0)#define USER\_CODE\_SEG 0x2b /\* at dpl=3 \*/

[ 20](arch_2x86_2ia32_2syscall_8h.md#a4a394d2afb6791022239b7526f24782c)#define USER\_DATA\_SEG 0x33 /\* at dpl=3 \*/

21

22#ifdef CONFIG\_USERSPACE

23#ifndef \_ASMLANGUAGE

24

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[stdbool.h](stdbool_8h.md)>

27#include <[zephyr/linker/sections.h](sections_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

33/\* Syscall invocation macros. x86-specific machine constraints used to ensure

34 \* args land in the proper registers, see implementation of

35 \* z\_x86\_syscall\_entry\_stub in userspace.S

36 \*/

37

38\_\_pinned\_func

[ 39](arch_2x86_2ia32_2syscall_8h.md#ac9d314e4cd03416c9327a90cf71ce7b8)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

40 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

41 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

42 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

43{

44 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

45

46 \_\_asm\_\_ volatile("push %%ebp\n\t"

47 "mov %[arg6], %%ebp\n\t"

48 "int $0x80\n\t"

49 "pop %%ebp\n\t"

50 : "=a" (ret)

51 : "S" (call\_id), "a" (arg1), "d" (arg2),

52 "c" (arg3), "b" (arg4), "D" (arg5),

53 [arg6] "m" (arg6)

54 : "memory");

55 return ret;

56}

57

58\_\_pinned\_func

[ 59](arch_2x86_2ia32_2syscall_8h.md#a892f88703053430c55312fe146b6967b)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

60 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

61 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5,

62 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

63{

64 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

65

66 \_\_asm\_\_ volatile("int $0x80"

67 : "=a" (ret)

68 : "S" (call\_id), "a" (arg1), "d" (arg2),

69 "c" (arg3), "b" (arg4), "D" (arg5)

70 : "memory");

71 return ret;

72}

73

74\_\_pinned\_func

[ 75](arch_2x86_2ia32_2syscall_8h.md#ae592b58d4430222fe9cd598b6ccbeb0a)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

76 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

77 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

78{

79 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

80

81 \_\_asm\_\_ volatile("int $0x80"

82 : "=a" (ret)

83 : "S" (call\_id), "a" (arg1), "d" (arg2), "c" (arg3),

84 "b" (arg4)

85 : "memory");

86 return ret;

87}

88

89\_\_pinned\_func

[ 90](arch_2x86_2ia32_2syscall_8h.md#a7804d200754b8dc00b211a6419241a6d)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

91 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3,

92 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

93{

94 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

95

96 \_\_asm\_\_ volatile("int $0x80"

97 : "=a" (ret)

98 : "S" (call\_id), "a" (arg1), "d" (arg2), "c" (arg3)

99 : "memory");

100 return ret;

101}

102

103\_\_pinned\_func

[ 104](arch_2x86_2ia32_2syscall_8h.md#adea10ca87424364cafb2e784873473f1)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

105 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

106{

107 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

108

109 \_\_asm\_\_ volatile("int $0x80"

110 : "=a" (ret)

111 : "S" (call\_id), "a" (arg1), "d" (arg2)

112 : "memory"

113 );

114 return ret;

115}

116

117\_\_pinned\_func

[ 118](arch_2x86_2ia32_2syscall_8h.md#a41d16c05d5ea97ba21f84120d9254d8c)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1,

119 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

120{

121 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

122

123 \_\_asm\_\_ volatile("int $0x80"

124 : "=a" (ret)

125 : "S" (call\_id), "a" (arg1)

126 : "memory"

127 );

128 return ret;

129}

130

131\_\_pinned\_func

[ 132](arch_2x86_2ia32_2syscall_8h.md#a3e917733f2f35e18d5b2813558fa375e)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

133{

134 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

135

136 \_\_asm\_\_ volatile("int $0x80"

137 : "=a" (ret)

138 : "S" (call\_id)

139 : "memory"

140 );

141 return ret;

142}

143

144\_\_pinned\_func

[ 145](arch_2x86_2ia32_2syscall_8h.md#a4c6ec696182878eab8c1093b1d25157c)static inline bool [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)(void)

146{

147 int cs;

148

149 /\* On x86, read the CS register (which cannot be manually set) \*/

150 \_\_asm\_\_ volatile ("mov %%cs, %[cs\_val]" : [cs\_val] "=r" (cs));

151

152 return cs == [USER\_CODE\_SEG](arch_2x86_2ia32_2syscall_8h.md#a719fbb690b1312f487003392d29970b0);

153}

154

155

156#ifdef \_\_cplusplus

157}

158#endif

159

160#endif /\* \_ASMLANGUAGE \*/

161#endif /\* CONFIG\_USERSPACE \*/

162#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_SYSCALL\_H\_ \*/

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

[USER\_CODE\_SEG](arch_2x86_2ia32_2syscall_8h.md#a719fbb690b1312f487003392d29970b0)

#define USER\_CODE\_SEG

**Definition** syscall.h:19

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

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [syscall.h](arch_2x86_2ia32_2syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
