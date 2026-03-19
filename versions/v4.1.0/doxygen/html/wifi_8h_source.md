---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/wifi_8h_source.html
original_path: doxygen/html/wifi_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi.h

[Go to the documentation of this file.](wifi_8h.md)

1/\*

2 \* Copyright (c) 2018 Texas Instruments, Incorporated

3 \* Copyright (c) 2023 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

21

22#ifndef ZEPHYR\_INCLUDE\_NET\_WIFI\_H\_

23#define ZEPHYR\_INCLUDE\_NET\_WIFI\_H\_

24

25#include <[zephyr/sys/util.h](sys_2util_8h.md)> /\* for ARRAY\_SIZE \*/

26

[ 28](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)#define WIFI\_COUNTRY\_CODE\_LEN 2

29

31

32#define WIFI\_LISTEN\_INTERVAL\_MIN 0

33#define WIFI\_LISTEN\_INTERVAL\_MAX 65535

34

36

37#ifdef \_\_cplusplus

38extern "C" {

39#endif

40

[ 42](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c)enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) {

[ 44](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e) [WIFI\_SECURITY\_TYPE\_NONE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e) = 0,

[ 46](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368) [WIFI\_SECURITY\_TYPE\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368),

[ 48](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e) [WIFI\_SECURITY\_TYPE\_PSK\_SHA256](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e),

[ 50](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f) [WIFI\_SECURITY\_TYPE\_SAE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f),

[ 52](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9caab329c818e10cbe98aac1f9c30849c91) [WIFI\_SECURITY\_TYPE\_SAE\_HNP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9caab329c818e10cbe98aac1f9c30849c91) = [WIFI\_SECURITY\_TYPE\_SAE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f),

[ 54](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca1e45d14be678d0693b3f03f73fc5b0df) [WIFI\_SECURITY\_TYPE\_SAE\_H2E](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca1e45d14be678d0693b3f03f73fc5b0df),

[ 56](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca4beacdae98f8ca155609d2fd660c5ed0) [WIFI\_SECURITY\_TYPE\_SAE\_AUTO](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca4beacdae98f8ca155609d2fd660c5ed0),

[ 58](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d) [WIFI\_SECURITY\_TYPE\_WAPI](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d),

[ 60](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80) [WIFI\_SECURITY\_TYPE\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80),

[ 62](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca85bcce61e75c01eb95083523e8925a40) [WIFI\_SECURITY\_TYPE\_EAP\_TLS](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca85bcce61e75c01eb95083523e8925a40) = [WIFI\_SECURITY\_TYPE\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80),

[ 64](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724) [WIFI\_SECURITY\_TYPE\_WEP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724),

[ 66](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a) [WIFI\_SECURITY\_TYPE\_WPA\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a),

[ 68](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff) [WIFI\_SECURITY\_TYPE\_WPA\_AUTO\_PERSONAL](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff),

[ 70](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca6cf0bd5db90deaa6b35f7afe122e8b5f) [WIFI\_SECURITY\_TYPE\_DPP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca6cf0bd5db90deaa6b35f7afe122e8b5f),

[ 72](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9caaa1dbea0100af80ca48ad594cddb4212) [WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_MSCHAPV2](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9caaa1dbea0100af80ca48ad594cddb4212),

[ 74](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca0c9db910757c5a715a5e88089362fab5) [WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_GTC](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca0c9db910757c5a715a5e88089362fab5),

[ 76](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca3a20bf15c1e51313629789e6abe0273d) [WIFI\_SECURITY\_TYPE\_EAP\_TTLS\_MSCHAPV2](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca3a20bf15c1e51313629789e6abe0273d),

[ 78](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca6d2e5f72b8bf76f093ab79be2a4b9477) [WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_TLS](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca6d2e5f72b8bf76f093ab79be2a4b9477),

[ 80](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5) [WIFI\_SECURITY\_TYPE\_FT\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5),

[ 82](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092) [WIFI\_SECURITY\_TYPE\_FT\_SAE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092),

[ 84](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5) [WIFI\_SECURITY\_TYPE\_FT\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5),

[ 86](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93) [WIFI\_SECURITY\_TYPE\_FT\_EAP\_SHA384](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93),

[ 88](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca64221ce0052ce510e16537a32c67bb02) [WIFI\_SECURITY\_TYPE\_SAE\_EXT\_KEY](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca64221ce0052ce510e16537a32c67bb02),

89

91 \_\_WIFI\_SECURITY\_TYPE\_AFTER\_LAST,

92 WIFI\_SECURITY\_TYPE\_MAX = \_\_WIFI\_SECURITY\_TYPE\_AFTER\_LAST - 1,

93 WIFI\_SECURITY\_TYPE\_UNKNOWN

95};

96

[ 98](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331)enum [wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331) {

[ 100](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a39edcc7a267ce608a1e818948b5d172b) [WIFI\_EAP\_TYPE\_NONE](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a39edcc7a267ce608a1e818948b5d172b) = 0,

[ 102](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a64daad77662868322e638da6531a5c0f) [WIFI\_EAP\_TYPE\_GTC](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a64daad77662868322e638da6531a5c0f) = 6,

[ 104](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a505b4b888231dd1fbc169d612d8f0c38) [WIFI\_EAP\_TYPE\_TLS](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a505b4b888231dd1fbc169d612d8f0c38) = 13,

[ 106](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a35fce37fccb3d27596c4e0a531109dac) [WIFI\_EAP\_TYPE\_TTLS](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a35fce37fccb3d27596c4e0a531109dac) = 21,

[ 108](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a8e619153aa3dad398c6ced36605f5e3f) [WIFI\_EAP\_TYPE\_PEAP](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a8e619153aa3dad398c6ced36605f5e3f) = 25,

[ 110](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a37f7681b1fb5d7165010ec941018882f) [WIFI\_EAP\_TYPE\_MSCHAPV2](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a37f7681b1fb5d7165010ec941018882f) = 26,

111};

112

[ 118](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a)enum [wifi\_wpa3\_enterprise\_type](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a) {

[ 120](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aa7c34eb5cf3e76c3c1b45c424436adbb1) [WIFI\_WPA3\_ENTERPRISE\_NA](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aa7c34eb5cf3e76c3c1b45c424436adbb1) = 0,

[ 122](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aaec90b38cb8fb95ff3a679da473537589) [WIFI\_WPA3\_ENTERPRISE\_SUITEB](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aaec90b38cb8fb95ff3a679da473537589) = 1,

[ 124](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aa577671035478f3a385b8e4fdf6abf5fa) [WIFI\_WPA3\_ENTERPRISE\_SUITEB\_192](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aa577671035478f3a385b8e4fdf6abf5fa),

[ 126](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aaf13490bee764dd77f770f07bf3dac3fa) [WIFI\_WPA3\_ENTERPRISE\_ONLY](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aaf13490bee764dd77f770f07bf3dac3fa),

127

129 \_\_WIFI\_WPA3\_ENTERPRISE\_AFTER\_LAST,

130 WIFI\_WPA3\_ENTERPRISE\_MAX = \_\_WIFI\_WPA3\_ENTERPRISE\_AFTER\_LAST - 1,

131 WIFI\_WPA3\_ENTERPRISE\_UNKNOWN

133};

134

[ 135](group__wifi__mgmt.md#ga218525a9d9ee64524f983e52d5767562)enum [wifi\_eap\_tls\_cipher\_type](group__wifi__mgmt.md#ga218525a9d9ee64524f983e52d5767562) {

[ 137](group__wifi__mgmt.md#gga218525a9d9ee64524f983e52d5767562a38f97de2297f9df6e4ac3cecfd0799df) [WIFI\_EAP\_TLS\_NONE](group__wifi__mgmt.md#gga218525a9d9ee64524f983e52d5767562a38f97de2297f9df6e4ac3cecfd0799df),

[ 139](group__wifi__mgmt.md#gga218525a9d9ee64524f983e52d5767562ae44c04c2d1510385fe43827dbe6026f9) [WIFI\_EAP\_TLS\_ECC\_P384](group__wifi__mgmt.md#gga218525a9d9ee64524f983e52d5767562ae44c04c2d1510385fe43827dbe6026f9),

[ 141](group__wifi__mgmt.md#gga218525a9d9ee64524f983e52d5767562ac5436dc7d2bbeded043b1102ee592e17) [WIFI\_EAP\_TLS\_RSA\_3K](group__wifi__mgmt.md#gga218525a9d9ee64524f983e52d5767562ac5436dc7d2bbeded043b1102ee592e17),

142};

143

[ 145](group__wifi__mgmt.md#ga7f7b23ac019ca504a2006f0376735645)enum [wifi\_cipher\_type](group__wifi__mgmt.md#ga7f7b23ac019ca504a2006f0376735645) {

[ 147](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1) [WPA\_CAPA\_ENC\_CCMP](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1),

[ 149](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d) [WPA\_CAPA\_ENC\_GCMP](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d),

[ 151](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4) [WPA\_CAPA\_ENC\_GCMP\_256](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4),

152};

153

[ 155](group__wifi__mgmt.md#gaf84d5e1a68393483fc6063c06b8f26e0)enum [wifi\_group\_mgmt\_cipher\_type](group__wifi__mgmt.md#gaf84d5e1a68393483fc6063c06b8f26e0) {

[ 159](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8) [WPA\_CAPA\_ENC\_BIP](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8),

[ 163](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70) [WPA\_CAPA\_ENC\_BIP\_GMAC\_128](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70),

[ 167](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096) [WPA\_CAPA\_ENC\_BIP\_GMAC\_256](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096),

168};

169

[ 170](structwifi__cipher__desc.md)struct [wifi\_cipher\_desc](structwifi__cipher__desc.md) {

[ 172](structwifi__cipher__desc.md#a6751019bb6da3032ca2f7bc42a3469e3) unsigned int [capa](structwifi__cipher__desc.md#a6751019bb6da3032ca2f7bc42a3469e3);

[ 174](structwifi__cipher__desc.md#a9396239f38613b151232a4c5f3d66a8f) char \*[name](structwifi__cipher__desc.md#a9396239f38613b151232a4c5f3d66a8f);

175};

176

[ 177](structwifi__eap__cipher__config.md)struct [wifi\_eap\_cipher\_config](structwifi__eap__cipher__config.md) {

[ 179](structwifi__eap__cipher__config.md#a385d365bb70a70fa09d321c55988afcc) char \*[key\_mgmt](structwifi__eap__cipher__config.md#a385d365bb70a70fa09d321c55988afcc);

[ 181](structwifi__eap__cipher__config.md#a14128465917447f38d3854444a9bf6e1) char \*[openssl\_ciphers](structwifi__eap__cipher__config.md#a14128465917447f38d3854444a9bf6e1);

[ 183](structwifi__eap__cipher__config.md#aa505ae934897742078aa46f1fdb5d0d1) char \*[group\_cipher](structwifi__eap__cipher__config.md#aa505ae934897742078aa46f1fdb5d0d1);

[ 185](structwifi__eap__cipher__config.md#a3917f94dfafb22df260db9c4a129c3c4) char \*[pairwise\_cipher](structwifi__eap__cipher__config.md#a3917f94dfafb22df260db9c4a129c3c4);

[ 187](structwifi__eap__cipher__config.md#ab53f5b5419b2b8c8a869ba4f9d645a41) char \*[group\_mgmt\_cipher](structwifi__eap__cipher__config.md#ab53f5b5419b2b8c8a869ba4f9d645a41);

[ 189](structwifi__eap__cipher__config.md#ae9a4b8a0f0b47ac1065562ce287473a5) char \*[tls\_flags](structwifi__eap__cipher__config.md#ae9a4b8a0f0b47ac1065562ce287473a5);

190};

191

[ 192](structwifi__eap__config.md)struct [wifi\_eap\_config](structwifi__eap__config.md) {

[ 194](structwifi__eap__config.md#a031a5c86551f90130ff74ed53977c49d) enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) [type](structwifi__eap__config.md#a031a5c86551f90130ff74ed53977c49d);

[ 196](structwifi__eap__config.md#ab44893426c89416ab24e3bfb57bf49ad) enum [wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331) [eap\_type\_phase1](structwifi__eap__config.md#ab44893426c89416ab24e3bfb57bf49ad);

[ 198](structwifi__eap__config.md#aaf73f2f986d56f95d196d02dcecbaff1) enum [wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331) [eap\_type\_phase2](structwifi__eap__config.md#aaf73f2f986d56f95d196d02dcecbaff1);

[ 200](structwifi__eap__config.md#aa7a42a1256ef26562e83f47498d87113) char \*[method](structwifi__eap__config.md#aa7a42a1256ef26562e83f47498d87113);

[ 202](structwifi__eap__config.md#abeed60cdf6c01751a4bb3c7ab67ea4e6) char \*[phase2](structwifi__eap__config.md#abeed60cdf6c01751a4bb3c7ab67ea4e6);

203};

204

[ 206](group__wifi__mgmt.md#ga9bb9f658d7806e42b3ee351fb3e7dfa0)const char \*[wifi\_security\_txt](group__wifi__mgmt.md#ga9bb9f658d7806e42b3ee351fb3e7dfa0)(enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) security);

207

[ 209](group__wifi__mgmt.md#gaf67f2900be88fdf3f282400d09f2ab88)const char \*[wifi\_wpa3\_enterprise\_txt](group__wifi__mgmt.md#gaf67f2900be88fdf3f282400d09f2ab88)(enum [wifi\_wpa3\_enterprise\_type](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a) wpa3\_ent);

210

[ 212](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) {

[ 214](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969) [WIFI\_MFP\_DISABLE](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969) = 0,

[ 216](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf) [WIFI\_MFP\_OPTIONAL](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf),

[ 218](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840) [WIFI\_MFP\_REQUIRED](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840),

219

221 \_\_WIFI\_MFP\_AFTER\_LAST,

222 WIFI\_MFP\_MAX = \_\_WIFI\_MFP\_AFTER\_LAST - 1,

223 WIFI\_MFP\_UNKNOWN

225};

226

[ 228](group__wifi__mgmt.md#ga22354241197a9227fdba77e67d471f5c)const char \*[wifi\_mfp\_txt](group__wifi__mgmt.md#ga22354241197a9227fdba77e67d471f5c)(enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) mfp);

229

[ 233](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d)enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) {

[ 235](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11) [WIFI\_FREQ\_BAND\_2\_4\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11) = 0,

[ 237](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895) [WIFI\_FREQ\_BAND\_5\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895),

[ 239](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0) [WIFI\_FREQ\_BAND\_6\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0),

240

242 \_\_WIFI\_FREQ\_BAND\_AFTER\_LAST,

[ 244](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5) [WIFI\_FREQ\_BAND\_MAX](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5) = \_\_WIFI\_FREQ\_BAND\_AFTER\_LAST - 1,

[ 246](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5) [WIFI\_FREQ\_BAND\_UNKNOWN](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)

247};

248

[ 250](group__wifi__mgmt.md#ga44f875bf0d931b66d582f5dca2d65ed5)const char \*[wifi\_band\_txt](group__wifi__mgmt.md#ga44f875bf0d931b66d582f5dca2d65ed5)(enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) band);

251

[ 255](group__wifi__mgmt.md#ga3b01cead3c2eb4581fe85e2aaaffbd49)enum [wifi\_frequency\_bandwidths](group__wifi__mgmt.md#ga3b01cead3c2eb4581fe85e2aaaffbd49) {

[ 257](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49ae5efe45d5211477322968e55014d22d5) [WIFI\_FREQ\_BANDWIDTH\_20MHZ](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49ae5efe45d5211477322968e55014d22d5) = 1,

[ 259](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49a9f984c246be1976cf1b799c4aed02ea1) [WIFI\_FREQ\_BANDWIDTH\_40MHZ](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49a9f984c246be1976cf1b799c4aed02ea1),

[ 261](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49a2c445a7a6345a66a41248bde2f7bf8cb) [WIFI\_FREQ\_BANDWIDTH\_80MHZ](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49a2c445a7a6345a66a41248bde2f7bf8cb),

262

264 \_\_WIFI\_FREQ\_BANDWIDTH\_AFTER\_LAST,

[ 266](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49af57b996c36f950143c9f23a25d402b90) [WIFI\_FREQ\_BANDWIDTH\_MAX](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49af57b996c36f950143c9f23a25d402b90) = \_\_WIFI\_FREQ\_BANDWIDTH\_AFTER\_LAST - 1,

[ 268](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49a4e45ec9ffe32912a5673f9bbffeeef2d) [WIFI\_FREQ\_BANDWIDTH\_UNKNOWN](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49a4e45ec9ffe32912a5673f9bbffeeef2d)

269};

270

[ 271](group__wifi__mgmt.md#gae479798eb864c3784d1c8c9375658647)const char \*const [wifi\_bandwidth\_txt](group__wifi__mgmt.md#gae479798eb864c3784d1c8c9375658647)(enum [wifi\_frequency\_bandwidths](group__wifi__mgmt.md#ga3b01cead3c2eb4581fe85e2aaaffbd49) bandwidth);

272

[ 274](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)#define WIFI\_SSID\_MAX\_LEN 32

[ 276](group__wifi__mgmt.md#gaa8e19abf8c85f237ba5033740ceff553)#define WIFI\_PSK\_MIN\_LEN 8

[ 278](group__wifi__mgmt.md#gad7c3b99c974b342935180a28fdc5ddfc)#define WIFI\_PSK\_MAX\_LEN 64

[ 280](group__wifi__mgmt.md#gab63fa744cc2e049cfd635ab0a187971f)#define WIFI\_SAE\_PSWD\_MAX\_LEN 128

[ 282](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)#define WIFI\_MAC\_ADDR\_LEN 6

[ 284](group__wifi__mgmt.md#gac6904487661f157274b0b60833f6684a)#define WIFI\_ENT\_IDENTITY\_MAX\_LEN 64

[ 286](group__wifi__mgmt.md#gae2fd55924f4078187431f7a1184f217f)#define WIFI\_ENT\_PSWD\_MAX\_LEN 128

287

[ 289](group__wifi__mgmt.md#ga260e473dac1e823fd298a2c982470e0b)#define WIFI\_CHANNEL\_MIN 1

[ 291](group__wifi__mgmt.md#ga8ea9141108f93b419f6a6530bf67bd95)#define WIFI\_CHANNEL\_MAX 233

[ 293](group__wifi__mgmt.md#ga3876cd718af9f8a7b3682546da854544)#define WIFI\_CHANNEL\_ANY 255

294

[ 299](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4)enum [wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4) {

[ 301](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) [WIFI\_STATE\_DISCONNECTED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) = 0,

[ 303](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) [WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c),

[ 305](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) [WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598),

[ 307](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) [WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b),

[ 309](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) [WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba),

[ 311](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) [WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b),

[ 313](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) [WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc),

[ 315](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) [WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969),

[ 317](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) [WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e),

[ 319](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f) [WIFI\_STATE\_COMPLETED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f),

320

322 \_\_WIFI\_STATE\_AFTER\_LAST,

323 WIFI\_STATE\_MAX = \_\_WIFI\_STATE\_AFTER\_LAST - 1,

324 WIFI\_STATE\_UNKNOWN

326};

327

328/\* We rely on the strict order of the enum values, so, let's check it \*/

329BUILD\_ASSERT([WIFI\_STATE\_DISCONNECTED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) < [WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) &&

330 [WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) < [WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) &&

331 [WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) < [WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) &&

332 [WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) < [WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) &&

333 [WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) < [WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) &&

334 [WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) < [WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) &&

335 [WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) < [WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) &&

336 [WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) < [WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) &&

337 [WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) < [WIFI\_STATE\_COMPLETED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f));

338

339

[ 341](group__wifi__mgmt.md#ga03d306912dc96178e21d3c82c104582f)const char \*[wifi\_state\_txt](group__wifi__mgmt.md#ga03d306912dc96178e21d3c82c104582f)(enum [wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

342

[ 347](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) {

[ 349](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813) [WIFI\_MODE\_INFRA](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813) = 0,

[ 351](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b) [WIFI\_MODE\_IBSS](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b) = 1,

[ 353](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8) [WIFI\_MODE\_AP](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8) = 2,

[ 355](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889) [WIFI\_MODE\_P2P\_GO](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889) = 3,

[ 357](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521) [WIFI\_MODE\_P2P\_GROUP\_FORMATION](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521) = 4,

[ 359](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68) [WIFI\_MODE\_MESH](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68) = 5,

360

362 \_\_WIFI\_MODE\_AFTER\_LAST,

363 WIFI\_MODE\_MAX = \_\_WIFI\_MODE\_AFTER\_LAST - 1,

364 WIFI\_MODE\_UNKNOWN

366};

367

[ 369](group__wifi__mgmt.md#gad78536ce1f30accfa45f258b6bf8c73d)const char \*[wifi\_mode\_txt](group__wifi__mgmt.md#gad78536ce1f30accfa45f258b6bf8c73d)(enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) mode);

370

[ 375](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) {

[ 377](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8) [WIFI\_0](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8) = 0,

[ 379](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c) [WIFI\_1](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c),

[ 381](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9) [WIFI\_2](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9),

[ 383](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362) [WIFI\_3](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362),

[ 385](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2) [WIFI\_4](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2),

[ 387](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824) [WIFI\_5](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824),

[ 389](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe) [WIFI\_6](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe),

[ 391](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6) [WIFI\_6E](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6),

[ 393](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934) [WIFI\_7](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934),

394

396 \_\_WIFI\_LINK\_MODE\_AFTER\_LAST,

397 WIFI\_LINK\_MODE\_MAX = \_\_WIFI\_LINK\_MODE\_AFTER\_LAST - 1,

398 WIFI\_LINK\_MODE\_UNKNOWN

400};

401

[ 403](group__wifi__mgmt.md#ga0d9d6e2150fb187025300904357f7b4d)const char \*[wifi\_link\_mode\_txt](group__wifi__mgmt.md#ga0d9d6e2150fb187025300904357f7b4d)(enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) link\_mode);

404

[ 406](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) {

[ 408](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9) [WIFI\_SCAN\_TYPE\_ACTIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9) = 0,

[ 410](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f) [WIFI\_SCAN\_TYPE\_PASSIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f),

411};

412

[ 414](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) {

[ 416](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82) [WIFI\_PS\_DISABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82) = 0,

[ 418](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47) [WIFI\_PS\_ENABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47),

419};

420

[ 422](group__wifi__mgmt.md#gafbeb5f7fa97fd2ba0c691da0f8853ef2)const char \*[wifi\_ps\_txt](group__wifi__mgmt.md#gafbeb5f7fa97fd2ba0c691da0f8853ef2)(enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) ps\_name);

423

[ 425](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c)enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) {

[ 427](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd) [WIFI\_PS\_MODE\_LEGACY](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd) = 0,

428 /\* This has to be configured before connecting to the AP,

429 \* as support for ADDTS action frames is not available.

430 \*/

[ 432](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5) [WIFI\_PS\_MODE\_WMM](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5),

433};

434

[ 436](group__wifi__mgmt.md#gadb21d49f64e04fba59433e51d5b3481c)const char \*[wifi\_ps\_mode\_txt](group__wifi__mgmt.md#gadb21d49f64e04fba59433e51d5b3481c)(enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) ps\_mode);

437

[ 439](group__wifi__mgmt.md#gaa1a74ef94af57a7ea966c691c065a46d)#define WIFI\_INTERFACE\_INDEX\_MIN 1

[ 441](group__wifi__mgmt.md#gaa6cbecd7d4197d453038d3da7ef6be7b)#define WIFI\_INTERFACE\_INDEX\_MAX 255

442

[ 444](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35)enum [wifi\_operational\_modes](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35) {

[ 446](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7) [WIFI\_STA\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 448](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696) [WIFI\_MONITOR\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 450](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74) [WIFI\_TX\_INJECTION\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 452](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56) [WIFI\_PROMISCUOUS\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 454](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd) [WIFI\_AP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 456](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623) [WIFI\_SOFTAP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

457};

458

[ 460](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f)enum [wifi\_filter](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f) {

[ 462](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b) [WIFI\_PACKET\_FILTER\_ALL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 464](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc) [WIFI\_PACKET\_FILTER\_MGMT](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 466](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244) [WIFI\_PACKET\_FILTER\_DATA](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 468](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de) [WIFI\_PACKET\_FILTER\_CTRL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

469};

470

[ 472](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) {

[ 474](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45) [WIFI\_TWT\_SETUP](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45) = 0,

[ 476](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f) [WIFI\_TWT\_TEARDOWN](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f),

477};

478

[ 480](group__wifi__mgmt.md#gadb125925e851bf7569424cd4295e7712)const char \*[wifi\_twt\_operation\_txt](group__wifi__mgmt.md#gadb125925e851bf7569424cd4295e7712)(enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) twt\_operation);

481

[ 483](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8)enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) {

[ 485](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0) [WIFI\_TWT\_INDIVIDUAL](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0) = 0,

[ 487](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa) [WIFI\_TWT\_BROADCAST](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa),

[ 489](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978) [WIFI\_TWT\_WAKE\_TBTT](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978)

490};

491

[ 493](group__wifi__mgmt.md#ga6a74e999d63ee491df68447219ef2a0d)const char \*[wifi\_twt\_negotiation\_type\_txt](group__wifi__mgmt.md#ga6a74e999d63ee491df68447219ef2a0d)(enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) twt\_negotiation);

494

[ 496](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) {

[ 498](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd) [WIFI\_TWT\_SETUP\_CMD\_REQUEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd) = 0,

[ 500](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648) [WIFI\_TWT\_SETUP\_CMD\_SUGGEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648),

[ 502](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e) [WIFI\_TWT\_SETUP\_CMD\_DEMAND](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e),

[ 504](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279) [WIFI\_TWT\_SETUP\_CMD\_GROUPING](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279),

[ 506](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a) [WIFI\_TWT\_SETUP\_CMD\_ACCEPT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a),

[ 508](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1) [WIFI\_TWT\_SETUP\_CMD\_ALTERNATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1),

[ 510](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3) [WIFI\_TWT\_SETUP\_CMD\_DICTATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3),

[ 512](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565) [WIFI\_TWT\_SETUP\_CMD\_REJECT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565),

513};

514

[ 516](group__wifi__mgmt.md#gae3ca047cc6ef6b6a2e44ba6574d41a44)const char \*[wifi\_twt\_setup\_cmd\_txt](group__wifi__mgmt.md#gae3ca047cc6ef6b6a2e44ba6574d41a44)(enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) twt\_setup);

517

[ 519](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) {

[ 521](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286) [WIFI\_TWT\_RESP\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286) = 0,

[ 523](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72) [WIFI\_TWT\_RESP\_NOT\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72),

524};

525

[ 527](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6)enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) {

[ 529](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13) [WIFI\_TWT\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13),

[ 531](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556) [WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556),

[ 533](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d) [WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d),

[ 535](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef) [WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef),

[ 537](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831) [WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831),

[ 539](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860) [WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860),

[ 541](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce) [WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce),

[ 543](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7) [WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7),

[ 545](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6) [WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6),

[ 547](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee) [WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee),

[ 549](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c) [WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c),

550};

551

[ 553](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) {

[ 555](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965) [WIFI\_TWT\_TEARDOWN\_SUCCESS](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965) = 0,

[ 557](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d) [WIFI\_TWT\_TEARDOWN\_FAILED](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d),

558};

559

561static const char \* const wifi\_twt\_err\_code\_tbl[] = {

562 [[WIFI\_TWT\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13)] = "Unspecified",

563 [[WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556)] = "Command Execution failed",

564 [[WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d)] =

565 "Operation not supported",

566 [[WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef)] =

567 "Unable to get iface status",

568 [[WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831)] =

569 "Device not connected",

570 [[WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860)] = "Peer not HE capable",

571 [[WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce)] = "Peer not TWT capable",

572 [[WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7)] =

573 "Operation already in progress",

574 [[WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6)] =

575 "Invalid negotiated flow id",

576 [[WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee)] =

577 "IP address not assigned",

578 [[WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)] =

579 "Flow already exists",

580};

582

[ 584](group__wifi__mgmt.md#gab2e6a6e1d8358a8f34d67bd632709b3d)static inline const char \*[wifi\_twt\_get\_err\_code\_str](group__wifi__mgmt.md#gab2e6a6e1d8358a8f34d67bd632709b3d)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) err\_no)

585{

586 if ((err\_no) < ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(wifi\_twt\_err\_code\_tbl)) {

587 return wifi\_twt\_err\_code\_tbl[err\_no];

588 }

589

590 return "<unknown>";

591}

592

[ 594](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)enum [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) {

[ 596](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d) [WIFI\_PS\_PARAM\_STATE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d),

[ 598](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90) [WIFI\_PS\_PARAM\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90),

[ 600](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8) [WIFI\_PS\_PARAM\_WAKEUP\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8),

[ 602](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab) [WIFI\_PS\_PARAM\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab),

[ 604](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03) [WIFI\_PS\_PARAM\_EXIT\_STRATEGY](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03),

[ 606](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29) [WIFI\_PS\_PARAM\_TIMEOUT](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29),

607};

608

[ 610](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) {

[ 612](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6) [WIFI\_PS\_WAKEUP\_MODE\_DTIM](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6) = 0,

[ 614](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30) [WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30),

615};

616

[ 618](group__wifi__mgmt.md#ga6fd645f891234136b3028574a0af9666)const char \*[wifi\_ps\_wakeup\_mode\_txt](group__wifi__mgmt.md#ga6fd645f891234136b3028574a0af9666)(enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) ps\_wakeup\_mode);

619

[ 623](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7)enum [wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7) {

[ 625](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5) [WIFI\_PS\_EXIT\_CUSTOM\_ALGO](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5) = 0,

[ 627](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832) [WIFI\_PS\_EXIT\_EVERY\_TIM](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832),

628

630 WIFI\_PS\_EXIT\_LAST,

631 WIFI\_PS\_EXIT\_MAX = WIFI\_PS\_EXIT\_LAST - 1,

633};

634

[ 636](group__wifi__mgmt.md#ga034bfcd7891caeb31820579b5ee22a7b)const char \*[wifi\_ps\_exit\_strategy\_txt](group__wifi__mgmt.md#ga034bfcd7891caeb31820579b5ee22a7b)(enum [wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7) ps\_exit\_strategy);

637

[ 639](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)enum [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) {

[ 641](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38) [WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38),

[ 643](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394) [WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394),

[ 645](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093) [WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093),

[ 647](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3) [WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3),

[ 649](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a) [WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a),

[ 651](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486) [WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486),

[ 653](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f) [WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f),

[ 655](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce) [WIFI\_PS\_PARAM\_FAIL\_INVALID\_EXIT\_STRATEGY](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce),

656};

657

659static const char \* const wifi\_ps\_param\_config\_err\_code\_tbl[] = {

660 [[WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38)] = "Unspecified",

661 [[WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394)] = "Command Execution failed",

662 [[WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093)] =

663 "Operation not supported",

664 [[WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3)] =

665 "Unable to get iface status",

666 [[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a)] =

667 "Cannot set parameters while device not connected",

668 [[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486)] =

669 "Cannot set parameters while device connected",

670 [[WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)] =

671 "Parameter out of range",

672};

674

[ 678](group__wifi__mgmt.md#ga4fced9c3627d8f65d75e1651b11916b0)enum [wifi\_btm\_query\_reason](group__wifi__mgmt.md#ga4fced9c3627d8f65d75e1651b11916b0) {

[ 680](group__wifi__mgmt.md#gga4fced9c3627d8f65d75e1651b11916b0a41376bed59184da60f7c6558d2524c58) [WIFI\_BTM\_QUERY\_REASON\_UNSPECIFIED](group__wifi__mgmt.md#gga4fced9c3627d8f65d75e1651b11916b0a41376bed59184da60f7c6558d2524c58) = 0,

[ 682](group__wifi__mgmt.md#gga4fced9c3627d8f65d75e1651b11916b0a718e2d9c2f18fafc70c389177a4a5257) [WIFI\_BTM\_QUERY\_REASON\_LOW\_RSSI](group__wifi__mgmt.md#gga4fced9c3627d8f65d75e1651b11916b0a718e2d9c2f18fafc70c389177a4a5257) = 16,

[ 684](group__wifi__mgmt.md#gga4fced9c3627d8f65d75e1651b11916b0a5491f6eabeae1cd0faec69b5ced04f49) [WIFI\_BTM\_QUERY\_REASON\_LEAVING\_ESS](group__wifi__mgmt.md#gga4fced9c3627d8f65d75e1651b11916b0a5491f6eabeae1cd0faec69b5ced04f49) = 20,

685};

686

[ 688](group__wifi__mgmt.md#ga8b72e7989964963a25f42ed1dba240a0)static inline const char \*[wifi\_ps\_get\_config\_err\_code\_str](group__wifi__mgmt.md#ga8b72e7989964963a25f42ed1dba240a0)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) err\_no)

689{

690 if ((err\_no) < ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(wifi\_ps\_param\_config\_err\_code\_tbl)) {

691 return wifi\_ps\_param\_config\_err\_code\_tbl[err\_no];

692 }

693

694 return "<unknown>";

695}

696

[ 698](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642)enum [wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642) {

[ 700](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c) [WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 702](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958) [WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 704](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a1c9f37033909236e6a2259465dda4ef7) [WIFI\_AP\_CONFIG\_PARAM\_BANDWIDTH](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a1c9f37033909236e6a2259465dda4ef7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 706](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642ac357562788ce489023e9e66296401199) [WIFI\_AP\_CONFIG\_PARAM\_HT\_CAPAB](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642ac357562788ce489023e9e66296401199) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 708](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642ac22e71c91a433674f0a96ec853539902) [WIFI\_AP\_CONFIG\_PARAM\_VHT\_CAPAB](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642ac22e71c91a433674f0a96ec853539902) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

709};

710

711#ifdef \_\_cplusplus

712}

713#endif

714

718#endif /\* ZEPHYR\_INCLUDE\_NET\_WIFI\_H\_ \*/

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:120

[wifi\_ps\_exit\_strategy\_txt](group__wifi__mgmt.md#ga034bfcd7891caeb31820579b5ee22a7b)

const char \* wifi\_ps\_exit\_strategy\_txt(enum wifi\_ps\_exit\_strategy ps\_exit\_strategy)

Helper function to get user-friendly ps exit strategy name.

[wifi\_state\_txt](group__wifi__mgmt.md#ga03d306912dc96178e21d3c82c104582f)

const char \* wifi\_state\_txt(enum wifi\_iface\_state state)

Helper function to get user-friendly interface state name.

[wifi\_link\_mode\_txt](group__wifi__mgmt.md#ga0d9d6e2150fb187025300904357f7b4d)

const char \* wifi\_link\_mode\_txt(enum wifi\_link\_mode link\_mode)

Helper function to get user-friendly link mode name.

[wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)

wifi\_ps

Wi-Fi power save states.

**Definition** wifi.h:414

[wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d)

wifi\_frequency\_bands

IEEE 802.11 operational frequency bands (not exhaustive).

**Definition** wifi.h:233

[wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)

wifi\_mfp\_options

IEEE 802.11w - Management frame protection.

**Definition** wifi.h:212

[wifi\_eap\_tls\_cipher\_type](group__wifi__mgmt.md#ga218525a9d9ee64524f983e52d5767562)

wifi\_eap\_tls\_cipher\_type

**Definition** wifi.h:135

[wifi\_mfp\_txt](group__wifi__mgmt.md#ga22354241197a9227fdba77e67d471f5c)

const char \* wifi\_mfp\_txt(enum wifi\_mfp\_options mfp)

Helper function to get user-friendly MFP name.

[wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7)

wifi\_ps\_exit\_strategy

Wi-Fi power save exit strategy.

**Definition** wifi.h:623

[wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)

wifi\_twt\_setup\_cmd

Wi-Fi Target Wake Time (TWT) setup commands.

**Definition** wifi.h:496

[wifi\_frequency\_bandwidths](group__wifi__mgmt.md#ga3b01cead3c2eb4581fe85e2aaaffbd49)

wifi\_frequency\_bandwidths

IEEE 802.11 operational frequency bandwidths (not exhaustive).

**Definition** wifi.h:255

[wifi\_band\_txt](group__wifi__mgmt.md#ga44f875bf0d931b66d582f5dca2d65ed5)

const char \* wifi\_band\_txt(enum wifi\_frequency\_bands band)

Helper function to get user-friendly frequency band name.

[wifi\_wpa3\_enterprise\_type](group__wifi__mgmt.md#ga48fea1f0c7d2700cef47068f96c6b71a)

wifi\_wpa3\_enterprise\_type

WPA3 Enterprise security types.

**Definition** wifi.h:118

[wifi\_operational\_modes](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35)

wifi\_operational\_modes

Wifi operational mode.

**Definition** wifi.h:444

[wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)

wifi\_twt\_setup\_resp\_status

Wi-Fi Target Wake Time (TWT) negotiation status.

**Definition** wifi.h:519

[wifi\_btm\_query\_reason](group__wifi__mgmt.md#ga4fced9c3627d8f65d75e1651b11916b0)

wifi\_btm\_query\_reason

IEEE 802.11v BTM (BSS transition management) Query reasons.

**Definition** wifi.h:678

[wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)

wifi\_iface\_mode

Wi-Fi interface modes.

**Definition** wifi.h:347

[wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8)

wifi\_twt\_negotiation\_type

Wi-Fi Target Wake Time (TWT) negotiation types.

**Definition** wifi.h:483

[wifi\_twt\_negotiation\_type\_txt](group__wifi__mgmt.md#ga6a74e999d63ee491df68447219ef2a0d)

const char \* wifi\_twt\_negotiation\_type\_txt(enum wifi\_twt\_negotiation\_type twt\_negotiation)

Helper function to get user-friendly twt negotiation type name.

[wifi\_ps\_wakeup\_mode\_txt](group__wifi__mgmt.md#ga6fd645f891234136b3028574a0af9666)

const char \* wifi\_ps\_wakeup\_mode\_txt(enum wifi\_ps\_wakeup\_mode ps\_wakeup\_mode)

Helper function to get user-friendly ps wakeup mode name.

[wifi\_cipher\_type](group__wifi__mgmt.md#ga7f7b23ac019ca504a2006f0376735645)

wifi\_cipher\_type

Group cipher and pairwise cipher types.

**Definition** wifi.h:145

[wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642)

wifi\_ap\_config\_param

Wi-Fi AP mode configuration parameter.

**Definition** wifi.h:698

[wifi\_ps\_get\_config\_err\_code\_str](group__wifi__mgmt.md#ga8b72e7989964963a25f42ed1dba240a0)

static const char \* wifi\_ps\_get\_config\_err\_code\_str(int16\_t err\_no)

Helper function to get user-friendly power save error code name.

**Definition** wifi.h:688

[wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331)

wifi\_eap\_type

EPA method Types.

**Definition** wifi.h:98

[wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6)

wifi\_twt\_fail\_reason

Target Wake Time (TWT) error codes.

**Definition** wifi.h:527

[wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4)

wifi\_iface\_state

Wi-Fi interface states.

**Definition** wifi.h:299

[wifi\_security\_txt](group__wifi__mgmt.md#ga9bb9f658d7806e42b3ee351fb3e7dfa0)

const char \* wifi\_security\_txt(enum wifi\_security\_type security)

Helper function to get user-friendly security type name.

[wifi\_filter](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f)

wifi\_filter

Mode filter settings.

**Definition** wifi.h:460

[wifi\_twt\_get\_err\_code\_str](group__wifi__mgmt.md#gab2e6a6e1d8358a8f34d67bd632709b3d)

static const char \* wifi\_twt\_get\_err\_code\_str(int16\_t err\_no)

Helper function to get user-friendly TWT error code name.

**Definition** wifi.h:584

[wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)

wifi\_link\_mode

Wi-Fi link operating modes.

**Definition** wifi.h:375

[wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)

wifi\_ps\_param\_type

Wi-Fi power save parameters.

**Definition** wifi.h:594

[wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)

wifi\_ps\_wakeup\_mode

Wi-Fi power save modes.

**Definition** wifi.h:610

[wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)

wifi\_twt\_operation

Wi-Fi Target Wake Time (TWT) operations.

**Definition** wifi.h:472

[wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)

wifi\_scan\_type

Wi-Fi scanning types.

**Definition** wifi.h:406

[wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)

wifi\_twt\_teardown\_status

Wi-Fi Target Wake Time (TWT) teradown status.

**Definition** wifi.h:553

[wifi\_mode\_txt](group__wifi__mgmt.md#gad78536ce1f30accfa45f258b6bf8c73d)

const char \* wifi\_mode\_txt(enum wifi\_iface\_mode mode)

Helper function to get user-friendly interface mode name.

[wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)

wifi\_config\_ps\_param\_fail\_reason

Wi-Fi power save error codes.

**Definition** wifi.h:639

[wifi\_twt\_operation\_txt](group__wifi__mgmt.md#gadb125925e851bf7569424cd4295e7712)

const char \* wifi\_twt\_operation\_txt(enum wifi\_twt\_operation twt\_operation)

Helper function to get user-friendly twt operation name.

[wifi\_ps\_mode\_txt](group__wifi__mgmt.md#gadb21d49f64e04fba59433e51d5b3481c)

const char \* wifi\_ps\_mode\_txt(enum wifi\_ps\_mode ps\_mode)

Helper function to get user-friendly ps mode name.

[wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c)

wifi\_security\_type

IEEE 802.11 security types.

**Definition** wifi.h:42

[wifi\_twt\_setup\_cmd\_txt](group__wifi__mgmt.md#gae3ca047cc6ef6b6a2e44ba6574d41a44)

const char \* wifi\_twt\_setup\_cmd\_txt(enum wifi\_twt\_setup\_cmd twt\_setup)

Helper function to get user-friendly twt setup cmd name.

[wifi\_bandwidth\_txt](group__wifi__mgmt.md#gae479798eb864c3784d1c8c9375658647)

const char \*const wifi\_bandwidth\_txt(enum wifi\_frequency\_bandwidths bandwidth)

[wifi\_wpa3\_enterprise\_txt](group__wifi__mgmt.md#gaf67f2900be88fdf3f282400d09f2ab88)

const char \* wifi\_wpa3\_enterprise\_txt(enum wifi\_wpa3\_enterprise\_type wpa3\_ent)

Helper function to get user-friendly wpa3 enterprise security type name.

[wifi\_group\_mgmt\_cipher\_type](group__wifi__mgmt.md#gaf84d5e1a68393483fc6063c06b8f26e0)

wifi\_group\_mgmt\_cipher\_type

group mgmt cipher types.

**Definition** wifi.h:155

[wifi\_ps\_txt](group__wifi__mgmt.md#gafbeb5f7fa97fd2ba0c691da0f8853ef2)

const char \* wifi\_ps\_txt(enum wifi\_ps ps\_name)

Helper function to get user-friendly ps name.

[wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c)

wifi\_ps\_mode

Wi-Fi power save modes.

**Definition** wifi.h:425

[WIFI\_PS\_ENABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47)

@ WIFI\_PS\_ENABLED

Power save enabled.

**Definition** wifi.h:418

[WIFI\_PS\_DISABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82)

@ WIFI\_PS\_DISABLED

Power save disabled.

**Definition** wifi.h:416

[WIFI\_FREQ\_BAND\_6\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0)

@ WIFI\_FREQ\_BAND\_6\_GHZ

6 GHz band (Wi-Fi 6E, also extends to 7GHz).

**Definition** wifi.h:239

[WIFI\_FREQ\_BAND\_2\_4\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11)

@ WIFI\_FREQ\_BAND\_2\_4\_GHZ

2.4 GHz band.

**Definition** wifi.h:235

[WIFI\_FREQ\_BAND\_UNKNOWN](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)

@ WIFI\_FREQ\_BAND\_UNKNOWN

Invalid frequency band.

**Definition** wifi.h:246

[WIFI\_FREQ\_BAND\_5\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895)

@ WIFI\_FREQ\_BAND\_5\_GHZ

5 GHz band.

**Definition** wifi.h:237

[WIFI\_FREQ\_BAND\_MAX](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5)

@ WIFI\_FREQ\_BAND\_MAX

Highest frequency band available.

**Definition** wifi.h:244

[WIFI\_MFP\_DISABLE](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969)

@ WIFI\_MFP\_DISABLE

MFP disabled.

**Definition** wifi.h:214

[WIFI\_MFP\_OPTIONAL](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf)

@ WIFI\_MFP\_OPTIONAL

MFP optional.

**Definition** wifi.h:216

[WIFI\_MFP\_REQUIRED](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840)

@ WIFI\_MFP\_REQUIRED

MFP required.

**Definition** wifi.h:218

[WIFI\_EAP\_TLS\_NONE](group__wifi__mgmt.md#gga218525a9d9ee64524f983e52d5767562a38f97de2297f9df6e4ac3cecfd0799df)

@ WIFI\_EAP\_TLS\_NONE

EAP TLS with NONE.

**Definition** wifi.h:137

[WIFI\_EAP\_TLS\_RSA\_3K](group__wifi__mgmt.md#gga218525a9d9ee64524f983e52d5767562ac5436dc7d2bbeded043b1102ee592e17)

@ WIFI\_EAP\_TLS\_RSA\_3K

EAP TLS with ECDH & RSA with > 3K.

**Definition** wifi.h:141

[WIFI\_EAP\_TLS\_ECC\_P384](group__wifi__mgmt.md#gga218525a9d9ee64524f983e52d5767562ae44c04c2d1510385fe43827dbe6026f9)

@ WIFI\_EAP\_TLS\_ECC\_P384

EAP TLS with ECDH & ECDSA with p384.

**Definition** wifi.h:139

[WIFI\_PS\_EXIT\_EVERY\_TIM](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832)

@ WIFI\_PS\_EXIT\_EVERY\_TIM

QoS NULL frame based.

**Definition** wifi.h:627

[WIFI\_PS\_EXIT\_CUSTOM\_ALGO](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5)

@ WIFI\_PS\_EXIT\_CUSTOM\_ALGO

PS-Poll frame based.

**Definition** wifi.h:625

[WIFI\_TWT\_SETUP\_CMD\_DEMAND](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e)

@ WIFI\_TWT\_SETUP\_CMD\_DEMAND

TWT setup demand (parameters can not be changed by AP).

**Definition** wifi.h:502

[WIFI\_TWT\_SETUP\_CMD\_REQUEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd)

@ WIFI\_TWT\_SETUP\_CMD\_REQUEST

TWT setup request.

**Definition** wifi.h:498

[WIFI\_TWT\_SETUP\_CMD\_ALTERNATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1)

@ WIFI\_TWT\_SETUP\_CMD\_ALTERNATE

TWT setup alternate (alternate parameters suggested by AP).

**Definition** wifi.h:508

[WIFI\_TWT\_SETUP\_CMD\_GROUPING](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279)

@ WIFI\_TWT\_SETUP\_CMD\_GROUPING

TWT setup grouping (grouping of TWT flows).

**Definition** wifi.h:504

[WIFI\_TWT\_SETUP\_CMD\_DICTATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3)

@ WIFI\_TWT\_SETUP\_CMD\_DICTATE

TWT setup dictate (parameters dictated by AP).

**Definition** wifi.h:510

[WIFI\_TWT\_SETUP\_CMD\_SUGGEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648)

@ WIFI\_TWT\_SETUP\_CMD\_SUGGEST

TWT setup suggest (parameters can be changed by AP).

**Definition** wifi.h:500

[WIFI\_TWT\_SETUP\_CMD\_REJECT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565)

@ WIFI\_TWT\_SETUP\_CMD\_REJECT

TWT setup reject (parameters rejected by AP).

**Definition** wifi.h:512

[WIFI\_TWT\_SETUP\_CMD\_ACCEPT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a)

@ WIFI\_TWT\_SETUP\_CMD\_ACCEPT

TWT setup accept (parameters accepted by AP).

**Definition** wifi.h:506

[WIFI\_FREQ\_BANDWIDTH\_80MHZ](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49a2c445a7a6345a66a41248bde2f7bf8cb)

@ WIFI\_FREQ\_BANDWIDTH\_80MHZ

80 MHz.

**Definition** wifi.h:261

[WIFI\_FREQ\_BANDWIDTH\_UNKNOWN](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49a4e45ec9ffe32912a5673f9bbffeeef2d)

@ WIFI\_FREQ\_BANDWIDTH\_UNKNOWN

Invalid frequency bandwidth.

**Definition** wifi.h:268

[WIFI\_FREQ\_BANDWIDTH\_40MHZ](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49a9f984c246be1976cf1b799c4aed02ea1)

@ WIFI\_FREQ\_BANDWIDTH\_40MHZ

40 MHz.

**Definition** wifi.h:259

[WIFI\_FREQ\_BANDWIDTH\_20MHZ](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49ae5efe45d5211477322968e55014d22d5)

@ WIFI\_FREQ\_BANDWIDTH\_20MHZ

20 MHz.

**Definition** wifi.h:257

[WIFI\_FREQ\_BANDWIDTH\_MAX](group__wifi__mgmt.md#gga3b01cead3c2eb4581fe85e2aaaffbd49af57b996c36f950143c9f23a25d402b90)

@ WIFI\_FREQ\_BANDWIDTH\_MAX

Highest frequency bandwidth available.

**Definition** wifi.h:266

[WIFI\_WPA3\_ENTERPRISE\_SUITEB\_192](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aa577671035478f3a385b8e4fdf6abf5fa)

@ WIFI\_WPA3\_ENTERPRISE\_SUITEB\_192

WPA3 enterprise Suite-B-192 (PMFR + WPA3-Suite-B-192).

**Definition** wifi.h:124

[WIFI\_WPA3\_ENTERPRISE\_NA](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aa7c34eb5cf3e76c3c1b45c424436adbb1)

@ WIFI\_WPA3\_ENTERPRISE\_NA

No WPA3 enterprise, either WPA2 Enterprise or personal mode.

**Definition** wifi.h:120

[WIFI\_WPA3\_ENTERPRISE\_SUITEB](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aaec90b38cb8fb95ff3a679da473537589)

@ WIFI\_WPA3\_ENTERPRISE\_SUITEB

WPA3 enterprise Suite-B (PMFR + WPA3-Suite-B).

**Definition** wifi.h:122

[WIFI\_WPA3\_ENTERPRISE\_ONLY](group__wifi__mgmt.md#gga48fea1f0c7d2700cef47068f96c6b71aaf13490bee764dd77f770f07bf3dac3fa)

@ WIFI\_WPA3\_ENTERPRISE\_ONLY

WPA3 enterprise only (PMFR + WPA2-ENT disabled).

**Definition** wifi.h:126

[WIFI\_TX\_INJECTION\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74)

@ WIFI\_TX\_INJECTION\_MODE

TX injection mode setting enable.

**Definition** wifi.h:450

[WIFI\_STA\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7)

@ WIFI\_STA\_MODE

STA mode setting enable.

**Definition** wifi.h:446

[WIFI\_AP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd)

@ WIFI\_AP\_MODE

AP mode setting enable.

**Definition** wifi.h:454

[WIFI\_SOFTAP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623)

@ WIFI\_SOFTAP\_MODE

Softap mode setting enable.

**Definition** wifi.h:456

[WIFI\_MONITOR\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696)

@ WIFI\_MONITOR\_MODE

Monitor mode setting enable.

**Definition** wifi.h:448

[WIFI\_PROMISCUOUS\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56)

@ WIFI\_PROMISCUOUS\_MODE

Promiscuous mode setting enable.

**Definition** wifi.h:452

[WIFI\_TWT\_RESP\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286)

@ WIFI\_TWT\_RESP\_RECEIVED

TWT response received for TWT request.

**Definition** wifi.h:521

[WIFI\_TWT\_RESP\_NOT\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72)

@ WIFI\_TWT\_RESP\_NOT\_RECEIVED

TWT response not received for TWT request.

**Definition** wifi.h:523

[WIFI\_BTM\_QUERY\_REASON\_UNSPECIFIED](group__wifi__mgmt.md#gga4fced9c3627d8f65d75e1651b11916b0a41376bed59184da60f7c6558d2524c58)

@ WIFI\_BTM\_QUERY\_REASON\_UNSPECIFIED

Unspecified.

**Definition** wifi.h:680

[WIFI\_BTM\_QUERY\_REASON\_LEAVING\_ESS](group__wifi__mgmt.md#gga4fced9c3627d8f65d75e1651b11916b0a5491f6eabeae1cd0faec69b5ced04f49)

@ WIFI\_BTM\_QUERY\_REASON\_LEAVING\_ESS

Leaving ESS.

**Definition** wifi.h:684

[WIFI\_BTM\_QUERY\_REASON\_LOW\_RSSI](group__wifi__mgmt.md#gga4fced9c3627d8f65d75e1651b11916b0a718e2d9c2f18fafc70c389177a4a5257)

@ WIFI\_BTM\_QUERY\_REASON\_LOW\_RSSI

Low RSSI.

**Definition** wifi.h:682

[WIFI\_MODE\_AP](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8)

@ WIFI\_MODE\_AP

AP mode.

**Definition** wifi.h:353

[WIFI\_MODE\_IBSS](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b)

@ WIFI\_MODE\_IBSS

IBSS (ad-hoc) station mode.

**Definition** wifi.h:351

[WIFI\_MODE\_P2P\_GO](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889)

@ WIFI\_MODE\_P2P\_GO

P2P group owner mode.

**Definition** wifi.h:355

[WIFI\_MODE\_P2P\_GROUP\_FORMATION](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521)

@ WIFI\_MODE\_P2P\_GROUP\_FORMATION

P2P group formation mode.

**Definition** wifi.h:357

[WIFI\_MODE\_INFRA](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813)

@ WIFI\_MODE\_INFRA

Infrastructure station mode.

**Definition** wifi.h:349

[WIFI\_MODE\_MESH](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68)

@ WIFI\_MODE\_MESH

802.11s Mesh mode.

**Definition** wifi.h:359

[WIFI\_TWT\_BROADCAST](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa)

@ WIFI\_TWT\_BROADCAST

TWT broadcast negotiation.

**Definition** wifi.h:487

[WIFI\_TWT\_WAKE\_TBTT](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978)

@ WIFI\_TWT\_WAKE\_TBTT

TWT wake TBTT negotiation.

**Definition** wifi.h:489

[WIFI\_TWT\_INDIVIDUAL](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0)

@ WIFI\_TWT\_INDIVIDUAL

TWT individual negotiation.

**Definition** wifi.h:485

[WPA\_CAPA\_ENC\_GCMP\_256](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4)

@ WPA\_CAPA\_ENC\_GCMP\_256

256-bit Galois/Counter Mode Protocol.

**Definition** wifi.h:151

[WPA\_CAPA\_ENC\_GCMP](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d)

@ WPA\_CAPA\_ENC\_GCMP

128-bit Galois/Counter Mode Protocol.

**Definition** wifi.h:149

[WPA\_CAPA\_ENC\_CCMP](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1)

@ WPA\_CAPA\_ENC\_CCMP

AES in counter mode with CBC-MAC (CCMP-128).

**Definition** wifi.h:147

[WIFI\_AP\_CONFIG\_PARAM\_BANDWIDTH](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a1c9f37033909236e6a2259465dda4ef7)

@ WIFI\_AP\_CONFIG\_PARAM\_BANDWIDTH

Used for AP mode configuration parameter bandwidth.

**Definition** wifi.h:704

[WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c)

@ WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY

Used for AP mode configuration parameter ap\_max\_inactivity.

**Definition** wifi.h:700

[WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958)

@ WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA

Used for AP mode configuration parameter max\_num\_sta.

**Definition** wifi.h:702

[WIFI\_AP\_CONFIG\_PARAM\_VHT\_CAPAB](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642ac22e71c91a433674f0a96ec853539902)

@ WIFI\_AP\_CONFIG\_PARAM\_VHT\_CAPAB

Used for AP mode configuration parameter vht\_capab.

**Definition** wifi.h:708

[WIFI\_AP\_CONFIG\_PARAM\_HT\_CAPAB](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642ac357562788ce489023e9e66296401199)

@ WIFI\_AP\_CONFIG\_PARAM\_HT\_CAPAB

Used for AP mode configuration parameter ht\_capab.

**Definition** wifi.h:706

[WIFI\_EAP\_TYPE\_TTLS](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a35fce37fccb3d27596c4e0a531109dac)

@ WIFI\_EAP\_TYPE\_TTLS

EPA TTLS security, refer to rfc5281.

**Definition** wifi.h:106

[WIFI\_EAP\_TYPE\_MSCHAPV2](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a37f7681b1fb5d7165010ec941018882f)

@ WIFI\_EAP\_TYPE\_MSCHAPV2

EPA MSCHAPV2 security, refer to draft-kamath-pppext-eap-mschapv2-00.txt.

**Definition** wifi.h:110

[WIFI\_EAP\_TYPE\_NONE](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a39edcc7a267ce608a1e818948b5d172b)

@ WIFI\_EAP\_TYPE\_NONE

No EPA security.

**Definition** wifi.h:100

[WIFI\_EAP\_TYPE\_TLS](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a505b4b888231dd1fbc169d612d8f0c38)

@ WIFI\_EAP\_TYPE\_TLS

EPA TLS security, refer to rfc5216.

**Definition** wifi.h:104

[WIFI\_EAP\_TYPE\_GTC](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a64daad77662868322e638da6531a5c0f)

@ WIFI\_EAP\_TYPE\_GTC

EPA GTC security, refer to rfc3748 chapter 5.

**Definition** wifi.h:102

[WIFI\_EAP\_TYPE\_PEAP](group__wifi__mgmt.md#gga92b6fa6755491c3bd61f895213d07331a8e619153aa3dad398c6ced36605f5e3f)

@ WIFI\_EAP\_TYPE\_PEAP

EPA PEAP security, refer to draft-josefsson-pppext-eap-tls-eap-06.txt.

**Definition** wifi.h:108

[WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee)

@ WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED

IP address not assigned or configured.

**Definition** wifi.h:547

[WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6)

@ WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID

Invalid negotiated flow id.

**Definition** wifi.h:545

[WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556)

@ WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL

Command execution failed.

**Definition** wifi.h:531

[WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d)

@ WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED

Operation not supported.

**Definition** wifi.h:533

[WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef)

@ WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS

Unable to get interface status.

**Definition** wifi.h:535

[WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860)

@ WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB

Peer not HE (802.11ax/Wi-Fi 6) capable.

**Definition** wifi.h:539

[WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831)

@ WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED

Device not connected to AP.

**Definition** wifi.h:537

[WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7)

@ WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS

A TWT flow is already in progress.

**Definition** wifi.h:543

[WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce)

@ WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB

Peer not TWT capable.

**Definition** wifi.h:541

[WIFI\_TWT\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13)

@ WIFI\_TWT\_FAIL\_UNSPECIFIED

Unspecified error.

**Definition** wifi.h:529

[WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)

@ WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS

Flow already exists.

**Definition** wifi.h:549

[WIFI\_STATE\_DISCONNECTED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f)

@ WIFI\_STATE\_DISCONNECTED

Interface is disconnected.

**Definition** wifi.h:301

[WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e)

@ WIFI\_STATE\_GROUP\_HANDSHAKE

Group Key exchange with a network is in progress.

**Definition** wifi.h:317

[WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c)

@ WIFI\_STATE\_INTERFACE\_DISABLED

Interface is disabled (administratively).

**Definition** wifi.h:303

[WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969)

@ WIFI\_STATE\_4WAY\_HANDSHAKE

4-way handshake with a network is in progress.

**Definition** wifi.h:315

[WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc)

@ WIFI\_STATE\_ASSOCIATED

Association with a network completed.

**Definition** wifi.h:313

[WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b)

@ WIFI\_STATE\_SCANNING

Interface is scanning for networks.

**Definition** wifi.h:307

[WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba)

@ WIFI\_STATE\_AUTHENTICATING

Authentication with a network is in progress.

**Definition** wifi.h:309

[WIFI\_STATE\_COMPLETED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f)

@ WIFI\_STATE\_COMPLETED

All authentication completed, ready to pass data.

**Definition** wifi.h:319

[WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b)

@ WIFI\_STATE\_ASSOCIATING

Association with a network is in progress.

**Definition** wifi.h:311

[WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598)

@ WIFI\_STATE\_INACTIVE

No enabled networks in the configuration.

**Definition** wifi.h:305

[WIFI\_PACKET\_FILTER\_MGMT](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc)

@ WIFI\_PACKET\_FILTER\_MGMT

Support only sniffing of management packets.

**Definition** wifi.h:464

[WIFI\_PACKET\_FILTER\_ALL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b)

@ WIFI\_PACKET\_FILTER\_ALL

Support management, data and control packet sniffing.

**Definition** wifi.h:462

[WIFI\_PACKET\_FILTER\_DATA](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244)

@ WIFI\_PACKET\_FILTER\_DATA

Support only sniffing of data packets.

**Definition** wifi.h:466

[WIFI\_PACKET\_FILTER\_CTRL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de)

@ WIFI\_PACKET\_FILTER\_CTRL

Support only sniffing of control packets.

**Definition** wifi.h:468

[WIFI\_6E](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6)

@ WIFI\_6E

802.11ax 6GHz.

**Definition** wifi.h:391

[WIFI\_5](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824)

@ WIFI\_5

802.11ac.

**Definition** wifi.h:387

[WIFI\_0](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8)

@ WIFI\_0

802.11 (legacy).

**Definition** wifi.h:377

[WIFI\_7](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934)

@ WIFI\_7

802.11be.

**Definition** wifi.h:393

[WIFI\_4](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2)

@ WIFI\_4

802.11n.

**Definition** wifi.h:385

[WIFI\_2](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9)

@ WIFI\_2

802.11a.

**Definition** wifi.h:381

[WIFI\_6](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe)

@ WIFI\_6

802.11ax.

**Definition** wifi.h:389

[WIFI\_1](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c)

@ WIFI\_1

802.11b.

**Definition** wifi.h:379

[WIFI\_3](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362)

@ WIFI\_3

802.11g.

**Definition** wifi.h:383

[WIFI\_PS\_PARAM\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90)

@ WIFI\_PS\_PARAM\_LISTEN\_INTERVAL

Power save listen interval (units: (short) beacon intervals).

**Definition** wifi.h:598

[WIFI\_PS\_PARAM\_STATE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d)

@ WIFI\_PS\_PARAM\_STATE

Power save state.

**Definition** wifi.h:596

[WIFI\_PS\_PARAM\_EXIT\_STRATEGY](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03)

@ WIFI\_PS\_PARAM\_EXIT\_STRATEGY

Power save exit strategy.

**Definition** wifi.h:604

[WIFI\_PS\_PARAM\_WAKEUP\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8)

@ WIFI\_PS\_PARAM\_WAKEUP\_MODE

Power save wakeup mode.

**Definition** wifi.h:600

[WIFI\_PS\_PARAM\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab)

@ WIFI\_PS\_PARAM\_MODE

Power save mode.

**Definition** wifi.h:602

[WIFI\_PS\_PARAM\_TIMEOUT](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29)

@ WIFI\_PS\_PARAM\_TIMEOUT

Power save timeout.

**Definition** wifi.h:606

[WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30)

@ WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL

Listen interval based wakeup.

**Definition** wifi.h:614

[WIFI\_PS\_WAKEUP\_MODE\_DTIM](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6)

@ WIFI\_PS\_WAKEUP\_MODE\_DTIM

DTIM based wakeup.

**Definition** wifi.h:612

[WIFI\_TWT\_SETUP](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45)

@ WIFI\_TWT\_SETUP

TWT setup operation.

**Definition** wifi.h:474

[WIFI\_TWT\_TEARDOWN](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f)

@ WIFI\_TWT\_TEARDOWN

TWT teardown operation.

**Definition** wifi.h:476

[WIFI\_SCAN\_TYPE\_ACTIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9)

@ WIFI\_SCAN\_TYPE\_ACTIVE

Active scanning (default).

**Definition** wifi.h:408

[WIFI\_SCAN\_TYPE\_PASSIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f)

@ WIFI\_SCAN\_TYPE\_PASSIVE

Passive scanning.

**Definition** wifi.h:410

[WIFI\_TWT\_TEARDOWN\_SUCCESS](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965)

@ WIFI\_TWT\_TEARDOWN\_SUCCESS

TWT teardown success.

**Definition** wifi.h:555

[WIFI\_TWT\_TEARDOWN\_FAILED](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d)

@ WIFI\_TWT\_TEARDOWN\_FAILED

TWT teardown failure.

**Definition** wifi.h:557

[WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3)

@ WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS

Unable to get interface status.

**Definition** wifi.h:647

[WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38)

@ WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED

Unspecified error.

**Definition** wifi.h:641

[WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394)

@ WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL

Command execution failed.

**Definition** wifi.h:643

[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a)

@ WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED

Device not connected to AP.

**Definition** wifi.h:649

[WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)

@ WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID

Listen interval out of range.

**Definition** wifi.h:653

[WIFI\_PS\_PARAM\_FAIL\_INVALID\_EXIT\_STRATEGY](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce)

@ WIFI\_PS\_PARAM\_FAIL\_INVALID\_EXIT\_STRATEGY

Invalid exit strategy.

**Definition** wifi.h:655

[WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093)

@ WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED

Parameter not supported.

**Definition** wifi.h:645

[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486)

@ WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED

Device already connected to AP.

**Definition** wifi.h:651

[WIFI\_SECURITY\_TYPE\_SAE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f)

@ WIFI\_SECURITY\_TYPE\_SAE

WPA3-SAE security.

**Definition** wifi.h:50

[WIFI\_SECURITY\_TYPE\_FT\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5)

@ WIFI\_SECURITY\_TYPE\_FT\_EAP

FT-EAP security.

**Definition** wifi.h:84

[WIFI\_SECURITY\_TYPE\_PSK\_SHA256](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e)

@ WIFI\_SECURITY\_TYPE\_PSK\_SHA256

WPA2-PSK-SHA256 security.

**Definition** wifi.h:48

[WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_GTC](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca0c9db910757c5a715a5e88089362fab5)

@ WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_GTC

EAP PEAP GTC security - Enterprise.

**Definition** wifi.h:74

[WIFI\_SECURITY\_TYPE\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368)

@ WIFI\_SECURITY\_TYPE\_PSK

WPA2-PSK security.

**Definition** wifi.h:46

[WIFI\_SECURITY\_TYPE\_SAE\_H2E](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca1e45d14be678d0693b3f03f73fc5b0df)

@ WIFI\_SECURITY\_TYPE\_SAE\_H2E

WPA3-SAE security with hash-to-element.

**Definition** wifi.h:54

[WIFI\_SECURITY\_TYPE\_WPA\_AUTO\_PERSONAL](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff)

@ WIFI\_SECURITY\_TYPE\_WPA\_AUTO\_PERSONAL

WPA/WPA2/WPA3 PSK security.

**Definition** wifi.h:68

[WIFI\_SECURITY\_TYPE\_WAPI](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d)

@ WIFI\_SECURITY\_TYPE\_WAPI

GB 15629.11-2003 WAPI security.

**Definition** wifi.h:58

[WIFI\_SECURITY\_TYPE\_WEP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724)

@ WIFI\_SECURITY\_TYPE\_WEP

WEP security.

**Definition** wifi.h:64

[WIFI\_SECURITY\_TYPE\_EAP\_TTLS\_MSCHAPV2](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca3a20bf15c1e51313629789e6abe0273d)

@ WIFI\_SECURITY\_TYPE\_EAP\_TTLS\_MSCHAPV2

EAP TTLS MSCHAPV2 security - Enterprise.

**Definition** wifi.h:76

[WIFI\_SECURITY\_TYPE\_NONE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e)

@ WIFI\_SECURITY\_TYPE\_NONE

No security.

**Definition** wifi.h:44

[WIFI\_SECURITY\_TYPE\_FT\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5)

@ WIFI\_SECURITY\_TYPE\_FT\_PSK

FT-PSK security.

**Definition** wifi.h:80

[WIFI\_SECURITY\_TYPE\_SAE\_AUTO](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca4beacdae98f8ca155609d2fd660c5ed0)

@ WIFI\_SECURITY\_TYPE\_SAE\_AUTO

WPA3-SAE security with both hunting-and-pecking loop and hash-to-element enabled.

**Definition** wifi.h:56

[WIFI\_SECURITY\_TYPE\_WPA\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a)

@ WIFI\_SECURITY\_TYPE\_WPA\_PSK

WPA-PSK security.

**Definition** wifi.h:66

[WIFI\_SECURITY\_TYPE\_FT\_EAP\_SHA384](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93)

@ WIFI\_SECURITY\_TYPE\_FT\_EAP\_SHA384

FT-EAP-SHA384 security.

**Definition** wifi.h:86

[WIFI\_SECURITY\_TYPE\_SAE\_EXT\_KEY](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca64221ce0052ce510e16537a32c67bb02)

@ WIFI\_SECURITY\_TYPE\_SAE\_EXT\_KEY

SAE Extended key (uses group-dependent hashing).

**Definition** wifi.h:88

[WIFI\_SECURITY\_TYPE\_DPP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca6cf0bd5db90deaa6b35f7afe122e8b5f)

@ WIFI\_SECURITY\_TYPE\_DPP

DPP security.

**Definition** wifi.h:70

[WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_TLS](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca6d2e5f72b8bf76f093ab79be2a4b9477)

@ WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_TLS

EAP PEAP security - Enterprise.

**Definition** wifi.h:78

[WIFI\_SECURITY\_TYPE\_EAP\_TLS](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca85bcce61e75c01eb95083523e8925a40)

@ WIFI\_SECURITY\_TYPE\_EAP\_TLS

EAP TLS security - Enterprise.

**Definition** wifi.h:62

[WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_MSCHAPV2](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9caaa1dbea0100af80ca48ad594cddb4212)

@ WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_MSCHAPV2

EAP PEAP MSCHAPV2 security - Enterprise.

**Definition** wifi.h:72

[WIFI\_SECURITY\_TYPE\_SAE\_HNP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9caab329c818e10cbe98aac1f9c30849c91)

@ WIFI\_SECURITY\_TYPE\_SAE\_HNP

WPA3-SAE security with hunting-and-pecking loop.

**Definition** wifi.h:52

[WIFI\_SECURITY\_TYPE\_FT\_SAE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092)

@ WIFI\_SECURITY\_TYPE\_FT\_SAE

FT-SAE security.

**Definition** wifi.h:82

[WIFI\_SECURITY\_TYPE\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80)

@ WIFI\_SECURITY\_TYPE\_EAP

EAP security - Enterprise.

**Definition** wifi.h:60

[WPA\_CAPA\_ENC\_BIP](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8)

@ WPA\_CAPA\_ENC\_BIP

128-bit Broadcast/Multicast Integrity Protocol Cipher-based Message Authentication Code .

**Definition** wifi.h:159

[WPA\_CAPA\_ENC\_BIP\_GMAC\_128](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70)

@ WPA\_CAPA\_ENC\_BIP\_GMAC\_128

128-bit Broadcast/Multicast Integrity Protocol Galois Message Authentication Code .

**Definition** wifi.h:163

[WPA\_CAPA\_ENC\_BIP\_GMAC\_256](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096)

@ WPA\_CAPA\_ENC\_BIP\_GMAC\_256

256-bit Broadcast/Multicast Integrity Protocol Galois Message Authentication Code .

**Definition** wifi.h:167

[WIFI\_PS\_MODE\_WMM](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5)

@ WIFI\_PS\_MODE\_WMM

WMM power save mode.

**Definition** wifi.h:432

[WIFI\_PS\_MODE\_LEGACY](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd)

@ WIFI\_PS\_MODE\_LEGACY

Legacy power save mode.

**Definition** wifi.h:427

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[wifi\_cipher\_desc](structwifi__cipher__desc.md)

**Definition** wifi.h:170

[wifi\_cipher\_desc::capa](structwifi__cipher__desc.md#a6751019bb6da3032ca2f7bc42a3469e3)

unsigned int capa

Cipher capability.

**Definition** wifi.h:172

[wifi\_cipher\_desc::name](structwifi__cipher__desc.md#a9396239f38613b151232a4c5f3d66a8f)

char \* name

Cipher name string.

**Definition** wifi.h:174

[wifi\_eap\_cipher\_config](structwifi__eap__cipher__config.md)

**Definition** wifi.h:177

[wifi\_eap\_cipher\_config::openssl\_ciphers](structwifi__eap__cipher__config.md#a14128465917447f38d3854444a9bf6e1)

char \* openssl\_ciphers

OpenSSL cipher string.

**Definition** wifi.h:181

[wifi\_eap\_cipher\_config::key\_mgmt](structwifi__eap__cipher__config.md#a385d365bb70a70fa09d321c55988afcc)

char \* key\_mgmt

Key management type string.

**Definition** wifi.h:179

[wifi\_eap\_cipher\_config::pairwise\_cipher](structwifi__eap__cipher__config.md#a3917f94dfafb22df260db9c4a129c3c4)

char \* pairwise\_cipher

Pairwise\_cipher cipher string.

**Definition** wifi.h:185

[wifi\_eap\_cipher\_config::group\_cipher](structwifi__eap__cipher__config.md#aa505ae934897742078aa46f1fdb5d0d1)

char \* group\_cipher

Group cipher cipher string.

**Definition** wifi.h:183

[wifi\_eap\_cipher\_config::group\_mgmt\_cipher](structwifi__eap__cipher__config.md#ab53f5b5419b2b8c8a869ba4f9d645a41)

char \* group\_mgmt\_cipher

Group management cipher string.

**Definition** wifi.h:187

[wifi\_eap\_cipher\_config::tls\_flags](structwifi__eap__cipher__config.md#ae9a4b8a0f0b47ac1065562ce287473a5)

char \* tls\_flags

Used to confiure TLS features.

**Definition** wifi.h:189

[wifi\_eap\_config](structwifi__eap__config.md)

**Definition** wifi.h:192

[wifi\_eap\_config::type](structwifi__eap__config.md#a031a5c86551f90130ff74ed53977c49d)

enum wifi\_security\_type type

Security type.

**Definition** wifi.h:194

[wifi\_eap\_config::method](structwifi__eap__config.md#aa7a42a1256ef26562e83f47498d87113)

char \* method

EAP method string.

**Definition** wifi.h:200

[wifi\_eap\_config::eap\_type\_phase2](structwifi__eap__config.md#aaf73f2f986d56f95d196d02dcecbaff1)

enum wifi\_eap\_type eap\_type\_phase2

EAP method type of phase2.

**Definition** wifi.h:198

[wifi\_eap\_config::eap\_type\_phase1](structwifi__eap__config.md#ab44893426c89416ab24e3bfb57bf49ad)

enum wifi\_eap\_type eap\_type\_phase1

EAP method type of phase1.

**Definition** wifi.h:196

[wifi\_eap\_config::phase2](structwifi__eap__config.md#abeed60cdf6c01751a4bb3c7ab67ea4e6)

char \* phase2

Phase2 setting string.

**Definition** wifi.h:202

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi.h](wifi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
