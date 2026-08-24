---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/bluetooth_2uuid_8h_source.html
original_path: doxygen/html/bluetooth_2uuid_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uuid.h

[Go to the documentation of this file.](bluetooth_2uuid_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_UUID\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_UUID\_H\_

12

19

20#include <stddef.h>

21#include <[stdint.h](stdint_8h.md)>

22

23#include <[zephyr/sys/util.h](sys_2util_8h.md)>

24#include <[zephyr/bluetooth/byteorder.h](bluetooth_2byteorder_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

31enum {

[ 33](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a8a5a0c5b6310aff10b182daec0e452ba) [BT\_UUID\_TYPE\_16](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a8a5a0c5b6310aff10b182daec0e452ba),

[ 35](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a27382df27b8098bf6144021c1b23c4c8) [BT\_UUID\_TYPE\_32](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a27382df27b8098bf6144021c1b23c4c8),

[ 37](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a786cbb74a1d74c77cb31ff3c4da45517) [BT\_UUID\_TYPE\_128](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a786cbb74a1d74c77cb31ff3c4da45517),

38};

39

[ 41](group__bt__uuid.md#ga9d3506fd135b5cd8763446f572c161da)#define BT\_UUID\_SIZE\_16 2

42

[ 44](group__bt__uuid.md#gaf35f2e5054bfcc81985e90b8ef659fd9)#define BT\_UUID\_SIZE\_32 4

45

[ 47](group__bt__uuid.md#ga86fdce8e63c0f8208bea6b0f2584eb67)#define BT\_UUID\_SIZE\_128 16

48

[ 50](structbt__uuid.md)struct [bt\_uuid](structbt__uuid.md) {

[ 51](structbt__uuid.md#abac3a8b54416cbd89ff55f8f82902dcb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__uuid.md#abac3a8b54416cbd89ff55f8f82902dcb);

52};

53

[ 54](structbt__uuid__16.md)struct [bt\_uuid\_16](structbt__uuid__16.md) {

[ 56](structbt__uuid__16.md#a08f8a5e0eadf1ef2c4c917a5dd3db191) struct [bt\_uuid](structbt__uuid.md) [uuid](structbt__uuid__16.md#a08f8a5e0eadf1ef2c4c917a5dd3db191);

[ 58](structbt__uuid__16.md#a13ee02ec58cf5fdede249aa8b20a1a9a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [val](structbt__uuid__16.md#a13ee02ec58cf5fdede249aa8b20a1a9a);

59};

60

[ 61](structbt__uuid__32.md)struct [bt\_uuid\_32](structbt__uuid__32.md) {

[ 63](structbt__uuid__32.md#ae37fff06890b200895d559ef42d454e2) struct [bt\_uuid](structbt__uuid.md) [uuid](structbt__uuid__32.md#ae37fff06890b200895d559ef42d454e2);

[ 65](structbt__uuid__32.md#a56e991966643c9a1ca689986e57e6bfc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [val](structbt__uuid__32.md#a56e991966643c9a1ca689986e57e6bfc);

66};

67

[ 68](structbt__uuid__128.md)struct [bt\_uuid\_128](structbt__uuid__128.md) {

[ 70](structbt__uuid__128.md#a3b8fd8a362ed8fd9eabcfa5bffa9eeee) struct [bt\_uuid](structbt__uuid.md) [uuid](structbt__uuid__128.md#a3b8fd8a362ed8fd9eabcfa5bffa9eeee);

[ 72](structbt__uuid__128.md#a0918addaa7afaf1eeb864d5ec40bd59a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [val](structbt__uuid__128.md#a0918addaa7afaf1eeb864d5ec40bd59a)[[BT\_UUID\_SIZE\_128](group__bt__uuid.md#ga86fdce8e63c0f8208bea6b0f2584eb67)];

73};

74

[ 79](group__bt__uuid.md#gab7c9f80628c5fb1b5d1c09d18a1baff7)#define BT\_UUID\_INIT\_16(value) \

80{ \

81 .uuid = { BT\_UUID\_TYPE\_16 }, \

82 .val = (value), \

83}

84

[ 89](group__bt__uuid.md#ga207ff52ebf1eea1c487fff3d840a38f8)#define BT\_UUID\_INIT\_32(value) \

90{ \

91 .uuid = { BT\_UUID\_TYPE\_32 }, \

92 .val = (value), \

93}

94

[ 101](group__bt__uuid.md#ga1a840adf4bc06cf2cd5dbeb0c868374b)#define BT\_UUID\_INIT\_128(value...) \

102{ \

103 .uuid = { BT\_UUID\_TYPE\_128 }, \

104 .val = { value }, \

105}

106

[ 113](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)#define BT\_UUID\_DECLARE\_16(value) \

114 ((const struct bt\_uuid \*) ((const struct bt\_uuid\_16[]) {BT\_UUID\_INIT\_16(value)}))

115

[ 122](group__bt__uuid.md#ga945448449c57b4800e25a363e7d4d1cc)#define BT\_UUID\_DECLARE\_32(value) \

123 ((const struct bt\_uuid \*) ((const struct bt\_uuid\_32[]) {BT\_UUID\_INIT\_32(value)}))

124

[ 133](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)#define BT\_UUID\_DECLARE\_128(value...) \

134 ((const struct bt\_uuid \*) ((const struct bt\_uuid\_128[]) {BT\_UUID\_INIT\_128(value)}))

135

[ 137](group__bt__uuid.md#ga7466cf356741d6348f332653a385fd01)#define BT\_UUID\_16(\_\_u) CONTAINER\_OF(\_\_u, struct bt\_uuid\_16, uuid)

138

[ 140](group__bt__uuid.md#gacc77f082e8dac620672676ed8d005504)#define BT\_UUID\_32(\_\_u) CONTAINER\_OF(\_\_u, struct bt\_uuid\_32, uuid)

141

[ 143](group__bt__uuid.md#ga931a0d5eb23537be31408c787fd8b48d)#define BT\_UUID\_128(\_\_u) CONTAINER\_OF(\_\_u, struct bt\_uuid\_128, uuid)

144

[ 178](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)#define BT\_UUID\_128\_ENCODE(w32, w1, w2, w3, w48) \

179 BT\_BYTES\_LIST\_LE48(w48),\

180 BT\_BYTES\_LIST\_LE16(w3), \

181 BT\_BYTES\_LIST\_LE16(w2), \

182 BT\_BYTES\_LIST\_LE16(w1), \

183 BT\_BYTES\_LIST\_LE32(w32)

184

[ 200](group__bt__uuid.md#ga16e057af1bb2f1c11e74b50bfd490586)#define BT\_UUID\_16\_ENCODE(w16) BT\_BYTES\_LIST\_LE16(w16)

201

[ 217](group__bt__uuid.md#gad5294c1c19c66b20321c88939a8849bf)#define BT\_UUID\_32\_ENCODE(w32) BT\_BYTES\_LIST\_LE32(w32)

218

[ 226](group__bt__uuid.md#gaf9a36381128454102c558568dfd5d029)#define BT\_UUID\_STR\_LEN 37

227

[ 231](group__bt__uuid.md#gaaf6715d89ba70a057949e636fb2368dd)#define BT\_UUID\_GAP\_VAL 0x1800

[ 235](group__bt__uuid.md#gae8b61f07e6732ffb876318045b5803c4)#define BT\_UUID\_GAP \

236 BT\_UUID\_DECLARE\_16(BT\_UUID\_GAP\_VAL)

237

[ 240](group__bt__uuid.md#gad893036bda14523c3e35ff66d23bacb2)#define BT\_UUID\_GATT\_VAL 0x1801

[ 244](group__bt__uuid.md#ga18f210e4e60b9fdd80d9d68f007b0728)#define BT\_UUID\_GATT \

245 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_VAL)

246

[ 249](group__bt__uuid.md#ga637aece6581426d8d5d7b9aeb546a67e)#define BT\_UUID\_IAS\_VAL 0x1802

[ 253](group__bt__uuid.md#ga9d99491d2957912ab80e2636d6ac7416)#define BT\_UUID\_IAS \

254 BT\_UUID\_DECLARE\_16(BT\_UUID\_IAS\_VAL)

255

[ 258](group__bt__uuid.md#ga1b868ca21fa47aba88601f71eb8ad1d5)#define BT\_UUID\_LLS\_VAL 0x1803

[ 262](group__bt__uuid.md#ga6bdab3bba88af7187eb50b7817cc317e)#define BT\_UUID\_LLS \

263 BT\_UUID\_DECLARE\_16(BT\_UUID\_LLS\_VAL)

264

[ 267](group__bt__uuid.md#gab8d79e7553b418eae94b9d790d9a422e)#define BT\_UUID\_TPS\_VAL 0x1804

[ 271](group__bt__uuid.md#ga2e250a6880be716f98e668ab26dcdac3)#define BT\_UUID\_TPS \

272 BT\_UUID\_DECLARE\_16(BT\_UUID\_TPS\_VAL)

273

[ 276](group__bt__uuid.md#ga264f3b58d4e3bee6a7533acf0670206d)#define BT\_UUID\_CTS\_VAL 0x1805

[ 280](group__bt__uuid.md#ga8c2c089f4cc458c0f4a5a7506c21a6f9)#define BT\_UUID\_CTS \

281 BT\_UUID\_DECLARE\_16(BT\_UUID\_CTS\_VAL)

282

[ 285](group__bt__uuid.md#ga13300d9d1074fd90a65233357dd9ad60)#define BT\_UUID\_RTUS\_VAL 0x1806

[ 289](group__bt__uuid.md#ga52c98d18473e61c581f0cab4839defa8)#define BT\_UUID\_RTUS \

290 BT\_UUID\_DECLARE\_16(BT\_UUID\_RTUS\_VAL)

291

[ 294](group__bt__uuid.md#ga0396837f73209e12bc6d11c64a3a6d67)#define BT\_UUID\_NDSTS\_VAL 0x1807

[ 298](group__bt__uuid.md#ga3a4f846cbf5dd4fccec26be00506a61c)#define BT\_UUID\_NDSTS \

299 BT\_UUID\_DECLARE\_16(BT\_UUID\_NDSTS\_VAL)

300

[ 303](group__bt__uuid.md#gab31578ab529cf755ec611c491a3676ac)#define BT\_UUID\_GS\_VAL 0x1808

[ 307](group__bt__uuid.md#gac1f5583a48b80fab9d05546d87cb6de0)#define BT\_UUID\_GS \

308 BT\_UUID\_DECLARE\_16(BT\_UUID\_GS\_VAL)

309

[ 312](group__bt__uuid.md#ga3caec4c6564711a2959ffadcf5598011)#define BT\_UUID\_HTS\_VAL 0x1809

[ 316](group__bt__uuid.md#gabffa5a0a0a57cfd330a8bef348c2c2ee)#define BT\_UUID\_HTS \

317 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTS\_VAL)

318

[ 321](group__bt__uuid.md#ga3eaf1d7bfeb9b9375e1e2b4ba7f23aed)#define BT\_UUID\_DIS\_VAL 0x180a

[ 325](group__bt__uuid.md#ga03ea74768fa1e69dad54cffe9eeeee31)#define BT\_UUID\_DIS \

326 BT\_UUID\_DECLARE\_16(BT\_UUID\_DIS\_VAL)

327

[ 330](group__bt__uuid.md#ga66870ecd34acfee828d55f63167b7e67)#define BT\_UUID\_NAS\_VAL 0x180b

[ 334](group__bt__uuid.md#ga92af25a46ae1b534fa248fd0516278cb)#define BT\_UUID\_NAS \

335 BT\_UUID\_DECLARE\_16(BT\_UUID\_NAS\_VAL)

336

[ 339](group__bt__uuid.md#ga110066c42ffc45bf86a9c90528aeb2e7)#define BT\_UUID\_WDS\_VAL 0x180c

[ 343](group__bt__uuid.md#ga7c501f33b29907d48dd31ed70eeb67d4)#define BT\_UUID\_WDS \

344 BT\_UUID\_DECLARE\_16(BT\_UUID\_WDS\_VAL)

345

[ 348](group__bt__uuid.md#ga912cb91295d110813a3db0144c95551d)#define BT\_UUID\_HRS\_VAL 0x180d

[ 352](group__bt__uuid.md#ga17893ceaa9bc20640d4ecdeabe9beb28)#define BT\_UUID\_HRS \

353 BT\_UUID\_DECLARE\_16(BT\_UUID\_HRS\_VAL)

354

[ 357](group__bt__uuid.md#gaea47ecf9bc957d813312a188a701db54)#define BT\_UUID\_PAS\_VAL 0x180e

[ 361](group__bt__uuid.md#gadd5233cc3cb516f8b7fb192d6c64bcad)#define BT\_UUID\_PAS \

362 BT\_UUID\_DECLARE\_16(BT\_UUID\_PAS\_VAL)

363

[ 366](group__bt__uuid.md#ga2ff64c18d7f8dae8a328b52f486161c4)#define BT\_UUID\_BAS\_VAL 0x180f

[ 370](group__bt__uuid.md#gabc55390a1144b556477df555e76848ab)#define BT\_UUID\_BAS \

371 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_VAL)

372

[ 375](group__bt__uuid.md#ga2ff98d3bfd27cba7eb99c62dfb31a6fd)#define BT\_UUID\_BPS\_VAL 0x1810

[ 379](group__bt__uuid.md#ga97ed88c10cdc3f1c32c4e53d260eaa3e)#define BT\_UUID\_BPS \

380 BT\_UUID\_DECLARE\_16(BT\_UUID\_BPS\_VAL)

381

[ 384](group__bt__uuid.md#ga0c6ee900cba57e40f8b3681e1ea404c7)#define BT\_UUID\_ANS\_VAL 0x1811

[ 388](group__bt__uuid.md#ga7a208b147e3b35857c72ba8f8db22d62)#define BT\_UUID\_ANS \

389 BT\_UUID\_DECLARE\_16(BT\_UUID\_ANS\_VAL)

390

[ 393](group__bt__uuid.md#ga2bf2ec6082e31f397dec6634cda56bbb)#define BT\_UUID\_HIDS\_VAL 0x1812

[ 397](group__bt__uuid.md#ga74e91eef3e2dcbb4499a0f70f3b479d4)#define BT\_UUID\_HIDS \

398 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_VAL)

399

[ 402](group__bt__uuid.md#ga73e7ff27e935868fa86c9d38e186e405)#define BT\_UUID\_SPS\_VAL 0x1813

[ 406](group__bt__uuid.md#ga7599a7a3cdc6a32c60862618b6b70327)#define BT\_UUID\_SPS \

407 BT\_UUID\_DECLARE\_16(BT\_UUID\_SPS\_VAL)

408

[ 411](group__bt__uuid.md#gad35b23e0814f0f74c3a33587f7922966)#define BT\_UUID\_RSCS\_VAL 0x1814

[ 415](group__bt__uuid.md#ga40a6402510b5c71b0eca5b2f7a914085)#define BT\_UUID\_RSCS \

416 BT\_UUID\_DECLARE\_16(BT\_UUID\_RSCS\_VAL)

417

[ 420](group__bt__uuid.md#ga4449d49abf6fed72da52b14a967aec4d)#define BT\_UUID\_AIOS\_VAL 0x1815

[ 424](group__bt__uuid.md#gaaa73f77971aad79900e18fd58d12ea22)#define BT\_UUID\_AIOS \

425 BT\_UUID\_DECLARE\_16(BT\_UUID\_AIOS\_VAL)

426

[ 429](group__bt__uuid.md#ga4d31b6944d378bcda7c8f7bfc74c5692)#define BT\_UUID\_CSC\_VAL 0x1816

[ 433](group__bt__uuid.md#ga6514fa0098d12c02aa34c18e1e5a6396)#define BT\_UUID\_CSC \

434 BT\_UUID\_DECLARE\_16(BT\_UUID\_CSC\_VAL)

435

[ 438](group__bt__uuid.md#gab063c1e5d2773927ce54c1745c7134d4)#define BT\_UUID\_CPS\_VAL 0x1818

[ 442](group__bt__uuid.md#gac3c2895467ba651b8ebad709fdd44f6d)#define BT\_UUID\_CPS \

443 BT\_UUID\_DECLARE\_16(BT\_UUID\_CPS\_VAL)

444

[ 447](group__bt__uuid.md#ga36161c4e68b691cfb6a9f691a8f693dd)#define BT\_UUID\_LNS\_VAL 0x1819

[ 451](group__bt__uuid.md#gac48ea20cb0503dd748862862157e9224)#define BT\_UUID\_LNS \

452 BT\_UUID\_DECLARE\_16(BT\_UUID\_LNS\_VAL)

453

[ 456](group__bt__uuid.md#ga8e8d24d0bf0a49713bbfa93cc2bdb0da)#define BT\_UUID\_ESS\_VAL 0x181a

[ 460](group__bt__uuid.md#ga96c5958372c4fdba211b4f74d342a5b3)#define BT\_UUID\_ESS \

461 BT\_UUID\_DECLARE\_16(BT\_UUID\_ESS\_VAL)

462

[ 465](group__bt__uuid.md#ga69baa896cd558487733cd575a6193e0d)#define BT\_UUID\_BCS\_VAL 0x181b

[ 469](group__bt__uuid.md#ga08170da6b471e937f64de6943b6e24bb)#define BT\_UUID\_BCS \

470 BT\_UUID\_DECLARE\_16(BT\_UUID\_BCS\_VAL)

471

[ 474](group__bt__uuid.md#ga035ee545fdd640745b3bcbd8b7e7b3b6)#define BT\_UUID\_UDS\_VAL 0x181c

[ 478](group__bt__uuid.md#gac6edbd84e5f0b454e130f835a32f1a44)#define BT\_UUID\_UDS \

479 BT\_UUID\_DECLARE\_16(BT\_UUID\_UDS\_VAL)

480

[ 483](group__bt__uuid.md#ga6b6566f914d2c92c9b1bb4efd6efee98)#define BT\_UUID\_WSS\_VAL 0x181d

[ 487](group__bt__uuid.md#gaa5c518578e2620aafad915a0291dfe8f)#define BT\_UUID\_WSS \

488 BT\_UUID\_DECLARE\_16(BT\_UUID\_WSS\_VAL)

489

[ 492](group__bt__uuid.md#ga399ffbd6e7d3e50010383f2d521d8089)#define BT\_UUID\_BMS\_VAL 0x181e

[ 496](group__bt__uuid.md#ga0a91114bf5e53c894d10d1e432223714)#define BT\_UUID\_BMS \

497 BT\_UUID\_DECLARE\_16(BT\_UUID\_BMS\_VAL)

498

[ 501](group__bt__uuid.md#ga9726266ed3399a646999e19f639457a7)#define BT\_UUID\_CGMS\_VAL 0x181f

[ 505](group__bt__uuid.md#ga04767d3a7461b3508bce584704d92c75)#define BT\_UUID\_CGMS \

506 BT\_UUID\_DECLARE\_16(BT\_UUID\_CGMS\_VAL)

507

[ 510](group__bt__uuid.md#gad8cc687442abd5eea3e367d2b859e2e8)#define BT\_UUID\_IPSS\_VAL 0x1820

[ 514](group__bt__uuid.md#ga32f10a8bfb452aee43c64eec3c2d5a0f)#define BT\_UUID\_IPSS \

515 BT\_UUID\_DECLARE\_16(BT\_UUID\_IPSS\_VAL)

516

[ 519](group__bt__uuid.md#ga8fafd81c36f6b515d2709d5f4efd9d00)#define BT\_UUID\_IPS\_VAL 0x1821

[ 523](group__bt__uuid.md#ga8dac7b88922315a2af06ad70cdfcfd0c)#define BT\_UUID\_IPS \

524 BT\_UUID\_DECLARE\_16(BT\_UUID\_IPS\_VAL)

525

[ 528](group__bt__uuid.md#gabfb8333e3fb8e819f02601ace836687b)#define BT\_UUID\_POS\_VAL 0x1822

[ 532](group__bt__uuid.md#gaa713f38e63cfc998559c862f80f2380b)#define BT\_UUID\_POS \

533 BT\_UUID\_DECLARE\_16(BT\_UUID\_POS\_VAL)

534

[ 537](group__bt__uuid.md#ga5f66d3e11dcde95c3c4e7055734c9aef)#define BT\_UUID\_HPS\_VAL 0x1823

[ 541](group__bt__uuid.md#gaade9071b49d238d13edf57e90655c41c)#define BT\_UUID\_HPS \

542 BT\_UUID\_DECLARE\_16(BT\_UUID\_HPS\_VAL)

543

[ 546](group__bt__uuid.md#gafafc31de7e0d06e831ef13f5ddb88685)#define BT\_UUID\_TDS\_VAL 0x1824

[ 550](group__bt__uuid.md#gaccdb682d8f53c8560bea355a5376d72d)#define BT\_UUID\_TDS \

551 BT\_UUID\_DECLARE\_16(BT\_UUID\_TDS\_VAL)

552

[ 555](group__bt__uuid.md#ga0a7a74bbb0c8bbd97d5fd6807deeb4c3)#define BT\_UUID\_OTS\_VAL 0x1825

[ 559](group__bt__uuid.md#ga4f18867b63edde824c1a57c0ee354282)#define BT\_UUID\_OTS \

560 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_VAL)

561

[ 564](group__bt__uuid.md#ga036c6c7b6589a7178851ff7004aa64db)#define BT\_UUID\_FMS\_VAL 0x1826

[ 568](group__bt__uuid.md#ga8935f33e5d388c96e38a172a5831b573)#define BT\_UUID\_FMS \

569 BT\_UUID\_DECLARE\_16(BT\_UUID\_FMS\_VAL)

570

[ 573](group__bt__uuid.md#gaa0bf05b5c11a3b6f9f0f8e48298b4776)#define BT\_UUID\_MESH\_PROV\_VAL 0x1827

[ 577](group__bt__uuid.md#ga665cc5a42b1b074536ce949fe1853f7b)#define BT\_UUID\_MESH\_PROV \

578 BT\_UUID\_DECLARE\_16(BT\_UUID\_MESH\_PROV\_VAL)

579

[ 582](group__bt__uuid.md#gaa347d1cf40b3eba7052c3e7c80e32a02)#define BT\_UUID\_MESH\_PROXY\_VAL 0x1828

[ 586](group__bt__uuid.md#ga34de82083c412e280bb585db519d70a2)#define BT\_UUID\_MESH\_PROXY \

587 BT\_UUID\_DECLARE\_16(BT\_UUID\_MESH\_PROXY\_VAL)

588

[ 591](group__bt__uuid.md#ga02eaaf8d7ec7981336713d4cb1ea6b6a)#define BT\_UUID\_MESH\_PROXY\_SOLICITATION\_VAL 0x1859

[ 595](group__bt__uuid.md#ga76f45a959cf7d4bb5b874ba2e2f8c5ad)#define BT\_UUID\_RCSRV\_VAL 0x1829

[ 599](group__bt__uuid.md#gafc39274d32d212b7b244f24809d00e15)#define BT\_UUID\_RCSRV \

600 BT\_UUID\_DECLARE\_16(BT\_UUID\_RCSRV\_VAL)

601

[ 604](group__bt__uuid.md#gac1069e0c1a650aa7659942f0533cb384)#define BT\_UUID\_IDS\_VAL 0x183a

[ 608](group__bt__uuid.md#gac3921b7c5c31423d7ac7ed4338ccf980)#define BT\_UUID\_IDS \

609 BT\_UUID\_DECLARE\_16(BT\_UUID\_IDS\_VAL)

610

[ 613](group__bt__uuid.md#gaa75f32c09a7f70c1b79fb7af1b50c0fe)#define BT\_UUID\_BSS\_VAL 0x183b

[ 617](group__bt__uuid.md#gacc9ac8d5418e857f70b7836629874296)#define BT\_UUID\_BSS \

618 BT\_UUID\_DECLARE\_16(BT\_UUID\_BSS\_VAL)

619

[ 622](group__bt__uuid.md#gabd1855b6ede9f8dcfa46b211ad7a33b5)#define BT\_UUID\_ECS\_VAL 0x183c

[ 626](group__bt__uuid.md#ga966e2b5ad06522d4a6e882755fc4dcbf)#define BT\_UUID\_ECS \

627 BT\_UUID\_DECLARE\_16(BT\_UUID\_ECS\_VAL)

628

[ 631](group__bt__uuid.md#ga72b1d17c97437e7ced4e1c7c3fb9d0cd)#define BT\_UUID\_ACLS\_VAL 0x183d

[ 635](group__bt__uuid.md#ga022390a0b44e81e0925e29a87fd4d1e3)#define BT\_UUID\_ACLS \

636 BT\_UUID\_DECLARE\_16(BT\_UUID\_ACLS\_VAL)

637

[ 640](group__bt__uuid.md#gaf85d03a7c42d040559874e6d1a6296a6)#define BT\_UUID\_PAMS\_VAL 0x183e

[ 644](group__bt__uuid.md#ga3c5590637fc3c90c4beed23bab9f5eb6)#define BT\_UUID\_PAMS \

645 BT\_UUID\_DECLARE\_16(BT\_UUID\_PAMS\_VAL)

646

[ 649](group__bt__uuid.md#ga67f3c417689d2a7af32e9bacaa274d44)#define BT\_UUID\_AICS\_VAL 0x1843

[ 653](group__bt__uuid.md#ga8e7ec38a733ebe33d9d1d525a7c2c051)#define BT\_UUID\_AICS \

654 BT\_UUID\_DECLARE\_16(BT\_UUID\_AICS\_VAL)

655

[ 658](group__bt__uuid.md#ga9de8d92b55a644904d5b7257608cba45)#define BT\_UUID\_VCS\_VAL 0x1844

[ 662](group__bt__uuid.md#gaaf797d6506d5f47e730e5bbf6ff79f7c)#define BT\_UUID\_VCS \

663 BT\_UUID\_DECLARE\_16(BT\_UUID\_VCS\_VAL)

664

[ 667](group__bt__uuid.md#ga78b30023b019279b2b9567d7c3ffeac2)#define BT\_UUID\_VOCS\_VAL 0x1845

[ 671](group__bt__uuid.md#ga2ab2f92985ca0f65fb066df57c2f1433)#define BT\_UUID\_VOCS \

672 BT\_UUID\_DECLARE\_16(BT\_UUID\_VOCS\_VAL)

673

[ 676](group__bt__uuid.md#ga5f2c25e1c3f14fb65f062dc34f56b3ed)#define BT\_UUID\_CSIS\_VAL 0x1846

[ 680](group__bt__uuid.md#ga111f2eb8e186444804b8b3c39f0f00a3)#define BT\_UUID\_CSIS \

681 BT\_UUID\_DECLARE\_16(BT\_UUID\_CSIS\_VAL)

682

[ 685](group__bt__uuid.md#gad8fc6ade8cafce1b9461de0a27389c88)#define BT\_UUID\_DTS\_VAL 0x1847

[ 689](group__bt__uuid.md#ga6417c327841fd7317515e394f5ac0089)#define BT\_UUID\_DTS \

690 BT\_UUID\_DECLARE\_16(BT\_UUID\_DTS\_VAL)

691

[ 694](group__bt__uuid.md#ga3cd2f717c107a3e8d65eb958155884fd)#define BT\_UUID\_MCS\_VAL 0x1848

[ 698](group__bt__uuid.md#ga7b84d0b301ce2f565de7eb89165af0cf)#define BT\_UUID\_MCS \

699 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_VAL)

700

[ 703](group__bt__uuid.md#ga35e8dae5a05985c10e3cdd610161ebcc)#define BT\_UUID\_GMCS\_VAL 0x1849

[ 707](group__bt__uuid.md#ga4efbadd4ce5a6fb64a5d9832b4626d0f)#define BT\_UUID\_GMCS \

708 BT\_UUID\_DECLARE\_16(BT\_UUID\_GMCS\_VAL)

709

[ 712](group__bt__uuid.md#ga9e7f780e9800abc6fa86fa034482df4b)#define BT\_UUID\_CTES\_VAL 0x184a

[ 716](group__bt__uuid.md#gaf85f0bff2abbe069d8d64a3eda2a066d)#define BT\_UUID\_CTES \

717 BT\_UUID\_DECLARE\_16(BT\_UUID\_CTES\_VAL)

718

[ 721](group__bt__uuid.md#gae25bb19fe3d92555a9c2c2de6fae5354)#define BT\_UUID\_TBS\_VAL 0x184b

[ 725](group__bt__uuid.md#ga70c7991e602fa8c87868cac63c838c21)#define BT\_UUID\_TBS \

726 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_VAL)

727

[ 730](group__bt__uuid.md#ga1e90e6d7a97ca28b842012f61b76a2cb)#define BT\_UUID\_GTBS\_VAL 0x184c

[ 734](group__bt__uuid.md#gabb0810fa80d5623a5af457a2fb02ca6e)#define BT\_UUID\_GTBS \

735 BT\_UUID\_DECLARE\_16(BT\_UUID\_GTBS\_VAL)

736

[ 739](group__bt__uuid.md#gac18fe10ee79d240af7c494fab0304d90)#define BT\_UUID\_MICS\_VAL 0x184d

[ 743](group__bt__uuid.md#ga411a51f52e6e63c905d86ce5b924e69c)#define BT\_UUID\_MICS \

744 BT\_UUID\_DECLARE\_16(BT\_UUID\_MICS\_VAL)

745

[ 748](group__bt__uuid.md#gaedc903cd915524adfa5d4d64fa38cf22)#define BT\_UUID\_ASCS\_VAL 0x184e

[ 752](group__bt__uuid.md#ga7d52614d936753738fb04f124c97fc09)#define BT\_UUID\_ASCS \

753 BT\_UUID\_DECLARE\_16(BT\_UUID\_ASCS\_VAL)

754

[ 757](group__bt__uuid.md#gaa671703a706fc97dcc9a4b1dd7f4fef3)#define BT\_UUID\_BASS\_VAL 0x184f

[ 761](group__bt__uuid.md#ga7d0e06ae7e089098ac9d0c32087d5803)#define BT\_UUID\_BASS \

762 BT\_UUID\_DECLARE\_16(BT\_UUID\_BASS\_VAL)

763

[ 766](group__bt__uuid.md#ga69dafd580d116dec74b54c818d5c275b)#define BT\_UUID\_PACS\_VAL 0x1850

[ 770](group__bt__uuid.md#ga86720eb2ad6aa3f66a9bf2248cb95383)#define BT\_UUID\_PACS \

771 BT\_UUID\_DECLARE\_16(BT\_UUID\_PACS\_VAL)

772

[ 775](group__bt__uuid.md#gaa1c0efca17e5b3de3c0fd254181a53db)#define BT\_UUID\_BASIC\_AUDIO\_VAL 0x1851

[ 779](group__bt__uuid.md#ga842f48f68be48c3379161b595fca22a2)#define BT\_UUID\_BASIC\_AUDIO \

780 BT\_UUID\_DECLARE\_16(BT\_UUID\_BASIC\_AUDIO\_VAL)

781

[ 784](group__bt__uuid.md#ga0c67f9e1a5fef34fd1fddc539e20119b)#define BT\_UUID\_BROADCAST\_AUDIO\_VAL 0x1852

[ 788](group__bt__uuid.md#gafe9b1d539a9c77037e0c8433b702790e)#define BT\_UUID\_BROADCAST\_AUDIO \

789 BT\_UUID\_DECLARE\_16(BT\_UUID\_BROADCAST\_AUDIO\_VAL)

790

[ 793](group__bt__uuid.md#gab3f48a2a32b3a2061f3b108350c59ec4)#define BT\_UUID\_CAS\_VAL 0x1853

[ 797](group__bt__uuid.md#gab69a851e430a0232abb839b0d9fc54e5)#define BT\_UUID\_CAS \

798 BT\_UUID\_DECLARE\_16(BT\_UUID\_CAS\_VAL)

799

[ 802](group__bt__uuid.md#ga8d937e82611aaa2da305795d00074c93)#define BT\_UUID\_HAS\_VAL 0x1854

[ 806](group__bt__uuid.md#gac5acaee5423acd4531768fbf8844676b)#define BT\_UUID\_HAS \

807 BT\_UUID\_DECLARE\_16(BT\_UUID\_HAS\_VAL)

808

[ 811](group__bt__uuid.md#ga42f0d2bf3ce4a258a6f9d14a828cf422)#define BT\_UUID\_TMAS\_VAL 0x1855

[ 815](group__bt__uuid.md#ga84ea43f70dee139497be28d90db70104)#define BT\_UUID\_TMAS \

816 BT\_UUID\_DECLARE\_16(BT\_UUID\_TMAS\_VAL)

817

[ 820](group__bt__uuid.md#ga06265a1d97c1b734340f9eb0055da913)#define BT\_UUID\_PBA\_VAL 0x1856

[ 824](group__bt__uuid.md#ga98f4f946c1bca483a7e81cad162ee0b1)#define BT\_UUID\_PBA \

825 BT\_UUID\_DECLARE\_16(BT\_UUID\_PBA\_VAL)

826

[ 829](group__bt__uuid.md#ga8244f6edaf3a347be1a3bf4e1d8fb4c3)#define BT\_UUID\_GATT\_PRIMARY\_VAL 0x2800

[ 833](group__bt__uuid.md#ga6e87ce1575494eb90358e074e8dbe276)#define BT\_UUID\_GATT\_PRIMARY \

834 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PRIMARY\_VAL)

835

[ 838](group__bt__uuid.md#ga764703eec266d58b0ea9e00d02f23d1d)#define BT\_UUID\_GATT\_SECONDARY\_VAL 0x2801

[ 842](group__bt__uuid.md#gad084d3658e663b6b8e200be256c54cdb)#define BT\_UUID\_GATT\_SECONDARY \

843 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SECONDARY\_VAL)

844

[ 847](group__bt__uuid.md#gaa493141bce2425fe40f809f151ace673)#define BT\_UUID\_GATT\_INCLUDE\_VAL 0x2802

[ 851](group__bt__uuid.md#ga995596ff7374ebcb44d4706bc16234e4)#define BT\_UUID\_GATT\_INCLUDE \

852 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_INCLUDE\_VAL)

853

[ 856](group__bt__uuid.md#gae8b1af5f3458ca8523db83a3d8ccc62c)#define BT\_UUID\_GATT\_CHRC\_VAL 0x2803

[ 860](group__bt__uuid.md#gadcedbbe1c432c4ac737e54b318e01a0f)#define BT\_UUID\_GATT\_CHRC \

861 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CHRC\_VAL)

862

[ 865](group__bt__uuid.md#ga68b7ae19aad514e4a6731796c34c59da)#define BT\_UUID\_GATT\_CEP\_VAL 0x2900

[ 869](group__bt__uuid.md#ga6aa143b721d810f1536d7431a9bf7cc7)#define BT\_UUID\_GATT\_CEP \

870 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CEP\_VAL)

871

[ 874](group__bt__uuid.md#ga2a168fa660bc6c3c3d5a85d99f2c9e60)#define BT\_UUID\_GATT\_CUD\_VAL 0x2901

[ 878](group__bt__uuid.md#gaaaf94f5d918a1b6715cf4816b03875a2)#define BT\_UUID\_GATT\_CUD \

879 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CUD\_VAL)

880

[ 883](group__bt__uuid.md#gaa7807cb9ed1aa19f48c7dc4904f52dbb)#define BT\_UUID\_GATT\_CCC\_VAL 0x2902

[ 887](group__bt__uuid.md#ga03a2d3f0ce89508b794d5c87a4303057)#define BT\_UUID\_GATT\_CCC \

888 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CCC\_VAL)

889

[ 892](group__bt__uuid.md#ga84cc4d600b5218baf5620b87cb8ddc55)#define BT\_UUID\_GATT\_SCC\_VAL 0x2903

[ 896](group__bt__uuid.md#ga82567cdce8c4411cd3daf26711ba9685)#define BT\_UUID\_GATT\_SCC \

897 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SCC\_VAL)

898

[ 901](group__bt__uuid.md#ga71924f95ca117ace35e64b0222bb5bf7)#define BT\_UUID\_GATT\_CPF\_VAL 0x2904

[ 905](group__bt__uuid.md#ga331a61702ffe9b15bac0de3d60414022)#define BT\_UUID\_GATT\_CPF \

906 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CPF\_VAL)

907

[ 910](group__bt__uuid.md#ga88dbd0deac028cb0df1a6bd1874aec7f)#define BT\_UUID\_GATT\_CAF\_VAL 0x2905

[ 914](group__bt__uuid.md#gadc590b4039c9f47965e88e57b5589a93)#define BT\_UUID\_GATT\_CAF \

915 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CAF\_VAL)

916

[ 919](group__bt__uuid.md#ga6fa0e8a8f2727e4646461ca14247466f)#define BT\_UUID\_VALID\_RANGE\_VAL 0x2906

[ 923](group__bt__uuid.md#gad53d373df905c4b11c39a3ae4284a6d1)#define BT\_UUID\_VALID\_RANGE \

924 BT\_UUID\_DECLARE\_16(BT\_UUID\_VALID\_RANGE\_VAL)

925

[ 928](group__bt__uuid.md#gaa8e06b1198ea23a01e892080df88e7f4)#define BT\_UUID\_HIDS\_EXT\_REPORT\_VAL 0x2907

[ 932](group__bt__uuid.md#gae945ad8eac1b444d92096c76239e106d)#define BT\_UUID\_HIDS\_EXT\_REPORT \

933 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_EXT\_REPORT\_VAL)

934

[ 937](group__bt__uuid.md#ga4c1f2a0f52f101910f9294b10b5af484)#define BT\_UUID\_HIDS\_REPORT\_REF\_VAL 0x2908

[ 941](group__bt__uuid.md#ga001e019b08f5f88a158ed0861c017609)#define BT\_UUID\_HIDS\_REPORT\_REF \

942 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_REPORT\_REF\_VAL)

943

[ 946](group__bt__uuid.md#ga882af0a9286c487c1f108346be9af304)#define BT\_UUID\_VAL\_TRIGGER\_SETTING\_VAL 0x290a

[ 950](group__bt__uuid.md#ga2601c8bcfd2efae9b20e67f5c95de3f1)#define BT\_UUID\_VAL\_TRIGGER\_SETTING \

951 BT\_UUID\_DECLARE\_16(BT\_UUID\_VAL\_TRIGGER\_SETTING\_VAL)

952

[ 955](group__bt__uuid.md#ga85eab7f3dbd2f517d36e750d3c020dec)#define BT\_UUID\_ES\_CONFIGURATION\_VAL 0x290b

[ 959](group__bt__uuid.md#gae2d7028c5102df6f53765a98b9b729ea)#define BT\_UUID\_ES\_CONFIGURATION \

960 BT\_UUID\_DECLARE\_16(BT\_UUID\_ES\_CONFIGURATION\_VAL)

961

[ 964](group__bt__uuid.md#ga8758259d984c0391feeceb459591e2fb)#define BT\_UUID\_ES\_MEASUREMENT\_VAL 0x290c

[ 968](group__bt__uuid.md#ga5e738598773234b87a1db746badce304)#define BT\_UUID\_ES\_MEASUREMENT \

969 BT\_UUID\_DECLARE\_16(BT\_UUID\_ES\_MEASUREMENT\_VAL)

970

[ 973](group__bt__uuid.md#ga0da1b874a844e15cdf185c6e7cbc9d64)#define BT\_UUID\_ES\_TRIGGER\_SETTING\_VAL 0x290d

[ 977](group__bt__uuid.md#gab9daf129a8625853989516032010f1a3)#define BT\_UUID\_ES\_TRIGGER\_SETTING \

978 BT\_UUID\_DECLARE\_16(BT\_UUID\_ES\_TRIGGER\_SETTING\_VAL)

979

[ 982](group__bt__uuid.md#gacacc7a2120d918c46a45cde0b0a8e44b)#define BT\_UUID\_TM\_TRIGGER\_SETTING\_VAL 0x290e

[ 986](group__bt__uuid.md#ga017b04e00401d50fc33cfd34d218492c)#define BT\_UUID\_TM\_TRIGGER\_SETTING \

987 BT\_UUID\_DECLARE\_16(BT\_UUID\_TM\_TRIGGER\_SETTING\_VAL)

988

[ 991](group__bt__uuid.md#gac7a400574b6c78638e41eeaf97b7e9f3)#define BT\_UUID\_GAP\_DEVICE\_NAME\_VAL 0x2a00

[ 995](group__bt__uuid.md#ga2bda01c9df904c8d0260ca3c0e3924cb)#define BT\_UUID\_GAP\_DEVICE\_NAME \

996 BT\_UUID\_DECLARE\_16(BT\_UUID\_GAP\_DEVICE\_NAME\_VAL)

997

[ 1000](group__bt__uuid.md#ga8789efbc24ac67479a86c3dfa0379154)#define BT\_UUID\_GAP\_APPEARANCE\_VAL 0x2a01

[ 1004](group__bt__uuid.md#ga4354d250e2cfca4fc868134bca4178b0)#define BT\_UUID\_GAP\_APPEARANCE \

1005 BT\_UUID\_DECLARE\_16(BT\_UUID\_GAP\_APPEARANCE\_VAL)

1006

[ 1009](group__bt__uuid.md#ga575ef013a228bb5bb728724c9334347f)#define BT\_UUID\_GAP\_PPF\_VAL 0x2a02

[ 1013](group__bt__uuid.md#ga4bec5c6656a10756a38ac9a6805f9757)#define BT\_UUID\_GAP\_PPF \

1014 BT\_UUID\_DECLARE\_16(BT\_UUID\_GAP\_PPF\_VAL)

1015

[ 1018](group__bt__uuid.md#ga739961cc85dd01779228f5054a3c3790)#define BT\_UUID\_GAP\_RA\_VAL 0x2a03

[ 1022](group__bt__uuid.md#ga569663025aceabcd964f9c423ab030b5)#define BT\_UUID\_GAP\_RA \

1023 BT\_UUID\_DECLARE\_16(BT\_UUID\_GAP\_RA\_VAL)

1024

[ 1028](group__bt__uuid.md#ga08be6df54da61393b3fe4efb7ab70b71)#define BT\_UUID\_GAP\_PPCP\_VAL 0x2a04

[ 1032](group__bt__uuid.md#gad174f313309b1bbb1208c61769566c77)#define BT\_UUID\_GAP\_PPCP \

1033 BT\_UUID\_DECLARE\_16(BT\_UUID\_GAP\_PPCP\_VAL)

1034

[ 1037](group__bt__uuid.md#gaf7af098d1487b3e09ded21b4490c50e0)#define BT\_UUID\_GATT\_SC\_VAL 0x2a05

[ 1041](group__bt__uuid.md#gad0609fd8c275c69cd0aabb7ba7c0f628)#define BT\_UUID\_GATT\_SC \

1042 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SC\_VAL)

1043

[ 1046](group__bt__uuid.md#ga2df4fc4fb971330cb7462911b68f73fd)#define BT\_UUID\_ALERT\_LEVEL\_VAL 0x2a06

[ 1050](group__bt__uuid.md#ga400e07242af41e836dfc250dc41cb010)#define BT\_UUID\_ALERT\_LEVEL \

1051 BT\_UUID\_DECLARE\_16(BT\_UUID\_ALERT\_LEVEL\_VAL)

1052

[ 1055](group__bt__uuid.md#ga07f1f99a8e237304f9415fade56432e4)#define BT\_UUID\_TPS\_TX\_POWER\_LEVEL\_VAL 0x2a07

[ 1059](group__bt__uuid.md#gade253bd200b4d2ea9f0463c3911295f1)#define BT\_UUID\_TPS\_TX\_POWER\_LEVEL \

1060 BT\_UUID\_DECLARE\_16(BT\_UUID\_TPS\_TX\_POWER\_LEVEL\_VAL)

1061

[ 1064](group__bt__uuid.md#ga71d42d8e00aa0b388315aeeb68c29839)#define BT\_UUID\_GATT\_DT\_VAL 0x2a08

[ 1068](group__bt__uuid.md#ga09cd4c6c81b8393f19b765a01ec556a0)#define BT\_UUID\_GATT\_DT \

1069 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DT\_VAL)

1070

[ 1073](group__bt__uuid.md#ga952c7341d02dd4bf3cea142b0b41e41c)#define BT\_UUID\_GATT\_DW\_VAL 0x2a09

[ 1077](group__bt__uuid.md#ga442781cffe3da4bff3c8903d46ae07a0)#define BT\_UUID\_GATT\_DW \

1078 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DW\_VAL)

1079

[ 1082](group__bt__uuid.md#ga02fd005f86fd9995d61f63c3e7735028)#define BT\_UUID\_GATT\_DDT\_VAL 0x2a0a

[ 1086](group__bt__uuid.md#gaee156d97abd11f1422677bbb08cd5193)#define BT\_UUID\_GATT\_DDT \

1087 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DDT\_VAL)

1088

[ 1091](group__bt__uuid.md#ga195fc66b479dec1131ea5e7cf1350afb)#define BT\_UUID\_GATT\_ET256\_VAL 0x2a0c

[ 1095](group__bt__uuid.md#ga3d5472767d50ddeabcdc7e2961610b78)#define BT\_UUID\_GATT\_ET256 \

1096 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ET256\_VAL)

1097

[ 1100](group__bt__uuid.md#gad826c92cd28e6eef5651474b611ab093)#define BT\_UUID\_GATT\_DST\_VAL 0x2a0d

[ 1104](group__bt__uuid.md#ga4b08c7472ecfe66eb2290fd83772ea24)#define BT\_UUID\_GATT\_DST \

1105 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DST\_VAL)

1106

[ 1109](group__bt__uuid.md#ga4e7082162bcdc58b385989e955ebb7f9)#define BT\_UUID\_GATT\_TZ\_VAL 0x2a0e

[ 1113](group__bt__uuid.md#ga83e5e48b8bd8955dc559b95ec6e73a78)#define BT\_UUID\_GATT\_TZ \

1114 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TZ\_VAL)

1115

[ 1118](group__bt__uuid.md#ga25c6a750b9548144da0e78cca3ad6a59)#define BT\_UUID\_GATT\_LTI\_VAL 0x2a0f

[ 1122](group__bt__uuid.md#ga6524bc40fbada1e558635af6b52283b9)#define BT\_UUID\_GATT\_LTI \

1123 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LTI\_VAL)

1124

[ 1127](group__bt__uuid.md#ga1bf3703c269e658c0e0e4ef822f14299)#define BT\_UUID\_GATT\_TDST\_VAL 0x2a11

[ 1131](group__bt__uuid.md#gace914257c496dbe17adc0d2b3db8f4c7)#define BT\_UUID\_GATT\_TDST \

1132 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TDST\_VAL)

1133

[ 1136](group__bt__uuid.md#gad304e85ca1a4b8f0f53d6068a37ae8d2)#define BT\_UUID\_GATT\_TA\_VAL 0x2a12

[ 1140](group__bt__uuid.md#ga75036cc3ceecebccfbfc153a0cc9920f)#define BT\_UUID\_GATT\_TA \

1141 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TA\_VAL)

1142

[ 1145](group__bt__uuid.md#ga188a456a10d2a44c19a6825bb288294f)#define BT\_UUID\_GATT\_TS\_VAL 0x2a13

[ 1149](group__bt__uuid.md#gaaaed25b2d73258322825ca9d2460c1a1)#define BT\_UUID\_GATT\_TS \

1150 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TS\_VAL)

1151

[ 1154](group__bt__uuid.md#ga668e9e73668b1c00a3bac74080ad7bcc)#define BT\_UUID\_GATT\_RTI\_VAL 0x2a14

[ 1158](group__bt__uuid.md#ga5b241e9ab9be83919aa99c24da34fa4b)#define BT\_UUID\_GATT\_RTI \

1159 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RTI\_VAL)

1160

[ 1163](group__bt__uuid.md#ga89f6031ef8778c4eb281dcda1afe5688)#define BT\_UUID\_GATT\_TUCP\_VAL 0x2a16

[ 1167](group__bt__uuid.md#gaead8cf75f2bdecf9188272da2b3c5d41)#define BT\_UUID\_GATT\_TUCP \

1168 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TUCP\_VAL)

1169

[ 1172](group__bt__uuid.md#ga0511dd52eadfa58395981b621b31c635)#define BT\_UUID\_GATT\_TUS\_VAL 0x2a17

[ 1176](group__bt__uuid.md#gaeef7563b0eb39783afc3c86147262aee)#define BT\_UUID\_GATT\_TUS \

1177 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TUS\_VAL)

1178

[ 1181](group__bt__uuid.md#gaa11e9838368e470262efc07f86d12fc7)#define BT\_UUID\_GATT\_GM\_VAL 0x2a18

[ 1185](group__bt__uuid.md#ga804ab92719239778e8328157876fce61)#define BT\_UUID\_GATT\_GM \

1186 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_GM\_VAL)

1187

[ 1190](group__bt__uuid.md#ga1961ff80d56b5c06185601cfce941cf1)#define BT\_UUID\_BAS\_BATTERY\_LEVEL\_VAL 0x2a19

[ 1194](group__bt__uuid.md#gae4f41b4e329c728767a8a99a3a89af7e)#define BT\_UUID\_BAS\_BATTERY\_LEVEL \

1195 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_BATTERY\_LEVEL\_VAL)

1196

[ 1199](group__bt__uuid.md#ga818b6cbee38384f23e1548d49c89e53e)#define BT\_UUID\_BAS\_BATTERY\_POWER\_STATE\_VAL 0x2a1a

[ 1203](group__bt__uuid.md#ga17d4a2ee5c7587ef35013f47dacfb95d)#define BT\_UUID\_BAS\_BATTERY\_POWER\_STATE \

1204 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_BATTERY\_POWER\_STATE\_VAL)

1205

[ 1208](group__bt__uuid.md#ga7dcdb33b95cc58489343c9591fc0b453)#define BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATE\_VAL 0x2a1b

[ 1212](group__bt__uuid.md#ga3022242a2bd7ccec5580d007182864dc)#define BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATE \

1213 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATE\_VAL)

1214

[ 1217](group__bt__uuid.md#ga612376c2ac9b3b21e1fe07aa2c931fad)#define BT\_UUID\_HTS\_MEASUREMENT\_VAL 0x2a1c

[ 1221](group__bt__uuid.md#gade726271d11b08b573aec3a1a6794c55)#define BT\_UUID\_HTS\_MEASUREMENT \

1222 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTS\_MEASUREMENT\_VAL)

1223

[ 1226](group__bt__uuid.md#ga1e2c9c8bf1c27e0dd3fd37910a349d75)#define BT\_UUID\_HTS\_TEMP\_TYP\_VAL 0x2a1d

[ 1230](group__bt__uuid.md#ga7055bba7158854729f65f76841a32de6)#define BT\_UUID\_HTS\_TEMP\_TYP \

1231 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTS\_TEMP\_TYP\_VAL)

1232

[ 1235](group__bt__uuid.md#ga4b13a008e37df4a0eb2b4b94bdb15126)#define BT\_UUID\_HTS\_TEMP\_INT\_VAL 0x2a1e

[ 1239](group__bt__uuid.md#ga98f9fe29431766e819b3ea014294431b)#define BT\_UUID\_HTS\_TEMP\_INT \

1240 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTS\_TEMP\_INT\_VAL)

1241

[ 1244](group__bt__uuid.md#ga67a6e1c0f24628e0cd11a4311de5a6fa)#define BT\_UUID\_HTS\_TEMP\_C\_VAL 0x2a1f

[ 1248](group__bt__uuid.md#ga51ef3d61ceffb85824b920fa7b04bd62)#define BT\_UUID\_HTS\_TEMP\_C \

1249 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTS\_TEMP\_C\_VAL)

1250

[ 1253](group__bt__uuid.md#ga002d02e831aa0c3ca24b61b2527ac65b)#define BT\_UUID\_HTS\_TEMP\_F\_VAL 0x2a20

[ 1257](group__bt__uuid.md#ga6835b7816c5dc5bb4453e0b82925bb99)#define BT\_UUID\_HTS\_TEMP\_F \

1258 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTS\_TEMP\_F\_VAL)

1259

[ 1262](group__bt__uuid.md#gac90751f69745ed65ff1739c1b86f3942)#define BT\_UUID\_HTS\_INTERVAL\_VAL 0x2a21

[ 1266](group__bt__uuid.md#ga993de0f6c8904f1d1f8527d8a4f31946)#define BT\_UUID\_HTS\_INTERVAL \

1267 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTS\_INTERVAL\_VAL)

1268

[ 1271](group__bt__uuid.md#gaa842693e29c174601e84feb43098b543)#define BT\_UUID\_HIDS\_BOOT\_KB\_IN\_REPORT\_VAL 0x2a22

[ 1275](group__bt__uuid.md#ga0ef3ddb08d602fcb513d348b1e1f2eb8)#define BT\_UUID\_HIDS\_BOOT\_KB\_IN\_REPORT \

1276 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_BOOT\_KB\_IN\_REPORT\_VAL)

1277

[ 1280](group__bt__uuid.md#ga4fdfa6e582c6367aea30e9846653ebd3)#define BT\_UUID\_DIS\_SYSTEM\_ID\_VAL 0x2a23

[ 1284](group__bt__uuid.md#gaac15c93c66cb583c3819036a2bd5ba24)#define BT\_UUID\_DIS\_SYSTEM\_ID \

1285 BT\_UUID\_DECLARE\_16(BT\_UUID\_DIS\_SYSTEM\_ID\_VAL)

1286

[ 1289](group__bt__uuid.md#ga32a4462aa866ff15bf33046efde8e796)#define BT\_UUID\_DIS\_MODEL\_NUMBER\_VAL 0x2a24

[ 1293](group__bt__uuid.md#ga250d08b7b3de123c866143599975aa41)#define BT\_UUID\_DIS\_MODEL\_NUMBER \

1294 BT\_UUID\_DECLARE\_16(BT\_UUID\_DIS\_MODEL\_NUMBER\_VAL)

1295

[ 1298](group__bt__uuid.md#ga40c84dd8ce10d983596a4f6b9cfea82f)#define BT\_UUID\_DIS\_SERIAL\_NUMBER\_VAL 0x2a25

[ 1302](group__bt__uuid.md#ga072770347ecf34cb89d293c31f59642d)#define BT\_UUID\_DIS\_SERIAL\_NUMBER \

1303 BT\_UUID\_DECLARE\_16(BT\_UUID\_DIS\_SERIAL\_NUMBER\_VAL)

1304

[ 1307](group__bt__uuid.md#ga220481d4fb2b498fad4e82637a0d02da)#define BT\_UUID\_DIS\_FIRMWARE\_REVISION\_VAL 0x2a26

[ 1311](group__bt__uuid.md#ga988bb4018b232cb4da64d522703ec5b3)#define BT\_UUID\_DIS\_FIRMWARE\_REVISION \

1312 BT\_UUID\_DECLARE\_16(BT\_UUID\_DIS\_FIRMWARE\_REVISION\_VAL)

1313

[ 1316](group__bt__uuid.md#ga3db6b3e905dd874c28a7b59c7a2a1b21)#define BT\_UUID\_DIS\_HARDWARE\_REVISION\_VAL 0x2a27

[ 1320](group__bt__uuid.md#ga3842092a747954d24ceef3a0951efac7)#define BT\_UUID\_DIS\_HARDWARE\_REVISION \

1321 BT\_UUID\_DECLARE\_16(BT\_UUID\_DIS\_HARDWARE\_REVISION\_VAL)

1322

[ 1325](group__bt__uuid.md#gabef02eec1e667b2b35521a46b355d2e8)#define BT\_UUID\_DIS\_SOFTWARE\_REVISION\_VAL 0x2a28

[ 1329](group__bt__uuid.md#ga8e9cc11f505e578851155659dc1ab262)#define BT\_UUID\_DIS\_SOFTWARE\_REVISION \

1330 BT\_UUID\_DECLARE\_16(BT\_UUID\_DIS\_SOFTWARE\_REVISION\_VAL)

1331

[ 1334](group__bt__uuid.md#gac726ebb1cbc1d7ed63df41c232ee4a42)#define BT\_UUID\_DIS\_MANUFACTURER\_NAME\_VAL 0x2a29

[ 1338](group__bt__uuid.md#gaefd466120c6923d806cfc4b5beb9899d)#define BT\_UUID\_DIS\_MANUFACTURER\_NAME \

1339 BT\_UUID\_DECLARE\_16(BT\_UUID\_DIS\_MANUFACTURER\_NAME\_VAL)

1340

[ 1343](group__bt__uuid.md#gabf8a181cbe973c985c71aa6eb7d92fe1)#define BT\_UUID\_GATT\_IEEE\_RCDL\_VAL 0x2a2a

[ 1347](group__bt__uuid.md#ga3d95539bee32ca38ea825aadf85840fb)#define BT\_UUID\_GATT\_IEEE\_RCDL \

1348 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IEEE\_RCDL\_VAL)

1349

[ 1352](group__bt__uuid.md#gae8de32ab38c9e160dc1883c345063855)#define BT\_UUID\_CTS\_CURRENT\_TIME\_VAL 0x2a2b

[ 1356](group__bt__uuid.md#gae0a920c076eb504b448f390c320ccfb8)#define BT\_UUID\_CTS\_CURRENT\_TIME \

1357 BT\_UUID\_DECLARE\_16(BT\_UUID\_CTS\_CURRENT\_TIME\_VAL)

1358

[ 1361](group__bt__uuid.md#ga6768ade4d8adf925fb52a27cee616e6e)#define BT\_UUID\_MAGN\_DECLINATION\_VAL 0x2a2c

[ 1365](group__bt__uuid.md#ga7322a8412c7aaf9e6f06473d3fa5186d)#define BT\_UUID\_MAGN\_DECLINATION \

1366 BT\_UUID\_DECLARE\_16(BT\_UUID\_MAGN\_DECLINATION\_VAL)

1367

[ 1370](group__bt__uuid.md#gabc9b96c541f0711bf5525269c4b3e5b0)#define BT\_UUID\_GATT\_LLAT\_VAL 0x2a2d

[ 1374](group__bt__uuid.md#gaa9187bacfb95b379734ccf89f7eef163)#define BT\_UUID\_GATT\_LLAT \

1375 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LLAT\_VAL)

1376

[ 1379](group__bt__uuid.md#ga5d369d45c15dad30ccf7c3066863401f)#define BT\_UUID\_GATT\_LLON\_VAL 0x2a2e

[ 1383](group__bt__uuid.md#gae090952d14ae3db50edabbdfc4d8ae25)#define BT\_UUID\_GATT\_LLON \

1384 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LLON\_VAL)

1385

[ 1388](group__bt__uuid.md#gaca1fdcec43844e0e6afeda46d7d60baf)#define BT\_UUID\_GATT\_POS\_2D\_VAL 0x2a2f

[ 1392](group__bt__uuid.md#ga21220783e6c7079bc9bd2f712b882dc6)#define BT\_UUID\_GATT\_POS\_2D \

1393 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_POS\_2D\_VAL)

1394

[ 1397](group__bt__uuid.md#ga66b1060fd8eaf94955211b87c9d940c2)#define BT\_UUID\_GATT\_POS\_3D\_VAL 0x2a30

[ 1401](group__bt__uuid.md#ga56e0a35ad8138b961f68155fa2091ae1)#define BT\_UUID\_GATT\_POS\_3D \

1402 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_POS\_3D\_VAL)

1403

[ 1406](group__bt__uuid.md#ga862122929d6e4717d21c84efc5869da2)#define BT\_UUID\_GATT\_SR\_VAL 0x2a31

[ 1410](group__bt__uuid.md#ga720d3e1f20d70cffe312f983224c2335)#define BT\_UUID\_GATT\_SR \

1411 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SR\_VAL)

1412

[ 1415](group__bt__uuid.md#ga79c18c840c919a2824d7bb84fa2217b5)#define BT\_UUID\_HIDS\_BOOT\_KB\_OUT\_REPORT\_VAL 0x2a32

[ 1419](group__bt__uuid.md#ga67e34824d0d393dcbb401c91690bce00)#define BT\_UUID\_HIDS\_BOOT\_KB\_OUT\_REPORT \

1420 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_BOOT\_KB\_OUT\_REPORT\_VAL)

1421

[ 1424](group__bt__uuid.md#ga804ec93e78855249a4a0a692314f4bf9)#define BT\_UUID\_HIDS\_BOOT\_MOUSE\_IN\_REPORT\_VAL 0x2a33

[ 1428](group__bt__uuid.md#gae86aedfdbe15939df6384870e883bfa5)#define BT\_UUID\_HIDS\_BOOT\_MOUSE\_IN\_REPORT \

1429 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_BOOT\_MOUSE\_IN\_REPORT\_VAL)

1430

[ 1433](group__bt__uuid.md#ga95629cec83007634ec69516be8086d5a)#define BT\_UUID\_GATT\_GMC\_VAL 0x2a34

[ 1437](group__bt__uuid.md#ga1ca1906ee4fc482d5bb83664362c19ae)#define BT\_UUID\_GATT\_GMC \

1438 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_GMC\_VAL)

1439

[ 1442](group__bt__uuid.md#ga2342a077a10cbf649bb46f64e5fa24cb)#define BT\_UUID\_GATT\_BPM\_VAL 0x2a35

[ 1446](group__bt__uuid.md#ga53f7809544d80bc8b797dfb0d0761ae2)#define BT\_UUID\_GATT\_BPM \

1447 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_BPM\_VAL)

1448

[ 1451](group__bt__uuid.md#gaf68e5c86b67a8065ca3a1dc8ed0bd9ea)#define BT\_UUID\_GATT\_ICP\_VAL 0x2a36

[ 1455](group__bt__uuid.md#ga33ffcb4cc70f133a29bbbe6c19d6e964)#define BT\_UUID\_GATT\_ICP \

1456 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ICP\_VAL)

1457

[ 1460](group__bt__uuid.md#ga44d502836331e3ffda5718d719e77ff6)#define BT\_UUID\_HRS\_MEASUREMENT\_VAL 0x2a37

[ 1464](group__bt__uuid.md#ga270ace7cd256a5441986d33becbbed05)#define BT\_UUID\_HRS\_MEASUREMENT \

1465 BT\_UUID\_DECLARE\_16(BT\_UUID\_HRS\_MEASUREMENT\_VAL)

1466

[ 1469](group__bt__uuid.md#gafed38fc5d9727fb2b1d009975142ec44)#define BT\_UUID\_HRS\_BODY\_SENSOR\_VAL 0x2a38

[ 1473](group__bt__uuid.md#ga6021612c89adac51569a14565f1f6dd2)#define BT\_UUID\_HRS\_BODY\_SENSOR \

1474 BT\_UUID\_DECLARE\_16(BT\_UUID\_HRS\_BODY\_SENSOR\_VAL)

1475

[ 1478](group__bt__uuid.md#ga83825772db7f9d5c4376a78d44d10a60)#define BT\_UUID\_HRS\_CONTROL\_POINT\_VAL 0x2a39

[ 1482](group__bt__uuid.md#gacec1c535fc0d96bbad3083240b5a87a1)#define BT\_UUID\_HRS\_CONTROL\_POINT \

1483 BT\_UUID\_DECLARE\_16(BT\_UUID\_HRS\_CONTROL\_POINT\_VAL)

1484

[ 1487](group__bt__uuid.md#gadb260392b00da4d849c03718aaf7d323)#define BT\_UUID\_GATT\_REM\_VAL 0x2a3a

[ 1491](group__bt__uuid.md#ga92564b1966ed0cacd36b13cdf44b9a04)#define BT\_UUID\_GATT\_REM \

1492 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_REM\_VAL)

1493

[ 1496](group__bt__uuid.md#gade09ce0a6c46fc85ada2d38c3240b953)#define BT\_UUID\_GATT\_SRVREQ\_VAL 0x2a3b

[ 1500](group__bt__uuid.md#ga66b18ba52088ed23136ffe121d350fa2)#define BT\_UUID\_GATT\_SRVREQ \

1501 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SRVREQ\_VAL)

1502

[ 1505](group__bt__uuid.md#ga2253ec9a6d97865c7408ea4ab18a392e)#define BT\_UUID\_GATT\_SC\_TEMP\_C\_VAL 0x2a3c

[ 1509](group__bt__uuid.md#ga2bb1b8f54f9cc4ef40650ad713181b49)#define BT\_UUID\_GATT\_SC\_TEMP\_C \

1510 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SC\_TEMP\_C\_VAL)

1511

[ 1514](group__bt__uuid.md#ga3b3f44113ca4a89e10d3d84eb02dd847)#define BT\_UUID\_GATT\_STRING\_VAL 0x2a3d

[ 1518](group__bt__uuid.md#ga4ca46824207979918b9a668cdf78e19a)#define BT\_UUID\_GATT\_STRING \

1519 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_STRING\_VAL)

1520

[ 1523](group__bt__uuid.md#gabd1aafbeaf157c4d515e5c2bae04823b)#define BT\_UUID\_GATT\_NETA\_VAL 0x2a3e

[ 1527](group__bt__uuid.md#ga98caa54c91df23461cac4b5db6a86330)#define BT\_UUID\_GATT\_NETA \

1528 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_NETA\_VAL)

1529

[ 1532](group__bt__uuid.md#ga11715889e92b0bf1942b3c4d84fa8aea)#define BT\_UUID\_GATT\_ALRTS\_VAL 0x2a3f

[ 1536](group__bt__uuid.md#ga0ef467a1b71b718216f08b21dca1e9b4)#define BT\_UUID\_GATT\_ALRTS \

1537 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ALRTS\_VAL)

1538

[ 1541](group__bt__uuid.md#gaacbe74b5b9267f2398ea1bbde0300dc6)#define BT\_UUID\_GATT\_RCP\_VAL 0x2a40

[ 1545](group__bt__uuid.md#ga54702c100d46cb9dc358fd511dbc0b7d)#define BT\_UUID\_GATT\_RCP \

1546 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RCP\_VAL)

1547

[ 1550](group__bt__uuid.md#ga1479dc83c76a07d7000d3b53f8dee08d)#define BT\_UUID\_GATT\_RS\_VAL 0x2a41

[ 1554](group__bt__uuid.md#ga5c78797bbe75b3b66cbc0d6ff1b185fa)#define BT\_UUID\_GATT\_RS \

1555 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RS\_VAL)

1556

[ 1559](group__bt__uuid.md#ga46356e3da57646e2a5bf2f6bc13e903f)#define BT\_UUID\_GATT\_ALRTCID\_MASK\_VAL 0x2a42

[ 1563](group__bt__uuid.md#ga7c905ac7003a24680ea6b2d3eeaee801)#define BT\_UUID\_GATT\_ALRTCID\_MASK \

1564 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ALRTCID\_MASK\_VAL)

1565

[ 1568](group__bt__uuid.md#gab8423dbeb2c21e6c7bc90fcfe34c3a3a)#define BT\_UUID\_GATT\_ALRTCID\_VAL 0x2a43

[ 1572](group__bt__uuid.md#ga207107524e82a8a34dc06263b434325f)#define BT\_UUID\_GATT\_ALRTCID \

1573 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ALRTCID\_VAL)

1574

[ 1577](group__bt__uuid.md#ga0ef4d1008dcfafce23b10ff3e9f13407)#define BT\_UUID\_GATT\_ALRTNCP\_VAL 0x2a44

[ 1581](group__bt__uuid.md#ga0c0c2f7825242e43ad13c070d1a8c137)#define BT\_UUID\_GATT\_ALRTNCP \

1582 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ALRTNCP\_VAL)

1583

[ 1586](group__bt__uuid.md#gacfacfd310975fb4fd6f25c33e658dfaa)#define BT\_UUID\_GATT\_UALRTS\_VAL 0x2a45

[ 1590](group__bt__uuid.md#gacf608b24c1f0c1d10fdabd8594fe91d4)#define BT\_UUID\_GATT\_UALRTS \

1591 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_UALRTS\_VAL)

1592

[ 1595](group__bt__uuid.md#ga61f32ab52c24492cc2a1f0c9ee042987)#define BT\_UUID\_GATT\_NALRT\_VAL 0x2a46

[ 1599](group__bt__uuid.md#gac66637f6bdb5c4efb56739ac3a370032)#define BT\_UUID\_GATT\_NALRT \

1600 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_NALRT\_VAL)

1601

[ 1604](group__bt__uuid.md#ga2cc802e286be6c6d97835bc21eaa0433)#define BT\_UUID\_GATT\_SNALRTC\_VAL 0x2a47

[ 1608](group__bt__uuid.md#ga30a9d308743e751e56890d48f6ef606b)#define BT\_UUID\_GATT\_SNALRTC \

1609 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SNALRTC\_VAL)

1610

[ 1613](group__bt__uuid.md#ga64a81cfd5ce67cd6c1d27f0a7e7433bd)#define BT\_UUID\_GATT\_SUALRTC\_VAL 0x2a48

[ 1617](group__bt__uuid.md#ga771c8d083004c4ef49e3334909f3d317)#define BT\_UUID\_GATT\_SUALRTC \

1618 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SUALRTC\_VAL)

1619

[ 1622](group__bt__uuid.md#gae5d786f2be340c5f126be0f500ade1f8)#define BT\_UUID\_GATT\_BPF\_VAL 0x2a49

[ 1626](group__bt__uuid.md#ga639e0f8fe154cca9773dd84e21ecc4d5)#define BT\_UUID\_GATT\_BPF \

1627 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_BPF\_VAL)

1628

[ 1631](group__bt__uuid.md#ga929e50a821031cfb9c0faa3e2b0e9c4a)#define BT\_UUID\_HIDS\_INFO\_VAL 0x2a4a

[ 1635](group__bt__uuid.md#ga28724b6efade76bfebeca2e8d7f9cdba)#define BT\_UUID\_HIDS\_INFO \

1636 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_INFO\_VAL)

1637

[ 1640](group__bt__uuid.md#ga8b3812488738cf6202586b9202403663)#define BT\_UUID\_HIDS\_REPORT\_MAP\_VAL 0x2a4b

[ 1644](group__bt__uuid.md#ga20a3521c85acd563064c5fc7ac022cda)#define BT\_UUID\_HIDS\_REPORT\_MAP \

1645 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_REPORT\_MAP\_VAL)

1646

[ 1649](group__bt__uuid.md#gabd625952d5706e851ff40b04e3d86547)#define BT\_UUID\_HIDS\_CTRL\_POINT\_VAL 0x2a4c

[ 1653](group__bt__uuid.md#ga8d867aac6ce50f6196c987438aa34c51)#define BT\_UUID\_HIDS\_CTRL\_POINT \

1654 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_CTRL\_POINT\_VAL)

1655

[ 1658](group__bt__uuid.md#gad6eea2097a8432254fd82ce3798869d7)#define BT\_UUID\_HIDS\_REPORT\_VAL 0x2a4d

[ 1662](group__bt__uuid.md#ga76e590c2499cc6d7540b0bbce20daec9)#define BT\_UUID\_HIDS\_REPORT \

1663 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_REPORT\_VAL)

1664

[ 1667](group__bt__uuid.md#ga7de83d3e0472f4edb4821e75fc209aff)#define BT\_UUID\_HIDS\_PROTOCOL\_MODE\_VAL 0x2a4e

[ 1671](group__bt__uuid.md#ga88f780ded3c66387af8825d7a3a1c8ba)#define BT\_UUID\_HIDS\_PROTOCOL\_MODE \

1672 BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDS\_PROTOCOL\_MODE\_VAL)

1673

[ 1676](group__bt__uuid.md#gacc5bebeb6cd2fb4c1b0bc7a78a9c67a2)#define BT\_UUID\_GATT\_SIW\_VAL 0x2a4f

[ 1680](group__bt__uuid.md#ga2bc786ce9acf331708f874261ab457d7)#define BT\_UUID\_GATT\_SIW \

1681 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SIW\_VAL)

1682

[ 1685](group__bt__uuid.md#gab01c14fa28140cae03cae611ee1d32a1)#define BT\_UUID\_DIS\_PNP\_ID\_VAL 0x2a50

[ 1689](group__bt__uuid.md#ga259ece0a5de917da4a497563197bcafe)#define BT\_UUID\_DIS\_PNP\_ID \

1690 BT\_UUID\_DECLARE\_16(BT\_UUID\_DIS\_PNP\_ID\_VAL)

1691

[ 1694](group__bt__uuid.md#gaea2d0fd8564007e96dcdcab634896fd7)#define BT\_UUID\_GATT\_GF\_VAL 0x2a51

[ 1698](group__bt__uuid.md#ga71ef8682466bc0418dfa848bf83af96c)#define BT\_UUID\_GATT\_GF \

1699 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_GF\_VAL)

1700

[ 1703](group__bt__uuid.md#ga413047b20718bddff95b45e1be0b5125)#define BT\_UUID\_RECORD\_ACCESS\_CONTROL\_POINT\_VAL 0x2a52

[ 1707](group__bt__uuid.md#ga8eedb1ff835988f3969a1b38713a6636)#define BT\_UUID\_RECORD\_ACCESS\_CONTROL\_POINT \

1708 BT\_UUID\_DECLARE\_16(BT\_UUID\_RECORD\_ACCESS\_CONTROL\_POINT\_VAL)

1709

[ 1712](group__bt__uuid.md#ga68f55222e780136b2c88ed9615c08f4e)#define BT\_UUID\_RSC\_MEASUREMENT\_VAL 0x2a53

[ 1716](group__bt__uuid.md#ga14a447a839d13bdc879da42399e39e63)#define BT\_UUID\_RSC\_MEASUREMENT \

1717 BT\_UUID\_DECLARE\_16(BT\_UUID\_RSC\_MEASUREMENT\_VAL)

1718

[ 1721](group__bt__uuid.md#ga9f07e47cd086e3158f637dc2266f7acb)#define BT\_UUID\_RSC\_FEATURE\_VAL 0x2a54

[ 1725](group__bt__uuid.md#ga4f64ed5b7c06c530320a9fa68794af3a)#define BT\_UUID\_RSC\_FEATURE \

1726 BT\_UUID\_DECLARE\_16(BT\_UUID\_RSC\_FEATURE\_VAL)

1727

[ 1730](group__bt__uuid.md#gad4fd923bb1733c2e9dd993cafa8b5b01)#define BT\_UUID\_SC\_CONTROL\_POINT\_VAL 0x2a55

[ 1734](group__bt__uuid.md#ga9d6efa914c5a83dcd39ec502e5ac4178)#define BT\_UUID\_SC\_CONTROL\_POINT \

1735 BT\_UUID\_DECLARE\_16(BT\_UUID\_SC\_CONTROL\_POINT\_VAL)

1736

[ 1739](group__bt__uuid.md#gab1af32d2ba06891961e32b46917b39ab)#define BT\_UUID\_GATT\_DI\_VAL 0x2a56

[ 1743](group__bt__uuid.md#ga8c4a4fd21416af1be4a0ff2760c48786)#define BT\_UUID\_GATT\_DI \

1744 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DI\_VAL)

1745

[ 1748](group__bt__uuid.md#gad9c70984dc907efd40e3652603012ada)#define BT\_UUID\_GATT\_DO\_VAL 0x2a57

[ 1752](group__bt__uuid.md#gab39f19f3e38e8954cac13c4ba6db2234)#define BT\_UUID\_GATT\_DO \

1753 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DO\_VAL)

1754

[ 1757](group__bt__uuid.md#ga6b9158a8808fe72710023efac16f8d7e)#define BT\_UUID\_GATT\_AI\_VAL 0x2a58

[ 1761](group__bt__uuid.md#ga8f60411278ff93a3d590050ed4a87a70)#define BT\_UUID\_GATT\_AI \

1762 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AI\_VAL)

1763

[ 1766](group__bt__uuid.md#gae6b9567925c04cde856d656c091540fc)#define BT\_UUID\_GATT\_AO\_VAL 0x2a59

[ 1770](group__bt__uuid.md#ga3f04b6880bc88de907a3c5b5e1acc10b)#define BT\_UUID\_GATT\_AO \

1771 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AO\_VAL)

1772

[ 1775](group__bt__uuid.md#gadb16be338b14fbd82f7c33b6b92502e8)#define BT\_UUID\_GATT\_AGGR\_VAL 0x2a5a

[ 1779](group__bt__uuid.md#ga7bc66b120e8a90631fe557c9393a7b88)#define BT\_UUID\_GATT\_AGGR \

1780 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AGGR\_VAL)

1781

[ 1784](group__bt__uuid.md#ga3465d2cfa3704021b137316d04d786b1)#define BT\_UUID\_CSC\_MEASUREMENT\_VAL 0x2a5b

[ 1788](group__bt__uuid.md#gab3a6cac39fe5370fe4c23f43a165db2d)#define BT\_UUID\_CSC\_MEASUREMENT \

1789 BT\_UUID\_DECLARE\_16(BT\_UUID\_CSC\_MEASUREMENT\_VAL)

1790

[ 1793](group__bt__uuid.md#ga7f697ab76e21d37c62080fe0b5a0e591)#define BT\_UUID\_CSC\_FEATURE\_VAL 0x2a5c

[ 1797](group__bt__uuid.md#gaa4d36cbd23dfb98f8baa5da37f7754ac)#define BT\_UUID\_CSC\_FEATURE \

1798 BT\_UUID\_DECLARE\_16(BT\_UUID\_CSC\_FEATURE\_VAL)

1799

[ 1802](group__bt__uuid.md#gae9aec5938fb89ffe510f66af4b330e19)#define BT\_UUID\_SENSOR\_LOCATION\_VAL 0x2a5d

[ 1806](group__bt__uuid.md#gad639330b00b9f8ffcd62c6c1ef7b75d0)#define BT\_UUID\_SENSOR\_LOCATION \

1807 BT\_UUID\_DECLARE\_16(BT\_UUID\_SENSOR\_LOCATION\_VAL)

1808

[ 1811](group__bt__uuid.md#ga828a25d5bd3e087a17460a6a0d10c0a9)#define BT\_UUID\_GATT\_PLX\_SCM\_VAL 0x2a5e

[ 1815](group__bt__uuid.md#ga0e691d0bdabf3b8df7c986b44eab4c85)#define BT\_UUID\_GATT\_PLX\_SCM \

1816 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PLX\_SCM\_VAL)

1817

[ 1820](group__bt__uuid.md#ga4eb8f3c1d2b33bac3b1e7e1d37cab6a3)#define BT\_UUID\_GATT\_PLX\_CM\_VAL 0x2a5f

[ 1824](group__bt__uuid.md#ga73cf57feba3e1388ad052ffad5832bc1)#define BT\_UUID\_GATT\_PLX\_CM \

1825 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PLX\_CM\_VAL)

1826

[ 1829](group__bt__uuid.md#ga8b523306abec9cadcdc742c21d86d702)#define BT\_UUID\_GATT\_PLX\_F\_VAL 0x2a60

[ 1833](group__bt__uuid.md#ga146ec7d39986333cd3583bbfc8ef27fd)#define BT\_UUID\_GATT\_PLX\_F \

1834 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PLX\_F\_VAL)

1835

[ 1838](group__bt__uuid.md#gaef6e49a81b4c5a7a32e17ed228a0415a)#define BT\_UUID\_GATT\_POPE\_VAL 0x2a61

[ 1842](group__bt__uuid.md#ga7fa4ae596a22b9fef9db13a830cb8739)#define BT\_UUID\_GATT\_POPE \

1843 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_POPE\_VAL)

1844

[ 1847](group__bt__uuid.md#gac98748753db550fcd2bf338f4e11c246)#define BT\_UUID\_GATT\_POCP\_VAL 0x2a62

[ 1851](group__bt__uuid.md#ga2ae69ed734761275ae0e4eb09080207a)#define BT\_UUID\_GATT\_POCP \

1852 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_POCP\_VAL)

1853

[ 1856](group__bt__uuid.md#gabab0970b455fb1f0ea87fb3010782ed0)#define BT\_UUID\_GATT\_CPS\_CPM\_VAL 0x2a63

[ 1860](group__bt__uuid.md#ga607c07b67d8af3554e36943cea63d1b5)#define BT\_UUID\_GATT\_CPS\_CPM \

1861 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CPS\_CPM\_VAL)

1862

[ 1865](group__bt__uuid.md#gac4bde8ba3ccd35dbd94018d40438b8fb)#define BT\_UUID\_GATT\_CPS\_CPV\_VAL 0x2a64

[ 1869](group__bt__uuid.md#ga99de832aed97db92213ffe90efd60fd7)#define BT\_UUID\_GATT\_CPS\_CPV \

1870 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CPS\_CPV\_VAL)

1871

[ 1874](group__bt__uuid.md#ga97647d99503cc60a335d6b9bacc693e9)#define BT\_UUID\_GATT\_CPS\_CPF\_VAL 0x2a65

[ 1878](group__bt__uuid.md#ga0b7fbbfa7d539676027d0345a3ce5d83)#define BT\_UUID\_GATT\_CPS\_CPF \

1879 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CPS\_CPF\_VAL)

1880

[ 1883](group__bt__uuid.md#ga1efedae02d29eeca33b7e527506169e8)#define BT\_UUID\_GATT\_CPS\_CPCP\_VAL 0x2a66

[ 1887](group__bt__uuid.md#gadc239b7879e9b3a082388331a50392c5)#define BT\_UUID\_GATT\_CPS\_CPCP \

1888 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CPS\_CPCP\_VAL)

1889

[ 1892](group__bt__uuid.md#gacc581ed161c7d5461b2d420b8b9a88f1)#define BT\_UUID\_GATT\_LOC\_SPD\_VAL 0x2a67

[ 1896](group__bt__uuid.md#gae3a4c256c950e72ecb5767b31033bcb8)#define BT\_UUID\_GATT\_LOC\_SPD \

1897 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LOC\_SPD\_VAL)

1898

[ 1901](group__bt__uuid.md#ga28c8f061887f0e0b25dff4d716a65d92)#define BT\_UUID\_GATT\_NAV\_VAL 0x2a68

[ 1905](group__bt__uuid.md#ga6e08e74465bf881a85136d99bec2dc3f)#define BT\_UUID\_GATT\_NAV \

1906 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_NAV\_VAL)

1907

[ 1910](group__bt__uuid.md#ga26f80b9d40ff1a9e6718150c337a018c)#define BT\_UUID\_GATT\_PQ\_VAL 0x2a69

[ 1914](group__bt__uuid.md#ga1da56c6bd8423c99aa143756415aebc5)#define BT\_UUID\_GATT\_PQ \

1915 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PQ\_VAL)

1916

[ 1919](group__bt__uuid.md#gab3d9abfecb080e73c7f7309cfaa2760e)#define BT\_UUID\_GATT\_LNF\_VAL 0x2a6a

[ 1923](group__bt__uuid.md#gaee45af0edec1f2d7528b03b3d65f37ea)#define BT\_UUID\_GATT\_LNF \

1924 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LNF\_VAL)

1925

[ 1928](group__bt__uuid.md#ga2026b24e2189a4fc8292487b7ee94429)#define BT\_UUID\_GATT\_LNCP\_VAL 0x2a6b

[ 1932](group__bt__uuid.md#ga732fde43bbaf6f4c25d824013882089d)#define BT\_UUID\_GATT\_LNCP \

1933 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LNCP\_VAL)

1934

[ 1937](group__bt__uuid.md#ga9ee48bd5d6b3ad89252c04861f6d8ff9)#define BT\_UUID\_ELEVATION\_VAL 0x2a6c

[ 1941](group__bt__uuid.md#ga6a556f695cf7c608b9667ecec3091e32)#define BT\_UUID\_ELEVATION \

1942 BT\_UUID\_DECLARE\_16(BT\_UUID\_ELEVATION\_VAL)

1943

[ 1946](group__bt__uuid.md#ga9bb13b8b9d9212f8f7ef4559db81ab00)#define BT\_UUID\_PRESSURE\_VAL 0x2a6d

[ 1950](group__bt__uuid.md#ga3c179c975cfd6f0797e1098d65d59654)#define BT\_UUID\_PRESSURE \

1951 BT\_UUID\_DECLARE\_16(BT\_UUID\_PRESSURE\_VAL)

1952

[ 1955](group__bt__uuid.md#ga9f420dc2ff26a723fe4cbdd467e64d47)#define BT\_UUID\_TEMPERATURE\_VAL 0x2a6e

[ 1959](group__bt__uuid.md#ga9ce10219c9d9b2f16b9bc101398a5093)#define BT\_UUID\_TEMPERATURE \

1960 BT\_UUID\_DECLARE\_16(BT\_UUID\_TEMPERATURE\_VAL)

1961

[ 1964](group__bt__uuid.md#gaa1739f28a51d563d6c9b77c2f7cbf081)#define BT\_UUID\_HUMIDITY\_VAL 0x2a6f

[ 1968](group__bt__uuid.md#gae6d2caca722e06366171b25659798478)#define BT\_UUID\_HUMIDITY \

1969 BT\_UUID\_DECLARE\_16(BT\_UUID\_HUMIDITY\_VAL)

1970

[ 1973](group__bt__uuid.md#gab89e34d55bd53f075dac53f0720241ba)#define BT\_UUID\_TRUE\_WIND\_SPEED\_VAL 0x2a70

[ 1977](group__bt__uuid.md#ga1bf8b992dc79021b1a3f876b2898d25d)#define BT\_UUID\_TRUE\_WIND\_SPEED \

1978 BT\_UUID\_DECLARE\_16(BT\_UUID\_TRUE\_WIND\_SPEED\_VAL)

1979

[ 1982](group__bt__uuid.md#ga7d77a45acb17505099602df264b8bb96)#define BT\_UUID\_TRUE\_WIND\_DIR\_VAL 0x2a71

[ 1986](group__bt__uuid.md#ga0ba41218ce4954620dfe73f06089fc96)#define BT\_UUID\_TRUE\_WIND\_DIR \

1987 BT\_UUID\_DECLARE\_16(BT\_UUID\_TRUE\_WIND\_DIR\_VAL)

1988

[ 1991](group__bt__uuid.md#gad0cff10ce44864db5128c438e4be7c8d)#define BT\_UUID\_APPARENT\_WIND\_SPEED\_VAL 0x2a72

[ 1995](group__bt__uuid.md#gaf6a81b9581f029463314fb25dd100e95)#define BT\_UUID\_APPARENT\_WIND\_SPEED \

1996 BT\_UUID\_DECLARE\_16(BT\_UUID\_APPARENT\_WIND\_SPEED\_VAL)

1997

[ 2000](group__bt__uuid.md#ga5eb592d6e55ca89ae5cd825edae6d508)#define BT\_UUID\_APPARENT\_WIND\_DIR\_VAL 0x2a73

[ 2004](group__bt__uuid.md#ga69adddc8dc981d2b5d02ab604826e42b)#define BT\_UUID\_APPARENT\_WIND\_DIR \

2005 BT\_UUID\_DECLARE\_16(BT\_UUID\_APPARENT\_WIND\_DIR\_VAL)

2006

[ 2009](group__bt__uuid.md#ga52857a87ddb7c2df50dcb8436804c7e2)#define BT\_UUID\_GUST\_FACTOR\_VAL 0x2a74

[ 2013](group__bt__uuid.md#ga0b97427c4d526e544b0fc1b778756941)#define BT\_UUID\_GUST\_FACTOR \

2014 BT\_UUID\_DECLARE\_16(BT\_UUID\_GUST\_FACTOR\_VAL)

2015

[ 2018](group__bt__uuid.md#gaececeeeb1976c979aafafe3c892f8a59)#define BT\_UUID\_POLLEN\_CONCENTRATION\_VAL 0x2a75

[ 2022](group__bt__uuid.md#gaa1a189a6d6b23f6983e38124e53aa8be)#define BT\_UUID\_POLLEN\_CONCENTRATION \

2023 BT\_UUID\_DECLARE\_16(BT\_UUID\_POLLEN\_CONCENTRATION\_VAL)

2024

[ 2027](group__bt__uuid.md#gae30333c9b8a0b24f1fa6790872fc7a55)#define BT\_UUID\_UV\_INDEX\_VAL 0x2a76

[ 2031](group__bt__uuid.md#gab47898ad86865b6fd514f577e3b7d6f6)#define BT\_UUID\_UV\_INDEX \

2032 BT\_UUID\_DECLARE\_16(BT\_UUID\_UV\_INDEX\_VAL)

2033

[ 2036](group__bt__uuid.md#gaa48c2c1a4c75a3b1071b0ef4ca480150)#define BT\_UUID\_IRRADIANCE\_VAL 0x2a77

[ 2040](group__bt__uuid.md#ga1e5254104ebb5ccd9a1e3c0915891aad)#define BT\_UUID\_IRRADIANCE \

2041 BT\_UUID\_DECLARE\_16(BT\_UUID\_IRRADIANCE\_VAL)

2042

[ 2045](group__bt__uuid.md#ga4ed507e7f1ecd49186411efbe4fc26ee)#define BT\_UUID\_RAINFALL\_VAL 0x2a78

[ 2049](group__bt__uuid.md#ga71278019b98dac06d067227ce47320ba)#define BT\_UUID\_RAINFALL \

2050 BT\_UUID\_DECLARE\_16(BT\_UUID\_RAINFALL\_VAL)

2051

[ 2054](group__bt__uuid.md#ga424993240c213443fc9e95fa9d4ea913)#define BT\_UUID\_WIND\_CHILL\_VAL 0x2a79

[ 2058](group__bt__uuid.md#ga2bd92aab9da9f594d8a061922c51a137)#define BT\_UUID\_WIND\_CHILL \

2059 BT\_UUID\_DECLARE\_16(BT\_UUID\_WIND\_CHILL\_VAL)

2060

[ 2063](group__bt__uuid.md#ga3c0468464a353c37ff4994f49439d27b)#define BT\_UUID\_HEAT\_INDEX\_VAL 0x2a7a

[ 2067](group__bt__uuid.md#ga56c812b5eb985ff21f91fb430d89deb3)#define BT\_UUID\_HEAT\_INDEX \

2068 BT\_UUID\_DECLARE\_16(BT\_UUID\_HEAT\_INDEX\_VAL)

2069

[ 2072](group__bt__uuid.md#gacf36659263e0a99aece77af08f4ca816)#define BT\_UUID\_DEW\_POINT\_VAL 0x2a7b

[ 2076](group__bt__uuid.md#gaf80bc7369817e44102e530371bdf7771)#define BT\_UUID\_DEW\_POINT \

2077 BT\_UUID\_DECLARE\_16(BT\_UUID\_DEW\_POINT\_VAL)

2078

[ 2081](group__bt__uuid.md#gabb35ed33581726b5eb3bd09abe3bf090)#define BT\_UUID\_GATT\_TREND\_VAL 0x2a7c

[ 2085](group__bt__uuid.md#ga8b36445adba800c187208c2822a4c0ef)#define BT\_UUID\_GATT\_TREND \

2086 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TREND\_VAL)

2087

[ 2090](group__bt__uuid.md#gadaf24469185095c9a64d09f9494202bd)#define BT\_UUID\_DESC\_VALUE\_CHANGED\_VAL 0x2a7d

[ 2094](group__bt__uuid.md#ga12ad8a70a766261bd258c5ff96dda1d0)#define BT\_UUID\_DESC\_VALUE\_CHANGED \

2095 BT\_UUID\_DECLARE\_16(BT\_UUID\_DESC\_VALUE\_CHANGED\_VAL)

2096

[ 2099](group__bt__uuid.md#gad0a8a823d03c2cfd29b330422d909468)#define BT\_UUID\_GATT\_AEHRLL\_VAL 0x2a7e

[ 2103](group__bt__uuid.md#ga185e4267f64937fae52a15297df555d0)#define BT\_UUID\_GATT\_AEHRLL \

2104 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AEHRLL\_VAL)

2105

[ 2108](group__bt__uuid.md#gafe43bdafe5d04b4b5ff205ee9c4efa59)#define BT\_UUID\_GATT\_AETHR\_VAL 0x2a7f

[ 2112](group__bt__uuid.md#ga81826c45c657d1b6e1ab391776e37d04)#define BT\_UUID\_GATT\_AETHR \

2113 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AETHR\_VAL)

2114

[ 2117](group__bt__uuid.md#ga783cfd994944d68e137d4101943d3665)#define BT\_UUID\_GATT\_AGE\_VAL 0x2a80

[ 2121](group__bt__uuid.md#ga76fb417fd8e60358ae753d7139be227f)#define BT\_UUID\_GATT\_AGE \

2122 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AGE\_VAL)

2123

[ 2126](group__bt__uuid.md#gac145e3d9d2b97eb18b059a0146bf4831)#define BT\_UUID\_GATT\_ANHRLL\_VAL 0x2a81

[ 2130](group__bt__uuid.md#ga8150d2662f87da3a2175f57236905dbd)#define BT\_UUID\_GATT\_ANHRLL \

2131 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ANHRLL\_VAL)

2132

[ 2135](group__bt__uuid.md#gaf160fd8971de7dcfd231474e928c20fd)#define BT\_UUID\_GATT\_ANHRUL\_VAL 0x2a82

[ 2139](group__bt__uuid.md#gae8c042a675573ca1078b0eacc2041a86)#define BT\_UUID\_GATT\_ANHRUL \

2140 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ANHRUL\_VAL)

2141

[ 2144](group__bt__uuid.md#ga21eb08c2a91f869b792b5f71135c2586)#define BT\_UUID\_GATT\_ANTHR\_VAL 0x2a83

[ 2148](group__bt__uuid.md#ga843badc1d786e621ef26b38fa973421a)#define BT\_UUID\_GATT\_ANTHR \

2149 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ANTHR\_VAL)

2150

[ 2153](group__bt__uuid.md#ga4e2a18435fac380402c890284f4b9cb2)#define BT\_UUID\_GATT\_AEHRUL\_VAL 0x2a84

[ 2157](group__bt__uuid.md#ga7477670294c4af4a0f55426653d382f6)#define BT\_UUID\_GATT\_AEHRUL \

2158 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AEHRUL\_VAL)

2159

[ 2162](group__bt__uuid.md#gab72ef81ad3ad789c024749d05cf8a132)#define BT\_UUID\_GATT\_DATE\_BIRTH\_VAL 0x2a85

[ 2166](group__bt__uuid.md#ga20f4e7f27ff0beae7239be8e69ec6cae)#define BT\_UUID\_GATT\_DATE\_BIRTH \

2167 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DATE\_BIRTH\_VAL)

2168

[ 2171](group__bt__uuid.md#ga896c861e50c844d821f571297f9c5e54)#define BT\_UUID\_GATT\_DATE\_THRASS\_VAL 0x2a86

[ 2175](group__bt__uuid.md#gaf8dbfb3be192a96f6da53a897e853b52)#define BT\_UUID\_GATT\_DATE\_THRASS \

2176 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DATE\_THRASS\_VAL)

2177

[ 2180](group__bt__uuid.md#gaf5b2e7bd75c03612409d34874275502b)#define BT\_UUID\_GATT\_EMAIL\_VAL 0x2a87

[ 2184](group__bt__uuid.md#gaf81242da24e4380fcf379cfc0a1bd2d6)#define BT\_UUID\_GATT\_EMAIL \

2185 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_EMAIL\_VAL)

2186

[ 2189](group__bt__uuid.md#ga1b56739dbd398eede2689af120d2ffab)#define BT\_UUID\_GATT\_FBHRLL\_VAL 0x2a88

[ 2193](group__bt__uuid.md#gafe6b60c5aeb090729e901de822a21179)#define BT\_UUID\_GATT\_FBHRLL \

2194 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FBHRLL\_VAL)

2195

[ 2198](group__bt__uuid.md#gadaed267d894b3f6637ec65c3ebcaafbe)#define BT\_UUID\_GATT\_FBHRUL\_VAL 0x2a89

[ 2202](group__bt__uuid.md#ga499864acace035767c673f7f992fb072)#define BT\_UUID\_GATT\_FBHRUL \

2203 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FBHRUL\_VAL)

2204

[ 2207](group__bt__uuid.md#ga05a1552396ae29c2e0e6f23e1e6fe41b)#define BT\_UUID\_GATT\_FIRST\_NAME\_VAL 0x2a8a

[ 2211](group__bt__uuid.md#ga5668fc0689a92ef812ed7ee1c4bdd2e4)#define BT\_UUID\_GATT\_FIRST\_NAME \

2212 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FIRST\_NAME\_VAL)

2213

[ 2216](group__bt__uuid.md#ga0bf726af2e7015a870cdd67e2e055b48)#define BT\_UUID\_GATT\_5ZHRL\_VAL 0x2a8b

[ 2220](group__bt__uuid.md#ga8c7ec19973ae92bb21e2c13bdc9762e2)#define BT\_UUID\_GATT\_5ZHRL \

2221 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_5ZHRL\_VAL)

2222

[ 2225](group__bt__uuid.md#gac5142588ca57f7c8202dab97e19c47f0)#define BT\_UUID\_GATT\_GENDER\_VAL 0x2a8c

[ 2229](group__bt__uuid.md#ga5f51ed2cf6d32af22216a9fd2d444ed3)#define BT\_UUID\_GATT\_GENDER \

2230 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_GENDER\_VAL)

2231

[ 2234](group__bt__uuid.md#ga8fe65597e6c89ad6fffc3f0c33169ebe)#define BT\_UUID\_GATT\_HR\_MAX\_VAL 0x2a8d

[ 2238](group__bt__uuid.md#ga94b53abaa40569423e0a47428379f42e)#define BT\_UUID\_GATT\_HR\_MAX \

2239 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_HR\_MAX\_VAL)

2240

[ 2243](group__bt__uuid.md#gaa147b4c9f91f0d0675ffba0c715154ec)#define BT\_UUID\_GATT\_HEIGHT\_VAL 0x2a8e

[ 2247](group__bt__uuid.md#gab80f4d69799421d48ab61a1832a575a7)#define BT\_UUID\_GATT\_HEIGHT \

2248 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_HEIGHT\_VAL)

2249

[ 2252](group__bt__uuid.md#gaedb0d5b971613bd7245c3f632b7a8a13)#define BT\_UUID\_GATT\_HC\_VAL 0x2a8f

[ 2256](group__bt__uuid.md#ga3c3e534e884b6b5215a43528a51ff4e3)#define BT\_UUID\_GATT\_HC \

2257 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_HC\_VAL)

2258

[ 2261](group__bt__uuid.md#ga242f34d1b3dbb26c0efa62e0d23888ea)#define BT\_UUID\_GATT\_LAST\_NAME\_VAL 0x2a90

[ 2265](group__bt__uuid.md#gabaae49281851c5d6626ef483b90e3d53)#define BT\_UUID\_GATT\_LAST\_NAME \

2266 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LAST\_NAME\_VAL)

2267

[ 2270](group__bt__uuid.md#ga98a0f14a9a0ac32e48280b1ce441a6fd)#define BT\_UUID\_GATT\_MRHR\_VAL 0x2a91

[ 2274](group__bt__uuid.md#gac855511d479c0c82971cadfff61a4178)#define BT\_UUID\_GATT\_MRHR \

2275 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_MRHR\_VAL)

2276

[ 2279](group__bt__uuid.md#gaed3bfd56abb70c0dff169c1d2813ec18)#define BT\_UUID\_GATT\_RHR\_VAL 0x2a92

[ 2283](group__bt__uuid.md#ga4b425ea527897b54a0ed6871ce65b7de)#define BT\_UUID\_GATT\_RHR \

2284 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RHR\_VAL)

2285

[ 2288](group__bt__uuid.md#ga5303fd51cf82df81f635cc1213b7e7c8)#define BT\_UUID\_GATT\_AEANTHR\_VAL 0x2a93

[ 2292](group__bt__uuid.md#gaf80845ed35ef1e841c4805d1a1b346af)#define BT\_UUID\_GATT\_AEANTHR \

2293 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AEANTHR\_VAL)

2294

[ 2297](group__bt__uuid.md#gafddfc45ece5b3f747190bd3de773ebbe)#define BT\_UUID\_GATT\_3ZHRL\_VAL 0x2a94

[ 2301](group__bt__uuid.md#ga0b303fde7bf69dfb0284034338ae1999)#define BT\_UUID\_GATT\_3ZHRL \

2302 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_3ZHRL\_VAL)

2303

[ 2306](group__bt__uuid.md#gaa252d83bfa77990bc93d98bda035fd9c)#define BT\_UUID\_GATT\_2ZHRL\_VAL 0x2a95

[ 2310](group__bt__uuid.md#ga5389bd047e5b6769083a59114ed5603b)#define BT\_UUID\_GATT\_2ZHRL \

2311 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_2ZHRL\_VAL)

2312

[ 2315](group__bt__uuid.md#ga2e3de0e6f3ca1dbad4d7dc559f5bc093)#define BT\_UUID\_GATT\_VO2\_MAX\_VAL 0x2a96

[ 2319](group__bt__uuid.md#gaec914c8c808dc5accb82f7c707f8f9c1)#define BT\_UUID\_GATT\_VO2\_MAX \

2320 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_VO2\_MAX\_VAL)

2321

[ 2324](group__bt__uuid.md#ga6f843d3c3131abe778d3ec9ce1bcee7d)#define BT\_UUID\_GATT\_WC\_VAL 0x2a97

[ 2328](group__bt__uuid.md#ga06e0730f0abf36dea42a713b22a0082a)#define BT\_UUID\_GATT\_WC \

2329 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_WC\_VAL)

2330

[ 2333](group__bt__uuid.md#gabd5f45139136449cac740e99e74a9894)#define BT\_UUID\_GATT\_WEIGHT\_VAL 0x2a98

[ 2337](group__bt__uuid.md#ga637f0da0906948ee5b7e40cc602ed167)#define BT\_UUID\_GATT\_WEIGHT \

2338 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_WEIGHT\_VAL)

2339

[ 2342](group__bt__uuid.md#gaa88fbc8a584c60ad025447e72c5b0cb6)#define BT\_UUID\_GATT\_DBCHINC\_VAL 0x2a99

[ 2346](group__bt__uuid.md#gafa555b52c6f195f3d01905a3923db9f3)#define BT\_UUID\_GATT\_DBCHINC \

2347 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DBCHINC\_VAL)

2348

[ 2351](group__bt__uuid.md#gadff9aa175bd9b12f9f882e24335aada5)#define BT\_UUID\_GATT\_USRIDX\_VAL 0x2a9a

[ 2355](group__bt__uuid.md#ga34b014cdec1c5cf41a65e47234eb3f4e)#define BT\_UUID\_GATT\_USRIDX \

2356 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_USRIDX\_VAL)

2357

[ 2360](group__bt__uuid.md#ga4cb5bc721905c8baa78dc25d9738cbad)#define BT\_UUID\_GATT\_BCF\_VAL 0x2a9b

[ 2364](group__bt__uuid.md#ga3d96fa7aafedab4d8b2e9910a8db1029)#define BT\_UUID\_GATT\_BCF \

2365 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_BCF\_VAL)

2366

[ 2369](group__bt__uuid.md#gafa981b32cb8b6babd737922ba8bf1430)#define BT\_UUID\_GATT\_BCM\_VAL 0x2a9c

[ 2373](group__bt__uuid.md#ga9ade71ac5e947cc41d5ab6b747232a7d)#define BT\_UUID\_GATT\_BCM \

2374 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_BCM\_VAL)

2375

[ 2378](group__bt__uuid.md#ga68a0df5e07c31bf5d532c9ef64c1568c)#define BT\_UUID\_GATT\_WM\_VAL 0x2a9d

[ 2382](group__bt__uuid.md#gab9a5d321fb5d2854d7edbe66c4d8956c)#define BT\_UUID\_GATT\_WM \

2383 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_WM\_VAL)

2384

[ 2387](group__bt__uuid.md#gae5fa58f25c54cbb228d816fb58eb5eed)#define BT\_UUID\_GATT\_WSF\_VAL 0x2a9e

[ 2391](group__bt__uuid.md#ga7c084498045835ca6b9037758ccb437e)#define BT\_UUID\_GATT\_WSF \

2392 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_WSF\_VAL)

2393

[ 2396](group__bt__uuid.md#ga0e8380df1c605924bf794974b9a0c811)#define BT\_UUID\_GATT\_USRCP\_VAL 0x2a9f

[ 2400](group__bt__uuid.md#ga6cf64ee2a0564da8c5468842d4ccca72)#define BT\_UUID\_GATT\_USRCP \

2401 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_USRCP\_VAL)

2402

[ 2405](group__bt__uuid.md#ga12df5c55e64d68377b144bbe6afc9fa1)#define BT\_UUID\_MAGN\_FLUX\_DENSITY\_2D\_VAL 0x2aa0

[ 2409](group__bt__uuid.md#ga7c6fe7de55f9167f0deb7e5793683df5)#define BT\_UUID\_MAGN\_FLUX\_DENSITY\_2D \

2410 BT\_UUID\_DECLARE\_16(BT\_UUID\_MAGN\_FLUX\_DENSITY\_2D\_VAL)

2411

[ 2414](group__bt__uuid.md#ga6eab42e702b2fe2f74ee316b565b6a15)#define BT\_UUID\_MAGN\_FLUX\_DENSITY\_3D\_VAL 0x2aa1

[ 2418](group__bt__uuid.md#ga40845b75cd4b7ec5a561123f58e33f70)#define BT\_UUID\_MAGN\_FLUX\_DENSITY\_3D \

2419 BT\_UUID\_DECLARE\_16(BT\_UUID\_MAGN\_FLUX\_DENSITY\_3D\_VAL)

2420

[ 2423](group__bt__uuid.md#ga1bf8e2d09646e1340f7195c90e7b53a5)#define BT\_UUID\_GATT\_LANG\_VAL 0x2aa2

[ 2427](group__bt__uuid.md#ga8738fa7d86325f46ac3560b646afd96c)#define BT\_UUID\_GATT\_LANG \

2428 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LANG\_VAL)

2429

[ 2432](group__bt__uuid.md#ga820b05ac625c07d538697ddda5573b46)#define BT\_UUID\_BAR\_PRESSURE\_TREND\_VAL 0x2aa3

[ 2436](group__bt__uuid.md#ga1fcf3463c69e2974877bfa953c9cbe52)#define BT\_UUID\_BAR\_PRESSURE\_TREND \

2437 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAR\_PRESSURE\_TREND\_VAL)

2438

[ 2441](group__bt__uuid.md#gaa3b803e6b55d72d830f0ee01cfc1c1f4)#define BT\_UUID\_BMS\_CONTROL\_POINT\_VAL 0x2aa4

[ 2445](group__bt__uuid.md#ga08c91b0e746cce311a0c96bf4347d300)#define BT\_UUID\_BMS\_CONTROL\_POINT \

2446 BT\_UUID\_DECLARE\_16(BT\_UUID\_BMS\_CONTROL\_POINT\_VAL)

2447

[ 2450](group__bt__uuid.md#ga666cd38fd2225997e302c0517b7d7070)#define BT\_UUID\_BMS\_FEATURE\_VAL 0x2aa5

[ 2454](group__bt__uuid.md#ga1d998f7915295eeec0895cfa9d500482)#define BT\_UUID\_BMS\_FEATURE \

2455 BT\_UUID\_DECLARE\_16(BT\_UUID\_BMS\_FEATURE\_VAL)

2456

[ 2459](group__bt__uuid.md#gad7e8753c103960268eafdf4b8fa5710e)#define BT\_UUID\_CENTRAL\_ADDR\_RES\_VAL 0x2aa6

[ 2463](group__bt__uuid.md#gaf3c3da6a9485674f8865764a831e6011)#define BT\_UUID\_CENTRAL\_ADDR\_RES \

2464 BT\_UUID\_DECLARE\_16(BT\_UUID\_CENTRAL\_ADDR\_RES\_VAL)

2465

[ 2468](group__bt__uuid.md#gacec2ac2f394b7d8af60163568581c9ac)#define BT\_UUID\_CGM\_MEASUREMENT\_VAL 0x2aa7

[ 2472](group__bt__uuid.md#ga634603e1545a177d0ccfad140103f7e5)#define BT\_UUID\_CGM\_MEASUREMENT \

2473 BT\_UUID\_DECLARE\_16(BT\_UUID\_CGM\_MEASUREMENT\_VAL)

2474

[ 2477](group__bt__uuid.md#ga693fb44bd4fe9b2da9071b04170bed8a)#define BT\_UUID\_CGM\_FEATURE\_VAL 0x2aa8

[ 2481](group__bt__uuid.md#ga6be4b6b21e0c5f1dd06f45e309cc4097)#define BT\_UUID\_CGM\_FEATURE \

2482 BT\_UUID\_DECLARE\_16(BT\_UUID\_CGM\_FEATURE\_VAL)

2483

[ 2486](group__bt__uuid.md#ga0c2ebf2de8e5f2a83ebc2f11a6a79441)#define BT\_UUID\_CGM\_STATUS\_VAL 0x2aa9

[ 2490](group__bt__uuid.md#ga040dec91474ceaf096c2864eb0f46bff)#define BT\_UUID\_CGM\_STATUS \

2491 BT\_UUID\_DECLARE\_16(BT\_UUID\_CGM\_STATUS\_VAL)

2492

[ 2495](group__bt__uuid.md#ga6f646767f25f2d94cb1190ad4acef86f)#define BT\_UUID\_CGM\_SESSION\_START\_TIME\_VAL 0x2aaa

[ 2499](group__bt__uuid.md#ga0f17cfb12a8c4d628a26f7c83c8a7f4b)#define BT\_UUID\_CGM\_SESSION\_START\_TIME \

2500 BT\_UUID\_DECLARE\_16(BT\_UUID\_CGM\_SESSION\_START\_TIME\_VAL)

2501

[ 2504](group__bt__uuid.md#ga98d88d1b785d3b71b9e3b95864efdbf7)#define BT\_UUID\_CGM\_SESSION\_RUN\_TIME\_VAL 0x2aab

[ 2508](group__bt__uuid.md#ga0f8565339251160fb439d06f5b29b4cf)#define BT\_UUID\_CGM\_SESSION\_RUN\_TIME \

2509 BT\_UUID\_DECLARE\_16(BT\_UUID\_CGM\_SESSION\_RUN\_TIME\_VAL)

2510

[ 2513](group__bt__uuid.md#gaec1bbb364e33912fcc22e63c369e4c77)#define BT\_UUID\_CGM\_SPECIFIC\_OPS\_CONTROL\_POINT\_VAL 0x2aac

[ 2517](group__bt__uuid.md#ga820aab0acff43919e2710b3d5f93ef4b)#define BT\_UUID\_CGM\_SPECIFIC\_OPS\_CONTROL\_POINT \

2518 BT\_UUID\_DECLARE\_16(BT\_UUID\_CGM\_SPECIFIC\_OPS\_CONTROL\_POINT\_VAL)

2519

[ 2522](group__bt__uuid.md#gafe31f631bf3f9a232214dafa76b35ba6)#define BT\_UUID\_GATT\_IPC\_VAL 0x2aad

[ 2526](group__bt__uuid.md#ga350bcb39fe9c71f12e5661e4157e95f2)#define BT\_UUID\_GATT\_IPC \

2527 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IPC\_VAL)

2528

[ 2531](group__bt__uuid.md#gadda62951b9abf642684b266f1f073856)#define BT\_UUID\_GATT\_LAT\_VAL 0x2aae

[ 2535](group__bt__uuid.md#ga0dcbbd018fd83efcb84721146fa8c47d)#define BT\_UUID\_GATT\_LAT \

2536 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LAT\_VAL)

2537

[ 2540](group__bt__uuid.md#ga89312e66f25972bced92a8ea1574037a)#define BT\_UUID\_GATT\_LON\_VAL 0x2aaf

[ 2544](group__bt__uuid.md#ga59aa1b51e5948c649d0d49d5d7fe45ed)#define BT\_UUID\_GATT\_LON \

2545 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LON\_VAL)

2546

[ 2549](group__bt__uuid.md#gab8183450fa0b94f92709a76f58ce041c)#define BT\_UUID\_GATT\_LNCOORD\_VAL 0x2ab0

[ 2553](group__bt__uuid.md#gaf1294000d6653870589cd0d4e2d3f05f)#define BT\_UUID\_GATT\_LNCOORD \

2554 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LNCOORD\_VAL)

2555

[ 2558](group__bt__uuid.md#ga700e5b0a5be6ba38c882692da43e41f0)#define BT\_UUID\_GATT\_LECOORD\_VAL 0x2ab1

[ 2562](group__bt__uuid.md#gac7d73c69f971bad67095ee6ad03ed0f2)#define BT\_UUID\_GATT\_LECOORD \

2563 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LECOORD\_VAL)

2564

[ 2567](group__bt__uuid.md#ga64e22e58c78f09f8614079bb8cd4092e)#define BT\_UUID\_GATT\_FN\_VAL 0x2ab2

[ 2571](group__bt__uuid.md#ga7fd58fd3410975a1a66f03bdcebabdc3)#define BT\_UUID\_GATT\_FN \

2572 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FN\_VAL)

2573

[ 2576](group__bt__uuid.md#ga5b30f97c97ee5006390ab895f4bc438e)#define BT\_UUID\_GATT\_ALT\_VAL 0x2ab3

[ 2580](group__bt__uuid.md#ga10bdfef928a7cd1da6bf3b3406121c99)#define BT\_UUID\_GATT\_ALT \

2581 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ALT\_VAL)

2582

[ 2585](group__bt__uuid.md#gaeff0f6c7ab86eb8b264d80d579ad4aa5)#define BT\_UUID\_GATT\_UNCERTAINTY\_VAL 0x2ab4

[ 2589](group__bt__uuid.md#ga5fc1842a9886deb02cc28887b2e21155)#define BT\_UUID\_GATT\_UNCERTAINTY \

2590 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_UNCERTAINTY\_VAL)

2591

[ 2594](group__bt__uuid.md#gaa7c22c7d434e3a9b9e2f3f44bd75dad1)#define BT\_UUID\_GATT\_LOC\_NAME\_VAL 0x2ab5

[ 2598](group__bt__uuid.md#gaa5418e610552e13acaa2c675564ae776)#define BT\_UUID\_GATT\_LOC\_NAME \

2599 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LOC\_NAME\_VAL)

2600

[ 2603](group__bt__uuid.md#gafb86347f61b0e745bf3b970eb6cf71b0)#define BT\_UUID\_URI\_VAL 0x2ab6

[ 2607](group__bt__uuid.md#gaee04f3121fa14082ffabc4d705325449)#define BT\_UUID\_URI \

2608 BT\_UUID\_DECLARE\_16(BT\_UUID\_URI\_VAL)

2609

[ 2612](group__bt__uuid.md#gaf489c9885e90b49b0f072d365c6a7098)#define BT\_UUID\_HTTP\_HEADERS\_VAL 0x2ab7

[ 2616](group__bt__uuid.md#gad88c1b58957bbcc2df817628a6f756db)#define BT\_UUID\_HTTP\_HEADERS \

2617 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTTP\_HEADERS\_VAL)

2618

[ 2621](group__bt__uuid.md#ga257e4213c8e4aa4e6b61dba44e36b268)#define BT\_UUID\_HTTP\_STATUS\_CODE\_VAL 0x2ab8

[ 2625](group__bt__uuid.md#gaf2e15b1eabca8c810e7f61ee0d650450)#define BT\_UUID\_HTTP\_STATUS\_CODE \

2626 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTTP\_STATUS\_CODE\_VAL)

2627

[ 2630](group__bt__uuid.md#ga84600520548f966e511355ee94edbcde)#define BT\_UUID\_HTTP\_ENTITY\_BODY\_VAL 0x2ab9

[ 2634](group__bt__uuid.md#ga2336a53590edbb9ba14c7aacfa36a592)#define BT\_UUID\_HTTP\_ENTITY\_BODY \

2635 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTTP\_ENTITY\_BODY\_VAL)

2636

[ 2639](group__bt__uuid.md#ga37eb19663266e076c35cfa0c73dd0f4f)#define BT\_UUID\_HTTP\_CONTROL\_POINT\_VAL 0x2aba

[ 2643](group__bt__uuid.md#ga996630b67869b95babf5f7b280f26c49)#define BT\_UUID\_HTTP\_CONTROL\_POINT \

2644 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTTP\_CONTROL\_POINT\_VAL)

2645

[ 2648](group__bt__uuid.md#gacaa02070d2036c0cc76b16437e1cc62b)#define BT\_UUID\_HTTPS\_SECURITY\_VAL 0x2abb

[ 2652](group__bt__uuid.md#ga365519de0ab148b5820442eca52ad700)#define BT\_UUID\_HTTPS\_SECURITY \

2653 BT\_UUID\_DECLARE\_16(BT\_UUID\_HTTPS\_SECURITY\_VAL)

2654

[ 2657](group__bt__uuid.md#ga44d037f49e771f08da2381c981fb6ea6)#define BT\_UUID\_GATT\_TDS\_CP\_VAL 0x2abc

[ 2661](group__bt__uuid.md#ga90f08ee842d221580b036d154417c122)#define BT\_UUID\_GATT\_TDS\_CP \

2662 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TDS\_CP\_VAL)

2663

[ 2666](group__bt__uuid.md#ga763bb4a64fa3ba2cd3680858d24dd200)#define BT\_UUID\_OTS\_FEATURE\_VAL 0x2abd

[ 2670](group__bt__uuid.md#ga6bf7967b64150e3bc7f849fa19ddfe7c)#define BT\_UUID\_OTS\_FEATURE \

2671 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_FEATURE\_VAL)

2672

[ 2675](group__bt__uuid.md#ga4768610413b66751e9e38eef00bc4516)#define BT\_UUID\_OTS\_NAME\_VAL 0x2abe

[ 2679](group__bt__uuid.md#gaa6b72769537df80ba5450b6a398b21ff)#define BT\_UUID\_OTS\_NAME \

2680 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_NAME\_VAL)

2681

[ 2684](group__bt__uuid.md#ga1e313ee3c5d5047b8d629d99976c1e32)#define BT\_UUID\_OTS\_TYPE\_VAL 0x2abf

[ 2688](group__bt__uuid.md#ga94b169c80d3d351c85535d085366086b)#define BT\_UUID\_OTS\_TYPE \

2689 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_TYPE\_VAL)

2690

[ 2693](group__bt__uuid.md#ga6072d84794782c93b6c8cb5f30707d9d)#define BT\_UUID\_OTS\_SIZE\_VAL 0x2ac0

[ 2697](group__bt__uuid.md#gae24957c8aad49fc0f98570b6b313098a)#define BT\_UUID\_OTS\_SIZE \

2698 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_SIZE\_VAL)

2699

[ 2702](group__bt__uuid.md#gab0c3ef2ee627f77c46cc78ec1b6e5543)#define BT\_UUID\_OTS\_FIRST\_CREATED\_VAL 0x2ac1

[ 2706](group__bt__uuid.md#gae5ac09c297a770ebbf7f2a344d24d153)#define BT\_UUID\_OTS\_FIRST\_CREATED \

2707 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_FIRST\_CREATED\_VAL)

2708

[ 2711](group__bt__uuid.md#gaa9016cda30f09bd61b38654d87198694)#define BT\_UUID\_OTS\_LAST\_MODIFIED\_VAL 0x2ac2

[ 2715](group__bt__uuid.md#ga06f1570cde6df5e932c72417fe59daef)#define BT\_UUID\_OTS\_LAST\_MODIFIED \

2716 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_LAST\_MODIFIED\_VAL)

2717

[ 2720](group__bt__uuid.md#gad32cdd62e0bead3599de3b3dd6e4e014)#define BT\_UUID\_OTS\_ID\_VAL 0x2ac3

[ 2724](group__bt__uuid.md#gaf301617baf5a039c202f0993d80061ce)#define BT\_UUID\_OTS\_ID \

2725 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_ID\_VAL)

2726

[ 2729](group__bt__uuid.md#ga0360f97a4f18b56ae3dac4e9b0287602)#define BT\_UUID\_OTS\_PROPERTIES\_VAL 0x2ac4

[ 2733](group__bt__uuid.md#ga215d8088166c529ad1d0024a8f362e3e)#define BT\_UUID\_OTS\_PROPERTIES \

2734 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_PROPERTIES\_VAL)

2735

[ 2738](group__bt__uuid.md#ga7ebe0c55c503cb82cf4d0ee3838f50fe)#define BT\_UUID\_OTS\_ACTION\_CP\_VAL 0x2ac5

[ 2742](group__bt__uuid.md#ga29c7bec908eeff922e1aaa3043278d2b)#define BT\_UUID\_OTS\_ACTION\_CP \

2743 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_ACTION\_CP\_VAL)

2744

[ 2747](group__bt__uuid.md#ga145f367de3db51b96ea6922017380aa3)#define BT\_UUID\_OTS\_LIST\_CP\_VAL 0x2ac6

[ 2751](group__bt__uuid.md#ga8acbfefbe1b7cbb5a7aba290d6e7effb)#define BT\_UUID\_OTS\_LIST\_CP \

2752 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_LIST\_CP\_VAL)

2753

[ 2756](group__bt__uuid.md#ga675bd50dd63de1a13363b041eefc1634)#define BT\_UUID\_OTS\_LIST\_FILTER\_VAL 0x2ac7

[ 2760](group__bt__uuid.md#gabca5bfb5f6fb4a92f29752cb686c7d88)#define BT\_UUID\_OTS\_LIST\_FILTER \

2761 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_LIST\_FILTER\_VAL)

2762

[ 2765](group__bt__uuid.md#gaea820a540c02088355739bf6ec6e26ba)#define BT\_UUID\_OTS\_CHANGED\_VAL 0x2ac8

[ 2769](group__bt__uuid.md#ga45dc6f040b210aac136b018c760ac37e)#define BT\_UUID\_OTS\_CHANGED \

2770 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_CHANGED\_VAL)

2771

[ 2774](group__bt__uuid.md#ga080af564ef60858fe3ddc0c487f06e97)#define BT\_UUID\_GATT\_RPAO\_VAL 0x2ac9

[ 2778](group__bt__uuid.md#ga5db6e037e7020b467a5218f828b8a7ea)#define BT\_UUID\_GATT\_RPAO \

2779 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RPAO\_VAL)

2780

[ 2783](group__bt__uuid.md#ga74f28ba3693c541b909580c4fd262416)#define BT\_UUID\_OTS\_TYPE\_UNSPECIFIED\_VAL 0x2aca

[ 2787](group__bt__uuid.md#gadc3afb0781f51b2550b077ee24ce9227)#define BT\_UUID\_OTS\_TYPE\_UNSPECIFIED \

2788 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_TYPE\_UNSPECIFIED\_VAL)

2789

[ 2792](group__bt__uuid.md#ga2fee72d19822abcf76cedfbfd96d4cdc)#define BT\_UUID\_OTS\_DIRECTORY\_LISTING\_VAL 0x2acb

[ 2796](group__bt__uuid.md#ga8f306bef03ca5204c99befc1c6e71225)#define BT\_UUID\_OTS\_DIRECTORY\_LISTING \

2797 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_DIRECTORY\_LISTING\_VAL)

2798

[ 2801](group__bt__uuid.md#ga556cd0fd7d3ff4f862dd3028f0206462)#define BT\_UUID\_GATT\_FMF\_VAL 0x2acc

[ 2805](group__bt__uuid.md#ga2aeb2e0aa454feb4438f9527c52780ed)#define BT\_UUID\_GATT\_FMF \

2806 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FMF\_VAL)

2807

[ 2810](group__bt__uuid.md#gaedc6e4f493355fe2999e7f1f84bf5d00)#define BT\_UUID\_GATT\_TD\_VAL 0x2acd

[ 2814](group__bt__uuid.md#gaa8a7f082cf9b4df21c07ded6a4913b35)#define BT\_UUID\_GATT\_TD \

2815 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TD\_VAL)

2816

[ 2819](group__bt__uuid.md#ga235dc61fb231d43a5aaab0b32f398a48)#define BT\_UUID\_GATT\_CTD\_VAL 0x2ace

[ 2823](group__bt__uuid.md#ga47d30eeb1bb66bb84b8b315fbeb76eea)#define BT\_UUID\_GATT\_CTD \

2824 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CTD\_VAL)

2825

[ 2828](group__bt__uuid.md#ga84863f0507404fd9637319c384468808)#define BT\_UUID\_GATT\_STPCD\_VAL 0x2acf

[ 2832](group__bt__uuid.md#ga4fd0ee59f5451669a389814d4390c6b5)#define BT\_UUID\_GATT\_STPCD \

2833 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_STPCD\_VAL)

2834

[ 2837](group__bt__uuid.md#ga222ab56024893f1019af55052f646aca)#define BT\_UUID\_GATT\_STRCD\_VAL 0x2ad0

[ 2841](group__bt__uuid.md#gae0b7d7316806ee18c4300b399faeb52e)#define BT\_UUID\_GATT\_STRCD \

2842 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_STRCD\_VAL)

2843

[ 2846](group__bt__uuid.md#gaed2b696b1a2ecbe1e981437ee9e58389)#define BT\_UUID\_GATT\_RD\_VAL 0x2ad1

[ 2850](group__bt__uuid.md#ga933043dfadcbebbbb2c10a828280c0a0)#define BT\_UUID\_GATT\_RD \

2851 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RD\_VAL)

2852

[ 2855](group__bt__uuid.md#ga92198d40e1a682c0c7515ba306af2093)#define BT\_UUID\_GATT\_IBD\_VAL 0x2ad2

[ 2859](group__bt__uuid.md#gaf6d86dfccb1bf3796b1dbd3c087b8127)#define BT\_UUID\_GATT\_IBD \

2860 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IBD\_VAL)

2861

[ 2864](group__bt__uuid.md#ga13e94c01279818ad0ce923051bf4fd1c)#define BT\_UUID\_GATT\_TRSTAT\_VAL 0x2ad3

[ 2868](group__bt__uuid.md#ga5a7f9c7d6d0e93f2d35ff308b875f883)#define BT\_UUID\_GATT\_TRSTAT \

2869 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TRSTAT\_VAL)

2870

[ 2873](group__bt__uuid.md#gadad6f8c3d4cf5f40c5f1f27d5ea38ac3)#define BT\_UUID\_GATT\_SSR\_VAL 0x2ad4

[ 2877](group__bt__uuid.md#gab6ef5e742460fba12f8b974fc4bf735d)#define BT\_UUID\_GATT\_SSR \

2878 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SSR\_VAL)

2879

[ 2882](group__bt__uuid.md#ga6339f09bf4e825454fd8c517faf53194)#define BT\_UUID\_GATT\_SIR\_VAL 0x2ad5

[ 2886](group__bt__uuid.md#gac69a06d1568114dec01f46df95a3c5ac)#define BT\_UUID\_GATT\_SIR \

2887 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SIR\_VAL)

2888

[ 2891](group__bt__uuid.md#gaf6fae4763a3aa3fe1f04b51b108ca642)#define BT\_UUID\_GATT\_SRLR\_VAL 0x2ad6

[ 2895](group__bt__uuid.md#ga4141c63e9e7924c8d9e27922ebda4b98)#define BT\_UUID\_GATT\_SRLR \

2896 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SRLR\_VAL)

2897

[ 2900](group__bt__uuid.md#ga8516dbe4b6b630f380f9ab3a80bce179)#define BT\_UUID\_GATT\_SHRR\_VAL 0x2ad7

[ 2904](group__bt__uuid.md#gabe5693829c64f8cd98444c853e0f121c)#define BT\_UUID\_GATT\_SHRR \

2905 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SHRR\_VAL)

2906

[ 2909](group__bt__uuid.md#ga1f7f6e8197940264ff921e6dec5c2e81)#define BT\_UUID\_GATT\_SPR\_VAL 0x2ad8

[ 2913](group__bt__uuid.md#gab82bacbce14b886d23f9368db97bb329)#define BT\_UUID\_GATT\_SPR \

2914 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SPR\_VAL)

2915

[ 2918](group__bt__uuid.md#gaf910e7d5ce12084045e9283b4c5b8b7e)#define BT\_UUID\_GATT\_FMCP\_VAL 0x2ad9

[ 2922](group__bt__uuid.md#ga26b12f1ef3313b7c28328ae22512b277)#define BT\_UUID\_GATT\_FMCP \

2923 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FMCP\_VAL)

2924

[ 2927](group__bt__uuid.md#gaea596e91c046949687c4331a4841dd07)#define BT\_UUID\_GATT\_FMS\_VAL 0x2ada

[ 2931](group__bt__uuid.md#ga9ff5045f804b6a2a8cd0b2ec8906e4b3)#define BT\_UUID\_GATT\_FMS \

2932 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FMS\_VAL)

2933

[ 2936](group__bt__uuid.md#ga2bde466cfcaeec5c542d5e74f51ddd05)#define BT\_UUID\_MESH\_PROV\_DATA\_IN\_VAL 0x2adb

[ 2940](group__bt__uuid.md#gaae548e7ca5a9835bd4dcfdf853c43993)#define BT\_UUID\_MESH\_PROV\_DATA\_IN \

2941 BT\_UUID\_DECLARE\_16(BT\_UUID\_MESH\_PROV\_DATA\_IN\_VAL)

2942

[ 2945](group__bt__uuid.md#gafd6e15eb3ae65d5f480706e68aabad8e)#define BT\_UUID\_MESH\_PROV\_DATA\_OUT\_VAL 0x2adc

[ 2949](group__bt__uuid.md#gaa003522c72e96e8b2c4b7b724aa2bf2e)#define BT\_UUID\_MESH\_PROV\_DATA\_OUT \

2950 BT\_UUID\_DECLARE\_16(BT\_UUID\_MESH\_PROV\_DATA\_OUT\_VAL)

2951

[ 2954](group__bt__uuid.md#ga55488739e50c8482da6f4ad0826f0cae)#define BT\_UUID\_MESH\_PROXY\_DATA\_IN\_VAL 0x2add

[ 2958](group__bt__uuid.md#gaebcae07983c397b0771f424d2d890259)#define BT\_UUID\_MESH\_PROXY\_DATA\_IN \

2959 BT\_UUID\_DECLARE\_16(BT\_UUID\_MESH\_PROXY\_DATA\_IN\_VAL)

2960

[ 2963](group__bt__uuid.md#ga452dfb3d0f4b62ec327910b9c578ffb0)#define BT\_UUID\_MESH\_PROXY\_DATA\_OUT\_VAL 0x2ade

[ 2967](group__bt__uuid.md#gaf3fbcbebb0507aec45d94244729f85d8)#define BT\_UUID\_MESH\_PROXY\_DATA\_OUT \

2968 BT\_UUID\_DECLARE\_16(BT\_UUID\_MESH\_PROXY\_DATA\_OUT\_VAL)

2969

[ 2972](group__bt__uuid.md#gab01aec4c2f19b53d919c89b58fd92956)#define BT\_UUID\_GATT\_NNN\_VAL 0x2adf

[ 2976](group__bt__uuid.md#ga355480e43c9fd2ee1e7fa72a05141c93)#define BT\_UUID\_GATT\_NNN \

2977 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_NNN\_VAL)

2978

[ 2981](group__bt__uuid.md#gaf2bc7408a53341478f1b41d54e888478)#define BT\_UUID\_GATT\_AC\_VAL 0x2ae0

[ 2985](group__bt__uuid.md#gadbe14281482e776e87facb9835f522af)#define BT\_UUID\_GATT\_AC \

2986 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AC\_VAL)

2987

[ 2990](group__bt__uuid.md#ga2b5c1eef80844de1d49a70314db91b1d)#define BT\_UUID\_GATT\_AV\_VAL 0x2ae1

[ 2994](group__bt__uuid.md#ga3c669e805ea7fc93cade56f2281b10dc)#define BT\_UUID\_GATT\_AV \

2995 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AV\_VAL)

2996

[ 2999](group__bt__uuid.md#ga0e1cbd1ae5c198c0f834802f9d354fb7)#define BT\_UUID\_GATT\_BOOLEAN\_VAL 0x2ae2

[ 3003](group__bt__uuid.md#ga1801b550a1be17bf0bb8c07818749e4e)#define BT\_UUID\_GATT\_BOOLEAN \

3004 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_BOOLEAN\_VAL)

3005

[ 3008](group__bt__uuid.md#ga2601e0757464729c789b58deeee15285)#define BT\_UUID\_GATT\_CRDFP\_VAL 0x2ae3

[ 3012](group__bt__uuid.md#gac5bc300a9b31543dc3847990832d78c3)#define BT\_UUID\_GATT\_CRDFP \

3013 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CRDFP\_VAL)

3014

[ 3017](group__bt__uuid.md#ga8fa1863d2ae7b22462be097308fb5c81)#define BT\_UUID\_GATT\_CRCOORDS\_VAL 0x2ae4

[ 3021](group__bt__uuid.md#gac43c1fdab4869d79c423399c864f6088)#define BT\_UUID\_GATT\_CRCOORDS \

3022 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CRCOORDS\_VAL)

3023

[ 3026](group__bt__uuid.md#gac6ef845c60c6d68ad0c3269690e97d51)#define BT\_UUID\_GATT\_CRCCT\_VAL 0x2ae5

[ 3030](group__bt__uuid.md#ga52a4a6bcb91935822f7e21fecbb283bc)#define BT\_UUID\_GATT\_CRCCT \

3031 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CRCCT\_VAL)

3032

[ 3035](group__bt__uuid.md#ga5d65027929bf31cdbdacc167c3f28951)#define BT\_UUID\_GATT\_CRT\_VAL 0x2ae6

[ 3039](group__bt__uuid.md#ga94c83c03f6cb240374af1bc4ec1b5f32)#define BT\_UUID\_GATT\_CRT \

3040 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CRT\_VAL)

3041

[ 3044](group__bt__uuid.md#ga361d00b8be7dc6c3d319a138bf5be1b9)#define BT\_UUID\_GATT\_CIEIDX\_VAL 0x2ae7

[ 3048](group__bt__uuid.md#ga706f4f40760275742a9834d4b94cd1ed)#define BT\_UUID\_GATT\_CIEIDX \

3049 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CIEIDX\_VAL)

3050

[ 3053](group__bt__uuid.md#ga298d1f0c9a48695488c7b211a7de66a9)#define BT\_UUID\_GATT\_COEFFICIENT\_VAL 0x2ae8

[ 3057](group__bt__uuid.md#ga941228f8812bfda85e86a15185a1270d)#define BT\_UUID\_GATT\_COEFFICIENT \

3058 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_COEFFICIENT\_VAL)

3059

[ 3062](group__bt__uuid.md#ga5533c28dc6bcaad3f66678d0e90a4e88)#define BT\_UUID\_GATT\_CCTEMP\_VAL 0x2ae9

[ 3066](group__bt__uuid.md#ga2562158387beea244d57757e9e87422e)#define BT\_UUID\_GATT\_CCTEMP \

3067 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CCTEMP\_VAL)

3068

[ 3071](group__bt__uuid.md#ga2c292a6bf086b695dce4c8a6fcb2e331)#define BT\_UUID\_GATT\_COUNT16\_VAL 0x2aea

[ 3075](group__bt__uuid.md#ga770c5a643468816820bdcc5db2af8d69)#define BT\_UUID\_GATT\_COUNT16 \

3076 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_COUNT16\_VAL)

3077

[ 3080](group__bt__uuid.md#ga360c3c084ac6f8f4ae6c0f8ddb1f2cf3)#define BT\_UUID\_GATT\_COUNT24\_VAL 0x2aeb

[ 3084](group__bt__uuid.md#ga7191613ab08efa46949ecb67d3512180)#define BT\_UUID\_GATT\_COUNT24 \

3085 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_COUNT24\_VAL)

3086

[ 3089](group__bt__uuid.md#ga77981b5aad0c0424a08c0bbc86c5ca71)#define BT\_UUID\_GATT\_CNTRCODE\_VAL 0x2aec

[ 3093](group__bt__uuid.md#gaf83aeabd260ea7d027aafa69beb2b050)#define BT\_UUID\_GATT\_CNTRCODE \

3094 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CNTRCODE\_VAL)

3095

[ 3098](group__bt__uuid.md#gad551c08d84b220342831bbb1d358efd6)#define BT\_UUID\_GATT\_DATEUTC\_VAL 0x2aed

[ 3102](group__bt__uuid.md#ga4151cbfefc334f33800be8fdc853ca34)#define BT\_UUID\_GATT\_DATEUTC \

3103 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DATEUTC\_VAL)

3104

[ 3107](group__bt__uuid.md#ga5ae0a7207e95f6aa2d982877057453d2)#define BT\_UUID\_GATT\_EC\_VAL 0x2aee

[ 3111](group__bt__uuid.md#ga9c86c847e1f2bb2deb23dbf4382b003f)#define BT\_UUID\_GATT\_EC \

3112 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_EC\_VAL)

3113

[ 3116](group__bt__uuid.md#ga67e672df782986945ab3103c4ddff412)#define BT\_UUID\_GATT\_ECR\_VAL 0x2aef

[ 3120](group__bt__uuid.md#gac2121117e06e8d90448733b7e2ac9b97)#define BT\_UUID\_GATT\_ECR \

3121 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ECR\_VAL)

3122

[ 3125](group__bt__uuid.md#gafd1eeaf887046c9f2785089a81275153)#define BT\_UUID\_GATT\_ECSPEC\_VAL 0x2af0

[ 3129](group__bt__uuid.md#gaabdf693ada22d60cb524b501b3203b59)#define BT\_UUID\_GATT\_ECSPEC \

3130 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ECSPEC\_VAL)

3131

[ 3134](group__bt__uuid.md#ga198d44bb45cf18921841e1788aeaa774)#define BT\_UUID\_GATT\_ECSTAT\_VAL 0x2af1

[ 3138](group__bt__uuid.md#ga6a1b29e07ffd6240e138c2a0ab1d6525)#define BT\_UUID\_GATT\_ECSTAT \

3139 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ECSTAT\_VAL)

3140

[ 3143](group__bt__uuid.md#gad6a61da207a152987afcad67fe4633d2)#define BT\_UUID\_GATT\_ENERGY\_VAL 0x2af2

[ 3147](group__bt__uuid.md#ga556811cb737ddccf121dda3d65f2d79f)#define BT\_UUID\_GATT\_ENERGY \

3148 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ENERGY\_VAL)

3149

[ 3152](group__bt__uuid.md#gab14d5fbaaa0e06c51db1cd41fcc368de)#define BT\_UUID\_GATT\_EPOD\_VAL 0x2af3

[ 3156](group__bt__uuid.md#ga2c5e6339a8d25083ce8656f02298cc57)#define BT\_UUID\_GATT\_EPOD \

3157 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_EPOD\_VAL)

3158

[ 3161](group__bt__uuid.md#gafec2c62ae00f7efb506341edf08b0d9a)#define BT\_UUID\_GATT\_EVTSTAT\_VAL 0x2af4

[ 3165](group__bt__uuid.md#gaa8f949e568dce7f639aeb80415674e2a)#define BT\_UUID\_GATT\_EVTSTAT \

3166 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_EVTSTAT\_VAL)

3167

[ 3170](group__bt__uuid.md#ga5d80019b1543d04e7cc5c7dc0f969c8c)#define BT\_UUID\_GATT\_FSTR16\_VAL 0x2af5

[ 3174](group__bt__uuid.md#ga8970252d984fd463369baab7445f7bf6)#define BT\_UUID\_GATT\_FSTR16 \

3175 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FSTR16\_VAL)

3176

[ 3179](group__bt__uuid.md#gafa6970b19301bfc1c5f3dc6392850bd8)#define BT\_UUID\_GATT\_FSTR24\_VAL 0x2af6

[ 3183](group__bt__uuid.md#ga421bb2147cbf541fed439273ee5f2119)#define BT\_UUID\_GATT\_FSTR24 \

3184 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FSTR24\_VAL)

3185

[ 3188](group__bt__uuid.md#ga2b90639839a47260c7f555eec0b8bcd0)#define BT\_UUID\_GATT\_FSTR36\_VAL 0x2af7

[ 3192](group__bt__uuid.md#ga0a03f71c8d0b616f3a496efe4b5c6561)#define BT\_UUID\_GATT\_FSTR36 \

3193 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FSTR36\_VAL)

3194

[ 3197](group__bt__uuid.md#gabafdb729c08aae0debace870f6043930)#define BT\_UUID\_GATT\_FSTR8\_VAL 0x2af8

[ 3201](group__bt__uuid.md#ga7b2a21e708cc13937038a3b88c0ad58b)#define BT\_UUID\_GATT\_FSTR8 \

3202 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FSTR8\_VAL)

3203

[ 3206](group__bt__uuid.md#ga18a4861ba81ae7f0a9ff0f1de37a6a0b)#define BT\_UUID\_GATT\_GENLVL\_VAL 0x2af9

[ 3210](group__bt__uuid.md#ga7250c5f01251cf185035c18cf5d087c6)#define BT\_UUID\_GATT\_GENLVL \

3211 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_GENLVL\_VAL)

3212

[ 3215](group__bt__uuid.md#ga1419411a928165a5cc4a26f0a97358d7)#define BT\_UUID\_GATT\_GTIN\_VAL 0x2afa

[ 3219](group__bt__uuid.md#ga27ef69db6e19c23b4f735bfbe2c83b7a)#define BT\_UUID\_GATT\_GTIN \

3220 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_GTIN\_VAL)

3221

[ 3224](group__bt__uuid.md#gaf660977f7494cecb5bd2d1d4808b0531)#define BT\_UUID\_GATT\_ILLUM\_VAL 0x2afb

[ 3228](group__bt__uuid.md#gacb727e39a14240931183e4cc608f3114)#define BT\_UUID\_GATT\_ILLUM \

3229 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ILLUM\_VAL)

3230

[ 3233](group__bt__uuid.md#ga742681175c952de8840c70df64b1562b)#define BT\_UUID\_GATT\_LUMEFF\_VAL 0x2afc

[ 3237](group__bt__uuid.md#ga3441cb7f9449be2ba9cc5cd73505f894)#define BT\_UUID\_GATT\_LUMEFF \

3238 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LUMEFF\_VAL)

3239

[ 3242](group__bt__uuid.md#gade0213130552d2757d74cdc2abe12d65)#define BT\_UUID\_GATT\_LUMNRG\_VAL 0x2afd

[ 3246](group__bt__uuid.md#gaa9ad315787bedcd20206b8dc99af4081)#define BT\_UUID\_GATT\_LUMNRG \

3247 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LUMNRG\_VAL)

3248

[ 3251](group__bt__uuid.md#ga3f2d4a042fb00481383b7b5e8837f24e)#define BT\_UUID\_GATT\_LUMEXP\_VAL 0x2afe

[ 3255](group__bt__uuid.md#ga38d3dd48f55ebfde06d52310324088d4)#define BT\_UUID\_GATT\_LUMEXP \

3256 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LUMEXP\_VAL)

3257

[ 3260](group__bt__uuid.md#ga26f37ccbd862af70e5fa7516e59da73e)#define BT\_UUID\_GATT\_LUMFLX\_VAL 0x2aff

[ 3264](group__bt__uuid.md#gae05c06b201217e919c8493d3245b2f52)#define BT\_UUID\_GATT\_LUMFLX \

3265 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LUMFLX\_VAL)

3266

[ 3269](group__bt__uuid.md#gab1080ef3dffbc5521c8f587766ac22d6)#define BT\_UUID\_GATT\_LUMFLXR\_VAL 0x2b00

[ 3273](group__bt__uuid.md#ga93a7fa9b6c9bbd12ef5d9a7169405e59)#define BT\_UUID\_GATT\_LUMFLXR \

3274 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LUMFLXR\_VAL)

3275

[ 3278](group__bt__uuid.md#ga00cfabe28348d7a86a54608b8f0ec3de)#define BT\_UUID\_GATT\_LUMINT\_VAL 0x2b01

[ 3282](group__bt__uuid.md#gaefd8b48d82a4c403e735badb04e812b4)#define BT\_UUID\_GATT\_LUMINT \

3283 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LUMINT\_VAL)

3284

[ 3287](group__bt__uuid.md#ga23f13789b3f3f19691dbfdc3a33a506e)#define BT\_UUID\_GATT\_MASSFLOW\_VAL 0x2b02

[ 3291](group__bt__uuid.md#ga8670491866b6b62a3834c4f619612a7d)#define BT\_UUID\_GATT\_MASSFLOW \

3292 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_MASSFLOW\_VAL)

3293

[ 3296](group__bt__uuid.md#ga4b8ec7d1538e6655b065a488d8c523af)#define BT\_UUID\_GATT\_PERLGHT\_VAL 0x2b03

[ 3300](group__bt__uuid.md#ga0f13aca1a13cc11b7e1adf7c1f7e75b1)#define BT\_UUID\_GATT\_PERLGHT \

3301 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PERLGHT\_VAL)

3302

[ 3305](group__bt__uuid.md#ga4bc9aee30308246d28eb96152eb686b1)#define BT\_UUID\_GATT\_PER8\_VAL 0x2b04

[ 3309](group__bt__uuid.md#ga60ea8b576b1d3951be45cb928ce841b0)#define BT\_UUID\_GATT\_PER8 \

3310 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PER8\_VAL)

3311

[ 3314](group__bt__uuid.md#gac70e24a9a91738c615e83e6238c96ed7)#define BT\_UUID\_GATT\_PWR\_VAL 0x2b05

[ 3318](group__bt__uuid.md#gaa374060d2715bfab9986c1eee2467ed5)#define BT\_UUID\_GATT\_PWR \

3319 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PWR\_VAL)

3320

[ 3323](group__bt__uuid.md#ga3db91205384fb559aa9f8865c15356d1)#define BT\_UUID\_GATT\_PWRSPEC\_VAL 0x2b06

[ 3327](group__bt__uuid.md#gad69a1f73335555e9a7c164ebd2474371)#define BT\_UUID\_GATT\_PWRSPEC \

3328 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PWRSPEC\_VAL)

3329

[ 3332](group__bt__uuid.md#gac5533a77612f300dd8f1cd8ccd2ee522)#define BT\_UUID\_GATT\_RRICR\_VAL 0x2b07

[ 3336](group__bt__uuid.md#ga7c3534f8bd7b9c662e73cd9d46dc8c79)#define BT\_UUID\_GATT\_RRICR \

3337 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RRICR\_VAL)

3338

[ 3341](group__bt__uuid.md#ga41b95788eb3271a8fe87766fe903e8d9)#define BT\_UUID\_GATT\_RRIGLR\_VAL 0x2b08

[ 3345](group__bt__uuid.md#ga2e1c29cac1ece5f3fad29c61ed2b0aa4)#define BT\_UUID\_GATT\_RRIGLR \

3346 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RRIGLR\_VAL)

3347

[ 3350](group__bt__uuid.md#gac3bb5af173f013c8a49227b2920bc107)#define BT\_UUID\_GATT\_RVIVR\_VAL 0x2b09

[ 3354](group__bt__uuid.md#gaac802734c88aac862fcab0599cb2e216)#define BT\_UUID\_GATT\_RVIVR \

3355 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RVIVR\_VAL)

3356

[ 3359](group__bt__uuid.md#ga2866d911411268e5026ef729efa990e9)#define BT\_UUID\_GATT\_RVIIR\_VAL 0x2b0a

[ 3363](group__bt__uuid.md#ga165f79f1dcde1e7359a4c4602dc88c40)#define BT\_UUID\_GATT\_RVIIR \

3364 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RVIIR\_VAL)

3365

[ 3368](group__bt__uuid.md#gab73b24f9941a80fab6423ff85f68aae6)#define BT\_UUID\_GATT\_RVIPOD\_VAL 0x2b0b

[ 3372](group__bt__uuid.md#ga9e6b0e6585f2ceb62dd236a0ae3afc6a)#define BT\_UUID\_GATT\_RVIPOD \

3373 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RVIPOD\_VAL)

3374

[ 3377](group__bt__uuid.md#gaac84e4bcae1a1b83af9124688e01912a)#define BT\_UUID\_GATT\_RVITR\_VAL 0x2b0c

[ 3381](group__bt__uuid.md#ga8c8e5e43e2bc8f7c26344fff4127e039)#define BT\_UUID\_GATT\_RVITR \

3382 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RVITR\_VAL)

3383

[ 3386](group__bt__uuid.md#gaa7a119bfd7df636f0ed0bf515232e6bb)#define BT\_UUID\_GATT\_TEMP8\_VAL 0x2b0d

[ 3390](group__bt__uuid.md#ga146d14e283686a5712c90698fd6a64ad)#define BT\_UUID\_GATT\_TEMP8 \

3391 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TEMP8\_VAL)

3392

[ 3395](group__bt__uuid.md#ga616708b903a88a6bb9eabdae60813063)#define BT\_UUID\_GATT\_TEMP8\_IPOD\_VAL 0x2b0e

[ 3399](group__bt__uuid.md#ga3d28ebdcaa93ed4ccdee512f7ddd979a)#define BT\_UUID\_GATT\_TEMP8\_IPOD \

3400 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TEMP8\_IPOD\_VAL)

3401

[ 3404](group__bt__uuid.md#ga3d54ad101d044924da30aa81a6b64111)#define BT\_UUID\_GATT\_TEMP8\_STAT\_VAL 0x2b0f

[ 3408](group__bt__uuid.md#ga071d32c5e9dd24fc179f8cac531e499f)#define BT\_UUID\_GATT\_TEMP8\_STAT \

3409 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TEMP8\_STAT\_VAL)

3410

[ 3413](group__bt__uuid.md#gadcdd9e4d2cfa09f6d766b513224ef7bf)#define BT\_UUID\_GATT\_TEMP\_RNG\_VAL 0x2b10

[ 3417](group__bt__uuid.md#ga99e73003bde4dac095f198dd7045b297)#define BT\_UUID\_GATT\_TEMP\_RNG \

3418 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TEMP\_RNG\_VAL)

3419

[ 3422](group__bt__uuid.md#ga035eaed3f130c2222236fdc194f9b1a4)#define BT\_UUID\_GATT\_TEMP\_STAT\_VAL 0x2b11

[ 3426](group__bt__uuid.md#ga8ae19f54cd4aa1c7ab42c48f33080f52)#define BT\_UUID\_GATT\_TEMP\_STAT \

3427 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TEMP\_STAT\_VAL)

3428

[ 3431](group__bt__uuid.md#gae5f1cda9dbc55f77cfbb4c00f4e359f0)#define BT\_UUID\_GATT\_TIM\_DC8\_VAL 0x2b12

[ 3435](group__bt__uuid.md#gae9feb929d7a7eb67dc1db02ce26cc82b)#define BT\_UUID\_GATT\_TIM\_DC8 \

3436 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TIM\_DC8\_VAL)

3437

[ 3440](group__bt__uuid.md#ga07a0510f652506225410b1865882d1ea)#define BT\_UUID\_GATT\_TIM\_EXP8\_VAL 0x2b13

[ 3444](group__bt__uuid.md#ga5e4aee6898f1ab1f8065c113241c99bd)#define BT\_UUID\_GATT\_TIM\_EXP8 \

3445 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TIM\_EXP8\_VAL)

3446

[ 3449](group__bt__uuid.md#ga272a11fc6d56e685243f6507708f8032)#define BT\_UUID\_GATT\_TIM\_H24\_VAL 0x2b14

[ 3453](group__bt__uuid.md#gac209c86c368f2ed7c20bae2b90f36a0a)#define BT\_UUID\_GATT\_TIM\_H24 \

3454 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TIM\_H24\_VAL)

3455

[ 3458](group__bt__uuid.md#ga181a187356797362b4a7d9a7d22f7fdc)#define BT\_UUID\_GATT\_TIM\_MS24\_VAL 0x2b15

[ 3462](group__bt__uuid.md#ga941191900854cfed39dae2b5dfba499b)#define BT\_UUID\_GATT\_TIM\_MS24 \

3463 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TIM\_MS24\_VAL)

3464

[ 3467](group__bt__uuid.md#ga2ad71e9a1912c84f31072edcf3234093)#define BT\_UUID\_GATT\_TIM\_S16\_VAL 0x2b16

[ 3471](group__bt__uuid.md#ga216c5c11e143571c5b40e7554c40ab91)#define BT\_UUID\_GATT\_TIM\_S16 \

3472 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TIM\_S16\_VAL)

3473

[ 3476](group__bt__uuid.md#gae7ad9e90132e56a59d3fb3cfaea55faa)#define BT\_UUID\_GATT\_TIM\_S8\_VAL 0x2b17

[ 3480](group__bt__uuid.md#gacf36b122fdeb96d6da4b710506118668)#define BT\_UUID\_GATT\_TIM\_S8 \

3481 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TIM\_S8\_VAL)

3482

[ 3485](group__bt__uuid.md#gae727674510a76ca337ea57c4222791ab)#define BT\_UUID\_GATT\_V\_VAL 0x2b18

[ 3489](group__bt__uuid.md#ga1cedb6e5b998d0edf435dd4203fee96c)#define BT\_UUID\_GATT\_V \

3490 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_V\_VAL)

3491

[ 3494](group__bt__uuid.md#ga5bc426767e92938654f24f0158a16b53)#define BT\_UUID\_GATT\_V\_SPEC\_VAL 0x2b19

[ 3498](group__bt__uuid.md#ga23440a5aff26bf0a737d4a48b6ce301d)#define BT\_UUID\_GATT\_V\_SPEC \

3499 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_V\_SPEC\_VAL)

3500

[ 3503](group__bt__uuid.md#gac655949e3c565b8835b099a93a24498f)#define BT\_UUID\_GATT\_V\_STAT\_VAL 0x2b1a

[ 3507](group__bt__uuid.md#gac1d74460417a592cbd4f5b6528c77e28)#define BT\_UUID\_GATT\_V\_STAT \

3508 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_V\_STAT\_VAL)

3509

[ 3512](group__bt__uuid.md#gae37019af7703f5b3abb99bcfbb1d5343)#define BT\_UUID\_GATT\_VOLF\_VAL 0x2b1b

[ 3516](group__bt__uuid.md#ga8ddcea2b365f55ac647562063ede0f3c)#define BT\_UUID\_GATT\_VOLF \

3517 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_VOLF\_VAL)

3518

[ 3521](group__bt__uuid.md#gaf7b547b7f4c6908f601afc33d0d0ebb8)#define BT\_UUID\_GATT\_CRCOORD\_VAL 0x2b1c

[ 3525](group__bt__uuid.md#ga53a898269a7f5ab84e9853521f69bc69)#define BT\_UUID\_GATT\_CRCOORD \

3526 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CRCOORD\_VAL)

3527

[ 3530](group__bt__uuid.md#ga8b2d587922902479e47bd316443e0a56)#define BT\_UUID\_GATT\_RCF\_VAL 0x2b1d

[ 3534](group__bt__uuid.md#gac6961922da80f8c628a35b8855cb788b)#define BT\_UUID\_GATT\_RCF \

3535 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RCF\_VAL)

3536

[ 3539](group__bt__uuid.md#ga47316949dd2eb5571e3b94240a4e6c90)#define BT\_UUID\_GATT\_RCSET\_VAL 0x2b1e

[ 3543](group__bt__uuid.md#ga2af1f07e6e4484476740db5bb6b31b8f)#define BT\_UUID\_GATT\_RCSET \

3544 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RCSET\_VAL)

3545

[ 3548](group__bt__uuid.md#gaabe52b93d5ac1e72c468be08fdea35ef)#define BT\_UUID\_GATT\_RCCP\_VAL 0x2b1f

[ 3552](group__bt__uuid.md#ga48b7a42b204407553262ea68e53f65d7)#define BT\_UUID\_GATT\_RCCP \

3553 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RCCP\_VAL)

3554

[ 3557](group__bt__uuid.md#gadc4e7dcda6314aa68b4165199ddc4123)#define BT\_UUID\_GATT\_IDD\_SC\_VAL 0x2b20

[ 3561](group__bt__uuid.md#gab36f1fff60a7657844985841bb0350f8)#define BT\_UUID\_GATT\_IDD\_SC \

3562 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IDD\_SC\_VAL)

3563

[ 3566](group__bt__uuid.md#gafb1511371c0c19323989961689425d08)#define BT\_UUID\_GATT\_IDD\_S\_VAL 0x2b21

[ 3570](group__bt__uuid.md#ga560d7cef69190752eb8a5c4f6fed5989)#define BT\_UUID\_GATT\_IDD\_S \

3571 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IDD\_S\_VAL)

3572

[ 3575](group__bt__uuid.md#ga2e854242941b30552241e1ee3669d669)#define BT\_UUID\_GATT\_IDD\_AS\_VAL 0x2b22

[ 3579](group__bt__uuid.md#ga980781b7142c177ed46b8caca9b8b518)#define BT\_UUID\_GATT\_IDD\_AS \

3580 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IDD\_AS\_VAL)

3581

[ 3584](group__bt__uuid.md#ga7d20cc62ad420b71d299361430005d27)#define BT\_UUID\_GATT\_IDD\_F\_VAL 0x2b23

[ 3588](group__bt__uuid.md#ga369b0b1ddac085d2812a42f737bdd594)#define BT\_UUID\_GATT\_IDD\_F \

3589 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IDD\_F\_VAL)

3590

[ 3593](group__bt__uuid.md#ga1e817e253f29e03a98327e08c2048e6b)#define BT\_UUID\_GATT\_IDD\_SRCP\_VAL 0x2b24

[ 3597](group__bt__uuid.md#ga13d829bfcacb036a2271cd09491c1578)#define BT\_UUID\_GATT\_IDD\_SRCP \

3598 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IDD\_SRCP\_VAL)

3599

[ 3602](group__bt__uuid.md#ga1dc738c5c564bf05d3c2669a79db6e17)#define BT\_UUID\_GATT\_IDD\_CCP\_VAL 0x2b25

[ 3606](group__bt__uuid.md#gaf2bc260638bc158b8bfd403bf43de2d9)#define BT\_UUID\_GATT\_IDD\_CCP \

3607 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IDD\_CCP\_VAL)

3608

[ 3611](group__bt__uuid.md#ga70d6ece9b4d331965c42f0606c0c7526)#define BT\_UUID\_GATT\_IDD\_CD\_VAL 0x2b26

[ 3615](group__bt__uuid.md#gac7dbb4cb283933558699d129928e37d5)#define BT\_UUID\_GATT\_IDD\_CD \

3616 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IDD\_CD\_VAL)

3617

[ 3620](group__bt__uuid.md#gab9ef1f54711a8d7d5884c7b3a798f615)#define BT\_UUID\_GATT\_IDD\_RACP\_VAL 0x2b27

[ 3624](group__bt__uuid.md#ga628c153b88ea0f504c234dc44248a237)#define BT\_UUID\_GATT\_IDD\_RACP \

3625 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IDD\_RACP\_VAL)

3626

[ 3629](group__bt__uuid.md#ga26f24abf219ce90fd002d995e3a19d30)#define BT\_UUID\_GATT\_IDD\_HD\_VAL 0x2b28

[ 3633](group__bt__uuid.md#ga88e2087b512092d91508f8e878a22f3a)#define BT\_UUID\_GATT\_IDD\_HD \

3634 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_IDD\_HD\_VAL)

3635

[ 3638](group__bt__uuid.md#ga54537cebc8ce6e7d8d0f377a38765635)#define BT\_UUID\_GATT\_CLIENT\_FEATURES\_VAL 0x2b29

[ 3642](group__bt__uuid.md#gae3faa1515f3aae0c71d4face04929dec)#define BT\_UUID\_GATT\_CLIENT\_FEATURES \

3643 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CLIENT\_FEATURES\_VAL)

3644

[ 3647](group__bt__uuid.md#gacead7897f5fed798714a79df2764d95a)#define BT\_UUID\_GATT\_DB\_HASH\_VAL 0x2b2a

[ 3651](group__bt__uuid.md#ga6b162958f4f406fd3e3d31a84393fe19)#define BT\_UUID\_GATT\_DB\_HASH \

3652 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DB\_HASH\_VAL)

3653

[ 3656](group__bt__uuid.md#gaf609e6663173f4c4bb6ed18274f9931b)#define BT\_UUID\_GATT\_BSS\_CP\_VAL 0x2b2b

[ 3660](group__bt__uuid.md#gadeabab76545da0de52cc26d48e564730)#define BT\_UUID\_GATT\_BSS\_CP \

3661 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_BSS\_CP\_VAL)

3662

[ 3665](group__bt__uuid.md#ga73cbe100a043e8f08b87fcfed82107ad)#define BT\_UUID\_GATT\_BSS\_R\_VAL 0x2b2c

[ 3669](group__bt__uuid.md#gae9f0db1cbcc6dfeda9beb96e14350cf6)#define BT\_UUID\_GATT\_BSS\_R \

3670 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_BSS\_R\_VAL)

3671

[ 3674](group__bt__uuid.md#ga77157df8db39286f6f6edf1dd71f4a5e)#define BT\_UUID\_GATT\_EMG\_ID\_VAL 0x2b2d

[ 3678](group__bt__uuid.md#ga6fdb1cd7bf1323b27645180ca39ca063)#define BT\_UUID\_GATT\_EMG\_ID \

3679 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_EMG\_ID\_VAL)

3680

[ 3683](group__bt__uuid.md#gabcea55cbf065daab8709e4d36941ad90)#define BT\_UUID\_GATT\_EMG\_TXT\_VAL 0x2b2e

[ 3687](group__bt__uuid.md#ga1bc6805b2948d3f36af972f2ee34f93a)#define BT\_UUID\_GATT\_EMG\_TXT \

3688 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_EMG\_TXT\_VAL)

3689

[ 3692](group__bt__uuid.md#ga7d46292e64c3a8bc9a2ddd71418e56c8)#define BT\_UUID\_GATT\_ACS\_S\_VAL 0x2b2f

[ 3696](group__bt__uuid.md#gad94f7adb29687b460fb7bb860023d890)#define BT\_UUID\_GATT\_ACS\_S \

3697 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACS\_S\_VAL)

3698

[ 3701](group__bt__uuid.md#ga0b19f25f01532abb98b63438d55b7683)#define BT\_UUID\_GATT\_ACS\_DI\_VAL 0x2b30

[ 3705](group__bt__uuid.md#gabd8886704d8fba31bbb1f9a8aeee9aa3)#define BT\_UUID\_GATT\_ACS\_DI \

3706 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACS\_DI\_VAL)

3707

[ 3710](group__bt__uuid.md#ga08ffe10a9e5e1f716581d96dd49bebac)#define BT\_UUID\_GATT\_ACS\_DON\_VAL 0x2b31

[ 3714](group__bt__uuid.md#ga0933ee4e3740e4f6c28522113b84c5b0)#define BT\_UUID\_GATT\_ACS\_DON \

3715 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACS\_DON\_VAL)

3716

[ 3719](group__bt__uuid.md#ga852f095873bee6c0dec742ea45817294)#define BT\_UUID\_GATT\_ACS\_DOI\_VAL 0x2b32

[ 3723](group__bt__uuid.md#ga4875b80953686217209dc8a90e705ff2)#define BT\_UUID\_GATT\_ACS\_DOI \

3724 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACS\_DOI\_VAL)

3725

[ 3728](group__bt__uuid.md#ga492e0766dd16dea9e63e80423c9210cb)#define BT\_UUID\_GATT\_ACS\_CP\_VAL 0x2b33

[ 3732](group__bt__uuid.md#gabd2164db62c4f29d2bafc272178312e5)#define BT\_UUID\_GATT\_ACS\_CP \

3733 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACS\_CP\_VAL)

3734

[ 3737](group__bt__uuid.md#ga3016f0dd266a98f7d88a3198f54caf7e)#define BT\_UUID\_GATT\_EBPM\_VAL 0x2b34

[ 3741](group__bt__uuid.md#gafe7d80c67c7c059c174c2ec8aa6cf92d)#define BT\_UUID\_GATT\_EBPM \

3742 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_EBPM\_VAL)

3743

[ 3746](group__bt__uuid.md#gad61213ed875c9d0b6bd5a2e7154f80d7)#define BT\_UUID\_GATT\_EICP\_VAL 0x2b35

[ 3750](group__bt__uuid.md#gab5032246e17304cb99bb619e6a3d70f1)#define BT\_UUID\_GATT\_EICP \

3751 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_EICP\_VAL)

3752

[ 3755](group__bt__uuid.md#ga5b59d10e5d4653ed774a05da55241368)#define BT\_UUID\_GATT\_BPR\_VAL 0x2b36

[ 3759](group__bt__uuid.md#gafa84009c324ee2e0a36efd0bbb486d4b)#define BT\_UUID\_GATT\_BPR \

3760 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_BPR\_VAL)

3761

[ 3764](group__bt__uuid.md#ga4ac04b637bed53a51dbf598bd54a827a)#define BT\_UUID\_GATT\_RU\_VAL 0x2b37

[ 3768](group__bt__uuid.md#ga8a00648e37c023bf06be268960071d27)#define BT\_UUID\_GATT\_RU \

3769 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RU\_VAL)

3770

[ 3773](group__bt__uuid.md#gab89358d9db126f1eb9e1df6dc4639b82)#define BT\_UUID\_GATT\_BR\_EDR\_HD\_VAL 0x2b38

[ 3777](group__bt__uuid.md#ga279da4b9d9aaccd67846d3ff93e25516)#define BT\_UUID\_GATT\_BR\_EDR\_HD \

3778 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_BR\_EDR\_HD\_VAL)

3779

[ 3782](group__bt__uuid.md#gaf95bc5640e25a651bb62f474fbdbd0f0)#define BT\_UUID\_GATT\_BT\_SIG\_D\_VAL 0x2b39

[ 3786](group__bt__uuid.md#ga268e9d8096668ef890f5c17c76c882c5)#define BT\_UUID\_GATT\_BT\_SIG\_D \

3787 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_BT\_SIG\_D\_VAL)

3788

[ 3791](group__bt__uuid.md#ga8d23a276e657bccde1385066ce2cd709)#define BT\_UUID\_GATT\_SERVER\_FEATURES\_VAL 0x2b3a

[ 3795](group__bt__uuid.md#ga261af6f050c6a16d174c80cfce48b13e)#define BT\_UUID\_GATT\_SERVER\_FEATURES \

3796 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SERVER\_FEATURES\_VAL)

3797

[ 3800](group__bt__uuid.md#gad94da8852116cc6651c2bb75b8420c95)#define BT\_UUID\_GATT\_PHY\_AMF\_VAL 0x2b3b

[ 3804](group__bt__uuid.md#ga6d227d76b62bcec99cc8a8b6b8054474)#define BT\_UUID\_GATT\_PHY\_AMF \

3805 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PHY\_AMF\_VAL)

3806

[ 3809](group__bt__uuid.md#ga8302d0d60c536b9862028633c8155a3a)#define BT\_UUID\_GATT\_GEN\_AID\_VAL 0x2b3c

[ 3813](group__bt__uuid.md#gacfbd8563c68df3aa15264fc81f0eabb8)#define BT\_UUID\_GATT\_GEN\_AID \

3814 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_GEN\_AID\_VAL)

3815

[ 3818](group__bt__uuid.md#ga4865adb3aadcb01834444e7fda021162)#define BT\_UUID\_GATT\_GEN\_ASD\_VAL 0x2b3d

[ 3822](group__bt__uuid.md#ga3b068ab73e6c277692a535b81b6e9ae1)#define BT\_UUID\_GATT\_GEN\_ASD \

3823 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_GEN\_ASD\_VAL)

3824

[ 3827](group__bt__uuid.md#gac82a202322d7ee65130150d09d82b76a)#define BT\_UUID\_GATT\_CR\_AID\_VAL 0x2b3e

[ 3831](group__bt__uuid.md#ga35d88cb3312b6867d153780ee3a57be2)#define BT\_UUID\_GATT\_CR\_AID \

3832 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CR\_AID\_VAL)

3833

[ 3836](group__bt__uuid.md#ga6606c6d6ac05bbdbbbd27af5c28b825a)#define BT\_UUID\_GATT\_CR\_ASD\_VAL 0x2b3f

[ 3840](group__bt__uuid.md#gadac7397ba9891282ef425e05c8161938)#define BT\_UUID\_GATT\_CR\_ASD \

3841 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CR\_ASD\_VAL)

3842

[ 3845](group__bt__uuid.md#ga2aed9d07c8f4d552a4d6a5c2b693e97e)#define BT\_UUID\_GATT\_SC\_ASD\_VAL 0x2b40

[ 3849](group__bt__uuid.md#ga9dd42f8966856001425c4bae4f6dc5a5)#define BT\_UUID\_GATT\_SC\_ASD \

3850 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SC\_ASD\_VAL)

3851

[ 3854](group__bt__uuid.md#gabb73d22b90482201f9f20d6f89aa6671)#define BT\_UUID\_GATT\_SLP\_AID\_VAL 0x2b41

[ 3858](group__bt__uuid.md#gaf0a5a409f91366422f145acbb45e4abd)#define BT\_UUID\_GATT\_SLP\_AID \

3859 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SLP\_AID\_VAL)

3860

[ 3863](group__bt__uuid.md#gaa309ce83ee85407cc8068aaccec95b94)#define BT\_UUID\_GATT\_SLP\_ASD\_VAL 0x2b42

[ 3867](group__bt__uuid.md#ga5232c5aac8c20f23aaadf1a023d91fcb)#define BT\_UUID\_GATT\_SLP\_ASD \

3868 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SLP\_ASD\_VAL)

3869

[ 3872](group__bt__uuid.md#ga1c2a6903fe19f05e4515122ddd6e454f)#define BT\_UUID\_GATT\_PHY\_AMCP\_VAL 0x2b43

[ 3876](group__bt__uuid.md#ga59ef934ce5ccf5e4ed309319f75c1150)#define BT\_UUID\_GATT\_PHY\_AMCP \

3877 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PHY\_AMCP\_VAL)

3878

[ 3881](group__bt__uuid.md#gad5ea6f8f92b3679cafed3ac61f5d9128)#define BT\_UUID\_GATT\_ACS\_VAL 0x2b44

[ 3885](group__bt__uuid.md#ga12e8344ffb0ae5d3ff088df56f22d440)#define BT\_UUID\_GATT\_ACS \

3886 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACS\_VAL)

3887

[ 3890](group__bt__uuid.md#ga16b2c15259a5c4d456a43df7be9080d6)#define BT\_UUID\_GATT\_PHY\_ASDESC\_VAL 0x2b45

[ 3894](group__bt__uuid.md#ga3906642c3830a0dff787b6218f502b74)#define BT\_UUID\_GATT\_PHY\_ASDESC \

3895 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PHY\_ASDESC\_VAL)

3896

[ 3899](group__bt__uuid.md#gae9e12c4297a520b3d626fbd7f4e9c49c)#define BT\_UUID\_GATT\_PREF\_U\_VAL 0x2b46

[ 3903](group__bt__uuid.md#ga323afc65d2c3568d9a3267328e46879e)#define BT\_UUID\_GATT\_PREF\_U \

3904 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PREF\_U\_VAL)

3905

[ 3908](group__bt__uuid.md#gab74738d5e1fde9be0ae137603d58266a)#define BT\_UUID\_GATT\_HRES\_H\_VAL 0x2b47

[ 3912](group__bt__uuid.md#gaf095ec3ea1b24f184fce737db3b16855)#define BT\_UUID\_GATT\_HRES\_H \

3913 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_HRES\_H\_VAL)

3914

[ 3917](group__bt__uuid.md#gae44137b7932e5493b66c037b93177f30)#define BT\_UUID\_GATT\_MID\_NAME\_VAL 0x2b48

[ 3921](group__bt__uuid.md#ga478706893a1e14f1af28928ea7ee3dde)#define BT\_UUID\_GATT\_MID\_NAME \

3922 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_MID\_NAME\_VAL)

3923

[ 3926](group__bt__uuid.md#ga8ebc62a93e6c323031cd64a4c89bc191)#define BT\_UUID\_GATT\_STRDLEN\_VAL 0x2b49

[ 3930](group__bt__uuid.md#ga1a05d2cef4e003d8a9f417cfb1915600)#define BT\_UUID\_GATT\_STRDLEN \

3931 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_STRDLEN\_VAL)

3932

[ 3935](group__bt__uuid.md#gaa3a2515dfef7871cb4f2ddaa9b1838bf)#define BT\_UUID\_GATT\_HANDEDNESS\_VAL 0x2b4a

[ 3939](group__bt__uuid.md#ga9e0dd2e887dacb08466f63951bdce22c)#define BT\_UUID\_GATT\_HANDEDNESS \

3940 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_HANDEDNESS\_VAL)

3941

[ 3944](group__bt__uuid.md#ga7e3028631b4f17fc6127eb41343f6113)#define BT\_UUID\_GATT\_DEVICE\_WP\_VAL 0x2b4b

[ 3948](group__bt__uuid.md#gaf26f9aa3d7566892cb4d851a212c7a26)#define BT\_UUID\_GATT\_DEVICE\_WP \

3949 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DEVICE\_WP\_VAL)

3950

[ 3953](group__bt__uuid.md#gaff4928b6e4a0e7329ab18beed9600f1a)#define BT\_UUID\_GATT\_4ZHRL\_VAL 0x2b4c

[ 3957](group__bt__uuid.md#ga1ead62ac6b72dfafdbe46f3c6a3202a1)#define BT\_UUID\_GATT\_4ZHRL \

3958 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_4ZHRL\_VAL)

3959

[ 3962](group__bt__uuid.md#ga7fcf423cf762d9c9b534c869581ef358)#define BT\_UUID\_GATT\_HIET\_VAL 0x2b4d

[ 3966](group__bt__uuid.md#gaa0a5aa82b3eccfc14eef8ce4006899f8)#define BT\_UUID\_GATT\_HIET \

3967 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_HIET\_VAL)

3968

[ 3971](group__bt__uuid.md#ga80d44e488176d215f9da4c531915b9f4)#define BT\_UUID\_GATT\_AG\_VAL 0x2b4e

[ 3975](group__bt__uuid.md#ga8ab5d539f23fd30b6b44294d52cd148f)#define BT\_UUID\_GATT\_AG \

3976 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AG\_VAL)

3977

[ 3980](group__bt__uuid.md#ga9f129bc582093032197016897e86748f)#define BT\_UUID\_GATT\_SIN\_VAL 0x2b4f

[ 3984](group__bt__uuid.md#gaac75b92f8daddb4aecd5b6e0b2a5d33b)#define BT\_UUID\_GATT\_SIN \

3985 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SIN\_VAL)

3986

[ 3989](group__bt__uuid.md#ga462b52ed2ca39b836e0d7ea3d7a6a609)#define BT\_UUID\_GATT\_CI\_VAL 0x2b50

[ 3993](group__bt__uuid.md#ga61d3e8f34e0f3d466d4a0b64258a6d13)#define BT\_UUID\_GATT\_CI \

3994 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CI\_VAL)

3995

[ 3998](group__bt__uuid.md#ga781de482737cfc42662f6e8b1114070f)#define BT\_UUID\_GATT\_TMAPR\_VAL 0x2b51

[ 4002](group__bt__uuid.md#ga66395bad8099540561670bd1e588e1e9)#define BT\_UUID\_GATT\_TMAPR \

4003 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TMAPR\_VAL)

4004

[ 4007](group__bt__uuid.md#ga95a4d3f8c62782325d2f2bb0df260a97)#define BT\_UUID\_AICS\_STATE\_VAL 0x2b77

[ 4011](group__bt__uuid.md#ga36fff8099e5a7d9c0cbd407b9b261742)#define BT\_UUID\_AICS\_STATE \

4012 BT\_UUID\_DECLARE\_16(BT\_UUID\_AICS\_STATE\_VAL)

4013

[ 4016](group__bt__uuid.md#gaab9ed2f83db5e1ea5c2756b8045ca708)#define BT\_UUID\_AICS\_GAIN\_SETTINGS\_VAL 0x2b78

[ 4020](group__bt__uuid.md#ga0b26573f473babc0d4b4d1f817a0e292)#define BT\_UUID\_AICS\_GAIN\_SETTINGS \

4021 BT\_UUID\_DECLARE\_16(BT\_UUID\_AICS\_GAIN\_SETTINGS\_VAL)

4022

[ 4025](group__bt__uuid.md#ga60250c00a3361316b78e5fa6fef335d7)#define BT\_UUID\_AICS\_INPUT\_TYPE\_VAL 0x2b79

[ 4029](group__bt__uuid.md#gaf9ba49297331bec61b2706ad43a88260)#define BT\_UUID\_AICS\_INPUT\_TYPE \

4030 BT\_UUID\_DECLARE\_16(BT\_UUID\_AICS\_INPUT\_TYPE\_VAL)

4031

[ 4034](group__bt__uuid.md#ga369eeaa589fbb61fffe8e3dabab5aebf)#define BT\_UUID\_AICS\_INPUT\_STATUS\_VAL 0x2b7a

[ 4038](group__bt__uuid.md#ga549930ceca2598871f140ec81778923b)#define BT\_UUID\_AICS\_INPUT\_STATUS \

4039 BT\_UUID\_DECLARE\_16(BT\_UUID\_AICS\_INPUT\_STATUS\_VAL)

4040

[ 4043](group__bt__uuid.md#gacd6c279c902bb8dfa59e886f52161f9a)#define BT\_UUID\_AICS\_CONTROL\_VAL 0x2b7b

[ 4047](group__bt__uuid.md#gae507a2c877c174accb4eb1c18fd7bbc4)#define BT\_UUID\_AICS\_CONTROL \

4048 BT\_UUID\_DECLARE\_16(BT\_UUID\_AICS\_CONTROL\_VAL)

4049

[ 4052](group__bt__uuid.md#ga0cb5c04f3f8c257d012d9907ba8cde38)#define BT\_UUID\_AICS\_DESCRIPTION\_VAL 0x2b7c

[ 4056](group__bt__uuid.md#ga9de23aa540a7e07e4c932d60dd84f7c5)#define BT\_UUID\_AICS\_DESCRIPTION \

4057 BT\_UUID\_DECLARE\_16(BT\_UUID\_AICS\_DESCRIPTION\_VAL)

4058

[ 4061](group__bt__uuid.md#ga40235c24d4ab2f3c068e8833295bfb89)#define BT\_UUID\_VCS\_STATE\_VAL 0x2b7d

[ 4065](group__bt__uuid.md#gac116f24a102a7b8e6aa80533cc096615)#define BT\_UUID\_VCS\_STATE \

4066 BT\_UUID\_DECLARE\_16(BT\_UUID\_VCS\_STATE\_VAL)

4067

[ 4070](group__bt__uuid.md#ga303c174785d397db54c53572c421e6d3)#define BT\_UUID\_VCS\_CONTROL\_VAL 0x2b7e

[ 4074](group__bt__uuid.md#ga24d297c008c9679dcb7078f68affe0a1)#define BT\_UUID\_VCS\_CONTROL \

4075 BT\_UUID\_DECLARE\_16(BT\_UUID\_VCS\_CONTROL\_VAL)

4076

[ 4079](group__bt__uuid.md#ga7f3385da26bf4cddfe12f48147457baf)#define BT\_UUID\_VCS\_FLAGS\_VAL 0x2b7f

[ 4083](group__bt__uuid.md#ga47ff83b277e87cf0629a633a67567e34)#define BT\_UUID\_VCS\_FLAGS \

4084 BT\_UUID\_DECLARE\_16(BT\_UUID\_VCS\_FLAGS\_VAL)

4085

[ 4088](group__bt__uuid.md#gae5535cd478c55390fa3c1199584e614d)#define BT\_UUID\_VOCS\_STATE\_VAL 0x2b80

[ 4092](group__bt__uuid.md#ga1d198cbdb65d99eb877fa871f4ac5155)#define BT\_UUID\_VOCS\_STATE \

4093 BT\_UUID\_DECLARE\_16(BT\_UUID\_VOCS\_STATE\_VAL)

4094

[ 4097](group__bt__uuid.md#ga784c29647d14983b3d3f37f9188b6b6f)#define BT\_UUID\_VOCS\_LOCATION\_VAL 0x2b81

[ 4101](group__bt__uuid.md#gad3493dcb58547b4108e8ded6e48e8a8c)#define BT\_UUID\_VOCS\_LOCATION \

4102 BT\_UUID\_DECLARE\_16(BT\_UUID\_VOCS\_LOCATION\_VAL)

4103

[ 4106](group__bt__uuid.md#gacc2e4a9ac1e93bf6ed1a7001c8038a52)#define BT\_UUID\_VOCS\_CONTROL\_VAL 0x2b82

[ 4110](group__bt__uuid.md#gafb68257cf790e12dab2b888320617de7)#define BT\_UUID\_VOCS\_CONTROL \

4111 BT\_UUID\_DECLARE\_16(BT\_UUID\_VOCS\_CONTROL\_VAL)

4112

[ 4115](group__bt__uuid.md#ga46471ebc019b7c842c0b76efed504625)#define BT\_UUID\_VOCS\_DESCRIPTION\_VAL 0x2b83

[ 4119](group__bt__uuid.md#gad4a8b4af9f5935b86d1541a2086609d3)#define BT\_UUID\_VOCS\_DESCRIPTION \

4120 BT\_UUID\_DECLARE\_16(BT\_UUID\_VOCS\_DESCRIPTION\_VAL)

4121

[ 4124](group__bt__uuid.md#gadaf8b170c1f603f8a61515090558b96c)#define BT\_UUID\_CSIS\_SIRK\_VAL 0x2b84

[ 4128](group__bt__uuid.md#gac0a3863cf4a928bfaae397b14771622d)#define BT\_UUID\_CSIS\_SIRK BT\_UUID\_DECLARE\_16(BT\_UUID\_CSIS\_SIRK\_VAL)

[ 4132](group__bt__uuid.md#ga7b5cf381c0806b01fc91c806588a3cfc)#define BT\_UUID\_CSIS\_SET\_SIZE\_VAL 0x2b85

[ 4136](group__bt__uuid.md#ga8995e2ac9173ab613c35f56c5a353d69)#define BT\_UUID\_CSIS\_SET\_SIZE \

4137 BT\_UUID\_DECLARE\_16(BT\_UUID\_CSIS\_SET\_SIZE\_VAL)

4138

[ 4141](group__bt__uuid.md#ga7f296b9f8b09bc62e639b2e1076894dc)#define BT\_UUID\_CSIS\_SET\_LOCK\_VAL 0x2b86

[ 4145](group__bt__uuid.md#gaf6493077e90f87765c1c1efc044436f0)#define BT\_UUID\_CSIS\_SET\_LOCK \

4146 BT\_UUID\_DECLARE\_16(BT\_UUID\_CSIS\_SET\_LOCK\_VAL)

4147

[ 4150](group__bt__uuid.md#ga21db384fb731b1903239a4ecc70138d4)#define BT\_UUID\_CSIS\_RANK\_VAL 0x2b87

[ 4154](group__bt__uuid.md#gaa356de4e79779132ed4eeda837b7db57)#define BT\_UUID\_CSIS\_RANK \

4155 BT\_UUID\_DECLARE\_16(BT\_UUID\_CSIS\_RANK\_VAL)

4156

[ 4159](group__bt__uuid.md#ga31e072f6706b28c309e518cd9449b883)#define BT\_UUID\_GATT\_EDKM\_VAL 0x2b88

[ 4163](group__bt__uuid.md#ga9b0daac4f03e23c10fca1a40d07e1618)#define BT\_UUID\_GATT\_EDKM \

4164 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_EDKM\_VAL)

4165

[ 4168](group__bt__uuid.md#gac74ea8f9e2800086c286c5fa4185a00e)#define BT\_UUID\_GATT\_AE32\_VAL 0x2b89

[ 4172](group__bt__uuid.md#ga646adee056d3097eb180bdea1ad0fd33)#define BT\_UUID\_GATT\_AE32 \

4173 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AE32\_VAL)

4174

[ 4177](group__bt__uuid.md#gac3a8b96b59612b0e4ef704afae04e7e3)#define BT\_UUID\_GATT\_AP\_VAL 0x2b8a

[ 4181](group__bt__uuid.md#ga91eea2c307dfa99632b52d062c2a2645)#define BT\_UUID\_GATT\_AP \

4182 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_AP\_VAL)

4183

[ 4186](group__bt__uuid.md#gaa1edc406495ec9797e153daf1e6cca1f)#define BT\_UUID\_GATT\_CO2CONC\_VAL 0x2b8c

[ 4190](group__bt__uuid.md#gab4db18c78e70c6e781dcda022be13276)#define BT\_UUID\_GATT\_CO2CONC \

4191 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CO2CONC\_VAL)

4192

[ 4195](group__bt__uuid.md#ga7a568dfc0ac219b16bdd606953b88184)#define BT\_UUID\_GATT\_COS\_VAL 0x2b8d

[ 4199](group__bt__uuid.md#ga7d456cc3cdf5d6b25a35f6cca08da585)#define BT\_UUID\_GATT\_COS \

4200 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_COS\_VAL)

4201

[ 4204](group__bt__uuid.md#ga7da79c223cdfb3be45607e86f71a6caa)#define BT\_UUID\_GATT\_DEVTF\_VAL 0x2b8e

[ 4208](group__bt__uuid.md#ga7e8485b07e0c359964be7b6f8e896546)#define BT\_UUID\_GATT\_DEVTF \

4209 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DEVTF\_VAL)

4210

[ 4213](group__bt__uuid.md#ga744f71f5b0c8d2cfe4faf6107f33633b)#define BT\_UUID\_GATT\_DEVTP\_VAL 0x2b8f

[ 4217](group__bt__uuid.md#ga0f22bf31cbe7a58944340b03ccf591c5)#define BT\_UUID\_GATT\_DEVTP \

4218 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DEVTP\_VAL)

4219

[ 4222](group__bt__uuid.md#ga7d0ff38d80780d63e4b43a200be5c7d3)#define BT\_UUID\_GATT\_DEVT\_VAL 0x2b90

[ 4226](group__bt__uuid.md#ga9eb6c84a8ab924deb9fbe5b331d2628a)#define BT\_UUID\_GATT\_DEVT \

4227 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DEVT\_VAL)

4228

[ 4231](group__bt__uuid.md#ga111396f18a4d565fabe50e4ab4bb6b01)#define BT\_UUID\_GATT\_DEVTCP\_VAL 0x2b91

[ 4235](group__bt__uuid.md#ga18de8889aa0297fc80a6fc2846f83da2)#define BT\_UUID\_GATT\_DEVTCP \

4236 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_DEVTCP\_VAL)

4237

[ 4240](group__bt__uuid.md#ga2aa7a226cd54e1e2435a045cd936c222)#define BT\_UUID\_GATT\_TCLD\_VAL 0x2b92

[ 4244](group__bt__uuid.md#ga0e38fdb6334c4aa1b3fe8163cad290ea)#define BT\_UUID\_GATT\_TCLD \

4245 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TCLD\_VAL)

4246

[ 4249](group__bt__uuid.md#ga26421e4fde9e424af8318a2a06e55729)#define BT\_UUID\_MCS\_PLAYER\_NAME\_VAL 0x2b93

[ 4253](group__bt__uuid.md#ga25706c3572dd91b223dd7cbea6cc71e2)#define BT\_UUID\_MCS\_PLAYER\_NAME \

4254 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_PLAYER\_NAME\_VAL)

4255

[ 4258](group__bt__uuid.md#gadefa705eae4221748b18f5a088c768ca)#define BT\_UUID\_MCS\_ICON\_OBJ\_ID\_VAL 0x2b94

[ 4262](group__bt__uuid.md#ga63ce9edebeebcac1e7344efdabc6519e)#define BT\_UUID\_MCS\_ICON\_OBJ\_ID \

4263 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_ICON\_OBJ\_ID\_VAL)

4264

[ 4267](group__bt__uuid.md#gad80db7e88bc50944b71ca4c51f6674db)#define BT\_UUID\_MCS\_ICON\_URL\_VAL 0x2b95

[ 4271](group__bt__uuid.md#ga1ff74274cc34b8ba88af2b455109eb98)#define BT\_UUID\_MCS\_ICON\_URL \

4272 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_ICON\_URL\_VAL)

4273

[ 4276](group__bt__uuid.md#ga71cb9b105eb4a581167e09fb293d7dd5)#define BT\_UUID\_MCS\_TRACK\_CHANGED\_VAL 0x2b96

[ 4280](group__bt__uuid.md#gae7e7b15660158399bd837f10c1380982)#define BT\_UUID\_MCS\_TRACK\_CHANGED \

4281 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_TRACK\_CHANGED\_VAL)

4282

[ 4285](group__bt__uuid.md#ga8082647831b1da4237b85346f1dca249)#define BT\_UUID\_MCS\_TRACK\_TITLE\_VAL 0x2b97

[ 4289](group__bt__uuid.md#gafb41d75e4bf569b1efeba763fb93722f)#define BT\_UUID\_MCS\_TRACK\_TITLE \

4290 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_TRACK\_TITLE\_VAL)

4291

[ 4294](group__bt__uuid.md#ga7786188af799df504bcbba1aa007a3eb)#define BT\_UUID\_MCS\_TRACK\_DURATION\_VAL 0x2b98

[ 4298](group__bt__uuid.md#ga76d4d2c92df6b9d82d60ee7fe835d29c)#define BT\_UUID\_MCS\_TRACK\_DURATION \

4299 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_TRACK\_DURATION\_VAL)

4300

[ 4303](group__bt__uuid.md#ga6b74c773a708eccb84074cb7ef8c8fe2)#define BT\_UUID\_MCS\_TRACK\_POSITION\_VAL 0x2b99

[ 4307](group__bt__uuid.md#gaa4665539c5027680a843d851bf1b8bfe)#define BT\_UUID\_MCS\_TRACK\_POSITION \

4308 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_TRACK\_POSITION\_VAL)

4309

[ 4312](group__bt__uuid.md#gadfe7acf9dbc6ebd3fe21fe469f39e937)#define BT\_UUID\_MCS\_PLAYBACK\_SPEED\_VAL 0x2b9a

[ 4316](group__bt__uuid.md#ga47629d64d3ed4587089fb8551c4c594c)#define BT\_UUID\_MCS\_PLAYBACK\_SPEED \

4317 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_PLAYBACK\_SPEED\_VAL)

4318

[ 4321](group__bt__uuid.md#gaf8ebb66a23e2bed1c7e5b08c79cfe579)#define BT\_UUID\_MCS\_SEEKING\_SPEED\_VAL 0x2b9b

[ 4325](group__bt__uuid.md#gac1d6109a86c67555c4b632d6a0563d92)#define BT\_UUID\_MCS\_SEEKING\_SPEED \

4326 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_SEEKING\_SPEED\_VAL)

4327

[ 4330](group__bt__uuid.md#gafa793d37f3d9c57d1f456a0a9c5dba36)#define BT\_UUID\_MCS\_TRACK\_SEGMENTS\_OBJ\_ID\_VAL 0x2b9c

[ 4334](group__bt__uuid.md#gaa1e0e61ba28da785308e5dafd72931fd)#define BT\_UUID\_MCS\_TRACK\_SEGMENTS\_OBJ\_ID \

4335 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_TRACK\_SEGMENTS\_OBJ\_ID\_VAL)

4336

[ 4339](group__bt__uuid.md#ga884f66865500c127def77f2764b7a322)#define BT\_UUID\_MCS\_CURRENT\_TRACK\_OBJ\_ID\_VAL 0x2b9d

[ 4343](group__bt__uuid.md#gad11916b1a6704ce9cc80a35ddd1b1023)#define BT\_UUID\_MCS\_CURRENT\_TRACK\_OBJ\_ID \

4344 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_CURRENT\_TRACK\_OBJ\_ID\_VAL)

4345

[ 4348](group__bt__uuid.md#ga791f147766bd7511fdeb98ed9f4e3e05)#define BT\_UUID\_MCS\_NEXT\_TRACK\_OBJ\_ID\_VAL 0x2b9e

[ 4352](group__bt__uuid.md#gaba85414e514d71f1ada3cd32ab7b9857)#define BT\_UUID\_MCS\_NEXT\_TRACK\_OBJ\_ID \

4353 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_NEXT\_TRACK\_OBJ\_ID\_VAL)

4354

[ 4357](group__bt__uuid.md#ga06410ca2d5575cb44f3f365c27960487)#define BT\_UUID\_MCS\_PARENT\_GROUP\_OBJ\_ID\_VAL 0x2b9f

[ 4361](group__bt__uuid.md#ga2dbb766bda1581f49ff331beefdad2c5)#define BT\_UUID\_MCS\_PARENT\_GROUP\_OBJ\_ID \

4362 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_PARENT\_GROUP\_OBJ\_ID\_VAL)

4363

[ 4366](group__bt__uuid.md#ga3873c1d5075d4cb3035509ce57595c28)#define BT\_UUID\_MCS\_CURRENT\_GROUP\_OBJ\_ID\_VAL 0x2ba0

[ 4370](group__bt__uuid.md#ga303b89c5ba301bd2c18a3eb48f214ded)#define BT\_UUID\_MCS\_CURRENT\_GROUP\_OBJ\_ID \

4371 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_CURRENT\_GROUP\_OBJ\_ID\_VAL)

4372

[ 4375](group__bt__uuid.md#ga0b17cfa67cdec5722cf51ebc9a616384)#define BT\_UUID\_MCS\_PLAYING\_ORDER\_VAL 0x2ba1

[ 4379](group__bt__uuid.md#ga7c676d7019e19189cffaf34aefe66c59)#define BT\_UUID\_MCS\_PLAYING\_ORDER \

4380 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_PLAYING\_ORDER\_VAL)

4381

[ 4384](group__bt__uuid.md#ga103cd4f0ae88b27c32ab7854c331de59)#define BT\_UUID\_MCS\_PLAYING\_ORDERS\_VAL 0x2ba2

[ 4388](group__bt__uuid.md#ga283a2f22a049a6c78221d1186d17e6f5)#define BT\_UUID\_MCS\_PLAYING\_ORDERS \

4389 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_PLAYING\_ORDERS\_VAL)

4390

[ 4393](group__bt__uuid.md#ga8f62ba6fe627eda5c188151a89d1299f)#define BT\_UUID\_MCS\_MEDIA\_STATE\_VAL 0x2ba3

[ 4397](group__bt__uuid.md#gaadaf94fbf0d316505e27fc115998ffd2)#define BT\_UUID\_MCS\_MEDIA\_STATE \

4398 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_MEDIA\_STATE\_VAL)

4399

[ 4402](group__bt__uuid.md#ga3b276420dc39941339c3f3bcb3835d3c)#define BT\_UUID\_MCS\_MEDIA\_CONTROL\_POINT\_VAL 0x2ba4

[ 4406](group__bt__uuid.md#gae3dc24d21d36349c7af95fe90db6ec91)#define BT\_UUID\_MCS\_MEDIA\_CONTROL\_POINT \

4407 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_MEDIA\_CONTROL\_POINT\_VAL)

4408

[ 4411](group__bt__uuid.md#ga6eb18372f842f362bb45c93bbefd560b)#define BT\_UUID\_MCS\_MEDIA\_CONTROL\_OPCODES\_VAL 0x2ba5

[ 4415](group__bt__uuid.md#ga6ef3d74033d401d7d5fb092485faee16)#define BT\_UUID\_MCS\_MEDIA\_CONTROL\_OPCODES \

4416 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_MEDIA\_CONTROL\_OPCODES\_VAL)

4417

[ 4420](group__bt__uuid.md#ga337509c52a77206589a8208cf6ac3ac0)#define BT\_UUID\_MCS\_SEARCH\_RESULTS\_OBJ\_ID\_VAL 0x2ba6

[ 4424](group__bt__uuid.md#ga2ce71ff006f161cd899fb6b09a98c66f)#define BT\_UUID\_MCS\_SEARCH\_RESULTS\_OBJ\_ID \

4425 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_SEARCH\_RESULTS\_OBJ\_ID\_VAL)

4426

[ 4429](group__bt__uuid.md#gab89e74c66515dfcdffcb4967b3de4f0d)#define BT\_UUID\_MCS\_SEARCH\_CONTROL\_POINT\_VAL 0x2ba7

[ 4433](group__bt__uuid.md#gab7892abc4201dc18da2bd4a2efca1963)#define BT\_UUID\_MCS\_SEARCH\_CONTROL\_POINT \

4434 BT\_UUID\_DECLARE\_16(BT\_UUID\_MCS\_SEARCH\_CONTROL\_POINT\_VAL)

4435

[ 4438](group__bt__uuid.md#ga8f238d8197b3293562809916eb667f27)#define BT\_UUID\_GATT\_E32\_VAL 0x2ba8

[ 4442](group__bt__uuid.md#ga6419bfcbe6cad1f568b9e212d704e7c7)#define BT\_UUID\_GATT\_E32 \

4443 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_E32\_VAL)

4444

[ 4448](group__bt__uuid.md#gaeb12a1e806156ec1b7f945dddce3fa24)#define BT\_UUID\_OTS\_TYPE\_MPL\_ICON\_VAL 0x2ba9

[ 4452](group__bt__uuid.md#ga3b425e5f019ba59d2d76a5d6e9cc16ee)#define BT\_UUID\_OTS\_TYPE\_MPL\_ICON \

4453 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_TYPE\_MPL\_ICON\_VAL)

4454

[ 4457](group__bt__uuid.md#gaf05ecc673eae8b56ce6d5a98e5b22130)#define BT\_UUID\_OTS\_TYPE\_TRACK\_SEGMENT\_VAL 0x2baa

[ 4461](group__bt__uuid.md#ga5f3fdbd12cc804ed0ca811d4bafe1109)#define BT\_UUID\_OTS\_TYPE\_TRACK\_SEGMENT \

4462 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_TYPE\_TRACK\_SEGMENT\_VAL)

4463

[ 4466](group__bt__uuid.md#gaf4094e3381053890f6264d17ff129255)#define BT\_UUID\_OTS\_TYPE\_TRACK\_VAL 0x2bab

[ 4470](group__bt__uuid.md#gafcf9774a2b6aa1081b6c1a03b31a0c07)#define BT\_UUID\_OTS\_TYPE\_TRACK \

4471 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_TYPE\_TRACK\_VAL)

4472

[ 4475](group__bt__uuid.md#gafc689c443c46385aefbca0e1db73f877)#define BT\_UUID\_OTS\_TYPE\_GROUP\_VAL 0x2bac

[ 4479](group__bt__uuid.md#ga7a6fd4221135821cd15a3ba10f33532d)#define BT\_UUID\_OTS\_TYPE\_GROUP \

4480 BT\_UUID\_DECLARE\_16(BT\_UUID\_OTS\_TYPE\_GROUP\_VAL)

4481

[ 4484](group__bt__uuid.md#ga6577476ef4d85191e5d5533f6bb99b2d)#define BT\_UUID\_GATT\_CTEE\_VAL 0x2bad

[ 4488](group__bt__uuid.md#ga985a0ebcc0a61e2c4d9f2f61a7a1afb0)#define BT\_UUID\_GATT\_CTEE \

4489 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CTEE\_VAL)

4490

[ 4493](group__bt__uuid.md#gaca4a23a27a2c06eb10da1a64c617cac1)#define BT\_UUID\_GATT\_ACTEML\_VAL 0x2bae

[ 4497](group__bt__uuid.md#ga51915bb0637c157a67ce4488e46905a6)#define BT\_UUID\_GATT\_ACTEML \

4498 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACTEML\_VAL)

4499

[ 4502](group__bt__uuid.md#gad3ddda1c88208094616608b178bb27ec)#define BT\_UUID\_GATT\_ACTEMTC\_VAL 0x2baf

[ 4506](group__bt__uuid.md#ga47620598a9365d2fc8d70ada1144c9c1)#define BT\_UUID\_GATT\_ACTEMTC \

4507 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACTEMTC\_VAL)

4508

[ 4511](group__bt__uuid.md#ga165c63f8c91f61a9930b3c804f7051b7)#define BT\_UUID\_GATT\_ACTETD\_VAL 0x2bb0

[ 4515](group__bt__uuid.md#ga5a15560d93177634882ff117b35deab4)#define BT\_UUID\_GATT\_ACTETD \

4516 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACTETD\_VAL)

4517

[ 4520](group__bt__uuid.md#ga3be14ce89c7c291cdde2bf1f4ce85808)#define BT\_UUID\_GATT\_ACTEI\_VAL 0x2bb1

[ 4524](group__bt__uuid.md#ga492d6a8c673f4df65d34abad342f4e75)#define BT\_UUID\_GATT\_ACTEI \

4525 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACTEI\_VAL)

4526

[ 4529](group__bt__uuid.md#gac32badacbe9099b6f00d5c3d780cdbfe)#define BT\_UUID\_GATT\_ACTEP\_VAL 0x2bb2

[ 4533](group__bt__uuid.md#gaff802fc0d7358acf3bd4bf3209d7aa15)#define BT\_UUID\_GATT\_ACTEP \

4534 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ACTEP\_VAL)

4535

[ 4538](group__bt__uuid.md#gaca347be4dd1f019c5d7421d7c2c0dd29)#define BT\_UUID\_TBS\_PROVIDER\_NAME\_VAL 0x2bb3

[ 4542](group__bt__uuid.md#gafaff1ecd49123fab18bce167342a0d3e)#define BT\_UUID\_TBS\_PROVIDER\_NAME \

4543 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_PROVIDER\_NAME\_VAL)

4544

[ 4547](group__bt__uuid.md#ga361ef37fd71a78544ffcbfd34ecbff6f)#define BT\_UUID\_TBS\_UCI\_VAL 0x2bb4

[ 4551](group__bt__uuid.md#ga2d4349fc96395f603cada574841a90d2)#define BT\_UUID\_TBS\_UCI \

4552 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_UCI\_VAL)

4553

[ 4556](group__bt__uuid.md#ga066546cd6eb07098643b0fa331b813d3)#define BT\_UUID\_TBS\_TECHNOLOGY\_VAL 0x2bb5

[ 4560](group__bt__uuid.md#ga37ec4aed5afafc2751ef3902f2ef7d73)#define BT\_UUID\_TBS\_TECHNOLOGY \

4561 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_TECHNOLOGY\_VAL)

4562

[ 4565](group__bt__uuid.md#ga5e499b3bcb22b0ddd719aba4fed5c644)#define BT\_UUID\_TBS\_URI\_LIST\_VAL 0x2bb6

[ 4569](group__bt__uuid.md#ga6c76f72b427694a1e1180b0d2a2adb38)#define BT\_UUID\_TBS\_URI\_LIST \

4570 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_URI\_LIST\_VAL)

4571

[ 4574](group__bt__uuid.md#ga44859b71e874ca148e708fde37882c4b)#define BT\_UUID\_TBS\_SIGNAL\_STRENGTH\_VAL 0x2bb7

[ 4578](group__bt__uuid.md#gaf5ebde9e6e4121909d8a165dee7fda3a)#define BT\_UUID\_TBS\_SIGNAL\_STRENGTH \

4579 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_SIGNAL\_STRENGTH\_VAL)

4580

[ 4583](group__bt__uuid.md#ga726edee9ad2a92f2a5687a3320f68f99)#define BT\_UUID\_TBS\_SIGNAL\_INTERVAL\_VAL 0x2bb8

[ 4587](group__bt__uuid.md#ga189f78c9eb6829851ab0497a0e6e3f51)#define BT\_UUID\_TBS\_SIGNAL\_INTERVAL \

4588 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_SIGNAL\_INTERVAL\_VAL)

4589

[ 4592](group__bt__uuid.md#ga1fcc7e36b3ca482eca7572c77fe3bba4)#define BT\_UUID\_TBS\_LIST\_CURRENT\_CALLS\_VAL 0x2bb9

[ 4596](group__bt__uuid.md#gaa5aea84109af0027aae9829169ab7789)#define BT\_UUID\_TBS\_LIST\_CURRENT\_CALLS \

4597 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_LIST\_CURRENT\_CALLS\_VAL)

4598

[ 4601](group__bt__uuid.md#ga01899f1d2f5ec81669b5012ab1448e5b)#define BT\_UUID\_CCID\_VAL 0x2bba

[ 4605](group__bt__uuid.md#gab76981ff7b5fe1949c606e901daa33d3)#define BT\_UUID\_CCID \

4606 BT\_UUID\_DECLARE\_16(BT\_UUID\_CCID\_VAL)

4607

[ 4610](group__bt__uuid.md#ga250a14189efd3cc176ae159de0ab03ed)#define BT\_UUID\_TBS\_STATUS\_FLAGS\_VAL 0x2bbb

[ 4614](group__bt__uuid.md#ga8f465ca9874ff4889614f13fa7057c87)#define BT\_UUID\_TBS\_STATUS\_FLAGS \

4615 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_STATUS\_FLAGS\_VAL)

4616

[ 4619](group__bt__uuid.md#ga89ec945699c44fbbb220fa6798efa986)#define BT\_UUID\_TBS\_INCOMING\_URI\_VAL 0x2bbc

[ 4623](group__bt__uuid.md#gaa11ae7df9db3a1a3576a413db9d70539)#define BT\_UUID\_TBS\_INCOMING\_URI \

4624 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_INCOMING\_URI\_VAL)

4625

[ 4628](group__bt__uuid.md#ga07adb1e98dfdeaa84efeb28a53087286)#define BT\_UUID\_TBS\_CALL\_STATE\_VAL 0x2bbd

[ 4632](group__bt__uuid.md#gaf3c8e758416d2d7d34adb4be895f1ed0)#define BT\_UUID\_TBS\_CALL\_STATE \

4633 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_CALL\_STATE\_VAL)

4634

[ 4637](group__bt__uuid.md#gadc6f999aa7d3ebc821405bac4ed4bf35)#define BT\_UUID\_TBS\_CALL\_CONTROL\_POINT\_VAL 0x2bbe

[ 4641](group__bt__uuid.md#ga9870653514120a07d85e4ea4f0a83f6e)#define BT\_UUID\_TBS\_CALL\_CONTROL\_POINT \

4642 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_CALL\_CONTROL\_POINT\_VAL)

4643

[ 4646](group__bt__uuid.md#ga0e2f14bde4f81d44bdd4171e1bfae68e)#define BT\_UUID\_TBS\_OPTIONAL\_OPCODES\_VAL 0x2bbf

[ 4650](group__bt__uuid.md#ga9c794c63e6c216b9a4a7518207ea7268)#define BT\_UUID\_TBS\_OPTIONAL\_OPCODES \

4651 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_OPTIONAL\_OPCODES\_VAL)

4652

[ 4655](group__bt__uuid.md#gab146e7f4f8b965634967ea7845a7d875)#define BT\_UUID\_TBS\_TERMINATE\_REASON\_VAL 0x2bc0

[ 4659](group__bt__uuid.md#ga5eb69cfa65d293421bd2f6797cf1bdd0)#define BT\_UUID\_TBS\_TERMINATE\_REASON \

4660 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_TERMINATE\_REASON\_VAL)

4661

[ 4664](group__bt__uuid.md#gaee6b14bcbd32f18efc4d7f805455deb1)#define BT\_UUID\_TBS\_INCOMING\_CALL\_VAL 0x2bc1

[ 4668](group__bt__uuid.md#ga4ec4bdf60129003573b79f8ffe993f20)#define BT\_UUID\_TBS\_INCOMING\_CALL \

4669 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_INCOMING\_CALL\_VAL)

4670

[ 4673](group__bt__uuid.md#ga598672b6e2aa0bc58c62ac9755aaf64c)#define BT\_UUID\_TBS\_FRIENDLY\_NAME\_VAL 0x2bc2

[ 4677](group__bt__uuid.md#ga32682d7390ccb0aafd82b57255007749)#define BT\_UUID\_TBS\_FRIENDLY\_NAME \

4678 BT\_UUID\_DECLARE\_16(BT\_UUID\_TBS\_FRIENDLY\_NAME\_VAL)

4679

[ 4682](group__bt__uuid.md#ga24667ed9a87ae7f1b529cfea8515b7f3)#define BT\_UUID\_MICS\_MUTE\_VAL 0x2bc3

[ 4686](group__bt__uuid.md#gada38c5574c186c19c71788d612bb7987)#define BT\_UUID\_MICS\_MUTE \

4687 BT\_UUID\_DECLARE\_16(BT\_UUID\_MICS\_MUTE\_VAL)

4688

[ 4691](group__bt__uuid.md#ga780a810da56da9b9dbba775305f70c69)#define BT\_UUID\_ASCS\_ASE\_SNK\_VAL 0x2bc4

[ 4695](group__bt__uuid.md#ga6542839cbcda51b512d04f1039840964)#define BT\_UUID\_ASCS\_ASE\_SNK \

4696 BT\_UUID\_DECLARE\_16(BT\_UUID\_ASCS\_ASE\_SNK\_VAL)

4697

[ 4700](group__bt__uuid.md#gace1bd537f3ecee4715efde2b68ebce70)#define BT\_UUID\_ASCS\_ASE\_SRC\_VAL 0x2bc5

[ 4704](group__bt__uuid.md#gae520d2f81b0ee284d42e80854217c209)#define BT\_UUID\_ASCS\_ASE\_SRC \

4705 BT\_UUID\_DECLARE\_16(BT\_UUID\_ASCS\_ASE\_SRC\_VAL)

4706

[ 4709](group__bt__uuid.md#ga6eeb6b573908fe77254894cf3efc5378)#define BT\_UUID\_ASCS\_ASE\_CP\_VAL 0x2bc6

[ 4713](group__bt__uuid.md#ga79416b6f0e79ee43bf9b495ec94cca4b)#define BT\_UUID\_ASCS\_ASE\_CP \

4714 BT\_UUID\_DECLARE\_16(BT\_UUID\_ASCS\_ASE\_CP\_VAL)

4715

[ 4718](group__bt__uuid.md#gad66cb5c49c932d3546fb549c6febeaa0)#define BT\_UUID\_BASS\_CONTROL\_POINT\_VAL 0x2bc7

[ 4722](group__bt__uuid.md#ga4d8a9467cf5fce4f6be36d160075984c)#define BT\_UUID\_BASS\_CONTROL\_POINT \

4723 BT\_UUID\_DECLARE\_16(BT\_UUID\_BASS\_CONTROL\_POINT\_VAL)

4724

[ 4727](group__bt__uuid.md#ga6c69b13ecbcca8121e6bbe49b58eb799)#define BT\_UUID\_BASS\_RECV\_STATE\_VAL 0x2bc8

[ 4731](group__bt__uuid.md#ga384b5b68bff445f353762e1e15d85aa4)#define BT\_UUID\_BASS\_RECV\_STATE \

4732 BT\_UUID\_DECLARE\_16(BT\_UUID\_BASS\_RECV\_STATE\_VAL)

4733

[ 4736](group__bt__uuid.md#gac27fec8eb7a757709f647cbaf5b9735f)#define BT\_UUID\_PACS\_SNK\_VAL 0x2bc9

[ 4740](group__bt__uuid.md#gaf103bb8e2866a7ab7df90f8b62d4edcd)#define BT\_UUID\_PACS\_SNK \

4741 BT\_UUID\_DECLARE\_16(BT\_UUID\_PACS\_SNK\_VAL)

4742

[ 4745](group__bt__uuid.md#ga3df681f24778459df49c4f2e8cae6c4b)#define BT\_UUID\_PACS\_SNK\_LOC\_VAL 0x2bca

[ 4749](group__bt__uuid.md#gab54021bccf67751069b0cf5eaef8c61c)#define BT\_UUID\_PACS\_SNK\_LOC \

4750 BT\_UUID\_DECLARE\_16(BT\_UUID\_PACS\_SNK\_LOC\_VAL)

4751

[ 4754](group__bt__uuid.md#gaa7c87310bea3593a8097fa20ec4c2c88)#define BT\_UUID\_PACS\_SRC\_VAL 0x2bcb

[ 4758](group__bt__uuid.md#ga958e64cfd0f6b21095b2de28f3b4a0ee)#define BT\_UUID\_PACS\_SRC \

4759 BT\_UUID\_DECLARE\_16(BT\_UUID\_PACS\_SRC\_VAL)

4760

[ 4763](group__bt__uuid.md#ga13eee95752b5b248888ad0328c2c7f99)#define BT\_UUID\_PACS\_SRC\_LOC\_VAL 0x2bcc

[ 4767](group__bt__uuid.md#ga0c89cb848378466beba18c389286cac7)#define BT\_UUID\_PACS\_SRC\_LOC \

4768 BT\_UUID\_DECLARE\_16(BT\_UUID\_PACS\_SRC\_LOC\_VAL)

4769

[ 4772](group__bt__uuid.md#ga64798749d367c63e3d9ed2d07a236e37)#define BT\_UUID\_PACS\_AVAILABLE\_CONTEXT\_VAL 0x2bcd

[ 4776](group__bt__uuid.md#ga0017f4e6621ba40e51062b8f7c77a634)#define BT\_UUID\_PACS\_AVAILABLE\_CONTEXT \

4777 BT\_UUID\_DECLARE\_16(BT\_UUID\_PACS\_AVAILABLE\_CONTEXT\_VAL)

4778

[ 4781](group__bt__uuid.md#ga63588c6624da5cba5b53e07c869c16ff)#define BT\_UUID\_PACS\_SUPPORTED\_CONTEXT\_VAL 0x2bce

[ 4785](group__bt__uuid.md#ga4f61367e2c6aeac35f2054759389306b)#define BT\_UUID\_PACS\_SUPPORTED\_CONTEXT \

4786 BT\_UUID\_DECLARE\_16(BT\_UUID\_PACS\_SUPPORTED\_CONTEXT\_VAL)

4787

[ 4790](group__bt__uuid.md#ga68bf0922cd7486337b912f8cce89140d)#define BT\_UUID\_GATT\_NH4CONC\_VAL 0x2bcf

[ 4794](group__bt__uuid.md#ga7204a371be3fb10d382ea00bc76b5102)#define BT\_UUID\_GATT\_NH4CONC \

4795 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_NH4CONC\_VAL)

4796

[ 4799](group__bt__uuid.md#ga397cccc077652fe327b7ceab3ccc1f4d)#define BT\_UUID\_GATT\_COCONC\_VAL 0x2bd0

[ 4803](group__bt__uuid.md#gab599f83b69654c1b3be91429d9f7bf32)#define BT\_UUID\_GATT\_COCONC \

4804 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_COCONC\_VAL)

4805

[ 4808](group__bt__uuid.md#ga13ecd6003180e0ed73d7aa80542dddd6)#define BT\_UUID\_GATT\_CH4CONC\_VAL 0x2bd1

[ 4812](group__bt__uuid.md#gad0496cbb8cf296852fe85b7694c1e3a8)#define BT\_UUID\_GATT\_CH4CONC \

4813 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_CH4CONC\_VAL)

4814

[ 4817](group__bt__uuid.md#ga37fdb9197c3003175875337df66c0937)#define BT\_UUID\_GATT\_NO2CONC\_VAL 0x2bd2

[ 4821](group__bt__uuid.md#ga1a0f1553bbf70517af224fd32a5842f6)#define BT\_UUID\_GATT\_NO2CONC \

4822 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_NO2CONC\_VAL)

4823

[ 4826](group__bt__uuid.md#ga2023c3c8c4fdf714a66dc64984a9f198)#define BT\_UUID\_GATT\_NONCH4CONC\_VAL 0x2bd3

[ 4830](group__bt__uuid.md#ga6770e5f7e2f46c604ada573dd8b950e9)#define BT\_UUID\_GATT\_NONCH4CONC \

4831 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_NONCH4CONC\_VAL)

4832

[ 4835](group__bt__uuid.md#ga4a022ea0079ebc09dedf5f472a8755ee)#define BT\_UUID\_GATT\_O3CONC\_VAL 0x2bd4

[ 4839](group__bt__uuid.md#ga23054b696f62c03afb73a0f5286dc2d5)#define BT\_UUID\_GATT\_O3CONC \

4840 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_O3CONC\_VAL)

4841

[ 4844](group__bt__uuid.md#ga8dde1677ff60c1970c427e9b984e24d9)#define BT\_UUID\_GATT\_PM1CONC\_VAL 0x2bd5

[ 4848](group__bt__uuid.md#ga9c39a445bab4603148d4256bcce23a5b)#define BT\_UUID\_GATT\_PM1CONC \

4849 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PM1CONC\_VAL)

4850

[ 4853](group__bt__uuid.md#ga055b7900ffda40c9ec4e1870abc1d855)#define BT\_UUID\_GATT\_PM25CONC\_VAL 0x2bd6

[ 4857](group__bt__uuid.md#ga88d2f1f4afcb89267c713144f84f4f7f)#define BT\_UUID\_GATT\_PM25CONC \

4858 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PM25CONC\_VAL)

4859

[ 4862](group__bt__uuid.md#gaebebc238d90e667f33d2c95690d67376)#define BT\_UUID\_GATT\_PM10CONC\_VAL 0x2bd7

[ 4866](group__bt__uuid.md#ga9668baee783462813c530f411da07890)#define BT\_UUID\_GATT\_PM10CONC \

4867 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_PM10CONC\_VAL)

4868

[ 4871](group__bt__uuid.md#gaf7ee2d08cd80e1d4afc777457217508d)#define BT\_UUID\_GATT\_SO2CONC\_VAL 0x2bd8

[ 4875](group__bt__uuid.md#ga3c7b7be6268bb748f7406737eaa129e2)#define BT\_UUID\_GATT\_SO2CONC \

4876 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SO2CONC\_VAL)

4877

[ 4880](group__bt__uuid.md#gaba0853f84e9e33dd4d7d71ecebc31bb6)#define BT\_UUID\_GATT\_SF6CONC\_VAL 0x2bd9

[ 4884](group__bt__uuid.md#gaf17d7037cdaed65e208df3792f1fd2d3)#define BT\_UUID\_GATT\_SF6CONC \

4885 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SF6CONC\_VAL)

4886

[ 4889](group__bt__uuid.md#gad4967e4904cd371940af8b135da21f47)#define BT\_UUID\_HAS\_HEARING\_AID\_FEATURES\_VAL 0x2bda

[ 4893](group__bt__uuid.md#gaebd2bbb103e6928059f1a76eac55916b)#define BT\_UUID\_HAS\_HEARING\_AID\_FEATURES \

4894 BT\_UUID\_DECLARE\_16(BT\_UUID\_HAS\_HEARING\_AID\_FEATURES\_VAL)

4895

[ 4898](group__bt__uuid.md#ga6fdc731a19072629917ce6ebf28c7fee)#define BT\_UUID\_HAS\_PRESET\_CONTROL\_POINT\_VAL 0x2bdb

[ 4902](group__bt__uuid.md#ga7f3a8eea9e7ee68d8865809a061a0e96)#define BT\_UUID\_HAS\_PRESET\_CONTROL\_POINT \

4903 BT\_UUID\_DECLARE\_16(BT\_UUID\_HAS\_PRESET\_CONTROL\_POINT\_VAL)

4904

[ 4907](group__bt__uuid.md#gae9b2bf949e992c7cd6f1aaaa49888189)#define BT\_UUID\_HAS\_ACTIVE\_PRESET\_INDEX\_VAL 0x2bdc

[ 4911](group__bt__uuid.md#ga9ef9b65a7c9a105798691a2cdffbaf7a)#define BT\_UUID\_HAS\_ACTIVE\_PRESET\_INDEX \

4912 BT\_UUID\_DECLARE\_16(BT\_UUID\_HAS\_ACTIVE\_PRESET\_INDEX\_VAL)

4913

[ 4916](group__bt__uuid.md#gac18b9e325ef1db22774f8da35b888223)#define BT\_UUID\_GATT\_FSTR64\_VAL 0x2bde

[ 4920](group__bt__uuid.md#gac617c317945f2b6d45de15eca1190823)#define BT\_UUID\_GATT\_FSTR64 \

4921 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_FSTR64\_VAL)

4922

[ 4925](group__bt__uuid.md#ga2a3928912a6eed082deac4893fb4f980)#define BT\_UUID\_GATT\_HITEMP\_VAL 0x2bdf

[ 4929](group__bt__uuid.md#ga8d9bad6c04ea4cf096d0d010208e1d2a)#define BT\_UUID\_GATT\_HITEMP \

4930 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_HITEMP\_VAL)

4931

[ 4934](group__bt__uuid.md#ga2b707ca8b876eded6b3adf9bb7132479)#define BT\_UUID\_GATT\_HV\_VAL 0x2be0

[ 4938](group__bt__uuid.md#ga1104d7e9d1571aacdb77693c64a15edc)#define BT\_UUID\_GATT\_HV \

4939 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_HV\_VAL)

4940

[ 4943](group__bt__uuid.md#ga67e534b02154fd7ff94b5ed21616f5f2)#define BT\_UUID\_GATT\_LD\_VAL 0x2be1

[ 4947](group__bt__uuid.md#ga5f68a688a1347d84bd28aa3df7252be9)#define BT\_UUID\_GATT\_LD \

4948 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LD\_VAL)

4949

[ 4952](group__bt__uuid.md#gaa127fa12de6d6a641183641853439708)#define BT\_UUID\_GATT\_LO\_VAL 0x2be2

[ 4956](group__bt__uuid.md#gacc7b122d7a849291a5c9c877acfbd50a)#define BT\_UUID\_GATT\_LO \

4957 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LO\_VAL)

4958

[ 4961](group__bt__uuid.md#ga34f9f97b35397e713f655b888845d443)#define BT\_UUID\_GATT\_LST\_VAL 0x2be3

[ 4965](group__bt__uuid.md#ga2794fa8a9e1030826b4d382cc59f835a)#define BT\_UUID\_GATT\_LST \

4966 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_LST\_VAL)

4967

[ 4970](group__bt__uuid.md#gab3b7b78bfb8b5dfd30a1751ce9ffaee7)#define BT\_UUID\_GATT\_NOISE\_VAL 0x2be4

[ 4974](group__bt__uuid.md#gaeb4d264b70d6d6c87a34f0da320f8e7a)#define BT\_UUID\_GATT\_NOISE \

4975 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_NOISE\_VAL)

4976

[ 4979](group__bt__uuid.md#ga8cbc0843565303e78f564517c21feb0f)#define BT\_UUID\_GATT\_RRCCTP\_VAL 0x2be5

[ 4983](group__bt__uuid.md#ga0f5bffe28d45d35fa2dc6680bc52476d)#define BT\_UUID\_GATT\_RRCCTR \

4984 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_RRCCTR\_VAL)

4985

[ 4988](group__bt__uuid.md#ga9fd1550589d248be145b120c446181ee)#define BT\_UUID\_GATT\_TIM\_S32\_VAL 0x2be6

[ 4992](group__bt__uuid.md#gac76fc378354bcd1a8c706f7438a90ebb)#define BT\_UUID\_GATT\_TIM\_S32 \

4993 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_TIM\_S32\_VAL)

4994

[ 4997](group__bt__uuid.md#gabf10e337b78be1ab371fbef771109c53)#define BT\_UUID\_GATT\_VOCCONC\_VAL 0x2be7

[ 5001](group__bt__uuid.md#ga7181f9f1dfaae6cfe3fd8cedd8c20917)#define BT\_UUID\_GATT\_VOCCONC \

5002 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_VOCCONC\_VAL)

5003

[ 5006](group__bt__uuid.md#ga4c57416ae5e84133339e3fab0ba31918)#define BT\_UUID\_GATT\_VF\_VAL 0x2be8

[ 5010](group__bt__uuid.md#gae8500640959d58da51aee03fa75c85ba)#define BT\_UUID\_GATT\_VF \

5011 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_VF\_VAL)

5012

[ 5015](group__bt__uuid.md#gaad27c84d46c85c4fc436e2d57249e562)#define BT\_UUID\_BAS\_BATTERY\_CRIT\_STATUS\_VAL 0x2be9

[ 5019](group__bt__uuid.md#ga678d5e47dee2070ce9208538c529460b)#define BT\_UUID\_BAS\_BATTERY\_CRIT\_STATUS \

5020 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_BATTERY\_CRIT\_STATUS\_VAL)

5021

[ 5024](group__bt__uuid.md#ga0dd78641b14fa1affa283f3f53a5f194)#define BT\_UUID\_BAS\_BATTERY\_HEALTH\_STATUS\_VAL 0x2bea

[ 5028](group__bt__uuid.md#gaa442c41b04c72f1a7a983e0c6561b90d)#define BT\_UUID\_BAS\_BATTERY\_HEALTH\_STATUS \

5029 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_BATTERY\_HEALTH\_STATUS\_VAL)

5030

[ 5033](group__bt__uuid.md#ga3324d4b7047cab8fb2c033c4c92c5793)#define BT\_UUID\_BAS\_BATTERY\_HEALTH\_INF\_VAL 0x2beb

[ 5037](group__bt__uuid.md#ga62ad5685a1fcbb18afd57c7ded6463a0)#define BT\_UUID\_BAS\_BATTERY\_HEALTH\_INF \

5038 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_BATTERY\_HEALTH\_INF\_VAL)

5039

[ 5042](group__bt__uuid.md#ga04f0ff51790e2c759b401f36a989f6b7)#define BT\_UUID\_BAS\_BATTERY\_INF\_VAL 0x2bec

[ 5046](group__bt__uuid.md#gad6dffe9e9e9684b2a943471e0a6c0918)#define BT\_UUID\_BAS\_BATTERY\_INF \

5047 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_BATTERY\_INF\_VAL)

5048

[ 5051](group__bt__uuid.md#gaf14fdc69148ba65b5fb7fe9d42706787)#define BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATUS\_VAL 0x2bed

[ 5055](group__bt__uuid.md#ga54a26381c17065abbda1eb4c2a35c244)#define BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATUS \

5056 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATUS\_VAL)

5057

[ 5060](group__bt__uuid.md#ga8a1d978914a8cb9c3744b4b333e38f46)#define BT\_UUID\_BAS\_BATTERY\_TIME\_STATUS\_VAL 0x2bee

[ 5064](group__bt__uuid.md#ga25e2b1b84d5b9dd46ae79ab26752a02f)#define BT\_UUID\_BAS\_BATTERY\_TIME\_STATUS \

5065 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_BATTERY\_TIME\_STATUS\_VAL)

5066

[ 5069](group__bt__uuid.md#gaff547b9ef568ae7ae70fdb18cbced21b)#define BT\_UUID\_GATT\_ESD\_VAL 0x2bef

[ 5073](group__bt__uuid.md#ga432ba40acfbe03c50b4a3ede80b972c1)#define BT\_UUID\_GATT\_ESD \

5074 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_ESD\_VAL)

5075

[ 5078](group__bt__uuid.md#ga7af8620512a789611a3c6c96bcbd6c06)#define BT\_UUID\_BAS\_BATTERY\_ENERGY\_STATUS\_VAL 0x2bf0

[ 5082](group__bt__uuid.md#gadc442a139fff871f63d5e11be37c8231)#define BT\_UUID\_BAS\_BATTERY\_ENERGY\_STATUS \

5083 BT\_UUID\_DECLARE\_16(BT\_UUID\_BAS\_BATTERY\_ENERGY\_STATUS\_VAL)

5084

[ 5087](group__bt__uuid.md#ga87e7a8d4ea7c2f0b4345c3ddd83e2bcc)#define BT\_UUID\_GATT\_SL\_VAL 0x2bf5

[ 5091](group__bt__uuid.md#ga07c07b64d8d06b76b64c71109dd39bc4)#define BT\_UUID\_GATT\_SL \

5092 BT\_UUID\_DECLARE\_16(BT\_UUID\_GATT\_SL\_VAL)

5093

[ 5097](group__bt__uuid.md#ga1904b4b736c5949b544cfd3cf270b9a1)#define BT\_UUID\_UDI\_FOR\_MEDICAL\_DEVICES\_VAL 0x2bff

[ 5101](group__bt__uuid.md#ga1d0210d3557a3838a4b04bedf413e80c)#define BT\_UUID\_UDI\_FOR\_MEDICAL\_DEVICES \

5102 BT\_UUID\_DECLARE\_16(BT\_UUID\_UDI\_FOR\_MEDICAL\_DEVICES\_VAL)

5103

[ 5107](group__bt__uuid.md#ga791ebaadcc3fac61cda4001d1dadc044)#define BT\_UUID\_GMAS\_VAL 0x1858

[ 5111](group__bt__uuid.md#gae48cde28242dd2813cb9259a3db4cd0f)#define BT\_UUID\_GMAS BT\_UUID\_DECLARE\_16(BT\_UUID\_GMAS\_VAL)

5112

[ 5116](group__bt__uuid.md#ga8a9ca3e7c352dcc5c6b4834f1c1b188c)#define BT\_UUID\_GMAP\_ROLE\_VAL 0x2C00

[ 5120](group__bt__uuid.md#gacb7897b761dc608e7814a2ad103e47a2)#define BT\_UUID\_GMAP\_ROLE BT\_UUID\_DECLARE\_16(BT\_UUID\_GMAP\_ROLE\_VAL)

5121

[ 5125](group__bt__uuid.md#ga9a79627722acfc4c93b2d251aefd8b83)#define BT\_UUID\_GMAP\_UGG\_FEAT\_VAL 0x2C01

[ 5129](group__bt__uuid.md#gafcdc548a86c976b07fa57bd0ccaee9c9)#define BT\_UUID\_GMAP\_UGG\_FEAT BT\_UUID\_DECLARE\_16(BT\_UUID\_GMAP\_UGG\_FEAT\_VAL)

5130

[ 5134](group__bt__uuid.md#ga24f317039700e33d09f6244d74e4c024)#define BT\_UUID\_GMAP\_UGT\_FEAT\_VAL 0x2C02

[ 5138](group__bt__uuid.md#gaf3b064865efb4e566ea3d00b1de932e1)#define BT\_UUID\_GMAP\_UGT\_FEAT BT\_UUID\_DECLARE\_16(BT\_UUID\_GMAP\_UGT\_FEAT\_VAL)

5139

[ 5143](group__bt__uuid.md#ga5aa7be5ea8b74329c07f7de879e9ab2f)#define BT\_UUID\_GMAP\_BGS\_FEAT\_VAL 0x2C03

[ 5147](group__bt__uuid.md#ga0aa83932e08ed22c1d75464b77e23b0c)#define BT\_UUID\_GMAP\_BGS\_FEAT BT\_UUID\_DECLARE\_16(BT\_UUID\_GMAP\_BGS\_FEAT\_VAL)

5148

[ 5152](group__bt__uuid.md#ga5b7fcf7e18179190c3cd3ec2289ebcd5)#define BT\_UUID\_GMAP\_BGR\_FEAT\_VAL 0x2C04

[ 5156](group__bt__uuid.md#ga0d13271568a11aceb9a6d169cdb6474c)#define BT\_UUID\_GMAP\_BGR\_FEAT BT\_UUID\_DECLARE\_16(BT\_UUID\_GMAP\_BGR\_FEAT\_VAL)

5157

5158/\*

5159 \* Protocol UUIDs

5160 \*/

[ 5161](group__bt__uuid.md#gaa82cf709aaa5986ada534ac4c24aa407)#define BT\_UUID\_SDP\_VAL 0x0001

[ 5162](group__bt__uuid.md#ga82f35da766ed6acfe18de8d119d19859)#define BT\_UUID\_SDP BT\_UUID\_DECLARE\_16(BT\_UUID\_SDP\_VAL)

[ 5163](group__bt__uuid.md#gab0d4e8012eef2d067b63e8e538d6317c)#define BT\_UUID\_UDP\_VAL 0x0002

[ 5164](group__bt__uuid.md#ga51e5cf4018099907c64eabf219a193c8)#define BT\_UUID\_UDP BT\_UUID\_DECLARE\_16(BT\_UUID\_UDP\_VAL)

[ 5165](group__bt__uuid.md#ga71dd44d6977cc000c00a6176f71053c9)#define BT\_UUID\_RFCOMM\_VAL 0x0003

[ 5166](group__bt__uuid.md#gafce3f7dd2fbd02c3a549f46395253cde)#define BT\_UUID\_RFCOMM BT\_UUID\_DECLARE\_16(BT\_UUID\_RFCOMM\_VAL)

[ 5167](group__bt__uuid.md#gab4dac3d360e3428cc0b66e34bea75285)#define BT\_UUID\_TCP\_VAL 0x0004

[ 5168](group__bt__uuid.md#ga419519758947e29b8ded5209b1c47743)#define BT\_UUID\_TCP BT\_UUID\_DECLARE\_16(BT\_UUID\_TCP\_VAL)

[ 5169](group__bt__uuid.md#gab7f9b345cb85f922840e6e21722c3373)#define BT\_UUID\_TCS\_BIN\_VAL 0x0005

[ 5170](group__bt__uuid.md#ga5c9bd29f560d84a30c0cb009ccfdc36a)#define BT\_UUID\_TCS\_BIN BT\_UUID\_DECLARE\_16(BT\_UUID\_TCS\_BIN\_VAL)

[ 5171](group__bt__uuid.md#ga09236e2cc7267043f47445e7b233bc38)#define BT\_UUID\_TCS\_AT\_VAL 0x0006

[ 5172](group__bt__uuid.md#ga7c31eb642d9cb8231de38f25c43ef23f)#define BT\_UUID\_TCS\_AT BT\_UUID\_DECLARE\_16(BT\_UUID\_TCS\_AT\_VAL)

[ 5173](group__bt__uuid.md#ga675b73753e13c6c6dbbc5f655b23e466)#define BT\_UUID\_ATT\_VAL 0x0007

[ 5174](group__bt__uuid.md#gaa91cf6c6639156a4b5c67041d479d555)#define BT\_UUID\_ATT BT\_UUID\_DECLARE\_16(BT\_UUID\_ATT\_VAL)

[ 5175](group__bt__uuid.md#gab63382153f97c79f7cdcdfa0a264d6e7)#define BT\_UUID\_OBEX\_VAL 0x0008

[ 5176](group__bt__uuid.md#ga8f660c1d39057815d0420d2dce00639e)#define BT\_UUID\_OBEX BT\_UUID\_DECLARE\_16(BT\_UUID\_OBEX\_VAL)

[ 5177](group__bt__uuid.md#ga5bd66bfdd6ee1f68dd2447aed448d860)#define BT\_UUID\_IP\_VAL 0x0009

[ 5178](group__bt__uuid.md#gad0469b885ffe7be0ff1bef7feb2395d5)#define BT\_UUID\_IP BT\_UUID\_DECLARE\_16(BT\_UUID\_IP\_VAL)

[ 5179](group__bt__uuid.md#gad8ecc3b05eb61d0a3da8daa38deb3887)#define BT\_UUID\_FTP\_VAL 0x000a

[ 5180](group__bt__uuid.md#gada757111154b60d3dbb375192ec48a0f)#define BT\_UUID\_FTP BT\_UUID\_DECLARE\_16(BT\_UUID\_FTP\_VAL)

[ 5181](group__bt__uuid.md#gafd11ab75ca80c343f894db89779419d4)#define BT\_UUID\_HTTP\_VAL 0x000c

[ 5182](group__bt__uuid.md#ga34afe0fe521f95f82f0c86e0de8c1d93)#define BT\_UUID\_HTTP BT\_UUID\_DECLARE\_16(BT\_UUID\_HTTP\_VAL)

[ 5183](group__bt__uuid.md#gac095fdb1bc8d0a07737061b428e12071)#define BT\_UUID\_WSP\_VAL 0x000e

[ 5184](group__bt__uuid.md#ga8f0f3c9e5ef2b6a313ed742a8f7ed0bd)#define BT\_UUID\_WSP BT\_UUID\_DECLARE\_16(BT\_UUID\_WSP\_VAL)

[ 5185](group__bt__uuid.md#gacf6c5a3e20d50500cca56daf5802faf5)#define BT\_UUID\_BNEP\_VAL 0x000f

[ 5186](group__bt__uuid.md#ga9bd1756830328cacd40fc8bf80ee176d)#define BT\_UUID\_BNEP BT\_UUID\_DECLARE\_16(BT\_UUID\_BNEP\_VAL)

[ 5187](group__bt__uuid.md#ga0dac826a9f670d1eba071603723fd3f5)#define BT\_UUID\_UPNP\_VAL 0x0010

[ 5188](group__bt__uuid.md#ga3f7ade885937ba780b0074516c180c42)#define BT\_UUID\_UPNP BT\_UUID\_DECLARE\_16(BT\_UUID\_UPNP\_VAL)

[ 5189](group__bt__uuid.md#gac30ff318ffebd4a6793a0267de6b84e9)#define BT\_UUID\_HIDP\_VAL 0x0011

[ 5190](group__bt__uuid.md#ga9cbd452d2c4fa9fae46cd39bb8133ea2)#define BT\_UUID\_HIDP BT\_UUID\_DECLARE\_16(BT\_UUID\_HIDP\_VAL)

[ 5191](group__bt__uuid.md#gaccdbcd9b4ab68185c4ba213d2b83fcf2)#define BT\_UUID\_HCRP\_CTRL\_VAL 0x0012

[ 5192](group__bt__uuid.md#ga731221f8f6711a400aa0e7c39c8520ea)#define BT\_UUID\_HCRP\_CTRL BT\_UUID\_DECLARE\_16(BT\_UUID\_HCRP\_CTRL\_VAL)

[ 5193](group__bt__uuid.md#ga61619a474d5278d79bf66fcda77076f6)#define BT\_UUID\_HCRP\_DATA\_VAL 0x0014

[ 5194](group__bt__uuid.md#ga0bd9a371c57ecc22cfb40b31025cc69e)#define BT\_UUID\_HCRP\_DATA BT\_UUID\_DECLARE\_16(BT\_UUID\_HCRP\_DATA\_VAL)

[ 5195](group__bt__uuid.md#ga99a3d8dfd8f46ece85f3fa5be8c94a64)#define BT\_UUID\_HCRP\_NOTE\_VAL 0x0016

[ 5196](group__bt__uuid.md#ga85372fbf20b7d83fdf5e780487f14974)#define BT\_UUID\_HCRP\_NOTE BT\_UUID\_DECLARE\_16(BT\_UUID\_HCRP\_NOTE\_VAL)

[ 5197](group__bt__uuid.md#ga07ce8ad97e49eb94eb08a75b8fa555ca)#define BT\_UUID\_AVCTP\_VAL 0x0017

[ 5198](group__bt__uuid.md#ga1b172e9a094474f5d7fe6b1b46dbc93e)#define BT\_UUID\_AVCTP BT\_UUID\_DECLARE\_16(BT\_UUID\_AVCTP\_VAL)

[ 5199](group__bt__uuid.md#ga4d08c3f7d19718e9107414d111940b43)#define BT\_UUID\_AVCTP\_BROWSING\_VAL 0x0018

[ 5200](group__bt__uuid.md#gae3f1b0e418dc12a1ef4c2d2f4f35c485)#define BT\_UUID\_AVCTP\_BROWSING BT\_UUID\_DECLARE\_16(BT\_UUID\_AVCTP\_BROWSING\_VAL)

[ 5201](group__bt__uuid.md#ga2e2934e79054324cec077903c07108ad)#define BT\_UUID\_AVDTP\_VAL 0x0019

[ 5202](group__bt__uuid.md#ga926c1d29d7655320c3b89558ec5b3d2f)#define BT\_UUID\_AVDTP BT\_UUID\_DECLARE\_16(BT\_UUID\_AVDTP\_VAL)

[ 5203](group__bt__uuid.md#gae83a731e34ef81a8340f9c5919ad0c6f)#define BT\_UUID\_CMTP\_VAL 0x001b

[ 5204](group__bt__uuid.md#gaa70481ddcb90e8232b3397580c5927a0)#define BT\_UUID\_CMTP BT\_UUID\_DECLARE\_16(BT\_UUID\_CMTP\_VAL)

[ 5205](group__bt__uuid.md#ga477f7e4e7baffa502a0d8ded852ec2e7)#define BT\_UUID\_UDI\_VAL 0x001d

[ 5206](group__bt__uuid.md#gaae2132eeff69adb594365a0af0419695)#define BT\_UUID\_UDI BT\_UUID\_DECLARE\_16(BT\_UUID\_UDI\_VAL)

[ 5207](group__bt__uuid.md#ga9a893aa35fe599d26b6dcfd9bd0fcb2e)#define BT\_UUID\_MCAP\_CTRL\_VAL 0x001e

[ 5208](group__bt__uuid.md#ga1f576ec8576152a951d44a87b8406514)#define BT\_UUID\_MCAP\_CTRL BT\_UUID\_DECLARE\_16(BT\_UUID\_MCAP\_CTRL\_VAL)

[ 5209](group__bt__uuid.md#gabc9726eea06d6f3cea2de134f62fb4f1)#define BT\_UUID\_MCAP\_DATA\_VAL 0x001f

[ 5210](group__bt__uuid.md#gab5607157844471d48d2d1db3e295cee3)#define BT\_UUID\_MCAP\_DATA BT\_UUID\_DECLARE\_16(BT\_UUID\_MCAP\_DATA\_VAL)

[ 5211](group__bt__uuid.md#ga64e0b2fde8593ae40dfc0d661240abb4)#define BT\_UUID\_L2CAP\_VAL 0x0100

[ 5212](group__bt__uuid.md#ga17007ef5a1e355f912af78f909a1d971)#define BT\_UUID\_L2CAP BT\_UUID\_DECLARE\_16(BT\_UUID\_L2CAP\_VAL)

5213

5214

[ 5225](group__bt__uuid.md#gafe17513c1f91cb3f3e61648b71620c6b)int [bt\_uuid\_cmp](group__bt__uuid.md#gafe17513c1f91cb3f3e61648b71620c6b)(const struct [bt\_uuid](structbt__uuid.md) \*u1, const struct [bt\_uuid](structbt__uuid.md) \*u2);

5226

[ 5239](group__bt__uuid.md#ga9e260584efcc111eb3ee02bf78f01881)bool [bt\_uuid\_create](group__bt__uuid.md#ga9e260584efcc111eb3ee02bf78f01881)(struct [bt\_uuid](structbt__uuid.md) \*[uuid](structuuid.md), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_len);

5240

[ 5250](group__bt__uuid.md#gab5ef78dd2263f08de16a0f1e764df657)void [bt\_uuid\_to\_str](group__bt__uuid.md#gab5ef78dd2263f08de16a0f1e764df657)(const struct [bt\_uuid](structbt__uuid.md) \*[uuid](structuuid.md), char \*str, size\_t len);

5251

5252#ifdef \_\_cplusplus

5253}

5254#endif

5255

5259

5260#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_UUID\_H\_ \*/

[byteorder.h](bluetooth_2byteorder_8h.md)

Bluetooth byteorder API.

[BT\_UUID\_SIZE\_128](group__bt__uuid.md#ga86fdce8e63c0f8208bea6b0f2584eb67)

#define BT\_UUID\_SIZE\_128

Size in octets of a 128-bit UUID.

**Definition** uuid.h:47

[bt\_uuid\_create](group__bt__uuid.md#ga9e260584efcc111eb3ee02bf78f01881)

bool bt\_uuid\_create(struct bt\_uuid \*uuid, const uint8\_t \*data, uint8\_t data\_len)

Create a bt\_uuid from a little-endian data buffer.

[bt\_uuid\_to\_str](group__bt__uuid.md#gab5ef78dd2263f08de16a0f1e764df657)

void bt\_uuid\_to\_str(const struct bt\_uuid \*uuid, char \*str, size\_t len)

Convert Bluetooth UUID to string.

[bt\_uuid\_cmp](group__bt__uuid.md#gafe17513c1f91cb3f3e61648b71620c6b)

int bt\_uuid\_cmp(const struct bt\_uuid \*u1, const struct bt\_uuid \*u2)

Compare Bluetooth UUIDs.

[BT\_UUID\_TYPE\_32](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a27382df27b8098bf6144021c1b23c4c8)

@ BT\_UUID\_TYPE\_32

UUID type 32-bit.

**Definition** uuid.h:35

[BT\_UUID\_TYPE\_128](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a786cbb74a1d74c77cb31ff3c4da45517)

@ BT\_UUID\_TYPE\_128

UUID type 128-bit.

**Definition** uuid.h:37

[BT\_UUID\_TYPE\_16](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a8a5a0c5b6310aff10b182daec0e452ba)

@ BT\_UUID\_TYPE\_16

UUID type 16-bit.

**Definition** uuid.h:33

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_uuid\_128](structbt__uuid__128.md)

**Definition** uuid.h:68

[bt\_uuid\_128::val](structbt__uuid__128.md#a0918addaa7afaf1eeb864d5ec40bd59a)

uint8\_t val[16]

UUID value, 128-bit in little-endian format.

**Definition** uuid.h:72

[bt\_uuid\_128::uuid](structbt__uuid__128.md#a3b8fd8a362ed8fd9eabcfa5bffa9eeee)

struct bt\_uuid uuid

UUID generic type.

**Definition** uuid.h:70

[bt\_uuid\_16](structbt__uuid__16.md)

**Definition** uuid.h:54

[bt\_uuid\_16::uuid](structbt__uuid__16.md#a08f8a5e0eadf1ef2c4c917a5dd3db191)

struct bt\_uuid uuid

UUID generic type.

**Definition** uuid.h:56

[bt\_uuid\_16::val](structbt__uuid__16.md#a13ee02ec58cf5fdede249aa8b20a1a9a)

uint16\_t val

UUID value, 16-bit in host endianness.

**Definition** uuid.h:58

[bt\_uuid\_32](structbt__uuid__32.md)

**Definition** uuid.h:61

[bt\_uuid\_32::val](structbt__uuid__32.md#a56e991966643c9a1ca689986e57e6bfc)

uint32\_t val

UUID value, 32-bit in host endianness.

**Definition** uuid.h:65

[bt\_uuid\_32::uuid](structbt__uuid__32.md#ae37fff06890b200895d559ef42d454e2)

struct bt\_uuid uuid

UUID generic type.

**Definition** uuid.h:63

[bt\_uuid](structbt__uuid.md)

This is a 'tentative' type and should be used as a pointer only.

**Definition** uuid.h:50

[bt\_uuid::type](structbt__uuid.md#abac3a8b54416cbd89ff55f8f82902dcb)

uint8\_t type

**Definition** uuid.h:51

[uuid](structuuid.md)

Binary representation of a UUID.

**Definition** uuid.h:48

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [uuid.h](bluetooth_2uuid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
