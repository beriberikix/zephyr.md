---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/wifi_8h_source.html
original_path: doxygen/html/wifi_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

[ 80](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca64ddf5be1aabce875fc66e39ff63be9b) [WIFI\_SECURITY\_TYPE\_EAP\_TLS\_SHA256](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca64ddf5be1aabce875fc66e39ff63be9b),

[ 82](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5) [WIFI\_SECURITY\_TYPE\_FT\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5),

[ 84](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092) [WIFI\_SECURITY\_TYPE\_FT\_SAE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092),

[ 86](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5) [WIFI\_SECURITY\_TYPE\_FT\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5),

[ 88](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93) [WIFI\_SECURITY\_TYPE\_FT\_EAP\_SHA384](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93),

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

[ 114](group__wifi__mgmt.md#ga168e7affe48d72d7d1e3ccddb63fe5a7)enum [wifi\_suiteb\_type](group__wifi__mgmt.md#ga168e7affe48d72d7d1e3ccddb63fe5a7) {

[ 116](group__wifi__mgmt.md#gga168e7affe48d72d7d1e3ccddb63fe5a7aa8e819a5bbe3bb65e98c69709c086d89) [WIFI\_SUITEB](group__wifi__mgmt.md#gga168e7affe48d72d7d1e3ccddb63fe5a7aa8e819a5bbe3bb65e98c69709c086d89) = 1,

[ 118](group__wifi__mgmt.md#gga168e7affe48d72d7d1e3ccddb63fe5a7a6fdf84ffa5fcca7371bf2da06be6c30d) [WIFI\_SUITEB\_192](group__wifi__mgmt.md#gga168e7affe48d72d7d1e3ccddb63fe5a7a6fdf84ffa5fcca7371bf2da06be6c30d),

119};

120

[ 122](group__wifi__mgmt.md#ga7f7b23ac019ca504a2006f0376735645)enum [wifi\_cipher\_type](group__wifi__mgmt.md#ga7f7b23ac019ca504a2006f0376735645) {

[ 124](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1) [WPA\_CAPA\_ENC\_CCMP](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1),

[ 126](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d) [WPA\_CAPA\_ENC\_GCMP](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d),

[ 128](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4) [WPA\_CAPA\_ENC\_GCMP\_256](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4),

129};

130

[ 132](group__wifi__mgmt.md#gaf84d5e1a68393483fc6063c06b8f26e0)enum [wifi\_group\_mgmt\_cipher\_type](group__wifi__mgmt.md#gaf84d5e1a68393483fc6063c06b8f26e0) {

[ 136](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8) [WPA\_CAPA\_ENC\_BIP](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8),

[ 140](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70) [WPA\_CAPA\_ENC\_BIP\_GMAC\_128](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70),

[ 144](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096) [WPA\_CAPA\_ENC\_BIP\_GMAC\_256](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096),

145};

146

[ 147](structwifi__cipher__desc.md)struct [wifi\_cipher\_desc](structwifi__cipher__desc.md) {

[ 149](structwifi__cipher__desc.md#a6751019bb6da3032ca2f7bc42a3469e3) unsigned int [capa](structwifi__cipher__desc.md#a6751019bb6da3032ca2f7bc42a3469e3);

[ 151](structwifi__cipher__desc.md#a9396239f38613b151232a4c5f3d66a8f) char \*[name](structwifi__cipher__desc.md#a9396239f38613b151232a4c5f3d66a8f);

152};

153

[ 154](structwifi__eap__cipher__config.md)struct [wifi\_eap\_cipher\_config](structwifi__eap__cipher__config.md) {

[ 156](structwifi__eap__cipher__config.md#a385d365bb70a70fa09d321c55988afcc) char \*[key\_mgmt](structwifi__eap__cipher__config.md#a385d365bb70a70fa09d321c55988afcc);

[ 158](structwifi__eap__cipher__config.md#a14128465917447f38d3854444a9bf6e1) char \*[openssl\_ciphers](structwifi__eap__cipher__config.md#a14128465917447f38d3854444a9bf6e1);

[ 160](structwifi__eap__cipher__config.md#aa505ae934897742078aa46f1fdb5d0d1) char \*[group\_cipher](structwifi__eap__cipher__config.md#aa505ae934897742078aa46f1fdb5d0d1);

[ 162](structwifi__eap__cipher__config.md#a3917f94dfafb22df260db9c4a129c3c4) char \*[pairwise\_cipher](structwifi__eap__cipher__config.md#a3917f94dfafb22df260db9c4a129c3c4);

[ 164](structwifi__eap__cipher__config.md#ab53f5b5419b2b8c8a869ba4f9d645a41) char \*[group\_mgmt\_cipher](structwifi__eap__cipher__config.md#ab53f5b5419b2b8c8a869ba4f9d645a41);

[ 166](structwifi__eap__cipher__config.md#ae9a4b8a0f0b47ac1065562ce287473a5) char \*[tls\_flags](structwifi__eap__cipher__config.md#ae9a4b8a0f0b47ac1065562ce287473a5);

167};

168

[ 169](structwifi__eap__config.md)struct [wifi\_eap\_config](structwifi__eap__config.md) {

[ 171](structwifi__eap__config.md#a0fc099524e283bb3ab1491b625d30d83) unsigned int [type](structwifi__eap__config.md#a0fc099524e283bb3ab1491b625d30d83);

[ 173](structwifi__eap__config.md#ab44893426c89416ab24e3bfb57bf49ad) enum [wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331) [eap\_type\_phase1](structwifi__eap__config.md#ab44893426c89416ab24e3bfb57bf49ad);

[ 175](structwifi__eap__config.md#aaf73f2f986d56f95d196d02dcecbaff1) enum [wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331) [eap\_type\_phase2](structwifi__eap__config.md#aaf73f2f986d56f95d196d02dcecbaff1);

[ 177](structwifi__eap__config.md#aa7a42a1256ef26562e83f47498d87113) char \*[method](structwifi__eap__config.md#aa7a42a1256ef26562e83f47498d87113);

[ 179](structwifi__eap__config.md#abeed60cdf6c01751a4bb3c7ab67ea4e6) char \*[phase2](structwifi__eap__config.md#abeed60cdf6c01751a4bb3c7ab67ea4e6);

180};

181

[ 183](group__wifi__mgmt.md#ga9bb9f658d7806e42b3ee351fb3e7dfa0)const char \*[wifi\_security\_txt](group__wifi__mgmt.md#ga9bb9f658d7806e42b3ee351fb3e7dfa0)(enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) security);

184

[ 186](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) {

[ 188](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969) [WIFI\_MFP\_DISABLE](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969) = 0,

[ 190](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf) [WIFI\_MFP\_OPTIONAL](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf),

[ 192](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840) [WIFI\_MFP\_REQUIRED](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840),

193

195 \_\_WIFI\_MFP\_AFTER\_LAST,

196 WIFI\_MFP\_MAX = \_\_WIFI\_MFP\_AFTER\_LAST - 1,

197 WIFI\_MFP\_UNKNOWN

199};

200

[ 202](group__wifi__mgmt.md#ga22354241197a9227fdba77e67d471f5c)const char \*[wifi\_mfp\_txt](group__wifi__mgmt.md#ga22354241197a9227fdba77e67d471f5c)(enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) mfp);

203

[ 207](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d)enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) {

[ 209](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11) [WIFI\_FREQ\_BAND\_2\_4\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11) = 0,

[ 211](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895) [WIFI\_FREQ\_BAND\_5\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895),

[ 213](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0) [WIFI\_FREQ\_BAND\_6\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0),

214

216 \_\_WIFI\_FREQ\_BAND\_AFTER\_LAST,

[ 218](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5) [WIFI\_FREQ\_BAND\_MAX](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5) = \_\_WIFI\_FREQ\_BAND\_AFTER\_LAST - 1,

[ 220](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5) [WIFI\_FREQ\_BAND\_UNKNOWN](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)

221};

222

[ 224](group__wifi__mgmt.md#ga44f875bf0d931b66d582f5dca2d65ed5)const char \*[wifi\_band\_txt](group__wifi__mgmt.md#ga44f875bf0d931b66d582f5dca2d65ed5)(enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) band);

225

[ 227](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)#define WIFI\_SSID\_MAX\_LEN 32

[ 229](group__wifi__mgmt.md#gaa8e19abf8c85f237ba5033740ceff553)#define WIFI\_PSK\_MIN\_LEN 8

[ 231](group__wifi__mgmt.md#gad7c3b99c974b342935180a28fdc5ddfc)#define WIFI\_PSK\_MAX\_LEN 64

[ 233](group__wifi__mgmt.md#gab63fa744cc2e049cfd635ab0a187971f)#define WIFI\_SAE\_PSWD\_MAX\_LEN 128

[ 235](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)#define WIFI\_MAC\_ADDR\_LEN 6

[ 237](group__wifi__mgmt.md#gac6904487661f157274b0b60833f6684a)#define WIFI\_ENT\_IDENTITY\_MAX\_LEN 64

[ 239](group__wifi__mgmt.md#gae2fd55924f4078187431f7a1184f217f)#define WIFI\_ENT\_PSWD\_MAX\_LEN 128

240

[ 242](group__wifi__mgmt.md#ga260e473dac1e823fd298a2c982470e0b)#define WIFI\_CHANNEL\_MIN 1

[ 244](group__wifi__mgmt.md#ga8ea9141108f93b419f6a6530bf67bd95)#define WIFI\_CHANNEL\_MAX 233

[ 246](group__wifi__mgmt.md#ga3876cd718af9f8a7b3682546da854544)#define WIFI\_CHANNEL\_ANY 255

247

[ 252](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4)enum [wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4) {

[ 254](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) [WIFI\_STATE\_DISCONNECTED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) = 0,

[ 256](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) [WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c),

[ 258](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) [WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598),

[ 260](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) [WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b),

[ 262](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) [WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba),

[ 264](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) [WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b),

[ 266](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) [WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc),

[ 268](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) [WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969),

[ 270](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) [WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e),

[ 272](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f) [WIFI\_STATE\_COMPLETED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f),

273

275 \_\_WIFI\_STATE\_AFTER\_LAST,

276 WIFI\_STATE\_MAX = \_\_WIFI\_STATE\_AFTER\_LAST - 1,

277 WIFI\_STATE\_UNKNOWN

279};

280

281/\* We rely on the strict order of the enum values, so, let's check it \*/

282BUILD\_ASSERT([WIFI\_STATE\_DISCONNECTED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) < [WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) &&

283 [WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) < [WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) &&

284 [WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) < [WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) &&

285 [WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) < [WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) &&

286 [WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) < [WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) &&

287 [WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) < [WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) &&

288 [WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) < [WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) &&

289 [WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) < [WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) &&

290 [WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) < [WIFI\_STATE\_COMPLETED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f));

291

292

[ 294](group__wifi__mgmt.md#ga03d306912dc96178e21d3c82c104582f)const char \*[wifi\_state\_txt](group__wifi__mgmt.md#ga03d306912dc96178e21d3c82c104582f)(enum [wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

295

[ 300](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) {

[ 302](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813) [WIFI\_MODE\_INFRA](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813) = 0,

[ 304](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b) [WIFI\_MODE\_IBSS](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b) = 1,

[ 306](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8) [WIFI\_MODE\_AP](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8) = 2,

[ 308](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889) [WIFI\_MODE\_P2P\_GO](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889) = 3,

[ 310](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521) [WIFI\_MODE\_P2P\_GROUP\_FORMATION](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521) = 4,

[ 312](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68) [WIFI\_MODE\_MESH](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68) = 5,

313

315 \_\_WIFI\_MODE\_AFTER\_LAST,

316 WIFI\_MODE\_MAX = \_\_WIFI\_MODE\_AFTER\_LAST - 1,

317 WIFI\_MODE\_UNKNOWN

319};

320

[ 322](group__wifi__mgmt.md#gad78536ce1f30accfa45f258b6bf8c73d)const char \*[wifi\_mode\_txt](group__wifi__mgmt.md#gad78536ce1f30accfa45f258b6bf8c73d)(enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) mode);

323

[ 328](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) {

[ 330](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8) [WIFI\_0](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8) = 0,

[ 332](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c) [WIFI\_1](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c),

[ 334](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9) [WIFI\_2](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9),

[ 336](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362) [WIFI\_3](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362),

[ 338](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2) [WIFI\_4](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2),

[ 340](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824) [WIFI\_5](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824),

[ 342](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe) [WIFI\_6](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe),

[ 344](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6) [WIFI\_6E](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6),

[ 346](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934) [WIFI\_7](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934),

347

349 \_\_WIFI\_LINK\_MODE\_AFTER\_LAST,

350 WIFI\_LINK\_MODE\_MAX = \_\_WIFI\_LINK\_MODE\_AFTER\_LAST - 1,

351 WIFI\_LINK\_MODE\_UNKNOWN

353};

354

[ 356](group__wifi__mgmt.md#ga0d9d6e2150fb187025300904357f7b4d)const char \*[wifi\_link\_mode\_txt](group__wifi__mgmt.md#ga0d9d6e2150fb187025300904357f7b4d)(enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) link\_mode);

357

[ 359](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) {

[ 361](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9) [WIFI\_SCAN\_TYPE\_ACTIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9) = 0,

[ 363](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f) [WIFI\_SCAN\_TYPE\_PASSIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f),

364};

365

[ 367](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) {

[ 369](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82) [WIFI\_PS\_DISABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82) = 0,

[ 371](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47) [WIFI\_PS\_ENABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47),

372};

373

[ 375](group__wifi__mgmt.md#gafbeb5f7fa97fd2ba0c691da0f8853ef2)const char \*[wifi\_ps\_txt](group__wifi__mgmt.md#gafbeb5f7fa97fd2ba0c691da0f8853ef2)(enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) ps\_name);

376

[ 378](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c)enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) {

[ 380](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd) [WIFI\_PS\_MODE\_LEGACY](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd) = 0,

381 /\* This has to be configured before connecting to the AP,

382 \* as support for ADDTS action frames is not available.

383 \*/

[ 385](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5) [WIFI\_PS\_MODE\_WMM](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5),

386};

387

[ 389](group__wifi__mgmt.md#gadb21d49f64e04fba59433e51d5b3481c)const char \*[wifi\_ps\_mode\_txt](group__wifi__mgmt.md#gadb21d49f64e04fba59433e51d5b3481c)(enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) ps\_mode);

390

[ 392](group__wifi__mgmt.md#gaa1a74ef94af57a7ea966c691c065a46d)#define WIFI\_INTERFACE\_INDEX\_MIN 1

[ 394](group__wifi__mgmt.md#gaa6cbecd7d4197d453038d3da7ef6be7b)#define WIFI\_INTERFACE\_INDEX\_MAX 255

395

[ 397](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35)enum [wifi\_operational\_modes](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35) {

[ 399](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7) [WIFI\_STA\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 401](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696) [WIFI\_MONITOR\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 403](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74) [WIFI\_TX\_INJECTION\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 405](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56) [WIFI\_PROMISCUOUS\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 407](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd) [WIFI\_AP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 409](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623) [WIFI\_SOFTAP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

410};

411

[ 413](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f)enum [wifi\_filter](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f) {

[ 415](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b) [WIFI\_PACKET\_FILTER\_ALL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 417](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc) [WIFI\_PACKET\_FILTER\_MGMT](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 419](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244) [WIFI\_PACKET\_FILTER\_DATA](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 421](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de) [WIFI\_PACKET\_FILTER\_CTRL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

422};

423

[ 425](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) {

[ 427](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45) [WIFI\_TWT\_SETUP](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45) = 0,

[ 429](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f) [WIFI\_TWT\_TEARDOWN](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f),

430};

431

[ 433](group__wifi__mgmt.md#gadb125925e851bf7569424cd4295e7712)const char \*[wifi\_twt\_operation\_txt](group__wifi__mgmt.md#gadb125925e851bf7569424cd4295e7712)(enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) twt\_operation);

434

[ 436](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8)enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) {

[ 438](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0) [WIFI\_TWT\_INDIVIDUAL](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0) = 0,

[ 440](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa) [WIFI\_TWT\_BROADCAST](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa),

[ 442](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978) [WIFI\_TWT\_WAKE\_TBTT](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978)

443};

444

[ 446](group__wifi__mgmt.md#ga6a74e999d63ee491df68447219ef2a0d)const char \*[wifi\_twt\_negotiation\_type\_txt](group__wifi__mgmt.md#ga6a74e999d63ee491df68447219ef2a0d)(enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) twt\_negotiation);

447

[ 449](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) {

[ 451](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd) [WIFI\_TWT\_SETUP\_CMD\_REQUEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd) = 0,

[ 453](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648) [WIFI\_TWT\_SETUP\_CMD\_SUGGEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648),

[ 455](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e) [WIFI\_TWT\_SETUP\_CMD\_DEMAND](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e),

[ 457](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279) [WIFI\_TWT\_SETUP\_CMD\_GROUPING](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279),

[ 459](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a) [WIFI\_TWT\_SETUP\_CMD\_ACCEPT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a),

[ 461](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1) [WIFI\_TWT\_SETUP\_CMD\_ALTERNATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1),

[ 463](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3) [WIFI\_TWT\_SETUP\_CMD\_DICTATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3),

[ 465](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565) [WIFI\_TWT\_SETUP\_CMD\_REJECT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565),

466};

467

[ 469](group__wifi__mgmt.md#gae3ca047cc6ef6b6a2e44ba6574d41a44)const char \*[wifi\_twt\_setup\_cmd\_txt](group__wifi__mgmt.md#gae3ca047cc6ef6b6a2e44ba6574d41a44)(enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) twt\_setup);

470

[ 472](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) {

[ 474](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286) [WIFI\_TWT\_RESP\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286) = 0,

[ 476](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72) [WIFI\_TWT\_RESP\_NOT\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72),

477};

478

[ 480](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6)enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) {

[ 482](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13) [WIFI\_TWT\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13),

[ 484](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556) [WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556),

[ 486](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d) [WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d),

[ 488](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef) [WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef),

[ 490](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831) [WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831),

[ 492](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860) [WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860),

[ 494](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce) [WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce),

[ 496](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7) [WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7),

[ 498](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6) [WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6),

[ 500](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee) [WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee),

[ 502](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c) [WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c),

503};

504

[ 506](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) {

[ 508](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965) [WIFI\_TWT\_TEARDOWN\_SUCCESS](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965) = 0,

[ 510](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d) [WIFI\_TWT\_TEARDOWN\_FAILED](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d),

511};

512

514static const char \* const wifi\_twt\_err\_code\_tbl[] = {

515 [[WIFI\_TWT\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13)] = "Unspecified",

516 [[WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556)] = "Command Execution failed",

517 [[WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d)] =

518 "Operation not supported",

519 [[WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef)] =

520 "Unable to get iface status",

521 [[WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831)] =

522 "Device not connected",

523 [[WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860)] = "Peer not HE capable",

524 [[WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce)] = "Peer not TWT capable",

525 [[WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7)] =

526 "Operation already in progress",

527 [[WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6)] =

528 "Invalid negotiated flow id",

529 [[WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee)] =

530 "IP address not assigned",

531 [[WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)] =

532 "Flow already exists",

533};

535

[ 537](group__wifi__mgmt.md#gab2e6a6e1d8358a8f34d67bd632709b3d)static inline const char \*[wifi\_twt\_get\_err\_code\_str](group__wifi__mgmt.md#gab2e6a6e1d8358a8f34d67bd632709b3d)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) err\_no)

538{

539 if ((err\_no) < ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(wifi\_twt\_err\_code\_tbl)) {

540 return wifi\_twt\_err\_code\_tbl[err\_no];

541 }

542

543 return "<unknown>";

544}

545

[ 547](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)enum [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) {

[ 549](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d) [WIFI\_PS\_PARAM\_STATE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d),

[ 551](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90) [WIFI\_PS\_PARAM\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90),

[ 553](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8) [WIFI\_PS\_PARAM\_WAKEUP\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8),

[ 555](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab) [WIFI\_PS\_PARAM\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab),

[ 557](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03) [WIFI\_PS\_PARAM\_EXIT\_STRATEGY](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03),

[ 559](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29) [WIFI\_PS\_PARAM\_TIMEOUT](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29),

560};

561

[ 563](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) {

[ 565](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6) [WIFI\_PS\_WAKEUP\_MODE\_DTIM](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6) = 0,

[ 567](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30) [WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30),

568};

569

[ 571](group__wifi__mgmt.md#ga6fd645f891234136b3028574a0af9666)const char \*[wifi\_ps\_wakeup\_mode\_txt](group__wifi__mgmt.md#ga6fd645f891234136b3028574a0af9666)(enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) ps\_wakeup\_mode);

572

[ 576](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7)enum [wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7) {

[ 578](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5) [WIFI\_PS\_EXIT\_CUSTOM\_ALGO](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5) = 0,

[ 580](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832) [WIFI\_PS\_EXIT\_EVERY\_TIM](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832),

581

583 WIFI\_PS\_EXIT\_LAST,

584 WIFI\_PS\_EXIT\_MAX = WIFI\_PS\_EXIT\_LAST - 1,

586};

587

[ 589](group__wifi__mgmt.md#gade667a55793caef820b570a248052327)const char \* const [wifi\_ps\_exit\_strategy\_txt](group__wifi__mgmt.md#gade667a55793caef820b570a248052327)(enum [wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7) ps\_exit\_strategy);

590

[ 592](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)enum [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) {

[ 594](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38) [WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38),

[ 596](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394) [WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394),

[ 598](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093) [WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093),

[ 600](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3) [WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3),

[ 602](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a) [WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a),

[ 604](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486) [WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486),

[ 606](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f) [WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f),

[ 608](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce) [WIFI\_PS\_PARAM\_FAIL\_INVALID\_EXIT\_STRATEGY](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce),

609};

610

612static const char \* const wifi\_ps\_param\_config\_err\_code\_tbl[] = {

613 [[WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38)] = "Unspecified",

614 [[WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394)] = "Command Execution failed",

615 [[WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093)] =

616 "Operation not supported",

617 [[WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3)] =

618 "Unable to get iface status",

619 [[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a)] =

620 "Cannot set parameters while device not connected",

621 [[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486)] =

622 "Cannot set parameters while device connected",

623 [[WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)] =

624 "Parameter out of range",

625};

627

628#ifdef CONFIG\_WIFI\_NM\_WPA\_SUPPLICANT\_WNM

632enum wifi\_btm\_query\_reason {

634 WIFI\_BTM\_QUERY\_REASON\_UNSPECIFIED = 0,

636 WIFI\_BTM\_QUERY\_REASON\_LOW\_RSSI = 16,

638 WIFI\_BTM\_QUERY\_REASON\_LEAVING\_ESS = 20,

639};

640#endif

641

[ 643](group__wifi__mgmt.md#ga8b72e7989964963a25f42ed1dba240a0)static inline const char \*[wifi\_ps\_get\_config\_err\_code\_str](group__wifi__mgmt.md#ga8b72e7989964963a25f42ed1dba240a0)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) err\_no)

644{

645 if ((err\_no) < ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(wifi\_ps\_param\_config\_err\_code\_tbl)) {

646 return wifi\_ps\_param\_config\_err\_code\_tbl[err\_no];

647 }

648

649 return "<unknown>";

650}

651

[ 653](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642)enum [wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642) {

[ 655](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c) [WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 657](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958) [WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

658};

659

660#ifdef \_\_cplusplus

661}

662#endif

663

667#endif /\* ZEPHYR\_INCLUDE\_NET\_WIFI\_H\_ \*/

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:120

[wifi\_state\_txt](group__wifi__mgmt.md#ga03d306912dc96178e21d3c82c104582f)

const char \* wifi\_state\_txt(enum wifi\_iface\_state state)

Helper function to get user-friendly interface state name.

[wifi\_link\_mode\_txt](group__wifi__mgmt.md#ga0d9d6e2150fb187025300904357f7b4d)

const char \* wifi\_link\_mode\_txt(enum wifi\_link\_mode link\_mode)

Helper function to get user-friendly link mode name.

[wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)

wifi\_ps

Wi-Fi power save states.

**Definition** wifi.h:367

[wifi\_suiteb\_type](group__wifi__mgmt.md#ga168e7affe48d72d7d1e3ccddb63fe5a7)

wifi\_suiteb\_type

Enterprise security WPA3 suiteb types.

**Definition** wifi.h:114

[wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d)

wifi\_frequency\_bands

IEEE 802.11 operational frequency bands (not exhaustive).

**Definition** wifi.h:207

[wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)

wifi\_mfp\_options

IEEE 802.11w - Management frame protection.

**Definition** wifi.h:186

[wifi\_mfp\_txt](group__wifi__mgmt.md#ga22354241197a9227fdba77e67d471f5c)

const char \* wifi\_mfp\_txt(enum wifi\_mfp\_options mfp)

Helper function to get user-friendly MFP name.

[wifi\_ps\_exit\_strategy](group__wifi__mgmt.md#ga2d424d1711389fb784e916a87ff854b7)

wifi\_ps\_exit\_strategy

Wi-Fi power save exit strategy.

**Definition** wifi.h:576

[wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)

wifi\_twt\_setup\_cmd

Wi-Fi Target Wake Time (TWT) setup commands.

**Definition** wifi.h:449

[wifi\_band\_txt](group__wifi__mgmt.md#ga44f875bf0d931b66d582f5dca2d65ed5)

const char \* wifi\_band\_txt(enum wifi\_frequency\_bands band)

Helper function to get user-friendly frequency band name.

[wifi\_operational\_modes](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35)

wifi\_operational\_modes

Wifi operational mode.

**Definition** wifi.h:397

[wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)

wifi\_twt\_setup\_resp\_status

Wi-Fi Target Wake Time (TWT) negotiation status.

**Definition** wifi.h:472

[wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)

wifi\_iface\_mode

Wi-Fi interface modes.

**Definition** wifi.h:300

[wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8)

wifi\_twt\_negotiation\_type

Wi-Fi Target Wake Time (TWT) negotiation types.

**Definition** wifi.h:436

[wifi\_twt\_negotiation\_type\_txt](group__wifi__mgmt.md#ga6a74e999d63ee491df68447219ef2a0d)

const char \* wifi\_twt\_negotiation\_type\_txt(enum wifi\_twt\_negotiation\_type twt\_negotiation)

Helper function to get user-friendly twt negotiation type name.

[wifi\_ps\_wakeup\_mode\_txt](group__wifi__mgmt.md#ga6fd645f891234136b3028574a0af9666)

const char \* wifi\_ps\_wakeup\_mode\_txt(enum wifi\_ps\_wakeup\_mode ps\_wakeup\_mode)

Helper function to get user-friendly ps wakeup mode name.

[wifi\_cipher\_type](group__wifi__mgmt.md#ga7f7b23ac019ca504a2006f0376735645)

wifi\_cipher\_type

Group cipher and pairwise cipher types.

**Definition** wifi.h:122

[wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642)

wifi\_ap\_config\_param

Wi-Fi AP mode configuration parameter.

**Definition** wifi.h:653

[wifi\_ps\_get\_config\_err\_code\_str](group__wifi__mgmt.md#ga8b72e7989964963a25f42ed1dba240a0)

static const char \* wifi\_ps\_get\_config\_err\_code\_str(int16\_t err\_no)

Helper function to get user-friendly power save error code name.

**Definition** wifi.h:643

[wifi\_eap\_type](group__wifi__mgmt.md#ga92b6fa6755491c3bd61f895213d07331)

wifi\_eap\_type

EPA method Types.

**Definition** wifi.h:98

[wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6)

wifi\_twt\_fail\_reason

Target Wake Time (TWT) error codes.

**Definition** wifi.h:480

[wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4)

wifi\_iface\_state

Wi-Fi interface states.

**Definition** wifi.h:252

[wifi\_security\_txt](group__wifi__mgmt.md#ga9bb9f658d7806e42b3ee351fb3e7dfa0)

const char \* wifi\_security\_txt(enum wifi\_security\_type security)

Helper function to get user-friendly security type name.

[wifi\_filter](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f)

wifi\_filter

Mode filter settings.

**Definition** wifi.h:413

[wifi\_twt\_get\_err\_code\_str](group__wifi__mgmt.md#gab2e6a6e1d8358a8f34d67bd632709b3d)

static const char \* wifi\_twt\_get\_err\_code\_str(int16\_t err\_no)

Helper function to get user-friendly TWT error code name.

**Definition** wifi.h:537

[wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)

wifi\_link\_mode

Wi-Fi link operating modes.

**Definition** wifi.h:328

[wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)

wifi\_ps\_param\_type

Wi-Fi power save parameters.

**Definition** wifi.h:547

[wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)

wifi\_ps\_wakeup\_mode

Wi-Fi power save modes.

**Definition** wifi.h:563

[wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)

wifi\_twt\_operation

Wi-Fi Target Wake Time (TWT) operations.

**Definition** wifi.h:425

[wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)

wifi\_scan\_type

Wi-Fi scanning types.

**Definition** wifi.h:359

[wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)

wifi\_twt\_teardown\_status

Wi-Fi Target Wake Time (TWT) teradown status.

**Definition** wifi.h:506

[wifi\_mode\_txt](group__wifi__mgmt.md#gad78536ce1f30accfa45f258b6bf8c73d)

const char \* wifi\_mode\_txt(enum wifi\_iface\_mode mode)

Helper function to get user-friendly interface mode name.

[wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)

wifi\_config\_ps\_param\_fail\_reason

Wi-Fi power save error codes.

**Definition** wifi.h:592

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

[wifi\_ps\_exit\_strategy\_txt](group__wifi__mgmt.md#gade667a55793caef820b570a248052327)

const char \*const wifi\_ps\_exit\_strategy\_txt(enum wifi\_ps\_exit\_strategy ps\_exit\_strategy)

Helper function to get user-friendly ps exit strategy name.

[wifi\_twt\_setup\_cmd\_txt](group__wifi__mgmt.md#gae3ca047cc6ef6b6a2e44ba6574d41a44)

const char \* wifi\_twt\_setup\_cmd\_txt(enum wifi\_twt\_setup\_cmd twt\_setup)

Helper function to get user-friendly twt setup cmd name.

[wifi\_group\_mgmt\_cipher\_type](group__wifi__mgmt.md#gaf84d5e1a68393483fc6063c06b8f26e0)

wifi\_group\_mgmt\_cipher\_type

group mgmt cipher types.

**Definition** wifi.h:132

[wifi\_ps\_txt](group__wifi__mgmt.md#gafbeb5f7fa97fd2ba0c691da0f8853ef2)

const char \* wifi\_ps\_txt(enum wifi\_ps ps\_name)

Helper function to get user-friendly ps name.

[wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c)

wifi\_ps\_mode

Wi-Fi power save modes.

**Definition** wifi.h:378

[WIFI\_PS\_ENABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47)

@ WIFI\_PS\_ENABLED

Power save enabled.

**Definition** wifi.h:371

[WIFI\_PS\_DISABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82)

@ WIFI\_PS\_DISABLED

Power save disabled.

**Definition** wifi.h:369

[WIFI\_SUITEB\_192](group__wifi__mgmt.md#gga168e7affe48d72d7d1e3ccddb63fe5a7a6fdf84ffa5fcca7371bf2da06be6c30d)

@ WIFI\_SUITEB\_192

suiteb-192.

**Definition** wifi.h:118

[WIFI\_SUITEB](group__wifi__mgmt.md#gga168e7affe48d72d7d1e3ccddb63fe5a7aa8e819a5bbe3bb65e98c69709c086d89)

@ WIFI\_SUITEB

suiteb.

**Definition** wifi.h:116

[WIFI\_FREQ\_BAND\_6\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0)

@ WIFI\_FREQ\_BAND\_6\_GHZ

6 GHz band (Wi-Fi 6E, also extends to 7GHz).

**Definition** wifi.h:213

[WIFI\_FREQ\_BAND\_2\_4\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11)

@ WIFI\_FREQ\_BAND\_2\_4\_GHZ

2.4 GHz band.

**Definition** wifi.h:209

[WIFI\_FREQ\_BAND\_UNKNOWN](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)

@ WIFI\_FREQ\_BAND\_UNKNOWN

Invalid frequency band.

**Definition** wifi.h:220

[WIFI\_FREQ\_BAND\_5\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895)

@ WIFI\_FREQ\_BAND\_5\_GHZ

5 GHz band.

**Definition** wifi.h:211

[WIFI\_FREQ\_BAND\_MAX](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5)

@ WIFI\_FREQ\_BAND\_MAX

Highest frequency band available.

**Definition** wifi.h:218

[WIFI\_MFP\_DISABLE](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969)

@ WIFI\_MFP\_DISABLE

MFP disabled.

**Definition** wifi.h:188

[WIFI\_MFP\_OPTIONAL](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf)

@ WIFI\_MFP\_OPTIONAL

MFP optional.

**Definition** wifi.h:190

[WIFI\_MFP\_REQUIRED](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840)

@ WIFI\_MFP\_REQUIRED

MFP required.

**Definition** wifi.h:192

[WIFI\_PS\_EXIT\_EVERY\_TIM](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832)

@ WIFI\_PS\_EXIT\_EVERY\_TIM

QoS NULL frame based.

**Definition** wifi.h:580

[WIFI\_PS\_EXIT\_CUSTOM\_ALGO](group__wifi__mgmt.md#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5)

@ WIFI\_PS\_EXIT\_CUSTOM\_ALGO

PS-Poll frame based.

**Definition** wifi.h:578

[WIFI\_TWT\_SETUP\_CMD\_DEMAND](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e)

@ WIFI\_TWT\_SETUP\_CMD\_DEMAND

TWT setup demand (parameters can not be changed by AP).

**Definition** wifi.h:455

[WIFI\_TWT\_SETUP\_CMD\_REQUEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd)

@ WIFI\_TWT\_SETUP\_CMD\_REQUEST

TWT setup request.

**Definition** wifi.h:451

[WIFI\_TWT\_SETUP\_CMD\_ALTERNATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1)

@ WIFI\_TWT\_SETUP\_CMD\_ALTERNATE

TWT setup alternate (alternate parameters suggested by AP).

**Definition** wifi.h:461

[WIFI\_TWT\_SETUP\_CMD\_GROUPING](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279)

@ WIFI\_TWT\_SETUP\_CMD\_GROUPING

TWT setup grouping (grouping of TWT flows).

**Definition** wifi.h:457

[WIFI\_TWT\_SETUP\_CMD\_DICTATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3)

@ WIFI\_TWT\_SETUP\_CMD\_DICTATE

TWT setup dictate (parameters dictated by AP).

**Definition** wifi.h:463

[WIFI\_TWT\_SETUP\_CMD\_SUGGEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648)

@ WIFI\_TWT\_SETUP\_CMD\_SUGGEST

TWT setup suggest (parameters can be changed by AP).

**Definition** wifi.h:453

[WIFI\_TWT\_SETUP\_CMD\_REJECT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565)

@ WIFI\_TWT\_SETUP\_CMD\_REJECT

TWT setup reject (parameters rejected by AP).

**Definition** wifi.h:465

[WIFI\_TWT\_SETUP\_CMD\_ACCEPT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a)

@ WIFI\_TWT\_SETUP\_CMD\_ACCEPT

TWT setup accept (parameters accepted by AP).

**Definition** wifi.h:459

[WIFI\_TX\_INJECTION\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74)

@ WIFI\_TX\_INJECTION\_MODE

TX injection mode setting enable.

**Definition** wifi.h:403

[WIFI\_STA\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7)

@ WIFI\_STA\_MODE

STA mode setting enable.

**Definition** wifi.h:399

[WIFI\_AP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd)

@ WIFI\_AP\_MODE

AP mode setting enable.

**Definition** wifi.h:407

[WIFI\_SOFTAP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623)

@ WIFI\_SOFTAP\_MODE

Softap mode setting enable.

**Definition** wifi.h:409

[WIFI\_MONITOR\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696)

@ WIFI\_MONITOR\_MODE

Monitor mode setting enable.

**Definition** wifi.h:401

[WIFI\_PROMISCUOUS\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56)

@ WIFI\_PROMISCUOUS\_MODE

Promiscuous mode setting enable.

**Definition** wifi.h:405

[WIFI\_TWT\_RESP\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286)

@ WIFI\_TWT\_RESP\_RECEIVED

TWT response received for TWT request.

**Definition** wifi.h:474

[WIFI\_TWT\_RESP\_NOT\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72)

@ WIFI\_TWT\_RESP\_NOT\_RECEIVED

TWT response not received for TWT request.

**Definition** wifi.h:476

[WIFI\_MODE\_AP](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8)

@ WIFI\_MODE\_AP

AP mode.

**Definition** wifi.h:306

[WIFI\_MODE\_IBSS](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b)

@ WIFI\_MODE\_IBSS

IBSS (ad-hoc) station mode.

**Definition** wifi.h:304

[WIFI\_MODE\_P2P\_GO](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889)

@ WIFI\_MODE\_P2P\_GO

P2P group owner mode.

**Definition** wifi.h:308

[WIFI\_MODE\_P2P\_GROUP\_FORMATION](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521)

@ WIFI\_MODE\_P2P\_GROUP\_FORMATION

P2P group formation mode.

**Definition** wifi.h:310

[WIFI\_MODE\_INFRA](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813)

@ WIFI\_MODE\_INFRA

Infrastructure station mode.

**Definition** wifi.h:302

[WIFI\_MODE\_MESH](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68)

@ WIFI\_MODE\_MESH

802.11s Mesh mode.

**Definition** wifi.h:312

[WIFI\_TWT\_BROADCAST](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa)

@ WIFI\_TWT\_BROADCAST

TWT broadcast negotiation.

**Definition** wifi.h:440

[WIFI\_TWT\_WAKE\_TBTT](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978)

@ WIFI\_TWT\_WAKE\_TBTT

TWT wake TBTT negotiation.

**Definition** wifi.h:442

[WIFI\_TWT\_INDIVIDUAL](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0)

@ WIFI\_TWT\_INDIVIDUAL

TWT individual negotiation.

**Definition** wifi.h:438

[WPA\_CAPA\_ENC\_GCMP\_256](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4)

@ WPA\_CAPA\_ENC\_GCMP\_256

256-bit Galois/Counter Mode Protocol.

**Definition** wifi.h:128

[WPA\_CAPA\_ENC\_GCMP](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d)

@ WPA\_CAPA\_ENC\_GCMP

128-bit Galois/Counter Mode Protocol.

**Definition** wifi.h:126

[WPA\_CAPA\_ENC\_CCMP](group__wifi__mgmt.md#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1)

@ WPA\_CAPA\_ENC\_CCMP

AES in counter mode with CBC-MAC (CCMP-128).

**Definition** wifi.h:124

[WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c)

@ WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY

Used for AP mode configuration parameter ap\_max\_inactivity.

**Definition** wifi.h:655

[WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958)

@ WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA

Used for AP mode configuration parameter max\_num\_sta.

**Definition** wifi.h:657

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

**Definition** wifi.h:500

[WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6)

@ WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID

Invalid negotiated flow id.

**Definition** wifi.h:498

[WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556)

@ WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL

Command execution failed.

**Definition** wifi.h:484

[WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d)

@ WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED

Operation not supported.

**Definition** wifi.h:486

[WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef)

@ WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS

Unable to get interface status.

**Definition** wifi.h:488

[WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860)

@ WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB

Peer not HE (802.11ax/Wi-Fi 6) capable.

**Definition** wifi.h:492

[WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831)

@ WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED

Device not connected to AP.

**Definition** wifi.h:490

[WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7)

@ WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS

A TWT flow is already in progress.

**Definition** wifi.h:496

[WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce)

@ WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB

Peer not TWT capable.

**Definition** wifi.h:494

[WIFI\_TWT\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13)

@ WIFI\_TWT\_FAIL\_UNSPECIFIED

Unspecified error.

**Definition** wifi.h:482

[WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)

@ WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS

Flow already exists.

**Definition** wifi.h:502

[WIFI\_STATE\_DISCONNECTED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f)

@ WIFI\_STATE\_DISCONNECTED

Interface is disconnected.

**Definition** wifi.h:254

[WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e)

@ WIFI\_STATE\_GROUP\_HANDSHAKE

Group Key exchange with a network is in progress.

**Definition** wifi.h:270

[WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c)

@ WIFI\_STATE\_INTERFACE\_DISABLED

Interface is disabled (administratively).

**Definition** wifi.h:256

[WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969)

@ WIFI\_STATE\_4WAY\_HANDSHAKE

4-way handshake with a network is in progress.

**Definition** wifi.h:268

[WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc)

@ WIFI\_STATE\_ASSOCIATED

Association with a network completed.

**Definition** wifi.h:266

[WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b)

@ WIFI\_STATE\_SCANNING

Interface is scanning for networks.

**Definition** wifi.h:260

[WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba)

@ WIFI\_STATE\_AUTHENTICATING

Authentication with a network is in progress.

**Definition** wifi.h:262

[WIFI\_STATE\_COMPLETED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f)

@ WIFI\_STATE\_COMPLETED

All authentication completed, ready to pass data.

**Definition** wifi.h:272

[WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b)

@ WIFI\_STATE\_ASSOCIATING

Association with a network is in progress.

**Definition** wifi.h:264

[WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598)

@ WIFI\_STATE\_INACTIVE

No enabled networks in the configuration.

**Definition** wifi.h:258

[WIFI\_PACKET\_FILTER\_MGMT](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc)

@ WIFI\_PACKET\_FILTER\_MGMT

Support only sniffing of management packets.

**Definition** wifi.h:417

[WIFI\_PACKET\_FILTER\_ALL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b)

@ WIFI\_PACKET\_FILTER\_ALL

Support management, data and control packet sniffing.

**Definition** wifi.h:415

[WIFI\_PACKET\_FILTER\_DATA](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244)

@ WIFI\_PACKET\_FILTER\_DATA

Support only sniffing of data packets.

**Definition** wifi.h:419

[WIFI\_PACKET\_FILTER\_CTRL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de)

@ WIFI\_PACKET\_FILTER\_CTRL

Support only sniffing of control packets.

**Definition** wifi.h:421

[WIFI\_6E](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6)

@ WIFI\_6E

802.11ax 6GHz.

**Definition** wifi.h:344

[WIFI\_5](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824)

@ WIFI\_5

802.11ac.

**Definition** wifi.h:340

[WIFI\_0](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8)

@ WIFI\_0

802.11 (legacy).

**Definition** wifi.h:330

[WIFI\_7](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934)

@ WIFI\_7

802.11be.

**Definition** wifi.h:346

[WIFI\_4](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2)

@ WIFI\_4

802.11n.

**Definition** wifi.h:338

[WIFI\_2](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9)

@ WIFI\_2

802.11a.

**Definition** wifi.h:334

[WIFI\_6](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe)

@ WIFI\_6

802.11ax.

**Definition** wifi.h:342

[WIFI\_1](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c)

@ WIFI\_1

802.11b.

**Definition** wifi.h:332

[WIFI\_3](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362)

@ WIFI\_3

802.11g.

**Definition** wifi.h:336

[WIFI\_PS\_PARAM\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90)

@ WIFI\_PS\_PARAM\_LISTEN\_INTERVAL

Power save listen interval.

**Definition** wifi.h:551

[WIFI\_PS\_PARAM\_STATE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d)

@ WIFI\_PS\_PARAM\_STATE

Power save state.

**Definition** wifi.h:549

[WIFI\_PS\_PARAM\_EXIT\_STRATEGY](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03)

@ WIFI\_PS\_PARAM\_EXIT\_STRATEGY

Power save exit strategy.

**Definition** wifi.h:557

[WIFI\_PS\_PARAM\_WAKEUP\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8)

@ WIFI\_PS\_PARAM\_WAKEUP\_MODE

Power save wakeup mode.

**Definition** wifi.h:553

[WIFI\_PS\_PARAM\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab)

@ WIFI\_PS\_PARAM\_MODE

Power save mode.

**Definition** wifi.h:555

[WIFI\_PS\_PARAM\_TIMEOUT](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29)

@ WIFI\_PS\_PARAM\_TIMEOUT

Power save timeout.

**Definition** wifi.h:559

[WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30)

@ WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL

Listen interval based wakeup.

**Definition** wifi.h:567

[WIFI\_PS\_WAKEUP\_MODE\_DTIM](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6)

@ WIFI\_PS\_WAKEUP\_MODE\_DTIM

DTIM based wakeup.

**Definition** wifi.h:565

[WIFI\_TWT\_SETUP](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45)

@ WIFI\_TWT\_SETUP

TWT setup operation.

**Definition** wifi.h:427

[WIFI\_TWT\_TEARDOWN](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f)

@ WIFI\_TWT\_TEARDOWN

TWT teardown operation.

**Definition** wifi.h:429

[WIFI\_SCAN\_TYPE\_ACTIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9)

@ WIFI\_SCAN\_TYPE\_ACTIVE

Active scanning (default).

**Definition** wifi.h:361

[WIFI\_SCAN\_TYPE\_PASSIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f)

@ WIFI\_SCAN\_TYPE\_PASSIVE

Passive scanning.

**Definition** wifi.h:363

[WIFI\_TWT\_TEARDOWN\_SUCCESS](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965)

@ WIFI\_TWT\_TEARDOWN\_SUCCESS

TWT teardown success.

**Definition** wifi.h:508

[WIFI\_TWT\_TEARDOWN\_FAILED](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d)

@ WIFI\_TWT\_TEARDOWN\_FAILED

TWT teardown failure.

**Definition** wifi.h:510

[WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3)

@ WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS

Unable to get interface status.

**Definition** wifi.h:600

[WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38)

@ WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED

Unspecified error.

**Definition** wifi.h:594

[WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394)

@ WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL

Command execution failed.

**Definition** wifi.h:596

[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a)

@ WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED

Device not connected to AP.

**Definition** wifi.h:602

[WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)

@ WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID

Listen interval out of range.

**Definition** wifi.h:606

[WIFI\_PS\_PARAM\_FAIL\_INVALID\_EXIT\_STRATEGY](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce)

@ WIFI\_PS\_PARAM\_FAIL\_INVALID\_EXIT\_STRATEGY

Invalid exit strategy.

**Definition** wifi.h:608

[WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093)

@ WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED

Parameter not supported.

**Definition** wifi.h:598

[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486)

@ WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED

Device already connected to AP.

**Definition** wifi.h:604

[WIFI\_SECURITY\_TYPE\_SAE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f)

@ WIFI\_SECURITY\_TYPE\_SAE

WPA3-SAE security.

**Definition** wifi.h:50

[WIFI\_SECURITY\_TYPE\_FT\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5)

@ WIFI\_SECURITY\_TYPE\_FT\_EAP

FT-EAP security.

**Definition** wifi.h:86

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

**Definition** wifi.h:82

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

**Definition** wifi.h:88

[WIFI\_SECURITY\_TYPE\_EAP\_TLS\_SHA256](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca64ddf5be1aabce875fc66e39ff63be9b)

@ WIFI\_SECURITY\_TYPE\_EAP\_TLS\_SHA256

EAP TLS SHA256 security - Enterprise.

**Definition** wifi.h:80

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

**Definition** wifi.h:84

[WIFI\_SECURITY\_TYPE\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80)

@ WIFI\_SECURITY\_TYPE\_EAP

EAP security - Enterprise.

**Definition** wifi.h:60

[WPA\_CAPA\_ENC\_BIP](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8)

@ WPA\_CAPA\_ENC\_BIP

128-bit Broadcast/Multicast Integrity Protocol Cipher-based Message Authentication Code .

**Definition** wifi.h:136

[WPA\_CAPA\_ENC\_BIP\_GMAC\_128](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70)

@ WPA\_CAPA\_ENC\_BIP\_GMAC\_128

128-bit Broadcast/Multicast Integrity Protocol Galois Message Authentication Code .

**Definition** wifi.h:140

[WPA\_CAPA\_ENC\_BIP\_GMAC\_256](group__wifi__mgmt.md#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096)

@ WPA\_CAPA\_ENC\_BIP\_GMAC\_256

256-bit Broadcast/Multicast Integrity Protocol Galois Message Authentication Code .

**Definition** wifi.h:144

[WIFI\_PS\_MODE\_WMM](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5)

@ WIFI\_PS\_MODE\_WMM

WMM power save mode.

**Definition** wifi.h:385

[WIFI\_PS\_MODE\_LEGACY](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd)

@ WIFI\_PS\_MODE\_LEGACY

Legacy power save mode.

**Definition** wifi.h:380

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[wifi\_cipher\_desc](structwifi__cipher__desc.md)

**Definition** wifi.h:147

[wifi\_cipher\_desc::capa](structwifi__cipher__desc.md#a6751019bb6da3032ca2f7bc42a3469e3)

unsigned int capa

Cipher capability.

**Definition** wifi.h:149

[wifi\_cipher\_desc::name](structwifi__cipher__desc.md#a9396239f38613b151232a4c5f3d66a8f)

char \* name

Cipher name string.

**Definition** wifi.h:151

[wifi\_eap\_cipher\_config](structwifi__eap__cipher__config.md)

**Definition** wifi.h:154

[wifi\_eap\_cipher\_config::openssl\_ciphers](structwifi__eap__cipher__config.md#a14128465917447f38d3854444a9bf6e1)

char \* openssl\_ciphers

OpenSSL cipher string.

**Definition** wifi.h:158

[wifi\_eap\_cipher\_config::key\_mgmt](structwifi__eap__cipher__config.md#a385d365bb70a70fa09d321c55988afcc)

char \* key\_mgmt

Key management type string.

**Definition** wifi.h:156

[wifi\_eap\_cipher\_config::pairwise\_cipher](structwifi__eap__cipher__config.md#a3917f94dfafb22df260db9c4a129c3c4)

char \* pairwise\_cipher

Pairwise\_cipher cipher string.

**Definition** wifi.h:162

[wifi\_eap\_cipher\_config::group\_cipher](structwifi__eap__cipher__config.md#aa505ae934897742078aa46f1fdb5d0d1)

char \* group\_cipher

Group cipher cipher string.

**Definition** wifi.h:160

[wifi\_eap\_cipher\_config::group\_mgmt\_cipher](structwifi__eap__cipher__config.md#ab53f5b5419b2b8c8a869ba4f9d645a41)

char \* group\_mgmt\_cipher

Group management cipher string.

**Definition** wifi.h:164

[wifi\_eap\_cipher\_config::tls\_flags](structwifi__eap__cipher__config.md#ae9a4b8a0f0b47ac1065562ce287473a5)

char \* tls\_flags

Used to confiure TLS features.

**Definition** wifi.h:166

[wifi\_eap\_config](structwifi__eap__config.md)

**Definition** wifi.h:169

[wifi\_eap\_config::type](structwifi__eap__config.md#a0fc099524e283bb3ab1491b625d30d83)

unsigned int type

Security type.

**Definition** wifi.h:171

[wifi\_eap\_config::method](structwifi__eap__config.md#aa7a42a1256ef26562e83f47498d87113)

char \* method

EPA method string.

**Definition** wifi.h:177

[wifi\_eap\_config::eap\_type\_phase2](structwifi__eap__config.md#aaf73f2f986d56f95d196d02dcecbaff1)

enum wifi\_eap\_type eap\_type\_phase2

EPA method type of phase2.

**Definition** wifi.h:175

[wifi\_eap\_config::eap\_type\_phase1](structwifi__eap__config.md#ab44893426c89416ab24e3bfb57bf49ad)

enum wifi\_eap\_type eap\_type\_phase1

EPA method type of phase1.

**Definition** wifi.h:173

[wifi\_eap\_config::phase2](structwifi__eap__config.md#abeed60cdf6c01751a4bb3c7ab67ea4e6)

char \* phase2

Phase2 setting string.

**Definition** wifi.h:179

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi.h](wifi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
