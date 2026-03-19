---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/bluetooth_2bluetooth_8h_source.html
original_path: doxygen/html/bluetooth_2bluetooth_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bluetooth.h

[Go to the documentation of this file.](bluetooth_2bluetooth_8h.md)

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

24#include <[zephyr/sys/util.h](sys_2util_8h.md)>

25#include <[zephyr/net\_buf.h](net__buf_8h.md)>

26#include <[zephyr/bluetooth/gap.h](gap_8h.md)>

27#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

28#include <[zephyr/bluetooth/crypto.h](bluetooth_2crypto_8h.md)>

29#include <[zephyr/bluetooth/classic/classic.h](classic_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

43

[ 49](group__bt__gap.md#gaded4b52c9bb87fd4d19b1eb9361973e5)#define BT\_ID\_DEFAULT 0

50

52struct bt\_le\_ext\_adv;

53

55struct bt\_le\_per\_adv\_sync;

56

57/\* Don't require everyone to include conn.h \*/

58struct bt\_conn;

59

60/\* Don't require everyone to include iso.h \*/

61struct [bt\_iso\_biginfo](structbt__iso__biginfo.md);

62

63/\* Don't require everyone to include direction.h \*/

64struct [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md);

65

[ 66](structbt__le__ext__adv__sent__info.md)struct [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) {

[ 68](structbt__le__ext__adv__sent__info.md#a80f661efd35b069c2f8700851e9429a2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_sent](structbt__le__ext__adv__sent__info.md#a80f661efd35b069c2f8700851e9429a2);

69};

70

[ 71](structbt__le__ext__adv__connected__info.md)struct [bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md) {

[ 73](structbt__le__ext__adv__connected__info.md#a157efa6206b418f768582107c566fde2) struct bt\_conn \*[conn](structbt__le__ext__adv__connected__info.md#a157efa6206b418f768582107c566fde2);

74};

75

[ 76](structbt__le__ext__adv__scanned__info.md)struct [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md) {

[ 78](structbt__le__ext__adv__scanned__info.md#a4431f157891d2c1a7d0e40f7e879ac3d) [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__ext__adv__scanned__info.md#a4431f157891d2c1a7d0e40f7e879ac3d);

79};

80

[ 81](structbt__le__per__adv__data__request.md)struct [bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md) {

[ 83](structbt__le__per__adv__data__request.md#a779ed161919c3117f6ce165deb0a9b0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [start](structbt__le__per__adv__data__request.md#a779ed161919c3117f6ce165deb0a9b0a);

84

[ 86](structbt__le__per__adv__data__request.md#a766991899bc3e689adec36bf1f12e802) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [count](structbt__le__per__adv__data__request.md#a766991899bc3e689adec36bf1f12e802);

87};

88

[ 89](structbt__le__per__adv__response__info.md)struct [bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md) {

[ 91](structbt__le__per__adv__response__info.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__le__per__adv__response__info.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5);

92

[ 99](structbt__le__per__adv__response__info.md#ab17f33cb713d258bf6c863a64e5aba07) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_status](structbt__le__per__adv__response__info.md#ab17f33cb713d258bf6c863a64e5aba07);

100

[ 102](structbt__le__per__adv__response__info.md#a7ed20f695e0d696eaab7cddc4e3c11fb) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__per__adv__response__info.md#a7ed20f695e0d696eaab7cddc4e3c11fb);

103

[ 105](structbt__le__per__adv__response__info.md#a2db58fb452a07290ab4a50892c682837) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__le__per__adv__response__info.md#a2db58fb452a07290ab4a50892c682837);

106

[ 108](structbt__le__per__adv__response__info.md#a52b0c612b09cfcb3eb2ea475614c34b8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__le__per__adv__response__info.md#a52b0c612b09cfcb3eb2ea475614c34b8);

109

[ 111](structbt__le__per__adv__response__info.md#a83cc642c9f22c767421644e7d8233001) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot](structbt__le__per__adv__response__info.md#a83cc642c9f22c767421644e7d8233001);

112};

113

[ 114](structbt__le__ext__adv__cb.md)struct [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md) {

[ 126](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60) void (\*[sent](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60))(struct bt\_le\_ext\_adv \*adv,

127 struct [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) \*info);

128

[ 138](structbt__le__ext__adv__cb.md#a7aad0fbd8e531e70f661500c338d870e) void (\*[connected](structbt__le__ext__adv__cb.md#a7aad0fbd8e531e70f661500c338d870e))(struct bt\_le\_ext\_adv \*adv,

139 struct [bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md) \*info);

140

[ 151](structbt__le__ext__adv__cb.md#a277dc3269741d40b644ae3c777198fab) void (\*[scanned](structbt__le__ext__adv__cb.md#a277dc3269741d40b644ae3c777198fab))(struct bt\_le\_ext\_adv \*adv,

152 struct [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md) \*info);

153

154#if defined(CONFIG\_BT\_PRIVACY)

171 [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*rpa\_expired)(struct bt\_le\_ext\_adv \*adv);

172#endif /\* defined(CONFIG\_BT\_PRIVACY) \*/

173

174#if defined(CONFIG\_BT\_PER\_ADV\_RSP)

184 void (\*pawr\_data\_request)(struct bt\_le\_ext\_adv \*adv,

185 const struct [bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md) \*request);

195 void (\*pawr\_response)(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md) \*info,

196 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

197

198#endif /\* defined(CONFIG\_BT\_PER\_ADV\_RSP) \*/

199};

200

[ 207](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb)typedef void (\*[bt\_ready\_cb\_t](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb))(int err);

208

[ 228](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b)int [bt\_enable](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b)([bt\_ready\_cb\_t](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb) cb);

229

[ 249](group__bt__gap.md#ga0a58e5a050170e84a80f8d5bb3516ec7)int [bt\_disable](group__bt__gap.md#ga0a58e5a050170e84a80f8d5bb3516ec7)(void);

250

[ 256](group__bt__gap.md#gaa8bf6854e7ad1fe7e0805737576e5d1a)bool [bt\_is\_ready](group__bt__gap.md#gaa8bf6854e7ad1fe7e0805737576e5d1a)(void);

257

[ 275](group__bt__gap.md#gac8bb3609a3d6da69ff736809e45f5c8a)int [bt\_set\_name](group__bt__gap.md#gac8bb3609a3d6da69ff736809e45f5c8a)(const char \*name);

276

[ 284](group__bt__gap.md#gad922d894b25e86de3f81ce77200a13fd)const char \*[bt\_get\_name](group__bt__gap.md#gad922d894b25e86de3f81ce77200a13fd)(void);

285

[ 296](group__bt__gap.md#ga35b76ea7ce79721e47ca4164e08b2dfb)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_get\_appearance](group__bt__gap.md#ga35b76ea7ce79721e47ca4164e08b2dfb)(void);

297

[ 312](group__bt__gap.md#gaf0729453790aab1bd3d52c623be3b35a)int [bt\_set\_appearance](group__bt__gap.md#gaf0729453790aab1bd3d52c623be3b35a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) new\_appearance);

313

[ 334](group__bt__gap.md#ga06d0ae35cbf4382679cc3cfe612cee4d)void [bt\_id\_get](group__bt__gap.md#ga06d0ae35cbf4382679cc3cfe612cee4d)([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addrs, size\_t \*count);

335

[ 382](group__bt__gap.md#gae11eb8ad254418c38a0e8689df25a159)int [bt\_id\_create](group__bt__gap.md#gae11eb8ad254418c38a0e8689df25a159)([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*irk);

383

[ 416](group__bt__gap.md#gabb3353edc8a3a8d29a0370049b20cbe4)int [bt\_id\_reset](group__bt__gap.md#gabb3353edc8a3a8d29a0370049b20cbe4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*irk);

417

[ 434](group__bt__gap.md#gaf6cd906690a51ebed04bea4f4ef716ff)int [bt\_id\_delete](group__bt__gap.md#gaf6cd906690a51ebed04bea4f4ef716ff)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id);

435

[ 447](group__bt__gap.md#ga7357d34bf295a16d8288df3bf75e7976)#define BT\_DATA\_SERIALIZED\_SIZE(data\_len) ((data\_len) + 2)

448

[ 456](structbt__data.md)struct [bt\_data](structbt__data.md) {

[ 457](structbt__data.md#a984aecb40a4993ffa113be53942db065) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__data.md#a984aecb40a4993ffa113be53942db065);

[ 458](structbt__data.md#abda19091a1b8f99d385f11772ef34d5f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_len](structbt__data.md#abda19091a1b8f99d385f11772ef34d5f);

[ 459](structbt__data.md#ac80ec10101ad69a86f703a4e652c7826) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__data.md#ac80ec10101ad69a86f703a4e652c7826);

460};

461

[ 472](group__bt__gap.md#ga8481217e632522e1f322de87d745f8f0)#define BT\_DATA(\_type, \_data, \_data\_len) \

473 { \

474 .type = (\_type), \

475 .data\_len = (\_data\_len), \

476 .data = (const uint8\_t \*)(\_data), \

477 }

478

[ 488](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)#define BT\_DATA\_BYTES(\_type, \_bytes...) \

489 BT\_DATA(\_type, ((uint8\_t []) { \_bytes }), \

490 sizeof((uint8\_t []) { \_bytes }))

491

[ 502](group__bt__gap.md#ga3d2c6adc42eb9510734630f38d921b9a)size\_t [bt\_data\_get\_len](group__bt__gap.md#ga3d2c6adc42eb9510734630f38d921b9a)(const struct [bt\_data](structbt__data.md) data[], size\_t data\_count);

503

[ 518](group__bt__gap.md#ga3c067b16468ebd17973faeded0fc83c9)size\_t [bt\_data\_serialize](group__bt__gap.md#ga3c067b16468ebd17973faeded0fc83c9)(const struct [bt\_data](structbt__data.md) \*input, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*output);

519

521enum {

[ 523](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea928b376123819cb0a69fbb5b35608dbf) [BT\_LE\_ADV\_OPT\_NONE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea928b376123819cb0a69fbb5b35608dbf) = 0,

524

[ 545](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) [BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) \_\_deprecated = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

546

557 \_BT\_LE\_ADV\_OPT\_CONNECTABLE = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

558

[ 575](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2) [BT\_LE\_ADV\_OPT\_ONE\_TIME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2) \_\_deprecated = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

576

583 \_BT\_LE\_ADV\_OPT\_ONE\_TIME = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

584

[ 603](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169) [BT\_LE\_ADV\_OPT\_CONN](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

604

[ 615](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e) [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

616

[ 641](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398) [BT\_LE\_ADV\_OPT\_USE\_NAME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

642

[ 649](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeafd164ec5476f5e2d9aedf50032946872) [BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeafd164ec5476f5e2d9aedf50032946872) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

650

[ 663](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabdcf1c80662061fa30575e1f9fc6cf6f) [BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabdcf1c80662061fa30575e1f9fc6cf6f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

664

[ 668](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea807ba316edc49c8448a8ff7d497173f5) [BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea807ba316edc49c8448a8ff7d497173f5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

669

[ 671](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead5efef3d01731110dbd71d5a5dc9baaf) [BT\_LE\_ADV\_OPT\_FILTER\_CONN](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead5efef3d01731110dbd71d5a5dc9baaf) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

672

[ 676](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea1563b053f457833d1a3d11c8dc4d394b) [BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea1563b053f457833d1a3d11c8dc4d394b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

677

[ 686](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) [BT\_LE\_ADV\_OPT\_SCANNABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

687

[ 708](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) [BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

709

[ 724](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae864aefcdfbecaffe823b9b144fe0a6b) [BT\_LE\_ADV\_OPT\_NO\_2M](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae864aefcdfbecaffe823b9b144fe0a6b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

725

[ 736](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1) [BT\_LE\_ADV\_OPT\_CODED](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

737

[ 743](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea185e0f884f8b0ce79625448638de8fab) [BT\_LE\_ADV\_OPT\_ANONYMOUS](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea185e0f884f8b0ce79625448638de8fab) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

744

[ 750](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaecff4fe3ac3d1fba3f6fa76c77713859) [BT\_LE\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaecff4fe3ac3d1fba3f6fa76c77713859) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

751

[ 753](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeab46741616f8bfe50c4b492d1f7970779) [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeab46741616f8bfe50c4b492d1f7970779) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

754

[ 756](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabd9cb02691d7e025fe3fea9a80123275) [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabd9cb02691d7e025fe3fea9a80123275) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

757

[ 759](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea89f7494620236c976bf1a76a880e2a28) [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea89f7494620236c976bf1a76a880e2a28) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17),

760

[ 772](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73) [BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18),

773

[ 786](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea22958d8539d661ad7ca8d3f1173e7e5e) [BT\_LE\_ADV\_OPT\_USE\_NRPA](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea22958d8539d661ad7ca8d3f1173e7e5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

787

[ 803](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea9a35ede118224d6ed17f252fff6bb47e) [BT\_LE\_ADV\_OPT\_REQUIRE\_S2\_CODING](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea9a35ede118224d6ed17f252fff6bb47e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20),

804

[ 820](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa6a61768ad4102f199d3970791118bb8) [BT\_LE\_ADV\_OPT\_REQUIRE\_S8\_CODING](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa6a61768ad4102f199d3970791118bb8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21),

821};

822

[ 824](structbt__le__adv__param.md)struct [bt\_le\_adv\_param](structbt__le__adv__param.md) {

[ 833](structbt__le__adv__param.md#af957bd92b949536af2b2db0db7b2b425) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__le__adv__param.md#af957bd92b949536af2b2db0db7b2b425);

834

[ 840](structbt__le__adv__param.md#a6e2f0e1b76495afe7fe661e8698d0909) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__adv__param.md#a6e2f0e1b76495afe7fe661e8698d0909);

841

[ 850](structbt__le__adv__param.md#a9911e9bfc97ff0c48a6decae3f922e95) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [secondary\_max\_skip](structbt__le__adv__param.md#a9911e9bfc97ff0c48a6decae3f922e95);

851

[ 853](structbt__le__adv__param.md#a2a978c60153eb03697769bc72928f4ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__adv__param.md#a2a978c60153eb03697769bc72928f4ef);

854

[ 862](structbt__le__adv__param.md#aca8ff5a4f5d29184535162f007b2d39e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval\_min](structbt__le__adv__param.md#aca8ff5a4f5d29184535162f007b2d39e);

863

[ 871](structbt__le__adv__param.md#afeba6973dca99d8ee818fdde0c22cb59) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval\_max](structbt__le__adv__param.md#afeba6973dca99d8ee818fdde0c22cb59);

872

[ 888](structbt__le__adv__param.md#a4cf31f54f067fffa3c848adc2ffd7119) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[peer](structbt__le__adv__param.md#a4cf31f54f067fffa3c848adc2ffd7119);

889};

890

891

893enum {

[ 895](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aaa2c689d726eacfb18d87655b1f587518) [BT\_LE\_PER\_ADV\_OPT\_NONE](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aaa2c689d726eacfb18d87655b1f587518) = 0,

896

[ 902](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa9524537e4cb726f4ff10ba93381bb27f) [BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa9524537e4cb726f4ff10ba93381bb27f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

903

[ 909](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa38cebc2ae885ff630b34c603e2ec6403) [BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa38cebc2ae885ff630b34c603e2ec6403) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

910};

911

[ 912](structbt__le__per__adv__param.md)struct [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md) {

[ 919](structbt__le__per__adv__param.md#a49da44a3c0e4e866ffccffae5a9a22f7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_min](structbt__le__per__adv__param.md#a49da44a3c0e4e866ffccffae5a9a22f7);

920

[ 927](structbt__le__per__adv__param.md#a61308cfe72ad23372dfd2a3bd2550726) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_max](structbt__le__per__adv__param.md#a61308cfe72ad23372dfd2a3bd2550726);

928

[ 930](structbt__le__per__adv__param.md#a9b80c2427171920f466601e7e8468814) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__per__adv__param.md#a9b80c2427171920f466601e7e8468814);

931

932#if defined(CONFIG\_BT\_PER\_ADV\_RSP)

938 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents;

939

945 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subevent\_interval;

946

952 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_delay;

953

959 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_spacing;

960

966 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_response\_slots;

967#endif /\* CONFIG\_BT\_PER\_ADV\_RSP \*/

968};

969

[ 979](group__bt__gap.md#ga71555b857cf8c2a47c36e4dafa7accf4)#define BT\_LE\_ADV\_PARAM\_INIT(\_options, \_int\_min, \_int\_max, \_peer) \

980{ \

981 .id = BT\_ID\_DEFAULT, \

982 .sid = 0, \

983 .secondary\_max\_skip = 0, \

984 .options = (\_options), \

985 .interval\_min = (\_int\_min), \

986 .interval\_max = (\_int\_max), \

987 .peer = (\_peer), \

988}

989

[ 999](group__bt__gap.md#ga9557269dd36b624b49e76c511c3a0cc1)#define BT\_LE\_ADV\_PARAM(\_options, \_int\_min, \_int\_max, \_peer) \

1000 ((const struct bt\_le\_adv\_param[]) { \

1001 BT\_LE\_ADV\_PARAM\_INIT(\_options, \_int\_min, \_int\_max, \_peer) \

1002 })

1003

[ 1004](group__bt__gap.md#ga1f5edc3c4cbead62e32cef8cc7b83725)#define BT\_LE\_ADV\_CONN\_DIR(\_peer) BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONN, 0, 0, \_peer)

1005

[ 1012](group__bt__gap.md#gad490487b9e196526a13fe249a4c25448)#define BT\_LE\_ADV\_CONN \

1013 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE, BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1014 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL) \

1015 \_\_DEPRECATED\_MACRO

1016

[ 1038](group__bt__gap.md#gaa700527b1caf3bef27d96a3f91a29f69)#define BT\_LE\_ADV\_CONN\_FAST\_1 \

1039 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONN, BT\_GAP\_ADV\_FAST\_INT\_MIN\_1, BT\_GAP\_ADV\_FAST\_INT\_MAX\_1, \

1040 NULL)

1041

[ 1054](group__bt__gap.md#ga684a1110a8973bc17211f6f0824beccd)#define BT\_LE\_ADV\_CONN\_FAST\_2 \

1055 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONN, BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1056 NULL)

1057

[ 1058](group__bt__gap.md#gac0430ab5a40a49b3281dd6ff8a7e7378)#define BT\_LE\_ADV\_CONN\_ONE\_TIME BT\_LE\_ADV\_CONN\_FAST\_2 \_\_DEPRECATED\_MACRO

1059

[ 1064](group__bt__gap.md#ga7b29dba3d892186897c5b4ca5adfd2e3)#define BT\_LE\_ADV\_CONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE | \

1065 BT\_LE\_ADV\_OPT\_USE\_NAME, \

1066 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1067 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL) \

1068 \_\_DEPRECATED\_MACRO

1069

[ 1074](group__bt__gap.md#ga213307090f1debdc783c54faf4a36740)#define BT\_LE\_ADV\_CONN\_NAME\_AD BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE | \

1075 BT\_LE\_ADV\_OPT\_USE\_NAME | \

1076 BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD, \

1077 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1078 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL) \

1079 \_\_DEPRECATED\_MACRO

1080

[ 1081](group__bt__gap.md#gab89e033ed3fd116c94120d177dfdc839)#define BT\_LE\_ADV\_CONN\_DIR\_LOW\_DUTY(\_peer) \

1082 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONN | BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY, \

1083 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \_peer)

1084

[ 1086](group__bt__gap.md#ga1610555bf59f1d691d640f245957fdce)#define BT\_LE\_ADV\_NCONN BT\_LE\_ADV\_PARAM(0, BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1087 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

1088

[ 1095](group__bt__gap.md#gac1c3c47e3136ce813bb50b00a9387cb4)#define BT\_LE\_ADV\_NCONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_USE\_NAME, \

1096 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1097 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL) \

1098 \_\_DEPRECATED\_MACRO

1099

[ 1101](group__bt__gap.md#ga6ef9fb7a469b03265c7adc99ea19a11b)#define BT\_LE\_ADV\_NCONN\_IDENTITY BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_USE\_IDENTITY, \

1102 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1103 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1104 NULL)

1105

[ 1107](group__bt__gap.md#gaeaaef4dede5d45251dfe12f329e070b7)#define BT\_LE\_EXT\_ADV\_CONN \

1108 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | BT\_LE\_ADV\_OPT\_CONN, BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1109 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

1110

[ 1117](group__bt__gap.md#gac4880197cbe21aad78c4edf10cde95da)#define BT\_LE\_EXT\_ADV\_CONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1118 BT\_LE\_ADV\_OPT\_CONNECTABLE | \

1119 BT\_LE\_ADV\_OPT\_USE\_NAME, \

1120 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1121 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1122 NULL) \

1123 \_\_DEPRECATED\_MACRO

1124

[ 1126](group__bt__gap.md#ga5dd57fc7f0e213db08655e631a2f314e)#define BT\_LE\_EXT\_ADV\_SCAN BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1127 BT\_LE\_ADV\_OPT\_SCANNABLE, \

1128 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1129 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1130 NULL)

1131

[ 1138](group__bt__gap.md#ga3e4abd3691e2c6d95acd21b9ca566edd)#define BT\_LE\_EXT\_ADV\_SCAN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1139 BT\_LE\_ADV\_OPT\_SCANNABLE | \

1140 BT\_LE\_ADV\_OPT\_USE\_NAME, \

1141 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1142 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1143 NULL) \

1144 \_\_DEPRECATED\_MACRO

1145

[ 1147](group__bt__gap.md#gaabc0385f6a5307b48ec43af6aae7dea6)#define BT\_LE\_EXT\_ADV\_NCONN BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV, \

1148 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1149 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

1150

[ 1157](group__bt__gap.md#ga5c79af6787ccda890f485a45c931cdc8)#define BT\_LE\_EXT\_ADV\_NCONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1158 BT\_LE\_ADV\_OPT\_USE\_NAME, \

1159 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1160 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1161 NULL) \

1162 \_\_DEPRECATED\_MACRO

1163

[ 1165](group__bt__gap.md#ga7e46a64af0036c433c2e940ce7db0a05)#define BT\_LE\_EXT\_ADV\_NCONN\_IDENTITY \

1166 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1167 BT\_LE\_ADV\_OPT\_USE\_IDENTITY, \

1168 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1169 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

1170

[ 1172](group__bt__gap.md#ga0e911d3aafdd0c926590b3272a3da564)#define BT\_LE\_EXT\_ADV\_CODED\_NCONN BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1173 BT\_LE\_ADV\_OPT\_CODED, \

1174 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1175 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1176 NULL)

1177

[ 1185](group__bt__gap.md#ga8c6027f7c0888c577f9b61a65104be05)#define BT\_LE\_EXT\_ADV\_CODED\_NCONN\_NAME \

1186 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | BT\_LE\_ADV\_OPT\_CODED | \

1187 BT\_LE\_ADV\_OPT\_USE\_NAME, \

1188 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1189 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL) \

1190 \_\_DEPRECATED\_MACRO

1191

[ 1195](group__bt__gap.md#gac67c52693154ebbeedbb31e100513812)#define BT\_LE\_EXT\_ADV\_CODED\_NCONN\_IDENTITY \

1196 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | BT\_LE\_ADV\_OPT\_CODED | \

1197 BT\_LE\_ADV\_OPT\_USE\_IDENTITY, \

1198 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1199 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

1200

[ 1207](group__bt__gap.md#gaf0d4c5b05deb5466a0e29c153263b489)#define BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT(\_timeout, \_n\_evts) \

1208{ \

1209 .timeout = (\_timeout), \

1210 .num\_events = (\_n\_evts), \

1211}

1212

[ 1219](group__bt__gap.md#ga9b2cefbcb0a85116cadb68f6d80c6429)#define BT\_LE\_EXT\_ADV\_START\_PARAM(\_timeout, \_n\_evts) \

1220 ((const struct bt\_le\_ext\_adv\_start\_param[]) { \

1221 BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT((\_timeout), (\_n\_evts)) \

1222 })

1223

[ 1224](group__bt__gap.md#ga8c83a6f322a479bc24a576a7f091312e)#define BT\_LE\_EXT\_ADV\_START\_DEFAULT BT\_LE\_EXT\_ADV\_START\_PARAM(0, 0)

1225

[ 1233](group__bt__gap.md#ga880567278a81098ae55f52f624c61041)#define BT\_LE\_PER\_ADV\_PARAM\_INIT(\_int\_min, \_int\_max, \_options) \

1234{ \

1235 .interval\_min = (\_int\_min), \

1236 .interval\_max = (\_int\_max), \

1237 .options = (\_options), \

1238}

1239

[ 1247](group__bt__gap.md#gaf46e54f8fcda7b65b659685bb225d243)#define BT\_LE\_PER\_ADV\_PARAM(\_int\_min, \_int\_max, \_options) \

1248 ((struct bt\_le\_per\_adv\_param[]) { \

1249 BT\_LE\_PER\_ADV\_PARAM\_INIT(\_int\_min, \_int\_max, \_options) \

1250 })

1251

[ 1252](group__bt__gap.md#ga8f6a00faaaab2a91ac943c71ed041ac1)#define BT\_LE\_PER\_ADV\_DEFAULT BT\_LE\_PER\_ADV\_PARAM(BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN, \

1253 BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX, \

1254 BT\_LE\_PER\_ADV\_OPT\_NONE)

1255

[ 1286](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02)int [bt\_le\_adv\_start](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02)(const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param,

1287 const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len,

1288 const struct [bt\_data](structbt__data.md) \*sd, size\_t sd\_len);

1289

[ 1302](group__bt__gap.md#ga9a406ebfefac3dd09935a4ae0e317817)int [bt\_le\_adv\_update\_data](group__bt__gap.md#ga9a406ebfefac3dd09935a4ae0e317817)(const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len,

1303 const struct [bt\_data](structbt__data.md) \*sd, size\_t sd\_len);

1304

[ 1312](group__bt__gap.md#ga1776e310b9d80898e6b32d50c4fe0b49)int [bt\_le\_adv\_stop](group__bt__gap.md#ga1776e310b9d80898e6b32d50c4fe0b49)(void);

1313

[ 1328](group__bt__gap.md#gad02b855dd7a26e3910b247fa73f19297)int [bt\_le\_ext\_adv\_create](group__bt__gap.md#gad02b855dd7a26e3910b247fa73f19297)(const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param,

1329 const struct [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md) \*cb,

1330 struct bt\_le\_ext\_adv \*\*adv);

1331

[ 1332](structbt__le__ext__adv__start__param.md)struct [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md) {

[ 1346](structbt__le__ext__adv__start__param.md#a80bb1ef4316dd75ea1268241333f4346) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__ext__adv__start__param.md#a80bb1ef4316dd75ea1268241333f4346);

[ 1353](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_events](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f);

1354};

1355

[ 1369](group__bt__gap.md#gaf0f436c55482d9429f674303ae3aa815)int [bt\_le\_ext\_adv\_start](group__bt__gap.md#gaf0f436c55482d9429f674303ae3aa815)(struct bt\_le\_ext\_adv \*adv,

1370 const struct [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md) \*param);

1371

[ 1382](group__bt__gap.md#ga1c864c4b183f9a86c9f70a11471c5b15)int [bt\_le\_ext\_adv\_stop](group__bt__gap.md#ga1c864c4b183f9a86c9f70a11471c5b15)(struct bt\_le\_ext\_adv \*adv);

1383

[ 1418](group__bt__gap.md#gad731f829b3566be3e56485b2a64f80b1)int [bt\_le\_ext\_adv\_set\_data](group__bt__gap.md#gad731f829b3566be3e56485b2a64f80b1)(struct bt\_le\_ext\_adv \*adv,

1419 const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len,

1420 const struct [bt\_data](structbt__data.md) \*sd, size\_t sd\_len);

1421

[ 1438](group__bt__gap.md#ga1aabdb81cb1a1841ff0fb91d849123fc)int [bt\_le\_ext\_adv\_update\_param](group__bt__gap.md#ga1aabdb81cb1a1841ff0fb91d849123fc)(struct bt\_le\_ext\_adv \*adv,

1439 const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param);

1440

[ 1449](group__bt__gap.md#ga62310a27f7fea925dfcf3abd7c454787)int [bt\_le\_ext\_adv\_delete](group__bt__gap.md#ga62310a27f7fea925dfcf3abd7c454787)(struct bt\_le\_ext\_adv \*adv);

1450

[ 1462](group__bt__gap.md#gaeb37d6cdd94a04b4cce8bc1e7aae70b4)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_le\_ext\_adv\_get\_index](group__bt__gap.md#gaeb37d6cdd94a04b4cce8bc1e7aae70b4)(struct bt\_le\_ext\_adv \*adv);

1463

[ 1465](structbt__le__ext__adv__info.md)struct [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md) {

1466 /\* Local identity \*/

[ 1467](structbt__le__ext__adv__info.md#a06aa727cd2523914bc7509713585bffd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__le__ext__adv__info.md#a06aa727cd2523914bc7509713585bffd);

1468

[ 1470](structbt__le__ext__adv__info.md#a485e4a8124fddee897fe744836cbfb24) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__ext__adv__info.md#a485e4a8124fddee897fe744836cbfb24);

1471

[ 1473](structbt__le__ext__adv__info.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__ext__adv__info.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9);

1474};

1475

[ 1484](group__bt__gap.md#gac06c9f55cf1da46e0d64b4d9af984ecb)int [bt\_le\_ext\_adv\_get\_info](group__bt__gap.md#gac06c9f55cf1da46e0d64b4d9af984ecb)(const struct bt\_le\_ext\_adv \*adv,

1485 struct [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md) \*info);

1486

[ 1500](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4)typedef void [bt\_le\_scan\_cb\_t](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) rssi,

1501 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adv\_type, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

1502

[ 1515](group__bt__gap.md#gaa72029a2759123ec776061d2e80bf3a1)int [bt\_le\_per\_adv\_set\_param](group__bt__gap.md#gaa72029a2759123ec776061d2e80bf3a1)(struct bt\_le\_ext\_adv \*adv,

1516 const struct [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md) \*param);

1517

[ 1531](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899)int [bt\_le\_per\_adv\_set\_data](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899)(const struct bt\_le\_ext\_adv \*adv,

1532 const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len);

1533

[ 1534](structbt__le__per__adv__subevent__data__params.md)struct [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md) {

[ 1536](structbt__le__per__adv__subevent__data__params.md#a55f2da6041b538b3bc4bff38cd4d2953) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__le__per__adv__subevent__data__params.md#a55f2da6041b538b3bc4bff38cd4d2953);

1537

[ 1539](structbt__le__per__adv__subevent__data__params.md#a1354e9505239de3c42969138d719d775) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_start](structbt__le__per__adv__subevent__data__params.md#a1354e9505239de3c42969138d719d775);

1540

[ 1542](structbt__le__per__adv__subevent__data__params.md#a86d858606943a82917835a0172e88663) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_count](structbt__le__per__adv__subevent__data__params.md#a86d858606943a82917835a0172e88663);

1543

[ 1545](structbt__le__per__adv__subevent__data__params.md#a46103c988d8ac360b7e26310a0322b4e) const struct [net\_buf\_simple](structnet__buf__simple.md) \*[data](structbt__le__per__adv__subevent__data__params.md#a46103c988d8ac360b7e26310a0322b4e);

1546};

1547

[ 1563](group__bt__gap.md#ga7de30fe5040b85bb9212e3a8fec4ac45)int [bt\_le\_per\_adv\_set\_subevent\_data](group__bt__gap.md#ga7de30fe5040b85bb9212e3a8fec4ac45)(const struct bt\_le\_ext\_adv \*adv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents,

1564 const struct [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md) \*params);

1565

[ 1583](group__bt__gap.md#ga0f23f4ed48e8679646f247ea0d687094)int [bt\_le\_per\_adv\_start](group__bt__gap.md#ga0f23f4ed48e8679646f247ea0d687094)(struct bt\_le\_ext\_adv \*adv);

1584

[ 1596](group__bt__gap.md#ga1b15206fc552d597c12af369d48ff7d5)int [bt\_le\_per\_adv\_stop](group__bt__gap.md#ga1b15206fc552d597c12af369d48ff7d5)(struct bt\_le\_ext\_adv \*adv);

1597

[ 1598](structbt__le__per__adv__sync__synced__info.md)struct [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md) {

[ 1600](structbt__le__per__adv__sync__synced__info.md#a7ca99b0596b08d153d3ba5310adab125) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__per__adv__sync__synced__info.md#a7ca99b0596b08d153d3ba5310adab125);

1601

[ 1603](structbt__le__per__adv__sync__synced__info.md#a5489c3038f7fff596316a456fc8d580b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__synced__info.md#a5489c3038f7fff596316a456fc8d580b);

1604

[ 1606](structbt__le__per__adv__sync__synced__info.md#a5304e1826face35c506f3b8f6cad7df2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__per__adv__sync__synced__info.md#a5304e1826face35c506f3b8f6cad7df2);

1607

[ 1609](structbt__le__per__adv__sync__synced__info.md#a8b7709011541e95ceaeac379cc3143bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__le__per__adv__sync__synced__info.md#a8b7709011541e95ceaeac379cc3143bb);

1610

[ 1612](structbt__le__per__adv__sync__synced__info.md#a0dd4b7646da0fadc48e94ff3dc91ef83) bool [recv\_enabled](structbt__le__per__adv__sync__synced__info.md#a0dd4b7646da0fadc48e94ff3dc91ef83);

1613

[ 1619](structbt__le__per__adv__sync__synced__info.md#adee2bdafa86a0c3c1dfb4660e85396a3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__le__per__adv__sync__synced__info.md#adee2bdafa86a0c3c1dfb4660e85396a3);

1620

[ 1627](structbt__le__per__adv__sync__synced__info.md#ada4cda53aa87f29d54f6cd88134efe14) struct bt\_conn \*[conn](structbt__le__per__adv__sync__synced__info.md#ada4cda53aa87f29d54f6cd88134efe14);

1628#if defined(CONFIG\_BT\_PER\_ADV\_SYNC\_RSP)

1630 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents;

1631

1633 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subevent\_interval;

1634

1636 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_delay;

1637

1639 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_spacing;

1640

1641#endif /\* CONFIG\_BT\_PER\_ADV\_SYNC\_RSP \*/

1642};

1643

[ 1644](structbt__le__per__adv__sync__term__info.md)struct [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md) {

[ 1646](structbt__le__per__adv__sync__term__info.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__per__adv__sync__term__info.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc);

1647

[ 1649](structbt__le__per__adv__sync__term__info.md#a7a5f2ecccaf698bad86f10d9a7d16189) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__term__info.md#a7a5f2ecccaf698bad86f10d9a7d16189);

1650

[ 1652](structbt__le__per__adv__sync__term__info.md#a429b8b665eacbfe9db013a571b829bac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__le__per__adv__sync__term__info.md#a429b8b665eacbfe9db013a571b829bac);

1653};

1654

[ 1655](structbt__le__per__adv__sync__recv__info.md)struct [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md) {

[ 1657](structbt__le__per__adv__sync__recv__info.md#a5817bd4fba2c93adebcebe007650b6eb) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__per__adv__sync__recv__info.md#a5817bd4fba2c93adebcebe007650b6eb);

1658

[ 1660](structbt__le__per__adv__sync__recv__info.md#a21b0ca87e46c6897282ebd877e45114e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__recv__info.md#a21b0ca87e46c6897282ebd877e45114e);

1661

[ 1663](structbt__le__per__adv__sync__recv__info.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__per__adv__sync__recv__info.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e);

1664

[ 1666](structbt__le__per__adv__sync__recv__info.md#aa17c9d917469f121448ed4e1db485700) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__le__per__adv__sync__recv__info.md#aa17c9d917469f121448ed4e1db485700);

1667

[ 1669](structbt__le__per__adv__sync__recv__info.md#a1591907e3cb1f4565b9d26c18bccc7d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__le__per__adv__sync__recv__info.md#a1591907e3cb1f4565b9d26c18bccc7d2);

1670#if defined(CONFIG\_BT\_PER\_ADV\_SYNC\_RSP)

1672 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) periodic\_event\_counter;

1673

1675 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subevent;

1676#endif /\* CONFIG\_BT\_PER\_ADV\_SYNC\_RSP \*/

1677};

1678

1679

[ 1680](structbt__le__per__adv__sync__state__info.md)struct [bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md) {

[ 1682](structbt__le__per__adv__sync__state__info.md#a4b0a3b7e36f935e06072304d6b92579f) bool [recv\_enabled](structbt__le__per__adv__sync__state__info.md#a4b0a3b7e36f935e06072304d6b92579f);

1683};

1684

[ 1685](structbt__le__per__adv__sync__cb.md)struct [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md) {

[ 1696](structbt__le__per__adv__sync__cb.md#a815be4343ab589df433a551663c5f4a1) void (\*[synced](structbt__le__per__adv__sync__cb.md#a815be4343ab589df433a551663c5f4a1))(struct bt\_le\_per\_adv\_sync \*sync,

1697 struct [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md) \*info);

1698

[ 1708](structbt__le__per__adv__sync__cb.md#acbd565a39918e5dfe7603a020e73daec) void (\*[term](structbt__le__per__adv__sync__cb.md#acbd565a39918e5dfe7603a020e73daec))(struct bt\_le\_per\_adv\_sync \*sync,

1709 const struct [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md) \*info);

1710

[ 1724](structbt__le__per__adv__sync__cb.md#a5576248e2eaef2afebe606e05e55f05f) void (\*[recv](structbt__le__per__adv__sync__cb.md#a5576248e2eaef2afebe606e05e55f05f))(struct bt\_le\_per\_adv\_sync \*sync,

1725 const struct [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md) \*info,

1726 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

1727

[ 1738](structbt__le__per__adv__sync__cb.md#a656b4802f79d4a472c2367ade144d72e) void (\*[state\_changed](structbt__le__per__adv__sync__cb.md#a656b4802f79d4a472c2367ade144d72e))(struct bt\_le\_per\_adv\_sync \*sync,

1739 const struct [bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md) \*info);

1740

[ 1751](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9) void (\*[biginfo](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9))(struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_iso\_biginfo](structbt__iso__biginfo.md) \*[biginfo](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9));

1752

[ 1760](structbt__le__per__adv__sync__cb.md#ad2dc168696fbd22f7e3a089ac56f62d7) void (\*[cte\_report\_cb](structbt__le__per__adv__sync__cb.md#ad2dc168696fbd22f7e3a089ac56f62d7))(struct bt\_le\_per\_adv\_sync \*sync,

1761 struct [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md) const \*info);

1762

[ 1763](structbt__le__per__adv__sync__cb.md#a1977d27941063773c953a5f1dfa9ca76) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__le__per__adv__sync__cb.md#a1977d27941063773c953a5f1dfa9ca76);

1764};

1765

1767enum {

[ 1769](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaeeef50a544edc104b39e4ef0c9a58d6c) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaeeef50a544edc104b39e4ef0c9a58d6c) = 0,

1770

[ 1777](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae9a88caa6a83da8b1697a6167629bf7e) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae9a88caa6a83da8b1697a6167629bf7e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

1778

[ 1784](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae35a6eb572a2842e4cc2fc3677e19b53) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae35a6eb572a2842e4cc2fc3677e19b53) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

1785

[ 1787](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa9ec2b0c346c2cab7f61c2efcc8e37db2) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa9ec2b0c346c2cab7f61c2efcc8e37db2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

1788

[ 1790](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaaa256e560f013eb74415d817154b8f4e) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaaa256e560f013eb74415d817154b8f4e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

1791

[ 1793](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa99034652a92249e6d04065d68352020b) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa99034652a92249e6d04065d68352020b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

1794

[ 1796](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa0f52e38e513ec7eefcbc5c86c36f002e) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa0f52e38e513ec7eefcbc5c86c36f002e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

1797

[ 1799](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa5c702876d70d5eadc4df6e59d96b8320) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa5c702876d70d5eadc4df6e59d96b8320) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

1800};

1801

[ 1802](structbt__le__per__adv__sync__param.md)struct [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md) {

[ 1809](structbt__le__per__adv__sync__param.md#ac93adedad747f61a771ac5445e486b74) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__le__per__adv__sync__param.md#ac93adedad747f61a771ac5445e486b74);

1810

[ 1817](structbt__le__per__adv__sync__param.md#a70795642ee94dd9e87f0cf251c095e7f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__param.md#a70795642ee94dd9e87f0cf251c095e7f);

1818

[ 1820](structbt__le__per__adv__sync__param.md#a4252f2b3b453c2f9c8fbf8c35a618ff2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__per__adv__sync__param.md#a4252f2b3b453c2f9c8fbf8c35a618ff2);

1821

[ 1829](structbt__le__per__adv__sync__param.md#af9abb65547fb5bfea65f4c22963c7da0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__le__per__adv__sync__param.md#af9abb65547fb5bfea65f4c22963c7da0);

1830

[ 1837](structbt__le__per__adv__sync__param.md#a301cfd3d6e5620d29c021ababe104754) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__per__adv__sync__param.md#a301cfd3d6e5620d29c021ababe104754);

1838};

1839

[ 1851](group__bt__gap.md#ga8d05bd864d98b5b43595eb256e464024)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_le\_per\_adv\_sync\_get\_index](group__bt__gap.md#ga8d05bd864d98b5b43595eb256e464024)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

1852

[ 1865](group__bt__gap.md#ga59532b37412b1b93f81cf5cc1bab0534)struct bt\_le\_per\_adv\_sync \*[bt\_le\_per\_adv\_sync\_lookup\_index](group__bt__gap.md#ga59532b37412b1b93f81cf5cc1bab0534)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index);

1866

[ 1868](structbt__le__per__adv__sync__info.md)struct [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md) {

[ 1870](structbt__le__per__adv__sync__info.md#ac10fc2e2d3ec2160db8c2aac148d18a2) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__le__per__adv__sync__info.md#ac10fc2e2d3ec2160db8c2aac148d18a2);

1871

[ 1873](structbt__le__per__adv__sync__info.md#acc0ef26c38279c9a67f8992005c2e58a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__info.md#acc0ef26c38279c9a67f8992005c2e58a);

1874

[ 1876](structbt__le__per__adv__sync__info.md#a365a0d8577429e4ee96e977071c9a906) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__per__adv__sync__info.md#a365a0d8577429e4ee96e977071c9a906);

1877

[ 1879](structbt__le__per__adv__sync__info.md#a4d9520ea6a803f8fe4f41190f55c26e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__le__per__adv__sync__info.md#a4d9520ea6a803f8fe4f41190f55c26e5);

1880};

1881

[ 1890](group__bt__gap.md#gabfaf265a48dd09ea02d114e2023c14a6)int [bt\_le\_per\_adv\_sync\_get\_info](group__bt__gap.md#gabfaf265a48dd09ea02d114e2023c14a6)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

1891 struct [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md) \*info);

1892

[ 1901](group__bt__gap.md#ga83126917373c0bcaa24964dd1d8bde46)struct bt\_le\_per\_adv\_sync \*[bt\_le\_per\_adv\_sync\_lookup\_addr](group__bt__gap.md#ga83126917373c0bcaa24964dd1d8bde46)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*adv\_addr,

1902 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid);

1903

[ 1920](group__bt__gap.md#ga061bf84b989b2c96ab51d2ca0debb017)int [bt\_le\_per\_adv\_sync\_create](group__bt__gap.md#ga061bf84b989b2c96ab51d2ca0debb017)(const struct [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md) \*param,

1921 struct bt\_le\_per\_adv\_sync \*\*out\_sync);

1922

[ 1939](group__bt__gap.md#gaa0c218ff3c78b26dcfaa726ee30267a6)int [bt\_le\_per\_adv\_sync\_delete](group__bt__gap.md#gaa0c218ff3c78b26dcfaa726ee30267a6)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

1940

[ 1955](group__bt__gap.md#ga4ee87bbf79e6ac844d14c3dafb2dadf4)int [bt\_le\_per\_adv\_sync\_cb\_register](group__bt__gap.md#ga4ee87bbf79e6ac844d14c3dafb2dadf4)(struct [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md) \*cb);

1956

[ 1966](group__bt__gap.md#ga07e4510de7e72c6ed6196b3da9fb40be)int [bt\_le\_per\_adv\_sync\_recv\_enable](group__bt__gap.md#ga07e4510de7e72c6ed6196b3da9fb40be)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

1967

[ 1977](group__bt__gap.md#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)int [bt\_le\_per\_adv\_sync\_recv\_disable](group__bt__gap.md#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

1978

1980enum {

[ 1982](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aef90aceabc3f9d0b17b7f3415152fca2) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aef90aceabc3f9d0b17b7f3415152fca2) = 0,

1983

[ 1989](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a2694870b7ebd2dcd0b3834367f7d7061) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a2694870b7ebd2dcd0b3834367f7d7061) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

1990

[ 1997](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ab0725048806858083be9ab3fcd9a36ed) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ab0725048806858083be9ab3fcd9a36ed) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

1998

[ 2005](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a433ae469b27e820fdfd2a1d562010991) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a433ae469b27e820fdfd2a1d562010991) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

2006

[ 2008](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aed2f78d682b5fbd1adf89c2f005e4f48) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aed2f78d682b5fbd1adf89c2f005e4f48) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

2009

[ 2016](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a3f0be549ca5cac1cfbdec2f2227e73dc) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a3f0be549ca5cac1cfbdec2f2227e73dc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

2017

[ 2024](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ad924f620ed6fdadbbea03f8e343b9d0c) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ad924f620ed6fdadbbea03f8e343b9d0c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

2025};

2026

[ 2027](structbt__le__per__adv__sync__transfer__param.md)struct [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md) {

[ 2034](structbt__le__per__adv__sync__transfer__param.md#a840e7cfac3a2947e5128d704067aaf7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__le__per__adv__sync__transfer__param.md#a840e7cfac3a2947e5128d704067aaf7e);

2035

[ 2042](structbt__le__per__adv__sync__transfer__param.md#a5bfa84c6bdacdf8893a0951a5ce71fc6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__per__adv__sync__transfer__param.md#a5bfa84c6bdacdf8893a0951a5ce71fc6);

2043

[ 2045](structbt__le__per__adv__sync__transfer__param.md#a0b3ee6df1b409e64a064ffb6ac632cce) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__per__adv__sync__transfer__param.md#a0b3ee6df1b409e64a064ffb6ac632cce);

2046};

2047

[ 2060](group__bt__gap.md#gaf81a1dd7a628d1a2f25c6b53b0679809)int [bt\_le\_per\_adv\_sync\_transfer](group__bt__gap.md#gaf81a1dd7a628d1a2f25c6b53b0679809)(const struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

2061 const struct bt\_conn \*conn,

2062 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) service\_data);

2063

2064

[ 2077](group__bt__gap.md#gac96199a4e5e6cfb789c1bd1c0e67d6fe)int [bt\_le\_per\_adv\_set\_info\_transfer](group__bt__gap.md#gac96199a4e5e6cfb789c1bd1c0e67d6fe)(const struct bt\_le\_ext\_adv \*adv,

2078 const struct bt\_conn \*conn,

2079 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) service\_data);

2080

[ 2094](group__bt__gap.md#gaa0658bd53df1d5e8e89e13330e4fd0ae)int [bt\_le\_per\_adv\_sync\_transfer\_subscribe](group__bt__gap.md#gaa0658bd53df1d5e8e89e13330e4fd0ae)(

2095 const struct bt\_conn \*conn,

2096 const struct [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md) \*param);

2097

[ 2111](group__bt__gap.md#ga08f872078045bbef4aca19761f25eeb8)int [bt\_le\_per\_adv\_sync\_transfer\_unsubscribe](group__bt__gap.md#ga08f872078045bbef4aca19761f25eeb8)(const struct bt\_conn \*conn);

2112

[ 2126](group__bt__gap.md#ga27c4961f3c7270a7f1caeadb4107854b)int [bt\_le\_per\_adv\_list\_add](group__bt__gap.md#ga27c4961f3c7270a7f1caeadb4107854b)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid);

2127

[ 2139](group__bt__gap.md#ga100efac4a49984e06202c63c4e5955cd)int [bt\_le\_per\_adv\_list\_remove](group__bt__gap.md#ga100efac4a49984e06202c63c4e5955cd)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid);

2140

[ 2148](group__bt__gap.md#ga5909bd768c23a19a42a660e3b814c981)int [bt\_le\_per\_adv\_list\_clear](group__bt__gap.md#ga5909bd768c23a19a42a660e3b814c981)(void);

2149

2150

2151enum {

[ 2153](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3aad3f19e5849b6d6813fa88257082e185) [BT\_LE\_SCAN\_OPT\_NONE](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3aad3f19e5849b6d6813fa88257082e185) = 0,

2154

[ 2156](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394) [BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

2157

[ 2159](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae) [BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

2160

[ 2162](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb) [BT\_LE\_SCAN\_OPT\_CODED](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

2163

[ 2169](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a7ff0c79b2675e7b7512379e2cbedc0a6) [BT\_LE\_SCAN\_OPT\_NO\_1M](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a7ff0c79b2675e7b7512379e2cbedc0a6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

2170};

2171

2172enum {

[ 2174](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006) [BT\_LE\_SCAN\_TYPE\_PASSIVE](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006) = 0x00,

2175

[ 2183](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22) [BT\_LE\_SCAN\_TYPE\_ACTIVE](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22) = 0x01,

2184};

2185

[ 2187](structbt__le__scan__param.md)struct [bt\_le\_scan\_param](structbt__le__scan__param.md) {

[ 2189](structbt__le__scan__param.md#a02d75322390287c3fa754bf915660d0c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__le__scan__param.md#a02d75322390287c3fa754bf915660d0c);

2190

[ 2192](structbt__le__scan__param.md#ac815b05fee8ce0dd24228305b7596207) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [options](structbt__le__scan__param.md#ac815b05fee8ce0dd24228305b7596207);

2193

[ 2202](structbt__le__scan__param.md#a2f4e053d97c62b6fdf42a245908607f8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__scan__param.md#a2f4e053d97c62b6fdf42a245908607f8);

2203

[ 2212](structbt__le__scan__param.md#a37a7ee82e86a91cf7a9c2adf60bb526a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window](structbt__le__scan__param.md#a37a7ee82e86a91cf7a9c2adf60bb526a);

2213

[ 2220](structbt__le__scan__param.md#a3e71ce551dcc7762c29e2316996e2912) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__scan__param.md#a3e71ce551dcc7762c29e2316996e2912);

2221

[ 2227](structbt__le__scan__param.md#a67a20bc94a3d98fa10af7b5b42dde328) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_coded](structbt__le__scan__param.md#a67a20bc94a3d98fa10af7b5b42dde328);

2228

[ 2234](structbt__le__scan__param.md#a93166af55dca71393c60cb3f7ac6d809) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window\_coded](structbt__le__scan__param.md#a93166af55dca71393c60cb3f7ac6d809);

2235};

2236

[ 2238](structbt__le__scan__recv__info.md)struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) {

[ 2245](structbt__le__scan__recv__info.md#a907fb7ec3c78d68da5015a8c3afc3084) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__scan__recv__info.md#a907fb7ec3c78d68da5015a8c3afc3084);

2246

[ 2248](structbt__le__scan__recv__info.md#a4df8d4e1fdd7514d170744856ebe7015) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__scan__recv__info.md#a4df8d4e1fdd7514d170744856ebe7015);

2249

[ 2251](structbt__le__scan__recv__info.md#a88f677733147245ccbf861c7fc5e0f11) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__le__scan__recv__info.md#a88f677733147245ccbf861c7fc5e0f11);

2252

[ 2254](structbt__le__scan__recv__info.md#a2addeba6d2ec8e55dc5379adf6519148) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__scan__recv__info.md#a2addeba6d2ec8e55dc5379adf6519148);

2255

[ 2264](structbt__le__scan__recv__info.md#adccb2ce5c6d228bd7f8f050088629524) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_type](structbt__le__scan__recv__info.md#adccb2ce5c6d228bd7f8f050088629524);

2265

[ 2274](structbt__le__scan__recv__info.md#af29ddfb59e286af9ca465cbd5a91bf2d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [adv\_props](structbt__le__scan__recv__info.md#af29ddfb59e286af9ca465cbd5a91bf2d);

2275

[ 2281](structbt__le__scan__recv__info.md#a1060c5937708ff81a64f068e02fc7826) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__scan__recv__info.md#a1060c5937708ff81a64f068e02fc7826);

2282

[ 2284](structbt__le__scan__recv__info.md#a6189ed8453cb7907f34dc7dfaf1343bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [primary\_phy](structbt__le__scan__recv__info.md#a6189ed8453cb7907f34dc7dfaf1343bd);

2285

[ 2287](structbt__le__scan__recv__info.md#ac797291291dc7ba7ac171ed7f24f0d16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [secondary\_phy](structbt__le__scan__recv__info.md#ac797291291dc7ba7ac171ed7f24f0d16);

2288};

2289

[ 2291](structbt__le__scan__cb.md)struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) {

2292

[ 2299](structbt__le__scan__cb.md#a71d73c1da28d4a27626f77d96a5b3541) void (\*[recv](structbt__le__scan__cb.md#a71d73c1da28d4a27626f77d96a5b3541))(const struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) \*info,

2300 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

2301

[ 2303](structbt__le__scan__cb.md#a2f57f3fee46bd137065f4c57d0cd5157) void (\*[timeout](structbt__le__scan__cb.md#a2f57f3fee46bd137065f4c57d0cd5157))(void);

2304

[ 2305](structbt__le__scan__cb.md#a50dbc5e7618fd488e9acb7ad8f104a63) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__le__scan__cb.md#a50dbc5e7618fd488e9acb7ad8f104a63);

2306};

2307

[ 2317](group__bt__gap.md#gac9f372ca16afb1c2f0e100c5b1b94cd5)#define BT\_LE\_SCAN\_PARAM\_INIT(\_type, \_options, \_interval, \_window) \

2318{ \

2319 .type = (\_type), \

2320 .options = (\_options), \

2321 .interval = (\_interval), \

2322 .window = (\_window), \

2323 .timeout = 0, \

2324 .interval\_coded = 0, \

2325 .window\_coded = 0, \

2326}

2327

[ 2337](group__bt__gap.md#ga57ace75133343ba8de7fa965f452ee3d)#define BT\_LE\_SCAN\_PARAM(\_type, \_options, \_interval, \_window) \

2338 ((struct bt\_le\_scan\_param[]) { \

2339 BT\_LE\_SCAN\_PARAM\_INIT(\_type, \_options, \_interval, \_window) \

2340 })

2341

[ 2345](group__bt__gap.md#gac137ea4ce32697582a337116ffa41da5)#define BT\_LE\_SCAN\_ACTIVE BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_ACTIVE, \

2346 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2347 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2348 BT\_GAP\_SCAN\_FAST\_WINDOW)

2349

[ 2355](group__bt__gap.md#ga9bd9701db0459c066ed7c18343f60911)#define BT\_LE\_SCAN\_ACTIVE\_CONTINUOUS BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_ACTIVE, \

2356 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2357 BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN, \

2358 BT\_GAP\_SCAN\_FAST\_WINDOW)

2359BUILD\_ASSERT([BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0) == [BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN](group__bt__gap__defines.md#gae9356673ee78d9abb27891738344513a),

2360 "Continuous scanning is requested by setting window and interval equal.");

2361

[ 2368](group__bt__gap.md#ga8ceaef6f0fbf4fe2d76d47e8f59aeb11)#define BT\_LE\_SCAN\_PASSIVE BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_PASSIVE, \

2369 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2370 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2371 BT\_GAP\_SCAN\_FAST\_WINDOW)

2372

[ 2379](group__bt__gap.md#ga8d8ccc9ea1db2c96deae1603ec1c78a3)#define BT\_LE\_SCAN\_PASSIVE\_CONTINUOUS BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_PASSIVE, \

2380 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2381 BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN, \

2382 BT\_GAP\_SCAN\_FAST\_WINDOW)

2383BUILD\_ASSERT([BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0) == [BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN](group__bt__gap__defines.md#gae9356673ee78d9abb27891738344513a),

2384 "Continuous scanning is requested by setting window and interval equal.");

2385

[ 2390](group__bt__gap.md#ga06380c4ae6289c704a143b9d192bc35f)#define BT\_LE\_SCAN\_CODED\_ACTIVE \

2391 BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_ACTIVE, \

2392 BT\_LE\_SCAN\_OPT\_CODED | \

2393 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2394 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2395 BT\_GAP\_SCAN\_FAST\_WINDOW)

2396

[ 2404](group__bt__gap.md#ga1e5a4589304babc6b0d49019ebcff6b0)#define BT\_LE\_SCAN\_CODED\_PASSIVE \

2405 BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_PASSIVE, \

2406 BT\_LE\_SCAN\_OPT\_CODED | \

2407 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2408 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2409 BT\_GAP\_SCAN\_FAST\_WINDOW)

2410

[ 2437](group__bt__gap.md#gac5e19c26b53a08dadb8efa7ecc692ad6)int [bt\_le\_scan\_start](group__bt__gap.md#gac5e19c26b53a08dadb8efa7ecc692ad6)(const struct [bt\_le\_scan\_param](structbt__le__scan__param.md) \*param, [bt\_le\_scan\_cb\_t](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4) cb);

2438

[ 2447](group__bt__gap.md#gaa2de1a1ab523606b36a4c445fb0c3b84)int [bt\_le\_scan\_stop](group__bt__gap.md#gaa2de1a1ab523606b36a4c445fb0c3b84)(void);

2448

[ 2463](group__bt__gap.md#ga80e870fa1de40c404c64624bef439067)int [bt\_le\_scan\_cb\_register](group__bt__gap.md#ga80e870fa1de40c404c64624bef439067)(struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \*cb);

2464

[ 2472](group__bt__gap.md#gac2718f2128b3f8c79b12d760771c8378)void [bt\_le\_scan\_cb\_unregister](group__bt__gap.md#gac2718f2128b3f8c79b12d760771c8378)(struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \*cb);

2473

[ 2488](group__bt__gap.md#ga40f2f7fdb09aba3c5137f680e67792f0)int [bt\_le\_filter\_accept\_list\_add](group__bt__gap.md#ga40f2f7fdb09aba3c5137f680e67792f0)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

2489

[ 2504](group__bt__gap.md#ga0532ed768ab4f9d69c202066d2f87e66)int [bt\_le\_filter\_accept\_list\_remove](group__bt__gap.md#ga0532ed768ab4f9d69c202066d2f87e66)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

2505

[ 2518](group__bt__gap.md#gac87df899d1e363c63162988157ee6d00)int [bt\_le\_filter\_accept\_list\_clear](group__bt__gap.md#gac87df899d1e363c63162988157ee6d00)(void);

2519

[ 2528](group__bt__gap.md#gabc115fd3fff6d00ae878a31613bf70aa)int [bt\_le\_set\_chan\_map](group__bt__gap.md#gabc115fd3fff6d00ae878a31613bf70aa)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_map[5]);

2529

[ 2548](group__bt__gap.md#ga9ab41e118b5496c196e56b8b5d023275)int [bt\_le\_set\_rpa\_timeout](group__bt__gap.md#ga9ab41e118b5496c196e56b8b5d023275)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) new\_rpa\_timeout);

2549

[ 2567](group__bt__gap.md#ga652eef01e5256e0d820cd1f4db877429)void [bt\_data\_parse](group__bt__gap.md#ga652eef01e5256e0d820cd1f4db877429)(struct [net\_buf\_simple](structnet__buf__simple.md) \*ad,

2568 bool (\*func)(struct [bt\_data](structbt__data.md) \*[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1), void \*user\_data),

2569 void \*user\_data);

2570

[ 2572](structbt__le__oob__sc__data.md)struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) {

[ 2574](structbt__le__oob__sc__data.md#afa64bcc048d0e8709e262e2848a39d2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [r](structbt__le__oob__sc__data.md#afa64bcc048d0e8709e262e2848a39d2c)[16];

2575

[ 2577](structbt__le__oob__sc__data.md#a9bd93f1e9e41e241d0f84ae16ae47ba1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c](structbt__le__oob__sc__data.md#a9bd93f1e9e41e241d0f84ae16ae47ba1)[16];

2578};

2579

[ 2581](structbt__le__oob.md)struct [bt\_le\_oob](structbt__le__oob.md) {

[ 2585](structbt__le__oob.md#a17cfed7683efbf5b5954847d655d7424) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__le__oob.md#a17cfed7683efbf5b5954847d655d7424);

2586

[ 2588](structbt__le__oob.md#a80ccd4ab120a880adfff9aba3b19b4fd) struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) [le\_sc\_data](structbt__le__oob.md#a80ccd4ab120a880adfff9aba3b19b4fd);

2589};

2590

[ 2619](group__bt__gap.md#ga296d1adf3c9ed2f2c65bb75b887d59ee)int [bt\_le\_oob\_get\_local](group__bt__gap.md#ga296d1adf3c9ed2f2c65bb75b887d59ee)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, struct [bt\_le\_oob](structbt__le__oob.md) \*oob);

2620

[ 2645](group__bt__gap.md#ga7486aab863ca497a50dacf81657f48d4)int [bt\_le\_ext\_adv\_oob\_get\_local](group__bt__gap.md#ga7486aab863ca497a50dacf81657f48d4)(struct bt\_le\_ext\_adv \*adv,

2646 struct [bt\_le\_oob](structbt__le__oob.md) \*oob);

2647

[ 2657](group__bt__gap.md#gaceabbbe6e844650f791010e53c9df6a4)int [bt\_unpair](group__bt__gap.md#gaceabbbe6e844650f791010e53c9df6a4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

2658

[ 2660](structbt__bond__info.md)struct [bt\_bond\_info](structbt__bond__info.md) {

[ 2662](structbt__bond__info.md#a6b328ce30fd53bb73ecd8e033bb91d1f) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__bond__info.md#a6b328ce30fd53bb73ecd8e033bb91d1f);

2663};

2664

[ 2672](group__bt__gap.md#gaad380b7f8984f8522c1b79f9bdc04905)void [bt\_foreach\_bond](group__bt__gap.md#gaad380b7f8984f8522c1b79f9bdc04905)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, void (\*func)(const struct [bt\_bond\_info](structbt__bond__info.md) \*info,

2673 void \*user\_data),

2674 void \*user\_data);

2675

[ 2690](group__bt__gap.md#ga8046c2b06d3dad0d6c8184de492517d2)int [bt\_configure\_data\_path](group__bt__gap.md#ga8046c2b06d3dad0d6c8184de492517d2)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dir, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vs\_config\_len,

2691 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vs\_config);

2692

[ 2693](structbt__le__per__adv__sync__subevent__params.md)struct [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md) {

[ 2699](structbt__le__per__adv__sync__subevent__params.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [properties](structbt__le__per__adv__sync__subevent__params.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4);

2700

[ 2702](structbt__le__per__adv__sync__subevent__params.md#a867c66bf09461a4369da3d250701d2ae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__le__per__adv__sync__subevent__params.md#a867c66bf09461a4369da3d250701d2ae);

2703

[ 2709](structbt__le__per__adv__sync__subevent__params.md#a5ac4e81ddd63797f921105748344c125) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[subevents](structbt__le__per__adv__sync__subevent__params.md#a5ac4e81ddd63797f921105748344c125);

2710};

2711

[ 2722](group__bt__gap.md#ga731f4b37a9e5cc13a6816ea23f751b0b)int [bt\_le\_per\_adv\_sync\_subevent](group__bt__gap.md#ga731f4b37a9e5cc13a6816ea23f751b0b)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

2723 struct [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md) \*params);

2724

[ 2725](structbt__le__per__adv__response__params.md)struct [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md) {

[ 2734](structbt__le__per__adv__response__params.md#a1af01d0a027fb8659615874acbd388f9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [request\_event](structbt__le__per__adv__response__params.md#a1af01d0a027fb8659615874acbd388f9);

2735

[ 2741](structbt__le__per__adv__response__params.md#a3fc8ab0feb06714b28d22439cce60e41) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [request\_subevent](structbt__le__per__adv__response__params.md#a3fc8ab0feb06714b28d22439cce60e41);

2742

[ 2744](structbt__le__per__adv__response__params.md#a0cec222d5ba8cc9e20939d441646c913) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_subevent](structbt__le__per__adv__response__params.md#a0cec222d5ba8cc9e20939d441646c913);

2745

[ 2747](structbt__le__per__adv__response__params.md#aea0428083ccd5f4dccc17e494f38b7c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot](structbt__le__per__adv__response__params.md#aea0428083ccd5f4dccc17e494f38b7c3);

2748};

2749

[ 2762](group__bt__gap.md#gaae6b8583f7d5457f20b03dccd146425e)int [bt\_le\_per\_adv\_set\_response\_data](group__bt__gap.md#gaae6b8583f7d5457f20b03dccd146425e)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

2763 const struct [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md) \*params,

2764 const struct [net\_buf\_simple](structnet__buf__simple.md) \*data);

2765

2769

2770#ifdef \_\_cplusplus

2771}

2772#endif

2776

2777#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_BLUETOOTH\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[crypto.h](bluetooth_2crypto_8h.md)

Bluetooth subsystem crypto APIs.

[classic.h](classic_8h.md)

Bluetooth subsystem classic core APIs.

[gap.h](gap_8h.md)

Bluetooth Generic Access Profile defines and Assigned Numbers.

[BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0)

#define BT\_GAP\_SCAN\_FAST\_WINDOW

**Definition** gap.h:719

[BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN](group__bt__gap__defines.md#gae9356673ee78d9abb27891738344513a)

#define BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN

**Definition** gap.h:717

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

[bt\_le\_per\_adv\_start](group__bt__gap.md#ga0f23f4ed48e8679646f247ea0d687094)

int bt\_le\_per\_adv\_start(struct bt\_le\_ext\_adv \*adv)

Starts periodic advertising.

[bt\_le\_per\_adv\_list\_remove](group__bt__gap.md#ga100efac4a49984e06202c63c4e5955cd)

int bt\_le\_per\_adv\_list\_remove(const bt\_addr\_le\_t \*addr, uint8\_t sid)

Remove a device from the periodic advertising list.

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

**Definition** bluetooth.h:1500

[bt\_le\_ext\_adv\_stop](group__bt__gap.md#ga1c864c4b183f9a86c9f70a11471c5b15)

int bt\_le\_ext\_adv\_stop(struct bt\_le\_ext\_adv \*adv)

Stop advertising with the given advertising set.

[bt\_le\_per\_adv\_list\_add](group__bt__gap.md#ga27c4961f3c7270a7f1caeadb4107854b)

int bt\_le\_per\_adv\_list\_add(const bt\_addr\_le\_t \*addr, uint8\_t sid)

Add a device to the periodic advertising list.

[bt\_le\_oob\_get\_local](group__bt__gap.md#ga296d1adf3c9ed2f2c65bb75b887d59ee)

int bt\_le\_oob\_get\_local(uint8\_t id, struct bt\_le\_oob \*oob)

Get local LE Out of Band (OOB) information.

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

[bt\_le\_per\_adv\_sync\_cb\_register](group__bt__gap.md#ga4ee87bbf79e6ac844d14c3dafb2dadf4)

int bt\_le\_per\_adv\_sync\_cb\_register(struct bt\_le\_per\_adv\_sync\_cb \*cb)

Register periodic advertising sync callbacks.

[bt\_ready\_cb\_t](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb)

void(\* bt\_ready\_cb\_t)(int err)

Callback for notifying that Bluetooth has been enabled.

**Definition** bluetooth.h:207

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

[bt\_le\_scan\_cb\_register](group__bt__gap.md#ga80e870fa1de40c404c64624bef439067)

int bt\_le\_scan\_cb\_register(struct bt\_le\_scan\_cb \*cb)

Register scanner packet callbacks.

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

[bt\_le\_ext\_adv\_set\_data](group__bt__gap.md#gad731f829b3566be3e56485b2a64f80b1)

int bt\_le\_ext\_adv\_set\_data(struct bt\_le\_ext\_adv \*adv, const struct bt\_data \*ad, size\_t ad\_len, const struct bt\_data \*sd, size\_t sd\_len)

Set an advertising set's advertising or scan response data.

[bt\_get\_name](group__bt__gap.md#gad922d894b25e86de3f81ce77200a13fd)

const char \* bt\_get\_name(void)

Get Bluetooth Device Name.

[bt\_id\_create](group__bt__gap.md#gae11eb8ad254418c38a0e8689df25a159)

int bt\_id\_create(bt\_addr\_le\_t \*addr, uint8\_t \*irk)

Create a new identity.

[bt\_le\_ext\_adv\_get\_index](group__bt__gap.md#gaeb37d6cdd94a04b4cce8bc1e7aae70b4)

uint8\_t bt\_le\_ext\_adv\_get\_index(struct bt\_le\_ext\_adv \*adv)

Get array index of an advertising set.

[bt\_set\_appearance](group__bt__gap.md#gaf0729453790aab1bd3d52c623be3b35a)

int bt\_set\_appearance(uint16\_t new\_appearance)

Set local Bluetooth appearance.

[bt\_le\_ext\_adv\_start](group__bt__gap.md#gaf0f436c55482d9429f674303ae3aa815)

int bt\_le\_ext\_adv\_start(struct bt\_le\_ext\_adv \*adv, const struct bt\_le\_ext\_adv\_start\_param \*param)

Start advertising with the given advertising set.

[bt\_id\_delete](group__bt__gap.md#gaf6cd906690a51ebed04bea4f4ef716ff)

int bt\_id\_delete(uint8\_t id)

Delete an identity.

[bt\_le\_per\_adv\_sync\_transfer](group__bt__gap.md#gaf81a1dd7a628d1a2f25c6b53b0679809)

int bt\_le\_per\_adv\_sync\_transfer(const struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, const struct bt\_conn \*conn, uint16\_t service\_data)

Transfer the periodic advertising sync information to a peer device.

[bt\_le\_per\_adv\_set\_data](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899)

int bt\_le\_per\_adv\_set\_data(const struct bt\_le\_ext\_adv \*adv, const struct bt\_data \*ad, size\_t ad\_len)

Set or update the periodic advertising data.

[BT\_LE\_SCAN\_TYPE\_PASSIVE](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006)

@ BT\_LE\_SCAN\_TYPE\_PASSIVE

Scan without requesting additional information from advertisers.

**Definition** bluetooth.h:2174

[BT\_LE\_SCAN\_TYPE\_ACTIVE](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22)

@ BT\_LE\_SCAN\_TYPE\_ACTIVE

Scan and request additional information from advertisers.

**Definition** bluetooth.h:2183

[BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa38cebc2ae885ff630b34c603e2ec6403)

@ BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI

Advertise with included AdvDataInfo (ADI).

**Definition** bluetooth.h:909

[BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa9524537e4cb726f4ff10ba93381bb27f)

@ BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER

Advertise with transmit power.

**Definition** bluetooth.h:902

[BT\_LE\_PER\_ADV\_OPT\_NONE](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aaa2c689d726eacfb18d87655b1f587518)

@ BT\_LE\_PER\_ADV\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:895

[BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394)

@ BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE

Filter duplicates.

**Definition** bluetooth.h:2156

[BT\_LE\_SCAN\_OPT\_CODED](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb)

@ BT\_LE\_SCAN\_OPT\_CODED

Enable scan on coded PHY (Long Range).

**Definition** bluetooth.h:2162

[BT\_LE\_SCAN\_OPT\_NO\_1M](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a7ff0c79b2675e7b7512379e2cbedc0a6)

@ BT\_LE\_SCAN\_OPT\_NO\_1M

Disable scan on 1M phy.

**Definition** bluetooth.h:2169

[BT\_LE\_SCAN\_OPT\_NONE](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3aad3f19e5849b6d6813fa88257082e185)

@ BT\_LE\_SCAN\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:2153

[BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae)

@ BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST

Filter using filter accept list.

**Definition** bluetooth.h:2159

[BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73)

@ BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD

Put GAP device name into advert data.

**Definition** bluetooth.h:772

[BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea1563b053f457833d1a3d11c8dc4d394b)

@ BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ

Notify the application when a scan response data has been sent to an active scanner.

**Definition** bluetooth.h:676

[BT\_LE\_ADV\_OPT\_ANONYMOUS](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea185e0f884f8b0ce79625448638de8fab)

@ BT\_LE\_ADV\_OPT\_ANONYMOUS

Advertise without a device address (identity or RPA).

**Definition** bluetooth.h:743

[BT\_LE\_ADV\_OPT\_USE\_NRPA](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea22958d8539d661ad7ca8d3f1173e7e5e)

@ BT\_LE\_ADV\_OPT\_USE\_NRPA

Advertise using a Non-Resolvable Private Address.

**Definition** bluetooth.h:786

[BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3)

@ BT\_LE\_ADV\_OPT\_CONNECTABLE

Advertise as connectable.

**Definition** bluetooth.h:545

[BT\_LE\_ADV\_OPT\_USE\_NAME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398)

@ BT\_LE\_ADV\_OPT\_USE\_NAME

Advertise using GAP device name.

**Definition** bluetooth.h:641

[BT\_LE\_ADV\_OPT\_USE\_IDENTITY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e)

@ BT\_LE\_ADV\_OPT\_USE\_IDENTITY

Advertise using identity address.

**Definition** bluetooth.h:615

[BT\_LE\_ADV\_OPT\_ONE\_TIME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2)

@ BT\_LE\_ADV\_OPT\_ONE\_TIME

Advertise one time.

**Definition** bluetooth.h:575

[BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea807ba316edc49c8448a8ff7d497173f5)

@ BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ

Use filter accept list to filter devices that can request scan response data.

**Definition** bluetooth.h:668

[BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea89f7494620236c976bf1a76a880e2a28)

@ BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39

Disable advertising on channel index 39.

**Definition** bluetooth.h:759

[BT\_LE\_ADV\_OPT\_NONE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea928b376123819cb0a69fbb5b35608dbf)

@ BT\_LE\_ADV\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:523

[BT\_LE\_ADV\_OPT\_REQUIRE\_S2\_CODING](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea9a35ede118224d6ed17f252fff6bb47e)

@ BT\_LE\_ADV\_OPT\_REQUIRE\_S2\_CODING

Configures the advertiser to use the S=2 coding scheme for LE Coded PHY.

**Definition** bluetooth.h:803

[BT\_LE\_ADV\_OPT\_CONN](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169)

@ BT\_LE\_ADV\_OPT\_CONN

Connectable advertising.

**Definition** bluetooth.h:603

[BT\_LE\_ADV\_OPT\_REQUIRE\_S8\_CODING](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa6a61768ad4102f199d3970791118bb8)

@ BT\_LE\_ADV\_OPT\_REQUIRE\_S8\_CODING

Configures the advertiser to use the S=8 coding scheme for LE Coded PHY.

**Definition** bluetooth.h:820

[BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeab46741616f8bfe50c4b492d1f7970779)

@ BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37

Disable advertising on channel index 37.

**Definition** bluetooth.h:753

[BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabd9cb02691d7e025fe3fea9a80123275)

@ BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38

Disable advertising on channel index 38.

**Definition** bluetooth.h:756

[BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabdcf1c80662061fa30575e1f9fc6cf6f)

@ BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA

Directed advertising to privacy-enabled peer.

**Definition** bluetooth.h:663

[BT\_LE\_ADV\_OPT\_CODED](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1)

@ BT\_LE\_ADV\_OPT\_CODED

Advertise on the LE Coded PHY (Long Range).

**Definition** bluetooth.h:736

[BT\_LE\_ADV\_OPT\_FILTER\_CONN](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead5efef3d01731110dbd71d5a5dc9baaf)

@ BT\_LE\_ADV\_OPT\_FILTER\_CONN

Use filter accept list to filter devices that can connect.

**Definition** bluetooth.h:671

[BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab)

@ BT\_LE\_ADV\_OPT\_EXT\_ADV

Advertise with extended advertising.

**Definition** bluetooth.h:708

[BT\_LE\_ADV\_OPT\_SCANNABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9)

@ BT\_LE\_ADV\_OPT\_SCANNABLE

Support scan response data.

**Definition** bluetooth.h:686

[BT\_LE\_ADV\_OPT\_NO\_2M](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae864aefcdfbecaffe823b9b144fe0a6b)

@ BT\_LE\_ADV\_OPT\_NO\_2M

Disable use of LE 2M PHY on the secondary advertising channel.

**Definition** bluetooth.h:724

[BT\_LE\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaecff4fe3ac3d1fba3f6fa76c77713859)

@ BT\_LE\_ADV\_OPT\_USE\_TX\_POWER

Advertise with transmit power.

**Definition** bluetooth.h:750

[BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeafd164ec5476f5e2d9aedf50032946872)

@ BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY

Low duty cycle directed advertising.

**Definition** bluetooth.h:649

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a2694870b7ebd2dcd0b3834367f7d7061)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA

No Angle of Arrival (AoA).

**Definition** bluetooth.h:1989

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a3f0be549ca5cac1cfbdec2f2227e73dc)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED

Sync to received PAST packets but don't generate sync reports.

**Definition** bluetooth.h:2016

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a433ae469b27e820fdfd2a1d562010991)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US

No Angle of Departure (AoD) 2.

**Definition** bluetooth.h:2005

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ab0725048806858083be9ab3fcd9a36ed)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US

No Angle of Departure (AoD) 1 us.

**Definition** bluetooth.h:1997

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ad924f620ed6fdadbbea03f8e343b9d0c)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES

Sync to received PAST packets and generate sync reports with duplicate filtering.

**Definition** bluetooth.h:2024

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aed2f78d682b5fbd1adf89c2f005e4f48)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE

Only sync to packets with constant tone extension.

**Definition** bluetooth.h:2008

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aef90aceabc3f9d0b17b7f3415152fca2)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:1982

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa0f52e38e513ec7eefcbc5c86c36f002e)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US

Sync with Angle of Departure (AoD) 2 us constant tone extension.

**Definition** bluetooth.h:1796

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa5c702876d70d5eadc4df6e59d96b8320)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT

Do not sync to packets without a constant tone extension.

**Definition** bluetooth.h:1799

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa99034652a92249e6d04065d68352020b)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US

Sync with Angle of Departure (AoD) 1 us constant tone extension.

**Definition** bluetooth.h:1793

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa9ec2b0c346c2cab7f61c2efcc8e37db2)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE

Filter duplicate Periodic Advertising reports.

**Definition** bluetooth.h:1787

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaaa256e560f013eb74415d817154b8f4e)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA

Sync with Angle of Arrival (AoA) constant tone extension.

**Definition** bluetooth.h:1790

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae35a6eb572a2842e4cc2fc3677e19b53)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED

Disables periodic advertising reports.

**Definition** bluetooth.h:1784

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae9a88caa6a83da8b1697a6167629bf7e)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST

Use the periodic advertising list to sync with advertiser.

**Definition** bluetooth.h:1777

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaeeef50a544edc104b39e4ef0c9a58d6c)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:1769

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[net\_buf.h](net__buf_8h.md)

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

[bt\_bond\_info](structbt__bond__info.md)

Information about a bond with a remote device.

**Definition** bluetooth.h:2660

[bt\_bond\_info::addr](structbt__bond__info.md#a6b328ce30fd53bb73ecd8e033bb91d1f)

bt\_addr\_le\_t addr

Address of the remote device.

**Definition** bluetooth.h:2662

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:456

[bt\_data::type](structbt__data.md#a984aecb40a4993ffa113be53942db065)

uint8\_t type

**Definition** bluetooth.h:457

[bt\_data::data\_len](structbt__data.md#abda19091a1b8f99d385f11772ef34d5f)

uint8\_t data\_len

**Definition** bluetooth.h:458

[bt\_data::data](structbt__data.md#ac80ec10101ad69a86f703a4e652c7826)

const uint8\_t \* data

**Definition** bluetooth.h:459

[bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md)

**Definition** direction.h:115

[bt\_iso\_biginfo](structbt__iso__biginfo.md)

Broadcast Isochronous Group (BIG) information.

**Definition** iso.h:628

[bt\_le\_adv\_param](structbt__le__adv__param.md)

LE Advertising Parameters.

**Definition** bluetooth.h:824

[bt\_le\_adv\_param::options](structbt__le__adv__param.md#a2a978c60153eb03697769bc72928f4ef)

uint32\_t options

Bit-field of advertising options.

**Definition** bluetooth.h:853

[bt\_le\_adv\_param::peer](structbt__le__adv__param.md#a4cf31f54f067fffa3c848adc2ffd7119)

const bt\_addr\_le\_t \* peer

Directed advertising to peer.

**Definition** bluetooth.h:888

[bt\_le\_adv\_param::sid](structbt__le__adv__param.md#a6e2f0e1b76495afe7fe661e8698d0909)

uint8\_t sid

Advertising Set Identifier, valid range 0x00 - 0x0f.

**Definition** bluetooth.h:840

[bt\_le\_adv\_param::secondary\_max\_skip](structbt__le__adv__param.md#a9911e9bfc97ff0c48a6decae3f922e95)

uint8\_t secondary\_max\_skip

Secondary channel maximum skip count.

**Definition** bluetooth.h:850

[bt\_le\_adv\_param::interval\_min](structbt__le__adv__param.md#aca8ff5a4f5d29184535162f007b2d39e)

uint32\_t interval\_min

Minimum Advertising Interval (N \* 0.625 milliseconds) Minimum Advertising Interval shall be less than...

**Definition** bluetooth.h:862

[bt\_le\_adv\_param::id](structbt__le__adv__param.md#af957bd92b949536af2b2db0db7b2b425)

uint8\_t id

Local identity.

**Definition** bluetooth.h:833

[bt\_le\_adv\_param::interval\_max](structbt__le__adv__param.md#afeba6973dca99d8ee818fdde0c22cb59)

uint32\_t interval\_max

Maximum Advertising Interval (N \* 0.625 milliseconds) Minimum Advertising Interval shall be less than...

**Definition** bluetooth.h:871

[bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md)

**Definition** bluetooth.h:114

[bt\_le\_ext\_adv\_cb::scanned](structbt__le__ext__adv__cb.md#a277dc3269741d40b644ae3c777198fab)

void(\* scanned)(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_scanned\_info \*info)

The advertising set has sent scan response data.

**Definition** bluetooth.h:151

[bt\_le\_ext\_adv\_cb::connected](structbt__le__ext__adv__cb.md#a7aad0fbd8e531e70f661500c338d870e)

void(\* connected)(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_connected\_info \*info)

The advertising set has accepted a new connection.

**Definition** bluetooth.h:138

[bt\_le\_ext\_adv\_cb::sent](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60)

void(\* sent)(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_sent\_info \*info)

The advertising set has finished sending adv data.

**Definition** bluetooth.h:126

[bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md)

**Definition** bluetooth.h:71

[bt\_le\_ext\_adv\_connected\_info::conn](structbt__le__ext__adv__connected__info.md#a157efa6206b418f768582107c566fde2)

struct bt\_conn \* conn

Connection object of the new connection.

**Definition** bluetooth.h:73

[bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md)

Advertising set info structure.

**Definition** bluetooth.h:1465

[bt\_le\_ext\_adv\_info::id](structbt__le__ext__adv__info.md#a06aa727cd2523914bc7509713585bffd)

uint8\_t id

**Definition** bluetooth.h:1467

[bt\_le\_ext\_adv\_info::addr](structbt__le__ext__adv__info.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9)

const bt\_addr\_le\_t \* addr

Current local advertising address used.

**Definition** bluetooth.h:1473

[bt\_le\_ext\_adv\_info::tx\_power](structbt__le__ext__adv__info.md#a485e4a8124fddee897fe744836cbfb24)

int8\_t tx\_power

Currently selected Transmit Power (dBM).

**Definition** bluetooth.h:1470

[bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md)

**Definition** bluetooth.h:76

[bt\_le\_ext\_adv\_scanned\_info::addr](structbt__le__ext__adv__scanned__info.md#a4431f157891d2c1a7d0e40f7e879ac3d)

bt\_addr\_le\_t \* addr

Active scanner LE address and type.

**Definition** bluetooth.h:78

[bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md)

**Definition** bluetooth.h:66

[bt\_le\_ext\_adv\_sent\_info::num\_sent](structbt__le__ext__adv__sent__info.md#a80f661efd35b069c2f8700851e9429a2)

uint8\_t num\_sent

The number of advertising events completed.

**Definition** bluetooth.h:68

[bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md)

**Definition** bluetooth.h:1332

[bt\_le\_ext\_adv\_start\_param::timeout](structbt__le__ext__adv__start__param.md#a80bb1ef4316dd75ea1268241333f4346)

uint16\_t timeout

Advertiser timeout (N \* 10 ms).

**Definition** bluetooth.h:1346

[bt\_le\_ext\_adv\_start\_param::num\_events](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f)

uint8\_t num\_events

Number of advertising events.

**Definition** bluetooth.h:1353

[bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md)

LE Secure Connections pairing Out of Band data.

**Definition** bluetooth.h:2572

[bt\_le\_oob\_sc\_data::c](structbt__le__oob__sc__data.md#a9bd93f1e9e41e241d0f84ae16ae47ba1)

uint8\_t c[16]

Confirm Value.

**Definition** bluetooth.h:2577

[bt\_le\_oob\_sc\_data::r](structbt__le__oob__sc__data.md#afa64bcc048d0e8709e262e2848a39d2c)

uint8\_t r[16]

Random Number.

**Definition** bluetooth.h:2574

[bt\_le\_oob](structbt__le__oob.md)

LE Out of Band information.

**Definition** bluetooth.h:2581

[bt\_le\_oob::addr](structbt__le__oob.md#a17cfed7683efbf5b5954847d655d7424)

bt\_addr\_le\_t addr

LE address.

**Definition** bluetooth.h:2585

[bt\_le\_oob::le\_sc\_data](structbt__le__oob.md#a80ccd4ab120a880adfff9aba3b19b4fd)

struct bt\_le\_oob\_sc\_data le\_sc\_data

LE Secure Connections pairing Out of Band data.

**Definition** bluetooth.h:2588

[bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md)

**Definition** bluetooth.h:81

[bt\_le\_per\_adv\_data\_request::count](structbt__le__per__adv__data__request.md#a766991899bc3e689adec36bf1f12e802)

uint8\_t count

The number of subevents data can be set for.

**Definition** bluetooth.h:86

[bt\_le\_per\_adv\_data\_request::start](structbt__le__per__adv__data__request.md#a779ed161919c3117f6ce165deb0a9b0a)

uint8\_t start

The first subevent data can be set for.

**Definition** bluetooth.h:83

[bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md)

**Definition** bluetooth.h:912

[bt\_le\_per\_adv\_param::interval\_min](structbt__le__per__adv__param.md#a49da44a3c0e4e866ffccffae5a9a22f7)

uint16\_t interval\_min

Minimum Periodic Advertising Interval (N \* 1.25 ms).

**Definition** bluetooth.h:919

[bt\_le\_per\_adv\_param::interval\_max](structbt__le__per__adv__param.md#a61308cfe72ad23372dfd2a3bd2550726)

uint16\_t interval\_max

Maximum Periodic Advertising Interval (N \* 1.25 ms).

**Definition** bluetooth.h:927

[bt\_le\_per\_adv\_param::options](structbt__le__per__adv__param.md#a9b80c2427171920f466601e7e8468814)

uint32\_t options

Bit-field of periodic advertising options.

**Definition** bluetooth.h:930

[bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md)

**Definition** bluetooth.h:89

[bt\_le\_per\_adv\_response\_info::subevent](structbt__le__per__adv__response__info.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5)

uint8\_t subevent

The subevent the response was received in.

**Definition** bluetooth.h:91

[bt\_le\_per\_adv\_response\_info::rssi](structbt__le__per__adv__response__info.md#a2db58fb452a07290ab4a50892c682837)

int8\_t rssi

The RSSI of the response in dBm.

**Definition** bluetooth.h:105

[bt\_le\_per\_adv\_response\_info::cte\_type](structbt__le__per__adv__response__info.md#a52b0c612b09cfcb3eb2ea475614c34b8)

uint8\_t cte\_type

The Constant Tone Extension (CTE) of the advertisement (bt\_df\_cte\_type).

**Definition** bluetooth.h:108

[bt\_le\_per\_adv\_response\_info::tx\_power](structbt__le__per__adv__response__info.md#a7ed20f695e0d696eaab7cddc4e3c11fb)

int8\_t tx\_power

The TX power of the response in dBm.

**Definition** bluetooth.h:102

[bt\_le\_per\_adv\_response\_info::response\_slot](structbt__le__per__adv__response__info.md#a83cc642c9f22c767421644e7d8233001)

uint8\_t response\_slot

The slot the response was received in.

**Definition** bluetooth.h:111

[bt\_le\_per\_adv\_response\_info::tx\_status](structbt__le__per__adv__response__info.md#ab17f33cb713d258bf6c863a64e5aba07)

uint8\_t tx\_status

Status of the subevent indication.

**Definition** bluetooth.h:99

[bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md)

**Definition** bluetooth.h:2725

[bt\_le\_per\_adv\_response\_params::response\_subevent](structbt__le__per__adv__response__params.md#a0cec222d5ba8cc9e20939d441646c913)

uint8\_t response\_subevent

The subevent the response shall be sent in.

**Definition** bluetooth.h:2744

[bt\_le\_per\_adv\_response\_params::request\_event](structbt__le__per__adv__response__params.md#a1af01d0a027fb8659615874acbd388f9)

uint16\_t request\_event

The periodic event counter of the request the response is sent to.

**Definition** bluetooth.h:2734

[bt\_le\_per\_adv\_response\_params::request\_subevent](structbt__le__per__adv__response__params.md#a3fc8ab0feb06714b28d22439cce60e41)

uint8\_t request\_subevent

The subevent counter of the request the response is sent to.

**Definition** bluetooth.h:2741

[bt\_le\_per\_adv\_response\_params::response\_slot](structbt__le__per__adv__response__params.md#aea0428083ccd5f4dccc17e494f38b7c3)

uint8\_t response\_slot

The response slot the response shall be sent in.

**Definition** bluetooth.h:2747

[bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md)

**Definition** bluetooth.h:1534

[bt\_le\_per\_adv\_subevent\_data\_params::response\_slot\_start](structbt__le__per__adv__subevent__data__params.md#a1354e9505239de3c42969138d719d775)

uint8\_t response\_slot\_start

The first response slot to listen to.

**Definition** bluetooth.h:1539

[bt\_le\_per\_adv\_subevent\_data\_params::data](structbt__le__per__adv__subevent__data__params.md#a46103c988d8ac360b7e26310a0322b4e)

const struct net\_buf\_simple \* data

The data to send.

**Definition** bluetooth.h:1545

[bt\_le\_per\_adv\_subevent\_data\_params::subevent](structbt__le__per__adv__subevent__data__params.md#a55f2da6041b538b3bc4bff38cd4d2953)

uint8\_t subevent

The subevent to set data for.

**Definition** bluetooth.h:1536

[bt\_le\_per\_adv\_subevent\_data\_params::response\_slot\_count](structbt__le__per__adv__subevent__data__params.md#a86d858606943a82917835a0172e88663)

uint8\_t response\_slot\_count

The number of response slots to listen to.

**Definition** bluetooth.h:1542

[bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md)

**Definition** bluetooth.h:1685

[bt\_le\_per\_adv\_sync\_cb::node](structbt__le__per__adv__sync__cb.md#a1977d27941063773c953a5f1dfa9ca76)

sys\_snode\_t node

**Definition** bluetooth.h:1763

[bt\_le\_per\_adv\_sync\_cb::recv](structbt__le__per__adv__sync__cb.md#a5576248e2eaef2afebe606e05e55f05f)

void(\* recv)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_le\_per\_adv\_sync\_recv\_info \*info, struct net\_buf\_simple \*buf)

Periodic advertising data received.

**Definition** bluetooth.h:1724

[bt\_le\_per\_adv\_sync\_cb::state\_changed](structbt__le__per__adv__sync__cb.md#a656b4802f79d4a472c2367ade144d72e)

void(\* state\_changed)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_le\_per\_adv\_sync\_state\_info \*info)

The periodic advertising sync state has changed.

**Definition** bluetooth.h:1738

[bt\_le\_per\_adv\_sync\_cb::synced](structbt__le__per__adv__sync__cb.md#a815be4343ab589df433a551663c5f4a1)

void(\* synced)(struct bt\_le\_per\_adv\_sync \*sync, struct bt\_le\_per\_adv\_sync\_synced\_info \*info)

The periodic advertising has been successfully synced.

**Definition** bluetooth.h:1696

[bt\_le\_per\_adv\_sync\_cb::biginfo](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9)

void(\* biginfo)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_iso\_biginfo \*biginfo)

BIGInfo advertising report received.

**Definition** bluetooth.h:1751

[bt\_le\_per\_adv\_sync\_cb::term](structbt__le__per__adv__sync__cb.md#acbd565a39918e5dfe7603a020e73daec)

void(\* term)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_le\_per\_adv\_sync\_term\_info \*info)

The periodic advertising sync has been terminated.

**Definition** bluetooth.h:1708

[bt\_le\_per\_adv\_sync\_cb::cte\_report\_cb](structbt__le__per__adv__sync__cb.md#ad2dc168696fbd22f7e3a089ac56f62d7)

void(\* cte\_report\_cb)(struct bt\_le\_per\_adv\_sync \*sync, struct bt\_df\_per\_adv\_sync\_iq\_samples\_report const \*info)

Callback for IQ samples report collected when sampling CTE received with periodic advertising PDU.

**Definition** bluetooth.h:1760

[bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md)

Advertising set info structure.

**Definition** bluetooth.h:1868

[bt\_le\_per\_adv\_sync\_info::interval](structbt__le__per__adv__sync__info.md#a365a0d8577429e4ee96e977071c9a906)

uint16\_t interval

Periodic advertising interval (N \* 1.25 ms).

**Definition** bluetooth.h:1876

[bt\_le\_per\_adv\_sync\_info::phy](structbt__le__per__adv__sync__info.md#a4d9520ea6a803f8fe4f41190f55c26e5)

uint8\_t phy

Advertiser PHY.

**Definition** bluetooth.h:1879

[bt\_le\_per\_adv\_sync\_info::addr](structbt__le__per__adv__sync__info.md#ac10fc2e2d3ec2160db8c2aac148d18a2)

bt\_addr\_le\_t addr

Periodic Advertiser Address.

**Definition** bluetooth.h:1870

[bt\_le\_per\_adv\_sync\_info::sid](structbt__le__per__adv__sync__info.md#acc0ef26c38279c9a67f8992005c2e58a)

uint8\_t sid

Advertiser SID.

**Definition** bluetooth.h:1873

[bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md)

**Definition** bluetooth.h:1802

[bt\_le\_per\_adv\_sync\_param::timeout](structbt__le__per__adv__sync__param.md#a301cfd3d6e5620d29c021ababe104754)

uint16\_t timeout

Synchronization timeout (N \* 10 ms).

**Definition** bluetooth.h:1837

[bt\_le\_per\_adv\_sync\_param::options](structbt__le__per__adv__sync__param.md#a4252f2b3b453c2f9c8fbf8c35a618ff2)

uint32\_t options

Bit-field of periodic advertising sync options.

**Definition** bluetooth.h:1820

[bt\_le\_per\_adv\_sync\_param::sid](structbt__le__per__adv__sync__param.md#a70795642ee94dd9e87f0cf251c095e7f)

uint8\_t sid

Advertiser SID.

**Definition** bluetooth.h:1817

[bt\_le\_per\_adv\_sync\_param::addr](structbt__le__per__adv__sync__param.md#ac93adedad747f61a771ac5445e486b74)

bt\_addr\_le\_t addr

Periodic Advertiser Address.

**Definition** bluetooth.h:1809

[bt\_le\_per\_adv\_sync\_param::skip](structbt__le__per__adv__sync__param.md#af9abb65547fb5bfea65f4c22963c7da0)

uint16\_t skip

Maximum event skip.

**Definition** bluetooth.h:1829

[bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md)

**Definition** bluetooth.h:1655

[bt\_le\_per\_adv\_sync\_recv\_info::cte\_type](structbt__le__per__adv__sync__recv__info.md#a1591907e3cb1f4565b9d26c18bccc7d2)

uint8\_t cte\_type

The Constant Tone Extension (CTE) of the advertisement (bt\_df\_cte\_type).

**Definition** bluetooth.h:1669

[bt\_le\_per\_adv\_sync\_recv\_info::sid](structbt__le__per__adv__sync__recv__info.md#a21b0ca87e46c6897282ebd877e45114e)

uint8\_t sid

Advertiser SID.

**Definition** bluetooth.h:1660

[bt\_le\_per\_adv\_sync\_recv\_info::addr](structbt__le__per__adv__sync__recv__info.md#a5817bd4fba2c93adebcebe007650b6eb)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:1657

[bt\_le\_per\_adv\_sync\_recv\_info::tx\_power](structbt__le__per__adv__sync__recv__info.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e)

int8\_t tx\_power

The TX power of the advertisement.

**Definition** bluetooth.h:1663

[bt\_le\_per\_adv\_sync\_recv\_info::rssi](structbt__le__per__adv__sync__recv__info.md#aa17c9d917469f121448ed4e1db485700)

int8\_t rssi

The RSSI of the advertisement excluding any CTE.

**Definition** bluetooth.h:1666

[bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md)

**Definition** bluetooth.h:1680

[bt\_le\_per\_adv\_sync\_state\_info::recv\_enabled](structbt__le__per__adv__sync__state__info.md#a4b0a3b7e36f935e06072304d6b92579f)

bool recv\_enabled

True if receiving periodic advertisements, false otherwise.

**Definition** bluetooth.h:1682

[bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md)

**Definition** bluetooth.h:2693

[bt\_le\_per\_adv\_sync\_subevent\_params::subevents](structbt__le__per__adv__sync__subevent__params.md#a5ac4e81ddd63797f921105748344c125)

uint8\_t \* subevents

The subevent(s) to synchronize with.

**Definition** bluetooth.h:2709

[bt\_le\_per\_adv\_sync\_subevent\_params::properties](structbt__le__per__adv__sync__subevent__params.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4)

uint16\_t properties

Periodic Advertising Properties.

**Definition** bluetooth.h:2699

[bt\_le\_per\_adv\_sync\_subevent\_params::num\_subevents](structbt__le__per__adv__sync__subevent__params.md#a867c66bf09461a4369da3d250701d2ae)

uint8\_t num\_subevents

Number of subevents to sync to.

**Definition** bluetooth.h:2702

[bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md)

**Definition** bluetooth.h:1598

[bt\_le\_per\_adv\_sync\_synced\_info::recv\_enabled](structbt__le__per__adv__sync__synced__info.md#a0dd4b7646da0fadc48e94ff3dc91ef83)

bool recv\_enabled

True if receiving periodic advertisements, false otherwise.

**Definition** bluetooth.h:1612

[bt\_le\_per\_adv\_sync\_synced\_info::interval](structbt__le__per__adv__sync__synced__info.md#a5304e1826face35c506f3b8f6cad7df2)

uint16\_t interval

Periodic advertising interval (N \* 1.25 ms).

**Definition** bluetooth.h:1606

[bt\_le\_per\_adv\_sync\_synced\_info::sid](structbt__le__per__adv__sync__synced__info.md#a5489c3038f7fff596316a456fc8d580b)

uint8\_t sid

Advertiser SID.

**Definition** bluetooth.h:1603

[bt\_le\_per\_adv\_sync\_synced\_info::addr](structbt__le__per__adv__sync__synced__info.md#a7ca99b0596b08d153d3ba5310adab125)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:1600

[bt\_le\_per\_adv\_sync\_synced\_info::phy](structbt__le__per__adv__sync__synced__info.md#a8b7709011541e95ceaeac379cc3143bb)

uint8\_t phy

Advertiser PHY.

**Definition** bluetooth.h:1609

[bt\_le\_per\_adv\_sync\_synced\_info::conn](structbt__le__per__adv__sync__synced__info.md#ada4cda53aa87f29d54f6cd88134efe14)

struct bt\_conn \* conn

Peer that transferred the periodic advertising sync.

**Definition** bluetooth.h:1627

[bt\_le\_per\_adv\_sync\_synced\_info::service\_data](structbt__le__per__adv__sync__synced__info.md#adee2bdafa86a0c3c1dfb4660e85396a3)

uint16\_t service\_data

Service Data provided by the peer when sync is transferred.

**Definition** bluetooth.h:1619

[bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md)

**Definition** bluetooth.h:1644

[bt\_le\_per\_adv\_sync\_term\_info::addr](structbt__le__per__adv__sync__term__info.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:1646

[bt\_le\_per\_adv\_sync\_term\_info::reason](structbt__le__per__adv__sync__term__info.md#a429b8b665eacbfe9db013a571b829bac)

uint8\_t reason

Cause of periodic advertising termination.

**Definition** bluetooth.h:1652

[bt\_le\_per\_adv\_sync\_term\_info::sid](structbt__le__per__adv__sync__term__info.md#a7a5f2ecccaf698bad86f10d9a7d16189)

uint8\_t sid

Advertiser SID.

**Definition** bluetooth.h:1649

[bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md)

**Definition** bluetooth.h:2027

[bt\_le\_per\_adv\_sync\_transfer\_param::options](structbt__le__per__adv__sync__transfer__param.md#a0b3ee6df1b409e64a064ffb6ac632cce)

uint32\_t options

Periodic Advertising Sync Transfer options.

**Definition** bluetooth.h:2045

[bt\_le\_per\_adv\_sync\_transfer\_param::timeout](structbt__le__per__adv__sync__transfer__param.md#a5bfa84c6bdacdf8893a0951a5ce71fc6)

uint16\_t timeout

Synchronization timeout (N \* 10 ms).

**Definition** bluetooth.h:2042

[bt\_le\_per\_adv\_sync\_transfer\_param::skip](structbt__le__per__adv__sync__transfer__param.md#a840e7cfac3a2947e5128d704067aaf7e)

uint16\_t skip

Maximum event skip.

**Definition** bluetooth.h:2034

[bt\_le\_scan\_cb](structbt__le__scan__cb.md)

Listener context for (LE) scanning.

**Definition** bluetooth.h:2291

[bt\_le\_scan\_cb::timeout](structbt__le__scan__cb.md#a2f57f3fee46bd137065f4c57d0cd5157)

void(\* timeout)(void)

The scanner has stopped scanning after scan timeout.

**Definition** bluetooth.h:2303

[bt\_le\_scan\_cb::node](structbt__le__scan__cb.md#a50dbc5e7618fd488e9acb7ad8f104a63)

sys\_snode\_t node

**Definition** bluetooth.h:2305

[bt\_le\_scan\_cb::recv](structbt__le__scan__cb.md#a71d73c1da28d4a27626f77d96a5b3541)

void(\* recv)(const struct bt\_le\_scan\_recv\_info \*info, struct net\_buf\_simple \*buf)

Advertisement packet and scan response received callback.

**Definition** bluetooth.h:2299

[bt\_le\_scan\_param](structbt__le__scan__param.md)

LE scan parameters.

**Definition** bluetooth.h:2187

[bt\_le\_scan\_param::type](structbt__le__scan__param.md#a02d75322390287c3fa754bf915660d0c)

uint8\_t type

Scan type (BT\_LE\_SCAN\_TYPE\_ACTIVE or BT\_LE\_SCAN\_TYPE\_PASSIVE).

**Definition** bluetooth.h:2189

[bt\_le\_scan\_param::interval](structbt__le__scan__param.md#a2f4e053d97c62b6fdf42a245908607f8)

uint16\_t interval

Scan interval (N \* 0.625 ms).

**Definition** bluetooth.h:2202

[bt\_le\_scan\_param::window](structbt__le__scan__param.md#a37a7ee82e86a91cf7a9c2adf60bb526a)

uint16\_t window

Scan window (N \* 0.625 ms).

**Definition** bluetooth.h:2212

[bt\_le\_scan\_param::timeout](structbt__le__scan__param.md#a3e71ce551dcc7762c29e2316996e2912)

uint16\_t timeout

Scan timeout (N \* 10 ms).

**Definition** bluetooth.h:2220

[bt\_le\_scan\_param::interval\_coded](structbt__le__scan__param.md#a67a20bc94a3d98fa10af7b5b42dde328)

uint16\_t interval\_coded

Scan interval LE Coded PHY (N \* 0.625 MS).

**Definition** bluetooth.h:2227

[bt\_le\_scan\_param::window\_coded](structbt__le__scan__param.md#a93166af55dca71393c60cb3f7ac6d809)

uint16\_t window\_coded

Scan window LE Coded PHY (N \* 0.625 MS).

**Definition** bluetooth.h:2234

[bt\_le\_scan\_param::options](structbt__le__scan__param.md#ac815b05fee8ce0dd24228305b7596207)

uint8\_t options

Bit-field of scanning options.

**Definition** bluetooth.h:2192

[bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md)

LE advertisement and scan response packet information.

**Definition** bluetooth.h:2238

[bt\_le\_scan\_recv\_info::interval](structbt__le__scan__recv__info.md#a1060c5937708ff81a64f068e02fc7826)

uint16\_t interval

Periodic advertising interval (N \* 1.25 ms).

**Definition** bluetooth.h:2281

[bt\_le\_scan\_recv\_info::tx\_power](structbt__le__scan__recv__info.md#a2addeba6d2ec8e55dc5379adf6519148)

int8\_t tx\_power

Transmit power of the advertiser.

**Definition** bluetooth.h:2254

[bt\_le\_scan\_recv\_info::sid](structbt__le__scan__recv__info.md#a4df8d4e1fdd7514d170744856ebe7015)

uint8\_t sid

Advertising Set Identifier.

**Definition** bluetooth.h:2248

[bt\_le\_scan\_recv\_info::primary\_phy](structbt__le__scan__recv__info.md#a6189ed8453cb7907f34dc7dfaf1343bd)

uint8\_t primary\_phy

Primary advertising channel PHY.

**Definition** bluetooth.h:2284

[bt\_le\_scan\_recv\_info::rssi](structbt__le__scan__recv__info.md#a88f677733147245ccbf861c7fc5e0f11)

int8\_t rssi

Strength of advertiser signal.

**Definition** bluetooth.h:2251

[bt\_le\_scan\_recv\_info::addr](structbt__le__scan__recv__info.md#a907fb7ec3c78d68da5015a8c3afc3084)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:2245

[bt\_le\_scan\_recv\_info::secondary\_phy](structbt__le__scan__recv__info.md#ac797291291dc7ba7ac171ed7f24f0d16)

uint8\_t secondary\_phy

Secondary advertising channel PHY.

**Definition** bluetooth.h:2287

[bt\_le\_scan\_recv\_info::adv\_type](structbt__le__scan__recv__info.md#adccb2ce5c6d228bd7f8f050088629524)

uint8\_t adv\_type

Advertising packet type.

**Definition** bluetooth.h:2264

[bt\_le\_scan\_recv\_info::adv\_props](structbt__le__scan__recv__info.md#af29ddfb59e286af9ca465cbd5a91bf2d)

uint16\_t adv\_props

Advertising packet properties bitfield.

**Definition** bluetooth.h:2274

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[net\_buf\_simple::data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** net\_buf.h:91

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [bluetooth.h](bluetooth_2bluetooth_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
