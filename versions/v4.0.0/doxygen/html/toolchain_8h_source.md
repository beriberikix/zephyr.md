---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/toolchain_8h_source.html
original_path: doxygen/html/toolchain_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

toolchain.h

[Go to the documentation of this file.](toolchain_8h.md)

1/\*

2 \* Copyright (c) 2010-2014, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_

16#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_

17

25#ifdef \_\_has\_builtin

26#define HAS\_BUILTIN(x) \_\_has\_builtin(x)

27#else

28/\*

29 \* The compiler doesn't provide the \_\_has\_builtin() macro, so instead we depend

30 \* on the toolchain-specific headers to define HAS\_BUILTIN\_x for the builtins

31 \* supported.

32 \*/

[ 33](toolchain_8h.md#a474a719388efd0578c7c98a0961e23dd)#define HAS\_BUILTIN(x) HAS\_BUILTIN\_##x

34#endif

35

36#if defined(\_\_TOOLCHAIN\_CUSTOM\_\_)

37/\* This include line exists for off-tree definitions of compilers,

38 \* and therefore this header is not meant to exist in-tree

39 \*/

40#include <toolchain/other.h>

41#elif defined(\_\_XCC\_\_)

42#include <[zephyr/toolchain/xcc.h](xcc_8h.md)>

43#elif defined(\_\_CCAC\_\_)

44#include <[zephyr/toolchain/mwdt.h](mwdt_8h.md)>

45#elif defined(\_\_ARMCOMPILER\_VERSION)

46#include <[zephyr/toolchain/armclang.h](armclang_8h.md)>

47#elif defined(\_\_llvm\_\_) || (defined(\_LINKER) && defined(\_\_LLD\_LINKER\_CMD\_\_))

48#include <[zephyr/toolchain/llvm.h](llvm_8h.md)>

49#elif defined(\_\_GNUC\_\_) || (defined(\_LINKER) && defined(\_\_GCC\_LINKER\_CMD\_\_))

50#include <[zephyr/toolchain/gcc.h](gcc_8h.md)>

51#else

52#error "Invalid/unknown toolchain configuration"

53#endif

54

66#ifndef \_\_noasan

67#define \_\_noasan /\*\*/

68#endif

69

74#ifndef TOOLCHAIN\_GCC\_VERSION

[ 75](toolchain_8h.md#acbf8a21b471b2086cbe276789c5061d5)#define TOOLCHAIN\_GCC\_VERSION 0

76#endif

77

82#ifndef TOOLCHAIN\_CLANG\_VERSION

[ 83](toolchain_8h.md#acdbda8f5e81a320dfdbc32bda1b33fad)#define TOOLCHAIN\_CLANG\_VERSION 0

84#endif

85

90#ifndef TOOLCHAIN\_HAS\_PRAGMA\_DIAG

[ 91](toolchain_8h.md#a763b60a74b3b8917b8a91614f1d443e4)#define TOOLCHAIN\_HAS\_PRAGMA\_DIAG 0

92#endif

93

98#if defined(\_\_STDC\_VERSION\_\_) && \_\_STDC\_VERSION\_\_ >= 201112L

99/\* \_Generic is introduced in C11, so it is supported. \*/

100# ifdef TOOLCHAIN\_HAS\_C\_GENERIC

101# undef TOOLCHAIN\_HAS\_C\_GENERIC

102# endif

103# define TOOLCHAIN\_HAS\_C\_GENERIC 1

104#else

105# ifndef TOOLCHAIN\_HAS\_C\_GENERIC

[ 106](toolchain_8h.md#a49263980cf39cd330a9e9976dccb4c90)# define TOOLCHAIN\_HAS\_C\_GENERIC 0

107# endif

108#endif

109

114#ifndef TOOLCHAIN\_HAS\_C\_AUTO\_TYPE

[ 115](toolchain_8h.md#a9502cad506e0dfb7c3a7b51b5eeb5eeb)#define TOOLCHAIN\_HAS\_C\_AUTO\_TYPE 0

116#endif

117

122#ifndef TOOLCHAIN\_HAS\_ZLA

[ 123](toolchain_8h.md#a90e5fd6ed234d1494c7f156635c2e6e1)#define TOOLCHAIN\_HAS\_ZLA 0

124#endif

125

133#ifndef TOOLCHAIN\_IGNORE\_WSHADOW\_BEGIN

[ 134](toolchain_8h.md#a7bcec2251379c10461a105633d66de46)#define TOOLCHAIN\_IGNORE\_WSHADOW\_BEGIN

135#endif

136

144#ifndef TOOLCHAIN\_IGNORE\_WSHADOW\_END

[ 145](toolchain_8h.md#a7226e5ae170e8d7e9d8bec8d625e3542)#define TOOLCHAIN\_IGNORE\_WSHADOW\_END

146#endif

147

148/\*

149 \* Ensure that \_\_BYTE\_ORDER\_\_ and related preprocessor definitions are defined,

150 \* and that they match the Kconfig option that is used in the code itself to

151 \* check for endianness.

152 \*/

153#ifndef \_LINKER

154#if !defined(\_\_BYTE\_ORDER\_\_) || !defined(\_\_ORDER\_BIG\_ENDIAN\_\_) || \

155 !defined(\_\_ORDER\_LITTLE\_ENDIAN\_\_)

156

157/\*

158 \* Displaying values unfortunately requires #pragma message which can't

159 \* be taken for granted + STRINGIFY() which is not available in this .h

160 \* file.

161 \*/

162#error "At least one byte \_ORDER\_ macro is not defined"

163

164#else

165

166#if (defined(CONFIG\_BIG\_ENDIAN) && (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_BIG\_ENDIAN\_\_)) || \

167 (defined(CONFIG\_LITTLE\_ENDIAN) && (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_LITTLE\_ENDIAN\_\_))

168

169# error "Kconfig/toolchain endianness mismatch:"

170

171# if (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_BIG\_ENDIAN\_\_) && (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_LITTLE\_ENDIAN\_\_)

172# error "Unknown \_\_BYTE\_ORDER\_\_ value"

173# else

174# ifdef CONFIG\_BIG\_ENDIAN

175# error "CONFIG\_BIG\_ENDIAN but \_\_ORDER\_LITTLE\_ENDIAN\_\_"

176# endif

177# ifdef CONFIG\_LITTLE\_ENDIAN

178# error "CONFIG\_LITTLE\_ENDIAN but \_\_ORDER\_BIG\_ENDIAN\_\_"

179# endif

180# endif

181

182#endif /\* Endianness mismatch \*/

183

184#endif /\* all \_ORDER\_ macros defined \*/

185

186#endif /\* !\_LINKER \*/

187

188#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_ \*/

[armclang.h](armclang_8h.md)

[gcc.h](gcc_8h.md)

GCC toolchain abstraction.

[llvm.h](llvm_8h.md)

[mwdt.h](mwdt_8h.md)

[xcc.h](xcc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain.h](toolchain_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
