---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm_2arch_8h_source.html
original_path: doxygen/html/arm_2arch_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](arm_2arch_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_ARCH\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_ARCH\_H\_

18

19/\* Add include for DTS generated information \*/

20#include <[zephyr/devicetree.h](devicetree_8h.md)>

21

22/\* ARM GPRs are often designated by two different names \*/

[ 23](arm_2arch_8h.md#a59d42697fc33d0b600597145a7b76dc7)#define sys\_define\_gpr\_with\_alias(name1, name2) union { uint32\_t name1, name2; }

24

25#include <[zephyr/arch/arm/thread.h](arch_2arm_2thread_8h.md)>

26#include <[zephyr/arch/arm/exception.h](arm_2exception_8h.md)>

27#include <[zephyr/arch/arm/irq.h](arch_2arm_2irq_8h.md)>

28#include <[zephyr/arch/arm/error.h](arm_2error_8h.md)>

29#include <[zephyr/arch/arm/misc.h](arm_2misc_8h.md)>

30#include <[zephyr/arch/common/addr\_types.h](addr__types_8h.md)>

31#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

32#include <[zephyr/arch/arm/nmi.h](nmi_8h.md)>

33#include <[zephyr/arch/arm/asm\_inline.h](arm_2asm__inline_8h.md)>

34#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

35#if defined(CONFIG\_GDBSTUB)

36#include <[zephyr/arch/arm/gdbstub.h](arch_2arm_2gdbstub_8h.md)>

37#endif

38

39#ifdef CONFIG\_CPU\_CORTEX\_M

40#include <[zephyr/arch/arm/cortex\_m/cpu.h](arm_2cortex__m_2cpu_8h.md)>

41#include <[zephyr/arch/arm/cortex\_m/memory\_map.h](memory__map_8h.md)>

42#include <[zephyr/arch/common/sys\_io.h](arch_2common_2sys__io_8h.md)>

43#elif defined(CONFIG\_CPU\_AARCH32\_CORTEX\_R) || defined(CONFIG\_CPU\_AARCH32\_CORTEX\_A)

44#include <[zephyr/arch/arm/cortex\_a\_r/cpu.h](arm_2cortex__a__r_2cpu_8h.md)>

45#include <[zephyr/arch/arm/cortex\_a\_r/sys\_io.h](arch_2arm_2cortex__a__r_2sys__io_8h.md)>

46#if defined(CONFIG\_AARCH32\_ARMV8\_R)

47#include <[zephyr/arch/arm/cortex\_a\_r/lib\_helpers.h](cortex__a__r_2lib__helpers_8h.md)>

48#include <[zephyr/arch/arm/cortex\_a\_r/armv8\_timer.h](armv8__timer_8h.md)>

49#else

50#include <[zephyr/arch/arm/cortex\_a\_r/timer.h](cortex__a__r_2timer_8h.md)>

51#endif

52#endif

53

54#ifdef \_\_cplusplus

55extern "C" {

56#endif

57

58#ifndef \_ASMLANGUAGE

59

60#include <[zephyr/fatal\_types.h](fatal__types_8h.md)>

61

[ 62](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4)enum [k\_fatal\_error\_reason\_arch](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4) {

63 /\* Cortex-M MEMFAULT exceptions \*/

[ 64](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a7ac465c1decca4d761d420f62700c940) [K\_ERR\_ARM\_MEM\_GENERIC](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a7ac465c1decca4d761d420f62700c940) = [K\_ERR\_ARCH\_START](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a45d4bf1a392f99d6b4d15f50a0e333d1),

[ 65](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a3de9e6e036d9022537164b68c2fc8fb9) [K\_ERR\_ARM\_MEM\_STACKING](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a3de9e6e036d9022537164b68c2fc8fb9),

[ 66](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a043da3af81148080b75ecf5002d3c6ea) [K\_ERR\_ARM\_MEM\_UNSTACKING](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a043da3af81148080b75ecf5002d3c6ea),

[ 67](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4af52bcf1db9ed0dfc47f4d1b9698c23a6) [K\_ERR\_ARM\_MEM\_DATA\_ACCESS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4af52bcf1db9ed0dfc47f4d1b9698c23a6),

[ 68](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a776523f4671f98f87ccf9a76db9a186c) [K\_ERR\_ARM\_MEM\_INSTRUCTION\_ACCESS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a776523f4671f98f87ccf9a76db9a186c),

[ 69](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5ad278e3284e621ace082e5d1d89c599) [K\_ERR\_ARM\_MEM\_FP\_LAZY\_STATE\_PRESERVATION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5ad278e3284e621ace082e5d1d89c599),

70

71 /\* Cortex-M BUSFAULT exceptions \*/

[ 72](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a899fe8e2d408404917b3bd166f07666c) [K\_ERR\_ARM\_BUS\_GENERIC](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a899fe8e2d408404917b3bd166f07666c),

[ 73](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a7b5e93c7163bea86dbeff21759f6472e) [K\_ERR\_ARM\_BUS\_STACKING](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a7b5e93c7163bea86dbeff21759f6472e),

[ 74](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a7a879301aa3ee1b2ce6abcacdc795b1d) [K\_ERR\_ARM\_BUS\_UNSTACKING](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a7a879301aa3ee1b2ce6abcacdc795b1d),

[ 75](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4aed122da9226657dea13a9afa9dbc43d5) [K\_ERR\_ARM\_BUS\_PRECISE\_DATA\_BUS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4aed122da9226657dea13a9afa9dbc43d5),

[ 76](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a8cbae40f6ee1f7b65f02b330d5f7a8ae) [K\_ERR\_ARM\_BUS\_IMPRECISE\_DATA\_BUS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a8cbae40f6ee1f7b65f02b330d5f7a8ae),

[ 77](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a916d2fb2799c0355aace800ed43ad69c) [K\_ERR\_ARM\_BUS\_INSTRUCTION\_BUS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a916d2fb2799c0355aace800ed43ad69c),

[ 78](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a03607bd98c8aebb5c4bd794278987317) [K\_ERR\_ARM\_BUS\_FP\_LAZY\_STATE\_PRESERVATION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a03607bd98c8aebb5c4bd794278987317),

79

80 /\* Cortex-M USAGEFAULT exceptions \*/

[ 81](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4afbe97c341bf54d94c42c4ec456d586ca) [K\_ERR\_ARM\_USAGE\_GENERIC](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4afbe97c341bf54d94c42c4ec456d586ca),

[ 82](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a802af0dbe318680dfcd1805cb8b99fd8) [K\_ERR\_ARM\_USAGE\_DIV\_0](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a802af0dbe318680dfcd1805cb8b99fd8),

[ 83](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5e41e262d0fb52266261a8e3a59e75ff) [K\_ERR\_ARM\_USAGE\_UNALIGNED\_ACCESS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5e41e262d0fb52266261a8e3a59e75ff),

[ 84](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4ada75e6e3d5102139cbcd7df2f67f8bc3) [K\_ERR\_ARM\_USAGE\_STACK\_OVERFLOW](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4ada75e6e3d5102139cbcd7df2f67f8bc3),

[ 85](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a4a10fc8ae3093fd24cb052457fa1783a) [K\_ERR\_ARM\_USAGE\_NO\_COPROCESSOR](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a4a10fc8ae3093fd24cb052457fa1783a),

[ 86](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a4646893d8e3fc6c19356c9c0e56e1766) [K\_ERR\_ARM\_USAGE\_ILLEGAL\_EXC\_RETURN](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a4646893d8e3fc6c19356c9c0e56e1766),

[ 87](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a750a9631b59488b406f228eb74656e82) [K\_ERR\_ARM\_USAGE\_ILLEGAL\_EPSR](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a750a9631b59488b406f228eb74656e82),

[ 88](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4aabd67bae03c199605f62c83b57b54159) [K\_ERR\_ARM\_USAGE\_UNDEFINED\_INSTRUCTION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4aabd67bae03c199605f62c83b57b54159),

89

90 /\* Cortex-M SECURE exceptions \*/

[ 91](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a3b437867ae7ec378d8a04f1da9891165) [K\_ERR\_ARM\_SECURE\_GENERIC](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a3b437867ae7ec378d8a04f1da9891165),

[ 92](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a454c50a4bf529eaf4a2e2fda636bbc3d) [K\_ERR\_ARM\_SECURE\_ENTRY\_POINT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a454c50a4bf529eaf4a2e2fda636bbc3d),

[ 93](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a50e6eccecb232ce9c9bf987be6263288) [K\_ERR\_ARM\_SECURE\_INTEGRITY\_SIGNATURE](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a50e6eccecb232ce9c9bf987be6263288),

[ 94](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a78c476ea635a8c9459f1b644101f9350) [K\_ERR\_ARM\_SECURE\_EXCEPTION\_RETURN](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a78c476ea635a8c9459f1b644101f9350),

[ 95](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4abbe3ce01c99bd423507dca6b27c4077b) [K\_ERR\_ARM\_SECURE\_ATTRIBUTION\_UNIT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4abbe3ce01c99bd423507dca6b27c4077b),

[ 96](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4accffbb9380478d8e1612d2481246390b) [K\_ERR\_ARM\_SECURE\_TRANSITION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4accffbb9380478d8e1612d2481246390b),

[ 97](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a37e19e97425d822a062fa0502c774d8b) [K\_ERR\_ARM\_SECURE\_LAZY\_STATE\_PRESERVATION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a37e19e97425d822a062fa0502c774d8b),

[ 98](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4acf891bac81ed5e29b423507ac0a35139) [K\_ERR\_ARM\_SECURE\_LAZY\_STATE\_ERROR](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4acf891bac81ed5e29b423507ac0a35139),

99

100 /\* Cortex-A/R exceptions\*/

[ 101](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a96392456666f9adb04ee89d78f208f6a) [K\_ERR\_ARM\_UNDEFINED\_INSTRUCTION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a96392456666f9adb04ee89d78f208f6a),

[ 102](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5be6201ceaa069b4497e5dad46e9f8c1) [K\_ERR\_ARM\_ALIGNMENT\_FAULT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5be6201ceaa069b4497e5dad46e9f8c1),

[ 103](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a08211aaa1c86b287354b336a8f6ef40f) [K\_ERR\_ARM\_BACKGROUND\_FAULT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a08211aaa1c86b287354b336a8f6ef40f),

[ 104](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4afbc0c25bea6fe87969248a41f58e6822) [K\_ERR\_ARM\_PERMISSION\_FAULT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4afbc0c25bea6fe87969248a41f58e6822),

[ 105](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a36cf0f17b0c5c880acc9ba3da2b42665) [K\_ERR\_ARM\_SYNC\_EXTERNAL\_ABORT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a36cf0f17b0c5c880acc9ba3da2b42665),

[ 106](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a54d95700befedeb1da3378d5abd8d833) [K\_ERR\_ARM\_ASYNC\_EXTERNAL\_ABORT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a54d95700befedeb1da3378d5abd8d833),

[ 107](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a4307218c98165be33c86e07c47fc0579) [K\_ERR\_ARM\_SYNC\_PARITY\_ERROR](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a4307218c98165be33c86e07c47fc0579),

[ 108](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4ab655e2d4d1cf6a441362e80e969287f8) [K\_ERR\_ARM\_ASYNC\_PARITY\_ERROR](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4ab655e2d4d1cf6a441362e80e969287f8),

[ 109](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4abb352aab2d7667ed3c72eabe024d4c5c) [K\_ERR\_ARM\_DEBUG\_EVENT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4abb352aab2d7667ed3c72eabe024d4c5c),

[ 110](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5c820b75e2d2941f160b1f47a6da6d76) [K\_ERR\_ARM\_TRANSLATION\_FAULT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5c820b75e2d2941f160b1f47a6da6d76),

[ 111](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a270c41c058d9fb3567a77419dae9cf3a) [K\_ERR\_ARM\_UNSUPPORTED\_EXCLUSIVE\_ACCESS\_FAULT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a270c41c058d9fb3567a77419dae9cf3a)

112};

113

114#endif /\* \_ASMLANGUAGE \*/

115

123#ifdef CONFIG\_STACK\_ALIGN\_DOUBLE\_WORD

124#define ARCH\_STACK\_PTR\_ALIGN 8

125#else

[ 126](arm_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 4

127#endif

128

138#if defined(CONFIG\_USERSPACE)

139#define Z\_THREAD\_MIN\_STACK\_ALIGN CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE

140#elif defined(CONFIG\_ARM\_AARCH32\_MMU)

141#define Z\_THREAD\_MIN\_STACK\_ALIGN CONFIG\_ARM\_MMU\_REGION\_MIN\_ALIGN\_AND\_SIZE

142#else

143#define Z\_THREAD\_MIN\_STACK\_ALIGN ARCH\_STACK\_PTR\_ALIGN

144#endif

145

193#if defined(CONFIG\_MPU\_STACK\_GUARD)

194/\* make sure there's more than enough space for an exception frame \*/

195#if CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE <= 0x20

196#define MPU\_GUARD\_ALIGN\_AND\_SIZE 0x40

197#else

198#define MPU\_GUARD\_ALIGN\_AND\_SIZE CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE

199#endif

200#else

[ 201](arm_2arch_8h.md#a08b1afe29bff127c0f3c0376ee6744b1)#define MPU\_GUARD\_ALIGN\_AND\_SIZE 0

202#endif

203

214#if defined(CONFIG\_FPU) && defined(CONFIG\_FPU\_SHARING) \

215 && defined(CONFIG\_MPU\_STACK\_GUARD)

216#if CONFIG\_MPU\_STACK\_GUARD\_MIN\_SIZE\_FLOAT <= 0x20

217#define MPU\_GUARD\_ALIGN\_AND\_SIZE\_FLOAT 0x40

218#else

219#define MPU\_GUARD\_ALIGN\_AND\_SIZE\_FLOAT CONFIG\_MPU\_STACK\_GUARD\_MIN\_SIZE\_FLOAT

220#endif

221#else

[ 222](arm_2arch_8h.md#a28b1b91e550d6b6fb08cf9aef9e9b0f2)#define MPU\_GUARD\_ALIGN\_AND\_SIZE\_FLOAT 0

223#endif

224

232#if defined(CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT)

233#define Z\_MPU\_GUARD\_ALIGN (MAX(MPU\_GUARD\_ALIGN\_AND\_SIZE, \

234 MPU\_GUARD\_ALIGN\_AND\_SIZE\_FLOAT))

235#else

236#define Z\_MPU\_GUARD\_ALIGN MPU\_GUARD\_ALIGN\_AND\_SIZE

237#endif

238

239#if defined(CONFIG\_USERSPACE) && \

240 defined(CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT)

241/\* This MPU requires regions to be sized to a power of two, and aligned to

242 \* their own size. Since an MPU region must be able to cover the entire

243 \* user-accessible stack buffer, we size/align to match. The privilege

244 \* mode stack is generated elsewhere in memory.

245 \*/

246#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) Z\_POW2\_CEIL(size)

247#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) Z\_POW2\_CEIL(size)

248#else

[ 249](arm_2arch_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7)#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) MAX(Z\_THREAD\_MIN\_STACK\_ALIGN, \

250 Z\_MPU\_GUARD\_ALIGN)

251#ifdef CONFIG\_USERSPACE

[ 252](arm_2arch_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8)#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

253 ROUND\_UP(size, CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE)

254#endif

255#endif

256

257#ifdef CONFIG\_MPU\_STACK\_GUARD

258/\* Kernel-only stacks need an MPU guard region programmed at the beginning of

259 \* the stack object, so align the object appropriately.

260 \*/

261#define ARCH\_KERNEL\_STACK\_RESERVED MPU\_GUARD\_ALIGN\_AND\_SIZE

262#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN Z\_MPU\_GUARD\_ALIGN

263#endif

264

265/\* On arm, all MPU guards are carve-outs. \*/

[ 266](arm_2arch_8h.md#ace8831316d471ccfb06eeddb6d69d817)#define ARCH\_THREAD\_STACK\_RESERVED 0

267

268/\* Legacy case: retain containing extern "C" with C++ \*/

269#ifdef CONFIG\_ARM\_MPU

270#ifdef CONFIG\_CPU\_HAS\_ARM\_MPU

271#include <[zephyr/arch/arm/mpu/arm\_mpu.h](mpu_2arm__mpu_8h.md)>

272#endif /\* CONFIG\_CPU\_HAS\_ARM\_MPU \*/

273#ifdef CONFIG\_CPU\_HAS\_NXP\_MPU

274#include <[zephyr/arch/arm/mpu/nxp\_mpu.h](nxp__mpu_8h.md)>

275#endif /\* CONFIG\_CPU\_HAS\_NXP\_MPU \*/

276#endif /\* CONFIG\_ARM\_MPU \*/

277#ifdef CONFIG\_ARM\_AARCH32\_MMU

278#include <[zephyr/arch/arm/mmu/arm\_mmu.h](mmu_2arm__mmu_8h.md)>

279#endif /\* CONFIG\_ARM\_AARCH32\_MMU \*/

280

281#ifdef \_\_cplusplus

282}

283#endif

284

285#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_ARCH\_H\_ \*/

[addr\_types.h](addr__types_8h.md)

[sys\_io.h](arch_2arm_2cortex__a__r_2sys__io_8h.md)

[gdbstub.h](arch_2arm_2gdbstub_8h.md)

[irq.h](arch_2arm_2irq_8h.md)

ARM AArch32 public interrupt handling.

[thread.h](arch_2arm_2thread_8h.md)

Per-arch thread definition.

[sys\_io.h](arch_2common_2sys__io_8h.md)

[k\_fatal\_error\_reason\_arch](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4)

k\_fatal\_error\_reason\_arch

**Definition** arch.h:62

[K\_ERR\_ARM\_BUS\_FP\_LAZY\_STATE\_PRESERVATION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a03607bd98c8aebb5c4bd794278987317)

@ K\_ERR\_ARM\_BUS\_FP\_LAZY\_STATE\_PRESERVATION

**Definition** arch.h:78

[K\_ERR\_ARM\_MEM\_UNSTACKING](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a043da3af81148080b75ecf5002d3c6ea)

@ K\_ERR\_ARM\_MEM\_UNSTACKING

**Definition** arch.h:66

[K\_ERR\_ARM\_BACKGROUND\_FAULT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a08211aaa1c86b287354b336a8f6ef40f)

@ K\_ERR\_ARM\_BACKGROUND\_FAULT

**Definition** arch.h:103

[K\_ERR\_ARM\_UNSUPPORTED\_EXCLUSIVE\_ACCESS\_FAULT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a270c41c058d9fb3567a77419dae9cf3a)

@ K\_ERR\_ARM\_UNSUPPORTED\_EXCLUSIVE\_ACCESS\_FAULT

**Definition** arch.h:111

[K\_ERR\_ARM\_SYNC\_EXTERNAL\_ABORT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a36cf0f17b0c5c880acc9ba3da2b42665)

@ K\_ERR\_ARM\_SYNC\_EXTERNAL\_ABORT

**Definition** arch.h:105

[K\_ERR\_ARM\_SECURE\_LAZY\_STATE\_PRESERVATION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a37e19e97425d822a062fa0502c774d8b)

@ K\_ERR\_ARM\_SECURE\_LAZY\_STATE\_PRESERVATION

**Definition** arch.h:97

[K\_ERR\_ARM\_SECURE\_GENERIC](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a3b437867ae7ec378d8a04f1da9891165)

@ K\_ERR\_ARM\_SECURE\_GENERIC

**Definition** arch.h:91

[K\_ERR\_ARM\_MEM\_STACKING](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a3de9e6e036d9022537164b68c2fc8fb9)

@ K\_ERR\_ARM\_MEM\_STACKING

**Definition** arch.h:65

[K\_ERR\_ARM\_SYNC\_PARITY\_ERROR](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a4307218c98165be33c86e07c47fc0579)

@ K\_ERR\_ARM\_SYNC\_PARITY\_ERROR

**Definition** arch.h:107

[K\_ERR\_ARM\_SECURE\_ENTRY\_POINT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a454c50a4bf529eaf4a2e2fda636bbc3d)

@ K\_ERR\_ARM\_SECURE\_ENTRY\_POINT

**Definition** arch.h:92

[K\_ERR\_ARM\_USAGE\_ILLEGAL\_EXC\_RETURN](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a4646893d8e3fc6c19356c9c0e56e1766)

@ K\_ERR\_ARM\_USAGE\_ILLEGAL\_EXC\_RETURN

**Definition** arch.h:86

[K\_ERR\_ARM\_USAGE\_NO\_COPROCESSOR](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a4a10fc8ae3093fd24cb052457fa1783a)

@ K\_ERR\_ARM\_USAGE\_NO\_COPROCESSOR

**Definition** arch.h:85

[K\_ERR\_ARM\_SECURE\_INTEGRITY\_SIGNATURE](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a50e6eccecb232ce9c9bf987be6263288)

@ K\_ERR\_ARM\_SECURE\_INTEGRITY\_SIGNATURE

**Definition** arch.h:93

[K\_ERR\_ARM\_ASYNC\_EXTERNAL\_ABORT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a54d95700befedeb1da3378d5abd8d833)

@ K\_ERR\_ARM\_ASYNC\_EXTERNAL\_ABORT

**Definition** arch.h:106

[K\_ERR\_ARM\_MEM\_FP\_LAZY\_STATE\_PRESERVATION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5ad278e3284e621ace082e5d1d89c599)

@ K\_ERR\_ARM\_MEM\_FP\_LAZY\_STATE\_PRESERVATION

**Definition** arch.h:69

[K\_ERR\_ARM\_ALIGNMENT\_FAULT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5be6201ceaa069b4497e5dad46e9f8c1)

@ K\_ERR\_ARM\_ALIGNMENT\_FAULT

**Definition** arch.h:102

[K\_ERR\_ARM\_TRANSLATION\_FAULT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5c820b75e2d2941f160b1f47a6da6d76)

@ K\_ERR\_ARM\_TRANSLATION\_FAULT

**Definition** arch.h:110

[K\_ERR\_ARM\_USAGE\_UNALIGNED\_ACCESS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a5e41e262d0fb52266261a8e3a59e75ff)

@ K\_ERR\_ARM\_USAGE\_UNALIGNED\_ACCESS

**Definition** arch.h:83

[K\_ERR\_ARM\_USAGE\_ILLEGAL\_EPSR](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a750a9631b59488b406f228eb74656e82)

@ K\_ERR\_ARM\_USAGE\_ILLEGAL\_EPSR

**Definition** arch.h:87

[K\_ERR\_ARM\_MEM\_INSTRUCTION\_ACCESS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a776523f4671f98f87ccf9a76db9a186c)

@ K\_ERR\_ARM\_MEM\_INSTRUCTION\_ACCESS

**Definition** arch.h:68

[K\_ERR\_ARM\_SECURE\_EXCEPTION\_RETURN](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a78c476ea635a8c9459f1b644101f9350)

@ K\_ERR\_ARM\_SECURE\_EXCEPTION\_RETURN

**Definition** arch.h:94

[K\_ERR\_ARM\_BUS\_UNSTACKING](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a7a879301aa3ee1b2ce6abcacdc795b1d)

@ K\_ERR\_ARM\_BUS\_UNSTACKING

**Definition** arch.h:74

[K\_ERR\_ARM\_MEM\_GENERIC](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a7ac465c1decca4d761d420f62700c940)

@ K\_ERR\_ARM\_MEM\_GENERIC

**Definition** arch.h:64

[K\_ERR\_ARM\_BUS\_STACKING](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a7b5e93c7163bea86dbeff21759f6472e)

@ K\_ERR\_ARM\_BUS\_STACKING

**Definition** arch.h:73

[K\_ERR\_ARM\_USAGE\_DIV\_0](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a802af0dbe318680dfcd1805cb8b99fd8)

@ K\_ERR\_ARM\_USAGE\_DIV\_0

**Definition** arch.h:82

[K\_ERR\_ARM\_BUS\_GENERIC](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a899fe8e2d408404917b3bd166f07666c)

@ K\_ERR\_ARM\_BUS\_GENERIC

**Definition** arch.h:72

[K\_ERR\_ARM\_BUS\_IMPRECISE\_DATA\_BUS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a8cbae40f6ee1f7b65f02b330d5f7a8ae)

@ K\_ERR\_ARM\_BUS\_IMPRECISE\_DATA\_BUS

**Definition** arch.h:76

[K\_ERR\_ARM\_BUS\_INSTRUCTION\_BUS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a916d2fb2799c0355aace800ed43ad69c)

@ K\_ERR\_ARM\_BUS\_INSTRUCTION\_BUS

**Definition** arch.h:77

[K\_ERR\_ARM\_UNDEFINED\_INSTRUCTION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4a96392456666f9adb04ee89d78f208f6a)

@ K\_ERR\_ARM\_UNDEFINED\_INSTRUCTION

**Definition** arch.h:101

[K\_ERR\_ARM\_USAGE\_UNDEFINED\_INSTRUCTION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4aabd67bae03c199605f62c83b57b54159)

@ K\_ERR\_ARM\_USAGE\_UNDEFINED\_INSTRUCTION

**Definition** arch.h:88

[K\_ERR\_ARM\_ASYNC\_PARITY\_ERROR](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4ab655e2d4d1cf6a441362e80e969287f8)

@ K\_ERR\_ARM\_ASYNC\_PARITY\_ERROR

**Definition** arch.h:108

[K\_ERR\_ARM\_DEBUG\_EVENT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4abb352aab2d7667ed3c72eabe024d4c5c)

@ K\_ERR\_ARM\_DEBUG\_EVENT

**Definition** arch.h:109

[K\_ERR\_ARM\_SECURE\_ATTRIBUTION\_UNIT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4abbe3ce01c99bd423507dca6b27c4077b)

@ K\_ERR\_ARM\_SECURE\_ATTRIBUTION\_UNIT

**Definition** arch.h:95

[K\_ERR\_ARM\_SECURE\_TRANSITION](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4accffbb9380478d8e1612d2481246390b)

@ K\_ERR\_ARM\_SECURE\_TRANSITION

**Definition** arch.h:96

[K\_ERR\_ARM\_SECURE\_LAZY\_STATE\_ERROR](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4acf891bac81ed5e29b423507ac0a35139)

@ K\_ERR\_ARM\_SECURE\_LAZY\_STATE\_ERROR

**Definition** arch.h:98

[K\_ERR\_ARM\_USAGE\_STACK\_OVERFLOW](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4ada75e6e3d5102139cbcd7df2f67f8bc3)

@ K\_ERR\_ARM\_USAGE\_STACK\_OVERFLOW

**Definition** arch.h:84

[K\_ERR\_ARM\_BUS\_PRECISE\_DATA\_BUS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4aed122da9226657dea13a9afa9dbc43d5)

@ K\_ERR\_ARM\_BUS\_PRECISE\_DATA\_BUS

**Definition** arch.h:75

[K\_ERR\_ARM\_MEM\_DATA\_ACCESS](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4af52bcf1db9ed0dfc47f4d1b9698c23a6)

@ K\_ERR\_ARM\_MEM\_DATA\_ACCESS

**Definition** arch.h:67

[K\_ERR\_ARM\_PERMISSION\_FAULT](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4afbc0c25bea6fe87969248a41f58e6822)

@ K\_ERR\_ARM\_PERMISSION\_FAULT

**Definition** arch.h:104

[K\_ERR\_ARM\_USAGE\_GENERIC](arm_2arch_8h.md#a5891f4f431f3817d4bb9f652ff45a9c4afbe97c341bf54d94c42c4ec456d586ca)

@ K\_ERR\_ARM\_USAGE\_GENERIC

**Definition** arch.h:81

[asm\_inline.h](arm_2asm__inline_8h.md)

[cpu.h](arm_2cortex__a__r_2cpu_8h.md)

[cpu.h](arm_2cortex__m_2cpu_8h.md)

[error.h](arm_2error_8h.md)

ARM AArch32 public error handling.

[exception.h](arm_2exception_8h.md)

ARM AArch32 public exception handling.

[misc.h](arm_2misc_8h.md)

ARM AArch32 public kernel miscellaneous.

[armv8\_timer.h](armv8__timer_8h.md)

[lib\_helpers.h](cortex__a__r_2lib__helpers_8h.md)

[timer.h](cortex__a__r_2timer_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[fatal\_types.h](fatal__types_8h.md)

Fatal base type definitions.

[ffs.h](ffs_8h.md)

[K\_ERR\_ARCH\_START](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a45d4bf1a392f99d6b4d15f50a0e333d1)

@ K\_ERR\_ARCH\_START

Arch specific fatal errors.

**Definition** fatal\_types.h:41

[memory\_map.h](memory__map_8h.md)

ARM CORTEX-M memory map.

[arm\_mmu.h](mmu_2arm__mmu_8h.md)

[arm\_mpu.h](mpu_2arm__mpu_8h.md)

[nmi.h](nmi_8h.md)

ARM AArch32 NMI routines.

[nxp\_mpu.h](nxp__mpu_8h.md)

[sys\_bitops.h](sys__bitops_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [arch.h](arm_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
