---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/inttypes_8h.html
original_path: doxygen/html/inttypes_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

inttypes.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](inttypes_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PRId8](#ae53c45f590033ad1f2f517faf3ab2f1b)   "d" /\* [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*/ |
| #define | [PRId16](#a087e50fe0283aacc71d7138d13e91939)   "d" /\* [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*/ |
| #define | [PRId32](#a6d94d1417e1b35c53aee6306590de72b)   "d" /\* [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*/ |
| #define | [PRId64](#ae372e90b62c1e8b51dc5d95bf7f5ba48)   "lld" /\* [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*/ |
| #define | [PRIdFAST8](#a943961b7e7e564388dd743593db5bbbb)   "d" /\* [int\_fast8\_t](stdint_8h.md#a98f573ff8187ff09c9594a3f2af7be0d) \*/ |
| #define | [PRIdFAST16](#a58cdfb02574b8c23d964a6e88a268782)   "d" /\* [int\_fast16\_t](stdint_8h.md#a888269be199d49b7f40006aaafa5a350) \*/ |
| #define | [PRIdFAST32](#aef5a98227a6af5fde95353ed303cfd1e)   "d" /\* [int\_fast32\_t](stdint_8h.md#a530ba8ffc89f6393d2d0e2fb2db38b54) \*/ |
| #define | [PRIdFAST64](#a9c63f907b68bfa374778aa59b3a360f5)   "lld" /\* [int\_fast64\_t](stdint_8h.md#abcdb0a9f6e7d139ad4f521ab8f4efdc0) \*/ |
| #define | [PRIdLEAST8](#a404fd01f0b890cb8fac8641aaa704b57)   "d" /\* [int\_least8\_t](stdint_8h.md#adb5f4bf8afa3bee9e4da1bb9daf4908d) \*/ |
| #define | [PRIdLEAST16](#ae90ab00cb4417081dc68e9fd6c0e129a)   "d" /\* [int\_least16\_t](stdint_8h.md#a3a4bc1e426626e17f6a6e0f64decec56) \*/ |
| #define | [PRIdLEAST32](#ad36a6b276bd808d713cc5603ba008c58)   "d" /\* [int\_least32\_t](stdint_8h.md#a4462f62ae74ff8172526401354d2fc9b) \*/ |
| #define | [PRIdLEAST64](#a6e7b87b6cb5b8298e0c7471f19d8321f)   "lld" /\* [int\_least64\_t](stdint_8h.md#a8a5003442318117c64d16d6f32f64f37) \*/ |
| #define | [PRIdMAX](#a11a8b311e64e0415db0d106fcebf6597)   "lld" /\* [intmax\_t](stdint_8h.md#a9d6c1dc12f73927ba41516de04a5fdb8) \*/ |
| #define | [PRIdPTR](#a7c8a9ccd40bd2053ca588d1b15e76a30)   "ld" /\* [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) \*/ |
| #define | [PRIi8](#adbe02b78cca747b2fe1a8f7fc5f5cd47)   "i" /\* [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*/ |
| #define | [PRIi16](#a655e9b358e0371a4bf5ff21cc08273e3)   "i" /\* [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*/ |
| #define | [PRIi32](#ae212e57631ec729f70e0cc42e51dd91e)   "i" /\* [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*/ |
| #define | [PRIi64](#ab8d0c29be4a0623c3de58011991e86e9)   "lli" /\* [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*/ |
| #define | [PRIiFAST8](#a64fb4e44c3ff09179fc445979b7fdad1)   "i" /\* [int\_fast8\_t](stdint_8h.md#a98f573ff8187ff09c9594a3f2af7be0d) \*/ |
| #define | [PRIiFAST16](#ac273fb2a05215962fbeae76abaaf0131)   "i" /\* [int\_fast16\_t](stdint_8h.md#a888269be199d49b7f40006aaafa5a350) \*/ |
| #define | [PRIiFAST32](#a192a69a2e6e63ed8393d306b4078d63f)   "i" /\* [int\_fast32\_t](stdint_8h.md#a530ba8ffc89f6393d2d0e2fb2db38b54) \*/ |
| #define | [PRIiFAST64](#af27d75f27f8038693a36c3dd14a82516)   "lli" /\* [int\_fast64\_t](stdint_8h.md#abcdb0a9f6e7d139ad4f521ab8f4efdc0) \*/ |
| #define | [PRIiLEAST8](#a526151b1725956030b501d9dd506f2e1)   "i" /\* [int\_least8\_t](stdint_8h.md#adb5f4bf8afa3bee9e4da1bb9daf4908d) \*/ |
| #define | [PRIiLEAST16](#a96945864cb2d1f7de861ccaf639af02e)   "i" /\* [int\_least16\_t](stdint_8h.md#a3a4bc1e426626e17f6a6e0f64decec56) \*/ |
| #define | [PRIiLEAST32](#ad7a1bae7ca12c7b5415fae1b3f258207)   "i" /\* [int\_least32\_t](stdint_8h.md#a4462f62ae74ff8172526401354d2fc9b) \*/ |
| #define | [PRIiLEAST64](#a0fb9f5cdca16045cc30b72d9174cdbfb)   "lli" /\* [int\_least64\_t](stdint_8h.md#a8a5003442318117c64d16d6f32f64f37) \*/ |
| #define | [PRIiMAX](#a0f30e8063c747a19c86574a1f61c0ad5)   "lli" /\* [intmax\_t](stdint_8h.md#a9d6c1dc12f73927ba41516de04a5fdb8) \*/ |
| #define | [PRIiPTR](#ac2d52bf83b783f530f02fa2eeabe703a)   "li" /\* [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) \*/ |
| #define | [PRIo8](#ad12493b9063f7b2630b90b7f9a7f3301)   "o" /\* [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*/ |
| #define | [PRIo16](#a55494a16151668ea78e0b808ef38c8c1)   "o" /\* [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*/ |
| #define | [PRIo32](#a7276f64276fd7223ca6f4cca0444239a)   "o" /\* [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*/ |
| #define | [PRIo64](#a792491e417d837fc693122428460bcba)   "llo" /\* [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*/ |
| #define | [PRIoFAST8](#a37f93445f1795033c9ba577661da6a91)   "o" /\* [int\_fast8\_t](stdint_8h.md#a98f573ff8187ff09c9594a3f2af7be0d) \*/ |
| #define | [PRIoFAST16](#a3eda49c829de683e701eaed3cbaf0e73)   "o" /\* [int\_fast16\_t](stdint_8h.md#a888269be199d49b7f40006aaafa5a350) \*/ |
| #define | [PRIoFAST32](#a6ac7e3111d008785ddf3b29dcd088732)   "o" /\* [int\_fast32\_t](stdint_8h.md#a530ba8ffc89f6393d2d0e2fb2db38b54) \*/ |
| #define | [PRIoFAST64](#aba7ffd10c01ee7e1264300568ade319e)   "llo" /\* [int\_fast64\_t](stdint_8h.md#abcdb0a9f6e7d139ad4f521ab8f4efdc0) \*/ |
| #define | [PRIoLEAST8](#aa5b3ca8091f4ed7d43f5eb971ce11114)   "o" /\* [int\_least8\_t](stdint_8h.md#adb5f4bf8afa3bee9e4da1bb9daf4908d) \*/ |
| #define | [PRIoLEAST16](#a1ecbd31333b358c22423a541fffbd122)   "o" /\* [int\_least16\_t](stdint_8h.md#a3a4bc1e426626e17f6a6e0f64decec56) \*/ |
| #define | [PRIoLEAST32](#a1e5c50a1ca71da7ff8c4f3f007411be8)   "o" /\* [int\_least32\_t](stdint_8h.md#a4462f62ae74ff8172526401354d2fc9b) \*/ |
| #define | [PRIoLEAST64](#a9540a0a3ff33b4f6a0feee15f3066984)   "llo" /\* [int\_least64\_t](stdint_8h.md#a8a5003442318117c64d16d6f32f64f37) \*/ |
| #define | [PRIoMAX](#a73ec9b744a867844fb1cbf5d600e15da)   "llo" /\* [intmax\_t](stdint_8h.md#a9d6c1dc12f73927ba41516de04a5fdb8) \*/ |
| #define | [PRIoPTR](#a1468793ce960b477922ef92b36a6c802)   "lo" /\* [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) \*/ |
| #define | [PRIu8](#a8673208d2d48018fcce020ef59f8ec4f)   "u" /\* [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*/ |
| #define | [PRIu16](#a86bc00ee87e8e40787e0681fc34c576a)   "u" /\* [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*/ |
| #define | [PRIu32](#aaf2af4a10f0bd308e9c349c8382382be)   "u" /\* [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*/ |
| #define | [PRIu64](#ac582131d7a7c8ee57e73180d1714f9d5)   "llu" /\* [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*/ |
| #define | [PRIuFAST8](#a0b0c7ad693c391e3e353e8f2d1df2ec3)   "u" /\* [uint\_fast8\_t](stdint_8h.md#a2464ed69ccd3fd2b3b4c93cb78f6fa20) \*/ |
| #define | [PRIuFAST16](#aa82e218a186691ebf7149b36746c12e7)   "u" /\* [uint\_fast16\_t](stdint_8h.md#aaabed6e034edb01c259c003894d7f7c8) \*/ |
| #define | [PRIuFAST32](#accc383115328197264988682edfcb72c)   "u" /\* [uint\_fast32\_t](stdint_8h.md#aa44ff507c3d9a49e27fac64e9fadf062) \*/ |
| #define | [PRIuFAST64](#ac1fdefbae4d6c8dcef5b91ef5b778a1c)   "llu" /\* [uint\_fast64\_t](stdint_8h.md#a62c711f66c6d29c81429aeafdc4bc592) \*/ |
| #define | [PRIuLEAST8](#a74cb15b101649124009c010a9055e885)   "u" /\* [uint\_least8\_t](stdint_8h.md#a61d44370ed65907c324edad5e8d34632) \*/ |
| #define | [PRIuLEAST16](#aa3ba696eef7c107c76c26eea76dcb4b4)   "u" /\* [uint\_least16\_t](stdint_8h.md#a1a01d6a4e68e435471be2ae8db7e8fdc) \*/ |
| #define | [PRIuLEAST32](#aab353a2898377162c1829f1a9708352e)   "u" /\* [uint\_least32\_t](stdint_8h.md#a678494ae5435d8904e7972c94618e774) \*/ |
| #define | [PRIuLEAST64](#a20b768c89c8693bdc3df5f2e76fe018c)   "llu" /\* [uint\_least64\_t](stdint_8h.md#aba0cb5638c172422eb4a7555a143fbbc) \*/ |
| #define | [PRIuMAX](#a5231235fbdc84d556db88609b469982b)   "llu" /\* [uintmax\_t](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40) \*/ |
| #define | [PRIuPTR](#aa1ca3a85113e897b5cf7ed6b92d74de2)   "lu" /\* [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*/ |
| #define | [PRIx8](#adac1acc1d24060aeee7791a99d1a3a8c)   "x" /\* [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*/ |
| #define | [PRIx16](#a70f5e38b517f714518c970a4da37bef1)   "x" /\* [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*/ |
| #define | [PRIx32](#a80ca66bcc9e366733f02c90ed4b0838c)   "x" /\* [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*/ |
| #define | [PRIx64](#aba38357387a474f439428dee1984fc5a)   "llx" /\* [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*/ |
| #define | [PRIxFAST8](#ae7e1780719eb0e4b2826a0da06255780)   "x" /\* [uint\_fast8\_t](stdint_8h.md#a2464ed69ccd3fd2b3b4c93cb78f6fa20) \*/ |
| #define | [PRIxFAST16](#a6f66e34285ab57a86aeb2f0f4895417d)   "x" /\* [uint\_fast16\_t](stdint_8h.md#aaabed6e034edb01c259c003894d7f7c8) \*/ |
| #define | [PRIxFAST32](#a22caa684d44725e1e6e638983380f68e)   "x" /\* [uint\_fast32\_t](stdint_8h.md#aa44ff507c3d9a49e27fac64e9fadf062) \*/ |
| #define | [PRIxFAST64](#a73fe58317ae146f316ddb0736d9ed9a4)   "llx" /\* [uint\_fast64\_t](stdint_8h.md#a62c711f66c6d29c81429aeafdc4bc592) \*/ |
| #define | [PRIxLEAST8](#a45d80a42b6cd25f3ed57b0e800e6e398)   "x" /\* [uint\_least8\_t](stdint_8h.md#a61d44370ed65907c324edad5e8d34632) \*/ |
| #define | [PRIxLEAST16](#ad00e2a12b813425800cad731f61497ae)   "x" /\* [uint\_least16\_t](stdint_8h.md#a1a01d6a4e68e435471be2ae8db7e8fdc) \*/ |
| #define | [PRIxLEAST32](#a1d766603a3524c9e03effbbece9c2118)   "x" /\* [uint\_least32\_t](stdint_8h.md#a678494ae5435d8904e7972c94618e774) \*/ |
| #define | [PRIxLEAST64](#a4df46377b2a3292ce6c7fd6724a045ab)   "llx" /\* [uint\_least64\_t](stdint_8h.md#aba0cb5638c172422eb4a7555a143fbbc) \*/ |
| #define | [PRIxMAX](#a1cb5f16ab28d09fa5fe07068bb8e2cea)   "llx" /\* [uintmax\_t](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40) \*/ |
| #define | [PRIxPTR](#a9c3c25e6145e629e4c9fabddc6061c30)   "lx" /\* [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*/ |
| #define | [PRIX8](#a4e9b835c85ffa875e8304e2b852b4c86)   "X" /\* [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*/ |
| #define | [PRIX16](#a570ca9af5087023f75fc8a1a602d26ab)   "X" /\* [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*/ |
| #define | [PRIX32](#a32b0c8a04aae5d4454d15e6cbe109f64)   "X" /\* [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*/ |
| #define | [PRIX64](#af56fc48030ace2ec83125c0f5f42816c)   "llX" /\* [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*/ |
| #define | [PRIXFAST8](#ab153efc9e6547ca56f42de767cde2595)   "X" /\* [uint\_fast8\_t](stdint_8h.md#a2464ed69ccd3fd2b3b4c93cb78f6fa20) \*/ |
| #define | [PRIXFAST16](#a785eabe6337a2fa85874ae99300abb66)   "X" /\* [uint\_fast16\_t](stdint_8h.md#aaabed6e034edb01c259c003894d7f7c8) \*/ |
| #define | [PRIXFAST32](#ace7057a6fa96ac7e2a05946ee96cf2d9)   "X" /\* [uint\_fast32\_t](stdint_8h.md#aa44ff507c3d9a49e27fac64e9fadf062) \*/ |
| #define | [PRIXFAST64](#ab94e8153da1da9e2762277c6b1cf21d7)   "llX" /\* [uint\_fast64\_t](stdint_8h.md#a62c711f66c6d29c81429aeafdc4bc592) \*/ |
| #define | [PRIXLEAST8](#a70aa3faf72084587fb18d03aa033a212)   "X" /\* [uint\_least8\_t](stdint_8h.md#a61d44370ed65907c324edad5e8d34632) \*/ |
| #define | [PRIXLEAST16](#afa4303b077ae4c6c58686178e4b90d18)   "X" /\* [uint\_least16\_t](stdint_8h.md#a1a01d6a4e68e435471be2ae8db7e8fdc) \*/ |
| #define | [PRIXLEAST32](#aaf100a10f9cd73d46294fd0e8db5246d)   "X" /\* [uint\_least32\_t](stdint_8h.md#a678494ae5435d8904e7972c94618e774) \*/ |
| #define | [PRIXLEAST64](#a4d1806a4ea59b88a7bd00d88b7e1747d)   "llX" /\* [uint\_least64\_t](stdint_8h.md#aba0cb5638c172422eb4a7555a143fbbc) \*/ |
| #define | [PRIXMAX](#aa7e1f0c8df36d801c81f6db762ec67ec)   "llX" /\* [uintmax\_t](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40) \*/ |
| #define | [PRIXPTR](#a65d9856517198cfc21558c0d6df64207)   "lX" /\* [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*/ |

## Macro Definition Documentation

## [◆ ](#a087e50fe0283aacc71d7138d13e91939)PRId16

| #define PRId16   "d" /\* [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*/ |
| --- |

## [◆ ](#a6d94d1417e1b35c53aee6306590de72b)PRId32

| #define PRId32   "d" /\* [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*/ |
| --- |

## [◆ ](#ae372e90b62c1e8b51dc5d95bf7f5ba48)PRId64

| #define PRId64   "lld" /\* [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*/ |
| --- |

## [◆ ](#ae53c45f590033ad1f2f517faf3ab2f1b)PRId8

| #define PRId8   "d" /\* [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*/ |
| --- |

## [◆ ](#a58cdfb02574b8c23d964a6e88a268782)PRIdFAST16

| #define PRIdFAST16   "d" /\* [int\_fast16\_t](stdint_8h.md#a888269be199d49b7f40006aaafa5a350) \*/ |
| --- |

## [◆ ](#aef5a98227a6af5fde95353ed303cfd1e)PRIdFAST32

| #define PRIdFAST32   "d" /\* [int\_fast32\_t](stdint_8h.md#a530ba8ffc89f6393d2d0e2fb2db38b54) \*/ |
| --- |

## [◆ ](#a9c63f907b68bfa374778aa59b3a360f5)PRIdFAST64

| #define PRIdFAST64   "lld" /\* [int\_fast64\_t](stdint_8h.md#abcdb0a9f6e7d139ad4f521ab8f4efdc0) \*/ |
| --- |

## [◆ ](#a943961b7e7e564388dd743593db5bbbb)PRIdFAST8

| #define PRIdFAST8   "d" /\* [int\_fast8\_t](stdint_8h.md#a98f573ff8187ff09c9594a3f2af7be0d) \*/ |
| --- |

## [◆ ](#ae90ab00cb4417081dc68e9fd6c0e129a)PRIdLEAST16

| #define PRIdLEAST16   "d" /\* [int\_least16\_t](stdint_8h.md#a3a4bc1e426626e17f6a6e0f64decec56) \*/ |
| --- |

## [◆ ](#ad36a6b276bd808d713cc5603ba008c58)PRIdLEAST32

| #define PRIdLEAST32   "d" /\* [int\_least32\_t](stdint_8h.md#a4462f62ae74ff8172526401354d2fc9b) \*/ |
| --- |

## [◆ ](#a6e7b87b6cb5b8298e0c7471f19d8321f)PRIdLEAST64

| #define PRIdLEAST64   "lld" /\* [int\_least64\_t](stdint_8h.md#a8a5003442318117c64d16d6f32f64f37) \*/ |
| --- |

## [◆ ](#a404fd01f0b890cb8fac8641aaa704b57)PRIdLEAST8

| #define PRIdLEAST8   "d" /\* [int\_least8\_t](stdint_8h.md#adb5f4bf8afa3bee9e4da1bb9daf4908d) \*/ |
| --- |

## [◆ ](#a11a8b311e64e0415db0d106fcebf6597)PRIdMAX

| #define PRIdMAX   "lld" /\* [intmax\_t](stdint_8h.md#a9d6c1dc12f73927ba41516de04a5fdb8) \*/ |
| --- |

## [◆ ](#a7c8a9ccd40bd2053ca588d1b15e76a30)PRIdPTR

| #define PRIdPTR   "ld" /\* [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) \*/ |
| --- |

## [◆ ](#a655e9b358e0371a4bf5ff21cc08273e3)PRIi16

| #define PRIi16   "i" /\* [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*/ |
| --- |

## [◆ ](#ae212e57631ec729f70e0cc42e51dd91e)PRIi32

| #define PRIi32   "i" /\* [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*/ |
| --- |

## [◆ ](#ab8d0c29be4a0623c3de58011991e86e9)PRIi64

| #define PRIi64   "lli" /\* [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*/ |
| --- |

## [◆ ](#adbe02b78cca747b2fe1a8f7fc5f5cd47)PRIi8

| #define PRIi8   "i" /\* [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*/ |
| --- |

## [◆ ](#ac273fb2a05215962fbeae76abaaf0131)PRIiFAST16

| #define PRIiFAST16   "i" /\* [int\_fast16\_t](stdint_8h.md#a888269be199d49b7f40006aaafa5a350) \*/ |
| --- |

## [◆ ](#a192a69a2e6e63ed8393d306b4078d63f)PRIiFAST32

| #define PRIiFAST32   "i" /\* [int\_fast32\_t](stdint_8h.md#a530ba8ffc89f6393d2d0e2fb2db38b54) \*/ |
| --- |

## [◆ ](#af27d75f27f8038693a36c3dd14a82516)PRIiFAST64

| #define PRIiFAST64   "lli" /\* [int\_fast64\_t](stdint_8h.md#abcdb0a9f6e7d139ad4f521ab8f4efdc0) \*/ |
| --- |

## [◆ ](#a64fb4e44c3ff09179fc445979b7fdad1)PRIiFAST8

| #define PRIiFAST8   "i" /\* [int\_fast8\_t](stdint_8h.md#a98f573ff8187ff09c9594a3f2af7be0d) \*/ |
| --- |

## [◆ ](#a96945864cb2d1f7de861ccaf639af02e)PRIiLEAST16

| #define PRIiLEAST16   "i" /\* [int\_least16\_t](stdint_8h.md#a3a4bc1e426626e17f6a6e0f64decec56) \*/ |
| --- |

## [◆ ](#ad7a1bae7ca12c7b5415fae1b3f258207)PRIiLEAST32

| #define PRIiLEAST32   "i" /\* [int\_least32\_t](stdint_8h.md#a4462f62ae74ff8172526401354d2fc9b) \*/ |
| --- |

## [◆ ](#a0fb9f5cdca16045cc30b72d9174cdbfb)PRIiLEAST64

| #define PRIiLEAST64   "lli" /\* [int\_least64\_t](stdint_8h.md#a8a5003442318117c64d16d6f32f64f37) \*/ |
| --- |

## [◆ ](#a526151b1725956030b501d9dd506f2e1)PRIiLEAST8

| #define PRIiLEAST8   "i" /\* [int\_least8\_t](stdint_8h.md#adb5f4bf8afa3bee9e4da1bb9daf4908d) \*/ |
| --- |

## [◆ ](#a0f30e8063c747a19c86574a1f61c0ad5)PRIiMAX

| #define PRIiMAX   "lli" /\* [intmax\_t](stdint_8h.md#a9d6c1dc12f73927ba41516de04a5fdb8) \*/ |
| --- |

## [◆ ](#ac2d52bf83b783f530f02fa2eeabe703a)PRIiPTR

| #define PRIiPTR   "li" /\* [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) \*/ |
| --- |

## [◆ ](#a55494a16151668ea78e0b808ef38c8c1)PRIo16

| #define PRIo16   "o" /\* [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*/ |
| --- |

## [◆ ](#a7276f64276fd7223ca6f4cca0444239a)PRIo32

| #define PRIo32   "o" /\* [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*/ |
| --- |

## [◆ ](#a792491e417d837fc693122428460bcba)PRIo64

| #define PRIo64   "llo" /\* [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*/ |
| --- |

## [◆ ](#ad12493b9063f7b2630b90b7f9a7f3301)PRIo8

| #define PRIo8   "o" /\* [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*/ |
| --- |

## [◆ ](#a3eda49c829de683e701eaed3cbaf0e73)PRIoFAST16

| #define PRIoFAST16   "o" /\* [int\_fast16\_t](stdint_8h.md#a888269be199d49b7f40006aaafa5a350) \*/ |
| --- |

## [◆ ](#a6ac7e3111d008785ddf3b29dcd088732)PRIoFAST32

| #define PRIoFAST32   "o" /\* [int\_fast32\_t](stdint_8h.md#a530ba8ffc89f6393d2d0e2fb2db38b54) \*/ |
| --- |

## [◆ ](#aba7ffd10c01ee7e1264300568ade319e)PRIoFAST64

| #define PRIoFAST64   "llo" /\* [int\_fast64\_t](stdint_8h.md#abcdb0a9f6e7d139ad4f521ab8f4efdc0) \*/ |
| --- |

## [◆ ](#a37f93445f1795033c9ba577661da6a91)PRIoFAST8

| #define PRIoFAST8   "o" /\* [int\_fast8\_t](stdint_8h.md#a98f573ff8187ff09c9594a3f2af7be0d) \*/ |
| --- |

## [◆ ](#a1ecbd31333b358c22423a541fffbd122)PRIoLEAST16

| #define PRIoLEAST16   "o" /\* [int\_least16\_t](stdint_8h.md#a3a4bc1e426626e17f6a6e0f64decec56) \*/ |
| --- |

## [◆ ](#a1e5c50a1ca71da7ff8c4f3f007411be8)PRIoLEAST32

| #define PRIoLEAST32   "o" /\* [int\_least32\_t](stdint_8h.md#a4462f62ae74ff8172526401354d2fc9b) \*/ |
| --- |

## [◆ ](#a9540a0a3ff33b4f6a0feee15f3066984)PRIoLEAST64

| #define PRIoLEAST64   "llo" /\* [int\_least64\_t](stdint_8h.md#a8a5003442318117c64d16d6f32f64f37) \*/ |
| --- |

## [◆ ](#aa5b3ca8091f4ed7d43f5eb971ce11114)PRIoLEAST8

| #define PRIoLEAST8   "o" /\* [int\_least8\_t](stdint_8h.md#adb5f4bf8afa3bee9e4da1bb9daf4908d) \*/ |
| --- |

## [◆ ](#a73ec9b744a867844fb1cbf5d600e15da)PRIoMAX

| #define PRIoMAX   "llo" /\* [intmax\_t](stdint_8h.md#a9d6c1dc12f73927ba41516de04a5fdb8) \*/ |
| --- |

## [◆ ](#a1468793ce960b477922ef92b36a6c802)PRIoPTR

| #define PRIoPTR   "lo" /\* [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) \*/ |
| --- |

## [◆ ](#a86bc00ee87e8e40787e0681fc34c576a)PRIu16

| #define PRIu16   "u" /\* [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*/ |
| --- |

## [◆ ](#aaf2af4a10f0bd308e9c349c8382382be)PRIu32

| #define PRIu32   "u" /\* [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*/ |
| --- |

## [◆ ](#ac582131d7a7c8ee57e73180d1714f9d5)PRIu64

| #define PRIu64   "llu" /\* [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*/ |
| --- |

## [◆ ](#a8673208d2d48018fcce020ef59f8ec4f)PRIu8

| #define PRIu8   "u" /\* [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*/ |
| --- |

## [◆ ](#aa82e218a186691ebf7149b36746c12e7)PRIuFAST16

| #define PRIuFAST16   "u" /\* [uint\_fast16\_t](stdint_8h.md#aaabed6e034edb01c259c003894d7f7c8) \*/ |
| --- |

## [◆ ](#accc383115328197264988682edfcb72c)PRIuFAST32

| #define PRIuFAST32   "u" /\* [uint\_fast32\_t](stdint_8h.md#aa44ff507c3d9a49e27fac64e9fadf062) \*/ |
| --- |

## [◆ ](#ac1fdefbae4d6c8dcef5b91ef5b778a1c)PRIuFAST64

| #define PRIuFAST64   "llu" /\* [uint\_fast64\_t](stdint_8h.md#a62c711f66c6d29c81429aeafdc4bc592) \*/ |
| --- |

## [◆ ](#a0b0c7ad693c391e3e353e8f2d1df2ec3)PRIuFAST8

| #define PRIuFAST8   "u" /\* [uint\_fast8\_t](stdint_8h.md#a2464ed69ccd3fd2b3b4c93cb78f6fa20) \*/ |
| --- |

## [◆ ](#aa3ba696eef7c107c76c26eea76dcb4b4)PRIuLEAST16

| #define PRIuLEAST16   "u" /\* [uint\_least16\_t](stdint_8h.md#a1a01d6a4e68e435471be2ae8db7e8fdc) \*/ |
| --- |

## [◆ ](#aab353a2898377162c1829f1a9708352e)PRIuLEAST32

| #define PRIuLEAST32   "u" /\* [uint\_least32\_t](stdint_8h.md#a678494ae5435d8904e7972c94618e774) \*/ |
| --- |

## [◆ ](#a20b768c89c8693bdc3df5f2e76fe018c)PRIuLEAST64

| #define PRIuLEAST64   "llu" /\* [uint\_least64\_t](stdint_8h.md#aba0cb5638c172422eb4a7555a143fbbc) \*/ |
| --- |

## [◆ ](#a74cb15b101649124009c010a9055e885)PRIuLEAST8

| #define PRIuLEAST8   "u" /\* [uint\_least8\_t](stdint_8h.md#a61d44370ed65907c324edad5e8d34632) \*/ |
| --- |

## [◆ ](#a5231235fbdc84d556db88609b469982b)PRIuMAX

| #define PRIuMAX   "llu" /\* [uintmax\_t](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40) \*/ |
| --- |

## [◆ ](#aa1ca3a85113e897b5cf7ed6b92d74de2)PRIuPTR

| #define PRIuPTR   "lu" /\* [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*/ |
| --- |

## [◆ ](#a570ca9af5087023f75fc8a1a602d26ab)PRIX16

| #define PRIX16   "X" /\* [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*/ |
| --- |

## [◆ ](#a70f5e38b517f714518c970a4da37bef1)PRIx16

| #define PRIx16   "x" /\* [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*/ |
| --- |

## [◆ ](#a32b0c8a04aae5d4454d15e6cbe109f64)PRIX32

| #define PRIX32   "X" /\* [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*/ |
| --- |

## [◆ ](#a80ca66bcc9e366733f02c90ed4b0838c)PRIx32

| #define PRIx32   "x" /\* [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*/ |
| --- |

## [◆ ](#af56fc48030ace2ec83125c0f5f42816c)PRIX64

| #define PRIX64   "llX" /\* [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*/ |
| --- |

## [◆ ](#aba38357387a474f439428dee1984fc5a)PRIx64

| #define PRIx64   "llx" /\* [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*/ |
| --- |

## [◆ ](#a4e9b835c85ffa875e8304e2b852b4c86)PRIX8

| #define PRIX8   "X" /\* [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*/ |
| --- |

## [◆ ](#adac1acc1d24060aeee7791a99d1a3a8c)PRIx8

| #define PRIx8   "x" /\* [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*/ |
| --- |

## [◆ ](#a785eabe6337a2fa85874ae99300abb66)PRIXFAST16

| #define PRIXFAST16   "X" /\* [uint\_fast16\_t](stdint_8h.md#aaabed6e034edb01c259c003894d7f7c8) \*/ |
| --- |

## [◆ ](#a6f66e34285ab57a86aeb2f0f4895417d)PRIxFAST16

| #define PRIxFAST16   "x" /\* [uint\_fast16\_t](stdint_8h.md#aaabed6e034edb01c259c003894d7f7c8) \*/ |
| --- |

## [◆ ](#ace7057a6fa96ac7e2a05946ee96cf2d9)PRIXFAST32

| #define PRIXFAST32   "X" /\* [uint\_fast32\_t](stdint_8h.md#aa44ff507c3d9a49e27fac64e9fadf062) \*/ |
| --- |

## [◆ ](#a22caa684d44725e1e6e638983380f68e)PRIxFAST32

| #define PRIxFAST32   "x" /\* [uint\_fast32\_t](stdint_8h.md#aa44ff507c3d9a49e27fac64e9fadf062) \*/ |
| --- |

## [◆ ](#ab94e8153da1da9e2762277c6b1cf21d7)PRIXFAST64

| #define PRIXFAST64   "llX" /\* [uint\_fast64\_t](stdint_8h.md#a62c711f66c6d29c81429aeafdc4bc592) \*/ |
| --- |

## [◆ ](#a73fe58317ae146f316ddb0736d9ed9a4)PRIxFAST64

| #define PRIxFAST64   "llx" /\* [uint\_fast64\_t](stdint_8h.md#a62c711f66c6d29c81429aeafdc4bc592) \*/ |
| --- |

## [◆ ](#ab153efc9e6547ca56f42de767cde2595)PRIXFAST8

| #define PRIXFAST8   "X" /\* [uint\_fast8\_t](stdint_8h.md#a2464ed69ccd3fd2b3b4c93cb78f6fa20) \*/ |
| --- |

## [◆ ](#ae7e1780719eb0e4b2826a0da06255780)PRIxFAST8

| #define PRIxFAST8   "x" /\* [uint\_fast8\_t](stdint_8h.md#a2464ed69ccd3fd2b3b4c93cb78f6fa20) \*/ |
| --- |

## [◆ ](#afa4303b077ae4c6c58686178e4b90d18)PRIXLEAST16

| #define PRIXLEAST16   "X" /\* [uint\_least16\_t](stdint_8h.md#a1a01d6a4e68e435471be2ae8db7e8fdc) \*/ |
| --- |

## [◆ ](#ad00e2a12b813425800cad731f61497ae)PRIxLEAST16

| #define PRIxLEAST16   "x" /\* [uint\_least16\_t](stdint_8h.md#a1a01d6a4e68e435471be2ae8db7e8fdc) \*/ |
| --- |

## [◆ ](#aaf100a10f9cd73d46294fd0e8db5246d)PRIXLEAST32

| #define PRIXLEAST32   "X" /\* [uint\_least32\_t](stdint_8h.md#a678494ae5435d8904e7972c94618e774) \*/ |
| --- |

## [◆ ](#a1d766603a3524c9e03effbbece9c2118)PRIxLEAST32

| #define PRIxLEAST32   "x" /\* [uint\_least32\_t](stdint_8h.md#a678494ae5435d8904e7972c94618e774) \*/ |
| --- |

## [◆ ](#a4d1806a4ea59b88a7bd00d88b7e1747d)PRIXLEAST64

| #define PRIXLEAST64   "llX" /\* [uint\_least64\_t](stdint_8h.md#aba0cb5638c172422eb4a7555a143fbbc) \*/ |
| --- |

## [◆ ](#a4df46377b2a3292ce6c7fd6724a045ab)PRIxLEAST64

| #define PRIxLEAST64   "llx" /\* [uint\_least64\_t](stdint_8h.md#aba0cb5638c172422eb4a7555a143fbbc) \*/ |
| --- |

## [◆ ](#a70aa3faf72084587fb18d03aa033a212)PRIXLEAST8

| #define PRIXLEAST8   "X" /\* [uint\_least8\_t](stdint_8h.md#a61d44370ed65907c324edad5e8d34632) \*/ |
| --- |

## [◆ ](#a45d80a42b6cd25f3ed57b0e800e6e398)PRIxLEAST8

| #define PRIxLEAST8   "x" /\* [uint\_least8\_t](stdint_8h.md#a61d44370ed65907c324edad5e8d34632) \*/ |
| --- |

## [◆ ](#aa7e1f0c8df36d801c81f6db762ec67ec)PRIXMAX

| #define PRIXMAX   "llX" /\* [uintmax\_t](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40) \*/ |
| --- |

## [◆ ](#a1cb5f16ab28d09fa5fe07068bb8e2cea)PRIxMAX

| #define PRIxMAX   "llx" /\* [uintmax\_t](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40) \*/ |
| --- |

## [◆ ](#a65d9856517198cfc21558c0d6df64207)PRIXPTR

| #define PRIXPTR   "lX" /\* [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*/ |
| --- |

## [◆ ](#a9c3c25e6145e629e4c9fabddc6061c30)PRIxPTR

| #define PRIxPTR   "lx" /\* [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*/ |
| --- |

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [inttypes.h](inttypes_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
