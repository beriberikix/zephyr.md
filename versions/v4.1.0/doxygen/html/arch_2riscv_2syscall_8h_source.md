---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arch_2riscv_2syscall_8h_source.html
original_path: doxygen/html/arch_2riscv_2syscall_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h

[Go to the documentation of this file.](arch_2riscv_2syscall_8h.md)

1/\*

2 \* Copyright (c) 2020 BayLibre, SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_SYSCALL\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_SYSCALL\_H\_

18

19/\*

20 \* Privileged mode system calls

21 \*/

[ 22](arch_2riscv_2syscall_8h.md#aaaa314af66dac111544e3a307c40aa7c)#define RV\_ECALL\_RUNTIME\_EXCEPT 0

[ 23](arch_2riscv_2syscall_8h.md#a7f48699bf5ec7239785d56a7ddbc5bc3)#define RV\_ECALL\_IRQ\_OFFLOAD 1

[ 24](arch_2riscv_2syscall_8h.md#a26019adf51e9a90aa823a1a59c2b25e3)#define RV\_ECALL\_SCHEDULE 2

25

26#ifndef \_ASMLANGUAGE

27

28#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

29#include <[stdbool.h](stdbool_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

35/\*

36 \* Syscall invocation macros. riscv-specific machine constraints used to ensure

37 \* args land in the proper registers.

38 \*/

[ 39](arch_2riscv_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke6](arch_2arc_2syscall_8h.md#ac6cae2197637993a86b6ec6803b5742b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

40 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

41 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

42 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

43{

44 register unsigned long a0 \_\_asm\_\_ ("a0") = arg1;

45 register unsigned long a1 \_\_asm\_\_ ("a1") = arg2;

46 register unsigned long a2 \_\_asm\_\_ ("a2") = arg3;

47 register unsigned long a3 \_\_asm\_\_ ("a3") = arg4;

48 register unsigned long a4 \_\_asm\_\_ ("a4") = arg5;

49 register unsigned long a5 \_\_asm\_\_ ("a5") = arg6;

50 register unsigned long t0 \_\_asm\_\_ ("t0") = call\_id;

51

52 \_\_asm\_\_ volatile ("ecall"

53 : "+r" (a0)

54 : "r" (a1), "r" (a2), "r" (a3), "r" (a4), "r" (a5),

55 "r" (t0)

56 : "memory");

57 return a0;

58}

59

[ 60](arch_2riscv_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke5](arch_2arc_2syscall_8h.md#a9971c78bc8f579a0dadf84225dc0c3ff)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

61 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

62 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5,

63 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

64{

65 register unsigned long a0 \_\_asm\_\_ ("a0") = arg1;

66 register unsigned long a1 \_\_asm\_\_ ("a1") = arg2;

67 register unsigned long a2 \_\_asm\_\_ ("a2") = arg3;

68 register unsigned long a3 \_\_asm\_\_ ("a3") = arg4;

69 register unsigned long a4 \_\_asm\_\_ ("a4") = arg5;

70 register unsigned long t0 \_\_asm\_\_ ("t0") = call\_id;

71

72 \_\_asm\_\_ volatile ("ecall"

73 : "+r" (a0)

74 : "r" (a1), "r" (a2), "r" (a3), "r" (a4), "r" (t0)

75 : "memory");

76 return a0;

77}

78

[ 79](arch_2riscv_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke4](arch_2arc_2syscall_8h.md#a0ba3ae2290827385b226ebdbf3de3b53)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

80 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

81 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

82{

83 register unsigned long a0 \_\_asm\_\_ ("a0") = arg1;

84 register unsigned long a1 \_\_asm\_\_ ("a1") = arg2;

85 register unsigned long a2 \_\_asm\_\_ ("a2") = arg3;

86 register unsigned long a3 \_\_asm\_\_ ("a3") = arg4;

87 register unsigned long t0 \_\_asm\_\_ ("t0") = call\_id;

88

89 \_\_asm\_\_ volatile ("ecall"

90 : "+r" (a0)

91 : "r" (a1), "r" (a2), "r" (a3), "r" (t0)

92 : "memory");

93 return a0;

94}

95

[ 96](arch_2riscv_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke3](arch_2arc_2syscall_8h.md#aacb1c66a1b7bf2293fea269f6b5e1c7e)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

97 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3,

98 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

99{

100 register unsigned long a0 \_\_asm\_\_ ("a0") = arg1;

101 register unsigned long a1 \_\_asm\_\_ ("a1") = arg2;

102 register unsigned long a2 \_\_asm\_\_ ("a2") = arg3;

103 register unsigned long t0 \_\_asm\_\_ ("t0") = call\_id;

104

105 \_\_asm\_\_ volatile ("ecall"

106 : "+r" (a0)

107 : "r" (a1), "r" (a2), "r" (t0)

108 : "memory");

109 return a0;

110}

111

[ 112](arch_2riscv_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke2](arch_2arc_2syscall_8h.md#a1e78f1022aaf10e88727b142b56d4ef0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

113 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

114{

115 register unsigned long a0 \_\_asm\_\_ ("a0") = arg1;

116 register unsigned long a1 \_\_asm\_\_ ("a1") = arg2;

117 register unsigned long t0 \_\_asm\_\_ ("t0") = call\_id;

118

119 \_\_asm\_\_ volatile ("ecall"

120 : "+r" (a0)

121 : "r" (a1), "r" (t0)

122 : "memory");

123 return a0;

124}

125

[ 126](arch_2riscv_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke1](arch_2arc_2syscall_8h.md#a4cfb3b2b38e5afca889e8b9765d6c3df)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

127{

128 register unsigned long a0 \_\_asm\_\_ ("a0") = arg1;

129 register unsigned long t0 \_\_asm\_\_ ("t0") = call\_id;

130

131 \_\_asm\_\_ volatile ("ecall"

132 : "+r" (a0)

133 : "r" (t0)

134 : "memory");

135 return a0;

136}

137

[ 138](arch_2riscv_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [arch\_syscall\_invoke0](arch_2arc_2syscall_8h.md#a5e9ab24b9c980e327903fbe3f5bd97f3)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id)

139{

140 register unsigned long a0 \_\_asm\_\_ ("a0");

141 register unsigned long t0 \_\_asm\_\_ ("t0") = call\_id;

142

143 \_\_asm\_\_ volatile ("ecall"

144 : "=r" (a0)

145 : "r" (t0)

146 : "memory");

147 return a0;

148}

149

150#ifdef CONFIG\_USERSPACE

151register unsigned long riscv\_tp\_reg \_\_asm\_\_ ("tp");

152

[ 153](arch_2riscv_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)static inline bool [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)(void)

154{

155 /\* don't try accessing TLS variables if tp is not initialized \*/

156 if (riscv\_tp\_reg == 0) {

157 return false;

158 }

159

160 /\* Defined in arch/riscv/core/thread.c \*/

161 extern Z\_THREAD\_LOCAL [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) is\_user\_mode;

162

163 return is\_user\_mode != 0;

164}

165#endif

166

167#ifdef \_\_cplusplus

168}

169#endif

170

171#endif /\* \_ASMLANGUAGE \*/

172#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RISCV\_SYSCALL\_H\_ \*/

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

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [syscall.h](arch_2riscv_2syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
