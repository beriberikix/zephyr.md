---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rtc_8h_source.html
original_path: doxygen/html/rtc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtc.h

[Go to the documentation of this file.](rtc_8h.md)

1/\*

2 \* Copyright (c) 2023 Trackunit Corporation

3 \* Copyright (c) 2023 Bjarki Arge Andreasen

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_H\_

15

22

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24#include <[zephyr/device.h](device_8h.md)>

25#include <[errno.h](errno_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 37](group__rtc__interface.md#gaae487761ea0c904f5715748dab5b03db)#define RTC\_ALARM\_TIME\_MASK\_SECOND BIT(0)

[ 38](group__rtc__interface.md#ga72eb18edb7399ce82fa4693e1301fa94)#define RTC\_ALARM\_TIME\_MASK\_MINUTE BIT(1)

[ 39](group__rtc__interface.md#ga31c1ba78aebf43d539aed3ed107a8132)#define RTC\_ALARM\_TIME\_MASK\_HOUR BIT(2)

[ 40](group__rtc__interface.md#ga08fa103b0055eecd4b887973f06beed7)#define RTC\_ALARM\_TIME\_MASK\_MONTHDAY BIT(3)

[ 41](group__rtc__interface.md#ga2233ee12335b762b728d47afa6c72d02)#define RTC\_ALARM\_TIME\_MASK\_MONTH BIT(4)

[ 42](group__rtc__interface.md#ga2d4baf31c5ba6703ebe64dbd212883ee)#define RTC\_ALARM\_TIME\_MASK\_YEAR BIT(5)

[ 43](group__rtc__interface.md#ga8e3cb85959d06f9b8603142156556ca3)#define RTC\_ALARM\_TIME\_MASK\_WEEKDAY BIT(6)

[ 44](group__rtc__interface.md#gad72da3fb8be2c5726bab837fcb97a67e)#define RTC\_ALARM\_TIME\_MASK\_YEARDAY BIT(7)

[ 45](group__rtc__interface.md#gaf8efe72ee6c332b21827317dde6b9766)#define RTC\_ALARM\_TIME\_MASK\_NSEC BIT(8)

49

[ 59](structrtc__time.md)struct [rtc\_time](structrtc__time.md) {

[ 60](structrtc__time.md#aed2640702991b684601d1771847bb50f) int [tm\_sec](structrtc__time.md#aed2640702991b684601d1771847bb50f);

[ 61](structrtc__time.md#a927b7e67b64708f671c1fe9409e9d794) int [tm\_min](structrtc__time.md#a927b7e67b64708f671c1fe9409e9d794);

[ 62](structrtc__time.md#aee14d277ac0339f587f4b946be53dc09) int [tm\_hour](structrtc__time.md#aee14d277ac0339f587f4b946be53dc09);

[ 63](structrtc__time.md#af56ccbce4cca252d2ab0d7516cc5e2db) int [tm\_mday](structrtc__time.md#af56ccbce4cca252d2ab0d7516cc5e2db);

[ 64](structrtc__time.md#aa17515d6d722d1e6e4427a129c8de9f8) int [tm\_mon](structrtc__time.md#aa17515d6d722d1e6e4427a129c8de9f8);

[ 65](structrtc__time.md#ad3fcf9be156258688742a511e8b36277) int [tm\_year](structrtc__time.md#ad3fcf9be156258688742a511e8b36277);

[ 66](structrtc__time.md#ac44442e37e069314e2b6bae0f0747f49) int [tm\_wday](structrtc__time.md#ac44442e37e069314e2b6bae0f0747f49);

[ 67](structrtc__time.md#a5a7837a78fb662831fa3186377d63375) int [tm\_yday](structrtc__time.md#a5a7837a78fb662831fa3186377d63375);

[ 68](structrtc__time.md#aa26da32caecabf386e9a204937d9f786) int [tm\_isdst](structrtc__time.md#aa26da32caecabf386e9a204937d9f786);

[ 69](structrtc__time.md#a876a66e76c713ead7c5eb2cc65d141ed) int [tm\_nsec](structrtc__time.md#a876a66e76c713ead7c5eb2cc65d141ed);

70};

71

[ 79](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07)typedef void (\*[rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07))(const struct [device](structdevice.md) \*dev, void \*user\_data);

80

[ 89](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d)typedef void (\*[rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*user\_data);

90

96

101typedef int (\*rtc\_api\_set\_time)(const struct [device](structdevice.md) \*dev, const struct [rtc\_time](structrtc__time.md) \*timeptr);

102

107typedef int (\*rtc\_api\_get\_time)(const struct [device](structdevice.md) \*dev, struct [rtc\_time](structrtc__time.md) \*timeptr);

108

113typedef int (\*rtc\_api\_alarm\_get\_supported\_fields)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

114 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask);

115

120typedef int (\*rtc\_api\_alarm\_set\_time)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask,

121 const struct [rtc\_time](structrtc__time.md) \*timeptr);

122

127typedef int (\*rtc\_api\_alarm\_get\_time)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask,

128 struct [rtc\_time](structrtc__time.md) \*timeptr);

129

134typedef int (\*rtc\_api\_alarm\_is\_pending)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id);

135

140typedef int (\*rtc\_api\_alarm\_set\_callback)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

141 [rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d) callback, void \*user\_data);

142

147typedef int (\*rtc\_api\_update\_set\_callback)(const struct [device](structdevice.md) \*dev,

148 [rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07) callback, void \*user\_data);

149

154typedef int (\*rtc\_api\_set\_calibration)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) calibration);

155

160typedef int (\*rtc\_api\_get\_calibration)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*calibration);

161

165\_\_subsystem struct rtc\_driver\_api {

166 rtc\_api\_set\_time set\_time;

167 rtc\_api\_get\_time get\_time;

168#if defined(CONFIG\_RTC\_ALARM) || defined(\_\_DOXYGEN\_\_)

169 rtc\_api\_alarm\_get\_supported\_fields alarm\_get\_supported\_fields;

170 rtc\_api\_alarm\_set\_time alarm\_set\_time;

171 rtc\_api\_alarm\_get\_time alarm\_get\_time;

172 rtc\_api\_alarm\_is\_pending alarm\_is\_pending;

173 rtc\_api\_alarm\_set\_callback alarm\_set\_callback;

174#endif /\* CONFIG\_RTC\_ALARM \*/

175#if defined(CONFIG\_RTC\_UPDATE) || defined(\_\_DOXYGEN\_\_)

176 rtc\_api\_update\_set\_callback update\_set\_callback;

177#endif /\* CONFIG\_RTC\_UPDATE \*/

178#if defined(CONFIG\_RTC\_CALIBRATION) || defined(\_\_DOXYGEN\_\_)

179 rtc\_api\_set\_calibration set\_calibration;

180 rtc\_api\_get\_calibration get\_calibration;

181#endif /\* CONFIG\_RTC\_CALIBRATION \*/

182};

183

185

[ 196](group__rtc__interface.md#ga52982b434c740e86aa5f3e35e9bee4a7)\_\_syscall int [rtc\_set\_time](group__rtc__interface.md#ga52982b434c740e86aa5f3e35e9bee4a7)(const struct [device](structdevice.md) \*dev, const struct [rtc\_time](structrtc__time.md) \*timeptr);

197

198static inline int z\_impl\_rtc\_set\_time(const struct [device](structdevice.md) \*dev, const struct [rtc\_time](structrtc__time.md) \*timeptr)

199{

200 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

201

202 return api->set\_time(dev, timeptr);

203}

204

[ 215](group__rtc__interface.md#ga208321104a1cdb39173317e6911aea87)\_\_syscall int [rtc\_get\_time](group__rtc__interface.md#ga208321104a1cdb39173317e6911aea87)(const struct [device](structdevice.md) \*dev, struct [rtc\_time](structrtc__time.md) \*timeptr);

216

217static inline int z\_impl\_rtc\_get\_time(const struct [device](structdevice.md) \*dev, struct [rtc\_time](structrtc__time.md) \*timeptr)

218{

219 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

220

221 return api->get\_time(dev, timeptr);

222}

223

228#if defined(CONFIG\_RTC\_ALARM) || defined(\_\_DOXYGEN\_\_)

229

[ 244](group__rtc__interface.md#ga62f8ece98065b9bd892908e2f0b1f9bb)\_\_syscall int [rtc\_alarm\_get\_supported\_fields](group__rtc__interface.md#ga62f8ece98065b9bd892908e2f0b1f9bb)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

245 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask);

246

247static inline int z\_impl\_rtc\_alarm\_get\_supported\_fields(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

248 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask)

249{

250 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

251

252 if (api->alarm\_get\_supported\_fields == NULL) {

253 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

254 }

255

256 return api->alarm\_get\_supported\_fields(dev, id, mask);

257}

258

[ 282](group__rtc__interface.md#ga1fc9f0ec9642dfbf742ea541a20bdad5)\_\_syscall int [rtc\_alarm\_set\_time](group__rtc__interface.md#ga1fc9f0ec9642dfbf742ea541a20bdad5)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask,

283 const struct [rtc\_time](structrtc__time.md) \*timeptr);

284

285static inline int z\_impl\_rtc\_alarm\_set\_time(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask,

286 const struct [rtc\_time](structrtc__time.md) \*timeptr)

287{

288 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

289

290 if (api->alarm\_set\_time == NULL) {

291 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

292 }

293

294 return api->alarm\_set\_time(dev, id, mask, timeptr);

295}

296

[ 312](group__rtc__interface.md#gacba4edcec86ccbea5cd676924840c47a)\_\_syscall int [rtc\_alarm\_get\_time](group__rtc__interface.md#gacba4edcec86ccbea5cd676924840c47a)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask,

313 struct [rtc\_time](structrtc__time.md) \*timeptr);

314

315static inline int z\_impl\_rtc\_alarm\_get\_time(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask,

316 struct [rtc\_time](structrtc__time.md) \*timeptr)

317{

318 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

319

320 if (api->alarm\_get\_time == NULL) {

321 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

322 }

323

324 return api->alarm\_get\_time(dev, id, mask, timeptr);

325}

326

[ 342](group__rtc__interface.md#ga531c379c437a91df44a45e95063700e8)\_\_syscall int [rtc\_alarm\_is\_pending](group__rtc__interface.md#ga531c379c437a91df44a45e95063700e8)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id);

343

344static inline int z\_impl\_rtc\_alarm\_is\_pending(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id)

345{

346 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

347

348 if (api->alarm\_is\_pending == NULL) {

349 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

350 }

351

352 return api->alarm\_is\_pending(dev, id);

353}

354

[ 381](group__rtc__interface.md#ga77ccb9e6bd32e97016e01729d95074b6)\_\_syscall int [rtc\_alarm\_set\_callback](group__rtc__interface.md#ga77ccb9e6bd32e97016e01729d95074b6)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

382 [rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d) callback, void \*user\_data);

383

384static inline int z\_impl\_rtc\_alarm\_set\_callback(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

385 [rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d) callback, void \*user\_data)

386{

387 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

388

389 if (api->alarm\_set\_callback == NULL) {

390 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

391 }

392

393 return api->alarm\_set\_callback(dev, id, callback, user\_data);

394}

395

396#endif /\* CONFIG\_RTC\_ALARM \*/

400

405#if defined(CONFIG\_RTC\_UPDATE) || defined(\_\_DOXYGEN\_\_)

406

[ 426](group__rtc__interface.md#gad9a48c4e7a05ee20c0edc96c348c9a45)\_\_syscall int [rtc\_update\_set\_callback](group__rtc__interface.md#gad9a48c4e7a05ee20c0edc96c348c9a45)(const struct [device](structdevice.md) \*dev, [rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07) callback,

427 void \*user\_data);

428

429static inline int z\_impl\_rtc\_update\_set\_callback(const struct [device](structdevice.md) \*dev,

430 [rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07) callback, void \*user\_data)

431{

432 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

433

434 if (api->update\_set\_callback == NULL) {

435 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

436 }

437

438 return api->update\_set\_callback(dev, callback, user\_data);

439}

440

441#endif /\* CONFIG\_RTC\_UPDATE \*/

445

450#if defined(CONFIG\_RTC\_CALIBRATION) || defined(\_\_DOXYGEN\_\_)

451

[ 468](group__rtc__interface.md#ga13395c6b38e06bcda23cc0e9c299c445)\_\_syscall int [rtc\_set\_calibration](group__rtc__interface.md#ga13395c6b38e06bcda23cc0e9c299c445)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) calibration);

469

470static inline int z\_impl\_rtc\_set\_calibration(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) calibration)

471{

472 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

473

474 if (api->set\_calibration == NULL) {

475 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

476 }

477

478 return api->set\_calibration(dev, calibration);

479}

480

[ 491](group__rtc__interface.md#gab29bc6bcea5eb71e03d3e6181d4bec2f)\_\_syscall int [rtc\_get\_calibration](group__rtc__interface.md#gab29bc6bcea5eb71e03d3e6181d4bec2f)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*calibration);

492

493static inline int z\_impl\_rtc\_get\_calibration(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*calibration)

494{

495 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

496

497 if (api->get\_calibration == NULL) {

498 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

499 }

500

501 return api->get\_calibration(dev, calibration);

502}

503

504#endif /\* CONFIG\_RTC\_CALIBRATION \*/

508

513

517struct [tm](structtm.md);

518

[ 523](group__rtc__interface.md#gac2bb774a4b512f76c35a0a6723a7c807)static inline struct [tm](structtm.md) \*[rtc\_time\_to\_tm](group__rtc__interface.md#gac2bb774a4b512f76c35a0a6723a7c807)(struct [rtc\_time](structrtc__time.md) \*timeptr)

524{

525 return (struct [tm](structtm.md) \*)timeptr;

526}

527

531

535

536#ifdef \_\_cplusplus

537}

538#endif

539

540#include <syscalls/rtc.h>

541

542#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[rtc\_set\_calibration](group__rtc__interface.md#ga13395c6b38e06bcda23cc0e9c299c445)

int rtc\_set\_calibration(const struct device \*dev, int32\_t calibration)

API for setting RTC calibration.

[rtc\_alarm\_set\_time](group__rtc__interface.md#ga1fc9f0ec9642dfbf742ea541a20bdad5)

int rtc\_alarm\_set\_time(const struct device \*dev, uint16\_t id, uint16\_t mask, const struct rtc\_time \*timeptr)

API for setting RTC alarm time.

[rtc\_get\_time](group__rtc__interface.md#ga208321104a1cdb39173317e6911aea87)

int rtc\_get\_time(const struct device \*dev, struct rtc\_time \*timeptr)

API for getting RTC time.

[rtc\_set\_time](group__rtc__interface.md#ga52982b434c740e86aa5f3e35e9bee4a7)

int rtc\_set\_time(const struct device \*dev, const struct rtc\_time \*timeptr)

API for setting RTC time.

[rtc\_alarm\_is\_pending](group__rtc__interface.md#ga531c379c437a91df44a45e95063700e8)

int rtc\_alarm\_is\_pending(const struct device \*dev, uint16\_t id)

API for testing if RTC alarm is pending.

[rtc\_alarm\_get\_supported\_fields](group__rtc__interface.md#ga62f8ece98065b9bd892908e2f0b1f9bb)

int rtc\_alarm\_get\_supported\_fields(const struct device \*dev, uint16\_t id, uint16\_t \*mask)

API for getting the supported fields of the RTC alarm time.

[rtc\_alarm\_set\_callback](group__rtc__interface.md#ga77ccb9e6bd32e97016e01729d95074b6)

int rtc\_alarm\_set\_callback(const struct device \*dev, uint16\_t id, rtc\_alarm\_callback callback, void \*user\_data)

API for setting alarm callback.

[rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d)

void(\* rtc\_alarm\_callback)(const struct device \*dev, uint16\_t id, void \*user\_data)

RTC alarm triggered callback.

**Definition** rtc.h:89

[rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07)

void(\* rtc\_update\_callback)(const struct device \*dev, void \*user\_data)

RTC update event callback.

**Definition** rtc.h:79

[rtc\_get\_calibration](group__rtc__interface.md#gab29bc6bcea5eb71e03d3e6181d4bec2f)

int rtc\_get\_calibration(const struct device \*dev, int32\_t \*calibration)

API for getting RTC calibration.

[rtc\_time\_to\_tm](group__rtc__interface.md#gac2bb774a4b512f76c35a0a6723a7c807)

static struct tm \* rtc\_time\_to\_tm(struct rtc\_time \*timeptr)

Convenience function for safely casting a rtc\_time pointer to a tm pointer.

**Definition** rtc.h:523

[rtc\_alarm\_get\_time](group__rtc__interface.md#gacba4edcec86ccbea5cd676924840c47a)

int rtc\_alarm\_get\_time(const struct device \*dev, uint16\_t id, uint16\_t \*mask, struct rtc\_time \*timeptr)

API for getting RTC alarm time.

[rtc\_update\_set\_callback](group__rtc__interface.md#gad9a48c4e7a05ee20c0edc96c348c9a45)

int rtc\_update\_set\_callback(const struct device \*dev, rtc\_update\_callback callback, void \*user\_data)

API for setting update callback.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

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

[rtc\_time](structrtc__time.md)

Structure for storing date and time values with sub-second precision.

**Definition** rtc.h:59

[rtc\_time::tm\_yday](structrtc__time.md#a5a7837a78fb662831fa3186377d63375)

int tm\_yday

Day of the year [0, 365] (Unknown = -1).

**Definition** rtc.h:67

[rtc\_time::tm\_nsec](structrtc__time.md#a876a66e76c713ead7c5eb2cc65d141ed)

int tm\_nsec

Nanoseconds [0, 999999999] (Unknown = 0).

**Definition** rtc.h:69

[rtc\_time::tm\_min](structrtc__time.md#a927b7e67b64708f671c1fe9409e9d794)

int tm\_min

Minutes [0, 59].

**Definition** rtc.h:61

[rtc\_time::tm\_mon](structrtc__time.md#aa17515d6d722d1e6e4427a129c8de9f8)

int tm\_mon

Month [0, 11].

**Definition** rtc.h:64

[rtc\_time::tm\_isdst](structrtc__time.md#aa26da32caecabf386e9a204937d9f786)

int tm\_isdst

Daylight saving time flag [-1] (Unknown = -1).

**Definition** rtc.h:68

[rtc\_time::tm\_wday](structrtc__time.md#ac44442e37e069314e2b6bae0f0747f49)

int tm\_wday

Day of the week [0, 6] (Sunday = 0) (Unknown = -1).

**Definition** rtc.h:66

[rtc\_time::tm\_year](structrtc__time.md#ad3fcf9be156258688742a511e8b36277)

int tm\_year

Year - 1900.

**Definition** rtc.h:65

[rtc\_time::tm\_sec](structrtc__time.md#aed2640702991b684601d1771847bb50f)

int tm\_sec

Seconds [0, 59].

**Definition** rtc.h:60

[rtc\_time::tm\_hour](structrtc__time.md#aee14d277ac0339f587f4b946be53dc09)

int tm\_hour

Hours [0, 23].

**Definition** rtc.h:62

[rtc\_time::tm\_mday](structrtc__time.md#af56ccbce4cca252d2ab0d7516cc5e2db)

int tm\_mday

Day of the month [1, 31].

**Definition** rtc.h:63

[tm](structtm.md)

**Definition** time.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc.h](rtc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
