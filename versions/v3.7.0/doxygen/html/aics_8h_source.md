---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/aics_8h_source.html
original_path: doxygen/html/aics_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

aics.h

[Go to the documentation of this file.](aics_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020-2024 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_AICS\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_AICS\_H\_

14

35#include <[stdint.h](stdint_8h.md)>

36#include <[stdbool.h](stdbool_8h.md)>

37

38#include <zephyr/autoconf.h>

39#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

40

41#ifdef \_\_cplusplus

42extern "C" {

43#endif

44

[ 50](group__bt__gatt__aics.md#ga47436e2df23067ce86dc761d77ed14b7)#define BT\_AICS\_STATE\_UNMUTED 0x00

[ 52](group__bt__gatt__aics.md#ga1572eaaffea5412b496eb714d64aa981)#define BT\_AICS\_STATE\_MUTED 0x01

[ 54](group__bt__gatt__aics.md#gad0063d0e0b622b4093607e5485897214)#define BT\_AICS\_STATE\_MUTE\_DISABLED 0x02

56

[ 66](group__bt__gatt__aics.md#gaecb9365a5e390111311d1b415a2cee79)#define BT\_AICS\_MODE\_MANUAL\_ONLY 0x00

[ 72](group__bt__gatt__aics.md#ga6b536bdcab602ccaccfafe3b37258890)#define BT\_AICS\_MODE\_AUTO\_ONLY 0x01

[ 78](group__bt__gatt__aics.md#ga7cf0508dd7407ec3bb92dec71cc00816)#define BT\_AICS\_MODE\_MANUAL 0x02

[ 84](group__bt__gatt__aics.md#ga0ac3a583dd7ca58a0d356d9f60797517)#define BT\_AICS\_MODE\_AUTO 0x03

86

[ 92](group__bt__gatt__aics.md#ga2204f35b5f1aa41c27f62b8f0dcf74b6)#define BT\_AICS\_INPUT\_TYPE\_UNSPECIFIED 0x00

[ 94](group__bt__gatt__aics.md#gac8ebf643f9a4101ea8da18827577bf5d)#define BT\_AICS\_INPUT\_TYPE\_BLUETOOTH 0x01

[ 96](group__bt__gatt__aics.md#ga7fcb5aefacb641a8ef7db4e9a554a65d)#define BT\_AICS\_INPUT\_TYPE\_MICROPHONE 0x02

[ 98](group__bt__gatt__aics.md#ga525b361d1d555f20d292cf1aded0d046)#define BT\_AICS\_INPUT\_TYPE\_ANALOG 0x03

[ 100](group__bt__gatt__aics.md#ga688605eb9eb5b27ca62fac9b85fde472)#define BT\_AICS\_INPUT\_TYPE\_DIGITAL 0x04

[ 102](group__bt__gatt__aics.md#ga3b878b41ab30067bceefc0cd72340376)#define BT\_AICS\_INPUT\_TYPE\_RADIO 0x05

[ 104](group__bt__gatt__aics.md#ga43a02e2025e3cb3e10bc2ee2128ee877)#define BT\_AICS\_INPUT\_TYPE\_STREAMING 0x06

[ 106](group__bt__gatt__aics.md#gaacf259f2bc3d341c8d2857de5d412219)#define BT\_AICS\_INPUT\_TYPE\_AMBIENT 0x07

108

[ 117](group__bt__gatt__aics.md#gae54199f78ff7d7380353f3950bd03a39)#define BT\_AICS\_ERR\_INVALID\_COUNTER 0x80

[ 119](group__bt__gatt__aics.md#ga00c0942dab2bf25c680278927aa49af8)#define BT\_AICS\_ERR\_OP\_NOT\_SUPPORTED 0x81

[ 121](group__bt__gatt__aics.md#ga1efb1f6a4c24c2a20fc7136928abac6b)#define BT\_AICS\_ERR\_MUTE\_DISABLED 0x82

[ 123](group__bt__gatt__aics.md#ga2f3806b8056ea8ed43b2a7cd52ffa4f3)#define BT\_AICS\_ERR\_OUT\_OF\_RANGE 0x83

[ 125](group__bt__gatt__aics.md#ga6673570f7679322bfa4719bf6e41e299)#define BT\_AICS\_ERR\_GAIN\_MODE\_NOT\_ALLOWED 0x84

127

129struct bt\_aics;

130

[ 132](structbt__aics__register__param.md)struct [bt\_aics\_register\_param](structbt__aics__register__param.md) {

[ 134](structbt__aics__register__param.md#a966e9e99544392cdfac264ee6effcc7c) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [gain](structbt__aics__register__param.md#a966e9e99544392cdfac264ee6effcc7c);

135

[ 137](structbt__aics__register__param.md#ac95e17bc53539deeab5d161ca1b08194) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mute](structbt__aics__register__param.md#ac95e17bc53539deeab5d161ca1b08194);

138

[ 140](structbt__aics__register__param.md#a3658ed1900a44eef84b5602e567fe085) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gain\_mode](structbt__aics__register__param.md#a3658ed1900a44eef84b5602e567fe085);

141

[ 143](structbt__aics__register__param.md#a4b2eae9a9716629e9c56ee3e6dc05e44) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [units](structbt__aics__register__param.md#a4b2eae9a9716629e9c56ee3e6dc05e44);

144

[ 146](structbt__aics__register__param.md#aac91095a831fe540ee356eb9b9d402d8) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [min\_gain](structbt__aics__register__param.md#aac91095a831fe540ee356eb9b9d402d8);

147

[ 149](structbt__aics__register__param.md#aa139122e2710d9ec28ec015692545dda) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [max\_gain](structbt__aics__register__param.md#aa139122e2710d9ec28ec015692545dda);

150

[ 152](structbt__aics__register__param.md#ad6afebea920fa4c168498ca11778ea7d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__aics__register__param.md#ad6afebea920fa4c168498ca11778ea7d);

153

[ 155](structbt__aics__register__param.md#a46437f4540d226ce3fbc470448f36e1f) bool [status](structbt__aics__register__param.md#a46437f4540d226ce3fbc470448f36e1f);

156

[ 158](structbt__aics__register__param.md#acc408a0318b94cdc952ef7d6682e5705) bool [desc\_writable](structbt__aics__register__param.md#acc408a0318b94cdc952ef7d6682e5705);

159

[ 161](structbt__aics__register__param.md#af99d31215008eb201c488a5b1107e009) char \*[description](structbt__aics__register__param.md#af99d31215008eb201c488a5b1107e009);

162

[ 164](structbt__aics__register__param.md#a6c961cde10dbfbaaa26bbc2b5c867001) struct [bt\_aics\_cb](structbt__aics__cb.md) \*[cb](structbt__aics__register__param.md#a6c961cde10dbfbaaa26bbc2b5c867001);

165};

166

[ 168](structbt__aics__discover__param.md)struct [bt\_aics\_discover\_param](structbt__aics__discover__param.md) {

[ 174](structbt__aics__discover__param.md#ab867f7d2ae219df0c479cce72d68842f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_handle](structbt__aics__discover__param.md#ab867f7d2ae219df0c479cce72d68842f);

[ 180](structbt__aics__discover__param.md#ab2931e7c4a627e717d943b2907b264cb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__aics__discover__param.md#ab2931e7c4a627e717d943b2907b264cb);

181};

182

[ 188](group__bt__gatt__aics.md#gab10ad3599f5b602cdf5504bc92508109)struct bt\_aics \*[bt\_aics\_free\_instance\_get](group__bt__gatt__aics.md#gab10ad3599f5b602cdf5504bc92508109)(void);

189

[ 199](group__bt__gatt__aics.md#ga8b415343e7ecf399ecfd0dcaa49bd1ee)void \*[bt\_aics\_svc\_decl\_get](group__bt__gatt__aics.md#ga8b415343e7ecf399ecfd0dcaa49bd1ee)(struct bt\_aics \*aics);

200

[ 212](group__bt__gatt__aics.md#ga0e088e26cf73f1f3b918660d4acdebb9)int [bt\_aics\_client\_conn\_get](group__bt__gatt__aics.md#ga0e088e26cf73f1f3b918660d4acdebb9)(const struct bt\_aics \*aics, struct bt\_conn \*\*conn);

213

[ 222](group__bt__gatt__aics.md#ga008ef5cebfcb9b4a3084f411fa81238e)int [bt\_aics\_register](group__bt__gatt__aics.md#ga008ef5cebfcb9b4a3084f411fa81238e)(struct bt\_aics \*aics, struct [bt\_aics\_register\_param](structbt__aics__register__param.md) \*param);

223

[ 231](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef)typedef void (\*[bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef))(struct bt\_aics \*inst, int err);

232

[ 247](group__bt__gatt__aics.md#ga2e851f49f9c7e71a18376468a13fdf4f)typedef void (\*[bt\_aics\_state\_cb](group__bt__gatt__aics.md#ga2e851f49f9c7e71a18376468a13fdf4f))(struct bt\_aics \*inst, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) gain,

248 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode);

249

[ 265](group__bt__gatt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb)typedef void (\*[bt\_aics\_gain\_setting\_cb](group__bt__gatt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb))(struct bt\_aics \*inst, int err,

266 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) units, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) minimum,

267 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) maximum);

268

[ 280](group__bt__gatt__aics.md#ga6e76b9f2de4cdbcd7539c76f6a347fa5)typedef void (\*[bt\_aics\_type\_cb](group__bt__gatt__aics.md#ga6e76b9f2de4cdbcd7539c76f6a347fa5))(struct bt\_aics \*inst, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type);

281

[ 293](group__bt__gatt__aics.md#ga044d92a4273c6537a9cdf20922352ed6)typedef void (\*[bt\_aics\_status\_cb](group__bt__gatt__aics.md#ga044d92a4273c6537a9cdf20922352ed6))(struct bt\_aics \*inst, int err, bool active);

294

[ 306](group__bt__gatt__aics.md#ga98b142ea7a66de5577c44aa90d507930)typedef void (\*[bt\_aics\_description\_cb](group__bt__gatt__aics.md#ga98b142ea7a66de5577c44aa90d507930))(struct bt\_aics \*inst, int err,

307 char \*description);

308

[ 320](group__bt__gatt__aics.md#ga9fda39f8410308e05eb928eeb7267e83)typedef void (\*[bt\_aics\_discover\_cb](group__bt__gatt__aics.md#ga9fda39f8410308e05eb928eeb7267e83))(struct bt\_aics \*inst, int err);

321

[ 327](structbt__aics__cb.md)struct [bt\_aics\_cb](structbt__aics__cb.md) {

[ 329](structbt__aics__cb.md#a70d099bec6407e5c92f6a4e8d6c44929) [bt\_aics\_state\_cb](group__bt__gatt__aics.md#ga2e851f49f9c7e71a18376468a13fdf4f) [state](structbt__aics__cb.md#a70d099bec6407e5c92f6a4e8d6c44929);

[ 331](structbt__aics__cb.md#a6b2f2a43d0a91abcecfe8372b6a1be4b) [bt\_aics\_gain\_setting\_cb](group__bt__gatt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb) [gain\_setting](structbt__aics__cb.md#a6b2f2a43d0a91abcecfe8372b6a1be4b);

[ 333](structbt__aics__cb.md#a41bc7a97e28c53772573d99a38e8ac55) [bt\_aics\_type\_cb](group__bt__gatt__aics.md#ga6e76b9f2de4cdbcd7539c76f6a347fa5) [type](structbt__aics__cb.md#a41bc7a97e28c53772573d99a38e8ac55);

[ 335](structbt__aics__cb.md#ac89882943c293e533bec55dd285d7aa0) [bt\_aics\_status\_cb](group__bt__gatt__aics.md#ga044d92a4273c6537a9cdf20922352ed6) [status](structbt__aics__cb.md#ac89882943c293e533bec55dd285d7aa0);

[ 337](structbt__aics__cb.md#ad37ae465600fa2e3c1868f0da07fd31a) [bt\_aics\_description\_cb](group__bt__gatt__aics.md#ga98b142ea7a66de5577c44aa90d507930) [description](structbt__aics__cb.md#ad37ae465600fa2e3c1868f0da07fd31a);

338

339#if defined(CONFIG\_BT\_AICS\_CLIENT) || defined(\_\_DOXYGEN\_\_)

[ 341](structbt__aics__cb.md#ae946f4b434b485774a3c8ddca5d86898) [bt\_aics\_discover\_cb](group__bt__gatt__aics.md#ga9fda39f8410308e05eb928eeb7267e83) [discover](structbt__aics__cb.md#ae946f4b434b485774a3c8ddca5d86898);

[ 343](structbt__aics__cb.md#a1f13bdcfbfac65800f9e66dad48c3b78) [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef) [set\_gain](structbt__aics__cb.md#a1f13bdcfbfac65800f9e66dad48c3b78);

[ 345](structbt__aics__cb.md#a80c8abd842706d2588e6a075cba61ba8) [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef) [unmute](structbt__aics__cb.md#a80c8abd842706d2588e6a075cba61ba8);

[ 347](structbt__aics__cb.md#a41b6cac6ccc0195921d2e5a127d9091d) [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef) [mute](structbt__aics__cb.md#a41b6cac6ccc0195921d2e5a127d9091d);

[ 349](structbt__aics__cb.md#a1b54464a8c6df54993914da97da2f93d) [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef) [set\_manual\_mode](structbt__aics__cb.md#a1b54464a8c6df54993914da97da2f93d);

[ 351](structbt__aics__cb.md#aac9dccf825f5aa423212af4af3d4ca38) [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef) [set\_auto\_mode](structbt__aics__cb.md#aac9dccf825f5aa423212af4af3d4ca38);

352#endif /\* CONFIG\_BT\_AICS\_CLIENT \*/

353};

354

355

[ 368](group__bt__gatt__aics.md#gad16d296462af2f61a893bda8d25cc9de)int [bt\_aics\_discover](group__bt__gatt__aics.md#gad16d296462af2f61a893bda8d25cc9de)(struct bt\_conn \*conn, struct bt\_aics \*inst,

369 const struct [bt\_aics\_discover\_param](structbt__aics__discover__param.md) \*param);

370

[ 381](group__bt__gatt__aics.md#ga4be4c4e3c74aa55fbf599157aa1c2098)int [bt\_aics\_deactivate](group__bt__gatt__aics.md#ga4be4c4e3c74aa55fbf599157aa1c2098)(struct bt\_aics \*inst);

382

[ 394](group__bt__gatt__aics.md#gac46268949fa7cbbb827d149a3a904daa)int [bt\_aics\_activate](group__bt__gatt__aics.md#gac46268949fa7cbbb827d149a3a904daa)(struct bt\_aics \*inst);

395

[ 403](group__bt__gatt__aics.md#ga23bbc1393d21fe38f501813935b25b3d)int [bt\_aics\_state\_get](group__bt__gatt__aics.md#ga23bbc1393d21fe38f501813935b25b3d)(struct bt\_aics \*inst);

404

[ 412](group__bt__gatt__aics.md#ga38d7131397d7762d3bd53e152a6c6130)int [bt\_aics\_gain\_setting\_get](group__bt__gatt__aics.md#ga38d7131397d7762d3bd53e152a6c6130)(struct bt\_aics \*inst);

413

[ 421](group__bt__gatt__aics.md#gaf57896e2096a5e96ec46a56cdf216159)int [bt\_aics\_type\_get](group__bt__gatt__aics.md#gaf57896e2096a5e96ec46a56cdf216159)(struct bt\_aics \*inst);

422

[ 430](group__bt__gatt__aics.md#gade387c52d201ce10b39ef52157dae83d)int [bt\_aics\_status\_get](group__bt__gatt__aics.md#gade387c52d201ce10b39ef52157dae83d)(struct bt\_aics \*inst);

431

[ 442](group__bt__gatt__aics.md#ga5a1ad98afe45da9ffbb7247671385d40)int [bt\_aics\_disable\_mute](group__bt__gatt__aics.md#ga5a1ad98afe45da9ffbb7247671385d40)(struct bt\_aics \*inst);

443

[ 451](group__bt__gatt__aics.md#ga43396d2d4b3bd9cdd0c82275fafeadfc)int [bt\_aics\_unmute](group__bt__gatt__aics.md#ga43396d2d4b3bd9cdd0c82275fafeadfc)(struct bt\_aics \*inst);

452

[ 460](group__bt__gatt__aics.md#ga5345254eaf099560e609d97044b39a97)int [bt\_aics\_mute](group__bt__gatt__aics.md#ga5345254eaf099560e609d97044b39a97)(struct bt\_aics \*inst);

461

[ 469](group__bt__gatt__aics.md#ga0460e82d4277a2c4b14964799ad5f2b0)int [bt\_aics\_gain\_set\_manual\_only](group__bt__gatt__aics.md#ga0460e82d4277a2c4b14964799ad5f2b0)(struct bt\_aics \*inst);

470

[ 481](group__bt__gatt__aics.md#ga22869d8a62eb59bc4aad25946da8f9cf)int [bt\_aics\_gain\_set\_auto\_only](group__bt__gatt__aics.md#ga22869d8a62eb59bc4aad25946da8f9cf)(struct bt\_aics \*inst);

482

[ 490](group__bt__gatt__aics.md#ga7ddb93125f6275fc7c99fbf448e24f0c)int [bt\_aics\_manual\_gain\_set](group__bt__gatt__aics.md#ga7ddb93125f6275fc7c99fbf448e24f0c)(struct bt\_aics \*inst);

491

[ 499](group__bt__gatt__aics.md#ga759712886cd3c4c025ea360dcb663c59)int [bt\_aics\_automatic\_gain\_set](group__bt__gatt__aics.md#ga759712886cd3c4c025ea360dcb663c59)(struct bt\_aics \*inst);

500

[ 510](group__bt__gatt__aics.md#ga20f3a178788ec6aef593034159793b94)int [bt\_aics\_gain\_set](group__bt__gatt__aics.md#ga20f3a178788ec6aef593034159793b94)(struct bt\_aics \*inst, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) gain);

511

[ 519](group__bt__gatt__aics.md#gaf0b659698aa6a6a79143d4f591f67e09)int [bt\_aics\_description\_get](group__bt__gatt__aics.md#gaf0b659698aa6a6a79143d4f591f67e09)(struct bt\_aics \*inst);

520

[ 529](group__bt__gatt__aics.md#ga7de5ffd2eb61ca562b9773b37470ebd9)int [bt\_aics\_description\_set](group__bt__gatt__aics.md#ga7de5ffd2eb61ca562b9773b37470ebd9)(struct bt\_aics \*inst, const char \*description);

530

[ 536](group__bt__gatt__aics.md#ga913838aa0d5bff239c2faef4d8a8b36b)struct bt\_aics \*[bt\_aics\_client\_free\_instance\_get](group__bt__gatt__aics.md#ga913838aa0d5bff239c2faef4d8a8b36b)(void);

537

[ 544](group__bt__gatt__aics.md#gabd6bdcdad0dd5a4c509f9e7cabb3e601)void [bt\_aics\_client\_cb\_register](group__bt__gatt__aics.md#gabd6bdcdad0dd5a4c509f9e7cabb3e601)(struct bt\_aics \*inst, struct [bt\_aics\_cb](structbt__aics__cb.md) \*cb);

545

546#ifdef \_\_cplusplus

547}

548#endif

549

553

554#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_AICS\_H\_ \*/

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[bt\_aics\_register](group__bt__gatt__aics.md#ga008ef5cebfcb9b4a3084f411fa81238e)

int bt\_aics\_register(struct bt\_aics \*aics, struct bt\_aics\_register\_param \*param)

Initialize the Audio Input Control Service instance.

[bt\_aics\_status\_cb](group__bt__gatt__aics.md#ga044d92a4273c6537a9cdf20922352ed6)

void(\* bt\_aics\_status\_cb)(struct bt\_aics \*inst, int err, bool active)

Callback function for the input status.

**Definition** aics.h:293

[bt\_aics\_gain\_set\_manual\_only](group__bt__gatt__aics.md#ga0460e82d4277a2c4b14964799ad5f2b0)

int bt\_aics\_gain\_set\_manual\_only(struct bt\_aics \*inst)

Set manual only gain mode in Audio Input Control Service.

[bt\_aics\_client\_conn\_get](group__bt__gatt__aics.md#ga0e088e26cf73f1f3b918660d4acdebb9)

int bt\_aics\_client\_conn\_get(const struct bt\_aics \*aics, struct bt\_conn \*\*conn)

Get the connection pointer of a client instance.

[bt\_aics\_gain\_setting\_cb](group__bt__gatt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb)

void(\* bt\_aics\_gain\_setting\_cb)(struct bt\_aics \*inst, int err, uint8\_t units, int8\_t minimum, int8\_t maximum)

Callback function for the gain settings.

**Definition** aics.h:265

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

**Definition** aics.h:247

[bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef)

void(\* bt\_aics\_write\_cb)(struct bt\_aics \*inst, int err)

Callback function for writes.

**Definition** aics.h:231

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

**Definition** aics.h:280

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

**Definition** aics.h:306

[bt\_aics\_discover\_cb](group__bt__gatt__aics.md#ga9fda39f8410308e05eb928eeb7267e83)

void(\* bt\_aics\_discover\_cb)(struct bt\_aics \*inst, int err)

Callback function for bt\_aics\_discover.

**Definition** aics.h:320

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

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

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

Struct to hold callbacks for the Audio Input Control Service.

**Definition** aics.h:327

[bt\_aics\_cb::set\_manual\_mode](structbt__aics__cb.md#a1b54464a8c6df54993914da97da2f93d)

bt\_aics\_write\_cb set\_manual\_mode

The set manual mode operation has completed.

**Definition** aics.h:349

[bt\_aics\_cb::set\_gain](structbt__aics__cb.md#a1f13bdcfbfac65800f9e66dad48c3b78)

bt\_aics\_write\_cb set\_gain

The set gain operation has completed.

**Definition** aics.h:343

[bt\_aics\_cb::mute](structbt__aics__cb.md#a41b6cac6ccc0195921d2e5a127d9091d)

bt\_aics\_write\_cb mute

The mut operation has completed.

**Definition** aics.h:347

[bt\_aics\_cb::type](structbt__aics__cb.md#a41bc7a97e28c53772573d99a38e8ac55)

bt\_aics\_type\_cb type

The audio input type has changed.

**Definition** aics.h:333

[bt\_aics\_cb::gain\_setting](structbt__aics__cb.md#a6b2f2a43d0a91abcecfe8372b6a1be4b)

bt\_aics\_gain\_setting\_cb gain\_setting

The gain setting has changed.

**Definition** aics.h:331

[bt\_aics\_cb::state](structbt__aics__cb.md#a70d099bec6407e5c92f6a4e8d6c44929)

bt\_aics\_state\_cb state

The audio input state has changed.

**Definition** aics.h:329

[bt\_aics\_cb::unmute](structbt__aics__cb.md#a80c8abd842706d2588e6a075cba61ba8)

bt\_aics\_write\_cb unmute

The unmute operation has completed.

**Definition** aics.h:345

[bt\_aics\_cb::set\_auto\_mode](structbt__aics__cb.md#aac9dccf825f5aa423212af4af3d4ca38)

bt\_aics\_write\_cb set\_auto\_mode

The set automatic mode has completed.

**Definition** aics.h:351

[bt\_aics\_cb::status](structbt__aics__cb.md#ac89882943c293e533bec55dd285d7aa0)

bt\_aics\_status\_cb status

The audio input status has changed.

**Definition** aics.h:335

[bt\_aics\_cb::description](structbt__aics__cb.md#ad37ae465600fa2e3c1868f0da07fd31a)

bt\_aics\_description\_cb description

The audio input decscription has changed.

**Definition** aics.h:337

[bt\_aics\_cb::discover](structbt__aics__cb.md#ae946f4b434b485774a3c8ddca5d86898)

bt\_aics\_discover\_cb discover

The discovery has completed.

**Definition** aics.h:341

[bt\_aics\_discover\_param](structbt__aics__discover__param.md)

Structure for discovering a Audio Input Control Service instance.

**Definition** aics.h:168

[bt\_aics\_discover\_param::end\_handle](structbt__aics__discover__param.md#ab2931e7c4a627e717d943b2907b264cb)

uint16\_t end\_handle

The end handle of the discovering.

**Definition** aics.h:180

[bt\_aics\_discover\_param::start\_handle](structbt__aics__discover__param.md#ab867f7d2ae219df0c479cce72d68842f)

uint16\_t start\_handle

The start handle of the discovering.

**Definition** aics.h:174

[bt\_aics\_register\_param](structbt__aics__register__param.md)

Structure for initializing a Audio Input Control Service instance.

**Definition** aics.h:132

[bt\_aics\_register\_param::gain\_mode](structbt__aics__register__param.md#a3658ed1900a44eef84b5602e567fe085)

uint8\_t gain\_mode

Initial audio input mode.

**Definition** aics.h:140

[bt\_aics\_register\_param::status](structbt__aics__register__param.md#a46437f4540d226ce3fbc470448f36e1f)

bool status

Initial audio input status (active/inactive).

**Definition** aics.h:155

[bt\_aics\_register\_param::units](structbt__aics__register__param.md#a4b2eae9a9716629e9c56ee3e6dc05e44)

uint8\_t units

Initial audio input gain units (N \* 0.1 dB).

**Definition** aics.h:143

[bt\_aics\_register\_param::cb](structbt__aics__register__param.md#a6c961cde10dbfbaaa26bbc2b5c867001)

struct bt\_aics\_cb \* cb

Pointer to the callback structure.

**Definition** aics.h:164

[bt\_aics\_register\_param::gain](structbt__aics__register__param.md#a966e9e99544392cdfac264ee6effcc7c)

int8\_t gain

Initial audio input gain (-128 to 127).

**Definition** aics.h:134

[bt\_aics\_register\_param::max\_gain](structbt__aics__register__param.md#aa139122e2710d9ec28ec015692545dda)

int8\_t max\_gain

Initial audio input maximum gain.

**Definition** aics.h:149

[bt\_aics\_register\_param::min\_gain](structbt__aics__register__param.md#aac91095a831fe540ee356eb9b9d402d8)

int8\_t min\_gain

Initial audio input minimum gain.

**Definition** aics.h:146

[bt\_aics\_register\_param::mute](structbt__aics__register__param.md#ac95e17bc53539deeab5d161ca1b08194)

uint8\_t mute

Initial audio input mute state.

**Definition** aics.h:137

[bt\_aics\_register\_param::desc\_writable](structbt__aics__register__param.md#acc408a0318b94cdc952ef7d6682e5705)

bool desc\_writable

Boolean to set whether the description is writable by clients.

**Definition** aics.h:158

[bt\_aics\_register\_param::type](structbt__aics__register__param.md#ad6afebea920fa4c168498ca11778ea7d)

uint8\_t type

Initial audio input type.

**Definition** aics.h:152

[bt\_aics\_register\_param::description](structbt__aics__register__param.md#af99d31215008eb201c488a5b1107e009)

char \* description

Initial audio input description.

**Definition** aics.h:161

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [aics.h](aics_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
