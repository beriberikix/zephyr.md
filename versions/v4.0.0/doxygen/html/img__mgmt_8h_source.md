---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/img__mgmt_8h_source.html
original_path: doxygen/html/img__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt.h

[Go to the documentation of this file.](img__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2018-2021 mcumgr authors

3 \* Copyright (c) 2022-2024 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef H\_IMG\_MGMT\_

9#define H\_IMG\_MGMT\_

10

11#include <[inttypes.h](inttypes_8h.md)>

12#include <[zephyr/mgmt/mcumgr/mgmt/mgmt.h](mgmt_8h.md)>

13#include <[zephyr/mgmt/mcumgr/smp/smp.h](mgmt_2mcumgr_2smp_2smp_8h.md)>

14#include <bootutil/image.h>

15#include <zcbor\_common.h>

16

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

[ 28](group__mcumgr__img__mgmt.md#ga70168b0d707c15658fd09b02c361a64c)#define IMG\_MGMT\_DATA\_SHA\_LEN 32 /\* SHA256 \*/

29

[ 33](group__mcumgr__img__mgmt.md#ga459776db5ce7bbfebae5e74aef4067ef)#define IMG\_MGMT\_STATE\_F\_PENDING 0x01

[ 34](group__mcumgr__img__mgmt.md#ga581c2626a47ca249ecbcc42edb7a59c2)#define IMG\_MGMT\_STATE\_F\_CONFIRMED 0x02

[ 35](group__mcumgr__img__mgmt.md#ga2a11cfad9698b0460b846fa079234c03)#define IMG\_MGMT\_STATE\_F\_ACTIVE 0x04

[ 36](group__mcumgr__img__mgmt.md#gae47e88131d96901e70b2b67ea43ceb4a)#define IMG\_MGMT\_STATE\_F\_PERMANENT 0x08

37

38/\* 255.255.65535.4294967295\0 \*/

[ 39](group__mcumgr__img__mgmt.md#ga57a5c429be5a3860981007e9728db181)#define IMG\_MGMT\_VER\_MAX\_STR\_LEN (sizeof("255.255.65535.4294967295"))

40

[ 44](group__mcumgr__img__mgmt.md#ga55e68ef4a5caa3c68987af438ebe8236)#define IMG\_MGMT\_SWAP\_TYPE\_NONE 0

[ 45](group__mcumgr__img__mgmt.md#ga71a0715be72de416f3d4744f4763a241)#define IMG\_MGMT\_SWAP\_TYPE\_TEST 1

[ 46](group__mcumgr__img__mgmt.md#ga69c51ca39c8d33db392e2353873aac43)#define IMG\_MGMT\_SWAP\_TYPE\_PERM 2

[ 47](group__mcumgr__img__mgmt.md#ga43a9afd49822eda7b640d3adb9219f10)#define IMG\_MGMT\_SWAP\_TYPE\_REVERT 3

[ 48](group__mcumgr__img__mgmt.md#ga35a8dd8ca661f2a602bc04d4ae6361a6)#define IMG\_MGMT\_SWAP\_TYPE\_UNKNOWN 255

49

[ 53](group__mcumgr__img__mgmt.md#ga19396c2690a0d40f625792ab644e7d17)#define IMG\_MGMT\_ID\_STATE 0

[ 54](group__mcumgr__img__mgmt.md#ga70541d06c76224a631f493023e05a73a)#define IMG\_MGMT\_ID\_UPLOAD 1

[ 55](group__mcumgr__img__mgmt.md#ga90225baf3e08859f294d9aaaf2012e6b)#define IMG\_MGMT\_ID\_FILE 2

[ 56](group__mcumgr__img__mgmt.md#ga46e9a83aab777da2591d4c7cb701b5cd)#define IMG\_MGMT\_ID\_CORELIST 3

[ 57](group__mcumgr__img__mgmt.md#ga22af869af6cbdde12f2cbc811fe7d443)#define IMG\_MGMT\_ID\_CORELOAD 4

[ 58](group__mcumgr__img__mgmt.md#gaf7de4c1d77bc29eea4b3d46382bd954f)#define IMG\_MGMT\_ID\_ERASE 5

[ 59](group__mcumgr__img__mgmt.md#gacb33e3b0729f8621275c6b3dc9795d57)#define IMG\_MGMT\_ID\_SLOT\_INFO 6

60

[ 64](group__mcumgr__img__mgmt.md#ga669286d96816e0e99792f407752c81a5)enum [img\_mgmt\_err\_code\_t](group__mcumgr__img__mgmt.md#ga669286d96816e0e99792f407752c81a5) {

[ 66](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0) [IMG\_MGMT\_ERR\_OK](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0) = 0,

67

[ 69](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe) [IMG\_MGMT\_ERR\_UNKNOWN](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe),

70

[ 72](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063) [IMG\_MGMT\_ERR\_FLASH\_CONFIG\_QUERY\_FAIL](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063),

73

[ 75](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6) [IMG\_MGMT\_ERR\_NO\_IMAGE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6),

76

[ 78](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10) [IMG\_MGMT\_ERR\_NO\_TLVS](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10),

79

[ 81](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb) [IMG\_MGMT\_ERR\_INVALID\_TLV](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb),

82

[ 84](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276) [IMG\_MGMT\_ERR\_TLV\_MULTIPLE\_HASHES\_FOUND](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276),

85

[ 87](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c) [IMG\_MGMT\_ERR\_TLV\_INVALID\_SIZE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c),

88

[ 90](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e) [IMG\_MGMT\_ERR\_HASH\_NOT\_FOUND](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e),

91

[ 93](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa) [IMG\_MGMT\_ERR\_NO\_FREE\_SLOT](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa),

94

[ 96](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071) [IMG\_MGMT\_ERR\_FLASH\_OPEN\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071),

97

[ 99](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355) [IMG\_MGMT\_ERR\_FLASH\_READ\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355),

100

[ 102](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f) [IMG\_MGMT\_ERR\_FLASH\_WRITE\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f),

103

[ 105](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c) [IMG\_MGMT\_ERR\_FLASH\_ERASE\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c),

106

[ 108](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5) [IMG\_MGMT\_ERR\_INVALID\_SLOT](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5),

109

[ 111](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de) [IMG\_MGMT\_ERR\_NO\_FREE\_MEMORY](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de),

112

[ 114](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e) [IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_ALREADY\_SET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e),

115

[ 117](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544) [IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_NOT\_SET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544),

118

[ 120](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2) [IMG\_MGMT\_ERR\_FLASH\_AREA\_DEVICE\_NULL](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2),

121

[ 123](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf) [IMG\_MGMT\_ERR\_INVALID\_PAGE\_OFFSET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf),

124

[ 126](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0) [IMG\_MGMT\_ERR\_INVALID\_OFFSET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0),

127

[ 129](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca) [IMG\_MGMT\_ERR\_INVALID\_LENGTH](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca),

130

[ 132](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7) [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7),

133

[ 135](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093) [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER\_MAGIC](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093),

136

[ 138](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6) [IMG\_MGMT\_ERR\_INVALID\_HASH](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6),

139

[ 141](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086) [IMG\_MGMT\_ERR\_INVALID\_FLASH\_ADDRESS](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086),

142

[ 144](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f) [IMG\_MGMT\_ERR\_VERSION\_GET\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f),

145

[ 147](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85) [IMG\_MGMT\_ERR\_CURRENT\_VERSION\_IS\_NEWER](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85),

148

[ 150](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3) [IMG\_MGMT\_ERR\_IMAGE\_ALREADY\_PENDING](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3),

151

[ 153](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7) [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_VECTOR\_TABLE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7),

154

[ 156](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b) [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_TOO\_LARGE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b),

157

[ 159](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b) [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_DATA\_OVERRUN](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b),

160

[ 162](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf) [IMG\_MGMT\_ERR\_IMAGE\_CONFIRMATION\_DENIED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf),

163

[ 165](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8) [IMG\_MGMT\_ERR\_IMAGE\_SETTING\_TEST\_TO\_ACTIVE\_DENIED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8),

166

[ 168](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6) [IMG\_MGMT\_ERR\_ACTIVE\_SLOT\_NOT\_KNOWN](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6),

169};

170

[ 174](group__mcumgr__img__mgmt.md#ga1d239fef127e65b11b71360eadfa1ede)enum [img\_mgmt\_id\_upload\_t](group__mcumgr__img__mgmt.md#ga1d239fef127e65b11b71360eadfa1ede) {

[ 175](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c) [IMG\_MGMT\_ID\_UPLOAD\_STATUS\_START](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c) = 0,

[ 176](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21) [IMG\_MGMT\_ID\_UPLOAD\_STATUS\_ONGOING](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21),

[ 177](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2) [IMG\_MGMT\_ID\_UPLOAD\_STATUS\_COMPLETE](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2),

178};

179

180extern int [boot\_current\_slot](group__mcumgr__img__mgmt.md#ga0d6bb8877516ca486c318fa12c129138);

181extern struct [img\_mgmt\_state](structimg__mgmt__state.md) [g\_img\_mgmt\_state](group__mcumgr__img__mgmt.md#gad3dce7b70ce3338588003a021eec1ab6);

182

[ 184](structimg__mgmt__upload__req.md)struct [img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md) {

[ 185](structimg__mgmt__upload__req.md#ad61f8c732f0b2150bd252e47eb539bb1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [image](structimg__mgmt__upload__req.md#ad61f8c732f0b2150bd252e47eb539bb1); /\* 0 by default \*/

[ 186](structimg__mgmt__upload__req.md#ae9c67210faa7dfc55a73f66defc00195) size\_t [off](structimg__mgmt__upload__req.md#ae9c67210faa7dfc55a73f66defc00195); /\* SIZE\_MAX if unspecified \*/

[ 187](structimg__mgmt__upload__req.md#a25cdcd55c77cde43af1a9ec9b414cecb) size\_t [size](structimg__mgmt__upload__req.md#a25cdcd55c77cde43af1a9ec9b414cecb); /\* SIZE\_MAX if unspecified \*/

[ 188](structimg__mgmt__upload__req.md#ade363ed09134ff2f3a1fcb20a6305cfa) struct zcbor\_string [img\_data](structimg__mgmt__upload__req.md#ade363ed09134ff2f3a1fcb20a6305cfa);

[ 189](structimg__mgmt__upload__req.md#ae30c1fc9257f04c88216ba92f8453dac) struct zcbor\_string [data\_sha](structimg__mgmt__upload__req.md#ae30c1fc9257f04c88216ba92f8453dac);

[ 190](structimg__mgmt__upload__req.md#a439504202c945a1dd74b75c35a1a8017) bool [upgrade](structimg__mgmt__upload__req.md#a439504202c945a1dd74b75c35a1a8017); /\* Only allow greater version numbers. \*/

191};

192

[ 194](structimg__mgmt__state.md)struct [img\_mgmt\_state](structimg__mgmt__state.md) {

[ 196](structimg__mgmt__state.md#a4da29c0c4b525463cce3f0d3ffbed633) int [area\_id](structimg__mgmt__state.md#a4da29c0c4b525463cce3f0d3ffbed633);

[ 198](structimg__mgmt__state.md#a965b6426ea57beac531af3bb9d2f0d0e) size\_t [off](structimg__mgmt__state.md#a965b6426ea57beac531af3bb9d2f0d0e);

[ 200](structimg__mgmt__state.md#a40619a325f216e1c27e45fd19ccd6db3) size\_t [size](structimg__mgmt__state.md#a40619a325f216e1c27e45fd19ccd6db3);

[ 202](structimg__mgmt__state.md#a6a3cbeb401f057fb1510e1acbdf7d71c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_sha\_len](structimg__mgmt__state.md#a6a3cbeb401f057fb1510e1acbdf7d71c);

[ 203](structimg__mgmt__state.md#a1c357f22c420a310c234c96a9bc7143f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_sha](structimg__mgmt__state.md#a1c357f22c420a310c234c96a9bc7143f)[[IMG\_MGMT\_DATA\_SHA\_LEN](group__mcumgr__img__mgmt.md#ga70168b0d707c15658fd09b02c361a64c)];

204};

205

[ 207](structimg__mgmt__upload__action.md)struct [img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md) {

[ 209](structimg__mgmt__upload__action.md#a4b1d3625ade4e4392094ace41ec4aa01) unsigned long long [size](structimg__mgmt__upload__action.md#a4b1d3625ade4e4392094ace41ec4aa01);

[ 211](structimg__mgmt__upload__action.md#aac493000e6989735531492f15edb6108) int [write\_bytes](structimg__mgmt__upload__action.md#aac493000e6989735531492f15edb6108);

[ 213](structimg__mgmt__upload__action.md#a6c9248e3c21325ed99ff8cf765f3ac82) int [area\_id](structimg__mgmt__upload__action.md#a6c9248e3c21325ed99ff8cf765f3ac82);

[ 215](structimg__mgmt__upload__action.md#a7661db4343ebf6f7d040e3e87d3611aa) bool [proceed](structimg__mgmt__upload__action.md#a7661db4343ebf6f7d040e3e87d3611aa);

[ 217](structimg__mgmt__upload__action.md#abe9c3503c6d58cf3b7ad637cd4fec852) bool [erase](structimg__mgmt__upload__action.md#abe9c3503c6d58cf3b7ad637cd4fec852);

218#ifdef CONFIG\_MCUMGR\_GRP\_IMG\_VERBOSE\_ERR

220 const char \*rc\_rsn;

221#endif

222};

223

224/\*

225 \* @brief Read info of an image at the specified slot number

226 \*

227 \* @param image\_slot image slot number

228 \* @param ver output buffer for image version

229 \* @param hash output buffer for image hash

230 \* @param flags output buffer for image flags

231 \*

232 \* @return 0 on success, non-zero on failure.

233 \*/

[ 234](group__mcumgr__img__mgmt.md#ga60ae88823a561160b1ddc406382e4ac3)int [img\_mgmt\_read\_info](group__mcumgr__img__mgmt.md#ga60ae88823a561160b1ddc406382e4ac3)(int image\_slot, struct image\_version \*ver, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hash, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

235

[ 243](group__mcumgr__img__mgmt.md#gae9cfa02e5f171d68287cdb0d7d4c0610)int [img\_mgmt\_my\_version](group__mcumgr__img__mgmt.md#gae9cfa02e5f171d68287cdb0d7d4c0610)(struct image\_version \*ver);

244

[ 253](group__mcumgr__img__mgmt.md#ga5199849b6d8847c6a1260254940db95b)int [img\_mgmt\_ver\_str](group__mcumgr__img__mgmt.md#ga5199849b6d8847c6a1260254940db95b)(const struct image\_version \*ver, char \*dst);

254

[ 262](group__mcumgr__img__mgmt.md#gab35c8adf2e5e2c941ecbaf3c03101e55)int [img\_mgmt\_active\_slot](group__mcumgr__img__mgmt.md#gab35c8adf2e5e2c941ecbaf3c03101e55)(int image);

263

[ 271](group__mcumgr__img__mgmt.md#gab6a92433b859fce18b58e6110fa5f489)int [img\_mgmt\_active\_image](group__mcumgr__img__mgmt.md#gab6a92433b859fce18b58e6110fa5f489)(void);

272

[ 284](group__mcumgr__img__mgmt.md#ga90de2da23bcd650ca59219fdfd4f55a1)int [img\_mgmt\_slot\_in\_use](group__mcumgr__img__mgmt.md#ga90de2da23bcd650ca59219fdfd4f55a1)(int slot);

285

[ 294](group__mcumgr__img__mgmt.md#ga3e496199d0ea4aa1b3f51e59bb7473f0)int [img\_mgmt\_state\_any\_pending](group__mcumgr__img__mgmt.md#ga3e496199d0ea4aa1b3f51e59bb7473f0)(void);

295

[ 311](group__mcumgr__img__mgmt.md#ga42475389b4e31d5f35ea58873527e948)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [img\_mgmt\_state\_flags](group__mcumgr__img__mgmt.md#ga42475389b4e31d5f35ea58873527e948)(int query\_slot);

312

[ 325](group__mcumgr__img__mgmt.md#ga7e529fa76ddb3d3bf4a527cb11fa9c89)int [img\_mgmt\_state\_set\_pending](group__mcumgr__img__mgmt.md#ga7e529fa76ddb3d3bf4a527cb11fa9c89)(int slot, int permanent);

326

[ 335](group__mcumgr__img__mgmt.md#gaed0b945d2f83daf63d850b232a2cfea8)int [img\_mgmt\_state\_confirm](group__mcumgr__img__mgmt.md#gaed0b945d2f83daf63d850b232a2cfea8)(void);

336

[ 347](group__mcumgr__img__mgmt.md#ga6c9124cc59c99769908cdf83f58e1bf1)int [img\_mgmt\_vercmp](group__mcumgr__img__mgmt.md#ga6c9124cc59c99769908cdf83f58e1bf1)(const struct image\_version \*a, const struct image\_version \*b);

348

349#if defined(CONFIG\_MCUMGR\_GRP\_IMG\_MUTEX)

350/\*

351 \* @brief Will reset the image management state back to default (no ongoing upload),

352 \* requires that CONFIG\_MCUMGR\_GRP\_IMG\_MUTEX be enabled to allow for mutex

353 \* locking of the image management state object.

354 \*/

355void img\_mgmt\_reset\_upload(void);

356#endif

357

358#ifdef CONFIG\_MCUMGR\_GRP\_IMG\_VERBOSE\_ERR

359#define IMG\_MGMT\_UPLOAD\_ACTION\_SET\_RC\_RSN(action, rsn) ((action)->rc\_rsn = (rsn))

360#define IMG\_MGMT\_UPLOAD\_ACTION\_RC\_RSN(action) ((action)->rc\_rsn)

361int img\_mgmt\_error\_rsp(struct [smp\_streamer](structsmp__streamer.md) \*ctxt, int rc, const char \*rsn);

362extern const char \*img\_mgmt\_err\_str\_app\_reject;

363extern const char \*img\_mgmt\_err\_str\_hdr\_malformed;

364extern const char \*img\_mgmt\_err\_str\_magic\_mismatch;

365extern const char \*img\_mgmt\_err\_str\_no\_slot;

366extern const char \*img\_mgmt\_err\_str\_flash\_open\_failed;

367extern const char \*img\_mgmt\_err\_str\_flash\_erase\_failed;

368extern const char \*img\_mgmt\_err\_str\_flash\_write\_failed;

369extern const char \*img\_mgmt\_err\_str\_downgrade;

370extern const char \*img\_mgmt\_err\_str\_image\_bad\_flash\_addr;

371extern const char \*img\_mgmt\_err\_str\_image\_too\_large;

372extern const char \*img\_mgmt\_err\_str\_data\_overrun;

373#else

[ 374](group__mcumgr__img__mgmt.md#ga56e01e5bfa9fdd9bf6ebdc0dc3ac19ba)#define IMG\_MGMT\_UPLOAD\_ACTION\_SET\_RC\_RSN(action, rsn)

[ 375](group__mcumgr__img__mgmt.md#gaee07bacea29269e24ca15a2e1716390d)#define IMG\_MGMT\_UPLOAD\_ACTION\_RC\_RSN(action) NULL

376#endif

377

381

382#ifdef \_\_cplusplus

383}

384#endif

385

386#endif /\* H\_IMG\_MGMT\_ \*/

[boot\_current\_slot](group__mcumgr__img__mgmt.md#ga0d6bb8877516ca486c318fa12c129138)

int boot\_current\_slot

[img\_mgmt\_id\_upload\_t](group__mcumgr__img__mgmt.md#ga1d239fef127e65b11b71360eadfa1ede)

img\_mgmt\_id\_upload\_t

IMG\_MGMT\_ID\_UPLOAD statuses.

**Definition** img\_mgmt.h:174

[img\_mgmt\_state\_any\_pending](group__mcumgr__img__mgmt.md#ga3e496199d0ea4aa1b3f51e59bb7473f0)

int img\_mgmt\_state\_any\_pending(void)

Check if any slot is in MCUboot pending state.

[img\_mgmt\_state\_flags](group__mcumgr__img__mgmt.md#ga42475389b4e31d5f35ea58873527e948)

uint8\_t img\_mgmt\_state\_flags(int query\_slot)

Returns state flags set to slot.

[img\_mgmt\_ver\_str](group__mcumgr__img__mgmt.md#ga5199849b6d8847c6a1260254940db95b)

int img\_mgmt\_ver\_str(const struct image\_version \*ver, char \*dst)

Format version string from struct image\_version.

[img\_mgmt\_read\_info](group__mcumgr__img__mgmt.md#ga60ae88823a561160b1ddc406382e4ac3)

int img\_mgmt\_read\_info(int image\_slot, struct image\_version \*ver, uint8\_t \*hash, uint32\_t \*flags)

[img\_mgmt\_err\_code\_t](group__mcumgr__img__mgmt.md#ga669286d96816e0e99792f407752c81a5)

img\_mgmt\_err\_code\_t

Command result codes for image management group.

**Definition** img\_mgmt.h:64

[img\_mgmt\_vercmp](group__mcumgr__img__mgmt.md#ga6c9124cc59c99769908cdf83f58e1bf1)

int img\_mgmt\_vercmp(const struct image\_version \*a, const struct image\_version \*b)

Compares two image version numbers in a semver-compatible way.

[IMG\_MGMT\_DATA\_SHA\_LEN](group__mcumgr__img__mgmt.md#ga70168b0d707c15658fd09b02c361a64c)

#define IMG\_MGMT\_DATA\_SHA\_LEN

**Definition** img\_mgmt.h:28

[img\_mgmt\_state\_set\_pending](group__mcumgr__img__mgmt.md#ga7e529fa76ddb3d3bf4a527cb11fa9c89)

int img\_mgmt\_state\_set\_pending(int slot, int permanent)

Sets the pending flag for the specified image slot.

[img\_mgmt\_slot\_in\_use](group__mcumgr__img__mgmt.md#ga90de2da23bcd650ca59219fdfd4f55a1)

int img\_mgmt\_slot\_in\_use(int slot)

Check if the image slot is in use.

[img\_mgmt\_active\_slot](group__mcumgr__img__mgmt.md#gab35c8adf2e5e2c941ecbaf3c03101e55)

int img\_mgmt\_active\_slot(int image)

Get active, running application slot number for an image.

[img\_mgmt\_active\_image](group__mcumgr__img__mgmt.md#gab6a92433b859fce18b58e6110fa5f489)

int img\_mgmt\_active\_image(void)

Get active image number.

[g\_img\_mgmt\_state](group__mcumgr__img__mgmt.md#gad3dce7b70ce3338588003a021eec1ab6)

struct img\_mgmt\_state g\_img\_mgmt\_state

[img\_mgmt\_my\_version](group__mcumgr__img__mgmt.md#gae9cfa02e5f171d68287cdb0d7d4c0610)

int img\_mgmt\_my\_version(struct image\_version \*ver)

Get the image version of the currently running application.

[img\_mgmt\_state\_confirm](group__mcumgr__img__mgmt.md#gaed0b945d2f83daf63d850b232a2cfea8)

int img\_mgmt\_state\_confirm(void)

Confirms the current image state.

[IMG\_MGMT\_ID\_UPLOAD\_STATUS\_ONGOING](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21)

@ IMG\_MGMT\_ID\_UPLOAD\_STATUS\_ONGOING

**Definition** img\_mgmt.h:176

[IMG\_MGMT\_ID\_UPLOAD\_STATUS\_COMPLETE](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2)

@ IMG\_MGMT\_ID\_UPLOAD\_STATUS\_COMPLETE

**Definition** img\_mgmt.h:177

[IMG\_MGMT\_ID\_UPLOAD\_STATUS\_START](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c)

@ IMG\_MGMT\_ID\_UPLOAD\_STATUS\_START

**Definition** img\_mgmt.h:175

[IMG\_MGMT\_ERR\_NO\_FREE\_SLOT](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa)

@ IMG\_MGMT\_ERR\_NO\_FREE\_SLOT

There is no free slot to place the image.

**Definition** img\_mgmt.h:93

[IMG\_MGMT\_ERR\_INVALID\_LENGTH](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca)

@ IMG\_MGMT\_ERR\_INVALID\_LENGTH

The length parameter was not provided and is required.

**Definition** img\_mgmt.h:129

[IMG\_MGMT\_ERR\_INVALID\_FLASH\_ADDRESS](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086)

@ IMG\_MGMT\_ERR\_INVALID\_FLASH\_ADDRESS

The image load address does not match the address of the flash area.

**Definition** img\_mgmt.h:141

[IMG\_MGMT\_ERR\_ACTIVE\_SLOT\_NOT\_KNOWN](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6)

@ IMG\_MGMT\_ERR\_ACTIVE\_SLOT\_NOT\_KNOWN

Current active slot for image cannot be determined.

**Definition** img\_mgmt.h:168

[IMG\_MGMT\_ERR\_NO\_IMAGE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6)

@ IMG\_MGMT\_ERR\_NO\_IMAGE

There is no image in the slot.

**Definition** img\_mgmt.h:75

[IMG\_MGMT\_ERR\_CURRENT\_VERSION\_IS\_NEWER](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85)

@ IMG\_MGMT\_ERR\_CURRENT\_VERSION\_IS\_NEWER

The currently running application is newer than the version being uploaded.

**Definition** img\_mgmt.h:147

[IMG\_MGMT\_ERR\_INVALID\_IMAGE\_VECTOR\_TABLE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7)

@ IMG\_MGMT\_ERR\_INVALID\_IMAGE\_VECTOR\_TABLE

The image vector table is invalid.

**Definition** img\_mgmt.h:153

[IMG\_MGMT\_ERR\_INVALID\_TLV](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb)

@ IMG\_MGMT\_ERR\_INVALID\_TLV

The image in the slot has an invalid TLV type and/or length.

**Definition** img\_mgmt.h:81

[IMG\_MGMT\_ERR\_INVALID\_HASH](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6)

@ IMG\_MGMT\_ERR\_INVALID\_HASH

The hash parameter provided is not valid.

**Definition** img\_mgmt.h:138

[IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER\_MAGIC](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093)

@ IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER\_MAGIC

The image header magic value does not match the expected value.

**Definition** img\_mgmt.h:135

[IMG\_MGMT\_ERR\_NO\_TLVS](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10)

@ IMG\_MGMT\_ERR\_NO\_TLVS

The image in the slot has no TLVs (tag, length, value).

**Definition** img\_mgmt.h:78

[IMG\_MGMT\_ERR\_FLASH\_CONFIG\_QUERY\_FAIL](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063)

@ IMG\_MGMT\_ERR\_FLASH\_CONFIG\_QUERY\_FAIL

Failed to query flash area configuration.

**Definition** img\_mgmt.h:72

[IMG\_MGMT\_ERR\_HASH\_NOT\_FOUND](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e)

@ IMG\_MGMT\_ERR\_HASH\_NOT\_FOUND

The image in the slot does not have a hash TLV, which is required.

**Definition** img\_mgmt.h:90

[IMG\_MGMT\_ERR\_FLASH\_AREA\_DEVICE\_NULL](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2)

@ IMG\_MGMT\_ERR\_FLASH\_AREA\_DEVICE\_NULL

The device for the flash area is NULL.

**Definition** img\_mgmt.h:120

[IMG\_MGMT\_ERR\_INVALID\_SLOT](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5)

@ IMG\_MGMT\_ERR\_INVALID\_SLOT

The provided slot is not valid.

**Definition** img\_mgmt.h:108

[IMG\_MGMT\_ERR\_OK](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0)

@ IMG\_MGMT\_ERR\_OK

No error, this is implied if there is no ret value in the response.

**Definition** img\_mgmt.h:66

[IMG\_MGMT\_ERR\_FLASH\_OPEN\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071)

@ IMG\_MGMT\_ERR\_FLASH\_OPEN\_FAILED

Flash area opening failed.

**Definition** img\_mgmt.h:96

[IMG\_MGMT\_ERR\_INVALID\_PAGE\_OFFSET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf)

@ IMG\_MGMT\_ERR\_INVALID\_PAGE\_OFFSET

The offset for a page number is invalid.

**Definition** img\_mgmt.h:123

[IMG\_MGMT\_ERR\_FLASH\_ERASE\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c)

@ IMG\_MGMT\_ERR\_FLASH\_ERASE\_FAILED

Flash area erase failed.

**Definition** img\_mgmt.h:105

[IMG\_MGMT\_ERR\_INVALID\_OFFSET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0)

@ IMG\_MGMT\_ERR\_INVALID\_OFFSET

The offset parameter was not provided and is required.

**Definition** img\_mgmt.h:126

[IMG\_MGMT\_ERR\_UNKNOWN](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe)

@ IMG\_MGMT\_ERR\_UNKNOWN

Unknown error occurred.

**Definition** img\_mgmt.h:69

[IMG\_MGMT\_ERR\_INVALID\_IMAGE\_DATA\_OVERRUN](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b)

@ IMG\_MGMT\_ERR\_INVALID\_IMAGE\_DATA\_OVERRUN

The amount of data sent is larger than the provided image size.

**Definition** img\_mgmt.h:159

[IMG\_MGMT\_ERR\_TLV\_INVALID\_SIZE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c)

@ IMG\_MGMT\_ERR\_TLV\_INVALID\_SIZE

The image in the slot has an invalid TLV size.

**Definition** img\_mgmt.h:87

[IMG\_MGMT\_ERR\_FLASH\_READ\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355)

@ IMG\_MGMT\_ERR\_FLASH\_READ\_FAILED

Flash area reading failed.

**Definition** img\_mgmt.h:99

[IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_NOT\_SET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544)

@ IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_NOT\_SET

The flash context is not set.

**Definition** img\_mgmt.h:117

[IMG\_MGMT\_ERR\_IMAGE\_SETTING\_TEST\_TO\_ACTIVE\_DENIED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8)

@ IMG\_MGMT\_ERR\_IMAGE\_SETTING\_TEST\_TO\_ACTIVE\_DENIED

Setting test to active slot is not allowed.

**Definition** img\_mgmt.h:165

[IMG\_MGMT\_ERR\_INVALID\_IMAGE\_TOO\_LARGE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b)

@ IMG\_MGMT\_ERR\_INVALID\_IMAGE\_TOO\_LARGE

The image it too large to fit.

**Definition** img\_mgmt.h:156

[IMG\_MGMT\_ERR\_NO\_FREE\_MEMORY](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de)

@ IMG\_MGMT\_ERR\_NO\_FREE\_MEMORY

Insufficient heap memory (malloc failed).

**Definition** img\_mgmt.h:111

[IMG\_MGMT\_ERR\_TLV\_MULTIPLE\_HASHES\_FOUND](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276)

@ IMG\_MGMT\_ERR\_TLV\_MULTIPLE\_HASHES\_FOUND

The image in the slot has multiple hash TLVs, which is invalid.

**Definition** img\_mgmt.h:84

[IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7)

@ IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER

The image length is smaller than the size of an image header.

**Definition** img\_mgmt.h:132

[IMG\_MGMT\_ERR\_FLASH\_WRITE\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f)

@ IMG\_MGMT\_ERR\_FLASH\_WRITE\_FAILED

Flash area writing failed.

**Definition** img\_mgmt.h:102

[IMG\_MGMT\_ERR\_IMAGE\_CONFIRMATION\_DENIED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf)

@ IMG\_MGMT\_ERR\_IMAGE\_CONFIRMATION\_DENIED

Confirmation of image has been denied.

**Definition** img\_mgmt.h:162

[IMG\_MGMT\_ERR\_VERSION\_GET\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f)

@ IMG\_MGMT\_ERR\_VERSION\_GET\_FAILED

Failed to get version of currently running application.

**Definition** img\_mgmt.h:144

[IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_ALREADY\_SET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e)

@ IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_ALREADY\_SET

The flash context is already set.

**Definition** img\_mgmt.h:114

[IMG\_MGMT\_ERR\_IMAGE\_ALREADY\_PENDING](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3)

@ IMG\_MGMT\_ERR\_IMAGE\_ALREADY\_PENDING

There is already an image operating pending.

**Definition** img\_mgmt.h:150

[inttypes.h](inttypes_8h.md)

[smp.h](mgmt_2mcumgr_2smp_2smp_8h.md)

SMP - Simple Management Protocol.

[mgmt.h](mgmt_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[img\_mgmt\_state](structimg__mgmt__state.md)

Global state for upload in progress.

**Definition** img\_mgmt.h:194

[img\_mgmt\_state::data\_sha](structimg__mgmt__state.md#a1c357f22c420a310c234c96a9bc7143f)

uint8\_t data\_sha[32]

**Definition** img\_mgmt.h:203

[img\_mgmt\_state::size](structimg__mgmt__state.md#a40619a325f216e1c27e45fd19ccd6db3)

size\_t size

Total size of image data.

**Definition** img\_mgmt.h:200

[img\_mgmt\_state::area\_id](structimg__mgmt__state.md#a4da29c0c4b525463cce3f0d3ffbed633)

int area\_id

Flash area being written; -1 if no upload in progress.

**Definition** img\_mgmt.h:196

[img\_mgmt\_state::data\_sha\_len](structimg__mgmt__state.md#a6a3cbeb401f057fb1510e1acbdf7d71c)

uint8\_t data\_sha\_len

Hash of image data; used for resumption of a partial upload.

**Definition** img\_mgmt.h:202

[img\_mgmt\_state::off](structimg__mgmt__state.md#a965b6426ea57beac531af3bb9d2f0d0e)

size\_t off

Flash offset of next chunk.

**Definition** img\_mgmt.h:198

[img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md)

Describes what to do during processing of an upload request.

**Definition** img\_mgmt.h:207

[img\_mgmt\_upload\_action::size](structimg__mgmt__upload__action.md#a4b1d3625ade4e4392094ace41ec4aa01)

unsigned long long size

The total size of the image.

**Definition** img\_mgmt.h:209

[img\_mgmt\_upload\_action::area\_id](structimg__mgmt__upload__action.md#a6c9248e3c21325ed99ff8cf765f3ac82)

int area\_id

The flash area to write to.

**Definition** img\_mgmt.h:213

[img\_mgmt\_upload\_action::proceed](structimg__mgmt__upload__action.md#a7661db4343ebf6f7d040e3e87d3611aa)

bool proceed

Whether to process the request; false if offset is wrong.

**Definition** img\_mgmt.h:215

[img\_mgmt\_upload\_action::write\_bytes](structimg__mgmt__upload__action.md#aac493000e6989735531492f15edb6108)

int write\_bytes

The number of image bytes to write to flash.

**Definition** img\_mgmt.h:211

[img\_mgmt\_upload\_action::erase](structimg__mgmt__upload__action.md#abe9c3503c6d58cf3b7ad637cd4fec852)

bool erase

Whether to erase the destination flash area.

**Definition** img\_mgmt.h:217

[img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md)

Represents an individual upload request.

**Definition** img\_mgmt.h:184

[img\_mgmt\_upload\_req::size](structimg__mgmt__upload__req.md#a25cdcd55c77cde43af1a9ec9b414cecb)

size\_t size

**Definition** img\_mgmt.h:187

[img\_mgmt\_upload\_req::upgrade](structimg__mgmt__upload__req.md#a439504202c945a1dd74b75c35a1a8017)

bool upgrade

**Definition** img\_mgmt.h:190

[img\_mgmt\_upload\_req::image](structimg__mgmt__upload__req.md#ad61f8c732f0b2150bd252e47eb539bb1)

uint32\_t image

**Definition** img\_mgmt.h:185

[img\_mgmt\_upload\_req::img\_data](structimg__mgmt__upload__req.md#ade363ed09134ff2f3a1fcb20a6305cfa)

struct zcbor\_string img\_data

**Definition** img\_mgmt.h:188

[img\_mgmt\_upload\_req::data\_sha](structimg__mgmt__upload__req.md#ae30c1fc9257f04c88216ba92f8453dac)

struct zcbor\_string data\_sha

**Definition** img\_mgmt.h:189

[img\_mgmt\_upload\_req::off](structimg__mgmt__upload__req.md#ae9c67210faa7dfc55a73f66defc00195)

size\_t off

**Definition** img\_mgmt.h:186

[smp\_streamer](structsmp__streamer.md)

Decodes, encodes, and transmits SMP packets.

**Definition** smp.h:83

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [img\_mgmt](dir_731c1b2142dfc9d7fee3a06aa394438e.md)
- [img\_mgmt.h](img__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
