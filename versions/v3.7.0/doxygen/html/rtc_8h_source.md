---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rtc_8h_source.html
original_path: doxygen/html/rtc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

24

25#include <[zephyr/kernel.h](kernel_8h.md)>

26#include <[zephyr/device.h](device_8h.md)>

27#include <[errno.h](errno_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 39](group__rtc__interface.md#gaae487761ea0c904f5715748dab5b03db)#define RTC\_ALARM\_TIME\_MASK\_SECOND BIT(0)

[ 40](group__rtc__interface.md#ga72eb18edb7399ce82fa4693e1301fa94)#define RTC\_ALARM\_TIME\_MASK\_MINUTE BIT(1)

[ 41](group__rtc__interface.md#ga31c1ba78aebf43d539aed3ed107a8132)#define RTC\_ALARM\_TIME\_MASK\_HOUR BIT(2)

[ 42](group__rtc__interface.md#ga08fa103b0055eecd4b887973f06beed7)#define RTC\_ALARM\_TIME\_MASK\_MONTHDAY BIT(3)

[ 43](group__rtc__interface.md#ga2233ee12335b762b728d47afa6c72d02)#define RTC\_ALARM\_TIME\_MASK\_MONTH BIT(4)

[ 44](group__rtc__interface.md#ga2d4baf31c5ba6703ebe64dbd212883ee)#define RTC\_ALARM\_TIME\_MASK\_YEAR BIT(5)

[ 45](group__rtc__interface.md#ga8e3cb85959d06f9b8603142156556ca3)#define RTC\_ALARM\_TIME\_MASK\_WEEKDAY BIT(6)

[ 46](group__rtc__interface.md#gad72da3fb8be2c5726bab837fcb97a67e)#define RTC\_ALARM\_TIME\_MASK\_YEARDAY BIT(7)

[ 47](group__rtc__interface.md#gaf8efe72ee6c332b21827317dde6b9766)#define RTC\_ALARM\_TIME\_MASK\_NSEC BIT(8)

51

[ 61](structrtc__time.md)struct [rtc\_time](structrtc__time.md) {

[ 62](structrtc__time.md#aed2640702991b684601d1771847bb50f) int [tm\_sec](structrtc__time.md#aed2640702991b684601d1771847bb50f);

[ 63](structrtc__time.md#a927b7e67b64708f671c1fe9409e9d794) int [tm\_min](structrtc__time.md#a927b7e67b64708f671c1fe9409e9d794);

[ 64](structrtc__time.md#aee14d277ac0339f587f4b946be53dc09) int [tm\_hour](structrtc__time.md#aee14d277ac0339f587f4b946be53dc09);

[ 65](structrtc__time.md#af56ccbce4cca252d2ab0d7516cc5e2db) int [tm\_mday](structrtc__time.md#af56ccbce4cca252d2ab0d7516cc5e2db);

[ 66](structrtc__time.md#aa17515d6d722d1e6e4427a129c8de9f8) int [tm\_mon](structrtc__time.md#aa17515d6d722d1e6e4427a129c8de9f8);

[ 67](structrtc__time.md#ad3fcf9be156258688742a511e8b36277) int [tm\_year](structrtc__time.md#ad3fcf9be156258688742a511e8b36277);

[ 68](structrtc__time.md#ac44442e37e069314e2b6bae0f0747f49) int [tm\_wday](structrtc__time.md#ac44442e37e069314e2b6bae0f0747f49);

[ 69](structrtc__time.md#a5a7837a78fb662831fa3186377d63375) int [tm\_yday](structrtc__time.md#a5a7837a78fb662831fa3186377d63375);

[ 70](structrtc__time.md#aa26da32caecabf386e9a204937d9f786) int [tm\_isdst](structrtc__time.md#aa26da32caecabf386e9a204937d9f786);

[ 71](structrtc__time.md#a876a66e76c713ead7c5eb2cc65d141ed) int [tm\_nsec](structrtc__time.md#a876a66e76c713ead7c5eb2cc65d141ed);

72};

73

[ 81](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07)typedef void (\*[rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07))(const struct [device](structdevice.md) \*dev, void \*user\_data);

82

[ 91](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d)typedef void (\*[rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*user\_data);

92

98

103typedef int (\*rtc\_api\_set\_time)(const struct [device](structdevice.md) \*dev, const struct [rtc\_time](structrtc__time.md) \*timeptr);

104

109typedef int (\*rtc\_api\_get\_time)(const struct [device](structdevice.md) \*dev, struct [rtc\_time](structrtc__time.md) \*timeptr);

110

115typedef int (\*rtc\_api\_alarm\_get\_supported\_fields)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

116 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask);

117

122typedef int (\*rtc\_api\_alarm\_set\_time)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask,

123 const struct [rtc\_time](structrtc__time.md) \*timeptr);

124

129typedef int (\*rtc\_api\_alarm\_get\_time)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask,

130 struct [rtc\_time](structrtc__time.md) \*timeptr);

131

136typedef int (\*rtc\_api\_alarm\_is\_pending)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id);

137

142typedef int (\*rtc\_api\_alarm\_set\_callback)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

143 [rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d) callback, void \*user\_data);

144

149typedef int (\*rtc\_api\_update\_set\_callback)(const struct [device](structdevice.md) \*dev,

150 [rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07) callback, void \*user\_data);

151

156typedef int (\*rtc\_api\_set\_calibration)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) calibration);

157

162typedef int (\*rtc\_api\_get\_calibration)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*calibration);

163

167\_\_subsystem struct rtc\_driver\_api {

168 rtc\_api\_set\_time set\_time;

169 rtc\_api\_get\_time get\_time;

170#if defined(CONFIG\_RTC\_ALARM) || defined(\_\_DOXYGEN\_\_)

171 rtc\_api\_alarm\_get\_supported\_fields alarm\_get\_supported\_fields;

172 rtc\_api\_alarm\_set\_time alarm\_set\_time;

173 rtc\_api\_alarm\_get\_time alarm\_get\_time;

174 rtc\_api\_alarm\_is\_pending alarm\_is\_pending;

175 rtc\_api\_alarm\_set\_callback alarm\_set\_callback;

176#endif /\* CONFIG\_RTC\_ALARM \*/

177#if defined(CONFIG\_RTC\_UPDATE) || defined(\_\_DOXYGEN\_\_)

178 rtc\_api\_update\_set\_callback update\_set\_callback;

179#endif /\* CONFIG\_RTC\_UPDATE \*/

180#if defined(CONFIG\_RTC\_CALIBRATION) || defined(\_\_DOXYGEN\_\_)

181 rtc\_api\_set\_calibration set\_calibration;

182 rtc\_api\_get\_calibration get\_calibration;

183#endif /\* CONFIG\_RTC\_CALIBRATION \*/

184};

185

187

[ 198](group__rtc__interface.md#ga52982b434c740e86aa5f3e35e9bee4a7)\_\_syscall int [rtc\_set\_time](group__rtc__interface.md#ga52982b434c740e86aa5f3e35e9bee4a7)(const struct [device](structdevice.md) \*dev, const struct [rtc\_time](structrtc__time.md) \*timeptr);

199

200static inline int z\_impl\_rtc\_set\_time(const struct [device](structdevice.md) \*dev, const struct [rtc\_time](structrtc__time.md) \*timeptr)

201{

202 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

203

204 return api->set\_time(dev, timeptr);

205}

206

[ 217](group__rtc__interface.md#ga208321104a1cdb39173317e6911aea87)\_\_syscall int [rtc\_get\_time](group__rtc__interface.md#ga208321104a1cdb39173317e6911aea87)(const struct [device](structdevice.md) \*dev, struct [rtc\_time](structrtc__time.md) \*timeptr);

218

219static inline int z\_impl\_rtc\_get\_time(const struct [device](structdevice.md) \*dev, struct [rtc\_time](structrtc__time.md) \*timeptr)

220{

221 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

222

223 return api->get\_time(dev, timeptr);

224}

225

230#if defined(CONFIG\_RTC\_ALARM) || defined(\_\_DOXYGEN\_\_)

231

[ 246](group__rtc__interface.md#ga62f8ece98065b9bd892908e2f0b1f9bb)\_\_syscall int [rtc\_alarm\_get\_supported\_fields](group__rtc__interface.md#ga62f8ece98065b9bd892908e2f0b1f9bb)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

247 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask);

248

249static inline int z\_impl\_rtc\_alarm\_get\_supported\_fields(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

250 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask)

251{

252 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

253

254 if (api->alarm\_get\_supported\_fields == NULL) {

255 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

256 }

257

258 return api->alarm\_get\_supported\_fields(dev, id, mask);

259}

260

[ 284](group__rtc__interface.md#ga1fc9f0ec9642dfbf742ea541a20bdad5)\_\_syscall int [rtc\_alarm\_set\_time](group__rtc__interface.md#ga1fc9f0ec9642dfbf742ea541a20bdad5)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask,

285 const struct [rtc\_time](structrtc__time.md) \*timeptr);

286

287static inline int z\_impl\_rtc\_alarm\_set\_time(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mask,

288 const struct [rtc\_time](structrtc__time.md) \*timeptr)

289{

290 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

291

292 if (api->alarm\_set\_time == NULL) {

293 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

294 }

295

296 return api->alarm\_set\_time(dev, id, mask, timeptr);

297}

298

[ 314](group__rtc__interface.md#gacba4edcec86ccbea5cd676924840c47a)\_\_syscall int [rtc\_alarm\_get\_time](group__rtc__interface.md#gacba4edcec86ccbea5cd676924840c47a)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask,

315 struct [rtc\_time](structrtc__time.md) \*timeptr);

316

317static inline int z\_impl\_rtc\_alarm\_get\_time(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*mask,

318 struct [rtc\_time](structrtc__time.md) \*timeptr)

319{

320 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

321

322 if (api->alarm\_get\_time == NULL) {

323 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

324 }

325

326 return api->alarm\_get\_time(dev, id, mask, timeptr);

327}

328

[ 344](group__rtc__interface.md#ga531c379c437a91df44a45e95063700e8)\_\_syscall int [rtc\_alarm\_is\_pending](group__rtc__interface.md#ga531c379c437a91df44a45e95063700e8)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id);

345

346static inline int z\_impl\_rtc\_alarm\_is\_pending(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id)

347{

348 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

349

350 if (api->alarm\_is\_pending == NULL) {

351 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

352 }

353

354 return api->alarm\_is\_pending(dev, id);

355}

356

[ 383](group__rtc__interface.md#ga77ccb9e6bd32e97016e01729d95074b6)\_\_syscall int [rtc\_alarm\_set\_callback](group__rtc__interface.md#ga77ccb9e6bd32e97016e01729d95074b6)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

384 [rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d) callback, void \*user\_data);

385

386static inline int z\_impl\_rtc\_alarm\_set\_callback(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

387 [rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d) callback, void \*user\_data)

388{

389 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

390

391 if (api->alarm\_set\_callback == NULL) {

392 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

393 }

394

395 return api->alarm\_set\_callback(dev, id, callback, user\_data);

396}

397

398#endif /\* CONFIG\_RTC\_ALARM \*/

402

407#if defined(CONFIG\_RTC\_UPDATE) || defined(\_\_DOXYGEN\_\_)

408

[ 428](group__rtc__interface.md#gad9a48c4e7a05ee20c0edc96c348c9a45)\_\_syscall int [rtc\_update\_set\_callback](group__rtc__interface.md#gad9a48c4e7a05ee20c0edc96c348c9a45)(const struct [device](structdevice.md) \*dev, [rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07) callback,

429 void \*user\_data);

430

431static inline int z\_impl\_rtc\_update\_set\_callback(const struct [device](structdevice.md) \*dev,

432 [rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07) callback, void \*user\_data)

433{

434 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

435

436 if (api->update\_set\_callback == NULL) {

437 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

438 }

439

440 return api->update\_set\_callback(dev, callback, user\_data);

441}

442

443#endif /\* CONFIG\_RTC\_UPDATE \*/

447

452#if defined(CONFIG\_RTC\_CALIBRATION) || defined(\_\_DOXYGEN\_\_)

453

[ 472](group__rtc__interface.md#ga13395c6b38e06bcda23cc0e9c299c445)\_\_syscall int [rtc\_set\_calibration](group__rtc__interface.md#ga13395c6b38e06bcda23cc0e9c299c445)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) calibration);

473

474static inline int z\_impl\_rtc\_set\_calibration(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) calibration)

475{

476 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

477

478 if (api->set\_calibration == NULL) {

479 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

480 }

481

482 return api->set\_calibration(dev, calibration);

483}

484

[ 495](group__rtc__interface.md#gab29bc6bcea5eb71e03d3e6181d4bec2f)\_\_syscall int [rtc\_get\_calibration](group__rtc__interface.md#gab29bc6bcea5eb71e03d3e6181d4bec2f)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*calibration);

496

497static inline int z\_impl\_rtc\_get\_calibration(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*calibration)

498{

499 const struct rtc\_driver\_api \*api = (const struct rtc\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

500

501 if (api->get\_calibration == NULL) {

502 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

503 }

504

505 return api->get\_calibration(dev, calibration);

506}

507

508#endif /\* CONFIG\_RTC\_CALIBRATION \*/

512

517

521struct [tm](structtm.md);

522

[ 527](group__rtc__interface.md#gac2bb774a4b512f76c35a0a6723a7c807)static inline struct [tm](structtm.md) \*[rtc\_time\_to\_tm](group__rtc__interface.md#gac2bb774a4b512f76c35a0a6723a7c807)(struct [rtc\_time](structrtc__time.md) \*timeptr)

528{

529 return (struct [tm](structtm.md) \*)timeptr;

530}

531

[ 539](group__rtc__interface.md#gacca437e504026d800aa481b870291fda)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [rtc\_calibration\_from\_frequency](group__rtc__interface.md#gacca437e504026d800aa481b870291fda)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frequency)

540{

541 \_\_ASSERT\_NO\_MSG(frequency > 0);

542

543 return ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))((1000000000000000000LL / frequency) - 1000000000);

544}

545

549

553

554#ifdef \_\_cplusplus

555}

556#endif

557

558#include <zephyr/syscalls/rtc.h>

559

560#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_H\_ \*/

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

**Definition** rtc.h:91

[rtc\_update\_callback](group__rtc__interface.md#ga99e4869ee85507befc7e7cf129b45b07)

void(\* rtc\_update\_callback)(const struct device \*dev, void \*user\_data)

RTC update event callback.

**Definition** rtc.h:81

[rtc\_get\_calibration](group__rtc__interface.md#gab29bc6bcea5eb71e03d3e6181d4bec2f)

int rtc\_get\_calibration(const struct device \*dev, int32\_t \*calibration)

API for getting RTC calibration.

[rtc\_time\_to\_tm](group__rtc__interface.md#gac2bb774a4b512f76c35a0a6723a7c807)

static struct tm \* rtc\_time\_to\_tm(struct rtc\_time \*timeptr)

Convenience function for safely casting a rtc\_time pointer to a tm pointer.

**Definition** rtc.h:527

[rtc\_alarm\_get\_time](group__rtc__interface.md#gacba4edcec86ccbea5cd676924840c47a)

int rtc\_alarm\_get\_time(const struct device \*dev, uint16\_t id, uint16\_t \*mask, struct rtc\_time \*timeptr)

API for getting RTC alarm time.

[rtc\_calibration\_from\_frequency](group__rtc__interface.md#gacca437e504026d800aa481b870291fda)

static int32\_t rtc\_calibration\_from\_frequency(uint32\_t frequency)

Determine required calibration to 1 Hertz from frequency.

**Definition** rtc.h:539

[rtc\_update\_set\_callback](group__rtc__interface.md#gad9a48c4e7a05ee20c0edc96c348c9a45)

int rtc\_update\_set\_callback(const struct device \*dev, rtc\_update\_callback callback, void \*user\_data)

API for setting update callback.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

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

[rtc\_time](structrtc__time.md)

Structure for storing date and time values with sub-second precision.

**Definition** rtc.h:61

[rtc\_time::tm\_yday](structrtc__time.md#a5a7837a78fb662831fa3186377d63375)

int tm\_yday

Day of the year [0, 365] (Unknown = -1).

**Definition** rtc.h:69

[rtc\_time::tm\_nsec](structrtc__time.md#a876a66e76c713ead7c5eb2cc65d141ed)

int tm\_nsec

Nanoseconds [0, 999999999] (Unknown = 0).

**Definition** rtc.h:71

[rtc\_time::tm\_min](structrtc__time.md#a927b7e67b64708f671c1fe9409e9d794)

int tm\_min

Minutes [0, 59].

**Definition** rtc.h:63

[rtc\_time::tm\_mon](structrtc__time.md#aa17515d6d722d1e6e4427a129c8de9f8)

int tm\_mon

Month [0, 11].

**Definition** rtc.h:66

[rtc\_time::tm\_isdst](structrtc__time.md#aa26da32caecabf386e9a204937d9f786)

int tm\_isdst

Daylight saving time flag [-1] (Unknown = -1).

**Definition** rtc.h:70

[rtc\_time::tm\_wday](structrtc__time.md#ac44442e37e069314e2b6bae0f0747f49)

int tm\_wday

Day of the week [0, 6] (Sunday = 0) (Unknown = -1).

**Definition** rtc.h:68

[rtc\_time::tm\_year](structrtc__time.md#ad3fcf9be156258688742a511e8b36277)

int tm\_year

Year - 1900.

**Definition** rtc.h:67

[rtc\_time::tm\_sec](structrtc__time.md#aed2640702991b684601d1771847bb50f)

int tm\_sec

Seconds [0, 59].

**Definition** rtc.h:62

[rtc\_time::tm\_hour](structrtc__time.md#aee14d277ac0339f587f4b946be53dc09)

int tm\_hour

Hours [0, 23].

**Definition** rtc.h:64

[rtc\_time::tm\_mday](structrtc__time.md#af56ccbce4cca252d2ab0d7516cc5e2db)

int tm\_mday

Day of the month [1, 31].

**Definition** rtc.h:65

[tm](structtm.md)

**Definition** time.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc.h](rtc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
