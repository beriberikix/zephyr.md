---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/video_8h_source.html
original_path: doxygen/html/video_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

30#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

36

[ 43](structvideo__format.md)struct [video\_format](structvideo__format.md) {

[ 45](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pixelformat](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef);

[ 47](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693);

[ 49](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0);

[ 57](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pitch](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6);

58};

59

60

[ 67](structvideo__format__cap.md)struct [video\_format\_cap](structvideo__format__cap.md) {

[ 69](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pixelformat](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59);

[ 71](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width\_min](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9);

[ 73](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width\_max](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66);

[ 75](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height\_min](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35);

[ 77](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height\_max](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f);

[ 79](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [width\_step](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad);

[ 81](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [height\_step](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e);

82};

83

[ 90](structvideo__caps.md)struct [video\_caps](structvideo__caps.md) {

[ 92](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185) const struct [video\_format\_cap](structvideo__format__cap.md) \*[format\_caps](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185);

[ 96](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_vbuf\_count](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a);

97};

98

[ 105](structvideo__buffer.md)struct [video\_buffer](structvideo__buffer.md) {

[ 107](structvideo__buffer.md#ab184d528487042650af105eb7d37381e) void \*[driver\_data](structvideo__buffer.md#ab184d528487042650af105eb7d37381e);

[ 109](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3);

[ 111](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b);

[ 113](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bytesused](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1);

[ 118](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba);

119};

120

[ 126](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9)enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) {

[ 127](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7) [VIDEO\_EP\_NONE](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7),

[ 128](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a450d124253f8463114b851b1e51960fb) [VIDEO\_EP\_ANY](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a450d124253f8463114b851b1e51960fb),

[ 129](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7) [VIDEO\_EP\_IN](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7),

[ 130](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a) [VIDEO\_EP\_OUT](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a),

131};

132

[ 138](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8)enum [video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8) {

[ 139](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8) [VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8),

[ 140](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8) [VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8),

[ 141](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3) [VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3),

142};

143

[ 150](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18)typedef int (\*[video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18))(const struct [device](structdevice.md) \*dev,

151 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

152 struct [video\_format](structvideo__format.md) \*fmt);

153

[ 160](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d)typedef int (\*[video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d))(const struct [device](structdevice.md) \*dev,

161 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

162 struct [video\_format](structvideo__format.md) \*fmt);

163

[ 170](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe)typedef int (\*[video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe))(const struct [device](structdevice.md) \*dev,

171 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

172 struct [video\_buffer](structvideo__buffer.md) \*buf);

173

[ 180](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d)typedef int (\*[video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d))(const struct [device](structdevice.md) \*dev,

181 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

182 struct [video\_buffer](structvideo__buffer.md) \*\*buf,

183 [k\_timeout\_t](structk__timeout__t.md) timeout);

184

[ 192](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db)typedef int (\*[video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db))(const struct [device](structdevice.md) \*dev,

193 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

194 bool cancel);

195

[ 202](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e)typedef int (\*[video\_api\_stream\_start\_t](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e))(const struct [device](structdevice.md) \*dev);

203

[ 210](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd)typedef int (\*[video\_api\_stream\_stop\_t](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd))(const struct [device](structdevice.md) \*dev);

211

[ 218](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a)typedef int (\*[video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a))(const struct [device](structdevice.md) \*dev,

219 unsigned int cid,

220 void \*value);

221

[ 228](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c)typedef int (\*[video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c))(const struct [device](structdevice.md) \*dev,

229 unsigned int cid,

230 void \*value);

231

[ 238](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312)typedef int (\*[video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312))(const struct [device](structdevice.md) \*dev,

239 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

240 struct [video\_caps](structvideo__caps.md) \*caps);

241

[ 248](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321)typedef int (\*[video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321))(const struct [device](structdevice.md) \*dev,

249 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

250 struct [k\_poll\_signal](structk__poll__signal.md) \*signal);

251

[ 252](structvideo__driver__api.md)\_\_subsystem struct [video\_driver\_api](structvideo__driver__api.md) {

253 /\* mandatory callbacks \*/

[ 254](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8) [video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18) [set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8);

[ 255](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4) [video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d) [get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4);

[ 256](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc) [video\_api\_stream\_start\_t](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e) [stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc);

[ 257](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c) [video\_api\_stream\_stop\_t](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd) [stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c);

[ 258](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078) [video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312) [get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078);

259 /\* optional callbacks \*/

[ 260](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75) [video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe) [enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75);

[ 261](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef) [video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d) [dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef);

[ 262](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6) [video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db) [flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6);

[ 263](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8) [video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a) [set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8);

[ 264](structvideo__driver__api.md#a40bc476e1e89c42ef78cb99e98d83b38) [video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a) [get\_ctrl](structvideo__driver__api.md#a40bc476e1e89c42ef78cb99e98d83b38);

[ 265](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2) [video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321) [set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2);

266};

267

[ 282](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)static inline int [video\_set\_format](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)(const struct [device](structdevice.md) \*dev,

283 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

284 struct [video\_format](structvideo__format.md) \*fmt)

285{

286 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

287 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

288

289 if (api->[set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8) == NULL) {

290 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

291 }

292

293 return api->[set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8)(dev, ep, fmt);

294}

295

[ 307](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)static inline int [video\_get\_format](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)(const struct [device](structdevice.md) \*dev,

308 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

309 struct [video\_format](structvideo__format.md) \*fmt)

310{

311 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

312 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

313

314 if (api->[get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4) == NULL) {

315 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

316 }

317

318 return api->[get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4)(dev, ep, fmt);

319}

320

[ 335](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)static inline int [video\_enqueue](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)(const struct [device](structdevice.md) \*dev,

336 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

337 struct [video\_buffer](structvideo__buffer.md) \*buf)

338{

339 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

340 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

341

342 if (api->[enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75) == NULL) {

343 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

344 }

345

346 return api->[enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75)(dev, ep, buf);

347}

348

[ 364](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)static inline int [video\_dequeue](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)(const struct [device](structdevice.md) \*dev,

365 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

366 struct [video\_buffer](structvideo__buffer.md) \*\*buf,

367 [k\_timeout\_t](structk__timeout__t.md) timeout)

368{

369 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

370 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

371

372 if (api->[dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef) == NULL) {

373 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

374 }

375

376 return api->[dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef)(dev, ep, buf, timeout);

377}

378

379

[ 394](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)static inline int [video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)(const struct [device](structdevice.md) \*dev,

395 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

396 bool cancel)

397{

398 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

399 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

400

401 if (api->[flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6) == NULL) {

402 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

403 }

404

405 return api->[flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6)(dev, ep, cancel);

406}

407

[ 420](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)static inline int [video\_stream\_start](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)(const struct [device](structdevice.md) \*dev)

421{

422 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

423 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

424

425 if (api->[stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc) == NULL) {

426 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

427 }

428

429 return api->[stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc)(dev);

430}

431

[ 441](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)static inline int [video\_stream\_stop](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)(const struct [device](structdevice.md) \*dev)

442{

443 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

444 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

445 int ret;

446

447 if (api->[stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c) == NULL) {

448 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

449 }

450

451 ret = api->[stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c)(dev);

452 [video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)(dev, [VIDEO\_EP\_ANY](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a450d124253f8463114b851b1e51960fb), true);

453

454 return ret;

455}

456

[ 466](group__video__interface.md#ga4d5237607c858708380955705a2023bd)static inline int [video\_get\_caps](group__video__interface.md#ga4d5237607c858708380955705a2023bd)(const struct [device](structdevice.md) \*dev,

467 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

468 struct [video\_caps](structvideo__caps.md) \*caps)

469{

470 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

471 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

472

473 if (api->[get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078) == NULL) {

474 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

475 }

476

477 return api->[get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078)(dev, ep, caps);

478}

479

[ 495](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)static inline int [video\_set\_ctrl](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)(const struct [device](structdevice.md) \*dev, unsigned int cid,

496 void \*value)

497{

498 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

499 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

500

501 if (api->[set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8) == NULL) {

502 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

503 }

504

505 return api->[set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8)(dev, cid, value);

506}

507

[ 523](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)static inline int [video\_get\_ctrl](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)(const struct [device](structdevice.md) \*dev, unsigned int cid,

524 void \*value)

525{

526 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

527 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

528

529 if (api->[get\_ctrl](structvideo__driver__api.md#a40bc476e1e89c42ef78cb99e98d83b38) == NULL) {

530 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

531 }

532

533 return api->[get\_ctrl](structvideo__driver__api.md#a40bc476e1e89c42ef78cb99e98d83b38)(dev, cid, value);

534}

535

[ 549](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)static inline int [video\_set\_signal](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)(const struct [device](structdevice.md) \*dev,

550 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

551 struct [k\_poll\_signal](structk__poll__signal.md) \*signal)

552{

553 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

554 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

555

556 if (api->[set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2) == NULL) {

557 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

558 }

559

560 return api->[set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2)(dev, ep, signal);

561}

562

[ 571](group__video__interface.md#ga9c734ef73159af10a0ca799a188ee096)struct [video\_buffer](structvideo__buffer.md) \*[video\_buffer\_aligned\_alloc](group__video__interface.md#ga9c734ef73159af10a0ca799a188ee096)(size\_t [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b), size\_t align);

572

[ 580](group__video__interface.md#ga8454f5568e24cf7b8a59dde765b4a804)struct [video\_buffer](structvideo__buffer.md) \*[video\_buffer\_alloc](group__video__interface.md#ga8454f5568e24cf7b8a59dde765b4a804)(size\_t [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b));

581

[ 587](group__video__interface.md#gad2661653db019b673153001b2c61b10f)void [video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f)(struct [video\_buffer](structvideo__buffer.md) \*buf);

588

589

590/\* fourcc - four-character-code \*/

[ 591](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)#define video\_fourcc(a, b, c, d)\

592 ((uint32\_t)(a) | ((uint32\_t)(b) << 8) | ((uint32\_t)(c) << 16) | ((uint32\_t)(d) << 24))

593

594

599

604

[ 606](group__video__pixel__formats.md#ga64ad74bb6c92041a4190614b684ae024)#define VIDEO\_PIX\_FMT\_BGGR8 video\_fourcc('B', 'G', 'G', 'R') /\* 8 BGBG.. GRGR.. \*/

[ 608](group__video__pixel__formats.md#gaebdfd9d4230b56f6b8533630356b8793)#define VIDEO\_PIX\_FMT\_GBRG8 video\_fourcc('G', 'B', 'R', 'G') /\* 8 GBGB.. RGRG.. \*/

[ 610](group__video__pixel__formats.md#ga6b9c8d43406e45927f4e9e94504eae9c)#define VIDEO\_PIX\_FMT\_GRBG8 video\_fourcc('G', 'R', 'B', 'G') /\* 8 GRGR.. BGBG.. \*/

[ 612](group__video__pixel__formats.md#ga0c98dc205b724c9e4556e41cc266d80e)#define VIDEO\_PIX\_FMT\_RGGB8 video\_fourcc('R', 'G', 'G', 'B') /\* 8 RGRG.. GBGB.. \*/

613

617

622

[ 624](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)#define VIDEO\_PIX\_FMT\_RGB565 video\_fourcc('R', 'G', 'B', 'P') /\* 16 RGB-5-6-5 \*/

625

[ 627](group__video__pixel__formats.md#ga8be24c04210f8818d75082bd710db8b1)#define VIDEO\_PIX\_FMT\_XRGB32 video\_fourcc('B', 'X', '2', '4') /\* 32 XRGB-8-8-8-8 \*/

628

632

637

[ 639](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)#define VIDEO\_PIX\_FMT\_YUYV video\_fourcc('Y', 'U', 'Y', 'V') /\* 16 Y0-Cb0 Y1-Cr0 \*/

640

[ 642](group__video__pixel__formats.md#ga017bcbec587314f569d6d0e4fbdda351)#define VIDEO\_PIX\_FMT\_XYUV32 video\_fourcc('X', 'Y', 'U', 'V') /\* 32 XYUV-8-8-8-8 \*/

643

648

653

[ 655](group__video__pixel__formats.md#ga035a13c38c4f123411547e2c40d58bd2)#define VIDEO\_PIX\_FMT\_JPEG video\_fourcc('J', 'P', 'E', 'G') /\* 8 JPEG \*/

656

660

664

665#ifdef \_\_cplusplus

666}

667#endif

668

672

673#endif /\* ZEPHYR\_INCLUDE\_VIDEO\_H\_ \*/

[device.h](device_8h.md)

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[video\_api\_stream\_start\_t](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e)

int(\* video\_api\_stream\_start\_t)(const struct device \*dev)

Start the capture or output process.

**Definition** video.h:202

[video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8)

video\_signal\_result

video\_event enum

**Definition** video.h:138

[video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe)

int(\* video\_api\_enqueue\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*buf)

Enqueue a buffer in the driver’s incoming queue.

**Definition** video.h:170

[video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d)

int(\* video\_api\_dequeue\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*\*buf, k\_timeout\_t timeout)

Dequeue a buffer from the driver’s outgoing queue.

**Definition** video.h:180

[video\_get\_caps](group__video__interface.md#ga4d5237607c858708380955705a2023bd)

static int video\_get\_caps(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_caps \*caps)

Get the capabilities of a video endpoint.

**Definition** video.h:466

[video\_api\_stream\_stop\_t](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd)

int(\* video\_api\_stream\_stop\_t)(const struct device \*dev)

Stop the capture or output process.

**Definition** video.h:210

[video\_stream\_stop](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)

static int video\_stream\_stop(const struct device \*dev)

Stop the video device function.

**Definition** video.h:441

[video\_get\_ctrl](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)

static int video\_get\_ctrl(const struct device \*dev, unsigned int cid, void \*value)

Get the current value of a control.

**Definition** video.h:523

[video\_stream\_start](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)

static int video\_stream\_start(const struct device \*dev)

Start the video device function.

**Definition** video.h:420

[video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d)

int(\* video\_api\_get\_format\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Get current video format.

**Definition** video.h:160

[video\_buffer\_alloc](group__video__interface.md#ga8454f5568e24cf7b8a59dde765b4a804)

struct video\_buffer \* video\_buffer\_alloc(size\_t size)

Allocate video buffer.

[video\_set\_ctrl](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)

static int video\_set\_ctrl(const struct device \*dev, unsigned int cid, void \*value)

Set the value of a control.

**Definition** video.h:495

[video\_dequeue](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)

static int video\_dequeue(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*\*buf, k\_timeout\_t timeout)

Dequeue a video buffer.

**Definition** video.h:364

[video\_buffer\_aligned\_alloc](group__video__interface.md#ga9c734ef73159af10a0ca799a188ee096)

struct video\_buffer \* video\_buffer\_aligned\_alloc(size\_t size, size\_t align)

Allocate aligned video buffer.

[video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321)

int(\* video\_api\_set\_signal\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct k\_poll\_signal \*signal)

Register/Unregister poll signal for buffer events.

**Definition** video.h:248

[video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c)

int(\* video\_api\_get\_ctrl\_t)(const struct device \*dev, unsigned int cid, void \*value)

Get a video control value.

**Definition** video.h:228

[video\_set\_signal](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)

static int video\_set\_signal(const struct device \*dev, enum video\_endpoint\_id ep, struct k\_poll\_signal \*signal)

Register/Unregister k\_poll signal for a video endpoint.

**Definition** video.h:549

[video\_get\_format](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)

static int video\_get\_format(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Get video format.

**Definition** video.h:307

[video\_enqueue](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)

static int video\_enqueue(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*buf)

Enqueue a video buffer.

**Definition** video.h:335

[video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f)

void video\_buffer\_release(struct video\_buffer \*buf)

Release a video buffer.

[video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db)

int(\* video\_api\_flush\_t)(const struct device \*dev, enum video\_endpoint\_id ep, bool cancel)

Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue.

**Definition** video.h:192

[video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a)

int(\* video\_api\_set\_ctrl\_t)(const struct device \*dev, unsigned int cid, void \*value)

Set a video control value.

**Definition** video.h:218

[video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312)

int(\* video\_api\_get\_caps\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_caps \*caps)

Get capabilities of a video endpoint.

**Definition** video.h:238

[video\_set\_format](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)

static int video\_set\_format(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Set video format.

**Definition** video.h:282

[video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)

static int video\_flush(const struct device \*dev, enum video\_endpoint\_id ep, bool cancel)

Flush endpoint buffers.

**Definition** video.h:394

[video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18)

int(\* video\_api\_set\_format\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Set video format.

**Definition** video.h:150

[video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9)

video\_endpoint\_id

video\_endpoint\_id enum

**Definition** video.h:126

[VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8)

@ VIDEO\_BUF\_ABORTED

**Definition** video.h:140

[VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8)

@ VIDEO\_BUF\_DONE

**Definition** video.h:139

[VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3)

@ VIDEO\_BUF\_ERROR

**Definition** video.h:141

[VIDEO\_EP\_IN](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7)

@ VIDEO\_EP\_IN

**Definition** video.h:129

[VIDEO\_EP\_NONE](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7)

@ VIDEO\_EP\_NONE

**Definition** video.h:127

[VIDEO\_EP\_ANY](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a450d124253f8463114b851b1e51960fb)

@ VIDEO\_EP\_ANY

**Definition** video.h:128

[VIDEO\_EP\_OUT](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a)

@ VIDEO\_EP\_OUT

**Definition** video.h:130

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

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5691

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[video\_buffer](structvideo__buffer.md)

Video buffer structure.

**Definition** video.h:105

[video\_buffer::bytesused](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1)

uint32\_t bytesused

number of bytes occupied by the valid data in the buffer.

**Definition** video.h:113

[video\_buffer::size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b)

uint32\_t size

size of the buffer in bytes.

**Definition** video.h:111

[video\_buffer::buffer](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3)

uint8\_t \* buffer

pointer to the start of the buffer.

**Definition** video.h:109

[video\_buffer::driver\_data](structvideo__buffer.md#ab184d528487042650af105eb7d37381e)

void \* driver\_data

pointer to driver specific data.

**Definition** video.h:107

[video\_buffer::timestamp](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba)

uint32\_t timestamp

time reference in milliseconds at which the last data byte was actually received for input endpoints ...

**Definition** video.h:118

[video\_caps](structvideo__caps.md)

Video format capabilities.

**Definition** video.h:90

[video\_caps::min\_vbuf\_count](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a)

uint8\_t min\_vbuf\_count

minimal count of video buffers to enqueue before being able to start the stream.

**Definition** video.h:96

[video\_caps::format\_caps](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185)

const struct video\_format\_cap \* format\_caps

list of video format capabilities (zero terminated).

**Definition** video.h:92

[video\_driver\_api](structvideo__driver__api.md)

**Definition** video.h:252

[video\_driver\_api::stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c)

video\_api\_stream\_stop\_t stream\_stop

**Definition** video.h:257

[video\_driver\_api::set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8)

video\_api\_set\_ctrl\_t set\_ctrl

**Definition** video.h:263

[video\_driver\_api::stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc)

video\_api\_stream\_start\_t stream\_start

**Definition** video.h:256

[video\_driver\_api::get\_ctrl](structvideo__driver__api.md#a40bc476e1e89c42ef78cb99e98d83b38)

video\_api\_set\_ctrl\_t get\_ctrl

**Definition** video.h:264

[video\_driver\_api::enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75)

video\_api\_enqueue\_t enqueue

**Definition** video.h:260

[video\_driver\_api::set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2)

video\_api\_set\_signal\_t set\_signal

**Definition** video.h:265

[video\_driver\_api::get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4)

video\_api\_get\_format\_t get\_format

**Definition** video.h:255

[video\_driver\_api::get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078)

video\_api\_get\_caps\_t get\_caps

**Definition** video.h:258

[video\_driver\_api::set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8)

video\_api\_set\_format\_t set\_format

**Definition** video.h:254

[video\_driver\_api::flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6)

video\_api\_flush\_t flush

**Definition** video.h:262

[video\_driver\_api::dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef)

video\_api\_dequeue\_t dequeue

**Definition** video.h:261

[video\_format\_cap](structvideo__format__cap.md)

Video format capability.

**Definition** video.h:67

[video\_format\_cap::height\_step](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e)

uint16\_t height\_step

height step size in pixels.

**Definition** video.h:81

[video\_format\_cap::width\_min](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9)

uint32\_t width\_min

minimum supported frame width in pixels.

**Definition** video.h:71

[video\_format\_cap::width\_max](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66)

uint32\_t width\_max

maximum supported frame width in pixels.

**Definition** video.h:73

[video\_format\_cap::width\_step](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad)

uint16\_t width\_step

width step size in pixels.

**Definition** video.h:79

[video\_format\_cap::height\_max](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f)

uint32\_t height\_max

maximum supported frame height in pixels.

**Definition** video.h:77

[video\_format\_cap::height\_min](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35)

uint32\_t height\_min

minimum supported frame height in pixels.

**Definition** video.h:75

[video\_format\_cap::pixelformat](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59)

uint32\_t pixelformat

FourCC pixel format value (Video pixel formats).

**Definition** video.h:69

[video\_format](structvideo__format.md)

Video format structure.

**Definition** video.h:43

[video\_format::height](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0)

uint32\_t height

frame height in pixels.

**Definition** video.h:49

[video\_format::width](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693)

uint32\_t width

frame width in pixels.

**Definition** video.h:47

[video\_format::pitch](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6)

uint32\_t pitch

line stride.

**Definition** video.h:57

[video\_format::pixelformat](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef)

uint32\_t pixelformat

FourCC pixel format value (Video pixel formats).

**Definition** video.h:45

[video-controls.h](video-controls_8h.md)

Public APIs for Video.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video.h](video_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
