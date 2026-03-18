---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/aics_8h_source.html
original_path: doxygen/html/aics_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

aics.h

[Go to the documentation of this file.](aics_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_AICS\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_AICS\_H\_

9

28

29#include <[zephyr/bluetooth/bluetooth.h](bluetooth_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

[ 36](group__bt__gatt__aics.md#ga47436e2df23067ce86dc761d77ed14b7)#define BT\_AICS\_STATE\_UNMUTED 0x00

[ 37](group__bt__gatt__aics.md#ga1572eaaffea5412b496eb714d64aa981)#define BT\_AICS\_STATE\_MUTED 0x01

[ 38](group__bt__gatt__aics.md#gad0063d0e0b622b4093607e5485897214)#define BT\_AICS\_STATE\_MUTE\_DISABLED 0x02

39

[ 41](group__bt__gatt__aics.md#gaecb9365a5e390111311d1b415a2cee79)#define BT\_AICS\_MODE\_MANUAL\_ONLY 0x00

[ 42](group__bt__gatt__aics.md#ga6b536bdcab602ccaccfafe3b37258890)#define BT\_AICS\_MODE\_AUTO\_ONLY 0x01

[ 43](group__bt__gatt__aics.md#ga7cf0508dd7407ec3bb92dec71cc00816)#define BT\_AICS\_MODE\_MANUAL 0x02

[ 44](group__bt__gatt__aics.md#ga0ac3a583dd7ca58a0d356d9f60797517)#define BT\_AICS\_MODE\_AUTO 0x03

45

[ 47](group__bt__gatt__aics.md#ga2204f35b5f1aa41c27f62b8f0dcf74b6)#define BT\_AICS\_INPUT\_TYPE\_UNSPECIFIED 0x00

[ 48](group__bt__gatt__aics.md#gac8ebf643f9a4101ea8da18827577bf5d)#define BT\_AICS\_INPUT\_TYPE\_BLUETOOTH 0x01

[ 49](group__bt__gatt__aics.md#ga7fcb5aefacb641a8ef7db4e9a554a65d)#define BT\_AICS\_INPUT\_TYPE\_MICROPHONE 0x02

[ 50](group__bt__gatt__aics.md#ga525b361d1d555f20d292cf1aded0d046)#define BT\_AICS\_INPUT\_TYPE\_ANALOG 0x03

[ 51](group__bt__gatt__aics.md#ga688605eb9eb5b27ca62fac9b85fde472)#define BT\_AICS\_INPUT\_TYPE\_DIGITAL 0x04

[ 52](group__bt__gatt__aics.md#ga3b878b41ab30067bceefc0cd72340376)#define BT\_AICS\_INPUT\_TYPE\_RADIO 0x05

[ 53](group__bt__gatt__aics.md#ga43a02e2025e3cb3e10bc2ee2128ee877)#define BT\_AICS\_INPUT\_TYPE\_STREAMING 0x06

54

[ 56](group__bt__gatt__aics.md#gae54199f78ff7d7380353f3950bd03a39)#define BT\_AICS\_ERR\_INVALID\_COUNTER 0x80

[ 57](group__bt__gatt__aics.md#ga00c0942dab2bf25c680278927aa49af8)#define BT\_AICS\_ERR\_OP\_NOT\_SUPPORTED 0x81

[ 58](group__bt__gatt__aics.md#ga1efb1f6a4c24c2a20fc7136928abac6b)#define BT\_AICS\_ERR\_MUTE\_DISABLED 0x82

[ 59](group__bt__gatt__aics.md#ga2f3806b8056ea8ed43b2a7cd52ffa4f3)#define BT\_AICS\_ERR\_OUT\_OF\_RANGE 0x83

[ 60](group__bt__gatt__aics.md#ga6673570f7679322bfa4719bf6e41e299)#define BT\_AICS\_ERR\_GAIN\_MODE\_NOT\_ALLOWED 0x84

61

63struct bt\_aics;

64

[ 66](structbt__aics__register__param.md)struct [bt\_aics\_register\_param](structbt__aics__register__param.md) {

[ 68](structbt__aics__register__param.md#a966e9e99544392cdfac264ee6effcc7c) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [gain](structbt__aics__register__param.md#a966e9e99544392cdfac264ee6effcc7c);

69

[ 71](structbt__aics__register__param.md#ac95e17bc53539deeab5d161ca1b08194) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mute](structbt__aics__register__param.md#ac95e17bc53539deeab5d161ca1b08194);

72

[ 74](structbt__aics__register__param.md#a3658ed1900a44eef84b5602e567fe085) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gain\_mode](structbt__aics__register__param.md#a3658ed1900a44eef84b5602e567fe085);

75

[ 77](structbt__aics__register__param.md#a4b2eae9a9716629e9c56ee3e6dc05e44) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [units](structbt__aics__register__param.md#a4b2eae9a9716629e9c56ee3e6dc05e44);

78

[ 80](structbt__aics__register__param.md#aac91095a831fe540ee356eb9b9d402d8) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [min\_gain](structbt__aics__register__param.md#aac91095a831fe540ee356eb9b9d402d8);

81

[ 83](structbt__aics__register__param.md#aa139122e2710d9ec28ec015692545dda) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_gain](structbt__aics__register__param.md#aa139122e2710d9ec28ec015692545dda);

84

[ 86](structbt__aics__register__param.md#ad6afebea920fa4c168498ca11778ea7d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__aics__register__param.md#ad6afebea920fa4c168498ca11778ea7d);

87

[ 89](structbt__aics__register__param.md#a46437f4540d226ce3fbc470448f36e1f) bool [status](structbt__aics__register__param.md#a46437f4540d226ce3fbc470448f36e1f);

90

[ 92](structbt__aics__register__param.md#acc408a0318b94cdc952ef7d6682e5705) bool [desc\_writable](structbt__aics__register__param.md#acc408a0318b94cdc952ef7d6682e5705);

93

[ 95](structbt__aics__register__param.md#af99d31215008eb201c488a5b1107e009) char \*[description](structbt__aics__register__param.md#af99d31215008eb201c488a5b1107e009);

96

[ 98](structbt__aics__register__param.md#a6c961cde10dbfbaaa26bbc2b5c867001) struct [bt\_aics\_cb](structbt__aics__cb.md) \*[cb](structbt__aics__register__param.md#a6c961cde10dbfbaaa26bbc2b5c867001);

99};

100

[ 102](structbt__aics__discover__param.md)struct [bt\_aics\_discover\_param](structbt__aics__discover__param.md) {

[ 107](structbt__aics__discover__param.md#ab867f7d2ae219df0c479cce72d68842f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_handle](structbt__aics__discover__param.md#ab867f7d2ae219df0c479cce72d68842f);

[ 112](structbt__aics__discover__param.md#ab2931e7c4a627e717d943b2907b264cb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__aics__discover__param.md#ab2931e7c4a627e717d943b2907b264cb);

113};

114

[ 120](group__bt__gatt__aics.md#gab10ad3599f5b602cdf5504bc92508109)struct bt\_aics \*[bt\_aics\_free\_instance\_get](group__bt__gatt__aics.md#gab10ad3599f5b602cdf5504bc92508109)(void);

121

[ 131](group__bt__gatt__aics.md#ga8b415343e7ecf399ecfd0dcaa49bd1ee)void \*[bt\_aics\_svc\_decl\_get](group__bt__gatt__aics.md#ga8b415343e7ecf399ecfd0dcaa49bd1ee)(struct bt\_aics \*aics);

132

[ 144](group__bt__gatt__aics.md#ga0e088e26cf73f1f3b918660d4acdebb9)int [bt\_aics\_client\_conn\_get](group__bt__gatt__aics.md#ga0e088e26cf73f1f3b918660d4acdebb9)(const struct bt\_aics \*aics, struct bt\_conn \*\*conn);

145

[ 154](group__bt__gatt__aics.md#ga008ef5cebfcb9b4a3084f411fa81238e)int [bt\_aics\_register](group__bt__gatt__aics.md#ga008ef5cebfcb9b4a3084f411fa81238e)(struct bt\_aics \*aics, struct [bt\_aics\_register\_param](structbt__aics__register__param.md) \*param);

155

[ 163](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef)typedef void (\*[bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef))(struct bt\_aics \*inst, int err);

164

[ 179](group__bt__gatt__aics.md#ga2e851f49f9c7e71a18376468a13fdf4f)typedef void (\*[bt\_aics\_state\_cb](group__bt__gatt__aics.md#ga2e851f49f9c7e71a18376468a13fdf4f))(struct bt\_aics \*inst, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) gain,

180 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode);

181

[ 197](group__bt__gatt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb)typedef void (\*[bt\_aics\_gain\_setting\_cb](group__bt__gatt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb))(struct bt\_aics \*inst, int err,

198 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) units, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) minimum,

199 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) maximum);

200

[ 212](group__bt__gatt__aics.md#ga6e76b9f2de4cdbcd7539c76f6a347fa5)typedef void (\*[bt\_aics\_type\_cb](group__bt__gatt__aics.md#ga6e76b9f2de4cdbcd7539c76f6a347fa5))(struct bt\_aics \*inst, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type);

213

[ 225](group__bt__gatt__aics.md#ga044d92a4273c6537a9cdf20922352ed6)typedef void (\*[bt\_aics\_status\_cb](group__bt__gatt__aics.md#ga044d92a4273c6537a9cdf20922352ed6))(struct bt\_aics \*inst, int err, bool active);

226

[ 238](group__bt__gatt__aics.md#ga98b142ea7a66de5577c44aa90d507930)typedef void (\*[bt\_aics\_description\_cb](group__bt__gatt__aics.md#ga98b142ea7a66de5577c44aa90d507930))(struct bt\_aics \*inst, int err,

239 char \*description);

240

[ 252](group__bt__gatt__aics.md#ga9fda39f8410308e05eb928eeb7267e83)typedef void (\*[bt\_aics\_discover\_cb](group__bt__gatt__aics.md#ga9fda39f8410308e05eb928eeb7267e83))(struct bt\_aics \*inst, int err);

253

[ 254](structbt__aics__cb.md)struct [bt\_aics\_cb](structbt__aics__cb.md) {

[ 255](structbt__aics__cb.md#a70d099bec6407e5c92f6a4e8d6c44929) [bt\_aics\_state\_cb](group__bt__gatt__aics.md#ga2e851f49f9c7e71a18376468a13fdf4f) [state](structbt__aics__cb.md#a70d099bec6407e5c92f6a4e8d6c44929);

[ 256](structbt__aics__cb.md#a6b2f2a43d0a91abcecfe8372b6a1be4b) [bt\_aics\_gain\_setting\_cb](group__bt__gatt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb) [gain\_setting](structbt__aics__cb.md#a6b2f2a43d0a91abcecfe8372b6a1be4b);

[ 257](structbt__aics__cb.md#a41bc7a97e28c53772573d99a38e8ac55) [bt\_aics\_type\_cb](group__bt__gatt__aics.md#ga6e76b9f2de4cdbcd7539c76f6a347fa5) [type](structbt__aics__cb.md#a41bc7a97e28c53772573d99a38e8ac55);

[ 258](structbt__aics__cb.md#ac89882943c293e533bec55dd285d7aa0) [bt\_aics\_status\_cb](group__bt__gatt__aics.md#ga044d92a4273c6537a9cdf20922352ed6) [status](structbt__aics__cb.md#ac89882943c293e533bec55dd285d7aa0);

[ 259](structbt__aics__cb.md#ad37ae465600fa2e3c1868f0da07fd31a) [bt\_aics\_description\_cb](group__bt__gatt__aics.md#ga98b142ea7a66de5577c44aa90d507930) [description](structbt__aics__cb.md#ad37ae465600fa2e3c1868f0da07fd31a);

260

261#if defined(CONFIG\_BT\_AICS\_CLIENT)

262 [bt\_aics\_discover\_cb](group__bt__gatt__aics.md#ga9fda39f8410308e05eb928eeb7267e83) discover;

263 [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef) set\_gain;

264 [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef) unmute;

265 [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef) mute;

266 [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef) set\_manual\_mode;

267 [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef) set\_auto\_mode;

268#endif /\* CONFIG\_BT\_AICS\_CLIENT \*/

269};

270

271

[ 284](group__bt__gatt__aics.md#gad16d296462af2f61a893bda8d25cc9de)int [bt\_aics\_discover](group__bt__gatt__aics.md#gad16d296462af2f61a893bda8d25cc9de)(struct bt\_conn \*conn, struct bt\_aics \*inst,

285 const struct [bt\_aics\_discover\_param](structbt__aics__discover__param.md) \*param);

286

[ 297](group__bt__gatt__aics.md#ga4be4c4e3c74aa55fbf599157aa1c2098)int [bt\_aics\_deactivate](group__bt__gatt__aics.md#ga4be4c4e3c74aa55fbf599157aa1c2098)(struct bt\_aics \*inst);

298

[ 310](group__bt__gatt__aics.md#gac46268949fa7cbbb827d149a3a904daa)int [bt\_aics\_activate](group__bt__gatt__aics.md#gac46268949fa7cbbb827d149a3a904daa)(struct bt\_aics \*inst);

311

[ 319](group__bt__gatt__aics.md#ga23bbc1393d21fe38f501813935b25b3d)int [bt\_aics\_state\_get](group__bt__gatt__aics.md#ga23bbc1393d21fe38f501813935b25b3d)(struct bt\_aics \*inst);

320

[ 328](group__bt__gatt__aics.md#ga38d7131397d7762d3bd53e152a6c6130)int [bt\_aics\_gain\_setting\_get](group__bt__gatt__aics.md#ga38d7131397d7762d3bd53e152a6c6130)(struct bt\_aics \*inst);

329

[ 337](group__bt__gatt__aics.md#gaf57896e2096a5e96ec46a56cdf216159)int [bt\_aics\_type\_get](group__bt__gatt__aics.md#gaf57896e2096a5e96ec46a56cdf216159)(struct bt\_aics \*inst);

338

[ 346](group__bt__gatt__aics.md#gade387c52d201ce10b39ef52157dae83d)int [bt\_aics\_status\_get](group__bt__gatt__aics.md#gade387c52d201ce10b39ef52157dae83d)(struct bt\_aics \*inst);

347

[ 358](group__bt__gatt__aics.md#ga5a1ad98afe45da9ffbb7247671385d40)int [bt\_aics\_disable\_mute](group__bt__gatt__aics.md#ga5a1ad98afe45da9ffbb7247671385d40)(struct bt\_aics \*inst);

359

[ 367](group__bt__gatt__aics.md#ga43396d2d4b3bd9cdd0c82275fafeadfc)int [bt\_aics\_unmute](group__bt__gatt__aics.md#ga43396d2d4b3bd9cdd0c82275fafeadfc)(struct bt\_aics \*inst);

368

[ 376](group__bt__gatt__aics.md#ga5345254eaf099560e609d97044b39a97)int [bt\_aics\_mute](group__bt__gatt__aics.md#ga5345254eaf099560e609d97044b39a97)(struct bt\_aics \*inst);

377

[ 385](group__bt__gatt__aics.md#ga0460e82d4277a2c4b14964799ad5f2b0)int [bt\_aics\_gain\_set\_manual\_only](group__bt__gatt__aics.md#ga0460e82d4277a2c4b14964799ad5f2b0)(struct bt\_aics \*inst);

386

[ 397](group__bt__gatt__aics.md#ga22869d8a62eb59bc4aad25946da8f9cf)int [bt\_aics\_gain\_set\_auto\_only](group__bt__gatt__aics.md#ga22869d8a62eb59bc4aad25946da8f9cf)(struct bt\_aics \*inst);

398

[ 406](group__bt__gatt__aics.md#ga7ddb93125f6275fc7c99fbf448e24f0c)int [bt\_aics\_manual\_gain\_set](group__bt__gatt__aics.md#ga7ddb93125f6275fc7c99fbf448e24f0c)(struct bt\_aics \*inst);

407

[ 415](group__bt__gatt__aics.md#ga759712886cd3c4c025ea360dcb663c59)int [bt\_aics\_automatic\_gain\_set](group__bt__gatt__aics.md#ga759712886cd3c4c025ea360dcb663c59)(struct bt\_aics \*inst);

416

[ 426](group__bt__gatt__aics.md#ga20f3a178788ec6aef593034159793b94)int [bt\_aics\_gain\_set](group__bt__gatt__aics.md#ga20f3a178788ec6aef593034159793b94)(struct bt\_aics \*inst, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) gain);

427

[ 435](group__bt__gatt__aics.md#gaf0b659698aa6a6a79143d4f591f67e09)int [bt\_aics\_description\_get](group__bt__gatt__aics.md#gaf0b659698aa6a6a79143d4f591f67e09)(struct bt\_aics \*inst);

436

[ 445](group__bt__gatt__aics.md#ga7de5ffd2eb61ca562b9773b37470ebd9)int [bt\_aics\_description\_set](group__bt__gatt__aics.md#ga7de5ffd2eb61ca562b9773b37470ebd9)(struct bt\_aics \*inst, const char \*description);

446

[ 452](group__bt__gatt__aics.md#ga913838aa0d5bff239c2faef4d8a8b36b)struct bt\_aics \*[bt\_aics\_client\_free\_instance\_get](group__bt__gatt__aics.md#ga913838aa0d5bff239c2faef4d8a8b36b)(void);

453

[ 460](group__bt__gatt__aics.md#gabd6bdcdad0dd5a4c509f9e7cabb3e601)void [bt\_aics\_client\_cb\_register](group__bt__gatt__aics.md#gabd6bdcdad0dd5a4c509f9e7cabb3e601)(struct bt\_aics \*inst, struct [bt\_aics\_cb](structbt__aics__cb.md) \*cb);

461

462#ifdef \_\_cplusplus

463}

464#endif

465

469

470#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_AICS\_H\_ \*/

[bluetooth.h](bluetooth_8h.md)

Bluetooth subsystem core APIs.

[bt\_aics\_register](group__bt__gatt__aics.md#ga008ef5cebfcb9b4a3084f411fa81238e)

int bt\_aics\_register(struct bt\_aics \*aics, struct bt\_aics\_register\_param \*param)

Initialize the Audio Input Control Service instance.

[bt\_aics\_status\_cb](group__bt__gatt__aics.md#ga044d92a4273c6537a9cdf20922352ed6)

void(\* bt\_aics\_status\_cb)(struct bt\_aics \*inst, int err, bool active)

Callback function for the input status.

**Definition** aics.h:225

[bt\_aics\_gain\_set\_manual\_only](group__bt__gatt__aics.md#ga0460e82d4277a2c4b14964799ad5f2b0)

int bt\_aics\_gain\_set\_manual\_only(struct bt\_aics \*inst)

Set manual only gain mode in Audio Input Control Service.

[bt\_aics\_client\_conn\_get](group__bt__gatt__aics.md#ga0e088e26cf73f1f3b918660d4acdebb9)

int bt\_aics\_client\_conn\_get(const struct bt\_aics \*aics, struct bt\_conn \*\*conn)

Get the connection pointer of a client instance.

[bt\_aics\_gain\_setting\_cb](group__bt__gatt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb)

void(\* bt\_aics\_gain\_setting\_cb)(struct bt\_aics \*inst, int err, uint8\_t units, int8\_t minimum, int8\_t maximum)

Callback function for the gain settings.

**Definition** aics.h:197

[bt\_aics\_gain\_set](group__bt__gatt__aics.md#ga20f3a178788ec6aef593034159793b94)

int bt\_aics\_gain\_set(struct bt\_aics \*inst, int8\_t gain)

Set the input gain.

[bt\_aics\_gain\_set\_auto\_only](group__bt__gatt__aics.md#ga22869d8a62eb59bc4aad25946da8f9cf)

int bt\_aics\_gain\_set\_auto\_only(struct bt\_aics \*inst)

Set automatic only gain mode in Audio Input Control Service.

[bt\_aics\_state\_get](group__bt__gatt__aics.md#ga23bbc1393d21fe38f501813935b25b3d)

int bt\_aics\_state\_get(struct bt\_aics \*inst)

Read the Audio Input Control Service input state.

[bt\_aics\_state\_cb](group__bt__gatt__aics.md#ga2e851f49f9c7e71a18376468a13fdf4f)

void(\* bt\_aics\_state\_cb)(struct bt\_aics \*inst, int err, int8\_t gain, uint8\_t mute, uint8\_t mode)

Callback function for the input state.

**Definition** aics.h:179

[bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef)

void(\* bt\_aics\_write\_cb)(struct bt\_aics \*inst, int err)

Callback function for writes.

**Definition** aics.h:163

[bt\_aics\_gain\_setting\_get](group__bt__gatt__aics.md#ga38d7131397d7762d3bd53e152a6c6130)

int bt\_aics\_gain\_setting\_get(struct bt\_aics \*inst)

Read the Audio Input Control Service gain settings.

[bt\_aics\_unmute](group__bt__gatt__aics.md#ga43396d2d4b3bd9cdd0c82275fafeadfc)

int bt\_aics\_unmute(struct bt\_aics \*inst)

Unmute the Audio Input Control Service input.

[bt\_aics\_deactivate](group__bt__gatt__aics.md#ga4be4c4e3c74aa55fbf599157aa1c2098)

int bt\_aics\_deactivate(struct bt\_aics \*inst)

Deactivates a Audio Input Control Service instance.

[bt\_aics\_mute](group__bt__gatt__aics.md#ga5345254eaf099560e609d97044b39a97)

int bt\_aics\_mute(struct bt\_aics \*inst)

Mute the Audio Input Control Service input.

[bt\_aics\_disable\_mute](group__bt__gatt__aics.md#ga5a1ad98afe45da9ffbb7247671385d40)

int bt\_aics\_disable\_mute(struct bt\_aics \*inst)

Disable mute in the Audio Input Control Service.

[bt\_aics\_type\_cb](group__bt__gatt__aics.md#ga6e76b9f2de4cdbcd7539c76f6a347fa5)

void(\* bt\_aics\_type\_cb)(struct bt\_aics \*inst, int err, uint8\_t type)

Callback function for the input type.

**Definition** aics.h:212

[bt\_aics\_automatic\_gain\_set](group__bt__gatt__aics.md#ga759712886cd3c4c025ea360dcb663c59)

int bt\_aics\_automatic\_gain\_set(struct bt\_aics \*inst)

Set the input gain to automatic.

[bt\_aics\_manual\_gain\_set](group__bt__gatt__aics.md#ga7ddb93125f6275fc7c99fbf448e24f0c)

int bt\_aics\_manual\_gain\_set(struct bt\_aics \*inst)

Set input gain to manual.

[bt\_aics\_description\_set](group__bt__gatt__aics.md#ga7de5ffd2eb61ca562b9773b37470ebd9)

int bt\_aics\_description\_set(struct bt\_aics \*inst, const char \*description)

Set the Audio Input Control Service description.

[bt\_aics\_svc\_decl\_get](group__bt__gatt__aics.md#ga8b415343e7ecf399ecfd0dcaa49bd1ee)

void \* bt\_aics\_svc\_decl\_get(struct bt\_aics \*aics)

Get the service declaration attribute.

[bt\_aics\_client\_free\_instance\_get](group__bt__gatt__aics.md#ga913838aa0d5bff239c2faef4d8a8b36b)

struct bt\_aics \* bt\_aics\_client\_free\_instance\_get(void)

Get a new Audio Input Control Service client instance.

[bt\_aics\_description\_cb](group__bt__gatt__aics.md#ga98b142ea7a66de5577c44aa90d507930)

void(\* bt\_aics\_description\_cb)(struct bt\_aics \*inst, int err, char \*description)

Callback function for the description.

**Definition** aics.h:238

[bt\_aics\_discover\_cb](group__bt__gatt__aics.md#ga9fda39f8410308e05eb928eeb7267e83)

void(\* bt\_aics\_discover\_cb)(struct bt\_aics \*inst, int err)

Callback function for bt\_aics\_discover.

**Definition** aics.h:252

[bt\_aics\_free\_instance\_get](group__bt__gatt__aics.md#gab10ad3599f5b602cdf5504bc92508109)

struct bt\_aics \* bt\_aics\_free\_instance\_get(void)

Get a free instance of Audio Input Control Service from the pool.

[bt\_aics\_client\_cb\_register](group__bt__gatt__aics.md#gabd6bdcdad0dd5a4c509f9e7cabb3e601)

void bt\_aics\_client\_cb\_register(struct bt\_aics \*inst, struct bt\_aics\_cb \*cb)

Registers the callbacks for the Audio Input Control Service client.

[bt\_aics\_activate](group__bt__gatt__aics.md#gac46268949fa7cbbb827d149a3a904daa)

int bt\_aics\_activate(struct bt\_aics \*inst)

Activates a Audio Input Control Service instance.

[bt\_aics\_discover](group__bt__gatt__aics.md#gad16d296462af2f61a893bda8d25cc9de)

int bt\_aics\_discover(struct bt\_conn \*conn, struct bt\_aics \*inst, const struct bt\_aics\_discover\_param \*param)

Discover a Audio Input Control Service.

[bt\_aics\_status\_get](group__bt__gatt__aics.md#gade387c52d201ce10b39ef52157dae83d)

int bt\_aics\_status\_get(struct bt\_aics \*inst)

Read the Audio Input Control Service input status.

[bt\_aics\_description\_get](group__bt__gatt__aics.md#gaf0b659698aa6a6a79143d4f591f67e09)

int bt\_aics\_description\_get(struct bt\_aics \*inst)

Read the Audio Input Control Service description.

[bt\_aics\_type\_get](group__bt__gatt__aics.md#gaf57896e2096a5e96ec46a56cdf216159)

int bt\_aics\_type\_get(struct bt\_aics \*inst)

Read the Audio Input Control Service input type.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[bt\_aics\_cb](structbt__aics__cb.md)

**Definition** aics.h:254

[bt\_aics\_cb::type](structbt__aics__cb.md#a41bc7a97e28c53772573d99a38e8ac55)

bt\_aics\_type\_cb type

**Definition** aics.h:257

[bt\_aics\_cb::gain\_setting](structbt__aics__cb.md#a6b2f2a43d0a91abcecfe8372b6a1be4b)

bt\_aics\_gain\_setting\_cb gain\_setting

**Definition** aics.h:256

[bt\_aics\_cb::state](structbt__aics__cb.md#a70d099bec6407e5c92f6a4e8d6c44929)

bt\_aics\_state\_cb state

**Definition** aics.h:255

[bt\_aics\_cb::status](structbt__aics__cb.md#ac89882943c293e533bec55dd285d7aa0)

bt\_aics\_status\_cb status

**Definition** aics.h:258

[bt\_aics\_cb::description](structbt__aics__cb.md#ad37ae465600fa2e3c1868f0da07fd31a)

bt\_aics\_description\_cb description

**Definition** aics.h:259

[bt\_aics\_discover\_param](structbt__aics__discover__param.md)

Structure for discovering a Audio Input Control Service instance.

**Definition** aics.h:102

[bt\_aics\_discover\_param::end\_handle](structbt__aics__discover__param.md#ab2931e7c4a627e717d943b2907b264cb)

uint16\_t end\_handle

The end handle of the discovering.

**Definition** aics.h:112

[bt\_aics\_discover\_param::start\_handle](structbt__aics__discover__param.md#ab867f7d2ae219df0c479cce72d68842f)

uint16\_t start\_handle

The start handle of the discovering.

**Definition** aics.h:107

[bt\_aics\_register\_param](structbt__aics__register__param.md)

Structure for initializing a Audio Input Control Service instance.

**Definition** aics.h:66

[bt\_aics\_register\_param::gain\_mode](structbt__aics__register__param.md#a3658ed1900a44eef84b5602e567fe085)

uint8\_t gain\_mode

Initial audio input mode.

**Definition** aics.h:74

[bt\_aics\_register\_param::status](structbt__aics__register__param.md#a46437f4540d226ce3fbc470448f36e1f)

bool status

Initial audio input status (active/inactive).

**Definition** aics.h:89

[bt\_aics\_register\_param::units](structbt__aics__register__param.md#a4b2eae9a9716629e9c56ee3e6dc05e44)

uint8\_t units

Initial audio input gain units (N \* 0.1 dB).

**Definition** aics.h:77

[bt\_aics\_register\_param::cb](structbt__aics__register__param.md#a6c961cde10dbfbaaa26bbc2b5c867001)

struct bt\_aics\_cb \* cb

Pointer to the callback structure.

**Definition** aics.h:98

[bt\_aics\_register\_param::gain](structbt__aics__register__param.md#a966e9e99544392cdfac264ee6effcc7c)

int8\_t gain

Initial audio input gain (-128 to 127).

**Definition** aics.h:68

[bt\_aics\_register\_param::max\_gain](structbt__aics__register__param.md#aa139122e2710d9ec28ec015692545dda)

int8\_t max\_gain

Initial audio input maximum gain.

**Definition** aics.h:83

[bt\_aics\_register\_param::min\_gain](structbt__aics__register__param.md#aac91095a831fe540ee356eb9b9d402d8)

int8\_t min\_gain

Initial audio input minimum gain.

**Definition** aics.h:80

[bt\_aics\_register\_param::mute](structbt__aics__register__param.md#ac95e17bc53539deeab5d161ca1b08194)

uint8\_t mute

Initial audio input mute state.

**Definition** aics.h:71

[bt\_aics\_register\_param::desc\_writable](structbt__aics__register__param.md#acc408a0318b94cdc952ef7d6682e5705)

bool desc\_writable

Boolean to set whether the description is writable by clients.

**Definition** aics.h:92

[bt\_aics\_register\_param::type](structbt__aics__register__param.md#ad6afebea920fa4c168498ca11778ea7d)

uint8\_t type

Initial audio input type.

**Definition** aics.h:86

[bt\_aics\_register\_param::description](structbt__aics__register__param.md#af99d31215008eb201c488a5b1107e009)

char \* description

Initial audio input description.

**Definition** aics.h:95

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [aics.h](aics_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
