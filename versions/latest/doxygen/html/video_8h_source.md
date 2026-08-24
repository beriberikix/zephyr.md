---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/video_8h_source.html
original_path: doxygen/html/video_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video.h

[Go to the documentation of this file.](video_8h.md)

1

6

7/\*

8 \* Copyright (c) 2019 Linaro Limited.

9 \* Copyright 2025 NXP

10 \* Copyright (c) 2025 STMicroelectronics

11 \*

12 \* SPDX-License-Identifier: Apache-2.0

13 \*/

14#ifndef ZEPHYR\_INCLUDE\_VIDEO\_H\_

15#define ZEPHYR\_INCLUDE\_VIDEO\_H\_

16

25

26#include <[zephyr/device.h](device_8h.md)>

27#include <stddef.h>

28#include <[zephyr/kernel.h](kernel_8h.md)>

29

30#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

36/\*

37 \* Flag used by @ref video\_caps structure to indicate endpoint operates on

38 \* buffers the size of the video frame

39 \*/

[ 40](group__video__interface.md#ga59e44ec7c8132f479f1aa71e5b2c6546)#define LINE\_COUNT\_HEIGHT (-1)

41

42struct [video\_control](structvideo__control.md);

43

[ 52](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e)enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) {

[ 54](group__video__interface.md#ggad386b2994b56844ebe713f156b9dfe4ea20b003de365a7e2c32bba889ae78a3a1) [VIDEO\_BUF\_TYPE\_INPUT](group__video__interface.md#ggad386b2994b56844ebe713f156b9dfe4ea20b003de365a7e2c32bba889ae78a3a1),

[ 56](group__video__interface.md#ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083) [VIDEO\_BUF\_TYPE\_OUTPUT](group__video__interface.md#ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083),

57};

58

[ 65](structvideo__format.md)struct [video\_format](structvideo__format.md) {

[ 67](structvideo__format.md#a233841606bfe82626f94906bf47f5f87) enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) [type](structvideo__format.md#a233841606bfe82626f94906bf47f5f87);

[ 69](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pixelformat](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef);

[ 71](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693);

[ 73](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0);

[ 81](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pitch](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6);

82};

83

[ 90](structvideo__format__cap.md)struct [video\_format\_cap](structvideo__format__cap.md) {

[ 92](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pixelformat](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59);

[ 94](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width\_min](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9);

[ 96](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width\_max](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66);

[ 98](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height\_min](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35);

[ 100](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height\_max](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f);

[ 102](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [width\_step](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad);

[ 104](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [height\_step](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e);

105};

106

[ 113](structvideo__caps.md)struct [video\_caps](structvideo__caps.md) {

[ 115](structvideo__caps.md#a31520f03f621082bbf516efce23ef1f6) enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) [type](structvideo__caps.md#a31520f03f621082bbf516efce23ef1f6);

[ 117](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185) const struct [video\_format\_cap](structvideo__format__cap.md) \*[format\_caps](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185);

[ 121](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_vbuf\_count](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a);

[ 130](structvideo__caps.md#a3ab95e55cd093f2414937a1916ef7f52) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [min\_line\_count](structvideo__caps.md#a3ab95e55cd093f2414937a1916ef7f52);

[ 137](structvideo__caps.md#a51a059da1f30cac333ad6aad4c37d739) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [max\_line\_count](structvideo__caps.md#a51a059da1f30cac333ad6aad4c37d739);

138};

139

[ 146](structvideo__buffer.md)struct [video\_buffer](structvideo__buffer.md) {

148 /\* It must be kept as first field of the struct if used for @ref k\_fifo APIs. \*/

[ 149](structvideo__buffer.md#ab184d528487042650af105eb7d37381e) void \*[driver\_data](structvideo__buffer.md#ab184d528487042650af105eb7d37381e);

[ 151](structvideo__buffer.md#a46dd9bd9398ff74e4f9859a07b9c48af) enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) [type](structvideo__buffer.md#a46dd9bd9398ff74e4f9859a07b9c48af);

[ 153](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3);

[ 155](structvideo__buffer.md#acb948f9f124f9f2bfe9b19b44af60854) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [index](structvideo__buffer.md#acb948f9f124f9f2bfe9b19b44af60854);

[ 157](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b);

[ 159](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bytesused](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1);

[ 164](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba);

[ 170](structvideo__buffer.md#abe25963ea5e42d6fe42de1f21b554b87) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [line\_offset](structvideo__buffer.md#abe25963ea5e42d6fe42de1f21b554b87);

171};

172

[ 178](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1)enum [video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1) {

[ 180](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4) [VIDEO\_FRMIVAL\_TYPE\_DISCRETE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4) = 1,

[ 182](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b) [VIDEO\_FRMIVAL\_TYPE\_STEPWISE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b) = 2,

183};

184

[ 191](structvideo__frmival.md)struct [video\_frmival](structvideo__frmival.md) {

[ 193](structvideo__frmival.md#a57ee282f01da0f1ef1db2558d777631c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [numerator](structvideo__frmival.md#a57ee282f01da0f1ef1db2558d777631c);

[ 195](structvideo__frmival.md#aba4a6700ea733c3b07ee6445856c580a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [denominator](structvideo__frmival.md#aba4a6700ea733c3b07ee6445856c580a);

196};

197

[ 204](structvideo__frmival__stepwise.md)struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) {

[ 206](structvideo__frmival__stepwise.md#aec892104241a9d4204c87af51765ee2f) struct [video\_frmival](structvideo__frmival.md) [min](structvideo__frmival__stepwise.md#aec892104241a9d4204c87af51765ee2f);

[ 208](structvideo__frmival__stepwise.md#af1c5a40da9fe7ad30185464eccf5b438) struct [video\_frmival](structvideo__frmival.md) [max](structvideo__frmival__stepwise.md#af1c5a40da9fe7ad30185464eccf5b438);

[ 210](structvideo__frmival__stepwise.md#afc3c4e4fe3641952c4e6fc494fa85760) struct [video\_frmival](structvideo__frmival.md) [step](structvideo__frmival__stepwise.md#afc3c4e4fe3641952c4e6fc494fa85760);

211};

212

[ 219](structvideo__frmival__enum.md)struct [video\_frmival\_enum](structvideo__frmival__enum.md) {

[ 221](structvideo__frmival__enum.md#a7654ce36fd942885b193da57579d88ed) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [index](structvideo__frmival__enum.md#a7654ce36fd942885b193da57579d88ed);

[ 223](structvideo__frmival__enum.md#a8c103777cd5db24a2197ef994b8d008d) const struct [video\_format](structvideo__format.md) \*[format](structvideo__frmival__enum.md#a8c103777cd5db24a2197ef994b8d008d);

[ 225](structvideo__frmival__enum.md#aec62b54ed1152d6b3ea80c24ce7624f7) enum [video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1) [type](structvideo__frmival__enum.md#aec62b54ed1152d6b3ea80c24ce7624f7);

227 union {

[ 228](structvideo__frmival__enum.md#af22ef303cdc75fd48b698ff72b57354c) struct [video\_frmival](structvideo__frmival.md) [discrete](structvideo__frmival__enum.md#af22ef303cdc75fd48b698ff72b57354c);

[ 229](structvideo__frmival__enum.md#aa3fda4e99646bff1d902198437982124) struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) [stepwise](structvideo__frmival__enum.md#aa3fda4e99646bff1d902198437982124);

230 };

231};

232

[ 238](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8)enum [video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8) {

[ 239](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8) [VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8),

[ 240](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8) [VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8),

[ 241](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3) [VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3),

242};

243

[ 250](group__video__interface.md#gae375c0586e3505632cc69348935c9b54)enum [video\_selection\_target](structvideo__selection__target.md) {

[ 252](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17) [VIDEO\_SEL\_TGT\_CROP](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17),

[ 254](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54ab1b1302e553daefb9c1017e0bed9d8f1) [VIDEO\_SEL\_TGT\_CROP\_BOUND](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54ab1b1302e553daefb9c1017e0bed9d8f1),

[ 256](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a7536f3626e44f03775f09a1813ec8b20) [VIDEO\_SEL\_TGT\_NATIVE\_SIZE](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a7536f3626e44f03775f09a1813ec8b20),

[ 258](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49) [VIDEO\_SEL\_TGT\_COMPOSE](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49),

[ 260](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a038df16bad455f389f5c24fc91c8bd4f) [VIDEO\_SEL\_TGT\_COMPOSE\_BOUND](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a038df16bad455f389f5c24fc91c8bd4f),

261};

262

[ 269](structvideo__rect.md)struct [video\_rect](structvideo__rect.md) {

[ 271](structvideo__rect.md#a94da5de0a4cc682556acd00fc05a8ea5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [left](structvideo__rect.md#a94da5de0a4cc682556acd00fc05a8ea5);

[ 273](structvideo__rect.md#a769fd3843bcb11211eccdd766d09d83a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [top](structvideo__rect.md#a769fd3843bcb11211eccdd766d09d83a);

[ 275](structvideo__rect.md#a26403179cc6d65ff6c07a4b31b1a5050) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width](structvideo__rect.md#a26403179cc6d65ff6c07a4b31b1a5050);

[ 277](structvideo__rect.md#a57d79483c9fc9bd800437160bd30664d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height](structvideo__rect.md#a57d79483c9fc9bd800437160bd30664d);

278};

279

[ 286](structvideo__selection.md)struct [video\_selection](structvideo__selection.md) {

[ 288](structvideo__selection.md#aec9dd0ae07f995f490ebdd86d48c1a63) enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) [type](structvideo__selection.md#aec9dd0ae07f995f490ebdd86d48c1a63);

[ 290](structvideo__selection.md#afe358118a1d3c373888674f331dd05f1) enum [video\_selection\_target](group__video__interface.md#gae375c0586e3505632cc69348935c9b54) [target](structvideo__selection.md#afe358118a1d3c373888674f331dd05f1);

[ 292](structvideo__selection.md#a2e634792c0758a3dd576e4871c250bd2) struct [video\_rect](structvideo__rect.md) [rect](structvideo__selection.md#a2e634792c0758a3dd576e4871c250bd2);

293};

294

[ 301](group__video__interface.md#ga964b301e45a42aa78799a1d9c9297ab1)typedef int (\*[video\_api\_format\_t](group__video__interface.md#ga964b301e45a42aa78799a1d9c9297ab1))(const struct [device](structdevice.md) \*dev, struct [video\_format](structvideo__format.md) \*fmt);

302

[ 309](group__video__interface.md#gaf63180944041a9e934c9f7567bdc1b88)typedef int (\*[video\_api\_frmival\_t](group__video__interface.md#gaf63180944041a9e934c9f7567bdc1b88))(const struct [device](structdevice.md) \*dev, struct [video\_frmival](structvideo__frmival.md) \*frmival);

310

[ 317](group__video__interface.md#ga026c9a4531a125339e69b81f75343555)typedef int (\*[video\_api\_enum\_frmival\_t](group__video__interface.md#ga026c9a4531a125339e69b81f75343555))(const struct [device](structdevice.md) \*dev, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie);

318

[ 325](group__video__interface.md#gae6849a22140b3507bab219b579bc3d40)typedef int (\*[video\_api\_enqueue\_t](group__video__interface.md#gae6849a22140b3507bab219b579bc3d40))(const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*buf);

326

[ 333](group__video__interface.md#ga4265087c8faf62bbc36e88c0587022a1)typedef int (\*[video\_api\_dequeue\_t](group__video__interface.md#ga4265087c8faf62bbc36e88c0587022a1))(const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*\*buf,

334 [k\_timeout\_t](structk__timeout__t.md) timeout);

335

[ 343](group__video__interface.md#ga990ba001531c7300a06ca02d64c31eaa)typedef int (\*[video\_api\_flush\_t](group__video__interface.md#ga990ba001531c7300a06ca02d64c31eaa))(const struct [device](structdevice.md) \*dev, bool cancel);

344

[ 357](group__video__interface.md#gacda90bacb17a53e0bd11e5bfd37be57a)typedef int (\*[video\_api\_set\_stream\_t](group__video__interface.md#gacda90bacb17a53e0bd11e5bfd37be57a))(const struct [device](structdevice.md) \*dev, bool enable,

358 enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) type);

359

[ 367](group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303)typedef int (\*[video\_api\_ctrl\_t](group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cid);

368

[ 375](group__video__interface.md#ga070cb5f5bf35b98e2e7dda3378114780)typedef int (\*[video\_api\_get\_caps\_t](group__video__interface.md#ga070cb5f5bf35b98e2e7dda3378114780))(const struct [device](structdevice.md) \*dev, struct [video\_caps](structvideo__caps.md) \*caps);

376

[ 383](group__video__interface.md#gad5aacb1386785a3587d41844c7854f83)typedef int (\*[video\_api\_set\_signal\_t](group__video__interface.md#gad5aacb1386785a3587d41844c7854f83))(const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*sig);

384

[ 391](group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a)typedef int (\*[video\_api\_selection\_t](group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a))(const struct [device](structdevice.md) \*dev, struct [video\_selection](structvideo__selection.md) \*sel);

392

[ 393](structvideo__driver__api.md)\_\_subsystem struct [video\_driver\_api](structvideo__driver__api.md) {

394 /\* mandatory callbacks \*/

[ 395](structvideo__driver__api.md#a1859e3a1db99d97c38ea24f2f9cd00be) [video\_api\_format\_t](group__video__interface.md#ga964b301e45a42aa78799a1d9c9297ab1) [set\_format](structvideo__driver__api.md#a1859e3a1db99d97c38ea24f2f9cd00be);

[ 396](structvideo__driver__api.md#a8daefeec3cfc01de56f0168b32cdb640) [video\_api\_format\_t](group__video__interface.md#ga964b301e45a42aa78799a1d9c9297ab1) [get\_format](structvideo__driver__api.md#a8daefeec3cfc01de56f0168b32cdb640);

[ 397](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04) [video\_api\_set\_stream\_t](group__video__interface.md#gacda90bacb17a53e0bd11e5bfd37be57a) [set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04);

[ 398](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078) [video\_api\_get\_caps\_t](group__video__interface.md#ga070cb5f5bf35b98e2e7dda3378114780) [get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078);

399 /\* optional callbacks \*/

[ 400](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75) [video\_api\_enqueue\_t](group__video__interface.md#gae6849a22140b3507bab219b579bc3d40) [enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75);

[ 401](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef) [video\_api\_dequeue\_t](group__video__interface.md#ga4265087c8faf62bbc36e88c0587022a1) [dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef);

[ 402](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6) [video\_api\_flush\_t](group__video__interface.md#ga990ba001531c7300a06ca02d64c31eaa) [flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6);

[ 403](structvideo__driver__api.md#a41cd20fbb013bdb6b28d79822733695c) [video\_api\_ctrl\_t](group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303) [set\_ctrl](structvideo__driver__api.md#a41cd20fbb013bdb6b28d79822733695c);

[ 404](structvideo__driver__api.md#af50329fd41db78f4c5a945f57a7c091e) [video\_api\_ctrl\_t](group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303) [get\_volatile\_ctrl](structvideo__driver__api.md#af50329fd41db78f4c5a945f57a7c091e);

[ 405](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2) [video\_api\_set\_signal\_t](group__video__interface.md#gad5aacb1386785a3587d41844c7854f83) [set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2);

[ 406](structvideo__driver__api.md#ac4b155a56c07bd8f7ecff9ec75dd0792) [video\_api\_frmival\_t](group__video__interface.md#gaf63180944041a9e934c9f7567bdc1b88) [set\_frmival](structvideo__driver__api.md#ac4b155a56c07bd8f7ecff9ec75dd0792);

[ 407](structvideo__driver__api.md#abddf2db6034d10f76ac90ed5974df788) [video\_api\_frmival\_t](group__video__interface.md#gaf63180944041a9e934c9f7567bdc1b88) [get\_frmival](structvideo__driver__api.md#abddf2db6034d10f76ac90ed5974df788);

[ 408](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726) [video\_api\_enum\_frmival\_t](group__video__interface.md#ga026c9a4531a125339e69b81f75343555) [enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726);

[ 409](structvideo__driver__api.md#a800a2e8aaf59fc3fbd4bd2caaaf40f51) [video\_api\_selection\_t](group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a) [set\_selection](structvideo__driver__api.md#a800a2e8aaf59fc3fbd4bd2caaaf40f51);

[ 410](structvideo__driver__api.md#a6ad8559ae0c2f6dc102e26e3714ded5d) [video\_api\_selection\_t](group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a) [get\_selection](structvideo__driver__api.md#a6ad8559ae0c2f6dc102e26e3714ded5d);

411};

412

[ 426](group__video__interface.md#gab93c2cb09bf5b0629b665cc4a079e3cd)static inline int [video\_set\_format](group__video__interface.md#gab93c2cb09bf5b0629b665cc4a079e3cd)(const struct [device](structdevice.md) \*dev, struct [video\_format](structvideo__format.md) \*fmt)

427{

428 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

429

430 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

431 \_\_ASSERT\_NO\_MSG(fmt != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

432

433 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

434 if (api->[set\_format](structvideo__driver__api.md#a1859e3a1db99d97c38ea24f2f9cd00be) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

435 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

436 }

437

438 return api->[set\_format](structvideo__driver__api.md#a1859e3a1db99d97c38ea24f2f9cd00be)(dev, fmt);

439}

440

[ 451](group__video__interface.md#gad4a5849af21d20197169f0557329fdc1)static inline int [video\_get\_format](group__video__interface.md#gad4a5849af21d20197169f0557329fdc1)(const struct [device](structdevice.md) \*dev, struct [video\_format](structvideo__format.md) \*fmt)

452{

453 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

454

455 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

456 \_\_ASSERT\_NO\_MSG(fmt != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

457

458 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

459 if (api->[get\_format](structvideo__driver__api.md#a8daefeec3cfc01de56f0168b32cdb640) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

460 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

461 }

462

463 return api->[get\_format](structvideo__driver__api.md#a8daefeec3cfc01de56f0168b32cdb640)(dev, fmt);

464}

465

[ 482](group__video__interface.md#gac7a047582183dcdc4fed58ef9b9b4a84)static inline int [video\_set\_frmival](group__video__interface.md#gac7a047582183dcdc4fed58ef9b9b4a84)(const struct [device](structdevice.md) \*dev, struct [video\_frmival](structvideo__frmival.md) \*frmival)

483{

484 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

485

486 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

487 \_\_ASSERT\_NO\_MSG(frmival != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

488

489 if (frmival->[numerator](structvideo__frmival.md#a57ee282f01da0f1ef1db2558d777631c) == 0 || frmival->[denominator](structvideo__frmival.md#aba4a6700ea733c3b07ee6445856c580a) == 0) {

490 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

491 }

492

493 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

494 if (api->[set\_frmival](structvideo__driver__api.md#ac4b155a56c07bd8f7ecff9ec75dd0792) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

495 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

496 }

497

498 return api->[set\_frmival](structvideo__driver__api.md#ac4b155a56c07bd8f7ecff9ec75dd0792)(dev, frmival);

499}

500

[ 514](group__video__interface.md#gaf5a5bcd6e05d38a55a296b8290c3e0aa)static inline int [video\_get\_frmival](group__video__interface.md#gaf5a5bcd6e05d38a55a296b8290c3e0aa)(const struct [device](structdevice.md) \*dev, struct [video\_frmival](structvideo__frmival.md) \*frmival)

515{

516 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

517

518 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

519 \_\_ASSERT\_NO\_MSG(frmival != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

520

521 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

522 if (api->[get\_frmival](structvideo__driver__api.md#abddf2db6034d10f76ac90ed5974df788) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

523 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

524 }

525

526 return api->[get\_frmival](structvideo__driver__api.md#abddf2db6034d10f76ac90ed5974df788)(dev, frmival);

527}

528

[ 546](group__video__interface.md#ga8141d7cb665fd975c4f852e40ba408e8)static inline int [video\_enum\_frmival](group__video__interface.md#ga8141d7cb665fd975c4f852e40ba408e8)(const struct [device](structdevice.md) \*dev, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie)

547{

548 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

549

550 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

551 \_\_ASSERT\_NO\_MSG(fie != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

552 \_\_ASSERT\_NO\_MSG(fie->[format](structvideo__frmival__enum.md#a8c103777cd5db24a2197ef994b8d008d) != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

553

554 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

555 if (api->[enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

556 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

557 }

558

559 return api->[enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726)(dev, fie);

560}

561

[ 575](group__video__interface.md#gaca3d87049c7631f2edbbb673da94836a)static inline int [video\_enqueue](group__video__interface.md#gaca3d87049c7631f2edbbb673da94836a)(const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*buf)

576{

577 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

578

579 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

580 \_\_ASSERT\_NO\_MSG(buf != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

581 \_\_ASSERT\_NO\_MSG(buf->[buffer](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3) != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

582

583 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

584 if (api->[enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

585 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

586 }

587

588 return api->[enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75)(dev, buf);

589}

590

[ 605](group__video__interface.md#ga45967c58a8cb6c18eac5b3ee3f1061f1)static inline int [video\_dequeue](group__video__interface.md#ga45967c58a8cb6c18eac5b3ee3f1061f1)(const struct [device](structdevice.md) \*dev, struct [video\_buffer](structvideo__buffer.md) \*\*buf,

606 [k\_timeout\_t](structk__timeout__t.md) timeout)

607{

608 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

609

610 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

611 \_\_ASSERT\_NO\_MSG(buf != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

612

613 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

614 if (api->[dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

615 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

616 }

617

618 return api->[dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef)(dev, buf, timeout);

619}

620

[ 634](group__video__interface.md#gaa670ffe1b3025ac48f132b4cac89693b)static inline int [video\_flush](group__video__interface.md#gaa670ffe1b3025ac48f132b4cac89693b)(const struct [device](structdevice.md) \*dev, bool cancel)

635{

636 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

637

638 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

639

640 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

641 if (api->[flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

642 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

643 }

644

645 return api->[flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6)(dev, cancel);

646}

647

[ 663](group__video__interface.md#ga835bb485fcf906cc5b27529a0fe218d3)static inline int [video\_stream\_start](group__video__interface.md#ga835bb485fcf906cc5b27529a0fe218d3)(const struct [device](structdevice.md) \*dev, enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) type)

664{

665 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

666

667 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

668

669 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

670 if (api->[set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

671 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

672 }

673

674 return api->[set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04)(dev, true, type);

675}

676

[ 689](group__video__interface.md#gaa8965272b3f2a7f6692b56ff569f190f)static inline int [video\_stream\_stop](group__video__interface.md#gaa8965272b3f2a7f6692b56ff569f190f)(const struct [device](structdevice.md) \*dev, enum [video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) type)

690{

691 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

692 int ret;

693

694 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

695

696 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

697 if (api->[set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

698 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

699 }

700

701 ret = api->[set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04)(dev, false, type);

702 [video\_flush](group__video__interface.md#gaa670ffe1b3025ac48f132b4cac89693b)(dev, true);

703

704 return ret;

705}

706

[ 715](group__video__interface.md#ga903c7fff276274c9f3a9ac88be02cba2)static inline int [video\_get\_caps](group__video__interface.md#ga903c7fff276274c9f3a9ac88be02cba2)(const struct [device](structdevice.md) \*dev, struct [video\_caps](structvideo__caps.md) \*caps)

716{

717 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

718

719 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

720 \_\_ASSERT\_NO\_MSG(caps != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

721

722 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

723 if (api->[get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

724 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

725 }

726

727 return api->[get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078)(dev, caps);

728}

729

[ 744](group__video__interface.md#ga1cce17a3dfc881a1080708c7bc417aac)int [video\_set\_ctrl](group__video__interface.md#ga1cce17a3dfc881a1080708c7bc417aac)(const struct [device](structdevice.md) \*dev, struct [video\_control](structvideo__control.md) \*control);

745

[ 760](group__video__interface.md#ga71853c720e6df1def4c945e23d103298)int [video\_get\_ctrl](group__video__interface.md#ga71853c720e6df1def4c945e23d103298)(const struct [device](structdevice.md) \*dev, struct [video\_control](structvideo__control.md) \*control);

761

762struct [video\_ctrl\_query](structvideo__ctrl__query.md);

763

[ 782](group__video__interface.md#ga8813a656a66adc6bfb10fb7f27194898)int [video\_query\_ctrl](group__video__interface.md#ga8813a656a66adc6bfb10fb7f27194898)(struct [video\_ctrl\_query](structvideo__ctrl__query.md) \*cq);

783

[ 793](group__video__interface.md#ga2bff04c6abc344350d6b0036289a701e)void [video\_print\_ctrl](group__video__interface.md#ga2bff04c6abc344350d6b0036289a701e)(const struct [video\_ctrl\_query](structvideo__ctrl__query.md) \*const cq);

794

[ 807](group__video__interface.md#gac67404c76cbd6183aee59f3b8243652b)static inline int [video\_set\_signal](group__video__interface.md#gac67404c76cbd6183aee59f3b8243652b)(const struct [device](structdevice.md) \*[dev](structvideo__ctrl__query.md#aa534262295f6bf6816222d32f2b0986a), struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

808{

809 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

810

811 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

812 \_\_ASSERT\_NO\_MSG(sig != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

813

814 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

815 if (api->[set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

816 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

817 }

818

819 return api->[set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2)(dev, sig);

820}

821

[ 841](group__video__interface.md#ga21f2e7d6b5ec0c50ceeee580c6272613)static inline int [video\_set\_selection](group__video__interface.md#ga21f2e7d6b5ec0c50ceeee580c6272613)(const struct [device](structdevice.md) \*dev, struct [video\_selection](structvideo__selection.md) \*sel)

842{

843 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

844

845 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

846 \_\_ASSERT\_NO\_MSG(sel != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

847

848 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

849 if (api->[set\_selection](structvideo__driver__api.md#a800a2e8aaf59fc3fbd4bd2caaaf40f51) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

850 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

851 }

852

853 return api->[set\_selection](structvideo__driver__api.md#a800a2e8aaf59fc3fbd4bd2caaaf40f51)(dev, sel);

854}

855

[ 873](group__video__interface.md#ga917889d41696ab12c92475b85caec13f)static inline int [video\_get\_selection](group__video__interface.md#ga917889d41696ab12c92475b85caec13f)(const struct [device](structdevice.md) \*dev, struct [video\_selection](structvideo__selection.md) \*sel)

874{

875 const struct [video\_driver\_api](structvideo__driver__api.md) \*api;

876

877 \_\_ASSERT\_NO\_MSG(dev != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

878 \_\_ASSERT\_NO\_MSG(sel != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

879

880 api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

881 if (api->[get\_selection](structvideo__driver__api.md#a6ad8559ae0c2f6dc102e26e3714ded5d) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

882 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

883 }

884

885 return api->[get\_selection](structvideo__driver__api.md#a6ad8559ae0c2f6dc102e26e3714ded5d)(dev, sel);

886}

887

[ 897](group__video__interface.md#ga195914c7f03f2241702c77d41d1ab750)struct [video\_buffer](structvideo__buffer.md) \*[video\_buffer\_aligned\_alloc](group__video__interface.md#ga195914c7f03f2241702c77d41d1ab750)(size\_t [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b), size\_t align, [k\_timeout\_t](structk__timeout__t.md) timeout);

898

[ 907](group__video__interface.md#gaee6eb26310a40d3f18161b3567f9e0a9)struct [video\_buffer](structvideo__buffer.md) \*[video\_buffer\_alloc](group__video__interface.md#gaee6eb26310a40d3f18161b3567f9e0a9)(size\_t [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b), [k\_timeout\_t](structk__timeout__t.md) timeout);

908

[ 914](group__video__interface.md#gad2661653db019b673153001b2c61b10f)void [video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f)(struct [video\_buffer](structvideo__buffer.md) \*buf);

915

[ 926](group__video__interface.md#gadbf59fd2d77b3d164cacf56bd4ae81ce)int [video\_format\_caps\_index](group__video__interface.md#gadbf59fd2d77b3d164cacf56bd4ae81ce)(const struct [video\_format\_cap](structvideo__format__cap.md) \*fmts, const struct [video\_format](structvideo__format.md) \*fmt,

927 size\_t \*idx);

928

[ 936](group__video__interface.md#ga6b3c7456b2527cc441a100ff50787dc2)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [video\_frmival\_nsec](group__video__interface.md#ga6b3c7456b2527cc441a100ff50787dc2)(const struct [video\_frmival](structvideo__frmival.md) \*frmival)

937{

938 \_\_ASSERT\_NO\_MSG(frmival != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

939 \_\_ASSERT\_NO\_MSG(frmival->[denominator](structvideo__frmival.md#aba4a6700ea733c3b07ee6445856c580a) != 0);

940

941 return ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) \* frmival->[numerator](structvideo__frmival.md#a57ee282f01da0f1ef1db2558d777631c) / frmival->[denominator](structvideo__frmival.md#aba4a6700ea733c3b07ee6445856c580a);

942}

943

[ 951](group__video__interface.md#gad11314e82e9207449b3c0b29fdc830d0)void [video\_closest\_frmival\_stepwise](group__video__interface.md#gad11314e82e9207449b3c0b29fdc830d0)(const struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) \*stepwise,

952 const struct [video\_frmival](structvideo__frmival.md) \*desired,

953 struct [video\_frmival](structvideo__frmival.md) \*match);

954

[ 972](group__video__interface.md#gaeeb67898719f094787d4157e8ce13209)void [video\_closest\_frmival](group__video__interface.md#gaeeb67898719f094787d4157e8ce13209)(const struct [device](structdevice.md) \*dev, struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*match);

973

[ 989](group__video__interface.md#ga41e450607b4dc062fac682728ec7a79d)[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [video\_get\_csi\_link\_freq](group__video__interface.md#ga41e450607b4dc062fac682728ec7a79d)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bpp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lane\_nb);

990

998

[ 1002](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)#define VIDEO\_FOURCC(a, b, c, d) \

1003 ((uint32\_t)(a) | ((uint32\_t)(b) << 8) | ((uint32\_t)(c) << 16) | ((uint32\_t)(d) << 24))

1004

[ 1014](group__video__pixel__formats.md#gafc6c4cb871f15464f2b7df86d91fd8f3)#define VIDEO\_FOURCC\_FROM\_STR(str) VIDEO\_FOURCC((str)[0], (str)[1], (str)[2], (str)[3])

1015

[ 1025](group__video__pixel__formats.md#gacd3805f57633c3db8c6adcd87384bd5c)#define VIDEO\_FOURCC\_TO\_STR(fourcc) \

1026 ((char[]){ \

1027 (char)((fourcc) & 0xFF), \

1028 (char)(((fourcc) >> 8) & 0xFF), \

1029 (char)(((fourcc) >> 16) & 0xFF), \

1030 (char)(((fourcc) >> 24) & 0xFF), \

1031 '\0' \

1032 })

1033

1047

[ 1055](group__video__pixel__formats.md#gabc0205ce5c6426051fdec88d92f123e3)#define VIDEO\_PIX\_FMT\_SBGGR8 VIDEO\_FOURCC('B', 'A', '8', '1')

1056

[ 1064](group__video__pixel__formats.md#gaa9edb9c562fc3c86b61e071970fae60d)#define VIDEO\_PIX\_FMT\_SGBRG8 VIDEO\_FOURCC('G', 'B', 'R', 'G')

1065

[ 1073](group__video__pixel__formats.md#ga19d8dc905695229097dffe659f2a806e)#define VIDEO\_PIX\_FMT\_SGRBG8 VIDEO\_FOURCC('G', 'R', 'B', 'G')

1074

[ 1082](group__video__pixel__formats.md#gabf0dde810e75d37823891ed03811482c)#define VIDEO\_PIX\_FMT\_SRGGB8 VIDEO\_FOURCC('R', 'G', 'G', 'B')

1083

[ 1091](group__video__pixel__formats.md#ga3751a8dce1c7459df06f83cd09449b5d)#define VIDEO\_PIX\_FMT\_SBGGR10P VIDEO\_FOURCC('p', 'B', 'A', 'A')

1092

[ 1100](group__video__pixel__formats.md#gad69ab9041428488051bdb45f42ad4271)#define VIDEO\_PIX\_FMT\_SGBRG10P VIDEO\_FOURCC('p', 'G', 'A', 'A')

1101

[ 1109](group__video__pixel__formats.md#gaa28c6306a3ed44a0e50c16e0eac86688)#define VIDEO\_PIX\_FMT\_SGRBG10P VIDEO\_FOURCC('p', 'g', 'A', 'A')

1110

[ 1118](group__video__pixel__formats.md#ga604d2f3501407546aa924e2fdb37be2f)#define VIDEO\_PIX\_FMT\_SRGGB10P VIDEO\_FOURCC('p', 'R', 'A', 'A')

1119

[ 1127](group__video__pixel__formats.md#gab5b5375f050d039e05032c77ac838b31)#define VIDEO\_PIX\_FMT\_SBGGR12P VIDEO\_FOURCC('p', 'B', 'C', 'C')

1128

[ 1136](group__video__pixel__formats.md#gaecedece3398a6e2f62c20c2eb3f6d3c2)#define VIDEO\_PIX\_FMT\_SGBRG12P VIDEO\_FOURCC('p', 'G', 'C', 'C')

1137

[ 1145](group__video__pixel__formats.md#ga02d91ebf4b5150d5fa437bb3a7a6e872)#define VIDEO\_PIX\_FMT\_SGRBG12P VIDEO\_FOURCC('p', 'g', 'C', 'C')

1146

[ 1154](group__video__pixel__formats.md#ga348c15cc77c728fdac773d58341cbc1d)#define VIDEO\_PIX\_FMT\_SRGGB12P VIDEO\_FOURCC('p', 'R', 'C', 'C')

1155

[ 1163](group__video__pixel__formats.md#gac3413c36b3ce91e5658cd0f973c1f3d7)#define VIDEO\_PIX\_FMT\_SBGGR14P VIDEO\_FOURCC('p', 'B', 'E', 'E')

1164

[ 1172](group__video__pixel__formats.md#ga89eb47d1dd60794781ee91cb5ae199ad)#define VIDEO\_PIX\_FMT\_SGBRG14P VIDEO\_FOURCC('p', 'G', 'E', 'E')

1173

[ 1181](group__video__pixel__formats.md#gae06f742e31a62295d3ee16af8eec1b06)#define VIDEO\_PIX\_FMT\_SGRBG14P VIDEO\_FOURCC('p', 'g', 'E', 'E')

1182

[ 1190](group__video__pixel__formats.md#ga66646a639518285810335a70337277d7)#define VIDEO\_PIX\_FMT\_SRGGB14P VIDEO\_FOURCC('p', 'R', 'E', 'E')

1191

[ 1198](group__video__pixel__formats.md#ga0b55190a343fe891bdbb7b148e7feeae)#define VIDEO\_PIX\_FMT\_SBGGR10 VIDEO\_FOURCC('B', 'G', '1', '0')

1199

[ 1206](group__video__pixel__formats.md#ga8e0f47c16483b14b45a593e9e542a987)#define VIDEO\_PIX\_FMT\_SGBRG10 VIDEO\_FOURCC('G', 'B', '1', '0')

1207

[ 1214](group__video__pixel__formats.md#ga011cc337bc54480d1e11c3e6833ae398)#define VIDEO\_PIX\_FMT\_SGRBG10 VIDEO\_FOURCC('B', 'A', '1', '0')

1215

[ 1222](group__video__pixel__formats.md#ga249cbf808658dab777a705fd9deb2986)#define VIDEO\_PIX\_FMT\_SRGGB10 VIDEO\_FOURCC('R', 'G', '1', '0')

1223

[ 1230](group__video__pixel__formats.md#gaa2d7712f655dfcb3c74b4f4ec9941402)#define VIDEO\_PIX\_FMT\_SBGGR12 VIDEO\_FOURCC('B', 'G', '1', '2')

1231

[ 1238](group__video__pixel__formats.md#gaa3df9d0af327e609b25e050a4362c2e2)#define VIDEO\_PIX\_FMT\_SGBRG12 VIDEO\_FOURCC('G', 'B', '1', '2')

1239

[ 1246](group__video__pixel__formats.md#gaf18e6647596613e07ec3c651574b08ba)#define VIDEO\_PIX\_FMT\_SGRBG12 VIDEO\_FOURCC('B', 'A', '1', '2')

1247

[ 1254](group__video__pixel__formats.md#ga7b167f2b6a147d325a685825274cd2f2)#define VIDEO\_PIX\_FMT\_SRGGB12 VIDEO\_FOURCC('R', 'G', '1', '2')

1255

[ 1262](group__video__pixel__formats.md#ga403f40a7e15319365c6ca8f3f5f19d21)#define VIDEO\_PIX\_FMT\_SBGGR14 VIDEO\_FOURCC('B', 'G', '1', '4')

1263

[ 1270](group__video__pixel__formats.md#ga6c98a7066d7d3bdd8fce3d3651772153)#define VIDEO\_PIX\_FMT\_SGBRG14 VIDEO\_FOURCC('G', 'B', '1', '4')

1271

[ 1278](group__video__pixel__formats.md#gaf58481956952b13b071b1a68541b9c21)#define VIDEO\_PIX\_FMT\_SGRBG14 VIDEO\_FOURCC('G', 'R', '1', '4')

1279

[ 1286](group__video__pixel__formats.md#gaa6e4c240372e53db8ea3472cc456af58)#define VIDEO\_PIX\_FMT\_SRGGB14 VIDEO\_FOURCC('R', 'G', '1', '4')

1287

[ 1294](group__video__pixel__formats.md#gae096669643176203199270317dc3449d)#define VIDEO\_PIX\_FMT\_SBGGR16 VIDEO\_FOURCC('B', 'Y', 'R', '2')

1295

[ 1302](group__video__pixel__formats.md#ga7f00eb633dd312ea89097edc82dc8f0c)#define VIDEO\_PIX\_FMT\_SGBRG16 VIDEO\_FOURCC('G', 'B', '1', '6')

1303

[ 1310](group__video__pixel__formats.md#ga4269984ce806e64ba5ccd41c1429769a)#define VIDEO\_PIX\_FMT\_SGRBG16 VIDEO\_FOURCC('G', 'R', '1', '6')

1311

[ 1318](group__video__pixel__formats.md#ga4f31b5d397868e952d53022c6c8e5823)#define VIDEO\_PIX\_FMT\_SRGGB16 VIDEO\_FOURCC('R', 'G', '1', '6')

1319

1323

1335

[ 1345](group__video__pixel__formats.md#gaa3af19adaf282b83a6c16f265a4260dc)#define VIDEO\_PIX\_FMT\_GREY VIDEO\_FOURCC('G', 'R', 'E', 'Y')

1346

[ 1353](group__video__pixel__formats.md#ga502df4612995fc39e03d6de3ec675159)#define VIDEO\_PIX\_FMT\_Y10P VIDEO\_FOURCC('Y', '1', '0', 'P')

1354

[ 1362](group__video__pixel__formats.md#ga263e6553a77d00bc509c1b270efebb0b)#define VIDEO\_PIX\_FMT\_Y12P VIDEO\_FOURCC('Y', '1', '2', 'P')

1363

[ 1371](group__video__pixel__formats.md#gada0124aad9c10d403966b1e3851cd968)#define VIDEO\_PIX\_FMT\_Y14P VIDEO\_FOURCC('Y', '1', '4', 'P')

1372

[ 1381](group__video__pixel__formats.md#ga0506f2c8aa1a82f02fc9383d99b43bc3)#define VIDEO\_PIX\_FMT\_Y10 VIDEO\_FOURCC('Y', '1', '0', ' ')

1382

[ 1391](group__video__pixel__formats.md#ga166b2144cec4b4f92fadda30e81b7d22)#define VIDEO\_PIX\_FMT\_Y12 VIDEO\_FOURCC('Y', '1', '2', ' ')

1392

[ 1401](group__video__pixel__formats.md#ga7d9379f19abcbac17bad3d6359a42d9d)#define VIDEO\_PIX\_FMT\_Y14 VIDEO\_FOURCC('Y', '1', '4', ' ')

1402

[ 1411](group__video__pixel__formats.md#gaa65fe8bd917dd2fe95fa87530fc3055f)#define VIDEO\_PIX\_FMT\_Y16 VIDEO\_FOURCC('Y', '1', '6', ' ')

1412

1416

1422

[ 1432](group__video__pixel__formats.md#gaf3830004bb857fa00a14d0a1209c61a8)#define VIDEO\_PIX\_FMT\_RGB565X VIDEO\_FOURCC('R', 'G', 'B', 'R')

1433

[ 1443](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)#define VIDEO\_PIX\_FMT\_RGB565 VIDEO\_FOURCC('R', 'G', 'B', 'P')

1444

[ 1452](group__video__pixel__formats.md#gaf1f8775bbdd0508c4e21a58dfcfc362d)#define VIDEO\_PIX\_FMT\_BGR24 VIDEO\_FOURCC('B', 'G', 'R', '3')

1453

[ 1461](group__video__pixel__formats.md#ga03e6be04b23b9735c96231eebc687158)#define VIDEO\_PIX\_FMT\_RGB24 VIDEO\_FOURCC('R', 'G', 'B', '3')

1462

1468

[ 1469](group__video__pixel__formats.md#ga5cd54fb54967a80576082cadd5941670)#define VIDEO\_PIX\_FMT\_ARGB32 VIDEO\_FOURCC('B', 'A', '2', '4')

1470

1476

[ 1477](group__video__pixel__formats.md#gaffb650a5f9b2b03890283ecfe95aee04)#define VIDEO\_PIX\_FMT\_ABGR32 VIDEO\_FOURCC('A', 'R', '2', '4')

1478

1484

[ 1485](group__video__pixel__formats.md#ga8ee1e3b82eeeb02188157aa4b4b5d842)#define VIDEO\_PIX\_FMT\_RGBA32 VIDEO\_FOURCC('A', 'B', '2', '4')

1486

1492

[ 1493](group__video__pixel__formats.md#ga515e379bc7f59a8062f3e2a5980b0626)#define VIDEO\_PIX\_FMT\_BGRA32 VIDEO\_FOURCC('R', 'A', '2', '4')

1494

[ 1502](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1)#define VIDEO\_PIX\_FMT\_XRGB32 VIDEO\_FOURCC('B', 'X', '2', '4')

1503

1507

1513

[ 1522](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)#define VIDEO\_PIX\_FMT\_YUYV VIDEO\_FOURCC('Y', 'U', 'Y', 'V')

1523

[ 1529](group__video__pixel__formats.md#ga299af047675a110c109cee954f55fca6)#define VIDEO\_PIX\_FMT\_YVYU VIDEO\_FOURCC('Y', 'V', 'Y', 'U')

1530

[ 1536](group__video__pixel__formats.md#ga63c825ce5dc6c863d355195fde40acb1)#define VIDEO\_PIX\_FMT\_VYUY VIDEO\_FOURCC('V', 'Y', 'U', 'Y')

1537

[ 1543](group__video__pixel__formats.md#gadca3ee56c798cf05b63cbfc87af98ce3)#define VIDEO\_PIX\_FMT\_UYVY VIDEO\_FOURCC('U', 'Y', 'V', 'Y')

1544

[ 1552](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351)#define VIDEO\_PIX\_FMT\_XYUV32 VIDEO\_FOURCC('X', 'Y', 'U', 'V')

1553

1557

1562

[ 1566](group__video__pixel__formats.md#ga035a13c38c4f123411547e2c40d58bd2)#define VIDEO\_PIX\_FMT\_JPEG VIDEO\_FOURCC('J', 'P', 'E', 'G')

1567

1571

[ 1580](group__video__pixel__formats.md#gabdbd1b0f40af6663d81402deefdd387f)static inline unsigned int [video\_bits\_per\_pixel](group__video__pixel__formats.md#gabdbd1b0f40af6663d81402deefdd387f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pixfmt)

1581{

1582 switch (pixfmt) {

1583 case [VIDEO\_PIX\_FMT\_SBGGR8](group__video__pixel__formats.md#gabc0205ce5c6426051fdec88d92f123e3):

1584 case [VIDEO\_PIX\_FMT\_SGBRG8](group__video__pixel__formats.md#gaa9edb9c562fc3c86b61e071970fae60d):

1585 case [VIDEO\_PIX\_FMT\_SGRBG8](group__video__pixel__formats.md#ga19d8dc905695229097dffe659f2a806e):

1586 case [VIDEO\_PIX\_FMT\_SRGGB8](group__video__pixel__formats.md#gabf0dde810e75d37823891ed03811482c):

1587 case [VIDEO\_PIX\_FMT\_GREY](group__video__pixel__formats.md#gaa3af19adaf282b83a6c16f265a4260dc):

1588 return 8;

1589 case [VIDEO\_PIX\_FMT\_SBGGR10P](group__video__pixel__formats.md#ga3751a8dce1c7459df06f83cd09449b5d):

1590 case [VIDEO\_PIX\_FMT\_SGBRG10P](group__video__pixel__formats.md#gad69ab9041428488051bdb45f42ad4271):

1591 case [VIDEO\_PIX\_FMT\_SGRBG10P](group__video__pixel__formats.md#gaa28c6306a3ed44a0e50c16e0eac86688):

1592 case [VIDEO\_PIX\_FMT\_SRGGB10P](group__video__pixel__formats.md#ga604d2f3501407546aa924e2fdb37be2f):

1593 case [VIDEO\_PIX\_FMT\_Y10P](group__video__pixel__formats.md#ga502df4612995fc39e03d6de3ec675159):

1594 return 10;

1595 case [VIDEO\_PIX\_FMT\_SBGGR12P](group__video__pixel__formats.md#gab5b5375f050d039e05032c77ac838b31):

1596 case [VIDEO\_PIX\_FMT\_SGBRG12P](group__video__pixel__formats.md#gaecedece3398a6e2f62c20c2eb3f6d3c2):

1597 case [VIDEO\_PIX\_FMT\_SGRBG12P](group__video__pixel__formats.md#ga02d91ebf4b5150d5fa437bb3a7a6e872):

1598 case [VIDEO\_PIX\_FMT\_SRGGB12P](group__video__pixel__formats.md#ga348c15cc77c728fdac773d58341cbc1d):

1599 case [VIDEO\_PIX\_FMT\_Y12P](group__video__pixel__formats.md#ga263e6553a77d00bc509c1b270efebb0b):

1600 return 12;

1601 case [VIDEO\_PIX\_FMT\_SBGGR14P](group__video__pixel__formats.md#gac3413c36b3ce91e5658cd0f973c1f3d7):

1602 case [VIDEO\_PIX\_FMT\_SGBRG14P](group__video__pixel__formats.md#ga89eb47d1dd60794781ee91cb5ae199ad):

1603 case [VIDEO\_PIX\_FMT\_SGRBG14P](group__video__pixel__formats.md#gae06f742e31a62295d3ee16af8eec1b06):

1604 case [VIDEO\_PIX\_FMT\_SRGGB14P](group__video__pixel__formats.md#ga66646a639518285810335a70337277d7):

1605 case [VIDEO\_PIX\_FMT\_Y14P](group__video__pixel__formats.md#gada0124aad9c10d403966b1e3851cd968):

1606 return 14;

1607 case [VIDEO\_PIX\_FMT\_RGB565](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec):

1608 case [VIDEO\_PIX\_FMT\_YUYV](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11):

1609 case [VIDEO\_PIX\_FMT\_YVYU](group__video__pixel__formats.md#ga299af047675a110c109cee954f55fca6):

1610 case [VIDEO\_PIX\_FMT\_UYVY](group__video__pixel__formats.md#gadca3ee56c798cf05b63cbfc87af98ce3):

1611 case [VIDEO\_PIX\_FMT\_VYUY](group__video__pixel__formats.md#ga63c825ce5dc6c863d355195fde40acb1):

1612 case [VIDEO\_PIX\_FMT\_SBGGR10](group__video__pixel__formats.md#ga0b55190a343fe891bdbb7b148e7feeae):

1613 case [VIDEO\_PIX\_FMT\_SGBRG10](group__video__pixel__formats.md#ga8e0f47c16483b14b45a593e9e542a987):

1614 case [VIDEO\_PIX\_FMT\_SGRBG10](group__video__pixel__formats.md#ga011cc337bc54480d1e11c3e6833ae398):

1615 case [VIDEO\_PIX\_FMT\_SRGGB10](group__video__pixel__formats.md#ga249cbf808658dab777a705fd9deb2986):

1616 case [VIDEO\_PIX\_FMT\_SBGGR12](group__video__pixel__formats.md#gaa2d7712f655dfcb3c74b4f4ec9941402):

1617 case [VIDEO\_PIX\_FMT\_SGBRG12](group__video__pixel__formats.md#gaa3df9d0af327e609b25e050a4362c2e2):

1618 case [VIDEO\_PIX\_FMT\_SGRBG12](group__video__pixel__formats.md#gaf18e6647596613e07ec3c651574b08ba):

1619 case [VIDEO\_PIX\_FMT\_SRGGB12](group__video__pixel__formats.md#ga7b167f2b6a147d325a685825274cd2f2):

1620 case [VIDEO\_PIX\_FMT\_SBGGR14](group__video__pixel__formats.md#ga403f40a7e15319365c6ca8f3f5f19d21):

1621 case [VIDEO\_PIX\_FMT\_SGBRG14](group__video__pixel__formats.md#ga6c98a7066d7d3bdd8fce3d3651772153):

1622 case [VIDEO\_PIX\_FMT\_SGRBG14](group__video__pixel__formats.md#gaf58481956952b13b071b1a68541b9c21):

1623 case [VIDEO\_PIX\_FMT\_SRGGB14](group__video__pixel__formats.md#gaa6e4c240372e53db8ea3472cc456af58):

1624 case [VIDEO\_PIX\_FMT\_SBGGR16](group__video__pixel__formats.md#gae096669643176203199270317dc3449d):

1625 case [VIDEO\_PIX\_FMT\_SGBRG16](group__video__pixel__formats.md#ga7f00eb633dd312ea89097edc82dc8f0c):

1626 case [VIDEO\_PIX\_FMT\_SGRBG16](group__video__pixel__formats.md#ga4269984ce806e64ba5ccd41c1429769a):

1627 case [VIDEO\_PIX\_FMT\_SRGGB16](group__video__pixel__formats.md#ga4f31b5d397868e952d53022c6c8e5823):

1628 case [VIDEO\_PIX\_FMT\_Y10](group__video__pixel__formats.md#ga0506f2c8aa1a82f02fc9383d99b43bc3):

1629 case [VIDEO\_PIX\_FMT\_Y12](group__video__pixel__formats.md#ga166b2144cec4b4f92fadda30e81b7d22):

1630 case [VIDEO\_PIX\_FMT\_Y14](group__video__pixel__formats.md#ga7d9379f19abcbac17bad3d6359a42d9d):

1631 case [VIDEO\_PIX\_FMT\_Y16](group__video__pixel__formats.md#gaa65fe8bd917dd2fe95fa87530fc3055f):

1632 return 16;

1633 case [VIDEO\_PIX\_FMT\_BGR24](group__video__pixel__formats.md#gaf1f8775bbdd0508c4e21a58dfcfc362d):

1634 case [VIDEO\_PIX\_FMT\_RGB24](group__video__pixel__formats.md#ga03e6be04b23b9735c96231eebc687158):

1635 return 24;

1636 case [VIDEO\_PIX\_FMT\_XRGB32](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1):

1637 case [VIDEO\_PIX\_FMT\_XYUV32](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351):

1638 case [VIDEO\_PIX\_FMT\_ARGB32](group__video__pixel__formats.md#ga5cd54fb54967a80576082cadd5941670):

1639 case [VIDEO\_PIX\_FMT\_ABGR32](group__video__pixel__formats.md#gaffb650a5f9b2b03890283ecfe95aee04):

1640 case [VIDEO\_PIX\_FMT\_RGBA32](group__video__pixel__formats.md#ga8ee1e3b82eeeb02188157aa4b4b5d842):

1641 case [VIDEO\_PIX\_FMT\_BGRA32](group__video__pixel__formats.md#ga515e379bc7f59a8062f3e2a5980b0626):

1642 return 32;

1643 default:

1644 /\* Variable number of bits per pixel or unknown format \*/

1645 return 0;

1646 }

1647}

1648

1652

[ 1658](group__video__interface.md#ga59d6f35198b6412a9aa78c094ecfaa19)#define VIDEO\_MIPI\_CSI2\_DT\_NULL 0x10

[ 1659](group__video__interface.md#gaede52c3391311b7cf931665afdeed720)#define VIDEO\_MIPI\_CSI2\_DT\_BLANKING 0x11

[ 1660](group__video__interface.md#ga2b16d411ffcbcc7e74fa6aa2966b4b0d)#define VIDEO\_MIPI\_CSI2\_DT\_EMBEDDED\_8 0x12

[ 1661](group__video__interface.md#gab8001106ce7c91573012a895a4b3f1a8)#define VIDEO\_MIPI\_CSI2\_DT\_YUV420\_8 0x18

[ 1662](group__video__interface.md#ga65dac1b59e00cb26e9af9e39663b20f0)#define VIDEO\_MIPI\_CSI2\_DT\_YUV420\_10 0x19

[ 1663](group__video__interface.md#ga9c40ffb7a4042dd9d149e960eeddd14e)#define VIDEO\_MIPI\_CSI2\_DT\_YUV420\_CSPS\_8 0x1c

[ 1664](group__video__interface.md#gad1d445cd3b576e4c7062f0a06f8dc71e)#define VIDEO\_MIPI\_CSI2\_DT\_YUV420\_CSPS\_10 0x1d

[ 1665](group__video__interface.md#ga18dac33c3f8afd80e08d69ed78aee5a9)#define VIDEO\_MIPI\_CSI2\_DT\_YUV422\_8 0x1e

[ 1666](group__video__interface.md#ga4b530659596536d30168161139cc46fb)#define VIDEO\_MIPI\_CSI2\_DT\_YUV422\_10 0x1f

[ 1667](group__video__interface.md#ga04efc97a4dab0af7c7266ab104b8d626)#define VIDEO\_MIPI\_CSI2\_DT\_RGB444 0x20

[ 1668](group__video__interface.md#ga351c2045810bb786d8232162f47fee7d)#define VIDEO\_MIPI\_CSI2\_DT\_RGB555 0x21

[ 1669](group__video__interface.md#gad5f04e5dd3d5e0c5f67c64e28cd91c56)#define VIDEO\_MIPI\_CSI2\_DT\_RGB565 0x22

[ 1670](group__video__interface.md#gaa452375e0454fa314eb140bac3c07e67)#define VIDEO\_MIPI\_CSI2\_DT\_RGB666 0x23

[ 1671](group__video__interface.md#ga0d637375f7bf081967135139a8f6c5b6)#define VIDEO\_MIPI\_CSI2\_DT\_RGB888 0x24

[ 1672](group__video__interface.md#gad251376f21a56d05742fcb68d228a677)#define VIDEO\_MIPI\_CSI2\_DT\_RAW6 0x28

[ 1673](group__video__interface.md#ga384e8203e1bb7208a4bcb1e4931a929b)#define VIDEO\_MIPI\_CSI2\_DT\_RAW7 0x29

[ 1674](group__video__interface.md#ga6d3881edac75ba2c12185dc119311945)#define VIDEO\_MIPI\_CSI2\_DT\_RAW8 0x2a

[ 1675](group__video__interface.md#ga64a52402a6883cb1b23a5524418528a9)#define VIDEO\_MIPI\_CSI2\_DT\_RAW10 0x2b

[ 1676](group__video__interface.md#gadadb66f582b5e014336e29c1dafc3631)#define VIDEO\_MIPI\_CSI2\_DT\_RAW12 0x2c

[ 1677](group__video__interface.md#ga2ad6b8870c5dca6a8d19b1f80d83b81b)#define VIDEO\_MIPI\_CSI2\_DT\_RAW14 0x2d

1678

1679/\* User-defined Data-Type range from 0x30 to 0x37 \*/

[ 1680](group__video__interface.md#ga98885f3584261947dd2b325bf12b2f3d)#define VIDEO\_MIPI\_CSI2\_DT\_USER(n) (0x30 + (n))

1681

1685

1686#ifdef \_\_cplusplus

1687}

1688#endif

1689

1693

1694#endif /\* ZEPHYR\_INCLUDE\_VIDEO\_H\_ \*/

[device.h](device_8h.md)

[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)

#define NSEC\_PER\_SEC

number of nanoseconds per second

**Definition** clock.h:113

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[video\_api\_enum\_frmival\_t](group__video__interface.md#ga026c9a4531a125339e69b81f75343555)

int(\* video\_api\_enum\_frmival\_t)(const struct device \*dev, struct video\_frmival\_enum \*fie)

List all supported frame intervals of a given format.

**Definition** video.h:317

[video\_api\_get\_caps\_t](group__video__interface.md#ga070cb5f5bf35b98e2e7dda3378114780)

int(\* video\_api\_get\_caps\_t)(const struct device \*dev, struct video\_caps \*caps)

Get capabilities of a video endpoint.

**Definition** video.h:375

[video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8)

video\_signal\_result

video\_event enum

**Definition** video.h:238

[video\_buffer\_aligned\_alloc](group__video__interface.md#ga195914c7f03f2241702c77d41d1ab750)

struct video\_buffer \* video\_buffer\_aligned\_alloc(size\_t size, size\_t align, k\_timeout\_t timeout)

Allocate aligned video buffer.

[video\_set\_ctrl](group__video__interface.md#ga1cce17a3dfc881a1080708c7bc417aac)

int video\_set\_ctrl(const struct device \*dev, struct video\_control \*control)

Set the value of a control.

[video\_set\_selection](group__video__interface.md#ga21f2e7d6b5ec0c50ceeee580c6272613)

static int video\_set\_selection(const struct device \*dev, struct video\_selection \*sel)

Set video selection (crop/compose).

**Definition** video.h:841

[video\_print\_ctrl](group__video__interface.md#ga2bff04c6abc344350d6b0036289a701e)

void video\_print\_ctrl(const struct video\_ctrl\_query \*const cq)

Print all the information of a control.

[video\_get\_csi\_link\_freq](group__video__interface.md#ga41e450607b4dc062fac682728ec7a79d)

int64\_t video\_get\_csi\_link\_freq(const struct device \*dev, uint8\_t bpp, uint8\_t lane\_nb)

Return the link-frequency advertised by a device.

[video\_api\_dequeue\_t](group__video__interface.md#ga4265087c8faf62bbc36e88c0587022a1)

int(\* video\_api\_dequeue\_t)(const struct device \*dev, struct video\_buffer \*\*buf, k\_timeout\_t timeout)

Dequeue a buffer from the driver’s outgoing queue.

**Definition** video.h:333

[video\_dequeue](group__video__interface.md#ga45967c58a8cb6c18eac5b3ee3f1061f1)

static int video\_dequeue(const struct device \*dev, struct video\_buffer \*\*buf, k\_timeout\_t timeout)

Dequeue a video buffer.

**Definition** video.h:605

[video\_api\_ctrl\_t](group__video__interface.md#ga522b4027fc6f22bf59f4face3c97e303)

int(\* video\_api\_ctrl\_t)(const struct device \*dev, uint32\_t cid)

Set/Get a video control value.

**Definition** video.h:367

[video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1)

video\_frmival\_type

video\_frmival\_type enum

**Definition** video.h:178

[video\_frmival\_nsec](group__video__interface.md#ga6b3c7456b2527cc441a100ff50787dc2)

static uint64\_t video\_frmival\_nsec(const struct video\_frmival \*frmival)

Compute the difference between two frame intervals.

**Definition** video.h:936

[video\_get\_ctrl](group__video__interface.md#ga71853c720e6df1def4c945e23d103298)

int video\_get\_ctrl(const struct device \*dev, struct video\_control \*control)

Get the current value of a control.

[video\_enum\_frmival](group__video__interface.md#ga8141d7cb665fd975c4f852e40ba408e8)

static int video\_enum\_frmival(const struct device \*dev, struct video\_frmival\_enum \*fie)

List video frame intervals.

**Definition** video.h:546

[video\_stream\_start](group__video__interface.md#ga835bb485fcf906cc5b27529a0fe218d3)

static int video\_stream\_start(const struct device \*dev, enum video\_buf\_type type)

Start the video device function.

**Definition** video.h:663

[video\_query\_ctrl](group__video__interface.md#ga8813a656a66adc6bfb10fb7f27194898)

int video\_query\_ctrl(struct video\_ctrl\_query \*cq)

Query information about a control.

[video\_get\_caps](group__video__interface.md#ga903c7fff276274c9f3a9ac88be02cba2)

static int video\_get\_caps(const struct device \*dev, struct video\_caps \*caps)

Get the capabilities of a video endpoint.

**Definition** video.h:715

[video\_get\_selection](group__video__interface.md#ga917889d41696ab12c92475b85caec13f)

static int video\_get\_selection(const struct device \*dev, struct video\_selection \*sel)

Get video selection (crop/compose).

**Definition** video.h:873

[video\_api\_format\_t](group__video__interface.md#ga964b301e45a42aa78799a1d9c9297ab1)

int(\* video\_api\_format\_t)(const struct device \*dev, struct video\_format \*fmt)

Function pointer type for video\_set/get\_format().

**Definition** video.h:301

[video\_api\_flush\_t](group__video__interface.md#ga990ba001531c7300a06ca02d64c31eaa)

int(\* video\_api\_flush\_t)(const struct device \*dev, bool cancel)

Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue.

**Definition** video.h:343

[video\_flush](group__video__interface.md#gaa670ffe1b3025ac48f132b4cac89693b)

static int video\_flush(const struct device \*dev, bool cancel)

Flush endpoint buffers.

**Definition** video.h:634

[video\_stream\_stop](group__video__interface.md#gaa8965272b3f2a7f6692b56ff569f190f)

static int video\_stream\_stop(const struct device \*dev, enum video\_buf\_type type)

Stop the video device function.

**Definition** video.h:689

[video\_api\_selection\_t](group__video__interface.md#gab4d2eb34f8ccc95fa6dcda7848f4408a)

int(\* video\_api\_selection\_t)(const struct device \*dev, struct video\_selection \*sel)

Get/Set video selection (crop / compose).

**Definition** video.h:391

[video\_set\_format](group__video__interface.md#gab93c2cb09bf5b0629b665cc4a079e3cd)

static int video\_set\_format(const struct device \*dev, struct video\_format \*fmt)

Set video format.

**Definition** video.h:426

[video\_set\_signal](group__video__interface.md#gac67404c76cbd6183aee59f3b8243652b)

static int video\_set\_signal(const struct device \*dev, struct k\_poll\_signal \*sig)

Register/Unregister k\_poll signal for a video endpoint.

**Definition** video.h:807

[video\_set\_frmival](group__video__interface.md#gac7a047582183dcdc4fed58ef9b9b4a84)

static int video\_set\_frmival(const struct device \*dev, struct video\_frmival \*frmival)

Set video frame interval.

**Definition** video.h:482

[video\_enqueue](group__video__interface.md#gaca3d87049c7631f2edbbb673da94836a)

static int video\_enqueue(const struct device \*dev, struct video\_buffer \*buf)

Enqueue a video buffer.

**Definition** video.h:575

[video\_api\_set\_stream\_t](group__video__interface.md#gacda90bacb17a53e0bd11e5bfd37be57a)

int(\* video\_api\_set\_stream\_t)(const struct device \*dev, bool enable, enum video\_buf\_type type)

Start or stop streaming on the video device.

**Definition** video.h:357

[video\_closest\_frmival\_stepwise](group__video__interface.md#gad11314e82e9207449b3c0b29fdc830d0)

void video\_closest\_frmival\_stepwise(const struct video\_frmival\_stepwise \*stepwise, const struct video\_frmival \*desired, struct video\_frmival \*match)

Find the closest match to a frame interval value within a stepwise frame interval.

[video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f)

void video\_buffer\_release(struct video\_buffer \*buf)

Release a video buffer.

[video\_buf\_type](group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e)

video\_buf\_type

video\_buf\_type enum

**Definition** video.h:52

[video\_get\_format](group__video__interface.md#gad4a5849af21d20197169f0557329fdc1)

static int video\_get\_format(const struct device \*dev, struct video\_format \*fmt)

Get video format.

**Definition** video.h:451

[video\_api\_set\_signal\_t](group__video__interface.md#gad5aacb1386785a3587d41844c7854f83)

int(\* video\_api\_set\_signal\_t)(const struct device \*dev, struct k\_poll\_signal \*sig)

Register/Unregister poll signal for buffer events.

**Definition** video.h:383

[video\_format\_caps\_index](group__video__interface.md#gadbf59fd2d77b3d164cacf56bd4ae81ce)

int video\_format\_caps\_index(const struct video\_format\_cap \*fmts, const struct video\_format \*fmt, size\_t \*idx)

Search for a format that matches in a list of capabilities.

[video\_selection\_target](group__video__interface.md#gae375c0586e3505632cc69348935c9b54)

video\_selection\_target

**Definition** video.h:250

[video\_api\_enqueue\_t](group__video__interface.md#gae6849a22140b3507bab219b579bc3d40)

int(\* video\_api\_enqueue\_t)(const struct device \*dev, struct video\_buffer \*buf)

Enqueue a buffer in the driver’s incoming queue.

**Definition** video.h:325

[video\_buffer\_alloc](group__video__interface.md#gaee6eb26310a40d3f18161b3567f9e0a9)

struct video\_buffer \* video\_buffer\_alloc(size\_t size, k\_timeout\_t timeout)

Allocate video buffer.

[video\_closest\_frmival](group__video__interface.md#gaeeb67898719f094787d4157e8ce13209)

void video\_closest\_frmival(const struct device \*dev, struct video\_frmival\_enum \*match)

Find the closest match to a frame interval value within a video device.

[video\_get\_frmival](group__video__interface.md#gaf5a5bcd6e05d38a55a296b8290c3e0aa)

static int video\_get\_frmival(const struct device \*dev, struct video\_frmival \*frmival)

Get video frame interval.

**Definition** video.h:514

[video\_api\_frmival\_t](group__video__interface.md#gaf63180944041a9e934c9f7567bdc1b88)

int(\* video\_api\_frmival\_t)(const struct device \*dev, struct video\_frmival \*frmival)

Function pointer type for video\_set/get\_frmival().

**Definition** video.h:309

[VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8)

@ VIDEO\_BUF\_ABORTED

**Definition** video.h:240

[VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8)

@ VIDEO\_BUF\_DONE

**Definition** video.h:239

[VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3)

@ VIDEO\_BUF\_ERROR

**Definition** video.h:241

[VIDEO\_FRMIVAL\_TYPE\_DISCRETE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4)

@ VIDEO\_FRMIVAL\_TYPE\_DISCRETE

discrete frame interval type

**Definition** video.h:180

[VIDEO\_FRMIVAL\_TYPE\_STEPWISE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b)

@ VIDEO\_FRMIVAL\_TYPE\_STEPWISE

stepwise frame interval type

**Definition** video.h:182

[VIDEO\_BUF\_TYPE\_INPUT](group__video__interface.md#ggad386b2994b56844ebe713f156b9dfe4ea20b003de365a7e2c32bba889ae78a3a1)

@ VIDEO\_BUF\_TYPE\_INPUT

input buffer type

**Definition** video.h:54

[VIDEO\_BUF\_TYPE\_OUTPUT](group__video__interface.md#ggad386b2994b56844ebe713f156b9dfe4eab51085ffb7e0d7a003dcb6b55a093083)

@ VIDEO\_BUF\_TYPE\_OUTPUT

output buffer type

**Definition** video.h:56

[VIDEO\_SEL\_TGT\_COMPOSE\_BOUND](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a038df16bad455f389f5c24fc91c8bd4f)

@ VIDEO\_SEL\_TGT\_COMPOSE\_BOUND

Compose bound (aka the maximum compose achievable).

**Definition** video.h:260

[VIDEO\_SEL\_TGT\_COMPOSE](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a0558ad68bff086cd3ff3f82b53946f49)

@ VIDEO\_SEL\_TGT\_COMPOSE

Current compose setting.

**Definition** video.h:258

[VIDEO\_SEL\_TGT\_NATIVE\_SIZE](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54a7536f3626e44f03775f09a1813ec8b20)

@ VIDEO\_SEL\_TGT\_NATIVE\_SIZE

Native size of the input frame.

**Definition** video.h:256

[VIDEO\_SEL\_TGT\_CROP](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54aa42c3de3eeefb5340a2a1877ec8c4b17)

@ VIDEO\_SEL\_TGT\_CROP

Current crop setting.

**Definition** video.h:252

[VIDEO\_SEL\_TGT\_CROP\_BOUND](group__video__interface.md#ggae375c0586e3505632cc69348935c9b54ab1b1302e553daefb9c1017e0bed9d8f1)

@ VIDEO\_SEL\_TGT\_CROP\_BOUND

Crop bound (aka the maximum crop achievable).

**Definition** video.h:254

[VIDEO\_PIX\_FMT\_SGRBG10](group__video__pixel__formats.md#ga011cc337bc54480d1e11c3e6833ae398)

#define VIDEO\_PIX\_FMT\_SGRBG10

**Definition** video.h:1214

[VIDEO\_PIX\_FMT\_XYUV32](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351)

#define VIDEO\_PIX\_FMT\_XYUV32

The first byte is empty (X) for each pixel.

**Definition** video.h:1552

[VIDEO\_PIX\_FMT\_SGRBG12P](group__video__pixel__formats.md#ga02d91ebf4b5150d5fa437bb3a7a6e872)

#define VIDEO\_PIX\_FMT\_SGRBG12P

**Definition** video.h:1145

[VIDEO\_PIX\_FMT\_RGB24](group__video__pixel__formats.md#ga03e6be04b23b9735c96231eebc687158)

#define VIDEO\_PIX\_FMT\_RGB24

24 bit RGB format with 8 bit per component

**Definition** video.h:1461

[VIDEO\_PIX\_FMT\_Y10](group__video__pixel__formats.md#ga0506f2c8aa1a82f02fc9383d99b43bc3)

#define VIDEO\_PIX\_FMT\_Y10

Little endian, with the 6 most significant bits set to Zero.

**Definition** video.h:1381

[VIDEO\_PIX\_FMT\_SBGGR10](group__video__pixel__formats.md#ga0b55190a343fe891bdbb7b148e7feeae)

#define VIDEO\_PIX\_FMT\_SBGGR10

**Definition** video.h:1198

[VIDEO\_PIX\_FMT\_Y12](group__video__pixel__formats.md#ga166b2144cec4b4f92fadda30e81b7d22)

#define VIDEO\_PIX\_FMT\_Y12

Little endian, with the 4 most significant bits set to Zero.

**Definition** video.h:1391

[VIDEO\_PIX\_FMT\_SGRBG8](group__video__pixel__formats.md#ga19d8dc905695229097dffe659f2a806e)

#define VIDEO\_PIX\_FMT\_SGRBG8

**Definition** video.h:1073

[VIDEO\_PIX\_FMT\_SRGGB10](group__video__pixel__formats.md#ga249cbf808658dab777a705fd9deb2986)

#define VIDEO\_PIX\_FMT\_SRGGB10

**Definition** video.h:1222

[VIDEO\_PIX\_FMT\_Y12P](group__video__pixel__formats.md#ga263e6553a77d00bc509c1b270efebb0b)

#define VIDEO\_PIX\_FMT\_Y12P

**Definition** video.h:1362

[VIDEO\_PIX\_FMT\_YVYU](group__video__pixel__formats.md#ga299af047675a110c109cee954f55fca6)

#define VIDEO\_PIX\_FMT\_YVYU

**Definition** video.h:1529

[VIDEO\_PIX\_FMT\_SRGGB12P](group__video__pixel__formats.md#ga348c15cc77c728fdac773d58341cbc1d)

#define VIDEO\_PIX\_FMT\_SRGGB12P

**Definition** video.h:1154

[VIDEO\_PIX\_FMT\_SBGGR10P](group__video__pixel__formats.md#ga3751a8dce1c7459df06f83cd09449b5d)

#define VIDEO\_PIX\_FMT\_SBGGR10P

**Definition** video.h:1091

[VIDEO\_PIX\_FMT\_SBGGR14](group__video__pixel__formats.md#ga403f40a7e15319365c6ca8f3f5f19d21)

#define VIDEO\_PIX\_FMT\_SBGGR14

**Definition** video.h:1262

[VIDEO\_PIX\_FMT\_SGRBG16](group__video__pixel__formats.md#ga4269984ce806e64ba5ccd41c1429769a)

#define VIDEO\_PIX\_FMT\_SGRBG16

**Definition** video.h:1310

[VIDEO\_PIX\_FMT\_SRGGB16](group__video__pixel__formats.md#ga4f31b5d397868e952d53022c6c8e5823)

#define VIDEO\_PIX\_FMT\_SRGGB16

**Definition** video.h:1318

[VIDEO\_PIX\_FMT\_Y10P](group__video__pixel__formats.md#ga502df4612995fc39e03d6de3ec675159)

#define VIDEO\_PIX\_FMT\_Y10P

**Definition** video.h:1353

[VIDEO\_PIX\_FMT\_BGRA32](group__video__pixel__formats.md#ga515e379bc7f59a8062f3e2a5980b0626)

#define VIDEO\_PIX\_FMT\_BGRA32

**Definition** video.h:1493

[VIDEO\_PIX\_FMT\_ARGB32](group__video__pixel__formats.md#ga5cd54fb54967a80576082cadd5941670)

#define VIDEO\_PIX\_FMT\_ARGB32

**Definition** video.h:1469

[VIDEO\_PIX\_FMT\_SRGGB10P](group__video__pixel__formats.md#ga604d2f3501407546aa924e2fdb37be2f)

#define VIDEO\_PIX\_FMT\_SRGGB10P

**Definition** video.h:1118

[VIDEO\_PIX\_FMT\_VYUY](group__video__pixel__formats.md#ga63c825ce5dc6c863d355195fde40acb1)

#define VIDEO\_PIX\_FMT\_VYUY

**Definition** video.h:1536

[VIDEO\_PIX\_FMT\_SRGGB14P](group__video__pixel__formats.md#ga66646a639518285810335a70337277d7)

#define VIDEO\_PIX\_FMT\_SRGGB14P

**Definition** video.h:1190

[VIDEO\_PIX\_FMT\_SGBRG14](group__video__pixel__formats.md#ga6c98a7066d7d3bdd8fce3d3651772153)

#define VIDEO\_PIX\_FMT\_SGBRG14

**Definition** video.h:1270

[VIDEO\_PIX\_FMT\_SRGGB12](group__video__pixel__formats.md#ga7b167f2b6a147d325a685825274cd2f2)

#define VIDEO\_PIX\_FMT\_SRGGB12

**Definition** video.h:1254

[VIDEO\_PIX\_FMT\_Y14](group__video__pixel__formats.md#ga7d9379f19abcbac17bad3d6359a42d9d)

#define VIDEO\_PIX\_FMT\_Y14

Little endian, with the 2 most significant bits set to Zero.

**Definition** video.h:1401

[VIDEO\_PIX\_FMT\_SGBRG16](group__video__pixel__formats.md#ga7f00eb633dd312ea89097edc82dc8f0c)

#define VIDEO\_PIX\_FMT\_SGBRG16

**Definition** video.h:1302

[VIDEO\_PIX\_FMT\_SGBRG14P](group__video__pixel__formats.md#ga89eb47d1dd60794781ee91cb5ae199ad)

#define VIDEO\_PIX\_FMT\_SGBRG14P

**Definition** video.h:1172

[VIDEO\_PIX\_FMT\_XRGB32](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1)

#define VIDEO\_PIX\_FMT\_XRGB32

The first byte is empty (X) for each pixel.

**Definition** video.h:1502

[VIDEO\_PIX\_FMT\_SGBRG10](group__video__pixel__formats.md#ga8e0f47c16483b14b45a593e9e542a987)

#define VIDEO\_PIX\_FMT\_SGBRG10

**Definition** video.h:1206

[VIDEO\_PIX\_FMT\_RGBA32](group__video__pixel__formats.md#ga8ee1e3b82eeeb02188157aa4b4b5d842)

#define VIDEO\_PIX\_FMT\_RGBA32

**Definition** video.h:1485

[VIDEO\_PIX\_FMT\_SGRBG10P](group__video__pixel__formats.md#gaa28c6306a3ed44a0e50c16e0eac86688)

#define VIDEO\_PIX\_FMT\_SGRBG10P

**Definition** video.h:1109

[VIDEO\_PIX\_FMT\_SBGGR12](group__video__pixel__formats.md#gaa2d7712f655dfcb3c74b4f4ec9941402)

#define VIDEO\_PIX\_FMT\_SBGGR12

**Definition** video.h:1230

[VIDEO\_PIX\_FMT\_GREY](group__video__pixel__formats.md#gaa3af19adaf282b83a6c16f265a4260dc)

#define VIDEO\_PIX\_FMT\_GREY

Same as Y8 (8-bit luma-only) following the standard FOURCC naming, or L8 in some graphics libraries.

**Definition** video.h:1345

[VIDEO\_PIX\_FMT\_SGBRG12](group__video__pixel__formats.md#gaa3df9d0af327e609b25e050a4362c2e2)

#define VIDEO\_PIX\_FMT\_SGBRG12

**Definition** video.h:1238

[VIDEO\_PIX\_FMT\_Y16](group__video__pixel__formats.md#gaa65fe8bd917dd2fe95fa87530fc3055f)

#define VIDEO\_PIX\_FMT\_Y16

Little endian.

**Definition** video.h:1411

[VIDEO\_PIX\_FMT\_SRGGB14](group__video__pixel__formats.md#gaa6e4c240372e53db8ea3472cc456af58)

#define VIDEO\_PIX\_FMT\_SRGGB14

**Definition** video.h:1286

[VIDEO\_PIX\_FMT\_SGBRG8](group__video__pixel__formats.md#gaa9edb9c562fc3c86b61e071970fae60d)

#define VIDEO\_PIX\_FMT\_SGBRG8

**Definition** video.h:1064

[VIDEO\_PIX\_FMT\_SBGGR12P](group__video__pixel__formats.md#gab5b5375f050d039e05032c77ac838b31)

#define VIDEO\_PIX\_FMT\_SBGGR12P

**Definition** video.h:1127

[VIDEO\_PIX\_FMT\_SBGGR8](group__video__pixel__formats.md#gabc0205ce5c6426051fdec88d92f123e3)

#define VIDEO\_PIX\_FMT\_SBGGR8

**Definition** video.h:1055

[video\_bits\_per\_pixel](group__video__pixel__formats.md#gabdbd1b0f40af6663d81402deefdd387f)

static unsigned int video\_bits\_per\_pixel(uint32\_t pixfmt)

Get number of bits per pixel of a pixel format.

**Definition** video.h:1580

[VIDEO\_PIX\_FMT\_SRGGB8](group__video__pixel__formats.md#gabf0dde810e75d37823891ed03811482c)

#define VIDEO\_PIX\_FMT\_SRGGB8

**Definition** video.h:1082

[VIDEO\_PIX\_FMT\_SBGGR14P](group__video__pixel__formats.md#gac3413c36b3ce91e5658cd0f973c1f3d7)

#define VIDEO\_PIX\_FMT\_SBGGR14P

**Definition** video.h:1163

[VIDEO\_PIX\_FMT\_YUYV](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)

#define VIDEO\_PIX\_FMT\_YUYV

There is either a missing channel per pixel, U or V.

**Definition** video.h:1522

[VIDEO\_PIX\_FMT\_SGBRG10P](group__video__pixel__formats.md#gad69ab9041428488051bdb45f42ad4271)

#define VIDEO\_PIX\_FMT\_SGBRG10P

**Definition** video.h:1100

[VIDEO\_PIX\_FMT\_Y14P](group__video__pixel__formats.md#gada0124aad9c10d403966b1e3851cd968)

#define VIDEO\_PIX\_FMT\_Y14P

**Definition** video.h:1371

[VIDEO\_PIX\_FMT\_UYVY](group__video__pixel__formats.md#gadca3ee56c798cf05b63cbfc87af98ce3)

#define VIDEO\_PIX\_FMT\_UYVY

**Definition** video.h:1543

[VIDEO\_PIX\_FMT\_SGRBG14P](group__video__pixel__formats.md#gae06f742e31a62295d3ee16af8eec1b06)

#define VIDEO\_PIX\_FMT\_SGRBG14P

**Definition** video.h:1181

[VIDEO\_PIX\_FMT\_SBGGR16](group__video__pixel__formats.md#gae096669643176203199270317dc3449d)

#define VIDEO\_PIX\_FMT\_SBGGR16

**Definition** video.h:1294

[VIDEO\_PIX\_FMT\_SGBRG12P](group__video__pixel__formats.md#gaecedece3398a6e2f62c20c2eb3f6d3c2)

#define VIDEO\_PIX\_FMT\_SGBRG12P

**Definition** video.h:1136

[VIDEO\_PIX\_FMT\_RGB565](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)

#define VIDEO\_PIX\_FMT\_RGB565

5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0].

**Definition** video.h:1443

[VIDEO\_PIX\_FMT\_SGRBG12](group__video__pixel__formats.md#gaf18e6647596613e07ec3c651574b08ba)

#define VIDEO\_PIX\_FMT\_SGRBG12

**Definition** video.h:1246

[VIDEO\_PIX\_FMT\_BGR24](group__video__pixel__formats.md#gaf1f8775bbdd0508c4e21a58dfcfc362d)

#define VIDEO\_PIX\_FMT\_BGR24

24 bit RGB format with 8 bit per component

**Definition** video.h:1452

[VIDEO\_PIX\_FMT\_SGRBG14](group__video__pixel__formats.md#gaf58481956952b13b071b1a68541b9c21)

#define VIDEO\_PIX\_FMT\_SGRBG14

**Definition** video.h:1278

[VIDEO\_PIX\_FMT\_ABGR32](group__video__pixel__formats.md#gaffb650a5f9b2b03890283ecfe95aee04)

#define VIDEO\_PIX\_FMT\_ABGR32

**Definition** video.h:1477

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

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

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:6122

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[video\_buffer](structvideo__buffer.md)

Video buffer structure.

**Definition** video.h:146

[video\_buffer::bytesused](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1)

uint32\_t bytesused

number of bytes occupied by the valid data in the buffer.

**Definition** video.h:159

[video\_buffer::size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b)

uint32\_t size

size of the buffer in bytes.

**Definition** video.h:157

[video\_buffer::type](structvideo__buffer.md#a46dd9bd9398ff74e4f9859a07b9c48af)

enum video\_buf\_type type

type of the buffer

**Definition** video.h:151

[video\_buffer::buffer](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3)

uint8\_t \* buffer

pointer to the start of the buffer.

**Definition** video.h:153

[video\_buffer::driver\_data](structvideo__buffer.md#ab184d528487042650af105eb7d37381e)

void \* driver\_data

Pointer to driver specific data.

**Definition** video.h:149

[video\_buffer::line\_offset](structvideo__buffer.md#abe25963ea5e42d6fe42de1f21b554b87)

uint16\_t line\_offset

Line offset within frame this buffer represents, from the beginning of the frame.

**Definition** video.h:170

[video\_buffer::index](structvideo__buffer.md#acb948f9f124f9f2bfe9b19b44af60854)

uint8\_t index

index of the buffer, optionally set by the application

**Definition** video.h:155

[video\_buffer::timestamp](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba)

uint32\_t timestamp

time reference in milliseconds at which the last data byte was actually received for input endpoints ...

**Definition** video.h:164

[video\_caps](structvideo__caps.md)

Video format capabilities.

**Definition** video.h:113

[video\_caps::min\_vbuf\_count](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a)

uint8\_t min\_vbuf\_count

minimal count of video buffers to enqueue before being able to start the stream.

**Definition** video.h:121

[video\_caps::type](structvideo__caps.md#a31520f03f621082bbf516efce23ef1f6)

enum video\_buf\_type type

type of the buffer

**Definition** video.h:115

[video\_caps::min\_line\_count](structvideo__caps.md#a3ab95e55cd093f2414937a1916ef7f52)

int16\_t min\_line\_count

Denotes minimum line count of a video buffer that this endpoint can fill or process.

**Definition** video.h:130

[video\_caps::max\_line\_count](structvideo__caps.md#a51a059da1f30cac333ad6aad4c37d739)

int16\_t max\_line\_count

Denotes maximum line count of a video buffer that this endpoint can fill or process.

**Definition** video.h:137

[video\_caps::format\_caps](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185)

const struct video\_format\_cap \* format\_caps

list of video format capabilities (zero terminated).

**Definition** video.h:117

[video\_control](structvideo__control.md)

Video control structure.

**Definition** video-controls.h:410

[video\_ctrl\_query](structvideo__ctrl__query.md)

**Definition** video-controls.h:457

[video\_ctrl\_query::dev](structvideo__ctrl__query.md#aa534262295f6bf6816222d32f2b0986a)

const struct device \* dev

device being queried, application needs to set this field

**Definition** video-controls.h:459

[video\_driver\_api](structvideo__driver__api.md)

**Definition** video.h:393

[video\_driver\_api::set\_format](structvideo__driver__api.md#a1859e3a1db99d97c38ea24f2f9cd00be)

video\_api\_format\_t set\_format

**Definition** video.h:395

[video\_driver\_api::set\_ctrl](structvideo__driver__api.md#a41cd20fbb013bdb6b28d79822733695c)

video\_api\_ctrl\_t set\_ctrl

**Definition** video.h:403

[video\_driver\_api::enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75)

video\_api\_enqueue\_t enqueue

**Definition** video.h:400

[video\_driver\_api::set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2)

video\_api\_set\_signal\_t set\_signal

**Definition** video.h:405

[video\_driver\_api::enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726)

video\_api\_enum\_frmival\_t enum\_frmival

**Definition** video.h:408

[video\_driver\_api::get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078)

video\_api\_get\_caps\_t get\_caps

**Definition** video.h:398

[video\_driver\_api::get\_selection](structvideo__driver__api.md#a6ad8559ae0c2f6dc102e26e3714ded5d)

video\_api\_selection\_t get\_selection

**Definition** video.h:410

[video\_driver\_api::set\_selection](structvideo__driver__api.md#a800a2e8aaf59fc3fbd4bd2caaaf40f51)

video\_api\_selection\_t set\_selection

**Definition** video.h:409

[video\_driver\_api::get\_format](structvideo__driver__api.md#a8daefeec3cfc01de56f0168b32cdb640)

video\_api\_format\_t get\_format

**Definition** video.h:396

[video\_driver\_api::flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6)

video\_api\_flush\_t flush

**Definition** video.h:402

[video\_driver\_api::dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef)

video\_api\_dequeue\_t dequeue

**Definition** video.h:401

[video\_driver\_api::get\_frmival](structvideo__driver__api.md#abddf2db6034d10f76ac90ed5974df788)

video\_api\_frmival\_t get\_frmival

**Definition** video.h:407

[video\_driver\_api::set\_frmival](structvideo__driver__api.md#ac4b155a56c07bd8f7ecff9ec75dd0792)

video\_api\_frmival\_t set\_frmival

**Definition** video.h:406

[video\_driver\_api::set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04)

video\_api\_set\_stream\_t set\_stream

**Definition** video.h:397

[video\_driver\_api::get\_volatile\_ctrl](structvideo__driver__api.md#af50329fd41db78f4c5a945f57a7c091e)

video\_api\_ctrl\_t get\_volatile\_ctrl

**Definition** video.h:404

[video\_format\_cap](structvideo__format__cap.md)

Video format capability.

**Definition** video.h:90

[video\_format\_cap::height\_step](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e)

uint16\_t height\_step

height step size in pixels.

**Definition** video.h:104

[video\_format\_cap::width\_min](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9)

uint32\_t width\_min

minimum supported frame width in pixels.

**Definition** video.h:94

[video\_format\_cap::width\_max](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66)

uint32\_t width\_max

maximum supported frame width in pixels.

**Definition** video.h:96

[video\_format\_cap::width\_step](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad)

uint16\_t width\_step

width step size in pixels.

**Definition** video.h:102

[video\_format\_cap::height\_max](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f)

uint32\_t height\_max

maximum supported frame height in pixels.

**Definition** video.h:100

[video\_format\_cap::height\_min](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35)

uint32\_t height\_min

minimum supported frame height in pixels.

**Definition** video.h:98

[video\_format\_cap::pixelformat](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59)

uint32\_t pixelformat

FourCC pixel format value (Video pixel formats).

**Definition** video.h:92

[video\_format](structvideo__format.md)

Video format structure.

**Definition** video.h:65

[video\_format::height](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0)

uint32\_t height

frame height in pixels.

**Definition** video.h:73

[video\_format::type](structvideo__format.md#a233841606bfe82626f94906bf47f5f87)

enum video\_buf\_type type

type of the buffer

**Definition** video.h:67

[video\_format::width](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693)

uint32\_t width

frame width in pixels.

**Definition** video.h:71

[video\_format::pitch](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6)

uint32\_t pitch

line stride.

**Definition** video.h:81

[video\_format::pixelformat](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef)

uint32\_t pixelformat

FourCC pixel format value (Video pixel formats).

**Definition** video.h:69

[video\_frmival\_enum](structvideo__frmival__enum.md)

Video frame interval enumeration structure.

**Definition** video.h:219

[video\_frmival\_enum::index](structvideo__frmival__enum.md#a7654ce36fd942885b193da57579d88ed)

uint32\_t index

frame interval index during enumeration

**Definition** video.h:221

[video\_frmival\_enum::format](structvideo__frmival__enum.md#a8c103777cd5db24a2197ef994b8d008d)

const struct video\_format \* format

video format for which the query is made

**Definition** video.h:223

[video\_frmival\_enum::stepwise](structvideo__frmival__enum.md#aa3fda4e99646bff1d902198437982124)

struct video\_frmival\_stepwise stepwise

**Definition** video.h:229

[video\_frmival\_enum::type](structvideo__frmival__enum.md#aec62b54ed1152d6b3ea80c24ce7624f7)

enum video\_frmival\_type type

frame interval type the device supports

**Definition** video.h:225

[video\_frmival\_enum::discrete](structvideo__frmival__enum.md#af22ef303cdc75fd48b698ff72b57354c)

struct video\_frmival discrete

**Definition** video.h:228

[video\_frmival\_stepwise](structvideo__frmival__stepwise.md)

Video frame interval stepwise structure.

**Definition** video.h:204

[video\_frmival\_stepwise::min](structvideo__frmival__stepwise.md#aec892104241a9d4204c87af51765ee2f)

struct video\_frmival min

minimum frame interval in seconds

**Definition** video.h:206

[video\_frmival\_stepwise::max](structvideo__frmival__stepwise.md#af1c5a40da9fe7ad30185464eccf5b438)

struct video\_frmival max

maximum frame interval in seconds

**Definition** video.h:208

[video\_frmival\_stepwise::step](structvideo__frmival__stepwise.md#afc3c4e4fe3641952c4e6fc494fa85760)

struct video\_frmival step

frame interval step size in seconds

**Definition** video.h:210

[video\_frmival](structvideo__frmival.md)

Video frame interval structure.

**Definition** video.h:191

[video\_frmival::numerator](structvideo__frmival.md#a57ee282f01da0f1ef1db2558d777631c)

uint32\_t numerator

numerator of the frame interval

**Definition** video.h:193

[video\_frmival::denominator](structvideo__frmival.md#aba4a6700ea733c3b07ee6445856c580a)

uint32\_t denominator

denominator of the frame interval

**Definition** video.h:195

[video\_rect](structvideo__rect.md)

Description of a rectangle area.

**Definition** video.h:269

[video\_rect::width](structvideo__rect.md#a26403179cc6d65ff6c07a4b31b1a5050)

uint32\_t width

width of selection rectangle

**Definition** video.h:275

[video\_rect::height](structvideo__rect.md#a57d79483c9fc9bd800437160bd30664d)

uint32\_t height

height of selection rectangle

**Definition** video.h:277

[video\_rect::top](structvideo__rect.md#a769fd3843bcb11211eccdd766d09d83a)

uint32\_t top

top offset of selection rectangle

**Definition** video.h:273

[video\_rect::left](structvideo__rect.md#a94da5de0a4cc682556acd00fc05a8ea5)

uint32\_t left

left offset of selection rectangle

**Definition** video.h:271

[video\_selection\_target](structvideo__selection__target.md)

Video selection target enum.

[video\_selection](structvideo__selection.md)

Video selection (crop / compose) structure.

**Definition** video.h:286

[video\_selection::rect](structvideo__selection.md#a2e634792c0758a3dd576e4871c250bd2)

struct video\_rect rect

selection target rectangle

**Definition** video.h:292

[video\_selection::type](structvideo__selection.md#aec9dd0ae07f995f490ebdd86d48c1a63)

enum video\_buf\_type type

buffer type, allow to select for device having both input and output

**Definition** video.h:288

[video\_selection::target](structvideo__selection.md#afe358118a1d3c373888674f331dd05f1)

enum video\_selection\_target target

selection target enum

**Definition** video.h:290

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video.h](video_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
