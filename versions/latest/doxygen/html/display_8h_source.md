---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/display_8h_source.html
original_path: doxygen/html/display_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

display.h

[Go to the documentation of this file.](display_8h.md)

1/\*

2 \* Copyright (c) 2017 Jan Van Winkel <jan.van\_winkel@dxplore.eu>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DISPLAY\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_DISPLAY\_H\_

14

21

22#include <[zephyr/device.h](device_8h.md)>

23#include <[errno.h](errno_8h.md)>

24#include <stddef.h>

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/dt-bindings/display/panel.h](panel_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 40](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c)enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) {

[ 41](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a) [PIXEL\_FORMAT\_RGB\_888](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 42](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c) [PIXEL\_FORMAT\_MONO01](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 43](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c) [PIXEL\_FORMAT\_MONO10](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 44](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9) [PIXEL\_FORMAT\_ARGB\_8888](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 45](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16) [PIXEL\_FORMAT\_RGB\_565](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 46](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cae9fdd617aaf49148d4c4cb5d47189289) [PIXEL\_FORMAT\_BGR\_565](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cae9fdd617aaf49148d4c4cb5d47189289) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

47};

48

[ 56](group__display__interface.md#ga3b305be04da5921ca4087498627dc061)#define DISPLAY\_BITS\_PER\_PIXEL(fmt) \

57 ((((fmt & PIXEL\_FORMAT\_RGB\_888) >> 0) \* 24U) + \

58 (((fmt & PIXEL\_FORMAT\_MONO01) >> 1) \* 1U) + \

59 (((fmt & PIXEL\_FORMAT\_MONO10) >> 2) \* 1U) + \

60 (((fmt & PIXEL\_FORMAT\_ARGB\_8888) >> 3) \* 32U) + \

61 (((fmt & PIXEL\_FORMAT\_RGB\_565) >> 4) \* 16U) + \

62 (((fmt & PIXEL\_FORMAT\_BGR\_565) >> 5) \* 16U))

63

[ 67](group__display__interface.md#ga23030b6c27446c4579103fe38e821341)enum [display\_screen\_info](group__display__interface.md#ga23030b6c27446c4579103fe38e821341) {

[ 72](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804) [SCREEN\_INFO\_MONO\_VTILED](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 77](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d) [SCREEN\_INFO\_MONO\_MSB\_FIRST](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 81](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85) [SCREEN\_INFO\_EPD](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 85](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842) [SCREEN\_INFO\_DOUBLE\_BUFFER](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 89](group__display__interface.md#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1) [SCREEN\_INFO\_X\_ALIGNMENT\_WIDTH](group__display__interface.md#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

90};

91

[ 95](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855)enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855) {

[ 96](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2) [DISPLAY\_ORIENTATION\_NORMAL](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2),

[ 97](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc) [DISPLAY\_ORIENTATION\_ROTATED\_90](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc),

[ 98](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29) [DISPLAY\_ORIENTATION\_ROTATED\_180](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29),

[ 99](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4) [DISPLAY\_ORIENTATION\_ROTATED\_270](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4),

100};

101

[ 103](structdisplay__capabilities.md)struct [display\_capabilities](structdisplay__capabilities.md) {

[ 105](structdisplay__capabilities.md#a09fa14e2c53126d5602cb7b51e21145f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [x\_resolution](structdisplay__capabilities.md#a09fa14e2c53126d5602cb7b51e21145f);

[ 107](structdisplay__capabilities.md#a2cacb194139aaff90fd56b469f6de4a9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [y\_resolution](structdisplay__capabilities.md#a2cacb194139aaff90fd56b469f6de4a9);

[ 109](structdisplay__capabilities.md#a07548bdd9671dd696b38a5bcf1599412) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [supported\_pixel\_formats](structdisplay__capabilities.md#a07548bdd9671dd696b38a5bcf1599412);

[ 111](structdisplay__capabilities.md#ac4a9098db4c2f721fa550c6142f541a9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [screen\_info](structdisplay__capabilities.md#ac4a9098db4c2f721fa550c6142f541a9);

[ 113](structdisplay__capabilities.md#aed51c9efdc76972fecfa8a733c2a8d0c) enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) [current\_pixel\_format](structdisplay__capabilities.md#aed51c9efdc76972fecfa8a733c2a8d0c);

[ 115](structdisplay__capabilities.md#a18986f5d2c385766d5ad3d68edd85887) enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855) [current\_orientation](structdisplay__capabilities.md#a18986f5d2c385766d5ad3d68edd85887);

116};

117

[ 119](structdisplay__buffer__descriptor.md)struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) {

[ 121](structdisplay__buffer__descriptor.md#aee9f34a6944b8e28622ab06d6907d40a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [buf\_size](structdisplay__buffer__descriptor.md#aee9f34a6944b8e28622ab06d6907d40a);

[ 123](structdisplay__buffer__descriptor.md#aa35cf372266199308211d28dae789be3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [width](structdisplay__buffer__descriptor.md#aa35cf372266199308211d28dae789be3);

[ 125](structdisplay__buffer__descriptor.md#a572c6560903553b6853360fd29631b95) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [height](structdisplay__buffer__descriptor.md#a572c6560903553b6853360fd29631b95);

[ 127](structdisplay__buffer__descriptor.md#a00d7d8da4e61f404ad353b9a8f49b2eb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pitch](structdisplay__buffer__descriptor.md#a00d7d8da4e61f404ad353b9a8f49b2eb);

128};

129

[ 135](group__display__interface.md#gacf66a054396ccd8e178591b8fc98ff4d)typedef int (\*[display\_blanking\_on\_api](group__display__interface.md#gacf66a054396ccd8e178591b8fc98ff4d))(const struct [device](structdevice.md) \*dev);

136

[ 142](group__display__interface.md#gab23bbd9305792d6e37d2e4ff91a2b175)typedef int (\*[display\_blanking\_off\_api](group__display__interface.md#gab23bbd9305792d6e37d2e4ff91a2b175))(const struct [device](structdevice.md) \*dev);

143

[ 149](group__display__interface.md#ga5cab904b24062fdea531f450a8e5c367)typedef int (\*[display\_write\_api](group__display__interface.md#ga5cab904b24062fdea531f450a8e5c367))(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x,

150 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y,

151 const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

152 const void \*buf);

153

[ 159](group__display__interface.md#ga9ed51d3f666f747d9fb7f1f7746611b3)typedef int (\*[display\_read\_api](group__display__interface.md#ga9ed51d3f666f747d9fb7f1f7746611b3))(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x,

160 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y,

161 const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

162 void \*buf);

163

[ 169](group__display__interface.md#ga6dd281032ad400d3adc7f5f812c5fe12)typedef void \*(\*display\_get\_framebuffer\_api)(const struct [device](structdevice.md) \*dev);

170

[ 176](group__display__interface.md#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a)typedef int (\*[display\_set\_brightness\_api](group__display__interface.md#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a))(const struct [device](structdevice.md) \*dev,

177 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness);

178

[ 184](group__display__interface.md#gadf115352908f94b0a0bf225dbdd8ee85)typedef int (\*[display\_set\_contrast\_api](group__display__interface.md#gadf115352908f94b0a0bf225dbdd8ee85))(const struct [device](structdevice.md) \*dev,

185 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) contrast);

186

[ 192](group__display__interface.md#ga474f85a33aef019dddb1c720ea23f3fb)typedef void (\*[display\_get\_capabilities\_api](group__display__interface.md#ga474f85a33aef019dddb1c720ea23f3fb))(const struct [device](structdevice.md) \*dev,

193 struct [display\_capabilities](structdisplay__capabilities.md) \*

194 capabilities);

195

[ 201](group__display__interface.md#ga2637286cf3a97c2b532bb33f22263303)typedef int (\*[display\_set\_pixel\_format\_api](group__display__interface.md#ga2637286cf3a97c2b532bb33f22263303))(const struct [device](structdevice.md) \*dev,

202 const enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c)

203 pixel\_format);

204

[ 210](group__display__interface.md#gaff3b76a6601cf176782be940139ccb48)typedef int (\*[display\_set\_orientation\_api](group__display__interface.md#gaff3b76a6601cf176782be940139ccb48))(const struct [device](structdevice.md) \*dev,

211 const enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855)

212 orientation);

213

[ 218](structdisplay__driver__api.md)struct [display\_driver\_api](structdisplay__driver__api.md) {

[ 219](structdisplay__driver__api.md#aafdd79a11b46d4fa9288ddf3ed994c18) [display\_blanking\_on\_api](group__display__interface.md#gacf66a054396ccd8e178591b8fc98ff4d) [blanking\_on](structdisplay__driver__api.md#aafdd79a11b46d4fa9288ddf3ed994c18);

[ 220](structdisplay__driver__api.md#a128c1324f4bfab707adc93aaff0f3371) [display\_blanking\_off\_api](group__display__interface.md#gab23bbd9305792d6e37d2e4ff91a2b175) [blanking\_off](structdisplay__driver__api.md#a128c1324f4bfab707adc93aaff0f3371);

[ 221](structdisplay__driver__api.md#a535221c00caef6f24dc75c919826a889) [display\_write\_api](group__display__interface.md#ga5cab904b24062fdea531f450a8e5c367) [write](structdisplay__driver__api.md#a535221c00caef6f24dc75c919826a889);

[ 222](structdisplay__driver__api.md#a431f765057a70e5d11ceaf93e8cc119a) [display\_read\_api](group__display__interface.md#ga9ed51d3f666f747d9fb7f1f7746611b3) [read](structdisplay__driver__api.md#a431f765057a70e5d11ceaf93e8cc119a);

[ 223](structdisplay__driver__api.md#aa7843031d91003dc458be4146503b7f0) [display\_get\_framebuffer\_api](group__display__interface.md#ga6dd281032ad400d3adc7f5f812c5fe12) [get\_framebuffer](structdisplay__driver__api.md#aa7843031d91003dc458be4146503b7f0);

[ 224](structdisplay__driver__api.md#aa40c04701b60f56c8998da55c2b254a8) [display\_set\_brightness\_api](group__display__interface.md#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a) [set\_brightness](structdisplay__driver__api.md#aa40c04701b60f56c8998da55c2b254a8);

[ 225](structdisplay__driver__api.md#acfdf1662c0b362d5a35a137c903a40ba) [display\_set\_contrast\_api](group__display__interface.md#gadf115352908f94b0a0bf225dbdd8ee85) [set\_contrast](structdisplay__driver__api.md#acfdf1662c0b362d5a35a137c903a40ba);

[ 226](structdisplay__driver__api.md#ace3a2eae73f639da890b6798bd215b29) [display\_get\_capabilities\_api](group__display__interface.md#ga474f85a33aef019dddb1c720ea23f3fb) [get\_capabilities](structdisplay__driver__api.md#ace3a2eae73f639da890b6798bd215b29);

[ 227](structdisplay__driver__api.md#a28801ba7578b9ab725c62b5f0d9f2c65) [display\_set\_pixel\_format\_api](group__display__interface.md#ga2637286cf3a97c2b532bb33f22263303) [set\_pixel\_format](structdisplay__driver__api.md#a28801ba7578b9ab725c62b5f0d9f2c65);

[ 228](structdisplay__driver__api.md#a4cbccfaafeb2f24c473bd967b9bc5f14) [display\_set\_orientation\_api](group__display__interface.md#gaff3b76a6601cf176782be940139ccb48) [set\_orientation](structdisplay__driver__api.md#a4cbccfaafeb2f24c473bd967b9bc5f14);

229};

230

[ 242](group__display__interface.md#ga3a5114b4537039fc4d3258678b82cd18)static inline int [display\_write](group__display__interface.md#ga3a5114b4537039fc4d3258678b82cd18)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x,

243 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y,

244 const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

245 const void \*buf)

246{

247 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

248 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

249

250 return api->[write](structdisplay__driver__api.md#a535221c00caef6f24dc75c919826a889)(dev, x, y, desc, buf);

251}

252

[ 265](group__display__interface.md#ga3f497776520b0eac16b8aea80ccbbcfc)static inline int [display\_read](group__display__interface.md#ga3f497776520b0eac16b8aea80ccbbcfc)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x,

266 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y,

267 const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

268 void \*buf)

269{

270 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

271 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

272

273 if (api->[read](structdisplay__driver__api.md#a431f765057a70e5d11ceaf93e8cc119a) == NULL) {

274 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

275 }

276

277 return api->[read](structdisplay__driver__api.md#a431f765057a70e5d11ceaf93e8cc119a)(dev, x, y, desc, buf);

278}

279

[ 289](group__display__interface.md#ga4b66d380e46909caaa7317857f84a9e8)static inline void \*[display\_get\_framebuffer](group__display__interface.md#ga4b66d380e46909caaa7317857f84a9e8)(const struct [device](structdevice.md) \*dev)

290{

291 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

292 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

293

294 if (api->[get\_framebuffer](structdisplay__driver__api.md#aa7843031d91003dc458be4146503b7f0) == NULL) {

295 return NULL;

296 }

297

298 return api->[get\_framebuffer](structdisplay__driver__api.md#aa7843031d91003dc458be4146503b7f0)(dev);

299}

300

[ 320](group__display__interface.md#gac6ad1f33067165e4c3bf7c0c345bb4e4)static inline int [display\_blanking\_on](group__display__interface.md#gac6ad1f33067165e4c3bf7c0c345bb4e4)(const struct [device](structdevice.md) \*dev)

321{

322 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

323 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

324

325 if (api->[blanking\_on](structdisplay__driver__api.md#aafdd79a11b46d4fa9288ddf3ed994c18) == NULL) {

326 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

327 }

328

329 return api->[blanking\_on](structdisplay__driver__api.md#aafdd79a11b46d4fa9288ddf3ed994c18)(dev);

330}

331

[ 344](group__display__interface.md#ga4d9e288891a6bde679c3aa00b9913e1d)static inline int [display\_blanking\_off](group__display__interface.md#ga4d9e288891a6bde679c3aa00b9913e1d)(const struct [device](structdevice.md) \*dev)

345{

346 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

347 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

348

349 if (api->[blanking\_off](structdisplay__driver__api.md#a128c1324f4bfab707adc93aaff0f3371) == NULL) {

350 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

351 }

352

353 return api->[blanking\_off](structdisplay__driver__api.md#a128c1324f4bfab707adc93aaff0f3371)(dev);

354}

355

[ 368](group__display__interface.md#gad5cdeb245d17c8d680a5843b3cce1f8c)static inline int [display\_set\_brightness](group__display__interface.md#gad5cdeb245d17c8d680a5843b3cce1f8c)(const struct [device](structdevice.md) \*dev,

369 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness)

370{

371 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

372 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

373

374 if (api->[set\_brightness](structdisplay__driver__api.md#aa40c04701b60f56c8998da55c2b254a8) == NULL) {

375 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

376 }

377

378 return api->[set\_brightness](structdisplay__driver__api.md#aa40c04701b60f56c8998da55c2b254a8)(dev, brightness);

379}

380

[ 393](group__display__interface.md#ga855c72f72238b25f23e95e50546e2f27)static inline int [display\_set\_contrast](group__display__interface.md#ga855c72f72238b25f23e95e50546e2f27)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) contrast)

394{

395 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

396 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

397

398 if (api->[set\_contrast](structdisplay__driver__api.md#acfdf1662c0b362d5a35a137c903a40ba) == NULL) {

399 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

400 }

401

402 return api->[set\_contrast](structdisplay__driver__api.md#acfdf1662c0b362d5a35a137c903a40ba)(dev, contrast);

403}

404

[ 411](group__display__interface.md#ga6a13e42773be13b141ebd8f047f8db50)static inline void [display\_get\_capabilities](group__display__interface.md#ga6a13e42773be13b141ebd8f047f8db50)(const struct [device](structdevice.md) \*dev,

412 struct [display\_capabilities](structdisplay__capabilities.md) \*

413 capabilities)

414{

415 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

416 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

417

418 api->[get\_capabilities](structdisplay__driver__api.md#ace3a2eae73f639da890b6798bd215b29)(dev, capabilities);

419}

420

430static inline int

[ 431](group__display__interface.md#ga7ede828663090760c2558a231d9f2150)[display\_set\_pixel\_format](group__display__interface.md#ga7ede828663090760c2558a231d9f2150)(const struct [device](structdevice.md) \*dev,

432 const enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixel\_format)

433{

434 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

435 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

436

437 if (api->[set\_pixel\_format](structdisplay__driver__api.md#a28801ba7578b9ab725c62b5f0d9f2c65) == NULL) {

438 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

439 }

440

441 return api->[set\_pixel\_format](structdisplay__driver__api.md#a28801ba7578b9ab725c62b5f0d9f2c65)(dev, pixel\_format);

442}

443

[ 453](group__display__interface.md#ga4e0a4dc2e434144874af014b8e7c4394)static inline int [display\_set\_orientation](group__display__interface.md#ga4e0a4dc2e434144874af014b8e7c4394)(const struct [device](structdevice.md) \*dev,

454 const enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855)

455 orientation)

456{

457 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

458 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

459

460 if (api->[set\_orientation](structdisplay__driver__api.md#a4cbccfaafeb2f24c473bd967b9bc5f14) == NULL) {

461 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

462 }

463

464 return api->[set\_orientation](structdisplay__driver__api.md#a4cbccfaafeb2f24c473bd967b9bc5f14)(dev, orientation);

465}

466

467#ifdef \_\_cplusplus

468}

469#endif

470

474

475#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DISPLAY\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[display\_screen\_info](group__display__interface.md#ga23030b6c27446c4579103fe38e821341)

display\_screen\_info

Display screen information.

**Definition** display.h:67

[display\_set\_pixel\_format\_api](group__display__interface.md#ga2637286cf3a97c2b532bb33f22263303)

int(\* display\_set\_pixel\_format\_api)(const struct device \*dev, const enum display\_pixel\_format pixel\_format)

Callback API to set pixel format used by the display See display\_set\_pixel\_format() for argument desc...

**Definition** display.h:201

[display\_write](group__display__interface.md#ga3a5114b4537039fc4d3258678b82cd18)

static int display\_write(const struct device \*dev, const uint16\_t x, const uint16\_t y, const struct display\_buffer\_descriptor \*desc, const void \*buf)

Write data to display.

**Definition** display.h:242

[display\_read](group__display__interface.md#ga3f497776520b0eac16b8aea80ccbbcfc)

static int display\_read(const struct device \*dev, const uint16\_t x, const uint16\_t y, const struct display\_buffer\_descriptor \*desc, void \*buf)

Read data from display.

**Definition** display.h:265

[display\_get\_capabilities\_api](group__display__interface.md#ga474f85a33aef019dddb1c720ea23f3fb)

void(\* display\_get\_capabilities\_api)(const struct device \*dev, struct display\_capabilities \*capabilities)

Callback API to get display capabilities See display\_get\_capabilities() for argument description.

**Definition** display.h:192

[display\_get\_framebuffer](group__display__interface.md#ga4b66d380e46909caaa7317857f84a9e8)

static void \* display\_get\_framebuffer(const struct device \*dev)

Get pointer to framebuffer for direct access.

**Definition** display.h:289

[display\_blanking\_off](group__display__interface.md#ga4d9e288891a6bde679c3aa00b9913e1d)

static int display\_blanking\_off(const struct device \*dev)

Turn display blanking off.

**Definition** display.h:344

[display\_set\_orientation](group__display__interface.md#ga4e0a4dc2e434144874af014b8e7c4394)

static int display\_set\_orientation(const struct device \*dev, const enum display\_orientation orientation)

Set display orientation.

**Definition** display.h:453

[display\_write\_api](group__display__interface.md#ga5cab904b24062fdea531f450a8e5c367)

int(\* display\_write\_api)(const struct device \*dev, const uint16\_t x, const uint16\_t y, const struct display\_buffer\_descriptor \*desc, const void \*buf)

Callback API for writing data to the display See display\_write() for argument description.

**Definition** display.h:149

[display\_get\_capabilities](group__display__interface.md#ga6a13e42773be13b141ebd8f047f8db50)

static void display\_get\_capabilities(const struct device \*dev, struct display\_capabilities \*capabilities)

Get display capabilities.

**Definition** display.h:411

[display\_set\_brightness\_api](group__display__interface.md#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a)

int(\* display\_set\_brightness\_api)(const struct device \*dev, const uint8\_t brightness)

Callback API to set display brightness See display\_set\_brightness() for argument description.

**Definition** display.h:176

[display\_get\_framebuffer\_api](group__display__interface.md#ga6dd281032ad400d3adc7f5f812c5fe12)

void \*(\* display\_get\_framebuffer\_api)(const struct device \*dev)

Callback API to get framebuffer pointer See display\_get\_framebuffer() for argument description.

**Definition** display.h:169

[display\_set\_pixel\_format](group__display__interface.md#ga7ede828663090760c2558a231d9f2150)

static int display\_set\_pixel\_format(const struct device \*dev, const enum display\_pixel\_format pixel\_format)

Set pixel format used by the display.

**Definition** display.h:431

[display\_set\_contrast](group__display__interface.md#ga855c72f72238b25f23e95e50546e2f27)

static int display\_set\_contrast(const struct device \*dev, uint8\_t contrast)

Set the contrast of the display.

**Definition** display.h:393

[display\_read\_api](group__display__interface.md#ga9ed51d3f666f747d9fb7f1f7746611b3)

int(\* display\_read\_api)(const struct device \*dev, const uint16\_t x, const uint16\_t y, const struct display\_buffer\_descriptor \*desc, void \*buf)

Callback API for reading data from the display See display\_read() for argument description.

**Definition** display.h:159

[display\_blanking\_off\_api](group__display__interface.md#gab23bbd9305792d6e37d2e4ff91a2b175)

int(\* display\_blanking\_off\_api)(const struct device \*dev)

Callback API to turn off display blanking See display\_blanking\_off() for argument description.

**Definition** display.h:142

[display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c)

display\_pixel\_format

Display pixel formats.

**Definition** display.h:40

[display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855)

display\_orientation

Enumeration with possible display orientation.

**Definition** display.h:95

[display\_blanking\_on](group__display__interface.md#gac6ad1f33067165e4c3bf7c0c345bb4e4)

static int display\_blanking\_on(const struct device \*dev)

Turn display blanking on.

**Definition** display.h:320

[display\_blanking\_on\_api](group__display__interface.md#gacf66a054396ccd8e178591b8fc98ff4d)

int(\* display\_blanking\_on\_api)(const struct device \*dev)

Callback API to turn on display blanking See display\_blanking\_on() for argument description.

**Definition** display.h:135

[display\_set\_brightness](group__display__interface.md#gad5cdeb245d17c8d680a5843b3cce1f8c)

static int display\_set\_brightness(const struct device \*dev, uint8\_t brightness)

Set the brightness of the display.

**Definition** display.h:368

[display\_set\_contrast\_api](group__display__interface.md#gadf115352908f94b0a0bf225dbdd8ee85)

int(\* display\_set\_contrast\_api)(const struct device \*dev, const uint8\_t contrast)

Callback API to set display contrast See display\_set\_contrast() for argument description.

**Definition** display.h:184

[display\_set\_orientation\_api](group__display__interface.md#gaff3b76a6601cf176782be940139ccb48)

int(\* display\_set\_orientation\_api)(const struct device \*dev, const enum display\_orientation orientation)

Callback API to set orientation used by the display See display\_set\_orientation() for argument descri...

**Definition** display.h:210

[SCREEN\_INFO\_X\_ALIGNMENT\_WIDTH](group__display__interface.md#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1)

@ SCREEN\_INFO\_X\_ALIGNMENT\_WIDTH

Screen has x alignment constrained to width.

**Definition** display.h:89

[SCREEN\_INFO\_EPD](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85)

@ SCREEN\_INFO\_EPD

Electrophoretic Display.

**Definition** display.h:81

[SCREEN\_INFO\_DOUBLE\_BUFFER](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842)

@ SCREEN\_INFO\_DOUBLE\_BUFFER

Screen has two alternating ram buffers.

**Definition** display.h:85

[SCREEN\_INFO\_MONO\_VTILED](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804)

@ SCREEN\_INFO\_MONO\_VTILED

If selected, one octet represents 8 pixels ordered vertically, otherwise ordered horizontally.

**Definition** display.h:72

[SCREEN\_INFO\_MONO\_MSB\_FIRST](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d)

@ SCREEN\_INFO\_MONO\_MSB\_FIRST

If selected, the MSB represents the first pixel, otherwise MSB represents the last pixel.

**Definition** display.h:77

[PIXEL\_FORMAT\_MONO10](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c)

@ PIXEL\_FORMAT\_MONO10

Monochrome (1=Black 0=White).

**Definition** display.h:43

[PIXEL\_FORMAT\_ARGB\_8888](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9)

@ PIXEL\_FORMAT\_ARGB\_8888

32-bit ARGB

**Definition** display.h:44

[PIXEL\_FORMAT\_MONO01](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c)

@ PIXEL\_FORMAT\_MONO01

Monochrome (0=Black 1=White).

**Definition** display.h:42

[PIXEL\_FORMAT\_RGB\_565](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16)

@ PIXEL\_FORMAT\_RGB\_565

16-bit RGB

**Definition** display.h:45

[PIXEL\_FORMAT\_RGB\_888](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a)

@ PIXEL\_FORMAT\_RGB\_888

24-bit RGB

**Definition** display.h:41

[PIXEL\_FORMAT\_BGR\_565](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cae9fdd617aaf49148d4c4cb5d47189289)

@ PIXEL\_FORMAT\_BGR\_565

16-bit BGR

**Definition** display.h:46

[DISPLAY\_ORIENTATION\_ROTATED\_90](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc)

@ DISPLAY\_ORIENTATION\_ROTATED\_90

Rotated 90 degrees clockwise.

**Definition** display.h:97

[DISPLAY\_ORIENTATION\_ROTATED\_180](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29)

@ DISPLAY\_ORIENTATION\_ROTATED\_180

Rotated 180 degrees clockwise.

**Definition** display.h:98

[DISPLAY\_ORIENTATION\_NORMAL](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2)

@ DISPLAY\_ORIENTATION\_NORMAL

No rotation.

**Definition** display.h:96

[DISPLAY\_ORIENTATION\_ROTATED\_270](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4)

@ DISPLAY\_ORIENTATION\_ROTATED\_270

Rotated 270 degrees clockwise.

**Definition** display.h:99

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[panel.h](panel_8h.md)

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

[display\_buffer\_descriptor](structdisplay__buffer__descriptor.md)

Structure to describe display data buffer layout.

**Definition** display.h:119

[display\_buffer\_descriptor::pitch](structdisplay__buffer__descriptor.md#a00d7d8da4e61f404ad353b9a8f49b2eb)

uint16\_t pitch

Number of pixels between consecutive rows in the data buffer.

**Definition** display.h:127

[display\_buffer\_descriptor::height](structdisplay__buffer__descriptor.md#a572c6560903553b6853360fd29631b95)

uint16\_t height

Data buffer column height in pixels.

**Definition** display.h:125

[display\_buffer\_descriptor::width](structdisplay__buffer__descriptor.md#aa35cf372266199308211d28dae789be3)

uint16\_t width

Data buffer row width in pixels.

**Definition** display.h:123

[display\_buffer\_descriptor::buf\_size](structdisplay__buffer__descriptor.md#aee9f34a6944b8e28622ab06d6907d40a)

uint32\_t buf\_size

Data buffer size in bytes.

**Definition** display.h:121

[display\_capabilities](structdisplay__capabilities.md)

Structure holding display capabilities.

**Definition** display.h:103

[display\_capabilities::supported\_pixel\_formats](structdisplay__capabilities.md#a07548bdd9671dd696b38a5bcf1599412)

uint32\_t supported\_pixel\_formats

Bitwise or of pixel formats supported by the display.

**Definition** display.h:109

[display\_capabilities::x\_resolution](structdisplay__capabilities.md#a09fa14e2c53126d5602cb7b51e21145f)

uint16\_t x\_resolution

Display resolution in the X direction.

**Definition** display.h:105

[display\_capabilities::current\_orientation](structdisplay__capabilities.md#a18986f5d2c385766d5ad3d68edd85887)

enum display\_orientation current\_orientation

Current display orientation.

**Definition** display.h:115

[display\_capabilities::y\_resolution](structdisplay__capabilities.md#a2cacb194139aaff90fd56b469f6de4a9)

uint16\_t y\_resolution

Display resolution in the Y direction.

**Definition** display.h:107

[display\_capabilities::screen\_info](structdisplay__capabilities.md#ac4a9098db4c2f721fa550c6142f541a9)

uint32\_t screen\_info

Information about display panel.

**Definition** display.h:111

[display\_capabilities::current\_pixel\_format](structdisplay__capabilities.md#aed51c9efdc76972fecfa8a733c2a8d0c)

enum display\_pixel\_format current\_pixel\_format

Currently active pixel format for the display.

**Definition** display.h:113

[display\_driver\_api](structdisplay__driver__api.md)

Display driver API API which a display driver should expose.

**Definition** display.h:218

[display\_driver\_api::blanking\_off](structdisplay__driver__api.md#a128c1324f4bfab707adc93aaff0f3371)

display\_blanking\_off\_api blanking\_off

**Definition** display.h:220

[display\_driver\_api::set\_pixel\_format](structdisplay__driver__api.md#a28801ba7578b9ab725c62b5f0d9f2c65)

display\_set\_pixel\_format\_api set\_pixel\_format

**Definition** display.h:227

[display\_driver\_api::read](structdisplay__driver__api.md#a431f765057a70e5d11ceaf93e8cc119a)

display\_read\_api read

**Definition** display.h:222

[display\_driver\_api::set\_orientation](structdisplay__driver__api.md#a4cbccfaafeb2f24c473bd967b9bc5f14)

display\_set\_orientation\_api set\_orientation

**Definition** display.h:228

[display\_driver\_api::write](structdisplay__driver__api.md#a535221c00caef6f24dc75c919826a889)

display\_write\_api write

**Definition** display.h:221

[display\_driver\_api::set\_brightness](structdisplay__driver__api.md#aa40c04701b60f56c8998da55c2b254a8)

display\_set\_brightness\_api set\_brightness

**Definition** display.h:224

[display\_driver\_api::get\_framebuffer](structdisplay__driver__api.md#aa7843031d91003dc458be4146503b7f0)

display\_get\_framebuffer\_api get\_framebuffer

**Definition** display.h:223

[display\_driver\_api::blanking\_on](structdisplay__driver__api.md#aafdd79a11b46d4fa9288ddf3ed994c18)

display\_blanking\_on\_api blanking\_on

**Definition** display.h:219

[display\_driver\_api::get\_capabilities](structdisplay__driver__api.md#ace3a2eae73f639da890b6798bd215b29)

display\_get\_capabilities\_api get\_capabilities

**Definition** display.h:226

[display\_driver\_api::set\_contrast](structdisplay__driver__api.md#acfdf1662c0b362d5a35a137c903a40ba)

display\_set\_contrast\_api set\_contrast

**Definition** display.h:225

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [display.h](display_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
