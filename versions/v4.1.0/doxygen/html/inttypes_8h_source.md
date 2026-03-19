---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/inttypes_8h_source.html
original_path: doxygen/html/inttypes_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

inttypes.h

[Go to the documentation of this file.](inttypes_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_INTTYPES\_H\_

9#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_INTTYPES\_H\_

10

11#include <[stdint.h](stdint_8h.md)>

12

[ 13](inttypes_8h.md#ae53c45f590033ad1f2f517faf3ab2f1b)#define PRId8 "d" /\* int8\_t \*/

[ 14](inttypes_8h.md#a087e50fe0283aacc71d7138d13e91939)#define PRId16 "d" /\* int16\_t \*/

[ 15](inttypes_8h.md#a6d94d1417e1b35c53aee6306590de72b)#define PRId32 "d" /\* int32\_t \*/

[ 16](inttypes_8h.md#ae372e90b62c1e8b51dc5d95bf7f5ba48)#define PRId64 "lld" /\* int64\_t \*/

[ 17](inttypes_8h.md#a943961b7e7e564388dd743593db5bbbb)#define PRIdFAST8 "d" /\* int\_fast8\_t \*/

[ 18](inttypes_8h.md#a58cdfb02574b8c23d964a6e88a268782)#define PRIdFAST16 "d" /\* int\_fast16\_t \*/

[ 19](inttypes_8h.md#aef5a98227a6af5fde95353ed303cfd1e)#define PRIdFAST32 "d" /\* int\_fast32\_t \*/

[ 20](inttypes_8h.md#a9c63f907b68bfa374778aa59b3a360f5)#define PRIdFAST64 "lld" /\* int\_fast64\_t \*/

[ 21](inttypes_8h.md#a404fd01f0b890cb8fac8641aaa704b57)#define PRIdLEAST8 "d" /\* int\_least8\_t \*/

[ 22](inttypes_8h.md#ae90ab00cb4417081dc68e9fd6c0e129a)#define PRIdLEAST16 "d" /\* int\_least16\_t \*/

[ 23](inttypes_8h.md#ad36a6b276bd808d713cc5603ba008c58)#define PRIdLEAST32 "d" /\* int\_least32\_t \*/

[ 24](inttypes_8h.md#a6e7b87b6cb5b8298e0c7471f19d8321f)#define PRIdLEAST64 "lld" /\* int\_least64\_t \*/

[ 25](inttypes_8h.md#a11a8b311e64e0415db0d106fcebf6597)#define PRIdMAX "lld" /\* intmax\_t \*/

[ 26](inttypes_8h.md#a7c8a9ccd40bd2053ca588d1b15e76a30)#define PRIdPTR "ld" /\* intptr\_t \*/

27

[ 28](inttypes_8h.md#adbe02b78cca747b2fe1a8f7fc5f5cd47)#define PRIi8 "i" /\* int8\_t \*/

[ 29](inttypes_8h.md#a655e9b358e0371a4bf5ff21cc08273e3)#define PRIi16 "i" /\* int16\_t \*/

[ 30](inttypes_8h.md#ae212e57631ec729f70e0cc42e51dd91e)#define PRIi32 "i" /\* int32\_t \*/

[ 31](inttypes_8h.md#ab8d0c29be4a0623c3de58011991e86e9)#define PRIi64 "lli" /\* int64\_t \*/

[ 32](inttypes_8h.md#a64fb4e44c3ff09179fc445979b7fdad1)#define PRIiFAST8 "i" /\* int\_fast8\_t \*/

[ 33](inttypes_8h.md#ac273fb2a05215962fbeae76abaaf0131)#define PRIiFAST16 "i" /\* int\_fast16\_t \*/

[ 34](inttypes_8h.md#a192a69a2e6e63ed8393d306b4078d63f)#define PRIiFAST32 "i" /\* int\_fast32\_t \*/

[ 35](inttypes_8h.md#af27d75f27f8038693a36c3dd14a82516)#define PRIiFAST64 "lli" /\* int\_fast64\_t \*/

[ 36](inttypes_8h.md#a526151b1725956030b501d9dd506f2e1)#define PRIiLEAST8 "i" /\* int\_least8\_t \*/

[ 37](inttypes_8h.md#a96945864cb2d1f7de861ccaf639af02e)#define PRIiLEAST16 "i" /\* int\_least16\_t \*/

[ 38](inttypes_8h.md#ad7a1bae7ca12c7b5415fae1b3f258207)#define PRIiLEAST32 "i" /\* int\_least32\_t \*/

[ 39](inttypes_8h.md#a0fb9f5cdca16045cc30b72d9174cdbfb)#define PRIiLEAST64 "lli" /\* int\_least64\_t \*/

[ 40](inttypes_8h.md#a0f30e8063c747a19c86574a1f61c0ad5)#define PRIiMAX "lli" /\* intmax\_t \*/

[ 41](inttypes_8h.md#ac2d52bf83b783f530f02fa2eeabe703a)#define PRIiPTR "li" /\* intptr\_t \*/

42

[ 43](inttypes_8h.md#ad12493b9063f7b2630b90b7f9a7f3301)#define PRIo8 "o" /\* int8\_t \*/

[ 44](inttypes_8h.md#a55494a16151668ea78e0b808ef38c8c1)#define PRIo16 "o" /\* int16\_t \*/

[ 45](inttypes_8h.md#a7276f64276fd7223ca6f4cca0444239a)#define PRIo32 "o" /\* int32\_t \*/

[ 46](inttypes_8h.md#a792491e417d837fc693122428460bcba)#define PRIo64 "llo" /\* int64\_t \*/

[ 47](inttypes_8h.md#a37f93445f1795033c9ba577661da6a91)#define PRIoFAST8 "o" /\* int\_fast8\_t \*/

[ 48](inttypes_8h.md#a3eda49c829de683e701eaed3cbaf0e73)#define PRIoFAST16 "o" /\* int\_fast16\_t \*/

[ 49](inttypes_8h.md#a6ac7e3111d008785ddf3b29dcd088732)#define PRIoFAST32 "o" /\* int\_fast32\_t \*/

[ 50](inttypes_8h.md#aba7ffd10c01ee7e1264300568ade319e)#define PRIoFAST64 "llo" /\* int\_fast64\_t \*/

[ 51](inttypes_8h.md#aa5b3ca8091f4ed7d43f5eb971ce11114)#define PRIoLEAST8 "o" /\* int\_least8\_t \*/

[ 52](inttypes_8h.md#a1ecbd31333b358c22423a541fffbd122)#define PRIoLEAST16 "o" /\* int\_least16\_t \*/

[ 53](inttypes_8h.md#a1e5c50a1ca71da7ff8c4f3f007411be8)#define PRIoLEAST32 "o" /\* int\_least32\_t \*/

[ 54](inttypes_8h.md#a9540a0a3ff33b4f6a0feee15f3066984)#define PRIoLEAST64 "llo" /\* int\_least64\_t \*/

[ 55](inttypes_8h.md#a73ec9b744a867844fb1cbf5d600e15da)#define PRIoMAX "llo" /\* intmax\_t \*/

[ 56](inttypes_8h.md#a1468793ce960b477922ef92b36a6c802)#define PRIoPTR "lo" /\* intptr\_t \*/

57

[ 58](inttypes_8h.md#a8673208d2d48018fcce020ef59f8ec4f)#define PRIu8 "u" /\* uint8\_t \*/

[ 59](inttypes_8h.md#a86bc00ee87e8e40787e0681fc34c576a)#define PRIu16 "u" /\* uint16\_t \*/

[ 60](inttypes_8h.md#aaf2af4a10f0bd308e9c349c8382382be)#define PRIu32 "u" /\* uint32\_t \*/

[ 61](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5)#define PRIu64 "llu" /\* uint64\_t \*/

[ 62](inttypes_8h.md#a0b0c7ad693c391e3e353e8f2d1df2ec3)#define PRIuFAST8 "u" /\* uint\_fast8\_t \*/

[ 63](inttypes_8h.md#aa82e218a186691ebf7149b36746c12e7)#define PRIuFAST16 "u" /\* uint\_fast16\_t \*/

[ 64](inttypes_8h.md#accc383115328197264988682edfcb72c)#define PRIuFAST32 "u" /\* uint\_fast32\_t \*/

[ 65](inttypes_8h.md#ac1fdefbae4d6c8dcef5b91ef5b778a1c)#define PRIuFAST64 "llu" /\* uint\_fast64\_t \*/

[ 66](inttypes_8h.md#a74cb15b101649124009c010a9055e885)#define PRIuLEAST8 "u" /\* uint\_least8\_t \*/

[ 67](inttypes_8h.md#aa3ba696eef7c107c76c26eea76dcb4b4)#define PRIuLEAST16 "u" /\* uint\_least16\_t \*/

[ 68](inttypes_8h.md#aab353a2898377162c1829f1a9708352e)#define PRIuLEAST32 "u" /\* uint\_least32\_t \*/

[ 69](inttypes_8h.md#a20b768c89c8693bdc3df5f2e76fe018c)#define PRIuLEAST64 "llu" /\* uint\_least64\_t \*/

[ 70](inttypes_8h.md#a5231235fbdc84d556db88609b469982b)#define PRIuMAX "llu" /\* uintmax\_t \*/

[ 71](inttypes_8h.md#aa1ca3a85113e897b5cf7ed6b92d74de2)#define PRIuPTR "lu" /\* uintptr\_t \*/

72

[ 73](inttypes_8h.md#adac1acc1d24060aeee7791a99d1a3a8c)#define PRIx8 "x" /\* uint8\_t \*/

[ 74](inttypes_8h.md#a70f5e38b517f714518c970a4da37bef1)#define PRIx16 "x" /\* uint16\_t \*/

[ 75](inttypes_8h.md#a80ca66bcc9e366733f02c90ed4b0838c)#define PRIx32 "x" /\* uint32\_t \*/

[ 76](inttypes_8h.md#aba38357387a474f439428dee1984fc5a)#define PRIx64 "llx" /\* uint64\_t \*/

[ 77](inttypes_8h.md#ae7e1780719eb0e4b2826a0da06255780)#define PRIxFAST8 "x" /\* uint\_fast8\_t \*/

[ 78](inttypes_8h.md#a6f66e34285ab57a86aeb2f0f4895417d)#define PRIxFAST16 "x" /\* uint\_fast16\_t \*/

[ 79](inttypes_8h.md#a22caa684d44725e1e6e638983380f68e)#define PRIxFAST32 "x" /\* uint\_fast32\_t \*/

[ 80](inttypes_8h.md#a73fe58317ae146f316ddb0736d9ed9a4)#define PRIxFAST64 "llx" /\* uint\_fast64\_t \*/

[ 81](inttypes_8h.md#a45d80a42b6cd25f3ed57b0e800e6e398)#define PRIxLEAST8 "x" /\* uint\_least8\_t \*/

[ 82](inttypes_8h.md#ad00e2a12b813425800cad731f61497ae)#define PRIxLEAST16 "x" /\* uint\_least16\_t \*/

[ 83](inttypes_8h.md#a1d766603a3524c9e03effbbece9c2118)#define PRIxLEAST32 "x" /\* uint\_least32\_t \*/

[ 84](inttypes_8h.md#a4df46377b2a3292ce6c7fd6724a045ab)#define PRIxLEAST64 "llx" /\* uint\_least64\_t \*/

[ 85](inttypes_8h.md#a1cb5f16ab28d09fa5fe07068bb8e2cea)#define PRIxMAX "llx" /\* uintmax\_t \*/

[ 86](inttypes_8h.md#a9c3c25e6145e629e4c9fabddc6061c30)#define PRIxPTR "lx" /\* uintptr\_t \*/

87

[ 88](inttypes_8h.md#a4e9b835c85ffa875e8304e2b852b4c86)#define PRIX8 "X" /\* uint8\_t \*/

[ 89](inttypes_8h.md#a570ca9af5087023f75fc8a1a602d26ab)#define PRIX16 "X" /\* uint16\_t \*/

[ 90](inttypes_8h.md#a32b0c8a04aae5d4454d15e6cbe109f64)#define PRIX32 "X" /\* uint32\_t \*/

[ 91](inttypes_8h.md#af56fc48030ace2ec83125c0f5f42816c)#define PRIX64 "llX" /\* uint64\_t \*/

[ 92](inttypes_8h.md#ab153efc9e6547ca56f42de767cde2595)#define PRIXFAST8 "X" /\* uint\_fast8\_t \*/

[ 93](inttypes_8h.md#a785eabe6337a2fa85874ae99300abb66)#define PRIXFAST16 "X" /\* uint\_fast16\_t \*/

[ 94](inttypes_8h.md#ace7057a6fa96ac7e2a05946ee96cf2d9)#define PRIXFAST32 "X" /\* uint\_fast32\_t \*/

[ 95](inttypes_8h.md#ab94e8153da1da9e2762277c6b1cf21d7)#define PRIXFAST64 "llX" /\* uint\_fast64\_t \*/

[ 96](inttypes_8h.md#a70aa3faf72084587fb18d03aa033a212)#define PRIXLEAST8 "X" /\* uint\_least8\_t \*/

[ 97](inttypes_8h.md#afa4303b077ae4c6c58686178e4b90d18)#define PRIXLEAST16 "X" /\* uint\_least16\_t \*/

[ 98](inttypes_8h.md#aaf100a10f9cd73d46294fd0e8db5246d)#define PRIXLEAST32 "X" /\* uint\_least32\_t \*/

[ 99](inttypes_8h.md#a4d1806a4ea59b88a7bd00d88b7e1747d)#define PRIXLEAST64 "llX" /\* uint\_least64\_t \*/

[ 100](inttypes_8h.md#aa7e1f0c8df36d801c81f6db762ec67ec)#define PRIXMAX "llX" /\* uintmax\_t \*/

[ 101](inttypes_8h.md#a65d9856517198cfc21558c0d6df64207)#define PRIXPTR "lX" /\* uintptr\_t \*/

102

103#endif

[stdint.h](stdint_8h.md)

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [inttypes.h](inttypes_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
