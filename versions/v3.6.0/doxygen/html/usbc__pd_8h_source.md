---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbc__pd_8h_source.html
original_path: doxygen/html/usbc__pd_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_pd.h

[Go to the documentation of this file.](usbc__pd_8h.md)

1/\*

2 \* Copyright 2022 The Chromium OS Authors

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

13

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_PD\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_PD\_H\_

16

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 35](group__usb__power__delivery.md#ga998b67d43674778e42f6c49ec6a99af4)#define PD\_MAX\_EXTENDED\_MSG\_LEGACY\_LEN 26

36

[ 42](group__usb__power__delivery.md#gabdb041542baaf2277e054dd9e3928b16)#define PD\_MAX\_EXTENDED\_MSG\_LEN 260

43

[ 54](group__usb__power__delivery.md#gac0588f94c1792b5b8fefa6a60c1b237b)#define PD\_MAX\_EXTENDED\_MSG\_CHUNK\_LEN 26

55

60

[ 67](group__usb__power__delivery.md#gac517b081df0572803efb374839846f1f)#define PD\_N\_CAPS\_COUNT 50

68

[ 74](group__usb__power__delivery.md#gae4f479f2e77066a9b870263e3580f03f)#define PD\_N\_HARD\_RESET\_COUNT 2

75

77

82

[ 88](group__usb__power__delivery.md#ga9dfd6527539e996ccc110036545e61e7)#define PD\_T\_NO\_RESPONSE\_MIN\_MS 4500

89

[ 95](group__usb__power__delivery.md#gaed69627505bdad8fb87c37084e2222e1)#define PD\_T\_NO\_RESPONSE\_MAX\_MS 5500

96

[ 103](group__usb__power__delivery.md#ga87d0eb341d76c01b4b355c1d5a0354a1)#define PD\_T\_PS\_HARD\_RESET\_MIN\_MS 25

104

[ 111](group__usb__power__delivery.md#ga2c4abfef3a581e19677d8f0d845a3582)#define PD\_T\_PS\_HARD\_RESET\_MAX\_MS 35

112

[ 118](group__usb__power__delivery.md#gae7db10623f2ec064ef0351bb1bba51cd)#define PD\_T\_SINK\_TX\_MIN\_MS 16

119

[ 125](group__usb__power__delivery.md#gadb55b3f260a17458bf479a7273fd946c)#define PD\_T\_SINK\_TX\_MAX\_MS 20

126

[ 134](group__usb__power__delivery.md#gabe6d36578671578eddf1381f58bcc80a)#define PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MIN\_MS 100

135

[ 143](group__usb__power__delivery.md#ga105a9791e086ade590b6fd825fe5cded)#define PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MAX\_MS 200

144

146

[ 153](group__usb__power__delivery.md#ga266725d0496981ee92b0008afe43505e)#define PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MIN\_MS 310

154

[ 161](group__usb__power__delivery.md#gae32afec56f34841200188e64dc1ab9ca)#define PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MAX\_MS 620

162

[ 168](group__usb__power__delivery.md#gac3a939394dab5a5038801f9a6b2dcd30)#define PD\_V\_SAFE\_0V\_MAX\_MV 800

169

[ 175](group__usb__power__delivery.md#gad4f0e12b7f0e2ccd6aee73cf1525b27c)#define PD\_V\_SAFE\_5V\_MIN\_MV 4750

176

[ 182](group__usb__power__delivery.md#gad5667f26343d4601c9fd5c5e9d046802)#define PD\_T\_SAFE\_0V\_MAX\_MS 650

183

[ 189](group__usb__power__delivery.md#ga123abee7651bca30a3e6ec2956eb0563)#define PD\_T\_SAFE\_5V\_MAX\_MS 275

190

[ 194](group__usb__power__delivery.md#gab6c168d490983a136c184bbe3ed9e7c5)#define PD\_T\_TX\_TIMEOUT\_MS 100

195

[ 200](group__usb__power__delivery.md#ga64b8c095dba137d7fe460ffe38f00ce5)#define PD\_T\_HARD\_RESET\_COMPLETE\_MIN\_MS 4

201

[ 206](group__usb__power__delivery.md#ga2748e0775b50552cc7d26cb2b2d3103d)#define PD\_T\_HARD\_RESET\_COMPLETE\_MAX\_MS 5

207

[ 212](group__usb__power__delivery.md#ga9722df85c1a842ff1661e534e88d472e)#define PD\_T\_SENDER\_RESPONSE\_MIN\_MS 24

213

[ 218](group__usb__power__delivery.md#gac905bf64de8a9f5acef6f8731c11d041)#define PD\_T\_SENDER\_RESPONSE\_NOM\_MS 27

219

[ 224](group__usb__power__delivery.md#ga4b7c238e12770841b1852a0517b12071)#define PD\_T\_SENDER\_RESPONSE\_MAX\_MS 30

225

[ 230](group__usb__power__delivery.md#ga4726113aa8c0100fa1a88435d3a6b1d1)#define PD\_T\_SPR\_PS\_TRANSITION\_MIN\_MS 450

231

[ 236](group__usb__power__delivery.md#ga01a2a71da7fdbe18d07dacb687f7d295)#define PD\_T\_SPR\_PS\_TRANSITION\_NOM\_MS 500

237

[ 242](group__usb__power__delivery.md#ga7dac8d411d8f4651b177a6495146acb0)#define PD\_T\_SPR\_PS\_TRANSITION\_MAX\_MS 550

243

[ 248](group__usb__power__delivery.md#ga7f9a916a88c626b76963a4950878fa20)#define PD\_T\_EPR\_PS\_TRANSITION\_MIN\_MS 830

249

[ 254](group__usb__power__delivery.md#gabcd0576899a6ce1a147bffbb0c1b517f)#define PD\_T\_EPR\_PS\_TRANSITION\_NOM\_MS 925

255

[ 260](group__usb__power__delivery.md#gaaea48ba7ea96b304b18293c202325b0e)#define PD\_T\_EPR\_PS\_TRANSITION\_MAX\_MS 1020

261

[ 266](group__usb__power__delivery.md#ga4416cfc999de1ee2ed49ce89f54074b1)#define PD\_T\_SINK\_REQUEST\_MIN\_MS 100

267

[ 273](group__usb__power__delivery.md#ga890ce7af4632f8a17b399f0821aee3cf)#define PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MIN\_MS 40

274

[ 280](group__usb__power__delivery.md#gad13130dbd7f6ed4276b1781c5bf2fb20)#define PD\_T\_CHUNKING\_NOT\_SUPPORTED\_NOM\_MS 45

281

[ 287](group__usb__power__delivery.md#gaf28df42c00394f9d11dfade2cae910d4)#define PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MAX\_MS 50

288

[ 295](group__usb__power__delivery.md#ga953bdd1d4893bebcaeb6b4b95667fd94)#define PD\_CONVERT\_BYTES\_TO\_PD\_HEADER\_COUNT(c) ((c) >> 2)

296

[ 302](group__usb__power__delivery.md#gad5c5b108e4b255633a52d0de48adaf71)#define PD\_CONVERT\_PD\_HEADER\_COUNT\_TO\_BYTES(c) ((c) << 2)

303

[ 308](group__usb__power__delivery.md#ga69f749b5c7ecf6368002aae12277ac9f)#define SINK\_TX\_OK TC\_RP\_3A0

309

[ 314](group__usb__power__delivery.md#gaa3ca6814e56859792dd5524fe8cef6b1)#define SINK\_TX\_NG TC\_RP\_1A5

315

[ 320](unionpd__header.md)union [pd\_header](unionpd__header.md) {

321 struct {

[ 323](unionpd__header.md#a70768acc6a6bc9ebb9249df7ed635a94) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_type](unionpd__header.md#a70768acc6a6bc9ebb9249df7ed635a94) : 5;

[ 325](unionpd__header.md#af1b027c9c57497421117b290dcb6ac66) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [port\_data\_role](unionpd__header.md#af1b027c9c57497421117b290dcb6ac66) : 1;

[ 327](unionpd__header.md#a85cce1728afe0d62bb29f618a1cf70e1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [specification\_revision](unionpd__header.md#a85cce1728afe0d62bb29f618a1cf70e1) : 2;

[ 329](unionpd__header.md#a20ac99d9738c9d278a78e8ccfc401902) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [port\_power\_role](unionpd__header.md#a20ac99d9738c9d278a78e8ccfc401902) : 1;

[ 331](unionpd__header.md#ae4a0a5695e73fd3e1b7e3f38cd2a758c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_id](unionpd__header.md#ae4a0a5695e73fd3e1b7e3f38cd2a758c) : 3;

[ 333](unionpd__header.md#a63d89119f0918ba7d6eb9e01fa1ed406) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [number\_of\_data\_objects](unionpd__header.md#a63d89119f0918ba7d6eb9e01fa1ed406) : 3;

[ 335](unionpd__header.md#a5750b964c12c3bc2d2523a64cb9eb7d0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [extended](unionpd__header.md#a5750b964c12c3bc2d2523a64cb9eb7d0) : 1;

336 };

[ 337](unionpd__header.md#afa6c6699be5fe95bcb4962396e33e35d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [raw\_value](unionpd__header.md#afa6c6699be5fe95bcb4962396e33e35d);

338};

339

[ 345](group__usb__power__delivery.md#gaf3acdb691327adef04e418d7ded3d883)#define PD\_GET\_EXT\_HEADER(c) ((c) & 0xffff)

346

[ 351](unionpd__ext__header.md)union [pd\_ext\_header](unionpd__ext__header.md) {

352 struct {

[ 354](unionpd__ext__header.md#a4a7a948d3463ddfbebf1d75faeda293e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data\_size](unionpd__ext__header.md#a4a7a948d3463ddfbebf1d75faeda293e) : 9;

[ 356](unionpd__ext__header.md#aae09d0399c0a121e3c216047e908b9ec) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved0](unionpd__ext__header.md#aae09d0399c0a121e3c216047e908b9ec) : 1;

[ 358](unionpd__ext__header.md#a36a65a1e52875721758d1273b0e76279) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [request\_chunk](unionpd__ext__header.md#a36a65a1e52875721758d1273b0e76279) : 1;

[ 360](unionpd__ext__header.md#aced0489c4e2462652c0d91187c07b27e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chunk\_number](unionpd__ext__header.md#aced0489c4e2462652c0d91187c07b27e) : 4;

[ 362](unionpd__ext__header.md#a180ccc6854c1341e638ca338e6eb1cd8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chunked](unionpd__ext__header.md#a180ccc6854c1341e638ca338e6eb1cd8) : 1;

363 };

[ 365](unionpd__ext__header.md#a8a1d0f0d38b3a5c4aa3a80586e7a1e8f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [raw\_value](unionpd__ext__header.md#a8a1d0f0d38b3a5c4aa3a80586e7a1e8f);

366};

367

372

[ 376](group__usb__power__delivery.md#gab1716bb587e2b162415ea21e3c8d4e74)#define PDO\_MAX\_DATA\_OBJECTS 7

377

[ 382](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328)enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) {

[ 384](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328abbc517bb47b6bdc76e44b599523e0d93) [PDO\_FIXED](pd_8h.md#a9fa615ab7f38385c21277d4e9e6a1441) = 0,

[ 386](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328a63f4fb7a4d2f7e265fd49be07966fbaa) [PDO\_BATTERY](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328a63f4fb7a4d2f7e265fd49be07966fbaa) = 1,

[ 388](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328a1726efca9ece0ff017cc4aaf05ce9624) [PDO\_VARIABLE](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328a1726efca9ece0ff017cc4aaf05ce9624) = 2,

[ 390](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328adb8478434cc1622e98bc22f4081dff1e) [PDO\_AUGMENTED](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328adb8478434cc1622e98bc22f4081dff1e) = 3

391};

392

[ 398](group__usb__power__delivery.md#ga65e9aa05457df787c5be6792ce725afd)#define PD\_CONVERT\_MA\_TO\_FIXED\_PDO\_CURRENT(c) ((c) / 10)

399

[ 405](group__usb__power__delivery.md#gad79de03a60054be13c9757d933069fe2)#define PD\_CONVERT\_MV\_TO\_FIXED\_PDO\_VOLTAGE(v) ((v) / 50)

406

[ 412](group__usb__power__delivery.md#gaa0997fc5d7f26115c64f220d2ab91ef2)#define PD\_CONVERT\_FIXED\_PDO\_CURRENT\_TO\_MA(c) ((c) \* 10)

413

[ 421](group__usb__power__delivery.md#gae9eaed8554f857d183e24b96cd69afe3)#define PD\_CONVERT\_FIXED\_PDO\_VOLTAGE\_TO\_MV(v) ((v) \* 50)

422

[ 427](unionpd__fixed__supply__pdo__source.md)union [pd\_fixed\_supply\_pdo\_source](unionpd__fixed__supply__pdo__source.md) {

428 struct {

[ 430](unionpd__fixed__supply__pdo__source.md#a86664d945f65f19f7b96da1148700640) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_current](unionpd__fixed__supply__pdo__source.md#a86664d945f65f19f7b96da1148700640) : 10;

[ 432](unionpd__fixed__supply__pdo__source.md#a66f55e177b6f2bc76b392707e39fa4fe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [voltage](unionpd__fixed__supply__pdo__source.md#a66f55e177b6f2bc76b392707e39fa4fe) : 10;

[ 434](unionpd__fixed__supply__pdo__source.md#a2c4b27407245da04b67e9524173d39bc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [peak\_current](unionpd__fixed__supply__pdo__source.md#a2c4b27407245da04b67e9524173d39bc) : 2;

[ 436](unionpd__fixed__supply__pdo__source.md#a6b0e04acd43c9b18bd1dea80508a8817) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved0](unionpd__fixed__supply__pdo__source.md#a6b0e04acd43c9b18bd1dea80508a8817) : 2;

[ 438](unionpd__fixed__supply__pdo__source.md#a440ff92d2bd533e3ddd6c65f9ac21772) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unchunked\_ext\_msg\_supported](unionpd__fixed__supply__pdo__source.md#a440ff92d2bd533e3ddd6c65f9ac21772) : 1;

[ 440](unionpd__fixed__supply__pdo__source.md#a7b89666e3753966001caf7602c796147) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dual\_role\_data](unionpd__fixed__supply__pdo__source.md#a7b89666e3753966001caf7602c796147) : 1;

[ 442](unionpd__fixed__supply__pdo__source.md#a6c1bcf37a1fc9a348cf19e16fbe01dac) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [usb\_comms\_capable](unionpd__fixed__supply__pdo__source.md#a6c1bcf37a1fc9a348cf19e16fbe01dac) : 1;

[ 444](unionpd__fixed__supply__pdo__source.md#a9fc10f3ec4126c063f5dd99e8f3e2723) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unconstrained\_power](unionpd__fixed__supply__pdo__source.md#a9fc10f3ec4126c063f5dd99e8f3e2723) : 1;

[ 446](unionpd__fixed__supply__pdo__source.md#a55003edba55a920a386cc04cbc7a72a0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [usb\_suspend\_supported](unionpd__fixed__supply__pdo__source.md#a55003edba55a920a386cc04cbc7a72a0) : 1;

[ 448](unionpd__fixed__supply__pdo__source.md#af96673f1ac078436a9eca0973e1bdef9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dual\_role\_power](unionpd__fixed__supply__pdo__source.md#af96673f1ac078436a9eca0973e1bdef9) : 1;

[ 450](unionpd__fixed__supply__pdo__source.md#a111b87e88b4f78e60b78d35dfbcbc307) enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) [type](unionpd__fixed__supply__pdo__source.md#a111b87e88b4f78e60b78d35dfbcbc307) : 2;

451 };

[ 453](unionpd__fixed__supply__pdo__source.md#a9227629f6c97357b71ea20e4e0572cf2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw\_value](unionpd__fixed__supply__pdo__source.md#a9227629f6c97357b71ea20e4e0572cf2);

454};

455

[ 459](group__usb__power__delivery.md#ga48b33240e19524ea003052103d310358)enum [pd\_frs\_type](group__usb__power__delivery.md#ga48b33240e19524ea003052103d310358) {

[ 461](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358acbf2bf3ae21ff1ea51d7fd2b823ce726) [FRS\_NOT\_SUPPORTED](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358acbf2bf3ae21ff1ea51d7fd2b823ce726),

[ 463](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358a4cd44f89f225f8869bfd901e7ea79aed) [FRS\_DEFAULT\_USB\_POWER](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358a4cd44f89f225f8869bfd901e7ea79aed),

[ 465](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358acac5008ded87d7a20b0b3b272075e4c1) [FRS\_1P5A\_5V](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358acac5008ded87d7a20b0b3b272075e4c1),

[ 467](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358a99ab2afc15809b5e89e3fb7106be37ba) [FRS\_3P0A\_5V](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358a99ab2afc15809b5e89e3fb7106be37ba)

468};

469

[ 474](unionpd__fixed__supply__pdo__sink.md)union [pd\_fixed\_supply\_pdo\_sink](unionpd__fixed__supply__pdo__sink.md) {

475 struct {

[ 477](unionpd__fixed__supply__pdo__sink.md#a2ac4005b0cf3e28ade8f508d2c6f5e20) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [operational\_current](unionpd__fixed__supply__pdo__sink.md#a2ac4005b0cf3e28ade8f508d2c6f5e20) : 10;

[ 479](unionpd__fixed__supply__pdo__sink.md#ac47dcf98dfca90eb0e6013a3e1c5eb18) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [voltage](unionpd__fixed__supply__pdo__sink.md#ac47dcf98dfca90eb0e6013a3e1c5eb18) : 10;

[ 481](unionpd__fixed__supply__pdo__sink.md#a22f9763652560dbd215324f1bb878a96) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved0](unionpd__fixed__supply__pdo__sink.md#a22f9763652560dbd215324f1bb878a96) : 3;

[ 483](unionpd__fixed__supply__pdo__sink.md#a7138e45345fc2cd486186190f11e847d) enum [pd\_frs\_type](group__usb__power__delivery.md#ga48b33240e19524ea003052103d310358) [frs\_required](unionpd__fixed__supply__pdo__sink.md#a7138e45345fc2cd486186190f11e847d) : 2;

[ 485](unionpd__fixed__supply__pdo__sink.md#a5c6bfb21c4d8e70a04895dd31a58885e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dual\_role\_data](unionpd__fixed__supply__pdo__sink.md#a5c6bfb21c4d8e70a04895dd31a58885e) : 1;

[ 487](unionpd__fixed__supply__pdo__sink.md#a0559272067e2d0c33f52274fb59ea18d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [usb\_comms\_capable](unionpd__fixed__supply__pdo__sink.md#a0559272067e2d0c33f52274fb59ea18d) : 1;

[ 489](unionpd__fixed__supply__pdo__sink.md#ab406f1f36e5fe6f7acb9abc91991a803) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unconstrained\_power](unionpd__fixed__supply__pdo__sink.md#ab406f1f36e5fe6f7acb9abc91991a803) : 1;

[ 491](unionpd__fixed__supply__pdo__sink.md#a3086d57313f05b8bc91fb3590e51c657) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [higher\_capability](unionpd__fixed__supply__pdo__sink.md#a3086d57313f05b8bc91fb3590e51c657) : 1;

[ 493](unionpd__fixed__supply__pdo__sink.md#aad255dbee3452bf3276464c59f113cb2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dual\_role\_power](unionpd__fixed__supply__pdo__sink.md#aad255dbee3452bf3276464c59f113cb2) : 1;

[ 495](unionpd__fixed__supply__pdo__sink.md#ac505fdd24064de98c5c17088b2c88c5c) enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) [type](unionpd__fixed__supply__pdo__sink.md#ac505fdd24064de98c5c17088b2c88c5c) : 2;

496 };

[ 498](unionpd__fixed__supply__pdo__sink.md#aebdeb854bcac0d20efcbe3be56dcc9f8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw\_value](unionpd__fixed__supply__pdo__sink.md#aebdeb854bcac0d20efcbe3be56dcc9f8);

499};

500

[ 506](group__usb__power__delivery.md#gab3ea3b392e8fc27b4f100a99988d0ca5)#define PD\_CONVERT\_MA\_TO\_VARIABLE\_PDO\_CURRENT(c) ((c) / 10)

507

[ 513](group__usb__power__delivery.md#gae729bb9b17bc0df4201ec27f1f506921)#define PD\_CONVERT\_MV\_TO\_VARIABLE\_PDO\_VOLTAGE(v) ((v) / 50)

514

[ 520](group__usb__power__delivery.md#ga9cd0c218385b400b3efe34474f546203)#define PD\_CONVERT\_VARIABLE\_PDO\_CURRENT\_TO\_MA(c) ((c) \* 10)

521

[ 527](group__usb__power__delivery.md#ga4973b120261cde51c86c7b76422222fc)#define PD\_CONVERT\_VARIABLE\_PDO\_VOLTAGE\_TO\_MV(v) ((v) \* 50)

528

[ 533](unionpd__variable__supply__pdo__source.md)union [pd\_variable\_supply\_pdo\_source](unionpd__variable__supply__pdo__source.md) {

534 struct {

[ 536](unionpd__variable__supply__pdo__source.md#a8193ca96084db5901bb30195113ff01f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_current](unionpd__variable__supply__pdo__source.md#a8193ca96084db5901bb30195113ff01f) : 10;

[ 538](unionpd__variable__supply__pdo__source.md#a67d86c71997a7c0605b8a199cd51c920) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_voltage](unionpd__variable__supply__pdo__source.md#a67d86c71997a7c0605b8a199cd51c920) : 10;

[ 540](unionpd__variable__supply__pdo__source.md#a008cf5201ea6d3e238d547b738570c45) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_voltage](unionpd__variable__supply__pdo__source.md#a008cf5201ea6d3e238d547b738570c45) : 10;

[ 542](unionpd__variable__supply__pdo__source.md#a5da7eb69fc69a58662f09690fba92633) enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) [type](unionpd__variable__supply__pdo__source.md#a5da7eb69fc69a58662f09690fba92633) : 2;

543 };

[ 545](unionpd__variable__supply__pdo__source.md#af00512126f128bf1cf31e802652af1bf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw\_value](unionpd__variable__supply__pdo__source.md#af00512126f128bf1cf31e802652af1bf);

546};

547

[ 552](unionpd__variable__supply__pdo__sink.md)union [pd\_variable\_supply\_pdo\_sink](unionpd__variable__supply__pdo__sink.md) {

553 struct {

[ 555](unionpd__variable__supply__pdo__sink.md#ad648f2400a495b37d8b9f995556419d0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [operational\_current](unionpd__variable__supply__pdo__sink.md#ad648f2400a495b37d8b9f995556419d0) : 10;

[ 557](unionpd__variable__supply__pdo__sink.md#aaaa1cf3f08208966fb00093f910f70ab) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_voltage](unionpd__variable__supply__pdo__sink.md#aaaa1cf3f08208966fb00093f910f70ab) : 10;

[ 559](unionpd__variable__supply__pdo__sink.md#ae360e7c2335a4f6cf5d267c8c82fdc45) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_voltage](unionpd__variable__supply__pdo__sink.md#ae360e7c2335a4f6cf5d267c8c82fdc45) : 10;

[ 561](unionpd__variable__supply__pdo__sink.md#a4a09b8b5e2397925d5a433917378193e) enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) [type](unionpd__variable__supply__pdo__sink.md#a4a09b8b5e2397925d5a433917378193e) : 2;

562 };

[ 564](unionpd__variable__supply__pdo__sink.md#a2ff80c049f98ab090b100b7f9877bffb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw\_value](unionpd__variable__supply__pdo__sink.md#a2ff80c049f98ab090b100b7f9877bffb);

565};

566

[ 572](group__usb__power__delivery.md#ga457907a516a2cf497569ce43561fe7dd)#define PD\_CONVERT\_MW\_TO\_BATTERY\_PDO\_POWER(c) ((c) / 250)

573

[ 579](group__usb__power__delivery.md#ga4832aa2b18ff84bfcf3a252361628281)#define PD\_CONVERT\_MV\_TO\_BATTERY\_PDO\_VOLTAGE(v) ((v) / 50)

580

[ 586](group__usb__power__delivery.md#ga614dd17b2b98309a837be8e0578bb06b)#define PD\_CONVERT\_BATTERY\_PDO\_POWER\_TO\_MW(c) ((c) \* 250)

587

[ 593](group__usb__power__delivery.md#ga74af9a3f10f1855d7322dc36fabdff1a)#define PD\_CONVERT\_BATTERY\_PDO\_VOLTAGE\_TO\_MV(v) ((v) \* 50)

594

[ 599](unionpd__battery__supply__pdo__source.md)union [pd\_battery\_supply\_pdo\_source](unionpd__battery__supply__pdo__source.md) {

600 struct {

[ 602](unionpd__battery__supply__pdo__source.md#a00ea9931d839cf83b56513f77aa7d5b9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_power](unionpd__battery__supply__pdo__source.md#a00ea9931d839cf83b56513f77aa7d5b9) : 10;

[ 604](unionpd__battery__supply__pdo__source.md#afa2335788e7fde01b90afd95bccf6d5f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_voltage](unionpd__battery__supply__pdo__source.md#afa2335788e7fde01b90afd95bccf6d5f) : 10;

[ 606](unionpd__battery__supply__pdo__source.md#a673ea076da8810bc694b2dc82bbede67) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_voltage](unionpd__battery__supply__pdo__source.md#a673ea076da8810bc694b2dc82bbede67) : 10;

[ 608](unionpd__battery__supply__pdo__source.md#ab546fd1a6caa77a57b5d5420a8ee31d7) enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) [type](unionpd__battery__supply__pdo__source.md#ab546fd1a6caa77a57b5d5420a8ee31d7) : 2;

609 };

[ 611](unionpd__battery__supply__pdo__source.md#a1e775dc0082b531216c154724be360b0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw\_value](unionpd__battery__supply__pdo__source.md#a1e775dc0082b531216c154724be360b0);

612};

613

[ 618](unionpd__battery__supply__pdo__sink.md)union [pd\_battery\_supply\_pdo\_sink](unionpd__battery__supply__pdo__sink.md) {

619 struct {

[ 621](unionpd__battery__supply__pdo__sink.md#a3f1072c4ca168aaedd13257f01f410aa) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [operational\_power](unionpd__battery__supply__pdo__sink.md#a3f1072c4ca168aaedd13257f01f410aa) : 10;

[ 623](unionpd__battery__supply__pdo__sink.md#a5a588a46ae8bef2dc10445c2f5422246) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_voltage](unionpd__battery__supply__pdo__sink.md#a5a588a46ae8bef2dc10445c2f5422246) : 10;

[ 625](unionpd__battery__supply__pdo__sink.md#a858efb23a0c143917b88e5596b899c79) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_voltage](unionpd__battery__supply__pdo__sink.md#a858efb23a0c143917b88e5596b899c79) : 10;

[ 627](unionpd__battery__supply__pdo__sink.md#acb8b674a789f0a5b397d7ab93d443543) enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) [type](unionpd__battery__supply__pdo__sink.md#acb8b674a789f0a5b397d7ab93d443543) : 2;

628 };

[ 630](unionpd__battery__supply__pdo__sink.md#aa973b26972c1e1a96c7e0c09dbed08f3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw\_value](unionpd__battery__supply__pdo__sink.md#aa973b26972c1e1a96c7e0c09dbed08f3);

631};

632

[ 638](group__usb__power__delivery.md#ga1d73d5ffc7e6657dae81604ffb49b358)#define PD\_CONVERT\_MA\_TO\_AUGMENTED\_PDO\_CURRENT(c) ((c) / 50)

639

[ 645](group__usb__power__delivery.md#ga1dd7da9850daae859d572d866c8c87e2)#define PD\_CONVERT\_MV\_TO\_AUGMENTED\_PDO\_VOLTAGE(v) ((v) / 100)

646

[ 652](group__usb__power__delivery.md#ga202d52036ee2fb6d6da3594c126cf82b)#define PD\_CONVERT\_AUGMENTED\_PDO\_CURRENT\_TO\_MA(c) ((c) \* 50)

653

[ 659](group__usb__power__delivery.md#ga8623c319b19e7444ba400c738848d9ae)#define PD\_CONVERT\_AUGMENTED\_PDO\_VOLTAGE\_TO\_MV(v) ((v) \* 100)

660

[ 665](unionpd__augmented__supply__pdo__source.md)union [pd\_augmented\_supply\_pdo\_source](unionpd__augmented__supply__pdo__source.md) {

666 struct {

[ 668](unionpd__augmented__supply__pdo__source.md#a7ef0b26951ce2683c9c4ca0f19b73d6d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_current](unionpd__augmented__supply__pdo__source.md#a7ef0b26951ce2683c9c4ca0f19b73d6d) : 7;

[ 670](unionpd__augmented__supply__pdo__source.md#ac046ddf128416ecbb8f3a26185d03e03) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved0](unionpd__augmented__supply__pdo__source.md#ac046ddf128416ecbb8f3a26185d03e03) : 1;

[ 672](unionpd__augmented__supply__pdo__source.md#a56e1af2acda73fee7e40449b7c39745d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_voltage](unionpd__augmented__supply__pdo__source.md#a56e1af2acda73fee7e40449b7c39745d) : 8;

[ 674](unionpd__augmented__supply__pdo__source.md#ae79eb7473040058c0b8572cfe4fa4dce) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved1](unionpd__augmented__supply__pdo__source.md#ae79eb7473040058c0b8572cfe4fa4dce) : 1;

[ 676](unionpd__augmented__supply__pdo__source.md#aba6df91a8c5da92517f885fa89af8747) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_voltage](unionpd__augmented__supply__pdo__source.md#aba6df91a8c5da92517f885fa89af8747) : 8;

[ 678](unionpd__augmented__supply__pdo__source.md#ab5868f6ba91821d56ddb419e895a05fa) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved2](unionpd__augmented__supply__pdo__source.md#ab5868f6ba91821d56ddb419e895a05fa) : 2;

[ 680](unionpd__augmented__supply__pdo__source.md#abfac34ee5da0b1700b784c7bfe925c19) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pps\_power\_limited](unionpd__augmented__supply__pdo__source.md#abfac34ee5da0b1700b784c7bfe925c19) : 1;

[ 686](unionpd__augmented__supply__pdo__source.md#aa59ad8a8eb4e2343c14bbe54937aa93d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved3](unionpd__augmented__supply__pdo__source.md#aa59ad8a8eb4e2343c14bbe54937aa93d) : 2;

[ 688](unionpd__augmented__supply__pdo__source.md#aaea2842b628bde92bb74ab0eb7d5aad4) enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) [type](unionpd__augmented__supply__pdo__source.md#aaea2842b628bde92bb74ab0eb7d5aad4) : 2;

689 };

[ 691](unionpd__augmented__supply__pdo__source.md#a093a674e538dcc2541ff86f50d0156df) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw\_value](unionpd__augmented__supply__pdo__source.md#a093a674e538dcc2541ff86f50d0156df);

692};

693

[ 698](unionpd__augmented__supply__pdo__sink.md)union [pd\_augmented\_supply\_pdo\_sink](unionpd__augmented__supply__pdo__sink.md) {

699 struct {

[ 701](unionpd__augmented__supply__pdo__sink.md#a0a5da0df48dff5fae42159026c91c7af) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_current](unionpd__augmented__supply__pdo__sink.md#a0a5da0df48dff5fae42159026c91c7af) : 7;

[ 703](unionpd__augmented__supply__pdo__sink.md#a3320455a4c7673d3db95f585b07cc319) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved0](unionpd__augmented__supply__pdo__sink.md#a3320455a4c7673d3db95f585b07cc319) : 1;

[ 705](unionpd__augmented__supply__pdo__sink.md#ad83710136d9dcad3644ec36c1eee9cb0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_voltage](unionpd__augmented__supply__pdo__sink.md#ad83710136d9dcad3644ec36c1eee9cb0) : 8;

[ 707](unionpd__augmented__supply__pdo__sink.md#a2f1f6094af7449619ab626476fa51698) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved1](unionpd__augmented__supply__pdo__sink.md#a2f1f6094af7449619ab626476fa51698) : 1;

[ 709](unionpd__augmented__supply__pdo__sink.md#af5eca8ab38a3eaaaecd10cdc1092ce3c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_voltage](unionpd__augmented__supply__pdo__sink.md#af5eca8ab38a3eaaaecd10cdc1092ce3c) : 8;

[ 711](unionpd__augmented__supply__pdo__sink.md#adfa0b8ab656255cfecc9ca5e1ee05d49) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved2](unionpd__augmented__supply__pdo__sink.md#adfa0b8ab656255cfecc9ca5e1ee05d49) : 3;

[ 717](unionpd__augmented__supply__pdo__sink.md#a22e63fa7e83af25d9822dcf3d9b35f40) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved3](unionpd__augmented__supply__pdo__sink.md#a22e63fa7e83af25d9822dcf3d9b35f40) : 2;

[ 719](unionpd__augmented__supply__pdo__sink.md#ad9d2fe810bd3959b99b38180c93a71c0) enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) [type](unionpd__augmented__supply__pdo__sink.md#ad9d2fe810bd3959b99b38180c93a71c0) : 2;

720 };

[ 722](unionpd__augmented__supply__pdo__sink.md#ae28a74642ffcdf1100f37e3542e1ca96) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw\_value](unionpd__augmented__supply__pdo__sink.md#ae28a74642ffcdf1100f37e3542e1ca96);

723};

724

[ 730](unionpd__rdo.md)union [pd\_rdo](unionpd__rdo.md) {

735 struct {

[ 743](unionpd__rdo.md#a41d023e9308e6d252f0bc8412a6c6184) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_or\_max\_operating\_current](unionpd__rdo.md#a41d023e9308e6d252f0bc8412a6c6184) : 10;

[ 745](unionpd__rdo.md#a8c11df4b75772cda511bd94e5a297128) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [operating\_current](unionpd__rdo.md#a8c11df4b75772cda511bd94e5a297128) : 10;

[ 747](unionpd__rdo.md#ab4065aee18c3a68df38592122f607343) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved0](unionpd__rdo.md#ab4065aee18c3a68df38592122f607343) : 3;

[ 749](unionpd__rdo.md#ae71e9abde3d69211c7bcfc7b80d18c41) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unchunked\_ext\_msg\_supported](unionpd__rdo.md#ae71e9abde3d69211c7bcfc7b80d18c41) : 1;

[ 751](unionpd__rdo.md#ae90a23cc166373f7bb3c35be0c3967f2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [no\_usb\_suspend](unionpd__rdo.md#ae90a23cc166373f7bb3c35be0c3967f2) : 1;

[ 753](unionpd__rdo.md#a30f6044378cad6f277f8694df5611230) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [usb\_comm\_capable](unionpd__rdo.md#a30f6044378cad6f277f8694df5611230) : 1;

[ 755](unionpd__rdo.md#afd24863b120085c57e77b8d246effd54) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cap\_mismatch](unionpd__rdo.md#afd24863b120085c57e77b8d246effd54) : 1;

[ 757](unionpd__rdo.md#ae5ae5d3c823254ab895becc3b01761fe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [giveback](unionpd__rdo.md#ae5ae5d3c823254ab895becc3b01761fe) : 1;

[ 759](unionpd__rdo.md#aff1b20a6e4905ac714ab5e7af7ff9593) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [object\_pos](unionpd__rdo.md#aff1b20a6e4905ac714ab5e7af7ff9593) : 3;

[ 761](unionpd__rdo.md#aa5af5685e6d9c3d8a7ec3a40d25b43ba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved1](unionpd__rdo.md#aa5af5685e6d9c3d8a7ec3a40d25b43ba) : 1;

[ 762](unionpd__rdo.md#a0b7502c79b0976b8e0d118cae3950191) } [fixed](unionpd__rdo.md#a0b7502c79b0976b8e0d118cae3950191);

763

768 struct {

776 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_or\_max\_operating\_current](unionpd__rdo.md#a41d023e9308e6d252f0bc8412a6c6184) : 10;

778 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [operating\_current](unionpd__rdo.md#a8c11df4b75772cda511bd94e5a297128) : 10;

780 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved0](unionpd__rdo.md#ab4065aee18c3a68df38592122f607343) : 3;

782 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unchunked\_ext\_msg\_supported](unionpd__rdo.md#ae71e9abde3d69211c7bcfc7b80d18c41) : 1;

784 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [no\_usb\_suspend](unionpd__rdo.md#ae90a23cc166373f7bb3c35be0c3967f2) : 1;

786 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [usb\_comm\_capable](unionpd__rdo.md#a30f6044378cad6f277f8694df5611230) : 1;

788 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cap\_mismatch](unionpd__rdo.md#afd24863b120085c57e77b8d246effd54) : 1;

790 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [giveback](unionpd__rdo.md#ae5ae5d3c823254ab895becc3b01761fe) : 1;

792 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [object\_pos](unionpd__rdo.md#aff1b20a6e4905ac714ab5e7af7ff9593) : 3;

794 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved1](unionpd__rdo.md#aa5af5685e6d9c3d8a7ec3a40d25b43ba) : 1;

[ 795](unionpd__rdo.md#a82e1adf30b6fc476b794b94cfb379214) } [variable](unionpd__rdo.md#a82e1adf30b6fc476b794b94cfb379214);

796

801 struct {

[ 803](unionpd__rdo.md#ab59da7098c1d33c9269f66dd3ac3fc5b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_operating\_power](unionpd__rdo.md#ab59da7098c1d33c9269f66dd3ac3fc5b) : 10;

[ 805](unionpd__rdo.md#a63dd2a9e94f3a61205b95efc0cf79f13) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [operating\_power](unionpd__rdo.md#a63dd2a9e94f3a61205b95efc0cf79f13) : 10;

807 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved0](unionpd__rdo.md#ab4065aee18c3a68df38592122f607343) : 3;

809 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unchunked\_ext\_msg\_supported](unionpd__rdo.md#ae71e9abde3d69211c7bcfc7b80d18c41) : 1;

811 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [no\_usb\_suspend](unionpd__rdo.md#ae90a23cc166373f7bb3c35be0c3967f2) : 1;

813 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [usb\_comm\_capable](unionpd__rdo.md#a30f6044378cad6f277f8694df5611230) : 1;

815 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cap\_mismatch](unionpd__rdo.md#afd24863b120085c57e77b8d246effd54) : 1;

817 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [giveback](unionpd__rdo.md#ae5ae5d3c823254ab895becc3b01761fe) : 1;

819 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [object\_pos](unionpd__rdo.md#aff1b20a6e4905ac714ab5e7af7ff9593) : 3;

821 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved1](unionpd__rdo.md#aa5af5685e6d9c3d8a7ec3a40d25b43ba) : 1;

[ 822](unionpd__rdo.md#a5838022e249981be50aee897c16ce56e) } [battery](unionpd__rdo.md#a5838022e249981be50aee897c16ce56e);

823

828 struct {

830 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [operating\_current](unionpd__rdo.md#a8c11df4b75772cda511bd94e5a297128) : 7;

832 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved0](unionpd__rdo.md#ab4065aee18c3a68df38592122f607343) : 2;

[ 834](unionpd__rdo.md#ad7a98411aad054f1161b4ce32ef3ee33) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [output\_voltage](unionpd__rdo.md#ad7a98411aad054f1161b4ce32ef3ee33) : 11;

836 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved1](unionpd__rdo.md#aa5af5685e6d9c3d8a7ec3a40d25b43ba) : 3;

838 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unchunked\_ext\_msg\_supported](unionpd__rdo.md#ae71e9abde3d69211c7bcfc7b80d18c41) : 1;

840 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [no\_usb\_suspend](unionpd__rdo.md#ae90a23cc166373f7bb3c35be0c3967f2) : 1;

842 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [usb\_comm\_capable](unionpd__rdo.md#a30f6044378cad6f277f8694df5611230) : 1;

844 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cap\_mismatch](unionpd__rdo.md#afd24863b120085c57e77b8d246effd54) : 1;

[ 846](unionpd__rdo.md#a5f8b64ce53d9881a007405a986b6b490) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved2](unionpd__rdo.md#a5f8b64ce53d9881a007405a986b6b490) : 1;

848 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [object\_pos](unionpd__rdo.md#aff1b20a6e4905ac714ab5e7af7ff9593) : 3;

[ 850](unionpd__rdo.md#aa0ddbfb3c345b671f97d4b4e760168b4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved3](unionpd__rdo.md#aa0ddbfb3c345b671f97d4b4e760168b4) : 1;

[ 851](unionpd__rdo.md#ad6b45a879e689dcd05bf9e07aedc4d20) } [augmented](unionpd__rdo.md#ad6b45a879e689dcd05bf9e07aedc4d20);

[ 853](unionpd__rdo.md#a477cf38b68b9386e950c085a1ce4f336) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [raw\_value](unionpd__rdo.md#a477cf38b68b9386e950c085a1ce4f336);

854};

855

[ 859](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700)enum [pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700) {

[ 861](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700a1d9b4c553f44dccdc67e4edb554557b9) [PD\_REV10](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700a1d9b4c553f44dccdc67e4edb554557b9) = 0,

[ 863](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700a22c122b1d30a3ab96fffd5dfa6bfb9ae) [PD\_REV20](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700a22c122b1d30a3ab96fffd5dfa6bfb9ae) = 1,

[ 865](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700af3770bcbcf6feaaab272c022d7a57c7a) [PD\_REV30](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700af3770bcbcf6feaaab272c022d7a57c7a) = 2,

866};

867

[ 873](group__usb__power__delivery.md#gad2df13a24f0365198d37b10af608376b)enum [pd\_packet\_type](group__usb__power__delivery.md#gad2df13a24f0365198d37b10af608376b) {

[ 875](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba0bede6a56c24b06fdf56cf1dc386bb14) [PD\_PACKET\_SOP](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba0bede6a56c24b06fdf56cf1dc386bb14) = 0,

[ 877](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376bae3a5f99242ab24a34706170101b38ef8) [PD\_PACKET\_SOP\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376bae3a5f99242ab24a34706170101b38ef8) = 1,

[ 879](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba5ecd663a9eecefcf965f605125d5188c) [PD\_PACKET\_PRIME\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba5ecd663a9eecefcf965f605125d5188c) = 2,

[ 881](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba63b2200ebaf016d06437f3586d15171d) [PD\_PACKET\_DEBUG\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba63b2200ebaf016d06437f3586d15171d) = 3,

[ 883](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1) [PD\_PACKET\_DEBUG\_PRIME\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1) = 4,

[ 885](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376baa5cd066e86fd55727c3625cd16633f73) [PD\_PACKET\_TX\_HARD\_RESET](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376baa5cd066e86fd55727c3625cd16633f73) = 5,

[ 887](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba531ebc6013984b81e6fb550618d6b4a8) [PD\_PACKET\_CABLE\_RESET](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba531ebc6013984b81e6fb550618d6b4a8) = 6,

[ 889](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376bafcd21cc6b1ae6c58b86c0619d687e8fc) [PD\_PACKET\_TX\_BIST\_MODE\_2](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376bafcd21cc6b1ae6c58b86c0619d687e8fc) = 7,

890

[ 892](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba55bb88e5955992170bee96ddbe8a7437) [PD\_PACKET\_MSG\_INVALID](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba55bb88e5955992170bee96ddbe8a7437) = 0xf

893};

894

[ 898](group__usb__power__delivery.md#ga1bb5fd6bb6657399a75b095eb3442bde)#define NUM\_SOP\_STAR\_TYPES (PD\_PACKET\_DEBUG\_PRIME\_PRIME + 1)

899

[ 904](group__usb__power__delivery.md#ga4c7862a3e953fb22534123223c942f9a)enum [pd\_ctrl\_msg\_type](group__usb__power__delivery.md#ga4c7862a3e953fb22534123223c942f9a) {

906

[ 908](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aae0895be53e5a1e54731e9608a8e0c6c9) [PD\_CTRL\_GOOD\_CRC](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aae0895be53e5a1e54731e9608a8e0c6c9) = 1,

[ 910](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa4ba7f63cdcbe766a34047e06145a591e) [PD\_CTRL\_GOTO\_MIN](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa4ba7f63cdcbe766a34047e06145a591e) = 2,

[ 912](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa56df68ed627b56bbcfc20900ec5d2e5d) [PD\_CTRL\_ACCEPT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa56df68ed627b56bbcfc20900ec5d2e5d) = 3,

[ 914](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa9dd7b559e78a99639056325a7be14d81) [PD\_CTRL\_REJECT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa9dd7b559e78a99639056325a7be14d81) = 4,

[ 916](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa8177040ca8a1f71dde67fc59060c35ed) [PD\_CTRL\_PING](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa8177040ca8a1f71dde67fc59060c35ed) = 5,

[ 918](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aafc449fc3dc39f2495494507cc97f53ad) [PD\_CTRL\_PS\_RDY](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aafc449fc3dc39f2495494507cc97f53ad) = 6,

[ 920](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa9324307526500683ae265e9cb0063929) [PD\_CTRL\_GET\_SOURCE\_CAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa9324307526500683ae265e9cb0063929) = 7,

[ 922](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aaaf5c221569a9108bdbc36545dcb37495) [PD\_CTRL\_GET\_SINK\_CAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aaaf5c221569a9108bdbc36545dcb37495) = 8,

[ 924](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa4aba967f7e363dbbadcc9a9ecf0c7ae4) [PD\_CTRL\_DR\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa4aba967f7e363dbbadcc9a9ecf0c7ae4) = 9,

[ 926](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aade67c4fb153e5ba87b6d6643f99260f9) [PD\_CTRL\_PR\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aade67c4fb153e5ba87b6d6643f99260f9) = 10,

[ 928](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa68820e99ce9c1c73180734372e5ede2b) [PD\_CTRL\_VCONN\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa68820e99ce9c1c73180734372e5ede2b) = 11,

[ 930](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa3b6fc49b1ae0bb343d39476350b59c90) [PD\_CTRL\_WAIT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa3b6fc49b1ae0bb343d39476350b59c90) = 12,

[ 932](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aadeb12ed01ec54ee55588bfb796dd0c11) [PD\_CTRL\_SOFT\_RESET](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aadeb12ed01ec54ee55588bfb796dd0c11) = 13,

933

935

[ 937](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa03f9886881aa493fb0f9bfac16713e7a) [PD\_CTRL\_DATA\_RESET](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa03f9886881aa493fb0f9bfac16713e7a) = 14,

[ 939](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa27caca37f9522045bc8612f7536cd792) [PD\_CTRL\_DATA\_RESET\_COMPLETE](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa27caca37f9522045bc8612f7536cd792) = 15,

[ 941](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aabfea5fdf0263fdf4c924bd603ee7256f) [PD\_CTRL\_NOT\_SUPPORTED](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aabfea5fdf0263fdf4c924bd603ee7256f) = 16,

[ 943](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aab0ca2628b144d092116b461703176eaa) [PD\_CTRL\_GET\_SOURCE\_CAP\_EXT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aab0ca2628b144d092116b461703176eaa) = 17,

[ 945](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa23287276ee22241906828515f38fedef) [PD\_CTRL\_GET\_STATUS](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa23287276ee22241906828515f38fedef) = 18,

[ 947](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa1c597b5f953e6e1791aa869025b98b24) [PD\_CTRL\_FR\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa1c597b5f953e6e1791aa869025b98b24) = 19,

[ 949](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aab82efb96b1f8f7dae3c76e362ae1715a) [PD\_CTRL\_GET\_PPS\_STATUS](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aab82efb96b1f8f7dae3c76e362ae1715a) = 20,

[ 951](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa677ebc41b4b67de6ee93b5e446af702e) [PD\_CTRL\_GET\_COUNTRY\_CODES](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa677ebc41b4b67de6ee93b5e446af702e) = 21,

[ 953](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aaaa0a5bba9a9f1573952141c4f8f77318) [PD\_CTRL\_GET\_SINK\_CAP\_EXT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aaaa0a5bba9a9f1573952141c4f8f77318) = 22

954

956};

957

[ 962](group__usb__power__delivery.md#ga8239651864b4cb0e1fc89ba2d7e59462)enum [pd\_data\_msg\_type](group__usb__power__delivery.md#ga8239651864b4cb0e1fc89ba2d7e59462) {

964

[ 966](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad9a0cf16cfa852111ea0ed3434b35dfc) [PD\_DATA\_SOURCE\_CAP](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad9a0cf16cfa852111ea0ed3434b35dfc) = 1,

[ 968](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad9c920f987e2578b030cc08f2e69998a) [PD\_DATA\_REQUEST](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad9c920f987e2578b030cc08f2e69998a) = 2,

[ 970](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a7c4bc907fb81082da05c64797854be9f) [PD\_DATA\_BIST](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a7c4bc907fb81082da05c64797854be9f) = 3,

[ 972](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a4cf30dcbce3fdf8076713e45d242b39a) [PD\_DATA\_SINK\_CAP](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a4cf30dcbce3fdf8076713e45d242b39a) = 4,

[ 974](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad493f01ffc4c3c164f874eb202f8adb0) [PD\_DATA\_BATTERY\_STATUS](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad493f01ffc4c3c164f874eb202f8adb0) = 5,

[ 976](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a7e3368e1c7bde4c6bb3136cb80209bb6) [PD\_DATA\_ALERT](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a7e3368e1c7bde4c6bb3136cb80209bb6) = 6,

[ 978](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a83d7098236e97972cf24b900f7e5e069) [PD\_DATA\_GET\_COUNTRY\_INFO](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a83d7098236e97972cf24b900f7e5e069) = 7,

979

981

[ 983](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a1a0829560f9f82182f7587fd8787a846) [PD\_DATA\_ENTER\_USB](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a1a0829560f9f82182f7587fd8787a846) = 8,

[ 985](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a881fcbc2dc5f8b1de7c97522df46242d) [PD\_DATA\_VENDOR\_DEF](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a881fcbc2dc5f8b1de7c97522df46242d) = 15,

986};

987

[ 992](group__usb__power__delivery.md#ga457308d50365e0a2440e94e41a316cbf)enum [pd\_ext\_msg\_type](group__usb__power__delivery.md#ga457308d50365e0a2440e94e41a316cbf) {

994

[ 996](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa51c03e44c3fe1bb59445bbc452ea7199) [PD\_EXT\_SOURCE\_CAP](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa51c03e44c3fe1bb59445bbc452ea7199) = 1,

[ 998](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa836130da5307aed6160deadadf2f4f3f) [PD\_EXT\_STATUS](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa836130da5307aed6160deadadf2f4f3f) = 2,

[ 1000](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa9c50488735d7723c3cc30f176c221e40) [PD\_EXT\_GET\_BATTERY\_CAP](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa9c50488735d7723c3cc30f176c221e40) = 3,

[ 1002](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa77ff801aa819461f0f5ff44546370bd7) [PD\_EXT\_GET\_BATTERY\_STATUS](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa77ff801aa819461f0f5ff44546370bd7) = 4,

[ 1004](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfae7f7b3f7233bb5cf600338b4a2c601c0) [PD\_EXT\_BATTERY\_CAP](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfae7f7b3f7233bb5cf600338b4a2c601c0) = 5,

[ 1006](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfac8fc4c3c64fb3eaba8cb61bd999c7033) [PD\_EXT\_GET\_MANUFACTURER\_INFO](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfac8fc4c3c64fb3eaba8cb61bd999c7033) = 6,

[ 1008](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa500d77f178123eab8073058dd9308ea6) [PD\_EXT\_MANUFACTURER\_INFO](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa500d77f178123eab8073058dd9308ea6) = 7,

[ 1010](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa0f62aa3774995018514dcd2f75ac1c1f) [PD\_EXT\_SECURITY\_REQUEST](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa0f62aa3774995018514dcd2f75ac1c1f) = 8,

[ 1012](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfad002882e8bce9cdfdb0864cd6a3e79a7) [PD\_EXT\_SECURITY\_RESPONSE](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfad002882e8bce9cdfdb0864cd6a3e79a7) = 9,

[ 1014](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa2a7b6a78cf3fd87a86f060f927b566af) [PD\_EXT\_FIRMWARE\_UPDATE\_REQUEST](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa2a7b6a78cf3fd87a86f060f927b566af) = 10,

[ 1016](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa4fe2d7028fa2bdf594cb8c87ac05fe67) [PD\_EXT\_FIRMWARE\_UPDATE\_RESPONSE](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa4fe2d7028fa2bdf594cb8c87ac05fe67) = 11,

[ 1018](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa7d04da3fdb96eac97200d11eb2dbe083) [PD\_EXT\_PPS\_STATUS](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa7d04da3fdb96eac97200d11eb2dbe083) = 12,

[ 1020](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfaa21adc92574ed1261b6c13df3592601b) [PD\_EXT\_COUNTRY\_INFO](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfaa21adc92574ed1261b6c13df3592601b) = 13,

[ 1022](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfae69b4a8ddba29bc6cd69d50c946bc658) [PD\_EXT\_COUNTRY\_CODES](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfae69b4a8ddba29bc6cd69d50c946bc658) = 14,

1023

1024 /\*8 15-31 Reserved \*/

1025};

1026

[ 1030](group__usb__power__delivery.md#gaee2fe2128557939404c62e8104269bbf)enum [usbpd\_cc\_pin](group__usb__power__delivery.md#gaee2fe2128557939404c62e8104269bbf) {

[ 1032](group__usb__power__delivery.md#ggaee2fe2128557939404c62e8104269bbfa59a0ed05c4e99acebaa11080dbbe7694) [USBPD\_CC\_PIN\_1](group__usb__power__delivery.md#ggaee2fe2128557939404c62e8104269bbfa59a0ed05c4e99acebaa11080dbbe7694) = 0,

[ 1034](group__usb__power__delivery.md#ggaee2fe2128557939404c62e8104269bbfa53a0a6ba0212b9cbb407522e7f35648e) [USBPD\_CC\_PIN\_2](group__usb__power__delivery.md#ggaee2fe2128557939404c62e8104269bbfa53a0a6ba0212b9cbb407522e7f35648e) = 1,

1035};

1036

[ 1040](structpd__msg.md)struct [pd\_msg](structpd__msg.md) {

[ 1042](structpd__msg.md#af9f676afd2c2824fb9f01a08d8339231) enum [pd\_packet\_type](group__usb__power__delivery.md#gad2df13a24f0365198d37b10af608376b) [type](structpd__msg.md#af9f676afd2c2824fb9f01a08d8339231);

[ 1044](structpd__msg.md#ae6f1fa8a1fb006e3d90e75cd834e6d05) union [pd\_header](unionpd__header.md) [header](structpd__msg.md#ae6f1fa8a1fb006e3d90e75cd834e6d05);

[ 1046](structpd__msg.md#aa03ec4ce6d2f0d16a829394ff0ed2688) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structpd__msg.md#aa03ec4ce6d2f0d16a829394ff0ed2688);

[ 1048](structpd__msg.md#ad6fd282617b5f6dfeeef6cf4598883ee) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structpd__msg.md#ad6fd282617b5f6dfeeef6cf4598883ee)[[PD\_MAX\_EXTENDED\_MSG\_LEN](group__usb__power__delivery.md#gabdb041542baaf2277e054dd9e3928b16)];

1049};

1050

1054

1055#ifdef \_\_cplusplus

1056}

1057#endif

1058

1059#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_PD\_H\_ \*/

[pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328)

pdo\_type

Power Data Object Type Table 6-7 Power Data Object.

**Definition** usbc\_pd.h:382

[pd\_ext\_msg\_type](group__usb__power__delivery.md#ga457308d50365e0a2440e94e41a316cbf)

pd\_ext\_msg\_type

Extended message type for REV 3.0 See Table 6-48 Extended Message Types.

**Definition** usbc\_pd.h:992

[pd\_frs\_type](group__usb__power__delivery.md#ga48b33240e19524ea003052103d310358)

pd\_frs\_type

Fast Role Swap Required for USB Type-C current.

**Definition** usbc\_pd.h:459

[pd\_ctrl\_msg\_type](group__usb__power__delivery.md#ga4c7862a3e953fb22534123223c942f9a)

pd\_ctrl\_msg\_type

Control Message type See Table 6-5 Control Message Types.

**Definition** usbc\_pd.h:904

[pd\_data\_msg\_type](group__usb__power__delivery.md#ga8239651864b4cb0e1fc89ba2d7e59462)

pd\_data\_msg\_type

Data message type See Table 6-6 Data Message Types.

**Definition** usbc\_pd.h:962

[pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700)

pd\_rev\_type

Protocol revision.

**Definition** usbc\_pd.h:859

[PD\_MAX\_EXTENDED\_MSG\_LEN](group__usb__power__delivery.md#gabdb041542baaf2277e054dd9e3928b16)

#define PD\_MAX\_EXTENDED\_MSG\_LEN

Maximum length of an Extended Message in bytes.

**Definition** usbc\_pd.h:42

[pd\_packet\_type](group__usb__power__delivery.md#gad2df13a24f0365198d37b10af608376b)

pd\_packet\_type

Power Delivery packet type See USB Type-C Port Controller Interface Specification,...

**Definition** usbc\_pd.h:873

[usbpd\_cc\_pin](group__usb__power__delivery.md#gaee2fe2128557939404c62e8104269bbf)

usbpd\_cc\_pin

Active PD CC pin.

**Definition** usbc\_pd.h:1030

[PDO\_VARIABLE](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328a1726efca9ece0ff017cc4aaf05ce9624)

@ PDO\_VARIABLE

Variable Supply (non-Battery).

**Definition** usbc\_pd.h:388

[PDO\_BATTERY](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328a63f4fb7a4d2f7e265fd49be07966fbaa)

@ PDO\_BATTERY

Battery.

**Definition** usbc\_pd.h:386

[PDO\_AUGMENTED](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328adb8478434cc1622e98bc22f4081dff1e)

@ PDO\_AUGMENTED

Augmented Power Data Object (APDO).

**Definition** usbc\_pd.h:390

[PD\_EXT\_SECURITY\_REQUEST](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa0f62aa3774995018514dcd2f75ac1c1f)

@ PD\_EXT\_SECURITY\_REQUEST

Security\_Request Message.

**Definition** usbc\_pd.h:1010

[PD\_EXT\_FIRMWARE\_UPDATE\_REQUEST](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa2a7b6a78cf3fd87a86f060f927b566af)

@ PD\_EXT\_FIRMWARE\_UPDATE\_REQUEST

Firmware\_Update\_Request Message.

**Definition** usbc\_pd.h:1014

[PD\_EXT\_FIRMWARE\_UPDATE\_RESPONSE](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa4fe2d7028fa2bdf594cb8c87ac05fe67)

@ PD\_EXT\_FIRMWARE\_UPDATE\_RESPONSE

Firmware\_Update\_Response Message.

**Definition** usbc\_pd.h:1016

[PD\_EXT\_MANUFACTURER\_INFO](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa500d77f178123eab8073058dd9308ea6)

@ PD\_EXT\_MANUFACTURER\_INFO

Manufacturer\_Info Message.

**Definition** usbc\_pd.h:1008

[PD\_EXT\_SOURCE\_CAP](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa51c03e44c3fe1bb59445bbc452ea7199)

@ PD\_EXT\_SOURCE\_CAP

0 Reserved

**Definition** usbc\_pd.h:996

[PD\_EXT\_GET\_BATTERY\_STATUS](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa77ff801aa819461f0f5ff44546370bd7)

@ PD\_EXT\_GET\_BATTERY\_STATUS

Get\_Battery\_Status Message.

**Definition** usbc\_pd.h:1002

[PD\_EXT\_PPS\_STATUS](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa7d04da3fdb96eac97200d11eb2dbe083)

@ PD\_EXT\_PPS\_STATUS

PPS\_Status Message.

**Definition** usbc\_pd.h:1018

[PD\_EXT\_STATUS](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa836130da5307aed6160deadadf2f4f3f)

@ PD\_EXT\_STATUS

Status Message.

**Definition** usbc\_pd.h:998

[PD\_EXT\_GET\_BATTERY\_CAP](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa9c50488735d7723c3cc30f176c221e40)

@ PD\_EXT\_GET\_BATTERY\_CAP

Get\_Battery\_Cap Message.

**Definition** usbc\_pd.h:1000

[PD\_EXT\_COUNTRY\_INFO](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfaa21adc92574ed1261b6c13df3592601b)

@ PD\_EXT\_COUNTRY\_INFO

Country\_Codes Message.

**Definition** usbc\_pd.h:1020

[PD\_EXT\_GET\_MANUFACTURER\_INFO](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfac8fc4c3c64fb3eaba8cb61bd999c7033)

@ PD\_EXT\_GET\_MANUFACTURER\_INFO

Get\_Manufacturer\_Info Message.

**Definition** usbc\_pd.h:1006

[PD\_EXT\_SECURITY\_RESPONSE](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfad002882e8bce9cdfdb0864cd6a3e79a7)

@ PD\_EXT\_SECURITY\_RESPONSE

Security\_Response Message.

**Definition** usbc\_pd.h:1012

[PD\_EXT\_COUNTRY\_CODES](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfae69b4a8ddba29bc6cd69d50c946bc658)

@ PD\_EXT\_COUNTRY\_CODES

Country\_Info Message.

**Definition** usbc\_pd.h:1022

[PD\_EXT\_BATTERY\_CAP](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfae7f7b3f7233bb5cf600338b4a2c601c0)

@ PD\_EXT\_BATTERY\_CAP

Battery\_Capabilities Message.

**Definition** usbc\_pd.h:1004

[FRS\_DEFAULT\_USB\_POWER](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358a4cd44f89f225f8869bfd901e7ea79aed)

@ FRS\_DEFAULT\_USB\_POWER

Default USB Power.

**Definition** usbc\_pd.h:463

[FRS\_3P0A\_5V](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358a99ab2afc15809b5e89e3fb7106be37ba)

@ FRS\_3P0A\_5V

3.0A @ 5V

**Definition** usbc\_pd.h:467

[FRS\_1P5A\_5V](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358acac5008ded87d7a20b0b3b272075e4c1)

@ FRS\_1P5A\_5V

1.5A @ 5V

**Definition** usbc\_pd.h:465

[FRS\_NOT\_SUPPORTED](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358acbf2bf3ae21ff1ea51d7fd2b823ce726)

@ FRS\_NOT\_SUPPORTED

Fast Swap not supported.

**Definition** usbc\_pd.h:461

[PD\_CTRL\_DATA\_RESET](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa03f9886881aa493fb0f9bfac16713e7a)

@ PD\_CTRL\_DATA\_RESET

Used for REV 3.0.

**Definition** usbc\_pd.h:937

[PD\_CTRL\_FR\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa1c597b5f953e6e1791aa869025b98b24)

@ PD\_CTRL\_FR\_SWAP

FR\_Swap Message.

**Definition** usbc\_pd.h:947

[PD\_CTRL\_GET\_STATUS](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa23287276ee22241906828515f38fedef)

@ PD\_CTRL\_GET\_STATUS

Get\_Status Message.

**Definition** usbc\_pd.h:945

[PD\_CTRL\_DATA\_RESET\_COMPLETE](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa27caca37f9522045bc8612f7536cd792)

@ PD\_CTRL\_DATA\_RESET\_COMPLETE

Data\_Reset\_Complete Message.

**Definition** usbc\_pd.h:939

[PD\_CTRL\_WAIT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa3b6fc49b1ae0bb343d39476350b59c90)

@ PD\_CTRL\_WAIT

Wait Message.

**Definition** usbc\_pd.h:930

[PD\_CTRL\_DR\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa4aba967f7e363dbbadcc9a9ecf0c7ae4)

@ PD\_CTRL\_DR\_SWAP

DR\_Swap Message.

**Definition** usbc\_pd.h:924

[PD\_CTRL\_GOTO\_MIN](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa4ba7f63cdcbe766a34047e06145a591e)

@ PD\_CTRL\_GOTO\_MIN

GotoMin Message.

**Definition** usbc\_pd.h:910

[PD\_CTRL\_ACCEPT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa56df68ed627b56bbcfc20900ec5d2e5d)

@ PD\_CTRL\_ACCEPT

Accept Message.

**Definition** usbc\_pd.h:912

[PD\_CTRL\_GET\_COUNTRY\_CODES](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa677ebc41b4b67de6ee93b5e446af702e)

@ PD\_CTRL\_GET\_COUNTRY\_CODES

Get\_Country\_Codes Message.

**Definition** usbc\_pd.h:951

[PD\_CTRL\_VCONN\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa68820e99ce9c1c73180734372e5ede2b)

@ PD\_CTRL\_VCONN\_SWAP

VCONN\_Swap Message.

**Definition** usbc\_pd.h:928

[PD\_CTRL\_PING](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa8177040ca8a1f71dde67fc59060c35ed)

@ PD\_CTRL\_PING

Ping Message.

**Definition** usbc\_pd.h:916

[PD\_CTRL\_GET\_SOURCE\_CAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa9324307526500683ae265e9cb0063929)

@ PD\_CTRL\_GET\_SOURCE\_CAP

Get\_Source\_Cap Message.

**Definition** usbc\_pd.h:920

[PD\_CTRL\_REJECT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa9dd7b559e78a99639056325a7be14d81)

@ PD\_CTRL\_REJECT

Reject Message.

**Definition** usbc\_pd.h:914

[PD\_CTRL\_GET\_SINK\_CAP\_EXT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aaaa0a5bba9a9f1573952141c4f8f77318)

@ PD\_CTRL\_GET\_SINK\_CAP\_EXT

Get\_Sink\_Cap\_Extended Message.

**Definition** usbc\_pd.h:953

[PD\_CTRL\_GET\_SINK\_CAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aaaf5c221569a9108bdbc36545dcb37495)

@ PD\_CTRL\_GET\_SINK\_CAP

Get\_Sink\_Cap Message.

**Definition** usbc\_pd.h:922

[PD\_CTRL\_GET\_SOURCE\_CAP\_EXT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aab0ca2628b144d092116b461703176eaa)

@ PD\_CTRL\_GET\_SOURCE\_CAP\_EXT

Get\_Source\_Cap\_Extended Message.

**Definition** usbc\_pd.h:943

[PD\_CTRL\_GET\_PPS\_STATUS](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aab82efb96b1f8f7dae3c76e362ae1715a)

@ PD\_CTRL\_GET\_PPS\_STATUS

Get\_PPS\_Status Message.

**Definition** usbc\_pd.h:949

[PD\_CTRL\_NOT\_SUPPORTED](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aabfea5fdf0263fdf4c924bd603ee7256f)

@ PD\_CTRL\_NOT\_SUPPORTED

Not\_Supported Message.

**Definition** usbc\_pd.h:941

[PD\_CTRL\_PR\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aade67c4fb153e5ba87b6d6643f99260f9)

@ PD\_CTRL\_PR\_SWAP

PR\_Swap Message.

**Definition** usbc\_pd.h:926

[PD\_CTRL\_SOFT\_RESET](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aadeb12ed01ec54ee55588bfb796dd0c11)

@ PD\_CTRL\_SOFT\_RESET

Soft Reset Message.

**Definition** usbc\_pd.h:932

[PD\_CTRL\_GOOD\_CRC](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aae0895be53e5a1e54731e9608a8e0c6c9)

@ PD\_CTRL\_GOOD\_CRC

0 Reserved

**Definition** usbc\_pd.h:908

[PD\_CTRL\_PS\_RDY](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aafc449fc3dc39f2495494507cc97f53ad)

@ PD\_CTRL\_PS\_RDY

PS\_RDY Message.

**Definition** usbc\_pd.h:918

[PD\_DATA\_ENTER\_USB](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a1a0829560f9f82182f7587fd8787a846)

@ PD\_DATA\_ENTER\_USB

8-14 Reserved for REV 3.0

**Definition** usbc\_pd.h:983

[PD\_DATA\_SINK\_CAP](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a4cf30dcbce3fdf8076713e45d242b39a)

@ PD\_DATA\_SINK\_CAP

Sink Capabilities Message.

**Definition** usbc\_pd.h:972

[PD\_DATA\_BIST](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a7c4bc907fb81082da05c64797854be9f)

@ PD\_DATA\_BIST

BIST Message.

**Definition** usbc\_pd.h:970

[PD\_DATA\_ALERT](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a7e3368e1c7bde4c6bb3136cb80209bb6)

@ PD\_DATA\_ALERT

Alert Message.

**Definition** usbc\_pd.h:976

[PD\_DATA\_GET\_COUNTRY\_INFO](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a83d7098236e97972cf24b900f7e5e069)

@ PD\_DATA\_GET\_COUNTRY\_INFO

Get Country Info Message.

**Definition** usbc\_pd.h:978

[PD\_DATA\_VENDOR\_DEF](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a881fcbc2dc5f8b1de7c97522df46242d)

@ PD\_DATA\_VENDOR\_DEF

Vendor Defined Message.

**Definition** usbc\_pd.h:985

[PD\_DATA\_BATTERY\_STATUS](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad493f01ffc4c3c164f874eb202f8adb0)

@ PD\_DATA\_BATTERY\_STATUS

5-14 Reserved for REV 2.0

**Definition** usbc\_pd.h:974

[PD\_DATA\_SOURCE\_CAP](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad9a0cf16cfa852111ea0ed3434b35dfc)

@ PD\_DATA\_SOURCE\_CAP

0 Reserved

**Definition** usbc\_pd.h:966

[PD\_DATA\_REQUEST](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad9c920f987e2578b030cc08f2e69998a)

@ PD\_DATA\_REQUEST

Request Message.

**Definition** usbc\_pd.h:968

[PD\_REV10](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700a1d9b4c553f44dccdc67e4edb554557b9)

@ PD\_REV10

PD revision 1.0.

**Definition** usbc\_pd.h:861

[PD\_REV20](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700a22c122b1d30a3ab96fffd5dfa6bfb9ae)

@ PD\_REV20

PD revision 2.0.

**Definition** usbc\_pd.h:863

[PD\_REV30](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700af3770bcbcf6feaaab272c022d7a57c7a)

@ PD\_REV30

PD revision 3.0.

**Definition** usbc\_pd.h:865

[PD\_PACKET\_SOP](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba0bede6a56c24b06fdf56cf1dc386bb14)

@ PD\_PACKET\_SOP

Port Partner message.

**Definition** usbc\_pd.h:875

[PD\_PACKET\_DEBUG\_PRIME\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1)

@ PD\_PACKET\_DEBUG\_PRIME\_PRIME

Currently undefined in the PD specification.

**Definition** usbc\_pd.h:883

[PD\_PACKET\_CABLE\_RESET](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba531ebc6013984b81e6fb550618d6b4a8)

@ PD\_PACKET\_CABLE\_RESET

Cable Reset message to the Cable.

**Definition** usbc\_pd.h:887

[PD\_PACKET\_MSG\_INVALID](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba55bb88e5955992170bee96ddbe8a7437)

@ PD\_PACKET\_MSG\_INVALID

USED ONLY FOR RECEPTION OF UNKNOWN MSG TYPES.

**Definition** usbc\_pd.h:892

[PD\_PACKET\_PRIME\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba5ecd663a9eecefcf965f605125d5188c)

@ PD\_PACKET\_PRIME\_PRIME

Cable Plug message far end.

**Definition** usbc\_pd.h:879

[PD\_PACKET\_DEBUG\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba63b2200ebaf016d06437f3586d15171d)

@ PD\_PACKET\_DEBUG\_PRIME

Currently undefined in the PD specification.

**Definition** usbc\_pd.h:881

[PD\_PACKET\_TX\_HARD\_RESET](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376baa5cd066e86fd55727c3625cd16633f73)

@ PD\_PACKET\_TX\_HARD\_RESET

Hard Reset message to the Port Partner.

**Definition** usbc\_pd.h:885

[PD\_PACKET\_SOP\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376bae3a5f99242ab24a34706170101b38ef8)

@ PD\_PACKET\_SOP\_PRIME

Cable Plug message.

**Definition** usbc\_pd.h:877

[PD\_PACKET\_TX\_BIST\_MODE\_2](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376bafcd21cc6b1ae6c58b86c0619d687e8fc)

@ PD\_PACKET\_TX\_BIST\_MODE\_2

BIST\_MODE\_2 message to the Port Partner.

**Definition** usbc\_pd.h:889

[USBPD\_CC\_PIN\_2](group__usb__power__delivery.md#ggaee2fe2128557939404c62e8104269bbfa53a0a6ba0212b9cbb407522e7f35648e)

@ USBPD\_CC\_PIN\_2

PD is active on CC2.

**Definition** usbc\_pd.h:1034

[USBPD\_CC\_PIN\_1](group__usb__power__delivery.md#ggaee2fe2128557939404c62e8104269bbfa59a0ed05c4e99acebaa11080dbbe7694)

@ USBPD\_CC\_PIN\_1

PD is active on CC1.

**Definition** usbc\_pd.h:1032

[types.h](include_2zephyr_2types_8h.md)

[PDO\_FIXED](pd_8h.md#a9fa615ab7f38385c21277d4e9e6a1441)

#define PDO\_FIXED(mv, ma, flags)

**Definition** pd.h:38

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[pd\_msg](structpd__msg.md)

Power Delivery message.

**Definition** usbc\_pd.h:1040

[pd\_msg::len](structpd__msg.md#aa03ec4ce6d2f0d16a829394ff0ed2688)

uint32\_t len

Length of bytes in data.

**Definition** usbc\_pd.h:1046

[pd\_msg::data](structpd__msg.md#ad6fd282617b5f6dfeeef6cf4598883ee)

uint8\_t data[260]

Message data.

**Definition** usbc\_pd.h:1048

[pd\_msg::header](structpd__msg.md#ae6f1fa8a1fb006e3d90e75cd834e6d05)

union pd\_header header

Header of this message.

**Definition** usbc\_pd.h:1044

[pd\_msg::type](structpd__msg.md#af9f676afd2c2824fb9f01a08d8339231)

enum pd\_packet\_type type

Type of this packet.

**Definition** usbc\_pd.h:1042

[pd\_augmented\_supply\_pdo\_sink](unionpd__augmented__supply__pdo__sink.md)

Create Augmented Supply PDO Sink value See Table 6-17 Programmable Power Supply APDO - Sink.

**Definition** usbc\_pd.h:698

[pd\_augmented\_supply\_pdo\_sink::max\_current](unionpd__augmented__supply__pdo__sink.md#a0a5da0df48dff5fae42159026c91c7af)

uint32\_t max\_current

Maximum Current in 50mA increments.

**Definition** usbc\_pd.h:701

[pd\_augmented\_supply\_pdo\_sink::reserved3](unionpd__augmented__supply__pdo__sink.md#a22e63fa7e83af25d9822dcf3d9b35f40)

uint32\_t reserved3

00b – Programmable Power Supply 01b…11b - Reserved, Shall Not be used Setting as reserved because it ...

**Definition** usbc\_pd.h:717

[pd\_augmented\_supply\_pdo\_sink::reserved1](unionpd__augmented__supply__pdo__sink.md#a2f1f6094af7449619ab626476fa51698)

uint32\_t reserved1

Reserved – Shall be set to zero.

**Definition** usbc\_pd.h:707

[pd\_augmented\_supply\_pdo\_sink::reserved0](unionpd__augmented__supply__pdo__sink.md#a3320455a4c7673d3db95f585b07cc319)

uint32\_t reserved0

Reserved – Shall be set to zero.

**Definition** usbc\_pd.h:703

[pd\_augmented\_supply\_pdo\_sink::min\_voltage](unionpd__augmented__supply__pdo__sink.md#ad83710136d9dcad3644ec36c1eee9cb0)

uint32\_t min\_voltage

Minimum Voltage in 100mV increments.

**Definition** usbc\_pd.h:705

[pd\_augmented\_supply\_pdo\_sink::type](unionpd__augmented__supply__pdo__sink.md#ad9d2fe810bd3959b99b38180c93a71c0)

enum pdo\_type type

Augmented Power Data Object (APDO).

**Definition** usbc\_pd.h:719

[pd\_augmented\_supply\_pdo\_sink::reserved2](unionpd__augmented__supply__pdo__sink.md#adfa0b8ab656255cfecc9ca5e1ee05d49)

uint32\_t reserved2

Reserved – Shall be set to zero.

**Definition** usbc\_pd.h:711

[pd\_augmented\_supply\_pdo\_sink::raw\_value](unionpd__augmented__supply__pdo__sink.md#ae28a74642ffcdf1100f37e3542e1ca96)

uint32\_t raw\_value

Raw PDO value.

**Definition** usbc\_pd.h:722

[pd\_augmented\_supply\_pdo\_sink::max\_voltage](unionpd__augmented__supply__pdo__sink.md#af5eca8ab38a3eaaaecd10cdc1092ce3c)

uint32\_t max\_voltage

Maximum Voltage in 100mV increments.

**Definition** usbc\_pd.h:709

[pd\_augmented\_supply\_pdo\_source](unionpd__augmented__supply__pdo__source.md)

Create Augmented Supply PDO Source value See Table 6-13 Programmable Power Supply APDO - Source.

**Definition** usbc\_pd.h:665

[pd\_augmented\_supply\_pdo\_source::raw\_value](unionpd__augmented__supply__pdo__source.md#a093a674e538dcc2541ff86f50d0156df)

uint32\_t raw\_value

Raw PDO value.

**Definition** usbc\_pd.h:691

[pd\_augmented\_supply\_pdo\_source::min\_voltage](unionpd__augmented__supply__pdo__source.md#a56e1af2acda73fee7e40449b7c39745d)

uint32\_t min\_voltage

Minimum Voltage in 100mV increments.

**Definition** usbc\_pd.h:672

[pd\_augmented\_supply\_pdo\_source::max\_current](unionpd__augmented__supply__pdo__source.md#a7ef0b26951ce2683c9c4ca0f19b73d6d)

uint32\_t max\_current

Maximum Current in 50mA increments.

**Definition** usbc\_pd.h:668

[pd\_augmented\_supply\_pdo\_source::reserved3](unionpd__augmented__supply__pdo__source.md#aa59ad8a8eb4e2343c14bbe54937aa93d)

uint32\_t reserved3

00b – Programmable Power Supply 01b…11b - Reserved, Shall Not be used Setting as reserved because it ...

**Definition** usbc\_pd.h:686

[pd\_augmented\_supply\_pdo\_source::type](unionpd__augmented__supply__pdo__source.md#aaea2842b628bde92bb74ab0eb7d5aad4)

enum pdo\_type type

Augmented Power Data Object (APDO).

**Definition** usbc\_pd.h:688

[pd\_augmented\_supply\_pdo\_source::reserved2](unionpd__augmented__supply__pdo__source.md#ab5868f6ba91821d56ddb419e895a05fa)

uint32\_t reserved2

Reserved – Shall be set to zero.

**Definition** usbc\_pd.h:678

[pd\_augmented\_supply\_pdo\_source::max\_voltage](unionpd__augmented__supply__pdo__source.md#aba6df91a8c5da92517f885fa89af8747)

uint32\_t max\_voltage

Maximum Voltage in 100mV increments.

**Definition** usbc\_pd.h:676

[pd\_augmented\_supply\_pdo\_source::pps\_power\_limited](unionpd__augmented__supply__pdo__source.md#abfac34ee5da0b1700b784c7bfe925c19)

uint32\_t pps\_power\_limited

PPS Power Limited.

**Definition** usbc\_pd.h:680

[pd\_augmented\_supply\_pdo\_source::reserved0](unionpd__augmented__supply__pdo__source.md#ac046ddf128416ecbb8f3a26185d03e03)

uint32\_t reserved0

Reserved – Shall be set to zero.

**Definition** usbc\_pd.h:670

[pd\_augmented\_supply\_pdo\_source::reserved1](unionpd__augmented__supply__pdo__source.md#ae79eb7473040058c0b8572cfe4fa4dce)

uint32\_t reserved1

Reserved – Shall be set to zero.

**Definition** usbc\_pd.h:674

[pd\_battery\_supply\_pdo\_sink](unionpd__battery__supply__pdo__sink.md)

Create a Battery Supply PDO Sink value See Table 6-16 Battery Supply PDO - Sink.

**Definition** usbc\_pd.h:618

[pd\_battery\_supply\_pdo\_sink::operational\_power](unionpd__battery__supply__pdo__sink.md#a3f1072c4ca168aaedd13257f01f410aa)

uint32\_t operational\_power

Operational Power in 250mW units.

**Definition** usbc\_pd.h:621

[pd\_battery\_supply\_pdo\_sink::min\_voltage](unionpd__battery__supply__pdo__sink.md#a5a588a46ae8bef2dc10445c2f5422246)

uint32\_t min\_voltage

Minimum Voltage in 50mV units.

**Definition** usbc\_pd.h:623

[pd\_battery\_supply\_pdo\_sink::max\_voltage](unionpd__battery__supply__pdo__sink.md#a858efb23a0c143917b88e5596b899c79)

uint32\_t max\_voltage

Maximum Voltage in 50mV units.

**Definition** usbc\_pd.h:625

[pd\_battery\_supply\_pdo\_sink::raw\_value](unionpd__battery__supply__pdo__sink.md#aa973b26972c1e1a96c7e0c09dbed08f3)

uint32\_t raw\_value

Raw PDO value.

**Definition** usbc\_pd.h:630

[pd\_battery\_supply\_pdo\_sink::type](unionpd__battery__supply__pdo__sink.md#acb8b674a789f0a5b397d7ab93d443543)

enum pdo\_type type

Battery supply.

**Definition** usbc\_pd.h:627

[pd\_battery\_supply\_pdo\_source](unionpd__battery__supply__pdo__source.md)

Create a Battery Supply PDO Source value See Table 6-12 Battery Supply PDO - Source.

**Definition** usbc\_pd.h:599

[pd\_battery\_supply\_pdo\_source::max\_power](unionpd__battery__supply__pdo__source.md#a00ea9931d839cf83b56513f77aa7d5b9)

uint32\_t max\_power

Maximum Allowable Power in 250mW units.

**Definition** usbc\_pd.h:602

[pd\_battery\_supply\_pdo\_source::raw\_value](unionpd__battery__supply__pdo__source.md#a1e775dc0082b531216c154724be360b0)

uint32\_t raw\_value

Raw PDO value.

**Definition** usbc\_pd.h:611

[pd\_battery\_supply\_pdo\_source::max\_voltage](unionpd__battery__supply__pdo__source.md#a673ea076da8810bc694b2dc82bbede67)

uint32\_t max\_voltage

Maximum Voltage in 50mV units.

**Definition** usbc\_pd.h:606

[pd\_battery\_supply\_pdo\_source::type](unionpd__battery__supply__pdo__source.md#ab546fd1a6caa77a57b5d5420a8ee31d7)

enum pdo\_type type

Battery supply.

**Definition** usbc\_pd.h:608

[pd\_battery\_supply\_pdo\_source::min\_voltage](unionpd__battery__supply__pdo__source.md#afa2335788e7fde01b90afd95bccf6d5f)

uint32\_t min\_voltage

Minimum Voltage in 50mV units.

**Definition** usbc\_pd.h:604

[pd\_ext\_header](unionpd__ext__header.md)

Build an extended message header See Table 6-3 Extended Message Header.

**Definition** usbc\_pd.h:351

[pd\_ext\_header::chunked](unionpd__ext__header.md#a180ccc6854c1341e638ca338e6eb1cd8)

uint16\_t chunked

1 for chunked messages

**Definition** usbc\_pd.h:362

[pd\_ext\_header::request\_chunk](unionpd__ext__header.md#a36a65a1e52875721758d1273b0e76279)

uint16\_t request\_chunk

1 for a chunked message, else 0

**Definition** usbc\_pd.h:358

[pd\_ext\_header::data\_size](unionpd__ext__header.md#a4a7a948d3463ddfbebf1d75faeda293e)

uint16\_t data\_size

Number of total bytes in data block.

**Definition** usbc\_pd.h:354

[pd\_ext\_header::raw\_value](unionpd__ext__header.md#a8a1d0f0d38b3a5c4aa3a80586e7a1e8f)

uint16\_t raw\_value

Raw PD Ext Header value.

**Definition** usbc\_pd.h:365

[pd\_ext\_header::reserved0](unionpd__ext__header.md#aae09d0399c0a121e3c216047e908b9ec)

uint16\_t reserved0

Reserved.

**Definition** usbc\_pd.h:356

[pd\_ext\_header::chunk\_number](unionpd__ext__header.md#aced0489c4e2462652c0d91187c07b27e)

uint16\_t chunk\_number

Chunk number when chkd = 1, else 0.

**Definition** usbc\_pd.h:360

[pd\_fixed\_supply\_pdo\_sink](unionpd__fixed__supply__pdo__sink.md)

Create a Fixed Supply PDO Sink value See Table 6-14 Fixed Supply PDO - Sink.

**Definition** usbc\_pd.h:474

[pd\_fixed\_supply\_pdo\_sink::usb\_comms\_capable](unionpd__fixed__supply__pdo__sink.md#a0559272067e2d0c33f52274fb59ea18d)

uint32\_t usb\_comms\_capable

USB Communications Capable.

**Definition** usbc\_pd.h:487

[pd\_fixed\_supply\_pdo\_sink::reserved0](unionpd__fixed__supply__pdo__sink.md#a22f9763652560dbd215324f1bb878a96)

uint32\_t reserved0

Reserved – Shall be set to zero.

**Definition** usbc\_pd.h:481

[pd\_fixed\_supply\_pdo\_sink::operational\_current](unionpd__fixed__supply__pdo__sink.md#a2ac4005b0cf3e28ade8f508d2c6f5e20)

uint32\_t operational\_current

Operational Current in 10mA units.

**Definition** usbc\_pd.h:477

[pd\_fixed\_supply\_pdo\_sink::higher\_capability](unionpd__fixed__supply__pdo__sink.md#a3086d57313f05b8bc91fb3590e51c657)

uint32\_t higher\_capability

Higher Capability.

**Definition** usbc\_pd.h:491

[pd\_fixed\_supply\_pdo\_sink::dual\_role\_data](unionpd__fixed__supply__pdo__sink.md#a5c6bfb21c4d8e70a04895dd31a58885e)

uint32\_t dual\_role\_data

Dual-Role Data.

**Definition** usbc\_pd.h:485

[pd\_fixed\_supply\_pdo\_sink::frs\_required](unionpd__fixed__supply__pdo__sink.md#a7138e45345fc2cd486186190f11e847d)

enum pd\_frs\_type frs\_required

Fast Role Swap required USB Type-C Current.

**Definition** usbc\_pd.h:483

[pd\_fixed\_supply\_pdo\_sink::dual\_role\_power](unionpd__fixed__supply__pdo__sink.md#aad255dbee3452bf3276464c59f113cb2)

uint32\_t dual\_role\_power

Dual-Role Power.

**Definition** usbc\_pd.h:493

[pd\_fixed\_supply\_pdo\_sink::unconstrained\_power](unionpd__fixed__supply__pdo__sink.md#ab406f1f36e5fe6f7acb9abc91991a803)

uint32\_t unconstrained\_power

Unconstrained Power.

**Definition** usbc\_pd.h:489

[pd\_fixed\_supply\_pdo\_sink::voltage](unionpd__fixed__supply__pdo__sink.md#ac47dcf98dfca90eb0e6013a3e1c5eb18)

uint32\_t voltage

Voltage in 50mV units.

**Definition** usbc\_pd.h:479

[pd\_fixed\_supply\_pdo\_sink::type](unionpd__fixed__supply__pdo__sink.md#ac505fdd24064de98c5c17088b2c88c5c)

enum pdo\_type type

Fixed supply.

**Definition** usbc\_pd.h:495

[pd\_fixed\_supply\_pdo\_sink::raw\_value](unionpd__fixed__supply__pdo__sink.md#aebdeb854bcac0d20efcbe3be56dcc9f8)

uint32\_t raw\_value

Raw PDO value.

**Definition** usbc\_pd.h:498

[pd\_fixed\_supply\_pdo\_source](unionpd__fixed__supply__pdo__source.md)

Create a Fixed Supply PDO Source value See Table 6-9 Fixed Supply PDO - Source.

**Definition** usbc\_pd.h:427

[pd\_fixed\_supply\_pdo\_source::type](unionpd__fixed__supply__pdo__source.md#a111b87e88b4f78e60b78d35dfbcbc307)

enum pdo\_type type

Fixed supply.

**Definition** usbc\_pd.h:450

[pd\_fixed\_supply\_pdo\_source::peak\_current](unionpd__fixed__supply__pdo__source.md#a2c4b27407245da04b67e9524173d39bc)

uint32\_t peak\_current

Peak Current.

**Definition** usbc\_pd.h:434

[pd\_fixed\_supply\_pdo\_source::unchunked\_ext\_msg\_supported](unionpd__fixed__supply__pdo__source.md#a440ff92d2bd533e3ddd6c65f9ac21772)

uint32\_t unchunked\_ext\_msg\_supported

Unchunked Extended Messages Supported.

**Definition** usbc\_pd.h:438

[pd\_fixed\_supply\_pdo\_source::usb\_suspend\_supported](unionpd__fixed__supply__pdo__source.md#a55003edba55a920a386cc04cbc7a72a0)

uint32\_t usb\_suspend\_supported

USB Suspend Supported.

**Definition** usbc\_pd.h:446

[pd\_fixed\_supply\_pdo\_source::voltage](unionpd__fixed__supply__pdo__source.md#a66f55e177b6f2bc76b392707e39fa4fe)

uint32\_t voltage

Voltage in 50mV units.

**Definition** usbc\_pd.h:432

[pd\_fixed\_supply\_pdo\_source::reserved0](unionpd__fixed__supply__pdo__source.md#a6b0e04acd43c9b18bd1dea80508a8817)

uint32\_t reserved0

Reserved – Shall be set to zero.

**Definition** usbc\_pd.h:436

[pd\_fixed\_supply\_pdo\_source::usb\_comms\_capable](unionpd__fixed__supply__pdo__source.md#a6c1bcf37a1fc9a348cf19e16fbe01dac)

uint32\_t usb\_comms\_capable

USB Communications Capable.

**Definition** usbc\_pd.h:442

[pd\_fixed\_supply\_pdo\_source::dual\_role\_data](unionpd__fixed__supply__pdo__source.md#a7b89666e3753966001caf7602c796147)

uint32\_t dual\_role\_data

Dual-Role Data.

**Definition** usbc\_pd.h:440

[pd\_fixed\_supply\_pdo\_source::max\_current](unionpd__fixed__supply__pdo__source.md#a86664d945f65f19f7b96da1148700640)

uint32\_t max\_current

Maximum Current in 10mA units.

**Definition** usbc\_pd.h:430

[pd\_fixed\_supply\_pdo\_source::raw\_value](unionpd__fixed__supply__pdo__source.md#a9227629f6c97357b71ea20e4e0572cf2)

uint32\_t raw\_value

Raw PDO value.

**Definition** usbc\_pd.h:453

[pd\_fixed\_supply\_pdo\_source::unconstrained\_power](unionpd__fixed__supply__pdo__source.md#a9fc10f3ec4126c063f5dd99e8f3e2723)

uint32\_t unconstrained\_power

Unconstrained Power.

**Definition** usbc\_pd.h:444

[pd\_fixed\_supply\_pdo\_source::dual\_role\_power](unionpd__fixed__supply__pdo__source.md#af96673f1ac078436a9eca0973e1bdef9)

uint32\_t dual\_role\_power

Dual-Role Power.

**Definition** usbc\_pd.h:448

[pd\_header](unionpd__header.md)

Build a PD message header See Table 6-1 Message Header.

**Definition** usbc\_pd.h:320

[pd\_header::port\_power\_role](unionpd__header.md#a20ac99d9738c9d278a78e8ccfc401902)

uint16\_t port\_power\_role

Port Power Role.

**Definition** usbc\_pd.h:329

[pd\_header::extended](unionpd__header.md#a5750b964c12c3bc2d2523a64cb9eb7d0)

uint16\_t extended

Extended Message.

**Definition** usbc\_pd.h:335

[pd\_header::number\_of\_data\_objects](unionpd__header.md#a63d89119f0918ba7d6eb9e01fa1ed406)

uint16\_t number\_of\_data\_objects

Number of Data Objects.

**Definition** usbc\_pd.h:333

[pd\_header::message\_type](unionpd__header.md#a70768acc6a6bc9ebb9249df7ed635a94)

uint16\_t message\_type

Type of message.

**Definition** usbc\_pd.h:323

[pd\_header::specification\_revision](unionpd__header.md#a85cce1728afe0d62bb29f618a1cf70e1)

uint16\_t specification\_revision

Specification Revision.

**Definition** usbc\_pd.h:327

[pd\_header::message\_id](unionpd__header.md#ae4a0a5695e73fd3e1b7e3f38cd2a758c)

uint16\_t message\_id

Message ID.

**Definition** usbc\_pd.h:331

[pd\_header::port\_data\_role](unionpd__header.md#af1b027c9c57497421117b290dcb6ac66)

uint16\_t port\_data\_role

Port Data role.

**Definition** usbc\_pd.h:325

[pd\_header::raw\_value](unionpd__header.md#afa6c6699be5fe95bcb4962396e33e35d)

uint16\_t raw\_value

**Definition** usbc\_pd.h:337

[pd\_rdo](unionpd__rdo.md)

The Request Data Object (RDO) Shall be returned by the Sink making a request for power.

**Definition** usbc\_pd.h:730

[pd\_rdo::fixed](unionpd__rdo.md#a0b7502c79b0976b8e0d118cae3950191)

struct pd\_rdo::@135007244246051072022174114066235300347325324272 fixed

Create a Fixed RDO value See Table 6-19 Fixed and Variable Request Data Object.

[pd\_rdo::usb\_comm\_capable](unionpd__rdo.md#a30f6044378cad6f277f8694df5611230)

uint32\_t usb\_comm\_capable

USB Communications Capable.

**Definition** usbc\_pd.h:753

[pd\_rdo::min\_or\_max\_operating\_current](unionpd__rdo.md#a41d023e9308e6d252f0bc8412a6c6184)

uint32\_t min\_or\_max\_operating\_current

Operating Current 10mA units NOTE: If Give Back Flag is zero, this field is the Maximum Operating Cur...

**Definition** usbc\_pd.h:743

[pd\_rdo::raw\_value](unionpd__rdo.md#a477cf38b68b9386e950c085a1ce4f336)

uint32\_t raw\_value

Raw RDO value.

**Definition** usbc\_pd.h:853

[pd\_rdo::battery](unionpd__rdo.md#a5838022e249981be50aee897c16ce56e)

struct pd\_rdo::@354331025254103020047350074060370065104054344136 battery

Create a Battery RDO value See Table 6-20 Battery Request Data Object.

[pd\_rdo::reserved2](unionpd__rdo.md#a5f8b64ce53d9881a007405a986b6b490)

uint32\_t reserved2

Reserved - Shall be set to zero.

**Definition** usbc\_pd.h:846

[pd\_rdo::operating\_power](unionpd__rdo.md#a63dd2a9e94f3a61205b95efc0cf79f13)

uint32\_t operating\_power

Operating power in 250mW units.

**Definition** usbc\_pd.h:805

[pd\_rdo::variable](unionpd__rdo.md#a82e1adf30b6fc476b794b94cfb379214)

struct pd\_rdo::@053333353216342225047121275130116114021106304351 variable

Create a Variable RDO value See Table 6-19 Fixed and Variable Request Data Object.

[pd\_rdo::operating\_current](unionpd__rdo.md#a8c11df4b75772cda511bd94e5a297128)

uint32\_t operating\_current

Operating current in 10mA units.

**Definition** usbc\_pd.h:745

[pd\_rdo::reserved3](unionpd__rdo.md#aa0ddbfb3c345b671f97d4b4e760168b4)

uint32\_t reserved3

Reserved - Shall be set to zero.

**Definition** usbc\_pd.h:850

[pd\_rdo::reserved1](unionpd__rdo.md#aa5af5685e6d9c3d8a7ec3a40d25b43ba)

uint32\_t reserved1

Reserved - Shall be set to zero.

**Definition** usbc\_pd.h:761

[pd\_rdo::reserved0](unionpd__rdo.md#ab4065aee18c3a68df38592122f607343)

uint32\_t reserved0

Reserved - Shall be set to zero.

**Definition** usbc\_pd.h:747

[pd\_rdo::min\_operating\_power](unionpd__rdo.md#ab59da7098c1d33c9269f66dd3ac3fc5b)

uint32\_t min\_operating\_power

Minimum Operating Power in 250mW units.

**Definition** usbc\_pd.h:803

[pd\_rdo::augmented](unionpd__rdo.md#ad6b45a879e689dcd05bf9e07aedc4d20)

struct pd\_rdo::@171266220200335172314343047176050247370270336321 augmented

Create an Augmented RDO value See Table 6-22 Programmable Request Data Object.

[pd\_rdo::output\_voltage](unionpd__rdo.md#ad7a98411aad054f1161b4ce32ef3ee33)

uint32\_t output\_voltage

Output Voltage in 20mV units.

**Definition** usbc\_pd.h:834

[pd\_rdo::giveback](unionpd__rdo.md#ae5ae5d3c823254ab895becc3b01761fe)

uint32\_t giveback

Give Back Flag.

**Definition** usbc\_pd.h:757

[pd\_rdo::unchunked\_ext\_msg\_supported](unionpd__rdo.md#ae71e9abde3d69211c7bcfc7b80d18c41)

uint32\_t unchunked\_ext\_msg\_supported

Unchunked Extended Messages Supported.

**Definition** usbc\_pd.h:749

[pd\_rdo::no\_usb\_suspend](unionpd__rdo.md#ae90a23cc166373f7bb3c35be0c3967f2)

uint32\_t no\_usb\_suspend

No USB Suspend.

**Definition** usbc\_pd.h:751

[pd\_rdo::cap\_mismatch](unionpd__rdo.md#afd24863b120085c57e77b8d246effd54)

uint32\_t cap\_mismatch

Capability Mismatch.

**Definition** usbc\_pd.h:755

[pd\_rdo::object\_pos](unionpd__rdo.md#aff1b20a6e4905ac714ab5e7af7ff9593)

uint32\_t object\_pos

Object Position (000b is Reserved and Shall Not be used).

**Definition** usbc\_pd.h:759

[pd\_variable\_supply\_pdo\_sink](unionpd__variable__supply__pdo__sink.md)

Create a Variable Supply PDO Sink value See Table 6-15 Variable Supply (non-Battery) PDO - Sink.

**Definition** usbc\_pd.h:552

[pd\_variable\_supply\_pdo\_sink::raw\_value](unionpd__variable__supply__pdo__sink.md#a2ff80c049f98ab090b100b7f9877bffb)

uint32\_t raw\_value

Raw PDO value.

**Definition** usbc\_pd.h:564

[pd\_variable\_supply\_pdo\_sink::type](unionpd__variable__supply__pdo__sink.md#a4a09b8b5e2397925d5a433917378193e)

enum pdo\_type type

Variable supply.

**Definition** usbc\_pd.h:561

[pd\_variable\_supply\_pdo\_sink::min\_voltage](unionpd__variable__supply__pdo__sink.md#aaaa1cf3f08208966fb00093f910f70ab)

uint32\_t min\_voltage

Minimum Voltage in 50mV units.

**Definition** usbc\_pd.h:557

[pd\_variable\_supply\_pdo\_sink::operational\_current](unionpd__variable__supply__pdo__sink.md#ad648f2400a495b37d8b9f995556419d0)

uint32\_t operational\_current

operational Current in 10mA units

**Definition** usbc\_pd.h:555

[pd\_variable\_supply\_pdo\_sink::max\_voltage](unionpd__variable__supply__pdo__sink.md#ae360e7c2335a4f6cf5d267c8c82fdc45)

uint32\_t max\_voltage

Maximum Voltage in 50mV units.

**Definition** usbc\_pd.h:559

[pd\_variable\_supply\_pdo\_source](unionpd__variable__supply__pdo__source.md)

Create a Variable Supply PDO Source value See Table 6-11 Variable Supply (non-Battery) PDO - Source.

**Definition** usbc\_pd.h:533

[pd\_variable\_supply\_pdo\_source::max\_voltage](unionpd__variable__supply__pdo__source.md#a008cf5201ea6d3e238d547b738570c45)

uint32\_t max\_voltage

Maximum Voltage in 50mV units.

**Definition** usbc\_pd.h:540

[pd\_variable\_supply\_pdo\_source::type](unionpd__variable__supply__pdo__source.md#a5da7eb69fc69a58662f09690fba92633)

enum pdo\_type type

Variable supply.

**Definition** usbc\_pd.h:542

[pd\_variable\_supply\_pdo\_source::min\_voltage](unionpd__variable__supply__pdo__source.md#a67d86c71997a7c0605b8a199cd51c920)

uint32\_t min\_voltage

Minimum Voltage in 50mV units.

**Definition** usbc\_pd.h:538

[pd\_variable\_supply\_pdo\_source::max\_current](unionpd__variable__supply__pdo__source.md#a8193ca96084db5901bb30195113ff01f)

uint32\_t max\_current

Maximum Current in 10mA units.

**Definition** usbc\_pd.h:536

[pd\_variable\_supply\_pdo\_source::raw\_value](unionpd__variable__supply__pdo__source.md#af00512126f128bf1cf31e802652af1bf)

uint32\_t raw\_value

Raw PDO value.

**Definition** usbc\_pd.h:545

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [usbc\_pd.h](usbc__pd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
