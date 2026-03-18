---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/wifi_8h_source.html
original_path: doxygen/html/wifi_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

19

20#ifndef ZEPHYR\_INCLUDE\_NET\_WIFI\_H\_

21#define ZEPHYR\_INCLUDE\_NET\_WIFI\_H\_

22

23#include <[zephyr/sys/util.h](util_8h.md)> /\* for ARRAY\_SIZE \*/

24

[ 26](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)#define WIFI\_COUNTRY\_CODE\_LEN 2

27

29

30#define WIFI\_LISTEN\_INTERVAL\_MIN 0

31#define WIFI\_LISTEN\_INTERVAL\_MAX 65535

32

34

35#ifdef \_\_cplusplus

36extern "C" {

37#endif

38

[ 40](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c)enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) {

[ 42](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e) [WIFI\_SECURITY\_TYPE\_NONE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e) = 0,

[ 44](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368) [WIFI\_SECURITY\_TYPE\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368),

[ 46](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e) [WIFI\_SECURITY\_TYPE\_PSK\_SHA256](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e),

[ 48](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f) [WIFI\_SECURITY\_TYPE\_SAE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f),

[ 50](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d) [WIFI\_SECURITY\_TYPE\_WAPI](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d),

[ 52](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80) [WIFI\_SECURITY\_TYPE\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80),

[ 54](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724) [WIFI\_SECURITY\_TYPE\_WEP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724),

[ 56](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a) [WIFI\_SECURITY\_TYPE\_WPA\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a),

[ 58](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff) [WIFI\_SECURITY\_TYPE\_WPA\_AUTO\_PERSONAL](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff),

59

61 \_\_WIFI\_SECURITY\_TYPE\_AFTER\_LAST,

62 WIFI\_SECURITY\_TYPE\_MAX = \_\_WIFI\_SECURITY\_TYPE\_AFTER\_LAST - 1,

63 WIFI\_SECURITY\_TYPE\_UNKNOWN

65};

66

[ 68](group__wifi__mgmt.md#ga9bb9f658d7806e42b3ee351fb3e7dfa0)const char \*[wifi\_security\_txt](group__wifi__mgmt.md#ga9bb9f658d7806e42b3ee351fb3e7dfa0)(enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) security);

69

[ 71](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) {

[ 73](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969) [WIFI\_MFP\_DISABLE](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969) = 0,

[ 75](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf) [WIFI\_MFP\_OPTIONAL](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf),

[ 77](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840) [WIFI\_MFP\_REQUIRED](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840),

78

80 \_\_WIFI\_MFP\_AFTER\_LAST,

81 WIFI\_MFP\_MAX = \_\_WIFI\_MFP\_AFTER\_LAST - 1,

82 WIFI\_MFP\_UNKNOWN

84};

85

[ 87](group__wifi__mgmt.md#ga22354241197a9227fdba77e67d471f5c)const char \*[wifi\_mfp\_txt](group__wifi__mgmt.md#ga22354241197a9227fdba77e67d471f5c)(enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) mfp);

88

[ 92](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d)enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) {

[ 94](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11) [WIFI\_FREQ\_BAND\_2\_4\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11) = 0,

[ 96](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895) [WIFI\_FREQ\_BAND\_5\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895),

[ 98](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0) [WIFI\_FREQ\_BAND\_6\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0),

99

101 \_\_WIFI\_FREQ\_BAND\_AFTER\_LAST,

[ 103](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5) [WIFI\_FREQ\_BAND\_MAX](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5) = \_\_WIFI\_FREQ\_BAND\_AFTER\_LAST - 1,

[ 105](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5) [WIFI\_FREQ\_BAND\_UNKNOWN](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)

106};

107

[ 109](group__wifi__mgmt.md#ga44f875bf0d931b66d582f5dca2d65ed5)const char \*[wifi\_band\_txt](group__wifi__mgmt.md#ga44f875bf0d931b66d582f5dca2d65ed5)(enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) band);

110

[ 112](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)#define WIFI\_SSID\_MAX\_LEN 32

[ 114](group__wifi__mgmt.md#gaa8e19abf8c85f237ba5033740ceff553)#define WIFI\_PSK\_MIN\_LEN 8

[ 116](group__wifi__mgmt.md#gad7c3b99c974b342935180a28fdc5ddfc)#define WIFI\_PSK\_MAX\_LEN 64

[ 118](group__wifi__mgmt.md#gab63fa744cc2e049cfd635ab0a187971f)#define WIFI\_SAE\_PSWD\_MAX\_LEN 128

[ 120](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)#define WIFI\_MAC\_ADDR\_LEN 6

121

[ 123](group__wifi__mgmt.md#ga260e473dac1e823fd298a2c982470e0b)#define WIFI\_CHANNEL\_MIN 1

[ 125](group__wifi__mgmt.md#ga8ea9141108f93b419f6a6530bf67bd95)#define WIFI\_CHANNEL\_MAX 233

[ 127](group__wifi__mgmt.md#ga3876cd718af9f8a7b3682546da854544)#define WIFI\_CHANNEL\_ANY 255

128

[ 133](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4)enum [wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4) {

[ 135](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) [WIFI\_STATE\_DISCONNECTED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) = 0,

[ 137](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) [WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c),

[ 139](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) [WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598),

[ 141](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) [WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b),

[ 143](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) [WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba),

[ 145](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) [WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b),

[ 147](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) [WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc),

[ 149](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) [WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969),

[ 151](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) [WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e),

[ 153](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f) [WIFI\_STATE\_COMPLETED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f),

154

156 \_\_WIFI\_STATE\_AFTER\_LAST,

157 WIFI\_STATE\_MAX = \_\_WIFI\_STATE\_AFTER\_LAST - 1,

158 WIFI\_STATE\_UNKNOWN

160};

161

162/\* We rely on the strict order of the enum values, so, let's check it \*/

163BUILD\_ASSERT([WIFI\_STATE\_DISCONNECTED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) < [WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) &&

164 [WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) < [WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) &&

165 [WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) < [WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) &&

166 [WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) < [WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) &&

167 [WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) < [WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) &&

168 [WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) < [WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) &&

169 [WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) < [WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) &&

170 [WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) < [WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) &&

171 [WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) < [WIFI\_STATE\_COMPLETED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f));

172

173

[ 175](group__wifi__mgmt.md#ga03d306912dc96178e21d3c82c104582f)const char \*[wifi\_state\_txt](group__wifi__mgmt.md#ga03d306912dc96178e21d3c82c104582f)(enum [wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

176

[ 181](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) {

[ 183](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813) [WIFI\_MODE\_INFRA](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813) = 0,

[ 185](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b) [WIFI\_MODE\_IBSS](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b) = 1,

[ 187](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8) [WIFI\_MODE\_AP](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8) = 2,

[ 189](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889) [WIFI\_MODE\_P2P\_GO](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889) = 3,

[ 191](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521) [WIFI\_MODE\_P2P\_GROUP\_FORMATION](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521) = 4,

[ 193](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68) [WIFI\_MODE\_MESH](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68) = 5,

194

196 \_\_WIFI\_MODE\_AFTER\_LAST,

197 WIFI\_MODE\_MAX = \_\_WIFI\_MODE\_AFTER\_LAST - 1,

198 WIFI\_MODE\_UNKNOWN

200};

201

[ 203](group__wifi__mgmt.md#gad78536ce1f30accfa45f258b6bf8c73d)const char \*[wifi\_mode\_txt](group__wifi__mgmt.md#gad78536ce1f30accfa45f258b6bf8c73d)(enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) mode);

204

[ 209](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) {

[ 211](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8) [WIFI\_0](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8) = 0,

[ 213](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c) [WIFI\_1](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c),

[ 215](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9) [WIFI\_2](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9),

[ 217](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362) [WIFI\_3](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362),

[ 219](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2) [WIFI\_4](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2),

[ 221](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824) [WIFI\_5](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824),

[ 223](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe) [WIFI\_6](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe),

[ 225](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6) [WIFI\_6E](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6),

[ 227](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934) [WIFI\_7](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934),

228

230 \_\_WIFI\_LINK\_MODE\_AFTER\_LAST,

231 WIFI\_LINK\_MODE\_MAX = \_\_WIFI\_LINK\_MODE\_AFTER\_LAST - 1,

232 WIFI\_LINK\_MODE\_UNKNOWN

234};

235

[ 237](group__wifi__mgmt.md#ga0d9d6e2150fb187025300904357f7b4d)const char \*[wifi\_link\_mode\_txt](group__wifi__mgmt.md#ga0d9d6e2150fb187025300904357f7b4d)(enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) link\_mode);

238

[ 240](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)enum [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) {

[ 242](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9) [WIFI\_SCAN\_TYPE\_ACTIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9) = 0,

[ 244](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f) [WIFI\_SCAN\_TYPE\_PASSIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f),

245};

246

[ 248](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) {

[ 250](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82) [WIFI\_PS\_DISABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82) = 0,

[ 252](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47) [WIFI\_PS\_ENABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47),

253};

254

[ 256](group__wifi__mgmt.md#gafbeb5f7fa97fd2ba0c691da0f8853ef2)const char \*[wifi\_ps\_txt](group__wifi__mgmt.md#gafbeb5f7fa97fd2ba0c691da0f8853ef2)(enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) ps\_name);

257

[ 259](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c)enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) {

[ 261](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd) [WIFI\_PS\_MODE\_LEGACY](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd) = 0,

262 /\* This has to be configured before connecting to the AP,

263 \* as support for ADDTS action frames is not available.

264 \*/

[ 266](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5) [WIFI\_PS\_MODE\_WMM](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5),

267};

268

[ 270](group__wifi__mgmt.md#gadb21d49f64e04fba59433e51d5b3481c)const char \*[wifi\_ps\_mode\_txt](group__wifi__mgmt.md#gadb21d49f64e04fba59433e51d5b3481c)(enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) ps\_mode);

271

[ 273](group__wifi__mgmt.md#gaa1a74ef94af57a7ea966c691c065a46d)#define WIFI\_INTERFACE\_INDEX\_MIN 1

[ 275](group__wifi__mgmt.md#gaa6cbecd7d4197d453038d3da7ef6be7b)#define WIFI\_INTERFACE\_INDEX\_MAX 255

276

[ 278](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35)enum [wifi\_operational\_modes](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35) {

[ 280](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7) [WIFI\_STA\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 282](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696) [WIFI\_MONITOR\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 284](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74) [WIFI\_TX\_INJECTION\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 286](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56) [WIFI\_PROMISCUOUS\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 288](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd) [WIFI\_AP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 290](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623) [WIFI\_SOFTAP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

291};

292

[ 294](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f)enum [wifi\_filter](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f) {

[ 296](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b) [WIFI\_PACKET\_FILTER\_ALL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 298](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc) [WIFI\_PACKET\_FILTER\_MGMT](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 300](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244) [WIFI\_PACKET\_FILTER\_DATA](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 302](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de) [WIFI\_PACKET\_FILTER\_CTRL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

303};

304

[ 306](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) {

[ 308](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45) [WIFI\_TWT\_SETUP](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45) = 0,

[ 310](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f) [WIFI\_TWT\_TEARDOWN](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f),

311};

312

[ 314](group__wifi__mgmt.md#gadb125925e851bf7569424cd4295e7712)const char \*[wifi\_twt\_operation\_txt](group__wifi__mgmt.md#gadb125925e851bf7569424cd4295e7712)(enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) twt\_operation);

315

[ 317](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8)enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) {

[ 319](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0) [WIFI\_TWT\_INDIVIDUAL](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0) = 0,

[ 321](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa) [WIFI\_TWT\_BROADCAST](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa),

[ 323](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978) [WIFI\_TWT\_WAKE\_TBTT](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978)

324};

325

[ 327](group__wifi__mgmt.md#ga6a74e999d63ee491df68447219ef2a0d)const char \*[wifi\_twt\_negotiation\_type\_txt](group__wifi__mgmt.md#ga6a74e999d63ee491df68447219ef2a0d)(enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) twt\_negotiation);

328

[ 330](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) {

[ 332](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd) [WIFI\_TWT\_SETUP\_CMD\_REQUEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd) = 0,

[ 334](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648) [WIFI\_TWT\_SETUP\_CMD\_SUGGEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648),

[ 336](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e) [WIFI\_TWT\_SETUP\_CMD\_DEMAND](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e),

[ 338](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279) [WIFI\_TWT\_SETUP\_CMD\_GROUPING](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279),

[ 340](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a) [WIFI\_TWT\_SETUP\_CMD\_ACCEPT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a),

[ 342](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1) [WIFI\_TWT\_SETUP\_CMD\_ALTERNATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1),

[ 344](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3) [WIFI\_TWT\_SETUP\_CMD\_DICTATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3),

[ 346](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565) [WIFI\_TWT\_SETUP\_CMD\_REJECT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565),

347};

348

[ 350](group__wifi__mgmt.md#gae3ca047cc6ef6b6a2e44ba6574d41a44)const char \*[wifi\_twt\_setup\_cmd\_txt](group__wifi__mgmt.md#gae3ca047cc6ef6b6a2e44ba6574d41a44)(enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) twt\_setup);

351

[ 353](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) {

[ 355](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286) [WIFI\_TWT\_RESP\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286) = 0,

[ 357](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72) [WIFI\_TWT\_RESP\_NOT\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72),

358};

359

[ 361](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6)enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) {

[ 363](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13) [WIFI\_TWT\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13),

[ 365](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556) [WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556),

[ 367](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d) [WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d),

[ 369](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef) [WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef),

[ 371](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831) [WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831),

[ 373](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860) [WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860),

[ 375](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce) [WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce),

[ 377](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7) [WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7),

[ 379](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6) [WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6),

[ 381](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee) [WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee),

[ 383](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c) [WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c),

384};

385

[ 387](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) {

[ 389](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965) [WIFI\_TWT\_TEARDOWN\_SUCCESS](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965) = 0,

[ 391](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d) [WIFI\_TWT\_TEARDOWN\_FAILED](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d),

392};

393

395static const char \* const wifi\_twt\_err\_code\_tbl[] = {

396 [[WIFI\_TWT\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13)] = "Unspecified",

397 [[WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556)] = "Command Execution failed",

398 [[WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d)] =

399 "Operation not supported",

400 [[WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef)] =

401 "Unable to get iface status",

402 [[WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831)] =

403 "Device not connected",

404 [[WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860)] = "Peer not HE capable",

405 [[WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce)] = "Peer not TWT capable",

406 [[WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7)] =

407 "Operation already in progress",

408 [[WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6)] =

409 "Invalid negotiated flow id",

410 [[WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee)] =

411 "IP address not assigned",

412 [[WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)] =

413 "Flow already exists",

414};

416

[ 418](group__wifi__mgmt.md#gab2e6a6e1d8358a8f34d67bd632709b3d)static inline const char \*[wifi\_twt\_get\_err\_code\_str](group__wifi__mgmt.md#gab2e6a6e1d8358a8f34d67bd632709b3d)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) err\_no)

419{

420 if ((err\_no) < ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(wifi\_twt\_err\_code\_tbl)) {

421 return wifi\_twt\_err\_code\_tbl[err\_no];

422 }

423

424 return "<unknown>";

425}

426

[ 428](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)enum [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) {

[ 430](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d) [WIFI\_PS\_PARAM\_STATE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d),

[ 432](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90) [WIFI\_PS\_PARAM\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90),

[ 434](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8) [WIFI\_PS\_PARAM\_WAKEUP\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8),

[ 436](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab) [WIFI\_PS\_PARAM\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab),

[ 438](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29) [WIFI\_PS\_PARAM\_TIMEOUT](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29),

439};

440

[ 442](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) {

[ 444](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6) [WIFI\_PS\_WAKEUP\_MODE\_DTIM](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6) = 0,

[ 446](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30) [WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30),

447};

448

[ 450](group__wifi__mgmt.md#ga6fd645f891234136b3028574a0af9666)const char \*[wifi\_ps\_wakeup\_mode\_txt](group__wifi__mgmt.md#ga6fd645f891234136b3028574a0af9666)(enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) ps\_wakeup\_mode);

451

[ 453](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)enum [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) {

[ 455](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38) [WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38),

[ 457](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394) [WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394),

[ 459](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093) [WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093),

[ 461](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3) [WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3),

[ 463](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a) [WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a),

[ 465](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486) [WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486),

[ 467](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f) [WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f),

468};

469

471static const char \* const wifi\_ps\_param\_config\_err\_code\_tbl[] = {

472 [[WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38)] = "Unspecified",

473 [[WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394)] = "Command Execution failed",

474 [[WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093)] =

475 "Operation not supported",

476 [[WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3)] =

477 "Unable to get iface status",

478 [[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a)] =

479 "Cannot set parameters while device not connected",

480 [[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486)] =

481 "Cannot set parameters while device connected",

482 [[WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)] =

483 "Parameter out of range",

484};

486

[ 488](group__wifi__mgmt.md#ga8b72e7989964963a25f42ed1dba240a0)static inline const char \*[wifi\_ps\_get\_config\_err\_code\_str](group__wifi__mgmt.md#ga8b72e7989964963a25f42ed1dba240a0)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) err\_no)

489{

490 if ((err\_no) < ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf))[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(wifi\_ps\_param\_config\_err\_code\_tbl)) {

491 return wifi\_ps\_param\_config\_err\_code\_tbl[err\_no];

492 }

493

494 return "<unknown>";

495}

496

[ 498](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642)enum [wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642) {

[ 500](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c) [WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 502](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958) [WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

503};

504

505#ifdef \_\_cplusplus

506}

507#endif

508

512#endif /\* ZEPHYR\_INCLUDE\_NET\_WIFI\_H\_ \*/

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:127

[wifi\_state\_txt](group__wifi__mgmt.md#ga03d306912dc96178e21d3c82c104582f)

const char \* wifi\_state\_txt(enum wifi\_iface\_state state)

Helper function to get user-friendly interface state name.

[wifi\_link\_mode\_txt](group__wifi__mgmt.md#ga0d9d6e2150fb187025300904357f7b4d)

const char \* wifi\_link\_mode\_txt(enum wifi\_link\_mode link\_mode)

Helper function to get user-friendly link mode name.

[wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca)

wifi\_ps

Wi-Fi power save states.

**Definition** wifi.h:248

[wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d)

wifi\_frequency\_bands

IEEE 802.11 operational frequency bands (not exhaustive).

**Definition** wifi.h:92

[wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76)

wifi\_mfp\_options

IEEE 802.11w - Management frame protection.

**Definition** wifi.h:71

[wifi\_mfp\_txt](group__wifi__mgmt.md#ga22354241197a9227fdba77e67d471f5c)

const char \* wifi\_mfp\_txt(enum wifi\_mfp\_options mfp)

Helper function to get user-friendly MFP name.

[wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022)

wifi\_twt\_setup\_cmd

Wi-Fi Target Wake Time (TWT) setup commands.

**Definition** wifi.h:330

[wifi\_band\_txt](group__wifi__mgmt.md#ga44f875bf0d931b66d582f5dca2d65ed5)

const char \* wifi\_band\_txt(enum wifi\_frequency\_bands band)

Helper function to get user-friendly frequency band name.

[wifi\_operational\_modes](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35)

wifi\_operational\_modes

Wifi operational mode.

**Definition** wifi.h:278

[wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a)

wifi\_twt\_setup\_resp\_status

Wi-Fi Target Wake Time (TWT) negotiation status.

**Definition** wifi.h:353

[wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b)

wifi\_iface\_mode

Wi-Fi interface modes.

**Definition** wifi.h:181

[wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8)

wifi\_twt\_negotiation\_type

Wi-Fi Target Wake Time (TWT) negotiation types.

**Definition** wifi.h:317

[wifi\_twt\_negotiation\_type\_txt](group__wifi__mgmt.md#ga6a74e999d63ee491df68447219ef2a0d)

const char \* wifi\_twt\_negotiation\_type\_txt(enum wifi\_twt\_negotiation\_type twt\_negotiation)

Helper function to get user-friendly twt negotiation type name.

[wifi\_ps\_wakeup\_mode\_txt](group__wifi__mgmt.md#ga6fd645f891234136b3028574a0af9666)

const char \* wifi\_ps\_wakeup\_mode\_txt(enum wifi\_ps\_wakeup\_mode ps\_wakeup\_mode)

Helper function to get user-friendly ps wakeup mode name.

[wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642)

wifi\_ap\_config\_param

Wi-Fi AP mode configuration parameter.

**Definition** wifi.h:498

[wifi\_ps\_get\_config\_err\_code\_str](group__wifi__mgmt.md#ga8b72e7989964963a25f42ed1dba240a0)

static const char \* wifi\_ps\_get\_config\_err\_code\_str(int16\_t err\_no)

Helper function to get user-friendly power save error code name.

**Definition** wifi.h:488

[wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6)

wifi\_twt\_fail\_reason

Target Wake Time (TWT) error codes.

**Definition** wifi.h:361

[wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4)

wifi\_iface\_state

Wi-Fi interface states.

**Definition** wifi.h:133

[wifi\_security\_txt](group__wifi__mgmt.md#ga9bb9f658d7806e42b3ee351fb3e7dfa0)

const char \* wifi\_security\_txt(enum wifi\_security\_type security)

Helper function to get user-friendly security type name.

[wifi\_filter](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f)

wifi\_filter

Mode filter settings.

**Definition** wifi.h:294

[wifi\_twt\_get\_err\_code\_str](group__wifi__mgmt.md#gab2e6a6e1d8358a8f34d67bd632709b3d)

static const char \* wifi\_twt\_get\_err\_code\_str(int16\_t err\_no)

Helper function to get user-friendly TWT error code name.

**Definition** wifi.h:418

[wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62)

wifi\_link\_mode

Wi-Fi link operating modes.

**Definition** wifi.h:209

[wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912)

wifi\_ps\_param\_type

Wi-Fi power save parameters.

**Definition** wifi.h:428

[wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f)

wifi\_ps\_wakeup\_mode

Wi-Fi power save modes.

**Definition** wifi.h:442

[wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3)

wifi\_twt\_operation

Wi-Fi Target Wake Time (TWT) operations.

**Definition** wifi.h:306

[wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea)

wifi\_scan\_type

Wi-Fi scanning types.

**Definition** wifi.h:240

[wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989)

wifi\_twt\_teardown\_status

Wi-Fi Target Wake Time (TWT) teradown status.

**Definition** wifi.h:387

[wifi\_mode\_txt](group__wifi__mgmt.md#gad78536ce1f30accfa45f258b6bf8c73d)

const char \* wifi\_mode\_txt(enum wifi\_iface\_mode mode)

Helper function to get user-friendly interface mode name.

[wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0)

wifi\_config\_ps\_param\_fail\_reason

Wi-Fi power save error codes.

**Definition** wifi.h:453

[wifi\_twt\_operation\_txt](group__wifi__mgmt.md#gadb125925e851bf7569424cd4295e7712)

const char \* wifi\_twt\_operation\_txt(enum wifi\_twt\_operation twt\_operation)

Helper function to get user-friendly twt operation name.

[wifi\_ps\_mode\_txt](group__wifi__mgmt.md#gadb21d49f64e04fba59433e51d5b3481c)

const char \* wifi\_ps\_mode\_txt(enum wifi\_ps\_mode ps\_mode)

Helper function to get user-friendly ps mode name.

[wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c)

wifi\_security\_type

IEEE 802.11 security types.

**Definition** wifi.h:40

[wifi\_twt\_setup\_cmd\_txt](group__wifi__mgmt.md#gae3ca047cc6ef6b6a2e44ba6574d41a44)

const char \* wifi\_twt\_setup\_cmd\_txt(enum wifi\_twt\_setup\_cmd twt\_setup)

Helper function to get user-friendly twt setup cmd name.

[wifi\_ps\_txt](group__wifi__mgmt.md#gafbeb5f7fa97fd2ba0c691da0f8853ef2)

const char \* wifi\_ps\_txt(enum wifi\_ps ps\_name)

Helper function to get user-friendly ps name.

[wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c)

wifi\_ps\_mode

Wi-Fi power save modes.

**Definition** wifi.h:259

[WIFI\_PS\_ENABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47)

@ WIFI\_PS\_ENABLED

Power save enabled.

**Definition** wifi.h:252

[WIFI\_PS\_DISABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82)

@ WIFI\_PS\_DISABLED

Power save disabled.

**Definition** wifi.h:250

[WIFI\_FREQ\_BAND\_6\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0)

@ WIFI\_FREQ\_BAND\_6\_GHZ

6 GHz band (Wi-Fi 6E, also extends to 7GHz).

**Definition** wifi.h:98

[WIFI\_FREQ\_BAND\_2\_4\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11)

@ WIFI\_FREQ\_BAND\_2\_4\_GHZ

2.4 GHz band.

**Definition** wifi.h:94

[WIFI\_FREQ\_BAND\_UNKNOWN](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)

@ WIFI\_FREQ\_BAND\_UNKNOWN

Invalid frequency band.

**Definition** wifi.h:105

[WIFI\_FREQ\_BAND\_5\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895)

@ WIFI\_FREQ\_BAND\_5\_GHZ

5 GHz band.

**Definition** wifi.h:96

[WIFI\_FREQ\_BAND\_MAX](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5)

@ WIFI\_FREQ\_BAND\_MAX

Highest frequency band available.

**Definition** wifi.h:103

[WIFI\_MFP\_DISABLE](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969)

@ WIFI\_MFP\_DISABLE

MFP disabled.

**Definition** wifi.h:73

[WIFI\_MFP\_OPTIONAL](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf)

@ WIFI\_MFP\_OPTIONAL

MFP optional.

**Definition** wifi.h:75

[WIFI\_MFP\_REQUIRED](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840)

@ WIFI\_MFP\_REQUIRED

MFP required.

**Definition** wifi.h:77

[WIFI\_TWT\_SETUP\_CMD\_DEMAND](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e)

@ WIFI\_TWT\_SETUP\_CMD\_DEMAND

TWT setup demand (parameters can not be changed by AP).

**Definition** wifi.h:336

[WIFI\_TWT\_SETUP\_CMD\_REQUEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd)

@ WIFI\_TWT\_SETUP\_CMD\_REQUEST

TWT setup request.

**Definition** wifi.h:332

[WIFI\_TWT\_SETUP\_CMD\_ALTERNATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1)

@ WIFI\_TWT\_SETUP\_CMD\_ALTERNATE

TWT setup alternate (alternate parameters suggested by AP).

**Definition** wifi.h:342

[WIFI\_TWT\_SETUP\_CMD\_GROUPING](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279)

@ WIFI\_TWT\_SETUP\_CMD\_GROUPING

TWT setup grouping (grouping of TWT flows).

**Definition** wifi.h:338

[WIFI\_TWT\_SETUP\_CMD\_DICTATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3)

@ WIFI\_TWT\_SETUP\_CMD\_DICTATE

TWT setup dictate (parameters dictated by AP).

**Definition** wifi.h:344

[WIFI\_TWT\_SETUP\_CMD\_SUGGEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648)

@ WIFI\_TWT\_SETUP\_CMD\_SUGGEST

TWT setup suggest (parameters can be changed by AP).

**Definition** wifi.h:334

[WIFI\_TWT\_SETUP\_CMD\_REJECT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565)

@ WIFI\_TWT\_SETUP\_CMD\_REJECT

TWT setup reject (parameters rejected by AP).

**Definition** wifi.h:346

[WIFI\_TWT\_SETUP\_CMD\_ACCEPT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a)

@ WIFI\_TWT\_SETUP\_CMD\_ACCEPT

TWT setup accept (parameters accepted by AP).

**Definition** wifi.h:340

[WIFI\_TX\_INJECTION\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74)

@ WIFI\_TX\_INJECTION\_MODE

TX injection mode setting enable.

**Definition** wifi.h:284

[WIFI\_STA\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7)

@ WIFI\_STA\_MODE

STA mode setting enable.

**Definition** wifi.h:280

[WIFI\_AP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd)

@ WIFI\_AP\_MODE

AP mode setting enable.

**Definition** wifi.h:288

[WIFI\_SOFTAP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623)

@ WIFI\_SOFTAP\_MODE

Softap mode setting enable.

**Definition** wifi.h:290

[WIFI\_MONITOR\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696)

@ WIFI\_MONITOR\_MODE

Monitor mode setting enable.

**Definition** wifi.h:282

[WIFI\_PROMISCUOUS\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56)

@ WIFI\_PROMISCUOUS\_MODE

Promiscuous mode setting enable.

**Definition** wifi.h:286

[WIFI\_TWT\_RESP\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286)

@ WIFI\_TWT\_RESP\_RECEIVED

TWT response received for TWT request.

**Definition** wifi.h:355

[WIFI\_TWT\_RESP\_NOT\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72)

@ WIFI\_TWT\_RESP\_NOT\_RECEIVED

TWT response not received for TWT request.

**Definition** wifi.h:357

[WIFI\_MODE\_AP](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8)

@ WIFI\_MODE\_AP

AP mode.

**Definition** wifi.h:187

[WIFI\_MODE\_IBSS](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b)

@ WIFI\_MODE\_IBSS

IBSS (ad-hoc) station mode.

**Definition** wifi.h:185

[WIFI\_MODE\_P2P\_GO](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889)

@ WIFI\_MODE\_P2P\_GO

P2P group owner mode.

**Definition** wifi.h:189

[WIFI\_MODE\_P2P\_GROUP\_FORMATION](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521)

@ WIFI\_MODE\_P2P\_GROUP\_FORMATION

P2P group formation mode.

**Definition** wifi.h:191

[WIFI\_MODE\_INFRA](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813)

@ WIFI\_MODE\_INFRA

Infrastructure station mode.

**Definition** wifi.h:183

[WIFI\_MODE\_MESH](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68)

@ WIFI\_MODE\_MESH

802.11s Mesh mode.

**Definition** wifi.h:193

[WIFI\_TWT\_BROADCAST](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa)

@ WIFI\_TWT\_BROADCAST

TWT broadcast negotiation.

**Definition** wifi.h:321

[WIFI\_TWT\_WAKE\_TBTT](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978)

@ WIFI\_TWT\_WAKE\_TBTT

TWT wake TBTT negotiation.

**Definition** wifi.h:323

[WIFI\_TWT\_INDIVIDUAL](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0)

@ WIFI\_TWT\_INDIVIDUAL

TWT individual negotiation.

**Definition** wifi.h:319

[WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c)

@ WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY

Used for AP mode configuration parameter ap\_max\_inactivity.

**Definition** wifi.h:500

[WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA](group__wifi__mgmt.md#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958)

@ WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA

Used for AP mode configuration parameter max\_num\_sta.

**Definition** wifi.h:502

[WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee)

@ WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED

IP address not assigned or configured.

**Definition** wifi.h:381

[WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6)

@ WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID

Invalid negotiated flow id.

**Definition** wifi.h:379

[WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556)

@ WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL

Command execution failed.

**Definition** wifi.h:365

[WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d)

@ WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED

Operation not supported.

**Definition** wifi.h:367

[WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef)

@ WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS

Unable to get interface status.

**Definition** wifi.h:369

[WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860)

@ WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB

Peer not HE (802.11ax/Wi-Fi 6) capable.

**Definition** wifi.h:373

[WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831)

@ WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED

Device not connected to AP.

**Definition** wifi.h:371

[WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7)

@ WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS

A TWT flow is already in progress.

**Definition** wifi.h:377

[WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce)

@ WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB

Peer not TWT capable.

**Definition** wifi.h:375

[WIFI\_TWT\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13)

@ WIFI\_TWT\_FAIL\_UNSPECIFIED

Unspecified error.

**Definition** wifi.h:363

[WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)

@ WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS

Flow already exists.

**Definition** wifi.h:383

[WIFI\_STATE\_DISCONNECTED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f)

@ WIFI\_STATE\_DISCONNECTED

Interface is disconnected.

**Definition** wifi.h:135

[WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e)

@ WIFI\_STATE\_GROUP\_HANDSHAKE

Group Key exchange with a network is in progress.

**Definition** wifi.h:151

[WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c)

@ WIFI\_STATE\_INTERFACE\_DISABLED

Interface is disabled (administratively).

**Definition** wifi.h:137

[WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969)

@ WIFI\_STATE\_4WAY\_HANDSHAKE

4-way handshake with a network is in progress.

**Definition** wifi.h:149

[WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc)

@ WIFI\_STATE\_ASSOCIATED

Association with a network completed.

**Definition** wifi.h:147

[WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b)

@ WIFI\_STATE\_SCANNING

Interface is scanning for networks.

**Definition** wifi.h:141

[WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba)

@ WIFI\_STATE\_AUTHENTICATING

Authentication with a network is in progress.

**Definition** wifi.h:143

[WIFI\_STATE\_COMPLETED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f)

@ WIFI\_STATE\_COMPLETED

All authentication completed, ready to pass data.

**Definition** wifi.h:153

[WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b)

@ WIFI\_STATE\_ASSOCIATING

Association with a network is in progress.

**Definition** wifi.h:145

[WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598)

@ WIFI\_STATE\_INACTIVE

No enabled networks in the configuration.

**Definition** wifi.h:139

[WIFI\_PACKET\_FILTER\_MGMT](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc)

@ WIFI\_PACKET\_FILTER\_MGMT

Support only sniffing of management packets.

**Definition** wifi.h:298

[WIFI\_PACKET\_FILTER\_ALL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b)

@ WIFI\_PACKET\_FILTER\_ALL

Support management, data and control packet sniffing.

**Definition** wifi.h:296

[WIFI\_PACKET\_FILTER\_DATA](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244)

@ WIFI\_PACKET\_FILTER\_DATA

Support only sniffing of data packets.

**Definition** wifi.h:300

[WIFI\_PACKET\_FILTER\_CTRL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de)

@ WIFI\_PACKET\_FILTER\_CTRL

Support only sniffing of control packets.

**Definition** wifi.h:302

[WIFI\_6E](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6)

@ WIFI\_6E

802.11ax 6GHz.

**Definition** wifi.h:225

[WIFI\_5](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824)

@ WIFI\_5

802.11ac.

**Definition** wifi.h:221

[WIFI\_0](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8)

@ WIFI\_0

802.11 (legacy).

**Definition** wifi.h:211

[WIFI\_7](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934)

@ WIFI\_7

802.11be.

**Definition** wifi.h:227

[WIFI\_4](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2)

@ WIFI\_4

802.11n.

**Definition** wifi.h:219

[WIFI\_2](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9)

@ WIFI\_2

802.11a.

**Definition** wifi.h:215

[WIFI\_6](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe)

@ WIFI\_6

802.11ax.

**Definition** wifi.h:223

[WIFI\_1](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c)

@ WIFI\_1

802.11b.

**Definition** wifi.h:213

[WIFI\_3](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362)

@ WIFI\_3

802.11g.

**Definition** wifi.h:217

[WIFI\_PS\_PARAM\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90)

@ WIFI\_PS\_PARAM\_LISTEN\_INTERVAL

Power save listen interval.

**Definition** wifi.h:432

[WIFI\_PS\_PARAM\_STATE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d)

@ WIFI\_PS\_PARAM\_STATE

Power save state.

**Definition** wifi.h:430

[WIFI\_PS\_PARAM\_WAKEUP\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8)

@ WIFI\_PS\_PARAM\_WAKEUP\_MODE

Power save wakeup mode.

**Definition** wifi.h:434

[WIFI\_PS\_PARAM\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab)

@ WIFI\_PS\_PARAM\_MODE

Power save mode.

**Definition** wifi.h:436

[WIFI\_PS\_PARAM\_TIMEOUT](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29)

@ WIFI\_PS\_PARAM\_TIMEOUT

Power save timeout.

**Definition** wifi.h:438

[WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30)

@ WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL

Listen interval based wakeup.

**Definition** wifi.h:446

[WIFI\_PS\_WAKEUP\_MODE\_DTIM](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6)

@ WIFI\_PS\_WAKEUP\_MODE\_DTIM

DTIM based wakeup.

**Definition** wifi.h:444

[WIFI\_TWT\_SETUP](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45)

@ WIFI\_TWT\_SETUP

TWT setup operation.

**Definition** wifi.h:308

[WIFI\_TWT\_TEARDOWN](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f)

@ WIFI\_TWT\_TEARDOWN

TWT teardown operation.

**Definition** wifi.h:310

[WIFI\_SCAN\_TYPE\_ACTIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9)

@ WIFI\_SCAN\_TYPE\_ACTIVE

Active scanning (default).

**Definition** wifi.h:242

[WIFI\_SCAN\_TYPE\_PASSIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f)

@ WIFI\_SCAN\_TYPE\_PASSIVE

Passive scanning.

**Definition** wifi.h:244

[WIFI\_TWT\_TEARDOWN\_SUCCESS](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965)

@ WIFI\_TWT\_TEARDOWN\_SUCCESS

TWT teardown success.

**Definition** wifi.h:389

[WIFI\_TWT\_TEARDOWN\_FAILED](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d)

@ WIFI\_TWT\_TEARDOWN\_FAILED

TWT teardown failure.

**Definition** wifi.h:391

[WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3)

@ WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS

Unable to get interface status.

**Definition** wifi.h:461

[WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38)

@ WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED

Unspecified error.

**Definition** wifi.h:455

[WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394)

@ WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL

Command execution failed.

**Definition** wifi.h:457

[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a)

@ WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED

Device not connected to AP.

**Definition** wifi.h:463

[WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)

@ WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID

Listen interval out of range.

**Definition** wifi.h:467

[WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093)

@ WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED

Parameter not supported.

**Definition** wifi.h:459

[WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486)

@ WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED

Device already connected to AP.

**Definition** wifi.h:465

[WIFI\_SECURITY\_TYPE\_SAE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f)

@ WIFI\_SECURITY\_TYPE\_SAE

WPA3-SAE security.

**Definition** wifi.h:48

[WIFI\_SECURITY\_TYPE\_PSK\_SHA256](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e)

@ WIFI\_SECURITY\_TYPE\_PSK\_SHA256

WPA2-PSK-SHA256 security.

**Definition** wifi.h:46

[WIFI\_SECURITY\_TYPE\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368)

@ WIFI\_SECURITY\_TYPE\_PSK

WPA2-PSK security.

**Definition** wifi.h:44

[WIFI\_SECURITY\_TYPE\_WPA\_AUTO\_PERSONAL](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff)

@ WIFI\_SECURITY\_TYPE\_WPA\_AUTO\_PERSONAL

WPA/WPA2/WPA3 PSK security.

**Definition** wifi.h:58

[WIFI\_SECURITY\_TYPE\_WAPI](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d)

@ WIFI\_SECURITY\_TYPE\_WAPI

GB 15629.11-2003 WAPI security.

**Definition** wifi.h:50

[WIFI\_SECURITY\_TYPE\_WEP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724)

@ WIFI\_SECURITY\_TYPE\_WEP

WEP security.

**Definition** wifi.h:54

[WIFI\_SECURITY\_TYPE\_NONE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e)

@ WIFI\_SECURITY\_TYPE\_NONE

No security.

**Definition** wifi.h:42

[WIFI\_SECURITY\_TYPE\_WPA\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a)

@ WIFI\_SECURITY\_TYPE\_WPA\_PSK

WPA-PSK security.

**Definition** wifi.h:56

[WIFI\_SECURITY\_TYPE\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80)

@ WIFI\_SECURITY\_TYPE\_EAP

EAP security - Enterprise.

**Definition** wifi.h:52

[WIFI\_PS\_MODE\_WMM](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5)

@ WIFI\_PS\_MODE\_WMM

WMM power save mode.

**Definition** wifi.h:266

[WIFI\_PS\_MODE\_LEGACY](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd)

@ WIFI\_PS\_MODE\_LEGACY

Legacy power save mode.

**Definition** wifi.h:261

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi.h](wifi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
