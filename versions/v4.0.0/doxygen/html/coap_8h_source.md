---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/coap_8h_source.html
original_path: doxygen/html/coap_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap.h

[Go to the documentation of this file.](coap_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \* Copyright (c) 2021 Nordic Semiconductor

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_COAP\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_COAP\_H\_

16

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <stddef.h>

28#include <[stdbool.h](stdbool_8h.md)>

29#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

30#include <[zephyr/sys/math\_extras.h](math__extras_8h.md)>

31#include <[zephyr/sys/slist.h](slist_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

[ 46](group__coap.md#ga7b8b3041e2f4ae26e663ff7431a6e6e3)enum [coap\_option\_num](group__coap.md#ga7b8b3041e2f4ae26e663ff7431a6e6e3) {

[ 47](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4c61e26d11841c76debe2f99de5e9756) [COAP\_OPTION\_IF\_MATCH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4c61e26d11841c76debe2f99de5e9756) = 1,

[ 48](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a402bb0a642a07d951c35d69736fd3f33) [COAP\_OPTION\_URI\_HOST](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a402bb0a642a07d951c35d69736fd3f33) = 3,

[ 49](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a0efdc30ce5551daffd093b2a8466978a) [COAP\_OPTION\_ETAG](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a0efdc30ce5551daffd093b2a8466978a) = 4,

[ 50](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a07ea6f395818a7019bb9e6a6e34d2d74) [COAP\_OPTION\_IF\_NONE\_MATCH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a07ea6f395818a7019bb9e6a6e34d2d74) = 5,

[ 51](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a06e91bbb4fa2144543d4148d3245ad25) [COAP\_OPTION\_OBSERVE](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a06e91bbb4fa2144543d4148d3245ad25) = 6,

[ 52](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a344707b9f4cb71310f2ccf5e8050d17a) [COAP\_OPTION\_URI\_PORT](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a344707b9f4cb71310f2ccf5e8050d17a) = 7,

[ 53](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae82be3591d43f0d1c7e89ab764d969bd) [COAP\_OPTION\_LOCATION\_PATH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae82be3591d43f0d1c7e89ab764d969bd) = 8,

[ 54](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a96b5a15937e875b3087307cc5faab1af) [COAP\_OPTION\_URI\_PATH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a96b5a15937e875b3087307cc5faab1af) = 11,

[ 55](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac3166e67b5f5bf3cefee58c8ff58e5b8) [COAP\_OPTION\_CONTENT\_FORMAT](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac3166e67b5f5bf3cefee58c8ff58e5b8) = 12,

[ 56](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ab4cda4d3732fd12b9f203a2475c20981) [COAP\_OPTION\_MAX\_AGE](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ab4cda4d3732fd12b9f203a2475c20981) = 14,

[ 57](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3adb4d27052247b9a79ad7fcc0cc30c71c) [COAP\_OPTION\_URI\_QUERY](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3adb4d27052247b9a79ad7fcc0cc30c71c) = 15,

[ 58](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3afd0725f0ceb5ce22a6c7b390ca7efc9d) [COAP\_OPTION\_ACCEPT](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3afd0725f0ceb5ce22a6c7b390ca7efc9d) = 17,

[ 59](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac728800fc8f0d80e37dcf322e75eb27d) [COAP\_OPTION\_LOCATION\_QUERY](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac728800fc8f0d80e37dcf322e75eb27d) = 20,

[ 60](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972) [COAP\_OPTION\_BLOCK2](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972) = 23,

[ 61](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a8aaa54af114fd1db631566afa69f162d) [COAP\_OPTION\_BLOCK1](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a8aaa54af114fd1db631566afa69f162d) = 27,

[ 62](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a26c1bcd7af4fccd949e3de35fc2d88e6) [COAP\_OPTION\_SIZE2](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a26c1bcd7af4fccd949e3de35fc2d88e6) = 28,

[ 63](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae4d2c93b545708926813217cd36a96ac) [COAP\_OPTION\_PROXY\_URI](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae4d2c93b545708926813217cd36a96ac) = 35,

[ 64](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a30da986503e1e15243b74a16b161901c) [COAP\_OPTION\_PROXY\_SCHEME](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a30da986503e1e15243b74a16b161901c) = 39,

[ 65](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a53169a1c7b07c9e97f79dfc06af3eb51) [COAP\_OPTION\_SIZE1](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a53169a1c7b07c9e97f79dfc06af3eb51) = 60,

[ 66](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a620e8b59f67f89de8a38dc76c8fcc594) [COAP\_OPTION\_ECHO](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a620e8b59f67f89de8a38dc76c8fcc594) = 252,

[ 67](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a7984f2c4845610491bda964111a1c8e7) [COAP\_OPTION\_NO\_RESPONSE](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a7984f2c4845610491bda964111a1c8e7) = 258,

[ 68](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2a47428ec35972d256da05104ea6396f) [COAP\_OPTION\_REQUEST\_TAG](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2a47428ec35972d256da05104ea6396f) = 292

69};

70

[ 76](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7)enum [coap\_method](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7) {

[ 77](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a025300cb0dc4c4de8eb0b0e0b4eb5317) [COAP\_METHOD\_GET](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a025300cb0dc4c4de8eb0b0e0b4eb5317) = 1,

[ 78](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7aba51bcab79bf75080ccf75c1ec38a3d6) [COAP\_METHOD\_POST](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7aba51bcab79bf75080ccf75c1ec38a3d6) = 2,

[ 79](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a91637ef7c9f57cdcc65d0118008251db) [COAP\_METHOD\_PUT](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a91637ef7c9f57cdcc65d0118008251db) = 3,

[ 80](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7adccbea1fe9a43433cf8471e32208a5ac) [COAP\_METHOD\_DELETE](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7adccbea1fe9a43433cf8471e32208a5ac) = 4,

[ 81](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7afa4070fed5c01b28bb1a59e3f0c021f4) [COAP\_METHOD\_FETCH](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7afa4070fed5c01b28bb1a59e3f0c021f4) = 5,

[ 82](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7adca55e3d2b4b41b249f6b2f67074d708) [COAP\_METHOD\_PATCH](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7adca55e3d2b4b41b249f6b2f67074d708) = 6,

[ 83](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a78f97b895f29819bf3f8b0314967f20e) [COAP\_METHOD\_IPATCH](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a78f97b895f29819bf3f8b0314967f20e) = 7,

84};

85

87

88#define COAP\_REQUEST\_MASK 0x07

89

90#define COAP\_VERSION\_1 1U

91

92#define COAP\_OBSERVE\_MAX\_AGE 0xFFFFFF

93

95

[ 99](group__coap.md#ga3b375b7580246d1266293d09902f3d9f)enum [coap\_msgtype](group__coap.md#ga3b375b7580246d1266293d09902f3d9f) {

[ 106](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa65c04ee4847d0c595238079ac9564e8d) [COAP\_TYPE\_CON](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa65c04ee4847d0c595238079ac9564e8d) = 0,

[ 113](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa629a304bea0c85c7b2bf746b26216a4f) [COAP\_TYPE\_NON\_CON](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa629a304bea0c85c7b2bf746b26216a4f) = 1,

[ 119](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa7b2fe2187018bce9132af2763b57307d) [COAP\_TYPE\_ACK](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa7b2fe2187018bce9132af2763b57307d) = 2,

[ 126](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa287b951159fd51b84a2e0491b012f84c) [COAP\_TYPE\_RESET](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa287b951159fd51b84a2e0491b012f84c) = 3

127};

128

[ 135](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)#define COAP\_MAKE\_RESPONSE\_CODE(class, det) ((class << 5) | (det))

136

[ 142](group__coap.md#ga1ea81a365834e96f43ab7be573069d26)enum [coap\_response\_code](group__coap.md#ga1ea81a365834e96f43ab7be573069d26) {

[ 144](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a0629da1898b934c3f699b98ff808c717) [COAP\_RESPONSE\_CODE\_OK](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a0629da1898b934c3f699b98ff808c717) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(2, 0),

[ 146](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ad2d9fe8dd5beda74b522377c0b76275b) [COAP\_RESPONSE\_CODE\_CREATED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ad2d9fe8dd5beda74b522377c0b76275b) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(2, 1),

[ 148](group__coap.md#gga1ea81a365834e96f43ab7be573069d26abf324915aa498c64a733a0098de4a082) [COAP\_RESPONSE\_CODE\_DELETED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26abf324915aa498c64a733a0098de4a082) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(2, 2),

[ 150](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aecaac4a0e9c821dfc20536951409dd48) [COAP\_RESPONSE\_CODE\_VALID](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aecaac4a0e9c821dfc20536951409dd48) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(2, 3),

[ 152](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3) [COAP\_RESPONSE\_CODE\_CHANGED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(2, 4),

[ 154](group__coap.md#gga1ea81a365834e96f43ab7be573069d26adfd3e5e3c6ad5715127bb444c205fbce) [COAP\_RESPONSE\_CODE\_CONTENT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26adfd3e5e3c6ad5715127bb444c205fbce) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(2, 5),

[ 156](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ae4e3ff451c626421b9b329790f019dd8) [COAP\_RESPONSE\_CODE\_CONTINUE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ae4e3ff451c626421b9b329790f019dd8) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(2, 31),

[ 158](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5) [COAP\_RESPONSE\_CODE\_BAD\_REQUEST](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 0),

[ 160](group__coap.md#gga1ea81a365834e96f43ab7be573069d26acb76dbf11b47477144cc4ece3357283c) [COAP\_RESPONSE\_CODE\_UNAUTHORIZED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26acb76dbf11b47477144cc4ece3357283c) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 1),

[ 162](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a989a6528edc653c0b693ed875481e82d) [COAP\_RESPONSE\_CODE\_BAD\_OPTION](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a989a6528edc653c0b693ed875481e82d) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 2),

[ 164](group__coap.md#gga1ea81a365834e96f43ab7be573069d26afeee555ef54f138db58b14ad2c328d04) [COAP\_RESPONSE\_CODE\_FORBIDDEN](group__coap.md#gga1ea81a365834e96f43ab7be573069d26afeee555ef54f138db58b14ad2c328d04) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 3),

[ 166](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a86c2bff8add69428d164431b3091a8e9) [COAP\_RESPONSE\_CODE\_NOT\_FOUND](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a86c2bff8add69428d164431b3091a8e9) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 4),

[ 168](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a301eb722445472dba93d5accd6e0dd31) [COAP\_RESPONSE\_CODE\_NOT\_ALLOWED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a301eb722445472dba93d5accd6e0dd31) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 5),

[ 170](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a4d77322514521e8dfea01f4a1a6e5886) [COAP\_RESPONSE\_CODE\_NOT\_ACCEPTABLE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a4d77322514521e8dfea01f4a1a6e5886) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 6),

[ 172](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a671730c6d2f1a339fcd557c5452150af) [COAP\_RESPONSE\_CODE\_INCOMPLETE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a671730c6d2f1a339fcd557c5452150af) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 8),

[ 174](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ab447505d233aed9fd8ad28070d317544) [COAP\_RESPONSE\_CODE\_CONFLICT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ab447505d233aed9fd8ad28070d317544) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 9),

[ 176](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a289ade02833b57bffd915e648e050e52) [COAP\_RESPONSE\_CODE\_PRECONDITION\_FAILED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a289ade02833b57bffd915e648e050e52) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 12),

[ 178](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aaa43062a8146c1e2e09183228a540d2e) [COAP\_RESPONSE\_CODE\_REQUEST\_TOO\_LARGE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aaa43062a8146c1e2e09183228a540d2e) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 13),

[ 180](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aef6b165b9d3f8f4b477431058815c16b) [COAP\_RESPONSE\_CODE\_UNSUPPORTED\_CONTENT\_FORMAT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aef6b165b9d3f8f4b477431058815c16b) =

181 [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 15),

[ 183](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a5e5e31cc4647d5e0fdd1c8fe6cfa2661) [COAP\_RESPONSE\_CODE\_UNPROCESSABLE\_ENTITY](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a5e5e31cc4647d5e0fdd1c8fe6cfa2661) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 22),

[ 185](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aabd72cff6669d382aa04c53e764d0b49) [COAP\_RESPONSE\_CODE\_TOO\_MANY\_REQUESTS](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aabd72cff6669d382aa04c53e764d0b49) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(4, 29),

[ 187](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499) [COAP\_RESPONSE\_CODE\_INTERNAL\_ERROR](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(5, 0),

[ 189](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a85c04541bc8580c2ae915946fd677c15) [COAP\_RESPONSE\_CODE\_NOT\_IMPLEMENTED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a85c04541bc8580c2ae915946fd677c15) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(5, 1),

[ 191](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a8de29a7ee6bb960a97d6b415217b4640) [COAP\_RESPONSE\_CODE\_BAD\_GATEWAY](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a8de29a7ee6bb960a97d6b415217b4640) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(5, 2),

[ 193](group__coap.md#gga1ea81a365834e96f43ab7be573069d26afebd274586351951ffe9c8f26b270dec) [COAP\_RESPONSE\_CODE\_SERVICE\_UNAVAILABLE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26afebd274586351951ffe9c8f26b270dec) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(5, 3),

[ 195](group__coap.md#gga1ea81a365834e96f43ab7be573069d26af6d379fef704c269406b782c60772ecd) [COAP\_RESPONSE\_CODE\_GATEWAY\_TIMEOUT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26af6d379fef704c269406b782c60772ecd) = [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(5, 4),

[ 197](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a5f49a566d37b2cda0c624d76aee08bd1) [COAP\_RESPONSE\_CODE\_PROXYING\_NOT\_SUPPORTED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a5f49a566d37b2cda0c624d76aee08bd1) =

198 [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(5, 5)

199};

200

202

203#define COAP\_CODE\_EMPTY (0)

204

205#define COAP\_TOKEN\_MAX\_LEN 8UL

206

208

[ 214](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73)enum [coap\_content\_format](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73) {

[ 215](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73af068aa8d09032352799bc60868607997) [COAP\_CONTENT\_FORMAT\_TEXT\_PLAIN](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73af068aa8d09032352799bc60868607997) = 0,

[ 216](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a1fbd90fd5cb309e2de6954f46174dc4f) [COAP\_CONTENT\_FORMAT\_APP\_LINK\_FORMAT](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a1fbd90fd5cb309e2de6954f46174dc4f) = 40,

[ 217](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73adb96bf55e914f4852e92dc65752c372a) [COAP\_CONTENT\_FORMAT\_APP\_XML](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73adb96bf55e914f4852e92dc65752c372a) = 41,

[ 218](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a88d952174bb3e4ffb9ab11a599952760) [COAP\_CONTENT\_FORMAT\_APP\_OCTET\_STREAM](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a88d952174bb3e4ffb9ab11a599952760) = 42,

[ 219](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a483a382550b38468cc66bdce9f4743ea) [COAP\_CONTENT\_FORMAT\_APP\_EXI](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a483a382550b38468cc66bdce9f4743ea) = 47,

[ 220](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a975381d286c1e9b998e41ef0a234d17a) [COAP\_CONTENT\_FORMAT\_APP\_JSON](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a975381d286c1e9b998e41ef0a234d17a) = 50,

[ 221](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a141f183724ad6da14c3992c0990d6239) [COAP\_CONTENT\_FORMAT\_APP\_JSON\_PATCH\_JSON](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a141f183724ad6da14c3992c0990d6239) = 51,

[ 222](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a2797149fb3811d706dab291e9edc9436) [COAP\_CONTENT\_FORMAT\_APP\_MERGE\_PATCH\_JSON](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a2797149fb3811d706dab291e9edc9436) = 52,

[ 223](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a7ca73ff57a6c7fb1517b44f2ce17d3f9) [COAP\_CONTENT\_FORMAT\_APP\_CBOR](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a7ca73ff57a6c7fb1517b44f2ce17d3f9) = 60

224};

225

[ 232](group__coap.md#ga2a323287262bbb6a4932e7911ddb652c)enum [coap\_no\_response](group__coap.md#ga2a323287262bbb6a4932e7911ddb652c) {

[ 233](group__coap.md#gga2a323287262bbb6a4932e7911ddb652caeeb51bb18780c20df5b25183d52d42de) [COAP\_NO\_RESPONSE\_SUPPRESS\_2\_XX](group__coap.md#gga2a323287262bbb6a4932e7911ddb652caeeb51bb18780c20df5b25183d52d42de) = 0x02,

[ 234](group__coap.md#gga2a323287262bbb6a4932e7911ddb652cae8b0b1231d095b3e7a972ca4c86d8dce) [COAP\_NO\_RESPONSE\_SUPPRESS\_4\_XX](group__coap.md#gga2a323287262bbb6a4932e7911ddb652cae8b0b1231d095b3e7a972ca4c86d8dce) = 0x08,

[ 235](group__coap.md#gga2a323287262bbb6a4932e7911ddb652ca19ebfb46899b440124322bb67c906cb3) [COAP\_NO\_RESPONSE\_SUPPRESS\_5\_XX](group__coap.md#gga2a323287262bbb6a4932e7911ddb652ca19ebfb46899b440124322bb67c906cb3) = 0x10,

236

[ 237](group__coap.md#gga2a323287262bbb6a4932e7911ddb652ca21758021d7f3a36bf6ede06daa82dbf0) [COAP\_NO\_RESPONSE\_SUPPRESS\_ALL](group__coap.md#gga2a323287262bbb6a4932e7911ddb652ca21758021d7f3a36bf6ede06daa82dbf0) = [COAP\_NO\_RESPONSE\_SUPPRESS\_2\_XX](group__coap.md#gga2a323287262bbb6a4932e7911ddb652caeeb51bb18780c20df5b25183d52d42de) |

238 [COAP\_NO\_RESPONSE\_SUPPRESS\_4\_XX](group__coap.md#gga2a323287262bbb6a4932e7911ddb652cae8b0b1231d095b3e7a972ca4c86d8dce) |

239 [COAP\_NO\_RESPONSE\_SUPPRESS\_5\_XX](group__coap.md#gga2a323287262bbb6a4932e7911ddb652ca19ebfb46899b440124322bb67c906cb3),

240};

241

243

244/\* block option helper \*/

245#define GET\_BLOCK\_NUM(v) ((v) >> 4)

246#define GET\_BLOCK\_SIZE(v) (((v) & 0x7))

247#define GET\_MORE(v) (!!((v) & 0x08))

248

250

251struct [coap\_observer](structcoap__observer.md);

252struct [coap\_packet](structcoap__packet.md);

253struct [coap\_pending](structcoap__pending.md);

254struct [coap\_reply](structcoap__reply.md);

255struct [coap\_resource](structcoap__resource.md);

256

[ 262](group__coap.md#gaa509d49f06101342908a71f2f18f18fc)typedef int (\*[coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc))(struct [coap\_resource](structcoap__resource.md) \*resource,

263 struct [coap\_packet](structcoap__packet.md) \*request,

264 struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len);

265

[ 271](group__coap.md#ga4180b2476430fbe4a5e0418fb628ea91)typedef void (\*[coap\_notify\_t](group__coap.md#ga4180b2476430fbe4a5e0418fb628ea91))(struct [coap\_resource](structcoap__resource.md) \*resource,

272 struct [coap\_observer](structcoap__observer.md) \*observer);

273

[ 280](structcoap__resource.md)struct [coap\_resource](structcoap__resource.md) {

[ 282](structcoap__resource.md#a77dfb6d59c25e6e58141226023bf59ea) [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) [get](structcoap__resource.md#aebe880e3ccbd2441854dfa899dc72c13), [post](structcoap__resource.md#a1efed8197d44aba3b63aaa9d9bb0f5bb), [put](structcoap__resource.md#a3152a778e27e36fad7dd62985621d58b), [del](structcoap__resource.md#a77dfb6d59c25e6e58141226023bf59ea), [fetch](structcoap__resource.md#a6975e84ebc67d6aff2efb755695518f5), [patch](structcoap__resource.md#aa0a5465fc5b49a566e3803a9f1638724), [ipatch](structcoap__resource.md#a7657cb2e9bbac7f98e35b4ed33f13163);

[ 284](structcoap__resource.md#a3199679fd990d757e9a500fbd7c653d7) [coap\_notify\_t](group__coap.md#ga4180b2476430fbe4a5e0418fb628ea91) [notify](structcoap__resource.md#a3199679fd990d757e9a500fbd7c653d7);

[ 286](structcoap__resource.md#ada7a41309b6ca11612b17fabf6cd56c5) const char \* const \*[path](structcoap__resource.md#ada7a41309b6ca11612b17fabf6cd56c5);

[ 288](structcoap__resource.md#a202a83a5aa024a62bd25cc40f42e8d65) void \*[user\_data](structcoap__resource.md#a202a83a5aa024a62bd25cc40f42e8d65);

[ 290](structcoap__resource.md#a5035dc9c88c2b0ae557608e34ec14433) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [observers](structcoap__resource.md#a5035dc9c88c2b0ae557608e34ec14433);

[ 292](structcoap__resource.md#ae8e1b2b1920689913e0910a82a30e009) int [age](structcoap__resource.md#ae8e1b2b1920689913e0910a82a30e009);

293};

294

[ 298](structcoap__observer.md)struct [coap\_observer](structcoap__observer.md) {

[ 300](structcoap__observer.md#a24a9f853db17ff623f4c510fd0892eb5) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [list](structcoap__observer.md#a24a9f853db17ff623f4c510fd0892eb5);

[ 302](structcoap__observer.md#a9b6f807a0fc5d141e0ee3dd9596c3c82) struct [sockaddr](structsockaddr.md) [addr](structcoap__observer.md#a9b6f807a0fc5d141e0ee3dd9596c3c82);

[ 304](structcoap__observer.md#a6d7d792120b935bf61c739f95dd7361c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [token](structcoap__observer.md#a6d7d792120b935bf61c739f95dd7361c)[8];

[ 306](structcoap__observer.md#a901f148d2eb697206fde732050c3d8b4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tkl](structcoap__observer.md#a901f148d2eb697206fde732050c3d8b4);

307};

308

[ 312](structcoap__packet.md)struct [coap\_packet](structcoap__packet.md) {

[ 313](structcoap__packet.md#a8116711bcdff1fa6b0cf5c4fa9ab88d1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structcoap__packet.md#a8116711bcdff1fa6b0cf5c4fa9ab88d1);

[ 314](structcoap__packet.md#a46c0842c785b8de5eb8564950a786c02) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [offset](structcoap__packet.md#a46c0842c785b8de5eb8564950a786c02);

[ 315](structcoap__packet.md#a48c216a7da37e85942d271c85a79bcb6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_len](structcoap__packet.md#a48c216a7da37e85942d271c85a79bcb6);

[ 316](structcoap__packet.md#ab302c002da88f6d3a44c3a2215082be4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hdr\_len](structcoap__packet.md#ab302c002da88f6d3a44c3a2215082be4);

[ 317](structcoap__packet.md#acc5542ba2a69db8957155b90e75fd563) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [opt\_len](structcoap__packet.md#acc5542ba2a69db8957155b90e75fd563);

[ 318](structcoap__packet.md#a95dd8c6fb08ac61a1571c84258579475) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [delta](structcoap__packet.md#a95dd8c6fb08ac61a1571c84258579475);

319#if defined(CONFIG\_COAP\_KEEP\_USER\_DATA) || defined(DOXYGEN)

324 void \*user\_data;

325#endif

326};

327

[ 331](structcoap__option.md)struct [coap\_option](structcoap__option.md) {

[ 332](structcoap__option.md#abca15b0a8f9bdcb3f493ab3801d4b58f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [delta](structcoap__option.md#abca15b0a8f9bdcb3f493ab3801d4b58f);

333#if defined(CONFIG\_COAP\_EXTENDED\_OPTIONS\_LEN)

334 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structcoap__option.md#a01c8abdf27c3f8c5a816af33c0c093d4);

335 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structcoap__option.md#aff07b5d3673169b6316b91dc27780891)[CONFIG\_COAP\_EXTENDED\_OPTIONS\_LEN\_VALUE];

336#else

[ 337](structcoap__option.md#a01c8abdf27c3f8c5a816af33c0c093d4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structcoap__option.md#a01c8abdf27c3f8c5a816af33c0c093d4);

[ 338](structcoap__option.md#aff07b5d3673169b6316b91dc27780891) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structcoap__option.md#aff07b5d3673169b6316b91dc27780891)[12];

339#endif

340};

341

[ 350](group__coap.md#ga556deaf757f3047eefc2f032d0d7e0bc)typedef int (\*[coap\_reply\_t](group__coap.md#ga556deaf757f3047eefc2f032d0d7e0bc))(const struct [coap\_packet](structcoap__packet.md) \*response,

351 struct [coap\_reply](structcoap__reply.md) \*[reply](structcoap__reply.md#a6a888bbb5652761002ce26aba09352cc),

352 const struct [sockaddr](structsockaddr.md) \*from);

353

[ 357](structcoap__transmission__parameters.md)struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) {

[ 359](structcoap__transmission__parameters.md#aca76954d785d04312fb834dc524f102c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ack\_timeout](structcoap__transmission__parameters.md#aca76954d785d04312fb834dc524f102c);

360#if defined(CONFIG\_COAP\_RANDOMIZE\_ACK\_TIMEOUT) || defined(\_\_DOXYGEN\_\_)

[ 365](structcoap__transmission__parameters.md#a0b43d9e3adfbf7cac09e1ffbbe1f8ce8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ack\_random\_percent](structcoap__transmission__parameters.md#a0b43d9e3adfbf7cac09e1ffbbe1f8ce8);

366#endif /\* defined(CONFIG\_COAP\_RANDOMIZE\_ACK\_TIMEOUT) \*/

[ 368](structcoap__transmission__parameters.md#a74c91235bf64fab5e7abc0c9f581e44c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [coap\_backoff\_percent](structcoap__transmission__parameters.md#a74c91235bf64fab5e7abc0c9f581e44c);

[ 370](structcoap__transmission__parameters.md#a3a9b8bf0f2e00fc0981acdd86d404190) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_retransmission](structcoap__transmission__parameters.md#a3a9b8bf0f2e00fc0981acdd86d404190);

371};

372

[ 376](structcoap__pending.md)struct [coap\_pending](structcoap__pending.md) {

[ 377](structcoap__pending.md#adcc34b0d0201a24b15a5adca89ae0da3) struct [sockaddr](structsockaddr.md) [addr](structcoap__pending.md#adcc34b0d0201a24b15a5adca89ae0da3);

[ 378](structcoap__pending.md#a8b95f80a6eaac759ed0895201ff089d9) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [t0](structcoap__pending.md#a8b95f80a6eaac759ed0895201ff089d9);

[ 379](structcoap__pending.md#ab31339cc91df71ee6f90d5702f722fd6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timeout](structcoap__pending.md#ab31339cc91df71ee6f90d5702f722fd6);

[ 380](structcoap__pending.md#a8b1952271bd0c733c2fbcb158b60ca99) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structcoap__pending.md#a8b1952271bd0c733c2fbcb158b60ca99);

[ 381](structcoap__pending.md#a0a506507e472b3813e672f2b455e4bcc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structcoap__pending.md#a0a506507e472b3813e672f2b455e4bcc);

[ 382](structcoap__pending.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structcoap__pending.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d);

[ 383](structcoap__pending.md#a8aebb187845bcb6cb07dee68927f1aa6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retries](structcoap__pending.md#a8aebb187845bcb6cb07dee68927f1aa6);

[ 384](structcoap__pending.md#a05ca08379d13e10dfe86322f666c3d97) struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) [params](structcoap__pending.md#a05ca08379d13e10dfe86322f666c3d97);

385};

386

[ 391](structcoap__reply.md)struct [coap\_reply](structcoap__reply.md) {

[ 393](structcoap__reply.md#a6a888bbb5652761002ce26aba09352cc) [coap\_reply\_t](group__coap.md#ga556deaf757f3047eefc2f032d0d7e0bc) [reply](structcoap__reply.md#a6a888bbb5652761002ce26aba09352cc);

[ 395](structcoap__reply.md#aa951d9ba4eb7f8041e8e82df9c1401dc) void \*[user\_data](structcoap__reply.md#aa951d9ba4eb7f8041e8e82df9c1401dc);

[ 397](structcoap__reply.md#aea6b98e109e270c08df1554c5eee65fe) int [age](structcoap__reply.md#aea6b98e109e270c08df1554c5eee65fe);

[ 399](structcoap__reply.md#a94d17732056de3d8ecb3412c686091f8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structcoap__reply.md#a94d17732056de3d8ecb3412c686091f8);

[ 401](structcoap__reply.md#a18d40c327933c30681b924446c21ea9d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [token](structcoap__reply.md#a18d40c327933c30681b924446c21ea9d)[8];

[ 403](structcoap__reply.md#a038ccb29c2abff6168db3247241a8cc3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tkl](structcoap__reply.md#a038ccb29c2abff6168db3247241a8cc3);

404};

405

[ 413](group__coap.md#gafd01c39fac8f173edc04337161e92264)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [coap\_header\_get\_version](group__coap.md#gafd01c39fac8f173edc04337161e92264)(const struct [coap\_packet](structcoap__packet.md) \*cpkt);

414

[ 422](group__coap.md#gaed883ea6cec3acc5eb570e152dc52e25)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [coap\_header\_get\_type](group__coap.md#gaed883ea6cec3acc5eb570e152dc52e25)(const struct [coap\_packet](structcoap__packet.md) \*cpkt);

423

[ 433](group__coap.md#ga6a5049accfa0cd7106a3a6593c598545)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [coap\_header\_get\_token](group__coap.md#ga6a5049accfa0cd7106a3a6593c598545)(const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token);

434

[ 442](group__coap.md#gae4bf952fdf9e3d03ab0b0df4c3c0d054)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [coap\_header\_get\_code](group__coap.md#gae4bf952fdf9e3d03ab0b0df4c3c0d054)(const struct [coap\_packet](structcoap__packet.md) \*cpkt);

443

[ 451](group__coap.md#gafdaecca5ad26bab4fb7c9ee3477318f8)int [coap\_header\_set\_code](group__coap.md#gafdaecca5ad26bab4fb7c9ee3477318f8)(const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code);

452

[ 460](group__coap.md#ga63388c629da5370d2e711cdc9aabd837)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [coap\_header\_get\_id](group__coap.md#ga63388c629da5370d2e711cdc9aabd837)(const struct [coap\_packet](structcoap__packet.md) \*cpkt);

461

[ 471](group__coap.md#ga28ccf00fb1f5f13f747e61c2e3008b5c)const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[coap\_packet\_get\_payload](group__coap.md#ga28ccf00fb1f5f13f747e61c2e3008b5c)(const struct [coap\_packet](structcoap__packet.md) \*cpkt,

472 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*len);

473

[ 484](group__coap.md#ga8b621232b740d8e8e1771fba24897121)bool [coap\_uri\_path\_match](group__coap.md#ga8b621232b740d8e8e1771fba24897121)(const char \* const \*path,

485 struct [coap\_option](structcoap__option.md) \*options,

486 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num);

487

[ 504](group__coap.md#ga27a58a69f632551aa7a2394ae2badacf)int [coap\_packet\_parse](group__coap.md#ga27a58a69f632551aa7a2394ae2badacf)(struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len,

505 struct [coap\_option](structcoap__option.md) \*options, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num);

506

[ 516](group__coap.md#gab8f9e9cdfa20920d5d25fb1507a2286d)int [coap\_packet\_set\_path](group__coap.md#gab8f9e9cdfa20920d5d25fb1507a2286d)(struct [coap\_packet](structcoap__packet.md) \*cpkt, const char \*path);

517

[ 533](group__coap.md#ga90e6aab174f8977f0a3b5fbe1a20297c)int [coap\_packet\_init](group__coap.md#ga90e6aab174f8977f0a3b5fbe1a20297c)(struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_len,

534 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ver, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len,

535 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id);

536

[ 552](group__coap.md#gae6d93b1f93734302be75ee417813e5d1)int [coap\_ack\_init](group__coap.md#gae6d93b1f93734302be75ee417813e5d1)(struct [coap\_packet](structcoap__packet.md) \*cpkt, const struct [coap\_packet](structcoap__packet.md) \*req,

553 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code);

554

[ 568](group__coap.md#ga9626781d73d18c1305f654ef4723e5db)int [coap\_rst\_init](group__coap.md#ga9626781d73d18c1305f654ef4723e5db)(struct [coap\_packet](structcoap__packet.md) \*cpkt, const struct [coap\_packet](structcoap__packet.md) \*req,

569 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_len);

[ 576](group__coap.md#ga66f986f8a1157236bea27133c2a2538b)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[coap\_next\_token](group__coap.md#ga66f986f8a1157236bea27133c2a2538b)(void);

577

[ 583](group__coap.md#gade5f4995c6419db03ce3e7ff7ca1cfcb)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [coap\_next\_id](group__coap.md#gade5f4995c6419db03ce3e7ff7ca1cfcb)(void);

584

[ 598](group__coap.md#gaf006c8048ed7b863e70dbdd64bc3d608)int [coap\_find\_options](group__coap.md#gaf006c8048ed7b863e70dbdd64bc3d608)(const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

599 struct [coap\_option](structcoap__option.md) \*options, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) veclen);

600

[ 615](group__coap.md#ga2aa4140ee83ca4090a5604e34d1f1446)int [coap\_packet\_append\_option](group__coap.md#ga2aa4140ee83ca4090a5604e34d1f1446)(struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

616 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

617

[ 626](group__coap.md#gaca300a216781d360d2cd64e8e9f1ae8f)int [coap\_packet\_remove\_option](group__coap.md#gaca300a216781d360d2cd64e8e9f1ae8f)(struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code);

627

[ 639](group__coap.md#ga2fd0613e61274ec4b9b7bab3ab11ccce)unsigned int [coap\_option\_value\_to\_int](group__coap.md#ga2fd0613e61274ec4b9b7bab3ab11ccce)(const struct [coap\_option](structcoap__option.md) \*option);

640

[ 653](group__coap.md#ga6bec94992ac450dca03436a6ad74efb4)int [coap\_append\_option\_int](group__coap.md#ga6bec94992ac450dca03436a6ad74efb4)(struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

654 unsigned int val);

655

[ 663](group__coap.md#ga24000def8534acdcd2c61836dc690367)int [coap\_packet\_append\_payload\_marker](group__coap.md#ga24000def8534acdcd2c61836dc690367)(struct [coap\_packet](structcoap__packet.md) \*cpkt);

664

[ 674](group__coap.md#gadcd3a93a702a2a0b428f39b71dd67954)int [coap\_packet\_append\_payload](group__coap.md#gadcd3a93a702a2a0b428f39b71dd67954)(struct [coap\_packet](structcoap__packet.md) \*cpkt, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload,

675 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) payload\_len);

676

[ 685](group__coap.md#ga323644931c927b8988aafd89dacb993c)bool [coap\_packet\_is\_request](group__coap.md#ga323644931c927b8988aafd89dacb993c)(const struct [coap\_packet](structcoap__packet.md) \*cpkt);

686

[ 704](group__coap.md#ga864a95bd0d095070200494c630f7e147)int [coap\_handle\_request\_len](group__coap.md#ga864a95bd0d095070200494c630f7e147)(struct [coap\_packet](structcoap__packet.md) \*cpkt,

705 struct [coap\_resource](structcoap__resource.md) \*resources,

706 size\_t resources\_len,

707 struct [coap\_option](structcoap__option.md) \*options,

708 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num,

709 struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len);

710

[ 727](group__coap.md#ga88a5f2c3915ef109eadfebaf82b53186)int [coap\_handle\_request](group__coap.md#ga88a5f2c3915ef109eadfebaf82b53186)(struct [coap\_packet](structcoap__packet.md) \*cpkt,

728 struct [coap\_resource](structcoap__resource.md) \*resources,

729 struct [coap\_option](structcoap__option.md) \*options,

730 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num,

731 struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len);

732

[ 741](group__coap.md#ga712c1468f936a3af7dc39a86a5961922)enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) {

[ 742](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968) [COAP\_BLOCK\_16](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968),

[ 743](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a1aaf8f841c18e281b176793bb331993d) [COAP\_BLOCK\_32](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a1aaf8f841c18e281b176793bb331993d),

[ 744](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a7266f448a391ea2a2763f1ded5397520) [COAP\_BLOCK\_64](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a7266f448a391ea2a2763f1ded5397520),

[ 745](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a147ddf4b0e5d1a8c11f0da2c71dee4d8) [COAP\_BLOCK\_128](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a147ddf4b0e5d1a8c11f0da2c71dee4d8),

[ 746](group__coap.md#gga712c1468f936a3af7dc39a86a5961922acfc37f84eabccdde4bd84b06c6a5e753) [COAP\_BLOCK\_256](group__coap.md#gga712c1468f936a3af7dc39a86a5961922acfc37f84eabccdde4bd84b06c6a5e753),

[ 747](group__coap.md#gga712c1468f936a3af7dc39a86a5961922ad2052905aff08c58585dcf6c6caddc19) [COAP\_BLOCK\_512](group__coap.md#gga712c1468f936a3af7dc39a86a5961922ad2052905aff08c58585dcf6c6caddc19),

[ 748](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce) [COAP\_BLOCK\_1024](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce),

749};

750

[ 759](group__coap.md#gafffadd4a837e48fd72af20468ccd86f2)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [coap\_block\_size\_to\_bytes](group__coap.md#gafffadd4a837e48fd72af20468ccd86f2)(

760 enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) block\_size)

761{

762 return (1 << (block\_size + 4));

763}

764

[ 773](group__coap.md#ga27e3008b8511333e0c0115ba928017f3)static inline enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) [coap\_bytes\_to\_block\_size](group__coap.md#ga27e3008b8511333e0c0115ba928017f3)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bytes)

774{

775 int sz = [u32\_count\_trailing\_zeros](group__math__extras.md#ga4cb313f98c3fd3b00d6f4db74a9a0076)(bytes) - 4;

776

777 if (sz < [COAP\_BLOCK\_16](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968)) {

778 return [COAP\_BLOCK\_16](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968);

779 }

780 if (sz > [COAP\_BLOCK\_1024](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce)) {

781 return [COAP\_BLOCK\_1024](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce);

782 }

783 return (enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922))sz;

784}

785

[ 789](structcoap__block__context.md)struct [coap\_block\_context](structcoap__block__context.md) {

[ 791](structcoap__block__context.md#a27db79dc3a2af6dd9f41e3008dcde87a) size\_t [total\_size](structcoap__block__context.md#a27db79dc3a2af6dd9f41e3008dcde87a);

[ 793](structcoap__block__context.md#a474f54e2a29d41b9d449f8574e747067) size\_t [current](structcoap__block__context.md#a474f54e2a29d41b9d449f8574e747067);

[ 795](structcoap__block__context.md#a27eb897fa2d455eb79220f1654509da3) enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) [block\_size](structcoap__block__context.md#a27eb897fa2d455eb79220f1654509da3);

796};

797

[ 807](group__coap.md#ga57486e764f0feb6544fa3b0d19935afd)int [coap\_block\_transfer\_init](group__coap.md#ga57486e764f0feb6544fa3b0d19935afd)(struct [coap\_block\_context](structcoap__block__context.md) \*ctx,

808 enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) block\_size,

809 size\_t total\_size);

810

[ 823](group__coap.md#ga8b5966a29054ace04cae81d4da588e72)int [coap\_append\_descriptive\_block\_option](group__coap.md#ga8b5966a29054ace04cae81d4da588e72)(struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx);

824

[ 836](group__coap.md#gaabdfa8cf28cc2c3a14ae0af5fa7e7212)bool [coap\_has\_descriptive\_block\_option](group__coap.md#gaabdfa8cf28cc2c3a14ae0af5fa7e7212)(struct [coap\_packet](structcoap__packet.md) \*cpkt);

837

[ 848](group__coap.md#ga941ee9d68f1a628755aa79c249cbae58)int [coap\_remove\_descriptive\_block\_option](group__coap.md#ga941ee9d68f1a628755aa79c249cbae58)(struct [coap\_packet](structcoap__packet.md) \*cpkt);

849

[ 857](group__coap.md#gafc61a6878d82f81565ab752ced0ce2be)bool [coap\_block\_has\_more](group__coap.md#gafc61a6878d82f81565ab752ced0ce2be)(struct [coap\_packet](structcoap__packet.md) \*cpkt);

858

[ 868](group__coap.md#ga518d5f4422ff45f2b4a296f249da89cd)int [coap\_append\_block1\_option](group__coap.md#ga518d5f4422ff45f2b4a296f249da89cd)(struct [coap\_packet](structcoap__packet.md) \*cpkt,

869 struct [coap\_block\_context](structcoap__block__context.md) \*ctx);

870

[ 880](group__coap.md#ga361c17b698bdaa0fc529b7338efefd8c)int [coap\_append\_block2\_option](group__coap.md#ga361c17b698bdaa0fc529b7338efefd8c)(struct [coap\_packet](structcoap__packet.md) \*cpkt,

881 struct [coap\_block\_context](structcoap__block__context.md) \*ctx);

882

[ 892](group__coap.md#ga3f66d5935dcacfeebcac2b3001d7b57a)int [coap\_append\_size1\_option](group__coap.md#ga3f66d5935dcacfeebcac2b3001d7b57a)(struct [coap\_packet](structcoap__packet.md) \*cpkt,

893 struct [coap\_block\_context](structcoap__block__context.md) \*ctx);

894

[ 904](group__coap.md#gafbc8c15ef03b762f9411c38b03aa403b)int [coap\_append\_size2\_option](group__coap.md#gafbc8c15ef03b762f9411c38b03aa403b)(struct [coap\_packet](structcoap__packet.md) \*cpkt,

905 struct [coap\_block\_context](structcoap__block__context.md) \*ctx);

906

[ 916](group__coap.md#ga21b8f4ffeecc7900f6bf299836d2b5b3)int [coap\_get\_option\_int](group__coap.md#ga21b8f4ffeecc7900f6bf299836d2b5b3)(const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code);

917

[ 929](group__coap.md#ga10c4a0d7e2052f3116fbf3b355fe75db)int [coap\_get\_block1\_option](group__coap.md#ga10c4a0d7e2052f3116fbf3b355fe75db)(const struct [coap\_packet](structcoap__packet.md) \*cpkt, bool \*has\_more, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*block\_number);

930

[ 943](group__coap.md#ga196390e6f016b72b3ae2ae9e69bed1b7)int [coap\_get\_block2\_option](group__coap.md#ga196390e6f016b72b3ae2ae9e69bed1b7)(const struct [coap\_packet](structcoap__packet.md) \*cpkt, bool \*has\_more,

944 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*block\_number);

945

[ 955](group__coap.md#ga3b0cc9bfabdddeffd98f36d7f15dd416)int [coap\_update\_from\_block](group__coap.md#ga3b0cc9bfabdddeffd98f36d7f15dd416)(const struct [coap\_packet](structcoap__packet.md) \*cpkt,

956 struct [coap\_block\_context](structcoap__block__context.md) \*ctx);

957

[ 970](group__coap.md#ga50f7837da003601479dbc470ba9898ae)int [coap\_next\_block\_for\_option](group__coap.md#ga50f7837da003601479dbc470ba9898ae)(const struct [coap\_packet](structcoap__packet.md) \*cpkt,

971 struct [coap\_block\_context](structcoap__block__context.md) \*ctx,

972 enum [coap\_option\_num](group__coap.md#ga7b8b3041e2f4ae26e663ff7431a6e6e3) option);

973

[ 985](group__coap.md#ga1244716ecf06fad1013131c42eab8c5c)size\_t [coap\_next\_block](group__coap.md#ga1244716ecf06fad1013131c42eab8c5c)(const struct [coap\_packet](structcoap__packet.md) \*cpkt,

986 struct [coap\_block\_context](structcoap__block__context.md) \*ctx);

987

[ 996](group__coap.md#ga3d720b0d222cc35ce56cc260df1609a3)void [coap\_observer\_init](group__coap.md#ga3d720b0d222cc35ce56cc260df1609a3)(struct [coap\_observer](structcoap__observer.md) \*observer,

997 const struct [coap\_packet](structcoap__packet.md) \*request,

998 const struct [sockaddr](structsockaddr.md) \*addr);

999

[ 1009](group__coap.md#ga3c42861f8442e548f560acf3deca6baa)bool [coap\_register\_observer](group__coap.md#ga3c42861f8442e548f560acf3deca6baa)(struct [coap\_resource](structcoap__resource.md) \*resource,

1010 struct [coap\_observer](structcoap__observer.md) \*observer);

1011

[ 1021](group__coap.md#ga33c351ac06b5ae9217cd53d8cf330fbd)bool [coap\_remove\_observer](group__coap.md#ga33c351ac06b5ae9217cd53d8cf330fbd)(struct [coap\_resource](structcoap__resource.md) \*resource,

1022 struct [coap\_observer](structcoap__observer.md) \*observer);

1023

[ 1037](group__coap.md#gaf9c1a55aee52588df2694ea947db5db4)struct [coap\_observer](structcoap__observer.md) \*[coap\_find\_observer](group__coap.md#gaf9c1a55aee52588df2694ea947db5db4)(

1038 struct [coap\_observer](structcoap__observer.md) \*observers, size\_t len,

1039 const struct [sockaddr](structsockaddr.md) \*[addr](structcoap__observer.md#a9b6f807a0fc5d141e0ee3dd9596c3c82),

1040 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[token](structcoap__observer.md#a6d7d792120b935bf61c739f95dd7361c), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len);

1041

[ 1055](group__coap.md#ga427167161529c24f5cf8c9ed2023e321)struct [coap\_observer](structcoap__observer.md) \*[coap\_find\_observer\_by\_addr](group__coap.md#ga427167161529c24f5cf8c9ed2023e321)(

1056 struct [coap\_observer](structcoap__observer.md) \*observers, size\_t len,

1057 const struct [sockaddr](structsockaddr.md) \*[addr](structcoap__observer.md#a9b6f807a0fc5d141e0ee3dd9596c3c82));

1058

[ 1073](group__coap.md#gadeaa59fd7b6eab454d5930289b4e08f7)struct [coap\_observer](structcoap__observer.md) \*[coap\_find\_observer\_by\_token](group__coap.md#gadeaa59fd7b6eab454d5930289b4e08f7)(

1074 struct [coap\_observer](structcoap__observer.md) \*observers, size\_t len,

1075 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[token](structcoap__observer.md#a6d7d792120b935bf61c739f95dd7361c), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len);

1076

[ 1086](group__coap.md#ga2410e973bf3192244426df346230608b)struct [coap\_observer](structcoap__observer.md) \*[coap\_observer\_next\_unused](group__coap.md#ga2410e973bf3192244426df346230608b)(

1087 struct [coap\_observer](structcoap__observer.md) \*observers, size\_t len);

1088

[ 1095](group__coap.md#gacfe30c84434dc8adbf3d399ec0e51bec)void [coap\_reply\_init](group__coap.md#gacfe30c84434dc8adbf3d399ec0e51bec)(struct [coap\_reply](structcoap__reply.md) \*reply,

1096 const struct [coap\_packet](structcoap__packet.md) \*request);

1097

[ 1114](group__coap.md#ga868f792abf555f01c28caa5413d9e84c)int [coap\_pending\_init](group__coap.md#ga868f792abf555f01c28caa5413d9e84c)(struct [coap\_pending](structcoap__pending.md) \*pending,

1115 const struct [coap\_packet](structcoap__packet.md) \*request,

1116 const struct [sockaddr](structsockaddr.md) \*[addr](structcoap__observer.md#a9b6f807a0fc5d141e0ee3dd9596c3c82),

1117 const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params);

1118

[ 1129](group__coap.md#ga800831ddfe19b1a5637a5edd9e78c470)struct [coap\_pending](structcoap__pending.md) \*[coap\_pending\_next\_unused](group__coap.md#ga800831ddfe19b1a5637a5edd9e78c470)(

1130 struct [coap\_pending](structcoap__pending.md) \*pendings, size\_t [len](structcoap__pending.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d));

1131

[ 1142](group__coap.md#ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e)struct [coap\_reply](structcoap__reply.md) \*[coap\_reply\_next\_unused](group__coap.md#ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e)(

1143 struct [coap\_reply](structcoap__reply.md) \*replies, size\_t len);

1144

[ 1158](group__coap.md#ga94ceba78cbd2440f91d9b30d6b06594d)struct [coap\_pending](structcoap__pending.md) \*[coap\_pending\_received](group__coap.md#ga94ceba78cbd2440f91d9b30d6b06594d)(

1159 const struct [coap\_packet](structcoap__packet.md) \*response,

1160 struct [coap\_pending](structcoap__pending.md) \*pendings, size\_t [len](structcoap__pending.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d));

1161

[ 1174](group__coap.md#ga3da23a809504025a24bf03daea3e606b)struct [coap\_reply](structcoap__reply.md) \*[coap\_response\_received](group__coap.md#ga3da23a809504025a24bf03daea3e606b)(

1175 const struct [coap\_packet](structcoap__packet.md) \*response,

1176 const struct [sockaddr](structsockaddr.md) \*from,

1177 struct [coap\_reply](structcoap__reply.md) \*replies, size\_t len);

1178

[ 1189](group__coap.md#ga9d63518c701ebdb4c7f65c5368d00d27)struct [coap\_pending](structcoap__pending.md) \*[coap\_pending\_next\_to\_expire](group__coap.md#ga9d63518c701ebdb4c7f65c5368d00d27)(

1190 struct [coap\_pending](structcoap__pending.md) \*pendings, size\_t [len](structcoap__pending.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d));

1191

[ 1200](group__coap.md#ga2bcfc7340ed2347862b0f003e1b00a4b)bool [coap\_pending\_cycle](group__coap.md#ga2bcfc7340ed2347862b0f003e1b00a4b)(struct [coap\_pending](structcoap__pending.md) \*pending);

1201

[ 1208](group__coap.md#ga03287eb3187aa28e0e83e0e0c72e2631)void [coap\_pending\_clear](group__coap.md#ga03287eb3187aa28e0e83e0e0c72e2631)(struct [coap\_pending](structcoap__pending.md) \*pending);

1209

[ 1217](group__coap.md#ga6e0947048052e733a3571fdc8955b2d7)void [coap\_pendings\_clear](group__coap.md#ga6e0947048052e733a3571fdc8955b2d7)(struct [coap\_pending](structcoap__pending.md) \*pendings, size\_t [len](structcoap__pending.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d));

1218

[ 1226](group__coap.md#gad9db2ced9b882265c16e3039f893ca03)size\_t [coap\_pendings\_count](group__coap.md#gad9db2ced9b882265c16e3039f893ca03)(struct [coap\_pending](structcoap__pending.md) \*pendings, size\_t [len](structcoap__pending.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d));

1227

[ 1234](group__coap.md#ga37b58c38c150751d31207ece416529d8)void [coap\_reply\_clear](group__coap.md#ga37b58c38c150751d31207ece416529d8)(struct [coap\_reply](structcoap__reply.md) \*reply);

1235

[ 1242](group__coap.md#gaddb02509934f5bac20b7c7f83aea4cd8)void [coap\_replies\_clear](group__coap.md#gaddb02509934f5bac20b7c7f83aea4cd8)(struct [coap\_reply](structcoap__reply.md) \*replies, size\_t [len](structcoap__pending.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d));

1243

[ 1252](group__coap.md#gad0c738d308f9cca8ea5cdb79449282cb)int [coap\_resource\_notify](group__coap.md#gad0c738d308f9cca8ea5cdb79449282cb)(struct [coap\_resource](structcoap__resource.md) \*resource);

1253

[ 1262](group__coap.md#ga46b315c30b642eec65bcb84e9c937ee7)bool [coap\_request\_is\_observe](group__coap.md#ga46b315c30b642eec65bcb84e9c937ee7)(const struct [coap\_packet](structcoap__packet.md) \*request);

1263

[ 1269](group__coap.md#ga1bd7be0a5390f0599e7bec0cbd79daf8)struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) [coap\_get\_transmission\_parameters](group__coap.md#ga1bd7be0a5390f0599e7bec0cbd79daf8)(void);

1270

[ 1276](group__coap.md#gaf361fd233f1aa650650108ae1e205ede)void [coap\_set\_transmission\_parameters](group__coap.md#gaf361fd233f1aa650650108ae1e205ede)(const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params);

1277

1278#ifdef \_\_cplusplus

1279}

1280#endif

1281

1285

1286#endif /\* ZEPHYR\_INCLUDE\_NET\_COAP\_H\_ \*/

[coap\_pending\_clear](group__coap.md#ga03287eb3187aa28e0e83e0e0c72e2631)

void coap\_pending\_clear(struct coap\_pending \*pending)

Cancels the pending retransmission, so it again becomes available.

[coap\_get\_block1\_option](group__coap.md#ga10c4a0d7e2052f3116fbf3b355fe75db)

int coap\_get\_block1\_option(const struct coap\_packet \*cpkt, bool \*has\_more, uint32\_t \*block\_number)

Get the block size, more flag and block number from the CoAP block1 option.

[coap\_next\_block](group__coap.md#ga1244716ecf06fad1013131c42eab8c5c)

size\_t coap\_next\_block(const struct coap\_packet \*cpkt, struct coap\_block\_context \*ctx)

Updates ctx so after this is called the current entry indicates the correct offset in the body of dat...

[coap\_get\_block2\_option](group__coap.md#ga196390e6f016b72b3ae2ae9e69bed1b7)

int coap\_get\_block2\_option(const struct coap\_packet \*cpkt, bool \*has\_more, uint32\_t \*block\_number)

Get values from CoAP block2 option.

[coap\_get\_transmission\_parameters](group__coap.md#ga1bd7be0a5390f0599e7bec0cbd79daf8)

struct coap\_transmission\_parameters coap\_get\_transmission\_parameters(void)

Get currently active CoAP transmission parameters.

[coap\_response\_code](group__coap.md#ga1ea81a365834e96f43ab7be573069d26)

coap\_response\_code

Set of response codes available for a response packet.

**Definition** coap.h:142

[coap\_get\_option\_int](group__coap.md#ga21b8f4ffeecc7900f6bf299836d2b5b3)

int coap\_get\_option\_int(const struct coap\_packet \*cpkt, uint16\_t code)

Get the integer representation of a CoAP option.

[coap\_packet\_append\_payload\_marker](group__coap.md#ga24000def8534acdcd2c61836dc690367)

int coap\_packet\_append\_payload\_marker(struct coap\_packet \*cpkt)

Append payload marker to CoAP packet.

[coap\_observer\_next\_unused](group__coap.md#ga2410e973bf3192244426df346230608b)

struct coap\_observer \* coap\_observer\_next\_unused(struct coap\_observer \*observers, size\_t len)

Returns the next available observer representation.

[coap\_packet\_parse](group__coap.md#ga27a58a69f632551aa7a2394ae2badacf)

int coap\_packet\_parse(struct coap\_packet \*cpkt, uint8\_t \*data, uint16\_t len, struct coap\_option \*options, uint8\_t opt\_num)

Parses the CoAP packet in data, validating it and initializing cpkt.

[coap\_bytes\_to\_block\_size](group__coap.md#ga27e3008b8511333e0c0115ba928017f3)

static enum coap\_block\_size coap\_bytes\_to\_block\_size(uint16\_t bytes)

Helper for converting block size in bytes to enumeration.

**Definition** coap.h:773

[coap\_packet\_get\_payload](group__coap.md#ga28ccf00fb1f5f13f747e61c2e3008b5c)

const uint8\_t \* coap\_packet\_get\_payload(const struct coap\_packet \*cpkt, uint16\_t \*len)

Returns the data pointer and length of the CoAP packet.

[coap\_no\_response](group__coap.md#ga2a323287262bbb6a4932e7911ddb652c)

coap\_no\_response

Set of No-Response option values for CoAP.

**Definition** coap.h:232

[coap\_packet\_append\_option](group__coap.md#ga2aa4140ee83ca4090a5604e34d1f1446)

int coap\_packet\_append\_option(struct coap\_packet \*cpkt, uint16\_t code, const uint8\_t \*value, uint16\_t len)

Appends an option to the packet.

[coap\_pending\_cycle](group__coap.md#ga2bcfc7340ed2347862b0f003e1b00a4b)

bool coap\_pending\_cycle(struct coap\_pending \*pending)

After a request is sent, user may want to cycle the pending retransmission so the timeout is updated.

[coap\_option\_value\_to\_int](group__coap.md#ga2fd0613e61274ec4b9b7bab3ab11ccce)

unsigned int coap\_option\_value\_to\_int(const struct coap\_option \*option)

Converts an option to its integer representation.

[coap\_packet\_is\_request](group__coap.md#ga323644931c927b8988aafd89dacb993c)

bool coap\_packet\_is\_request(const struct coap\_packet \*cpkt)

Check if a CoAP packet is a CoAP request.

[coap\_remove\_observer](group__coap.md#ga33c351ac06b5ae9217cd53d8cf330fbd)

bool coap\_remove\_observer(struct coap\_resource \*resource, struct coap\_observer \*observer)

Remove this observer from the list of registered observers of that resource.

[coap\_append\_block2\_option](group__coap.md#ga361c17b698bdaa0fc529b7338efefd8c)

int coap\_append\_block2\_option(struct coap\_packet \*cpkt, struct coap\_block\_context \*ctx)

Append BLOCK2 option to the packet.

[coap\_reply\_clear](group__coap.md#ga37b58c38c150751d31207ece416529d8)

void coap\_reply\_clear(struct coap\_reply \*reply)

Cancels awaiting for this reply, so it becomes available again.

[coap\_update\_from\_block](group__coap.md#ga3b0cc9bfabdddeffd98f36d7f15dd416)

int coap\_update\_from\_block(const struct coap\_packet \*cpkt, struct coap\_block\_context \*ctx)

Retrieves BLOCK{1,2} and SIZE{1,2} from cpkt and updates ctx accordingly.

[coap\_msgtype](group__coap.md#ga3b375b7580246d1266293d09902f3d9f)

coap\_msgtype

CoAP packets may be of one of these types.

**Definition** coap.h:99

[coap\_register\_observer](group__coap.md#ga3c42861f8442e548f560acf3deca6baa)

bool coap\_register\_observer(struct coap\_resource \*resource, struct coap\_observer \*observer)

After the observer is initialized, associate the observer with an resource.

[coap\_observer\_init](group__coap.md#ga3d720b0d222cc35ce56cc260df1609a3)

void coap\_observer\_init(struct coap\_observer \*observer, const struct coap\_packet \*request, const struct sockaddr \*addr)

Indicates that the remote device referenced by addr, with request, wants to observe a resource.

[coap\_response\_received](group__coap.md#ga3da23a809504025a24bf03daea3e606b)

struct coap\_reply \* coap\_response\_received(const struct coap\_packet \*response, const struct sockaddr \*from, struct coap\_reply \*replies, size\_t len)

After a response is received, call coap\_reply\_t handler registered in coap\_reply structure.

[coap\_append\_size1\_option](group__coap.md#ga3f66d5935dcacfeebcac2b3001d7b57a)

int coap\_append\_size1\_option(struct coap\_packet \*cpkt, struct coap\_block\_context \*ctx)

Append SIZE1 option to the packet.

[coap\_notify\_t](group__coap.md#ga4180b2476430fbe4a5e0418fb628ea91)

void(\* coap\_notify\_t)(struct coap\_resource \*resource, struct coap\_observer \*observer)

Type of the callback being called when a resource's has observers to be informed when an update happe...

**Definition** coap.h:271

[coap\_find\_observer\_by\_addr](group__coap.md#ga427167161529c24f5cf8c9ed2023e321)

struct coap\_observer \* coap\_find\_observer\_by\_addr(struct coap\_observer \*observers, size\_t len, const struct sockaddr \*addr)

Returns the observer that matches address addr.

[coap\_request\_is\_observe](group__coap.md#ga46b315c30b642eec65bcb84e9c937ee7)

bool coap\_request\_is\_observe(const struct coap\_packet \*request)

Returns if this request is enabling observing a resource.

[coap\_next\_block\_for\_option](group__coap.md#ga50f7837da003601479dbc470ba9898ae)

int coap\_next\_block\_for\_option(const struct coap\_packet \*cpkt, struct coap\_block\_context \*ctx, enum coap\_option\_num option)

Updates ctx according to option set in cpkt so after this is called the current entry indicates the c...

[coap\_append\_block1\_option](group__coap.md#ga518d5f4422ff45f2b4a296f249da89cd)

int coap\_append\_block1\_option(struct coap\_packet \*cpkt, struct coap\_block\_context \*ctx)

Append BLOCK1 option to the packet.

[coap\_reply\_t](group__coap.md#ga556deaf757f3047eefc2f032d0d7e0bc)

int(\* coap\_reply\_t)(const struct coap\_packet \*response, struct coap\_reply \*reply, const struct sockaddr \*from)

Helper function to be called when a response matches the a pending request.

**Definition** coap.h:350

[coap\_block\_transfer\_init](group__coap.md#ga57486e764f0feb6544fa3b0d19935afd)

int coap\_block\_transfer\_init(struct coap\_block\_context \*ctx, enum coap\_block\_size block\_size, size\_t total\_size)

Initializes the context of a block-wise transfer.

[coap\_header\_get\_id](group__coap.md#ga63388c629da5370d2e711cdc9aabd837)

uint16\_t coap\_header\_get\_id(const struct coap\_packet \*cpkt)

Returns the message id associated with the CoAP packet.

[coap\_reply\_next\_unused](group__coap.md#ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e)

struct coap\_reply \* coap\_reply\_next\_unused(struct coap\_reply \*replies, size\_t len)

Returns the next available reply struct, so it can be used to track replies and notifications receive...

[coap\_next\_token](group__coap.md#ga66f986f8a1157236bea27133c2a2538b)

uint8\_t \* coap\_next\_token(void)

Returns a randomly generated array of 8 bytes, that can be used as a message's token.

[coap\_header\_get\_token](group__coap.md#ga6a5049accfa0cd7106a3a6593c598545)

uint8\_t coap\_header\_get\_token(const struct coap\_packet \*cpkt, uint8\_t \*token)

Returns the token (if any) in the CoAP packet.

[coap\_method](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7)

coap\_method

Available request methods.

**Definition** coap.h:76

[coap\_append\_option\_int](group__coap.md#ga6bec94992ac450dca03436a6ad74efb4)

int coap\_append\_option\_int(struct coap\_packet \*cpkt, uint16\_t code, unsigned int val)

Appends an integer value option to the packet.

[coap\_pendings\_clear](group__coap.md#ga6e0947048052e733a3571fdc8955b2d7)

void coap\_pendings\_clear(struct coap\_pending \*pendings, size\_t len)

Cancels all pending retransmissions, so they become available again.

[coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922)

coap\_block\_size

Represents the size of each block that will be transferred using block-wise transfers [RFC7959]:

**Definition** coap.h:741

[coap\_option\_num](group__coap.md#ga7b8b3041e2f4ae26e663ff7431a6e6e3)

coap\_option\_num

Set of CoAP packet options we are aware of.

**Definition** coap.h:46

[coap\_pending\_next\_unused](group__coap.md#ga800831ddfe19b1a5637a5edd9e78c470)

struct coap\_pending \* coap\_pending\_next\_unused(struct coap\_pending \*pendings, size\_t len)

Returns the next available pending struct, that can be used to track the retransmission status of a r...

[coap\_handle\_request\_len](group__coap.md#ga864a95bd0d095070200494c630f7e147)

int coap\_handle\_request\_len(struct coap\_packet \*cpkt, struct coap\_resource \*resources, size\_t resources\_len, struct coap\_option \*options, uint8\_t opt\_num, struct sockaddr \*addr, socklen\_t addr\_len)

When a request is received, call the appropriate methods of the matching resources.

[coap\_pending\_init](group__coap.md#ga868f792abf555f01c28caa5413d9e84c)

int coap\_pending\_init(struct coap\_pending \*pending, const struct coap\_packet \*request, const struct sockaddr \*addr, const struct coap\_transmission\_parameters \*params)

Initialize a pending request with a request.

[coap\_handle\_request](group__coap.md#ga88a5f2c3915ef109eadfebaf82b53186)

int coap\_handle\_request(struct coap\_packet \*cpkt, struct coap\_resource \*resources, struct coap\_option \*options, uint8\_t opt\_num, struct sockaddr \*addr, socklen\_t addr\_len)

When a request is received, call the appropriate methods of the matching resources.

[coap\_append\_descriptive\_block\_option](group__coap.md#ga8b5966a29054ace04cae81d4da588e72)

int coap\_append\_descriptive\_block\_option(struct coap\_packet \*cpkt, struct coap\_block\_context \*ctx)

Append BLOCK1 or BLOCK2 option to the packet.

[coap\_uri\_path\_match](group__coap.md#ga8b621232b740d8e8e1771fba24897121)

bool coap\_uri\_path\_match(const char \*const \*path, struct coap\_option \*options, uint8\_t opt\_num)

Verify if CoAP URI path matches with provided options.

[coap\_packet\_init](group__coap.md#ga90e6aab174f8977f0a3b5fbe1a20297c)

int coap\_packet\_init(struct coap\_packet \*cpkt, uint8\_t \*data, uint16\_t max\_len, uint8\_t ver, uint8\_t type, uint8\_t token\_len, const uint8\_t \*token, uint8\_t code, uint16\_t id)

Creates a new CoAP Packet from input data.

[coap\_remove\_descriptive\_block\_option](group__coap.md#ga941ee9d68f1a628755aa79c249cbae58)

int coap\_remove\_descriptive\_block\_option(struct coap\_packet \*cpkt)

Remove BLOCK1 or BLOCK2 option from the packet.

[coap\_content\_format](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73)

coap\_content\_format

Set of Content-Format option values for CoAP.

**Definition** coap.h:214

[coap\_pending\_received](group__coap.md#ga94ceba78cbd2440f91d9b30d6b06594d)

struct coap\_pending \* coap\_pending\_received(const struct coap\_packet \*response, struct coap\_pending \*pendings, size\_t len)

After a response is received, returns if there is any matching pending request exits.

[coap\_rst\_init](group__coap.md#ga9626781d73d18c1305f654ef4723e5db)

int coap\_rst\_init(struct coap\_packet \*cpkt, const struct coap\_packet \*req, uint8\_t \*data, uint16\_t max\_len)

Create a new CoAP Reset message for given request.

[coap\_pending\_next\_to\_expire](group__coap.md#ga9d63518c701ebdb4c7f65c5368d00d27)

struct coap\_pending \* coap\_pending\_next\_to\_expire(struct coap\_pending \*pendings, size\_t len)

Returns the next pending about to expire, pending->timeout informs how many ms to next expiration.

[coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc)

int(\* coap\_method\_t)(struct coap\_resource \*resource, struct coap\_packet \*request, struct sockaddr \*addr, socklen\_t addr\_len)

Type of the callback being called when a resource's method is invoked by the remote entity.

**Definition** coap.h:262

[coap\_has\_descriptive\_block\_option](group__coap.md#gaabdfa8cf28cc2c3a14ae0af5fa7e7212)

bool coap\_has\_descriptive\_block\_option(struct coap\_packet \*cpkt)

Check if a descriptive block option is set in the packet.

[coap\_packet\_set\_path](group__coap.md#gab8f9e9cdfa20920d5d25fb1507a2286d)

int coap\_packet\_set\_path(struct coap\_packet \*cpkt, const char \*path)

Parses provided coap path (with/without query) or query and appends that as options to the cpkt.

[COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)

#define COAP\_MAKE\_RESPONSE\_CODE(class, det)

Utility macro to create a CoAP response code.

**Definition** coap.h:135

[coap\_packet\_remove\_option](group__coap.md#gaca300a216781d360d2cd64e8e9f1ae8f)

int coap\_packet\_remove\_option(struct coap\_packet \*cpkt, uint16\_t code)

Remove an option from the packet.

[coap\_reply\_init](group__coap.md#gacfe30c84434dc8adbf3d399ec0e51bec)

void coap\_reply\_init(struct coap\_reply \*reply, const struct coap\_packet \*request)

Indicates that a reply is expected for request.

[coap\_resource\_notify](group__coap.md#gad0c738d308f9cca8ea5cdb79449282cb)

int coap\_resource\_notify(struct coap\_resource \*resource)

Indicates that this resource was updated and that the notify callback should be called for every regi...

[coap\_pendings\_count](group__coap.md#gad9db2ced9b882265c16e3039f893ca03)

size\_t coap\_pendings\_count(struct coap\_pending \*pendings, size\_t len)

Count number of pending requests.

[coap\_packet\_append\_payload](group__coap.md#gadcd3a93a702a2a0b428f39b71dd67954)

int coap\_packet\_append\_payload(struct coap\_packet \*cpkt, const uint8\_t \*payload, uint16\_t payload\_len)

Append payload to CoAP packet.

[coap\_replies\_clear](group__coap.md#gaddb02509934f5bac20b7c7f83aea4cd8)

void coap\_replies\_clear(struct coap\_reply \*replies, size\_t len)

Cancels all replies, so they become available again.

[coap\_next\_id](group__coap.md#gade5f4995c6419db03ce3e7ff7ca1cfcb)

uint16\_t coap\_next\_id(void)

Helper to generate message ids.

[coap\_find\_observer\_by\_token](group__coap.md#gadeaa59fd7b6eab454d5930289b4e08f7)

struct coap\_observer \* coap\_find\_observer\_by\_token(struct coap\_observer \*observers, size\_t len, const uint8\_t \*token, uint8\_t token\_len)

Returns the observer that has token token.

[coap\_header\_get\_code](group__coap.md#gae4bf952fdf9e3d03ab0b0df4c3c0d054)

uint8\_t coap\_header\_get\_code(const struct coap\_packet \*cpkt)

Returns the code of the CoAP packet.

[coap\_ack\_init](group__coap.md#gae6d93b1f93734302be75ee417813e5d1)

int coap\_ack\_init(struct coap\_packet \*cpkt, const struct coap\_packet \*req, uint8\_t \*data, uint16\_t max\_len, uint8\_t code)

Create a new CoAP Acknowledgment message for given request.

[coap\_header\_get\_type](group__coap.md#gaed883ea6cec3acc5eb570e152dc52e25)

uint8\_t coap\_header\_get\_type(const struct coap\_packet \*cpkt)

Returns the type of the CoAP packet.

[coap\_find\_options](group__coap.md#gaf006c8048ed7b863e70dbdd64bc3d608)

int coap\_find\_options(const struct coap\_packet \*cpkt, uint16\_t code, struct coap\_option \*options, uint16\_t veclen)

Return the values associated with the option of value code.

[coap\_set\_transmission\_parameters](group__coap.md#gaf361fd233f1aa650650108ae1e205ede)

void coap\_set\_transmission\_parameters(const struct coap\_transmission\_parameters \*params)

Set CoAP transmission parameters.

[coap\_find\_observer](group__coap.md#gaf9c1a55aee52588df2694ea947db5db4)

struct coap\_observer \* coap\_find\_observer(struct coap\_observer \*observers, size\_t len, const struct sockaddr \*addr, const uint8\_t \*token, uint8\_t token\_len)

Returns the observer that matches address addr and has token token.

[coap\_append\_size2\_option](group__coap.md#gafbc8c15ef03b762f9411c38b03aa403b)

int coap\_append\_size2\_option(struct coap\_packet \*cpkt, struct coap\_block\_context \*ctx)

Append SIZE2 option to the packet.

[coap\_block\_has\_more](group__coap.md#gafc61a6878d82f81565ab752ced0ce2be)

bool coap\_block\_has\_more(struct coap\_packet \*cpkt)

Check if BLOCK1 or BLOCK2 option has more flag set.

[coap\_header\_get\_version](group__coap.md#gafd01c39fac8f173edc04337161e92264)

uint8\_t coap\_header\_get\_version(const struct coap\_packet \*cpkt)

Returns the version present in a CoAP packet.

[coap\_header\_set\_code](group__coap.md#gafdaecca5ad26bab4fb7c9ee3477318f8)

int coap\_header\_set\_code(const struct coap\_packet \*cpkt, uint8\_t code)

Modifies the code of the CoAP packet.

[coap\_block\_size\_to\_bytes](group__coap.md#gafffadd4a837e48fd72af20468ccd86f2)

static uint16\_t coap\_block\_size\_to\_bytes(enum coap\_block\_size block\_size)

Helper for converting the enumeration to the size expressed in bytes.

**Definition** coap.h:759

[COAP\_RESPONSE\_CODE\_OK](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a0629da1898b934c3f699b98ff808c717)

@ COAP\_RESPONSE\_CODE\_OK

2.00 - OK

**Definition** coap.h:144

[COAP\_RESPONSE\_CODE\_INTERNAL\_ERROR](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499)

@ COAP\_RESPONSE\_CODE\_INTERNAL\_ERROR

5.00 - Internal Server Error

**Definition** coap.h:187

[COAP\_RESPONSE\_CODE\_PRECONDITION\_FAILED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a289ade02833b57bffd915e648e050e52)

@ COAP\_RESPONSE\_CODE\_PRECONDITION\_FAILED

4.12 - Precondition Failed

**Definition** coap.h:176

[COAP\_RESPONSE\_CODE\_NOT\_ALLOWED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a301eb722445472dba93d5accd6e0dd31)

@ COAP\_RESPONSE\_CODE\_NOT\_ALLOWED

4.05 - Method Not Allowed

**Definition** coap.h:168

[COAP\_RESPONSE\_CODE\_CHANGED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3)

@ COAP\_RESPONSE\_CODE\_CHANGED

2.04 - Changed

**Definition** coap.h:152

[COAP\_RESPONSE\_CODE\_NOT\_ACCEPTABLE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a4d77322514521e8dfea01f4a1a6e5886)

@ COAP\_RESPONSE\_CODE\_NOT\_ACCEPTABLE

4.06 - Not Acceptable

**Definition** coap.h:170

[COAP\_RESPONSE\_CODE\_UNPROCESSABLE\_ENTITY](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a5e5e31cc4647d5e0fdd1c8fe6cfa2661)

@ COAP\_RESPONSE\_CODE\_UNPROCESSABLE\_ENTITY

4.22 - Unprocessable Entity

**Definition** coap.h:183

[COAP\_RESPONSE\_CODE\_PROXYING\_NOT\_SUPPORTED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a5f49a566d37b2cda0c624d76aee08bd1)

@ COAP\_RESPONSE\_CODE\_PROXYING\_NOT\_SUPPORTED

5.05 - Proxying Not Supported

**Definition** coap.h:197

[COAP\_RESPONSE\_CODE\_BAD\_REQUEST](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5)

@ COAP\_RESPONSE\_CODE\_BAD\_REQUEST

4.00 - Bad Request

**Definition** coap.h:158

[COAP\_RESPONSE\_CODE\_INCOMPLETE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a671730c6d2f1a339fcd557c5452150af)

@ COAP\_RESPONSE\_CODE\_INCOMPLETE

4.08 - Request Entity Incomplete

**Definition** coap.h:172

[COAP\_RESPONSE\_CODE\_NOT\_IMPLEMENTED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a85c04541bc8580c2ae915946fd677c15)

@ COAP\_RESPONSE\_CODE\_NOT\_IMPLEMENTED

5.01 - Not Implemented

**Definition** coap.h:189

[COAP\_RESPONSE\_CODE\_NOT\_FOUND](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a86c2bff8add69428d164431b3091a8e9)

@ COAP\_RESPONSE\_CODE\_NOT\_FOUND

4.04 - Not Found

**Definition** coap.h:166

[COAP\_RESPONSE\_CODE\_BAD\_GATEWAY](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a8de29a7ee6bb960a97d6b415217b4640)

@ COAP\_RESPONSE\_CODE\_BAD\_GATEWAY

5.02 - Bad Gateway

**Definition** coap.h:191

[COAP\_RESPONSE\_CODE\_BAD\_OPTION](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a989a6528edc653c0b693ed875481e82d)

@ COAP\_RESPONSE\_CODE\_BAD\_OPTION

4.02 - Bad Option

**Definition** coap.h:162

[COAP\_RESPONSE\_CODE\_REQUEST\_TOO\_LARGE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aaa43062a8146c1e2e09183228a540d2e)

@ COAP\_RESPONSE\_CODE\_REQUEST\_TOO\_LARGE

4.13 - Request Entity Too Large

**Definition** coap.h:178

[COAP\_RESPONSE\_CODE\_TOO\_MANY\_REQUESTS](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aabd72cff6669d382aa04c53e764d0b49)

@ COAP\_RESPONSE\_CODE\_TOO\_MANY\_REQUESTS

4.29 - Too Many Requests

**Definition** coap.h:185

[COAP\_RESPONSE\_CODE\_CONFLICT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ab447505d233aed9fd8ad28070d317544)

@ COAP\_RESPONSE\_CODE\_CONFLICT

4.12 - Precondition Failed

**Definition** coap.h:174

[COAP\_RESPONSE\_CODE\_DELETED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26abf324915aa498c64a733a0098de4a082)

@ COAP\_RESPONSE\_CODE\_DELETED

2.02 - Deleted

**Definition** coap.h:148

[COAP\_RESPONSE\_CODE\_UNAUTHORIZED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26acb76dbf11b47477144cc4ece3357283c)

@ COAP\_RESPONSE\_CODE\_UNAUTHORIZED

4.01 - Unauthorized

**Definition** coap.h:160

[COAP\_RESPONSE\_CODE\_CREATED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ad2d9fe8dd5beda74b522377c0b76275b)

@ COAP\_RESPONSE\_CODE\_CREATED

2.01 - Created

**Definition** coap.h:146

[COAP\_RESPONSE\_CODE\_CONTENT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26adfd3e5e3c6ad5715127bb444c205fbce)

@ COAP\_RESPONSE\_CODE\_CONTENT

2.05 - Content

**Definition** coap.h:154

[COAP\_RESPONSE\_CODE\_CONTINUE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ae4e3ff451c626421b9b329790f019dd8)

@ COAP\_RESPONSE\_CODE\_CONTINUE

2.31 - Continue

**Definition** coap.h:156

[COAP\_RESPONSE\_CODE\_VALID](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aecaac4a0e9c821dfc20536951409dd48)

@ COAP\_RESPONSE\_CODE\_VALID

2.03 - Valid

**Definition** coap.h:150

[COAP\_RESPONSE\_CODE\_UNSUPPORTED\_CONTENT\_FORMAT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aef6b165b9d3f8f4b477431058815c16b)

@ COAP\_RESPONSE\_CODE\_UNSUPPORTED\_CONTENT\_FORMAT

4.15 - Unsupported Content-Format

**Definition** coap.h:180

[COAP\_RESPONSE\_CODE\_GATEWAY\_TIMEOUT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26af6d379fef704c269406b782c60772ecd)

@ COAP\_RESPONSE\_CODE\_GATEWAY\_TIMEOUT

5.04 - Gateway Timeout

**Definition** coap.h:195

[COAP\_RESPONSE\_CODE\_SERVICE\_UNAVAILABLE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26afebd274586351951ffe9c8f26b270dec)

@ COAP\_RESPONSE\_CODE\_SERVICE\_UNAVAILABLE

5.03 - Service Unavailable

**Definition** coap.h:193

[COAP\_RESPONSE\_CODE\_FORBIDDEN](group__coap.md#gga1ea81a365834e96f43ab7be573069d26afeee555ef54f138db58b14ad2c328d04)

@ COAP\_RESPONSE\_CODE\_FORBIDDEN

4.03 - Forbidden

**Definition** coap.h:164

[COAP\_NO\_RESPONSE\_SUPPRESS\_5\_XX](group__coap.md#gga2a323287262bbb6a4932e7911ddb652ca19ebfb46899b440124322bb67c906cb3)

@ COAP\_NO\_RESPONSE\_SUPPRESS\_5\_XX

**Definition** coap.h:235

[COAP\_NO\_RESPONSE\_SUPPRESS\_ALL](group__coap.md#gga2a323287262bbb6a4932e7911ddb652ca21758021d7f3a36bf6ede06daa82dbf0)

@ COAP\_NO\_RESPONSE\_SUPPRESS\_ALL

**Definition** coap.h:237

[COAP\_NO\_RESPONSE\_SUPPRESS\_4\_XX](group__coap.md#gga2a323287262bbb6a4932e7911ddb652cae8b0b1231d095b3e7a972ca4c86d8dce)

@ COAP\_NO\_RESPONSE\_SUPPRESS\_4\_XX

**Definition** coap.h:234

[COAP\_NO\_RESPONSE\_SUPPRESS\_2\_XX](group__coap.md#gga2a323287262bbb6a4932e7911ddb652caeeb51bb18780c20df5b25183d52d42de)

@ COAP\_NO\_RESPONSE\_SUPPRESS\_2\_XX

**Definition** coap.h:233

[COAP\_TYPE\_RESET](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa287b951159fd51b84a2e0491b012f84c)

@ COAP\_TYPE\_RESET

Reset.

**Definition** coap.h:126

[COAP\_TYPE\_NON\_CON](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa629a304bea0c85c7b2bf746b26216a4f)

@ COAP\_TYPE\_NON\_CON

Non-confirmable message.

**Definition** coap.h:113

[COAP\_TYPE\_CON](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa65c04ee4847d0c595238079ac9564e8d)

@ COAP\_TYPE\_CON

Confirmable message.

**Definition** coap.h:106

[COAP\_TYPE\_ACK](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa7b2fe2187018bce9132af2763b57307d)

@ COAP\_TYPE\_ACK

Acknowledge.

**Definition** coap.h:119

[COAP\_METHOD\_GET](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a025300cb0dc4c4de8eb0b0e0b4eb5317)

@ COAP\_METHOD\_GET

GET.

**Definition** coap.h:77

[COAP\_METHOD\_IPATCH](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a78f97b895f29819bf3f8b0314967f20e)

@ COAP\_METHOD\_IPATCH

IPATCH.

**Definition** coap.h:83

[COAP\_METHOD\_PUT](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a91637ef7c9f57cdcc65d0118008251db)

@ COAP\_METHOD\_PUT

PUT.

**Definition** coap.h:79

[COAP\_METHOD\_POST](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7aba51bcab79bf75080ccf75c1ec38a3d6)

@ COAP\_METHOD\_POST

POST.

**Definition** coap.h:78

[COAP\_METHOD\_PATCH](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7adca55e3d2b4b41b249f6b2f67074d708)

@ COAP\_METHOD\_PATCH

PATCH.

**Definition** coap.h:82

[COAP\_METHOD\_DELETE](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7adccbea1fe9a43433cf8471e32208a5ac)

@ COAP\_METHOD\_DELETE

DELETE.

**Definition** coap.h:80

[COAP\_METHOD\_FETCH](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7afa4070fed5c01b28bb1a59e3f0c021f4)

@ COAP\_METHOD\_FETCH

FETCH.

**Definition** coap.h:81

[COAP\_BLOCK\_128](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a147ddf4b0e5d1a8c11f0da2c71dee4d8)

@ COAP\_BLOCK\_128

128-byte block size

**Definition** coap.h:745

[COAP\_BLOCK\_32](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a1aaf8f841c18e281b176793bb331993d)

@ COAP\_BLOCK\_32

32-byte block size

**Definition** coap.h:743

[COAP\_BLOCK\_1024](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce)

@ COAP\_BLOCK\_1024

1024-byte block size

**Definition** coap.h:748

[COAP\_BLOCK\_64](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a7266f448a391ea2a2763f1ded5397520)

@ COAP\_BLOCK\_64

64-byte block size

**Definition** coap.h:744

[COAP\_BLOCK\_16](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968)

@ COAP\_BLOCK\_16

16-byte block size

**Definition** coap.h:742

[COAP\_BLOCK\_256](group__coap.md#gga712c1468f936a3af7dc39a86a5961922acfc37f84eabccdde4bd84b06c6a5e753)

@ COAP\_BLOCK\_256

256-byte block size

**Definition** coap.h:746

[COAP\_BLOCK\_512](group__coap.md#gga712c1468f936a3af7dc39a86a5961922ad2052905aff08c58585dcf6c6caddc19)

@ COAP\_BLOCK\_512

512-byte block size

**Definition** coap.h:747

[COAP\_OPTION\_OBSERVE](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a06e91bbb4fa2144543d4148d3245ad25)

@ COAP\_OPTION\_OBSERVE

Observe (RFC 7641).

**Definition** coap.h:51

[COAP\_OPTION\_IF\_NONE\_MATCH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a07ea6f395818a7019bb9e6a6e34d2d74)

@ COAP\_OPTION\_IF\_NONE\_MATCH

If-None-Match.

**Definition** coap.h:50

[COAP\_OPTION\_ETAG](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a0efdc30ce5551daffd093b2a8466978a)

@ COAP\_OPTION\_ETAG

ETag.

**Definition** coap.h:49

[COAP\_OPTION\_SIZE2](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a26c1bcd7af4fccd949e3de35fc2d88e6)

@ COAP\_OPTION\_SIZE2

Size2 (RFC 7959).

**Definition** coap.h:62

[COAP\_OPTION\_REQUEST\_TAG](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2a47428ec35972d256da05104ea6396f)

@ COAP\_OPTION\_REQUEST\_TAG

Request-Tag (RFC 9175).

**Definition** coap.h:68

[COAP\_OPTION\_PROXY\_SCHEME](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a30da986503e1e15243b74a16b161901c)

@ COAP\_OPTION\_PROXY\_SCHEME

Proxy-Scheme.

**Definition** coap.h:64

[COAP\_OPTION\_URI\_PORT](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a344707b9f4cb71310f2ccf5e8050d17a)

@ COAP\_OPTION\_URI\_PORT

Uri-Port.

**Definition** coap.h:52

[COAP\_OPTION\_URI\_HOST](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a402bb0a642a07d951c35d69736fd3f33)

@ COAP\_OPTION\_URI\_HOST

Uri-Host.

**Definition** coap.h:48

[COAP\_OPTION\_BLOCK2](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972)

@ COAP\_OPTION\_BLOCK2

Block2 (RFC 7959).

**Definition** coap.h:60

[COAP\_OPTION\_IF\_MATCH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4c61e26d11841c76debe2f99de5e9756)

@ COAP\_OPTION\_IF\_MATCH

If-Match.

**Definition** coap.h:47

[COAP\_OPTION\_SIZE1](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a53169a1c7b07c9e97f79dfc06af3eb51)

@ COAP\_OPTION\_SIZE1

Size1.

**Definition** coap.h:65

[COAP\_OPTION\_ECHO](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a620e8b59f67f89de8a38dc76c8fcc594)

@ COAP\_OPTION\_ECHO

Echo (RFC 9175).

**Definition** coap.h:66

[COAP\_OPTION\_NO\_RESPONSE](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a7984f2c4845610491bda964111a1c8e7)

@ COAP\_OPTION\_NO\_RESPONSE

No-Response (RFC 7967).

**Definition** coap.h:67

[COAP\_OPTION\_BLOCK1](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a8aaa54af114fd1db631566afa69f162d)

@ COAP\_OPTION\_BLOCK1

Block1 (RFC 7959).

**Definition** coap.h:61

[COAP\_OPTION\_URI\_PATH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a96b5a15937e875b3087307cc5faab1af)

@ COAP\_OPTION\_URI\_PATH

Uri-Path.

**Definition** coap.h:54

[COAP\_OPTION\_MAX\_AGE](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ab4cda4d3732fd12b9f203a2475c20981)

@ COAP\_OPTION\_MAX\_AGE

Max-Age.

**Definition** coap.h:56

[COAP\_OPTION\_CONTENT\_FORMAT](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac3166e67b5f5bf3cefee58c8ff58e5b8)

@ COAP\_OPTION\_CONTENT\_FORMAT

Content-Format.

**Definition** coap.h:55

[COAP\_OPTION\_LOCATION\_QUERY](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac728800fc8f0d80e37dcf322e75eb27d)

@ COAP\_OPTION\_LOCATION\_QUERY

Location-Query.

**Definition** coap.h:59

[COAP\_OPTION\_URI\_QUERY](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3adb4d27052247b9a79ad7fcc0cc30c71c)

@ COAP\_OPTION\_URI\_QUERY

Uri-Query.

**Definition** coap.h:57

[COAP\_OPTION\_PROXY\_URI](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae4d2c93b545708926813217cd36a96ac)

@ COAP\_OPTION\_PROXY\_URI

Proxy-Uri.

**Definition** coap.h:63

[COAP\_OPTION\_LOCATION\_PATH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae82be3591d43f0d1c7e89ab764d969bd)

@ COAP\_OPTION\_LOCATION\_PATH

Location-Path.

**Definition** coap.h:53

[COAP\_OPTION\_ACCEPT](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3afd0725f0ceb5ce22a6c7b390ca7efc9d)

@ COAP\_OPTION\_ACCEPT

Accept.

**Definition** coap.h:58

[COAP\_CONTENT\_FORMAT\_APP\_JSON\_PATCH\_JSON](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a141f183724ad6da14c3992c0990d6239)

@ COAP\_CONTENT\_FORMAT\_APP\_JSON\_PATCH\_JSON

application/json-patch+json

**Definition** coap.h:221

[COAP\_CONTENT\_FORMAT\_APP\_LINK\_FORMAT](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a1fbd90fd5cb309e2de6954f46174dc4f)

@ COAP\_CONTENT\_FORMAT\_APP\_LINK\_FORMAT

application/link-format

**Definition** coap.h:216

[COAP\_CONTENT\_FORMAT\_APP\_MERGE\_PATCH\_JSON](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a2797149fb3811d706dab291e9edc9436)

@ COAP\_CONTENT\_FORMAT\_APP\_MERGE\_PATCH\_JSON

application/merge-patch+json

**Definition** coap.h:222

[COAP\_CONTENT\_FORMAT\_APP\_EXI](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a483a382550b38468cc66bdce9f4743ea)

@ COAP\_CONTENT\_FORMAT\_APP\_EXI

application/exi

**Definition** coap.h:219

[COAP\_CONTENT\_FORMAT\_APP\_CBOR](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a7ca73ff57a6c7fb1517b44f2ce17d3f9)

@ COAP\_CONTENT\_FORMAT\_APP\_CBOR

application/cbor

**Definition** coap.h:223

[COAP\_CONTENT\_FORMAT\_APP\_OCTET\_STREAM](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a88d952174bb3e4ffb9ab11a599952760)

@ COAP\_CONTENT\_FORMAT\_APP\_OCTET\_STREAM

application/octet-stream

**Definition** coap.h:218

[COAP\_CONTENT\_FORMAT\_APP\_JSON](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a975381d286c1e9b998e41ef0a234d17a)

@ COAP\_CONTENT\_FORMAT\_APP\_JSON

application/json

**Definition** coap.h:220

[COAP\_CONTENT\_FORMAT\_APP\_XML](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73adb96bf55e914f4852e92dc65752c372a)

@ COAP\_CONTENT\_FORMAT\_APP\_XML

application/xml

**Definition** coap.h:217

[COAP\_CONTENT\_FORMAT\_TEXT\_PLAIN](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73af068aa8d09032352799bc60868607997)

@ COAP\_CONTENT\_FORMAT\_TEXT\_PLAIN

text/plain;charset=utf-8

**Definition** coap.h:215

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:171

[u32\_count\_trailing\_zeros](group__math__extras.md#ga4cb313f98c3fd3b00d6f4db74a9a0076)

static int u32\_count\_trailing\_zeros(uint32\_t x)

Count the number of trailing zero bits in a 32-bit integer.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](include_2zephyr_2types_8h.md)

[math\_extras.h](math__extras_8h.md)

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[coap\_block\_context](structcoap__block__context.md)

Represents the current state of a block-wise transaction.

**Definition** coap.h:789

[coap\_block\_context::total\_size](structcoap__block__context.md#a27db79dc3a2af6dd9f41e3008dcde87a)

size\_t total\_size

Total size of the block-wise transaction.

**Definition** coap.h:791

[coap\_block\_context::block\_size](structcoap__block__context.md#a27eb897fa2d455eb79220f1654509da3)

enum coap\_block\_size block\_size

Block size.

**Definition** coap.h:795

[coap\_block\_context::current](structcoap__block__context.md#a474f54e2a29d41b9d449f8574e747067)

size\_t current

Current size of the block-wise transaction.

**Definition** coap.h:793

[coap\_observer](structcoap__observer.md)

Represents a remote device that is observing a local resource.

**Definition** coap.h:298

[coap\_observer::list](structcoap__observer.md#a24a9f853db17ff623f4c510fd0892eb5)

sys\_snode\_t list

Observer list node.

**Definition** coap.h:300

[coap\_observer::token](structcoap__observer.md#a6d7d792120b935bf61c739f95dd7361c)

uint8\_t token[8]

Observer token.

**Definition** coap.h:304

[coap\_observer::tkl](structcoap__observer.md#a901f148d2eb697206fde732050c3d8b4)

uint8\_t tkl

Extended token length.

**Definition** coap.h:306

[coap\_observer::addr](structcoap__observer.md#a9b6f807a0fc5d141e0ee3dd9596c3c82)

struct sockaddr addr

Observer connection end point information.

**Definition** coap.h:302

[coap\_option](structcoap__option.md)

Representation of a CoAP option.

**Definition** coap.h:331

[coap\_option::len](structcoap__option.md#a01c8abdf27c3f8c5a816af33c0c093d4)

uint8\_t len

Option length.

**Definition** coap.h:337

[coap\_option::delta](structcoap__option.md#abca15b0a8f9bdcb3f493ab3801d4b58f)

uint16\_t delta

Option delta.

**Definition** coap.h:332

[coap\_option::value](structcoap__option.md#aff07b5d3673169b6316b91dc27780891)

uint8\_t value[12]

Option value.

**Definition** coap.h:338

[coap\_packet](structcoap__packet.md)

Representation of a CoAP Packet.

**Definition** coap.h:312

[coap\_packet::offset](structcoap__packet.md#a46c0842c785b8de5eb8564950a786c02)

uint16\_t offset

CoAP lib maintains offset while adding data.

**Definition** coap.h:314

[coap\_packet::max\_len](structcoap__packet.md#a48c216a7da37e85942d271c85a79bcb6)

uint16\_t max\_len

Max CoAP packet data length.

**Definition** coap.h:315

[coap\_packet::data](structcoap__packet.md#a8116711bcdff1fa6b0cf5c4fa9ab88d1)

uint8\_t \* data

User allocated buffer.

**Definition** coap.h:313

[coap\_packet::delta](structcoap__packet.md#a95dd8c6fb08ac61a1571c84258579475)

uint16\_t delta

Used for delta calculation in CoAP packet.

**Definition** coap.h:318

[coap\_packet::hdr\_len](structcoap__packet.md#ab302c002da88f6d3a44c3a2215082be4)

uint8\_t hdr\_len

CoAP header length.

**Definition** coap.h:316

[coap\_packet::opt\_len](structcoap__packet.md#acc5542ba2a69db8957155b90e75fd563)

uint16\_t opt\_len

Total options length (delta + len + value).

**Definition** coap.h:317

[coap\_pending](structcoap__pending.md)

Represents a request awaiting for an acknowledgment (ACK).

**Definition** coap.h:376

[coap\_pending::params](structcoap__pending.md#a05ca08379d13e10dfe86322f666c3d97)

struct coap\_transmission\_parameters params

Transmission parameters.

**Definition** coap.h:384

[coap\_pending::data](structcoap__pending.md#a0a506507e472b3813e672f2b455e4bcc)

uint8\_t \* data

User allocated buffer.

**Definition** coap.h:381

[coap\_pending::len](structcoap__pending.md#a4eb95f8fadef7d42aecdf25cc5ee3b1d)

uint16\_t len

Length of the CoAP packet.

**Definition** coap.h:382

[coap\_pending::retries](structcoap__pending.md#a8aebb187845bcb6cb07dee68927f1aa6)

uint8\_t retries

Number of times the request has been sent.

**Definition** coap.h:383

[coap\_pending::id](structcoap__pending.md#a8b1952271bd0c733c2fbcb158b60ca99)

uint16\_t id

Message id.

**Definition** coap.h:380

[coap\_pending::t0](structcoap__pending.md#a8b95f80a6eaac759ed0895201ff089d9)

int64\_t t0

Time when the request was sent.

**Definition** coap.h:378

[coap\_pending::timeout](structcoap__pending.md#ab31339cc91df71ee6f90d5702f722fd6)

uint32\_t timeout

Timeout in ms.

**Definition** coap.h:379

[coap\_pending::addr](structcoap__pending.md#adcc34b0d0201a24b15a5adca89ae0da3)

struct sockaddr addr

Remote address.

**Definition** coap.h:377

[coap\_reply](structcoap__reply.md)

Represents the handler for the reply of a request, it is also used when observing resources.

**Definition** coap.h:391

[coap\_reply::tkl](structcoap__reply.md#a038ccb29c2abff6168db3247241a8cc3)

uint8\_t tkl

Extended token length.

**Definition** coap.h:403

[coap\_reply::token](structcoap__reply.md#a18d40c327933c30681b924446c21ea9d)

uint8\_t token[8]

Reply token.

**Definition** coap.h:401

[coap\_reply::reply](structcoap__reply.md#a6a888bbb5652761002ce26aba09352cc)

coap\_reply\_t reply

CoAP reply callback.

**Definition** coap.h:393

[coap\_reply::id](structcoap__reply.md#a94d17732056de3d8ecb3412c686091f8)

uint16\_t id

Reply id.

**Definition** coap.h:399

[coap\_reply::user\_data](structcoap__reply.md#aa951d9ba4eb7f8041e8e82df9c1401dc)

void \* user\_data

User specific opaque data.

**Definition** coap.h:395

[coap\_reply::age](structcoap__reply.md#aea6b98e109e270c08df1554c5eee65fe)

int age

Reply age.

**Definition** coap.h:397

[coap\_resource](structcoap__resource.md)

Description of CoAP resource.

**Definition** coap.h:280

[coap\_resource::post](structcoap__resource.md#a1efed8197d44aba3b63aaa9d9bb0f5bb)

coap\_method\_t post

**Definition** coap.h:282

[coap\_resource::user\_data](structcoap__resource.md#a202a83a5aa024a62bd25cc40f42e8d65)

void \* user\_data

User specific opaque data.

**Definition** coap.h:288

[coap\_resource::put](structcoap__resource.md#a3152a778e27e36fad7dd62985621d58b)

coap\_method\_t put

**Definition** coap.h:282

[coap\_resource::notify](structcoap__resource.md#a3199679fd990d757e9a500fbd7c653d7)

coap\_notify\_t notify

Notify function to call.

**Definition** coap.h:284

[coap\_resource::observers](structcoap__resource.md#a5035dc9c88c2b0ae557608e34ec14433)

sys\_slist\_t observers

List of resource observers.

**Definition** coap.h:290

[coap\_resource::fetch](structcoap__resource.md#a6975e84ebc67d6aff2efb755695518f5)

coap\_method\_t fetch

**Definition** coap.h:282

[coap\_resource::ipatch](structcoap__resource.md#a7657cb2e9bbac7f98e35b4ed33f13163)

coap\_method\_t ipatch

**Definition** coap.h:282

[coap\_resource::del](structcoap__resource.md#a77dfb6d59c25e6e58141226023bf59ea)

coap\_method\_t del

**Definition** coap.h:282

[coap\_resource::patch](structcoap__resource.md#aa0a5465fc5b49a566e3803a9f1638724)

coap\_method\_t patch

**Definition** coap.h:282

[coap\_resource::path](structcoap__resource.md#ada7a41309b6ca11612b17fabf6cd56c5)

const char \*const \* path

Resource path.

**Definition** coap.h:286

[coap\_resource::age](structcoap__resource.md#ae8e1b2b1920689913e0910a82a30e009)

int age

Resource age.

**Definition** coap.h:292

[coap\_resource::get](structcoap__resource.md#aebe880e3ccbd2441854dfa899dc72c13)

coap\_method\_t get

Which function to be called for each CoAP method.

**Definition** coap.h:282

[coap\_transmission\_parameters](structcoap__transmission__parameters.md)

CoAP transmission parameters.

**Definition** coap.h:357

[coap\_transmission\_parameters::ack\_random\_percent](structcoap__transmission__parameters.md#a0b43d9e3adfbf7cac09e1ffbbe1f8ce8)

uint16\_t ack\_random\_percent

Set CoAP ack random factor.

**Definition** coap.h:365

[coap\_transmission\_parameters::max\_retransmission](structcoap__transmission__parameters.md#a3a9b8bf0f2e00fc0981acdd86d404190)

uint8\_t max\_retransmission

Maximum number of retransmissions.

**Definition** coap.h:370

[coap\_transmission\_parameters::coap\_backoff\_percent](structcoap__transmission__parameters.md#a74c91235bf64fab5e7abc0c9f581e44c)

uint16\_t coap\_backoff\_percent

Set CoAP retry backoff factor.

**Definition** coap.h:368

[coap\_transmission\_parameters::ack\_timeout](structcoap__transmission__parameters.md#aca76954d785d04312fb834dc524f102c)

uint32\_t ack\_timeout

Initial ACK timeout.

**Definition** coap.h:359

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:388

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap.h](coap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
