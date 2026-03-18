---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bluetooth_8h_source.html
original_path: doxygen/html/bluetooth_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bluetooth.h

[Go to the documentation of this file.](bluetooth_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Nordic Semiconductor ASA

7 \* Copyright (c) 2015-2016 Intel Corporation

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_BLUETOOTH\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_BLUETOOTH\_H\_

13

20

21#include <[stdbool.h](stdbool_8h.md)>

22#include <[string.h](string_8h.md)>

23

24#include <[zephyr/sys/util.h](util_8h.md)>

25#include <[zephyr/net/buf.h](net_2buf_8h.md)>

26#include <[zephyr/bluetooth/gap.h](gap_8h.md)>

27#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

28#include <[zephyr/bluetooth/crypto.h](bluetooth_2crypto_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

40

[ 46](group__bt__gap.md#gaded4b52c9bb87fd4d19b1eb9361973e5)#define BT\_ID\_DEFAULT 0

47

49struct bt\_le\_ext\_adv;

50

52struct bt\_le\_per\_adv\_sync;

53

54/\* Don't require everyone to include conn.h \*/

55struct bt\_conn;

56

57/\* Don't require everyone to include iso.h \*/

58struct [bt\_iso\_biginfo](structbt__iso__biginfo.md);

59

60/\* Don't require everyone to include direction.h \*/

61struct [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md);

62

[ 63](structbt__le__ext__adv__sent__info.md)struct [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) {

[ 65](structbt__le__ext__adv__sent__info.md#a80f661efd35b069c2f8700851e9429a2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_sent](structbt__le__ext__adv__sent__info.md#a80f661efd35b069c2f8700851e9429a2);

66};

67

[ 68](structbt__le__ext__adv__connected__info.md)struct [bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md) {

[ 70](structbt__le__ext__adv__connected__info.md#a157efa6206b418f768582107c566fde2) struct bt\_conn \*[conn](structbt__le__ext__adv__connected__info.md#a157efa6206b418f768582107c566fde2);

71};

72

[ 73](structbt__le__ext__adv__scanned__info.md)struct [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md) {

[ 75](structbt__le__ext__adv__scanned__info.md#a4431f157891d2c1a7d0e40f7e879ac3d) [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__ext__adv__scanned__info.md#a4431f157891d2c1a7d0e40f7e879ac3d);

76};

77

[ 78](structbt__le__per__adv__data__request.md)struct [bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md) {

[ 80](structbt__le__per__adv__data__request.md#a779ed161919c3117f6ce165deb0a9b0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [start](structbt__le__per__adv__data__request.md#a779ed161919c3117f6ce165deb0a9b0a);

81

[ 83](structbt__le__per__adv__data__request.md#a766991899bc3e689adec36bf1f12e802) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [count](structbt__le__per__adv__data__request.md#a766991899bc3e689adec36bf1f12e802);

84};

85

[ 86](structbt__le__per__adv__response__info.md)struct [bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md) {

[ 88](structbt__le__per__adv__response__info.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__le__per__adv__response__info.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5);

89

[ 96](structbt__le__per__adv__response__info.md#ab17f33cb713d258bf6c863a64e5aba07) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_status](structbt__le__per__adv__response__info.md#ab17f33cb713d258bf6c863a64e5aba07);

97

[ 99](structbt__le__per__adv__response__info.md#a7ed20f695e0d696eaab7cddc4e3c11fb) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__per__adv__response__info.md#a7ed20f695e0d696eaab7cddc4e3c11fb);

100

[ 102](structbt__le__per__adv__response__info.md#a2db58fb452a07290ab4a50892c682837) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__le__per__adv__response__info.md#a2db58fb452a07290ab4a50892c682837);

103

[ 105](structbt__le__per__adv__response__info.md#a52b0c612b09cfcb3eb2ea475614c34b8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__le__per__adv__response__info.md#a52b0c612b09cfcb3eb2ea475614c34b8);

106

[ 108](structbt__le__per__adv__response__info.md#a83cc642c9f22c767421644e7d8233001) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot](structbt__le__per__adv__response__info.md#a83cc642c9f22c767421644e7d8233001);

109};

110

[ 111](structbt__le__ext__adv__cb.md)struct [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md) {

[ 123](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60) void (\*[sent](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60))(struct bt\_le\_ext\_adv \*adv,

124 struct [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) \*info);

125

[ 135](structbt__le__ext__adv__cb.md#a7aad0fbd8e531e70f661500c338d870e) void (\*[connected](structbt__le__ext__adv__cb.md#a7aad0fbd8e531e70f661500c338d870e))(struct bt\_le\_ext\_adv \*adv,

136 struct [bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md) \*info);

137

[ 148](structbt__le__ext__adv__cb.md#a277dc3269741d40b644ae3c777198fab) void (\*[scanned](structbt__le__ext__adv__cb.md#a277dc3269741d40b644ae3c777198fab))(struct bt\_le\_ext\_adv \*adv,

149 struct [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md) \*info);

150

151#if defined(CONFIG\_BT\_PRIVACY)

164 [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*rpa\_expired)(struct bt\_le\_ext\_adv \*adv);

165#endif /\* defined(CONFIG\_BT\_PRIVACY) \*/

166

167#if defined(CONFIG\_BT\_PER\_ADV\_RSP)

177 void (\*pawr\_data\_request)(struct bt\_le\_ext\_adv \*adv,

178 const struct [bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md) \*request);

188 void (\*pawr\_response)(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md) \*info,

189 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

190

191#endif /\* defined(CONFIG\_BT\_PER\_ADV\_RSP) \*/

192};

193

[ 200](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb)typedef void (\*[bt\_ready\_cb\_t](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb))(int err);

201

[ 221](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b)int [bt\_enable](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b)([bt\_ready\_cb\_t](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb) cb);

222

[ 232](group__bt__gap.md#ga0a58e5a050170e84a80f8d5bb3516ec7)int [bt\_disable](group__bt__gap.md#ga0a58e5a050170e84a80f8d5bb3516ec7)(void);

233

[ 239](group__bt__gap.md#gaa8bf6854e7ad1fe7e0805737576e5d1a)bool [bt\_is\_ready](group__bt__gap.md#gaa8bf6854e7ad1fe7e0805737576e5d1a)(void);

240

[ 258](group__bt__gap.md#gac8bb3609a3d6da69ff736809e45f5c8a)int [bt\_set\_name](group__bt__gap.md#gac8bb3609a3d6da69ff736809e45f5c8a)(const char \*name);

259

[ 267](group__bt__gap.md#gad922d894b25e86de3f81ce77200a13fd)const char \*[bt\_get\_name](group__bt__gap.md#gad922d894b25e86de3f81ce77200a13fd)(void);

268

[ 279](group__bt__gap.md#ga35b76ea7ce79721e47ca4164e08b2dfb)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_get\_appearance](group__bt__gap.md#ga35b76ea7ce79721e47ca4164e08b2dfb)(void);

280

[ 295](group__bt__gap.md#gaf0729453790aab1bd3d52c623be3b35a)int [bt\_set\_appearance](group__bt__gap.md#gaf0729453790aab1bd3d52c623be3b35a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) new\_appearance);

296

[ 317](group__bt__gap.md#ga06d0ae35cbf4382679cc3cfe612cee4d)void [bt\_id\_get](group__bt__gap.md#ga06d0ae35cbf4382679cc3cfe612cee4d)([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addrs, size\_t \*count);

318

[ 365](group__bt__gap.md#gae11eb8ad254418c38a0e8689df25a159)int [bt\_id\_create](group__bt__gap.md#gae11eb8ad254418c38a0e8689df25a159)([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*irk);

366

[ 399](group__bt__gap.md#gabb3353edc8a3a8d29a0370049b20cbe4)int [bt\_id\_reset](group__bt__gap.md#gabb3353edc8a3a8d29a0370049b20cbe4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*irk);

400

[ 417](group__bt__gap.md#gaf6cd906690a51ebed04bea4f4ef716ff)int [bt\_id\_delete](group__bt__gap.md#gaf6cd906690a51ebed04bea4f4ef716ff)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id);

418

[ 430](group__bt__gap.md#ga7357d34bf295a16d8288df3bf75e7976)#define BT\_DATA\_SERIALIZED\_SIZE(data\_len) ((data\_len) + 2)

431

[ 439](structbt__data.md)struct [bt\_data](structbt__data.md) {

[ 440](structbt__data.md#a984aecb40a4993ffa113be53942db065) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__data.md#a984aecb40a4993ffa113be53942db065);

[ 441](structbt__data.md#abda19091a1b8f99d385f11772ef34d5f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_len](structbt__data.md#abda19091a1b8f99d385f11772ef34d5f);

[ 442](structbt__data.md#ac80ec10101ad69a86f703a4e652c7826) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__data.md#ac80ec10101ad69a86f703a4e652c7826);

443};

444

[ 455](group__bt__gap.md#ga8481217e632522e1f322de87d745f8f0)#define BT\_DATA(\_type, \_data, \_data\_len) \

456 { \

457 .type = (\_type), \

458 .data\_len = (\_data\_len), \

459 .data = (const uint8\_t \*)(\_data), \

460 }

461

[ 471](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)#define BT\_DATA\_BYTES(\_type, \_bytes...) \

472 BT\_DATA(\_type, ((uint8\_t []) { \_bytes }), \

473 sizeof((uint8\_t []) { \_bytes }))

474

[ 485](group__bt__gap.md#ga3d2c6adc42eb9510734630f38d921b9a)size\_t [bt\_data\_get\_len](group__bt__gap.md#ga3d2c6adc42eb9510734630f38d921b9a)(const struct [bt\_data](structbt__data.md) data[], size\_t data\_count);

486

[ 501](group__bt__gap.md#ga3c067b16468ebd17973faeded0fc83c9)size\_t [bt\_data\_serialize](group__bt__gap.md#ga3c067b16468ebd17973faeded0fc83c9)(const struct [bt\_data](structbt__data.md) \*input, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*output);

502

504enum {

[ 506](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea928b376123819cb0a69fbb5b35608dbf) [BT\_LE\_ADV\_OPT\_NONE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea928b376123819cb0a69fbb5b35608dbf) = 0,

507

[ 516](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) [BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

517

[ 532](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2) [BT\_LE\_ADV\_OPT\_ONE\_TIME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

533

[ 544](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e) [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

545

[ 566](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398) [BT\_LE\_ADV\_OPT\_USE\_NAME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

567

[ 574](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeafd164ec5476f5e2d9aedf50032946872) [BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeafd164ec5476f5e2d9aedf50032946872) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

575

[ 588](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabdcf1c80662061fa30575e1f9fc6cf6f) [BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabdcf1c80662061fa30575e1f9fc6cf6f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

589

[ 593](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea807ba316edc49c8448a8ff7d497173f5) [BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea807ba316edc49c8448a8ff7d497173f5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

594

[ 596](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead5efef3d01731110dbd71d5a5dc9baaf) [BT\_LE\_ADV\_OPT\_FILTER\_CONN](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead5efef3d01731110dbd71d5a5dc9baaf) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

597

[ 601](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea1563b053f457833d1a3d11c8dc4d394b) [BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea1563b053f457833d1a3d11c8dc4d394b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

602

[ 612](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) [BT\_LE\_ADV\_OPT\_SCANNABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

613

[ 634](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) [BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

635

[ 650](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae864aefcdfbecaffe823b9b144fe0a6b) [BT\_LE\_ADV\_OPT\_NO\_2M](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae864aefcdfbecaffe823b9b144fe0a6b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

651

[ 662](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1) [BT\_LE\_ADV\_OPT\_CODED](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

663

[ 669](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea185e0f884f8b0ce79625448638de8fab) [BT\_LE\_ADV\_OPT\_ANONYMOUS](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea185e0f884f8b0ce79625448638de8fab) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

670

[ 676](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaecff4fe3ac3d1fba3f6fa76c77713859) [BT\_LE\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaecff4fe3ac3d1fba3f6fa76c77713859) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

677

[ 679](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeab46741616f8bfe50c4b492d1f7970779) [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeab46741616f8bfe50c4b492d1f7970779) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

680

[ 682](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabd9cb02691d7e025fe3fea9a80123275) [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabd9cb02691d7e025fe3fea9a80123275) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

683

[ 685](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea89f7494620236c976bf1a76a880e2a28) [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea89f7494620236c976bf1a76a880e2a28) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17),

686

[ 695](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73) [BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18),

696

[ 709](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea22958d8539d661ad7ca8d3f1173e7e5e) [BT\_LE\_ADV\_OPT\_USE\_NRPA](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea22958d8539d661ad7ca8d3f1173e7e5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

710};

711

[ 713](structbt__le__adv__param.md)struct [bt\_le\_adv\_param](structbt__le__adv__param.md) {

[ 722](structbt__le__adv__param.md#af957bd92b949536af2b2db0db7b2b425) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__le__adv__param.md#af957bd92b949536af2b2db0db7b2b425);

723

[ 729](structbt__le__adv__param.md#a6e2f0e1b76495afe7fe661e8698d0909) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__adv__param.md#a6e2f0e1b76495afe7fe661e8698d0909);

730

[ 739](structbt__le__adv__param.md#a9911e9bfc97ff0c48a6decae3f922e95) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [secondary\_max\_skip](structbt__le__adv__param.md#a9911e9bfc97ff0c48a6decae3f922e95);

740

[ 742](structbt__le__adv__param.md#a2a978c60153eb03697769bc72928f4ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__adv__param.md#a2a978c60153eb03697769bc72928f4ef);

743

[ 751](structbt__le__adv__param.md#aca8ff5a4f5d29184535162f007b2d39e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval\_min](structbt__le__adv__param.md#aca8ff5a4f5d29184535162f007b2d39e);

752

[ 760](structbt__le__adv__param.md#afeba6973dca99d8ee818fdde0c22cb59) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval\_max](structbt__le__adv__param.md#afeba6973dca99d8ee818fdde0c22cb59);

761

[ 777](structbt__le__adv__param.md#a4cf31f54f067fffa3c848adc2ffd7119) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[peer](structbt__le__adv__param.md#a4cf31f54f067fffa3c848adc2ffd7119);

778};

779

780

782enum {

[ 784](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aaa2c689d726eacfb18d87655b1f587518) [BT\_LE\_PER\_ADV\_OPT\_NONE](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aaa2c689d726eacfb18d87655b1f587518) = 0,

785

[ 791](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa9524537e4cb726f4ff10ba93381bb27f) [BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa9524537e4cb726f4ff10ba93381bb27f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

792

[ 798](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa38cebc2ae885ff630b34c603e2ec6403) [BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa38cebc2ae885ff630b34c603e2ec6403) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

799};

800

[ 801](structbt__le__per__adv__param.md)struct [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md) {

[ 808](structbt__le__per__adv__param.md#a49da44a3c0e4e866ffccffae5a9a22f7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_min](structbt__le__per__adv__param.md#a49da44a3c0e4e866ffccffae5a9a22f7);

809

[ 816](structbt__le__per__adv__param.md#a61308cfe72ad23372dfd2a3bd2550726) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_max](structbt__le__per__adv__param.md#a61308cfe72ad23372dfd2a3bd2550726);

817

[ 819](structbt__le__per__adv__param.md#a9b80c2427171920f466601e7e8468814) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__per__adv__param.md#a9b80c2427171920f466601e7e8468814);

820

821#if defined(CONFIG\_BT\_PER\_ADV\_RSP)

827 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents;

828

834 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subevent\_interval;

835

841 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_delay;

842

848 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_spacing;

849

855 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_response\_slots;

856#endif /\* CONFIG\_BT\_PER\_ADV\_RSP \*/

857};

858

[ 868](group__bt__gap.md#ga71555b857cf8c2a47c36e4dafa7accf4)#define BT\_LE\_ADV\_PARAM\_INIT(\_options, \_int\_min, \_int\_max, \_peer) \

869{ \

870 .id = BT\_ID\_DEFAULT, \

871 .sid = 0, \

872 .secondary\_max\_skip = 0, \

873 .options = (\_options), \

874 .interval\_min = (\_int\_min), \

875 .interval\_max = (\_int\_max), \

876 .peer = (\_peer), \

877}

878

[ 888](group__bt__gap.md#ga9557269dd36b624b49e76c511c3a0cc1)#define BT\_LE\_ADV\_PARAM(\_options, \_int\_min, \_int\_max, \_peer) \

889 ((struct bt\_le\_adv\_param[]) { \

890 BT\_LE\_ADV\_PARAM\_INIT(\_options, \_int\_min, \_int\_max, \_peer) \

891 })

892

[ 893](group__bt__gap.md#ga1f5edc3c4cbead62e32cef8cc7b83725)#define BT\_LE\_ADV\_CONN\_DIR(\_peer) BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE | \

894 BT\_LE\_ADV\_OPT\_ONE\_TIME, 0, 0,\

895 \_peer)

896

897

[ 898](group__bt__gap.md#gad490487b9e196526a13fe249a4c25448)#define BT\_LE\_ADV\_CONN BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE, \

899 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

900 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

901

[ 902](group__bt__gap.md#ga7b29dba3d892186897c5b4ca5adfd2e3)#define BT\_LE\_ADV\_CONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE | \

903 BT\_LE\_ADV\_OPT\_USE\_NAME, \

904 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

905 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

906

[ 907](group__bt__gap.md#ga213307090f1debdc783c54faf4a36740)#define BT\_LE\_ADV\_CONN\_NAME\_AD BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE | \

908 BT\_LE\_ADV\_OPT\_USE\_NAME | \

909 BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD, \

910 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

911 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

912

[ 913](group__bt__gap.md#gab89e033ed3fd116c94120d177dfdc839)#define BT\_LE\_ADV\_CONN\_DIR\_LOW\_DUTY(\_peer) \

914 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE | BT\_LE\_ADV\_OPT\_ONE\_TIME | \

915 BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY, \

916 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

917 \_peer)

918

[ 920](group__bt__gap.md#ga1610555bf59f1d691d640f245957fdce)#define BT\_LE\_ADV\_NCONN BT\_LE\_ADV\_PARAM(0, BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

921 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

922

[ 924](group__bt__gap.md#gac1c3c47e3136ce813bb50b00a9387cb4)#define BT\_LE\_ADV\_NCONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_USE\_NAME, \

925 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

926 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

927

[ 929](group__bt__gap.md#ga6ef9fb7a469b03265c7adc99ea19a11b)#define BT\_LE\_ADV\_NCONN\_IDENTITY BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_USE\_IDENTITY, \

930 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

931 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

932 NULL)

933

[ 935](group__bt__gap.md#gac4880197cbe21aad78c4edf10cde95da)#define BT\_LE\_EXT\_ADV\_CONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

936 BT\_LE\_ADV\_OPT\_CONNECTABLE | \

937 BT\_LE\_ADV\_OPT\_USE\_NAME, \

938 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

939 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

940 NULL)

941

[ 943](group__bt__gap.md#ga3e4abd3691e2c6d95acd21b9ca566edd)#define BT\_LE\_EXT\_ADV\_SCAN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

944 BT\_LE\_ADV\_OPT\_SCANNABLE | \

945 BT\_LE\_ADV\_OPT\_USE\_NAME, \

946 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

947 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

948 NULL)

949

[ 951](group__bt__gap.md#gaabc0385f6a5307b48ec43af6aae7dea6)#define BT\_LE\_EXT\_ADV\_NCONN BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV, \

952 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

953 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

954

[ 956](group__bt__gap.md#ga5c79af6787ccda890f485a45c931cdc8)#define BT\_LE\_EXT\_ADV\_NCONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

957 BT\_LE\_ADV\_OPT\_USE\_NAME, \

958 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

959 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

960 NULL)

961

[ 963](group__bt__gap.md#ga7e46a64af0036c433c2e940ce7db0a05)#define BT\_LE\_EXT\_ADV\_NCONN\_IDENTITY \

964 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

965 BT\_LE\_ADV\_OPT\_USE\_IDENTITY, \

966 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

967 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

968

[ 970](group__bt__gap.md#ga0e911d3aafdd0c926590b3272a3da564)#define BT\_LE\_EXT\_ADV\_CODED\_NCONN BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

971 BT\_LE\_ADV\_OPT\_CODED, \

972 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

973 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

974 NULL)

975

[ 979](group__bt__gap.md#ga8c6027f7c0888c577f9b61a65104be05)#define BT\_LE\_EXT\_ADV\_CODED\_NCONN\_NAME \

980 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | BT\_LE\_ADV\_OPT\_CODED | \

981 BT\_LE\_ADV\_OPT\_USE\_NAME, \

982 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

983 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

984

[ 988](group__bt__gap.md#gac67c52693154ebbeedbb31e100513812)#define BT\_LE\_EXT\_ADV\_CODED\_NCONN\_IDENTITY \

989 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | BT\_LE\_ADV\_OPT\_CODED | \

990 BT\_LE\_ADV\_OPT\_USE\_IDENTITY, \

991 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

992 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

993

[ 1000](group__bt__gap.md#gaf0d4c5b05deb5466a0e29c153263b489)#define BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT(\_timeout, \_n\_evts) \

1001{ \

1002 .timeout = (\_timeout), \

1003 .num\_events = (\_n\_evts), \

1004}

1005

[ 1012](group__bt__gap.md#ga9b2cefbcb0a85116cadb68f6d80c6429)#define BT\_LE\_EXT\_ADV\_START\_PARAM(\_timeout, \_n\_evts) \

1013 ((struct bt\_le\_ext\_adv\_start\_param[]) { \

1014 BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT((\_timeout), (\_n\_evts)) \

1015 })

1016

[ 1017](group__bt__gap.md#ga8c83a6f322a479bc24a576a7f091312e)#define BT\_LE\_EXT\_ADV\_START\_DEFAULT BT\_LE\_EXT\_ADV\_START\_PARAM(0, 0)

1018

[ 1026](group__bt__gap.md#ga880567278a81098ae55f52f624c61041)#define BT\_LE\_PER\_ADV\_PARAM\_INIT(\_int\_min, \_int\_max, \_options) \

1027{ \

1028 .interval\_min = (\_int\_min), \

1029 .interval\_max = (\_int\_max), \

1030 .options = (\_options), \

1031}

1032

[ 1040](group__bt__gap.md#gaf46e54f8fcda7b65b659685bb225d243)#define BT\_LE\_PER\_ADV\_PARAM(\_int\_min, \_int\_max, \_options) \

1041 ((struct bt\_le\_per\_adv\_param[]) { \

1042 BT\_LE\_PER\_ADV\_PARAM\_INIT(\_int\_min, \_int\_max, \_options) \

1043 })

1044

[ 1045](group__bt__gap.md#ga8f6a00faaaab2a91ac943c71ed041ac1)#define BT\_LE\_PER\_ADV\_DEFAULT BT\_LE\_PER\_ADV\_PARAM(BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN, \

1046 BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX, \

1047 BT\_LE\_PER\_ADV\_OPT\_NONE)

1048

[ 1079](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02)int [bt\_le\_adv\_start](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02)(const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param,

1080 const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len,

1081 const struct [bt\_data](structbt__data.md) \*sd, size\_t sd\_len);

1082

[ 1095](group__bt__gap.md#ga9a406ebfefac3dd09935a4ae0e317817)int [bt\_le\_adv\_update\_data](group__bt__gap.md#ga9a406ebfefac3dd09935a4ae0e317817)(const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len,

1096 const struct [bt\_data](structbt__data.md) \*sd, size\_t sd\_len);

1097

[ 1105](group__bt__gap.md#ga1776e310b9d80898e6b32d50c4fe0b49)int [bt\_le\_adv\_stop](group__bt__gap.md#ga1776e310b9d80898e6b32d50c4fe0b49)(void);

1106

[ 1121](group__bt__gap.md#gad02b855dd7a26e3910b247fa73f19297)int [bt\_le\_ext\_adv\_create](group__bt__gap.md#gad02b855dd7a26e3910b247fa73f19297)(const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param,

1122 const struct [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md) \*cb,

1123 struct bt\_le\_ext\_adv \*\*adv);

1124

[ 1125](structbt__le__ext__adv__start__param.md)struct [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md) {

[ 1139](structbt__le__ext__adv__start__param.md#a80bb1ef4316dd75ea1268241333f4346) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__ext__adv__start__param.md#a80bb1ef4316dd75ea1268241333f4346);

[ 1146](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_events](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f);

1147};

1148

[ 1162](group__bt__gap.md#gaddc6da5166cd8415d2b367380447eac1)int [bt\_le\_ext\_adv\_start](group__bt__gap.md#gaddc6da5166cd8415d2b367380447eac1)(struct bt\_le\_ext\_adv \*adv,

1163 struct [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md) \*param);

1164

[ 1175](group__bt__gap.md#ga1c864c4b183f9a86c9f70a11471c5b15)int [bt\_le\_ext\_adv\_stop](group__bt__gap.md#ga1c864c4b183f9a86c9f70a11471c5b15)(struct bt\_le\_ext\_adv \*adv);

1176

[ 1211](group__bt__gap.md#gad731f829b3566be3e56485b2a64f80b1)int [bt\_le\_ext\_adv\_set\_data](group__bt__gap.md#gad731f829b3566be3e56485b2a64f80b1)(struct bt\_le\_ext\_adv \*adv,

1212 const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len,

1213 const struct [bt\_data](structbt__data.md) \*sd, size\_t sd\_len);

1214

[ 1231](group__bt__gap.md#ga1aabdb81cb1a1841ff0fb91d849123fc)int [bt\_le\_ext\_adv\_update\_param](group__bt__gap.md#ga1aabdb81cb1a1841ff0fb91d849123fc)(struct bt\_le\_ext\_adv \*adv,

1232 const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param);

1233

[ 1242](group__bt__gap.md#ga62310a27f7fea925dfcf3abd7c454787)int [bt\_le\_ext\_adv\_delete](group__bt__gap.md#ga62310a27f7fea925dfcf3abd7c454787)(struct bt\_le\_ext\_adv \*adv);

1243

[ 1255](group__bt__gap.md#gaeb37d6cdd94a04b4cce8bc1e7aae70b4)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_le\_ext\_adv\_get\_index](group__bt__gap.md#gaeb37d6cdd94a04b4cce8bc1e7aae70b4)(struct bt\_le\_ext\_adv \*adv);

1256

[ 1258](structbt__le__ext__adv__info.md)struct [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md) {

1259 /\* Local identity \*/

[ 1260](structbt__le__ext__adv__info.md#a06aa727cd2523914bc7509713585bffd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__le__ext__adv__info.md#a06aa727cd2523914bc7509713585bffd);

1261

[ 1263](structbt__le__ext__adv__info.md#a485e4a8124fddee897fe744836cbfb24) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__ext__adv__info.md#a485e4a8124fddee897fe744836cbfb24);

1264

[ 1266](structbt__le__ext__adv__info.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__ext__adv__info.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9);

1267};

1268

[ 1277](group__bt__gap.md#gac06c9f55cf1da46e0d64b4d9af984ecb)int [bt\_le\_ext\_adv\_get\_info](group__bt__gap.md#gac06c9f55cf1da46e0d64b4d9af984ecb)(const struct bt\_le\_ext\_adv \*adv,

1278 struct [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md) \*info);

1279

[ 1293](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4)typedef void [bt\_le\_scan\_cb\_t](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) rssi,

1294 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adv\_type, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

1295

[ 1308](group__bt__gap.md#gaa72029a2759123ec776061d2e80bf3a1)int [bt\_le\_per\_adv\_set\_param](group__bt__gap.md#gaa72029a2759123ec776061d2e80bf3a1)(struct bt\_le\_ext\_adv \*adv,

1309 const struct [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md) \*param);

1310

[ 1324](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899)int [bt\_le\_per\_adv\_set\_data](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899)(const struct bt\_le\_ext\_adv \*adv,

1325 const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len);

1326

[ 1327](structbt__le__per__adv__subevent__data__params.md)struct [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md) {

[ 1329](structbt__le__per__adv__subevent__data__params.md#a55f2da6041b538b3bc4bff38cd4d2953) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__le__per__adv__subevent__data__params.md#a55f2da6041b538b3bc4bff38cd4d2953);

1330

[ 1332](structbt__le__per__adv__subevent__data__params.md#a1354e9505239de3c42969138d719d775) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_start](structbt__le__per__adv__subevent__data__params.md#a1354e9505239de3c42969138d719d775);

1333

[ 1335](structbt__le__per__adv__subevent__data__params.md#a86d858606943a82917835a0172e88663) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_count](structbt__le__per__adv__subevent__data__params.md#a86d858606943a82917835a0172e88663);

1336

[ 1338](structbt__le__per__adv__subevent__data__params.md#a46103c988d8ac360b7e26310a0322b4e) const struct [net\_buf\_simple](structnet__buf__simple.md) \*[data](structbt__le__per__adv__subevent__data__params.md#a46103c988d8ac360b7e26310a0322b4e);

1339};

1340

[ 1356](group__bt__gap.md#ga7de30fe5040b85bb9212e3a8fec4ac45)int [bt\_le\_per\_adv\_set\_subevent\_data](group__bt__gap.md#ga7de30fe5040b85bb9212e3a8fec4ac45)(const struct bt\_le\_ext\_adv \*adv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents,

1357 const struct [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md) \*params);

1358

[ 1376](group__bt__gap.md#ga0f23f4ed48e8679646f247ea0d687094)int [bt\_le\_per\_adv\_start](group__bt__gap.md#ga0f23f4ed48e8679646f247ea0d687094)(struct bt\_le\_ext\_adv \*adv);

1377

[ 1389](group__bt__gap.md#ga1b15206fc552d597c12af369d48ff7d5)int [bt\_le\_per\_adv\_stop](group__bt__gap.md#ga1b15206fc552d597c12af369d48ff7d5)(struct bt\_le\_ext\_adv \*adv);

1390

[ 1391](structbt__le__per__adv__sync__synced__info.md)struct [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md) {

[ 1393](structbt__le__per__adv__sync__synced__info.md#a7ca99b0596b08d153d3ba5310adab125) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__per__adv__sync__synced__info.md#a7ca99b0596b08d153d3ba5310adab125);

1394

[ 1396](structbt__le__per__adv__sync__synced__info.md#a5489c3038f7fff596316a456fc8d580b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__synced__info.md#a5489c3038f7fff596316a456fc8d580b);

1397

[ 1399](structbt__le__per__adv__sync__synced__info.md#a5304e1826face35c506f3b8f6cad7df2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__per__adv__sync__synced__info.md#a5304e1826face35c506f3b8f6cad7df2);

1400

[ 1402](structbt__le__per__adv__sync__synced__info.md#a8b7709011541e95ceaeac379cc3143bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__le__per__adv__sync__synced__info.md#a8b7709011541e95ceaeac379cc3143bb);

1403

[ 1405](structbt__le__per__adv__sync__synced__info.md#a0dd4b7646da0fadc48e94ff3dc91ef83) bool [recv\_enabled](structbt__le__per__adv__sync__synced__info.md#a0dd4b7646da0fadc48e94ff3dc91ef83);

1406

[ 1412](structbt__le__per__adv__sync__synced__info.md#adee2bdafa86a0c3c1dfb4660e85396a3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__le__per__adv__sync__synced__info.md#adee2bdafa86a0c3c1dfb4660e85396a3);

1413

[ 1420](structbt__le__per__adv__sync__synced__info.md#ada4cda53aa87f29d54f6cd88134efe14) struct bt\_conn \*[conn](structbt__le__per__adv__sync__synced__info.md#ada4cda53aa87f29d54f6cd88134efe14);

1421#if defined(CONFIG\_BT\_PER\_ADV\_SYNC\_RSP)

1423 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents;

1424

1426 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subevent\_interval;

1427

1429 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_delay;

1430

1432 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_spacing;

1433

1434#endif /\* CONFIG\_BT\_PER\_ADV\_SYNC\_RSP \*/

1435};

1436

[ 1437](structbt__le__per__adv__sync__term__info.md)struct [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md) {

[ 1439](structbt__le__per__adv__sync__term__info.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__per__adv__sync__term__info.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc);

1440

[ 1442](structbt__le__per__adv__sync__term__info.md#a7a5f2ecccaf698bad86f10d9a7d16189) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__term__info.md#a7a5f2ecccaf698bad86f10d9a7d16189);

1443

[ 1445](structbt__le__per__adv__sync__term__info.md#a429b8b665eacbfe9db013a571b829bac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__le__per__adv__sync__term__info.md#a429b8b665eacbfe9db013a571b829bac);

1446};

1447

[ 1448](structbt__le__per__adv__sync__recv__info.md)struct [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md) {

[ 1450](structbt__le__per__adv__sync__recv__info.md#a5817bd4fba2c93adebcebe007650b6eb) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__per__adv__sync__recv__info.md#a5817bd4fba2c93adebcebe007650b6eb);

1451

[ 1453](structbt__le__per__adv__sync__recv__info.md#a21b0ca87e46c6897282ebd877e45114e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__recv__info.md#a21b0ca87e46c6897282ebd877e45114e);

1454

[ 1456](structbt__le__per__adv__sync__recv__info.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__per__adv__sync__recv__info.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e);

1457

[ 1459](structbt__le__per__adv__sync__recv__info.md#aa17c9d917469f121448ed4e1db485700) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__le__per__adv__sync__recv__info.md#aa17c9d917469f121448ed4e1db485700);

1460

[ 1462](structbt__le__per__adv__sync__recv__info.md#a1591907e3cb1f4565b9d26c18bccc7d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__le__per__adv__sync__recv__info.md#a1591907e3cb1f4565b9d26c18bccc7d2);

1463#if defined(CONFIG\_BT\_PER\_ADV\_SYNC\_RSP)

1465 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) periodic\_event\_counter;

1466

1468 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subevent;

1469#endif /\* CONFIG\_BT\_PER\_ADV\_SYNC\_RSP \*/

1470};

1471

1472

[ 1473](structbt__le__per__adv__sync__state__info.md)struct [bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md) {

[ 1475](structbt__le__per__adv__sync__state__info.md#a4b0a3b7e36f935e06072304d6b92579f) bool [recv\_enabled](structbt__le__per__adv__sync__state__info.md#a4b0a3b7e36f935e06072304d6b92579f);

1476};

1477

[ 1478](structbt__le__per__adv__sync__cb.md)struct [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md) {

[ 1489](structbt__le__per__adv__sync__cb.md#a815be4343ab589df433a551663c5f4a1) void (\*[synced](structbt__le__per__adv__sync__cb.md#a815be4343ab589df433a551663c5f4a1))(struct bt\_le\_per\_adv\_sync \*sync,

1490 struct [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md) \*info);

1491

[ 1501](structbt__le__per__adv__sync__cb.md#acbd565a39918e5dfe7603a020e73daec) void (\*[term](structbt__le__per__adv__sync__cb.md#acbd565a39918e5dfe7603a020e73daec))(struct bt\_le\_per\_adv\_sync \*sync,

1502 const struct [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md) \*info);

1503

[ 1517](structbt__le__per__adv__sync__cb.md#a5576248e2eaef2afebe606e05e55f05f) void (\*[recv](structbt__le__per__adv__sync__cb.md#a5576248e2eaef2afebe606e05e55f05f))(struct bt\_le\_per\_adv\_sync \*sync,

1518 const struct [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md) \*info,

1519 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

1520

[ 1531](structbt__le__per__adv__sync__cb.md#a656b4802f79d4a472c2367ade144d72e) void (\*[state\_changed](structbt__le__per__adv__sync__cb.md#a656b4802f79d4a472c2367ade144d72e))(struct bt\_le\_per\_adv\_sync \*sync,

1532 const struct [bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md) \*info);

1533

[ 1544](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9) void (\*[biginfo](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9))(struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_iso\_biginfo](structbt__iso__biginfo.md) \*[biginfo](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9));

1545

[ 1553](structbt__le__per__adv__sync__cb.md#ad2dc168696fbd22f7e3a089ac56f62d7) void (\*[cte\_report\_cb](structbt__le__per__adv__sync__cb.md#ad2dc168696fbd22f7e3a089ac56f62d7))(struct bt\_le\_per\_adv\_sync \*sync,

1554 struct [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md) const \*info);

1555

[ 1556](structbt__le__per__adv__sync__cb.md#a1977d27941063773c953a5f1dfa9ca76) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__le__per__adv__sync__cb.md#a1977d27941063773c953a5f1dfa9ca76);

1557};

1558

1560enum {

[ 1562](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaeeef50a544edc104b39e4ef0c9a58d6c) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaeeef50a544edc104b39e4ef0c9a58d6c) = 0,

1563

[ 1570](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae9a88caa6a83da8b1697a6167629bf7e) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae9a88caa6a83da8b1697a6167629bf7e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

1571

[ 1577](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae35a6eb572a2842e4cc2fc3677e19b53) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae35a6eb572a2842e4cc2fc3677e19b53) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

1578

[ 1580](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa9ec2b0c346c2cab7f61c2efcc8e37db2) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa9ec2b0c346c2cab7f61c2efcc8e37db2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

1581

[ 1583](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaaa256e560f013eb74415d817154b8f4e) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaaa256e560f013eb74415d817154b8f4e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

1584

[ 1586](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa99034652a92249e6d04065d68352020b) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa99034652a92249e6d04065d68352020b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

1587

[ 1589](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa0f52e38e513ec7eefcbc5c86c36f002e) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa0f52e38e513ec7eefcbc5c86c36f002e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

1590

[ 1592](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa5c702876d70d5eadc4df6e59d96b8320) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa5c702876d70d5eadc4df6e59d96b8320) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

1593};

1594

[ 1595](structbt__le__per__adv__sync__param.md)struct [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md) {

[ 1602](structbt__le__per__adv__sync__param.md#ac93adedad747f61a771ac5445e486b74) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__le__per__adv__sync__param.md#ac93adedad747f61a771ac5445e486b74);

1603

[ 1610](structbt__le__per__adv__sync__param.md#a70795642ee94dd9e87f0cf251c095e7f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__param.md#a70795642ee94dd9e87f0cf251c095e7f);

1611

[ 1613](structbt__le__per__adv__sync__param.md#a4252f2b3b453c2f9c8fbf8c35a618ff2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__per__adv__sync__param.md#a4252f2b3b453c2f9c8fbf8c35a618ff2);

1614

[ 1622](structbt__le__per__adv__sync__param.md#af9abb65547fb5bfea65f4c22963c7da0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__le__per__adv__sync__param.md#af9abb65547fb5bfea65f4c22963c7da0);

1623

[ 1630](structbt__le__per__adv__sync__param.md#a301cfd3d6e5620d29c021ababe104754) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__per__adv__sync__param.md#a301cfd3d6e5620d29c021ababe104754);

1631};

1632

[ 1644](group__bt__gap.md#ga8d05bd864d98b5b43595eb256e464024)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_le\_per\_adv\_sync\_get\_index](group__bt__gap.md#ga8d05bd864d98b5b43595eb256e464024)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

1645

[ 1658](group__bt__gap.md#ga59532b37412b1b93f81cf5cc1bab0534)struct bt\_le\_per\_adv\_sync \*[bt\_le\_per\_adv\_sync\_lookup\_index](group__bt__gap.md#ga59532b37412b1b93f81cf5cc1bab0534)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index);

1659

[ 1661](structbt__le__per__adv__sync__info.md)struct [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md) {

[ 1663](structbt__le__per__adv__sync__info.md#ac10fc2e2d3ec2160db8c2aac148d18a2) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__le__per__adv__sync__info.md#ac10fc2e2d3ec2160db8c2aac148d18a2);

1664

[ 1666](structbt__le__per__adv__sync__info.md#acc0ef26c38279c9a67f8992005c2e58a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__info.md#acc0ef26c38279c9a67f8992005c2e58a);

1667

[ 1669](structbt__le__per__adv__sync__info.md#a365a0d8577429e4ee96e977071c9a906) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__per__adv__sync__info.md#a365a0d8577429e4ee96e977071c9a906);

1670

[ 1672](structbt__le__per__adv__sync__info.md#a4d9520ea6a803f8fe4f41190f55c26e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__le__per__adv__sync__info.md#a4d9520ea6a803f8fe4f41190f55c26e5);

1673};

1674

[ 1683](group__bt__gap.md#gabfaf265a48dd09ea02d114e2023c14a6)int [bt\_le\_per\_adv\_sync\_get\_info](group__bt__gap.md#gabfaf265a48dd09ea02d114e2023c14a6)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

1684 struct [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md) \*info);

1685

[ 1694](group__bt__gap.md#ga83126917373c0bcaa24964dd1d8bde46)struct bt\_le\_per\_adv\_sync \*[bt\_le\_per\_adv\_sync\_lookup\_addr](group__bt__gap.md#ga83126917373c0bcaa24964dd1d8bde46)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*adv\_addr,

1695 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid);

1696

[ 1713](group__bt__gap.md#ga061bf84b989b2c96ab51d2ca0debb017)int [bt\_le\_per\_adv\_sync\_create](group__bt__gap.md#ga061bf84b989b2c96ab51d2ca0debb017)(const struct [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md) \*param,

1714 struct bt\_le\_per\_adv\_sync \*\*out\_sync);

1715

[ 1732](group__bt__gap.md#gaa0c218ff3c78b26dcfaa726ee30267a6)int [bt\_le\_per\_adv\_sync\_delete](group__bt__gap.md#gaa0c218ff3c78b26dcfaa726ee30267a6)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

1733

[ 1745](group__bt__gap.md#ga0df428314deaa84c7f5680a90c38729a)void [bt\_le\_per\_adv\_sync\_cb\_register](group__bt__gap.md#ga0df428314deaa84c7f5680a90c38729a)(struct [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md) \*cb);

1746

[ 1756](group__bt__gap.md#ga07e4510de7e72c6ed6196b3da9fb40be)int [bt\_le\_per\_adv\_sync\_recv\_enable](group__bt__gap.md#ga07e4510de7e72c6ed6196b3da9fb40be)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

1757

[ 1767](group__bt__gap.md#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)int [bt\_le\_per\_adv\_sync\_recv\_disable](group__bt__gap.md#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

1768

1770enum {

[ 1772](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aef90aceabc3f9d0b17b7f3415152fca2) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aef90aceabc3f9d0b17b7f3415152fca2) = 0,

1773

[ 1779](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a2694870b7ebd2dcd0b3834367f7d7061) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a2694870b7ebd2dcd0b3834367f7d7061) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

1780

[ 1787](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ab0725048806858083be9ab3fcd9a36ed) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ab0725048806858083be9ab3fcd9a36ed) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

1788

[ 1795](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a433ae469b27e820fdfd2a1d562010991) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a433ae469b27e820fdfd2a1d562010991) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

1796

[ 1798](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aed2f78d682b5fbd1adf89c2f005e4f48) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aed2f78d682b5fbd1adf89c2f005e4f48) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

1799

[ 1806](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a3f0be549ca5cac1cfbdec2f2227e73dc) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a3f0be549ca5cac1cfbdec2f2227e73dc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

1807

[ 1814](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ad924f620ed6fdadbbea03f8e343b9d0c) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ad924f620ed6fdadbbea03f8e343b9d0c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

1815};

1816

[ 1817](structbt__le__per__adv__sync__transfer__param.md)struct [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md) {

[ 1824](structbt__le__per__adv__sync__transfer__param.md#a840e7cfac3a2947e5128d704067aaf7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__le__per__adv__sync__transfer__param.md#a840e7cfac3a2947e5128d704067aaf7e);

1825

[ 1832](structbt__le__per__adv__sync__transfer__param.md#a5bfa84c6bdacdf8893a0951a5ce71fc6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__per__adv__sync__transfer__param.md#a5bfa84c6bdacdf8893a0951a5ce71fc6);

1833

[ 1835](structbt__le__per__adv__sync__transfer__param.md#a0b3ee6df1b409e64a064ffb6ac632cce) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__per__adv__sync__transfer__param.md#a0b3ee6df1b409e64a064ffb6ac632cce);

1836};

1837

[ 1850](group__bt__gap.md#gaf81a1dd7a628d1a2f25c6b53b0679809)int [bt\_le\_per\_adv\_sync\_transfer](group__bt__gap.md#gaf81a1dd7a628d1a2f25c6b53b0679809)(const struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

1851 const struct bt\_conn \*conn,

1852 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) service\_data);

1853

1854

[ 1867](group__bt__gap.md#gac96199a4e5e6cfb789c1bd1c0e67d6fe)int [bt\_le\_per\_adv\_set\_info\_transfer](group__bt__gap.md#gac96199a4e5e6cfb789c1bd1c0e67d6fe)(const struct bt\_le\_ext\_adv \*adv,

1868 const struct bt\_conn \*conn,

1869 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) service\_data);

1870

[ 1884](group__bt__gap.md#gaa0658bd53df1d5e8e89e13330e4fd0ae)int [bt\_le\_per\_adv\_sync\_transfer\_subscribe](group__bt__gap.md#gaa0658bd53df1d5e8e89e13330e4fd0ae)(

1885 const struct bt\_conn \*conn,

1886 const struct [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md) \*param);

1887

[ 1901](group__bt__gap.md#ga08f872078045bbef4aca19761f25eeb8)int [bt\_le\_per\_adv\_sync\_transfer\_unsubscribe](group__bt__gap.md#ga08f872078045bbef4aca19761f25eeb8)(const struct bt\_conn \*conn);

1902

[ 1916](group__bt__gap.md#ga27c4961f3c7270a7f1caeadb4107854b)int [bt\_le\_per\_adv\_list\_add](group__bt__gap.md#ga27c4961f3c7270a7f1caeadb4107854b)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid);

1917

[ 1929](group__bt__gap.md#ga100efac4a49984e06202c63c4e5955cd)int [bt\_le\_per\_adv\_list\_remove](group__bt__gap.md#ga100efac4a49984e06202c63c4e5955cd)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid);

1930

[ 1938](group__bt__gap.md#ga5909bd768c23a19a42a660e3b814c981)int [bt\_le\_per\_adv\_list\_clear](group__bt__gap.md#ga5909bd768c23a19a42a660e3b814c981)(void);

1939

1940

1941enum {

[ 1943](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3aad3f19e5849b6d6813fa88257082e185) [BT\_LE\_SCAN\_OPT\_NONE](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3aad3f19e5849b6d6813fa88257082e185) = 0,

1944

[ 1946](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394) [BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

1947

[ 1949](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae) [BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

1950

[ 1952](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb) [BT\_LE\_SCAN\_OPT\_CODED](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

1953

[ 1959](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a7ff0c79b2675e7b7512379e2cbedc0a6) [BT\_LE\_SCAN\_OPT\_NO\_1M](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a7ff0c79b2675e7b7512379e2cbedc0a6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

1960};

1961

[ 1962](group__bt__gap.md#ga33e84f4ccbf4d0aa2527e9fe1086e252)#define BT\_LE\_SCAN\_OPT\_FILTER\_WHITELIST \_\_DEPRECATED\_MACRO BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST

1963

1964enum {

[ 1966](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006) [BT\_LE\_SCAN\_TYPE\_PASSIVE](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006) = 0x00,

1967

[ 1975](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22) [BT\_LE\_SCAN\_TYPE\_ACTIVE](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22) = 0x01,

1976};

1977

[ 1979](structbt__le__scan__param.md)struct [bt\_le\_scan\_param](structbt__le__scan__param.md) {

[ 1981](structbt__le__scan__param.md#a02d75322390287c3fa754bf915660d0c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__le__scan__param.md#a02d75322390287c3fa754bf915660d0c);

1982

[ 1984](structbt__le__scan__param.md#ac702ecbd938b9a73156a0c6fcf603812) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__scan__param.md#ac702ecbd938b9a73156a0c6fcf603812);

1985

[ 1987](structbt__le__scan__param.md#a2f4e053d97c62b6fdf42a245908607f8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__scan__param.md#a2f4e053d97c62b6fdf42a245908607f8);

1988

[ 1990](structbt__le__scan__param.md#a37a7ee82e86a91cf7a9c2adf60bb526a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window](structbt__le__scan__param.md#a37a7ee82e86a91cf7a9c2adf60bb526a);

1991

[ 1998](structbt__le__scan__param.md#a3e71ce551dcc7762c29e2316996e2912) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__scan__param.md#a3e71ce551dcc7762c29e2316996e2912);

1999

[ 2005](structbt__le__scan__param.md#a67a20bc94a3d98fa10af7b5b42dde328) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_coded](structbt__le__scan__param.md#a67a20bc94a3d98fa10af7b5b42dde328);

2006

[ 2012](structbt__le__scan__param.md#a93166af55dca71393c60cb3f7ac6d809) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window\_coded](structbt__le__scan__param.md#a93166af55dca71393c60cb3f7ac6d809);

2013};

2014

[ 2016](structbt__le__scan__recv__info.md)struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) {

[ 2023](structbt__le__scan__recv__info.md#a907fb7ec3c78d68da5015a8c3afc3084) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__scan__recv__info.md#a907fb7ec3c78d68da5015a8c3afc3084);

2024

[ 2026](structbt__le__scan__recv__info.md#a4df8d4e1fdd7514d170744856ebe7015) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__scan__recv__info.md#a4df8d4e1fdd7514d170744856ebe7015);

2027

[ 2029](structbt__le__scan__recv__info.md#a88f677733147245ccbf861c7fc5e0f11) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__le__scan__recv__info.md#a88f677733147245ccbf861c7fc5e0f11);

2030

[ 2032](structbt__le__scan__recv__info.md#a2addeba6d2ec8e55dc5379adf6519148) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__scan__recv__info.md#a2addeba6d2ec8e55dc5379adf6519148);

2033

[ 2042](structbt__le__scan__recv__info.md#adccb2ce5c6d228bd7f8f050088629524) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_type](structbt__le__scan__recv__info.md#adccb2ce5c6d228bd7f8f050088629524);

2043

[ 2052](structbt__le__scan__recv__info.md#af29ddfb59e286af9ca465cbd5a91bf2d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [adv\_props](structbt__le__scan__recv__info.md#af29ddfb59e286af9ca465cbd5a91bf2d);

2053

[ 2059](structbt__le__scan__recv__info.md#a1060c5937708ff81a64f068e02fc7826) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__scan__recv__info.md#a1060c5937708ff81a64f068e02fc7826);

2060

[ 2062](structbt__le__scan__recv__info.md#a6189ed8453cb7907f34dc7dfaf1343bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [primary\_phy](structbt__le__scan__recv__info.md#a6189ed8453cb7907f34dc7dfaf1343bd);

2063

[ 2065](structbt__le__scan__recv__info.md#ac797291291dc7ba7ac171ed7f24f0d16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [secondary\_phy](structbt__le__scan__recv__info.md#ac797291291dc7ba7ac171ed7f24f0d16);

2066};

2067

[ 2069](structbt__le__scan__cb.md)struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) {

2070

[ 2077](structbt__le__scan__cb.md#a71d73c1da28d4a27626f77d96a5b3541) void (\*[recv](structbt__le__scan__cb.md#a71d73c1da28d4a27626f77d96a5b3541))(const struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) \*info,

2078 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

2079

[ 2081](structbt__le__scan__cb.md#a2f57f3fee46bd137065f4c57d0cd5157) void (\*[timeout](structbt__le__scan__cb.md#a2f57f3fee46bd137065f4c57d0cd5157))(void);

2082

[ 2083](structbt__le__scan__cb.md#a50dbc5e7618fd488e9acb7ad8f104a63) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__le__scan__cb.md#a50dbc5e7618fd488e9acb7ad8f104a63);

2084};

2085

[ 2095](group__bt__gap.md#gac9f372ca16afb1c2f0e100c5b1b94cd5)#define BT\_LE\_SCAN\_PARAM\_INIT(\_type, \_options, \_interval, \_window) \

2096{ \

2097 .type = (\_type), \

2098 .options = (\_options), \

2099 .interval = (\_interval), \

2100 .window = (\_window), \

2101 .timeout = 0, \

2102 .interval\_coded = 0, \

2103 .window\_coded = 0, \

2104}

2105

[ 2115](group__bt__gap.md#ga57ace75133343ba8de7fa965f452ee3d)#define BT\_LE\_SCAN\_PARAM(\_type, \_options, \_interval, \_window) \

2116 ((struct bt\_le\_scan\_param[]) { \

2117 BT\_LE\_SCAN\_PARAM\_INIT(\_type, \_options, \_interval, \_window) \

2118 })

2119

[ 2123](group__bt__gap.md#gac137ea4ce32697582a337116ffa41da5)#define BT\_LE\_SCAN\_ACTIVE BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_ACTIVE, \

2124 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2125 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2126 BT\_GAP\_SCAN\_FAST\_WINDOW)

2127

[ 2134](group__bt__gap.md#ga8ceaef6f0fbf4fe2d76d47e8f59aeb11)#define BT\_LE\_SCAN\_PASSIVE BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_PASSIVE, \

2135 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2136 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2137 BT\_GAP\_SCAN\_FAST\_WINDOW)

2138

[ 2143](group__bt__gap.md#ga06380c4ae6289c704a143b9d192bc35f)#define BT\_LE\_SCAN\_CODED\_ACTIVE \

2144 BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_ACTIVE, \

2145 BT\_LE\_SCAN\_OPT\_CODED | \

2146 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2147 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2148 BT\_GAP\_SCAN\_FAST\_WINDOW)

2149

[ 2157](group__bt__gap.md#ga1e5a4589304babc6b0d49019ebcff6b0)#define BT\_LE\_SCAN\_CODED\_PASSIVE \

2158 BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_PASSIVE, \

2159 BT\_LE\_SCAN\_OPT\_CODED | \

2160 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2161 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2162 BT\_GAP\_SCAN\_FAST\_WINDOW)

2163

[ 2184](group__bt__gap.md#gac5e19c26b53a08dadb8efa7ecc692ad6)int [bt\_le\_scan\_start](group__bt__gap.md#gac5e19c26b53a08dadb8efa7ecc692ad6)(const struct [bt\_le\_scan\_param](structbt__le__scan__param.md) \*param, [bt\_le\_scan\_cb\_t](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4) cb);

2185

[ 2194](group__bt__gap.md#gaa2de1a1ab523606b36a4c445fb0c3b84)int [bt\_le\_scan\_stop](group__bt__gap.md#gaa2de1a1ab523606b36a4c445fb0c3b84)(void);

2195

[ 2207](group__bt__gap.md#gad7c2f18de7f67b73ccc0e7813f48f096)void [bt\_le\_scan\_cb\_register](group__bt__gap.md#gad7c2f18de7f67b73ccc0e7813f48f096)(struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \*cb);

2208

[ 2216](group__bt__gap.md#gac2718f2128b3f8c79b12d760771c8378)void [bt\_le\_scan\_cb\_unregister](group__bt__gap.md#gac2718f2128b3f8c79b12d760771c8378)(struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \*cb);

2217

[ 2232](group__bt__gap.md#ga40f2f7fdb09aba3c5137f680e67792f0)int [bt\_le\_filter\_accept\_list\_add](group__bt__gap.md#ga40f2f7fdb09aba3c5137f680e67792f0)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

2233\_\_deprecated

[ 2234](group__bt__gap.md#ga1423cb91b0e9e7633bf9a3e7aa73d730)static inline int [bt\_le\_whitelist\_add](group__bt__gap.md#ga1423cb91b0e9e7633bf9a3e7aa73d730)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr)

2235{

2236 return [bt\_le\_filter\_accept\_list\_add](group__bt__gap.md#ga40f2f7fdb09aba3c5137f680e67792f0)(addr);

2237}

2238

[ 2253](group__bt__gap.md#ga0532ed768ab4f9d69c202066d2f87e66)int [bt\_le\_filter\_accept\_list\_remove](group__bt__gap.md#ga0532ed768ab4f9d69c202066d2f87e66)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

2254\_\_deprecated

[ 2255](group__bt__gap.md#ga0f3bbbfca7dc10003258d9b0a051e653)static inline int [bt\_le\_whitelist\_rem](group__bt__gap.md#ga0f3bbbfca7dc10003258d9b0a051e653)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr)

2256{

2257 return [bt\_le\_filter\_accept\_list\_remove](group__bt__gap.md#ga0532ed768ab4f9d69c202066d2f87e66)(addr);

2258}

2259

[ 2272](group__bt__gap.md#gac87df899d1e363c63162988157ee6d00)int [bt\_le\_filter\_accept\_list\_clear](group__bt__gap.md#gac87df899d1e363c63162988157ee6d00)(void);

2273\_\_deprecated

[ 2274](group__bt__gap.md#ga1e80196fbf29a539cdf5c21fbc96cfef)static inline int [bt\_le\_whitelist\_clear](group__bt__gap.md#ga1e80196fbf29a539cdf5c21fbc96cfef)(void)

2275{

2276 return [bt\_le\_filter\_accept\_list\_clear](group__bt__gap.md#gac87df899d1e363c63162988157ee6d00)();

2277}

2278

[ 2287](group__bt__gap.md#gabc115fd3fff6d00ae878a31613bf70aa)int [bt\_le\_set\_chan\_map](group__bt__gap.md#gabc115fd3fff6d00ae878a31613bf70aa)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_map[5]);

2288

[ 2307](group__bt__gap.md#ga9ab41e118b5496c196e56b8b5d023275)int [bt\_le\_set\_rpa\_timeout](group__bt__gap.md#ga9ab41e118b5496c196e56b8b5d023275)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) new\_rpa\_timeout);

2308

[ 2326](group__bt__gap.md#ga652eef01e5256e0d820cd1f4db877429)void [bt\_data\_parse](group__bt__gap.md#ga652eef01e5256e0d820cd1f4db877429)(struct [net\_buf\_simple](structnet__buf__simple.md) \*ad,

2327 bool (\*func)(struct [bt\_data](structbt__data.md) \*[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1), void \*user\_data),

2328 void \*user\_data);

2329

[ 2331](structbt__le__oob__sc__data.md)struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) {

[ 2333](structbt__le__oob__sc__data.md#afa64bcc048d0e8709e262e2848a39d2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [r](structbt__le__oob__sc__data.md#afa64bcc048d0e8709e262e2848a39d2c)[16];

2334

[ 2336](structbt__le__oob__sc__data.md#a9bd93f1e9e41e241d0f84ae16ae47ba1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c](structbt__le__oob__sc__data.md#a9bd93f1e9e41e241d0f84ae16ae47ba1)[16];

2337};

2338

[ 2340](structbt__le__oob.md)struct [bt\_le\_oob](structbt__le__oob.md) {

[ 2344](structbt__le__oob.md#a17cfed7683efbf5b5954847d655d7424) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__le__oob.md#a17cfed7683efbf5b5954847d655d7424);

2345

[ 2347](structbt__le__oob.md#a80ccd4ab120a880adfff9aba3b19b4fd) struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) [le\_sc\_data](structbt__le__oob.md#a80ccd4ab120a880adfff9aba3b19b4fd);

2348};

2349

[ 2378](group__bt__gap.md#ga296d1adf3c9ed2f2c65bb75b887d59ee)int [bt\_le\_oob\_get\_local](group__bt__gap.md#ga296d1adf3c9ed2f2c65bb75b887d59ee)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, struct [bt\_le\_oob](structbt__le__oob.md) \*oob);

2379

[ 2404](group__bt__gap.md#ga7486aab863ca497a50dacf81657f48d4)int [bt\_le\_ext\_adv\_oob\_get\_local](group__bt__gap.md#ga7486aab863ca497a50dacf81657f48d4)(struct bt\_le\_ext\_adv \*adv,

2405 struct [bt\_le\_oob](structbt__le__oob.md) \*oob);

2406

[ 2408](structbt__br__discovery__result.md)struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) {

2410 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_priv[4];

2411

[ 2413](structbt__br__discovery__result.md#a833b05883132a0c20690f71b2c14a62a) [bt\_addr\_t](structbt__addr__t.md) [addr](structbt__br__discovery__result.md#a833b05883132a0c20690f71b2c14a62a);

2414

[ 2416](structbt__br__discovery__result.md#ad1f6bbfc27796e998ed30e307a251841) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__br__discovery__result.md#ad1f6bbfc27796e998ed30e307a251841);

2417

[ 2419](structbt__br__discovery__result.md#aec239cbb82436ace39c8928a3baa0cf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cod](structbt__br__discovery__result.md#aec239cbb82436ace39c8928a3baa0cf6)[3];

2420

[ 2422](structbt__br__discovery__result.md#a6bfe9a421257e2460eb9b4381252f9cc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [eir](structbt__br__discovery__result.md#a6bfe9a421257e2460eb9b4381252f9cc)[240];

2423};

2424

[ 2437](group__bt__gap.md#ga4606f9a083b5c333d8c1dc92b759333a)typedef void [bt\_br\_discovery\_cb\_t](group__bt__gap.md#ga4606f9a083b5c333d8c1dc92b759333a)(struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*results,

2438 size\_t count);

2439

[ 2441](structbt__br__discovery__param.md)struct [bt\_br\_discovery\_param](structbt__br__discovery__param.md) {

[ 2445](structbt__br__discovery__param.md#a3087af0c5a264d50a27395d974f99e1e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [length](structbt__br__discovery__param.md#a3087af0c5a264d50a27395d974f99e1e);

2446

[ 2448](structbt__br__discovery__param.md#ac02d03f8cfdf4ad7aee3178e871cc105) bool [limited](structbt__br__discovery__param.md#ac02d03f8cfdf4ad7aee3178e871cc105);

2449};

2450

[ 2468](group__bt__gap.md#gaf7efa6302cde58a10efaf0b68f5cb3c6)int [bt\_br\_discovery\_start](group__bt__gap.md#gaf7efa6302cde58a10efaf0b68f5cb3c6)(const struct [bt\_br\_discovery\_param](structbt__br__discovery__param.md) \*param,

2469 struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*results, size\_t count,

2470 [bt\_br\_discovery\_cb\_t](group__bt__gap.md#ga4606f9a083b5c333d8c1dc92b759333a) cb);

2471

[ 2481](group__bt__gap.md#ga567c71b49399fe7e1a5593edbf005e3a)int [bt\_br\_discovery\_stop](group__bt__gap.md#ga567c71b49399fe7e1a5593edbf005e3a)(void);

2482

[ 2483](structbt__br__oob.md)struct [bt\_br\_oob](structbt__br__oob.md) {

[ 2485](structbt__br__oob.md#a9b9f4c830a4e48736ac6b793d628ee98) [bt\_addr\_t](structbt__addr__t.md) [addr](structbt__br__oob.md#a9b9f4c830a4e48736ac6b793d628ee98);

2486};

2487

[ 2496](group__bt__gap.md#ga2ec860d06c45098624b106b59fbab634)int [bt\_br\_oob\_get\_local](group__bt__gap.md#ga2ec860d06c45098624b106b59fbab634)(struct [bt\_br\_oob](structbt__br__oob.md) \*oob);

2497

2498

[ 2511](group__bt__gap.md#gad3b9075cc9bab5c1ae37514a6dfe555c)int [bt\_br\_set\_discoverable](group__bt__gap.md#gad3b9075cc9bab5c1ae37514a6dfe555c)(bool enable);

2512

[ 2525](group__bt__gap.md#ga80aed18a099948bef8f3649ad537e541)int [bt\_br\_set\_connectable](group__bt__gap.md#ga80aed18a099948bef8f3649ad537e541)(bool enable);

2526

[ 2536](group__bt__gap.md#gaceabbbe6e844650f791010e53c9df6a4)int [bt\_unpair](group__bt__gap.md#gaceabbbe6e844650f791010e53c9df6a4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

2537

[ 2539](structbt__bond__info.md)struct [bt\_bond\_info](structbt__bond__info.md) {

[ 2541](structbt__bond__info.md#a6b328ce30fd53bb73ecd8e033bb91d1f) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__bond__info.md#a6b328ce30fd53bb73ecd8e033bb91d1f);

2542};

2543

[ 2551](group__bt__gap.md#gaad380b7f8984f8522c1b79f9bdc04905)void [bt\_foreach\_bond](group__bt__gap.md#gaad380b7f8984f8522c1b79f9bdc04905)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, void (\*func)(const struct [bt\_bond\_info](structbt__bond__info.md) \*info,

2552 void \*user\_data),

2553 void \*user\_data);

2554

[ 2569](group__bt__gap.md#ga8046c2b06d3dad0d6c8184de492517d2)int [bt\_configure\_data\_path](group__bt__gap.md#ga8046c2b06d3dad0d6c8184de492517d2)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dir, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vs\_config\_len,

2570 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vs\_config);

2571

[ 2572](structbt__le__per__adv__sync__subevent__params.md)struct [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md) {

[ 2578](structbt__le__per__adv__sync__subevent__params.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [properties](structbt__le__per__adv__sync__subevent__params.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4);

2579

[ 2581](structbt__le__per__adv__sync__subevent__params.md#a867c66bf09461a4369da3d250701d2ae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__le__per__adv__sync__subevent__params.md#a867c66bf09461a4369da3d250701d2ae);

2582

[ 2588](structbt__le__per__adv__sync__subevent__params.md#a5ac4e81ddd63797f921105748344c125) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[subevents](structbt__le__per__adv__sync__subevent__params.md#a5ac4e81ddd63797f921105748344c125);

2589};

2590

[ 2601](group__bt__gap.md#ga731f4b37a9e5cc13a6816ea23f751b0b)int [bt\_le\_per\_adv\_sync\_subevent](group__bt__gap.md#ga731f4b37a9e5cc13a6816ea23f751b0b)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

2602 struct [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md) \*params);

2603

[ 2604](structbt__le__per__adv__response__params.md)struct [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md) {

[ 2613](structbt__le__per__adv__response__params.md#a1af01d0a027fb8659615874acbd388f9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [request\_event](structbt__le__per__adv__response__params.md#a1af01d0a027fb8659615874acbd388f9);

2614

[ 2620](structbt__le__per__adv__response__params.md#a3fc8ab0feb06714b28d22439cce60e41) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [request\_subevent](structbt__le__per__adv__response__params.md#a3fc8ab0feb06714b28d22439cce60e41);

2621

[ 2623](structbt__le__per__adv__response__params.md#a0cec222d5ba8cc9e20939d441646c913) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_subevent](structbt__le__per__adv__response__params.md#a0cec222d5ba8cc9e20939d441646c913);

2624

[ 2626](structbt__le__per__adv__response__params.md#aea0428083ccd5f4dccc17e494f38b7c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot](structbt__le__per__adv__response__params.md#aea0428083ccd5f4dccc17e494f38b7c3);

2627};

2628

[ 2641](group__bt__gap.md#gaae6b8583f7d5457f20b03dccd146425e)int [bt\_le\_per\_adv\_set\_response\_data](group__bt__gap.md#gaae6b8583f7d5457f20b03dccd146425e)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

2642 const struct [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md) \*params,

2643 const struct [net\_buf\_simple](structnet__buf__simple.md) \*data);

2644

2648

2649#ifdef \_\_cplusplus

2650}

2651#endif

2655

2656#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_BLUETOOTH\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[crypto.h](bluetooth_2crypto_8h.md)

Bluetooth subsystem crypto APIs.

[gap.h](gap_8h.md)

Bluetooth Generic Access Profile defines and Assigned Numbers.

[bt\_le\_filter\_accept\_list\_remove](group__bt__gap.md#ga0532ed768ab4f9d69c202066d2f87e66)

int bt\_le\_filter\_accept\_list\_remove(const bt\_addr\_le\_t \*addr)

Remove device (LE) from filter accept list.

[bt\_le\_per\_adv\_sync\_create](group__bt__gap.md#ga061bf84b989b2c96ab51d2ca0debb017)

int bt\_le\_per\_adv\_sync\_create(const struct bt\_le\_per\_adv\_sync\_param \*param, struct bt\_le\_per\_adv\_sync \*\*out\_sync)

Create a periodic advertising sync object.

[bt\_id\_get](group__bt__gap.md#ga06d0ae35cbf4382679cc3cfe612cee4d)

void bt\_id\_get(bt\_addr\_le\_t \*addrs, size\_t \*count)

Get the currently configured identities.

[bt\_le\_per\_adv\_sync\_recv\_enable](group__bt__gap.md#ga07e4510de7e72c6ed6196b3da9fb40be)

int bt\_le\_per\_adv\_sync\_recv\_enable(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync)

Enables receiving periodic advertising reports for a sync.

[bt\_le\_per\_adv\_sync\_transfer\_unsubscribe](group__bt__gap.md#ga08f872078045bbef4aca19761f25eeb8)

int bt\_le\_per\_adv\_sync\_transfer\_unsubscribe(const struct bt\_conn \*conn)

Unsubscribe from periodic advertising sync transfers (PASTs).

[bt\_disable](group__bt__gap.md#ga0a58e5a050170e84a80f8d5bb3516ec7)

int bt\_disable(void)

Disable Bluetooth.

[bt\_le\_per\_adv\_sync\_cb\_register](group__bt__gap.md#ga0df428314deaa84c7f5680a90c38729a)

void bt\_le\_per\_adv\_sync\_cb\_register(struct bt\_le\_per\_adv\_sync\_cb \*cb)

Register periodic advertising sync callbacks.

[bt\_le\_per\_adv\_start](group__bt__gap.md#ga0f23f4ed48e8679646f247ea0d687094)

int bt\_le\_per\_adv\_start(struct bt\_le\_ext\_adv \*adv)

Starts periodic advertising.

[bt\_le\_whitelist\_rem](group__bt__gap.md#ga0f3bbbfca7dc10003258d9b0a051e653)

static int bt\_le\_whitelist\_rem(const bt\_addr\_le\_t \*addr)

**Definition** bluetooth.h:2255

[bt\_le\_per\_adv\_list\_remove](group__bt__gap.md#ga100efac4a49984e06202c63c4e5955cd)

int bt\_le\_per\_adv\_list\_remove(const bt\_addr\_le\_t \*addr, uint8\_t sid)

Remove a device from the periodic advertising list.

[bt\_le\_whitelist\_add](group__bt__gap.md#ga1423cb91b0e9e7633bf9a3e7aa73d730)

static int bt\_le\_whitelist\_add(const bt\_addr\_le\_t \*addr)

**Definition** bluetooth.h:2234

[bt\_le\_adv\_stop](group__bt__gap.md#ga1776e310b9d80898e6b32d50c4fe0b49)

int bt\_le\_adv\_stop(void)

Stop advertising.

[bt\_le\_ext\_adv\_update\_param](group__bt__gap.md#ga1aabdb81cb1a1841ff0fb91d849123fc)

int bt\_le\_ext\_adv\_update\_param(struct bt\_le\_ext\_adv \*adv, const struct bt\_le\_adv\_param \*param)

Update advertising parameters.

[bt\_le\_per\_adv\_stop](group__bt__gap.md#ga1b15206fc552d597c12af369d48ff7d5)

int bt\_le\_per\_adv\_stop(struct bt\_le\_ext\_adv \*adv)

Stops periodic advertising.

[bt\_le\_scan\_cb\_t](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4)

void bt\_le\_scan\_cb\_t(const bt\_addr\_le\_t \*addr, int8\_t rssi, uint8\_t adv\_type, struct net\_buf\_simple \*buf)

Callback type for reporting LE scan results.

**Definition** bluetooth.h:1293

[bt\_le\_ext\_adv\_stop](group__bt__gap.md#ga1c864c4b183f9a86c9f70a11471c5b15)

int bt\_le\_ext\_adv\_stop(struct bt\_le\_ext\_adv \*adv)

Stop advertising with the given advertising set.

[bt\_le\_whitelist\_clear](group__bt__gap.md#ga1e80196fbf29a539cdf5c21fbc96cfef)

static int bt\_le\_whitelist\_clear(void)

**Definition** bluetooth.h:2274

[bt\_le\_per\_adv\_list\_add](group__bt__gap.md#ga27c4961f3c7270a7f1caeadb4107854b)

int bt\_le\_per\_adv\_list\_add(const bt\_addr\_le\_t \*addr, uint8\_t sid)

Add a device to the periodic advertising list.

[bt\_le\_oob\_get\_local](group__bt__gap.md#ga296d1adf3c9ed2f2c65bb75b887d59ee)

int bt\_le\_oob\_get\_local(uint8\_t id, struct bt\_le\_oob \*oob)

Get local LE Out of Band (OOB) information.

[bt\_br\_oob\_get\_local](group__bt__gap.md#ga2ec860d06c45098624b106b59fbab634)

int bt\_br\_oob\_get\_local(struct bt\_br\_oob \*oob)

Get BR/EDR local Out Of Band information.

[bt\_get\_appearance](group__bt__gap.md#ga35b76ea7ce79721e47ca4164e08b2dfb)

uint16\_t bt\_get\_appearance(void)

Get local Bluetooth appearance.

[bt\_data\_serialize](group__bt__gap.md#ga3c067b16468ebd17973faeded0fc83c9)

size\_t bt\_data\_serialize(const struct bt\_data \*input, uint8\_t \*output)

Serialize a bt\_data struct into an advertising structure (a flat byte array).

[bt\_data\_get\_len](group__bt__gap.md#ga3d2c6adc42eb9510734630f38d921b9a)

size\_t bt\_data\_get\_len(const struct bt\_data data[], size\_t data\_count)

Get the total size (in bytes) of a given set of bt\_data structures.

[bt\_le\_per\_adv\_sync\_recv\_disable](group__bt__gap.md#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)

int bt\_le\_per\_adv\_sync\_recv\_disable(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync)

Disables receiving periodic advertising reports for a sync.

[bt\_le\_filter\_accept\_list\_add](group__bt__gap.md#ga40f2f7fdb09aba3c5137f680e67792f0)

int bt\_le\_filter\_accept\_list\_add(const bt\_addr\_le\_t \*addr)

Add device (LE) to filter accept list.

[bt\_br\_discovery\_cb\_t](group__bt__gap.md#ga4606f9a083b5c333d8c1dc92b759333a)

void bt\_br\_discovery\_cb\_t(struct bt\_br\_discovery\_result \*results, size\_t count)

Callback type for reporting BR/EDR discovery (inquiry) results.

**Definition** bluetooth.h:2437

[bt\_ready\_cb\_t](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb)

void(\* bt\_ready\_cb\_t)(int err)

Callback for notifying that Bluetooth has been enabled.

**Definition** bluetooth.h:200

[bt\_br\_discovery\_stop](group__bt__gap.md#ga567c71b49399fe7e1a5593edbf005e3a)

int bt\_br\_discovery\_stop(void)

Stop BR/EDR discovery.

[bt\_le\_per\_adv\_list\_clear](group__bt__gap.md#ga5909bd768c23a19a42a660e3b814c981)

int bt\_le\_per\_adv\_list\_clear(void)

Clear the periodic advertising list.

[bt\_le\_per\_adv\_sync\_lookup\_index](group__bt__gap.md#ga59532b37412b1b93f81cf5cc1bab0534)

struct bt\_le\_per\_adv\_sync \* bt\_le\_per\_adv\_sync\_lookup\_index(uint8\_t index)

Get a periodic advertising sync object from the array index.

[bt\_le\_ext\_adv\_delete](group__bt__gap.md#ga62310a27f7fea925dfcf3abd7c454787)

int bt\_le\_ext\_adv\_delete(struct bt\_le\_ext\_adv \*adv)

Delete advertising set.

[bt\_data\_parse](group__bt__gap.md#ga652eef01e5256e0d820cd1f4db877429)

void bt\_data\_parse(struct net\_buf\_simple \*ad, bool(\*func)(struct bt\_data \*data, void \*user\_data), void \*user\_data)

Helper for parsing advertising (or EIR or OOB) data.

[bt\_le\_per\_adv\_sync\_subevent](group__bt__gap.md#ga731f4b37a9e5cc13a6816ea23f751b0b)

int bt\_le\_per\_adv\_sync\_subevent(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, struct bt\_le\_per\_adv\_sync\_subevent\_params \*params)

Synchronize with a subset of subevents.

[bt\_le\_ext\_adv\_oob\_get\_local](group__bt__gap.md#ga7486aab863ca497a50dacf81657f48d4)

int bt\_le\_ext\_adv\_oob\_get\_local(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_oob \*oob)

Get local LE Out of Band (OOB) information.

[bt\_le\_per\_adv\_set\_subevent\_data](group__bt__gap.md#ga7de30fe5040b85bb9212e3a8fec4ac45)

int bt\_le\_per\_adv\_set\_subevent\_data(const struct bt\_le\_ext\_adv \*adv, uint8\_t num\_subevents, const struct bt\_le\_per\_adv\_subevent\_data\_params \*params)

Set the periodic advertising with response subevent data.

[bt\_configure\_data\_path](group__bt__gap.md#ga8046c2b06d3dad0d6c8184de492517d2)

int bt\_configure\_data\_path(uint8\_t dir, uint8\_t id, uint8\_t vs\_config\_len, const uint8\_t \*vs\_config)

Configure vendor data path.

[bt\_br\_set\_connectable](group__bt__gap.md#ga80aed18a099948bef8f3649ad537e541)

int bt\_br\_set\_connectable(bool enable)

Enable/disable set controller in connectable state.

[bt\_le\_per\_adv\_sync\_lookup\_addr](group__bt__gap.md#ga83126917373c0bcaa24964dd1d8bde46)

struct bt\_le\_per\_adv\_sync \* bt\_le\_per\_adv\_sync\_lookup\_addr(const bt\_addr\_le\_t \*adv\_addr, uint8\_t sid)

Look up an existing periodic advertising sync object by advertiser address.

[bt\_le\_per\_adv\_sync\_get\_index](group__bt__gap.md#ga8d05bd864d98b5b43595eb256e464024)

uint8\_t bt\_le\_per\_adv\_sync\_get\_index(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync)

Get array index of an periodic advertising sync object.

[bt\_le\_adv\_update\_data](group__bt__gap.md#ga9a406ebfefac3dd09935a4ae0e317817)

int bt\_le\_adv\_update\_data(const struct bt\_data \*ad, size\_t ad\_len, const struct bt\_data \*sd, size\_t sd\_len)

Update advertising.

[bt\_le\_set\_rpa\_timeout](group__bt__gap.md#ga9ab41e118b5496c196e56b8b5d023275)

int bt\_le\_set\_rpa\_timeout(uint16\_t new\_rpa\_timeout)

Set the Resolvable Private Address timeout in runtime.

[bt\_le\_per\_adv\_sync\_transfer\_subscribe](group__bt__gap.md#gaa0658bd53df1d5e8e89e13330e4fd0ae)

int bt\_le\_per\_adv\_sync\_transfer\_subscribe(const struct bt\_conn \*conn, const struct bt\_le\_per\_adv\_sync\_transfer\_param \*param)

Subscribe to periodic advertising sync transfers (PASTs).

[bt\_le\_per\_adv\_sync\_delete](group__bt__gap.md#gaa0c218ff3c78b26dcfaa726ee30267a6)

int bt\_le\_per\_adv\_sync\_delete(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync)

Delete periodic advertising sync.

[bt\_le\_scan\_stop](group__bt__gap.md#gaa2de1a1ab523606b36a4c445fb0c3b84)

int bt\_le\_scan\_stop(void)

Stop (LE) scanning.

[bt\_le\_per\_adv\_set\_param](group__bt__gap.md#gaa72029a2759123ec776061d2e80bf3a1)

int bt\_le\_per\_adv\_set\_param(struct bt\_le\_ext\_adv \*adv, const struct bt\_le\_per\_adv\_param \*param)

Set or update the periodic advertising parameters.

[bt\_is\_ready](group__bt__gap.md#gaa8bf6854e7ad1fe7e0805737576e5d1a)

bool bt\_is\_ready(void)

Check if Bluetooth is ready.

[bt\_foreach\_bond](group__bt__gap.md#gaad380b7f8984f8522c1b79f9bdc04905)

void bt\_foreach\_bond(uint8\_t id, void(\*func)(const struct bt\_bond\_info \*info, void \*user\_data), void \*user\_data)

Iterate through all existing bonds.

[bt\_le\_per\_adv\_set\_response\_data](group__bt__gap.md#gaae6b8583f7d5457f20b03dccd146425e)

int bt\_le\_per\_adv\_set\_response\_data(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, const struct bt\_le\_per\_adv\_response\_params \*params, const struct net\_buf\_simple \*data)

Set the data for a response slot in a specific subevent of the PAwR.

[bt\_id\_reset](group__bt__gap.md#gabb3353edc8a3a8d29a0370049b20cbe4)

int bt\_id\_reset(uint8\_t id, bt\_addr\_le\_t \*addr, uint8\_t \*irk)

Reset/reclaim an identity for reuse.

[bt\_le\_set\_chan\_map](group__bt__gap.md#gabc115fd3fff6d00ae878a31613bf70aa)

int bt\_le\_set\_chan\_map(uint8\_t chan\_map[5])

Set (LE) channel map.

[bt\_le\_per\_adv\_sync\_get\_info](group__bt__gap.md#gabfaf265a48dd09ea02d114e2023c14a6)

int bt\_le\_per\_adv\_sync\_get\_info(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, struct bt\_le\_per\_adv\_sync\_info \*info)

Get periodic adv sync information.

[bt\_le\_ext\_adv\_get\_info](group__bt__gap.md#gac06c9f55cf1da46e0d64b4d9af984ecb)

int bt\_le\_ext\_adv\_get\_info(const struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_info \*info)

Get advertising set info.

[bt\_le\_scan\_cb\_unregister](group__bt__gap.md#gac2718f2128b3f8c79b12d760771c8378)

void bt\_le\_scan\_cb\_unregister(struct bt\_le\_scan\_cb \*cb)

Unregister scanner packet callbacks.

[bt\_enable](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b)

int bt\_enable(bt\_ready\_cb\_t cb)

Enable Bluetooth.

[bt\_le\_scan\_start](group__bt__gap.md#gac5e19c26b53a08dadb8efa7ecc692ad6)

int bt\_le\_scan\_start(const struct bt\_le\_scan\_param \*param, bt\_le\_scan\_cb\_t cb)

Start (LE) scanning.

[bt\_le\_filter\_accept\_list\_clear](group__bt__gap.md#gac87df899d1e363c63162988157ee6d00)

int bt\_le\_filter\_accept\_list\_clear(void)

Clear filter accept list.

[bt\_set\_name](group__bt__gap.md#gac8bb3609a3d6da69ff736809e45f5c8a)

int bt\_set\_name(const char \*name)

Set Bluetooth Device Name.

[bt\_le\_per\_adv\_set\_info\_transfer](group__bt__gap.md#gac96199a4e5e6cfb789c1bd1c0e67d6fe)

int bt\_le\_per\_adv\_set\_info\_transfer(const struct bt\_le\_ext\_adv \*adv, const struct bt\_conn \*conn, uint16\_t service\_data)

Transfer the information about a periodic advertising set.

[bt\_unpair](group__bt__gap.md#gaceabbbe6e844650f791010e53c9df6a4)

int bt\_unpair(uint8\_t id, const bt\_addr\_le\_t \*addr)

Clear pairing information.

[bt\_le\_ext\_adv\_create](group__bt__gap.md#gad02b855dd7a26e3910b247fa73f19297)

int bt\_le\_ext\_adv\_create(const struct bt\_le\_adv\_param \*param, const struct bt\_le\_ext\_adv\_cb \*cb, struct bt\_le\_ext\_adv \*\*adv)

Create advertising set.

[bt\_le\_adv\_start](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02)

int bt\_le\_adv\_start(const struct bt\_le\_adv\_param \*param, const struct bt\_data \*ad, size\_t ad\_len, const struct bt\_data \*sd, size\_t sd\_len)

Start advertising.

[bt\_br\_set\_discoverable](group__bt__gap.md#gad3b9075cc9bab5c1ae37514a6dfe555c)

int bt\_br\_set\_discoverable(bool enable)

Enable/disable set controller in discoverable state.

[bt\_le\_ext\_adv\_set\_data](group__bt__gap.md#gad731f829b3566be3e56485b2a64f80b1)

int bt\_le\_ext\_adv\_set\_data(struct bt\_le\_ext\_adv \*adv, const struct bt\_data \*ad, size\_t ad\_len, const struct bt\_data \*sd, size\_t sd\_len)

Set an advertising set's advertising or scan response data.

[bt\_le\_scan\_cb\_register](group__bt__gap.md#gad7c2f18de7f67b73ccc0e7813f48f096)

void bt\_le\_scan\_cb\_register(struct bt\_le\_scan\_cb \*cb)

Register scanner packet callbacks.

[bt\_get\_name](group__bt__gap.md#gad922d894b25e86de3f81ce77200a13fd)

const char \* bt\_get\_name(void)

Get Bluetooth Device Name.

[bt\_le\_ext\_adv\_start](group__bt__gap.md#gaddc6da5166cd8415d2b367380447eac1)

int bt\_le\_ext\_adv\_start(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_start\_param \*param)

Start advertising with the given advertising set.

[bt\_id\_create](group__bt__gap.md#gae11eb8ad254418c38a0e8689df25a159)

int bt\_id\_create(bt\_addr\_le\_t \*addr, uint8\_t \*irk)

Create a new identity.

[bt\_le\_ext\_adv\_get\_index](group__bt__gap.md#gaeb37d6cdd94a04b4cce8bc1e7aae70b4)

uint8\_t bt\_le\_ext\_adv\_get\_index(struct bt\_le\_ext\_adv \*adv)

Get array index of an advertising set.

[bt\_set\_appearance](group__bt__gap.md#gaf0729453790aab1bd3d52c623be3b35a)

int bt\_set\_appearance(uint16\_t new\_appearance)

Set local Bluetooth appearance.

[bt\_id\_delete](group__bt__gap.md#gaf6cd906690a51ebed04bea4f4ef716ff)

int bt\_id\_delete(uint8\_t id)

Delete an identity.

[bt\_br\_discovery\_start](group__bt__gap.md#gaf7efa6302cde58a10efaf0b68f5cb3c6)

int bt\_br\_discovery\_start(const struct bt\_br\_discovery\_param \*param, struct bt\_br\_discovery\_result \*results, size\_t count, bt\_br\_discovery\_cb\_t cb)

Start BR/EDR discovery.

[bt\_le\_per\_adv\_sync\_transfer](group__bt__gap.md#gaf81a1dd7a628d1a2f25c6b53b0679809)

int bt\_le\_per\_adv\_sync\_transfer(const struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, const struct bt\_conn \*conn, uint16\_t service\_data)

Transfer the periodic advertising sync information to a peer device.

[bt\_le\_per\_adv\_set\_data](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899)

int bt\_le\_per\_adv\_set\_data(const struct bt\_le\_ext\_adv \*adv, const struct bt\_data \*ad, size\_t ad\_len)

Set or update the periodic advertising data.

[BT\_LE\_SCAN\_TYPE\_PASSIVE](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006)

@ BT\_LE\_SCAN\_TYPE\_PASSIVE

Scan without requesting additional information from advertisers.

**Definition** bluetooth.h:1966

[BT\_LE\_SCAN\_TYPE\_ACTIVE](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22)

@ BT\_LE\_SCAN\_TYPE\_ACTIVE

Scan and request additional information from advertisers.

**Definition** bluetooth.h:1975

[BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa38cebc2ae885ff630b34c603e2ec6403)

@ BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI

Advertise with included AdvDataInfo (ADI).

**Definition** bluetooth.h:798

[BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa9524537e4cb726f4ff10ba93381bb27f)

@ BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER

Advertise with transmit power.

**Definition** bluetooth.h:791

[BT\_LE\_PER\_ADV\_OPT\_NONE](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aaa2c689d726eacfb18d87655b1f587518)

@ BT\_LE\_PER\_ADV\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:784

[BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394)

@ BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE

Filter duplicates.

**Definition** bluetooth.h:1946

[BT\_LE\_SCAN\_OPT\_CODED](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb)

@ BT\_LE\_SCAN\_OPT\_CODED

Enable scan on coded PHY (Long Range).

**Definition** bluetooth.h:1952

[BT\_LE\_SCAN\_OPT\_NO\_1M](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a7ff0c79b2675e7b7512379e2cbedc0a6)

@ BT\_LE\_SCAN\_OPT\_NO\_1M

Disable scan on 1M phy.

**Definition** bluetooth.h:1959

[BT\_LE\_SCAN\_OPT\_NONE](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3aad3f19e5849b6d6813fa88257082e185)

@ BT\_LE\_SCAN\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:1943

[BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae)

@ BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST

Filter using filter accept list.

**Definition** bluetooth.h:1949

[BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73)

@ BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD

Put GAP device name into advert data.

**Definition** bluetooth.h:695

[BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea1563b053f457833d1a3d11c8dc4d394b)

@ BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ

Notify the application when a scan response data has been sent to an active scanner.

**Definition** bluetooth.h:601

[BT\_LE\_ADV\_OPT\_ANONYMOUS](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea185e0f884f8b0ce79625448638de8fab)

@ BT\_LE\_ADV\_OPT\_ANONYMOUS

Advertise without a device address (identity or RPA).

**Definition** bluetooth.h:669

[BT\_LE\_ADV\_OPT\_USE\_NRPA](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea22958d8539d661ad7ca8d3f1173e7e5e)

@ BT\_LE\_ADV\_OPT\_USE\_NRPA

Advertise using a Non-Resolvable Private Address.

**Definition** bluetooth.h:709

[BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3)

@ BT\_LE\_ADV\_OPT\_CONNECTABLE

Advertise as connectable.

**Definition** bluetooth.h:516

[BT\_LE\_ADV\_OPT\_USE\_NAME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398)

@ BT\_LE\_ADV\_OPT\_USE\_NAME

Advertise using GAP device name.

**Definition** bluetooth.h:566

[BT\_LE\_ADV\_OPT\_USE\_IDENTITY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e)

@ BT\_LE\_ADV\_OPT\_USE\_IDENTITY

Advertise using identity address.

**Definition** bluetooth.h:544

[BT\_LE\_ADV\_OPT\_ONE\_TIME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2)

@ BT\_LE\_ADV\_OPT\_ONE\_TIME

Advertise one time.

**Definition** bluetooth.h:532

[BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea807ba316edc49c8448a8ff7d497173f5)

@ BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ

Use filter accept list to filter devices that can request scan response data.

**Definition** bluetooth.h:593

[BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea89f7494620236c976bf1a76a880e2a28)

@ BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39

Disable advertising on channel index 39.

**Definition** bluetooth.h:685

[BT\_LE\_ADV\_OPT\_NONE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea928b376123819cb0a69fbb5b35608dbf)

@ BT\_LE\_ADV\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:506

[BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeab46741616f8bfe50c4b492d1f7970779)

@ BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37

Disable advertising on channel index 37.

**Definition** bluetooth.h:679

[BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabd9cb02691d7e025fe3fea9a80123275)

@ BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38

Disable advertising on channel index 38.

**Definition** bluetooth.h:682

[BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabdcf1c80662061fa30575e1f9fc6cf6f)

@ BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA

Directed advertising to privacy-enabled peer.

**Definition** bluetooth.h:588

[BT\_LE\_ADV\_OPT\_CODED](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1)

@ BT\_LE\_ADV\_OPT\_CODED

Advertise on the LE Coded PHY (Long Range).

**Definition** bluetooth.h:662

[BT\_LE\_ADV\_OPT\_FILTER\_CONN](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead5efef3d01731110dbd71d5a5dc9baaf)

@ BT\_LE\_ADV\_OPT\_FILTER\_CONN

Use filter accept list to filter devices that can connect.

**Definition** bluetooth.h:596

[BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab)

@ BT\_LE\_ADV\_OPT\_EXT\_ADV

Advertise with extended advertising.

**Definition** bluetooth.h:634

[BT\_LE\_ADV\_OPT\_SCANNABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9)

@ BT\_LE\_ADV\_OPT\_SCANNABLE

Support scan response data.

**Definition** bluetooth.h:612

[BT\_LE\_ADV\_OPT\_NO\_2M](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae864aefcdfbecaffe823b9b144fe0a6b)

@ BT\_LE\_ADV\_OPT\_NO\_2M

Disable use of LE 2M PHY on the secondary advertising channel.

**Definition** bluetooth.h:650

[BT\_LE\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaecff4fe3ac3d1fba3f6fa76c77713859)

@ BT\_LE\_ADV\_OPT\_USE\_TX\_POWER

Advertise with transmit power.

**Definition** bluetooth.h:676

[BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeafd164ec5476f5e2d9aedf50032946872)

@ BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY

Low duty cycle directed advertising.

**Definition** bluetooth.h:574

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a2694870b7ebd2dcd0b3834367f7d7061)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA

No Angle of Arrival (AoA).

**Definition** bluetooth.h:1779

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a3f0be549ca5cac1cfbdec2f2227e73dc)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED

Sync to received PAST packets but don't generate sync reports.

**Definition** bluetooth.h:1806

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a433ae469b27e820fdfd2a1d562010991)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US

No Angle of Departure (AoD) 2.

**Definition** bluetooth.h:1795

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ab0725048806858083be9ab3fcd9a36ed)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US

No Angle of Departure (AoD) 1 us.

**Definition** bluetooth.h:1787

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ad924f620ed6fdadbbea03f8e343b9d0c)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES

Sync to received PAST packets and generate sync reports with duplicate filtering.

**Definition** bluetooth.h:1814

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aed2f78d682b5fbd1adf89c2f005e4f48)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE

Only sync to packets with constant tone extension.

**Definition** bluetooth.h:1798

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aef90aceabc3f9d0b17b7f3415152fca2)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:1772

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa0f52e38e513ec7eefcbc5c86c36f002e)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US

Sync with Angle of Departure (AoD) 2 us constant tone extension.

**Definition** bluetooth.h:1589

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa5c702876d70d5eadc4df6e59d96b8320)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT

Do not sync to packets without a constant tone extension.

**Definition** bluetooth.h:1592

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa99034652a92249e6d04065d68352020b)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US

Sync with Angle of Departure (AoD) 1 us constant tone extension.

**Definition** bluetooth.h:1586

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa9ec2b0c346c2cab7f61c2efcc8e37db2)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE

Filter duplicate Periodic Advertising reports.

**Definition** bluetooth.h:1580

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaaa256e560f013eb74415d817154b8f4e)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA

Sync with Angle of Arrival (AoA) constant tone extension.

**Definition** bluetooth.h:1583

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae35a6eb572a2842e4cc2fc3677e19b53)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED

Disables periodic advertising reports.

**Definition** bluetooth.h:1577

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae9a88caa6a83da8b1697a6167629bf7e)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST

Use the periodic advertising list to sync with advertiser.

**Definition** bluetooth.h:1570

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaeeef50a544edc104b39e4ef0c9a58d6c)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:1562

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[buf.h](net_2buf_8h.md)

Buffer management.

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[string.h](string_8h.md)

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_addr\_t](structbt__addr__t.md)

Bluetooth Device Address.

**Definition** addr.h:40

[bt\_bond\_info](structbt__bond__info.md)

Information about a bond with a remote device.

**Definition** bluetooth.h:2539

[bt\_bond\_info::addr](structbt__bond__info.md#a6b328ce30fd53bb73ecd8e033bb91d1f)

bt\_addr\_le\_t addr

Address of the remote device.

**Definition** bluetooth.h:2541

[bt\_br\_discovery\_param](structbt__br__discovery__param.md)

BR/EDR discovery parameters.

**Definition** bluetooth.h:2441

[bt\_br\_discovery\_param::length](structbt__br__discovery__param.md#a3087af0c5a264d50a27395d974f99e1e)

uint8\_t length

Maximum length of the discovery in units of 1.28 seconds.

**Definition** bluetooth.h:2445

[bt\_br\_discovery\_param::limited](structbt__br__discovery__param.md#ac02d03f8cfdf4ad7aee3178e871cc105)

bool limited

True if limited discovery procedure is to be used.

**Definition** bluetooth.h:2448

[bt\_br\_discovery\_result](structbt__br__discovery__result.md)

BR/EDR discovery result structure.

**Definition** bluetooth.h:2408

[bt\_br\_discovery\_result::eir](structbt__br__discovery__result.md#a6bfe9a421257e2460eb9b4381252f9cc)

uint8\_t eir[240]

Extended Inquiry Response.

**Definition** bluetooth.h:2422

[bt\_br\_discovery\_result::addr](structbt__br__discovery__result.md#a833b05883132a0c20690f71b2c14a62a)

bt\_addr\_t addr

Remote device address.

**Definition** bluetooth.h:2413

[bt\_br\_discovery\_result::rssi](structbt__br__discovery__result.md#ad1f6bbfc27796e998ed30e307a251841)

int8\_t rssi

RSSI from inquiry.

**Definition** bluetooth.h:2416

[bt\_br\_discovery\_result::cod](structbt__br__discovery__result.md#aec239cbb82436ace39c8928a3baa0cf6)

uint8\_t cod[3]

Class of Device.

**Definition** bluetooth.h:2419

[bt\_br\_oob](structbt__br__oob.md)

**Definition** bluetooth.h:2483

[bt\_br\_oob::addr](structbt__br__oob.md#a9b9f4c830a4e48736ac6b793d628ee98)

bt\_addr\_t addr

BR/EDR address.

**Definition** bluetooth.h:2485

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:439

[bt\_data::type](structbt__data.md#a984aecb40a4993ffa113be53942db065)

uint8\_t type

**Definition** bluetooth.h:440

[bt\_data::data\_len](structbt__data.md#abda19091a1b8f99d385f11772ef34d5f)

uint8\_t data\_len

**Definition** bluetooth.h:441

[bt\_data::data](structbt__data.md#ac80ec10101ad69a86f703a4e652c7826)

const uint8\_t \* data

**Definition** bluetooth.h:442

[bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md)

**Definition** direction.h:115

[bt\_iso\_biginfo](structbt__iso__biginfo.md)

Broadcast Isochronous Group (BIG) information.

**Definition** iso.h:563

[bt\_le\_adv\_param](structbt__le__adv__param.md)

LE Advertising Parameters.

**Definition** bluetooth.h:713

[bt\_le\_adv\_param::options](structbt__le__adv__param.md#a2a978c60153eb03697769bc72928f4ef)

uint32\_t options

Bit-field of advertising options.

**Definition** bluetooth.h:742

[bt\_le\_adv\_param::peer](structbt__le__adv__param.md#a4cf31f54f067fffa3c848adc2ffd7119)

const bt\_addr\_le\_t \* peer

Directed advertising to peer.

**Definition** bluetooth.h:777

[bt\_le\_adv\_param::sid](structbt__le__adv__param.md#a6e2f0e1b76495afe7fe661e8698d0909)

uint8\_t sid

Advertising Set Identifier, valid range 0x00 - 0x0f.

**Definition** bluetooth.h:729

[bt\_le\_adv\_param::secondary\_max\_skip](structbt__le__adv__param.md#a9911e9bfc97ff0c48a6decae3f922e95)

uint8\_t secondary\_max\_skip

Secondary channel maximum skip count.

**Definition** bluetooth.h:739

[bt\_le\_adv\_param::interval\_min](structbt__le__adv__param.md#aca8ff5a4f5d29184535162f007b2d39e)

uint32\_t interval\_min

Minimum Advertising Interval (N \* 0.625 milliseconds) Minimum Advertising Interval shall be less than...

**Definition** bluetooth.h:751

[bt\_le\_adv\_param::id](structbt__le__adv__param.md#af957bd92b949536af2b2db0db7b2b425)

uint8\_t id

Local identity.

**Definition** bluetooth.h:722

[bt\_le\_adv\_param::interval\_max](structbt__le__adv__param.md#afeba6973dca99d8ee818fdde0c22cb59)

uint32\_t interval\_max

Maximum Advertising Interval (N \* 0.625 milliseconds) Minimum Advertising Interval shall be less than...

**Definition** bluetooth.h:760

[bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md)

**Definition** bluetooth.h:111

[bt\_le\_ext\_adv\_cb::scanned](structbt__le__ext__adv__cb.md#a277dc3269741d40b644ae3c777198fab)

void(\* scanned)(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_scanned\_info \*info)

The advertising set has sent scan response data.

**Definition** bluetooth.h:148

[bt\_le\_ext\_adv\_cb::connected](structbt__le__ext__adv__cb.md#a7aad0fbd8e531e70f661500c338d870e)

void(\* connected)(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_connected\_info \*info)

The advertising set has accepted a new connection.

**Definition** bluetooth.h:135

[bt\_le\_ext\_adv\_cb::sent](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60)

void(\* sent)(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_sent\_info \*info)

The advertising set has finished sending adv data.

**Definition** bluetooth.h:123

[bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md)

**Definition** bluetooth.h:68

[bt\_le\_ext\_adv\_connected\_info::conn](structbt__le__ext__adv__connected__info.md#a157efa6206b418f768582107c566fde2)

struct bt\_conn \* conn

Connection object of the new connection.

**Definition** bluetooth.h:70

[bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md)

Advertising set info structure.

**Definition** bluetooth.h:1258

[bt\_le\_ext\_adv\_info::id](structbt__le__ext__adv__info.md#a06aa727cd2523914bc7509713585bffd)

uint8\_t id

**Definition** bluetooth.h:1260

[bt\_le\_ext\_adv\_info::addr](structbt__le__ext__adv__info.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9)

const bt\_addr\_le\_t \* addr

Current local advertising address used.

**Definition** bluetooth.h:1266

[bt\_le\_ext\_adv\_info::tx\_power](structbt__le__ext__adv__info.md#a485e4a8124fddee897fe744836cbfb24)

int8\_t tx\_power

Currently selected Transmit Power (dBM).

**Definition** bluetooth.h:1263

[bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md)

**Definition** bluetooth.h:73

[bt\_le\_ext\_adv\_scanned\_info::addr](structbt__le__ext__adv__scanned__info.md#a4431f157891d2c1a7d0e40f7e879ac3d)

bt\_addr\_le\_t \* addr

Active scanner LE address and type.

**Definition** bluetooth.h:75

[bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md)

**Definition** bluetooth.h:63

[bt\_le\_ext\_adv\_sent\_info::num\_sent](structbt__le__ext__adv__sent__info.md#a80f661efd35b069c2f8700851e9429a2)

uint8\_t num\_sent

The number of advertising events completed.

**Definition** bluetooth.h:65

[bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md)

**Definition** bluetooth.h:1125

[bt\_le\_ext\_adv\_start\_param::timeout](structbt__le__ext__adv__start__param.md#a80bb1ef4316dd75ea1268241333f4346)

uint16\_t timeout

Advertiser timeout (N \* 10 ms).

**Definition** bluetooth.h:1139

[bt\_le\_ext\_adv\_start\_param::num\_events](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f)

uint8\_t num\_events

Number of advertising events.

**Definition** bluetooth.h:1146

[bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md)

LE Secure Connections pairing Out of Band data.

**Definition** bluetooth.h:2331

[bt\_le\_oob\_sc\_data::c](structbt__le__oob__sc__data.md#a9bd93f1e9e41e241d0f84ae16ae47ba1)

uint8\_t c[16]

Confirm Value.

**Definition** bluetooth.h:2336

[bt\_le\_oob\_sc\_data::r](structbt__le__oob__sc__data.md#afa64bcc048d0e8709e262e2848a39d2c)

uint8\_t r[16]

Random Number.

**Definition** bluetooth.h:2333

[bt\_le\_oob](structbt__le__oob.md)

LE Out of Band information.

**Definition** bluetooth.h:2340

[bt\_le\_oob::addr](structbt__le__oob.md#a17cfed7683efbf5b5954847d655d7424)

bt\_addr\_le\_t addr

LE address.

**Definition** bluetooth.h:2344

[bt\_le\_oob::le\_sc\_data](structbt__le__oob.md#a80ccd4ab120a880adfff9aba3b19b4fd)

struct bt\_le\_oob\_sc\_data le\_sc\_data

LE Secure Connections pairing Out of Band data.

**Definition** bluetooth.h:2347

[bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md)

**Definition** bluetooth.h:78

[bt\_le\_per\_adv\_data\_request::count](structbt__le__per__adv__data__request.md#a766991899bc3e689adec36bf1f12e802)

uint8\_t count

The number of subevents data can be set for.

**Definition** bluetooth.h:83

[bt\_le\_per\_adv\_data\_request::start](structbt__le__per__adv__data__request.md#a779ed161919c3117f6ce165deb0a9b0a)

uint8\_t start

The first subevent data can be set for.

**Definition** bluetooth.h:80

[bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md)

**Definition** bluetooth.h:801

[bt\_le\_per\_adv\_param::interval\_min](structbt__le__per__adv__param.md#a49da44a3c0e4e866ffccffae5a9a22f7)

uint16\_t interval\_min

Minimum Periodic Advertising Interval (N \* 1.25 ms).

**Definition** bluetooth.h:808

[bt\_le\_per\_adv\_param::interval\_max](structbt__le__per__adv__param.md#a61308cfe72ad23372dfd2a3bd2550726)

uint16\_t interval\_max

Maximum Periodic Advertising Interval (N \* 1.25 ms).

**Definition** bluetooth.h:816

[bt\_le\_per\_adv\_param::options](structbt__le__per__adv__param.md#a9b80c2427171920f466601e7e8468814)

uint32\_t options

Bit-field of periodic advertising options.

**Definition** bluetooth.h:819

[bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md)

**Definition** bluetooth.h:86

[bt\_le\_per\_adv\_response\_info::subevent](structbt__le__per__adv__response__info.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5)

uint8\_t subevent

The subevent the response was received in.

**Definition** bluetooth.h:88

[bt\_le\_per\_adv\_response\_info::rssi](structbt__le__per__adv__response__info.md#a2db58fb452a07290ab4a50892c682837)

int8\_t rssi

The RSSI of the response in dBm.

**Definition** bluetooth.h:102

[bt\_le\_per\_adv\_response\_info::cte\_type](structbt__le__per__adv__response__info.md#a52b0c612b09cfcb3eb2ea475614c34b8)

uint8\_t cte\_type

The Constant Tone Extension (CTE) of the advertisement (bt\_df\_cte\_type).

**Definition** bluetooth.h:105

[bt\_le\_per\_adv\_response\_info::tx\_power](structbt__le__per__adv__response__info.md#a7ed20f695e0d696eaab7cddc4e3c11fb)

int8\_t tx\_power

The TX power of the response in dBm.

**Definition** bluetooth.h:99

[bt\_le\_per\_adv\_response\_info::response\_slot](structbt__le__per__adv__response__info.md#a83cc642c9f22c767421644e7d8233001)

uint8\_t response\_slot

The slot the response was received in.

**Definition** bluetooth.h:108

[bt\_le\_per\_adv\_response\_info::tx\_status](structbt__le__per__adv__response__info.md#ab17f33cb713d258bf6c863a64e5aba07)

uint8\_t tx\_status

Status of the subevent indication.

**Definition** bluetooth.h:96

[bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md)

**Definition** bluetooth.h:2604

[bt\_le\_per\_adv\_response\_params::response\_subevent](structbt__le__per__adv__response__params.md#a0cec222d5ba8cc9e20939d441646c913)

uint8\_t response\_subevent

The subevent the response shall be sent in.

**Definition** bluetooth.h:2623

[bt\_le\_per\_adv\_response\_params::request\_event](structbt__le__per__adv__response__params.md#a1af01d0a027fb8659615874acbd388f9)

uint16\_t request\_event

The periodic event counter of the request the response is sent to.

**Definition** bluetooth.h:2613

[bt\_le\_per\_adv\_response\_params::request\_subevent](structbt__le__per__adv__response__params.md#a3fc8ab0feb06714b28d22439cce60e41)

uint8\_t request\_subevent

The subevent counter of the request the response is sent to.

**Definition** bluetooth.h:2620

[bt\_le\_per\_adv\_response\_params::response\_slot](structbt__le__per__adv__response__params.md#aea0428083ccd5f4dccc17e494f38b7c3)

uint8\_t response\_slot

The response slot the response shall be sent in.

**Definition** bluetooth.h:2626

[bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md)

**Definition** bluetooth.h:1327

[bt\_le\_per\_adv\_subevent\_data\_params::response\_slot\_start](structbt__le__per__adv__subevent__data__params.md#a1354e9505239de3c42969138d719d775)

uint8\_t response\_slot\_start

The first response slot to listen to.

**Definition** bluetooth.h:1332

[bt\_le\_per\_adv\_subevent\_data\_params::data](structbt__le__per__adv__subevent__data__params.md#a46103c988d8ac360b7e26310a0322b4e)

const struct net\_buf\_simple \* data

The data to send.

**Definition** bluetooth.h:1338

[bt\_le\_per\_adv\_subevent\_data\_params::subevent](structbt__le__per__adv__subevent__data__params.md#a55f2da6041b538b3bc4bff38cd4d2953)

uint8\_t subevent

The subevent to set data for.

**Definition** bluetooth.h:1329

[bt\_le\_per\_adv\_subevent\_data\_params::response\_slot\_count](structbt__le__per__adv__subevent__data__params.md#a86d858606943a82917835a0172e88663)

uint8\_t response\_slot\_count

The number of response slots to listen to.

**Definition** bluetooth.h:1335

[bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md)

**Definition** bluetooth.h:1478

[bt\_le\_per\_adv\_sync\_cb::node](structbt__le__per__adv__sync__cb.md#a1977d27941063773c953a5f1dfa9ca76)

sys\_snode\_t node

**Definition** bluetooth.h:1556

[bt\_le\_per\_adv\_sync\_cb::recv](structbt__le__per__adv__sync__cb.md#a5576248e2eaef2afebe606e05e55f05f)

void(\* recv)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_le\_per\_adv\_sync\_recv\_info \*info, struct net\_buf\_simple \*buf)

Periodic advertising data received.

**Definition** bluetooth.h:1517

[bt\_le\_per\_adv\_sync\_cb::state\_changed](structbt__le__per__adv__sync__cb.md#a656b4802f79d4a472c2367ade144d72e)

void(\* state\_changed)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_le\_per\_adv\_sync\_state\_info \*info)

The periodic advertising sync state has changed.

**Definition** bluetooth.h:1531

[bt\_le\_per\_adv\_sync\_cb::synced](structbt__le__per__adv__sync__cb.md#a815be4343ab589df433a551663c5f4a1)

void(\* synced)(struct bt\_le\_per\_adv\_sync \*sync, struct bt\_le\_per\_adv\_sync\_synced\_info \*info)

The periodic advertising has been successfully synced.

**Definition** bluetooth.h:1489

[bt\_le\_per\_adv\_sync\_cb::biginfo](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9)

void(\* biginfo)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_iso\_biginfo \*biginfo)

BIGInfo advertising report received.

**Definition** bluetooth.h:1544

[bt\_le\_per\_adv\_sync\_cb::term](structbt__le__per__adv__sync__cb.md#acbd565a39918e5dfe7603a020e73daec)

void(\* term)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_le\_per\_adv\_sync\_term\_info \*info)

The periodic advertising sync has been terminated.

**Definition** bluetooth.h:1501

[bt\_le\_per\_adv\_sync\_cb::cte\_report\_cb](structbt__le__per__adv__sync__cb.md#ad2dc168696fbd22f7e3a089ac56f62d7)

void(\* cte\_report\_cb)(struct bt\_le\_per\_adv\_sync \*sync, struct bt\_df\_per\_adv\_sync\_iq\_samples\_report const \*info)

Callback for IQ samples report collected when sampling CTE received with periodic advertising PDU.

**Definition** bluetooth.h:1553

[bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md)

Advertising set info structure.

**Definition** bluetooth.h:1661

[bt\_le\_per\_adv\_sync\_info::interval](structbt__le__per__adv__sync__info.md#a365a0d8577429e4ee96e977071c9a906)

uint16\_t interval

Periodic advertising interval (N \* 1.25 ms).

**Definition** bluetooth.h:1669

[bt\_le\_per\_adv\_sync\_info::phy](structbt__le__per__adv__sync__info.md#a4d9520ea6a803f8fe4f41190f55c26e5)

uint8\_t phy

Advertiser PHY.

**Definition** bluetooth.h:1672

[bt\_le\_per\_adv\_sync\_info::addr](structbt__le__per__adv__sync__info.md#ac10fc2e2d3ec2160db8c2aac148d18a2)

bt\_addr\_le\_t addr

Periodic Advertiser Address.

**Definition** bluetooth.h:1663

[bt\_le\_per\_adv\_sync\_info::sid](structbt__le__per__adv__sync__info.md#acc0ef26c38279c9a67f8992005c2e58a)

uint8\_t sid

Advertiser SID.

**Definition** bluetooth.h:1666

[bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md)

**Definition** bluetooth.h:1595

[bt\_le\_per\_adv\_sync\_param::timeout](structbt__le__per__adv__sync__param.md#a301cfd3d6e5620d29c021ababe104754)

uint16\_t timeout

Synchronization timeout (N \* 10 ms).

**Definition** bluetooth.h:1630

[bt\_le\_per\_adv\_sync\_param::options](structbt__le__per__adv__sync__param.md#a4252f2b3b453c2f9c8fbf8c35a618ff2)

uint32\_t options

Bit-field of periodic advertising sync options.

**Definition** bluetooth.h:1613

[bt\_le\_per\_adv\_sync\_param::sid](structbt__le__per__adv__sync__param.md#a70795642ee94dd9e87f0cf251c095e7f)

uint8\_t sid

Advertiser SID.

**Definition** bluetooth.h:1610

[bt\_le\_per\_adv\_sync\_param::addr](structbt__le__per__adv__sync__param.md#ac93adedad747f61a771ac5445e486b74)

bt\_addr\_le\_t addr

Periodic Advertiser Address.

**Definition** bluetooth.h:1602

[bt\_le\_per\_adv\_sync\_param::skip](structbt__le__per__adv__sync__param.md#af9abb65547fb5bfea65f4c22963c7da0)

uint16\_t skip

Maximum event skip.

**Definition** bluetooth.h:1622

[bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md)

**Definition** bluetooth.h:1448

[bt\_le\_per\_adv\_sync\_recv\_info::cte\_type](structbt__le__per__adv__sync__recv__info.md#a1591907e3cb1f4565b9d26c18bccc7d2)

uint8\_t cte\_type

The Constant Tone Extension (CTE) of the advertisement (bt\_df\_cte\_type).

**Definition** bluetooth.h:1462

[bt\_le\_per\_adv\_sync\_recv\_info::sid](structbt__le__per__adv__sync__recv__info.md#a21b0ca87e46c6897282ebd877e45114e)

uint8\_t sid

Advertiser SID.

**Definition** bluetooth.h:1453

[bt\_le\_per\_adv\_sync\_recv\_info::addr](structbt__le__per__adv__sync__recv__info.md#a5817bd4fba2c93adebcebe007650b6eb)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:1450

[bt\_le\_per\_adv\_sync\_recv\_info::tx\_power](structbt__le__per__adv__sync__recv__info.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e)

int8\_t tx\_power

The TX power of the advertisement.

**Definition** bluetooth.h:1456

[bt\_le\_per\_adv\_sync\_recv\_info::rssi](structbt__le__per__adv__sync__recv__info.md#aa17c9d917469f121448ed4e1db485700)

int8\_t rssi

The RSSI of the advertisement excluding any CTE.

**Definition** bluetooth.h:1459

[bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md)

**Definition** bluetooth.h:1473

[bt\_le\_per\_adv\_sync\_state\_info::recv\_enabled](structbt__le__per__adv__sync__state__info.md#a4b0a3b7e36f935e06072304d6b92579f)

bool recv\_enabled

True if receiving periodic advertisements, false otherwise.

**Definition** bluetooth.h:1475

[bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md)

**Definition** bluetooth.h:2572

[bt\_le\_per\_adv\_sync\_subevent\_params::subevents](structbt__le__per__adv__sync__subevent__params.md#a5ac4e81ddd63797f921105748344c125)

uint8\_t \* subevents

The subevent(s) to synchronize with.

**Definition** bluetooth.h:2588

[bt\_le\_per\_adv\_sync\_subevent\_params::properties](structbt__le__per__adv__sync__subevent__params.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4)

uint16\_t properties

Periodic Advertising Properties.

**Definition** bluetooth.h:2578

[bt\_le\_per\_adv\_sync\_subevent\_params::num\_subevents](structbt__le__per__adv__sync__subevent__params.md#a867c66bf09461a4369da3d250701d2ae)

uint8\_t num\_subevents

Number of subevents to sync to.

**Definition** bluetooth.h:2581

[bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md)

**Definition** bluetooth.h:1391

[bt\_le\_per\_adv\_sync\_synced\_info::recv\_enabled](structbt__le__per__adv__sync__synced__info.md#a0dd4b7646da0fadc48e94ff3dc91ef83)

bool recv\_enabled

True if receiving periodic advertisements, false otherwise.

**Definition** bluetooth.h:1405

[bt\_le\_per\_adv\_sync\_synced\_info::interval](structbt__le__per__adv__sync__synced__info.md#a5304e1826face35c506f3b8f6cad7df2)

uint16\_t interval

Periodic advertising interval (N \* 1.25 ms).

**Definition** bluetooth.h:1399

[bt\_le\_per\_adv\_sync\_synced\_info::sid](structbt__le__per__adv__sync__synced__info.md#a5489c3038f7fff596316a456fc8d580b)

uint8\_t sid

Advertiser SID.

**Definition** bluetooth.h:1396

[bt\_le\_per\_adv\_sync\_synced\_info::addr](structbt__le__per__adv__sync__synced__info.md#a7ca99b0596b08d153d3ba5310adab125)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:1393

[bt\_le\_per\_adv\_sync\_synced\_info::phy](structbt__le__per__adv__sync__synced__info.md#a8b7709011541e95ceaeac379cc3143bb)

uint8\_t phy

Advertiser PHY.

**Definition** bluetooth.h:1402

[bt\_le\_per\_adv\_sync\_synced\_info::conn](structbt__le__per__adv__sync__synced__info.md#ada4cda53aa87f29d54f6cd88134efe14)

struct bt\_conn \* conn

Peer that transferred the periodic advertising sync.

**Definition** bluetooth.h:1420

[bt\_le\_per\_adv\_sync\_synced\_info::service\_data](structbt__le__per__adv__sync__synced__info.md#adee2bdafa86a0c3c1dfb4660e85396a3)

uint16\_t service\_data

Service Data provided by the peer when sync is transferred.

**Definition** bluetooth.h:1412

[bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md)

**Definition** bluetooth.h:1437

[bt\_le\_per\_adv\_sync\_term\_info::addr](structbt__le__per__adv__sync__term__info.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:1439

[bt\_le\_per\_adv\_sync\_term\_info::reason](structbt__le__per__adv__sync__term__info.md#a429b8b665eacbfe9db013a571b829bac)

uint8\_t reason

Cause of periodic advertising termination.

**Definition** bluetooth.h:1445

[bt\_le\_per\_adv\_sync\_term\_info::sid](structbt__le__per__adv__sync__term__info.md#a7a5f2ecccaf698bad86f10d9a7d16189)

uint8\_t sid

Advertiser SID.

**Definition** bluetooth.h:1442

[bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md)

**Definition** bluetooth.h:1817

[bt\_le\_per\_adv\_sync\_transfer\_param::options](structbt__le__per__adv__sync__transfer__param.md#a0b3ee6df1b409e64a064ffb6ac632cce)

uint32\_t options

Periodic Advertising Sync Transfer options.

**Definition** bluetooth.h:1835

[bt\_le\_per\_adv\_sync\_transfer\_param::timeout](structbt__le__per__adv__sync__transfer__param.md#a5bfa84c6bdacdf8893a0951a5ce71fc6)

uint16\_t timeout

Synchronization timeout (N \* 10 ms).

**Definition** bluetooth.h:1832

[bt\_le\_per\_adv\_sync\_transfer\_param::skip](structbt__le__per__adv__sync__transfer__param.md#a840e7cfac3a2947e5128d704067aaf7e)

uint16\_t skip

Maximum event skip.

**Definition** bluetooth.h:1824

[bt\_le\_scan\_cb](structbt__le__scan__cb.md)

Listener context for (LE) scanning.

**Definition** bluetooth.h:2069

[bt\_le\_scan\_cb::timeout](structbt__le__scan__cb.md#a2f57f3fee46bd137065f4c57d0cd5157)

void(\* timeout)(void)

The scanner has stopped scanning after scan timeout.

**Definition** bluetooth.h:2081

[bt\_le\_scan\_cb::node](structbt__le__scan__cb.md#a50dbc5e7618fd488e9acb7ad8f104a63)

sys\_snode\_t node

**Definition** bluetooth.h:2083

[bt\_le\_scan\_cb::recv](structbt__le__scan__cb.md#a71d73c1da28d4a27626f77d96a5b3541)

void(\* recv)(const struct bt\_le\_scan\_recv\_info \*info, struct net\_buf\_simple \*buf)

Advertisement packet and scan response received callback.

**Definition** bluetooth.h:2077

[bt\_le\_scan\_param](structbt__le__scan__param.md)

LE scan parameters.

**Definition** bluetooth.h:1979

[bt\_le\_scan\_param::type](structbt__le__scan__param.md#a02d75322390287c3fa754bf915660d0c)

uint8\_t type

Scan type (BT\_LE\_SCAN\_TYPE\_ACTIVE or BT\_LE\_SCAN\_TYPE\_PASSIVE).

**Definition** bluetooth.h:1981

[bt\_le\_scan\_param::interval](structbt__le__scan__param.md#a2f4e053d97c62b6fdf42a245908607f8)

uint16\_t interval

Scan interval (N \* 0.625 ms).

**Definition** bluetooth.h:1987

[bt\_le\_scan\_param::window](structbt__le__scan__param.md#a37a7ee82e86a91cf7a9c2adf60bb526a)

uint16\_t window

Scan window (N \* 0.625 ms).

**Definition** bluetooth.h:1990

[bt\_le\_scan\_param::timeout](structbt__le__scan__param.md#a3e71ce551dcc7762c29e2316996e2912)

uint16\_t timeout

Scan timeout (N \* 10 ms).

**Definition** bluetooth.h:1998

[bt\_le\_scan\_param::interval\_coded](structbt__le__scan__param.md#a67a20bc94a3d98fa10af7b5b42dde328)

uint16\_t interval\_coded

Scan interval LE Coded PHY (N \* 0.625 MS).

**Definition** bluetooth.h:2005

[bt\_le\_scan\_param::window\_coded](structbt__le__scan__param.md#a93166af55dca71393c60cb3f7ac6d809)

uint16\_t window\_coded

Scan window LE Coded PHY (N \* 0.625 MS).

**Definition** bluetooth.h:2012

[bt\_le\_scan\_param::options](structbt__le__scan__param.md#ac702ecbd938b9a73156a0c6fcf603812)

uint32\_t options

Bit-field of scanning options.

**Definition** bluetooth.h:1984

[bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md)

LE advertisement and scan response packet information.

**Definition** bluetooth.h:2016

[bt\_le\_scan\_recv\_info::interval](structbt__le__scan__recv__info.md#a1060c5937708ff81a64f068e02fc7826)

uint16\_t interval

Periodic advertising interval.

**Definition** bluetooth.h:2059

[bt\_le\_scan\_recv\_info::tx\_power](structbt__le__scan__recv__info.md#a2addeba6d2ec8e55dc5379adf6519148)

int8\_t tx\_power

Transmit power of the advertiser.

**Definition** bluetooth.h:2032

[bt\_le\_scan\_recv\_info::sid](structbt__le__scan__recv__info.md#a4df8d4e1fdd7514d170744856ebe7015)

uint8\_t sid

Advertising Set Identifier.

**Definition** bluetooth.h:2026

[bt\_le\_scan\_recv\_info::primary\_phy](structbt__le__scan__recv__info.md#a6189ed8453cb7907f34dc7dfaf1343bd)

uint8\_t primary\_phy

Primary advertising channel PHY.

**Definition** bluetooth.h:2062

[bt\_le\_scan\_recv\_info::rssi](structbt__le__scan__recv__info.md#a88f677733147245ccbf861c7fc5e0f11)

int8\_t rssi

Strength of advertiser signal.

**Definition** bluetooth.h:2029

[bt\_le\_scan\_recv\_info::addr](structbt__le__scan__recv__info.md#a907fb7ec3c78d68da5015a8c3afc3084)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:2023

[bt\_le\_scan\_recv\_info::secondary\_phy](structbt__le__scan__recv__info.md#ac797291291dc7ba7ac171ed7f24f0d16)

uint8\_t secondary\_phy

Secondary advertising channel PHY.

**Definition** bluetooth.h:2065

[bt\_le\_scan\_recv\_info::adv\_type](structbt__le__scan__recv__info.md#adccb2ce5c6d228bd7f8f050088629524)

uint8\_t adv\_type

Advertising packet type.

**Definition** bluetooth.h:2042

[bt\_le\_scan\_recv\_info::adv\_props](structbt__le__scan__recv__info.md#af29ddfb59e286af9ca465cbd5a91bf2d)

uint16\_t adv\_props

Advertising packet properties bitfield.

**Definition** bluetooth.h:2052

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

[net\_buf\_simple::data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** buf.h:89

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [bluetooth.h](bluetooth_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
