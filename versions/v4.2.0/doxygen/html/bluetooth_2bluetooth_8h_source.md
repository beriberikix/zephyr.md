---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/bluetooth_2bluetooth_8h_source.html
original_path: doxygen/html/bluetooth_2bluetooth_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bluetooth.h

[Go to the documentation of this file.](bluetooth_2bluetooth_8h.md)

1

5

6/\*

7 \* Copyright (c) 2017 Nordic Semiconductor ASA

8 \* Copyright (c) 2015-2016 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_BLUETOOTH\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_BLUETOOTH\_H\_

14

29

30#include <[stdbool.h](stdbool_8h.md)>

31#include <[stdint.h](stdint_8h.md)>

32#include <[string.h](string_8h.md)>

33

34#include <[zephyr/bluetooth/gap.h](gap_8h.md)>

35#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

36#include <[zephyr/bluetooth/crypto.h](bluetooth_2crypto_8h.md)>

37#include <[zephyr/bluetooth/classic/classic.h](classic_8h.md)>

38#include <[zephyr/net\_buf.h](net__buf_8h.md)>

39#include <[zephyr/sys/slist.h](slist_8h.md)>

40#include <[zephyr/sys/util.h](sys_2util_8h.md)>

41#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

42#include <[zephyr/toolchain.h](toolchain_8h.md)>

43

44#ifdef \_\_cplusplus

45extern "C" {

46#endif

47

65

[ 71](group__bt__gap.md#gaded4b52c9bb87fd4d19b1eb9361973e5)#define BT\_ID\_DEFAULT 0

72

[ 78](group__bt__gap.md#gaa26f90b188caa50ca12247b7911a0a5f)#define BT\_LE\_LOCAL\_SUPPORTED\_FEATURES\_SIZE 8

79

81struct bt\_le\_ext\_adv;

82

84struct bt\_le\_per\_adv\_sync;

85

86/\* Don't require everyone to include conn.h \*/

87struct bt\_conn;

88

89/\* Don't require everyone to include iso.h \*/

90struct [bt\_iso\_biginfo](structbt__iso__biginfo.md);

91

92/\* Don't require everyone to include direction.h \*/

93struct [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md);

94

[ 100](structbt__le__ext__adv__sent__info.md)struct [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) {

[ 107](structbt__le__ext__adv__sent__info.md#a80f661efd35b069c2f8700851e9429a2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_sent](structbt__le__ext__adv__sent__info.md#a80f661efd35b069c2f8700851e9429a2);

108};

109

[ 115](structbt__le__ext__adv__connected__info.md)struct [bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md) {

[ 117](structbt__le__ext__adv__connected__info.md#a157efa6206b418f768582107c566fde2) struct bt\_conn \*[conn](structbt__le__ext__adv__connected__info.md#a157efa6206b418f768582107c566fde2);

118};

119

[ 125](structbt__le__ext__adv__scanned__info.md)struct [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md) {

[ 127](structbt__le__ext__adv__scanned__info.md#a4431f157891d2c1a7d0e40f7e879ac3d) [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__ext__adv__scanned__info.md#a4431f157891d2c1a7d0e40f7e879ac3d);

128};

129

[ 139](structbt__le__per__adv__data__request.md)struct [bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md) {

[ 141](structbt__le__per__adv__data__request.md#a779ed161919c3117f6ce165deb0a9b0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [start](structbt__le__per__adv__data__request.md#a779ed161919c3117f6ce165deb0a9b0a);

142

[ 144](structbt__le__per__adv__data__request.md#a766991899bc3e689adec36bf1f12e802) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [count](structbt__le__per__adv__data__request.md#a766991899bc3e689adec36bf1f12e802);

145};

146

[ 157](structbt__le__per__adv__response__info.md)struct [bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md) {

[ 159](structbt__le__per__adv__response__info.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__le__per__adv__response__info.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5);

160

[ 167](structbt__le__per__adv__response__info.md#ab17f33cb713d258bf6c863a64e5aba07) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_status](structbt__le__per__adv__response__info.md#ab17f33cb713d258bf6c863a64e5aba07);

168

[ 170](structbt__le__per__adv__response__info.md#a7ed20f695e0d696eaab7cddc4e3c11fb) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__per__adv__response__info.md#a7ed20f695e0d696eaab7cddc4e3c11fb);

171

[ 173](structbt__le__per__adv__response__info.md#a2db58fb452a07290ab4a50892c682837) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__le__per__adv__response__info.md#a2db58fb452a07290ab4a50892c682837);

174

[ 176](structbt__le__per__adv__response__info.md#a52b0c612b09cfcb3eb2ea475614c34b8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__le__per__adv__response__info.md#a52b0c612b09cfcb3eb2ea475614c34b8);

177

[ 179](structbt__le__per__adv__response__info.md#a83cc642c9f22c767421644e7d8233001) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot](structbt__le__per__adv__response__info.md#a83cc642c9f22c767421644e7d8233001);

180};

181

[ 202](structbt__le__ext__adv__cb.md)struct [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md) {

[ 213](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60) void (\*[sent](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60))(struct bt\_le\_ext\_adv \*adv,

214 struct [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) \*info);

215

[ 225](structbt__le__ext__adv__cb.md#a7aad0fbd8e531e70f661500c338d870e) void (\*[connected](structbt__le__ext__adv__cb.md#a7aad0fbd8e531e70f661500c338d870e))(struct bt\_le\_ext\_adv \*adv,

226 struct [bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md) \*info);

227

[ 238](structbt__le__ext__adv__cb.md#a277dc3269741d40b644ae3c777198fab) void (\*[scanned](structbt__le__ext__adv__cb.md#a277dc3269741d40b644ae3c777198fab))(struct bt\_le\_ext\_adv \*adv,

239 struct [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md) \*info);

240

241#if defined(CONFIG\_BT\_PRIVACY)

258 [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*rpa\_expired)(struct bt\_le\_ext\_adv \*adv);

259#endif /\* defined(CONFIG\_BT\_PRIVACY) \*/

260

261#if defined(CONFIG\_BT\_PER\_ADV\_RSP)

271 void (\*pawr\_data\_request)(struct bt\_le\_ext\_adv \*adv,

272 const struct [bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md) \*request);

282 void (\*pawr\_response)(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md) \*info,

283 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

284

285#endif /\* defined(CONFIG\_BT\_PER\_ADV\_RSP) \*/

286};

287

[ 294](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb)typedef void (\*[bt\_ready\_cb\_t](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb))(int err);

295

[ 315](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b)int [bt\_enable](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b)([bt\_ready\_cb\_t](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb) cb);

316

[ 336](group__bt__gap.md#ga0a58e5a050170e84a80f8d5bb3516ec7)int [bt\_disable](group__bt__gap.md#ga0a58e5a050170e84a80f8d5bb3516ec7)(void);

337

[ 343](group__bt__gap.md#gaa8bf6854e7ad1fe7e0805737576e5d1a)bool [bt\_is\_ready](group__bt__gap.md#gaa8bf6854e7ad1fe7e0805737576e5d1a)(void);

344

[ 362](group__bt__gap.md#gac8bb3609a3d6da69ff736809e45f5c8a)int [bt\_set\_name](group__bt__gap.md#gac8bb3609a3d6da69ff736809e45f5c8a)(const char \*name);

363

[ 371](group__bt__gap.md#gad922d894b25e86de3f81ce77200a13fd)const char \*[bt\_get\_name](group__bt__gap.md#gad922d894b25e86de3f81ce77200a13fd)(void);

372

[ 383](group__bt__gap.md#ga35b76ea7ce79721e47ca4164e08b2dfb)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_get\_appearance](group__bt__gap.md#ga35b76ea7ce79721e47ca4164e08b2dfb)(void);

384

[ 398](group__bt__gap.md#gaf0729453790aab1bd3d52c623be3b35a)int [bt\_set\_appearance](group__bt__gap.md#gaf0729453790aab1bd3d52c623be3b35a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) new\_appearance);

399

[ 419](group__bt__gap.md#ga06d0ae35cbf4382679cc3cfe612cee4d)void [bt\_id\_get](group__bt__gap.md#ga06d0ae35cbf4382679cc3cfe612cee4d)([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addrs, size\_t \*count);

420

[ 463](group__bt__gap.md#gae11eb8ad254418c38a0e8689df25a159)int [bt\_id\_create](group__bt__gap.md#gae11eb8ad254418c38a0e8689df25a159)([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*irk);

464

[ 491](group__bt__gap.md#gabb3353edc8a3a8d29a0370049b20cbe4)int [bt\_id\_reset](group__bt__gap.md#gabb3353edc8a3a8d29a0370049b20cbe4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*irk);

492

[ 509](group__bt__gap.md#gaf6cd906690a51ebed04bea4f4ef716ff)int [bt\_id\_delete](group__bt__gap.md#gaf6cd906690a51ebed04bea4f4ef716ff)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id);

510

[ 522](group__bt__gap.md#ga7357d34bf295a16d8288df3bf75e7976)#define BT\_DATA\_SERIALIZED\_SIZE(data\_len) ((data\_len) + 2)

523

[ 531](structbt__data.md)struct [bt\_data](structbt__data.md) {

[ 533](structbt__data.md#a984aecb40a4993ffa113be53942db065) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__data.md#a984aecb40a4993ffa113be53942db065);

[ 535](structbt__data.md#abda19091a1b8f99d385f11772ef34d5f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_len](structbt__data.md#abda19091a1b8f99d385f11772ef34d5f);

[ 537](structbt__data.md#ac80ec10101ad69a86f703a4e652c7826) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__data.md#ac80ec10101ad69a86f703a4e652c7826);

538};

539

[ 550](group__bt__gap.md#ga8481217e632522e1f322de87d745f8f0)#define BT\_DATA(\_type, \_data, \_data\_len) \

551 { \

552 .type = (\_type), \

553 .data\_len = (\_data\_len), \

554 .data = (const uint8\_t \*)(\_data), \

555 }

556

[ 566](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)#define BT\_DATA\_BYTES(\_type, \_bytes...) \

567 BT\_DATA(\_type, ((uint8\_t []) { \_bytes }), \

568 sizeof((uint8\_t []) { \_bytes }))

569

[ 582](group__bt__gap.md#ga3d2c6adc42eb9510734630f38d921b9a)size\_t [bt\_data\_get\_len](group__bt__gap.md#ga3d2c6adc42eb9510734630f38d921b9a)(const struct [bt\_data](structbt__data.md) data[], size\_t data\_count);

583

[ 597](group__bt__gap.md#ga3c067b16468ebd17973faeded0fc83c9)size\_t [bt\_data\_serialize](group__bt__gap.md#ga3c067b16468ebd17973faeded0fc83c9)(const struct [bt\_data](structbt__data.md) \*input, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*output);

598

[ 610](structbt__le__local__features.md)struct [bt\_le\_local\_features](structbt__le__local__features.md) {

[ 618](structbt__le__local__features.md#a76b8cc9bd4ab099cb94ebe997d991f68) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [features](structbt__le__local__features.md#a76b8cc9bd4ab099cb94ebe997d991f68)[[BT\_LE\_LOCAL\_SUPPORTED\_FEATURES\_SIZE](group__bt__gap.md#gaa26f90b188caa50ca12247b7911a0a5f)];

619

[ 626](structbt__le__local__features.md#aa2dc6363feab37af195ee192f2b906f1) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [states](structbt__le__local__features.md#aa2dc6363feab37af195ee192f2b906f1);

627

[ 636](structbt__le__local__features.md#a22ce370b338f687ce6860435cc0ec9c5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [acl\_mtu](structbt__le__local__features.md#a22ce370b338f687ce6860435cc0ec9c5);

[ 638](structbt__le__local__features.md#a19cecbe8574229844e9416842bc42b0c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [acl\_pkts](structbt__le__local__features.md#a19cecbe8574229844e9416842bc42b0c);

639

[ 648](structbt__le__local__features.md#ad7b95feb82c1dece8bb8bb7969efa2ec) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_mtu](structbt__le__local__features.md#ad7b95feb82c1dece8bb8bb7969efa2ec);

[ 650](structbt__le__local__features.md#a8b413bf80ccd7e3af67f7e1c28a1beeb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [iso\_pkts](structbt__le__local__features.md#a8b413bf80ccd7e3af67f7e1c28a1beeb);

651

[ 657](structbt__le__local__features.md#ac86ae6974627ddb2e34b0d028cdcfe32) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rl\_size](structbt__le__local__features.md#ac86ae6974627ddb2e34b0d028cdcfe32);

658

[ 666](structbt__le__local__features.md#a932af365332149ec620413a8504d342c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_adv\_data\_len](structbt__le__local__features.md#a932af365332149ec620413a8504d342c);

667};

668

[ 680](group__bt__gap.md#ga650faa2a86f54499f4bc5a8657a55a87)int [bt\_le\_get\_local\_features](group__bt__gap.md#ga650faa2a86f54499f4bc5a8657a55a87)(struct [bt\_le\_local\_features](structbt__le__local__features.md) \*local\_features);

681

[ 683](group__bt__gap.md#gafbf81dab68b0e484d4742471c722fc28)enum [bt\_le\_adv\_opt](group__bt__gap.md#gafbf81dab68b0e484d4742471c722fc28) {

[ 685](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a928b376123819cb0a69fbb5b35608dbf) [BT\_LE\_ADV\_OPT\_NONE](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a928b376123819cb0a69fbb5b35608dbf) = 0,

686

[ 707](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a2a90f8d144a194f74c5432079c5d42a3) [BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a2a90f8d144a194f74c5432079c5d42a3) \_\_deprecated = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

708

719 \_BT\_LE\_ADV\_OPT\_CONNECTABLE = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

720

[ 737](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a7d12782a02afefcf4b5c04442a99f8a2) [BT\_LE\_ADV\_OPT\_ONE\_TIME](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a7d12782a02afefcf4b5c04442a99f8a2) \_\_deprecated = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

738

745 \_BT\_LE\_ADV\_OPT\_ONE\_TIME = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

746

[ 765](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169) [BT\_LE\_ADV\_OPT\_CONN](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

766

[ 777](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a407cf5ae358d3c00dd7e47dfaad3ec6e) [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a407cf5ae358d3c00dd7e47dfaad3ec6e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

778

[ 803](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a2dbc9ec77d6de134d96a7bd3d9256398) [BT\_LE\_ADV\_OPT\_USE\_NAME](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a2dbc9ec77d6de134d96a7bd3d9256398) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

804

[ 811](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872) [BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

812

[ 825](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28abdcf1c80662061fa30575e1f9fc6cf6f) [BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28abdcf1c80662061fa30575e1f9fc6cf6f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

826

[ 830](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a807ba316edc49c8448a8ff7d497173f5) [BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a807ba316edc49c8448a8ff7d497173f5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

831

[ 833](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ad5efef3d01731110dbd71d5a5dc9baaf) [BT\_LE\_ADV\_OPT\_FILTER\_CONN](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ad5efef3d01731110dbd71d5a5dc9baaf) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

834

[ 838](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a1563b053f457833d1a3d11c8dc4d394b) [BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a1563b053f457833d1a3d11c8dc4d394b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

839

[ 848](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae60eafe69ef10b84f61a1f4accf789c9) [BT\_LE\_ADV\_OPT\_SCANNABLE](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae60eafe69ef10b84f61a1f4accf789c9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

849

[ 870](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab) [BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

871

[ 887](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae864aefcdfbecaffe823b9b144fe0a6b) [BT\_LE\_ADV\_OPT\_NO\_2M](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae864aefcdfbecaffe823b9b144fe0a6b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

888

[ 900](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ad01c4962a350d3218ba0cabd713708b1) [BT\_LE\_ADV\_OPT\_CODED](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ad01c4962a350d3218ba0cabd713708b1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

901

[ 908](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a185e0f884f8b0ce79625448638de8fab) [BT\_LE\_ADV\_OPT\_ANONYMOUS](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a185e0f884f8b0ce79625448638de8fab) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

909

[ 916](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aecff4fe3ac3d1fba3f6fa76c77713859) [BT\_LE\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aecff4fe3ac3d1fba3f6fa76c77713859) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

917

[ 919](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ab46741616f8bfe50c4b492d1f7970779) [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ab46741616f8bfe50c4b492d1f7970779) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

920

[ 922](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28abd9cb02691d7e025fe3fea9a80123275) [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28abd9cb02691d7e025fe3fea9a80123275) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

923

[ 925](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a89f7494620236c976bf1a76a880e2a28) [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a89f7494620236c976bf1a76a880e2a28) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17),

926

[ 938](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a0a9642077d93cf9c0eb42f64a9e34e73) [BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a0a9642077d93cf9c0eb42f64a9e34e73) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18),

939

[ 952](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a22958d8539d661ad7ca8d3f1173e7e5e) [BT\_LE\_ADV\_OPT\_USE\_NRPA](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a22958d8539d661ad7ca8d3f1173e7e5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

953

[ 969](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a9a35ede118224d6ed17f252fff6bb47e) [BT\_LE\_ADV\_OPT\_REQUIRE\_S2\_CODING](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a9a35ede118224d6ed17f252fff6bb47e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20),

970

[ 986](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aa6a61768ad4102f199d3970791118bb8) [BT\_LE\_ADV\_OPT\_REQUIRE\_S8\_CODING](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aa6a61768ad4102f199d3970791118bb8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21),

987};

988

[ 990](structbt__le__adv__param.md)struct [bt\_le\_adv\_param](structbt__le__adv__param.md) {

[ 1001](structbt__le__adv__param.md#af957bd92b949536af2b2db0db7b2b425) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__le__adv__param.md#af957bd92b949536af2b2db0db7b2b425);

1002

[ 1010](structbt__le__adv__param.md#a6e2f0e1b76495afe7fe661e8698d0909) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__adv__param.md#a6e2f0e1b76495afe7fe661e8698d0909);

1011

[ 1021](structbt__le__adv__param.md#a9911e9bfc97ff0c48a6decae3f922e95) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [secondary\_max\_skip](structbt__le__adv__param.md#a9911e9bfc97ff0c48a6decae3f922e95);

1022

[ 1024](structbt__le__adv__param.md#a2a978c60153eb03697769bc72928f4ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__adv__param.md#a2a978c60153eb03697769bc72928f4ef);

1025

[ 1036](structbt__le__adv__param.md#aca8ff5a4f5d29184535162f007b2d39e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval\_min](structbt__le__adv__param.md#aca8ff5a4f5d29184535162f007b2d39e);

1037

[ 1048](structbt__le__adv__param.md#afeba6973dca99d8ee818fdde0c22cb59) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval\_max](structbt__le__adv__param.md#afeba6973dca99d8ee818fdde0c22cb59);

1049

[ 1065](structbt__le__adv__param.md#a4cf31f54f067fffa3c848adc2ffd7119) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[peer](structbt__le__adv__param.md#a4cf31f54f067fffa3c848adc2ffd7119);

1066};

1067

1068

[ 1070](group__bt__gap.md#gae60a45dde6b4d9f4c54a2a6070254f11)enum [bt\_le\_per\_adv\_opt](group__bt__gap.md#gae60a45dde6b4d9f4c54a2a6070254f11) {

[ 1072](group__bt__gap.md#ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518) [BT\_LE\_PER\_ADV\_OPT\_NONE](group__bt__gap.md#ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518) = 0,

1073

[ 1080](group__bt__gap.md#ggae60a45dde6b4d9f4c54a2a6070254f11a9524537e4cb726f4ff10ba93381bb27f) [BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#ggae60a45dde6b4d9f4c54a2a6070254f11a9524537e4cb726f4ff10ba93381bb27f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

1081

[ 1088](group__bt__gap.md#ggae60a45dde6b4d9f4c54a2a6070254f11a38cebc2ae885ff630b34c603e2ec6403) [BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI](group__bt__gap.md#ggae60a45dde6b4d9f4c54a2a6070254f11a38cebc2ae885ff630b34c603e2ec6403) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

1089};

1090

[ 1104](structbt__le__per__adv__param.md)struct [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md) {

[ 1111](structbt__le__per__adv__param.md#a49da44a3c0e4e866ffccffae5a9a22f7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_min](structbt__le__per__adv__param.md#a49da44a3c0e4e866ffccffae5a9a22f7);

1112

[ 1119](structbt__le__per__adv__param.md#a61308cfe72ad23372dfd2a3bd2550726) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_max](structbt__le__per__adv__param.md#a61308cfe72ad23372dfd2a3bd2550726);

1120

[ 1122](structbt__le__per__adv__param.md#a9b80c2427171920f466601e7e8468814) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__per__adv__param.md#a9b80c2427171920f466601e7e8468814);

1123

1124#if defined(CONFIG\_BT\_PER\_ADV\_RSP)

1130 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents;

1131

1137 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subevent\_interval;

1138

1144 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_delay;

1145

1151 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_spacing;

1152

1158 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_response\_slots;

1159#endif /\* CONFIG\_BT\_PER\_ADV\_RSP \*/

1160};

1161

[ 1171](group__bt__gap.md#ga71555b857cf8c2a47c36e4dafa7accf4)#define BT\_LE\_ADV\_PARAM\_INIT(\_options, \_int\_min, \_int\_max, \_peer) \

1172{ \

1173 .id = BT\_ID\_DEFAULT, \

1174 .sid = 0, \

1175 .secondary\_max\_skip = 0, \

1176 .options = (\_options), \

1177 .interval\_min = (\_int\_min), \

1178 .interval\_max = (\_int\_max), \

1179 .peer = (\_peer), \

1180}

1181

[ 1191](group__bt__gap.md#ga9557269dd36b624b49e76c511c3a0cc1)#define BT\_LE\_ADV\_PARAM(\_options, \_int\_min, \_int\_max, \_peer) \

1192 ((const struct bt\_le\_adv\_param[]) { \

1193 BT\_LE\_ADV\_PARAM\_INIT(\_options, \_int\_min, \_int\_max, \_peer) \

1194 })

1195

[ 1196](group__bt__gap.md#ga1f5edc3c4cbead62e32cef8cc7b83725)#define BT\_LE\_ADV\_CONN\_DIR(\_peer) BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONN, 0, 0, \_peer)

1197

[ 1204](group__bt__gap.md#gad490487b9e196526a13fe249a4c25448)#define BT\_LE\_ADV\_CONN \

1205 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE, BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1206 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL) \

1207 \_\_DEPRECATED\_MACRO

1208

1236

[ 1237](group__bt__gap.md#gaa700527b1caf3bef27d96a3f91a29f69)#define BT\_LE\_ADV\_CONN\_FAST\_1 \

1238 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONN, BT\_GAP\_ADV\_FAST\_INT\_MIN\_1, BT\_GAP\_ADV\_FAST\_INT\_MAX\_1, \

1239 NULL)

1240

[ 1261](group__bt__gap.md#ga684a1110a8973bc17211f6f0824beccd)#define BT\_LE\_ADV\_CONN\_FAST\_2 \

1262 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONN, BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1263 NULL)

1264

[ 1265](group__bt__gap.md#gac0430ab5a40a49b3281dd6ff8a7e7378)#define BT\_LE\_ADV\_CONN\_ONE\_TIME BT\_LE\_ADV\_CONN\_FAST\_2 \_\_DEPRECATED\_MACRO

1266

[ 1271](group__bt__gap.md#ga7b29dba3d892186897c5b4ca5adfd2e3)#define BT\_LE\_ADV\_CONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE | \

1272 BT\_LE\_ADV\_OPT\_USE\_NAME, \

1273 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1274 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL) \

1275 \_\_DEPRECATED\_MACRO

1276

[ 1281](group__bt__gap.md#ga213307090f1debdc783c54faf4a36740)#define BT\_LE\_ADV\_CONN\_NAME\_AD BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONNECTABLE | \

1282 BT\_LE\_ADV\_OPT\_USE\_NAME | \

1283 BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD, \

1284 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1285 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL) \

1286 \_\_DEPRECATED\_MACRO

1287

[ 1288](group__bt__gap.md#gab89e033ed3fd116c94120d177dfdc839)#define BT\_LE\_ADV\_CONN\_DIR\_LOW\_DUTY(\_peer) \

1289 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_CONN | BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY, \

1290 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \_peer)

1291

[ 1293](group__bt__gap.md#ga1610555bf59f1d691d640f245957fdce)#define BT\_LE\_ADV\_NCONN BT\_LE\_ADV\_PARAM(0, BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1294 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

1295

[ 1302](group__bt__gap.md#gac1c3c47e3136ce813bb50b00a9387cb4)#define BT\_LE\_ADV\_NCONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_USE\_NAME, \

1303 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1304 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL) \

1305 \_\_DEPRECATED\_MACRO

1306

[ 1308](group__bt__gap.md#ga6ef9fb7a469b03265c7adc99ea19a11b)#define BT\_LE\_ADV\_NCONN\_IDENTITY BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_USE\_IDENTITY, \

1309 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1310 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1311 NULL)

1312

[ 1314](group__bt__gap.md#gaeaaef4dede5d45251dfe12f329e070b7)#define BT\_LE\_EXT\_ADV\_CONN \

1315 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | BT\_LE\_ADV\_OPT\_CONN, BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1316 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

1317

[ 1324](group__bt__gap.md#gac4880197cbe21aad78c4edf10cde95da)#define BT\_LE\_EXT\_ADV\_CONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1325 BT\_LE\_ADV\_OPT\_CONNECTABLE | \

1326 BT\_LE\_ADV\_OPT\_USE\_NAME, \

1327 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1328 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1329 NULL) \

1330 \_\_DEPRECATED\_MACRO

1331

[ 1333](group__bt__gap.md#ga5dd57fc7f0e213db08655e631a2f314e)#define BT\_LE\_EXT\_ADV\_SCAN BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1334 BT\_LE\_ADV\_OPT\_SCANNABLE, \

1335 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1336 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1337 NULL)

1338

[ 1345](group__bt__gap.md#ga3e4abd3691e2c6d95acd21b9ca566edd)#define BT\_LE\_EXT\_ADV\_SCAN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1346 BT\_LE\_ADV\_OPT\_SCANNABLE | \

1347 BT\_LE\_ADV\_OPT\_USE\_NAME, \

1348 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1349 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1350 NULL) \

1351 \_\_DEPRECATED\_MACRO

1352

[ 1354](group__bt__gap.md#gaabc0385f6a5307b48ec43af6aae7dea6)#define BT\_LE\_EXT\_ADV\_NCONN BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV, \

1355 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1356 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

1357

[ 1364](group__bt__gap.md#ga5c79af6787ccda890f485a45c931cdc8)#define BT\_LE\_EXT\_ADV\_NCONN\_NAME BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1365 BT\_LE\_ADV\_OPT\_USE\_NAME, \

1366 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1367 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1368 NULL) \

1369 \_\_DEPRECATED\_MACRO

1370

[ 1372](group__bt__gap.md#ga7e46a64af0036c433c2e940ce7db0a05)#define BT\_LE\_EXT\_ADV\_NCONN\_IDENTITY \

1373 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1374 BT\_LE\_ADV\_OPT\_USE\_IDENTITY, \

1375 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1376 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

1377

[ 1379](group__bt__gap.md#ga0e911d3aafdd0c926590b3272a3da564)#define BT\_LE\_EXT\_ADV\_CODED\_NCONN BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | \

1380 BT\_LE\_ADV\_OPT\_CODED, \

1381 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1382 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, \

1383 NULL)

1384

[ 1392](group__bt__gap.md#ga8c6027f7c0888c577f9b61a65104be05)#define BT\_LE\_EXT\_ADV\_CODED\_NCONN\_NAME \

1393 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | BT\_LE\_ADV\_OPT\_CODED | \

1394 BT\_LE\_ADV\_OPT\_USE\_NAME, \

1395 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1396 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL) \

1397 \_\_DEPRECATED\_MACRO

1398

[ 1402](group__bt__gap.md#gac67c52693154ebbeedbb31e100513812)#define BT\_LE\_EXT\_ADV\_CODED\_NCONN\_IDENTITY \

1403 BT\_LE\_ADV\_PARAM(BT\_LE\_ADV\_OPT\_EXT\_ADV | BT\_LE\_ADV\_OPT\_CODED | \

1404 BT\_LE\_ADV\_OPT\_USE\_IDENTITY, \

1405 BT\_GAP\_ADV\_FAST\_INT\_MIN\_2, \

1406 BT\_GAP\_ADV\_FAST\_INT\_MAX\_2, NULL)

1407

[ 1414](group__bt__gap.md#gaf0d4c5b05deb5466a0e29c153263b489)#define BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT(\_timeout, \_n\_evts) \

1415{ \

1416 .timeout = (\_timeout), \

1417 .num\_events = (\_n\_evts), \

1418}

1419

[ 1426](group__bt__gap.md#ga9b2cefbcb0a85116cadb68f6d80c6429)#define BT\_LE\_EXT\_ADV\_START\_PARAM(\_timeout, \_n\_evts) \

1427 ((const struct bt\_le\_ext\_adv\_start\_param[]) { \

1428 BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT((\_timeout), (\_n\_evts)) \

1429 })

1430

[ 1431](group__bt__gap.md#ga8c83a6f322a479bc24a576a7f091312e)#define BT\_LE\_EXT\_ADV\_START\_DEFAULT BT\_LE\_EXT\_ADV\_START\_PARAM(0, 0)

1432

[ 1441](group__bt__gap.md#ga880567278a81098ae55f52f624c61041)#define BT\_LE\_PER\_ADV\_PARAM\_INIT(\_int\_min, \_int\_max, \_options) \

1442{ \

1443 .interval\_min = (\_int\_min), \

1444 .interval\_max = (\_int\_max), \

1445 .options = (\_options), \

1446}

1447

[ 1456](group__bt__gap.md#gaf46e54f8fcda7b65b659685bb225d243)#define BT\_LE\_PER\_ADV\_PARAM(\_int\_min, \_int\_max, \_options) \

1457 ((struct bt\_le\_per\_adv\_param[]) { \

1458 BT\_LE\_PER\_ADV\_PARAM\_INIT(\_int\_min, \_int\_max, \_options) \

1459 })

1460

[ 1461](group__bt__gap.md#ga8f6a00faaaab2a91ac943c71ed041ac1)#define BT\_LE\_PER\_ADV\_DEFAULT BT\_LE\_PER\_ADV\_PARAM(BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN, \

1462 BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX, \

1463 BT\_LE\_PER\_ADV\_OPT\_NONE)

1464

[ 1493](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02)int [bt\_le\_adv\_start](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02)(const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param,

1494 const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len,

1495 const struct [bt\_data](structbt__data.md) \*sd, size\_t sd\_len);

1496

[ 1509](group__bt__gap.md#ga9a406ebfefac3dd09935a4ae0e317817)int [bt\_le\_adv\_update\_data](group__bt__gap.md#ga9a406ebfefac3dd09935a4ae0e317817)(const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len,

1510 const struct [bt\_data](structbt__data.md) \*sd, size\_t sd\_len);

1511

[ 1519](group__bt__gap.md#ga1776e310b9d80898e6b32d50c4fe0b49)int [bt\_le\_adv\_stop](group__bt__gap.md#ga1776e310b9d80898e6b32d50c4fe0b49)(void);

1520

[ 1540](group__bt__gap.md#gad02b855dd7a26e3910b247fa73f19297)int [bt\_le\_ext\_adv\_create](group__bt__gap.md#gad02b855dd7a26e3910b247fa73f19297)(const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param,

1541 const struct [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md) \*cb,

1542 struct bt\_le\_ext\_adv \*\*adv);

1543

[ 1557](structbt__le__ext__adv__start__param.md)struct [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md) {

[ 1582](structbt__le__ext__adv__start__param.md#a80bb1ef4316dd75ea1268241333f4346) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__ext__adv__start__param.md#a80bb1ef4316dd75ea1268241333f4346);

1583

[ 1602](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_events](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f);

1603};

1604

[ 1620](group__bt__gap.md#gaf0f436c55482d9429f674303ae3aa815)int [bt\_le\_ext\_adv\_start](group__bt__gap.md#gaf0f436c55482d9429f674303ae3aa815)(struct bt\_le\_ext\_adv \*adv,

1621 const struct [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md) \*param);

1622

[ 1633](group__bt__gap.md#ga1c864c4b183f9a86c9f70a11471c5b15)int [bt\_le\_ext\_adv\_stop](group__bt__gap.md#ga1c864c4b183f9a86c9f70a11471c5b15)(struct bt\_le\_ext\_adv \*adv);

1634

[ 1670](group__bt__gap.md#gad731f829b3566be3e56485b2a64f80b1)int [bt\_le\_ext\_adv\_set\_data](group__bt__gap.md#gad731f829b3566be3e56485b2a64f80b1)(struct bt\_le\_ext\_adv \*adv,

1671 const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len,

1672 const struct [bt\_data](structbt__data.md) \*sd, size\_t sd\_len);

1673

[ 1690](group__bt__gap.md#ga1aabdb81cb1a1841ff0fb91d849123fc)int [bt\_le\_ext\_adv\_update\_param](group__bt__gap.md#ga1aabdb81cb1a1841ff0fb91d849123fc)(struct bt\_le\_ext\_adv \*adv,

1691 const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param);

1692

[ 1702](group__bt__gap.md#ga62310a27f7fea925dfcf3abd7c454787)int [bt\_le\_ext\_adv\_delete](group__bt__gap.md#ga62310a27f7fea925dfcf3abd7c454787)(struct bt\_le\_ext\_adv \*adv);

1703

[ 1715](group__bt__gap.md#gaeb37d6cdd94a04b4cce8bc1e7aae70b4)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_le\_ext\_adv\_get\_index](group__bt__gap.md#gaeb37d6cdd94a04b4cce8bc1e7aae70b4)(struct bt\_le\_ext\_adv \*adv);

1716

[ 1718](group__bt__gap.md#ga544ccde35638d8f580942d830fe9f242)enum [bt\_le\_ext\_adv\_state](group__bt__gap.md#ga544ccde35638d8f580942d830fe9f242) {

[ 1720](group__bt__gap.md#gga544ccde35638d8f580942d830fe9f242a4423f4792711b21cf38a4e63c148760d) [BT\_LE\_EXT\_ADV\_STATE\_DISABLED](group__bt__gap.md#gga544ccde35638d8f580942d830fe9f242a4423f4792711b21cf38a4e63c148760d),

1721

[ 1723](group__bt__gap.md#gga544ccde35638d8f580942d830fe9f242afe851bf904c1cfed3ff10a57430d6a07) [BT\_LE\_EXT\_ADV\_STATE\_ENABLED](group__bt__gap.md#gga544ccde35638d8f580942d830fe9f242afe851bf904c1cfed3ff10a57430d6a07),

1724};

1725

[ 1727](group__bt__gap.md#ga6bb77c0808c761753650cde28ddb013e)enum [bt\_le\_per\_adv\_state](group__bt__gap.md#ga6bb77c0808c761753650cde28ddb013e) {

[ 1729](group__bt__gap.md#gga6bb77c0808c761753650cde28ddb013ead690730da823fcb31f102f154a23b01c) [BT\_LE\_PER\_ADV\_STATE\_NONE](group__bt__gap.md#gga6bb77c0808c761753650cde28ddb013ead690730da823fcb31f102f154a23b01c),

1730

[ 1732](group__bt__gap.md#gga6bb77c0808c761753650cde28ddb013eac26ccfbb5c715b515ef82c1993eff03b) [BT\_LE\_PER\_ADV\_STATE\_DISABLED](group__bt__gap.md#gga6bb77c0808c761753650cde28ddb013eac26ccfbb5c715b515ef82c1993eff03b),

1733

[ 1735](group__bt__gap.md#gga6bb77c0808c761753650cde28ddb013ea492cf25dc85090cfa72d5e2bdc0917f3) [BT\_LE\_PER\_ADV\_STATE\_ENABLED](group__bt__gap.md#gga6bb77c0808c761753650cde28ddb013ea492cf25dc85090cfa72d5e2bdc0917f3),

1736};

1737

[ 1739](structbt__le__ext__adv__info.md)struct [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md) {

[ 1741](structbt__le__ext__adv__info.md#a06aa727cd2523914bc7509713585bffd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__le__ext__adv__info.md#a06aa727cd2523914bc7509713585bffd);

1742

[ 1744](structbt__le__ext__adv__info.md#a485e4a8124fddee897fe744836cbfb24) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__ext__adv__info.md#a485e4a8124fddee897fe744836cbfb24);

1745

[ 1747](structbt__le__ext__adv__info.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__ext__adv__info.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9);

1748

[ 1750](structbt__le__ext__adv__info.md#a0ae2f62772732a6db460d4a0127dd17a) enum [bt\_le\_ext\_adv\_state](group__bt__gap.md#ga544ccde35638d8f580942d830fe9f242) [ext\_adv\_state](structbt__le__ext__adv__info.md#a0ae2f62772732a6db460d4a0127dd17a);

1751

[ 1753](structbt__le__ext__adv__info.md#ad802b5af32353d757a84e5039c973f3a) enum [bt\_le\_per\_adv\_state](group__bt__gap.md#ga6bb77c0808c761753650cde28ddb013e) [per\_adv\_state](structbt__le__ext__adv__info.md#ad802b5af32353d757a84e5039c973f3a);

1754};

1755

[ 1765](group__bt__gap.md#gac06c9f55cf1da46e0d64b4d9af984ecb)int [bt\_le\_ext\_adv\_get\_info](group__bt__gap.md#gac06c9f55cf1da46e0d64b4d9af984ecb)(const struct bt\_le\_ext\_adv \*adv,

1766 struct [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md) \*info);

1767

[ 1781](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4)typedef void [bt\_le\_scan\_cb\_t](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) rssi,

1782 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adv\_type, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

1783

[ 1797](group__bt__gap.md#gaa72029a2759123ec776061d2e80bf3a1)int [bt\_le\_per\_adv\_set\_param](group__bt__gap.md#gaa72029a2759123ec776061d2e80bf3a1)(struct bt\_le\_ext\_adv \*adv,

1798 const struct [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md) \*param);

1799

[ 1814](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899)int [bt\_le\_per\_adv\_set\_data](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899)(const struct bt\_le\_ext\_adv \*adv,

1815 const struct [bt\_data](structbt__data.md) \*ad, size\_t ad\_len);

1816

[ 1827](structbt__le__per__adv__subevent__data__params.md)struct [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md) {

[ 1829](structbt__le__per__adv__subevent__data__params.md#a55f2da6041b538b3bc4bff38cd4d2953) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [subevent](structbt__le__per__adv__subevent__data__params.md#a55f2da6041b538b3bc4bff38cd4d2953);

1830

[ 1832](structbt__le__per__adv__subevent__data__params.md#a1354e9505239de3c42969138d719d775) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_start](structbt__le__per__adv__subevent__data__params.md#a1354e9505239de3c42969138d719d775);

1833

[ 1835](structbt__le__per__adv__subevent__data__params.md#a86d858606943a82917835a0172e88663) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot\_count](structbt__le__per__adv__subevent__data__params.md#a86d858606943a82917835a0172e88663);

1836

[ 1838](structbt__le__per__adv__subevent__data__params.md#a46103c988d8ac360b7e26310a0322b4e) const struct [net\_buf\_simple](structnet__buf__simple.md) \*[data](structbt__le__per__adv__subevent__data__params.md#a46103c988d8ac360b7e26310a0322b4e);

1839};

1840

[ 1856](group__bt__gap.md#ga7de30fe5040b85bb9212e3a8fec4ac45)int [bt\_le\_per\_adv\_set\_subevent\_data](group__bt__gap.md#ga7de30fe5040b85bb9212e3a8fec4ac45)(const struct bt\_le\_ext\_adv \*adv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents,

1857 const struct [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md) \*params);

1858

[ 1876](group__bt__gap.md#ga0f23f4ed48e8679646f247ea0d687094)int [bt\_le\_per\_adv\_start](group__bt__gap.md#ga0f23f4ed48e8679646f247ea0d687094)(struct bt\_le\_ext\_adv \*adv);

1877

[ 1889](group__bt__gap.md#ga1b15206fc552d597c12af369d48ff7d5)int [bt\_le\_per\_adv\_stop](group__bt__gap.md#ga1b15206fc552d597c12af369d48ff7d5)(struct bt\_le\_ext\_adv \*adv);

1890

[ 1903](structbt__le__per__adv__sync__synced__info.md)struct [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md) {

[ 1905](structbt__le__per__adv__sync__synced__info.md#a7ca99b0596b08d153d3ba5310adab125) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__per__adv__sync__synced__info.md#a7ca99b0596b08d153d3ba5310adab125);

1906

[ 1908](structbt__le__per__adv__sync__synced__info.md#a5489c3038f7fff596316a456fc8d580b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__synced__info.md#a5489c3038f7fff596316a456fc8d580b);

1909

[ 1911](structbt__le__per__adv__sync__synced__info.md#a5304e1826face35c506f3b8f6cad7df2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__per__adv__sync__synced__info.md#a5304e1826face35c506f3b8f6cad7df2);

1912

[ 1914](structbt__le__per__adv__sync__synced__info.md#a8b7709011541e95ceaeac379cc3143bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__le__per__adv__sync__synced__info.md#a8b7709011541e95ceaeac379cc3143bb);

1915

[ 1917](structbt__le__per__adv__sync__synced__info.md#a0dd4b7646da0fadc48e94ff3dc91ef83) bool [recv\_enabled](structbt__le__per__adv__sync__synced__info.md#a0dd4b7646da0fadc48e94ff3dc91ef83);

1918

[ 1924](structbt__le__per__adv__sync__synced__info.md#adee2bdafa86a0c3c1dfb4660e85396a3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [service\_data](structbt__le__per__adv__sync__synced__info.md#adee2bdafa86a0c3c1dfb4660e85396a3);

1925

[ 1932](structbt__le__per__adv__sync__synced__info.md#ada4cda53aa87f29d54f6cd88134efe14) struct bt\_conn \*[conn](structbt__le__per__adv__sync__synced__info.md#ada4cda53aa87f29d54f6cd88134efe14);

1933#if defined(CONFIG\_BT\_PER\_ADV\_SYNC\_RSP)

1935 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents;

1936

1938 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subevent\_interval;

1939

1941 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_delay;

1942

1944 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) response\_slot\_spacing;

1945

1946#endif /\* CONFIG\_BT\_PER\_ADV\_SYNC\_RSP \*/

1947};

1948

[ 1959](structbt__le__per__adv__sync__term__info.md)struct [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md) {

[ 1961](structbt__le__per__adv__sync__term__info.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__per__adv__sync__term__info.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc);

1962

[ 1964](structbt__le__per__adv__sync__term__info.md#a7a5f2ecccaf698bad86f10d9a7d16189) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__term__info.md#a7a5f2ecccaf698bad86f10d9a7d16189);

1965

[ 1967](structbt__le__per__adv__sync__term__info.md#a429b8b665eacbfe9db013a571b829bac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reason](structbt__le__per__adv__sync__term__info.md#a429b8b665eacbfe9db013a571b829bac);

1968};

1969

[ 1981](structbt__le__per__adv__sync__recv__info.md)struct [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md) {

[ 1983](structbt__le__per__adv__sync__recv__info.md#a5817bd4fba2c93adebcebe007650b6eb) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__per__adv__sync__recv__info.md#a5817bd4fba2c93adebcebe007650b6eb);

1984

[ 1986](structbt__le__per__adv__sync__recv__info.md#a21b0ca87e46c6897282ebd877e45114e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__recv__info.md#a21b0ca87e46c6897282ebd877e45114e);

1987

[ 1989](structbt__le__per__adv__sync__recv__info.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__per__adv__sync__recv__info.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e);

1990

[ 1992](structbt__le__per__adv__sync__recv__info.md#aa17c9d917469f121448ed4e1db485700) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__le__per__adv__sync__recv__info.md#aa17c9d917469f121448ed4e1db485700);

1993

[ 1995](structbt__le__per__adv__sync__recv__info.md#a1591907e3cb1f4565b9d26c18bccc7d2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cte\_type](structbt__le__per__adv__sync__recv__info.md#a1591907e3cb1f4565b9d26c18bccc7d2);

1996#if defined(CONFIG\_BT\_PER\_ADV\_SYNC\_RSP)

1998 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) periodic\_event\_counter;

1999

2001 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subevent;

2002#endif /\* CONFIG\_BT\_PER\_ADV\_SYNC\_RSP \*/

2003};

2004

[ 2012](structbt__le__per__adv__sync__state__info.md)struct [bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md) {

[ 2014](structbt__le__per__adv__sync__state__info.md#a4b0a3b7e36f935e06072304d6b92579f) bool [recv\_enabled](structbt__le__per__adv__sync__state__info.md#a4b0a3b7e36f935e06072304d6b92579f);

2015};

2016

2027

[ 2028](structbt__le__per__adv__sync__cb.md)struct [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md) {

[ 2039](structbt__le__per__adv__sync__cb.md#a815be4343ab589df433a551663c5f4a1) void (\*[synced](structbt__le__per__adv__sync__cb.md#a815be4343ab589df433a551663c5f4a1))(struct bt\_le\_per\_adv\_sync \*sync,

2040 struct [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md) \*info);

2041

[ 2052](structbt__le__per__adv__sync__cb.md#acbd565a39918e5dfe7603a020e73daec) void (\*[term](structbt__le__per__adv__sync__cb.md#acbd565a39918e5dfe7603a020e73daec))(struct bt\_le\_per\_adv\_sync \*sync,

2053 const struct [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md) \*info);

2054

[ 2068](structbt__le__per__adv__sync__cb.md#a5576248e2eaef2afebe606e05e55f05f) void (\*[recv](structbt__le__per__adv__sync__cb.md#a5576248e2eaef2afebe606e05e55f05f))(struct bt\_le\_per\_adv\_sync \*sync,

2069 const struct [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md) \*info,

2070 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

2071

[ 2082](structbt__le__per__adv__sync__cb.md#a656b4802f79d4a472c2367ade144d72e) void (\*[state\_changed](structbt__le__per__adv__sync__cb.md#a656b4802f79d4a472c2367ade144d72e))(struct bt\_le\_per\_adv\_sync \*sync,

2083 const struct [bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md) \*info);

2084

[ 2095](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9) void (\*[biginfo](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9))(struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_iso\_biginfo](structbt__iso__biginfo.md) \*[biginfo](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9));

2096

[ 2104](structbt__le__per__adv__sync__cb.md#ad2dc168696fbd22f7e3a089ac56f62d7) void (\*[cte\_report\_cb](structbt__le__per__adv__sync__cb.md#ad2dc168696fbd22f7e3a089ac56f62d7))(struct bt\_le\_per\_adv\_sync \*sync,

2105 struct [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md) const \*info);

2106

[ 2107](structbt__le__per__adv__sync__cb.md#a1977d27941063773c953a5f1dfa9ca76) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__le__per__adv__sync__cb.md#a1977d27941063773c953a5f1dfa9ca76);

2108};

2109

[ 2111](group__bt__gap.md#gac942d7e3cae8fca22080f93bf9528ee9)enum [bt\_le\_per\_adv\_sync\_opt](group__bt__gap.md#gac942d7e3cae8fca22080f93bf9528ee9) {

[ 2113](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9aeeef50a544edc104b39e4ef0c9a58d6c) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9aeeef50a544edc104b39e4ef0c9a58d6c) = 0,

2114

[ 2121](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9ae9a88caa6a83da8b1697a6167629bf7e) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9ae9a88caa6a83da8b1697a6167629bf7e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

2122

[ 2128](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9ae35a6eb572a2842e4cc2fc3677e19b53) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9ae35a6eb572a2842e4cc2fc3677e19b53) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

2129

[ 2131](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a9ec2b0c346c2cab7f61c2efcc8e37db2) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a9ec2b0c346c2cab7f61c2efcc8e37db2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

2132

[ 2134](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9aaa256e560f013eb74415d817154b8f4e) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9aaa256e560f013eb74415d817154b8f4e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

2135

[ 2137](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a99034652a92249e6d04065d68352020b) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a99034652a92249e6d04065d68352020b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

2138

[ 2140](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a0f52e38e513ec7eefcbc5c86c36f002e) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a0f52e38e513ec7eefcbc5c86c36f002e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

2141

[ 2143](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a5c702876d70d5eadc4df6e59d96b8320) [BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a5c702876d70d5eadc4df6e59d96b8320) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

2144};

2145

[ 2157](structbt__le__per__adv__sync__param.md)struct [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md) {

[ 2164](structbt__le__per__adv__sync__param.md#ac93adedad747f61a771ac5445e486b74) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__le__per__adv__sync__param.md#ac93adedad747f61a771ac5445e486b74);

2165

[ 2173](structbt__le__per__adv__sync__param.md#a70795642ee94dd9e87f0cf251c095e7f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__param.md#a70795642ee94dd9e87f0cf251c095e7f);

2174

[ 2176](structbt__le__per__adv__sync__param.md#a4252f2b3b453c2f9c8fbf8c35a618ff2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__per__adv__sync__param.md#a4252f2b3b453c2f9c8fbf8c35a618ff2);

2177

[ 2185](structbt__le__per__adv__sync__param.md#af9abb65547fb5bfea65f4c22963c7da0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__le__per__adv__sync__param.md#af9abb65547fb5bfea65f4c22963c7da0);

2186

[ 2193](structbt__le__per__adv__sync__param.md#a301cfd3d6e5620d29c021ababe104754) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__per__adv__sync__param.md#a301cfd3d6e5620d29c021ababe104754);

2194};

2195

[ 2207](group__bt__gap.md#ga8d05bd864d98b5b43595eb256e464024)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_le\_per\_adv\_sync\_get\_index](group__bt__gap.md#ga8d05bd864d98b5b43595eb256e464024)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

2208

[ 2221](group__bt__gap.md#ga59532b37412b1b93f81cf5cc1bab0534)struct bt\_le\_per\_adv\_sync \*[bt\_le\_per\_adv\_sync\_lookup\_index](group__bt__gap.md#ga59532b37412b1b93f81cf5cc1bab0534)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index);

2222

[ 2224](structbt__le__per__adv__sync__info.md)struct [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md) {

[ 2226](structbt__le__per__adv__sync__info.md#ac10fc2e2d3ec2160db8c2aac148d18a2) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__le__per__adv__sync__info.md#ac10fc2e2d3ec2160db8c2aac148d18a2);

2227

[ 2229](structbt__le__per__adv__sync__info.md#acc0ef26c38279c9a67f8992005c2e58a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__per__adv__sync__info.md#acc0ef26c38279c9a67f8992005c2e58a);

2230

[ 2232](structbt__le__per__adv__sync__info.md#a365a0d8577429e4ee96e977071c9a906) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__per__adv__sync__info.md#a365a0d8577429e4ee96e977071c9a906);

2233

[ 2235](structbt__le__per__adv__sync__info.md#a4d9520ea6a803f8fe4f41190f55c26e5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__le__per__adv__sync__info.md#a4d9520ea6a803f8fe4f41190f55c26e5);

2236};

2237

[ 2246](group__bt__gap.md#gabfaf265a48dd09ea02d114e2023c14a6)int [bt\_le\_per\_adv\_sync\_get\_info](group__bt__gap.md#gabfaf265a48dd09ea02d114e2023c14a6)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

2247 struct [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md) \*info);

2248

[ 2257](group__bt__gap.md#ga83126917373c0bcaa24964dd1d8bde46)struct bt\_le\_per\_adv\_sync \*[bt\_le\_per\_adv\_sync\_lookup\_addr](group__bt__gap.md#ga83126917373c0bcaa24964dd1d8bde46)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*adv\_addr,

2258 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid);

2259

[ 2276](group__bt__gap.md#ga061bf84b989b2c96ab51d2ca0debb017)int [bt\_le\_per\_adv\_sync\_create](group__bt__gap.md#ga061bf84b989b2c96ab51d2ca0debb017)(const struct [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md) \*param,

2277 struct bt\_le\_per\_adv\_sync \*\*out\_sync);

2278

[ 2295](group__bt__gap.md#gaa0c218ff3c78b26dcfaa726ee30267a6)int [bt\_le\_per\_adv\_sync\_delete](group__bt__gap.md#gaa0c218ff3c78b26dcfaa726ee30267a6)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

2296

[ 2311](group__bt__gap.md#ga4ee87bbf79e6ac844d14c3dafb2dadf4)int [bt\_le\_per\_adv\_sync\_cb\_register](group__bt__gap.md#ga4ee87bbf79e6ac844d14c3dafb2dadf4)(struct [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md) \*cb);

2312

[ 2322](group__bt__gap.md#ga07e4510de7e72c6ed6196b3da9fb40be)int [bt\_le\_per\_adv\_sync\_recv\_enable](group__bt__gap.md#ga07e4510de7e72c6ed6196b3da9fb40be)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

2323

[ 2333](group__bt__gap.md#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)int [bt\_le\_per\_adv\_sync\_recv\_disable](group__bt__gap.md#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync);

2334

[ 2336](group__bt__gap.md#ga820c5f3721e72662e558cc4576b6111b)enum [bt\_le\_per\_adv\_sync\_transfer\_opt](group__bt__gap.md#ga820c5f3721e72662e558cc4576b6111b) {

[ 2338](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111baef90aceabc3f9d0b17b7f3415152fca2) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111baef90aceabc3f9d0b17b7f3415152fca2) = 0,

2339

[ 2345](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111ba2694870b7ebd2dcd0b3834367f7d7061) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111ba2694870b7ebd2dcd0b3834367f7d7061) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

2346

[ 2353](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111bab0725048806858083be9ab3fcd9a36ed) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111bab0725048806858083be9ab3fcd9a36ed) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

2354

[ 2361](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111ba433ae469b27e820fdfd2a1d562010991) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111ba433ae469b27e820fdfd2a1d562010991) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

2362

[ 2364](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111baed2f78d682b5fbd1adf89c2f005e4f48) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111baed2f78d682b5fbd1adf89c2f005e4f48) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

2365

[ 2372](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111ba3f0be549ca5cac1cfbdec2f2227e73dc) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111ba3f0be549ca5cac1cfbdec2f2227e73dc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

2373

[ 2380](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111bad924f620ed6fdadbbea03f8e343b9d0c) [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111bad924f620ed6fdadbbea03f8e343b9d0c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

2381};

2382

[ 2393](structbt__le__per__adv__sync__transfer__param.md)struct [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md) {

[ 2400](structbt__le__per__adv__sync__transfer__param.md#a840e7cfac3a2947e5128d704067aaf7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [skip](structbt__le__per__adv__sync__transfer__param.md#a840e7cfac3a2947e5128d704067aaf7e);

2401

[ 2408](structbt__le__per__adv__sync__transfer__param.md#a5bfa84c6bdacdf8893a0951a5ce71fc6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__per__adv__sync__transfer__param.md#a5bfa84c6bdacdf8893a0951a5ce71fc6);

2409

[ 2411](structbt__le__per__adv__sync__transfer__param.md#a0b3ee6df1b409e64a064ffb6ac632cce) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structbt__le__per__adv__sync__transfer__param.md#a0b3ee6df1b409e64a064ffb6ac632cce);

2412};

2413

[ 2426](group__bt__gap.md#gaf81a1dd7a628d1a2f25c6b53b0679809)int [bt\_le\_per\_adv\_sync\_transfer](group__bt__gap.md#gaf81a1dd7a628d1a2f25c6b53b0679809)(const struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

2427 const struct bt\_conn \*conn,

2428 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) service\_data);

2429

2430

[ 2443](group__bt__gap.md#gac96199a4e5e6cfb789c1bd1c0e67d6fe)int [bt\_le\_per\_adv\_set\_info\_transfer](group__bt__gap.md#gac96199a4e5e6cfb789c1bd1c0e67d6fe)(const struct bt\_le\_ext\_adv \*adv,

2444 const struct bt\_conn \*conn,

2445 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) service\_data);

2446

[ 2460](group__bt__gap.md#gaa0658bd53df1d5e8e89e13330e4fd0ae)int [bt\_le\_per\_adv\_sync\_transfer\_subscribe](group__bt__gap.md#gaa0658bd53df1d5e8e89e13330e4fd0ae)(

2461 const struct bt\_conn \*conn,

2462 const struct [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md) \*param);

2463

[ 2477](group__bt__gap.md#ga08f872078045bbef4aca19761f25eeb8)int [bt\_le\_per\_adv\_sync\_transfer\_unsubscribe](group__bt__gap.md#ga08f872078045bbef4aca19761f25eeb8)(const struct bt\_conn \*conn);

2478

[ 2492](group__bt__gap.md#ga27c4961f3c7270a7f1caeadb4107854b)int [bt\_le\_per\_adv\_list\_add](group__bt__gap.md#ga27c4961f3c7270a7f1caeadb4107854b)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid);

2493

[ 2505](group__bt__gap.md#ga100efac4a49984e06202c63c4e5955cd)int [bt\_le\_per\_adv\_list\_remove](group__bt__gap.md#ga100efac4a49984e06202c63c4e5955cd)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid);

2506

[ 2514](group__bt__gap.md#ga5909bd768c23a19a42a660e3b814c981)int [bt\_le\_per\_adv\_list\_clear](group__bt__gap.md#ga5909bd768c23a19a42a660e3b814c981)(void);

2515

2516

[ 2517](group__bt__gap.md#gab4b5773898e2a1eef21557915a21c996)enum [bt\_le\_scan\_opt](group__bt__gap.md#gab4b5773898e2a1eef21557915a21c996) {

[ 2519](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996aad3f19e5849b6d6813fa88257082e185) [BT\_LE\_SCAN\_OPT\_NONE](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996aad3f19e5849b6d6813fa88257082e185) = 0,

2520

[ 2522](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996a0af65ac48e068f7e6f1815cb151d4394) [BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996a0af65ac48e068f7e6f1815cb151d4394) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

2523

[ 2525](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996af7a25b6790b138b2b88de3c7d81cb0ae) [BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996af7a25b6790b138b2b88de3c7d81cb0ae) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

2526

[ 2528](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996a16f171c649dd090333e9822a92b4bbdb) [BT\_LE\_SCAN\_OPT\_CODED](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996a16f171c649dd090333e9822a92b4bbdb) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

2529

[ 2535](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996a7ff0c79b2675e7b7512379e2cbedc0a6) [BT\_LE\_SCAN\_OPT\_NO\_1M](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996a7ff0c79b2675e7b7512379e2cbedc0a6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

2536};

2537

[ 2538](group__bt__gap.md#gaf980473379afa477c09e19912d40d29e)enum [bt\_le\_scan\_type](group__bt__gap.md#gaf980473379afa477c09e19912d40d29e) {

[ 2540](group__bt__gap.md#ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006) [BT\_LE\_SCAN\_TYPE\_PASSIVE](group__bt__gap.md#ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006) = 0x00,

2541

[ 2549](group__bt__gap.md#ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22) [BT\_LE\_SCAN\_TYPE\_ACTIVE](group__bt__gap.md#ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22) = 0x01,

2550};

2551

[ 2553](structbt__le__scan__param.md)struct [bt\_le\_scan\_param](structbt__le__scan__param.md) {

[ 2555](structbt__le__scan__param.md#a02d75322390287c3fa754bf915660d0c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__le__scan__param.md#a02d75322390287c3fa754bf915660d0c);

2556

[ 2558](structbt__le__scan__param.md#ac815b05fee8ce0dd24228305b7596207) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [options](structbt__le__scan__param.md#ac815b05fee8ce0dd24228305b7596207);

2559

[ 2568](structbt__le__scan__param.md#a2f4e053d97c62b6fdf42a245908607f8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__scan__param.md#a2f4e053d97c62b6fdf42a245908607f8);

2569

[ 2578](structbt__le__scan__param.md#a37a7ee82e86a91cf7a9c2adf60bb526a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window](structbt__le__scan__param.md#a37a7ee82e86a91cf7a9c2adf60bb526a);

2579

[ 2586](structbt__le__scan__param.md#a3e71ce551dcc7762c29e2316996e2912) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structbt__le__scan__param.md#a3e71ce551dcc7762c29e2316996e2912);

2587

[ 2593](structbt__le__scan__param.md#a67a20bc94a3d98fa10af7b5b42dde328) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval\_coded](structbt__le__scan__param.md#a67a20bc94a3d98fa10af7b5b42dde328);

2594

[ 2600](structbt__le__scan__param.md#a93166af55dca71393c60cb3f7ac6d809) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [window\_coded](structbt__le__scan__param.md#a93166af55dca71393c60cb3f7ac6d809);

2601};

2602

[ 2604](structbt__le__scan__recv__info.md)struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) {

[ 2611](structbt__le__scan__recv__info.md#a907fb7ec3c78d68da5015a8c3afc3084) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__le__scan__recv__info.md#a907fb7ec3c78d68da5015a8c3afc3084);

2612

[ 2614](structbt__le__scan__recv__info.md#a4df8d4e1fdd7514d170744856ebe7015) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__le__scan__recv__info.md#a4df8d4e1fdd7514d170744856ebe7015);

2615

[ 2617](structbt__le__scan__recv__info.md#a88f677733147245ccbf861c7fc5e0f11) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [rssi](structbt__le__scan__recv__info.md#a88f677733147245ccbf861c7fc5e0f11);

2618

[ 2620](structbt__le__scan__recv__info.md#a2addeba6d2ec8e55dc5379adf6519148) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structbt__le__scan__recv__info.md#a2addeba6d2ec8e55dc5379adf6519148);

2621

[ 2630](structbt__le__scan__recv__info.md#adccb2ce5c6d228bd7f8f050088629524) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [adv\_type](structbt__le__scan__recv__info.md#adccb2ce5c6d228bd7f8f050088629524);

2631

[ 2640](structbt__le__scan__recv__info.md#af29ddfb59e286af9ca465cbd5a91bf2d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [adv\_props](structbt__le__scan__recv__info.md#af29ddfb59e286af9ca465cbd5a91bf2d);

2641

[ 2647](structbt__le__scan__recv__info.md#a1060c5937708ff81a64f068e02fc7826) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structbt__le__scan__recv__info.md#a1060c5937708ff81a64f068e02fc7826);

2648

[ 2650](structbt__le__scan__recv__info.md#a6189ed8453cb7907f34dc7dfaf1343bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [primary\_phy](structbt__le__scan__recv__info.md#a6189ed8453cb7907f34dc7dfaf1343bd);

2651

[ 2653](structbt__le__scan__recv__info.md#ac797291291dc7ba7ac171ed7f24f0d16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [secondary\_phy](structbt__le__scan__recv__info.md#ac797291291dc7ba7ac171ed7f24f0d16);

2654};

2655

[ 2657](structbt__le__scan__cb.md)struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) {

2658

[ 2665](structbt__le__scan__cb.md#a71d73c1da28d4a27626f77d96a5b3541) void (\*[recv](structbt__le__scan__cb.md#a71d73c1da28d4a27626f77d96a5b3541))(const struct [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) \*info,

2666 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

2667

[ 2669](structbt__le__scan__cb.md#a2f57f3fee46bd137065f4c57d0cd5157) void (\*[timeout](structbt__le__scan__cb.md#a2f57f3fee46bd137065f4c57d0cd5157))(void);

2670

[ 2671](structbt__le__scan__cb.md#a50dbc5e7618fd488e9acb7ad8f104a63) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__le__scan__cb.md#a50dbc5e7618fd488e9acb7ad8f104a63);

2672};

2673

[ 2682](group__bt__gap.md#gac9f372ca16afb1c2f0e100c5b1b94cd5)#define BT\_LE\_SCAN\_PARAM\_INIT(\_type, \_options, \_interval, \_window) \

2683{ \

2684 .type = (\_type), \

2685 .options = (\_options), \

2686 .interval = (\_interval), \

2687 .window = (\_window), \

2688 .timeout = 0, \

2689 .interval\_coded = 0, \

2690 .window\_coded = 0, \

2691}

2692

[ 2701](group__bt__gap.md#ga57ace75133343ba8de7fa965f452ee3d)#define BT\_LE\_SCAN\_PARAM(\_type, \_options, \_interval, \_window) \

2702 ((struct bt\_le\_scan\_param[]) { \

2703 BT\_LE\_SCAN\_PARAM\_INIT(\_type, \_options, \_interval, \_window) \

2704 })

2705

[ 2709](group__bt__gap.md#gac137ea4ce32697582a337116ffa41da5)#define BT\_LE\_SCAN\_ACTIVE BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_ACTIVE, \

2710 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2711 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2712 BT\_GAP\_SCAN\_FAST\_WINDOW)

2713

[ 2719](group__bt__gap.md#ga9bd9701db0459c066ed7c18343f60911)#define BT\_LE\_SCAN\_ACTIVE\_CONTINUOUS BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_ACTIVE, \

2720 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2721 BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN, \

2722 BT\_GAP\_SCAN\_FAST\_WINDOW)

2723BUILD\_ASSERT([BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0) == [BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN](group__bt__gap__defines.md#gae9356673ee78d9abb27891738344513a),

2724 "Continuous scanning is requested by setting window and interval equal.");

2725

[ 2732](group__bt__gap.md#ga8ceaef6f0fbf4fe2d76d47e8f59aeb11)#define BT\_LE\_SCAN\_PASSIVE BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_PASSIVE, \

2733 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2734 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2735 BT\_GAP\_SCAN\_FAST\_WINDOW)

2736

[ 2743](group__bt__gap.md#ga8d8ccc9ea1db2c96deae1603ec1c78a3)#define BT\_LE\_SCAN\_PASSIVE\_CONTINUOUS BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_PASSIVE, \

2744 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2745 BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN, \

2746 BT\_GAP\_SCAN\_FAST\_WINDOW)

2747BUILD\_ASSERT([BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0) == [BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN](group__bt__gap__defines.md#gae9356673ee78d9abb27891738344513a),

2748 "Continuous scanning is requested by setting window and interval equal.");

2749

[ 2754](group__bt__gap.md#ga06380c4ae6289c704a143b9d192bc35f)#define BT\_LE\_SCAN\_CODED\_ACTIVE \

2755 BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_ACTIVE, \

2756 BT\_LE\_SCAN\_OPT\_CODED | \

2757 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2758 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2759 BT\_GAP\_SCAN\_FAST\_WINDOW)

2760

[ 2768](group__bt__gap.md#ga1e5a4589304babc6b0d49019ebcff6b0)#define BT\_LE\_SCAN\_CODED\_PASSIVE \

2769 BT\_LE\_SCAN\_PARAM(BT\_LE\_SCAN\_TYPE\_PASSIVE, \

2770 BT\_LE\_SCAN\_OPT\_CODED | \

2771 BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE, \

2772 BT\_GAP\_SCAN\_FAST\_INTERVAL, \

2773 BT\_GAP\_SCAN\_FAST\_WINDOW)

2774

[ 2804](group__bt__gap.md#gac5e19c26b53a08dadb8efa7ecc692ad6)int [bt\_le\_scan\_start](group__bt__gap.md#gac5e19c26b53a08dadb8efa7ecc692ad6)(const struct [bt\_le\_scan\_param](structbt__le__scan__param.md) \*param, [bt\_le\_scan\_cb\_t](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4) cb);

2805

[ 2814](group__bt__gap.md#gaa2de1a1ab523606b36a4c445fb0c3b84)int [bt\_le\_scan\_stop](group__bt__gap.md#gaa2de1a1ab523606b36a4c445fb0c3b84)(void);

2815

[ 2829](group__bt__gap.md#ga80e870fa1de40c404c64624bef439067)int [bt\_le\_scan\_cb\_register](group__bt__gap.md#ga80e870fa1de40c404c64624bef439067)(struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \*cb);

2830

[ 2838](group__bt__gap.md#gac2718f2128b3f8c79b12d760771c8378)void [bt\_le\_scan\_cb\_unregister](group__bt__gap.md#gac2718f2128b3f8c79b12d760771c8378)(struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \*cb);

2839

[ 2854](group__bt__gap.md#ga40f2f7fdb09aba3c5137f680e67792f0)int [bt\_le\_filter\_accept\_list\_add](group__bt__gap.md#ga40f2f7fdb09aba3c5137f680e67792f0)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

2855

[ 2870](group__bt__gap.md#ga0532ed768ab4f9d69c202066d2f87e66)int [bt\_le\_filter\_accept\_list\_remove](group__bt__gap.md#ga0532ed768ab4f9d69c202066d2f87e66)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

2871

[ 2884](group__bt__gap.md#gac87df899d1e363c63162988157ee6d00)int [bt\_le\_filter\_accept\_list\_clear](group__bt__gap.md#gac87df899d1e363c63162988157ee6d00)(void);

2885

[ 2901](group__bt__gap.md#gabc115fd3fff6d00ae878a31613bf70aa)int [bt\_le\_set\_chan\_map](group__bt__gap.md#gabc115fd3fff6d00ae878a31613bf70aa)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_map[5]);

2902

[ 2919](group__bt__gap.md#ga9ab41e118b5496c196e56b8b5d023275)int [bt\_le\_set\_rpa\_timeout](group__bt__gap.md#ga9ab41e118b5496c196e56b8b5d023275)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) new\_rpa\_timeout);

2920

[ 2940](group__bt__gap.md#ga652eef01e5256e0d820cd1f4db877429)void [bt\_data\_parse](group__bt__gap.md#ga652eef01e5256e0d820cd1f4db877429)(struct [net\_buf\_simple](structnet__buf__simple.md) \*ad,

2941 bool (\*func)(struct [bt\_data](structbt__data.md) \*[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1), void \*user\_data),

2942 void \*user\_data);

2943

[ 2945](structbt__le__oob__sc__data.md)struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) {

[ 2947](structbt__le__oob__sc__data.md#afa64bcc048d0e8709e262e2848a39d2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [r](structbt__le__oob__sc__data.md#afa64bcc048d0e8709e262e2848a39d2c)[16];

2948

[ 2950](structbt__le__oob__sc__data.md#a9bd93f1e9e41e241d0f84ae16ae47ba1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c](structbt__le__oob__sc__data.md#a9bd93f1e9e41e241d0f84ae16ae47ba1)[16];

2951};

2952

[ 2954](structbt__le__oob.md)struct [bt\_le\_oob](structbt__le__oob.md) {

[ 2958](structbt__le__oob.md#a17cfed7683efbf5b5954847d655d7424) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__le__oob.md#a17cfed7683efbf5b5954847d655d7424);

2959

[ 2961](structbt__le__oob.md#a80ccd4ab120a880adfff9aba3b19b4fd) struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) [le\_sc\_data](structbt__le__oob.md#a80ccd4ab120a880adfff9aba3b19b4fd);

2962};

2963

[ 2993](group__bt__gap.md#ga296d1adf3c9ed2f2c65bb75b887d59ee)int [bt\_le\_oob\_get\_local](group__bt__gap.md#ga296d1adf3c9ed2f2c65bb75b887d59ee)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, struct [bt\_le\_oob](structbt__le__oob.md) \*oob);

2994

[ 3019](group__bt__gap.md#ga7486aab863ca497a50dacf81657f48d4)int [bt\_le\_ext\_adv\_oob\_get\_local](group__bt__gap.md#ga7486aab863ca497a50dacf81657f48d4)(struct bt\_le\_ext\_adv \*adv,

3020 struct [bt\_le\_oob](structbt__le__oob.md) \*oob);

3021

[ 3032](group__bt__gap.md#gaceabbbe6e844650f791010e53c9df6a4)int [bt\_unpair](group__bt__gap.md#gaceabbbe6e844650f791010e53c9df6a4)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

3033

[ 3035](structbt__bond__info.md)struct [bt\_bond\_info](structbt__bond__info.md) {

[ 3037](structbt__bond__info.md#a6b328ce30fd53bb73ecd8e033bb91d1f) [bt\_addr\_le\_t](structbt__addr__le__t.md) [addr](structbt__bond__info.md#a6b328ce30fd53bb73ecd8e033bb91d1f);

3038};

3039

[ 3048](group__bt__gap.md#gaad380b7f8984f8522c1b79f9bdc04905)void [bt\_foreach\_bond](group__bt__gap.md#gaad380b7f8984f8522c1b79f9bdc04905)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, void (\*func)(const struct [bt\_bond\_info](structbt__bond__info.md) \*info,

3049 void \*user\_data),

3050 void \*user\_data);

3051

[ 3067](group__bt__gap.md#ga8046c2b06d3dad0d6c8184de492517d2)int [bt\_configure\_data\_path](group__bt__gap.md#ga8046c2b06d3dad0d6c8184de492517d2)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dir, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vs\_config\_len,

3068 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vs\_config);

3069

[ 3079](structbt__le__per__adv__sync__subevent__params.md)struct [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md) {

[ 3085](structbt__le__per__adv__sync__subevent__params.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [properties](structbt__le__per__adv__sync__subevent__params.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4);

3086

[ 3088](structbt__le__per__adv__sync__subevent__params.md#a867c66bf09461a4369da3d250701d2ae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__le__per__adv__sync__subevent__params.md#a867c66bf09461a4369da3d250701d2ae);

3089

[ 3095](structbt__le__per__adv__sync__subevent__params.md#a5ac4e81ddd63797f921105748344c125) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[subevents](structbt__le__per__adv__sync__subevent__params.md#a5ac4e81ddd63797f921105748344c125);

3096};

3097

[ 3108](group__bt__gap.md#ga731f4b37a9e5cc13a6816ea23f751b0b)int [bt\_le\_per\_adv\_sync\_subevent](group__bt__gap.md#ga731f4b37a9e5cc13a6816ea23f751b0b)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

3109 struct [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md) \*params);

3110

[ 3119](structbt__le__per__adv__response__params.md)struct [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md) {

[ 3129](structbt__le__per__adv__response__params.md#a1af01d0a027fb8659615874acbd388f9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [request\_event](structbt__le__per__adv__response__params.md#a1af01d0a027fb8659615874acbd388f9);

3130

[ 3137](structbt__le__per__adv__response__params.md#a3fc8ab0feb06714b28d22439cce60e41) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [request\_subevent](structbt__le__per__adv__response__params.md#a3fc8ab0feb06714b28d22439cce60e41);

3138

[ 3140](structbt__le__per__adv__response__params.md#a0cec222d5ba8cc9e20939d441646c913) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_subevent](structbt__le__per__adv__response__params.md#a0cec222d5ba8cc9e20939d441646c913);

3141

[ 3143](structbt__le__per__adv__response__params.md#aea0428083ccd5f4dccc17e494f38b7c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [response\_slot](structbt__le__per__adv__response__params.md#aea0428083ccd5f4dccc17e494f38b7c3);

3144};

3145

[ 3158](group__bt__gap.md#gaae6b8583f7d5457f20b03dccd146425e)int [bt\_le\_per\_adv\_set\_response\_data](group__bt__gap.md#gaae6b8583f7d5457f20b03dccd146425e)(struct bt\_le\_per\_adv\_sync \*per\_adv\_sync,

3159 const struct [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md) \*params,

3160 const struct [net\_buf\_simple](structnet__buf__simple.md) \*data);

3161

[ 3174](group__bt__gap.md#ga309a67de79cc215db1d33251f267f361)bool [bt\_le\_bond\_exists](group__bt__gap.md#ga309a67de79cc215db1d33251f267f361)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr);

3175

3179

3180#ifdef \_\_cplusplus

3181}

3182#endif

3186

3187#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_BLUETOOTH\_H\_ \*/

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

Get the currently configured identity addresses.

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

**Definition** bluetooth.h:1781

[bt\_le\_ext\_adv\_stop](group__bt__gap.md#ga1c864c4b183f9a86c9f70a11471c5b15)

int bt\_le\_ext\_adv\_stop(struct bt\_le\_ext\_adv \*adv)

Stop advertising with the given advertising set.

[bt\_le\_per\_adv\_list\_add](group__bt__gap.md#ga27c4961f3c7270a7f1caeadb4107854b)

int bt\_le\_per\_adv\_list\_add(const bt\_addr\_le\_t \*addr, uint8\_t sid)

Add a device to the periodic advertising list.

[bt\_le\_oob\_get\_local](group__bt__gap.md#ga296d1adf3c9ed2f2c65bb75b887d59ee)

int bt\_le\_oob\_get\_local(uint8\_t id, struct bt\_le\_oob \*oob)

Get local LE Out of Band (OOB) information.

[bt\_le\_bond\_exists](group__bt__gap.md#ga309a67de79cc215db1d33251f267f361)

bool bt\_le\_bond\_exists(uint8\_t id, const bt\_addr\_le\_t \*addr)

Check if a device identified by a Bluetooth LE address is bonded.

[bt\_get\_appearance](group__bt__gap.md#ga35b76ea7ce79721e47ca4164e08b2dfb)

uint16\_t bt\_get\_appearance(void)

Get local Bluetooth appearance.

[bt\_data\_serialize](group__bt__gap.md#ga3c067b16468ebd17973faeded0fc83c9)

size\_t bt\_data\_serialize(const struct bt\_data \*input, uint8\_t \*output)

Serialize a bt\_data struct into an advertising structure (a flat array).

[bt\_data\_get\_len](group__bt__gap.md#ga3d2c6adc42eb9510734630f38d921b9a)

size\_t bt\_data\_get\_len(const struct bt\_data data[], size\_t data\_count)

Get the total size (in octets) of a given set of bt\_data structures.

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

**Definition** bluetooth.h:294

[bt\_le\_ext\_adv\_state](group__bt__gap.md#ga544ccde35638d8f580942d830fe9f242)

bt\_le\_ext\_adv\_state

Advertising states.

**Definition** bluetooth.h:1718

[bt\_le\_per\_adv\_list\_clear](group__bt__gap.md#ga5909bd768c23a19a42a660e3b814c981)

int bt\_le\_per\_adv\_list\_clear(void)

Clear the periodic advertising list.

[bt\_le\_per\_adv\_sync\_lookup\_index](group__bt__gap.md#ga59532b37412b1b93f81cf5cc1bab0534)

struct bt\_le\_per\_adv\_sync \* bt\_le\_per\_adv\_sync\_lookup\_index(uint8\_t index)

Get a periodic advertising sync object from the array index.

[bt\_le\_ext\_adv\_delete](group__bt__gap.md#ga62310a27f7fea925dfcf3abd7c454787)

int bt\_le\_ext\_adv\_delete(struct bt\_le\_ext\_adv \*adv)

Delete advertising set.

[bt\_le\_get\_local\_features](group__bt__gap.md#ga650faa2a86f54499f4bc5a8657a55a87)

int bt\_le\_get\_local\_features(struct bt\_le\_local\_features \*local\_features)

Get local Bluetooth LE controller features.

[bt\_data\_parse](group__bt__gap.md#ga652eef01e5256e0d820cd1f4db877429)

void bt\_data\_parse(struct net\_buf\_simple \*ad, bool(\*func)(struct bt\_data \*data, void \*user\_data), void \*user\_data)

Helper for parsing advertising (or EIR or OOB) data.

[bt\_le\_per\_adv\_state](group__bt__gap.md#ga6bb77c0808c761753650cde28ddb013e)

bt\_le\_per\_adv\_state

Periodic Advertising states.

**Definition** bluetooth.h:1727

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

[bt\_le\_per\_adv\_sync\_transfer\_opt](group__bt__gap.md#ga820c5f3721e72662e558cc4576b6111b)

bt\_le\_per\_adv\_sync\_transfer\_opt

Periodic Advertising Sync Transfer options.

**Definition** bluetooth.h:2336

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

[BT\_LE\_LOCAL\_SUPPORTED\_FEATURES\_SIZE](group__bt__gap.md#gaa26f90b188caa50ca12247b7911a0a5f)

#define BT\_LE\_LOCAL\_SUPPORTED\_FEATURES\_SIZE

Number of octets for local supported.

**Definition** bluetooth.h:78

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

[bt\_le\_scan\_opt](group__bt__gap.md#gab4b5773898e2a1eef21557915a21c996)

bt\_le\_scan\_opt

**Definition** bluetooth.h:2517

[bt\_id\_reset](group__bt__gap.md#gabb3353edc8a3a8d29a0370049b20cbe4)

int bt\_id\_reset(uint8\_t id, bt\_addr\_le\_t \*addr, uint8\_t \*irk)

Reset/reclaim an identity address for reuse.

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

[bt\_le\_per\_adv\_sync\_opt](group__bt__gap.md#gac942d7e3cae8fca22080f93bf9528ee9)

bt\_le\_per\_adv\_sync\_opt

Periodic advertising sync options.

**Definition** bluetooth.h:2111

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

Create a new identity address.

[bt\_le\_per\_adv\_opt](group__bt__gap.md#gae60a45dde6b4d9f4c54a2a6070254f11)

bt\_le\_per\_adv\_opt

Periodic Advertising options.

**Definition** bluetooth.h:1070

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

Delete an identity address.

[bt\_le\_per\_adv\_sync\_transfer](group__bt__gap.md#gaf81a1dd7a628d1a2f25c6b53b0679809)

int bt\_le\_per\_adv\_sync\_transfer(const struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, const struct bt\_conn \*conn, uint16\_t service\_data)

Transfer the periodic advertising sync information to a peer device.

[bt\_le\_scan\_type](group__bt__gap.md#gaf980473379afa477c09e19912d40d29e)

bt\_le\_scan\_type

**Definition** bluetooth.h:2538

[bt\_le\_adv\_opt](group__bt__gap.md#gafbf81dab68b0e484d4742471c722fc28)

bt\_le\_adv\_opt

Advertising options.

**Definition** bluetooth.h:683

[bt\_le\_per\_adv\_set\_data](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899)

int bt\_le\_per\_adv\_set\_data(const struct bt\_le\_ext\_adv \*adv, const struct bt\_data \*ad, size\_t ad\_len)

Set or update the periodic advertising data.

[BT\_LE\_EXT\_ADV\_STATE\_DISABLED](group__bt__gap.md#gga544ccde35638d8f580942d830fe9f242a4423f4792711b21cf38a4e63c148760d)

@ BT\_LE\_EXT\_ADV\_STATE\_DISABLED

The advertising set has been created but not enabled.

**Definition** bluetooth.h:1720

[BT\_LE\_EXT\_ADV\_STATE\_ENABLED](group__bt__gap.md#gga544ccde35638d8f580942d830fe9f242afe851bf904c1cfed3ff10a57430d6a07)

@ BT\_LE\_EXT\_ADV\_STATE\_ENABLED

The advertising set is enabled.

**Definition** bluetooth.h:1723

[BT\_LE\_PER\_ADV\_STATE\_ENABLED](group__bt__gap.md#gga6bb77c0808c761753650cde28ddb013ea492cf25dc85090cfa72d5e2bdc0917f3)

@ BT\_LE\_PER\_ADV\_STATE\_ENABLED

Periodic advertising is enabled.

**Definition** bluetooth.h:1735

[BT\_LE\_PER\_ADV\_STATE\_DISABLED](group__bt__gap.md#gga6bb77c0808c761753650cde28ddb013eac26ccfbb5c715b515ef82c1993eff03b)

@ BT\_LE\_PER\_ADV\_STATE\_DISABLED

The advertising set has been configured for periodic advertising, but is not enabled.

**Definition** bluetooth.h:1732

[BT\_LE\_PER\_ADV\_STATE\_NONE](group__bt__gap.md#gga6bb77c0808c761753650cde28ddb013ead690730da823fcb31f102f154a23b01c)

@ BT\_LE\_PER\_ADV\_STATE\_NONE

Not configured for periodic advertising.

**Definition** bluetooth.h:1729

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111ba2694870b7ebd2dcd0b3834367f7d7061)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA

No Angle of Arrival (AoA).

**Definition** bluetooth.h:2345

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111ba3f0be549ca5cac1cfbdec2f2227e73dc)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED

Sync to received PAST packets but don't generate sync reports.

**Definition** bluetooth.h:2372

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111ba433ae469b27e820fdfd2a1d562010991)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US

No Angle of Departure (AoD) 2.

**Definition** bluetooth.h:2361

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111bab0725048806858083be9ab3fcd9a36ed)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US

No Angle of Departure (AoD) 1 us.

**Definition** bluetooth.h:2353

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111bad924f620ed6fdadbbea03f8e343b9d0c)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES

Sync to received PAST packets and generate sync reports with duplicate filtering.

**Definition** bluetooth.h:2380

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111baed2f78d682b5fbd1adf89c2f005e4f48)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE

Only sync to packets with constant tone extension.

**Definition** bluetooth.h:2364

[BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE](group__bt__gap.md#gga820c5f3721e72662e558cc4576b6111baef90aceabc3f9d0b17b7f3415152fca2)

@ BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:2338

[BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996a0af65ac48e068f7e6f1815cb151d4394)

@ BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE

Filter duplicates.

**Definition** bluetooth.h:2522

[BT\_LE\_SCAN\_OPT\_CODED](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996a16f171c649dd090333e9822a92b4bbdb)

@ BT\_LE\_SCAN\_OPT\_CODED

Enable scan on coded PHY (Long Range).

**Definition** bluetooth.h:2528

[BT\_LE\_SCAN\_OPT\_NO\_1M](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996a7ff0c79b2675e7b7512379e2cbedc0a6)

@ BT\_LE\_SCAN\_OPT\_NO\_1M

Disable scan on 1M phy.

**Definition** bluetooth.h:2535

[BT\_LE\_SCAN\_OPT\_NONE](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996aad3f19e5849b6d6813fa88257082e185)

@ BT\_LE\_SCAN\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:2519

[BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](group__bt__gap.md#ggab4b5773898e2a1eef21557915a21c996af7a25b6790b138b2b88de3c7d81cb0ae)

@ BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST

Filter using filter accept list.

**Definition** bluetooth.h:2525

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a0f52e38e513ec7eefcbc5c86c36f002e)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US

Sync with Angle of Departure (AoD) 2 us constant tone extension.

**Definition** bluetooth.h:2140

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a5c702876d70d5eadc4df6e59d96b8320)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT

Do not sync to packets without a constant tone extension.

**Definition** bluetooth.h:2143

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a99034652a92249e6d04065d68352020b)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US

Sync with Angle of Departure (AoD) 1 us constant tone extension.

**Definition** bluetooth.h:2137

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9a9ec2b0c346c2cab7f61c2efcc8e37db2)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE

Filter duplicate Periodic Advertising reports.

**Definition** bluetooth.h:2131

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9aaa256e560f013eb74415d817154b8f4e)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA

Sync with Angle of Arrival (AoA) constant tone extension.

**Definition** bluetooth.h:2134

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9ae35a6eb572a2842e4cc2fc3677e19b53)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED

Disables periodic advertising reports.

**Definition** bluetooth.h:2128

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9ae9a88caa6a83da8b1697a6167629bf7e)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST

Use the periodic advertising list to sync with advertiser.

**Definition** bluetooth.h:2121

[BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE](group__bt__gap.md#ggac942d7e3cae8fca22080f93bf9528ee9aeeef50a544edc104b39e4ef0c9a58d6c)

@ BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:2113

[BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI](group__bt__gap.md#ggae60a45dde6b4d9f4c54a2a6070254f11a38cebc2ae885ff630b34c603e2ec6403)

@ BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI

Advertise with included AdvDataInfo (ADI).

**Definition** bluetooth.h:1088

[BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#ggae60a45dde6b4d9f4c54a2a6070254f11a9524537e4cb726f4ff10ba93381bb27f)

@ BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER

Advertise with transmit power.

**Definition** bluetooth.h:1080

[BT\_LE\_PER\_ADV\_OPT\_NONE](group__bt__gap.md#ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518)

@ BT\_LE\_PER\_ADV\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:1072

[BT\_LE\_SCAN\_TYPE\_PASSIVE](group__bt__gap.md#ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006)

@ BT\_LE\_SCAN\_TYPE\_PASSIVE

Scan without requesting additional information from advertisers.

**Definition** bluetooth.h:2540

[BT\_LE\_SCAN\_TYPE\_ACTIVE](group__bt__gap.md#ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22)

@ BT\_LE\_SCAN\_TYPE\_ACTIVE

Scan and request additional information from advertisers.

**Definition** bluetooth.h:2549

[BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a0a9642077d93cf9c0eb42f64a9e34e73)

@ BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD

Put GAP device name into advert data.

**Definition** bluetooth.h:938

[BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a1563b053f457833d1a3d11c8dc4d394b)

@ BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ

Notify the application when a scan response data has been sent to an active scanner.

**Definition** bluetooth.h:838

[BT\_LE\_ADV\_OPT\_ANONYMOUS](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a185e0f884f8b0ce79625448638de8fab)

@ BT\_LE\_ADV\_OPT\_ANONYMOUS

Advertise without a device address (identity address or RPA).

**Definition** bluetooth.h:908

[BT\_LE\_ADV\_OPT\_USE\_NRPA](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a22958d8539d661ad7ca8d3f1173e7e5e)

@ BT\_LE\_ADV\_OPT\_USE\_NRPA

Advertise using a Non-Resolvable Private Address.

**Definition** bluetooth.h:952

[BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a2a90f8d144a194f74c5432079c5d42a3)

@ BT\_LE\_ADV\_OPT\_CONNECTABLE

Advertise as connectable.

**Definition** bluetooth.h:707

[BT\_LE\_ADV\_OPT\_USE\_NAME](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a2dbc9ec77d6de134d96a7bd3d9256398)

@ BT\_LE\_ADV\_OPT\_USE\_NAME

Advertise using GAP device name.

**Definition** bluetooth.h:803

[BT\_LE\_ADV\_OPT\_USE\_IDENTITY](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a407cf5ae358d3c00dd7e47dfaad3ec6e)

@ BT\_LE\_ADV\_OPT\_USE\_IDENTITY

Advertise using identity address.

**Definition** bluetooth.h:777

[BT\_LE\_ADV\_OPT\_ONE\_TIME](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a7d12782a02afefcf4b5c04442a99f8a2)

@ BT\_LE\_ADV\_OPT\_ONE\_TIME

Advertise one time.

**Definition** bluetooth.h:737

[BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a807ba316edc49c8448a8ff7d497173f5)

@ BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ

Use filter accept list to filter devices that can request scan response data.

**Definition** bluetooth.h:830

[BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a89f7494620236c976bf1a76a880e2a28)

@ BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39

Disable advertising on channel index 39.

**Definition** bluetooth.h:925

[BT\_LE\_ADV\_OPT\_NONE](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a928b376123819cb0a69fbb5b35608dbf)

@ BT\_LE\_ADV\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:685

[BT\_LE\_ADV\_OPT\_REQUIRE\_S2\_CODING](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28a9a35ede118224d6ed17f252fff6bb47e)

@ BT\_LE\_ADV\_OPT\_REQUIRE\_S2\_CODING

Configures the advertiser to use the S=2 coding scheme for LE Coded PHY.

**Definition** bluetooth.h:969

[BT\_LE\_ADV\_OPT\_CONN](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169)

@ BT\_LE\_ADV\_OPT\_CONN

Connectable advertising.

**Definition** bluetooth.h:765

[BT\_LE\_ADV\_OPT\_REQUIRE\_S8\_CODING](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aa6a61768ad4102f199d3970791118bb8)

@ BT\_LE\_ADV\_OPT\_REQUIRE\_S8\_CODING

Configures the advertiser to use the S=8 coding scheme for LE Coded PHY.

**Definition** bluetooth.h:986

[BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ab46741616f8bfe50c4b492d1f7970779)

@ BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37

Disable advertising on channel index 37.

**Definition** bluetooth.h:919

[BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28abd9cb02691d7e025fe3fea9a80123275)

@ BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38

Disable advertising on channel index 38.

**Definition** bluetooth.h:922

[BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28abdcf1c80662061fa30575e1f9fc6cf6f)

@ BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA

Directed advertising to privacy-enabled peer.

**Definition** bluetooth.h:825

[BT\_LE\_ADV\_OPT\_CODED](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ad01c4962a350d3218ba0cabd713708b1)

@ BT\_LE\_ADV\_OPT\_CODED

Advertise on the LE Coded PHY (Long Range).

**Definition** bluetooth.h:900

[BT\_LE\_ADV\_OPT\_FILTER\_CONN](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ad5efef3d01731110dbd71d5a5dc9baaf)

@ BT\_LE\_ADV\_OPT\_FILTER\_CONN

Use filter accept list to filter devices that can connect.

**Definition** bluetooth.h:833

[BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab)

@ BT\_LE\_ADV\_OPT\_EXT\_ADV

Advertise with extended advertising.

**Definition** bluetooth.h:870

[BT\_LE\_ADV\_OPT\_SCANNABLE](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae60eafe69ef10b84f61a1f4accf789c9)

@ BT\_LE\_ADV\_OPT\_SCANNABLE

Support scan response data.

**Definition** bluetooth.h:848

[BT\_LE\_ADV\_OPT\_NO\_2M](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28ae864aefcdfbecaffe823b9b144fe0a6b)

@ BT\_LE\_ADV\_OPT\_NO\_2M

Disable use of LE 2M PHY on the secondary advertising channel.

**Definition** bluetooth.h:887

[BT\_LE\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28aecff4fe3ac3d1fba3f6fa76c77713859)

@ BT\_LE\_ADV\_OPT\_USE\_TX\_POWER

Advertise with transmit power.

**Definition** bluetooth.h:916

[BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](group__bt__gap.md#ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872)

@ BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY

Low duty cycle directed advertising.

**Definition** bluetooth.h:811

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

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

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

**Definition** bluetooth.h:3035

[bt\_bond\_info::addr](structbt__bond__info.md#a6b328ce30fd53bb73ecd8e033bb91d1f)

bt\_addr\_le\_t addr

Address of the remote device.

**Definition** bluetooth.h:3037

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:531

[bt\_data::type](structbt__data.md#a984aecb40a4993ffa113be53942db065)

uint8\_t type

Type of scan response data or advertisement data.

**Definition** bluetooth.h:533

[bt\_data::data\_len](structbt__data.md#abda19091a1b8f99d385f11772ef34d5f)

uint8\_t data\_len

Length of scan response data or advertisement data.

**Definition** bluetooth.h:535

[bt\_data::data](structbt__data.md#ac80ec10101ad69a86f703a4e652c7826)

const uint8\_t \* data

Pointer to Scan response or advertisement data.

**Definition** bluetooth.h:537

[bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md)

**Definition** direction.h:118

[bt\_iso\_biginfo](structbt__iso__biginfo.md)

Broadcast Isochronous Group (BIG) information.

**Definition** iso.h:648

[bt\_le\_adv\_param](structbt__le__adv__param.md)

LE Advertising Parameters.

**Definition** bluetooth.h:990

[bt\_le\_adv\_param::options](structbt__le__adv__param.md#a2a978c60153eb03697769bc72928f4ef)

uint32\_t options

Bit-field of advertising options, see the bt\_le\_adv\_opt field.

**Definition** bluetooth.h:1024

[bt\_le\_adv\_param::peer](structbt__le__adv__param.md#a4cf31f54f067fffa3c848adc2ffd7119)

const bt\_addr\_le\_t \* peer

Directed advertising to peer.

**Definition** bluetooth.h:1065

[bt\_le\_adv\_param::sid](structbt__le__adv__param.md#a6e2f0e1b76495afe7fe661e8698d0909)

uint8\_t sid

Advertising Set Identifier, valid range is BT\_GAP\_SID\_MIN to BT\_GAP\_SID\_MAX.

**Definition** bluetooth.h:1010

[bt\_le\_adv\_param::secondary\_max\_skip](structbt__le__adv__param.md#a9911e9bfc97ff0c48a6decae3f922e95)

uint8\_t secondary\_max\_skip

Secondary channel maximum skip count.

**Definition** bluetooth.h:1021

[bt\_le\_adv\_param::interval\_min](structbt__le__adv__param.md#aca8ff5a4f5d29184535162f007b2d39e)

uint32\_t interval\_min

Minimum Advertising Interval (N \* 0.625 milliseconds).

**Definition** bluetooth.h:1036

[bt\_le\_adv\_param::id](structbt__le__adv__param.md#af957bd92b949536af2b2db0db7b2b425)

uint8\_t id

Local identity handle.

**Definition** bluetooth.h:1001

[bt\_le\_adv\_param::interval\_max](structbt__le__adv__param.md#afeba6973dca99d8ee818fdde0c22cb59)

uint32\_t interval\_max

Maximum Advertising Interval (N \* 0.625 milliseconds).

**Definition** bluetooth.h:1048

[bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md)

Callback struct to notify about advertiser activity.

**Definition** bluetooth.h:202

[bt\_le\_ext\_adv\_cb::scanned](structbt__le__ext__adv__cb.md#a277dc3269741d40b644ae3c777198fab)

void(\* scanned)(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_scanned\_info \*info)

The advertising set has sent scan response data.

**Definition** bluetooth.h:238

[bt\_le\_ext\_adv\_cb::connected](structbt__le__ext__adv__cb.md#a7aad0fbd8e531e70f661500c338d870e)

void(\* connected)(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_connected\_info \*info)

The advertising set has accepted a new connection.

**Definition** bluetooth.h:225

[bt\_le\_ext\_adv\_cb::sent](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60)

void(\* sent)(struct bt\_le\_ext\_adv \*adv, struct bt\_le\_ext\_adv\_sent\_info \*info)

The advertising set was disabled after reaching limit.

**Definition** bluetooth.h:213

[bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md)

Info of the advertising connected event.

**Definition** bluetooth.h:115

[bt\_le\_ext\_adv\_connected\_info::conn](structbt__le__ext__adv__connected__info.md#a157efa6206b418f768582107c566fde2)

struct bt\_conn \* conn

Connection object of the new connection.

**Definition** bluetooth.h:117

[bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md)

Advertising set info structure.

**Definition** bluetooth.h:1739

[bt\_le\_ext\_adv\_info::id](structbt__le__ext__adv__info.md#a06aa727cd2523914bc7509713585bffd)

uint8\_t id

Local identity handle.

**Definition** bluetooth.h:1741

[bt\_le\_ext\_adv\_info::ext\_adv\_state](structbt__le__ext__adv__info.md#a0ae2f62772732a6db460d4a0127dd17a)

enum bt\_le\_ext\_adv\_state ext\_adv\_state

Extended advertising state.

**Definition** bluetooth.h:1750

[bt\_le\_ext\_adv\_info::addr](structbt__le__ext__adv__info.md#a0dd0aa8a26fe1ef5813fa07732c5c4c9)

const bt\_addr\_le\_t \* addr

Current local advertising address used.

**Definition** bluetooth.h:1747

[bt\_le\_ext\_adv\_info::tx\_power](structbt__le__ext__adv__info.md#a485e4a8124fddee897fe744836cbfb24)

int8\_t tx\_power

Currently selected Transmit Power (dBM).

**Definition** bluetooth.h:1744

[bt\_le\_ext\_adv\_info::per\_adv\_state](structbt__le__ext__adv__info.md#ad802b5af32353d757a84e5039c973f3a)

enum bt\_le\_per\_adv\_state per\_adv\_state

Periodic advertising state.

**Definition** bluetooth.h:1753

[bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md)

Info of the advertising scanned event.

**Definition** bluetooth.h:125

[bt\_le\_ext\_adv\_scanned\_info::addr](structbt__le__ext__adv__scanned__info.md#a4431f157891d2c1a7d0e40f7e879ac3d)

bt\_addr\_le\_t \* addr

Active scanner LE address and type.

**Definition** bluetooth.h:127

[bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md)

Info of the advertising sent event.

**Definition** bluetooth.h:100

[bt\_le\_ext\_adv\_sent\_info::num\_sent](structbt__le__ext__adv__sent__info.md#a80f661efd35b069c2f8700851e9429a2)

uint8\_t num\_sent

If the advertising set was started with a non-zero bt\_le\_ext\_adv\_start\_param::num\_events,...

**Definition** bluetooth.h:107

[bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md)

Parameters for starting an extended advertising session.

**Definition** bluetooth.h:1557

[bt\_le\_ext\_adv\_start\_param::timeout](structbt__le__ext__adv__start__param.md#a80bb1ef4316dd75ea1268241333f4346)

uint16\_t timeout

Maximum advertising set duration (N \* 10 ms).

**Definition** bluetooth.h:1582

[bt\_le\_ext\_adv\_start\_param::num\_events](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f)

uint8\_t num\_events

Maximum number of extended advertising events to be sent.

**Definition** bluetooth.h:1602

[bt\_le\_local\_features](structbt__le__local__features.md)

Local Bluetooth LE controller features and capabilities.

**Definition** bluetooth.h:610

[bt\_le\_local\_features::acl\_pkts](structbt__le__local__features.md#a19cecbe8574229844e9416842bc42b0c)

uint8\_t acl\_pkts

Total number of ACL data packets.

**Definition** bluetooth.h:638

[bt\_le\_local\_features::acl\_mtu](structbt__le__local__features.md#a22ce370b338f687ce6860435cc0ec9c5)

uint16\_t acl\_mtu

ACL data packet length.

**Definition** bluetooth.h:636

[bt\_le\_local\_features::features](structbt__le__local__features.md#a76b8cc9bd4ab099cb94ebe997d991f68)

uint8\_t features[8]

Local LE controller supported features.

**Definition** bluetooth.h:618

[bt\_le\_local\_features::iso\_pkts](structbt__le__local__features.md#a8b413bf80ccd7e3af67f7e1c28a1beeb)

uint8\_t iso\_pkts

Total number of ISO data packets.

**Definition** bluetooth.h:650

[bt\_le\_local\_features::max\_adv\_data\_len](structbt__le__local__features.md#a932af365332149ec620413a8504d342c)

uint16\_t max\_adv\_data\_len

Maximum advertising data length.

**Definition** bluetooth.h:666

[bt\_le\_local\_features::states](structbt__le__local__features.md#aa2dc6363feab37af195ee192f2b906f1)

uint64\_t states

Local LE controller supported states.

**Definition** bluetooth.h:626

[bt\_le\_local\_features::rl\_size](structbt__le__local__features.md#ac86ae6974627ddb2e34b0d028cdcfe32)

uint8\_t rl\_size

Maximum size of the controller resolving list.

**Definition** bluetooth.h:657

[bt\_le\_local\_features::iso\_mtu](structbt__le__local__features.md#ad7b95feb82c1dece8bb8bb7969efa2ec)

uint16\_t iso\_mtu

ISO data packet length.

**Definition** bluetooth.h:648

[bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md)

LE Secure Connections pairing Out of Band data.

**Definition** bluetooth.h:2945

[bt\_le\_oob\_sc\_data::c](structbt__le__oob__sc__data.md#a9bd93f1e9e41e241d0f84ae16ae47ba1)

uint8\_t c[16]

Confirm Value.

**Definition** bluetooth.h:2950

[bt\_le\_oob\_sc\_data::r](structbt__le__oob__sc__data.md#afa64bcc048d0e8709e262e2848a39d2c)

uint8\_t r[16]

Random Number.

**Definition** bluetooth.h:2947

[bt\_le\_oob](structbt__le__oob.md)

LE Out of Band information.

**Definition** bluetooth.h:2954

[bt\_le\_oob::addr](structbt__le__oob.md#a17cfed7683efbf5b5954847d655d7424)

bt\_addr\_le\_t addr

LE address.

**Definition** bluetooth.h:2958

[bt\_le\_oob::le\_sc\_data](structbt__le__oob.md#a80ccd4ab120a880adfff9aba3b19b4fd)

struct bt\_le\_oob\_sc\_data le\_sc\_data

LE Secure Connections pairing Out of Band data.

**Definition** bluetooth.h:2961

[bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md)

Info of the PAwR subevents.

**Definition** bluetooth.h:139

[bt\_le\_per\_adv\_data\_request::count](structbt__le__per__adv__data__request.md#a766991899bc3e689adec36bf1f12e802)

uint8\_t count

The number of subevents data can be set for.

**Definition** bluetooth.h:144

[bt\_le\_per\_adv\_data\_request::start](structbt__le__per__adv__data__request.md#a779ed161919c3117f6ce165deb0a9b0a)

uint8\_t start

The first subevent data can be set for.

**Definition** bluetooth.h:141

[bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md)

Parameters for configuring periodic advertising.

**Definition** bluetooth.h:1104

[bt\_le\_per\_adv\_param::interval\_min](structbt__le__per__adv__param.md#a49da44a3c0e4e866ffccffae5a9a22f7)

uint16\_t interval\_min

Minimum Periodic Advertising Interval (N \* 1.25 ms).

**Definition** bluetooth.h:1111

[bt\_le\_per\_adv\_param::interval\_max](structbt__le__per__adv__param.md#a61308cfe72ad23372dfd2a3bd2550726)

uint16\_t interval\_max

Maximum Periodic Advertising Interval (N \* 1.25 ms).

**Definition** bluetooth.h:1119

[bt\_le\_per\_adv\_param::options](structbt__le__per__adv__param.md#a9b80c2427171920f466601e7e8468814)

uint32\_t options

Bit-field of periodic advertising options, see the bt\_le\_adv\_opt field.

**Definition** bluetooth.h:1122

[bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md)

Info about the PAwR responses received.

**Definition** bluetooth.h:157

[bt\_le\_per\_adv\_response\_info::subevent](structbt__le__per__adv__response__info.md#a1b87ab77f5c7d4ee0c1c612bcfb424d5)

uint8\_t subevent

The subevent the response was received in.

**Definition** bluetooth.h:159

[bt\_le\_per\_adv\_response\_info::rssi](structbt__le__per__adv__response__info.md#a2db58fb452a07290ab4a50892c682837)

int8\_t rssi

The RSSI of the response in dBm.

**Definition** bluetooth.h:173

[bt\_le\_per\_adv\_response\_info::cte\_type](structbt__le__per__adv__response__info.md#a52b0c612b09cfcb3eb2ea475614c34b8)

uint8\_t cte\_type

The Constant Tone Extension (CTE) of the advertisement (bt\_df\_cte\_type).

**Definition** bluetooth.h:176

[bt\_le\_per\_adv\_response\_info::tx\_power](structbt__le__per__adv__response__info.md#a7ed20f695e0d696eaab7cddc4e3c11fb)

int8\_t tx\_power

The TX power of the response in dBm.

**Definition** bluetooth.h:170

[bt\_le\_per\_adv\_response\_info::response\_slot](structbt__le__per__adv__response__info.md#a83cc642c9f22c767421644e7d8233001)

uint8\_t response\_slot

The slot the response was received in.

**Definition** bluetooth.h:179

[bt\_le\_per\_adv\_response\_info::tx\_status](structbt__le__per__adv__response__info.md#ab17f33cb713d258bf6c863a64e5aba07)

uint8\_t tx\_status

Status of the subevent indication.

**Definition** bluetooth.h:167

[bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md)

Parameters for sending a periodic advertising response.

**Definition** bluetooth.h:3119

[bt\_le\_per\_adv\_response\_params::response\_subevent](structbt__le__per__adv__response__params.md#a0cec222d5ba8cc9e20939d441646c913)

uint8\_t response\_subevent

The subevent the response shall be sent in.

**Definition** bluetooth.h:3140

[bt\_le\_per\_adv\_response\_params::request\_event](structbt__le__per__adv__response__params.md#a1af01d0a027fb8659615874acbd388f9)

uint16\_t request\_event

The periodic event counter of the request the response is sent to.

**Definition** bluetooth.h:3129

[bt\_le\_per\_adv\_response\_params::request\_subevent](structbt__le__per__adv__response__params.md#a3fc8ab0feb06714b28d22439cce60e41)

uint8\_t request\_subevent

The subevent counter of the request the response is sent to.

**Definition** bluetooth.h:3137

[bt\_le\_per\_adv\_response\_params::response\_slot](structbt__le__per__adv__response__params.md#aea0428083ccd5f4dccc17e494f38b7c3)

uint8\_t response\_slot

The response slot the response shall be sent in.

**Definition** bluetooth.h:3143

[bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md)

Parameters for setting data for a specific periodic advertising with response subevent.

**Definition** bluetooth.h:1827

[bt\_le\_per\_adv\_subevent\_data\_params::response\_slot\_start](structbt__le__per__adv__subevent__data__params.md#a1354e9505239de3c42969138d719d775)

uint8\_t response\_slot\_start

The first response slot to listen to.

**Definition** bluetooth.h:1832

[bt\_le\_per\_adv\_subevent\_data\_params::data](structbt__le__per__adv__subevent__data__params.md#a46103c988d8ac360b7e26310a0322b4e)

const struct net\_buf\_simple \* data

The data to send.

**Definition** bluetooth.h:1838

[bt\_le\_per\_adv\_subevent\_data\_params::subevent](structbt__le__per__adv__subevent__data__params.md#a55f2da6041b538b3bc4bff38cd4d2953)

uint8\_t subevent

The subevent to set data for.

**Definition** bluetooth.h:1829

[bt\_le\_per\_adv\_subevent\_data\_params::response\_slot\_count](structbt__le__per__adv__subevent__data__params.md#a86d858606943a82917835a0172e88663)

uint8\_t response\_slot\_count

The number of response slots to listen to.

**Definition** bluetooth.h:1835

[bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md)

Callback struct for periodic advertising sync events.

**Definition** bluetooth.h:2028

[bt\_le\_per\_adv\_sync\_cb::node](structbt__le__per__adv__sync__cb.md#a1977d27941063773c953a5f1dfa9ca76)

sys\_snode\_t node

**Definition** bluetooth.h:2107

[bt\_le\_per\_adv\_sync\_cb::recv](structbt__le__per__adv__sync__cb.md#a5576248e2eaef2afebe606e05e55f05f)

void(\* recv)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_le\_per\_adv\_sync\_recv\_info \*info, struct net\_buf\_simple \*buf)

Periodic advertising data received.

**Definition** bluetooth.h:2068

[bt\_le\_per\_adv\_sync\_cb::state\_changed](structbt__le__per__adv__sync__cb.md#a656b4802f79d4a472c2367ade144d72e)

void(\* state\_changed)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_le\_per\_adv\_sync\_state\_info \*info)

The periodic advertising sync state has changed.

**Definition** bluetooth.h:2082

[bt\_le\_per\_adv\_sync\_cb::synced](structbt__le__per__adv__sync__cb.md#a815be4343ab589df433a551663c5f4a1)

void(\* synced)(struct bt\_le\_per\_adv\_sync \*sync, struct bt\_le\_per\_adv\_sync\_synced\_info \*info)

The periodic advertising has been successfully synced.

**Definition** bluetooth.h:2039

[bt\_le\_per\_adv\_sync\_cb::biginfo](structbt__le__per__adv__sync__cb.md#aa44efa17bc28da1952785063a9baf6a9)

void(\* biginfo)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_iso\_biginfo \*biginfo)

BIGInfo advertising report received.

**Definition** bluetooth.h:2095

[bt\_le\_per\_adv\_sync\_cb::term](structbt__le__per__adv__sync__cb.md#acbd565a39918e5dfe7603a020e73daec)

void(\* term)(struct bt\_le\_per\_adv\_sync \*sync, const struct bt\_le\_per\_adv\_sync\_term\_info \*info)

The periodic advertising sync has been terminated.

**Definition** bluetooth.h:2052

[bt\_le\_per\_adv\_sync\_cb::cte\_report\_cb](structbt__le__per__adv__sync__cb.md#ad2dc168696fbd22f7e3a089ac56f62d7)

void(\* cte\_report\_cb)(struct bt\_le\_per\_adv\_sync \*sync, struct bt\_df\_per\_adv\_sync\_iq\_samples\_report const \*info)

Callback for IQ samples report collected when sampling CTE received with periodic advertising PDU.

**Definition** bluetooth.h:2104

[bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md)

Periodic advertising set info structure.

**Definition** bluetooth.h:2224

[bt\_le\_per\_adv\_sync\_info::interval](structbt__le__per__adv__sync__info.md#a365a0d8577429e4ee96e977071c9a906)

uint16\_t interval

Periodic advertising interval (N \* 1.25 ms).

**Definition** bluetooth.h:2232

[bt\_le\_per\_adv\_sync\_info::phy](structbt__le__per__adv__sync__info.md#a4d9520ea6a803f8fe4f41190f55c26e5)

uint8\_t phy

Advertiser PHY (see bt\_gap\_le\_phy).

**Definition** bluetooth.h:2235

[bt\_le\_per\_adv\_sync\_info::addr](structbt__le__per__adv__sync__info.md#ac10fc2e2d3ec2160db8c2aac148d18a2)

bt\_addr\_le\_t addr

Periodic Advertiser Address.

**Definition** bluetooth.h:2226

[bt\_le\_per\_adv\_sync\_info::sid](structbt__le__per__adv__sync__info.md#acc0ef26c38279c9a67f8992005c2e58a)

uint8\_t sid

Advertising Set Identifier, valid range BT\_GAP\_SID\_MIN to BT\_GAP\_SID\_MAX.

**Definition** bluetooth.h:2229

[bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md)

Parameters for creating a periodic advertising sync object.

**Definition** bluetooth.h:2157

[bt\_le\_per\_adv\_sync\_param::timeout](structbt__le__per__adv__sync__param.md#a301cfd3d6e5620d29c021ababe104754)

uint16\_t timeout

Synchronization timeout (N \* 10 ms).

**Definition** bluetooth.h:2193

[bt\_le\_per\_adv\_sync\_param::options](structbt__le__per__adv__sync__param.md#a4252f2b3b453c2f9c8fbf8c35a618ff2)

uint32\_t options

Bit-field of periodic advertising sync options, see the bt\_le\_adv\_opt field.

**Definition** bluetooth.h:2176

[bt\_le\_per\_adv\_sync\_param::sid](structbt__le__per__adv__sync__param.md#a70795642ee94dd9e87f0cf251c095e7f)

uint8\_t sid

Advertising Set Identifier.

**Definition** bluetooth.h:2173

[bt\_le\_per\_adv\_sync\_param::addr](structbt__le__per__adv__sync__param.md#ac93adedad747f61a771ac5445e486b74)

bt\_addr\_le\_t addr

Periodic Advertiser Address.

**Definition** bluetooth.h:2164

[bt\_le\_per\_adv\_sync\_param::skip](structbt__le__per__adv__sync__param.md#af9abb65547fb5bfea65f4c22963c7da0)

uint16\_t skip

Maximum event skip.

**Definition** bluetooth.h:2185

[bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md)

Information about a received periodic advertising report.

**Definition** bluetooth.h:1981

[bt\_le\_per\_adv\_sync\_recv\_info::cte\_type](structbt__le__per__adv__sync__recv__info.md#a1591907e3cb1f4565b9d26c18bccc7d2)

uint8\_t cte\_type

The Constant Tone Extension (CTE) of the advertisement (bt\_df\_cte\_type).

**Definition** bluetooth.h:1995

[bt\_le\_per\_adv\_sync\_recv\_info::sid](structbt__le__per__adv__sync__recv__info.md#a21b0ca87e46c6897282ebd877e45114e)

uint8\_t sid

Advertising Set Identifier, valid range BT\_GAP\_SID\_MIN to BT\_GAP\_SID\_MAX.

**Definition** bluetooth.h:1986

[bt\_le\_per\_adv\_sync\_recv\_info::addr](structbt__le__per__adv__sync__recv__info.md#a5817bd4fba2c93adebcebe007650b6eb)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:1983

[bt\_le\_per\_adv\_sync\_recv\_info::tx\_power](structbt__le__per__adv__sync__recv__info.md#a65f1a2adb7c3d740cb8262ae7f5a7c3e)

int8\_t tx\_power

The TX power of the advertisement.

**Definition** bluetooth.h:1989

[bt\_le\_per\_adv\_sync\_recv\_info::rssi](structbt__le__per__adv__sync__recv__info.md#aa17c9d917469f121448ed4e1db485700)

int8\_t rssi

The RSSI of the advertisement excluding any CTE.

**Definition** bluetooth.h:1992

[bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md)

Information about the state of periodic advertising sync.

**Definition** bluetooth.h:2012

[bt\_le\_per\_adv\_sync\_state\_info::recv\_enabled](structbt__le__per__adv__sync__state__info.md#a4b0a3b7e36f935e06072304d6b92579f)

bool recv\_enabled

True if receiving periodic advertisements, false otherwise.

**Definition** bluetooth.h:2014

[bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md)

Parameters for synchronizing with specific periodic advertising subevents.

**Definition** bluetooth.h:3079

[bt\_le\_per\_adv\_sync\_subevent\_params::subevents](structbt__le__per__adv__sync__subevent__params.md#a5ac4e81ddd63797f921105748344c125)

uint8\_t \* subevents

The subevent(s) to synchronize with.

**Definition** bluetooth.h:3095

[bt\_le\_per\_adv\_sync\_subevent\_params::properties](structbt__le__per__adv__sync__subevent__params.md#a6b23cd4b7e6a3f1d65b9a7eff85bcfb4)

uint16\_t properties

Periodic Advertising Properties.

**Definition** bluetooth.h:3085

[bt\_le\_per\_adv\_sync\_subevent\_params::num\_subevents](structbt__le__per__adv__sync__subevent__params.md#a867c66bf09461a4369da3d250701d2ae)

uint8\_t num\_subevents

Number of subevents to sync to.

**Definition** bluetooth.h:3088

[bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md)

Information about the successful synchronization with periodic advertising.

**Definition** bluetooth.h:1903

[bt\_le\_per\_adv\_sync\_synced\_info::recv\_enabled](structbt__le__per__adv__sync__synced__info.md#a0dd4b7646da0fadc48e94ff3dc91ef83)

bool recv\_enabled

True if receiving periodic advertisements, false otherwise.

**Definition** bluetooth.h:1917

[bt\_le\_per\_adv\_sync\_synced\_info::interval](structbt__le__per__adv__sync__synced__info.md#a5304e1826face35c506f3b8f6cad7df2)

uint16\_t interval

Periodic advertising interval (N \* 1.25 ms).

**Definition** bluetooth.h:1911

[bt\_le\_per\_adv\_sync\_synced\_info::sid](structbt__le__per__adv__sync__synced__info.md#a5489c3038f7fff596316a456fc8d580b)

uint8\_t sid

Advertising Set Identifier, valid range BT\_GAP\_SID\_MIN to BT\_GAP\_SID\_MAX.

**Definition** bluetooth.h:1908

[bt\_le\_per\_adv\_sync\_synced\_info::addr](structbt__le__per__adv__sync__synced__info.md#a7ca99b0596b08d153d3ba5310adab125)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:1905

[bt\_le\_per\_adv\_sync\_synced\_info::phy](structbt__le__per__adv__sync__synced__info.md#a8b7709011541e95ceaeac379cc3143bb)

uint8\_t phy

Advertiser PHY (see bt\_gap\_le\_phy).

**Definition** bluetooth.h:1914

[bt\_le\_per\_adv\_sync\_synced\_info::conn](structbt__le__per__adv__sync__synced__info.md#ada4cda53aa87f29d54f6cd88134efe14)

struct bt\_conn \* conn

Peer that transferred the periodic advertising sync.

**Definition** bluetooth.h:1932

[bt\_le\_per\_adv\_sync\_synced\_info::service\_data](structbt__le__per__adv__sync__synced__info.md#adee2bdafa86a0c3c1dfb4660e85396a3)

uint16\_t service\_data

Service Data provided by the peer when sync is transferred.

**Definition** bluetooth.h:1924

[bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md)

Information about the termination of a periodic advertising sync.

**Definition** bluetooth.h:1959

[bt\_le\_per\_adv\_sync\_term\_info::addr](structbt__le__per__adv__sync__term__info.md#a2b76ccd5e4c9933f2c05db2ec5b8e2fc)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:1961

[bt\_le\_per\_adv\_sync\_term\_info::reason](structbt__le__per__adv__sync__term__info.md#a429b8b665eacbfe9db013a571b829bac)

uint8\_t reason

Cause of periodic advertising termination (see the BT\_HCI\_ERR\_\* values).

**Definition** bluetooth.h:1967

[bt\_le\_per\_adv\_sync\_term\_info::sid](structbt__le__per__adv__sync__term__info.md#a7a5f2ecccaf698bad86f10d9a7d16189)

uint8\_t sid

Advertising Set Identifier, valid range BT\_GAP\_SID\_MIN to BT\_GAP\_SID\_MAX.

**Definition** bluetooth.h:1964

[bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md)

Parameters for periodic advertising sync transfer.

**Definition** bluetooth.h:2393

[bt\_le\_per\_adv\_sync\_transfer\_param::options](structbt__le__per__adv__sync__transfer__param.md#a0b3ee6df1b409e64a064ffb6ac632cce)

uint32\_t options

Periodic Advertising Sync Transfer options, see bt\_le\_per\_adv\_sync\_transfer\_opt.

**Definition** bluetooth.h:2411

[bt\_le\_per\_adv\_sync\_transfer\_param::timeout](structbt__le__per__adv__sync__transfer__param.md#a5bfa84c6bdacdf8893a0951a5ce71fc6)

uint16\_t timeout

Synchronization timeout (N \* 10 ms).

**Definition** bluetooth.h:2408

[bt\_le\_per\_adv\_sync\_transfer\_param::skip](structbt__le__per__adv__sync__transfer__param.md#a840e7cfac3a2947e5128d704067aaf7e)

uint16\_t skip

Maximum event skip.

**Definition** bluetooth.h:2400

[bt\_le\_scan\_cb](structbt__le__scan__cb.md)

Listener context for (LE) scanning.

**Definition** bluetooth.h:2657

[bt\_le\_scan\_cb::timeout](structbt__le__scan__cb.md#a2f57f3fee46bd137065f4c57d0cd5157)

void(\* timeout)(void)

The scanner has stopped scanning after scan timeout.

**Definition** bluetooth.h:2669

[bt\_le\_scan\_cb::node](structbt__le__scan__cb.md#a50dbc5e7618fd488e9acb7ad8f104a63)

sys\_snode\_t node

**Definition** bluetooth.h:2671

[bt\_le\_scan\_cb::recv](structbt__le__scan__cb.md#a71d73c1da28d4a27626f77d96a5b3541)

void(\* recv)(const struct bt\_le\_scan\_recv\_info \*info, struct net\_buf\_simple \*buf)

Advertisement packet and scan response received callback.

**Definition** bluetooth.h:2665

[bt\_le\_scan\_param](structbt__le__scan__param.md)

LE scan parameters.

**Definition** bluetooth.h:2553

[bt\_le\_scan\_param::type](structbt__le__scan__param.md#a02d75322390287c3fa754bf915660d0c)

uint8\_t type

Scan type.

**Definition** bluetooth.h:2555

[bt\_le\_scan\_param::interval](structbt__le__scan__param.md#a2f4e053d97c62b6fdf42a245908607f8)

uint16\_t interval

Scan interval (N \* 0.625 ms).

**Definition** bluetooth.h:2568

[bt\_le\_scan\_param::window](structbt__le__scan__param.md#a37a7ee82e86a91cf7a9c2adf60bb526a)

uint16\_t window

Scan window (N \* 0.625 ms).

**Definition** bluetooth.h:2578

[bt\_le\_scan\_param::timeout](structbt__le__scan__param.md#a3e71ce551dcc7762c29e2316996e2912)

uint16\_t timeout

Scan timeout (N \* 10 ms).

**Definition** bluetooth.h:2586

[bt\_le\_scan\_param::interval\_coded](structbt__le__scan__param.md#a67a20bc94a3d98fa10af7b5b42dde328)

uint16\_t interval\_coded

Scan interval LE Coded PHY (N \* 0.625 MS).

**Definition** bluetooth.h:2593

[bt\_le\_scan\_param::window\_coded](structbt__le__scan__param.md#a93166af55dca71393c60cb3f7ac6d809)

uint16\_t window\_coded

Scan window LE Coded PHY (N \* 0.625 MS).

**Definition** bluetooth.h:2600

[bt\_le\_scan\_param::options](structbt__le__scan__param.md#ac815b05fee8ce0dd24228305b7596207)

uint8\_t options

Bit-field of scanning options.

**Definition** bluetooth.h:2558

[bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md)

LE advertisement and scan response packet information.

**Definition** bluetooth.h:2604

[bt\_le\_scan\_recv\_info::interval](structbt__le__scan__recv__info.md#a1060c5937708ff81a64f068e02fc7826)

uint16\_t interval

Periodic advertising interval (N \* 1.25 ms).

**Definition** bluetooth.h:2647

[bt\_le\_scan\_recv\_info::tx\_power](structbt__le__scan__recv__info.md#a2addeba6d2ec8e55dc5379adf6519148)

int8\_t tx\_power

Transmit power of the advertiser.

**Definition** bluetooth.h:2620

[bt\_le\_scan\_recv\_info::sid](structbt__le__scan__recv__info.md#a4df8d4e1fdd7514d170744856ebe7015)

uint8\_t sid

Advertising Set Identifier, valid range BT\_GAP\_SID\_MIN to BT\_GAP\_SID\_MAX.

**Definition** bluetooth.h:2614

[bt\_le\_scan\_recv\_info::primary\_phy](structbt__le__scan__recv__info.md#a6189ed8453cb7907f34dc7dfaf1343bd)

uint8\_t primary\_phy

Primary advertising channel PHY.

**Definition** bluetooth.h:2650

[bt\_le\_scan\_recv\_info::rssi](structbt__le__scan__recv__info.md#a88f677733147245ccbf861c7fc5e0f11)

int8\_t rssi

Strength of advertiser signal.

**Definition** bluetooth.h:2617

[bt\_le\_scan\_recv\_info::addr](structbt__le__scan__recv__info.md#a907fb7ec3c78d68da5015a8c3afc3084)

const bt\_addr\_le\_t \* addr

Advertiser LE address and type.

**Definition** bluetooth.h:2611

[bt\_le\_scan\_recv\_info::secondary\_phy](structbt__le__scan__recv__info.md#ac797291291dc7ba7ac171ed7f24f0d16)

uint8\_t secondary\_phy

Secondary advertising channel PHY.

**Definition** bluetooth.h:2653

[bt\_le\_scan\_recv\_info::adv\_type](structbt__le__scan__recv__info.md#adccb2ce5c6d228bd7f8f050088629524)

uint8\_t adv\_type

Advertising packet type.

**Definition** bluetooth.h:2630

[bt\_le\_scan\_recv\_info::adv\_props](structbt__le__scan__recv__info.md#af29ddfb59e286af9ca465cbd5a91bf2d)

uint16\_t adv\_props

Advertising packet properties bitfield.

**Definition** bluetooth.h:2640

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[net\_buf\_simple::data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** net\_buf.h:91

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [bluetooth.h](bluetooth_2bluetooth_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
