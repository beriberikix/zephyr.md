---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/tbs_8h_source.html
original_path: doxygen/html/tbs_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tbs.h

[Go to the documentation of this file.](tbs_8h.md)

1

9

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_TBS\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_TBS\_H\_

12

13#include <[stdint.h](stdint_8h.md)>

14#include <[stdbool.h](stdbool_8h.md)>

15

16#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

17

18/\* Call States \*/

[ 19](tbs_8h.md#a829309945831c0e8ac36c3dd79ae26f3)#define BT\_TBS\_CALL\_STATE\_INCOMING 0x00

[ 20](tbs_8h.md#a482f9627308cad1e56a4a5a5906c2308)#define BT\_TBS\_CALL\_STATE\_DIALING 0x01

[ 21](tbs_8h.md#ada61fd749f2119452429dd712d283dad)#define BT\_TBS\_CALL\_STATE\_ALERTING 0x02

[ 22](tbs_8h.md#a3100ab7a7db823d86198847ec0df4adc)#define BT\_TBS\_CALL\_STATE\_ACTIVE 0x03

[ 23](tbs_8h.md#ac900fe331fe5b81d7ed0b21796d3e16c)#define BT\_TBS\_CALL\_STATE\_LOCALLY\_HELD 0x04

[ 24](tbs_8h.md#a76acd3539931a32361fd0deb3bbe8243)#define BT\_TBS\_CALL\_STATE\_REMOTELY\_HELD 0x05

[ 25](tbs_8h.md#a0d28984faadc6904f72068df6ab6c97d)#define BT\_TBS\_CALL\_STATE\_LOCALLY\_AND\_REMOTELY\_HELD 0x06

26

27/\* Terminate Reason \*/

[ 28](tbs_8h.md#af7f2abd7e794806ab6b119bee47db6c6)#define BT\_TBS\_REASON\_BAD\_REMOTE\_URI 0x00

[ 29](tbs_8h.md#acd5a09f5786e01662e29d49aa5307046)#define BT\_TBS\_REASON\_CALL\_FAILED 0x01

[ 30](tbs_8h.md#a4bc073b85c6eca1f0a4b0757e1050dde)#define BT\_TBS\_REASON\_REMOTE\_ENDED\_CALL 0x02

[ 31](tbs_8h.md#aa4f89b5fa61dcc4ee7e4fb6ae0e12384)#define BT\_TBS\_REASON\_SERVER\_ENDED\_CALL 0x03

[ 32](tbs_8h.md#a3105e7b0b91b71eb55c1ea5c3bfd6df3)#define BT\_TBS\_REASON\_LINE\_BUSY 0x04

[ 33](tbs_8h.md#ae195db56d2cd949a29d261c5473eea89)#define BT\_TBS\_REASON\_NETWORK\_CONGESTED 0x05

[ 34](tbs_8h.md#a614adc266444030ac83dc6f4d2e89563)#define BT\_TBS\_REASON\_CLIENT\_TERMINATED 0x06

[ 35](tbs_8h.md#aa4dab0b5c08dcf092a125986519a7d55)#define BT\_TBS\_REASON\_UNSPECIFIED 0x07

36

37/\* Application error codes \*/

[ 38](tbs_8h.md#aa92fdb19227ee0b268f2395f3f6a5f63)#define BT\_TBS\_RESULT\_CODE\_SUCCESS 0x00

[ 39](tbs_8h.md#afac3c970b36f37c815c4370dfef89f09)#define BT\_TBS\_RESULT\_CODE\_OPCODE\_NOT\_SUPPORTED 0x01

[ 40](tbs_8h.md#ae83a73a5a0474a62dfbcb5ced6eb3f78)#define BT\_TBS\_RESULT\_CODE\_OPERATION\_NOT\_POSSIBLE 0x02

[ 41](tbs_8h.md#adc371a3a898b3ecac56d8778109f315d)#define BT\_TBS\_RESULT\_CODE\_INVALID\_CALL\_INDEX 0x03

[ 42](tbs_8h.md#a3fa49179525369502018912115c1ccce)#define BT\_TBS\_RESULT\_CODE\_STATE\_MISMATCH 0x04

[ 43](tbs_8h.md#a148585f5cfe8b1cd7f8db404dac91cdd)#define BT\_TBS\_RESULT\_CODE\_OUT\_OF\_RESOURCES 0x05

[ 44](tbs_8h.md#aa60f75b90f461246b2f470930a60efc2)#define BT\_TBS\_RESULT\_CODE\_INVALID\_URI 0x06

45

[ 46](tbs_8h.md#abb6c3b57d7c48620b0f019992c55e585)#define BT\_TBS\_FEATURE\_HOLD BIT(0)

[ 47](tbs_8h.md#a962ce8d27abbdc48adbc01b2c68cb042)#define BT\_TBS\_FEATURE\_JOIN BIT(1)

48

[ 49](tbs_8h.md#a30e16c850047bed67ce70c02b793e6e1)#define BT\_TBS\_CALL\_FLAG\_SET\_INCOMING(flag) (flag &= ~BIT(0))

[ 50](tbs_8h.md#a95f2433c1c809ee449def18aae81919f)#define BT\_TBS\_CALL\_FLAG\_SET\_OUTGOING(flag) (flag |= BIT(0))

51

[ 52](tbs_8h.md#a310c1cdffee350fe5235b3ad929ac715)#define BT\_TBS\_SIGNAL\_STRENGTH\_NO\_SERVICE 0

[ 53](tbs_8h.md#ae619d9096b41690ba77ee3e7bd838be3)#define BT\_TBS\_SIGNAL\_STRENGTH\_MAX 100

[ 54](tbs_8h.md#ab8a433da27a61cf1c7be2fc7b006e298)#define BT\_TBS\_SIGNAL\_STRENGTH\_UNKNOWN 255

55

56/\* Bearer Technology \*/

[ 57](tbs_8h.md#af125f3486c88517c9e1e218c6ce492e4)#define BT\_TBS\_TECHNOLOGY\_3G 0x01

[ 58](tbs_8h.md#a967b2b97a2e862f5ae235fc9b728b15c)#define BT\_TBS\_TECHNOLOGY\_4G 0x02

[ 59](tbs_8h.md#a6962ce833da01b3a584528b2ce361447)#define BT\_TBS\_TECHNOLOGY\_LTE 0x03

[ 60](tbs_8h.md#a02af096f1153eed9623f7a7324956e86)#define BT\_TBS\_TECHNOLOGY\_WIFI 0x04

[ 61](tbs_8h.md#a28c1928de97f2b7f0e7e36bfe1a5bdde)#define BT\_TBS\_TECHNOLOGY\_5G 0x05

[ 62](tbs_8h.md#ad530e2c9b8b616a9674012ecc801421f)#define BT\_TBS\_TECHNOLOGY\_GSM 0x06

[ 63](tbs_8h.md#aeb6d5ed9dcdba0849f81413ef08570bc)#define BT\_TBS\_TECHNOLOGY\_CDMA 0x07

[ 64](tbs_8h.md#afcb1e805e56eb93f6a19b63f2cbf524c)#define BT\_TBS\_TECHNOLOGY\_2G 0x08

[ 65](tbs_8h.md#a3b828481ce60034abbdab8aa4b1ae972)#define BT\_TBS\_TECHNOLOGY\_WCDMA 0x09

[ 66](tbs_8h.md#a8fe15369938db5e013a3cafe9bbb2b73)#define BT\_TBS\_TECHNOLOGY\_IP 0x0a

67

[ 74](tbs_8h.md#a25aa807f2e3a01d030edf4f064a4fbfd)#define BT\_TBS\_GTBS\_INDEX 0xFF

75

77struct bt\_tbs\_instance;

78

[ 89](tbs_8h.md#a60e9e143f247bb7e668293f0233ce300)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_tbs\_originate\_call\_cb](tbs_8h.md#a60e9e143f247bb7e668293f0233ce300))(struct bt\_conn \*conn,

90 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index,

91 const char \*uri);

92

[ 102](tbs_8h.md#a69e93b48b2a48e8a6552882660b791cc)typedef void (\*[bt\_tbs\_terminate\_call\_cb](tbs_8h.md#a69e93b48b2a48e8a6552882660b791cc))(struct bt\_conn \*conn,

103 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index,

104 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

105

[ 113](tbs_8h.md#aa45b3f4837165d722c2df6f202a39058)typedef void (\*[bt\_tbs\_join\_calls\_cb](tbs_8h.md#aa45b3f4837165d722c2df6f202a39058))(struct bt\_conn \*conn,

114 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index\_count,

115 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes);

116

[ 123](tbs_8h.md#a2fa85f3cd96f25f6bb4f449fc9210fa1)typedef void (\*[bt\_tbs\_call\_change\_cb](tbs_8h.md#a2fa85f3cd96f25f6bb4f449fc9210fa1))(struct bt\_conn \*conn,

124 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

125

[ 135](tbs_8h.md#a1cc9e7140531b07bf6a8dedbc17f24c0)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_tbs\_authorize\_cb](tbs_8h.md#a1cc9e7140531b07bf6a8dedbc17f24c0))(struct bt\_conn \*conn);

136

[ 137](structbt__tbs__cb.md)struct [bt\_tbs\_cb](structbt__tbs__cb.md) {

[ 138](structbt__tbs__cb.md#a566504bee9c7334c53a23223e544855f) [bt\_tbs\_originate\_call\_cb](tbs_8h.md#a60e9e143f247bb7e668293f0233ce300) [originate\_call](structbt__tbs__cb.md#a566504bee9c7334c53a23223e544855f);

[ 139](structbt__tbs__cb.md#ab065a5c58db19feb2a1d3013983ed5aa) [bt\_tbs\_terminate\_call\_cb](tbs_8h.md#a69e93b48b2a48e8a6552882660b791cc) [terminate\_call](structbt__tbs__cb.md#ab065a5c58db19feb2a1d3013983ed5aa);

[ 140](structbt__tbs__cb.md#a8b76dd9243e97d22e0d6c2ac578aa383) [bt\_tbs\_call\_change\_cb](tbs_8h.md#a2fa85f3cd96f25f6bb4f449fc9210fa1) [hold\_call](structbt__tbs__cb.md#a8b76dd9243e97d22e0d6c2ac578aa383);

[ 141](structbt__tbs__cb.md#a798c09c04a563800c4d9328c1d9e2de6) [bt\_tbs\_call\_change\_cb](tbs_8h.md#a2fa85f3cd96f25f6bb4f449fc9210fa1) [accept\_call](structbt__tbs__cb.md#a798c09c04a563800c4d9328c1d9e2de6);

[ 142](structbt__tbs__cb.md#ad543a2f26d1749eba0774e2352b53692) [bt\_tbs\_call\_change\_cb](tbs_8h.md#a2fa85f3cd96f25f6bb4f449fc9210fa1) [retrieve\_call](structbt__tbs__cb.md#ad543a2f26d1749eba0774e2352b53692);

[ 143](structbt__tbs__cb.md#ac1a99a703687a3ef5ebc12eca5f6c2e7) [bt\_tbs\_join\_calls\_cb](tbs_8h.md#aa45b3f4837165d722c2df6f202a39058) [join\_calls](structbt__tbs__cb.md#ac1a99a703687a3ef5ebc12eca5f6c2e7);

[ 144](structbt__tbs__cb.md#ab7c859ffaebcf16db71c5d54bd4f5802) [bt\_tbs\_authorize\_cb](tbs_8h.md#a1cc9e7140531b07bf6a8dedbc17f24c0) [authorize](structbt__tbs__cb.md#ab7c859ffaebcf16db71c5d54bd4f5802);

145};

146

[ 155](tbs_8h.md#a1b942bcf8287641f9cd53824b4d6e77b)int [bt\_tbs\_accept](tbs_8h.md#a1b942bcf8287641f9cd53824b4d6e77b)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

156

[ 165](tbs_8h.md#ab72044a1f5466114b5efb88dfcd2f097)int [bt\_tbs\_hold](tbs_8h.md#ab72044a1f5466114b5efb88dfcd2f097)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

166

[ 175](tbs_8h.md#ad0b45af09b82d6cd66a8481c0e67e04e)int [bt\_tbs\_retrieve](tbs_8h.md#ad0b45af09b82d6cd66a8481c0e67e04e)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

176

[ 185](tbs_8h.md#a82553640882ac74f9af84bfe09ff47ee)int [bt\_tbs\_terminate](tbs_8h.md#a82553640882ac74f9af84bfe09ff47ee)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

186

[ 198](tbs_8h.md#adeae51d7cecd80abcdcde1195bb1dfba)int [bt\_tbs\_originate](tbs_8h.md#adeae51d7cecd80abcdcde1195bb1dfba)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, char \*uri, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_index);

199

[ 209](tbs_8h.md#a23226d41e3b98a53ec9a9c2fa346c9ac)int [bt\_tbs\_join](tbs_8h.md#a23226d41e3b98a53ec9a9c2fa346c9ac)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index\_cnt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes);

210

[ 219](tbs_8h.md#a868b83450f7425e8a0c8cfb7c1de45d8)int [bt\_tbs\_remote\_answer](tbs_8h.md#a868b83450f7425e8a0c8cfb7c1de45d8)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

220

[ 229](tbs_8h.md#a5ffa1a3e3b548d90a3b6a07c6bb4fc7e)int [bt\_tbs\_remote\_hold](tbs_8h.md#a5ffa1a3e3b548d90a3b6a07c6bb4fc7e)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

230

[ 239](tbs_8h.md#a09a3e64040819b6b8b694b94d2f62ca0)int [bt\_tbs\_remote\_retrieve](tbs_8h.md#a09a3e64040819b6b8b694b94d2f62ca0)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

240

[ 249](tbs_8h.md#a52afc7b8a22b071dbac10057579f319c)int [bt\_tbs\_remote\_terminate](tbs_8h.md#a52afc7b8a22b071dbac10057579f319c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

250

[ 262](tbs_8h.md#a47939f557e4d6503af9b7b85aff9d60f)int [bt\_tbs\_remote\_incoming](tbs_8h.md#a47939f557e4d6503af9b7b85aff9d60f)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*to,

263 const char \*from, const char \*friendly\_name);

264

[ 275](tbs_8h.md#a5118db6b23b387956e75eda8aecd53d5)int [bt\_tbs\_set\_bearer\_provider\_name](tbs_8h.md#a5118db6b23b387956e75eda8aecd53d5)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*name);

276

[ 287](tbs_8h.md#af4c576b8aa599f1bd9598964bc1b779f)int [bt\_tbs\_set\_bearer\_technology](tbs_8h.md#af4c576b8aa599f1bd9598964bc1b779f)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_technology);

288

[ 299](tbs_8h.md#ac316adedf7fda441ee55feb9d24d1a94)int [bt\_tbs\_set\_signal\_strength](tbs_8h.md#ac316adedf7fda441ee55feb9d24d1a94)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index,

300 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_signal\_strength);

301

[ 312](tbs_8h.md#a838e51a85f9833e0822090cd3df09e00)int [bt\_tbs\_set\_status\_flags](tbs_8h.md#a838e51a85f9833e0822090cd3df09e00)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) status\_flags);

313

[ 322](tbs_8h.md#a90b3fb1d757fbb134649b0d7f9047123)int [bt\_tbs\_set\_uri\_scheme\_list](tbs_8h.md#a90b3fb1d757fbb134649b0d7f9047123)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*\*uri\_list,

323 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uri\_count);

[ 329](tbs_8h.md#a76f120dba549225a6f2c2c22be08edfc)void [bt\_tbs\_register\_cb](tbs_8h.md#a76f120dba549225a6f2c2c22be08edfc)(struct [bt\_tbs\_cb](structbt__tbs__cb.md) \*cbs);

330

[ 332](tbs_8h.md#a62f5008cbfba158fe399cfaf683d1d2e)void [bt\_tbs\_dbg\_print\_calls](tbs_8h.md#a62f5008cbfba158fe399cfaf683d1d2e)(void);

333

[ 334](structbt__tbs__client__call__state.md)struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) {

[ 335](structbt__tbs__client__call__state.md#a3d6eb4dda7adcd16c04ebbd41242c292) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [index](structbt__tbs__client__call__state.md#a3d6eb4dda7adcd16c04ebbd41242c292);

[ 336](structbt__tbs__client__call__state.md#a3e758ad6d0b35f26f43584e50c9a9895) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](structbt__tbs__client__call__state.md#a3e758ad6d0b35f26f43584e50c9a9895);

[ 337](structbt__tbs__client__call__state.md#a57ed9dd726faa3c219e1c858ad6659d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structbt__tbs__client__call__state.md#a57ed9dd726faa3c219e1c858ad6659d9);

338} \_\_packed;

339

[ 340](structbt__tbs__client__call.md)struct [bt\_tbs\_client\_call](structbt__tbs__client__call.md) {

[ 341](structbt__tbs__client__call.md#a480279fea551db1bcb260de81edd6571) struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) [call\_info](structbt__tbs__client__call.md#a480279fea551db1bcb260de81edd6571);

[ 342](structbt__tbs__client__call.md#af04f0576e786250526c12e1436a60c4e) char \*[remote\_uri](structbt__tbs__client__call.md#af04f0576e786250526c12e1436a60c4e);

343};

344

[ 355](tbs_8h.md#a9cac11cc696be9fb387f2f7685e0d8a7)typedef void (\*[bt\_tbs\_client\_discover\_cb](tbs_8h.md#a9cac11cc696be9fb387f2f7685e0d8a7))(struct bt\_conn \*conn, int err,

356 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tbs\_count, bool gtbs\_found);

357

[ 366](tbs_8h.md#af77231168e4444da7aef203cc9eaca95)typedef void (\*[bt\_tbs\_client\_write\_value\_cb](tbs_8h.md#af77231168e4444da7aef203cc9eaca95))(struct bt\_conn \*conn, int err,

367 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

368

[ 379](tbs_8h.md#a40b8b3d1b318a1b5c5524877bbc2f90f)typedef void (\*[bt\_tbs\_client\_cp\_cb](tbs_8h.md#a40b8b3d1b318a1b5c5524877bbc2f90f))(struct bt\_conn \*conn, int err,

380 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

381

[ 392](tbs_8h.md#a4d7632de7c2006e478880950076908a9)typedef void (\*[bt\_tbs\_client\_read\_string\_cb](tbs_8h.md#a4d7632de7c2006e478880950076908a9))(struct bt\_conn \*conn, int err,

393 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

394 const char \*value);

395

[ 405](tbs_8h.md#a600051910ed538a2da823554df23dd20)typedef void (\*[bt\_tbs\_client\_read\_value\_cb](tbs_8h.md#a600051910ed538a2da823554df23dd20))(struct bt\_conn \*conn, int err,

406 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

407

[ 418](tbs_8h.md#ab881b3caaaa4425e52afd84e53adee78)typedef void (\*[bt\_tbs\_client\_termination\_reason\_cb](tbs_8h.md#ab881b3caaaa4425e52afd84e53adee78))(struct bt\_conn \*conn,

419 int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

420 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index,

421 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

422

[ 434](tbs_8h.md#a7b31e1c30fa96081a3ef38e1a481b64f)typedef void (\*[bt\_tbs\_client\_current\_calls\_cb](tbs_8h.md#a7b31e1c30fa96081a3ef38e1a481b64f))(struct bt\_conn \*conn, int err,

435 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

436 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_count,

437 const struct [bt\_tbs\_client\_call](structbt__tbs__client__call.md) \*calls);

438

[ 450](tbs_8h.md#a262ca74b7ae2f0c52657066549fa4f92)typedef void (\*[bt\_tbs\_client\_call\_states\_cb](tbs_8h.md#a262ca74b7ae2f0c52657066549fa4f92))(struct bt\_conn \*conn, int err,

451 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

452 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_count,

453 const struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) \*call\_states);

454

[ 455](structbt__tbs__client__cb.md)struct [bt\_tbs\_client\_cb](structbt__tbs__client__cb.md) {

[ 456](structbt__tbs__client__cb.md#abfd4542a0781ff5676a191249f121e91) [bt\_tbs\_client\_discover\_cb](tbs_8h.md#a9cac11cc696be9fb387f2f7685e0d8a7) [discover](structbt__tbs__client__cb.md#abfd4542a0781ff5676a191249f121e91);

457#if defined(CONFIG\_BT\_TBS\_CLIENT\_ORIGINATE\_CALL)

458 [bt\_tbs\_client\_cp\_cb](tbs_8h.md#a40b8b3d1b318a1b5c5524877bbc2f90f) originate\_call;

459#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_ORIGINATE\_CALL) \*/

460#if defined(CONFIG\_BT\_TBS\_CLIENT\_TERMINATE\_CALL)

461 [bt\_tbs\_client\_cp\_cb](tbs_8h.md#a40b8b3d1b318a1b5c5524877bbc2f90f) terminate\_call;

462#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_TERMINATE\_CALL) \*/

463#if defined(CONFIG\_BT\_TBS\_CLIENT\_HOLD\_CALL)

464 [bt\_tbs\_client\_cp\_cb](tbs_8h.md#a40b8b3d1b318a1b5c5524877bbc2f90f) hold\_call;

465#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_HOLD\_CALL) \*/

466#if defined(CONFIG\_BT\_TBS\_CLIENT\_ACCEPT\_CALL)

467 [bt\_tbs\_client\_cp\_cb](tbs_8h.md#a40b8b3d1b318a1b5c5524877bbc2f90f) accept\_call;

468#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_ACCEPT\_CALL) \*/

469#if defined(CONFIG\_BT\_TBS\_CLIENT\_RETRIEVE\_CALL)

470 [bt\_tbs\_client\_cp\_cb](tbs_8h.md#a40b8b3d1b318a1b5c5524877bbc2f90f) retrieve\_call;

471#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_RETRIEVE\_CALL) \*/

472#if defined(CONFIG\_BT\_TBS\_CLIENT\_JOIN\_CALLS)

473 [bt\_tbs\_client\_cp\_cb](tbs_8h.md#a40b8b3d1b318a1b5c5524877bbc2f90f) join\_calls;

474#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_JOIN\_CALLS) \*/

475#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_PROVIDER\_NAME)

476 [bt\_tbs\_client\_read\_string\_cb](tbs_8h.md#a4d7632de7c2006e478880950076908a9) bearer\_provider\_name;

477#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_PROVIDER\_NAME) \*/

478#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_UCI)

479 [bt\_tbs\_client\_read\_string\_cb](tbs_8h.md#a4d7632de7c2006e478880950076908a9) bearer\_uci;

480#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_UCI) \*/

481#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_TECHNOLOGY)

482 [bt\_tbs\_client\_read\_value\_cb](tbs_8h.md#a600051910ed538a2da823554df23dd20) technology;

483#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_TECHNOLOGY) \*/

484#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_URI\_SCHEMES\_SUPPORTED\_LIST)

485 [bt\_tbs\_client\_read\_string\_cb](tbs_8h.md#a4d7632de7c2006e478880950076908a9) uri\_list;

486#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_URI\_SCHEMES\_SUPPORTED\_LIST) \*/

487#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_SIGNAL\_STRENGTH)

488 [bt\_tbs\_client\_read\_value\_cb](tbs_8h.md#a600051910ed538a2da823554df23dd20) signal\_strength;

489#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_SIGNAL\_STRENGTH) \*/

490#if defined(CONFIG\_BT\_TBS\_CLIENT\_READ\_BEARER\_SIGNAL\_INTERVAL)

491 [bt\_tbs\_client\_read\_value\_cb](tbs_8h.md#a600051910ed538a2da823554df23dd20) signal\_interval;

492#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_READ\_BEARER\_SIGNAL\_INTERVAL) \*/

493#if defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_LIST\_CURRENT\_CALLS)

494 [bt\_tbs\_client\_current\_calls\_cb](tbs_8h.md#a7b31e1c30fa96081a3ef38e1a481b64f) current\_calls;

495#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_BEARER\_LIST\_CURRENT\_CALLS) \*/

496#if defined(CONFIG\_BT\_TBS\_CLIENT\_CCID)

497 [bt\_tbs\_client\_read\_value\_cb](tbs_8h.md#a600051910ed538a2da823554df23dd20) ccid;

498#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_CCID) \*/

499#if defined(CONFIG\_BT\_TBS\_CLIENT\_INCOMING\_URI)

500 [bt\_tbs\_client\_read\_string\_cb](tbs_8h.md#a4d7632de7c2006e478880950076908a9) call\_uri;

501#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_INCOMING\_URI) \*/

502#if defined(CONFIG\_BT\_TBS\_CLIENT\_STATUS\_FLAGS)

503 [bt\_tbs\_client\_read\_value\_cb](tbs_8h.md#a600051910ed538a2da823554df23dd20) status\_flags;

504#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_STATUS\_FLAGS) \*/

[ 505](structbt__tbs__client__cb.md#a88cb69ef54c9399bceb5641202eeabce) [bt\_tbs\_client\_call\_states\_cb](tbs_8h.md#a262ca74b7ae2f0c52657066549fa4f92) [call\_state](structbt__tbs__client__cb.md#a88cb69ef54c9399bceb5641202eeabce);

506#if defined(CONFIG\_BT\_TBS\_CLIENT\_OPTIONAL\_OPCODES)

507 [bt\_tbs\_client\_read\_value\_cb](tbs_8h.md#a600051910ed538a2da823554df23dd20) optional\_opcodes;

508#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_OPTIONAL\_OPCODES) \*/

[ 509](structbt__tbs__client__cb.md#ae8e5cbe52cbb300e1cd919d24c85c4df) [bt\_tbs\_client\_termination\_reason\_cb](tbs_8h.md#ab881b3caaaa4425e52afd84e53adee78) [termination\_reason](structbt__tbs__client__cb.md#ae8e5cbe52cbb300e1cd919d24c85c4df);

510#if defined(CONFIG\_BT\_TBS\_CLIENT\_INCOMING\_CALL)

511 [bt\_tbs\_client\_read\_string\_cb](tbs_8h.md#a4d7632de7c2006e478880950076908a9) remote\_uri;

512#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_INCOMING\_CALL) \*/

513#if defined(CONFIG\_BT\_TBS\_CLIENT\_CALL\_FRIENDLY\_NAME)

514 [bt\_tbs\_client\_read\_string\_cb](tbs_8h.md#a4d7632de7c2006e478880950076908a9) friendly\_name;

515#endif /\* defined(CONFIG\_BT\_TBS\_CLIENT\_CALL\_FRIENDLY\_NAME) \*/

516};

517

[ 526](tbs_8h.md#ac59f3dec092a14bdf234039e3dcd12eb)int [bt\_tbs\_client\_discover](tbs_8h.md#ac59f3dec092a14bdf234039e3dcd12eb)(struct bt\_conn \*conn);

527

[ 537](tbs_8h.md#a3a71c51d464aa19fbfbd2d60fc4901bc)int [bt\_tbs\_client\_set\_outgoing\_uri](tbs_8h.md#a3a71c51d464aa19fbfbd2d60fc4901bc)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

538 const char \*uri);

539

[ 552](tbs_8h.md#aa1dcb9908057d75a54fa447639826f3c)int [bt\_tbs\_client\_set\_signal\_strength\_interval](tbs_8h.md#aa1dcb9908057d75a54fa447639826f3c)(struct bt\_conn \*conn,

553 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

554 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval);

555

[ 568](tbs_8h.md#a0aac704008ffc92ce6609d3ffffc4523)int [bt\_tbs\_client\_originate\_call](tbs_8h.md#a0aac704008ffc92ce6609d3ffffc4523)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

569 const char \*uri);

570

[ 583](tbs_8h.md#a25b803bb5cae2e1a8b0398bc48137d80)int [bt\_tbs\_client\_terminate\_call](tbs_8h.md#a25b803bb5cae2e1a8b0398bc48137d80)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

584 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

585

[ 598](tbs_8h.md#a23e825de6af71d4e456b63c3a621fb61)int [bt\_tbs\_client\_hold\_call](tbs_8h.md#a23e825de6af71d4e456b63c3a621fb61)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

599 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

600

[ 613](tbs_8h.md#a625fc73885c2bfd63f0f4b2d7f72eaef)int [bt\_tbs\_client\_accept\_call](tbs_8h.md#a625fc73885c2bfd63f0f4b2d7f72eaef)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

614 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

615

[ 628](tbs_8h.md#abbe194a63da0b95dc1dca0337560a585)int [bt\_tbs\_client\_retrieve\_call](tbs_8h.md#abbe194a63da0b95dc1dca0337560a585)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

629 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index);

630

[ 644](tbs_8h.md#aae1925deb0b5865af601aa8278ffb10a)int [bt\_tbs\_client\_join\_calls](tbs_8h.md#aae1925deb0b5865af601aa8278ffb10a)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index,

645 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count);

646

[ 658](tbs_8h.md#a2053a9eb7cf28f66febd365f0b682be0)int [bt\_tbs\_client\_read\_bearer\_provider\_name](tbs_8h.md#a2053a9eb7cf28f66febd365f0b682be0)(struct bt\_conn \*conn,

659 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

660

[ 672](tbs_8h.md#aba92039d3b44da9163a22400951fafa7)int [bt\_tbs\_client\_read\_bearer\_uci](tbs_8h.md#aba92039d3b44da9163a22400951fafa7)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

673

[ 685](tbs_8h.md#a7684dbcb78e407f7002d44fbdb805e5d)int [bt\_tbs\_client\_read\_technology](tbs_8h.md#a7684dbcb78e407f7002d44fbdb805e5d)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

686

[ 698](tbs_8h.md#ad19db25591c7ae5bd0b4c2bbaefc9bed)int [bt\_tbs\_client\_read\_uri\_list](tbs_8h.md#ad19db25591c7ae5bd0b4c2bbaefc9bed)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

699

[ 711](tbs_8h.md#aabe97df55817b8e36c79de4bf30fc83f)int [bt\_tbs\_client\_read\_signal\_strength](tbs_8h.md#aabe97df55817b8e36c79de4bf30fc83f)(struct bt\_conn \*conn,

712 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

713

[ 725](tbs_8h.md#a38046c5c715d451b21a3076742268010)int [bt\_tbs\_client\_read\_signal\_interval](tbs_8h.md#a38046c5c715d451b21a3076742268010)(struct bt\_conn \*conn,

726 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

727

[ 739](tbs_8h.md#a895c7f54300e5452fb8d0c9d4b3306ae)int [bt\_tbs\_client\_read\_current\_calls](tbs_8h.md#a895c7f54300e5452fb8d0c9d4b3306ae)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

740

[ 752](tbs_8h.md#ac070ec0590df5820b7721d579ceeeb15)int [bt\_tbs\_client\_read\_ccid](tbs_8h.md#ac070ec0590df5820b7721d579ceeeb15)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

753

[ 765](tbs_8h.md#a4238a37b80b7d7ff611fe9b02b7cf54d)int [bt\_tbs\_client\_read\_call\_uri](tbs_8h.md#a4238a37b80b7d7ff611fe9b02b7cf54d)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

766

[ 778](tbs_8h.md#a9fe91df1a31ce59401347fc0eac2b701)int [bt\_tbs\_client\_read\_status\_flags](tbs_8h.md#a9fe91df1a31ce59401347fc0eac2b701)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

779

[ 788](tbs_8h.md#afeaaaefb9d4eb773dd0cbdfebe26e0b7)int [bt\_tbs\_client\_read\_call\_state](tbs_8h.md#afeaaaefb9d4eb773dd0cbdfebe26e0b7)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

789

[ 801](tbs_8h.md#ab04f8355c32fce501bd757b75ee9d38a)int [bt\_tbs\_client\_read\_remote\_uri](tbs_8h.md#ab04f8355c32fce501bd757b75ee9d38a)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

802

[ 814](tbs_8h.md#a99549dd6244580e157006fb17772fd8f)int [bt\_tbs\_client\_read\_friendly\_name](tbs_8h.md#a99549dd6244580e157006fb17772fd8f)(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

815

[ 826](tbs_8h.md#af504e1a11352d77a36aa087b587e4ba8)int [bt\_tbs\_client\_read\_optional\_opcodes](tbs_8h.md#af504e1a11352d77a36aa087b587e4ba8)(struct bt\_conn \*conn,

827 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index);

828

[ 834](tbs_8h.md#a349f86bbb9932bd5926008214ef297eb)void [bt\_tbs\_client\_register\_cb](tbs_8h.md#a349f86bbb9932bd5926008214ef297eb)(const struct [bt\_tbs\_client\_cb](structbt__tbs__client__cb.md) \*cbs);

835

[ 847](tbs_8h.md#aadae501fa6f7771bb9661af829805a5f)struct bt\_tbs\_instance \*[bt\_tbs\_client\_get\_by\_ccid](tbs_8h.md#aadae501fa6f7771bb9661af829805a5f)(const struct bt\_conn \*conn,

848 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid);

849

850#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_TBS\_H\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

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

**Definition** tbs.h:137

[bt\_tbs\_cb::originate\_call](structbt__tbs__cb.md#a566504bee9c7334c53a23223e544855f)

bt\_tbs\_originate\_call\_cb originate\_call

**Definition** tbs.h:138

[bt\_tbs\_cb::accept\_call](structbt__tbs__cb.md#a798c09c04a563800c4d9328c1d9e2de6)

bt\_tbs\_call\_change\_cb accept\_call

**Definition** tbs.h:141

[bt\_tbs\_cb::hold\_call](structbt__tbs__cb.md#a8b76dd9243e97d22e0d6c2ac578aa383)

bt\_tbs\_call\_change\_cb hold\_call

**Definition** tbs.h:140

[bt\_tbs\_cb::terminate\_call](structbt__tbs__cb.md#ab065a5c58db19feb2a1d3013983ed5aa)

bt\_tbs\_terminate\_call\_cb terminate\_call

**Definition** tbs.h:139

[bt\_tbs\_cb::authorize](structbt__tbs__cb.md#ab7c859ffaebcf16db71c5d54bd4f5802)

bt\_tbs\_authorize\_cb authorize

**Definition** tbs.h:144

[bt\_tbs\_cb::join\_calls](structbt__tbs__cb.md#ac1a99a703687a3ef5ebc12eca5f6c2e7)

bt\_tbs\_join\_calls\_cb join\_calls

**Definition** tbs.h:143

[bt\_tbs\_cb::retrieve\_call](structbt__tbs__cb.md#ad543a2f26d1749eba0774e2352b53692)

bt\_tbs\_call\_change\_cb retrieve\_call

**Definition** tbs.h:142

[bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md)

**Definition** tbs.h:334

[bt\_tbs\_client\_call\_state::index](structbt__tbs__client__call__state.md#a3d6eb4dda7adcd16c04ebbd41242c292)

uint8\_t index

**Definition** tbs.h:335

[bt\_tbs\_client\_call\_state::state](structbt__tbs__client__call__state.md#a3e758ad6d0b35f26f43584e50c9a9895)

uint8\_t state

**Definition** tbs.h:336

[bt\_tbs\_client\_call\_state::flags](structbt__tbs__client__call__state.md#a57ed9dd726faa3c219e1c858ad6659d9)

uint8\_t flags

**Definition** tbs.h:337

[bt\_tbs\_client\_call](structbt__tbs__client__call.md)

**Definition** tbs.h:340

[bt\_tbs\_client\_call::call\_info](structbt__tbs__client__call.md#a480279fea551db1bcb260de81edd6571)

struct bt\_tbs\_client\_call\_state call\_info

**Definition** tbs.h:341

[bt\_tbs\_client\_call::remote\_uri](structbt__tbs__client__call.md#af04f0576e786250526c12e1436a60c4e)

char \* remote\_uri

**Definition** tbs.h:342

[bt\_tbs\_client\_cb](structbt__tbs__client__cb.md)

**Definition** tbs.h:455

[bt\_tbs\_client\_cb::call\_state](structbt__tbs__client__cb.md#a88cb69ef54c9399bceb5641202eeabce)

bt\_tbs\_client\_call\_states\_cb call\_state

**Definition** tbs.h:505

[bt\_tbs\_client\_cb::discover](structbt__tbs__client__cb.md#abfd4542a0781ff5676a191249f121e91)

bt\_tbs\_client\_discover\_cb discover

**Definition** tbs.h:456

[bt\_tbs\_client\_cb::termination\_reason](structbt__tbs__client__cb.md#ae8e5cbe52cbb300e1cd919d24c85c4df)

bt\_tbs\_client\_termination\_reason\_cb termination\_reason

**Definition** tbs.h:509

[bt\_tbs\_remote\_retrieve](tbs_8h.md#a09a3e64040819b6b8b694b94d2f62ca0)

int bt\_tbs\_remote\_retrieve(uint8\_t call\_index)

Notify the server that the remote party retrieved the call.

[bt\_tbs\_client\_originate\_call](tbs_8h.md#a0aac704008ffc92ce6609d3ffffc4523)

int bt\_tbs\_client\_originate\_call(struct bt\_conn \*conn, uint8\_t inst\_index, const char \*uri)

Request to originate a call.

[bt\_tbs\_accept](tbs_8h.md#a1b942bcf8287641f9cd53824b4d6e77b)

int bt\_tbs\_accept(uint8\_t call\_index)

Accept an alerting call.

[bt\_tbs\_authorize\_cb](tbs_8h.md#a1cc9e7140531b07bf6a8dedbc17f24c0)

bool(\* bt\_tbs\_authorize\_cb)(struct bt\_conn \*conn)

Callback function for authorizing a client.

**Definition** tbs.h:135

[bt\_tbs\_client\_read\_bearer\_provider\_name](tbs_8h.md#a2053a9eb7cf28f66febd365f0b682be0)

int bt\_tbs\_client\_read\_bearer\_provider\_name(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the bearer provider name of a TBS instance.

[bt\_tbs\_join](tbs_8h.md#a23226d41e3b98a53ec9a9c2fa346c9ac)

int bt\_tbs\_join(uint8\_t call\_index\_cnt, uint8\_t \*call\_indexes)

Join calls.

[bt\_tbs\_client\_hold\_call](tbs_8h.md#a23e825de6af71d4e456b63c3a621fb61)

int bt\_tbs\_client\_hold\_call(struct bt\_conn \*conn, uint8\_t inst\_index, uint8\_t call\_index)

Request to hold a call.

[bt\_tbs\_client\_terminate\_call](tbs_8h.md#a25b803bb5cae2e1a8b0398bc48137d80)

int bt\_tbs\_client\_terminate\_call(struct bt\_conn \*conn, uint8\_t inst\_index, uint8\_t call\_index)

Request to terminate a call.

[bt\_tbs\_client\_call\_states\_cb](tbs_8h.md#a262ca74b7ae2f0c52657066549fa4f92)

void(\* bt\_tbs\_client\_call\_states\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, uint8\_t call\_count, const struct bt\_tbs\_client\_call\_state \*call\_states)

Callback function for ccp\_read\_call\_state.

**Definition** tbs.h:450

[bt\_tbs\_call\_change\_cb](tbs_8h.md#a2fa85f3cd96f25f6bb4f449fc9210fa1)

void(\* bt\_tbs\_call\_change\_cb)(struct bt\_conn \*conn, uint8\_t call\_index)

Callback function for client request call state change.

**Definition** tbs.h:123

[bt\_tbs\_client\_register\_cb](tbs_8h.md#a349f86bbb9932bd5926008214ef297eb)

void bt\_tbs\_client\_register\_cb(const struct bt\_tbs\_client\_cb \*cbs)

Register the callbacks for CCP.

[bt\_tbs\_client\_read\_signal\_interval](tbs_8h.md#a38046c5c715d451b21a3076742268010)

int bt\_tbs\_client\_read\_signal\_interval(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the signal strength reporting interval of a TBS instance.

[bt\_tbs\_client\_set\_outgoing\_uri](tbs_8h.md#a3a71c51d464aa19fbfbd2d60fc4901bc)

int bt\_tbs\_client\_set\_outgoing\_uri(struct bt\_conn \*conn, uint8\_t inst\_index, const char \*uri)

Set the outgoing URI for a TBS instance on the peer device.

[bt\_tbs\_client\_cp\_cb](tbs_8h.md#a40b8b3d1b318a1b5c5524877bbc2f90f)

void(\* bt\_tbs\_client\_cp\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, uint8\_t call\_index)

Callback function for the CCP call control functions.

**Definition** tbs.h:379

[bt\_tbs\_client\_read\_call\_uri](tbs_8h.md#a4238a37b80b7d7ff611fe9b02b7cf54d)

int bt\_tbs\_client\_read\_call\_uri(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the call target URI of a TBS instance.

[bt\_tbs\_remote\_incoming](tbs_8h.md#a47939f557e4d6503af9b7b85aff9d60f)

int bt\_tbs\_remote\_incoming(uint8\_t bearer\_index, const char \*to, const char \*from, const char \*friendly\_name)

Notify the server of an incoming call.

[bt\_tbs\_client\_read\_string\_cb](tbs_8h.md#a4d7632de7c2006e478880950076908a9)

void(\* bt\_tbs\_client\_read\_string\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, const char \*value)

Callback function for functions that read a string value.

**Definition** tbs.h:392

[bt\_tbs\_set\_bearer\_provider\_name](tbs_8h.md#a5118db6b23b387956e75eda8aecd53d5)

int bt\_tbs\_set\_bearer\_provider\_name(uint8\_t bearer\_index, const char \*name)

Set a new bearer provider.

[bt\_tbs\_remote\_terminate](tbs_8h.md#a52afc7b8a22b071dbac10057579f319c)

int bt\_tbs\_remote\_terminate(uint8\_t call\_index)

Notify the server that the remote party terminated the call.

[bt\_tbs\_remote\_hold](tbs_8h.md#a5ffa1a3e3b548d90a3b6a07c6bb4fc7e)

int bt\_tbs\_remote\_hold(uint8\_t call\_index)

Notify the server that the remote party held the call.

[bt\_tbs\_client\_read\_value\_cb](tbs_8h.md#a600051910ed538a2da823554df23dd20)

void(\* bt\_tbs\_client\_read\_value\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, uint32\_t value)

Callback function for functions that read an integer value.

**Definition** tbs.h:405

[bt\_tbs\_originate\_call\_cb](tbs_8h.md#a60e9e143f247bb7e668293f0233ce300)

bool(\* bt\_tbs\_originate\_call\_cb)(struct bt\_conn \*conn, uint8\_t call\_index, const char \*uri)

Callback function for client originating a call.

**Definition** tbs.h:89

[bt\_tbs\_client\_accept\_call](tbs_8h.md#a625fc73885c2bfd63f0f4b2d7f72eaef)

int bt\_tbs\_client\_accept\_call(struct bt\_conn \*conn, uint8\_t inst\_index, uint8\_t call\_index)

Accept an incoming call.

[bt\_tbs\_dbg\_print\_calls](tbs_8h.md#a62f5008cbfba158fe399cfaf683d1d2e)

void bt\_tbs\_dbg\_print\_calls(void)

Prints all calls of all services to the debug log.

[bt\_tbs\_terminate\_call\_cb](tbs_8h.md#a69e93b48b2a48e8a6552882660b791cc)

void(\* bt\_tbs\_terminate\_call\_cb)(struct bt\_conn \*conn, uint8\_t call\_index, uint8\_t reason)

Callback function for client terminating a call.

**Definition** tbs.h:102

[bt\_tbs\_client\_read\_technology](tbs_8h.md#a7684dbcb78e407f7002d44fbdb805e5d)

int bt\_tbs\_client\_read\_technology(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the technology of a TBS instance.

[bt\_tbs\_register\_cb](tbs_8h.md#a76f120dba549225a6f2c2c22be08edfc)

void bt\_tbs\_register\_cb(struct bt\_tbs\_cb \*cbs)

Register the callbacks for TBS.

[bt\_tbs\_client\_current\_calls\_cb](tbs_8h.md#a7b31e1c30fa96081a3ef38e1a481b64f)

void(\* bt\_tbs\_client\_current\_calls\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, uint8\_t call\_count, const struct bt\_tbs\_client\_call \*calls)

Callback function for ccp\_read\_current\_calls.

**Definition** tbs.h:434

[bt\_tbs\_terminate](tbs_8h.md#a82553640882ac74f9af84bfe09ff47ee)

int bt\_tbs\_terminate(uint8\_t call\_index)

Terminate a call.

[bt\_tbs\_set\_status\_flags](tbs_8h.md#a838e51a85f9833e0822090cd3df09e00)

int bt\_tbs\_set\_status\_flags(uint8\_t bearer\_index, uint16\_t status\_flags)

Sets the feature and status value.

[bt\_tbs\_remote\_answer](tbs_8h.md#a868b83450f7425e8a0c8cfb7c1de45d8)

int bt\_tbs\_remote\_answer(uint8\_t call\_index)

Notify the server that the remote party answered the call.

[bt\_tbs\_client\_read\_current\_calls](tbs_8h.md#a895c7f54300e5452fb8d0c9d4b3306ae)

int bt\_tbs\_client\_read\_current\_calls(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the list of current calls of a TBS instance.

[bt\_tbs\_set\_uri\_scheme\_list](tbs_8h.md#a90b3fb1d757fbb134649b0d7f9047123)

int bt\_tbs\_set\_uri\_scheme\_list(uint8\_t bearer\_index, const char \*\*uri\_list, uint8\_t uri\_count)

Sets the URI scheme list of a bearer.

[bt\_tbs\_client\_read\_friendly\_name](tbs_8h.md#a99549dd6244580e157006fb17772fd8f)

int bt\_tbs\_client\_read\_friendly\_name(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the friendly name of a call for a TBS instance.

[bt\_tbs\_client\_discover\_cb](tbs_8h.md#a9cac11cc696be9fb387f2f7685e0d8a7)

void(\* bt\_tbs\_client\_discover\_cb)(struct bt\_conn \*conn, int err, uint8\_t tbs\_count, bool gtbs\_found)

Callback function for ccp\_discover.

**Definition** tbs.h:355

[bt\_tbs\_client\_read\_status\_flags](tbs_8h.md#a9fe91df1a31ce59401347fc0eac2b701)

int bt\_tbs\_client\_read\_status\_flags(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the feature and status value of a TBS instance.

[bt\_tbs\_client\_set\_signal\_strength\_interval](tbs_8h.md#aa1dcb9908057d75a54fa447639826f3c)

int bt\_tbs\_client\_set\_signal\_strength\_interval(struct bt\_conn \*conn, uint8\_t inst\_index, uint8\_t interval)

Set the signal strength reporting interval for a TBS instance.

[bt\_tbs\_join\_calls\_cb](tbs_8h.md#aa45b3f4837165d722c2df6f202a39058)

void(\* bt\_tbs\_join\_calls\_cb)(struct bt\_conn \*conn, uint8\_t call\_index\_count, const uint8\_t \*call\_indexes)

Callback function for client joining calls.

**Definition** tbs.h:113

[bt\_tbs\_client\_read\_signal\_strength](tbs_8h.md#aabe97df55817b8e36c79de4bf30fc83f)

int bt\_tbs\_client\_read\_signal\_strength(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the current signal strength of a TBS instance.

[bt\_tbs\_client\_get\_by\_ccid](tbs_8h.md#aadae501fa6f7771bb9661af829805a5f)

struct bt\_tbs\_instance \* bt\_tbs\_client\_get\_by\_ccid(const struct bt\_conn \*conn, uint8\_t ccid)

Look up Telephone Bearer Service instance by CCID.

[bt\_tbs\_client\_join\_calls](tbs_8h.md#aae1925deb0b5865af601aa8278ffb10a)

int bt\_tbs\_client\_join\_calls(struct bt\_conn \*conn, uint8\_t inst\_index, const uint8\_t \*call\_indexes, uint8\_t count)

Join multiple calls.

[bt\_tbs\_client\_read\_remote\_uri](tbs_8h.md#ab04f8355c32fce501bd757b75ee9d38a)

int bt\_tbs\_client\_read\_remote\_uri(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the remote URI of a TBS instance.

[bt\_tbs\_hold](tbs_8h.md#ab72044a1f5466114b5efb88dfcd2f097)

int bt\_tbs\_hold(uint8\_t call\_index)

Hold a call.

[bt\_tbs\_client\_termination\_reason\_cb](tbs_8h.md#ab881b3caaaa4425e52afd84e53adee78)

void(\* bt\_tbs\_client\_termination\_reason\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index, uint8\_t call\_index, uint8\_t reason)

Callback function for ccp\_read\_termination\_reason.

**Definition** tbs.h:418

[bt\_tbs\_client\_read\_bearer\_uci](tbs_8h.md#aba92039d3b44da9163a22400951fafa7)

int bt\_tbs\_client\_read\_bearer\_uci(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the UCI of a TBS instance.

[bt\_tbs\_client\_retrieve\_call](tbs_8h.md#abbe194a63da0b95dc1dca0337560a585)

int bt\_tbs\_client\_retrieve\_call(struct bt\_conn \*conn, uint8\_t inst\_index, uint8\_t call\_index)

Retrieve call from (local) hold.

[bt\_tbs\_client\_read\_ccid](tbs_8h.md#ac070ec0590df5820b7721d579ceeeb15)

int bt\_tbs\_client\_read\_ccid(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the content ID of a TBS instance.

[bt\_tbs\_set\_signal\_strength](tbs_8h.md#ac316adedf7fda441ee55feb9d24d1a94)

int bt\_tbs\_set\_signal\_strength(uint8\_t bearer\_index, uint8\_t new\_signal\_strength)

Update the signal strength reported by the server.

[bt\_tbs\_client\_discover](tbs_8h.md#ac59f3dec092a14bdf234039e3dcd12eb)

int bt\_tbs\_client\_discover(struct bt\_conn \*conn)

Discover TBS for a connection.

[bt\_tbs\_retrieve](tbs_8h.md#ad0b45af09b82d6cd66a8481c0e67e04e)

int bt\_tbs\_retrieve(uint8\_t call\_index)

Retrieve a call.

[bt\_tbs\_client\_read\_uri\_list](tbs_8h.md#ad19db25591c7ae5bd0b4c2bbaefc9bed)

int bt\_tbs\_client\_read\_uri\_list(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the URI schemes list of a TBS instance.

[bt\_tbs\_originate](tbs_8h.md#adeae51d7cecd80abcdcde1195bb1dfba)

int bt\_tbs\_originate(uint8\_t bearer\_index, char \*uri, uint8\_t \*call\_index)

Originate a call.

[bt\_tbs\_set\_bearer\_technology](tbs_8h.md#af4c576b8aa599f1bd9598964bc1b779f)

int bt\_tbs\_set\_bearer\_technology(uint8\_t bearer\_index, uint8\_t new\_technology)

Set a new bearer technology.

[bt\_tbs\_client\_read\_optional\_opcodes](tbs_8h.md#af504e1a11352d77a36aa087b587e4ba8)

int bt\_tbs\_client\_read\_optional\_opcodes(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the supported opcode of a TBS instance.

[bt\_tbs\_client\_write\_value\_cb](tbs_8h.md#af77231168e4444da7aef203cc9eaca95)

void(\* bt\_tbs\_client\_write\_value\_cb)(struct bt\_conn \*conn, int err, uint8\_t inst\_index)

Callback function for writing values to peer device.

**Definition** tbs.h:366

[bt\_tbs\_client\_read\_call\_state](tbs_8h.md#afeaaaefb9d4eb773dd0cbdfebe26e0b7)

int bt\_tbs\_client\_read\_call\_state(struct bt\_conn \*conn, uint8\_t inst\_index)

Read the states of the current calls of a TBS instance.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [tbs.h](tbs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
