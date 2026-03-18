---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/kernel_2thread__stack_8h_source.html
original_path: doxygen/html/kernel_2thread__stack_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_stack.h

[Go to the documentation of this file.](kernel_2thread__stack_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

20

21#ifndef ZEPHYR\_INCLUDE\_KERNEL\_THREAD\_STACK\_H

22#define ZEPHYR\_INCLUDE\_KERNEL\_THREAD\_STACK\_H

23

24#if !defined(\_ASMLANGUAGE)

25#include <[zephyr/arch/cpu.h](cpu_8h.md)>

26#include <[zephyr/sys/util.h](util_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

32/\* Using typedef deliberately here, this is quite intended to be an opaque

33 \* type.

34 \*

35 \* The purpose of this data type is to clearly distinguish between the

36 \* declared symbol for a stack (of type k\_thread\_stack\_t) and the underlying

37 \* buffer which composes the stack data actually used by the underlying

38 \* thread; they cannot be used interchangeably as some arches precede the

39 \* stack buffer region with guard areas that trigger a MPU or MMU fault

40 \* if written to.

41 \*

42 \* APIs that want to work with the buffer inside should continue to use

43 \* char \*.

44 \*

45 \* Stacks should always be created with K\_THREAD\_STACK\_DEFINE().

46 \*/

47struct \_\_packed z\_thread\_stack\_element {

48 char data;

49};

50

57

58

69static inline char \*z\_stack\_ptr\_align(char \*ptr)

70{

71 return (char \*)[ROUND\_DOWN](group__sys-util.md#gad8d2389dbe7ea135eccf237dbafb76dd)(ptr, [ARCH\_STACK\_PTR\_ALIGN](arc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3));

72}

73#define Z\_STACK\_PTR\_ALIGN(ptr) ((uintptr\_t)z\_stack\_ptr\_align((char \*)(ptr)))

74

88#define Z\_STACK\_PTR\_TO\_FRAME(type, ptr) \

89 (type \*)((ptr) - sizeof(type))

90

91#ifdef ARCH\_KERNEL\_STACK\_RESERVED

92#define K\_KERNEL\_STACK\_RESERVED ((size\_t)ARCH\_KERNEL\_STACK\_RESERVED)

93#else

[ 94](kernel_2thread__stack_8h.md#aa66525a4ec83e91d97ec4699acaa72fd)#define K\_KERNEL\_STACK\_RESERVED ((size\_t)0)

95#endif /\* ARCH\_KERNEL\_STACK\_RESERVED \*/

96

97#define Z\_KERNEL\_STACK\_SIZE\_ADJUST(size) (ROUND\_UP(size, \

98 ARCH\_STACK\_PTR\_ALIGN) + \

99 K\_KERNEL\_STACK\_RESERVED)

100

101#ifdef ARCH\_KERNEL\_STACK\_OBJ\_ALIGN

102#define Z\_KERNEL\_STACK\_OBJ\_ALIGN ARCH\_KERNEL\_STACK\_OBJ\_ALIGN

103#else

104#define Z\_KERNEL\_STACK\_OBJ\_ALIGN ARCH\_STACK\_PTR\_ALIGN

105#endif /\* ARCH\_KERNEL\_STACK\_OBJ\_ALIGN \*/

106

[ 107](kernel_2thread__stack_8h.md#a12f78cb2d5b9bf83068e810bf1e31937)#define K\_KERNEL\_STACK\_LEN(size) \

108 ROUND\_UP(Z\_KERNEL\_STACK\_SIZE\_ADJUST(size), Z\_KERNEL\_STACK\_OBJ\_ALIGN)

109

114

[ 124](group__thread__stack__api.md#ga1ba82b0f3abe9c573930ea73e9ed528e)#define K\_KERNEL\_STACK\_DECLARE(sym, size) \

125 extern struct z\_thread\_stack\_element \

126 sym[K\_KERNEL\_STACK\_LEN(size)]

127

[ 138](group__thread__stack__api.md#gae7562ba4ce258964c7f28eb0611d1b75)#define K\_KERNEL\_STACK\_ARRAY\_DECLARE(sym, nmemb, size) \

139 extern struct z\_thread\_stack\_element \

140 sym[nmemb][K\_KERNEL\_STACK\_LEN(size)]

141

[ 152](group__thread__stack__api.md#gaaf146fa0dc43938d7ac4a8d2e79b673d)#define K\_KERNEL\_PINNED\_STACK\_ARRAY\_DECLARE(sym, nmemb, size) \

153 extern struct z\_thread\_stack\_element \

154 sym[nmemb][K\_KERNEL\_STACK\_LEN(size)]

155

175#define Z\_KERNEL\_STACK\_DEFINE\_IN(sym, size, lsect) \

176 struct z\_thread\_stack\_element lsect \

177 \_\_aligned(Z\_KERNEL\_STACK\_OBJ\_ALIGN) \

178 sym[K\_KERNEL\_STACK\_LEN(size)]

179

188#define Z\_KERNEL\_STACK\_ARRAY\_DEFINE\_IN(sym, nmemb, size, lsect) \

189 struct z\_thread\_stack\_element lsect \

190 \_\_aligned(Z\_KERNEL\_STACK\_OBJ\_ALIGN) \

191 sym[nmemb][K\_KERNEL\_STACK\_LEN(size)]

192

[ 214](group__thread__stack__api.md#ga9e05e3cb5aa5b72d6f19e2f327313271)#define K\_KERNEL\_STACK\_DEFINE(sym, size) \

215 Z\_KERNEL\_STACK\_DEFINE\_IN(sym, size, \_\_kstackmem)

216

229#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

230#define K\_KERNEL\_PINNED\_STACK\_DEFINE(sym, size) \

231 Z\_KERNEL\_STACK\_DEFINE\_IN(sym, size, \_\_pinned\_noinit)

232#else

[ 233](group__thread__stack__api.md#ga7f6a9e1bd5f99b5240c69d372bfd4aa0)#define K\_KERNEL\_PINNED\_STACK\_DEFINE(sym, size) \

234 Z\_KERNEL\_STACK\_DEFINE\_IN(sym, size, \_\_kstackmem)

235#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

236

[ 246](group__thread__stack__api.md#gaf05127bd2ab7e8a0aeb394f18cbd923a)#define K\_KERNEL\_STACK\_ARRAY\_DEFINE(sym, nmemb, size) \

247 Z\_KERNEL\_STACK\_ARRAY\_DEFINE\_IN(sym, nmemb, size, \_\_kstackmem)

248

262#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

263#define K\_KERNEL\_PINNED\_STACK\_ARRAY\_DEFINE(sym, nmemb, size) \

264 Z\_KERNEL\_STACK\_ARRAY\_DEFINE\_IN(sym, nmemb, size, \_\_pinned\_noinit)

265#else

[ 266](group__thread__stack__api.md#ga628f79ffde2cc43cf7b5525e5f4276df)#define K\_KERNEL\_PINNED\_STACK\_ARRAY\_DEFINE(sym, nmemb, size) \

267 Z\_KERNEL\_STACK\_ARRAY\_DEFINE\_IN(sym, nmemb, size, \_\_kstackmem)

268#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

269

[ 279](group__thread__stack__api.md#ga600162959def399e70310b944834711f)#define K\_KERNEL\_STACK\_MEMBER(sym, size) \

280 Z\_KERNEL\_STACK\_DEFINE\_IN(sym, size,)

281

[ 282](group__thread__stack__api.md#ga57b3824b117c634dbb6052d47dc4301c)#define K\_KERNEL\_STACK\_SIZEOF(sym) (sizeof(sym) - K\_KERNEL\_STACK\_RESERVED)

283

285

[ 286](kernel_2thread__stack_8h.md#a2a62720663b4529ac89af173e79707d7)static inline char \*[K\_KERNEL\_STACK\_BUFFER](kernel_2thread__stack_8h.md#a2a62720663b4529ac89af173e79707d7)([k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*sym)

287{

288 return (char \*)sym + [K\_KERNEL\_STACK\_RESERVED](kernel_2thread__stack_8h.md#aa66525a4ec83e91d97ec4699acaa72fd);

289}

290#ifndef CONFIG\_USERSPACE

291#define K\_THREAD\_STACK\_RESERVED K\_KERNEL\_STACK\_RESERVED

292#define K\_THREAD\_STACK\_SIZEOF K\_KERNEL\_STACK\_SIZEOF

293#define K\_THREAD\_STACK\_LEN K\_KERNEL\_STACK\_LEN

294#define K\_THREAD\_STACK\_DEFINE K\_KERNEL\_STACK\_DEFINE

295#define K\_THREAD\_STACK\_ARRAY\_DEFINE K\_KERNEL\_STACK\_ARRAY\_DEFINE

296#define K\_THREAD\_STACK\_MEMBER K\_KERNEL\_STACK\_MEMBER

297#define K\_THREAD\_STACK\_BUFFER K\_KERNEL\_STACK\_BUFFER

298#define K\_THREAD\_STACK\_DECLARE K\_KERNEL\_STACK\_DECLARE

299#define K\_THREAD\_STACK\_ARRAY\_DECLARE K\_KERNEL\_STACK\_ARRAY\_DECLARE

300#define K\_THREAD\_PINNED\_STACK\_DEFINE K\_KERNEL\_PINNED\_STACK\_DEFINE

301#define K\_THREAD\_PINNED\_STACK\_ARRAY\_DEFINE \

302 K\_KERNEL\_PINNED\_STACK\_ARRAY\_DEFINE

303#else

319#ifdef ARCH\_THREAD\_STACK\_RESERVED

320#define K\_THREAD\_STACK\_RESERVED ((size\_t)(ARCH\_THREAD\_STACK\_RESERVED))

321#else

[ 322](kernel_2thread__stack_8h.md#a025b257739ad52fe7106585b51468e49)#define K\_THREAD\_STACK\_RESERVED ((size\_t)0U)

323#endif /\* ARCH\_THREAD\_STACK\_RESERVED \*/

324

350#if defined(ARCH\_THREAD\_STACK\_OBJ\_ALIGN)

351#define Z\_THREAD\_STACK\_OBJ\_ALIGN(size) \

352 ARCH\_THREAD\_STACK\_OBJ\_ALIGN(Z\_THREAD\_STACK\_SIZE\_ADJUST(size))

353#else

354#define Z\_THREAD\_STACK\_OBJ\_ALIGN(size) ARCH\_STACK\_PTR\_ALIGN

355#endif /\* ARCH\_THREAD\_STACK\_OBJ\_ALIGN \*/

356

383#if defined(ARCH\_THREAD\_STACK\_SIZE\_ADJUST)

384#define Z\_THREAD\_STACK\_SIZE\_ADJUST(size) \

385 ARCH\_THREAD\_STACK\_SIZE\_ADJUST((size) + K\_THREAD\_STACK\_RESERVED)

386#else

387#define Z\_THREAD\_STACK\_SIZE\_ADJUST(size) \

388 (ROUND\_UP((size), ARCH\_STACK\_PTR\_ALIGN) + K\_THREAD\_STACK\_RESERVED)

389#endif /\* ARCH\_THREAD\_STACK\_SIZE\_ADJUST \*/

390

395

[ 405](group__thread__stack__api.md#gab42c634630b892599bdf797e65563a83)#define K\_THREAD\_STACK\_DECLARE(sym, size) \

406 extern struct z\_thread\_stack\_element \

407 sym[K\_THREAD\_STACK\_LEN(size)]

408

[ 419](group__thread__stack__api.md#ga9c7578df16dfbd9067ee2a6ec5fc0ab6)#define K\_THREAD\_STACK\_ARRAY\_DECLARE(sym, nmemb, size) \

420 extern struct z\_thread\_stack\_element \

421 sym[nmemb][K\_THREAD\_STACK\_LEN(size)]

422

[ 437](group__thread__stack__api.md#ga775f8e6b4144cfdd24f3261b6db64150)#define K\_THREAD\_STACK\_SIZEOF(sym) (sizeof(sym) - K\_THREAD\_STACK\_RESERVED)

438

467#define Z\_THREAD\_STACK\_DEFINE\_IN(sym, size, lsect) \

468 struct z\_thread\_stack\_element lsect \

469 \_\_aligned(Z\_THREAD\_STACK\_OBJ\_ALIGN(size)) \

470 sym[K\_THREAD\_STACK\_LEN(size)]

471

486#define Z\_THREAD\_STACK\_ARRAY\_DEFINE\_IN(sym, nmemb, size, lsect) \

487 struct z\_thread\_stack\_element lsect \

488 \_\_aligned(Z\_THREAD\_STACK\_OBJ\_ALIGN(size)) \

489 sym[nmemb][K\_THREAD\_STACK\_LEN(size)]

490

[ 517](group__thread__stack__api.md#gac5368ce24fdeab3863b5c8dee2ebd955)#define K\_THREAD\_STACK\_DEFINE(sym, size) \

518 Z\_THREAD\_STACK\_DEFINE\_IN(sym, size, \_\_stackmem)

519

550#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

551#define K\_THREAD\_PINNED\_STACK\_DEFINE(sym, size) \

552 Z\_THREAD\_STACK\_DEFINE\_IN(sym, size, \_\_pinned\_noinit)

553#else

[ 554](group__thread__stack__api.md#ga7227f78410cf126deb5b185a0534f7f3)#define K\_THREAD\_PINNED\_STACK\_DEFINE(sym, size) \

555 K\_THREAD\_STACK\_DEFINE(sym, size)

556#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

557

[ 571](group__thread__stack__api.md#ga72fa31a9d8e28ccabd6e5e908a24ec00)#define K\_THREAD\_STACK\_LEN(size) \

572 ROUND\_UP(Z\_THREAD\_STACK\_SIZE\_ADJUST(size), \

573 Z\_THREAD\_STACK\_OBJ\_ALIGN(size))

574

[ 588](group__thread__stack__api.md#gaae2471b24bdc574382f083163fb42597)#define K\_THREAD\_STACK\_ARRAY\_DEFINE(sym, nmemb, size) \

589 Z\_THREAD\_STACK\_ARRAY\_DEFINE\_IN(sym, nmemb, size, \_\_stackmem)

590

608#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

609#define K\_THREAD\_PINNED\_STACK\_ARRAY\_DEFINE(sym, nmemb, size) \

610 Z\_THREAD\_PINNED\_STACK\_DEFINE\_IN(sym, nmemb, size, \_\_pinned\_noinit)

611#else

[ 612](group__thread__stack__api.md#gaa2e5014926e11e2241141cdd82888b09)#define K\_THREAD\_PINNED\_STACK\_ARRAY\_DEFINE(sym, nmemb, size) \

613 K\_THREAD\_STACK\_ARRAY\_DEFINE(sym, nmemb, size)

614#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

615

[ 634](group__thread__stack__api.md#ga753188e7f124f0ee03ed0fa1dad8ecfb)#define K\_THREAD\_STACK\_MEMBER(sym, size) \_\_DEPRECATED\_MACRO \

635 Z\_THREAD\_STACK\_DEFINE\_IN(sym, size,)

636

638

[ 653](kernel_2thread__stack_8h.md#a14296483e6ba0ef950a4b0e719b388e6)static inline char \*[K\_THREAD\_STACK\_BUFFER](kernel_2thread__stack_8h.md#a14296483e6ba0ef950a4b0e719b388e6)([k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*sym)

654{

655 return (char \*)sym + [K\_THREAD\_STACK\_RESERVED](kernel_2thread__stack_8h.md#a025b257739ad52fe7106585b51468e49);

656}

657

658#endif /\* CONFIG\_USERSPACE \*/

659

660#ifdef \_\_cplusplus

661}

662#endif

663

664#endif /\* \_ASMLANGUAGE \*/

665#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_THREAD\_STACK\_H \*/

[ARCH\_STACK\_PTR\_ALIGN](arc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)

#define ARCH\_STACK\_PTR\_ALIGN

**Definition** arch.h:98

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:46

[cpu.h](cpu_8h.md)

[ROUND\_DOWN](group__sys-util.md#gad8d2389dbe7ea135eccf237dbafb76dd)

#define ROUND\_DOWN(x, align)

Value of x rounded down to the previous multiple of align.

**Definition** util.h:313

[K\_THREAD\_STACK\_RESERVED](kernel_2thread__stack_8h.md#a025b257739ad52fe7106585b51468e49)

#define K\_THREAD\_STACK\_RESERVED

Indicate how much additional memory is reserved for stack objects.

**Definition** thread\_stack.h:322

[K\_THREAD\_STACK\_BUFFER](kernel_2thread__stack_8h.md#a14296483e6ba0ef950a4b0e719b388e6)

static char \* K\_THREAD\_STACK\_BUFFER(k\_thread\_stack\_t \*sym)

Get a pointer to the physical stack buffer.

**Definition** thread\_stack.h:653

[K\_KERNEL\_STACK\_BUFFER](kernel_2thread__stack_8h.md#a2a62720663b4529ac89af173e79707d7)

static char \* K\_KERNEL\_STACK\_BUFFER(k\_thread\_stack\_t \*sym)

**Definition** thread\_stack.h:286

[K\_KERNEL\_STACK\_RESERVED](kernel_2thread__stack_8h.md#aa66525a4ec83e91d97ec4699acaa72fd)

#define K\_KERNEL\_STACK\_RESERVED

**Definition** thread\_stack.h:94

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [thread\_stack.h](kernel_2thread__stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
