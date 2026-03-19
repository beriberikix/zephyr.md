---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stdint_8h.html
original_path: doxygen/html/stdint_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stdint.h File Reference

[Go to the source code of this file.](stdint_8h_source.md)

| Macros | |
| --- | --- |
| #define | [INT8\_MAX](#aaf7f29f45f1a513b4748a4e5014ddf6a)   \_\_INT8\_MAX\_\_ |
| #define | [INT16\_MAX](#ac58f2c111cc9989c86db2a7dc4fd84ca)   \_\_INT16\_MAX\_\_ |
| #define | [INT32\_MAX](#a181807730d4a375f848ba139813ce04f)   \_\_INT32\_MAX\_\_ |
| #define | [INT64\_MAX](#ad0d744f05898e32d01f73f8af3cd2071)   \_\_INT64\_MAX\_\_ |
| #define | [INTMAX\_MAX](#a022b9b0a3564d786244a4631847c37a3)   \_\_INT64\_MAX\_\_ |
| #define | [INT8\_MIN](#aadcf2a81af243df333b31efa6461ab8e)   (-[INT8\_MAX](#aaf7f29f45f1a513b4748a4e5014ddf6a) - 1) |
| #define | [INT16\_MIN](#ad4e9955955b27624963643eac448118a)   (-[INT16\_MAX](#ac58f2c111cc9989c86db2a7dc4fd84ca) - 1) |
| #define | [INT32\_MIN](#a688eb21a22db27c2b2bd5836943cdcbe)   (-[INT32\_MAX](#a181807730d4a375f848ba139813ce04f) - 1) |
| #define | [INT64\_MIN](#ab21f12f372f67b8ff0aa3432336ede67)   (-[INT64\_MAX](#ad0d744f05898e32d01f73f8af3cd2071) - 1LL) |
| #define | [UINT8\_MAX](#aeb4e270a084ee26fe73e799861bd0252)   \_\_UINT8\_MAX\_\_ |
| #define | [UINT16\_MAX](#a3ea490c9b3617d4479bd80ef93cd5602)   \_\_UINT16\_MAX\_\_ |
| #define | [UINT32\_MAX](#ab5eb23180f7cc12b7d6c04a8ec067fdd)   \_\_UINT32\_MAX\_\_ |
| #define | [UINT64\_MAX](#a30654b4b67d97c42ca3f9b6052dda916)   \_\_UINT64\_MAX\_\_ |
| #define | [UINTMAX\_MAX](#aa54fd5210434219e9027bfa0f0e325c8)   \_\_UINT64\_MAX\_\_ |
| #define | [INT\_FAST8\_MAX](#acbcdb3bee0f5f904da5df8de69a80ca3)   \_\_INT\_FAST8\_MAX\_\_ |
| #define | [INT\_FAST16\_MAX](#a2fd35d0ea091e04caec504ff0042cf00)   \_\_INT\_FAST16\_MAX\_\_ |
| #define | [INT\_FAST32\_MAX](#ac96fa0f41b19e89f109e4f9913ca6635)   \_\_INT\_FAST32\_MAX\_\_ |
| #define | [INT\_FAST64\_MAX](#a13c95cf9c209d8daacb36cbf0d5ba275)   \_\_INT\_FAST64\_MAX\_\_ |
| #define | [INT\_FAST8\_MIN](#aad8fb982cb19143efd5ee9a1a7a89390)   (-[INT\_FAST8\_MAX](#acbcdb3bee0f5f904da5df8de69a80ca3) - 1) |
| #define | [INT\_FAST16\_MIN](#a169460a4e2a79138723d68d99372d958)   (-[INT\_FAST16\_MAX](#a2fd35d0ea091e04caec504ff0042cf00) - 1) |
| #define | [INT\_FAST32\_MIN](#ad93df1652ed0635513d5efe4f1219926)   (-[INT\_FAST32\_MAX](#ac96fa0f41b19e89f109e4f9913ca6635) - 1) |
| #define | [INT\_FAST64\_MIN](#a50f0fdcb00ea2500cec0f3d6d45c36f3)   (-[INT\_FAST64\_MAX](#a13c95cf9c209d8daacb36cbf0d5ba275) - 1LL) |
| #define | [UINT\_FAST8\_MAX](#a2c6f97ea2d76d0cf6260c84046cdb44e)   \_\_UINT\_FAST8\_MAX\_\_ |
| #define | [UINT\_FAST16\_MAX](#aed28ca63d9b222f6f1377358fe73a183)   \_\_UINT\_FAST16\_MAX\_\_ |
| #define | [UINT\_FAST32\_MAX](#ad51246a178143208b2db3315efd21c45)   \_\_UINT\_FAST32\_MAX\_\_ |
| #define | [UINT\_FAST64\_MAX](#aeb74410af7781bc84b5f64ae7a8f4a17)   \_\_UINT\_FAST64\_MAX\_\_ |
| #define | [INT\_LEAST8\_MAX](#aa05109908fb2770f632d2b646b9f85bf)   \_\_INT\_LEAST8\_MAX\_\_ |
| #define | [INT\_LEAST16\_MAX](#a7eb2a8e2a1c65d6c9ad0f86154890baa)   \_\_INT\_LEAST16\_MAX\_\_ |
| #define | [INT\_LEAST32\_MAX](#a5618711a0a54f722190a3a1219e278c2)   \_\_INT\_LEAST32\_MAX\_\_ |
| #define | [INT\_LEAST64\_MAX](#a35d0f98a2e507fd1be779d49da92724e)   \_\_INT\_LEAST64\_MAX\_\_ |
| #define | [INT\_LEAST8\_MIN](#a3e986cad833f63f420962ff60eda87e5)   (-[INT\_LEAST8\_MAX](#aa05109908fb2770f632d2b646b9f85bf) - 1) |
| #define | [INT\_LEAST16\_MIN](#a1f91bfd5820c2f27af3d260fc75813e1)   (-[INT\_LEAST16\_MAX](#a7eb2a8e2a1c65d6c9ad0f86154890baa) - 1) |
| #define | [INT\_LEAST32\_MIN](#a2360a536116dd734820a6b5b3d560ce7)   (-[INT\_LEAST32\_MAX](#a5618711a0a54f722190a3a1219e278c2) - 1) |
| #define | [INT\_LEAST64\_MIN](#ac12b4f6966b57ad82feb683b284b4060)   (-[INT\_LEAST64\_MAX](#a35d0f98a2e507fd1be779d49da92724e) - 1LL) |
| #define | [UINT\_LEAST8\_MAX](#a2a80bde77ee1698d0f42f334adad4f2b)   \_\_UINT\_LEAST8\_MAX\_\_ |
| #define | [UINT\_LEAST16\_MAX](#a6ef6a1a518bbf516ca8b0180b11c358f)   \_\_UINT\_LEAST16\_MAX\_\_ |
| #define | [UINT\_LEAST32\_MAX](#a70cad8bacc9a6db301e1cdc86cc8d571)   \_\_UINT\_LEAST32\_MAX\_\_ |
| #define | [UINT\_LEAST64\_MAX](#aab530113fa96e280e49c3c138b0f917d)   \_\_UINT\_LEAST64\_MAX\_\_ |
| #define | [INTPTR\_MAX](#a9e5742f2bae4a5283431a3c03499e3a9)   \_\_INTPTR\_MAX\_\_ |
| #define | [INTPTR\_MIN](#a2aaa6d3aa1d7d1e0e326955aa24db752)   (-[INTPTR\_MAX](#a9e5742f2bae4a5283431a3c03499e3a9) - 1) |
| #define | [UINTPTR\_MAX](#ab2355300ea19395357e62d780f4dd073)   \_\_UINTPTR\_MAX\_\_ |
| #define | [PTRDIFF\_MAX](#add2ef7bffac19cfdd1f4b5495409672f)   \_\_PTRDIFF\_MAX\_\_ |
| #define | [PTRDIFF\_MIN](#ad9b88ba2fb858f98b50b38e49875d90e)   (-[PTRDIFF\_MAX](#add2ef7bffac19cfdd1f4b5495409672f) - 1) |
| #define | [SIZE\_MAX](#a3c75bb398badb69c7577b21486f9963f)   \_\_SIZE\_MAX\_\_ |

| Typedefs | |
| --- | --- |
| typedef \_\_INT8\_TYPE\_\_ | [int8\_t](#accbd6432732c88ad6adc5365800433b6) |
| typedef \_\_INT16\_TYPE\_\_ | [int16\_t](#afe270aee8d96ad7f279a4020b9d58bdf) |
| typedef \_\_INT32\_TYPE\_\_ | [int32\_t](#a0c18914b3041c2f583aba76f418399c2) |
| typedef \_\_INT64\_TYPE\_\_ | [int64\_t](#ac714c0d2c1a4adb10e73cab29623314b) |
| typedef \_\_INT64\_TYPE\_\_ | [intmax\_t](#a9d6c1dc12f73927ba41516de04a5fdb8) |
| typedef \_\_INT\_FAST8\_TYPE\_\_ | [int\_fast8\_t](#a98f573ff8187ff09c9594a3f2af7be0d) |
| typedef \_\_INT\_FAST16\_TYPE\_\_ | [int\_fast16\_t](#a888269be199d49b7f40006aaafa5a350) |
| typedef \_\_INT\_FAST32\_TYPE\_\_ | [int\_fast32\_t](#a530ba8ffc89f6393d2d0e2fb2db38b54) |
| typedef \_\_INT\_FAST64\_TYPE\_\_ | [int\_fast64\_t](#abcdb0a9f6e7d139ad4f521ab8f4efdc0) |
| typedef \_\_INT\_LEAST8\_TYPE\_\_ | [int\_least8\_t](#adb5f4bf8afa3bee9e4da1bb9daf4908d) |
| typedef \_\_INT\_LEAST16\_TYPE\_\_ | [int\_least16\_t](#a3a4bc1e426626e17f6a6e0f64decec56) |
| typedef \_\_INT\_LEAST32\_TYPE\_\_ | [int\_least32\_t](#a4462f62ae74ff8172526401354d2fc9b) |
| typedef \_\_INT\_LEAST64\_TYPE\_\_ | [int\_least64\_t](#a8a5003442318117c64d16d6f32f64f37) |
| typedef \_\_UINT8\_TYPE\_\_ | [uint8\_t](#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) |
| typedef \_\_UINT16\_TYPE\_\_ | [uint16\_t](#a5debae8b2a1ec20a6694c0c443ee399e) |
| typedef \_\_UINT32\_TYPE\_\_ | [uint32\_t](#a0a8582351ac627ee8bde2973c825e47f) |
| typedef \_\_UINT64\_TYPE\_\_ | [uint64\_t](#a2095b9bffea4b2656950c6c0419edbf1) |
| typedef \_\_UINT64\_TYPE\_\_ | [uintmax\_t](#aac7deaa1633720ec64bd432bbc31af40) |
| typedef \_\_UINT\_FAST8\_TYPE\_\_ | [uint\_fast8\_t](#a2464ed69ccd3fd2b3b4c93cb78f6fa20) |
| typedef \_\_UINT\_FAST16\_TYPE\_\_ | [uint\_fast16\_t](#aaabed6e034edb01c259c003894d7f7c8) |
| typedef \_\_UINT\_FAST32\_TYPE\_\_ | [uint\_fast32\_t](#aa44ff507c3d9a49e27fac64e9fadf062) |
| typedef \_\_UINT\_FAST64\_TYPE\_\_ | [uint\_fast64\_t](#a62c711f66c6d29c81429aeafdc4bc592) |
| typedef \_\_UINT\_LEAST8\_TYPE\_\_ | [uint\_least8\_t](#a61d44370ed65907c324edad5e8d34632) |
| typedef \_\_UINT\_LEAST16\_TYPE\_\_ | [uint\_least16\_t](#a1a01d6a4e68e435471be2ae8db7e8fdc) |
| typedef \_\_UINT\_LEAST32\_TYPE\_\_ | [uint\_least32\_t](#a678494ae5435d8904e7972c94618e774) |
| typedef \_\_UINT\_LEAST64\_TYPE\_\_ | [uint\_least64\_t](#aba0cb5638c172422eb4a7555a143fbbc) |
| typedef \_\_INTPTR\_TYPE\_\_ | [intptr\_t](#a0bd5dec00e345e69027427f8621d6a6c) |
| typedef \_\_UINTPTR\_TYPE\_\_ | [uintptr\_t](#a4788399d1d0b37ccf098a7da82254808) |

## Macro Definition Documentation

## [◆ ](#ac58f2c111cc9989c86db2a7dc4fd84ca)INT16\_MAX

| #define INT16\_MAX   \_\_INT16\_MAX\_\_ |
| --- |

## [◆ ](#ad4e9955955b27624963643eac448118a)INT16\_MIN

| #define INT16\_MIN   (-[INT16\_MAX](#ac58f2c111cc9989c86db2a7dc4fd84ca) - 1) |
| --- |

## [◆ ](#a181807730d4a375f848ba139813ce04f)INT32\_MAX

| #define INT32\_MAX   \_\_INT32\_MAX\_\_ |
| --- |

## [◆ ](#a688eb21a22db27c2b2bd5836943cdcbe)INT32\_MIN

| #define INT32\_MIN   (-[INT32\_MAX](#a181807730d4a375f848ba139813ce04f) - 1) |
| --- |

## [◆ ](#ad0d744f05898e32d01f73f8af3cd2071)INT64\_MAX

| #define INT64\_MAX   \_\_INT64\_MAX\_\_ |
| --- |

## [◆ ](#ab21f12f372f67b8ff0aa3432336ede67)INT64\_MIN

| #define INT64\_MIN   (-[INT64\_MAX](#ad0d744f05898e32d01f73f8af3cd2071) - 1LL) |
| --- |

## [◆ ](#aaf7f29f45f1a513b4748a4e5014ddf6a)INT8\_MAX

| #define INT8\_MAX   \_\_INT8\_MAX\_\_ |
| --- |

## [◆ ](#aadcf2a81af243df333b31efa6461ab8e)INT8\_MIN

| #define INT8\_MIN   (-[INT8\_MAX](#aaf7f29f45f1a513b4748a4e5014ddf6a) - 1) |
| --- |

## [◆ ](#a2fd35d0ea091e04caec504ff0042cf00)INT\_FAST16\_MAX

| #define INT\_FAST16\_MAX   \_\_INT\_FAST16\_MAX\_\_ |
| --- |

## [◆ ](#a169460a4e2a79138723d68d99372d958)INT\_FAST16\_MIN

| #define INT\_FAST16\_MIN   (-[INT\_FAST16\_MAX](#a2fd35d0ea091e04caec504ff0042cf00) - 1) |
| --- |

## [◆ ](#ac96fa0f41b19e89f109e4f9913ca6635)INT\_FAST32\_MAX

| #define INT\_FAST32\_MAX   \_\_INT\_FAST32\_MAX\_\_ |
| --- |

## [◆ ](#ad93df1652ed0635513d5efe4f1219926)INT\_FAST32\_MIN

| #define INT\_FAST32\_MIN   (-[INT\_FAST32\_MAX](#ac96fa0f41b19e89f109e4f9913ca6635) - 1) |
| --- |

## [◆ ](#a13c95cf9c209d8daacb36cbf0d5ba275)INT\_FAST64\_MAX

| #define INT\_FAST64\_MAX   \_\_INT\_FAST64\_MAX\_\_ |
| --- |

## [◆ ](#a50f0fdcb00ea2500cec0f3d6d45c36f3)INT\_FAST64\_MIN

| #define INT\_FAST64\_MIN   (-[INT\_FAST64\_MAX](#a13c95cf9c209d8daacb36cbf0d5ba275) - 1LL) |
| --- |

## [◆ ](#acbcdb3bee0f5f904da5df8de69a80ca3)INT\_FAST8\_MAX

| #define INT\_FAST8\_MAX   \_\_INT\_FAST8\_MAX\_\_ |
| --- |

## [◆ ](#aad8fb982cb19143efd5ee9a1a7a89390)INT\_FAST8\_MIN

| #define INT\_FAST8\_MIN   (-[INT\_FAST8\_MAX](#acbcdb3bee0f5f904da5df8de69a80ca3) - 1) |
| --- |

## [◆ ](#a7eb2a8e2a1c65d6c9ad0f86154890baa)INT\_LEAST16\_MAX

| #define INT\_LEAST16\_MAX   \_\_INT\_LEAST16\_MAX\_\_ |
| --- |

## [◆ ](#a1f91bfd5820c2f27af3d260fc75813e1)INT\_LEAST16\_MIN

| #define INT\_LEAST16\_MIN   (-[INT\_LEAST16\_MAX](#a7eb2a8e2a1c65d6c9ad0f86154890baa) - 1) |
| --- |

## [◆ ](#a5618711a0a54f722190a3a1219e278c2)INT\_LEAST32\_MAX

| #define INT\_LEAST32\_MAX   \_\_INT\_LEAST32\_MAX\_\_ |
| --- |

## [◆ ](#a2360a536116dd734820a6b5b3d560ce7)INT\_LEAST32\_MIN

| #define INT\_LEAST32\_MIN   (-[INT\_LEAST32\_MAX](#a5618711a0a54f722190a3a1219e278c2) - 1) |
| --- |

## [◆ ](#a35d0f98a2e507fd1be779d49da92724e)INT\_LEAST64\_MAX

| #define INT\_LEAST64\_MAX   \_\_INT\_LEAST64\_MAX\_\_ |
| --- |

## [◆ ](#ac12b4f6966b57ad82feb683b284b4060)INT\_LEAST64\_MIN

| #define INT\_LEAST64\_MIN   (-[INT\_LEAST64\_MAX](#a35d0f98a2e507fd1be779d49da92724e) - 1LL) |
| --- |

## [◆ ](#aa05109908fb2770f632d2b646b9f85bf)INT\_LEAST8\_MAX

| #define INT\_LEAST8\_MAX   \_\_INT\_LEAST8\_MAX\_\_ |
| --- |

## [◆ ](#a3e986cad833f63f420962ff60eda87e5)INT\_LEAST8\_MIN

| #define INT\_LEAST8\_MIN   (-[INT\_LEAST8\_MAX](#aa05109908fb2770f632d2b646b9f85bf) - 1) |
| --- |

## [◆ ](#a022b9b0a3564d786244a4631847c37a3)INTMAX\_MAX

| #define INTMAX\_MAX   \_\_INT64\_MAX\_\_ |
| --- |

## [◆ ](#a9e5742f2bae4a5283431a3c03499e3a9)INTPTR\_MAX

| #define INTPTR\_MAX   \_\_INTPTR\_MAX\_\_ |
| --- |

## [◆ ](#a2aaa6d3aa1d7d1e0e326955aa24db752)INTPTR\_MIN

| #define INTPTR\_MIN   (-[INTPTR\_MAX](#a9e5742f2bae4a5283431a3c03499e3a9) - 1) |
| --- |

## [◆ ](#add2ef7bffac19cfdd1f4b5495409672f)PTRDIFF\_MAX

| #define PTRDIFF\_MAX   \_\_PTRDIFF\_MAX\_\_ |
| --- |

## [◆ ](#ad9b88ba2fb858f98b50b38e49875d90e)PTRDIFF\_MIN

| #define PTRDIFF\_MIN   (-[PTRDIFF\_MAX](#add2ef7bffac19cfdd1f4b5495409672f) - 1) |
| --- |

## [◆ ](#a3c75bb398badb69c7577b21486f9963f)SIZE\_MAX

| #define SIZE\_MAX   \_\_SIZE\_MAX\_\_ |
| --- |

## [◆ ](#a3ea490c9b3617d4479bd80ef93cd5602)UINT16\_MAX

| #define UINT16\_MAX   \_\_UINT16\_MAX\_\_ |
| --- |

## [◆ ](#ab5eb23180f7cc12b7d6c04a8ec067fdd)UINT32\_MAX

| #define UINT32\_MAX   \_\_UINT32\_MAX\_\_ |
| --- |

## [◆ ](#a30654b4b67d97c42ca3f9b6052dda916)UINT64\_MAX

| #define UINT64\_MAX   \_\_UINT64\_MAX\_\_ |
| --- |

## [◆ ](#aeb4e270a084ee26fe73e799861bd0252)UINT8\_MAX

| #define UINT8\_MAX   \_\_UINT8\_MAX\_\_ |
| --- |

## [◆ ](#aed28ca63d9b222f6f1377358fe73a183)UINT\_FAST16\_MAX

| #define UINT\_FAST16\_MAX   \_\_UINT\_FAST16\_MAX\_\_ |
| --- |

## [◆ ](#ad51246a178143208b2db3315efd21c45)UINT\_FAST32\_MAX

| #define UINT\_FAST32\_MAX   \_\_UINT\_FAST32\_MAX\_\_ |
| --- |

## [◆ ](#aeb74410af7781bc84b5f64ae7a8f4a17)UINT\_FAST64\_MAX

| #define UINT\_FAST64\_MAX   \_\_UINT\_FAST64\_MAX\_\_ |
| --- |

## [◆ ](#a2c6f97ea2d76d0cf6260c84046cdb44e)UINT\_FAST8\_MAX

| #define UINT\_FAST8\_MAX   \_\_UINT\_FAST8\_MAX\_\_ |
| --- |

## [◆ ](#a6ef6a1a518bbf516ca8b0180b11c358f)UINT\_LEAST16\_MAX

| #define UINT\_LEAST16\_MAX   \_\_UINT\_LEAST16\_MAX\_\_ |
| --- |

## [◆ ](#a70cad8bacc9a6db301e1cdc86cc8d571)UINT\_LEAST32\_MAX

| #define UINT\_LEAST32\_MAX   \_\_UINT\_LEAST32\_MAX\_\_ |
| --- |

## [◆ ](#aab530113fa96e280e49c3c138b0f917d)UINT\_LEAST64\_MAX

| #define UINT\_LEAST64\_MAX   \_\_UINT\_LEAST64\_MAX\_\_ |
| --- |

## [◆ ](#a2a80bde77ee1698d0f42f334adad4f2b)UINT\_LEAST8\_MAX

| #define UINT\_LEAST8\_MAX   \_\_UINT\_LEAST8\_MAX\_\_ |
| --- |

## [◆ ](#aa54fd5210434219e9027bfa0f0e325c8)UINTMAX\_MAX

| #define UINTMAX\_MAX   \_\_UINT64\_MAX\_\_ |
| --- |

## [◆ ](#ab2355300ea19395357e62d780f4dd073)UINTPTR\_MAX

| #define UINTPTR\_MAX   \_\_UINTPTR\_MAX\_\_ |
| --- |

## Typedef Documentation

## [◆ ](#afe270aee8d96ad7f279a4020b9d58bdf)int16\_t

| typedef \_\_INT16\_TYPE\_\_ [int16\_t](#afe270aee8d96ad7f279a4020b9d58bdf) |
| --- |

## [◆ ](#a0c18914b3041c2f583aba76f418399c2)int32\_t

| typedef \_\_INT32\_TYPE\_\_ [int32\_t](#a0c18914b3041c2f583aba76f418399c2) |
| --- |

## [◆ ](#ac714c0d2c1a4adb10e73cab29623314b)int64\_t

| typedef \_\_INT64\_TYPE\_\_ [int64\_t](#ac714c0d2c1a4adb10e73cab29623314b) |
| --- |

## [◆ ](#accbd6432732c88ad6adc5365800433b6)int8\_t

| typedef \_\_INT8\_TYPE\_\_ [int8\_t](#accbd6432732c88ad6adc5365800433b6) |
| --- |

## [◆ ](#a888269be199d49b7f40006aaafa5a350)int\_fast16\_t

| typedef \_\_INT\_FAST16\_TYPE\_\_ [int\_fast16\_t](#a888269be199d49b7f40006aaafa5a350) |
| --- |

## [◆ ](#a530ba8ffc89f6393d2d0e2fb2db38b54)int\_fast32\_t

| typedef \_\_INT\_FAST32\_TYPE\_\_ [int\_fast32\_t](#a530ba8ffc89f6393d2d0e2fb2db38b54) |
| --- |

## [◆ ](#abcdb0a9f6e7d139ad4f521ab8f4efdc0)int\_fast64\_t

| typedef \_\_INT\_FAST64\_TYPE\_\_ [int\_fast64\_t](#abcdb0a9f6e7d139ad4f521ab8f4efdc0) |
| --- |

## [◆ ](#a98f573ff8187ff09c9594a3f2af7be0d)int\_fast8\_t

| typedef \_\_INT\_FAST8\_TYPE\_\_ [int\_fast8\_t](#a98f573ff8187ff09c9594a3f2af7be0d) |
| --- |

## [◆ ](#a3a4bc1e426626e17f6a6e0f64decec56)int\_least16\_t

| typedef \_\_INT\_LEAST16\_TYPE\_\_ [int\_least16\_t](#a3a4bc1e426626e17f6a6e0f64decec56) |
| --- |

## [◆ ](#a4462f62ae74ff8172526401354d2fc9b)int\_least32\_t

| typedef \_\_INT\_LEAST32\_TYPE\_\_ [int\_least32\_t](#a4462f62ae74ff8172526401354d2fc9b) |
| --- |

## [◆ ](#a8a5003442318117c64d16d6f32f64f37)int\_least64\_t

| typedef \_\_INT\_LEAST64\_TYPE\_\_ [int\_least64\_t](#a8a5003442318117c64d16d6f32f64f37) |
| --- |

## [◆ ](#adb5f4bf8afa3bee9e4da1bb9daf4908d)int\_least8\_t

| typedef \_\_INT\_LEAST8\_TYPE\_\_ [int\_least8\_t](#adb5f4bf8afa3bee9e4da1bb9daf4908d) |
| --- |

## [◆ ](#a9d6c1dc12f73927ba41516de04a5fdb8)intmax\_t

| typedef \_\_INT64\_TYPE\_\_ [intmax\_t](#a9d6c1dc12f73927ba41516de04a5fdb8) |
| --- |

## [◆ ](#a0bd5dec00e345e69027427f8621d6a6c)intptr\_t

| typedef \_\_INTPTR\_TYPE\_\_ [intptr\_t](#a0bd5dec00e345e69027427f8621d6a6c) |
| --- |

## [◆ ](#a5debae8b2a1ec20a6694c0c443ee399e)uint16\_t

| typedef \_\_UINT16\_TYPE\_\_ [uint16\_t](#a5debae8b2a1ec20a6694c0c443ee399e) |
| --- |

## [◆ ](#a0a8582351ac627ee8bde2973c825e47f)uint32\_t

| typedef \_\_UINT32\_TYPE\_\_ [uint32\_t](#a0a8582351ac627ee8bde2973c825e47f) |
| --- |

## [◆ ](#a2095b9bffea4b2656950c6c0419edbf1)uint64\_t

| typedef \_\_UINT64\_TYPE\_\_ [uint64\_t](#a2095b9bffea4b2656950c6c0419edbf1) |
| --- |

## [◆ ](#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)uint8\_t

| typedef \_\_UINT8\_TYPE\_\_ [uint8\_t](#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) |
| --- |

## [◆ ](#aaabed6e034edb01c259c003894d7f7c8)uint\_fast16\_t

| typedef \_\_UINT\_FAST16\_TYPE\_\_ [uint\_fast16\_t](#aaabed6e034edb01c259c003894d7f7c8) |
| --- |

## [◆ ](#aa44ff507c3d9a49e27fac64e9fadf062)uint\_fast32\_t

| typedef \_\_UINT\_FAST32\_TYPE\_\_ [uint\_fast32\_t](#aa44ff507c3d9a49e27fac64e9fadf062) |
| --- |

## [◆ ](#a62c711f66c6d29c81429aeafdc4bc592)uint\_fast64\_t

| typedef \_\_UINT\_FAST64\_TYPE\_\_ [uint\_fast64\_t](#a62c711f66c6d29c81429aeafdc4bc592) |
| --- |

## [◆ ](#a2464ed69ccd3fd2b3b4c93cb78f6fa20)uint\_fast8\_t

| typedef \_\_UINT\_FAST8\_TYPE\_\_ [uint\_fast8\_t](#a2464ed69ccd3fd2b3b4c93cb78f6fa20) |
| --- |

## [◆ ](#a1a01d6a4e68e435471be2ae8db7e8fdc)uint\_least16\_t

| typedef \_\_UINT\_LEAST16\_TYPE\_\_ [uint\_least16\_t](#a1a01d6a4e68e435471be2ae8db7e8fdc) |
| --- |

## [◆ ](#a678494ae5435d8904e7972c94618e774)uint\_least32\_t

| typedef \_\_UINT\_LEAST32\_TYPE\_\_ [uint\_least32\_t](#a678494ae5435d8904e7972c94618e774) |
| --- |

## [◆ ](#aba0cb5638c172422eb4a7555a143fbbc)uint\_least64\_t

| typedef \_\_UINT\_LEAST64\_TYPE\_\_ [uint\_least64\_t](#aba0cb5638c172422eb4a7555a143fbbc) |
| --- |

## [◆ ](#a61d44370ed65907c324edad5e8d34632)uint\_least8\_t

| typedef \_\_UINT\_LEAST8\_TYPE\_\_ [uint\_least8\_t](#a61d44370ed65907c324edad5e8d34632) |
| --- |

## [◆ ](#aac7deaa1633720ec64bd432bbc31af40)uintmax\_t

| typedef \_\_UINT64\_TYPE\_\_ [uintmax\_t](#aac7deaa1633720ec64bd432bbc31af40) |
| --- |

## [◆ ](#a4788399d1d0b37ccf098a7da82254808)uintptr\_t

| typedef \_\_UINTPTR\_TYPE\_\_ [uintptr\_t](#a4788399d1d0b37ccf098a7da82254808) |
| --- |

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [stdint.h](stdint_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
