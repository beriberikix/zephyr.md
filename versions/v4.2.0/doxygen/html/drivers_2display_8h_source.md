---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2display_8h_source.html
original_path: doxygen/html/drivers_2display_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

display.h

[Go to the documentation of this file.](drivers_2display_8h.md)

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

23

24#include <[zephyr/device.h](device_8h.md)>

25#include <[errno.h](errno_8h.md)>

26#include <stddef.h>

27#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

28#include <[zephyr/dt-bindings/display/panel.h](panel_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 42](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c)enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) {

[ 43](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a) [PIXEL\_FORMAT\_RGB\_888](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 44](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c) [PIXEL\_FORMAT\_MONO01](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 45](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c) [PIXEL\_FORMAT\_MONO10](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 46](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9) [PIXEL\_FORMAT\_ARGB\_8888](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 47](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16) [PIXEL\_FORMAT\_RGB\_565](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 48](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cae9fdd617aaf49148d4c4cb5d47189289) [PIXEL\_FORMAT\_BGR\_565](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cae9fdd617aaf49148d4c4cb5d47189289) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 49](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca14f33dfec4a630f5be50622a535434df) [PIXEL\_FORMAT\_L\_8](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca14f33dfec4a630f5be50622a535434df) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

51};

52

[ 60](group__display__interface.md#ga3b305be04da5921ca4087498627dc061)#define DISPLAY\_BITS\_PER\_PIXEL(fmt) \

61 ((((fmt & PIXEL\_FORMAT\_RGB\_888) >> 0) \* 24U) + \

62 (((fmt & PIXEL\_FORMAT\_MONO01) >> 1) \* 1U) + \

63 (((fmt & PIXEL\_FORMAT\_MONO10) >> 2) \* 1U) + \

64 (((fmt & PIXEL\_FORMAT\_ARGB\_8888) >> 3) \* 32U) + \

65 (((fmt & PIXEL\_FORMAT\_RGB\_565) >> 4) \* 16U) + \

66 (((fmt & PIXEL\_FORMAT\_BGR\_565) >> 5) \* 16U) + \

67 (((fmt & PIXEL\_FORMAT\_L\_8) >> 6) \* 8U))

68

[ 72](group__display__interface.md#ga23030b6c27446c4579103fe38e821341)enum [display\_screen\_info](group__display__interface.md#ga23030b6c27446c4579103fe38e821341) {

[ 77](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804) [SCREEN\_INFO\_MONO\_VTILED](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 82](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d) [SCREEN\_INFO\_MONO\_MSB\_FIRST](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 86](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85) [SCREEN\_INFO\_EPD](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 90](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842) [SCREEN\_INFO\_DOUBLE\_BUFFER](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 94](group__display__interface.md#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1) [SCREEN\_INFO\_X\_ALIGNMENT\_WIDTH](group__display__interface.md#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

95};

96

[ 100](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855)enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855) {

[ 101](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2) [DISPLAY\_ORIENTATION\_NORMAL](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2),

[ 102](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc) [DISPLAY\_ORIENTATION\_ROTATED\_90](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc),

[ 103](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29) [DISPLAY\_ORIENTATION\_ROTATED\_180](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29),

[ 104](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4) [DISPLAY\_ORIENTATION\_ROTATED\_270](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4),

105};

106

[ 108](structdisplay__capabilities.md)struct [display\_capabilities](structdisplay__capabilities.md) {

[ 110](structdisplay__capabilities.md#a09fa14e2c53126d5602cb7b51e21145f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [x\_resolution](structdisplay__capabilities.md#a09fa14e2c53126d5602cb7b51e21145f);

[ 112](structdisplay__capabilities.md#a2cacb194139aaff90fd56b469f6de4a9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [y\_resolution](structdisplay__capabilities.md#a2cacb194139aaff90fd56b469f6de4a9);

[ 114](structdisplay__capabilities.md#a07548bdd9671dd696b38a5bcf1599412) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [supported\_pixel\_formats](structdisplay__capabilities.md#a07548bdd9671dd696b38a5bcf1599412);

[ 116](structdisplay__capabilities.md#ac4a9098db4c2f721fa550c6142f541a9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [screen\_info](structdisplay__capabilities.md#ac4a9098db4c2f721fa550c6142f541a9);

[ 118](structdisplay__capabilities.md#aed51c9efdc76972fecfa8a733c2a8d0c) enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) [current\_pixel\_format](structdisplay__capabilities.md#aed51c9efdc76972fecfa8a733c2a8d0c);

[ 120](structdisplay__capabilities.md#a18986f5d2c385766d5ad3d68edd85887) enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855) [current\_orientation](structdisplay__capabilities.md#a18986f5d2c385766d5ad3d68edd85887);

121};

122

[ 124](structdisplay__buffer__descriptor.md)struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) {

[ 126](structdisplay__buffer__descriptor.md#aee9f34a6944b8e28622ab06d6907d40a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [buf\_size](structdisplay__buffer__descriptor.md#aee9f34a6944b8e28622ab06d6907d40a);

[ 128](structdisplay__buffer__descriptor.md#aa35cf372266199308211d28dae789be3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [width](structdisplay__buffer__descriptor.md#aa35cf372266199308211d28dae789be3);

[ 130](structdisplay__buffer__descriptor.md#a572c6560903553b6853360fd29631b95) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [height](structdisplay__buffer__descriptor.md#a572c6560903553b6853360fd29631b95);

[ 132](structdisplay__buffer__descriptor.md#a00d7d8da4e61f404ad353b9a8f49b2eb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pitch](structdisplay__buffer__descriptor.md#a00d7d8da4e61f404ad353b9a8f49b2eb);

[ 134](structdisplay__buffer__descriptor.md#a29e49359561cc0c601196eb9cf1f93b7) bool [frame\_incomplete](structdisplay__buffer__descriptor.md#a29e49359561cc0c601196eb9cf1f93b7);

135};

136

[ 142](group__display__interface.md#gacf66a054396ccd8e178591b8fc98ff4d)typedef int (\*[display\_blanking\_on\_api](group__display__interface.md#gacf66a054396ccd8e178591b8fc98ff4d))(const struct [device](structdevice.md) \*dev);

143

[ 149](group__display__interface.md#gab23bbd9305792d6e37d2e4ff91a2b175)typedef int (\*[display\_blanking\_off\_api](group__display__interface.md#gab23bbd9305792d6e37d2e4ff91a2b175))(const struct [device](structdevice.md) \*dev);

150

[ 156](group__display__interface.md#ga5cab904b24062fdea531f450a8e5c367)typedef int (\*[display\_write\_api](group__display__interface.md#ga5cab904b24062fdea531f450a8e5c367))(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x,

157 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y,

158 const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

159 const void \*buf);

160

[ 166](group__display__interface.md#ga9ed51d3f666f747d9fb7f1f7746611b3)typedef int (\*[display\_read\_api](group__display__interface.md#ga9ed51d3f666f747d9fb7f1f7746611b3))(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x,

167 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y,

168 const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

169 void \*buf);

170

[ 176](group__display__interface.md#gaf42820ae69452788bf51f37512ca8586)typedef int (\*[display\_clear\_api](group__display__interface.md#gaf42820ae69452788bf51f37512ca8586))(const struct [device](structdevice.md) \*dev);

177

[ 183](group__display__interface.md#ga6dd281032ad400d3adc7f5f812c5fe12)typedef void \*(\*display\_get\_framebuffer\_api)(const struct [device](structdevice.md) \*dev);

184

[ 190](group__display__interface.md#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a)typedef int (\*[display\_set\_brightness\_api](group__display__interface.md#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a))(const struct [device](structdevice.md) \*dev,

191 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness);

192

[ 198](group__display__interface.md#gadf115352908f94b0a0bf225dbdd8ee85)typedef int (\*[display\_set\_contrast\_api](group__display__interface.md#gadf115352908f94b0a0bf225dbdd8ee85))(const struct [device](structdevice.md) \*dev,

199 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) contrast);

200

[ 206](group__display__interface.md#ga474f85a33aef019dddb1c720ea23f3fb)typedef void (\*[display\_get\_capabilities\_api](group__display__interface.md#ga474f85a33aef019dddb1c720ea23f3fb))(const struct [device](structdevice.md) \*dev,

207 struct [display\_capabilities](structdisplay__capabilities.md) \*

208 capabilities);

209

[ 215](group__display__interface.md#ga2637286cf3a97c2b532bb33f22263303)typedef int (\*[display\_set\_pixel\_format\_api](group__display__interface.md#ga2637286cf3a97c2b532bb33f22263303))(const struct [device](structdevice.md) \*dev,

216 const enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c)

217 pixel\_format);

218

[ 224](group__display__interface.md#gaff3b76a6601cf176782be940139ccb48)typedef int (\*[display\_set\_orientation\_api](group__display__interface.md#gaff3b76a6601cf176782be940139ccb48))(const struct [device](structdevice.md) \*dev,

225 const enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855)

226 orientation);

227

[ 232](structdisplay__driver__api.md)\_\_subsystem struct [display\_driver\_api](structdisplay__driver__api.md) {

[ 233](structdisplay__driver__api.md#aafdd79a11b46d4fa9288ddf3ed994c18) [display\_blanking\_on\_api](group__display__interface.md#gacf66a054396ccd8e178591b8fc98ff4d) [blanking\_on](structdisplay__driver__api.md#aafdd79a11b46d4fa9288ddf3ed994c18);

[ 234](structdisplay__driver__api.md#a128c1324f4bfab707adc93aaff0f3371) [display\_blanking\_off\_api](group__display__interface.md#gab23bbd9305792d6e37d2e4ff91a2b175) [blanking\_off](structdisplay__driver__api.md#a128c1324f4bfab707adc93aaff0f3371);

[ 235](structdisplay__driver__api.md#a535221c00caef6f24dc75c919826a889) [display\_write\_api](group__display__interface.md#ga5cab904b24062fdea531f450a8e5c367) [write](structdisplay__driver__api.md#a535221c00caef6f24dc75c919826a889);

[ 236](structdisplay__driver__api.md#a431f765057a70e5d11ceaf93e8cc119a) [display\_read\_api](group__display__interface.md#ga9ed51d3f666f747d9fb7f1f7746611b3) [read](structdisplay__driver__api.md#a431f765057a70e5d11ceaf93e8cc119a);

[ 237](structdisplay__driver__api.md#a913e21f2f3cdf6c20d0b3d00ec698b12) [display\_clear\_api](group__display__interface.md#gaf42820ae69452788bf51f37512ca8586) [clear](structdisplay__driver__api.md#a913e21f2f3cdf6c20d0b3d00ec698b12);

[ 238](structdisplay__driver__api.md#aa7843031d91003dc458be4146503b7f0) [display\_get\_framebuffer\_api](group__display__interface.md#ga6dd281032ad400d3adc7f5f812c5fe12) [get\_framebuffer](structdisplay__driver__api.md#aa7843031d91003dc458be4146503b7f0);

[ 239](structdisplay__driver__api.md#aa40c04701b60f56c8998da55c2b254a8) [display\_set\_brightness\_api](group__display__interface.md#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a) [set\_brightness](structdisplay__driver__api.md#aa40c04701b60f56c8998da55c2b254a8);

[ 240](structdisplay__driver__api.md#acfdf1662c0b362d5a35a137c903a40ba) [display\_set\_contrast\_api](group__display__interface.md#gadf115352908f94b0a0bf225dbdd8ee85) [set\_contrast](structdisplay__driver__api.md#acfdf1662c0b362d5a35a137c903a40ba);

[ 241](structdisplay__driver__api.md#ace3a2eae73f639da890b6798bd215b29) [display\_get\_capabilities\_api](group__display__interface.md#ga474f85a33aef019dddb1c720ea23f3fb) [get\_capabilities](structdisplay__driver__api.md#ace3a2eae73f639da890b6798bd215b29);

[ 242](structdisplay__driver__api.md#a28801ba7578b9ab725c62b5f0d9f2c65) [display\_set\_pixel\_format\_api](group__display__interface.md#ga2637286cf3a97c2b532bb33f22263303) [set\_pixel\_format](structdisplay__driver__api.md#a28801ba7578b9ab725c62b5f0d9f2c65);

[ 243](structdisplay__driver__api.md#a4cbccfaafeb2f24c473bd967b9bc5f14) [display\_set\_orientation\_api](group__display__interface.md#gaff3b76a6601cf176782be940139ccb48) [set\_orientation](structdisplay__driver__api.md#a4cbccfaafeb2f24c473bd967b9bc5f14);

244};

245

[ 257](group__display__interface.md#ga3a5114b4537039fc4d3258678b82cd18)static inline int [display\_write](group__display__interface.md#ga3a5114b4537039fc4d3258678b82cd18)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x,

258 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y,

259 const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

260 const void \*buf)

261{

262 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

263 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

264

265 return api->[write](structdisplay__driver__api.md#a535221c00caef6f24dc75c919826a889)(dev, x, y, desc, buf);

266}

267

[ 280](group__display__interface.md#ga3f497776520b0eac16b8aea80ccbbcfc)static inline int [display\_read](group__display__interface.md#ga3f497776520b0eac16b8aea80ccbbcfc)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x,

281 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y,

282 const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

283 void \*buf)

284{

285 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

286 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

287

288 if (api->[read](structdisplay__driver__api.md#a431f765057a70e5d11ceaf93e8cc119a) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

289 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

290 }

291

292 return api->[read](structdisplay__driver__api.md#a431f765057a70e5d11ceaf93e8cc119a)(dev, x, y, desc, buf);

293}

294

[ 303](group__display__interface.md#ga62a6cd9e338aa07f789de60e64d3b3c4)static inline int [display\_clear](group__display__interface.md#ga62a6cd9e338aa07f789de60e64d3b3c4)(const struct [device](structdevice.md) \*dev)

304{

305 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

306 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

307

308 if (api->[clear](structdisplay__driver__api.md#a913e21f2f3cdf6c20d0b3d00ec698b12) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

309 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

310 }

311

312 return api->[clear](structdisplay__driver__api.md#a913e21f2f3cdf6c20d0b3d00ec698b12)(dev);

313}

314

[ 324](group__display__interface.md#ga4b66d380e46909caaa7317857f84a9e8)static inline void \*[display\_get\_framebuffer](group__display__interface.md#ga4b66d380e46909caaa7317857f84a9e8)(const struct [device](structdevice.md) \*dev)

325{

326 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

327 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

328

329 if (api->[get\_framebuffer](structdisplay__driver__api.md#aa7843031d91003dc458be4146503b7f0) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

330 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

331 }

332

333 return api->[get\_framebuffer](structdisplay__driver__api.md#aa7843031d91003dc458be4146503b7f0)(dev);

334}

335

[ 355](group__display__interface.md#gac6ad1f33067165e4c3bf7c0c345bb4e4)static inline int [display\_blanking\_on](group__display__interface.md#gac6ad1f33067165e4c3bf7c0c345bb4e4)(const struct [device](structdevice.md) \*dev)

356{

357 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

358 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

359

360 if (api->[blanking\_on](structdisplay__driver__api.md#aafdd79a11b46d4fa9288ddf3ed994c18) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

361 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

362 }

363

364 return api->[blanking\_on](structdisplay__driver__api.md#aafdd79a11b46d4fa9288ddf3ed994c18)(dev);

365}

366

[ 379](group__display__interface.md#ga4d9e288891a6bde679c3aa00b9913e1d)static inline int [display\_blanking\_off](group__display__interface.md#ga4d9e288891a6bde679c3aa00b9913e1d)(const struct [device](structdevice.md) \*dev)

380{

381 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

382 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

383

384 if (api->[blanking\_off](structdisplay__driver__api.md#a128c1324f4bfab707adc93aaff0f3371) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

385 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

386 }

387

388 return api->[blanking\_off](structdisplay__driver__api.md#a128c1324f4bfab707adc93aaff0f3371)(dev);

389}

390

[ 403](group__display__interface.md#gad5cdeb245d17c8d680a5843b3cce1f8c)static inline int [display\_set\_brightness](group__display__interface.md#gad5cdeb245d17c8d680a5843b3cce1f8c)(const struct [device](structdevice.md) \*dev,

404 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness)

405{

406 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

407 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

408

409 if (api->[set\_brightness](structdisplay__driver__api.md#aa40c04701b60f56c8998da55c2b254a8) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

410 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

411 }

412

413 return api->[set\_brightness](structdisplay__driver__api.md#aa40c04701b60f56c8998da55c2b254a8)(dev, brightness);

414}

415

[ 428](group__display__interface.md#ga855c72f72238b25f23e95e50546e2f27)static inline int [display\_set\_contrast](group__display__interface.md#ga855c72f72238b25f23e95e50546e2f27)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) contrast)

429{

430 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

431 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

432

433 if (api->[set\_contrast](structdisplay__driver__api.md#acfdf1662c0b362d5a35a137c903a40ba) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

434 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

435 }

436

437 return api->[set\_contrast](structdisplay__driver__api.md#acfdf1662c0b362d5a35a137c903a40ba)(dev, contrast);

438}

439

[ 446](group__display__interface.md#ga6a13e42773be13b141ebd8f047f8db50)static inline void [display\_get\_capabilities](group__display__interface.md#ga6a13e42773be13b141ebd8f047f8db50)(const struct [device](structdevice.md) \*dev,

447 struct [display\_capabilities](structdisplay__capabilities.md) \*

448 capabilities)

449{

450 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

451 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

452

453 api->[get\_capabilities](structdisplay__driver__api.md#ace3a2eae73f639da890b6798bd215b29)(dev, capabilities);

454}

455

465static inline int

[ 466](group__display__interface.md#ga7ede828663090760c2558a231d9f2150)[display\_set\_pixel\_format](group__display__interface.md#ga7ede828663090760c2558a231d9f2150)(const struct [device](structdevice.md) \*dev,

467 const enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixel\_format)

468{

469 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

470 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

471

472 if (api->[set\_pixel\_format](structdisplay__driver__api.md#a28801ba7578b9ab725c62b5f0d9f2c65) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

473 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

474 }

475

476 return api->[set\_pixel\_format](structdisplay__driver__api.md#a28801ba7578b9ab725c62b5f0d9f2c65)(dev, pixel\_format);

477}

478

[ 488](group__display__interface.md#ga4e0a4dc2e434144874af014b8e7c4394)static inline int [display\_set\_orientation](group__display__interface.md#ga4e0a4dc2e434144874af014b8e7c4394)(const struct [device](structdevice.md) \*dev,

489 const enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855)

490 orientation)

491{

492 struct [display\_driver\_api](structdisplay__driver__api.md) \*api =

493 (struct [display\_driver\_api](structdisplay__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

494

495 if (api->[set\_orientation](structdisplay__driver__api.md#a4cbccfaafeb2f24c473bd967b9bc5f14) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

496 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

497 }

498

499 return api->[set\_orientation](structdisplay__driver__api.md#a4cbccfaafeb2f24c473bd967b9bc5f14)(dev, orientation);

500}

501

502#ifdef \_\_cplusplus

503}

504#endif

505

509

510#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DISPLAY\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[display\_screen\_info](group__display__interface.md#ga23030b6c27446c4579103fe38e821341)

display\_screen\_info

Display screen information.

**Definition** display.h:72

[display\_set\_pixel\_format\_api](group__display__interface.md#ga2637286cf3a97c2b532bb33f22263303)

int(\* display\_set\_pixel\_format\_api)(const struct device \*dev, const enum display\_pixel\_format pixel\_format)

Callback API to set pixel format used by the display See display\_set\_pixel\_format() for argument desc...

**Definition** display.h:215

[display\_write](group__display__interface.md#ga3a5114b4537039fc4d3258678b82cd18)

static int display\_write(const struct device \*dev, const uint16\_t x, const uint16\_t y, const struct display\_buffer\_descriptor \*desc, const void \*buf)

Write data to display.

**Definition** display.h:257

[display\_read](group__display__interface.md#ga3f497776520b0eac16b8aea80ccbbcfc)

static int display\_read(const struct device \*dev, const uint16\_t x, const uint16\_t y, const struct display\_buffer\_descriptor \*desc, void \*buf)

Read data from display.

**Definition** display.h:280

[display\_get\_capabilities\_api](group__display__interface.md#ga474f85a33aef019dddb1c720ea23f3fb)

void(\* display\_get\_capabilities\_api)(const struct device \*dev, struct display\_capabilities \*capabilities)

Callback API to get display capabilities See display\_get\_capabilities() for argument description.

**Definition** display.h:206

[display\_get\_framebuffer](group__display__interface.md#ga4b66d380e46909caaa7317857f84a9e8)

static void \* display\_get\_framebuffer(const struct device \*dev)

Get pointer to framebuffer for direct access.

**Definition** display.h:324

[display\_blanking\_off](group__display__interface.md#ga4d9e288891a6bde679c3aa00b9913e1d)

static int display\_blanking\_off(const struct device \*dev)

Turn display blanking off.

**Definition** display.h:379

[display\_set\_orientation](group__display__interface.md#ga4e0a4dc2e434144874af014b8e7c4394)

static int display\_set\_orientation(const struct device \*dev, const enum display\_orientation orientation)

Set display orientation.

**Definition** display.h:488

[display\_write\_api](group__display__interface.md#ga5cab904b24062fdea531f450a8e5c367)

int(\* display\_write\_api)(const struct device \*dev, const uint16\_t x, const uint16\_t y, const struct display\_buffer\_descriptor \*desc, const void \*buf)

Callback API for writing data to the display See display\_write() for argument description.

**Definition** display.h:156

[display\_clear](group__display__interface.md#ga62a6cd9e338aa07f789de60e64d3b3c4)

static int display\_clear(const struct device \*dev)

Clear the screen of the display device.

**Definition** display.h:303

[display\_get\_capabilities](group__display__interface.md#ga6a13e42773be13b141ebd8f047f8db50)

static void display\_get\_capabilities(const struct device \*dev, struct display\_capabilities \*capabilities)

Get display capabilities.

**Definition** display.h:446

[display\_set\_brightness\_api](group__display__interface.md#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a)

int(\* display\_set\_brightness\_api)(const struct device \*dev, const uint8\_t brightness)

Callback API to set display brightness See display\_set\_brightness() for argument description.

**Definition** display.h:190

[display\_get\_framebuffer\_api](group__display__interface.md#ga6dd281032ad400d3adc7f5f812c5fe12)

void \*(\* display\_get\_framebuffer\_api)(const struct device \*dev)

Callback API to get framebuffer pointer See display\_get\_framebuffer() for argument description.

**Definition** display.h:183

[display\_set\_pixel\_format](group__display__interface.md#ga7ede828663090760c2558a231d9f2150)

static int display\_set\_pixel\_format(const struct device \*dev, const enum display\_pixel\_format pixel\_format)

Set pixel format used by the display.

**Definition** display.h:466

[display\_set\_contrast](group__display__interface.md#ga855c72f72238b25f23e95e50546e2f27)

static int display\_set\_contrast(const struct device \*dev, uint8\_t contrast)

Set the contrast of the display.

**Definition** display.h:428

[display\_read\_api](group__display__interface.md#ga9ed51d3f666f747d9fb7f1f7746611b3)

int(\* display\_read\_api)(const struct device \*dev, const uint16\_t x, const uint16\_t y, const struct display\_buffer\_descriptor \*desc, void \*buf)

Callback API for reading data from the display See display\_read() for argument description.

**Definition** display.h:166

[display\_blanking\_off\_api](group__display__interface.md#gab23bbd9305792d6e37d2e4ff91a2b175)

int(\* display\_blanking\_off\_api)(const struct device \*dev)

Callback API to turn off display blanking See display\_blanking\_off() for argument description.

**Definition** display.h:149

[display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c)

display\_pixel\_format

Display pixel formats.

**Definition** display.h:42

[display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855)

display\_orientation

Enumeration with possible display orientation.

**Definition** display.h:100

[display\_blanking\_on](group__display__interface.md#gac6ad1f33067165e4c3bf7c0c345bb4e4)

static int display\_blanking\_on(const struct device \*dev)

Turn display blanking on.

**Definition** display.h:355

[display\_blanking\_on\_api](group__display__interface.md#gacf66a054396ccd8e178591b8fc98ff4d)

int(\* display\_blanking\_on\_api)(const struct device \*dev)

Callback API to turn on display blanking See display\_blanking\_on() for argument description.

**Definition** display.h:142

[display\_set\_brightness](group__display__interface.md#gad5cdeb245d17c8d680a5843b3cce1f8c)

static int display\_set\_brightness(const struct device \*dev, uint8\_t brightness)

Set the brightness of the display.

**Definition** display.h:403

[display\_set\_contrast\_api](group__display__interface.md#gadf115352908f94b0a0bf225dbdd8ee85)

int(\* display\_set\_contrast\_api)(const struct device \*dev, const uint8\_t contrast)

Callback API to set display contrast See display\_set\_contrast() for argument description.

**Definition** display.h:198

[display\_clear\_api](group__display__interface.md#gaf42820ae69452788bf51f37512ca8586)

int(\* display\_clear\_api)(const struct device \*dev)

**Definition** display.h:176

[display\_set\_orientation\_api](group__display__interface.md#gaff3b76a6601cf176782be940139ccb48)

int(\* display\_set\_orientation\_api)(const struct device \*dev, const enum display\_orientation orientation)

Callback API to set orientation used by the display See display\_set\_orientation() for argument descri...

**Definition** display.h:224

[SCREEN\_INFO\_X\_ALIGNMENT\_WIDTH](group__display__interface.md#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1)

@ SCREEN\_INFO\_X\_ALIGNMENT\_WIDTH

Screen has x alignment constrained to width.

**Definition** display.h:94

[SCREEN\_INFO\_EPD](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85)

@ SCREEN\_INFO\_EPD

Electrophoretic Display.

**Definition** display.h:86

[SCREEN\_INFO\_DOUBLE\_BUFFER](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842)

@ SCREEN\_INFO\_DOUBLE\_BUFFER

Screen has two alternating ram buffers.

**Definition** display.h:90

[SCREEN\_INFO\_MONO\_VTILED](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804)

@ SCREEN\_INFO\_MONO\_VTILED

If selected, one octet represents 8 pixels ordered vertically, otherwise ordered horizontally.

**Definition** display.h:77

[SCREEN\_INFO\_MONO\_MSB\_FIRST](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d)

@ SCREEN\_INFO\_MONO\_MSB\_FIRST

If selected, the MSB represents the first pixel, otherwise MSB represents the last pixel.

**Definition** display.h:82

[PIXEL\_FORMAT\_L\_8](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca14f33dfec4a630f5be50622a535434df)

@ PIXEL\_FORMAT\_L\_8

8-bit Grayscale/Luminance, equivalent to

**Definition** display.h:49

[PIXEL\_FORMAT\_MONO10](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c)

@ PIXEL\_FORMAT\_MONO10

Monochrome (1=Black 0=White).

**Definition** display.h:45

[PIXEL\_FORMAT\_ARGB\_8888](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9)

@ PIXEL\_FORMAT\_ARGB\_8888

32-bit ARGB

**Definition** display.h:46

[PIXEL\_FORMAT\_MONO01](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c)

@ PIXEL\_FORMAT\_MONO01

Monochrome (0=Black 1=White).

**Definition** display.h:44

[PIXEL\_FORMAT\_RGB\_565](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16)

@ PIXEL\_FORMAT\_RGB\_565

16-bit RGB

**Definition** display.h:47

[PIXEL\_FORMAT\_RGB\_888](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a)

@ PIXEL\_FORMAT\_RGB\_888

24-bit RGB

**Definition** display.h:43

[PIXEL\_FORMAT\_BGR\_565](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cae9fdd617aaf49148d4c4cb5d47189289)

@ PIXEL\_FORMAT\_BGR\_565

16-bit BGR

**Definition** display.h:48

[DISPLAY\_ORIENTATION\_ROTATED\_90](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc)

@ DISPLAY\_ORIENTATION\_ROTATED\_90

Rotated 90 degrees clockwise.

**Definition** display.h:102

[DISPLAY\_ORIENTATION\_ROTATED\_180](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29)

@ DISPLAY\_ORIENTATION\_ROTATED\_180

Rotated 180 degrees clockwise.

**Definition** display.h:103

[DISPLAY\_ORIENTATION\_NORMAL](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2)

@ DISPLAY\_ORIENTATION\_NORMAL

No rotation.

**Definition** display.h:101

[DISPLAY\_ORIENTATION\_ROTATED\_270](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4)

@ DISPLAY\_ORIENTATION\_ROTATED\_270

Rotated 270 degrees clockwise.

**Definition** display.h:104

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

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

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[display\_buffer\_descriptor](structdisplay__buffer__descriptor.md)

Structure to describe display data buffer layout.

**Definition** display.h:124

[display\_buffer\_descriptor::pitch](structdisplay__buffer__descriptor.md#a00d7d8da4e61f404ad353b9a8f49b2eb)

uint16\_t pitch

Number of pixels between consecutive rows in the data buffer.

**Definition** display.h:132

[display\_buffer\_descriptor::frame\_incomplete](structdisplay__buffer__descriptor.md#a29e49359561cc0c601196eb9cf1f93b7)

bool frame\_incomplete

Indicates that this is not the last write buffer of the frame.

**Definition** display.h:134

[display\_buffer\_descriptor::height](structdisplay__buffer__descriptor.md#a572c6560903553b6853360fd29631b95)

uint16\_t height

Data buffer column height in pixels.

**Definition** display.h:130

[display\_buffer\_descriptor::width](structdisplay__buffer__descriptor.md#aa35cf372266199308211d28dae789be3)

uint16\_t width

Data buffer row width in pixels.

**Definition** display.h:128

[display\_buffer\_descriptor::buf\_size](structdisplay__buffer__descriptor.md#aee9f34a6944b8e28622ab06d6907d40a)

uint32\_t buf\_size

Data buffer size in bytes.

**Definition** display.h:126

[display\_capabilities](structdisplay__capabilities.md)

Structure holding display capabilities.

**Definition** display.h:108

[display\_capabilities::supported\_pixel\_formats](structdisplay__capabilities.md#a07548bdd9671dd696b38a5bcf1599412)

uint32\_t supported\_pixel\_formats

Bitwise or of pixel formats supported by the display.

**Definition** display.h:114

[display\_capabilities::x\_resolution](structdisplay__capabilities.md#a09fa14e2c53126d5602cb7b51e21145f)

uint16\_t x\_resolution

Display resolution in the X direction.

**Definition** display.h:110

[display\_capabilities::current\_orientation](structdisplay__capabilities.md#a18986f5d2c385766d5ad3d68edd85887)

enum display\_orientation current\_orientation

Current display orientation.

**Definition** display.h:120

[display\_capabilities::y\_resolution](structdisplay__capabilities.md#a2cacb194139aaff90fd56b469f6de4a9)

uint16\_t y\_resolution

Display resolution in the Y direction.

**Definition** display.h:112

[display\_capabilities::screen\_info](structdisplay__capabilities.md#ac4a9098db4c2f721fa550c6142f541a9)

uint32\_t screen\_info

Information about display panel.

**Definition** display.h:116

[display\_capabilities::current\_pixel\_format](structdisplay__capabilities.md#aed51c9efdc76972fecfa8a733c2a8d0c)

enum display\_pixel\_format current\_pixel\_format

Currently active pixel format for the display.

**Definition** display.h:118

[display\_driver\_api](structdisplay__driver__api.md)

Display driver API API which a display driver should expose.

**Definition** display.h:232

[display\_driver\_api::blanking\_off](structdisplay__driver__api.md#a128c1324f4bfab707adc93aaff0f3371)

display\_blanking\_off\_api blanking\_off

**Definition** display.h:234

[display\_driver\_api::set\_pixel\_format](structdisplay__driver__api.md#a28801ba7578b9ab725c62b5f0d9f2c65)

display\_set\_pixel\_format\_api set\_pixel\_format

**Definition** display.h:242

[display\_driver\_api::read](structdisplay__driver__api.md#a431f765057a70e5d11ceaf93e8cc119a)

display\_read\_api read

**Definition** display.h:236

[display\_driver\_api::set\_orientation](structdisplay__driver__api.md#a4cbccfaafeb2f24c473bd967b9bc5f14)

display\_set\_orientation\_api set\_orientation

**Definition** display.h:243

[display\_driver\_api::write](structdisplay__driver__api.md#a535221c00caef6f24dc75c919826a889)

display\_write\_api write

**Definition** display.h:235

[display\_driver\_api::clear](structdisplay__driver__api.md#a913e21f2f3cdf6c20d0b3d00ec698b12)

display\_clear\_api clear

**Definition** display.h:237

[display\_driver\_api::set\_brightness](structdisplay__driver__api.md#aa40c04701b60f56c8998da55c2b254a8)

display\_set\_brightness\_api set\_brightness

**Definition** display.h:239

[display\_driver\_api::get\_framebuffer](structdisplay__driver__api.md#aa7843031d91003dc458be4146503b7f0)

display\_get\_framebuffer\_api get\_framebuffer

**Definition** display.h:238

[display\_driver\_api::blanking\_on](structdisplay__driver__api.md#aafdd79a11b46d4fa9288ddf3ed994c18)

display\_blanking\_on\_api blanking\_on

**Definition** display.h:233

[display\_driver\_api::get\_capabilities](structdisplay__driver__api.md#ace3a2eae73f639da890b6798bd215b29)

display\_get\_capabilities\_api get\_capabilities

**Definition** display.h:241

[display\_driver\_api::set\_contrast](structdisplay__driver__api.md#acfdf1662c0b362d5a35a137c903a40ba)

display\_set\_contrast\_api set\_contrast

**Definition** display.h:240

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [display.h](drivers_2display_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
