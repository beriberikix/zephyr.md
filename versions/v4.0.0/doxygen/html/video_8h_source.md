---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/video_8h_source.html
original_path: doxygen/html/video_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

[ 310](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e)typedef int (\*[video\_api\_stream\_start\_t](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e))(const struct [device](structdevice.md) \*dev);

311

[ 318](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd)typedef int (\*[video\_api\_stream\_stop\_t](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd))(const struct [device](structdevice.md) \*dev);

319

[ 326](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a)typedef int (\*[video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a))(const struct [device](structdevice.md) \*dev, unsigned int cid, void \*value);

327

[ 334](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c)typedef int (\*[video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c))(const struct [device](structdevice.md) \*dev, unsigned int cid, void \*value);

335

[ 342](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312)typedef int (\*[video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

343 struct [video\_caps](structvideo__caps.md) \*caps);

344

[ 351](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321)typedef int (\*[video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321))(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

352 struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69));

353

[ 354](structvideo__driver__api.md)\_\_subsystem struct [video\_driver\_api](structvideo__driver__api.md) {

355 /\* mandatory callbacks \*/

[ 356](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8) [video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18) [set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8);

[ 357](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4) [video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d) [get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4);

[ 358](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc) [video\_api\_stream\_start\_t](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e) [stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc);

[ 359](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c) [video\_api\_stream\_stop\_t](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd) [stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c);

[ 360](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078) [video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312) [get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078);

361 /\* optional callbacks \*/

[ 362](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75) [video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe) [enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75);

[ 363](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef) [video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d) [dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef);

[ 364](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6) [video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db) [flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6);

[ 365](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8) [video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a) [set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8);

[ 366](structvideo__driver__api.md#ab5e5176079fcba90bd57a6ce19adcaeb) [video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c) [get\_ctrl](structvideo__driver__api.md#ab5e5176079fcba90bd57a6ce19adcaeb);

[ 367](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2) [video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321) [set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2);

[ 368](structvideo__driver__api.md#ae10587ed4c5cc43f244209b1f18ddc68) [video\_api\_set\_frmival\_t](group__video__interface.md#gac69b1ab2877112983b421c650076da89) [set\_frmival](structvideo__driver__api.md#ae10587ed4c5cc43f244209b1f18ddc68);

[ 369](structvideo__driver__api.md#acce22c3f6185c2777bbeda4f32e84940) [video\_api\_get\_frmival\_t](group__video__interface.md#gaa7fae28aae3959ea09f9ffc87fa42c7e) [get\_frmival](structvideo__driver__api.md#acce22c3f6185c2777bbeda4f32e84940);

[ 370](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726) [video\_api\_enum\_frmival\_t](group__video__interface.md#gab8bd3f3a430e6872facad2749d7f2240) [enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726);

371};

372

[ 387](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)static inline int [video\_set\_format](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

388 struct [video\_format](structvideo__format.md) \*fmt)

389{

390 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

391

392 if (api->[set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8) == NULL) {

393 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

394 }

395

396 return api->[set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8)(dev, ep, fmt);

397}

398

[ 410](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)static inline int [video\_get\_format](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

411 struct [video\_format](structvideo__format.md) \*fmt)

412{

413 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

414

415 if (api->[get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4) == NULL) {

416 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

417 }

418

419 return api->[get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4)(dev, ep, fmt);

420}

421

[ 439](group__video__interface.md#ga50149acd5c56d237c5a6988bdf1cc241)static inline int [video\_set\_frmival](group__video__interface.md#ga50149acd5c56d237c5a6988bdf1cc241)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

440 struct [video\_frmival](structvideo__frmival.md) \*frmival)

441{

442 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

443

444 if (api->[set\_frmival](structvideo__driver__api.md#ae10587ed4c5cc43f244209b1f18ddc68) == NULL) {

445 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

446 }

447

448 return api->[set\_frmival](structvideo__driver__api.md#ae10587ed4c5cc43f244209b1f18ddc68)(dev, ep, frmival);

449}

450

[ 465](group__video__interface.md#gaa7a61a51424e0d030b87ec52ceb8dc07)static inline int [video\_get\_frmival](group__video__interface.md#gaa7a61a51424e0d030b87ec52ceb8dc07)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

466 struct [video\_frmival](structvideo__frmival.md) \*frmival)

467{

468 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

469

470 if (api->[get\_frmival](structvideo__driver__api.md#acce22c3f6185c2777bbeda4f32e84940) == NULL) {

471 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

472 }

473

474 return api->[get\_frmival](structvideo__driver__api.md#acce22c3f6185c2777bbeda4f32e84940)(dev, ep, frmival);

475}

476

[ 495](group__video__interface.md#gabd7f2fe113e3ade441a1d6cce66c1cda)static inline int [video\_enum\_frmival](group__video__interface.md#gabd7f2fe113e3ade441a1d6cce66c1cda)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

496 struct [video\_frmival\_enum](structvideo__frmival__enum.md) \*fie)

497{

498 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

499

500 if (api->[enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726) == NULL) {

501 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

502 }

503

504 return api->[enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726)(dev, ep, fie);

505}

506

[ 521](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)static inline int [video\_enqueue](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

522 struct [video\_buffer](structvideo__buffer.md) \*buf)

523{

524 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

525

526 if (api->[enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75) == NULL) {

527 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

528 }

529

530 return api->[enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75)(dev, ep, buf);

531}

532

[ 548](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)static inline int [video\_dequeue](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

549 struct [video\_buffer](structvideo__buffer.md) \*\*buf, [k\_timeout\_t](structk__timeout__t.md) timeout)

550{

551 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

552

553 if (api->[dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef) == NULL) {

554 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

555 }

556

557 return api->[dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef)(dev, ep, buf, timeout);

558}

559

[ 574](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)static inline int [video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep, bool cancel)

575{

576 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

577

578 if (api->[flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6) == NULL) {

579 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

580 }

581

582 return api->[flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6)(dev, ep, cancel);

583}

584

[ 597](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)static inline int [video\_stream\_start](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)(const struct [device](structdevice.md) \*dev)

598{

599 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

600

601 if (api->[stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc) == NULL) {

602 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

603 }

604

605 return api->[stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc)(dev);

606}

607

[ 617](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)static inline int [video\_stream\_stop](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)(const struct [device](structdevice.md) \*dev)

618{

619 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

620 int ret;

621

622 if (api->[stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c) == NULL) {

623 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

624 }

625

626 ret = api->[stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c)(dev);

627 [video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)(dev, [VIDEO\_EP\_ALL](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9afb3b8e141a5675a7d299b82dca5f36a9), true);

628

629 return ret;

630}

631

[ 641](group__video__interface.md#ga4d5237607c858708380955705a2023bd)static inline int [video\_get\_caps](group__video__interface.md#ga4d5237607c858708380955705a2023bd)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

642 struct [video\_caps](structvideo__caps.md) \*caps)

643{

644 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

645

646 if (api->[get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078) == NULL) {

647 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

648 }

649

650 return api->[get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078)(dev, ep, caps);

651}

652

[ 668](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)static inline int [video\_set\_ctrl](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)(const struct [device](structdevice.md) \*dev, unsigned int cid, void \*value)

669{

670 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

671

672 if (api->[set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8) == NULL) {

673 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

674 }

675

676 return api->[set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8)(dev, cid, value);

677}

678

[ 694](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)static inline int [video\_get\_ctrl](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)(const struct [device](structdevice.md) \*dev, unsigned int cid, void \*value)

695{

696 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

697

698 if (api->[get\_ctrl](structvideo__driver__api.md#ab5e5176079fcba90bd57a6ce19adcaeb) == NULL) {

699 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

700 }

701

702 return api->[get\_ctrl](structvideo__driver__api.md#ab5e5176079fcba90bd57a6ce19adcaeb)(dev, cid, value);

703}

704

[ 718](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)static inline int [video\_set\_signal](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)(const struct [device](structdevice.md) \*dev, enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

719 struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69))

720{

721 const struct [video\_driver\_api](structvideo__driver__api.md) \*api = (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

722

723 if (api->[set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2) == NULL) {

724 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

725 }

726

727 return api->[set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2)(dev, ep, [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69));

728}

729

[ 738](group__video__interface.md#ga9c734ef73159af10a0ca799a188ee096)struct [video\_buffer](structvideo__buffer.md) \*[video\_buffer\_aligned\_alloc](group__video__interface.md#ga9c734ef73159af10a0ca799a188ee096)(size\_t [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b), size\_t align);

739

[ 747](group__video__interface.md#ga8454f5568e24cf7b8a59dde765b4a804)struct [video\_buffer](structvideo__buffer.md) \*[video\_buffer\_alloc](group__video__interface.md#ga8454f5568e24cf7b8a59dde765b4a804)(size\_t [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b));

748

[ 754](group__video__interface.md#gad2661653db019b673153001b2c61b10f)void [video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f)(struct [video\_buffer](structvideo__buffer.md) \*buf);

755

756/\* fourcc - four-character-code \*/

[ 757](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)#define video\_fourcc(a, b, c, d) \

758 ((uint32\_t)(a) | ((uint32\_t)(b) << 8) | ((uint32\_t)(c) << 16) | ((uint32\_t)(d) << 24))

759

764

769

[ 771](group__video__pixel__formats.md#ga64ad74bb6c92041a4190614b684ae024)#define VIDEO\_PIX\_FMT\_BGGR8 video\_fourcc('B', 'G', 'G', 'R') /\* 8 BGBG.. GRGR.. \*/

[ 773](group__video__pixel__formats.md#gaebdfd9d4230b56f6b8533630356b8793)#define VIDEO\_PIX\_FMT\_GBRG8 video\_fourcc('G', 'B', 'R', 'G') /\* 8 GBGB.. RGRG.. \*/

[ 775](group__video__pixel__formats.md#ga6b9c8d43406e45927f4e9e94504eae9c)#define VIDEO\_PIX\_FMT\_GRBG8 video\_fourcc('G', 'R', 'B', 'G') /\* 8 GRGR.. BGBG.. \*/

[ 777](group__video__pixel__formats.md#ga0c98dc205b724c9e4556e41cc266d80e)#define VIDEO\_PIX\_FMT\_RGGB8 video\_fourcc('R', 'G', 'G', 'B') /\* 8 RGRG.. GBGB.. \*/

778

782

787

[ 789](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)#define VIDEO\_PIX\_FMT\_RGB565 video\_fourcc('R', 'G', 'B', 'P') /\* 16 RGB-5-6-5 \*/

790

[ 792](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1)#define VIDEO\_PIX\_FMT\_XRGB32 video\_fourcc('B', 'X', '2', '4') /\* 32 XRGB-8-8-8-8 \*/

793

797

802

[ 804](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)#define VIDEO\_PIX\_FMT\_YUYV video\_fourcc('Y', 'U', 'Y', 'V') /\* 16 Y0-Cb0 Y1-Cr0 \*/

805

[ 807](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351)#define VIDEO\_PIX\_FMT\_XYUV32 video\_fourcc('X', 'Y', 'U', 'V') /\* 32 XYUV-8-8-8-8 \*/

808

813

818

[ 820](group__video__pixel__formats.md#ga035a13c38c4f123411547e2c40d58bd2)#define VIDEO\_PIX\_FMT\_JPEG video\_fourcc('J', 'P', 'E', 'G') /\* 8 JPEG \*/

821

825

829

[ 835](group__video__interface.md#gabc1c6fd4e13480b269cac9f224ee1c5b)static inline unsigned int [video\_pix\_fmt\_bpp](group__video__interface.md#gabc1c6fd4e13480b269cac9f224ee1c5b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pixfmt)

836{

837 switch (pixfmt) {

838 case [VIDEO\_PIX\_FMT\_BGGR8](group__video__pixel__formats.md#ga64ad74bb6c92041a4190614b684ae024):

839 case [VIDEO\_PIX\_FMT\_GBRG8](group__video__pixel__formats.md#gaebdfd9d4230b56f6b8533630356b8793):

840 case [VIDEO\_PIX\_FMT\_GRBG8](group__video__pixel__formats.md#ga6b9c8d43406e45927f4e9e94504eae9c):

841 case [VIDEO\_PIX\_FMT\_RGGB8](group__video__pixel__formats.md#ga0c98dc205b724c9e4556e41cc266d80e):

842 return 1;

843 case [VIDEO\_PIX\_FMT\_RGB565](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec):

844 case [VIDEO\_PIX\_FMT\_YUYV](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11):

845 return 2;

846 case [VIDEO\_PIX\_FMT\_XRGB32](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1):

847 case [VIDEO\_PIX\_FMT\_XYUV32](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351):

848 return 4;

849 default:

850 return 0;

851 }

852}

853

854#ifdef \_\_cplusplus

855}

856#endif

857

861

862#endif /\* ZEPHYR\_INCLUDE\_VIDEO\_H\_ \*/

[device.h](device_8h.md)

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[video\_api\_stream\_start\_t](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e)

int(\* video\_api\_stream\_start\_t)(const struct device \*dev)

Start the capture or output process.

**Definition** video.h:310

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

[video\_get\_caps](group__video__interface.md#ga4d5237607c858708380955705a2023bd)

static int video\_get\_caps(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_caps \*caps)

Get the capabilities of a video endpoint.

**Definition** video.h:641

[video\_set\_frmival](group__video__interface.md#ga50149acd5c56d237c5a6988bdf1cc241)

static int video\_set\_frmival(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival \*frmival)

Set video frame interval.

**Definition** video.h:439

[video\_api\_stream\_stop\_t](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd)

int(\* video\_api\_stream\_stop\_t)(const struct device \*dev)

Stop the capture or output process.

**Definition** video.h:318

[video\_stream\_stop](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)

static int video\_stream\_stop(const struct device \*dev)

Stop the video device function.

**Definition** video.h:617

[video\_get\_ctrl](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)

static int video\_get\_ctrl(const struct device \*dev, unsigned int cid, void \*value)

Get the current value of a control.

**Definition** video.h:694

[video\_frmival\_type](group__video__interface.md#ga6abf1fc9c35cf1d1648cde7616e7cad1)

video\_frmival\_type

video\_frmival\_type enum

**Definition** video.h:150

[video\_stream\_start](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)

static int video\_stream\_start(const struct device \*dev)

Start the video device function.

**Definition** video.h:597

[video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d)

int(\* video\_api\_get\_format\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Get current video format.

**Definition** video.h:247

[video\_buffer\_alloc](group__video__interface.md#ga8454f5568e24cf7b8a59dde765b4a804)

struct video\_buffer \* video\_buffer\_alloc(size\_t size)

Allocate video buffer.

[video\_set\_ctrl](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)

static int video\_set\_ctrl(const struct device \*dev, unsigned int cid, void \*value)

Set the value of a control.

**Definition** video.h:668

[video\_dequeue](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)

static int video\_dequeue(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*\*buf, k\_timeout\_t timeout)

Dequeue a video buffer.

**Definition** video.h:548

[video\_buffer\_aligned\_alloc](group__video__interface.md#ga9c734ef73159af10a0ca799a188ee096)

struct video\_buffer \* video\_buffer\_aligned\_alloc(size\_t size, size\_t align)

Allocate aligned video buffer.

[video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321)

int(\* video\_api\_set\_signal\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct k\_poll\_signal \*signal)

Register/Unregister poll signal for buffer events.

**Definition** video.h:351

[video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c)

int(\* video\_api\_get\_ctrl\_t)(const struct device \*dev, unsigned int cid, void \*value)

Get a video control value.

**Definition** video.h:334

[video\_get\_frmival](group__video__interface.md#gaa7a61a51424e0d030b87ec52ceb8dc07)

static int video\_get\_frmival(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival \*frmival)

Get video frame interval.

**Definition** video.h:465

[video\_api\_get\_frmival\_t](group__video__interface.md#gaa7fae28aae3959ea09f9ffc87fa42c7e)

int(\* video\_api\_get\_frmival\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival \*frmival)

Get current video frame interval.

**Definition** video.h:265

[video\_set\_signal](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)

static int video\_set\_signal(const struct device \*dev, enum video\_endpoint\_id ep, struct k\_poll\_signal \*signal)

Register/Unregister k\_poll signal for a video endpoint.

**Definition** video.h:718

[video\_api\_enum\_frmival\_t](group__video__interface.md#gab8bd3f3a430e6872facad2749d7f2240)

int(\* video\_api\_enum\_frmival\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival\_enum \*fie)

List all supported frame intervals of a given format.

**Definition** video.h:274

[video\_pix\_fmt\_bpp](group__video__interface.md#gabc1c6fd4e13480b269cac9f224ee1c5b)

static unsigned int video\_pix\_fmt\_bpp(uint32\_t pixfmt)

Get number of bytes per pixel of a pixel format.

**Definition** video.h:835

[video\_enum\_frmival](group__video__interface.md#gabd7f2fe113e3ade441a1d6cce66c1cda)

static int video\_enum\_frmival(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival\_enum \*fie)

List video frame intervals.

**Definition** video.h:495

[video\_get\_format](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)

static int video\_get\_format(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Get video format.

**Definition** video.h:410

[video\_enqueue](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)

static int video\_enqueue(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*buf)

Enqueue a video buffer.

**Definition** video.h:521

[video\_api\_set\_frmival\_t](group__video__interface.md#gac69b1ab2877112983b421c650076da89)

int(\* video\_api\_set\_frmival\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_frmival \*frmival)

Set video frame interval.

**Definition** video.h:256

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

**Definition** video.h:326

[video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312)

int(\* video\_api\_get\_caps\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_caps \*caps)

Get capabilities of a video endpoint.

**Definition** video.h:342

[video\_set\_format](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)

static int video\_set\_format(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Set video format.

**Definition** video.h:387

[video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)

static int video\_flush(const struct device \*dev, enum video\_endpoint\_id ep, bool cancel)

Flush endpoint buffers.

**Definition** video.h:574

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

XYUV32 pixel format.

**Definition** video.h:807

[VIDEO\_PIX\_FMT\_RGGB8](group__video__pixel__formats.md#ga0c98dc205b724c9e4556e41cc266d80e)

#define VIDEO\_PIX\_FMT\_RGGB8

RGGB8 pixel format.

**Definition** video.h:777

[VIDEO\_PIX\_FMT\_BGGR8](group__video__pixel__formats.md#ga64ad74bb6c92041a4190614b684ae024)

#define VIDEO\_PIX\_FMT\_BGGR8

BGGR8 pixel format.

**Definition** video.h:771

[VIDEO\_PIX\_FMT\_GRBG8](group__video__pixel__formats.md#ga6b9c8d43406e45927f4e9e94504eae9c)

#define VIDEO\_PIX\_FMT\_GRBG8

GRBG8 pixel format.

**Definition** video.h:775

[VIDEO\_PIX\_FMT\_XRGB32](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1)

#define VIDEO\_PIX\_FMT\_XRGB32

XRGB32 pixel format.

**Definition** video.h:792

[VIDEO\_PIX\_FMT\_YUYV](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)

#define VIDEO\_PIX\_FMT\_YUYV

YUYV pixel format.

**Definition** video.h:804

[VIDEO\_PIX\_FMT\_GBRG8](group__video__pixel__formats.md#gaebdfd9d4230b56f6b8533630356b8793)

#define VIDEO\_PIX\_FMT\_GBRG8

GBRG8 pixel format.

**Definition** video.h:773

[VIDEO\_PIX\_FMT\_RGB565](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)

#define VIDEO\_PIX\_FMT\_RGB565

RGB565 pixel format.

**Definition** video.h:789

[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)

sighandler\_t signal(int signo, sighandler\_t handler)

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

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

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5768

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

**Definition** video.h:354

[video\_driver\_api::stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c)

video\_api\_stream\_stop\_t stream\_stop

**Definition** video.h:359

[video\_driver\_api::set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8)

video\_api\_set\_ctrl\_t set\_ctrl

**Definition** video.h:365

[video\_driver\_api::stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc)

video\_api\_stream\_start\_t stream\_start

**Definition** video.h:358

[video\_driver\_api::enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75)

video\_api\_enqueue\_t enqueue

**Definition** video.h:362

[video\_driver\_api::set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2)

video\_api\_set\_signal\_t set\_signal

**Definition** video.h:367

[video\_driver\_api::get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4)

video\_api\_get\_format\_t get\_format

**Definition** video.h:357

[video\_driver\_api::enum\_frmival](structvideo__driver__api.md#a6481a76f3f4d33629bbebb29ef9e8726)

video\_api\_enum\_frmival\_t enum\_frmival

**Definition** video.h:370

[video\_driver\_api::get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078)

video\_api\_get\_caps\_t get\_caps

**Definition** video.h:360

[video\_driver\_api::set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8)

video\_api\_set\_format\_t set\_format

**Definition** video.h:356

[video\_driver\_api::flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6)

video\_api\_flush\_t flush

**Definition** video.h:364

[video\_driver\_api::dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef)

video\_api\_dequeue\_t dequeue

**Definition** video.h:363

[video\_driver\_api::get\_ctrl](structvideo__driver__api.md#ab5e5176079fcba90bd57a6ce19adcaeb)

video\_api\_get\_ctrl\_t get\_ctrl

**Definition** video.h:366

[video\_driver\_api::get\_frmival](structvideo__driver__api.md#acce22c3f6185c2777bbeda4f32e84940)

video\_api\_get\_frmival\_t get\_frmival

**Definition** video.h:369

[video\_driver\_api::set\_frmival](structvideo__driver__api.md#ae10587ed4c5cc43f244209b1f18ddc68)

video\_api\_set\_frmival\_t set\_frmival

**Definition** video.h:368

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
