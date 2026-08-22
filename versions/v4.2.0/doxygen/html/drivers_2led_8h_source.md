---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2led_8h_source.html
original_path: doxygen/html/drivers_2led_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

led.h

[Go to the documentation of this file.](drivers_2led_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LED\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_LED\_H\_

14

23

24#include <[errno.h](errno_8h.md)>

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <[zephyr/device.h](device_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 36](group__led__interface.md#ga7bb18ca9f746ebcfbfc397886643f16d)#define LED\_BRIGHTNESS\_MAX 100u

37

[ 43](structled__info.md)struct [led\_info](structled__info.md) {

[ 45](structled__info.md#a5d01795e49663654e9fe4a821797956a) const char \*[label](structled__info.md#a5d01795e49663654e9fe4a821797956a);

[ 47](structled__info.md#a7f87ebb0718e1dc189e6d48d5bb97c55) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [index](structled__info.md#a7f87ebb0718e1dc189e6d48d5bb97c55);

[ 49](structled__info.md#ab6db05157b960669e3b01154a9621530) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_colors](structled__info.md#ab6db05157b960669e3b01154a9621530);

[ 51](structled__info.md#a8daacbe0a68d7ff710938722003fceaf) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[color\_mapping](structled__info.md#a8daacbe0a68d7ff710938722003fceaf);

52};

53

[ 60](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd)typedef int (\*[led\_api\_blink](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

61 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off);

62

[ 69](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77)typedef int (\*[led\_api\_get\_info](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

70 const struct [led\_info](structled__info.md) \*\*info);

71

[ 78](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f)typedef int (\*[led\_api\_set\_brightness](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

79 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

[ 86](group__led__interface.md#ga977317f3208d5336463edf9979def4ae)typedef int (\*[led\_api\_set\_color](group__led__interface.md#ga977317f3208d5336463edf9979def4ae))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

87 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color);

88

[ 95](group__led__interface.md#gad13f55702668133575658d2ccc295339)typedef int (\*[led\_api\_on](group__led__interface.md#gad13f55702668133575658d2ccc295339))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

96

[ 103](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)typedef int (\*[led\_api\_off](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

104

[ 111](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae)typedef int (\*[led\_api\_write\_channels](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae))(const struct [device](structdevice.md) \*dev,

112 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel,

113 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels,

114 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

115

[ 119](structled__driver__api.md)\_\_subsystem struct [led\_driver\_api](structled__driver__api.md) {

120 /\* Mandatory callbacks, either on/off or set\_brightness. \*/

[ 121](structled__driver__api.md#a9ce7322282f8c525256d3c16a514ecc4) [led\_api\_on](group__led__interface.md#gad13f55702668133575658d2ccc295339) [on](structled__driver__api.md#a9ce7322282f8c525256d3c16a514ecc4);

[ 122](structled__driver__api.md#a19ad736a130da2aff6bd5b299d8c33a7) [led\_api\_off](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd) [off](structled__driver__api.md#a19ad736a130da2aff6bd5b299d8c33a7);

[ 123](structled__driver__api.md#a9c3e3c4d40c4b8219755df6df96b0058) [led\_api\_set\_brightness](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f) [set\_brightness](structled__driver__api.md#a9c3e3c4d40c4b8219755df6df96b0058);

124 /\* Optional callbacks. \*/

[ 125](structled__driver__api.md#af1974c5cc20c818e0e387b34cd14ac3b) [led\_api\_blink](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd) [blink](structled__driver__api.md#af1974c5cc20c818e0e387b34cd14ac3b);

[ 126](structled__driver__api.md#a7c68219e44bcf6e766e64fd3967ecf7e) [led\_api\_get\_info](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77) [get\_info](structled__driver__api.md#a7c68219e44bcf6e766e64fd3967ecf7e);

[ 127](structled__driver__api.md#a336f30f2c1bd3d99213cae66911c142a) [led\_api\_set\_color](group__led__interface.md#ga977317f3208d5336463edf9979def4ae) [set\_color](structled__driver__api.md#a336f30f2c1bd3d99213cae66911c142a);

[ 128](structled__driver__api.md#ada1dfb1830b48afb020c7e60dbd92337) [led\_api\_write\_channels](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae) [write\_channels](structled__driver__api.md#ada1dfb1830b48afb020c7e60dbd92337);

129};

130

[ 143](group__led__interface.md#ga4f31fecd215e5597999be4d16b0d2dd5)\_\_syscall int [led\_blink](group__led__interface.md#ga4f31fecd215e5597999be4d16b0d2dd5)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

144 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off);

145

146static inline int z\_impl\_led\_blink(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

147 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off)

148{

149 const struct [led\_driver\_api](structled__driver__api.md) \*api =

150 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

151

152 if (api->blink == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

153 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

154 }

155 return api->blink(dev, led, delay\_on, delay\_off);

156}

157

[ 168](group__led__interface.md#ga9925483b97073354f7be6b40aa2dad1a)\_\_syscall int [led\_get\_info](group__led__interface.md#ga9925483b97073354f7be6b40aa2dad1a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

169 const struct [led\_info](structled__info.md) \*\*info);

170

171static inline int z\_impl\_led\_get\_info(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

172 const struct [led\_info](structled__info.md) \*\*info)

173{

174 const struct [led\_driver\_api](structled__driver__api.md) \*api =

175 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

176

177 if (api->get\_info == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

178 \*info = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

179 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

180 }

181 return api->get\_info(dev, led, info);

182}

183

[ 200](group__led__interface.md#gaca479fd77518331f4fc84f788e345882)\_\_syscall int [led\_set\_brightness](group__led__interface.md#gaca479fd77518331f4fc84f788e345882)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

201 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

202

203static inline int z\_impl\_led\_set\_brightness(const struct [device](structdevice.md) \*dev,

204 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

205 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

206{

207 const struct [led\_driver\_api](structled__driver__api.md) \*api =

208 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

209

210 if (api->set\_brightness == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

211 if (api->on == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) || api->off == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

212 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

213 }

214 }

215

216 if (value > [LED\_BRIGHTNESS\_MAX](group__led__interface.md#ga7bb18ca9f746ebcfbfc397886643f16d)) {

217 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

218 }

219

220 if (api->set\_brightness == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

221 if (value) {

222 return api->on(dev, led);

223 } else {

224 return api->off(dev, led);

225 }

226 }

227

228 return api->set\_brightness(dev, led, value);

229}

230

[ 247](group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a)\_\_syscall int [led\_write\_channels](group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a)(const struct [device](structdevice.md) \*dev,

248 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel,

249 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

250

251static inline int

252z\_impl\_led\_write\_channels(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel,

253 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf)

254{

255 const struct [led\_driver\_api](structled__driver__api.md) \*api =

256 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

257

258 if (api->write\_channels == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

259 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

260 }

261 return api->write\_channels(dev, start\_channel, num\_channels, buf);

262}

263

[ 276](group__led__interface.md#ga717bdbe76331b6286c58feb6e3e214dd)\_\_syscall int [led\_set\_channel](group__led__interface.md#ga717bdbe76331b6286c58feb6e3e214dd)(const struct [device](structdevice.md) \*dev,

277 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

278

279static inline int z\_impl\_led\_set\_channel(const struct [device](structdevice.md) \*dev,

280 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

281{

282 return z\_impl\_led\_write\_channels(dev, channel, 1, &value);

283}

284

[ 301](group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)\_\_syscall int [led\_set\_color](group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

302 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color);

303

304static inline int z\_impl\_led\_set\_color(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

305 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color)

306{

307 const struct [led\_driver\_api](structled__driver__api.md) \*api =

308 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

309

310 if (api->set\_color == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

311 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

312 }

313 return api->set\_color(dev, led, num\_colors, color);

314}

315

[ 328](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73)\_\_syscall int [led\_on](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

329

330static inline int z\_impl\_led\_on(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led)

331{

332 const struct [led\_driver\_api](structled__driver__api.md) \*api =

333 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

334

335 if (api->set\_brightness == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) && api->on == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

336 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

337 }

338

339 if (api->on == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

340 return api->set\_brightness(dev, led, [LED\_BRIGHTNESS\_MAX](group__led__interface.md#ga7bb18ca9f746ebcfbfc397886643f16d));

341 }

342

343 return api->on(dev, led);

344}

345

[ 358](group__led__interface.md#ga22c9dbe76f06fec327aebe06448d1542)\_\_syscall int [led\_off](group__led__interface.md#ga22c9dbe76f06fec327aebe06448d1542)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

359

360static inline int z\_impl\_led\_off(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led)

361{

362 const struct [led\_driver\_api](structled__driver__api.md) \*api =

363 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

364

365 if (api->set\_brightness == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) && api->off == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

366 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

367 }

368

369 if (api->off == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

370 return api->set\_brightness(dev, led, 0);

371 }

372

373 return api->off(dev, led);

374}

375

376/\*

377 \* LED DT helpers.

378 \*/

379

[ 388](structled__dt__spec.md)struct [led\_dt\_spec](structled__dt__spec.md) {

[ 390](structled__dt__spec.md#ad92b9ee24cb31fcc0a2352bcf831cecb) const struct [device](structdevice.md) \*[dev](structled__dt__spec.md#ad92b9ee24cb31fcc0a2352bcf831cecb);

[ 392](structled__dt__spec.md#a72c5ff64b89344ca9644fd2b4f4c9515) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [index](structled__dt__spec.md#a72c5ff64b89344ca9644fd2b4f4c9515);

393};

394

[ 404](group__led__interface.md#gaecc33acfc2b1dde870b411d7f30eed82)static inline int [led\_set\_brightness\_dt](group__led__interface.md#gaecc33acfc2b1dde870b411d7f30eed82)(const struct [led\_dt\_spec](structled__dt__spec.md) \*spec,

405 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

406{

407 return [led\_set\_brightness](group__led__interface.md#gaca479fd77518331f4fc84f788e345882)(spec->[dev](structled__dt__spec.md#ad92b9ee24cb31fcc0a2352bcf831cecb), spec->[index](structled__dt__spec.md#a72c5ff64b89344ca9644fd2b4f4c9515), value);

408}

409

[ 418](group__led__interface.md#gaa2b262a309e4ede4cb5715c69d900804)static inline int [led\_on\_dt](group__led__interface.md#gaa2b262a309e4ede4cb5715c69d900804)(const struct [led\_dt\_spec](structled__dt__spec.md) \*spec)

419{

420 return [led\_on](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73)(spec->[dev](structled__dt__spec.md#ad92b9ee24cb31fcc0a2352bcf831cecb), spec->[index](structled__dt__spec.md#a72c5ff64b89344ca9644fd2b4f4c9515));

421}

422

[ 431](group__led__interface.md#ga8b6618e4fea4f44f218f95fd16abc16b)static inline int [led\_off\_dt](group__led__interface.md#ga8b6618e4fea4f44f218f95fd16abc16b)(const struct [led\_dt\_spec](structled__dt__spec.md) \*spec)

432{

433 return [led\_off](group__led__interface.md#ga22c9dbe76f06fec327aebe06448d1542)(spec->[dev](structled__dt__spec.md#ad92b9ee24cb31fcc0a2352bcf831cecb), spec->[index](structled__dt__spec.md#a72c5ff64b89344ca9644fd2b4f4c9515));

434}

435

[ 444](group__led__interface.md#gaa2994b959c730dad3432481bba278497)static inline bool [led\_is\_ready\_dt](group__led__interface.md#gaa2994b959c730dad3432481bba278497)(const struct [led\_dt\_spec](structled__dt__spec.md) \*spec)

445{

446 return [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[dev](structled__dt__spec.md#ad92b9ee24cb31fcc0a2352bcf831cecb));

447}

448

[ 485](group__led__interface.md#ga537f733ae3070fbe279834c76cda35ae)#define LED\_DT\_SPEC\_GET(node\_id) \

486 { \

487 .dev = DEVICE\_DT\_GET(DT\_PARENT(node\_id)), \

488 .index = DT\_NODE\_CHILD\_IDX(node\_id), \

489 }

490

[ 500](group__led__interface.md#gade3059194ce428783ea3e9900ed0be52)#define LED\_DT\_SPEC\_GET\_OR(node\_id, default\_value) \

501 COND\_CODE\_1(DT\_NODE\_EXISTS(node\_id), \

502 (LED\_DT\_SPEC\_GET(node\_id)), \

503 (default\_value))

504

508

509#ifdef \_\_cplusplus

510}

511#endif

512

513#include <zephyr/syscalls/led.h>

514

515#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LED\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[led\_off](group__led__interface.md#ga22c9dbe76f06fec327aebe06448d1542)

int led\_off(const struct device \*dev, uint32\_t led)

Turn off an LED.

[led\_write\_channels](group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a)

int led\_write\_channels(const struct device \*dev, uint32\_t start\_channel, uint32\_t num\_channels, const uint8\_t \*buf)

Write/update a strip of LED channels.

[led\_api\_get\_info](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77)

int(\* led\_api\_get\_info)(const struct device \*dev, uint32\_t led, const struct led\_info \*\*info)

Optional API callback to get LED information.

**Definition** led.h:69

[led\_blink](group__led__interface.md#ga4f31fecd215e5597999be4d16b0d2dd5)

int led\_blink(const struct device \*dev, uint32\_t led, uint32\_t delay\_on, uint32\_t delay\_off)

Blink an LED.

[led\_api\_off](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)

int(\* led\_api\_off)(const struct device \*dev, uint32\_t led)

Callback API for turning off an LED.

**Definition** led.h:103

[led\_api\_write\_channels](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae)

int(\* led\_api\_write\_channels)(const struct device \*dev, uint32\_t start\_channel, uint32\_t num\_channels, const uint8\_t \*buf)

Callback API for writing a strip of LED channels.

**Definition** led.h:111

[led\_set\_channel](group__led__interface.md#ga717bdbe76331b6286c58feb6e3e214dd)

int led\_set\_channel(const struct device \*dev, uint32\_t channel, uint8\_t value)

Set a single LED channel.

[LED\_BRIGHTNESS\_MAX](group__led__interface.md#ga7bb18ca9f746ebcfbfc397886643f16d)

#define LED\_BRIGHTNESS\_MAX

Maximum brightness level, range is 0 to 100.

**Definition** led.h:36

[led\_off\_dt](group__led__interface.md#ga8b6618e4fea4f44f218f95fd16abc16b)

static int led\_off\_dt(const struct led\_dt\_spec \*spec)

Turn off an LED from a struct led\_dt\_spec.

**Definition** led.h:431

[led\_set\_color](group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)

int led\_set\_color(const struct device \*dev, uint32\_t led, uint8\_t num\_colors, const uint8\_t \*color)

Set LED color.

[led\_api\_set\_color](group__led__interface.md#ga977317f3208d5336463edf9979def4ae)

int(\* led\_api\_set\_color)(const struct device \*dev, uint32\_t led, uint8\_t num\_colors, const uint8\_t \*color)

Optional API callback to set the colors of a LED.

**Definition** led.h:86

[led\_get\_info](group__led__interface.md#ga9925483b97073354f7be6b40aa2dad1a)

int led\_get\_info(const struct device \*dev, uint32\_t led, const struct led\_info \*\*info)

Get LED information.

[led\_is\_ready\_dt](group__led__interface.md#gaa2994b959c730dad3432481bba278497)

static bool led\_is\_ready\_dt(const struct led\_dt\_spec \*spec)

Validate that the LED device is ready.

**Definition** led.h:444

[led\_on\_dt](group__led__interface.md#gaa2b262a309e4ede4cb5715c69d900804)

static int led\_on\_dt(const struct led\_dt\_spec \*spec)

Turn on an LED from a struct led\_dt\_spec.

**Definition** led.h:418

[led\_set\_brightness](group__led__interface.md#gaca479fd77518331f4fc84f788e345882)

int led\_set\_brightness(const struct device \*dev, uint32\_t led, uint8\_t value)

Set LED brightness.

[led\_api\_on](group__led__interface.md#gad13f55702668133575658d2ccc295339)

int(\* led\_api\_on)(const struct device \*dev, uint32\_t led)

Callback API for turning on an LED.

**Definition** led.h:95

[led\_api\_blink](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd)

int(\* led\_api\_blink)(const struct device \*dev, uint32\_t led, uint32\_t delay\_on, uint32\_t delay\_off)

Callback API for blinking an LED.

**Definition** led.h:60

[led\_on](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73)

int led\_on(const struct device \*dev, uint32\_t led)

Turn on an LED.

[led\_api\_set\_brightness](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f)

int(\* led\_api\_set\_brightness)(const struct device \*dev, uint32\_t led, uint8\_t value)

Callback API for setting brightness of an LED.

**Definition** led.h:78

[led\_set\_brightness\_dt](group__led__interface.md#gaecc33acfc2b1dde870b411d7f30eed82)

static int led\_set\_brightness\_dt(const struct led\_dt\_spec \*spec, uint8\_t value)

Set LED brightness from a led\_dt\_spec.

**Definition** led.h:404

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[led\_driver\_api](structled__driver__api.md)

LED driver API.

**Definition** led.h:119

[led\_driver\_api::off](structled__driver__api.md#a19ad736a130da2aff6bd5b299d8c33a7)

led\_api\_off off

**Definition** led.h:122

[led\_driver\_api::set\_color](structled__driver__api.md#a336f30f2c1bd3d99213cae66911c142a)

led\_api\_set\_color set\_color

**Definition** led.h:127

[led\_driver\_api::get\_info](structled__driver__api.md#a7c68219e44bcf6e766e64fd3967ecf7e)

led\_api\_get\_info get\_info

**Definition** led.h:126

[led\_driver\_api::set\_brightness](structled__driver__api.md#a9c3e3c4d40c4b8219755df6df96b0058)

led\_api\_set\_brightness set\_brightness

**Definition** led.h:123

[led\_driver\_api::on](structled__driver__api.md#a9ce7322282f8c525256d3c16a514ecc4)

led\_api\_on on

**Definition** led.h:121

[led\_driver\_api::write\_channels](structled__driver__api.md#ada1dfb1830b48afb020c7e60dbd92337)

led\_api\_write\_channels write\_channels

**Definition** led.h:128

[led\_driver\_api::blink](structled__driver__api.md#af1974c5cc20c818e0e387b34cd14ac3b)

led\_api\_blink blink

**Definition** led.h:125

[led\_dt\_spec](structled__dt__spec.md)

Container for an LED information specified in devicetree.

**Definition** led.h:388

[led\_dt\_spec::index](structled__dt__spec.md#a72c5ff64b89344ca9644fd2b4f4c9515)

uint32\_t index

Index of the LED on the controller.

**Definition** led.h:392

[led\_dt\_spec::dev](structled__dt__spec.md#ad92b9ee24cb31fcc0a2352bcf831cecb)

const struct device \* dev

LED device instance.

**Definition** led.h:390

[led\_info](structled__info.md)

LED information structure.

**Definition** led.h:43

[led\_info::label](structled__info.md#a5d01795e49663654e9fe4a821797956a)

const char \* label

LED label.

**Definition** led.h:45

[led\_info::index](structled__info.md#a7f87ebb0718e1dc189e6d48d5bb97c55)

uint32\_t index

Index of the LED on the controller.

**Definition** led.h:47

[led\_info::color\_mapping](structled__info.md#a8daacbe0a68d7ff710938722003fceaf)

const uint8\_t \* color\_mapping

Mapping of the LED colors.

**Definition** led.h:51

[led\_info::num\_colors](structled__info.md#ab6db05157b960669e3b01154a9621530)

uint8\_t num\_colors

Number of colors per LED.

**Definition** led.h:49

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led.h](drivers_2led_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
