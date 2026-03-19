---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/toolchain_8h_source.html
original_path: doxygen/html/toolchain_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

47#elif defined(\_\_IAR\_SYSTEMS\_ICC\_\_)

48#include <[zephyr/toolchain/iar.h](iar_8h.md)>

49#elif defined(\_\_llvm\_\_) || (defined(\_LINKER) && defined(\_\_LLD\_LINKER\_CMD\_\_))

50#include <[zephyr/toolchain/llvm.h](llvm_8h.md)>

51#elif defined(\_\_GNUC\_\_) || (defined(\_LINKER) && defined(\_\_GCC\_LINKER\_CMD\_\_))

52#include <[zephyr/toolchain/gcc.h](gcc_8h.md)>

53#else

54#error "Invalid/unknown toolchain configuration"

55#endif

56

68#ifndef \_\_noasan

69#define \_\_noasan /\*\*/

70#endif

71

76#ifndef TOOLCHAIN\_GCC\_VERSION

[ 77](toolchain_8h.md#acbf8a21b471b2086cbe276789c5061d5)#define TOOLCHAIN\_GCC\_VERSION 0

78#endif

79

84#ifndef TOOLCHAIN\_CLANG\_VERSION

[ 85](toolchain_8h.md#acdbda8f5e81a320dfdbc32bda1b33fad)#define TOOLCHAIN\_CLANG\_VERSION 0

86#endif

87

92#ifndef TOOLCHAIN\_HAS\_PRAGMA\_DIAG

[ 93](toolchain_8h.md#a763b60a74b3b8917b8a91614f1d443e4)#define TOOLCHAIN\_HAS\_PRAGMA\_DIAG 0

94#endif

95

100#if defined(\_\_STDC\_VERSION\_\_) && \_\_STDC\_VERSION\_\_ >= 201112L

101/\* \_Generic is introduced in C11, so it is supported. \*/

102# ifdef TOOLCHAIN\_HAS\_C\_GENERIC

103# undef TOOLCHAIN\_HAS\_C\_GENERIC

104# endif

105# define TOOLCHAIN\_HAS\_C\_GENERIC 1

106#else

107# ifndef TOOLCHAIN\_HAS\_C\_GENERIC

[ 108](toolchain_8h.md#a49263980cf39cd330a9e9976dccb4c90)# define TOOLCHAIN\_HAS\_C\_GENERIC 0

109# endif

110#endif

111

116#ifndef TOOLCHAIN\_HAS\_C\_AUTO\_TYPE

[ 117](toolchain_8h.md#a9502cad506e0dfb7c3a7b51b5eeb5eeb)#define TOOLCHAIN\_HAS\_C\_AUTO\_TYPE 0

118#endif

119

124#ifndef TOOLCHAIN\_HAS\_ZLA

[ 125](toolchain_8h.md#a90e5fd6ed234d1494c7f156635c2e6e1)#define TOOLCHAIN\_HAS\_ZLA 0

126#endif

127

135#ifndef TOOLCHAIN\_IGNORE\_WSHADOW\_BEGIN

[ 136](toolchain_8h.md#a7bcec2251379c10461a105633d66de46)#define TOOLCHAIN\_IGNORE\_WSHADOW\_BEGIN

137#endif

138

146#ifndef TOOLCHAIN\_IGNORE\_WSHADOW\_END

[ 147](toolchain_8h.md#a7226e5ae170e8d7e9d8bec8d625e3542)#define TOOLCHAIN\_IGNORE\_WSHADOW\_END

148#endif

149

154#ifdef TOOLCHAIN\_HAS\_PRAGMA\_DIAG

[ 155](toolchain_8h.md#a4bd2473c4ecff861c6bc3e187b0fee12)#define TOOLCHAIN\_PRAGMA(x) \_Pragma(#x)

156#else

157#define TOOLCHAIN\_PRAGMA(x)

158#endif

159

164#ifndef TOOLCHAIN\_DISABLE\_WARNING

[ 165](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5)#define TOOLCHAIN\_DISABLE\_WARNING(warning)

166#endif

167

174#ifndef TOOLCHAIN\_ENABLE\_WARNING

[ 175](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561)#define TOOLCHAIN\_ENABLE\_WARNING(warning)

176#endif

177

182#ifndef TOOLCHAIN\_DISABLE\_CLANG\_WARNING

[ 183](toolchain_8h.md#ac4bfe24556e3dd2bfb093434a4e98517)#define TOOLCHAIN\_DISABLE\_CLANG\_WARNING(warning)

184#endif

185

192#ifndef TOOLCHAIN\_ENABLE\_CLANG\_WARNING

[ 193](toolchain_8h.md#a35eaaf7a69eae890687c196e81304667)#define TOOLCHAIN\_ENABLE\_CLANG\_WARNING(warning)

194#endif

195

200#ifndef TOOLCHAIN\_DISABLE\_GCC\_WARNING

[ 201](toolchain_8h.md#a245aa1544cf704ac88da3904e0982f05)#define TOOLCHAIN\_DISABLE\_GCC\_WARNING(warning)

202#endif

203

210#ifndef TOOLCHAIN\_ENABLE\_GCC\_WARNING

[ 211](toolchain_8h.md#a57a000da2786521299f7bc9460977c60)#define TOOLCHAIN\_ENABLE\_GCC\_WARNING(warning)

212#endif

213

214/\*

215 \* Ensure that \_\_BYTE\_ORDER\_\_ and related preprocessor definitions are defined,

216 \* and that they match the Kconfig option that is used in the code itself to

217 \* check for endianness.

218 \*/

219#ifndef \_LINKER

220#if !defined(\_\_BYTE\_ORDER\_\_) || !defined(\_\_ORDER\_BIG\_ENDIAN\_\_) || \

221 !defined(\_\_ORDER\_LITTLE\_ENDIAN\_\_)

222

223/\*

224 \* Displaying values unfortunately requires #pragma message which can't

225 \* be taken for granted + STRINGIFY() which is not available in this .h

226 \* file.

227 \*/

228#error "At least one byte \_ORDER\_ macro is not defined"

229

230#else

231

232#if (defined(CONFIG\_BIG\_ENDIAN) && (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_BIG\_ENDIAN\_\_)) || \

233 (defined(CONFIG\_LITTLE\_ENDIAN) && (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_LITTLE\_ENDIAN\_\_))

234

235# error "Kconfig/toolchain endianness mismatch:"

236

237# if (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_BIG\_ENDIAN\_\_) && (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_LITTLE\_ENDIAN\_\_)

238# error "Unknown \_\_BYTE\_ORDER\_\_ value"

239# else

240# ifdef CONFIG\_BIG\_ENDIAN

241# error "CONFIG\_BIG\_ENDIAN but \_\_ORDER\_LITTLE\_ENDIAN\_\_"

242# endif

243# ifdef CONFIG\_LITTLE\_ENDIAN

244# error "CONFIG\_LITTLE\_ENDIAN but \_\_ORDER\_BIG\_ENDIAN\_\_"

245# endif

246# endif

247

248#endif /\* Endianness mismatch \*/

249

250#endif /\* all \_ORDER\_ macros defined \*/

251

252#endif /\* !\_LINKER \*/

253

254#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_ \*/

[armclang.h](armclang_8h.md)

[gcc.h](gcc_8h.md)

GCC toolchain abstraction.

[iar.h](iar_8h.md)

[llvm.h](llvm_8h.md)

[mwdt.h](mwdt_8h.md)

[xcc.h](xcc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain.h](toolchain_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
