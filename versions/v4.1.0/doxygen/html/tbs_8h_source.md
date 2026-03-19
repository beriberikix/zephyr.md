---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tbs_8h_source.html
original_path: doxygen/html/tbs_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tbs.h

[Go to the documentation of this file.](tbs_8h.md)

1

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_TBS\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_TBS\_H\_

13

28

29#include <[stdint.h](stdint_8h.md)>

30#include <[stdbool.h](stdbool_8h.md)>

31

32#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

33#include <[zephyr/sys/slist.h](slist_8h.md)>

34#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

35

36#ifdef \_\_cplusplus

37extern "C" {

38#endif

39

[ 45](group__bt__tbs.md#ga829309945831c0e8ac36c3dd79ae26f3)#define BT\_TBS\_CALL\_STATE\_INCOMING 0x00

[ 50](group__bt__tbs.md#ga482f9627308cad1e56a4a5a5906c2308)#define BT\_TBS\_CALL\_STATE\_DIALING 0x01

[ 52](group__bt__tbs.md#gada61fd749f2119452429dd712d283dad)#define BT\_TBS\_CALL\_STATE\_ALERTING 0x02

[ 54](group__bt__tbs.md#ga3100ab7a7db823d86198847ec0df4adc)#define BT\_TBS\_CALL\_STATE\_ACTIVE 0x03

[ 59](group__bt__tbs.md#gac900fe331fe5b81d7ed0b21796d3e16c)#define BT\_TBS\_CALL\_STATE\_LOCALLY\_HELD 0x04

[ 64](group__bt__tbs.md#ga76acd3539931a32361fd0deb3bbe8243)#define BT\_TBS\_CALL\_STATE\_REMOTELY\_HELD 0x05

[ 66](group__bt__tbs.md#ga0d28984faadc6904f72068df6ab6c97d)#define BT\_TBS\_CALL\_STATE\_LOCALLY\_AND\_REMOTELY\_HELD 0x06

68

[ 74](group__bt__tbs.md#gaf7f2abd7e794806ab6b119bee47db6c6)#define BT\_TBS\_REASON\_BAD\_REMOTE\_URI 0x00

[ 76](group__bt__tbs.md#gacd5a09f5786e01662e29d49aa5307046)#define BT\_TBS\_REASON\_CALL\_FAILED 0x01

[ 78](group__bt__tbs.md#ga4bc073b85c6eca1f0a4b0757e1050dde)#define BT\_TBS\_REASON\_REMOTE\_ENDED\_CALL 0x02

[ 80](group__bt__tbs.md#gaa4f89b5fa61dcc4ee7e4fb6ae0e12384)#define BT\_TBS\_REASON\_SERVER\_ENDED\_CALL 0x03

[ 82](group__bt__tbs.md#ga3105e7b0b91b71eb55c1ea5c3bfd6df3)#define BT\_TBS\_REASON\_LINE\_BUSY 0x04

[ 84](group__bt__tbs.md#gae195db56d2cd949a29d261c5473eea89)#define BT\_TBS\_REASON\_NETWORK\_CONGESTED 0x05

[ 86](group__bt__tbs.md#ga614adc266444030ac83dc6f4d2e89563)#define BT\_TBS\_REASON\_CLIENT\_TERMINATED 0x06

[ 88](group__bt__tbs.md#ga137b813cf902c8209a624c6ae8d4a93b)#define BT\_TBS\_REASON\_NO\_SERVICE 0x07

[ 90](group__bt__tbs.md#ga893d3c79ca62c5e5487d7ca7cd403ce2)#define BT\_TBS\_REASON\_NO\_ANSWER 0x08

[ 92](group__bt__tbs.md#gaa4dab0b5c08dcf092a125986519a7d55)#define BT\_TBS\_REASON\_UNSPECIFIED 0x09

94

[ 100](group__bt__tbs.md#gaa92fdb19227ee0b268f2395f3f6a5f63)#define BT\_TBS\_RESULT\_CODE\_SUCCESS 0x00

[ 102](group__bt__tbs.md#gafac3c970b36f37c815c4370dfef89f09)#define BT\_TBS\_RESULT\_CODE\_OPCODE\_NOT\_SUPPORTED 0x01

[ 104](group__bt__tbs.md#gae83a73a5a0474a62dfbcb5ced6eb3f78)#define BT\_TBS\_RESULT\_CODE\_OPERATION\_NOT\_POSSIBLE 0x02

[ 106](group__bt__tbs.md#gadc371a3a898b3ecac56d8778109f315d)#define BT\_TBS\_RESULT\_CODE\_INVALID\_CALL\_INDEX 0x03

[ 111](group__bt__tbs.md#ga3fa49179525369502018912115c1ccce)#define BT\_TBS\_RESULT\_CODE\_STATE\_MISMATCH 0x04

[ 113](group__bt__tbs.md#ga148585f5cfe8b1cd7f8db404dac91cdd)#define BT\_TBS\_RESULT\_CODE\_OUT\_OF\_RESOURCES 0x05

[ 115](group__bt__tbs.md#gaa60f75b90f461246b2f470930a60efc2)#define BT\_TBS\_RESULT\_CODE\_INVALID\_URI 0x06

117

[ 126](group__bt__tbs.md#gabb6c3b57d7c48620b0f019992c55e585)#define BT\_TBS\_FEATURE\_HOLD BIT(0)

[ 128](group__bt__tbs.md#ga962ce8d27abbdc48adbc01b2c68cb042)#define BT\_TBS\_FEATURE\_JOIN BIT(1)

[ 130](group__bt__tbs.md#gadd72fdfd22c6a3abca8a270aae6a689a)#define BT\_TBS\_FEATURE\_ALL (BT\_TBS\_FEATURE\_HOLD | BT\_TBS\_FEATURE\_JOIN)

132

[ 138](group__bt__tbs.md#ga310c1cdffee350fe5235b3ad929ac715)#define BT\_TBS\_SIGNAL\_STRENGTH\_NO\_SERVICE 0

[ 140](group__bt__tbs.md#gae619d9096b41690ba77ee3e7bd838be3)#define BT\_TBS\_SIGNAL\_STRENGTH\_MAX 100

[ 142](group__bt__tbs.md#gab8a433da27a61cf1c7be2fc7b006e298)#define BT\_TBS\_SIGNAL\_STRENGTH\_UNKNOWN 255

144

[ 150](group__bt__tbs.md#gaf125f3486c88517c9e1e218c6ce492e4)#define BT\_TBS\_TECHNOLOGY\_3G 0x01

[ 152](group__bt__tbs.md#ga967b2b97a2e862f5ae235fc9b728b15c)#define BT\_TBS\_TECHNOLOGY\_4G 0x02

[ 154](group__bt__tbs.md#ga6962ce833da01b3a584528b2ce361447)#define BT\_TBS\_TECHNOLOGY\_LTE 0x03

[ 156](group__bt__tbs.md#ga02af096f1153eed9623f7a7324956e86)#define BT\_TBS\_TECHNOLOGY\_WIFI 0x04

[ 158](group__bt__tbs.md#ga28c1928de97f2b7f0e7e36bfe1a5bdde)#define BT\_TBS\_TECHNOLOGY\_5G 0x05

[ 160](group__bt__tbs.md#gad530e2c9b8b616a9674012ecc801421f)#define BT\_TBS\_TECHNOLOGY\_GSM 0x06

[ 162](group__bt__tbs.md#gaeb6d5ed9dcdba0849f81413ef08570bc)#define BT\_TBS\_TECHNOLOGY\_CDMA 0x07

[ 164](group__bt__tbs.md#gafcb1e805e56eb93f6a19b63f2cbf524c)#define BT\_TBS\_TECHNOLOGY\_2G 0x08

[ 166](group__bt__tbs.md#ga3b828481ce60034abbdab8aa4b1ae972)#define BT\_TBS\_TECHNOLOGY\_WCDMA 0x09

168

[ 174](group__bt__tbs.md#gadc590b9f5813e190fa14644412aee25c)#define BT\_TBS\_STATUS\_FLAG\_INBAND\_RINGTONE BIT(0)

[ 176](group__bt__tbs.md#ga53dfa36830f8c562711d9c6f9111929e)#define BT\_TBS\_STATUS\_FLAG\_SILENT\_MOD BIT(1)

178

[ 184](group__bt__tbs.md#ga74344c01327304f1d2da050ddc589735)#define BT\_TBS\_CALL\_FLAG\_OUTGOING BIT(0)

[ 186](group__bt__tbs.md#ga25ff3c36aaabc5e37b08acc62ac21be6)#define BT\_TBS\_CALL\_FLAG\_WITHHELD BIT(1)

[ 188](group__bt__tbs.md#ga466c1c3c50e82fee9e5c8323e89be414)#define BT\_TBS\_CALL\_FLAG\_WITHHELD\_BY\_NETWORK BIT(2)

190

[ 197](group__bt__tbs.md#ga25aa807f2e3a01d030edf4f064a4fbfd)#define BT\_TBS\_GTBS\_INDEX 0xFF

198

200struct bt\_tbs\_instance;

201

[ 212](group__bt__tbs.md#ga60e9e143f247bb7e668293f0233ce300)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_tbs\_originate\_call\_cb](group__bt__tbs.md#ga60e9e143f247bb7e668293f0233ce300))(struct bt\_conn \*conn,

213 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index,

214 const char \*uri);

215

[ 225](group__bt__tbs.md#ga69e93b48b2a48e8a6552882660b791cc)typedef void (\*[bt\_tbs\_terminate\_call\_cb](group__bt__tbs.md#ga69e93b48b2a48e8a6552882660b791cc))(struct bt\_conn \*conn,

226 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index,

227 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

228

[ 236](group__bt__tbs.md#gaa45b3f4837165d722c2df6f202a39058)typedef void (\*[bt\_tbs\_join\_calls\_cb](group__bt__tbs.md#gaa45b3f4837165d722c2df6f202a39058))(struct bt\_conn \*conn,

237 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index\_count,

238 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes);

239

[ 246](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1)typedef void (\*[bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1))(struct bt\_conn \*conn,

247 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

248

[ 256](group__bt__tbs.md#ga1cc9e7140531b07bf6a8dedbc17f24c0)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_tbs\_authorize\_cb](group__bt__tbs.md#ga1cc9e7140531b07bf6a8dedbc17f24c0))(struct bt\_conn \*conn);

257

[ 263](structbt__tbs__cb.md)struct [bt\_tbs\_cb](structbt__tbs__cb.md) {

[ 265](structbt__tbs__cb.md#a566504bee9c7334c53a23223e544855f) [bt\_tbs\_originate\_call\_cb](group__bt__tbs.md#ga60e9e143f247bb7e668293f0233ce300) [originate\_call](structbt__tbs__cb.md#a566504bee9c7334c53a23223e544855f);

[ 267](structbt__tbs__cb.md#ab065a5c58db19feb2a1d3013983ed5aa) [bt\_tbs\_terminate\_call\_cb](group__bt__tbs.md#ga69e93b48b2a48e8a6552882660b791cc) [terminate\_call](structbt__tbs__cb.md#ab065a5c58db19feb2a1d3013983ed5aa);

[ 269](structbt__tbs__cb.md#a8b76dd9243e97d22e0d6c2ac578aa383) [bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1) [hold\_call](structbt__tbs__cb.md#a8b76dd9243e97d22e0d6c2ac578aa383);

[ 271](structbt__tbs__cb.md#a798c09c04a563800c4d9328c1d9e2de6) [bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1) [accept\_call](structbt__tbs__cb.md#a798c09c04a563800c4d9328c1d9e2de6);

[ 273](structbt__tbs__cb.md#ad543a2f26d1749eba0774e2352b53692) [bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1) [retrieve\_call](structbt__tbs__cb.md#ad543a2f26d1749eba0774e2352b53692);

[ 275](structbt__tbs__cb.md#ac1a99a703687a3ef5ebc12eca5f6c2e7) [bt\_tbs\_join\_calls\_cb](group__bt__tbs.md#gaa45b3f4837165d722c2df6f202a39058) [join\_calls](structbt__tbs__cb.md#ac1a99a703687a3ef5ebc12eca5f6c2e7);

[ 277](structbt__tbs__cb.md#ab7c859ffaebcf16db71c5d54bd4f5802) [bt\_tbs\_authorize\_cb](group__bt__tbs.md#ga1cc9e7140531b07bf6a8dedbc17f24c0) [authorize](structbt__tbs__cb.md#ab7c859ffaebcf16db71c5d54bd4f5802);

278};

279

[ 288](group__bt__tbs.md#ga1b942bcf8287641f9cd53824b4d6e77b)int [bt\_tbs\_accept](group__bt__tbs.md#ga1b942bcf8287641f9cd53824b4d6e77b)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

289

[ 298](group__bt__tbs.md#gab72044a1f5466114b5efb88dfcd2f097)int [bt\_tbs\_hold](group__bt__tbs.md#gab72044a1f5466114b5efb88dfcd2f097)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

299

[ 308](group__bt__tbs.md#gad0b45af09b82d6cd66a8481c0e67e04e)int [bt\_tbs\_retrieve](group__bt__tbs.md#gad0b45af09b82d6cd66a8481c0e67e04e)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

309

[ 318](group__bt__tbs.md#ga82553640882ac74f9af84bfe09ff47ee)int [bt\_tbs\_terminate](group__bt__tbs.md#ga82553640882ac74f9af84bfe09ff47ee)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

319

[ 331](group__bt__tbs.md#gadeae51d7cecd80abcdcde1195bb1dfba)int [bt\_tbs\_originate](group__bt__tbs.md#gadeae51d7cecd80abcdcde1195bb1dfba)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, char \*uri, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_index);

332

[ 342](group__bt__tbs.md#ga23226d41e3b98a53ec9a9c2fa346c9ac)int [bt\_tbs\_join](group__bt__tbs.md#ga23226d41e3b98a53ec9a9c2fa346c9ac)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index\_cnt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes);

343

[ 352](group__bt__tbs.md#ga868b83450f7425e8a0c8cfb7c1de45d8)int [bt\_tbs\_remote\_answer](group__bt__tbs.md#ga868b83450f7425e8a0c8cfb7c1de45d8)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

353

[ 362](group__bt__tbs.md#ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e)int [bt\_tbs\_remote\_hold](group__bt__tbs.md#ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

363

[ 372](group__bt__tbs.md#ga09a3e64040819b6b8b694b94d2f62ca0)int [bt\_tbs\_remote\_retrieve](group__bt__tbs.md#ga09a3e64040819b6b8b694b94d2f62ca0)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

373

[ 382](group__bt__tbs.md#ga52afc7b8a22b071dbac10057579f319c)int [bt\_tbs\_remote\_terminate](group__bt__tbs.md#ga52afc7b8a22b071dbac10057579f319c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

383

[ 395](group__bt__tbs.md#ga47939f557e4d6503af9b7b85aff9d60f)int [bt\_tbs\_remote\_incoming](group__bt__tbs.md#ga47939f557e4d6503af9b7b85aff9d60f)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*to,

396 const char \*from, const char \*friendly\_name);

397

[ 408](group__bt__tbs.md#ga5118db6b23b387956e75eda8aecd53d5)int [bt\_tbs\_set\_bearer\_provider\_name](group__bt__tbs.md#ga5118db6b23b387956e75eda8aecd53d5)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*name);

409

[ 420](group__bt__tbs.md#gaf4c576b8aa599f1bd9598964bc1b779f)int [bt\_tbs\_set\_bearer\_technology](group__bt__tbs.md#gaf4c576b8aa599f1bd9598964bc1b779f)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_technology);

421

[ 432](group__bt__tbs.md#gac316adedf7fda441ee55feb9d24d1a94)int [bt\_tbs\_set\_signal\_strength](group__bt__tbs.md#gac316adedf7fda441ee55feb9d24d1a94)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index,

433 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_signal\_strength);

434

[ 445](group__bt__tbs.md#ga838e51a85f9833e0822090cd3df09e00)int [bt\_tbs\_set\_status\_flags](group__bt__tbs.md#ga838e51a85f9833e0822090cd3df09e00)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) status\_flags);

446

[ 456](group__bt__tbs.md#ga90b3fb1d757fbb134649b0d7f9047123)int [bt\_tbs\_set\_uri\_scheme\_list](group__bt__tbs.md#ga90b3fb1d757fbb134649b0d7f9047123)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*\*uri\_list,

457 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uri\_count);

[ 463](group__bt__tbs.md#ga76f120dba549225a6f2c2c22be08edfc)void [bt\_tbs\_register\_cb](group__bt__tbs.md#ga76f120dba549225a6f2c2c22be08edfc)(struct [bt\_tbs\_cb](structbt__tbs__cb.md) \*cbs);

464

[ 466](structbt__tbs__register__param.md)struct [bt\_tbs\_register\_param](structbt__tbs__register__param.md) {

[ 468](structbt__tbs__register__param.md#a8cf7713269e8bb193c61be01d6971922) char \*[provider\_name](structbt__tbs__register__param.md#a8cf7713269e8bb193c61be01d6971922);

469

[ 475](structbt__tbs__register__param.md#ab7a0dc41a9e4c898ffd1afaffdfae51d) char \*[uci](structbt__tbs__register__param.md#ab7a0dc41a9e4c898ffd1afaffdfae51d);

476

[ 483](structbt__tbs__register__param.md#a4ffe59cd6d00b9b45db304b17efa22b0) char \*[uri\_schemes\_supported](structbt__tbs__register__param.md#a4ffe59cd6d00b9b45db304b17efa22b0);

484

[ 491](structbt__tbs__register__param.md#aa38a646b7121b555846f7acea9bc9365) bool [gtbs](structbt__tbs__register__param.md#aa38a646b7121b555846f7acea9bc9365);

492

[ 498](structbt__tbs__register__param.md#af88bfd0ac0e83f94e9e467064b4c6c32) bool [authorization\_required](structbt__tbs__register__param.md#af88bfd0ac0e83f94e9e467064b4c6c32);

499

[ 505](structbt__tbs__register__param.md#a248601152be83c807671e2ed635a36a7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [technology](structbt__tbs__register__param.md#a248601152be83c807671e2ed635a36a7);

506

[ 512](structbt__tbs__register__param.md#a3539dcc4f088a643634aef39a0783726) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [supported\_features](structbt__tbs__register__param.md#a3539dcc4f088a643634aef39a0783726);

513};

514

[ 536](group__bt__tbs.md#ga970c970bedd6e94aa4c92479183554e9)int [bt\_tbs\_register\_bearer](group__bt__tbs.md#ga970c970bedd6e94aa4c92479183554e9)(const struct [bt\_tbs\_register\_param](structbt__tbs__register__param.md) \*param);

537

[ 556](group__bt__tbs.md#ga8edd4d31478ed9e0aedbd1a34bdfca96)int [bt\_tbs\_unregister\_bearer](group__bt__tbs.md#ga8edd4d31478ed9e0aedbd1a34bdfca96)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index);

557

[ 559](group__bt__tbs.md#ga62f5008cbfba158fe399cfaf683d1d2e)void [bt\_tbs\_dbg\_print\_calls](group__bt__tbs.md#ga62f5008cbfba158fe399cfaf683d1d2e)(void);

560

[ 562](structbt__tbs__client__call__state.md)struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) {

[ 564](structbt__tbs__client__call__state.md#a3d6eb4dda7adcd16c04ebbd41242c292) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [index](structbt__tbs__client__call__state.md#a3d6eb4dda7adcd16c04ebbd41242c292);

[ 566](structbt__tbs__client__call__state.md#a3e758ad6d0b35f26f43584e50c9a9895) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](structbt__tbs__client__call__state.md#a3e758ad6d0b35f26f43584e50c9a9895);

[ 568](structbt__tbs__client__call__state.md#a57ed9dd726faa3c219e1c858ad6659d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structbt__tbs__client__call__state.md#a57ed9dd726faa3c219e1c858ad6659d9);

569} \_\_packed;

570

[ 572](structbt__tbs__client__call.md)struct [bt\_tbs\_client\_call](structbt__tbs__client__call.md) {

[ 574](structbt__tbs__client__call.md#a480279fea551db1bcb260de81edd6571) struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) [call\_info](structbt__tbs__client__call.md#a480279fea551db1bcb260de81edd6571);

[ 576](structbt__tbs__client__call.md#af04f0576e786250526c12e1436a60c4e) char \*[remote\_uri](structbt__tbs__client__call.md#af04f0576e786250526c12e1436a60c4e);

577};

578

[ 589](group__bt__tbs.md#ga9cac11cc696be9fb387f2f7685e0d8a7)typedef void (\*[bt\_tbs\_client\_discover\_cb](group__bt__tbs.md#ga9cac11cc696be9fb387f2f7685e0d8a7))(struct bt\_conn \*conn, int err,

590 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tbs\_count, bool gtbs\_found);

591

[ 600](group__bt__tbs.md#gaf77231168e4444da7aef203cc9eaca95)typedef void (\*[bt\_tbs\_client\_write\_value\_cb](group__bt__tbs.md#gaf77231168e4444da7aef203cc9eaca95))(struct bt\_conn \*conn, int err,

601 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

602

[ 613](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f)typedef void (\*[bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f))(struct bt\_conn \*conn, int err,

614 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

615

[ 626](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9)typedef void (\*[bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9))(struct bt\_conn \*conn, int err,

627 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

628 const char \*value);

629

[ 639](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20)typedef void (\*[bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20))(struct bt\_conn \*conn, int err,

640 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

641

[ 652](group__bt__tbs.md#gab881b3caaaa4425e52afd84e53adee78)typedef void (\*[bt\_tbs\_client\_termination\_reason\_cb](group__bt__tbs.md#gab881b3caaaa4425e52afd84e53adee78))(struct bt\_conn \*conn,

653 int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

654 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index,

655 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

656

[ 668](group__bt__tbs.md#ga7b31e1c30fa96081a3ef38e1a481b64f)typedef void (\*[bt\_tbs\_client\_current\_calls\_cb](group__bt__tbs.md#ga7b31e1c30fa96081a3ef38e1a481b64f))(struct bt\_conn \*conn, int err,

669 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

670 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_count,

671 const struct [bt\_tbs\_client\_call](structbt__tbs__client__call.md) \*calls);

672

[ 684](group__bt__tbs.md#ga262ca74b7ae2f0c52657066549fa4f92)typedef void (\*[bt\_tbs\_client\_call\_states\_cb](group__bt__tbs.md#ga262ca74b7ae2f0c52657066549fa4f92))(struct bt\_conn \*conn, int err,

685 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

686 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_count,

687 const struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) \*call\_states);

688

[ 694](structbt__tbs__client__cb.md)struct [bt\_tbs\_client\_cb](structbt__tbs__client__cb.md) {

[ 696](structbt__tbs__client__cb.md#abfd4542a0781ff5676a191249f121e91) [bt\_tbs\_client\_discover\_cb](group__bt__tbs.md#ga9cac11cc696be9fb387f2f7685e0d8a7) [discover](structbt__tbs__client__cb.md#abfd4542a0781ff5676a191249f121e91);

697#if defined(CONFIG\_BT\_TBS\_CLIENT\_ORIGINATE\_CALL) || defined(\_\_DOXYGEN\_\_)

[ 699](structbt__tbs__client__cb.md#a0bc51181f188a1249407f2e50431d9fd) [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) [originate\_call](structbt__tbs__client__cb.md#a0bc51181f188a1249407f2e50431d9fd);

700#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_ORIGINATE\_CALL) \*/

701#if defined(CONFIG\_BT\_TBS\_CLIENT\_TERMINATE\_CALL) || defined(\_\_DOXYGEN\_\_)

[ 703](structbt__tbs__client__cb.md#aa78425597fe7fd0db09d69c3ed757293) [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) [terminate\_call](structbt__tbs__client__cb.md#aa78425597fe7fd0db09d69c3ed757293);

704#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_TERMINATE\_CALL) \*/

705#if defined(CONFIG\_BT\_TBS\_CLIENT\_HOLD\_CALL) || defined(\_\_DOXYGEN\_\_)

[ 707](structbt__tbs__client__cb.md#a304a5fd373f1ba5ccb2eb77fcdbbd380) [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) [hold\_call](structbt__tbs__client__cb.md#a304a5fd373f1ba5ccb2eb77fcdbbd380);

708#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_HOLD\_CALL) \*/

709#if defined(CONFIG\_BT\_TBS\_CLIENT\_ACCEPT\_CALL) || defined(\_\_DOXYGEN\_\_)

[ 711](structbt__tbs__client__cb.md#a41242d76c976eef102d480965f977537) [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) [accept\_call](structbt__tbs__client__cb.md#a41242d76c976eef102d480965f977537);

712#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_ACCEPT\_CALL) \*/

713#if defined(CONFIG\_BT\_TBS\_CLIENT\_RETRIEVE\_CALL) || defined(\_\_DOXYGEN\_\_)

[ 715](structbt__tbs__client__cb.md#a2a5fb7de5c3c4aab290c0163c0b40858) [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) [retrieve\_call](structbt__tbs__client__cb.md#a2a5fb7de5c3c4aab290c0163c0b40858);

716#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_RETRIEVE\_CALL) \*/

717#if defined(CONFIG\_BT\_TBS\_CLIENT\_JOIN\_CALLS) || defined(\_\_DOXYGEN\_\_)

[ 719](structbt__tbs__client__cb.md#a2d6b7acd90d05c61f60f27236ab6f1ee) [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f) [join\_calls](structbt__tbs__client__cb.md#a2d6b7acd90d05c61f60f27236ab6f1ee);

720#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_JOIN\_CALLS) \*/

721#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_PROVIDER\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 723](structbt__tbs__client__cb.md#a36d8ea1717e57b9440e9b58e9411422a) [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) [bearer\_provider\_name](structbt__tbs__client__cb.md#a36d8ea1717e57b9440e9b58e9411422a);

724#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_PROVIDER\_NAME) \*/

725#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_UCI) || defined(\_\_DOXYGEN\_\_)

[ 727](structbt__tbs__client__cb.md#a15ccb7de457631620983e7d2d0372967) [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) [bearer\_uci](structbt__tbs__client__cb.md#a15ccb7de457631620983e7d2d0372967);

728#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_UCI) \*/

729#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_TECHNOLOGY) || defined(\_\_DOXYGEN\_\_)

[ 731](structbt__tbs__client__cb.md#a803d8268ee1271f41aec68f6d9b811bf) [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) [technology](structbt__tbs__client__cb.md#a803d8268ee1271f41aec68f6d9b811bf);

732#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_TECHNOLOGY) \*/

733#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_URI\_SCHEMES\_SUPPORTED\_LIST) || defined(\_\_DOXYGEN\_\_)

[ 735](structbt__tbs__client__cb.md#a7f64cf8e3d0bc4ec21c44bd4fea6d7ee) [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) [uri\_list](structbt__tbs__client__cb.md#a7f64cf8e3d0bc4ec21c44bd4fea6d7ee);

736#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_URI\_SCHEMES\_SUPPORTED\_LIST) \*/

737#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_SIGNAL\_STRENGTH) || defined(\_\_DOXYGEN\_\_)

[ 739](structbt__tbs__client__cb.md#a96df90461159f97f5dc8cbb72cd0cbc4) [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) [signal\_strength](structbt__tbs__client__cb.md#a96df90461159f97f5dc8cbb72cd0cbc4);

740#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_SIGNAL\_STRENGTH) \*/

741#if defined(CONFIG\_BT\_TBS\_CLIENT\_READ\_BEARER\_SIGNAL\_INTERVAL) || defined(\_\_DOXYGEN\_\_)

[ 743](structbt__tbs__client__cb.md#a01426c4a84e71a9395cce2963e2e83a3) [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) [signal\_interval](structbt__tbs__client__cb.md#a01426c4a84e71a9395cce2963e2e83a3);

744#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_READ\_BEARER\_SIGNAL\_INTERVAL) \*/

745#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_LIST\_CURRENT\_CALLS) || defined(\_\_DOXYGEN\_\_)

[ 747](structbt__tbs__client__cb.md#a10dc9404533db388b3ae1058542efd66) [bt\_tbs\_client\_current\_calls\_cb](group__bt__tbs.md#ga7b31e1c30fa96081a3ef38e1a481b64f) [current\_calls](structbt__tbs__client__cb.md#a10dc9404533db388b3ae1058542efd66);

748#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_LIST\_CURRENT\_CALLS) \*/

749#if defined(CONFIG\_BT\_TBS\_CLIENT\_CCID) || defined(\_\_DOXYGEN\_\_)

[ 751](structbt__tbs__client__cb.md#a90acde153f8893b5cba891884529d86c) [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) [ccid](structbt__tbs__client__cb.md#a90acde153f8893b5cba891884529d86c);

752#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_CCID) \*/

753#if defined(CONFIG\_BT\_TBS\_CLIENT\_INCOMING\_URI) || defined(\_\_DOXYGEN\_\_)

[ 755](structbt__tbs__client__cb.md#ae95494a76e1f3275f48204dcd4798712) [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) [call\_uri](structbt__tbs__client__cb.md#ae95494a76e1f3275f48204dcd4798712);

756#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_INCOMING\_URI) \*/

757#if defined(CONFIG\_BT\_TBS\_CLIENT\_STATUS\_FLAGS) || defined(\_\_DOXYGEN\_\_)

[ 759](structbt__tbs__client__cb.md#a94c3bfc1e88518de9e29e947064ec8dc) [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) [status\_flags](structbt__tbs__client__cb.md#a94c3bfc1e88518de9e29e947064ec8dc);

760#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_STATUS\_FLAGS) \*/

[ 762](structbt__tbs__client__cb.md#a88cb69ef54c9399bceb5641202eeabce) [bt\_tbs\_client\_call\_states\_cb](group__bt__tbs.md#ga262ca74b7ae2f0c52657066549fa4f92) [call\_state](structbt__tbs__client__cb.md#a88cb69ef54c9399bceb5641202eeabce);

763#if defined(CONFIG\_BT\_TBS\_CLIENT\_OPTIONAL\_OPCODES) || defined(\_\_DOXYGEN\_\_)

[ 765](structbt__tbs__client__cb.md#a91c61b29c16a43fd3f781fd7e0ab4618) [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20) [optional\_opcodes](structbt__tbs__client__cb.md#a91c61b29c16a43fd3f781fd7e0ab4618);

766#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_OPTIONAL\_OPCODES) \*/

[ 768](structbt__tbs__client__cb.md#ae8e5cbe52cbb300e1cd919d24c85c4df) [bt\_tbs\_client\_termination\_reason\_cb](group__bt__tbs.md#gab881b3caaaa4425e52afd84e53adee78) [termination\_reason](structbt__tbs__client__cb.md#ae8e5cbe52cbb300e1cd919d24c85c4df);

769#if defined(CONFIG\_BT\_TBS\_CLIENT\_INCOMING\_CALL) || defined(\_\_DOXYGEN\_\_)

[ 771](structbt__tbs__client__cb.md#a354ba5d21376813adc5c9765a5da1a09) [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) [remote\_uri](structbt__tbs__client__cb.md#a354ba5d21376813adc5c9765a5da1a09);

772#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_INCOMING\_CALL) \*/

773#if defined(CONFIG\_BT\_TBS\_CLIENT\_CALL\_FRIENDLY\_NAME) || defined(\_\_DOXYGEN\_\_)

[ 775](structbt__tbs__client__cb.md#ad2089050db76453b7f9c51c3d2fa4d17) [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9) [friendly\_name](structbt__tbs__client__cb.md#ad2089050db76453b7f9c51c3d2fa4d17);

776#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_CALL\_FRIENDLY\_NAME) \*/

777

780 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

782};

783

[ 792](group__bt__tbs.md#gac59f3dec092a14bdf234039e3dcd12eb)int [bt\_tbs\_client\_discover](group__bt__tbs.md#gac59f3dec092a14bdf234039e3dcd12eb)(struct bt\_conn \*conn);

793

[ 803](group__bt__tbs.md#ga3a71c51d464aa19fbfbd2d60fc4901bc)int [bt\_tbs\_client\_set\_outgoing\_uri](group__bt__tbs.md#ga3a71c51d464aa19fbfbd2d60fc4901bc)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

804 const char \*uri);

805

[ 818](group__bt__tbs.md#gaa1dcb9908057d75a54fa447639826f3c)int [bt\_tbs\_client\_set\_signal\_strength\_interval](group__bt__tbs.md#gaa1dcb9908057d75a54fa447639826f3c)(struct bt\_conn \*conn,

819 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

820 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval);

821

[ 834](group__bt__tbs.md#ga0aac704008ffc92ce6609d3ffffc4523)int [bt\_tbs\_client\_originate\_call](group__bt__tbs.md#ga0aac704008ffc92ce6609d3ffffc4523)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

835 const char \*uri);

836

[ 849](group__bt__tbs.md#ga25b803bb5cae2e1a8b0398bc48137d80)int [bt\_tbs\_client\_terminate\_call](group__bt__tbs.md#ga25b803bb5cae2e1a8b0398bc48137d80)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

850 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

851

[ 864](group__bt__tbs.md#ga23e825de6af71d4e456b63c3a621fb61)int [bt\_tbs\_client\_hold\_call](group__bt__tbs.md#ga23e825de6af71d4e456b63c3a621fb61)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

865 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

866

[ 879](group__bt__tbs.md#ga625fc73885c2bfd63f0f4b2d7f72eaef)int [bt\_tbs\_client\_accept\_call](group__bt__tbs.md#ga625fc73885c2bfd63f0f4b2d7f72eaef)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

880 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

881

[ 894](group__bt__tbs.md#gabbe194a63da0b95dc1dca0337560a585)int [bt\_tbs\_client\_retrieve\_call](group__bt__tbs.md#gabbe194a63da0b95dc1dca0337560a585)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

895 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

896

[ 910](group__bt__tbs.md#gaae1925deb0b5865af601aa8278ffb10a)int [bt\_tbs\_client\_join\_calls](group__bt__tbs.md#gaae1925deb0b5865af601aa8278ffb10a)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

911 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count);

912

[ 924](group__bt__tbs.md#ga2053a9eb7cf28f66febd365f0b682be0)int [bt\_tbs\_client\_read\_bearer\_provider\_name](group__bt__tbs.md#ga2053a9eb7cf28f66febd365f0b682be0)(struct bt\_conn \*conn,

925 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

926

[ 938](group__bt__tbs.md#gaba92039d3b44da9163a22400951fafa7)int [bt\_tbs\_client\_read\_bearer\_uci](group__bt__tbs.md#gaba92039d3b44da9163a22400951fafa7)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

939

[ 951](group__bt__tbs.md#ga7684dbcb78e407f7002d44fbdb805e5d)int [bt\_tbs\_client\_read\_technology](group__bt__tbs.md#ga7684dbcb78e407f7002d44fbdb805e5d)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

952

[ 964](group__bt__tbs.md#gad19db25591c7ae5bd0b4c2bbaefc9bed)int [bt\_tbs\_client\_read\_uri\_list](group__bt__tbs.md#gad19db25591c7ae5bd0b4c2bbaefc9bed)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

965

[ 977](group__bt__tbs.md#gaabe97df55817b8e36c79de4bf30fc83f)int [bt\_tbs\_client\_read\_signal\_strength](group__bt__tbs.md#gaabe97df55817b8e36c79de4bf30fc83f)(struct bt\_conn \*conn,

978 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

979

[ 991](group__bt__tbs.md#ga38046c5c715d451b21a3076742268010)int [bt\_tbs\_client\_read\_signal\_interval](group__bt__tbs.md#ga38046c5c715d451b21a3076742268010)(struct bt\_conn \*conn,

992 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

993

[ 1005](group__bt__tbs.md#ga895c7f54300e5452fb8d0c9d4b3306ae)int [bt\_tbs\_client\_read\_current\_calls](group__bt__tbs.md#ga895c7f54300e5452fb8d0c9d4b3306ae)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

1006

[ 1018](group__bt__tbs.md#gac070ec0590df5820b7721d579ceeeb15)int [bt\_tbs\_client\_read\_ccid](group__bt__tbs.md#gac070ec0590df5820b7721d579ceeeb15)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

1019

[ 1031](group__bt__tbs.md#ga4238a37b80b7d7ff611fe9b02b7cf54d)int [bt\_tbs\_client\_read\_call\_uri](group__bt__tbs.md#ga4238a37b80b7d7ff611fe9b02b7cf54d)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

1032

[ 1044](group__bt__tbs.md#ga9fe91df1a31ce59401347fc0eac2b701)int [bt\_tbs\_client\_read\_status\_flags](group__bt__tbs.md#ga9fe91df1a31ce59401347fc0eac2b701)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

1045

[ 1054](group__bt__tbs.md#gafeaaaefb9d4eb773dd0cbdfebe26e0b7)int [bt\_tbs\_client\_read\_call\_state](group__bt__tbs.md#gafeaaaefb9d4eb773dd0cbdfebe26e0b7)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

1055

[ 1067](group__bt__tbs.md#gab04f8355c32fce501bd757b75ee9d38a)int [bt\_tbs\_client\_read\_remote\_uri](group__bt__tbs.md#gab04f8355c32fce501bd757b75ee9d38a)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

1068

[ 1080](group__bt__tbs.md#ga99549dd6244580e157006fb17772fd8f)int [bt\_tbs\_client\_read\_friendly\_name](group__bt__tbs.md#ga99549dd6244580e157006fb17772fd8f)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

1081

[ 1093](group__bt__tbs.md#gaf504e1a11352d77a36aa087b587e4ba8)int [bt\_tbs\_client\_read\_optional\_opcodes](group__bt__tbs.md#gaf504e1a11352d77a36aa087b587e4ba8)(struct bt\_conn \*conn,

1094 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

1095

[ 1105](group__bt__tbs.md#gabe2251d4ea88306793dc68ae683886bb)int [bt\_tbs\_client\_register\_cb](group__bt__tbs.md#gabe2251d4ea88306793dc68ae683886bb)(struct [bt\_tbs\_client\_cb](structbt__tbs__client__cb.md) \*cbs);

1106

[ 1118](group__bt__tbs.md#gaadae501fa6f7771bb9661af829805a5f)struct bt\_tbs\_instance \*[bt\_tbs\_client\_get\_by\_ccid](group__bt__tbs.md#gaadae501fa6f7771bb9661af829805a5f)(const struct bt\_conn \*conn,

1119 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid);

1120

1121#ifdef \_\_cplusplus

1122}

1123#endif

1124

1126

1127#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_TBS\_H\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_tbs\_remote\_retrieve](group__bt__tbs.md#ga09a3e64040819b6b8b694b94d2f62ca0)

int bt\_tbs\_remote\_retrieve(uint8\_t call\_index)

Notify the server that the remote party retrieved the call.

[bt\_tbs\_client\_originate\_call](group__bt__tbs.md#ga0aac704008ffc92ce6609d3ffffc4523)

int bt\_tbs\_client\_originate\_call(struct bt\_conn \*conn, uint8\_t inst\_index, const char \*uri)

Request to originate a call.

[bt\_tbs\_accept](group__bt__tbs.md#ga1b942bcf8287641f9cd53824b4d6e77b)

int bt\_tbs\_accept(uint8\_t call\_index)

Accept an alerting call.

[bt\_tbs\_authorize\_cb](group__bt__tbs.md#ga1cc9e7140531b07bf6a8dedbc17f24c0)

bool(\* bt\_tbs\_authorize\_cb)(struct bt\_conn \*conn)

Callback function for authorizing a client.

**Definition** tbs.h:256

[bt\_tbs\_client\_read\_bearer\_provider\_name](group__bt__tbs.md#ga2053a9eb7cf28f66febd365f0b682be0)

int bt\_tbs\_client\_read\_bearer\_provider\_name(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the bearer provider name of a TBS instance.

[bt\_tbs\_join](group__bt__tbs.md#ga23226d41e3b98a53ec9a9c2fa346c9ac)

int bt\_tbs\_join(uint8\_t call\_index\_cnt, uint8\_t \*call\_indexes)

Join calls.

[bt\_tbs\_client\_hold\_call](group__bt__tbs.md#ga23e825de6af71d4e456b63c3a621fb61)

int bt\_tbs\_client\_hold\_call(struct bt\_conn \*conn, uint8\_t inst\_index, uint8\_t call\_index)

Request to hold a call.

[bt\_tbs\_client\_terminate\_call](group__bt__tbs.md#ga25b803bb5cae2e1a8b0398bc48137d80)

int bt\_tbs\_client\_terminate\_call(struct bt\_conn \*conn, uint8\_t inst\_index, uint8\_t call\_index)

Request to terminate a call.

[bt\_tbs\_client\_call\_states\_cb](group__bt__tbs.md#ga262ca74b7ae2f0c52657066549fa4f92)

void(\* bt\_tbs\_client\_call\_states\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, uint8\_t call\_count, const struct bt\_tbs\_client\_call\_state \*call\_states)

Callback function for ccp\_read\_call\_state.

**Definition** tbs.h:684

[bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1)

void(\* bt\_tbs\_call\_change\_cb)(struct bt\_conn \*conn, uint8\_t call\_index)

Callback function for client request call state change.

**Definition** tbs.h:246

[bt\_tbs\_client\_read\_signal\_interval](group__bt__tbs.md#ga38046c5c715d451b21a3076742268010)

int bt\_tbs\_client\_read\_signal\_interval(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the signal strength reporting interval of a TBS instance.

[bt\_tbs\_client\_set\_outgoing\_uri](group__bt__tbs.md#ga3a71c51d464aa19fbfbd2d60fc4901bc)

int bt\_tbs\_client\_set\_outgoing\_uri(struct bt\_conn \*conn, uint8\_t inst\_index, const char \*uri)

Set the outgoing URI for a TBS instance on the peer device.

[bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f)

void(\* bt\_tbs\_client\_cp\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, uint8\_t call\_index)

Callback function for the CCP call control functions.

**Definition** tbs.h:613

[bt\_tbs\_client\_read\_call\_uri](group__bt__tbs.md#ga4238a37b80b7d7ff611fe9b02b7cf54d)

int bt\_tbs\_client\_read\_call\_uri(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the call target URI of a TBS instance.

[bt\_tbs\_remote\_incoming](group__bt__tbs.md#ga47939f557e4d6503af9b7b85aff9d60f)

int bt\_tbs\_remote\_incoming(uint8\_t bearer\_index, const char \*to, const char \*from, const char \*friendly\_name)

Notify the server of an incoming call.

[bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9)

void(\* bt\_tbs\_client\_read\_string\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, const char \*value)

Callback function for functions that read a string value.

**Definition** tbs.h:626

[bt\_tbs\_set\_bearer\_provider\_name](group__bt__tbs.md#ga5118db6b23b387956e75eda8aecd53d5)

int bt\_tbs\_set\_bearer\_provider\_name(uint8\_t bearer\_index, const char \*name)

Set a new bearer provider.

[bt\_tbs\_remote\_terminate](group__bt__tbs.md#ga52afc7b8a22b071dbac10057579f319c)

int bt\_tbs\_remote\_terminate(uint8\_t call\_index)

Notify the server that the remote party terminated the call.

[bt\_tbs\_remote\_hold](group__bt__tbs.md#ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e)

int bt\_tbs\_remote\_hold(uint8\_t call\_index)

Notify the server that the remote party held the call.

[bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20)

void(\* bt\_tbs\_client\_read\_value\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, uint32\_t value)

Callback function for functions that read an integer value.

**Definition** tbs.h:639

[bt\_tbs\_originate\_call\_cb](group__bt__tbs.md#ga60e9e143f247bb7e668293f0233ce300)

bool(\* bt\_tbs\_originate\_call\_cb)(struct bt\_conn \*conn, uint8\_t call\_index, const char \*uri)

Callback function for client originating a call.

**Definition** tbs.h:212

[bt\_tbs\_client\_accept\_call](group__bt__tbs.md#ga625fc73885c2bfd63f0f4b2d7f72eaef)

int bt\_tbs\_client\_accept\_call(struct bt\_conn \*conn, uint8\_t inst\_index, uint8\_t call\_index)

Accept an incoming call.

[bt\_tbs\_dbg\_print\_calls](group__bt__tbs.md#ga62f5008cbfba158fe399cfaf683d1d2e)

void bt\_tbs\_dbg\_print\_calls(void)

Prints all calls of all services to the debug log.

[bt\_tbs\_terminate\_call\_cb](group__bt__tbs.md#ga69e93b48b2a48e8a6552882660b791cc)

void(\* bt\_tbs\_terminate\_call\_cb)(struct bt\_conn \*conn, uint8\_t call\_index, uint8\_t reason)

Callback function for client terminating a call.

**Definition** tbs.h:225

[bt\_tbs\_client\_read\_technology](group__bt__tbs.md#ga7684dbcb78e407f7002d44fbdb805e5d)

int bt\_tbs\_client\_read\_technology(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the technology of a TBS instance.

[bt\_tbs\_register\_cb](group__bt__tbs.md#ga76f120dba549225a6f2c2c22be08edfc)

void bt\_tbs\_register\_cb(struct bt\_tbs\_cb \*cbs)

Register the callbacks for TBS.

[bt\_tbs\_client\_current\_calls\_cb](group__bt__tbs.md#ga7b31e1c30fa96081a3ef38e1a481b64f)

void(\* bt\_tbs\_client\_current\_calls\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, uint8\_t call\_count, const struct bt\_tbs\_client\_call \*calls)

Callback function for ccp\_read\_current\_calls.

**Definition** tbs.h:668

[bt\_tbs\_terminate](group__bt__tbs.md#ga82553640882ac74f9af84bfe09ff47ee)

int bt\_tbs\_terminate(uint8\_t call\_index)

Terminate a call.

[bt\_tbs\_set\_status\_flags](group__bt__tbs.md#ga838e51a85f9833e0822090cd3df09e00)

int bt\_tbs\_set\_status\_flags(uint8\_t bearer\_index, uint16\_t status\_flags)

Sets the feature and status value.

[bt\_tbs\_remote\_answer](group__bt__tbs.md#ga868b83450f7425e8a0c8cfb7c1de45d8)

int bt\_tbs\_remote\_answer(uint8\_t call\_index)

Notify the server that the remote party answered the call.

[bt\_tbs\_client\_read\_current\_calls](group__bt__tbs.md#ga895c7f54300e5452fb8d0c9d4b3306ae)

int bt\_tbs\_client\_read\_current\_calls(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the list of current calls of a TBS instance.

[bt\_tbs\_unregister\_bearer](group__bt__tbs.md#ga8edd4d31478ed9e0aedbd1a34bdfca96)

int bt\_tbs\_unregister\_bearer(uint8\_t bearer\_index)

Unregister a Telephone Bearer.

[bt\_tbs\_set\_uri\_scheme\_list](group__bt__tbs.md#ga90b3fb1d757fbb134649b0d7f9047123)

int bt\_tbs\_set\_uri\_scheme\_list(uint8\_t bearer\_index, const char \*\*uri\_list, uint8\_t uri\_count)

Sets the URI scheme list of a bearer.

[bt\_tbs\_register\_bearer](group__bt__tbs.md#ga970c970bedd6e94aa4c92479183554e9)

int bt\_tbs\_register\_bearer(const struct bt\_tbs\_register\_param \*param)

Register a Telephone Bearer.

[bt\_tbs\_client\_read\_friendly\_name](group__bt__tbs.md#ga99549dd6244580e157006fb17772fd8f)

int bt\_tbs\_client\_read\_friendly\_name(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the friendly name of a call for a TBS instance.

[bt\_tbs\_client\_discover\_cb](group__bt__tbs.md#ga9cac11cc696be9fb387f2f7685e0d8a7)

void(\* bt\_tbs\_client\_discover\_cb)(struct bt\_conn \*conn, int err, uint8\_t tbs\_count, bool gtbs\_found)

Callback function for ccp\_discover.

**Definition** tbs.h:589

[bt\_tbs\_client\_read\_status\_flags](group__bt__tbs.md#ga9fe91df1a31ce59401347fc0eac2b701)

int bt\_tbs\_client\_read\_status\_flags(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the feature and status value of a TBS instance.

[bt\_tbs\_client\_set\_signal\_strength\_interval](group__bt__tbs.md#gaa1dcb9908057d75a54fa447639826f3c)

int bt\_tbs\_client\_set\_signal\_strength\_interval(struct bt\_conn \*conn, uint8\_t inst\_index, uint8\_t interval)

Set the signal strength reporting interval for a TBS instance.

[bt\_tbs\_join\_calls\_cb](group__bt__tbs.md#gaa45b3f4837165d722c2df6f202a39058)

void(\* bt\_tbs\_join\_calls\_cb)(struct bt\_conn \*conn, uint8\_t call\_index\_count, const uint8\_t \*call\_indexes)

Callback function for client joining calls.

**Definition** tbs.h:236

[bt\_tbs\_client\_read\_signal\_strength](group__bt__tbs.md#gaabe97df55817b8e36c79de4bf30fc83f)

int bt\_tbs\_client\_read\_signal\_strength(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the current signal strength of a TBS instance.

[bt\_tbs\_client\_get\_by\_ccid](group__bt__tbs.md#gaadae501fa6f7771bb9661af829805a5f)

struct bt\_tbs\_instance \* bt\_tbs\_client\_get\_by\_ccid(const struct bt\_conn \*conn, uint8\_t ccid)

Look up Telephone Bearer Service instance by CCID.

[bt\_tbs\_client\_join\_calls](group__bt__tbs.md#gaae1925deb0b5865af601aa8278ffb10a)

int bt\_tbs\_client\_join\_calls(struct bt\_conn \*conn, uint8\_t inst\_index, const uint8\_t \*call\_indexes, uint8\_t count)

Join multiple calls.

[bt\_tbs\_client\_read\_remote\_uri](group__bt__tbs.md#gab04f8355c32fce501bd757b75ee9d38a)

int bt\_tbs\_client\_read\_remote\_uri(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the remote URI of a TBS instance.

[bt\_tbs\_hold](group__bt__tbs.md#gab72044a1f5466114b5efb88dfcd2f097)

int bt\_tbs\_hold(uint8\_t call\_index)

Hold a call.

[bt\_tbs\_client\_termination\_reason\_cb](group__bt__tbs.md#gab881b3caaaa4425e52afd84e53adee78)

void(\* bt\_tbs\_client\_termination\_reason\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, uint8\_t call\_index, uint8\_t reason)

Callback function for ccp\_read\_termination\_reason.

**Definition** tbs.h:652

[bt\_tbs\_client\_read\_bearer\_uci](group__bt__tbs.md#gaba92039d3b44da9163a22400951fafa7)

int bt\_tbs\_client\_read\_bearer\_uci(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the UCI of a TBS instance.

[bt\_tbs\_client\_retrieve\_call](group__bt__tbs.md#gabbe194a63da0b95dc1dca0337560a585)

int bt\_tbs\_client\_retrieve\_call(struct bt\_conn \*conn, uint8\_t inst\_index, uint8\_t call\_index)

Retrieve call from (local) hold.

[bt\_tbs\_client\_register\_cb](group__bt__tbs.md#gabe2251d4ea88306793dc68ae683886bb)

int bt\_tbs\_client\_register\_cb(struct bt\_tbs\_client\_cb \*cbs)

Register the callbacks for CCP.

[bt\_tbs\_client\_read\_ccid](group__bt__tbs.md#gac070ec0590df5820b7721d579ceeeb15)

int bt\_tbs\_client\_read\_ccid(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the content ID of a TBS instance.

[bt\_tbs\_set\_signal\_strength](group__bt__tbs.md#gac316adedf7fda441ee55feb9d24d1a94)

int bt\_tbs\_set\_signal\_strength(uint8\_t bearer\_index, uint8\_t new\_signal\_strength)

Update the signal strength reported by the server.

[bt\_tbs\_client\_discover](group__bt__tbs.md#gac59f3dec092a14bdf234039e3dcd12eb)

int bt\_tbs\_client\_discover(struct bt\_conn \*conn)

Discover TBS for a connection.

[bt\_tbs\_retrieve](group__bt__tbs.md#gad0b45af09b82d6cd66a8481c0e67e04e)

int bt\_tbs\_retrieve(uint8\_t call\_index)

Retrieve a call.

[bt\_tbs\_client\_read\_uri\_list](group__bt__tbs.md#gad19db25591c7ae5bd0b4c2bbaefc9bed)

int bt\_tbs\_client\_read\_uri\_list(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the URI schemes list of a TBS instance.

[bt\_tbs\_originate](group__bt__tbs.md#gadeae51d7cecd80abcdcde1195bb1dfba)

int bt\_tbs\_originate(uint8\_t bearer\_index, char \*uri, uint8\_t \*call\_index)

Originate a call.

[bt\_tbs\_set\_bearer\_technology](group__bt__tbs.md#gaf4c576b8aa599f1bd9598964bc1b779f)

int bt\_tbs\_set\_bearer\_technology(uint8\_t bearer\_index, uint8\_t new\_technology)

Set a new bearer technology.

[bt\_tbs\_client\_read\_optional\_opcodes](group__bt__tbs.md#gaf504e1a11352d77a36aa087b587e4ba8)

int bt\_tbs\_client\_read\_optional\_opcodes(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the supported opcode of a TBS instance.

[bt\_tbs\_client\_write\_value\_cb](group__bt__tbs.md#gaf77231168e4444da7aef203cc9eaca95)

void(\* bt\_tbs\_client\_write\_value\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index)

Callback function for writing values to peer device.

**Definition** tbs.h:600

[bt\_tbs\_client\_read\_call\_state](group__bt__tbs.md#gafeaaaefb9d4eb773dd0cbdfebe26e0b7)

int bt\_tbs\_client\_read\_call\_state(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the states of the current calls of a TBS instance.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

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

[bt\_tbs\_cb](structbt__tbs__cb.md)

Struct to hold the Telephone Bearer Service callbacks.

**Definition** tbs.h:263

[bt\_tbs\_cb::originate\_call](structbt__tbs__cb.md#a566504bee9c7334c53a23223e544855f)

bt\_tbs\_originate\_call\_cb originate\_call

Client originating call.

**Definition** tbs.h:265

[bt\_tbs\_cb::accept\_call](structbt__tbs__cb.md#a798c09c04a563800c4d9328c1d9e2de6)

bt\_tbs\_call\_change\_cb accept\_call

Client accepting call.

**Definition** tbs.h:271

[bt\_tbs\_cb::hold\_call](structbt__tbs__cb.md#a8b76dd9243e97d22e0d6c2ac578aa383)

bt\_tbs\_call\_change\_cb hold\_call

Client holding call.

**Definition** tbs.h:269

[bt\_tbs\_cb::terminate\_call](structbt__tbs__cb.md#ab065a5c58db19feb2a1d3013983ed5aa)

bt\_tbs\_terminate\_call\_cb terminate\_call

Client terminating call.

**Definition** tbs.h:267

[bt\_tbs\_cb::authorize](structbt__tbs__cb.md#ab7c859ffaebcf16db71c5d54bd4f5802)

bt\_tbs\_authorize\_cb authorize

Callback to authorize a client.

**Definition** tbs.h:277

[bt\_tbs\_cb::join\_calls](structbt__tbs__cb.md#ac1a99a703687a3ef5ebc12eca5f6c2e7)

bt\_tbs\_join\_calls\_cb join\_calls

Client joining calls.

**Definition** tbs.h:275

[bt\_tbs\_cb::retrieve\_call](structbt__tbs__cb.md#ad543a2f26d1749eba0774e2352b53692)

bt\_tbs\_call\_change\_cb retrieve\_call

Client retrieving call.

**Definition** tbs.h:273

[bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md)

Struct to hold a call state.

**Definition** tbs.h:562

[bt\_tbs\_client\_call\_state::index](structbt__tbs__client__call__state.md#a3d6eb4dda7adcd16c04ebbd41242c292)

uint8\_t index

Index of the call.

**Definition** tbs.h:564

[bt\_tbs\_client\_call\_state::state](structbt__tbs__client__call__state.md#a3e758ad6d0b35f26f43584e50c9a9895)

uint8\_t state

State of the call (see BT\_TBS\_CALL\_STATE\_\*).

**Definition** tbs.h:566

[bt\_tbs\_client\_call\_state::flags](structbt__tbs__client__call__state.md#a57ed9dd726faa3c219e1c858ad6659d9)

uint8\_t flags

Call flags (see BT\_TBS\_CALL\_FLAG\_\*).

**Definition** tbs.h:568

[bt\_tbs\_client\_call](structbt__tbs__client__call.md)

Struct to hold a call as the Telephone Bearer Service client.

**Definition** tbs.h:572

[bt\_tbs\_client\_call::call\_info](structbt__tbs__client__call.md#a480279fea551db1bcb260de81edd6571)

struct bt\_tbs\_client\_call\_state call\_info

Call information.

**Definition** tbs.h:574

[bt\_tbs\_client\_call::remote\_uri](structbt__tbs__client__call.md#af04f0576e786250526c12e1436a60c4e)

char \* remote\_uri

The remove URI.

**Definition** tbs.h:576

[bt\_tbs\_client\_cb](structbt__tbs__client__cb.md)

Struct to hold the Telephone Bearer Service client callbacks.

**Definition** tbs.h:694

[bt\_tbs\_client\_cb::signal\_interval](structbt__tbs__client__cb.md#a01426c4a84e71a9395cce2963e2e83a3)

bt\_tbs\_client\_read\_value\_cb signal\_interval

Bearer signal interval has been read.

**Definition** tbs.h:743

[bt\_tbs\_client\_cb::originate\_call](structbt__tbs__client__cb.md#a0bc51181f188a1249407f2e50431d9fd)

bt\_tbs\_client\_cp\_cb originate\_call

Originate call has completed.

**Definition** tbs.h:699

[bt\_tbs\_client\_cb::current\_calls](structbt__tbs__client__cb.md#a10dc9404533db388b3ae1058542efd66)

bt\_tbs\_client\_current\_calls\_cb current\_calls

Bearer current calls has been read.

**Definition** tbs.h:747

[bt\_tbs\_client\_cb::bearer\_uci](structbt__tbs__client__cb.md#a15ccb7de457631620983e7d2d0372967)

bt\_tbs\_client\_read\_string\_cb bearer\_uci

Bearer UCI has been read.

**Definition** tbs.h:727

[bt\_tbs\_client\_cb::retrieve\_call](structbt__tbs__client__cb.md#a2a5fb7de5c3c4aab290c0163c0b40858)

bt\_tbs\_client\_cp\_cb retrieve\_call

Retrieve call has completed.

**Definition** tbs.h:715

[bt\_tbs\_client\_cb::join\_calls](structbt__tbs__client__cb.md#a2d6b7acd90d05c61f60f27236ab6f1ee)

bt\_tbs\_client\_cp\_cb join\_calls

Join calls has completed.

**Definition** tbs.h:719

[bt\_tbs\_client\_cb::hold\_call](structbt__tbs__client__cb.md#a304a5fd373f1ba5ccb2eb77fcdbbd380)

bt\_tbs\_client\_cp\_cb hold\_call

Hold call has completed.

**Definition** tbs.h:707

[bt\_tbs\_client\_cb::remote\_uri](structbt__tbs__client__cb.md#a354ba5d21376813adc5c9765a5da1a09)

bt\_tbs\_client\_read\_string\_cb remote\_uri

Bearer remote URI has been read.

**Definition** tbs.h:771

[bt\_tbs\_client\_cb::bearer\_provider\_name](structbt__tbs__client__cb.md#a36d8ea1717e57b9440e9b58e9411422a)

bt\_tbs\_client\_read\_string\_cb bearer\_provider\_name

Bearer provider name has been read.

**Definition** tbs.h:723

[bt\_tbs\_client\_cb::accept\_call](structbt__tbs__client__cb.md#a41242d76c976eef102d480965f977537)

bt\_tbs\_client\_cp\_cb accept\_call

Accept call has completed.

**Definition** tbs.h:711

[bt\_tbs\_client\_cb::uri\_list](structbt__tbs__client__cb.md#a7f64cf8e3d0bc4ec21c44bd4fea6d7ee)

bt\_tbs\_client\_read\_string\_cb uri\_list

Bearer URI list has been read.

**Definition** tbs.h:735

[bt\_tbs\_client\_cb::technology](structbt__tbs__client__cb.md#a803d8268ee1271f41aec68f6d9b811bf)

bt\_tbs\_client\_read\_value\_cb technology

Bearer technology has been read.

**Definition** tbs.h:731

[bt\_tbs\_client\_cb::call\_state](structbt__tbs__client__cb.md#a88cb69ef54c9399bceb5641202eeabce)

bt\_tbs\_client\_call\_states\_cb call\_state

Bearer call states has been read.

**Definition** tbs.h:762

[bt\_tbs\_client\_cb::ccid](structbt__tbs__client__cb.md#a90acde153f8893b5cba891884529d86c)

bt\_tbs\_client\_read\_value\_cb ccid

Bearer CCID has been read.

**Definition** tbs.h:751

[bt\_tbs\_client\_cb::optional\_opcodes](structbt__tbs__client__cb.md#a91c61b29c16a43fd3f781fd7e0ab4618)

bt\_tbs\_client\_read\_value\_cb optional\_opcodes

Bearer optional opcodes has been read.

**Definition** tbs.h:765

[bt\_tbs\_client\_cb::status\_flags](structbt__tbs__client__cb.md#a94c3bfc1e88518de9e29e947064ec8dc)

bt\_tbs\_client\_read\_value\_cb status\_flags

Bearer status flags has been read.

**Definition** tbs.h:759

[bt\_tbs\_client\_cb::signal\_strength](structbt__tbs__client__cb.md#a96df90461159f97f5dc8cbb72cd0cbc4)

bt\_tbs\_client\_read\_value\_cb signal\_strength

Bearer signal strength has been read.

**Definition** tbs.h:739

[bt\_tbs\_client\_cb::terminate\_call](structbt__tbs__client__cb.md#aa78425597fe7fd0db09d69c3ed757293)

bt\_tbs\_client\_cp\_cb terminate\_call

Terminate call has completed.

**Definition** tbs.h:703

[bt\_tbs\_client\_cb::discover](structbt__tbs__client__cb.md#abfd4542a0781ff5676a191249f121e91)

bt\_tbs\_client\_discover\_cb discover

Discovery has completed.

**Definition** tbs.h:696

[bt\_tbs\_client\_cb::friendly\_name](structbt__tbs__client__cb.md#ad2089050db76453b7f9c51c3d2fa4d17)

bt\_tbs\_client\_read\_string\_cb friendly\_name

Bearer friendly name has been read.

**Definition** tbs.h:775

[bt\_tbs\_client\_cb::termination\_reason](structbt__tbs__client__cb.md#ae8e5cbe52cbb300e1cd919d24c85c4df)

bt\_tbs\_client\_termination\_reason\_cb termination\_reason

Bearer terminate reason has been read.

**Definition** tbs.h:768

[bt\_tbs\_client\_cb::call\_uri](structbt__tbs__client__cb.md#ae95494a76e1f3275f48204dcd4798712)

bt\_tbs\_client\_read\_string\_cb call\_uri

Bearer call URI has been read.

**Definition** tbs.h:755

[bt\_tbs\_register\_param](structbt__tbs__register__param.md)

Parameters for registering a Telephone Bearer Service.

**Definition** tbs.h:466

[bt\_tbs\_register\_param::technology](structbt__tbs__register__param.md#a248601152be83c807671e2ed635a36a7)

uint8\_t technology

The technology of the bearer.

**Definition** tbs.h:505

[bt\_tbs\_register\_param::supported\_features](structbt__tbs__register__param.md#a3539dcc4f088a643634aef39a0783726)

uint8\_t supported\_features

The optional supported features of the bearer.

**Definition** tbs.h:512

[bt\_tbs\_register\_param::uri\_schemes\_supported](structbt__tbs__register__param.md#a4ffe59cd6d00b9b45db304b17efa22b0)

char \* uri\_schemes\_supported

The Uniform Resource Identifiers schemes supported by this bearer as an UTF-8 string.

**Definition** tbs.h:483

[bt\_tbs\_register\_param::provider\_name](structbt__tbs__register__param.md#a8cf7713269e8bb193c61be01d6971922)

char \* provider\_name

The name of the provider, for example a cellular service provider.

**Definition** tbs.h:468

[bt\_tbs\_register\_param::gtbs](structbt__tbs__register__param.md#aa38a646b7121b555846f7acea9bc9365)

bool gtbs

Whether this bearer shall be registered as a Generic Telephone Bearer server.

**Definition** tbs.h:491

[bt\_tbs\_register\_param::uci](structbt__tbs__register__param.md#ab7a0dc41a9e4c898ffd1afaffdfae51d)

char \* uci

The Uniform Caller Identifier of the bearer.

**Definition** tbs.h:475

[bt\_tbs\_register\_param::authorization\_required](structbt__tbs__register__param.md#af88bfd0ac0e83f94e9e467064b4c6c32)

bool authorization\_required

Whether the application will need to authorize changes to calls.

**Definition** tbs.h:498

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [tbs.h](tbs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
