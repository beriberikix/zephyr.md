---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/video-controls_8h_source.html
original_path: doxygen/html/video-controls_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video-controls.h

[Go to the documentation of this file.](video-controls_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited.

3 \* Copyright (c) 2024 tinyVision.ai Inc.

4 \* Copyright 2025 NXP

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8#ifndef ZEPHYR\_INCLUDE\_VIDEO\_CONTROLS\_H\_

9#define ZEPHYR\_INCLUDE\_VIDEO\_CONTROLS\_H\_

10

16

32

33#include <[stdint.h](stdint_8h.md)>

34

35#ifdef \_\_cplusplus

36extern "C" {

37#endif

38

[ 43](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)#define VIDEO\_CID\_BASE 0x00980900

44

[ 46](group__video__controls.md#ga1529eeb7c36bfe53e3916dbd9c6f5b1e)#define VIDEO\_CID\_BRIGHTNESS (VIDEO\_CID\_BASE + 0)

47

[ 49](group__video__controls.md#ga9ca85f6b1d9add05eacb008dc4ccb2e4)#define VIDEO\_CID\_CONTRAST (VIDEO\_CID\_BASE + 1)

50

[ 52](group__video__controls.md#ga200017c2141f5c90ade652224d1d4364)#define VIDEO\_CID\_SATURATION (VIDEO\_CID\_BASE + 2)

53

[ 55](group__video__controls.md#ga588a1206d5046a7b9e8415db725cae81)#define VIDEO\_CID\_HUE (VIDEO\_CID\_BASE + 3)

56

[ 58](group__video__controls.md#ga7e2ce049ed534e1c29ac47d33013e180)#define VIDEO\_CID\_AUTO\_WHITE\_BALANCE (VIDEO\_CID\_BASE + 12)

59

[ 61](group__video__controls.md#gab534e6263a6b5caae48543346ba2f7ef)#define VIDEO\_CID\_RED\_BALANCE (VIDEO\_CID\_BASE + 14)

62

[ 64](group__video__controls.md#gaf4d38f5eed6feb9ef9509c1747a332b8)#define VIDEO\_CID\_BLUE\_BALANCE (VIDEO\_CID\_BASE + 15)

65

[ 67](group__video__controls.md#ga4e38bb3fcb80b2d28fa88186b65e4fea)#define VIDEO\_CID\_GAMMA (VIDEO\_CID\_BASE + 16)

68

[ 70](group__video__controls.md#ga24e259a6466537377b7bb8a151311ae1)#define VIDEO\_CID\_EXPOSURE (VIDEO\_CID\_BASE + 17)

71

[ 73](group__video__controls.md#gac1c1d3580b7ff84b6a461cea0b3942e8)#define VIDEO\_CID\_AUTOGAIN (VIDEO\_CID\_BASE + 18)

74

[ 79](group__video__controls.md#ga36259be44d9d08b149fd35dd28bbaf50)#define VIDEO\_CID\_GAIN (VIDEO\_CID\_BASE + 19)

80

[ 82](group__video__controls.md#ga59aa47b6f558ef5ae64a67f4a7ac7e31)#define VIDEO\_CID\_HFLIP (VIDEO\_CID\_BASE + 20)

83

[ 85](group__video__controls.md#ga16651a6825b619399a333ed39e802dfc)#define VIDEO\_CID\_VFLIP (VIDEO\_CID\_BASE + 21)

86

[ 88](group__video__controls.md#ga762a6c2b0fb032b9ebdfeff5ed15c3de)#define VIDEO\_CID\_POWER\_LINE\_FREQUENCY (VIDEO\_CID\_BASE + 24)

[ 89](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a)enum [video\_power\_line\_frequency](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a) {

[ 90](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93) = 0,

[ 91](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10) = 1,

[ 92](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796) = 2,

[ 93](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0) = 3,

94};

95

[ 100](group__video__controls.md#ga9c0df146e6064169a89bd88b10085cec)#define VIDEO\_CID\_HUE\_AUTO (VIDEO\_CID\_BASE + 25)

101

[ 105](group__video__controls.md#ga0670d89542dc532a9c775e8e9c2638b1)#define VIDEO\_CID\_WHITE\_BALANCE\_TEMPERATURE (VIDEO\_CID\_BASE + 26)

106

[ 110](group__video__controls.md#gab0509f0d3106bca07658e7cfcb1883cf)#define VIDEO\_CID\_SHARPNESS (VIDEO\_CID\_BASE + 27)

111

[ 115](group__video__controls.md#ga2f22b11b526154e66440eca74ec5bd66)#define VIDEO\_CID\_BACKLIGHT\_COMPENSATION (VIDEO\_CID\_BASE + 28)

116

[ 118](group__video__controls.md#ga3fe7778ddb5c3f945b7649379a13321e)#define VIDEO\_CID\_COLORFX (VIDEO\_CID\_BASE + 31)

[ 119](group__video__controls.md#ga99f4b6cf21c8baaf510fbcfccb645960)enum [video\_colorfx](group__video__controls.md#ga99f4b6cf21c8baaf510fbcfccb645960) {

[ 120](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a9960e8b54cf9070c04664246e67f3237) [VIDEO\_COLORFX\_NONE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a9960e8b54cf9070c04664246e67f3237) = 0,

[ 121](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a52f62a92f6f0e158b1797719efb79735) [VIDEO\_COLORFX\_BW](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a52f62a92f6f0e158b1797719efb79735) = 1,

[ 122](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a483faa51fb4728b89c1a8da60b139a37) [VIDEO\_COLORFX\_SEPIA](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a483faa51fb4728b89c1a8da60b139a37) = 2,

[ 123](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960ac9367e073eef47865d90ba9ae6eb98a0) [VIDEO\_COLORFX\_NEGATIVE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960ac9367e073eef47865d90ba9ae6eb98a0) = 3,

[ 124](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960aae3d42f32c4f14e371343a32e8132cc0) [VIDEO\_COLORFX\_EMBOSS](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960aae3d42f32c4f14e371343a32e8132cc0) = 4,

[ 125](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a789155f47a0302661a71155c1e6045fc) [VIDEO\_COLORFX\_SKETCH](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a789155f47a0302661a71155c1e6045fc) = 5,

[ 126](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a09b5346a7431c2c0e7415037ee5a6f8b) [VIDEO\_COLORFX\_SKY\_BLUE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a09b5346a7431c2c0e7415037ee5a6f8b) = 6,

[ 127](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960abd0ddf263af2224bebe12da19711c6a1) [VIDEO\_COLORFX\_GRASS\_GREEN](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960abd0ddf263af2224bebe12da19711c6a1) = 7,

[ 128](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a3d4856179a0279a23f1597c3c0a615ef) [VIDEO\_COLORFX\_SKIN\_WHITEN](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a3d4856179a0279a23f1597c3c0a615ef) = 8,

[ 129](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a5e77aa2b5530062aaaf1156a340e3826) [VIDEO\_COLORFX\_VIVID](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a5e77aa2b5530062aaaf1156a340e3826) = 9,

[ 130](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960adb9e16ef9511c8eec1d6dbead4843a4c) [VIDEO\_COLORFX\_AQUA](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960adb9e16ef9511c8eec1d6dbead4843a4c) = 10,

[ 131](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a00faf2d7d366f0109d64568839416ccd) [VIDEO\_COLORFX\_ART\_FREEZE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a00faf2d7d366f0109d64568839416ccd) = 11,

[ 132](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a1c93819be559612ccea3a2781cbb7d25) [VIDEO\_COLORFX\_SILHOUETTE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a1c93819be559612ccea3a2781cbb7d25) = 12,

[ 133](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a2f6f282e1e195bdc29aa6a351c2bc715) [VIDEO\_COLORFX\_SOLARIZATION](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a2f6f282e1e195bdc29aa6a351c2bc715) = 13,

[ 134](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a71acc838d9197b671accab7763c5388b) [VIDEO\_COLORFX\_ANTIQUE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a71acc838d9197b671accab7763c5388b) = 14,

135};

136

137/\* Enable Automatic Brightness. \*/

[ 138](group__video__controls.md#ga46bb41b012b1a2240270817b9ce57637)#define VIDEO\_CID\_AUTOBRIGHTNESS (VIDEO\_CID\_BASE + 32)

139

[ 143](group__video__controls.md#ga5d2c02644e26f6a7f9887d5879231106)#define VIDEO\_CID\_BAND\_STOP\_FILTER (VIDEO\_CID\_BASE + 33)

144

[ 149](group__video__controls.md#ga78dcca8b4c8b29f23e983974b861f157)#define VIDEO\_CID\_ALPHA\_COMPONENT (VIDEO\_CID\_BASE + 41)

150

[ 152](group__video__controls.md#ga829221ec6ea7348e743173ce5e6bd635)#define VIDEO\_CID\_LASTP1 (VIDEO\_CID\_BASE + 44)

153

157

[ 162](group__video__controls.md#gadf37e306a8d73cec4674422e74ffc85e)#define VIDEO\_CID\_CODEC\_CLASS\_BASE 0x00990900

163

167

[ 172](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26)#define VIDEO\_CID\_CAMERA\_CLASS\_BASE 0x009a0900

173

[ 178](group__video__controls.md#gab83ae3ca7fa3da66243431d489be37bd)#define VIDEO\_CID\_EXPOSURE\_AUTO (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 1)

[ 179](group__video__controls.md#ga167cf84b8f4259e6cdd333748deafaf6)enum [video\_exposure\_type](group__video__controls.md#ga167cf84b8f4259e6cdd333748deafaf6) {

[ 180](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b) [VIDEO\_EXPOSURE\_AUTO](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b) = 0,

[ 181](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224) [VIDEO\_EXPOSURE\_MANUAL](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224) = 1,

[ 182](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61) [VIDEO\_EXPOSURE\_SHUTTER\_PRIORITY](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61) = 2,

[ 183](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd) [VIDEO\_EXPOSURE\_APERTURE\_PRIORITY](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd) = 3

184};

185

[ 191](group__video__controls.md#ga036f78623bcae18ea9627d45d1209245)#define VIDEO\_CID\_EXPOSURE\_ABSOLUTE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 2)

192

[ 197](group__video__controls.md#gaa5f2ebd1e1aef2da68be4742941c1f50)#define VIDEO\_CID\_EXPOSURE\_AUTO\_PRIORITY (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 3)

198

[ 203](group__video__controls.md#ga23ed465d76fc54680d1e22422b66c829)#define VIDEO\_CID\_PAN\_RELATIVE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 4)

204

[ 209](group__video__controls.md#ga7c51639505c7b97fb1953ade5fc72534)#define VIDEO\_CID\_TILT\_RELATIVE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 5)

210

[ 216](group__video__controls.md#ga3b45437f606b8717dcadc22d56a706da)#define VIDEO\_CID\_PAN\_ABSOLUTE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 8)

217

[ 222](group__video__controls.md#gae474209914926f2bd38c99e020224b9c)#define VIDEO\_CID\_TILT\_ABSOLUTE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 9)

223

[ 228](group__video__controls.md#ga9ce95d3c135a9221a8d0431d9df9836b)#define VIDEO\_CID\_FOCUS\_ABSOLUTE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 10)

229

[ 234](group__video__controls.md#ga4137146c348efdcc8088f6be1274b164)#define VIDEO\_CID\_FOCUS\_RELATIVE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 11)

235

[ 240](group__video__controls.md#ga031525e88a6c0f915903f5c9068589f4)#define VIDEO\_CID\_FOCUS\_AUTO (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 12)

241

[ 245](group__video__controls.md#ga1033858d5515c2016a0cc6ac06fd8b91)#define VIDEO\_CID\_ZOOM\_ABSOLUTE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 13)

246

[ 251](group__video__controls.md#ga40e76f27e97549a779a6581bd210b0f4)#define VIDEO\_CID\_ZOOM\_RELATIVE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 14)

252

[ 260](group__video__controls.md#ga1a79541da7b7a37d9358fb1a3c42a1b7)#define VIDEO\_CID\_ZOOM\_CONTINUOUS (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 15)

261

[ 265](group__video__controls.md#ga452858d6adfec3b58db6b26c96638fb2)#define VIDEO\_CID\_IRIS\_ABSOLUTE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 17)

266

[ 271](group__video__controls.md#ga8d1452dfe9c190f6e28e5e3dd35c52cc)#define VIDEO\_CID\_IRIS\_RELATIVE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 18)

272

[ 279](group__video__controls.md#ga9d224bc93e5c23317f9ccf89713a18d6)#define VIDEO\_CID\_WIDE\_DYNAMIC\_RANGE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 21)

280

[ 286](group__video__controls.md#ga99996bce4091e4223130d9ae5e1024cd)#define VIDEO\_CID\_PAN\_SPEED (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 32)

287

[ 292](group__video__controls.md#ga3bfeedcd519191bcf1d684fd983ca9bc)#define VIDEO\_CID\_TILT\_SPEED (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 33)

293

[ 302](group__video__controls.md#ga57e5c3f562683a2b7ea1f96a58f633be)#define VIDEO\_CID\_CAMERA\_ORIENTATION (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 34)

[ 303](group__video__controls.md#ga1fb4e9981b362010439b9419691ac2af)enum [video\_camera\_orientation](group__video__controls.md#ga1fb4e9981b362010439b9419691ac2af) {

[ 305](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef) [VIDEO\_CAMERA\_ORIENTATION\_FRONT](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef) = 0,

[ 307](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072) [VIDEO\_CAMERA\_ORIENTATION\_BACK](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072) = 1,

[ 309](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594) [VIDEO\_CAMERA\_ORIENTATION\_EXTERNAL](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594) = 2,

310};

311

[ 317](group__video__controls.md#ga0d48a910e8d6797842dc25b33fc3f187)#define VIDEO\_CID\_CAMERA\_SENSOR\_ROTATION (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 35)

318

322

[ 327](group__video__controls.md#ga9e0c8dc67fab1a80f81cd4be2e875954)#define VIDEO\_CID\_FLASH\_CLASS\_BASE 0x009c0900

328

332

[ 337](group__video__controls.md#ga9281f5a61120a6de015a9bbc75ee8b91)#define VIDEO\_CID\_JPEG\_CLASS\_BASE 0x009d0900

338

[ 340](group__video__controls.md#ga883c2a761ea0f00e83c884a5b4b45eee)#define VIDEO\_CID\_JPEG\_COMPRESSION\_QUALITY (VIDEO\_CID\_JPEG\_CLASS\_BASE + 3)

341

345

[ 350](group__video__controls.md#ga3cc32750dec0096ea873ea13e83d202e)#define VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE 0x009e0900

351

[ 353](group__video__controls.md#ga41b451aace98fb81633983a413d2724f)#define VIDEO\_CID\_ANALOGUE\_GAIN (VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE + 3)

354

358

[ 363](group__video__controls.md#ga0329342731999405d1f8d6c89470dff7)#define VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE 0x009f0900

364

[ 366](group__video__controls.md#ga2142e2819c445b70d82067a3cfb193c8)#define VIDEO\_CID\_LINK\_FREQ (VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE + 1)

367

[ 369](group__video__controls.md#ga6f6eaed7defdbb5f440874c7c6d0a6eb)#define VIDEO\_CID\_PIXEL\_RATE (VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE + 2)

370

[ 372](group__video__controls.md#gad1ce88a5c071eaeb8d5db9dc722a2cd4)#define VIDEO\_CID\_TEST\_PATTERN (VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE + 3)

373

377

[ 382](group__video__controls.md#ga05e2fe16eafe259061af62ac31dfaeca)#define VIDEO\_CID\_PRIVATE\_BASE 0x08000000

383

387

[ 392](group__video__controls.md#ga6fc7bcd4b280b4598ea3a03108881b5c)#define VIDEO\_CTRL\_FLAG\_NEXT\_CTRL 0x80000000

393

397

402

[ 410](structvideo__control.md)struct [video\_control](structvideo__control.md) {

[ 412](structvideo__control.md#a9ff5d90ec4ccb2b23dbd84c0eacdad75) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structvideo__control.md#a9ff5d90ec4ccb2b23dbd84c0eacdad75);

414 union {

[ 415](structvideo__control.md#a9068d0a2e351688a9077e607042a4ed3) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [val](structvideo__control.md#a9068d0a2e351688a9077e607042a4ed3);

[ 416](structvideo__control.md#ab0504077a3dcc37f5781a54baeb1e65f) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [val64](structvideo__control.md#ab0504077a3dcc37f5781a54baeb1e65f);

417 };

418};

419

[ 426](structvideo__ctrl__range.md)struct [video\_ctrl\_range](structvideo__ctrl__range.md) {

428 union {

[ 429](structvideo__ctrl__range.md#a0814e901d0edfcfa8be5419eb5bf063e) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [min](structvideo__ctrl__range.md#a0814e901d0edfcfa8be5419eb5bf063e);

[ 430](structvideo__ctrl__range.md#a25e816ab3403881ea1b0db70fbe736f1) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [min64](structvideo__ctrl__range.md#a25e816ab3403881ea1b0db70fbe736f1);

431 };

433 union {

[ 434](structvideo__ctrl__range.md#a3c2108ece802872716abf1672ccde5fa) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [max](structvideo__ctrl__range.md#a3c2108ece802872716abf1672ccde5fa);

[ 435](structvideo__ctrl__range.md#a7acb36bff57836f7bffd3ccbb2e4691e) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [max64](structvideo__ctrl__range.md#a7acb36bff57836f7bffd3ccbb2e4691e);

436 };

438 union {

[ 439](structvideo__ctrl__range.md#ab1ca560d28446134189cd7d585bd146a) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [step](structvideo__ctrl__range.md#ab1ca560d28446134189cd7d585bd146a);

[ 440](structvideo__ctrl__range.md#a9912a5060e6615388b5c8f013eaa3c51) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [step64](structvideo__ctrl__range.md#a9912a5060e6615388b5c8f013eaa3c51);

441 };

445 union {

[ 446](structvideo__ctrl__range.md#ac41aad65e524036c1f01f164726dc209) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [def](structvideo__ctrl__range.md#ac41aad65e524036c1f01f164726dc209);

[ 447](structvideo__ctrl__range.md#a9f339e7fce8f61b939d68421169a7030) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [def64](structvideo__ctrl__range.md#a9f339e7fce8f61b939d68421169a7030);

448 };

449};

450

[ 457](structvideo__ctrl__query.md)struct [video\_ctrl\_query](structvideo__ctrl__query.md) {

[ 459](structvideo__ctrl__query.md#aa534262295f6bf6816222d32f2b0986a) const struct [device](structdevice.md) \*[dev](structvideo__ctrl__query.md#aa534262295f6bf6816222d32f2b0986a);

[ 461](structvideo__ctrl__query.md#a9444f2b8c981e61ec1b01a498b3d5506) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structvideo__ctrl__query.md#a9444f2b8c981e61ec1b01a498b3d5506);

[ 463](structvideo__ctrl__query.md#a5a9cc00ce51abb9e3748100dc5d9403e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structvideo__ctrl__query.md#a5a9cc00ce51abb9e3748100dc5d9403e);

[ 465](structvideo__ctrl__query.md#a0b2744becc777f7465fd9981c9e639f6) const char \*[name](structvideo__ctrl__query.md#a0b2744becc777f7465fd9981c9e639f6);

[ 467](structvideo__ctrl__query.md#afc3e9b8a15e2d4eb04b17e0f7cd6a8cb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structvideo__ctrl__query.md#afc3e9b8a15e2d4eb04b17e0f7cd6a8cb);

[ 469](structvideo__ctrl__query.md#a37ac4deb89a9d5e4b30ff9293301feb5) struct [video\_ctrl\_range](structvideo__ctrl__range.md) [range](structvideo__ctrl__query.md#a37ac4deb89a9d5e4b30ff9293301feb5);

471 union {

[ 472](structvideo__ctrl__query.md#a56323de13c279c678ffcddc2ea355eea) const char \*const \*[menu](structvideo__ctrl__query.md#a56323de13c279c678ffcddc2ea355eea);

[ 473](structvideo__ctrl__query.md#ad0d74a650e83dece50ca2d46d9e5c750) const [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*[int\_menu](structvideo__ctrl__query.md#ad0d74a650e83dece50ca2d46d9e5c750);

474 };

475};

476

480

481#ifdef \_\_cplusplus

482}

483#endif

484

488

489#endif /\* ZEPHYR\_INCLUDE\_VIDEO\_H\_ \*/

[video\_exposure\_type](group__video__controls.md#ga167cf84b8f4259e6cdd333748deafaf6)

video\_exposure\_type

**Definition** video-controls.h:179

[video\_camera\_orientation](group__video__controls.md#ga1fb4e9981b362010439b9419691ac2af)

video\_camera\_orientation

**Definition** video-controls.h:303

[video\_colorfx](group__video__controls.md#ga99f4b6cf21c8baaf510fbcfccb645960)

video\_colorfx

**Definition** video-controls.h:119

[video\_power\_line\_frequency](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a)

video\_power\_line\_frequency

**Definition** video-controls.h:89

[VIDEO\_EXPOSURE\_MANUAL](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224)

@ VIDEO\_EXPOSURE\_MANUAL

**Definition** video-controls.h:181

[VIDEO\_EXPOSURE\_APERTURE\_PRIORITY](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd)

@ VIDEO\_EXPOSURE\_APERTURE\_PRIORITY

**Definition** video-controls.h:183

[VIDEO\_EXPOSURE\_AUTO](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b)

@ VIDEO\_EXPOSURE\_AUTO

**Definition** video-controls.h:180

[VIDEO\_EXPOSURE\_SHUTTER\_PRIORITY](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61)

@ VIDEO\_EXPOSURE\_SHUTTER\_PRIORITY

**Definition** video-controls.h:182

[VIDEO\_CAMERA\_ORIENTATION\_FRONT](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef)

@ VIDEO\_CAMERA\_ORIENTATION\_FRONT

Camera installed on the user-facing side of a phone/tablet/laptop device.

**Definition** video-controls.h:305

[VIDEO\_CAMERA\_ORIENTATION\_BACK](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072)

@ VIDEO\_CAMERA\_ORIENTATION\_BACK

Camera installed on the opposite side of the user.

**Definition** video-controls.h:307

[VIDEO\_CAMERA\_ORIENTATION\_EXTERNAL](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594)

@ VIDEO\_CAMERA\_ORIENTATION\_EXTERNAL

Camera sensors not directly attached to the device or that can move freely.

**Definition** video-controls.h:309

[VIDEO\_COLORFX\_ART\_FREEZE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a00faf2d7d366f0109d64568839416ccd)

@ VIDEO\_COLORFX\_ART\_FREEZE

**Definition** video-controls.h:131

[VIDEO\_COLORFX\_SKY\_BLUE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a09b5346a7431c2c0e7415037ee5a6f8b)

@ VIDEO\_COLORFX\_SKY\_BLUE

**Definition** video-controls.h:126

[VIDEO\_COLORFX\_SILHOUETTE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a1c93819be559612ccea3a2781cbb7d25)

@ VIDEO\_COLORFX\_SILHOUETTE

**Definition** video-controls.h:132

[VIDEO\_COLORFX\_SOLARIZATION](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a2f6f282e1e195bdc29aa6a351c2bc715)

@ VIDEO\_COLORFX\_SOLARIZATION

**Definition** video-controls.h:133

[VIDEO\_COLORFX\_SKIN\_WHITEN](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a3d4856179a0279a23f1597c3c0a615ef)

@ VIDEO\_COLORFX\_SKIN\_WHITEN

**Definition** video-controls.h:128

[VIDEO\_COLORFX\_SEPIA](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a483faa51fb4728b89c1a8da60b139a37)

@ VIDEO\_COLORFX\_SEPIA

**Definition** video-controls.h:122

[VIDEO\_COLORFX\_BW](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a52f62a92f6f0e158b1797719efb79735)

@ VIDEO\_COLORFX\_BW

**Definition** video-controls.h:121

[VIDEO\_COLORFX\_VIVID](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a5e77aa2b5530062aaaf1156a340e3826)

@ VIDEO\_COLORFX\_VIVID

**Definition** video-controls.h:129

[VIDEO\_COLORFX\_ANTIQUE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a71acc838d9197b671accab7763c5388b)

@ VIDEO\_COLORFX\_ANTIQUE

**Definition** video-controls.h:134

[VIDEO\_COLORFX\_SKETCH](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a789155f47a0302661a71155c1e6045fc)

@ VIDEO\_COLORFX\_SKETCH

**Definition** video-controls.h:125

[VIDEO\_COLORFX\_NONE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a9960e8b54cf9070c04664246e67f3237)

@ VIDEO\_COLORFX\_NONE

**Definition** video-controls.h:120

[VIDEO\_COLORFX\_EMBOSS](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960aae3d42f32c4f14e371343a32e8132cc0)

@ VIDEO\_COLORFX\_EMBOSS

**Definition** video-controls.h:124

[VIDEO\_COLORFX\_GRASS\_GREEN](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960abd0ddf263af2224bebe12da19711c6a1)

@ VIDEO\_COLORFX\_GRASS\_GREEN

**Definition** video-controls.h:127

[VIDEO\_COLORFX\_NEGATIVE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960ac9367e073eef47865d90ba9ae6eb98a0)

@ VIDEO\_COLORFX\_NEGATIVE

**Definition** video-controls.h:123

[VIDEO\_COLORFX\_AQUA](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960adb9e16ef9511c8eec1d6dbead4843a4c)

@ VIDEO\_COLORFX\_AQUA

**Definition** video-controls.h:130

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED

**Definition** video-controls.h:90

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO

**Definition** video-controls.h:93

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ

**Definition** video-controls.h:92

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ

**Definition** video-controls.h:91

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[video\_control](structvideo__control.md)

Video control structure.

**Definition** video-controls.h:410

[video\_control::val](structvideo__control.md#a9068d0a2e351688a9077e607042a4ed3)

int32\_t val

**Definition** video-controls.h:415

[video\_control::id](structvideo__control.md#a9ff5d90ec4ccb2b23dbd84c0eacdad75)

uint32\_t id

control id

**Definition** video-controls.h:412

[video\_control::val64](structvideo__control.md#ab0504077a3dcc37f5781a54baeb1e65f)

int64\_t val64

**Definition** video-controls.h:416

[video\_ctrl\_query](structvideo__ctrl__query.md)

**Definition** video-controls.h:457

[video\_ctrl\_query::name](structvideo__ctrl__query.md#a0b2744becc777f7465fd9981c9e639f6)

const char \* name

control name

**Definition** video-controls.h:465

[video\_ctrl\_query::range](structvideo__ctrl__query.md#a37ac4deb89a9d5e4b30ff9293301feb5)

struct video\_ctrl\_range range

control range

**Definition** video-controls.h:469

[video\_ctrl\_query::menu](structvideo__ctrl__query.md#a56323de13c279c678ffcddc2ea355eea)

const char \*const \* menu

**Definition** video-controls.h:472

[video\_ctrl\_query::type](structvideo__ctrl__query.md#a5a9cc00ce51abb9e3748100dc5d9403e)

uint32\_t type

control type

**Definition** video-controls.h:463

[video\_ctrl\_query::id](structvideo__ctrl__query.md#a9444f2b8c981e61ec1b01a498b3d5506)

uint32\_t id

control id, application needs to set this field

**Definition** video-controls.h:461

[video\_ctrl\_query::dev](structvideo__ctrl__query.md#aa534262295f6bf6816222d32f2b0986a)

const struct device \* dev

device being queried, application needs to set this field

**Definition** video-controls.h:459

[video\_ctrl\_query::int\_menu](structvideo__ctrl__query.md#ad0d74a650e83dece50ca2d46d9e5c750)

const int64\_t \* int\_menu

**Definition** video-controls.h:473

[video\_ctrl\_query::flags](structvideo__ctrl__query.md#afc3e9b8a15e2d4eb04b17e0f7cd6a8cb)

uint32\_t flags

control flags

**Definition** video-controls.h:467

[video\_ctrl\_range](structvideo__ctrl__range.md)

**Definition** video-controls.h:426

[video\_ctrl\_range::min](structvideo__ctrl__range.md#a0814e901d0edfcfa8be5419eb5bf063e)

int32\_t min

**Definition** video-controls.h:429

[video\_ctrl\_range::min64](structvideo__ctrl__range.md#a25e816ab3403881ea1b0db70fbe736f1)

int64\_t min64

**Definition** video-controls.h:430

[video\_ctrl\_range::max](structvideo__ctrl__range.md#a3c2108ece802872716abf1672ccde5fa)

int32\_t max

**Definition** video-controls.h:434

[video\_ctrl\_range::max64](structvideo__ctrl__range.md#a7acb36bff57836f7bffd3ccbb2e4691e)

int64\_t max64

**Definition** video-controls.h:435

[video\_ctrl\_range::step64](structvideo__ctrl__range.md#a9912a5060e6615388b5c8f013eaa3c51)

int64\_t step64

**Definition** video-controls.h:440

[video\_ctrl\_range::def64](structvideo__ctrl__range.md#a9f339e7fce8f61b939d68421169a7030)

int64\_t def64

**Definition** video-controls.h:447

[video\_ctrl\_range::step](structvideo__ctrl__range.md#ab1ca560d28446134189cd7d585bd146a)

int32\_t step

**Definition** video-controls.h:439

[video\_ctrl\_range::def](structvideo__ctrl__range.md#ac41aad65e524036c1f01f164726dc209)

int32\_t def

**Definition** video-controls.h:446

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video-controls.h](video-controls_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
