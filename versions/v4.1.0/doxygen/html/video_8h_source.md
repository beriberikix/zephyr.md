---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/video_8h_source.html
original_path: doxygen/html/video_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_VIDEO\_H\_

13#define ZEPHYR\_INCLUDE\_VIDEO\_H\_

14

23

24#include <[zephyr/device.h](device_8h.md)>

25#include <stddef.h>

26#include <[zephyr/kernel.h](kernel_8h.md)>

27

28#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

34/\*

35 \* Flag used by @ref video\_caps structure to indicate endpoint operates on

36 \* buffers the size of the video frame

37 \*/

[ 38](group__video__interface.md#ga59e44ec7c8132f479f1aa71e5b2c6546)#define LINE\_COUNT\_HEIGHT (-1)

39

[ 46](structvideo__format.md)struct [video\_format](structvideo__format.md) {

[ 48](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pixelformat](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef);

[ 50](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693);

[ 52](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0);

[ 60](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pitch](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6);

61};

62

[ 69](structvideo__format__cap.md)struct [video\_format\_cap](structvideo__format__cap.md) {

[ 71](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pixelformat](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59);

[ 73](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width\_min](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9);

[ 75](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width\_max](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66);

[ 77](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height\_min](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35);

[ 79](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height\_max](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f);

[ 81](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [width\_step](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad);

[ 83](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [height\_step](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e);

84};

85

[ 92](structvideo__caps.md)struct [video\_caps](structvideo__caps.md) {

[ 94](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185) const struct [video\_format\_cap](structvideo__format__cap.md) \*[format\_caps](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185);

[ 98](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_vbuf\_count](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a);

[ 107](structvideo__caps.md#a3ab95e55cd093f2414937a1916ef7f52) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [min\_line\_count](structvideo__caps.md#a3ab95e55cd093f2414937a1916ef7f52);

[ 114](structvideo__caps.md#a51a059da1f30cac333ad6aad4c37d739) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [max\_line\_count](structvideo__caps.md#a51a059da1f30cac333ad6aad4c37d739);

115};

116

[ 123](structvideo__buffer.md)struct [video\_buffer](structvideo__buffer.md) {

[ 125](structvideo__buffer.md#ab184d528487042650af105eb7d37381e) void \*[driver\_data](structvideo__buffer.md#ab184d528487042650af105eb7d37381e);

[ 127](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3);

[ 129](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b);

[ 131](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bytesused](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1);

[ 136](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba);

[ 142](structvideo__buffer.md#abe25963ea5e42d6fe42de1f21b554b87) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [line\_offset](structvideo__buffer.md#abe25963ea5e42d6fe42de1f21b554b87);

143};

144

[ 150](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1)enum [video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1) {

[ 152](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4) [VIDEO\_FRMIVAL\_TYPE\_DISCRETE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4) = 1,

[ 154](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b) [VIDEO\_FRMIVAL\_TYPE\_STEPWISE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b) = 2,

155};

156

[ 163](structvideo__frmival.md)struct [video\_frmival](structvideo__frmival.md) {

[ 165](structvideo__frmival.md#a57ee282f01da0f1ef1db2558d777631c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [numerator](structvideo__frmival.md#a57ee282f01da0f1ef1db2558d777631c);

[ 167](structvideo__frmival.md#aba4a6700ea733c3b07ee6445856c580a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [denominator](structvideo__frmival.md#aba4a6700ea733c3b07ee6445856c580a);

168};

169

[ 176](structvideo__frmival__stepwise.md)struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) {

[ 178](structvideo__frmival__stepwise.md#aec892104241a9d4204c87af51765ee2f) struct [video\_frmival](structvideo__frmival.md) [min](structvideo__frmival__stepwise.md#aec892104241a9d4204c87af51765ee2f);

[ 180](structvideo__frmival__stepwise.md#af1c5a40da9fe7ad30185464eccf5b438) struct [video\_frmival](structvideo__frmival.md) [max](structvideo__frmival__stepwise.md#af1c5a40da9fe7ad30185464eccf5b438);

[ 182](structvideo__frmival__stepwise.md#afc3c4e4fe3641952c4e6fc494fa85760) struct [video\_frmival](structvideo__frmival.md) [step](structvideo__frmival__stepwise.md#afc3c4e4fe3641952c4e6fc494fa85760);

183};

184

[ 191](structvideo__frmival__enum.md)struct [video\_frmival\_enum](structvideo__frmival__enum.md) {

[ 193](structvideo__frmival__enum.md#a7654ce36fd942885b193da57579d88ed) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [index](structvideo__frmival__enum.md#a7654ce36fd942885b193da57579d88ed);

[ 195](structvideo__frmival__enum.md#a8c103777cd5db24a2197ef994b8d008d) const struct [video\_format](structvideo__format.md) \*[format](structvideo__frmival__enum.md#a8c103777cd5db24a2197ef994b8d008d);

[ 197](structvideo__frmival__enum.md#aec62b54ed1152d6b3ea80c24ce7624f7) enum [video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1) [type](structvideo__frmival__enum.md#aec62b54ed1152d6b3ea80c24ce7624f7);

199 union {

[ 200](structvideo__frmival__enum.md#af22ef303cdc75fd48b698ff72b57354c) struct [video\_frmival](structvideo__frmival.md) [discrete](structvideo__frmival__enum.md#af22ef303cdc75fd48b698ff72b57354c);

[ 201](structvideo__frmival__enum.md#aa3fda4e99646bff1d902198437982124) struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) [stepwise](structvideo__frmival__enum.md#aa3fda4e99646bff1d902198437982124);

202 };

203};

204

[ 210](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9)enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) {

[ 212](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7) [VIDEO\_EP\_NONE](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7) = -1,

[ 214](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9afb3b8e141a5675a7d299b82dca5f36a9) [VIDEO\_EP\_ALL](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9afb3b8e141a5675a7d299b82dca5f36a9) = -2,

[ 216](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7) [VIDEO\_EP\_IN](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7) = -3,

[ 218](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a) [VIDEO\_EP\_OUT](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a) = -4,

219};

220

[ 226](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8)enum [video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8) {

[ 227](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8) [VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8),

[ 228](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8) [VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8),

[ 229](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3) [VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3),

230};

231

[ 238](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18)typedef int (\*[video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

239 struct [video\_format](structvideo__format.md) \*fmt);

240

[ 247](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d)typedef int (\*[video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

248 struct [video\_format](structvideo__format.md) \*fmt);

249

[ 256](group__video__interface.md#gac69b1ab2877112983b421c650076da89)typedef int (\*[video\_api\_set\_frmival\_t](group__video__interface.md#gac69b1ab2877112983b421c650076da89))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

257 struct [video\_frmival](structvideo__frmival.md) \*frmival);

258

[ 265](group__video__interface.md#gaa7fae28aae3959ea09f9ffc87fa42c7e)typedef int (\*[video\_api\_get\_frmival\_t](group__video__interface.md#gaa7fae28aae3959ea09f9ffc87fa42c7e))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

266 struct [video\_frmival](structvideo__frmival.md) \*frmival);

267

[ 274](group__video__interface.md#gab8bd3f3a430e6872facad2749d7f2240)typedef int (\*[video\_api\_enum\_frmival\_t](group__video__interface.md#gab8bd3f3a430e6872facad2749d7f2240))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

275 struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie);

276

[ 283](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe)typedef int (\*[video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

284 struct [video\_buffer](structvideo__buffer.md) \*buf);

285

[ 292](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d)typedef int (\*[video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

293 struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout);

294

[ 302](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db)typedef int (\*[video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, bool cancel);

303

[ 315](group__video__interface.md#ga4293068f01f310a8d9452fb68fb9afa0)typedef int (\*[video\_api\_set\_stream\_t](group__video__interface.md#ga4293068f01f310a8d9452fb68fb9afa0))(const struct [device](structdevice.md) \*dev, bool enable);

316

[ 323](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a)typedef int (\*[video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a))(const struct [device](structdevice.md) \*dev, unsigned int cid, void \*value);

324

[ 331](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c)typedef int (\*[video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c))(const struct [device](structdevice.md) \*dev, unsigned int cid, void \*value);

332

[ 339](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312)typedef int (\*[video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

340 struct [video\_caps](structvideo__caps.md) \*caps);

341

[ 348](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321)typedef int (\*[video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

349 struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69));

350

[ 351](structvideo__driver__api.md)\_\_subsystem struct [video\_driver\_api](structvideo__driver__api.md) {

352 /\* mandatory callbacks \*/

[ 353](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8) [video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18) [set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8);

[ 354](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4) [video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d) [get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4);

[ 355](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04) [video\_api\_set\_stream\_t](group__video__interface.md#ga4293068f01f310a8d9452fb68fb9afa0) [set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04);

[ 356](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078) [video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312) [get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078);

357 /\* optional callbacks \*/

[ 358](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75) [video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe) [enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75);

[ 359](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef) [video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d) [dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef);

[ 360](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6) [video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db) [flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6);

[ 361](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8) [video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a) [set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8);

[ 362](structvideo__driver__api.md#ab5e5176079fcba90bd57a6ce19adcaeb) [video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c) [get\_ctrl](structvideo__driver__api.md#ab5e5176079fcba90bd57a6ce19adcaeb);

[ 363](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2) [video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321) [set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2);

[ 364](structvideo__driver__api.md#ae10587ed4c5cc43f244209b1f18ddc68) [video\_api\_set\_frmival\_t](group__video__interface.md#gac69b1ab2877112983b421c650076da89) [set\_frmival](structvideo__driver__api.md#ae10587ed4c5cc43f244209b1f18ddc68);

[ 365](structvideo__driver__api.md#acce22c3f6185c2777bbeda4f32e84940) [video\_api\_get\_frmival\_t](group__video__interface.md#gaa7fae28aae3959ea09f9ffc87fa42c7e) [get\_frmival](structvideo__driver__api.md#acce22c3f6185c2777bbeda4f32e84940);

[ 366](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726) [video\_api\_enum\_frmival\_t](group__video__interface.md#gab8bd3f3a430e6872facad2749d7f2240) [enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726);

367};

368

[ 383](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)static inline int [video\_set\_format](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

384 struct [video\_format](structvideo__format.md) \*fmt)

385{

386 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

387

388 if (api->[set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

389 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

390 }

391

392 return api->[set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8)(dev, ep, fmt);

393}

394

[ 406](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)static inline int [video\_get\_format](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

407 struct [video\_format](structvideo__format.md) \*fmt)

408{

409 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

410

411 if (api->[get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

412 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

413 }

414

415 return api->[get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4)(dev, ep, fmt);

416}

417

[ 435](group__video__interface.md#ga50149acd5c56d237c5a6988bdf1cc241)static inline int [video\_set\_frmival](group__video__interface.md#ga50149acd5c56d237c5a6988bdf1cc241)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

436 struct [video\_frmival](structvideo__frmival.md) \*frmival)

437{

438 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

439

440 if (api->[set\_frmival](structvideo__driver__api.md#ae10587ed4c5cc43f244209b1f18ddc68) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

441 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

442 }

443

444 return api->[set\_frmival](structvideo__driver__api.md#ae10587ed4c5cc43f244209b1f18ddc68)(dev, ep, frmival);

445}

446

[ 461](group__video__interface.md#gaa7a61a51424e0d030b87ec52ceb8dc07)static inline int [video\_get\_frmival](group__video__interface.md#gaa7a61a51424e0d030b87ec52ceb8dc07)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

462 struct [video\_frmival](structvideo__frmival.md) \*frmival)

463{

464 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

465

466 if (api->[get\_frmival](structvideo__driver__api.md#acce22c3f6185c2777bbeda4f32e84940) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

467 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

468 }

469

470 return api->[get\_frmival](structvideo__driver__api.md#acce22c3f6185c2777bbeda4f32e84940)(dev, ep, frmival);

471}

472

[ 491](group__video__interface.md#gabd7f2fe113e3ade441a1d6cce66c1cda)static inline int [video\_enum\_frmival](group__video__interface.md#gabd7f2fe113e3ade441a1d6cce66c1cda)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

492 struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie)

493{

494 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

495

496 if (api->[enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

497 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

498 }

499

500 return api->[enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726)(dev, ep, fie);

501}

502

[ 517](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)static inline int [video\_enqueue](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

518 struct [video\_buffer](structvideo__buffer.md) \*buf)

519{

520 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

521

522 if (api->[enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

523 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

524 }

525

526 return api->[enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75)(dev, ep, buf);

527}

528

[ 544](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)static inline int [video\_dequeue](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

545 struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout)

546{

547 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

548

549 if (api->[dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

550 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

551 }

552

553 return api->[dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef)(dev, ep, buf, timeout);

554}

555

[ 570](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)static inline int [video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, bool cancel)

571{

572 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

573

574 if (api->[flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

575 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

576 }

577

578 return api->[flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6)(dev, ep, cancel);

579}

580

[ 593](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)static inline int [video\_stream\_start](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)(const struct [device](structdevice.md) \*dev)

594{

595 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

596

597 if (api->[set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

598 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

599 }

600

601 return api->[set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04)(dev, true);

602}

603

[ 613](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)static inline int [video\_stream\_stop](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)(const struct [device](structdevice.md) \*dev)

614{

615 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

616 int ret;

617

618 if (api->[set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

619 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

620 }

621

622 ret = api->[set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04)(dev, false);

623 [video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)(dev, [VIDEO\_EP\_ALL](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9afb3b8e141a5675a7d299b82dca5f36a9), true);

624

625 return ret;

626}

627

[ 637](group__video__interface.md#ga4d5237607c858708380955705a2023bd)static inline int [video\_get\_caps](group__video__interface.md#ga4d5237607c858708380955705a2023bd)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

638 struct [video\_caps](structvideo__caps.md) \*caps)

639{

640 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

641

642 if (api->[get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

643 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

644 }

645

646 return api->[get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078)(dev, ep, caps);

647}

648

[ 664](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)static inline int [video\_set\_ctrl](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)(const struct [device](structdevice.md) \*dev, unsigned int cid, void \*value)

665{

666 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

667

668 if (api->[set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

669 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

670 }

671

672 return api->[set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8)(dev, cid, value);

673}

674

[ 690](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)static inline int [video\_get\_ctrl](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)(const struct [device](structdevice.md) \*dev, unsigned int cid, void \*value)

691{

692 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

693

694 if (api->[get\_ctrl](structvideo__driver__api.md#ab5e5176079fcba90bd57a6ce19adcaeb) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

695 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

696 }

697

698 return api->[get\_ctrl](structvideo__driver__api.md#ab5e5176079fcba90bd57a6ce19adcaeb)(dev, cid, value);

699}

700

[ 714](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)static inline int [video\_set\_signal](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

715 struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69))

716{

717 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

718

719 if (api->[set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

720 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

721 }

722

723 return api->[set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2)(dev, ep, [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69));

724}

725

[ 735](group__video__interface.md#ga195914c7f03f2241702c77d41d1ab750)struct [video\_buffer](structvideo__buffer.md) \*[video\_buffer\_aligned\_alloc](group__video__interface.md#ga195914c7f03f2241702c77d41d1ab750)(size\_t [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b), size\_t align, [k\_timeout\_t](structk__timeout__t.md) timeout);

736

[ 745](group__video__interface.md#gaee6eb26310a40d3f18161b3567f9e0a9)struct [video\_buffer](structvideo__buffer.md) \*[video\_buffer\_alloc](group__video__interface.md#gaee6eb26310a40d3f18161b3567f9e0a9)(size\_t [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b), [k\_timeout\_t](structk__timeout__t.md) timeout);

746

[ 752](group__video__interface.md#gad2661653db019b673153001b2c61b10f)void [video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f)(struct [video\_buffer](structvideo__buffer.md) \*buf);

753

[ 764](group__video__interface.md#gadbf59fd2d77b3d164cacf56bd4ae81ce)int [video\_format\_caps\_index](group__video__interface.md#gadbf59fd2d77b3d164cacf56bd4ae81ce)(const struct [video\_format\_cap](structvideo__format__cap.md) \*fmts, const struct [video\_format](structvideo__format.md) \*fmt,

765 size\_t \*idx);

766

[ 774](group__video__interface.md#ga6b3c7456b2527cc441a100ff50787dc2)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [video\_frmival\_nsec](group__video__interface.md#ga6b3c7456b2527cc441a100ff50787dc2)(const struct [video\_frmival](structvideo__frmival.md) \*frmival)

775{

776 return ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) \* frmival->[numerator](structvideo__frmival.md#a57ee282f01da0f1ef1db2558d777631c) / frmival->[denominator](structvideo__frmival.md#aba4a6700ea733c3b07ee6445856c580a);

777}

778

[ 786](group__video__interface.md#gad11314e82e9207449b3c0b29fdc830d0)void [video\_closest\_frmival\_stepwise](group__video__interface.md#gad11314e82e9207449b3c0b29fdc830d0)(const struct [video\_frmival\_stepwise](structvideo__frmival__stepwise.md) \*stepwise,

787 const struct [video\_frmival](structvideo__frmival.md) \*desired,

788 struct [video\_frmival](structvideo__frmival.md) \*match);

789

[ 808](group__video__interface.md#ga67a86a3f920332347d8224a3074f6e23)void [video\_closest\_frmival](group__video__interface.md#ga67a86a3f920332347d8224a3074f6e23)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

809 struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*match);

810

818

[ 822](group__video__pixel__formats.md#gafb9e36597c39face52cd0c010df20951)#define VIDEO\_FOURCC(a, b, c, d) \

823 ((uint32\_t)(a) | ((uint32\_t)(b) << 8) | ((uint32\_t)(c) << 16) | ((uint32\_t)(d) << 24))

824

[ 834](group__video__pixel__formats.md#gafc6c4cb871f15464f2b7df86d91fd8f3)#define VIDEO\_FOURCC\_FROM\_STR(str) VIDEO\_FOURCC((str)[0], (str)[1], (str)[2], (str)[3])

835

843

[ 850](group__video__pixel__formats.md#ga64ad74bb6c92041a4190614b684ae024)#define VIDEO\_PIX\_FMT\_BGGR8 VIDEO\_FOURCC('B', 'A', '8', '1')

851

[ 858](group__video__pixel__formats.md#gaebdfd9d4230b56f6b8533630356b8793)#define VIDEO\_PIX\_FMT\_GBRG8 VIDEO\_FOURCC('G', 'B', 'R', 'G')

859

[ 866](group__video__pixel__formats.md#ga6b9c8d43406e45927f4e9e94504eae9c)#define VIDEO\_PIX\_FMT\_GRBG8 VIDEO\_FOURCC('G', 'R', 'B', 'G')

867

[ 874](group__video__pixel__formats.md#ga0c98dc205b724c9e4556e41cc266d80e)#define VIDEO\_PIX\_FMT\_RGGB8 VIDEO\_FOURCC('R', 'G', 'G', 'B')

875

879

885

[ 895](group__video__pixel__formats.md#gaf3830004bb857fa00a14d0a1209c61a8)#define VIDEO\_PIX\_FMT\_RGB565X VIDEO\_FOURCC('R', 'G', 'B', 'R')

896

[ 906](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)#define VIDEO\_PIX\_FMT\_RGB565 VIDEO\_FOURCC('R', 'G', 'B', 'P')

907

[ 915](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1)#define VIDEO\_PIX\_FMT\_XRGB32 VIDEO\_FOURCC('B', 'X', '2', '4')

916

920

926

[ 935](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)#define VIDEO\_PIX\_FMT\_YUYV VIDEO\_FOURCC('Y', 'U', 'Y', 'V')

936

[ 944](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351)#define VIDEO\_PIX\_FMT\_XYUV32 VIDEO\_FOURCC('X', 'Y', 'U', 'V')

945

949

954

[ 958](group__video__pixel__formats.md#ga035a13c38c4f123411547e2c40d58bd2)#define VIDEO\_PIX\_FMT\_JPEG VIDEO\_FOURCC('J', 'P', 'E', 'G')

959

963

[ 972](group__video__pixel__formats.md#gabdbd1b0f40af6663d81402deefdd387f)static inline unsigned int [video\_bits\_per\_pixel](group__video__pixel__formats.md#gabdbd1b0f40af6663d81402deefdd387f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pixfmt)

973{

974 switch (pixfmt) {

975 case [VIDEO\_PIX\_FMT\_BGGR8](group__video__pixel__formats.md#ga64ad74bb6c92041a4190614b684ae024):

976 case [VIDEO\_PIX\_FMT\_GBRG8](group__video__pixel__formats.md#gaebdfd9d4230b56f6b8533630356b8793):

977 case [VIDEO\_PIX\_FMT\_GRBG8](group__video__pixel__formats.md#ga6b9c8d43406e45927f4e9e94504eae9c):

978 case [VIDEO\_PIX\_FMT\_RGGB8](group__video__pixel__formats.md#ga0c98dc205b724c9e4556e41cc266d80e):

979 return 8;

980 case [VIDEO\_PIX\_FMT\_RGB565](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec):

981 case [VIDEO\_PIX\_FMT\_YUYV](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11):

982 return 16;

983 case [VIDEO\_PIX\_FMT\_XRGB32](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1):

984 case [VIDEO\_PIX\_FMT\_XYUV32](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351):

985 return 32;

986 default:

987 /\* Variable number of bits per pixel or unknown format \*/

988 return 0;

989 }

990}

991

995

996#ifdef \_\_cplusplus

997}

998#endif

999

1003

1004#endif /\* ZEPHYR\_INCLUDE\_VIDEO\_H\_ \*/

[device.h](device_8h.md)

[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)

#define NSEC\_PER\_SEC

number of nanoseconds per second

**Definition** sys\_clock.h:113

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8)

video\_signal\_result

video\_event enum

**Definition** video.h:226

[video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe)

int(\* video\_api\_enqueue\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*buf)

Enqueue a buffer in the driver’s incoming queue.

**Definition** video.h:283

[video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d)

int(\* video\_api\_dequeue\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*\*buf, k\_timeout\_t timeout)

Dequeue a buffer from the driver’s outgoing queue.

**Definition** video.h:292

[video\_buffer\_aligned\_alloc](group__video__interface.md#ga195914c7f03f2241702c77d41d1ab750)

struct video\_buffer \* video\_buffer\_aligned\_alloc(size\_t size, size\_t align, k\_timeout\_t timeout)

Allocate aligned video buffer.

[video\_api\_set\_stream\_t](group__video__interface.md#ga4293068f01f310a8d9452fb68fb9afa0)

int(\* video\_api\_set\_stream\_t)(const struct device \*dev, bool enable)

Start or stop streaming on the video device.

**Definition** video.h:315

[video\_get\_caps](group__video__interface.md#ga4d5237607c858708380955705a2023bd)

static int video\_get\_caps(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_caps \*caps)

Get the capabilities of a video endpoint.

**Definition** video.h:637

[video\_set\_frmival](group__video__interface.md#ga50149acd5c56d237c5a6988bdf1cc241)

static int video\_set\_frmival(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival \*frmival)

Set video frame interval.

**Definition** video.h:435

[video\_stream\_stop](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)

static int video\_stream\_stop(const struct device \*dev)

Stop the video device function.

**Definition** video.h:613

[video\_get\_ctrl](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)

static int video\_get\_ctrl(const struct device \*dev, unsigned int cid, void \*value)

Get the current value of a control.

**Definition** video.h:690

[video\_closest\_frmival](group__video__interface.md#ga67a86a3f920332347d8224a3074f6e23)

void video\_closest\_frmival(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival\_enum \*match)

Find the closest match to a frame interval value within a video device.

[video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1)

video\_frmival\_type

video\_frmival\_type enum

**Definition** video.h:150

[video\_frmival\_nsec](group__video__interface.md#ga6b3c7456b2527cc441a100ff50787dc2)

static uint64\_t video\_frmival\_nsec(const struct video\_frmival \*frmival)

Compute the difference between two frame intervals.

**Definition** video.h:774

[video\_stream\_start](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)

static int video\_stream\_start(const struct device \*dev)

Start the video device function.

**Definition** video.h:593

[video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d)

int(\* video\_api\_get\_format\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Get current video format.

**Definition** video.h:247

[video\_set\_ctrl](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)

static int video\_set\_ctrl(const struct device \*dev, unsigned int cid, void \*value)

Set the value of a control.

**Definition** video.h:664

[video\_dequeue](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)

static int video\_dequeue(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*\*buf, k\_timeout\_t timeout)

Dequeue a video buffer.

**Definition** video.h:544

[video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321)

int(\* video\_api\_set\_signal\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct k\_poll\_signal \*signal)

Register/Unregister poll signal for buffer events.

**Definition** video.h:348

[video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c)

int(\* video\_api\_get\_ctrl\_t)(const struct device \*dev, unsigned int cid, void \*value)

Get a video control value.

**Definition** video.h:331

[video\_get\_frmival](group__video__interface.md#gaa7a61a51424e0d030b87ec52ceb8dc07)

static int video\_get\_frmival(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival \*frmival)

Get video frame interval.

**Definition** video.h:461

[video\_api\_get\_frmival\_t](group__video__interface.md#gaa7fae28aae3959ea09f9ffc87fa42c7e)

int(\* video\_api\_get\_frmival\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival \*frmival)

Get current video frame interval.

**Definition** video.h:265

[video\_set\_signal](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)

static int video\_set\_signal(const struct device \*dev, enum video\_endpoint\_id ep, struct k\_poll\_signal \*signal)

Register/Unregister k\_poll signal for a video endpoint.

**Definition** video.h:714

[video\_api\_enum\_frmival\_t](group__video__interface.md#gab8bd3f3a430e6872facad2749d7f2240)

int(\* video\_api\_enum\_frmival\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival\_enum \*fie)

List all supported frame intervals of a given format.

**Definition** video.h:274

[video\_enum\_frmival](group__video__interface.md#gabd7f2fe113e3ade441a1d6cce66c1cda)

static int video\_enum\_frmival(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival\_enum \*fie)

List video frame intervals.

**Definition** video.h:491

[video\_get\_format](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)

static int video\_get\_format(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Get video format.

**Definition** video.h:406

[video\_enqueue](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)

static int video\_enqueue(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*buf)

Enqueue a video buffer.

**Definition** video.h:517

[video\_api\_set\_frmival\_t](group__video__interface.md#gac69b1ab2877112983b421c650076da89)

int(\* video\_api\_set\_frmival\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival \*frmival)

Set video frame interval.

**Definition** video.h:256

[video\_closest\_frmival\_stepwise](group__video__interface.md#gad11314e82e9207449b3c0b29fdc830d0)

void video\_closest\_frmival\_stepwise(const struct video\_frmival\_stepwise \*stepwise, const struct video\_frmival \*desired, struct video\_frmival \*match)

Find the closest match to a frame interval value within a stepwise frame interval.

[video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f)

void video\_buffer\_release(struct video\_buffer \*buf)

Release a video buffer.

[video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db)

int(\* video\_api\_flush\_t)(const struct device \*dev, enum video\_endpoint\_id ep, bool cancel)

Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue.

**Definition** video.h:302

[video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a)

int(\* video\_api\_set\_ctrl\_t)(const struct device \*dev, unsigned int cid, void \*value)

Set a video control value.

**Definition** video.h:323

[video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312)

int(\* video\_api\_get\_caps\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_caps \*caps)

Get capabilities of a video endpoint.

**Definition** video.h:339

[video\_format\_caps\_index](group__video__interface.md#gadbf59fd2d77b3d164cacf56bd4ae81ce)

int video\_format\_caps\_index(const struct video\_format\_cap \*fmts, const struct video\_format \*fmt, size\_t \*idx)

Search for a format that matches in a list of capabilities.

[video\_set\_format](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)

static int video\_set\_format(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Set video format.

**Definition** video.h:383

[video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)

static int video\_flush(const struct device \*dev, enum video\_endpoint\_id ep, bool cancel)

Flush endpoint buffers.

**Definition** video.h:570

[video\_buffer\_alloc](group__video__interface.md#gaee6eb26310a40d3f18161b3567f9e0a9)

struct video\_buffer \* video\_buffer\_alloc(size\_t size, k\_timeout\_t timeout)

Allocate video buffer.

[video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18)

int(\* video\_api\_set\_format\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Set video format.

**Definition** video.h:238

[video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9)

video\_endpoint\_id

video\_endpoint\_id enum

**Definition** video.h:210

[VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8)

@ VIDEO\_BUF\_ABORTED

**Definition** video.h:228

[VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8)

@ VIDEO\_BUF\_DONE

**Definition** video.h:227

[VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3)

@ VIDEO\_BUF\_ERROR

**Definition** video.h:229

[VIDEO\_FRMIVAL\_TYPE\_DISCRETE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a28c2c75ff3617952db572ce4c1ca7aa4)

@ VIDEO\_FRMIVAL\_TYPE\_DISCRETE

discrete frame interval type

**Definition** video.h:152

[VIDEO\_FRMIVAL\_TYPE\_STEPWISE](group__video__interface.md#gga6abf1fc9c35cf1d1648cde7616e7cad1a6546b3e1b4c7dae8c2448e437c5d928b)

@ VIDEO\_FRMIVAL\_TYPE\_STEPWISE

stepwise frame interval type

**Definition** video.h:154

[VIDEO\_EP\_IN](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7)

@ VIDEO\_EP\_IN

Targets all input endpoints of the device: those consuming data.

**Definition** video.h:216

[VIDEO\_EP\_NONE](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7)

@ VIDEO\_EP\_NONE

Targets some part of the video device not bound to an endpoint.

**Definition** video.h:212

[VIDEO\_EP\_OUT](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a)

@ VIDEO\_EP\_OUT

Targets all output endpoints of the device: those producing data.

**Definition** video.h:218

[VIDEO\_EP\_ALL](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9afb3b8e141a5675a7d299b82dca5f36a9)

@ VIDEO\_EP\_ALL

Targets all input or output endpoints of the device.

**Definition** video.h:214

[VIDEO\_PIX\_FMT\_XYUV32](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351)

#define VIDEO\_PIX\_FMT\_XYUV32

The first byte is empty (X) for each pixel.

**Definition** video.h:944

[VIDEO\_PIX\_FMT\_RGGB8](group__video__pixel__formats.md#ga0c98dc205b724c9e4556e41cc266d80e)

#define VIDEO\_PIX\_FMT\_RGGB8

**Definition** video.h:874

[VIDEO\_PIX\_FMT\_BGGR8](group__video__pixel__formats.md#ga64ad74bb6c92041a4190614b684ae024)

#define VIDEO\_PIX\_FMT\_BGGR8

**Definition** video.h:850

[VIDEO\_PIX\_FMT\_GRBG8](group__video__pixel__formats.md#ga6b9c8d43406e45927f4e9e94504eae9c)

#define VIDEO\_PIX\_FMT\_GRBG8

**Definition** video.h:866

[VIDEO\_PIX\_FMT\_XRGB32](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1)

#define VIDEO\_PIX\_FMT\_XRGB32

The first byte is empty (X) for each pixel.

**Definition** video.h:915

[video\_bits\_per\_pixel](group__video__pixel__formats.md#gabdbd1b0f40af6663d81402deefdd387f)

static unsigned int video\_bits\_per\_pixel(uint32\_t pixfmt)

Get number of bits per pixel of a pixel format.

**Definition** video.h:972

[VIDEO\_PIX\_FMT\_YUYV](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)

#define VIDEO\_PIX\_FMT\_YUYV

There is either a missing channel per pixel, U or V.

**Definition** video.h:935

[VIDEO\_PIX\_FMT\_GBRG8](group__video__pixel__formats.md#gaebdfd9d4230b56f6b8533630356b8793)

#define VIDEO\_PIX\_FMT\_GBRG8

**Definition** video.h:858

[VIDEO\_PIX\_FMT\_RGB565](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)

#define VIDEO\_PIX\_FMT\_RGB565

5 red bits [15:11], 6 green bits [10:5], 5 blue bits [4:0].

**Definition** video.h:906

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)

sighandler\_t signal(int signo, sighandler\_t handler)

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

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5964

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[video\_buffer](structvideo__buffer.md)

Video buffer structure.

**Definition** video.h:123

[video\_buffer::bytesused](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1)

uint32\_t bytesused

number of bytes occupied by the valid data in the buffer.

**Definition** video.h:131

[video\_buffer::size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b)

uint32\_t size

size of the buffer in bytes.

**Definition** video.h:129

[video\_buffer::buffer](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3)

uint8\_t \* buffer

pointer to the start of the buffer.

**Definition** video.h:127

[video\_buffer::driver\_data](structvideo__buffer.md#ab184d528487042650af105eb7d37381e)

void \* driver\_data

pointer to driver specific data.

**Definition** video.h:125

[video\_buffer::line\_offset](structvideo__buffer.md#abe25963ea5e42d6fe42de1f21b554b87)

uint16\_t line\_offset

Line offset within frame this buffer represents, from the beginning of the frame.

**Definition** video.h:142

[video\_buffer::timestamp](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba)

uint32\_t timestamp

time reference in milliseconds at which the last data byte was actually received for input endpoints ...

**Definition** video.h:136

[video\_caps](structvideo__caps.md)

Video format capabilities.

**Definition** video.h:92

[video\_caps::min\_vbuf\_count](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a)

uint8\_t min\_vbuf\_count

minimal count of video buffers to enqueue before being able to start the stream.

**Definition** video.h:98

[video\_caps::min\_line\_count](structvideo__caps.md#a3ab95e55cd093f2414937a1916ef7f52)

int16\_t min\_line\_count

Denotes minimum line count of a video buffer that this endpoint can fill or process.

**Definition** video.h:107

[video\_caps::max\_line\_count](structvideo__caps.md#a51a059da1f30cac333ad6aad4c37d739)

int16\_t max\_line\_count

Denotes maximum line count of a video buffer that this endpoint can fill or process.

**Definition** video.h:114

[video\_caps::format\_caps](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185)

const struct video\_format\_cap \* format\_caps

list of video format capabilities (zero terminated).

**Definition** video.h:94

[video\_driver\_api](structvideo__driver__api.md)

**Definition** video.h:351

[video\_driver\_api::set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8)

video\_api\_set\_ctrl\_t set\_ctrl

**Definition** video.h:361

[video\_driver\_api::enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75)

video\_api\_enqueue\_t enqueue

**Definition** video.h:358

[video\_driver\_api::set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2)

video\_api\_set\_signal\_t set\_signal

**Definition** video.h:363

[video\_driver\_api::get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4)

video\_api\_get\_format\_t get\_format

**Definition** video.h:354

[video\_driver\_api::enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726)

video\_api\_enum\_frmival\_t enum\_frmival

**Definition** video.h:366

[video\_driver\_api::get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078)

video\_api\_get\_caps\_t get\_caps

**Definition** video.h:356

[video\_driver\_api::set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8)

video\_api\_set\_format\_t set\_format

**Definition** video.h:353

[video\_driver\_api::flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6)

video\_api\_flush\_t flush

**Definition** video.h:360

[video\_driver\_api::dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef)

video\_api\_dequeue\_t dequeue

**Definition** video.h:359

[video\_driver\_api::get\_ctrl](structvideo__driver__api.md#ab5e5176079fcba90bd57a6ce19adcaeb)

video\_api\_get\_ctrl\_t get\_ctrl

**Definition** video.h:362

[video\_driver\_api::get\_frmival](structvideo__driver__api.md#acce22c3f6185c2777bbeda4f32e84940)

video\_api\_get\_frmival\_t get\_frmival

**Definition** video.h:365

[video\_driver\_api::set\_stream](structvideo__driver__api.md#adc08ef9eeeaac584c1b9ae5e6fb70c04)

video\_api\_set\_stream\_t set\_stream

**Definition** video.h:355

[video\_driver\_api::set\_frmival](structvideo__driver__api.md#ae10587ed4c5cc43f244209b1f18ddc68)

video\_api\_set\_frmival\_t set\_frmival

**Definition** video.h:364

[video\_format\_cap](structvideo__format__cap.md)

Video format capability.

**Definition** video.h:69

[video\_format\_cap::height\_step](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e)

uint16\_t height\_step

height step size in pixels.

**Definition** video.h:83

[video\_format\_cap::width\_min](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9)

uint32\_t width\_min

minimum supported frame width in pixels.

**Definition** video.h:73

[video\_format\_cap::width\_max](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66)

uint32\_t width\_max

maximum supported frame width in pixels.

**Definition** video.h:75

[video\_format\_cap::width\_step](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad)

uint16\_t width\_step

width step size in pixels.

**Definition** video.h:81

[video\_format\_cap::height\_max](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f)

uint32\_t height\_max

maximum supported frame height in pixels.

**Definition** video.h:79

[video\_format\_cap::height\_min](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35)

uint32\_t height\_min

minimum supported frame height in pixels.

**Definition** video.h:77

[video\_format\_cap::pixelformat](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59)

uint32\_t pixelformat

FourCC pixel format value (Video pixel formats).

**Definition** video.h:71

[video\_format](structvideo__format.md)

Video format structure.

**Definition** video.h:46

[video\_format::height](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0)

uint32\_t height

frame height in pixels.

**Definition** video.h:52

[video\_format::width](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693)

uint32\_t width

frame width in pixels.

**Definition** video.h:50

[video\_format::pitch](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6)

uint32\_t pitch

line stride.

**Definition** video.h:60

[video\_format::pixelformat](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef)

uint32\_t pixelformat

FourCC pixel format value (Video pixel formats).

**Definition** video.h:48

[video\_frmival\_enum](structvideo__frmival__enum.md)

Video frame interval enumeration structure.

**Definition** video.h:191

[video\_frmival\_enum::index](structvideo__frmival__enum.md#a7654ce36fd942885b193da57579d88ed)

uint32\_t index

frame interval index during enumeration

**Definition** video.h:193

[video\_frmival\_enum::format](structvideo__frmival__enum.md#a8c103777cd5db24a2197ef994b8d008d)

const struct video\_format \* format

video format for which the query is made

**Definition** video.h:195

[video\_frmival\_enum::stepwise](structvideo__frmival__enum.md#aa3fda4e99646bff1d902198437982124)

struct video\_frmival\_stepwise stepwise

**Definition** video.h:201

[video\_frmival\_enum::type](structvideo__frmival__enum.md#aec62b54ed1152d6b3ea80c24ce7624f7)

enum video\_frmival\_type type

frame interval type the device supports

**Definition** video.h:197

[video\_frmival\_enum::discrete](structvideo__frmival__enum.md#af22ef303cdc75fd48b698ff72b57354c)

struct video\_frmival discrete

**Definition** video.h:200

[video\_frmival\_stepwise](structvideo__frmival__stepwise.md)

Video frame interval stepwise structure.

**Definition** video.h:176

[video\_frmival\_stepwise::min](structvideo__frmival__stepwise.md#aec892104241a9d4204c87af51765ee2f)

struct video\_frmival min

minimum frame interval in seconds

**Definition** video.h:178

[video\_frmival\_stepwise::max](structvideo__frmival__stepwise.md#af1c5a40da9fe7ad30185464eccf5b438)

struct video\_frmival max

maximum frame interval in seconds

**Definition** video.h:180

[video\_frmival\_stepwise::step](structvideo__frmival__stepwise.md#afc3c4e4fe3641952c4e6fc494fa85760)

struct video\_frmival step

frame interval step size in seconds

**Definition** video.h:182

[video\_frmival](structvideo__frmival.md)

Video frame interval structure.

**Definition** video.h:163

[video\_frmival::numerator](structvideo__frmival.md#a57ee282f01da0f1ef1db2558d777631c)

uint32\_t numerator

numerator of the frame interval

**Definition** video.h:165

[video\_frmival::denominator](structvideo__frmival.md#aba4a6700ea733c3b07ee6445856c580a)

uint32\_t denominator

denominator of the frame interval

**Definition** video.h:167

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video.h](video_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
