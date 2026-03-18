---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/video_8h_source.html
original_path: doxygen/html/video_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

21

22#include <[zephyr/device.h](device_8h.md)>

23#include <stddef.h>

24#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27

28#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

34

[ 41](structvideo__format.md)struct [video\_format](structvideo__format.md) {

[ 43](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pixelformat](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef);

[ 45](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693);

[ 47](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0);

[ 55](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pitch](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6);

56};

57

58

[ 65](structvideo__format__cap.md)struct [video\_format\_cap](structvideo__format__cap.md) {

[ 67](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pixelformat](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59);

[ 69](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width\_min](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9);

[ 71](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [width\_max](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66);

[ 73](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height\_min](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35);

[ 75](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [height\_max](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f);

[ 77](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [width\_step](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad);

[ 79](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [height\_step](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e);

80};

81

[ 88](structvideo__caps.md)struct [video\_caps](structvideo__caps.md) {

[ 90](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185) const struct [video\_format\_cap](structvideo__format__cap.md) \*[format\_caps](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185);

[ 94](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_vbuf\_count](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a);

95};

96

[ 103](structvideo__buffer.md)struct [video\_buffer](structvideo__buffer.md) {

[ 105](structvideo__buffer.md#ab184d528487042650af105eb7d37381e) void \*[driver\_data](structvideo__buffer.md#ab184d528487042650af105eb7d37381e);

[ 107](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3);

[ 109](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b);

[ 111](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bytesused](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1);

[ 116](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba);

117};

118

[ 124](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9)enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) {

[ 125](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7) [VIDEO\_EP\_NONE](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7),

[ 126](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a450d124253f8463114b851b1e51960fb) [VIDEO\_EP\_ANY](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a450d124253f8463114b851b1e51960fb),

[ 127](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7) [VIDEO\_EP\_IN](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7),

[ 128](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a) [VIDEO\_EP\_OUT](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a),

129};

130

[ 136](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8)enum [video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8) {

[ 137](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8) [VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8),

[ 138](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8) [VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8),

[ 139](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3) [VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3),

140};

141

[ 148](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18)typedef int (\*[video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18))(const struct [device](structdevice.md) \*dev,

149 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

150 struct [video\_format](structvideo__format.md) \*fmt);

151

[ 158](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d)typedef int (\*[video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d))(const struct [device](structdevice.md) \*dev,

159 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

160 struct [video\_format](structvideo__format.md) \*fmt);

161

[ 168](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe)typedef int (\*[video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe))(const struct [device](structdevice.md) \*dev,

169 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

170 struct [video\_buffer](structvideo__buffer.md) \*buf);

171

[ 178](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d)typedef int (\*[video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d))(const struct [device](structdevice.md) \*dev,

179 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

180 struct [video\_buffer](structvideo__buffer.md) \*\*buf,

181 [k\_timeout\_t](structk__timeout__t.md) timeout);

182

[ 190](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db)typedef int (\*[video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db))(const struct [device](structdevice.md) \*dev,

191 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

192 bool cancel);

193

[ 200](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e)typedef int (\*[video\_api\_stream\_start\_t](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e))(const struct [device](structdevice.md) \*dev);

201

[ 208](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd)typedef int (\*[video\_api\_stream\_stop\_t](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd))(const struct [device](structdevice.md) \*dev);

209

[ 216](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a)typedef int (\*[video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a))(const struct [device](structdevice.md) \*dev,

217 unsigned int cid,

218 void \*value);

219

[ 226](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c)typedef int (\*[video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c))(const struct [device](structdevice.md) \*dev,

227 unsigned int cid,

228 void \*value);

229

[ 236](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312)typedef int (\*[video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312))(const struct [device](structdevice.md) \*dev,

237 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

238 struct [video\_caps](structvideo__caps.md) \*caps);

239

[ 246](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321)typedef int (\*[video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321))(const struct [device](structdevice.md) \*dev,

247 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

248 struct [k\_poll\_signal](structk__poll__signal.md) \*signal);

249

[ 250](structvideo__driver__api.md)struct [video\_driver\_api](structvideo__driver__api.md) {

251 /\* mandatory callbacks \*/

[ 252](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8) [video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18) [set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8);

[ 253](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4) [video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d) [get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4);

[ 254](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc) [video\_api\_stream\_start\_t](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e) [stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc);

[ 255](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c) [video\_api\_stream\_stop\_t](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd) [stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c);

[ 256](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078) [video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312) [get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078);

257 /\* optional callbacks \*/

[ 258](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75) [video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe) [enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75);

[ 259](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef) [video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d) [dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef);

[ 260](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6) [video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db) [flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6);

[ 261](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8) [video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a) [set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8);

[ 262](structvideo__driver__api.md#a40bc476e1e89c42ef78cb99e98d83b38) [video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a) [get\_ctrl](structvideo__driver__api.md#a40bc476e1e89c42ef78cb99e98d83b38);

[ 263](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2) [video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321) [set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2);

264};

265

[ 280](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)static inline int [video\_set\_format](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)(const struct [device](structdevice.md) \*dev,

281 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

282 struct [video\_format](structvideo__format.md) \*fmt)

283{

284 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

285 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

286

287 if (api->[set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8) == NULL) {

288 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

289 }

290

291 return api->[set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8)(dev, ep, fmt);

292}

293

[ 305](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)static inline int [video\_get\_format](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)(const struct [device](structdevice.md) \*dev,

306 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

307 struct [video\_format](structvideo__format.md) \*fmt)

308{

309 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

310 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

311

312 if (api->[get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4) == NULL) {

313 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

314 }

315

316 return api->[get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4)(dev, ep, fmt);

317}

318

[ 333](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)static inline int [video\_enqueue](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)(const struct [device](structdevice.md) \*dev,

334 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

335 struct [video\_buffer](structvideo__buffer.md) \*buf)

336{

337 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

338 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

339

340 if (api->[enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75) == NULL) {

341 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

342 }

343

344 return api->[enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75)(dev, ep, buf);

345}

346

[ 362](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)static inline int [video\_dequeue](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)(const struct [device](structdevice.md) \*dev,

363 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

364 struct [video\_buffer](structvideo__buffer.md) \*\*buf,

365 [k\_timeout\_t](structk__timeout__t.md) timeout)

366{

367 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

368 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

369

370 if (api->[dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef) == NULL) {

371 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

372 }

373

374 return api->[dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef)(dev, ep, buf, timeout);

375}

376

377

[ 392](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)static inline int [video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)(const struct [device](structdevice.md) \*dev,

393 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

394 bool cancel)

395{

396 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

397 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

398

399 if (api->[flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6) == NULL) {

400 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

401 }

402

403 return api->[flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6)(dev, ep, cancel);

404}

405

[ 418](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)static inline int [video\_stream\_start](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)(const struct [device](structdevice.md) \*dev)

419{

420 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

421 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

422

423 if (api->[stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc) == NULL) {

424 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

425 }

426

427 return api->[stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc)(dev);

428}

429

[ 439](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)static inline int [video\_stream\_stop](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)(const struct [device](structdevice.md) \*dev)

440{

441 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

442 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

443 int ret;

444

445 if (api->[stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c) == NULL) {

446 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

447 }

448

449 ret = api->[stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c)(dev);

450 [video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)(dev, [VIDEO\_EP\_ANY](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a450d124253f8463114b851b1e51960fb), true);

451

452 return ret;

453}

454

[ 464](group__video__interface.md#ga4d5237607c858708380955705a2023bd)static inline int [video\_get\_caps](group__video__interface.md#ga4d5237607c858708380955705a2023bd)(const struct [device](structdevice.md) \*dev,

465 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

466 struct [video\_caps](structvideo__caps.md) \*caps)

467{

468 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

469 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

470

471 if (api->[get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078) == NULL) {

472 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

473 }

474

475 return api->[get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078)(dev, ep, caps);

476}

477

[ 493](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)static inline int [video\_set\_ctrl](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)(const struct [device](structdevice.md) \*dev, unsigned int cid,

494 void \*value)

495{

496 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

497 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

498

499 if (api->[set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8) == NULL) {

500 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

501 }

502

503 return api->[set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8)(dev, cid, value);

504}

505

[ 521](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)static inline int [video\_get\_ctrl](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)(const struct [device](structdevice.md) \*dev, unsigned int cid,

522 void \*value)

523{

524 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

525 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

526

527 if (api->[get\_ctrl](structvideo__driver__api.md#a40bc476e1e89c42ef78cb99e98d83b38) == NULL) {

528 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

529 }

530

531 return api->[get\_ctrl](structvideo__driver__api.md#a40bc476e1e89c42ef78cb99e98d83b38)(dev, cid, value);

532}

533

[ 547](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)static inline int [video\_set\_signal](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)(const struct [device](structdevice.md) \*dev,

548 enum [video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9) ep,

549 struct [k\_poll\_signal](structk__poll__signal.md) \*signal)

550{

551 const struct [video\_driver\_api](structvideo__driver__api.md) \*api =

552 (const struct [video\_driver\_api](structvideo__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

553

554 if (api->[set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2) == NULL) {

555 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

556 }

557

558 return api->[set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2)(dev, ep, signal);

559}

560

[ 568](group__video__interface.md#ga8454f5568e24cf7b8a59dde765b4a804)struct [video\_buffer](structvideo__buffer.md) \*[video\_buffer\_alloc](group__video__interface.md#ga8454f5568e24cf7b8a59dde765b4a804)(size\_t [size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b));

569

[ 575](group__video__interface.md#gad2661653db019b673153001b2c61b10f)void [video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f)(struct [video\_buffer](structvideo__buffer.md) \*buf);

576

577

578/\* fourcc - four-character-code \*/

[ 579](group__video__interface.md#gabeacdd211927e893561446fd7299ab08)#define video\_fourcc(a, b, c, d)\

580 ((uint32\_t)(a) | ((uint32\_t)(b) << 8) | ((uint32\_t)(c) << 16) | ((uint32\_t)(d) << 24))

581

582

587

592

[ 594](group__video__pixel__formats.md#ga64ad74bb6c92041a4190614b684ae024)#define VIDEO\_PIX\_FMT\_BGGR8 video\_fourcc('B', 'G', 'G', 'R') /\* 8 BGBG.. GRGR.. \*/

[ 596](group__video__pixel__formats.md#gaebdfd9d4230b56f6b8533630356b8793)#define VIDEO\_PIX\_FMT\_GBRG8 video\_fourcc('G', 'B', 'R', 'G') /\* 8 GBGB.. RGRG.. \*/

[ 598](group__video__pixel__formats.md#ga6b9c8d43406e45927f4e9e94504eae9c)#define VIDEO\_PIX\_FMT\_GRBG8 video\_fourcc('G', 'R', 'B', 'G') /\* 8 GRGR.. BGBG.. \*/

[ 600](group__video__pixel__formats.md#ga0c98dc205b724c9e4556e41cc266d80e)#define VIDEO\_PIX\_FMT\_RGGB8 video\_fourcc('R', 'G', 'G', 'B') /\* 8 RGRG.. GBGB.. \*/

601

605

610

[ 612](group__video__pixel__formats.md#gaf009d0eb7dbdb3bfd8883da03478c1ec)#define VIDEO\_PIX\_FMT\_RGB565 video\_fourcc('R', 'G', 'B', 'P') /\* 16 RGB-5-6-5 \*/

613

617

622

[ 624](group__video__pixel__formats.md#gad186d3166acec11c893ae57a0ae68f11)#define VIDEO\_PIX\_FMT\_YUYV video\_fourcc('Y', 'U', 'Y', 'V') /\* 16 Y0-Cb0 Y1-Cr0 \*/

625

630

635

[ 637](group__video__pixel__formats.md#ga035a13c38c4f123411547e2c40d58bd2)#define VIDEO\_PIX\_FMT\_JPEG video\_fourcc('J', 'P', 'E', 'G') /\* 8 JPEG \*/

638

642

646

647#ifdef \_\_cplusplus

648}

649#endif

650

654

655#endif /\* ZEPHYR\_INCLUDE\_VIDEO\_H\_ \*/

[device.h](device_8h.md)

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[video\_api\_stream\_start\_t](group__video__interface.md#ga06fe3e6bfed2d817c5c239161d8a777e)

int(\* video\_api\_stream\_start\_t)(const struct device \*dev)

Start the capture or output process.

**Definition** video.h:200

[video\_signal\_result](group__video__interface.md#ga0f50f287c4075e992fbab6d8a990d7a8)

video\_signal\_result

video\_event enum

**Definition** video.h:136

[video\_api\_enqueue\_t](group__video__interface.md#ga161a0320e7e84935f809d6460064c0fe)

int(\* video\_api\_enqueue\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*buf)

Enqueue a buffer in the driver’s incoming queue.

**Definition** video.h:168

[video\_api\_dequeue\_t](group__video__interface.md#ga16c82da50c6024d36b65fd1c6f33721d)

int(\* video\_api\_dequeue\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*\*buf, k\_timeout\_t timeout)

Dequeue a buffer from the driver’s outgoing queue.

**Definition** video.h:178

[video\_get\_caps](group__video__interface.md#ga4d5237607c858708380955705a2023bd)

static int video\_get\_caps(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_caps \*caps)

Get the capabilities of a video endpoint.

**Definition** video.h:464

[video\_api\_stream\_stop\_t](group__video__interface.md#ga5e8564970bd5cc3b57ee23ff223460bd)

int(\* video\_api\_stream\_stop\_t)(const struct device \*dev)

Stop the capture or output process.

**Definition** video.h:208

[video\_stream\_stop](group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48)

static int video\_stream\_stop(const struct device \*dev)

Stop the video device function.

**Definition** video.h:439

[video\_get\_ctrl](group__video__interface.md#ga664122e82da802f1dff8b5c30e158acd)

static int video\_get\_ctrl(const struct device \*dev, unsigned int cid, void \*value)

Get the current value of a control.

**Definition** video.h:521

[video\_stream\_start](group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0)

static int video\_stream\_start(const struct device \*dev)

Start the video device function.

**Definition** video.h:418

[video\_api\_get\_format\_t](group__video__interface.md#ga7c85f21c1e1839bce84bbce3e339903d)

int(\* video\_api\_get\_format\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Get current video format.

**Definition** video.h:158

[video\_buffer\_alloc](group__video__interface.md#ga8454f5568e24cf7b8a59dde765b4a804)

struct video\_buffer \* video\_buffer\_alloc(size\_t size)

Allocate video buffer.

[video\_set\_ctrl](group__video__interface.md#ga87873a4612cfbd2cb62595dec15cb77e)

static int video\_set\_ctrl(const struct device \*dev, unsigned int cid, void \*value)

Set the value of a control.

**Definition** video.h:493

[video\_dequeue](group__video__interface.md#ga9862024c9b07855609ea2078680c9afd)

static int video\_dequeue(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*\*buf, k\_timeout\_t timeout)

Dequeue a video buffer.

**Definition** video.h:362

[video\_api\_set\_signal\_t](group__video__interface.md#ga9d08347300d2e3c8dc7ae01d2902d321)

int(\* video\_api\_set\_signal\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct k\_poll\_signal \*signal)

Register/Unregister poll signal for buffer events.

**Definition** video.h:246

[video\_api\_get\_ctrl\_t](group__video__interface.md#gaa0779e606de3ec27e1e9230cd13a090c)

int(\* video\_api\_get\_ctrl\_t)(const struct device \*dev, unsigned int cid, void \*value)

Get a video control value.

**Definition** video.h:226

[video\_set\_signal](group__video__interface.md#gab38a9f956f5d5452fc6e0c0f1bf382be)

static int video\_set\_signal(const struct device \*dev, enum video\_endpoint\_id ep, struct k\_poll\_signal \*signal)

Register/Unregister k\_poll signal for a video endpoint.

**Definition** video.h:547

[video\_get\_format](group__video__interface.md#gac0964bd0b57c6be5e773a21af0438edc)

static int video\_get\_format(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Get video format.

**Definition** video.h:305

[video\_enqueue](group__video__interface.md#gac19d14a5875d48c96bd66a8bb65e8a51)

static int video\_enqueue(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_buffer \*buf)

Enqueue a video buffer.

**Definition** video.h:333

[video\_buffer\_release](group__video__interface.md#gad2661653db019b673153001b2c61b10f)

void video\_buffer\_release(struct video\_buffer \*buf)

Release a video buffer.

[video\_api\_flush\_t](group__video__interface.md#gad308f355cd9d5a5d56bd0c81d31626db)

int(\* video\_api\_flush\_t)(const struct device \*dev, enum video\_endpoint\_id ep, bool cancel)

Flush endpoint buffers, buffer are moved from incoming queue to outgoing queue.

**Definition** video.h:190

[video\_api\_set\_ctrl\_t](group__video__interface.md#gad392294a57d6fb191058cf852a5adc8a)

int(\* video\_api\_set\_ctrl\_t)(const struct device \*dev, unsigned int cid, void \*value)

Set a video control value.

**Definition** video.h:216

[video\_api\_get\_caps\_t](group__video__interface.md#gad4a0c666d5534f9daed7d3c9a00c1312)

int(\* video\_api\_get\_caps\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_caps \*caps)

Get capabilities of a video endpoint.

**Definition** video.h:236

[video\_set\_format](group__video__interface.md#gae38df95199e41ac197b9754824b2bd29)

static int video\_set\_format(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Set video format.

**Definition** video.h:280

[video\_flush](group__video__interface.md#gae5e6256ab799ca1cbbac4987b82bb145)

static int video\_flush(const struct device \*dev, enum video\_endpoint\_id ep, bool cancel)

Flush endpoint buffers.

**Definition** video.h:392

[video\_api\_set\_format\_t](group__video__interface.md#gaf6e1ac05a51ae9afaf2569311853ee18)

int(\* video\_api\_set\_format\_t)(const struct device \*dev, enum video\_endpoint\_id ep, struct video\_format \*fmt)

Set video format.

**Definition** video.h:148

[video\_endpoint\_id](group__video__interface.md#gafa3d076a1324ea54b5c5ec7806cb2ef9)

video\_endpoint\_id

video\_endpoint\_id enum

**Definition** video.h:124

[VIDEO\_BUF\_ABORTED](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8a268855ccd0d8e10f608d4dac5f76fac8)

@ VIDEO\_BUF\_ABORTED

**Definition** video.h:138

[VIDEO\_BUF\_DONE](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8ad7499b0b62f470b63d624ec49d358db8)

@ VIDEO\_BUF\_DONE

**Definition** video.h:137

[VIDEO\_BUF\_ERROR](group__video__interface.md#gga0f50f287c4075e992fbab6d8a990d7a8afe8726c40851834057bbf9d99b0433a3)

@ VIDEO\_BUF\_ERROR

**Definition** video.h:139

[VIDEO\_EP\_IN](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a33427df6cd696ceede84d93d5245d3e7)

@ VIDEO\_EP\_IN

**Definition** video.h:127

[VIDEO\_EP\_NONE](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a4293b9f211c8ec80d5ad873cec7022c7)

@ VIDEO\_EP\_NONE

**Definition** video.h:125

[VIDEO\_EP\_ANY](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a450d124253f8463114b851b1e51960fb)

@ VIDEO\_EP\_ANY

**Definition** video.h:126

[VIDEO\_EP\_OUT](group__video__interface.md#ggafa3d076a1324ea54b5c5ec7806cb2ef9a69d107ac2c94372d4ae872b4e7e4b35a)

@ VIDEO\_EP\_OUT

**Definition** video.h:128

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

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

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5622

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[video\_buffer](structvideo__buffer.md)

Video buffer structure.

**Definition** video.h:103

[video\_buffer::bytesused](structvideo__buffer.md#a17505a283ab5ef65047b798cb49aa9e1)

uint32\_t bytesused

number of bytes occupied by the valid data in the buffer.

**Definition** video.h:111

[video\_buffer::size](structvideo__buffer.md#a3f040775c683c91740c8bda5c96e621b)

uint32\_t size

size of the buffer in bytes.

**Definition** video.h:109

[video\_buffer::buffer](structvideo__buffer.md#a6a62d7a50c717dc6bc85e2d8f6ae95e3)

uint8\_t \* buffer

pointer to the start of the buffer.

**Definition** video.h:107

[video\_buffer::driver\_data](structvideo__buffer.md#ab184d528487042650af105eb7d37381e)

void \* driver\_data

pointer to driver specific data.

**Definition** video.h:105

[video\_buffer::timestamp](structvideo__buffer.md#af5c1abf09e0047334e03afbc64226eba)

uint32\_t timestamp

time reference in milliseconds at which the last data byte was actually received for input endpoints ...

**Definition** video.h:116

[video\_caps](structvideo__caps.md)

Video format capabilities.

**Definition** video.h:88

[video\_caps::min\_vbuf\_count](structvideo__caps.md#a2b2604a36a2f7a5013d9383ab5ef198a)

uint8\_t min\_vbuf\_count

minimal count of video buffers to enqueue before being able to start the stream.

**Definition** video.h:94

[video\_caps::format\_caps](structvideo__caps.md#adb454a88504d9fd6e40510171a53b185)

const struct video\_format\_cap \* format\_caps

list of video format capabilities (zero terminated).

**Definition** video.h:90

[video\_driver\_api](structvideo__driver__api.md)

**Definition** video.h:250

[video\_driver\_api::stream\_stop](structvideo__driver__api.md#a07335db8e854f8561f8fdf037def106c)

video\_api\_stream\_stop\_t stream\_stop

**Definition** video.h:255

[video\_driver\_api::set\_ctrl](structvideo__driver__api.md#a1037a6a768906604c58032e25efabbb8)

video\_api\_set\_ctrl\_t set\_ctrl

**Definition** video.h:261

[video\_driver\_api::stream\_start](structvideo__driver__api.md#a32759d924c983ca5aabf47e7c2d23acc)

video\_api\_stream\_start\_t stream\_start

**Definition** video.h:254

[video\_driver\_api::get\_ctrl](structvideo__driver__api.md#a40bc476e1e89c42ef78cb99e98d83b38)

video\_api\_set\_ctrl\_t get\_ctrl

**Definition** video.h:262

[video\_driver\_api::enqueue](structvideo__driver__api.md#a4762a3f103ca5999e3d3f790bb74af75)

video\_api\_enqueue\_t enqueue

**Definition** video.h:258

[video\_driver\_api::set\_signal](structvideo__driver__api.md#a59dbaa93982c354c16d5de63c0d03ec2)

video\_api\_set\_signal\_t set\_signal

**Definition** video.h:263

[video\_driver\_api::get\_format](structvideo__driver__api.md#a5c89e8128d610dd123456f83a4f2cca4)

video\_api\_get\_format\_t get\_format

**Definition** video.h:253

[video\_driver\_api::get\_caps](structvideo__driver__api.md#a6ab4deb345d2138e63e0c6126eeb5078)

video\_api\_get\_caps\_t get\_caps

**Definition** video.h:256

[video\_driver\_api::set\_format](structvideo__driver__api.md#a6ef22653b6ba24b935390795830251f8)

video\_api\_set\_format\_t set\_format

**Definition** video.h:252

[video\_driver\_api::flush](structvideo__driver__api.md#a963927cc38174c4703470df04ec73dc6)

video\_api\_flush\_t flush

**Definition** video.h:260

[video\_driver\_api::dequeue](structvideo__driver__api.md#a96ba1bb4b76c7efc445b3071ef3a05ef)

video\_api\_dequeue\_t dequeue

**Definition** video.h:259

[video\_format\_cap](structvideo__format__cap.md)

Video format capability.

**Definition** video.h:65

[video\_format\_cap::height\_step](structvideo__format__cap.md#a512907acd398e053d48d26aab611772e)

uint16\_t height\_step

height step size in pixels.

**Definition** video.h:79

[video\_format\_cap::width\_min](structvideo__format__cap.md#a539b75ac7b1eadc8c9ee9395b5b2fba9)

uint32\_t width\_min

minimum supported frame width in pixels.

**Definition** video.h:69

[video\_format\_cap::width\_max](structvideo__format__cap.md#ab45cdeb28d93d670f06caca449fccd66)

uint32\_t width\_max

maximum supported frame width in pixels.

**Definition** video.h:71

[video\_format\_cap::width\_step](structvideo__format__cap.md#ab86710dfc4da3b5d0f9dd5017f971aad)

uint16\_t width\_step

width step size in pixels.

**Definition** video.h:77

[video\_format\_cap::height\_max](structvideo__format__cap.md#ae5f4de43c4fdaa6bc7085042ec67cd5f)

uint32\_t height\_max

maximum supported frame height in pixels.

**Definition** video.h:75

[video\_format\_cap::height\_min](structvideo__format__cap.md#ae6f82b60ad822a37a3c97a71892d8d35)

uint32\_t height\_min

minimum supported frame height in pixels.

**Definition** video.h:73

[video\_format\_cap::pixelformat](structvideo__format__cap.md#af5beb952295592dc9dc235a4151b2f59)

uint32\_t pixelformat

FourCC pixel format value (Video pixel formats).

**Definition** video.h:67

[video\_format](structvideo__format.md)

Video format structure.

**Definition** video.h:41

[video\_format::height](structvideo__format.md#a0e71fa7a0abd7740d5245021ba1acbb0)

uint32\_t height

frame height in pixels.

**Definition** video.h:47

[video\_format::width](structvideo__format.md#a7b0cc009ac03437e7e3e86b45545b693)

uint32\_t width

frame width in pixels.

**Definition** video.h:45

[video\_format::pitch](structvideo__format.md#aa4cd70933938ec6f52175232cf403ef6)

uint32\_t pitch

line stride.

**Definition** video.h:55

[video\_format::pixelformat](structvideo__format.md#adb8bf2c8d59125c050cdfe160c30f5ef)

uint32\_t pixelformat

FourCC pixel format value (Video pixel formats).

**Definition** video.h:43

[video-controls.h](video-controls_8h.md)

Public APIs for Video.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video.h](video_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
