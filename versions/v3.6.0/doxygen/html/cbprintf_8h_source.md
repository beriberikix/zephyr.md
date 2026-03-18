---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/cbprintf_8h_source.html
original_path: doxygen/html/cbprintf_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cbprintf.h

[Go to the documentation of this file.](cbprintf_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_H\_

9

10#include <stdarg.h>

11#include <stddef.h>

12#include <[stdint.h](stdint_8h.md)>

13#include <[zephyr/toolchain.h](toolchain_8h.md)>

14#include <[string.h](string_8h.md)>

15

16#ifdef CONFIG\_CBPRINTF\_LIBC\_SUBSTS

17#include <[stdio.h](stdio_8h.md)>

18#endif /\* CONFIG\_CBPRINTF\_LIBC\_SUBSTS \*/

19

20/\* Determine if \_Generic is supported using macro from toolchain.h.

21 \*

22 \* @note Z\_C\_GENERIC is also set for C++ where functionality is implemented

23 \* using overloading and templates.

24 \*/

25#ifndef Z\_C\_GENERIC

26#if defined(\_\_cplusplus) || TOOLCHAIN\_HAS\_C\_GENERIC

27#define Z\_C\_GENERIC 1

28#else

29#define Z\_C\_GENERIC 0

30#endif

31#endif

32

33#ifdef \_\_xtensa\_\_

34#define Z\_PKG\_HDR\_EXT\_XTENSA\_ALIGNMENT 8

35#ifdef CONFIG\_CBPRINTF\_PACKAGE\_HEADER\_STORE\_CREATION\_FLAGS

36#define Z\_PKG\_DESC\_XTENSA\_PADDING 1

37#else

38#define Z\_PKG\_DESC\_XTENSA\_PADDING 0

39#endif

40#endif /\* \_\_xtensa\_\_ \*/

41

[ 45](structcbprintf__package__desc.md)struct [cbprintf\_package\_desc](structcbprintf__package__desc.md) {

[ 47](structcbprintf__package__desc.md#a02876d066dd9ac4ba5bd3bdc19ff7681) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structcbprintf__package__desc.md#a02876d066dd9ac4ba5bd3bdc19ff7681);

48

[ 50](structcbprintf__package__desc.md#a3614347546912dae53d8f9633299912d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [str\_cnt](structcbprintf__package__desc.md#a3614347546912dae53d8f9633299912d);

51

[ 53](structcbprintf__package__desc.md#ad9878876ae963e93850dcfd8d5df7b2f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ro\_str\_cnt](structcbprintf__package__desc.md#ad9878876ae963e93850dcfd8d5df7b2f);

54

[ 56](structcbprintf__package__desc.md#ae9695a5e1a4fb70e3be5e9ab63c89937) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rw\_str\_cnt](structcbprintf__package__desc.md#ae9695a5e1a4fb70e3be5e9ab63c89937);

57

58#ifdef CONFIG\_CBPRINTF\_PACKAGE\_HEADER\_STORE\_CREATION\_FLAGS

60 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pkg\_flags;

61#endif

62#ifdef \_\_xtensa\_\_

63 /\*

64 \* On Xtensa, the first argument needs to be aligned to 8-byte.

65 \* With 32-bit pointers, we need another 4 bytes padding so

66 \* that whole struct cbprintf\_package\_hdr\_ext is of multiple of

67 \* 8 bytes.

68 \*/

69 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_padding[Z\_PKG\_DESC\_XTENSA\_PADDING];

70#endif

71

72} \_\_packed;

73

[ 78](unioncbprintf__package__hdr.md)union [cbprintf\_package\_hdr](unioncbprintf__package__hdr.md) {

[ 80](unioncbprintf__package__hdr.md#aa5e4c2d21fde006827031c41e64e0c04) struct [cbprintf\_package\_desc](structcbprintf__package__desc.md) [desc](unioncbprintf__package__hdr.md#aa5e4c2d21fde006827031c41e64e0c04);

81

[ 82](unioncbprintf__package__hdr.md#a5370d9447cf6266178e06e8f6967ba29) void \*[raw](unioncbprintf__package__hdr.md#a5370d9447cf6266178e06e8f6967ba29);

83

84#if defined(CONFIG\_CBPRINTF\_PACKAGE\_HEADER\_STORE\_CREATION\_FLAGS) && !defined(CONFIG\_64BIT)

85 void \*raw2[2];

86#endif

87

88} \_\_packed;

89

90

91

[ 96](structcbprintf__package__hdr__ext.md)struct [cbprintf\_package\_hdr\_ext](structcbprintf__package__hdr__ext.md) {

[ 98](structcbprintf__package__hdr__ext.md#a3f1d9bc9ee58367a8e0a4ce29c73a0f5) union [cbprintf\_package\_hdr](unioncbprintf__package__hdr.md) [hdr](structcbprintf__package__hdr__ext.md#a3f1d9bc9ee58367a8e0a4ce29c73a0f5);

99

[ 101](structcbprintf__package__hdr__ext.md#af726d9f674740030ccf5f7e13a9b0aa9) char \*[fmt](structcbprintf__package__hdr__ext.md#af726d9f674740030ccf5f7e13a9b0aa9);

102

103 /\*

104 \* When extending this struct, make sure this align

105 \* to pointer size.

106 \*/

107} \_\_packed;

108

109

115#ifdef \_\_xtensa\_\_

116BUILD\_ASSERT(sizeof(struct [cbprintf\_package\_hdr\_ext](structcbprintf__package__hdr__ext.md)) % Z\_PKG\_HDR\_EXT\_XTENSA\_ALIGNMENT == 0,

117 "Package header size on Xtensa must be aligned");

118#endif

122

123/\* Z\_C\_GENERIC is used there \*/

124#include <[zephyr/sys/cbprintf\_internal.h](cbprintf__internal_8h.md)>

125

126#ifdef \_\_cplusplus

127extern "C" {

128#endif

129

135

137#ifdef \_\_xtensa\_\_

138#define CBPRINTF\_PACKAGE\_ALIGNMENT 16

139#else

[ 140](group__cbprintf__apis.md#ga3b917fb81bb246a0910066e2708dbd78)#define CBPRINTF\_PACKAGE\_ALIGNMENT \

141 Z\_POW2\_CEIL(COND\_CODE\_1(CONFIG\_CBPRINTF\_PACKAGE\_LONGDOUBLE, \

142 (sizeof(long double)), (MAX(sizeof(double), sizeof(long long)))))

143#endif

144

145BUILD\_ASSERT(Z\_IS\_POW2([CBPRINTF\_PACKAGE\_ALIGNMENT](group__cbprintf__apis.md#ga3b917fb81bb246a0910066e2708dbd78)));

146

147

151

[ 156](group__CBPRINTF__PACKAGE__FLAGS.md#ga6c16ab0b5d98012ffb00942e85d859b3)#define CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO BIT(0)

157

[ 159](group__CBPRINTF__PACKAGE__FLAGS.md#ga406facc18bf99afe16d453253d042dbb)#define CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS BIT(1)

160

[ 165](group__CBPRINTF__PACKAGE__FLAGS.md#gac6ac59dda3a1a8a4572c1012b4adcbaa)#define CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS BIT(2)

166

167#define Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_BITS 3

168#define Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_OFFSET 3

169#define Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_MASK BIT\_MASK(Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_BITS)

170

[ 178](group__CBPRINTF__PACKAGE__FLAGS.md#ga26b5e05198f6609049c54e439b78cf3c)#define CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT(n) \

179 (n << Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_OFFSET)

180

184#define Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT\_GET(flags) \

185 (((flags) >> Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_OFFSET) & Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_MASK)

186

[ 193](group__CBPRINTF__PACKAGE__FLAGS.md#ga95b0b7f91303781b8bad610f7cac3fa3)#define CBPRINTF\_PACKAGE\_ADD\_STRING\_IDXS \

194 (CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS | CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO)

195

[ 201](group__CBPRINTF__PACKAGE__FLAGS.md#gaa8edaf31e7acfb7cb113afa873efa126)#define CBPRINTF\_PACKAGE\_ARGS\_ARE\_TAGGED BIT(6)

202

204

209

[ 218](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga9802b700abd5d3cd7cef0e0cbcceb3e7)#define CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR BIT(0)

[ 220](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga3da36360cc579adbd5e991addf4c3fc6)#define CBPRINTF\_PACKAGE\_COPY\_RO\_STR CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR \_\_DEPRECATED\_MACRO

221

[ 232](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga983c65ed8afb356a29fa2736f9de7b39)#define CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR BIT(1)

[ 234](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga1b3b798a2a208276ddc3931b06064323)#define CBPRINTF\_PACKAGE\_COPY\_RW\_STR CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR \_\_DEPRECATED\_MACRO

235

[ 241](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga582ebea3e0d18285840bf277c5382da6)#define CBPRINTF\_PACKAGE\_CONVERT\_KEEP\_RO\_STR BIT(2)

[ 243](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga66d65a0f8f9c32440cb7b92a37d0e248)#define CBPRINTF\_PACKAGE\_COPY\_KEEP\_RO\_STR CBPRINTF\_PACKAGE\_CONVERT\_KEEP\_RO\_STR \_\_DEPRECATED\_MACRO

244

[ 262](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga370563f835488868020effcd48b23b90)#define CBPRINTF\_PACKAGE\_CONVERT\_PTR\_CHECK BIT(3)

263

265

270

276#define Z\_CBVPRINTF\_PROCESS\_FLAG\_TAGGED\_ARGS BIT(0)

277

279

280#include <[zephyr/sys/cbprintf\_enums.h](cbprintf__enums_8h.md)>

281

299#ifdef \_\_CHECKER\_\_

300typedef int (\*[cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83))(int c, void \*ctx);

301#else

[ 302](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83)typedef int (\*[cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83))(/\* int c, void \*ctx \*/);

303#endif

304

[ 313](group__cbprintf__apis.md#ga6e31a5fb5cd760fbb8d0ff5fd5cc3991)typedef int (\*[cbprintf\_convert\_cb](group__cbprintf__apis.md#ga6e31a5fb5cd760fbb8d0ff5fd5cc3991))(const void \*buf, size\_t len, void \*ctx);

314

[ 333](group__cbprintf__apis.md#ga0decdf49ce8a1594d5c99e93648a24f7)typedef int (\*[cbvprintf\_external\_formatter\_func](group__cbprintf__apis.md#ga0decdf49ce8a1594d5c99e93648a24f7))([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx,

334 const char \*fmt, va\_list ap);

335

[ 353](group__cbprintf__apis.md#ga4d0a2d35198c2feef1423a1454a98ae6)#define CBPRINTF\_MUST\_RUNTIME\_PACKAGE(flags, ... /\* fmt, ... \*/) \

354 Z\_CBPRINTF\_MUST\_RUNTIME\_PACKAGE(flags, \_\_VA\_ARGS\_\_)

355

[ 385](group__cbprintf__apis.md#ga1ac0f7d0956fc96a9d850d2fef928285)#define CBPRINTF\_STATIC\_PACKAGE(packaged, inlen, outlen, align\_offset, flags, \

386 ... /\* fmt, ... \*/) \

387 Z\_CBPRINTF\_STATIC\_PACKAGE(packaged, inlen, outlen, \

388 align\_offset, flags, \_\_VA\_ARGS\_\_)

389

430\_\_printf\_like(4, 5)

[ 431](group__cbprintf__apis.md#gad9c56f0a84f60cc53fa9e687069a8f1b)int [cbprintf\_package](group__cbprintf__apis.md#gad9c56f0a84f60cc53fa9e687069a8f1b)(void \*packaged,

432 size\_t len,

433 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

434 const char \*format,

435 ...);

436

[ 471](group__cbprintf__apis.md#gaa83f17925daa9747d329b6f1078ab15a)int [cbvprintf\_package](group__cbprintf__apis.md#gaa83f17925daa9747d329b6f1078ab15a)(void \*packaged,

472 size\_t len,

473 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

474 const char \*format,

475 va\_list ap);

476

[ 512](group__cbprintf__apis.md#ga3d7895fa3997bfd4ecf9cb3711c9bf3f)int [cbprintf\_package\_convert](group__cbprintf__apis.md#ga3d7895fa3997bfd4ecf9cb3711c9bf3f)(void \*in\_packaged,

513 size\_t in\_len,

514 [cbprintf\_convert\_cb](group__cbprintf__apis.md#ga6e31a5fb5cd760fbb8d0ff5fd5cc3991) cb,

515 void \*ctx,

516 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

517 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*strl,

518 size\_t strl\_len);

519

520/\* @interal Context used for package copying. \*/

521struct z\_cbprintf\_buf\_desc {

522 void \*buf;

523 size\_t size;

524 size\_t [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394);

525};

526

527/\* @internal Function callback used for package copying. \*/

528static inline int z\_cbprintf\_cpy(const void \*buf, size\_t len, void \*ctx)

529{

530 struct z\_cbprintf\_buf\_desc \*desc = (struct z\_cbprintf\_buf\_desc \*)ctx;

531

532 if ((desc->size - desc->off) < len) {

533 return -[ENOSPC](group__system__errno.md#ga088abe8bad2df798edad3053d719b937);

534 }

535

536 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)desc->buf)[desc->off], buf, len);

537 desc->off += len;

538

539 return len;

540}

541

[ 572](group__cbprintf__apis.md#ga881520f4756c1a00270b3b3d12d6fc32)static inline int [cbprintf\_package\_copy](group__cbprintf__apis.md#ga881520f4756c1a00270b3b3d12d6fc32)(void \*in\_packaged,

573 size\_t in\_len,

574 void \*packaged,

575 size\_t len,

576 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

577 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*strl,

578 size\_t strl\_len)

579{

580 struct z\_cbprintf\_buf\_desc buf\_desc = {

581 .buf = packaged,

582 .size = len,

583 .off = 0,

584 };

585

586 return [cbprintf\_package\_convert](group__cbprintf__apis.md#ga3d7895fa3997bfd4ecf9cb3711c9bf3f)(in\_packaged, in\_len,

587 packaged ? z\_cbprintf\_cpy : NULL, &buf\_desc,

588 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), strl, strl\_len);

589}

590

[ 620](group__cbprintf__apis.md#ga66fcefde504d543eb9114bc2fff230d2)static inline int [cbprintf\_fsc\_package](group__cbprintf__apis.md#ga66fcefde504d543eb9114bc2fff230d2)(void \*in\_packaged,

621 size\_t in\_len,

622 void \*packaged,

623 size\_t len)

624{

625 return [cbprintf\_package\_copy](group__cbprintf__apis.md#ga881520f4756c1a00270b3b3d12d6fc32)(in\_packaged, in\_len, packaged, len,

626 [CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga9802b700abd5d3cd7cef0e0cbcceb3e7) |

627 [CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga983c65ed8afb356a29fa2736f9de7b39), NULL, 0);

628}

629

[ 650](group__cbprintf__apis.md#gaa1a040db7e5171dd80d84cd871dfc687)int [cbpprintf\_external](group__cbprintf__apis.md#gaa1a040db7e5171dd80d84cd871dfc687)([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out,

651 [cbvprintf\_external\_formatter\_func](group__cbprintf__apis.md#ga0decdf49ce8a1594d5c99e93648a24f7) formatter,

652 void \*ctx,

653 void \*packaged);

654

681\_\_printf\_like(3, 4)

[ 682](group__cbprintf__apis.md#ga0cebdbf4f142ee28c5bd80a1615647da)int [cbprintf](group__cbprintf__apis.md#ga0cebdbf4f142ee28c5bd80a1615647da)([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*format, ...);

683

712int z\_cbvprintf\_impl([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*format,

713 va\_list ap, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

714

740#ifdef CONFIG\_PICOLIBC

741int [cbvprintf](group__cbprintf__apis.md#ga8958868def2ba1675ebc8b3a70ff86f8)([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*format, va\_list ap);

742#else

743static inline

[ 744](group__cbprintf__apis.md#ga8958868def2ba1675ebc8b3a70ff86f8)int [cbvprintf](group__cbprintf__apis.md#ga8958868def2ba1675ebc8b3a70ff86f8)([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx, const char \*format, va\_list ap)

745{

746 return z\_cbvprintf\_impl(out, ctx, format, ap, 0);

747}

748#endif

749

777static inline

[ 778](group__cbprintf__apis.md#gae4d5066fff73bb38250f4dc82c43ebdc)int [cbvprintf\_tagged\_args](group__cbprintf__apis.md#gae4d5066fff73bb38250f4dc82c43ebdc)([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx,

779 const char \*format, va\_list ap)

780{

781 return z\_cbvprintf\_impl(out, ctx, format, ap,

782 Z\_CBVPRINTF\_PROCESS\_FLAG\_TAGGED\_ARGS);

783}

784

802static inline

[ 803](group__cbprintf__apis.md#ga150fa7bb8dfb96db886006c9115e1dd7)int [cbpprintf](group__cbprintf__apis.md#ga150fa7bb8dfb96db886006c9115e1dd7)([cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83) out, void \*ctx, void \*packaged)

804{

805#if defined(CONFIG\_CBPRINTF\_PACKAGE\_SUPPORT\_TAGGED\_ARGUMENTS)

806 union [cbprintf\_package\_hdr](unioncbprintf__package__hdr.md) \*hdr =

807 (union [cbprintf\_package\_hdr](unioncbprintf__package__hdr.md) \*)packaged;

808

809 if ((hdr->[desc](unioncbprintf__package__hdr.md#aa5e4c2d21fde006827031c41e64e0c04).pkg\_flags & [CBPRINTF\_PACKAGE\_ARGS\_ARE\_TAGGED](group__CBPRINTF__PACKAGE__FLAGS.md#gaa8edaf31e7acfb7cb113afa873efa126))

810 == [CBPRINTF\_PACKAGE\_ARGS\_ARE\_TAGGED](group__CBPRINTF__PACKAGE__FLAGS.md#gaa8edaf31e7acfb7cb113afa873efa126)) {

811 return [cbpprintf\_external](group__cbprintf__apis.md#gaa1a040db7e5171dd80d84cd871dfc687)(out, [cbvprintf\_tagged\_args](group__cbprintf__apis.md#gae4d5066fff73bb38250f4dc82c43ebdc),

812 ctx, packaged);

813 }

814#endif

815

816 return [cbpprintf\_external](group__cbprintf__apis.md#gaa1a040db7e5171dd80d84cd871dfc687)(out, [cbvprintf](group__cbprintf__apis.md#ga8958868def2ba1675ebc8b3a70ff86f8), ctx, packaged);

817}

818

819#ifdef CONFIG\_CBPRINTF\_LIBC\_SUBSTS

820

821#ifdef CONFIG\_PICOLIBC

822

823#define fprintfcb(stream, ...) fprintf(stream, \_\_VA\_ARGS\_\_)

824#define vfprintfcb(stream, format, ap) vfprintf(stream, format, ap)

825#define printfcb(format, ...) printf(format, \_\_VA\_ARGS\_\_)

826#define vprintfcb(format, ap) vprintf(format, ap)

827#define snprintfcb(str, size, ...) snprintf(str, size, \_\_VA\_ARGS\_\_)

828#define vsnprintfcb(str, size, format, ap) vsnprintf(str, size, format, ap)

829

830#else

831

850\_\_printf\_like(2, 3)

[ 851](group__cbprintf__apis.md#ga2636e91fd5d78835cfaffe5b5012638b)int [fprintfcb](group__cbprintf__apis.md#ga2636e91fd5d78835cfaffe5b5012638b)([FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \* stream, const char \*format, ...);

852

[ 870](group__cbprintf__apis.md#ga24d7226976f3acbe579b6d6b5d530ade)int [vfprintfcb](group__cbprintf__apis.md#ga24d7226976f3acbe579b6d6b5d530ade)([FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*stream, const char \*format, va\_list ap);

871

888\_\_printf\_like(1, 2)

[ 889](group__cbprintf__apis.md#ga17aa694ea800f8188a3de3babd524c3f)int [printfcb](group__cbprintf__apis.md#ga17aa694ea800f8188a3de3babd524c3f)(const char \*format, ...);

890

[ 906](group__cbprintf__apis.md#gaa70a1b73fb04b88b40c1fa5fd65efd15)int [vprintfcb](group__cbprintf__apis.md#gaa70a1b73fb04b88b40c1fa5fd65efd15)(const char \*format, va\_list ap);

907

931\_\_printf\_like(3, 4)

[ 932](group__cbprintf__apis.md#ga909f859afbc2a596cd0174f711a60047)int [snprintfcb](group__cbprintf__apis.md#ga909f859afbc2a596cd0174f711a60047)(char \*str, size\_t size, const char \*format, ...);

933

[ 956](group__cbprintf__apis.md#ga37b0f96a7b9c025659a902e8fd614b33)int [vsnprintfcb](group__cbprintf__apis.md#ga37b0f96a7b9c025659a902e8fd614b33)(char \*str, size\_t size, const char \*format, va\_list ap);

957

958#endif /\* CONFIG\_PICOLIBC \*/

959#endif /\* CONFIG\_CBPRINTF\_LIBC\_SUBSTS \*/

960

964

965#ifdef \_\_cplusplus

966}

967#endif

968

969#endif /\* ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_H\_ \*/

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[cbprintf\_enums.h](cbprintf__enums_8h.md)

[cbprintf\_internal.h](cbprintf__internal_8h.md)

[CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga9802b700abd5d3cd7cef0e0cbcceb3e7)

#define CBPRINTF\_PACKAGE\_CONVERT\_RO\_STR

Append read-only strings from source package to destination package.

**Definition** cbprintf.h:218

[CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR](group__CBPRINTF__PACKAGE__CONVERT__FLAGS.md#ga983c65ed8afb356a29fa2736f9de7b39)

#define CBPRINTF\_PACKAGE\_CONVERT\_RW\_STR

Append read-write strings from source package to destination package.

**Definition** cbprintf.h:232

[CBPRINTF\_PACKAGE\_ARGS\_ARE\_TAGGED](group__CBPRINTF__PACKAGE__FLAGS.md#gaa8edaf31e7acfb7cb113afa873efa126)

#define CBPRINTF\_PACKAGE\_ARGS\_ARE\_TAGGED

Indicate the incoming arguments are tagged.

**Definition** cbprintf.h:201

[cbprintf](group__cbprintf__apis.md#ga0cebdbf4f142ee28c5bd80a1615647da)

int cbprintf(cbprintf\_cb out, void \*ctx, const char \*format,...)

\*printf-like output through a callback.

[cbvprintf\_external\_formatter\_func](group__cbprintf__apis.md#ga0decdf49ce8a1594d5c99e93648a24f7)

int(\* cbvprintf\_external\_formatter\_func)(cbprintf\_cb out, void \*ctx, const char \*fmt, va\_list ap)

Signature for a external formatter function identical to cbvprintf.

**Definition** cbprintf.h:333

[cbpprintf](group__cbprintf__apis.md#ga150fa7bb8dfb96db886006c9115e1dd7)

static int cbpprintf(cbprintf\_cb out, void \*ctx, void \*packaged)

Generate the output for a previously captured format operation.

**Definition** cbprintf.h:803

[printfcb](group__cbprintf__apis.md#ga17aa694ea800f8188a3de3babd524c3f)

int printfcb(const char \*format,...)

printf using Zephyrs cbprintf infrastructure.

[vfprintfcb](group__cbprintf__apis.md#ga24d7226976f3acbe579b6d6b5d530ade)

int vfprintfcb(FILE \*stream, const char \*format, va\_list ap)

vfprintf using Zephyrs cbprintf infrastructure.

[fprintfcb](group__cbprintf__apis.md#ga2636e91fd5d78835cfaffe5b5012638b)

int fprintfcb(FILE \*stream, const char \*format,...)

fprintf using Zephyrs cbprintf infrastructure.

[vsnprintfcb](group__cbprintf__apis.md#ga37b0f96a7b9c025659a902e8fd614b33)

int vsnprintfcb(char \*str, size\_t size, const char \*format, va\_list ap)

vsnprintf using Zephyrs cbprintf infrastructure.

[CBPRINTF\_PACKAGE\_ALIGNMENT](group__cbprintf__apis.md#ga3b917fb81bb246a0910066e2708dbd78)

#define CBPRINTF\_PACKAGE\_ALIGNMENT

Required alignment of the buffer used for packaging.

**Definition** cbprintf.h:140

[cbprintf\_package\_convert](group__cbprintf__apis.md#ga3d7895fa3997bfd4ecf9cb3711c9bf3f)

int cbprintf\_package\_convert(void \*in\_packaged, size\_t in\_len, cbprintf\_convert\_cb cb, void \*ctx, uint32\_t flags, uint16\_t \*strl, size\_t strl\_len)

Convert a package.

[cbprintf\_fsc\_package](group__cbprintf__apis.md#ga66fcefde504d543eb9114bc2fff230d2)

static int cbprintf\_fsc\_package(void \*in\_packaged, size\_t in\_len, void \*packaged, size\_t len)

Convert package to fully self-contained (fsc) package.

**Definition** cbprintf.h:620

[cbprintf\_convert\_cb](group__cbprintf__apis.md#ga6e31a5fb5cd760fbb8d0ff5fd5cc3991)

int(\* cbprintf\_convert\_cb)(const void \*buf, size\_t len, void \*ctx)

Signature for a cbprintf multibyte callback function.

**Definition** cbprintf.h:313

[cbprintf\_package\_copy](group__cbprintf__apis.md#ga881520f4756c1a00270b3b3d12d6fc32)

static int cbprintf\_package\_copy(void \*in\_packaged, size\_t in\_len, void \*packaged, size\_t len, uint32\_t flags, uint16\_t \*strl, size\_t strl\_len)

Copy package with optional appending of strings.

**Definition** cbprintf.h:572

[cbvprintf](group__cbprintf__apis.md#ga8958868def2ba1675ebc8b3a70ff86f8)

static int cbvprintf(cbprintf\_cb out, void \*ctx, const char \*format, va\_list ap)

varargs-aware \*printf-like output through a callback.

**Definition** cbprintf.h:744

[snprintfcb](group__cbprintf__apis.md#ga909f859afbc2a596cd0174f711a60047)

int snprintfcb(char \*str, size\_t size, const char \*format,...)

snprintf using Zephyrs cbprintf infrastructure.

[cbpprintf\_external](group__cbprintf__apis.md#gaa1a040db7e5171dd80d84cd871dfc687)

int cbpprintf\_external(cbprintf\_cb out, cbvprintf\_external\_formatter\_func formatter, void \*ctx, void \*packaged)

Generate the output for a previously captured format operation using an external formatter.

[vprintfcb](group__cbprintf__apis.md#gaa70a1b73fb04b88b40c1fa5fd65efd15)

int vprintfcb(const char \*format, va\_list ap)

vprintf using Zephyrs cbprintf infrastructure.

[cbvprintf\_package](group__cbprintf__apis.md#gaa83f17925daa9747d329b6f1078ab15a)

int cbvprintf\_package(void \*packaged, size\_t len, uint32\_t flags, const char \*format, va\_list ap)

Capture state required to output formatted data later.

[cbprintf\_cb](group__cbprintf__apis.md#gaca8362dda031a176d96855a604395a83)

int(\* cbprintf\_cb)()

Signature for a cbprintf callback function.

**Definition** cbprintf.h:302

[cbprintf\_package](group__cbprintf__apis.md#gad9c56f0a84f60cc53fa9e687069a8f1b)

int cbprintf\_package(void \*packaged, size\_t len, uint32\_t flags, const char \*format,...)

Capture state required to output formatted data later.

[cbvprintf\_tagged\_args](group__cbprintf__apis.md#gae4d5066fff73bb38250f4dc82c43ebdc)

static int cbvprintf\_tagged\_args(cbprintf\_cb out, void \*ctx, const char \*format, va\_list ap)

varargs-aware \*printf-like output through a callback with tagged arguments.

**Definition** cbprintf.h:778

[ENOSPC](group__system__errno.md#ga088abe8bad2df798edad3053d719b937)

#define ENOSPC

No space left on device.

**Definition** errno.h:67

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[stdio.h](stdio_8h.md)

[FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7)

int FILE

**Definition** stdio.h:22

[string.h](string_8h.md)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[cbprintf\_package\_desc](structcbprintf__package__desc.md)

cbprintf package descriptor.

**Definition** cbprintf.h:45

[cbprintf\_package\_desc::len](structcbprintf__package__desc.md#a02876d066dd9ac4ba5bd3bdc19ff7681)

uint8\_t len

Package length (in 32 bit words).

**Definition** cbprintf.h:47

[cbprintf\_package\_desc::str\_cnt](structcbprintf__package__desc.md#a3614347546912dae53d8f9633299912d)

uint8\_t str\_cnt

Number of appended strings in the package.

**Definition** cbprintf.h:50

[cbprintf\_package\_desc::ro\_str\_cnt](structcbprintf__package__desc.md#ad9878876ae963e93850dcfd8d5df7b2f)

uint8\_t ro\_str\_cnt

Number of read-only strings, indexes appended to the package.

**Definition** cbprintf.h:53

[cbprintf\_package\_desc::rw\_str\_cnt](structcbprintf__package__desc.md#ae9695a5e1a4fb70e3be5e9ab63c89937)

uint8\_t rw\_str\_cnt

Number of read-write strings, indexes appended to the package.

**Definition** cbprintf.h:56

[cbprintf\_package\_hdr\_ext](structcbprintf__package__hdr__ext.md)

cbprintf package header with format string pointer.

**Definition** cbprintf.h:96

[cbprintf\_package\_hdr\_ext::hdr](structcbprintf__package__hdr__ext.md#a3f1d9bc9ee58367a8e0a4ce29c73a0f5)

union cbprintf\_package\_hdr hdr

Header of package.

**Definition** cbprintf.h:98

[cbprintf\_package\_hdr\_ext::fmt](structcbprintf__package__hdr__ext.md#af726d9f674740030ccf5f7e13a9b0aa9)

char \* fmt

Pointer to format string.

**Definition** cbprintf.h:101

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[cbprintf\_package\_hdr](unioncbprintf__package__hdr.md)

cbprintf package header

**Definition** cbprintf.h:78

[cbprintf\_package\_hdr::raw](unioncbprintf__package__hdr.md#a5370d9447cf6266178e06e8f6967ba29)

void \* raw

**Definition** cbprintf.h:82

[cbprintf\_package\_hdr::desc](unioncbprintf__package__hdr.md#aa5e4c2d21fde006827031c41e64e0c04)

struct cbprintf\_package\_desc desc

Header description.

**Definition** cbprintf.h:80

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [cbprintf.h](cbprintf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
