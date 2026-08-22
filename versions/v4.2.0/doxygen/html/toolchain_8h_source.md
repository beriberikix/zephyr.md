---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/toolchain_8h_source.html
original_path: doxygen/html/toolchain_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

50#include <[zephyr/toolchain/llvm.h](include_2zephyr_2toolchain_2llvm_8h.md)>

51#elif defined(\_\_GNUC\_\_) || (defined(\_LINKER) && defined(\_\_GCC\_LINKER\_CMD\_\_))

52#include <[zephyr/toolchain/gcc.h](include_2zephyr_2toolchain_2gcc_8h.md)>

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

132#ifdef TOOLCHAIN\_HAS\_PRAGMA\_DIAG

[ 133](toolchain_8h.md#a4bd2473c4ecff861c6bc3e187b0fee12)#define TOOLCHAIN\_PRAGMA(x) \_Pragma(#x)

134#else

135#define TOOLCHAIN\_PRAGMA(x)

136#endif

137

145#ifndef TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER

[ 146](toolchain_8h.md#aef9c3722dc2b189226eb2e6223c080bf)#define TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER

147#endif

148

156#ifndef TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS

[ 157](toolchain_8h.md#a8b81dbfdc3dde900a58540709a4f1dff)#define TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS

158#endif

159

167#ifndef TOOLCHAIN\_WARNING\_ATTRIBUTES

[ 168](toolchain_8h.md#a5f5fef9bda4762c368f26c9028cdd34a)#define TOOLCHAIN\_WARNING\_ATTRIBUTES

169#endif

170

179#ifndef TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR

[ 180](toolchain_8h.md#a003b55bfd0a8b95a4e57e419eb980a39)#define TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR

181#endif

182

190#ifndef TOOLCHAIN\_WARNING\_EXTRA

[ 191](toolchain_8h.md#a64d8f26c21ee3639e82d93783e09387e)#define TOOLCHAIN\_WARNING\_EXTRA

192#endif

193

201#ifndef TOOLCHAIN\_WARNING\_NONNULL

[ 202](toolchain_8h.md#af990df9b277505b97d4c9c2549fffa9f)#define TOOLCHAIN\_WARNING\_NONNULL

203#endif

204

212#ifndef TOOLCHAIN\_WARNING\_POINTER\_ARITH

[ 213](toolchain_8h.md#a9c83552055a1817801dedc6655fc0cbf)#define TOOLCHAIN\_WARNING\_POINTER\_ARITH

214#endif

215

223#ifndef TOOLCHAIN\_WARNING\_SHADOW

[ 224](toolchain_8h.md#ae917ae1adad468956fa5d28a50d10670)#define TOOLCHAIN\_WARNING\_SHADOW

225#endif

226

234#ifndef TOOLCHAIN\_WARNING\_UNUSED\_LABEL

[ 235](toolchain_8h.md#a49dfbc1f801e1f3ae9a0dfaee4b1b5c9)#define TOOLCHAIN\_WARNING\_UNUSED\_LABEL

236#endif

237

245#ifndef TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE

[ 246](toolchain_8h.md#ac567335f987f8f89640e22bd8e3e9385)#define TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE

247#endif

248

253#ifndef TOOLCHAIN\_DISABLE\_WARNING

[ 254](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5)#define TOOLCHAIN\_DISABLE\_WARNING(warning)

255#endif

256

263#ifndef TOOLCHAIN\_ENABLE\_WARNING

[ 264](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561)#define TOOLCHAIN\_ENABLE\_WARNING(warning)

265#endif

266

271#ifndef TOOLCHAIN\_DISABLE\_CLANG\_WARNING

[ 272](toolchain_8h.md#ac4bfe24556e3dd2bfb093434a4e98517)#define TOOLCHAIN\_DISABLE\_CLANG\_WARNING(warning)

273#endif

274

281#ifndef TOOLCHAIN\_ENABLE\_CLANG\_WARNING

[ 282](toolchain_8h.md#a35eaaf7a69eae890687c196e81304667)#define TOOLCHAIN\_ENABLE\_CLANG\_WARNING(warning)

283#endif

284

289#ifndef TOOLCHAIN\_DISABLE\_GCC\_WARNING

[ 290](toolchain_8h.md#a245aa1544cf704ac88da3904e0982f05)#define TOOLCHAIN\_DISABLE\_GCC\_WARNING(warning)

291#endif

292

299#ifndef TOOLCHAIN\_ENABLE\_GCC\_WARNING

[ 300](toolchain_8h.md#a57a000da2786521299f7bc9460977c60)#define TOOLCHAIN\_ENABLE\_GCC\_WARNING(warning)

301#endif

302

307#ifndef TOOLCHAIN\_DISABLE\_IAR\_WARNING

[ 308](toolchain_8h.md#aace39dc11f4da885c3a75210519cff13)#define TOOLCHAIN\_DISABLE\_IAR\_WARNING(warning)

309#endif

310

317#ifndef TOOLCHAIN\_ENABLE\_IAR\_WARNING

[ 318](toolchain_8h.md#a8a1fc59f2665be53c4e183d295d91e15)#define TOOLCHAIN\_ENABLE\_IAR\_WARNING(warning)

319#endif

320

321/\*

322 \* Ensure that \_\_BYTE\_ORDER\_\_ and related preprocessor definitions are defined,

323 \* and that they match the Kconfig option that is used in the code itself to

324 \* check for endianness.

325 \*/

326#ifndef \_LINKER

327#if !defined(\_\_BYTE\_ORDER\_\_) || !defined(\_\_ORDER\_BIG\_ENDIAN\_\_) || \

328 !defined(\_\_ORDER\_LITTLE\_ENDIAN\_\_)

329

330/\*

331 \* Displaying values unfortunately requires #pragma message which can't

332 \* be taken for granted + STRINGIFY() which is not available in this .h

333 \* file.

334 \*/

335#error "At least one byte \_ORDER\_ macro is not defined"

336

337#else

338

339#if (defined(CONFIG\_BIG\_ENDIAN) && (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_BIG\_ENDIAN\_\_)) || \

340 (defined(CONFIG\_LITTLE\_ENDIAN) && (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_LITTLE\_ENDIAN\_\_))

341

342# error "Kconfig/toolchain endianness mismatch:"

343

344# if (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_BIG\_ENDIAN\_\_) && (\_\_BYTE\_ORDER\_\_ != \_\_ORDER\_LITTLE\_ENDIAN\_\_)

345# error "Unknown \_\_BYTE\_ORDER\_\_ value"

346# else

347# ifdef CONFIG\_BIG\_ENDIAN

348# error "CONFIG\_BIG\_ENDIAN but \_\_ORDER\_LITTLE\_ENDIAN\_\_"

349# endif

350# ifdef CONFIG\_LITTLE\_ENDIAN

351# error "CONFIG\_LITTLE\_ENDIAN but \_\_ORDER\_BIG\_ENDIAN\_\_"

352# endif

353# endif

354

355#endif /\* Endianness mismatch \*/

356

357#endif /\* all \_ORDER\_ macros defined \*/

358

359#endif /\* !\_LINKER \*/

360

361#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_ \*/

[armclang.h](armclang_8h.md)

[iar.h](iar_8h.md)

[gcc.h](include_2zephyr_2toolchain_2gcc_8h.md)

GCC toolchain abstraction.

[llvm.h](include_2zephyr_2toolchain_2llvm_8h.md)

[mwdt.h](mwdt_8h.md)

[xcc.h](xcc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain.h](toolchain_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
