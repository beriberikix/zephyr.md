---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/has_8h_source.html
original_path: doxygen/html/has_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

has.h

[Go to the documentation of this file.](has_8h.md)

1

5

6/\*

7 \* Copyright (c) 2022 Codecoup

8 \* Copyright (c) 2024 Nordic Semiconductor ASA

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_HAS\_H\_

14#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_HAS\_H\_

15

30

31#include <[stdint.h](stdint_8h.md)>

32#include <[stdbool.h](stdbool_8h.md)>

33

34#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

35#include <[zephyr/sys/util.h](sys_2util_8h.md)>

36#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

37

38#ifdef \_\_cplusplus

39extern "C" {

40#endif

41

[ 47](group__bt__has.md#ga462679b8b5c91762c6d1daf03c5675d0)#define BT\_HAS\_PRESET\_INDEX\_NONE 0x00

[ 49](group__bt__has.md#ga38df8301e78111dc1e6241594a9bf8c3)#define BT\_HAS\_PRESET\_INDEX\_FIRST 0x01

[ 51](group__bt__has.md#ga2e1b80739eeb56d8e0b7779c3d488faa)#define BT\_HAS\_PRESET\_INDEX\_LAST 0xFF

53

[ 55](group__bt__has.md#gacbc29958c09b26a81e02893cd5914074)#define BT\_HAS\_PRESET\_NAME\_MIN 1

[ 57](group__bt__has.md#gae133807f12d0d7a1ecd1f8dda24c7f09)#define BT\_HAS\_PRESET\_NAME\_MAX 40

58

60struct bt\_has;

61

[ 63](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540)enum [bt\_has\_hearing\_aid\_type](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540) {

[ 68](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c) [BT\_HAS\_HEARING\_AID\_TYPE\_BINAURAL](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c) = 0x00,

[ 73](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8) [BT\_HAS\_HEARING\_AID\_TYPE\_MONAURAL](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8) = 0x01,

[ 78](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b) [BT\_HAS\_HEARING\_AID\_TYPE\_BANDED](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b) = 0x02,

79};

80

[ 82](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274)enum [bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) {

[ 84](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173) [BT\_HAS\_PROP\_NONE](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173) = 0,

85

[ 87](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09) [BT\_HAS\_PROP\_WRITABLE](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

88

[ 90](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59) [BT\_HAS\_PROP\_AVAILABLE](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

91};

92

[ 94](group__bt__has.md#ga50d470390967317cb84b17fd450546a4)enum [bt\_has\_capabilities](group__bt__has.md#ga50d470390967317cb84b17fd450546a4) {

[ 96](group__bt__has.md#gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258) [BT\_HAS\_PRESET\_SUPPORT](group__bt__has.md#gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

97};

98

[ 100](structbt__has__features__param.md)struct [bt\_has\_features\_param](structbt__has__features__param.md) {

[ 102](structbt__has__features__param.md#abcaf8630309bcae1a8184095c1eca656) enum [bt\_has\_hearing\_aid\_type](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540) [type](structbt__has__features__param.md#abcaf8630309bcae1a8184095c1eca656);

103

[ 110](structbt__has__features__param.md#ada946ee62547349bc01054db5cafa279) bool [preset\_sync\_support](structbt__has__features__param.md#ada946ee62547349bc01054db5cafa279);

111

[ 118](structbt__has__features__param.md#a5ff95f2633bf577fc0f4c3d714d53bb1) bool [independent\_presets](structbt__has__features__param.md#a5ff95f2633bf577fc0f4c3d714d53bb1);

119};

120

[ 122](structbt__has__preset__record.md)struct [bt\_has\_preset\_record](structbt__has__preset__record.md) {

[ 124](structbt__has__preset__record.md#a68484827708a19a75f2cdf922f01e677) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [index](structbt__has__preset__record.md#a68484827708a19a75f2cdf922f01e677);

125

[ 127](structbt__has__preset__record.md#ad3fc652d24a8b625b97abb02f0fb66bb) enum [bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) [properties](structbt__has__preset__record.md#ad3fc652d24a8b625b97abb02f0fb66bb);

128

[ 130](structbt__has__preset__record.md#ac064f0ae2841627930fb3ca0370ef5ec) const char \*[name](structbt__has__preset__record.md#ac064f0ae2841627930fb3ca0370ef5ec);

131};

132

[ 134](structbt__has__client__cb.md)struct [bt\_has\_client\_cb](structbt__has__client__cb.md) {

[ 146](structbt__has__client__cb.md#acf35d62cce0c2181e2eefd8c43e3b568) void (\*[discover](structbt__has__client__cb.md#acf35d62cce0c2181e2eefd8c43e3b568))(struct bt\_conn \*conn, int err, struct bt\_has \*has,

147 enum [bt\_has\_hearing\_aid\_type](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540) type, enum [bt\_has\_capabilities](group__bt__has.md#ga50d470390967317cb84b17fd450546a4) caps);

148

[ 162](structbt__has__client__cb.md#a4217754818ad047f287aceda8326bf99) void (\*[preset\_switch](structbt__has__client__cb.md#a4217754818ad047f287aceda8326bf99))(struct bt\_has \*has, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index);

163

[ 176](structbt__has__client__cb.md#a50759c76add5f4f76e23e742ae3ebe1b) void (\*[preset\_read\_rsp](structbt__has__client__cb.md#a50759c76add5f4f76e23e742ae3ebe1b))(struct bt\_has \*has, int err,

177 const struct [bt\_has\_preset\_record](structbt__has__preset__record.md) \*record, bool is\_last);

178

[ 191](structbt__has__client__cb.md#aa54cf5f268e542947ffb30531b7702ba) void (\*[preset\_update](structbt__has__client__cb.md#aa54cf5f268e542947ffb30531b7702ba))(struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index\_prev,

192 const struct [bt\_has\_preset\_record](structbt__has__preset__record.md) \*record, bool is\_last);

193

[ 203](structbt__has__client__cb.md#a1c28e7b5542100ce93727ac097cc6dee) void (\*[preset\_deleted](structbt__has__client__cb.md#a1c28e7b5542100ce93727ac097cc6dee))(struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, bool is\_last);

204

[ 216](structbt__has__client__cb.md#a903397650915f3335dd2b8cd4f51d293) void (\*[preset\_availability](structbt__has__client__cb.md#a903397650915f3335dd2b8cd4f51d293))(struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, bool available,

217 bool is\_last);

218};

219

[ 227](group__bt__has.md#ga9bc61dfc710070fb136120944c0776b9)int [bt\_has\_client\_cb\_register](group__bt__has.md#ga9bc61dfc710070fb136120944c0776b9)(const struct [bt\_has\_client\_cb](structbt__has__client__cb.md) \*cb);

228

[ 240](group__bt__has.md#gaf3765300072b0a6d1ee45699e710d4da)int [bt\_has\_client\_discover](group__bt__has.md#gaf3765300072b0a6d1ee45699e710d4da)(struct bt\_conn \*conn);

241

[ 253](group__bt__has.md#ga8303b5fb2558a35bb2cb06cd5788e636)int [bt\_has\_client\_conn\_get](group__bt__has.md#ga8303b5fb2558a35bb2cb06cd5788e636)(const struct bt\_has \*has, struct bt\_conn \*\*conn);

254

[ 268](group__bt__has.md#ga54ef9918e4fb458b7416ffb94acca808)int [bt\_has\_client\_presets\_read](group__bt__has.md#ga54ef9918e4fb458b7416ffb94acca808)(struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_count);

269

[ 282](group__bt__has.md#ga4a228ee29a26346867a6427f81816336)int [bt\_has\_client\_preset\_set](group__bt__has.md#ga4a228ee29a26346867a6427f81816336)(struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, bool sync);

283

[ 295](group__bt__has.md#ga66943cb5275ca660f2eab11e37708d81)int [bt\_has\_client\_preset\_next](group__bt__has.md#ga66943cb5275ca660f2eab11e37708d81)(struct bt\_has \*has, bool sync);

296

[ 308](group__bt__has.md#ga3a564b18ce6cbc7a5af970474ddf25a2)int [bt\_has\_client\_preset\_prev](group__bt__has.md#ga3a564b18ce6cbc7a5af970474ddf25a2)(struct bt\_has \*has, bool sync);

309

[ 311](structbt__has__preset__ops.md)struct [bt\_has\_preset\_ops](structbt__has__preset__ops.md) {

[ 327](structbt__has__preset__ops.md#aec9d0f01c03f02f0a6f124527b72235e) int (\*[select](structbt__has__preset__ops.md#aec9d0f01c03f02f0a6f124527b72235e))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, bool sync);

328

[ 337](structbt__has__preset__ops.md#a7f0069639eb3b1f8b0d290a752b68770) void (\*[name\_changed](structbt__has__preset__ops.md#a7f0069639eb3b1f8b0d290a752b68770))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, const char \*name);

338};

339

[ 341](structbt__has__preset__register__param.md)struct [bt\_has\_preset\_register\_param](structbt__has__preset__register__param.md) {

[ 347](structbt__has__preset__register__param.md#a9a3ade943b4f7569577c092df3ec467c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [index](structbt__has__preset__register__param.md#a9a3ade943b4f7569577c092df3ec467c);

348

[ 354](structbt__has__preset__register__param.md#a8273bbec14040a7dd67aeac14188b86b) enum [bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) [properties](structbt__has__preset__register__param.md#a8273bbec14040a7dd67aeac14188b86b);

355

[ 364](structbt__has__preset__register__param.md#a35b8d2e9a01198cc34350595c786f1ae) const char \*[name](structbt__has__preset__register__param.md#a35b8d2e9a01198cc34350595c786f1ae);

365

[ 367](structbt__has__preset__register__param.md#a6e480fb6337d363353ca7ba6f716cd71) const struct [bt\_has\_preset\_ops](structbt__has__preset__ops.md) \*[ops](structbt__has__preset__register__param.md#a6e480fb6337d363353ca7ba6f716cd71);

368};

369

[ 377](group__bt__has.md#gac39ca2d72273bd591618d186b48c20b0)int [bt\_has\_register](group__bt__has.md#gac39ca2d72273bd591618d186b48c20b0)(const struct [bt\_has\_features\_param](structbt__has__features__param.md) \*features);

378

[ 389](group__bt__has.md#gadf0a488721910633fa2b54b2c7645bd9)int [bt\_has\_preset\_register](group__bt__has.md#gadf0a488721910633fa2b54b2c7645bd9)(const struct [bt\_has\_preset\_register\_param](structbt__has__preset__register__param.md) \*param);

390

[ 400](group__bt__has.md#ga39f9ac2f94b1febe8e834ae54e110e90)int [bt\_has\_preset\_unregister](group__bt__has.md#ga39f9ac2f94b1febe8e834ae54e110e90)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index);

401

[ 412](group__bt__has.md#gacaa997913949b6ea98c5c6233fefdc52)int [bt\_has\_preset\_available](group__bt__has.md#gacaa997913949b6ea98c5c6233fefdc52)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index);

413

[ 424](group__bt__has.md#gabe523e1aefc789ad0031e3c0efb27379)int [bt\_has\_preset\_unavailable](group__bt__has.md#gabe523e1aefc789ad0031e3c0efb27379)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index);

425

427enum {

[ 429](group__bt__has.md#ggaeb9b1dcf3e33fac6c44aa952c478f917af9ea42147bbce222b024fb922c52daaa) [BT\_HAS\_PRESET\_ITER\_STOP](group__bt__has.md#ggaeb9b1dcf3e33fac6c44aa952c478f917af9ea42147bbce222b024fb922c52daaa) = 0,

[ 431](group__bt__has.md#ggaeb9b1dcf3e33fac6c44aa952c478f917a5acb1c7f3113a21e19e4a37fd8e099bf) [BT\_HAS\_PRESET\_ITER\_CONTINUE](group__bt__has.md#ggaeb9b1dcf3e33fac6c44aa952c478f917a5acb1c7f3113a21e19e4a37fd8e099bf),

432};

433

[ 446](group__bt__has.md#ga4b8e97b1aeed16ac8356953ca4008ec6)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_has\_preset\_func\_t](group__bt__has.md#ga4b8e97b1aeed16ac8356953ca4008ec6))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, enum [bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) properties,

447 const char \*name, void \*user\_data);

448

[ 458](group__bt__has.md#ga8e366c90dc240acc6d4b40d087154eba)void [bt\_has\_preset\_foreach](group__bt__has.md#ga8e366c90dc240acc6d4b40d087154eba)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bt\_has\_preset\_func\_t](group__bt__has.md#ga4b8e97b1aeed16ac8356953ca4008ec6) func, void \*user\_data);

459

[ 470](group__bt__has.md#ga2c0fe62baa63b72703d6f553f1de072b)int [bt\_has\_preset\_active\_set](group__bt__has.md#ga2c0fe62baa63b72703d6f553f1de072b)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index);

471

[ 479](group__bt__has.md#gae1787671fac3b7873c5994adc7d19b20)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_has\_preset\_active\_get](group__bt__has.md#gae1787671fac3b7873c5994adc7d19b20)(void);

480

[ 488](group__bt__has.md#ga715cfe5bd08fbd4557ee6052b38f27de)static inline int [bt\_has\_preset\_active\_clear](group__bt__has.md#ga715cfe5bd08fbd4557ee6052b38f27de)(void)

489{

490 return [bt\_has\_preset\_active\_set](group__bt__has.md#ga2c0fe62baa63b72703d6f553f1de072b)([BT\_HAS\_PRESET\_INDEX\_NONE](group__bt__has.md#ga462679b8b5c91762c6d1daf03c5675d0));

491}

492

[ 503](group__bt__has.md#ga6f06adc529a500fcfcfea2ae89ea60d5)int [bt\_has\_preset\_name\_change](group__bt__has.md#ga6f06adc529a500fcfcfea2ae89ea60d5)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, const char \*name);

504

[ 514](group__bt__has.md#ga7e37a89b1bf0a732045276cf6b922956)int [bt\_has\_features\_set](group__bt__has.md#ga7e37a89b1bf0a732045276cf6b922956)(const struct [bt\_has\_features\_param](structbt__has__features__param.md) \*features);

515

516#ifdef \_\_cplusplus

517}

518#endif

519

523

524#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_HAS\_H\_ \*/

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[bt\_has\_preset\_active\_set](group__bt__has.md#ga2c0fe62baa63b72703d6f553f1de072b)

int bt\_has\_preset\_active\_set(uint8\_t index)

Set active preset.

[bt\_has\_preset\_unregister](group__bt__has.md#ga39f9ac2f94b1febe8e834ae54e110e90)

int bt\_has\_preset\_unregister(uint8\_t index)

Unregister Preset.

[bt\_has\_client\_preset\_prev](group__bt__has.md#ga3a564b18ce6cbc7a5af970474ddf25a2)

int bt\_has\_client\_preset\_prev(struct bt\_has \*has, bool sync)

Activate Previous Preset.

[BT\_HAS\_PRESET\_INDEX\_NONE](group__bt__has.md#ga462679b8b5c91762c6d1daf03c5675d0)

#define BT\_HAS\_PRESET\_INDEX\_NONE

No index.

**Definition** has.h:47

[bt\_has\_client\_preset\_set](group__bt__has.md#ga4a228ee29a26346867a6427f81816336)

int bt\_has\_client\_preset\_set(struct bt\_has \*has, uint8\_t index, bool sync)

Set Active Preset.

[bt\_has\_preset\_func\_t](group__bt__has.md#ga4b8e97b1aeed16ac8356953ca4008ec6)

uint8\_t(\* bt\_has\_preset\_func\_t)(uint8\_t index, enum bt\_has\_properties properties, const char \*name, void \*user\_data)

Preset iterator callback.

**Definition** has.h:446

[bt\_has\_capabilities](group__bt__has.md#ga50d470390967317cb84b17fd450546a4)

bt\_has\_capabilities

Hearing Aid device capabilities.

**Definition** has.h:94

[bt\_has\_client\_presets\_read](group__bt__has.md#ga54ef9918e4fb458b7416ffb94acca808)

int bt\_has\_client\_presets\_read(struct bt\_has \*has, uint8\_t index, uint8\_t max\_count)

Read Preset Records.

[bt\_has\_client\_preset\_next](group__bt__has.md#ga66943cb5275ca660f2eab11e37708d81)

int bt\_has\_client\_preset\_next(struct bt\_has \*has, bool sync)

Activate Next Preset.

[bt\_has\_preset\_name\_change](group__bt__has.md#ga6f06adc529a500fcfcfea2ae89ea60d5)

int bt\_has\_preset\_name\_change(uint8\_t index, const char \*name)

Change the Preset Name.

[bt\_has\_preset\_active\_clear](group__bt__has.md#ga715cfe5bd08fbd4557ee6052b38f27de)

static int bt\_has\_preset\_active\_clear(void)

Clear out active preset.

**Definition** has.h:488

[bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274)

bt\_has\_properties

Preset Properties values.

**Definition** has.h:82

[bt\_has\_features\_set](group__bt__has.md#ga7e37a89b1bf0a732045276cf6b922956)

int bt\_has\_features\_set(const struct bt\_has\_features\_param \*features)

Change the Hearing Aid Features.

[bt\_has\_client\_conn\_get](group__bt__has.md#ga8303b5fb2558a35bb2cb06cd5788e636)

int bt\_has\_client\_conn\_get(const struct bt\_has \*has, struct bt\_conn \*\*conn)

Get the Bluetooth connection object of the service object.

[bt\_has\_preset\_foreach](group__bt__has.md#ga8e366c90dc240acc6d4b40d087154eba)

void bt\_has\_preset\_foreach(uint8\_t index, bt\_has\_preset\_func\_t func, void \*user\_data)

Preset iterator.

[bt\_has\_client\_cb\_register](group__bt__has.md#ga9bc61dfc710070fb136120944c0776b9)

int bt\_has\_client\_cb\_register(const struct bt\_has\_client\_cb \*cb)

Registers the callbacks used by the Hearing Access Service client.

[bt\_has\_hearing\_aid\_type](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540)

bt\_has\_hearing\_aid\_type

Hearing Aid device type.

**Definition** has.h:63

[bt\_has\_preset\_unavailable](group__bt__has.md#gabe523e1aefc789ad0031e3c0efb27379)

int bt\_has\_preset\_unavailable(uint8\_t index)

Set the preset as unavailable.

[bt\_has\_register](group__bt__has.md#gac39ca2d72273bd591618d186b48c20b0)

int bt\_has\_register(const struct bt\_has\_features\_param \*features)

Register the Hearing Access Service instance.

[bt\_has\_preset\_available](group__bt__has.md#gacaa997913949b6ea98c5c6233fefdc52)

int bt\_has\_preset\_available(uint8\_t index)

Set the preset as available.

[bt\_has\_preset\_register](group__bt__has.md#gadf0a488721910633fa2b54b2c7645bd9)

int bt\_has\_preset\_register(const struct bt\_has\_preset\_register\_param \*param)

Register preset.

[bt\_has\_preset\_active\_get](group__bt__has.md#gae1787671fac3b7873c5994adc7d19b20)

uint8\_t bt\_has\_preset\_active\_get(void)

Get active preset.

[bt\_has\_client\_discover](group__bt__has.md#gaf3765300072b0a6d1ee45699e710d4da)

int bt\_has\_client\_discover(struct bt\_conn \*conn)

Discover Hearing Access Service on a remote device.

[BT\_HAS\_PRESET\_SUPPORT](group__bt__has.md#gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258)

@ BT\_HAS\_PRESET\_SUPPORT

Indicate support for presets.

**Definition** has.h:96

[BT\_HAS\_PROP\_NONE](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173)

@ BT\_HAS\_PROP\_NONE

No properties set.

**Definition** has.h:84

[BT\_HAS\_PROP\_AVAILABLE](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59)

@ BT\_HAS\_PROP\_AVAILABLE

Preset availability.

**Definition** has.h:90

[BT\_HAS\_PROP\_WRITABLE](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09)

@ BT\_HAS\_PROP\_WRITABLE

Preset name can be written by the client.

**Definition** has.h:87

[BT\_HAS\_HEARING\_AID\_TYPE\_MONAURAL](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8)

@ BT\_HAS\_HEARING\_AID\_TYPE\_MONAURAL

A single hearing aid for the left or the right ear.

**Definition** has.h:73

[BT\_HAS\_HEARING\_AID\_TYPE\_BINAURAL](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c)

@ BT\_HAS\_HEARING\_AID\_TYPE\_BINAURAL

Two hearing aids that form a Coordinated Set, one for the right ear and one for the left ear of the u...

**Definition** has.h:68

[BT\_HAS\_HEARING\_AID\_TYPE\_BANDED](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b)

@ BT\_HAS\_HEARING\_AID\_TYPE\_BANDED

Two hearing aids with a connection to one another that expose a single Bluetooth radio interface.

**Definition** has.h:78

[BT\_HAS\_PRESET\_ITER\_CONTINUE](group__bt__has.md#ggaeb9b1dcf3e33fac6c44aa952c478f917a5acb1c7f3113a21e19e4a37fd8e099bf)

@ BT\_HAS\_PRESET\_ITER\_CONTINUE

Continue iterating.

**Definition** has.h:431

[BT\_HAS\_PRESET\_ITER\_STOP](group__bt__has.md#ggaeb9b1dcf3e33fac6c44aa952c478f917af9ea42147bbce222b024fb922c52daaa)

@ BT\_HAS\_PRESET\_ITER\_STOP

Stop iterating.

**Definition** has.h:429

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_has\_client\_cb](structbt__has__client__cb.md)

Hearing Access Service Client callback structure.

**Definition** has.h:134

[bt\_has\_client\_cb::preset\_deleted](structbt__has__client__cb.md#a1c28e7b5542100ce93727ac097cc6dee)

void(\* preset\_deleted)(struct bt\_has \*has, uint8\_t index, bool is\_last)

Callback function for preset deletion notifications.

**Definition** has.h:203

[bt\_has\_client\_cb::preset\_switch](structbt__has__client__cb.md#a4217754818ad047f287aceda8326bf99)

void(\* preset\_switch)(struct bt\_has \*has, int err, uint8\_t index)

Callback function for Hearing Access Service active preset changes.

**Definition** has.h:162

[bt\_has\_client\_cb::preset\_read\_rsp](structbt__has__client__cb.md#a50759c76add5f4f76e23e742ae3ebe1b)

void(\* preset\_read\_rsp)(struct bt\_has \*has, int err, const struct bt\_has\_preset\_record \*record, bool is\_last)

Callback function for presets read operation.

**Definition** has.h:176

[bt\_has\_client\_cb::preset\_availability](structbt__has__client__cb.md#a903397650915f3335dd2b8cd4f51d293)

void(\* preset\_availability)(struct bt\_has \*has, uint8\_t index, bool available, bool is\_last)

Callback function for preset availability notifications.

**Definition** has.h:216

[bt\_has\_client\_cb::preset\_update](structbt__has__client__cb.md#aa54cf5f268e542947ffb30531b7702ba)

void(\* preset\_update)(struct bt\_has \*has, uint8\_t index\_prev, const struct bt\_has\_preset\_record \*record, bool is\_last)

Callback function for preset update notifications.

**Definition** has.h:191

[bt\_has\_client\_cb::discover](structbt__has__client__cb.md#acf35d62cce0c2181e2eefd8c43e3b568)

void(\* discover)(struct bt\_conn \*conn, int err, struct bt\_has \*has, enum bt\_has\_hearing\_aid\_type type, enum bt\_has\_capabilities caps)

Callback function for bt\_has\_discover.

**Definition** has.h:146

[bt\_has\_features\_param](structbt__has__features__param.md)

Structure for registering features of a Hearing Access Service instance.

**Definition** has.h:100

[bt\_has\_features\_param::independent\_presets](structbt__has__features__param.md#a5ff95f2633bf577fc0f4c3d714d53bb1)

bool independent\_presets

Independent Presets.

**Definition** has.h:118

[bt\_has\_features\_param::type](structbt__has__features__param.md#abcaf8630309bcae1a8184095c1eca656)

enum bt\_has\_hearing\_aid\_type type

Hearing Aid Type value.

**Definition** has.h:102

[bt\_has\_features\_param::preset\_sync\_support](structbt__has__features__param.md#ada946ee62547349bc01054db5cafa279)

bool preset\_sync\_support

Preset Synchronization Support.

**Definition** has.h:110

[bt\_has\_preset\_ops](structbt__has__preset__ops.md)

Preset operations structure.

**Definition** has.h:311

[bt\_has\_preset\_ops::name\_changed](structbt__has__preset__ops.md#a7f0069639eb3b1f8b0d290a752b68770)

void(\* name\_changed)(uint8\_t index, const char \*name)

Preset name changed callback.

**Definition** has.h:337

[bt\_has\_preset\_ops::select](structbt__has__preset__ops.md#aec9d0f01c03f02f0a6f124527b72235e)

int(\* select)(uint8\_t index, bool sync)

Preset select callback.

**Definition** has.h:327

[bt\_has\_preset\_record](structbt__has__preset__record.md)

Preset record definition.

**Definition** has.h:122

[bt\_has\_preset\_record::index](structbt__has__preset__record.md#a68484827708a19a75f2cdf922f01e677)

uint8\_t index

Unique preset index.

**Definition** has.h:124

[bt\_has\_preset\_record::name](structbt__has__preset__record.md#ac064f0ae2841627930fb3ca0370ef5ec)

const char \* name

Preset name.

**Definition** has.h:130

[bt\_has\_preset\_record::properties](structbt__has__preset__record.md#ad3fc652d24a8b625b97abb02f0fb66bb)

enum bt\_has\_properties properties

Bitfield of preset properties.

**Definition** has.h:127

[bt\_has\_preset\_register\_param](structbt__has__preset__register__param.md)

Register structure for preset.

**Definition** has.h:341

[bt\_has\_preset\_register\_param::name](structbt__has__preset__register__param.md#a35b8d2e9a01198cc34350595c786f1ae)

const char \* name

Preset name.

**Definition** has.h:364

[bt\_has\_preset\_register\_param::ops](structbt__has__preset__register__param.md#a6e480fb6337d363353ca7ba6f716cd71)

const struct bt\_has\_preset\_ops \* ops

Preset operations structure.

**Definition** has.h:367

[bt\_has\_preset\_register\_param::properties](structbt__has__preset__register__param.md#a8273bbec14040a7dd67aeac14188b86b)

enum bt\_has\_properties properties

Preset properties.

**Definition** has.h:354

[bt\_has\_preset\_register\_param::index](structbt__has__preset__register__param.md#a9a3ade943b4f7569577c092df3ec467c)

uint8\_t index

Preset index.

**Definition** has.h:347

[util.h](sys_2util_8h.md)

Misc utilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [has.h](has_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
