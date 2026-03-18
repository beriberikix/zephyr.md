---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dai_8h_source.html
original_path: doxygen/html/dai_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dai.h

[Go to the documentation of this file.](dai_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DAI\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_DAI\_H\_

14

28

29#include <[errno.h](errno_8h.md)>

30

31#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

32#include <[zephyr/device.h](device_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 39](group__dai__interface.md#ga2a51e43f9a14435a64e428df0b393703)#define DAI\_FORMAT\_CLOCK\_PROVIDER\_MASK 0xf000

[ 41](group__dai__interface.md#gaef86b295b1a13cc91e53f8cdbb4cf008)#define DAI\_FORMAT\_PROTOCOL\_MASK 0x000f

[ 43](group__dai__interface.md#ga8891542769e33930342bb5039b57fda8)#define DAI\_FORMAT\_CLOCK\_INVERSION\_MASK 0x0f00

44

[ 51](group__dai__interface.md#ga840116b8b56fd0263a17791e7156975d)enum [dai\_clock\_provider](group__dai__interface.md#ga840116b8b56fd0263a17791e7156975d) {

[ 53](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3) [DAI\_CBP\_CFP](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3) = (0 << 12),

[ 55](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1) [DAI\_CBC\_CFP](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1) = (2 << 12),

[ 57](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b) [DAI\_CBP\_CFC](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b) = (3 << 12),

[ 59](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84) [DAI\_CBC\_CFC](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84) = (4 << 12),

60};

61

[ 67](group__dai__interface.md#ga3fa4c114ad6a3dd6a6015b6ab3d119a2)enum [dai\_protocol](group__dai__interface.md#ga3fa4c114ad6a3dd6a6015b6ab3d119a2) {

[ 68](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2) [DAI\_PROTO\_I2S](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2) = 1,

[ 69](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f) [DAI\_PROTO\_RIGHT\_J](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f),

[ 70](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b) [DAI\_PROTO\_LEFT\_J](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b),

[ 71](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3) [DAI\_PROTO\_DSP\_A](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3),

[ 72](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0) [DAI\_PROTO\_DSP\_B](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0),

[ 73](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758) [DAI\_PROTO\_PDM](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758),

74};

75

[ 82](group__dai__interface.md#gaf66ca0bbc1f8ba2f2b81caf92bd09b60)enum [dai\_clock\_inversion](group__dai__interface.md#gaf66ca0bbc1f8ba2f2b81caf92bd09b60) {

[ 84](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698) [DAI\_INVERSION\_NB\_NF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698) = 0,

[ 86](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43) [DAI\_INVERSION\_NB\_IF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43) = (2 << 8),

[ 88](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c) [DAI\_INVERSION\_IB\_NF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c) = (3 << 8),

[ 90](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1) [DAI\_INVERSION\_IB\_IF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1) = (4 << 8),

91};

92

[ 102](group__dai__interface.md#gac95242d83a2c2b477fcb9eb3da420797)enum [dai\_type](group__dai__interface.md#gac95242d83a2c2b477fcb9eb3da420797) {

[ 103](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe) [DAI\_LEGACY\_I2S](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe) = 0,

[ 104](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9) [DAI\_INTEL\_SSP](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9),

[ 105](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36) [DAI\_INTEL\_DMIC](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36),

[ 106](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326) [DAI\_INTEL\_HDA](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326),

[ 107](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141) [DAI\_INTEL\_ALH](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141),

[ 108](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec) [DAI\_IMX\_SAI](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec),

[ 109](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa) [DAI\_IMX\_ESAI](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa),

[ 110](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0) [DAI\_AMD\_BT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0),

[ 111](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b) [DAI\_AMD\_SP](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b),

[ 112](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75) [DAI\_AMD\_DMIC](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75),

[ 113](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00) [DAI\_MEDIATEK\_AFE](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00),

[ 114](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa) [DAI\_INTEL\_SSP\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa),

[ 115](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2) [DAI\_INTEL\_DMIC\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2),

[ 116](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b) [DAI\_INTEL\_HDA\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b),

[ 117](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976) [DAI\_INTEL\_ALH\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976),

118};

119

[ 123](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f)enum [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) {

[ 125](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c) [DAI\_DIR\_TX](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c) = 0,

[ 127](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b) [DAI\_DIR\_RX](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b),

[ 129](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1) [DAI\_DIR\_BOTH](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1),

130};

131

[ 133](group__dai__interface.md#ga18f708594ea85d6b893906336047c3a5)enum [dai\_state](group__dai__interface.md#ga18f708594ea85d6b893906336047c3a5) {

[ 140](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987) [DAI\_STATE\_NOT\_READY](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987) = 0,

[ 142](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650) [DAI\_STATE\_READY](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650),

[ 144](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f) [DAI\_STATE\_RUNNING](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f),

[ 146](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953) [DAI\_STATE\_PRE\_RUNNING](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953),

[ 148](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13) [DAI\_STATE\_PAUSED](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13),

[ 150](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b) [DAI\_STATE\_STOPPING](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b),

[ 152](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef) [DAI\_STATE\_ERROR](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef),

153};

154

[ 156](group__dai__interface.md#gaee6445967afb3ecf2c0470ca0c104a1a)enum [dai\_trigger\_cmd](group__dai__interface.md#gaee6445967afb3ecf2c0470ca0c104a1a) {

[ 163](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222) [DAI\_TRIGGER\_START](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222) = 0,

[ 169](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec) [DAI\_TRIGGER\_PRE\_START](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec),

[ 179](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35) [DAI\_TRIGGER\_STOP](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35),

[ 187](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5) [DAI\_TRIGGER\_PAUSE](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5),

[ 193](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3) [DAI\_TRIGGER\_POST\_STOP](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3),

[ 202](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02) [DAI\_TRIGGER\_DRAIN](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02),

[ 209](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234) [DAI\_TRIGGER\_DROP](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234),

[ 215](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70) [DAI\_TRIGGER\_PREPARE](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70),

[ 221](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711) [DAI\_TRIGGER\_RESET](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711),

[ 226](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f) [DAI\_TRIGGER\_COPY](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f),

227};

228

[ 235](structdai__properties.md)struct [dai\_properties](structdai__properties.md) {

[ 237](structdai__properties.md#a98053c85634b80b144bda05d83f2eb7e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fifo\_address](structdai__properties.md#a98053c85634b80b144bda05d83f2eb7e);

[ 239](structdai__properties.md#a9b056f0ff59b473d3040851642d1601c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fifo\_depth](structdai__properties.md#a9b056f0ff59b473d3040851642d1601c);

[ 241](structdai__properties.md#a7203f5c97aaf8f48f9eb51d88424afce) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dma\_hs\_id](structdai__properties.md#a7203f5c97aaf8f48f9eb51d88424afce);

[ 243](structdai__properties.md#a8fc2d359fe889b3a46ecc8918a82f680) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reg\_init\_delay](structdai__properties.md#a8fc2d359fe889b3a46ecc8918a82f680);

[ 245](structdai__properties.md#adab0f1199c7169a521329adc98c2f0ac) int [stream\_id](structdai__properties.md#adab0f1199c7169a521329adc98c2f0ac);

246};

247

[ 252](structdai__config.md)struct [dai\_config](structdai__config.md) {

[ 254](structdai__config.md#acfb621417b789c71608ad50d0b54c1f6) enum [dai\_type](group__dai__interface.md#gac95242d83a2c2b477fcb9eb3da420797) [type](structdai__config.md#acfb621417b789c71608ad50d0b54c1f6);

[ 256](structdai__config.md#aecb9fe475d71d55d8b19eb3faa697606) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dai\_index](structdai__config.md#aecb9fe475d71d55d8b19eb3faa697606);

[ 258](structdai__config.md#ac3f39c351ad9659356ad5ad4306585b8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channels](structdai__config.md#ac3f39c351ad9659356ad5ad4306585b8);

[ 260](structdai__config.md#a2d46087a3c94845d52b44386dd20cfc0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rate](structdai__config.md#a2d46087a3c94845d52b44386dd20cfc0);

[ 262](structdai__config.md#ac2c2c4a39bfe917d5a784d8bc596eb10) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [format](structdai__config.md#ac2c2c4a39bfe917d5a784d8bc596eb10);

[ 264](structdai__config.md#ac8b2936e194421f95d03e1c595017306) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [options](structdai__config.md#ac8b2936e194421f95d03e1c595017306);

[ 266](structdai__config.md#afe7ab1b6c1163ca1bf4141bc6f2439ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [word\_size](structdai__config.md#afe7ab1b6c1163ca1bf4141bc6f2439ba);

[ 268](structdai__config.md#af3c768d9597298cea94bbdd6e5b5c4f3) size\_t [block\_size](structdai__config.md#af3c768d9597298cea94bbdd6e5b5c4f3);

[ 270](structdai__config.md#afd3bcee428b5359b7151a269973049a1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [link\_config](structdai__config.md#afd3bcee428b5359b7151a269973049a1);

[ 272](structdai__config.md#a32830675c7bf7125c5006579d33e5e96) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tdm\_slot\_group](structdai__config.md#a32830675c7bf7125c5006579d33e5e96);

273};

274

[ 278](structdai__ts__cfg.md)struct [dai\_ts\_cfg](structdai__ts__cfg.md) {

[ 280](structdai__ts__cfg.md#ac17d3da9de6d860f2fa04286a4c43a1d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [walclk\_rate](structdai__ts__cfg.md#ac17d3da9de6d860f2fa04286a4c43a1d);

[ 282](structdai__ts__cfg.md#a2b0be9c840de941e4a87c422fa82356d) int [type](structdai__ts__cfg.md#a2b0be9c840de941e4a87c422fa82356d);

[ 284](structdai__ts__cfg.md#afdaf1a4ef6a00201b3790187ec44370f) int [direction](structdai__ts__cfg.md#afdaf1a4ef6a00201b3790187ec44370f);

[ 286](structdai__ts__cfg.md#aff3dc52737d1261cd56c084c104691eb) int [index](structdai__ts__cfg.md#aff3dc52737d1261cd56c084c104691eb);

[ 288](structdai__ts__cfg.md#ab874249dcb9377fafa35764b4f1c0ea0) int [dma\_id](structdai__ts__cfg.md#ab874249dcb9377fafa35764b4f1c0ea0);

[ 290](structdai__ts__cfg.md#aa87fc1e3072490e44f65bc7690f85ce8) int [dma\_chan\_index](structdai__ts__cfg.md#aa87fc1e3072490e44f65bc7690f85ce8);

[ 292](structdai__ts__cfg.md#a37c6379686435994b9050d1e9c249756) int [dma\_chan\_count](structdai__ts__cfg.md#a37c6379686435994b9050d1e9c249756);

293};

294

[ 298](structdai__ts__data.md)struct [dai\_ts\_data](structdai__ts__data.md) {

[ 300](structdai__ts__data.md#a11133d72485786e75a9d94f218fe699b) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [walclk](structdai__ts__data.md#a11133d72485786e75a9d94f218fe699b);

[ 302](structdai__ts__data.md#a933cbc19cc837683581db806702fba36) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sample](structdai__ts__data.md#a933cbc19cc837683581db806702fba36);

[ 304](structdai__ts__data.md#ace2686aa6ff5aed346705cbb0d198d36) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [walclk\_rate](structdai__ts__data.md#ace2686aa6ff5aed346705cbb0d198d36);

305};

306

312\_\_subsystem struct dai\_driver\_api {

313 int (\*probe)(const struct [device](structdevice.md) \*dev);

314 int (\*remove)(const struct [device](structdevice.md) \*dev);

315 int (\*config\_set)(const struct [device](structdevice.md) \*dev, const struct [dai\_config](structdai__config.md) \*cfg,

316 const void \*bespoke\_cfg);

317 int (\*config\_get)(const struct [device](structdevice.md) \*dev, struct [dai\_config](structdai__config.md) \*cfg,

318 enum [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) dir);

319

320 const struct [dai\_properties](structdai__properties.md) \*(\*get\_properties)(const struct [device](structdevice.md) \*dev,

321 enum [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) dir,

322 int stream\_id);

323

324 int (\*trigger)(const struct [device](structdevice.md) \*dev, enum [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) dir,

325 enum [dai\_trigger\_cmd](group__dai__interface.md#gaee6445967afb3ecf2c0470ca0c104a1a) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

326

327 /\* optional methods \*/

328 int (\*ts\_config)(const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg);

329 int (\*ts\_start)(const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg);

330 int (\*ts\_stop)(const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg);

331 int (\*ts\_get)(const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg,

332 struct [dai\_ts\_data](structdai__ts__data.md) \*tsd);

333};

334

338

[ 350](group__dai__interface.md#ga40d5fd2676a9195c07fd7382aa1cea4a)static inline int [dai\_probe](group__dai__interface.md#ga40d5fd2676a9195c07fd7382aa1cea4a)(const struct [device](structdevice.md) \*dev)

351{

352 const struct dai\_driver\_api \*api = (const struct dai\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

353

354 return api->probe(dev);

355}

356

[ 367](group__dai__interface.md#ga91482e349a735a927fa396f4636247e5)static inline int [dai\_remove](group__dai__interface.md#ga91482e349a735a927fa396f4636247e5)(const struct [device](structdevice.md) \*dev)

368{

369 const struct dai\_driver\_api \*api = (const struct dai\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

370

371 return api->remove(dev);

372}

373

[ 394](group__dai__interface.md#ga182f79eeaf83ba8936298fcc93ad760a)static inline int [dai\_config\_set](group__dai__interface.md#ga182f79eeaf83ba8936298fcc93ad760a)(const struct [device](structdevice.md) \*dev,

395 const struct [dai\_config](structdai__config.md) \*cfg,

396 const void \*bespoke\_cfg)

397{

398 const struct dai\_driver\_api \*api = (const struct dai\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

399

400 return api->config\_set(dev, cfg, bespoke\_cfg);

401}

402

[ 411](group__dai__interface.md#gab093045778b0d0d1eee06e50e8c6481b)static inline int [dai\_config\_get](group__dai__interface.md#gab093045778b0d0d1eee06e50e8c6481b)(const struct [device](structdevice.md) \*dev,

412 struct [dai\_config](structdai__config.md) \*cfg,

413 enum [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) dir)

414{

415 const struct dai\_driver\_api \*api = (const struct dai\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

416

417 return api->config\_get(dev, cfg, dir);

418}

419

[ 430](group__dai__interface.md#gac732c8b3e737ecca187f38e308d95724)static inline const struct [dai\_properties](structdai__properties.md) \*[dai\_get\_properties](group__dai__interface.md#gac732c8b3e737ecca187f38e308d95724)(const struct [device](structdevice.md) \*dev,

431 enum [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) dir,

432 int [stream\_id](structdai__properties.md#adab0f1199c7169a521329adc98c2f0ac))

433{

434 const struct dai\_driver\_api \*api = (const struct dai\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

435

436 return api->get\_properties(dev, dir, stream\_id);

437}

438

[ 456](group__dai__interface.md#gabea217717edd2e986efeb475bbbc2208)static inline int [dai\_trigger](group__dai__interface.md#gabea217717edd2e986efeb475bbbc2208)(const struct [device](structdevice.md) \*dev,

457 enum [dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f) dir,

458 enum [dai\_trigger\_cmd](group__dai__interface.md#gaee6445967afb3ecf2c0470ca0c104a1a) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615))

459{

460 const struct dai\_driver\_api \*api = (const struct dai\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

461

462 return api->trigger(dev, dir, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

463}

464

[ 474](group__dai__interface.md#gac401703e4054d1eeeaf619b295f5d6d8)static inline int [dai\_ts\_config](group__dai__interface.md#gac401703e4054d1eeeaf619b295f5d6d8)(const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg)

475{

476 const struct dai\_driver\_api \*api = (const struct dai\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

477

478 if (!api->ts\_config)

479 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

480

481 return api->ts\_config(dev, cfg);

482}

483

[ 493](group__dai__interface.md#ga3dd0fd529c091d64dcb92d0c579a34ad)static inline int [dai\_ts\_start](group__dai__interface.md#ga3dd0fd529c091d64dcb92d0c579a34ad)(const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg)

494{

495 const struct dai\_driver\_api \*api = (const struct dai\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

496

497 if (!api->ts\_start)

498 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

499

500 return api->ts\_start(dev, cfg);

501}

502

[ 512](group__dai__interface.md#gaa3f2e59655c13101faf91ab2a6fd2f5e)static inline int [dai\_ts\_stop](group__dai__interface.md#gaa3f2e59655c13101faf91ab2a6fd2f5e)(const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg)

513{

514 const struct dai\_driver\_api \*api = (const struct dai\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

515

516 if (!api->ts\_stop)

517 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

518

519 return api->ts\_stop(dev, cfg);

520}

521

[ 532](group__dai__interface.md#gaf6a4127a0edb48814aebf2f3fbaa3651)static inline int [dai\_ts\_get](group__dai__interface.md#gaf6a4127a0edb48814aebf2f3fbaa3651)(const struct [device](structdevice.md) \*dev, struct [dai\_ts\_cfg](structdai__ts__cfg.md) \*cfg,

533 struct [dai\_ts\_data](structdai__ts__data.md) \*tsd)

534{

535 const struct dai\_driver\_api \*api = (const struct dai\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

536

537 if (!api->ts\_get)

538 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

539

540 return api->ts\_get(dev, cfg, tsd);

541}

542

546

547#ifdef \_\_cplusplus

548}

549#endif

550

551#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DAI\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[dai\_config\_set](group__dai__interface.md#ga182f79eeaf83ba8936298fcc93ad760a)

static int dai\_config\_set(const struct device \*dev, const struct dai\_config \*cfg, const void \*bespoke\_cfg)

Configure operation of a DAI driver.

**Definition** dai.h:394

[dai\_state](group__dai__interface.md#ga18f708594ea85d6b893906336047c3a5)

dai\_state

Interface state.

**Definition** dai.h:133

[dai\_ts\_start](group__dai__interface.md#ga3dd0fd529c091d64dcb92d0c579a34ad)

static int dai\_ts\_start(const struct device \*dev, struct dai\_ts\_cfg \*cfg)

Starts timestamping.

**Definition** dai.h:493

[dai\_protocol](group__dai__interface.md#ga3fa4c114ad6a3dd6a6015b6ab3d119a2)

dai\_protocol

DAI protocol.

**Definition** dai.h:67

[dai\_probe](group__dai__interface.md#ga40d5fd2676a9195c07fd7382aa1cea4a)

static int dai\_probe(const struct device \*dev)

Probe operation of DAI driver.

**Definition** dai.h:350

[dai\_clock\_provider](group__dai__interface.md#ga840116b8b56fd0263a17791e7156975d)

dai\_clock\_provider

DAI clock configurations.

**Definition** dai.h:51

[dai\_remove](group__dai__interface.md#ga91482e349a735a927fa396f4636247e5)

static int dai\_remove(const struct device \*dev)

Remove operation of DAI driver.

**Definition** dai.h:367

[dai\_ts\_stop](group__dai__interface.md#gaa3f2e59655c13101faf91ab2a6fd2f5e)

static int dai\_ts\_stop(const struct device \*dev, struct dai\_ts\_cfg \*cfg)

Stops timestamping.

**Definition** dai.h:512

[dai\_config\_get](group__dai__interface.md#gab093045778b0d0d1eee06e50e8c6481b)

static int dai\_config\_get(const struct device \*dev, struct dai\_config \*cfg, enum dai\_dir dir)

Fetch configuration information of a DAI driver.

**Definition** dai.h:411

[dai\_trigger](group__dai__interface.md#gabea217717edd2e986efeb475bbbc2208)

static int dai\_trigger(const struct device \*dev, enum dai\_dir dir, enum dai\_trigger\_cmd cmd)

Send a trigger command.

**Definition** dai.h:456

[dai\_ts\_config](group__dai__interface.md#gac401703e4054d1eeeaf619b295f5d6d8)

static int dai\_ts\_config(const struct device \*dev, struct dai\_ts\_cfg \*cfg)

Configures timestamping in attached DAI.

**Definition** dai.h:474

[dai\_get\_properties](group__dai__interface.md#gac732c8b3e737ecca187f38e308d95724)

static const struct dai\_properties \* dai\_get\_properties(const struct device \*dev, enum dai\_dir dir, int stream\_id)

Fetch properties of a DAI driver.

**Definition** dai.h:430

[dai\_type](group__dai__interface.md#gac95242d83a2c2b477fcb9eb3da420797)

dai\_type

Types of DAI.

**Definition** dai.h:102

[dai\_trigger\_cmd](group__dai__interface.md#gaee6445967afb3ecf2c0470ca0c104a1a)

dai\_trigger\_cmd

Trigger command.

**Definition** dai.h:156

[dai\_clock\_inversion](group__dai__interface.md#gaf66ca0bbc1f8ba2f2b81caf92bd09b60)

dai\_clock\_inversion

DAI clock inversion.

**Definition** dai.h:82

[dai\_ts\_get](group__dai__interface.md#gaf6a4127a0edb48814aebf2f3fbaa3651)

static int dai\_ts\_get(const struct device \*dev, struct dai\_ts\_cfg \*cfg, struct dai\_ts\_data \*tsd)

Gets timestamp.

**Definition** dai.h:532

[dai\_dir](group__dai__interface.md#gafa7b22e4250c6479301fc657fea8a60f)

dai\_dir

DAI Direction.

**Definition** dai.h:123

[DAI\_STATE\_READY](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a095422b1a71b65e5a5902e0ca5cd3650)

@ DAI\_STATE\_READY

The interface is ready to receive / transmit data.

**Definition** dai.h:142

[DAI\_STATE\_PRE\_RUNNING](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a234306cd9cc97674455f8a9321834953)

@ DAI\_STATE\_PRE\_RUNNING

The interface is clocking but not receiving / transmitting data.

**Definition** dai.h:146

[DAI\_STATE\_ERROR](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a5030da046fda46120d9b54a686fb35ef)

@ DAI\_STATE\_ERROR

TX buffer underrun or RX buffer overrun has occurred.

**Definition** dai.h:152

[DAI\_STATE\_NOT\_READY](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a8486be6ff6f6bf91ee4a8ad632377987)

@ DAI\_STATE\_NOT\_READY

The interface is not ready.

**Definition** dai.h:140

[DAI\_STATE\_RUNNING](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5a8692bbb3fce619aec3dfe5ed9697f73f)

@ DAI\_STATE\_RUNNING

The interface is receiving / transmitting data.

**Definition** dai.h:144

[DAI\_STATE\_STOPPING](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5aba10f89376d67abdc3dc704c6b283d2b)

@ DAI\_STATE\_STOPPING

The interface is draining its transmit queue.

**Definition** dai.h:150

[DAI\_STATE\_PAUSED](group__dai__interface.md#gga18f708594ea85d6b893906336047c3a5acb4e0c1f9df9eb0b7cf965b710a2ad13)

@ DAI\_STATE\_PAUSED

The interface paused.

**Definition** dai.h:148

[DAI\_PROTO\_LEFT\_J](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a0d0f5db48e33cef8aa6c59a00792866b)

@ DAI\_PROTO\_LEFT\_J

Left Justified.

**Definition** dai.h:70

[DAI\_PROTO\_PDM](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a3235bf6888b65c9c6e3a0d2f95fc0758)

@ DAI\_PROTO\_PDM

Pulse Density Modulation.

**Definition** dai.h:73

[DAI\_PROTO\_DSP\_A](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a6ffdc334c0f64feeb95297293f747bc3)

@ DAI\_PROTO\_DSP\_A

TDM, FSYNC asserted 1 BCLK early.

**Definition** dai.h:71

[DAI\_PROTO\_RIGHT\_J](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2a9ed5273ee9ea0761ccf9cbc7f7295a3f)

@ DAI\_PROTO\_RIGHT\_J

Right Justified.

**Definition** dai.h:69

[DAI\_PROTO\_I2S](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2adf515857c95ea685a32bf18c0ebb9af2)

@ DAI\_PROTO\_I2S

I2S.

**Definition** dai.h:68

[DAI\_PROTO\_DSP\_B](group__dai__interface.md#gga3fa4c114ad6a3dd6a6015b6ab3d119a2aea1fd67c47f7d8d7e3ca18b2f2e806a0)

@ DAI\_PROTO\_DSP\_B

TDM, FSYNC asserted at the same time as MSB.

**Definition** dai.h:72

[DAI\_CBP\_CFP](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da347440e41adadd2b6a91076f53abe2e3)

@ DAI\_CBP\_CFP

codec BLCK provider, codec FSYNC provider

**Definition** dai.h:53

[DAI\_CBP\_CFC](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da4baee3a3ab87e540b5f4caf26e8d8c4b)

@ DAI\_CBP\_CFC

codec BCLK consumer, codec FSYNC consumer

**Definition** dai.h:57

[DAI\_CBC\_CFC](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975da9f8f99d63e607d9603f54d535bd89f84)

@ DAI\_CBC\_CFC

**Definition** dai.h:59

[DAI\_CBC\_CFP](group__dai__interface.md#gga840116b8b56fd0263a17791e7156975daf4862a3af6fb46f6ac9ffc0cdbbcf0a1)

@ DAI\_CBC\_CFP

codec BCLK provider, codec FSYNC consumer

**Definition** dai.h:55

[DAI\_INTEL\_ALH](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a19dd111b0d7f7772415bc60c1256d141)

@ DAI\_INTEL\_ALH

Intel ALH.

**Definition** dai.h:107

[DAI\_INTEL\_HDA](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a1a591d4c0b7a70e175fc967b59929326)

@ DAI\_INTEL\_HDA

Intel HD/A.

**Definition** dai.h:106

[DAI\_LEGACY\_I2S](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a2560d8f844796f647ed774748c44adfe)

@ DAI\_LEGACY\_I2S

Legacy I2S compatible with i2s.h.

**Definition** dai.h:103

[DAI\_INTEL\_ALH\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a2a12c2858722c553cb31f24aacd83976)

@ DAI\_INTEL\_ALH\_NHLT

nhlt Intel ALH

**Definition** dai.h:117

[DAI\_INTEL\_DMIC](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a366db52bd49557d047f091cdb96b5e36)

@ DAI\_INTEL\_DMIC

Intel DMIC.

**Definition** dai.h:105

[DAI\_AMD\_DMIC](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a37f79dfe1804d4abeb89a9767bf37c75)

@ DAI\_AMD\_DMIC

Amd DMIC.

**Definition** dai.h:112

[DAI\_INTEL\_DMIC\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a3d759f9665a4db0c974913c4aa71e6f2)

@ DAI\_INTEL\_DMIC\_NHLT

nhlt ssp

**Definition** dai.h:115

[DAI\_AMD\_BT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a6c0c4b31c71c9e779a2a9325dc119fd0)

@ DAI\_AMD\_BT

Amd BT.

**Definition** dai.h:110

[DAI\_IMX\_ESAI](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a75bfaa3859321a283929ae033fcf22aa)

@ DAI\_IMX\_ESAI

i.MX ESAI

**Definition** dai.h:109

[DAI\_INTEL\_SSP\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a8d75b1d72f5fcff348c15281001f9aaa)

@ DAI\_INTEL\_SSP\_NHLT

nhlt ssp

**Definition** dai.h:114

[DAI\_INTEL\_SSP](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797a9301e2ec67fa75aefc0e59df727adcc9)

@ DAI\_INTEL\_SSP

Intel SSP.

**Definition** dai.h:104

[DAI\_IMX\_SAI](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797aa94ef995d95f9d0ad8b404e26b79faec)

@ DAI\_IMX\_SAI

i.MX SAI

**Definition** dai.h:108

[DAI\_AMD\_SP](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797ab675d7b5204a2cbc09f1f60a44f4ff3b)

@ DAI\_AMD\_SP

Amd SP.

**Definition** dai.h:111

[DAI\_MEDIATEK\_AFE](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797ac5095e399162d248e638b87a61b59a00)

@ DAI\_MEDIATEK\_AFE

Mtk AFE.

**Definition** dai.h:113

[DAI\_INTEL\_HDA\_NHLT](group__dai__interface.md#ggac95242d83a2c2b477fcb9eb3da420797afd1f617fdd16363c1a10e9f45a67a99b)

@ DAI\_INTEL\_HDA\_NHLT

nhlt Intel HD/A

**Definition** dai.h:116

[DAI\_TRIGGER\_DRAIN](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa1c17da0f6a54c2c25f2dd2349b5c0e02)

@ DAI\_TRIGGER\_DRAIN

Empty the transmit queue.

**Definition** dai.h:202

[DAI\_TRIGGER\_DROP](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa1f004f7d4dcb67d2c3a89298400b2234)

@ DAI\_TRIGGER\_DROP

Discard the transmit / receive queue.

**Definition** dai.h:209

[DAI\_TRIGGER\_STOP](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa23dd7f534a18f92cbf12ad957674ba35)

@ DAI\_TRIGGER\_STOP

Stop the transmission / reception of data.

**Definition** dai.h:179

[DAI\_TRIGGER\_COPY](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aa6720f67f3bc6ab62eacf986316df0a9f)

@ DAI\_TRIGGER\_COPY

Copy.

**Definition** dai.h:226

[DAI\_TRIGGER\_START](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aabcbb4f151183d54d51dde07d09b3f222)

@ DAI\_TRIGGER\_START

Start the transmission / reception of data.

**Definition** dai.h:163

[DAI\_TRIGGER\_PRE\_START](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aac7647bb0111f043abcdaa4b3e703b2ec)

@ DAI\_TRIGGER\_PRE\_START

Optional - Pre Start the transmission / reception of data.

**Definition** dai.h:169

[DAI\_TRIGGER\_POST\_STOP](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aad2fcfa3c229bfc0a82ec7841ab9f88c3)

@ DAI\_TRIGGER\_POST\_STOP

Optional - Post Stop the transmission / reception of data.

**Definition** dai.h:193

[DAI\_TRIGGER\_PREPARE](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aad9d4e12f62ee2e106abaeb3bb341ee70)

@ DAI\_TRIGGER\_PREPARE

Prepare the queues after underrun/overrun error has occurred.

**Definition** dai.h:215

[DAI\_TRIGGER\_PAUSE](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aadb17f3981cf0e248187c4006f527a3a5)

@ DAI\_TRIGGER\_PAUSE

Pause the transmission / reception of data.

**Definition** dai.h:187

[DAI\_TRIGGER\_RESET](group__dai__interface.md#ggaee6445967afb3ecf2c0470ca0c104a1aafa607dff411961ae22e44f1a972c4711)

@ DAI\_TRIGGER\_RESET

Reset.

**Definition** dai.h:221

[DAI\_INVERSION\_NB\_NF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60a35606eb43c6d77204bff029bfab37698)

@ DAI\_INVERSION\_NB\_NF

no BCLK inversion, no FSYNC inversion

**Definition** dai.h:84

[DAI\_INVERSION\_IB\_IF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ab35554010caadb69a5414c7f07649ee1)

@ DAI\_INVERSION\_IB\_IF

**Definition** dai.h:90

[DAI\_INVERSION\_NB\_IF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ad6622f24986622cf16fdeada99356c43)

@ DAI\_INVERSION\_NB\_IF

BCLK inversion, no FSYNC inversion.

**Definition** dai.h:86

[DAI\_INVERSION\_IB\_NF](group__dai__interface.md#ggaf66ca0bbc1f8ba2f2b81caf92bd09b60ae0a56f8334363d4a1aa916ffe5d70e5c)

@ DAI\_INVERSION\_IB\_NF

BCLK inversion, FSYNC inversion.

**Definition** dai.h:88

[DAI\_DIR\_RX](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fa48cc817cda4907b94a03e13e8b9aa69b)

@ DAI\_DIR\_RX

Receive data.

**Definition** dai.h:127

[DAI\_DIR\_BOTH](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fa58581d875a6a8c28adb0f6351a37f3e1)

@ DAI\_DIR\_BOTH

Both receive and transmit data.

**Definition** dai.h:129

[DAI\_DIR\_TX](group__dai__interface.md#ggafa7b22e4250c6479301fc657fea8a60fadfdf2212e2d86296dbccc60cfd60368c)

@ DAI\_DIR\_TX

Transmit data.

**Definition** dai.h:125

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[dai\_config](structdai__config.md)

Main DAI config structure.

**Definition** dai.h:252

[dai\_config::rate](structdai__config.md#a2d46087a3c94845d52b44386dd20cfc0)

uint32\_t rate

Frame clock (WS) frequency, sampling rate.

**Definition** dai.h:260

[dai\_config::tdm\_slot\_group](structdai__config.md#a32830675c7bf7125c5006579d33e5e96)

uint32\_t tdm\_slot\_group

**Definition** dai.h:272

[dai\_config::format](structdai__config.md#ac2c2c4a39bfe917d5a784d8bc596eb10)

uint16\_t format

DAI specific data stream format.

**Definition** dai.h:262

[dai\_config::channels](structdai__config.md#ac3f39c351ad9659356ad5ad4306585b8)

uint8\_t channels

Number of audio channels, words in frame.

**Definition** dai.h:258

[dai\_config::options](structdai__config.md#ac8b2936e194421f95d03e1c595017306)

uint8\_t options

DAI specific configuration options.

**Definition** dai.h:264

[dai\_config::type](structdai__config.md#acfb621417b789c71608ad50d0b54c1f6)

enum dai\_type type

Type of the DAI.

**Definition** dai.h:254

[dai\_config::dai\_index](structdai__config.md#aecb9fe475d71d55d8b19eb3faa697606)

uint32\_t dai\_index

Index of the DAI.

**Definition** dai.h:256

[dai\_config::block\_size](structdai__config.md#af3c768d9597298cea94bbdd6e5b5c4f3)

size\_t block\_size

Size of one RX/TX memory block (buffer) in bytes.

**Definition** dai.h:268

[dai\_config::link\_config](structdai__config.md#afd3bcee428b5359b7151a269973049a1)

uint16\_t link\_config

DAI specific link configuration.

**Definition** dai.h:270

[dai\_config::word\_size](structdai__config.md#afe7ab1b6c1163ca1bf4141bc6f2439ba)

uint8\_t word\_size

Number of bits representing one data word.

**Definition** dai.h:266

[dai\_properties](structdai__properties.md)

DAI properties.

**Definition** dai.h:235

[dai\_properties::dma\_hs\_id](structdai__properties.md#a7203f5c97aaf8f48f9eb51d88424afce)

uint32\_t dma\_hs\_id

DMA handshake id.

**Definition** dai.h:241

[dai\_properties::reg\_init\_delay](structdai__properties.md#a8fc2d359fe889b3a46ecc8918a82f680)

uint32\_t reg\_init\_delay

Delay for initializing registers.

**Definition** dai.h:243

[dai\_properties::fifo\_address](structdai__properties.md#a98053c85634b80b144bda05d83f2eb7e)

uint32\_t fifo\_address

Fifo hw address for e.g.

**Definition** dai.h:237

[dai\_properties::fifo\_depth](structdai__properties.md#a9b056f0ff59b473d3040851642d1601c)

uint32\_t fifo\_depth

Fifo depth.

**Definition** dai.h:239

[dai\_properties::stream\_id](structdai__properties.md#adab0f1199c7169a521329adc98c2f0ac)

int stream\_id

Stream ID.

**Definition** dai.h:245

[dai\_ts\_cfg](structdai__ts__cfg.md)

DAI timestamp configuration.

**Definition** dai.h:278

[dai\_ts\_cfg::type](structdai__ts__cfg.md#a2b0be9c840de941e4a87c422fa82356d)

int type

Type of the DAI (SSP, DMIC, HDA, etc.).

**Definition** dai.h:282

[dai\_ts\_cfg::dma\_chan\_count](structdai__ts__cfg.md#a37c6379686435994b9050d1e9c249756)

int dma\_chan\_count

Number of channels in single DMA.

**Definition** dai.h:292

[dai\_ts\_cfg::dma\_chan\_index](structdai__ts__cfg.md#aa87fc1e3072490e44f65bc7690f85ce8)

int dma\_chan\_index

Used DMA channel index.

**Definition** dai.h:290

[dai\_ts\_cfg::dma\_id](structdai__ts__cfg.md#ab874249dcb9377fafa35764b4f1c0ea0)

int dma\_id

DMA instance id.

**Definition** dai.h:288

[dai\_ts\_cfg::walclk\_rate](structdai__ts__cfg.md#ac17d3da9de6d860f2fa04286a4c43a1d)

uint32\_t walclk\_rate

Rate in Hz, e.g.

**Definition** dai.h:280

[dai\_ts\_cfg::direction](structdai__ts__cfg.md#afdaf1a4ef6a00201b3790187ec44370f)

int direction

Direction (playback/capture).

**Definition** dai.h:284

[dai\_ts\_cfg::index](structdai__ts__cfg.md#aff3dc52737d1261cd56c084c104691eb)

int index

Index for SSPx to select correct timestamp register.

**Definition** dai.h:286

[dai\_ts\_data](structdai__ts__data.md)

DAI timestamp data.

**Definition** dai.h:298

[dai\_ts\_data::walclk](structdai__ts__data.md#a11133d72485786e75a9d94f218fe699b)

uint64\_t walclk

Wall clock.

**Definition** dai.h:300

[dai\_ts\_data::sample](structdai__ts__data.md#a933cbc19cc837683581db806702fba36)

uint64\_t sample

Sample count.

**Definition** dai.h:302

[dai\_ts\_data::walclk\_rate](structdai__ts__data.md#ace2686aa6ff5aed346705cbb0d198d36)

uint32\_t walclk\_rate

Rate in Hz, e.g.

**Definition** dai.h:304

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dai.h](dai_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
