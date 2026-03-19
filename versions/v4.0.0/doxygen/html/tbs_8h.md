---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tbs_8h.html
original_path: doxygen/html/tbs_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tbs.h File Reference

Public APIs for Bluetooth Telephone Bearer Service.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](tbs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_tbs\_cb](structbt__tbs__cb.md) |
|  | Struct to hold the Telephone Bearer Service callbacks. [More...](structbt__tbs__cb.md#details) |
| struct | [bt\_tbs\_register\_param](structbt__tbs__register__param.md) |
| struct | [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) |
|  | Struct to hold a call state. [More...](structbt__tbs__client__call__state.md#details) |
| struct | [bt\_tbs\_client\_call](structbt__tbs__client__call.md) |
|  | Struct to hold a call as the Telephone Bearer Service client. [More...](structbt__tbs__client__call.md#details) |
| struct | [bt\_tbs\_client\_cb](structbt__tbs__client__cb.md) |
|  | Struct to hold the Telephone Bearer Service client callbacks. [More...](structbt__tbs__client__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_TBS\_GTBS\_INDEX](group__bt__tbs.md#ga25aa807f2e3a01d030edf4f064a4fbfd)   0xFF |
|  | The GTBS index denotes whenever a callback is from a Generic Telephone Bearer Service (GTBS) instance, or whenever the client should perform on action on the GTBS instance of the server, rather than any of the specific Telephone Bearer Service instances. |
| Call States | |
| #define | [BT\_TBS\_CALL\_STATE\_INCOMING](group__bt__tbs.md#ga829309945831c0e8ac36c3dd79ae26f3)   0x00 |
|  | A remote party is calling (incoming call). |
| #define | [BT\_TBS\_CALL\_STATE\_DIALING](group__bt__tbs.md#ga482f9627308cad1e56a4a5a5906c2308)   0x01 |
|  | The process to call the remote party has started on the server, but the remote party is not being alerted (outgoing call). |
| #define | [BT\_TBS\_CALL\_STATE\_ALERTING](group__bt__tbs.md#gada61fd749f2119452429dd712d283dad)   0x02 |
|  | A remote party is being alerted (outgoing call). |
| #define | [BT\_TBS\_CALL\_STATE\_ACTIVE](group__bt__tbs.md#ga3100ab7a7db823d86198847ec0df4adc)   0x03 |
|  | The call is in an active conversation. |
| #define | [BT\_TBS\_CALL\_STATE\_LOCALLY\_HELD](group__bt__tbs.md#gac900fe331fe5b81d7ed0b21796d3e16c)   0x04 |
|  | The call is connected but held locally. |
| #define | [BT\_TBS\_CALL\_STATE\_REMOTELY\_HELD](group__bt__tbs.md#ga76acd3539931a32361fd0deb3bbe8243)   0x05 |
|  | The call is connected but held remotely. |
| #define | [BT\_TBS\_CALL\_STATE\_LOCALLY\_AND\_REMOTELY\_HELD](group__bt__tbs.md#ga0d28984faadc6904f72068df6ab6c97d)   0x06 |
|  | The call is connected but held both locally and remotely. |
| Terminate Reason | |
| #define | [BT\_TBS\_REASON\_BAD\_REMOTE\_URI](group__bt__tbs.md#gaf7f2abd7e794806ab6b119bee47db6c6)   0x00 |
|  | The URI value used to originate a call was formed improperly. |
| #define | [BT\_TBS\_REASON\_CALL\_FAILED](group__bt__tbs.md#gacd5a09f5786e01662e29d49aa5307046)   0x01 |
|  | The call failed. |
| #define | [BT\_TBS\_REASON\_REMOTE\_ENDED\_CALL](group__bt__tbs.md#ga4bc073b85c6eca1f0a4b0757e1050dde)   0x02 |
|  | The remote party ended the call. |
| #define | [BT\_TBS\_REASON\_SERVER\_ENDED\_CALL](group__bt__tbs.md#gaa4f89b5fa61dcc4ee7e4fb6ae0e12384)   0x03 |
|  | The call ended from the server. |
| #define | [BT\_TBS\_REASON\_LINE\_BUSY](group__bt__tbs.md#ga3105e7b0b91b71eb55c1ea5c3bfd6df3)   0x04 |
|  | The line was busy. |
| #define | [BT\_TBS\_REASON\_NETWORK\_CONGESTED](group__bt__tbs.md#gae195db56d2cd949a29d261c5473eea89)   0x05 |
|  | Network congestion. |
| #define | [BT\_TBS\_REASON\_CLIENT\_TERMINATED](group__bt__tbs.md#ga614adc266444030ac83dc6f4d2e89563)   0x06 |
|  | The client terminated the call. |
| #define | [BT\_TBS\_REASON\_NO\_SERVICE](group__bt__tbs.md#ga137b813cf902c8209a624c6ae8d4a93b)   0x07 |
|  | No service. |
| #define | [BT\_TBS\_REASON\_NO\_ANSWER](group__bt__tbs.md#ga893d3c79ca62c5e5487d7ca7cd403ce2)   0x08 |
|  | No answer. |
| #define | [BT\_TBS\_REASON\_UNSPECIFIED](group__bt__tbs.md#gaa4dab0b5c08dcf092a125986519a7d55)   0x09 |
|  | Unspecified. |
| Control point error codes | |
| #define | [BT\_TBS\_RESULT\_CODE\_SUCCESS](group__bt__tbs.md#gaa92fdb19227ee0b268f2395f3f6a5f63)   0x00 |
|  | The opcode write was successful. |
| #define | [BT\_TBS\_RESULT\_CODE\_OPCODE\_NOT\_SUPPORTED](group__bt__tbs.md#gafac3c970b36f37c815c4370dfef89f09)   0x01 |
|  | An invalid opcode was used for the Call Control Point write. |
| #define | [BT\_TBS\_RESULT\_CODE\_OPERATION\_NOT\_POSSIBLE](group__bt__tbs.md#gae83a73a5a0474a62dfbcb5ced6eb3f78)   0x02 |
|  | The requested operation cannot be completed. |
| #define | [BT\_TBS\_RESULT\_CODE\_INVALID\_CALL\_INDEX](group__bt__tbs.md#gadc371a3a898b3ecac56d8778109f315d)   0x03 |
|  | The Call Index used for the Call Control Point write is invalid. |
| #define | [BT\_TBS\_RESULT\_CODE\_STATE\_MISMATCH](group__bt__tbs.md#ga3fa49179525369502018912115c1ccce)   0x04 |
|  | The opcode written to the Call Control Point was received when the current Call State for the Call Index was not in the expected state. |
| #define | [BT\_TBS\_RESULT\_CODE\_OUT\_OF\_RESOURCES](group__bt__tbs.md#ga148585f5cfe8b1cd7f8db404dac91cdd)   0x05 |
|  | Lack of internal resources to complete the requested action. |
| #define | [BT\_TBS\_RESULT\_CODE\_INVALID\_URI](group__bt__tbs.md#gaa60f75b90f461246b2f470930a60efc2)   0x06 |
|  | The Outgoing URI is incorrect or invalid when an Originate opcode is sent. |
| Optional feature bits | |
| Optional features that can be supported.  See [bt\_tbs\_client\_read\_optional\_opcodes()](group__bt__tbs.md#gaf504e1a11352d77a36aa087b587e4ba8 "Read the supported opcode of a TBS instance.") on how to read these from a remote device | |
| #define | [BT\_TBS\_FEATURE\_HOLD](group__bt__tbs.md#gabb6c3b57d7c48620b0f019992c55e585)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Local Hold and Local Retrieve Call Control Point Opcodes supported. |
| #define | [BT\_TBS\_FEATURE\_JOIN](group__bt__tbs.md#ga962ce8d27abbdc48adbc01b2c68cb042)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Join Call Control Point Opcode supported. |
| #define | [BT\_TBS\_FEATURE\_ALL](group__bt__tbs.md#gadd72fdfd22c6a3abca8a270aae6a689a)   ([BT\_TBS\_FEATURE\_HOLD](group__bt__tbs.md#gabb6c3b57d7c48620b0f019992c55e585) | [BT\_TBS\_FEATURE\_JOIN](group__bt__tbs.md#ga962ce8d27abbdc48adbc01b2c68cb042)) |
|  | All Control Point Opcodes supported. |
| Signal strength value limits | |
| #define | [BT\_TBS\_SIGNAL\_STRENGTH\_NO\_SERVICE](group__bt__tbs.md#ga310c1cdffee350fe5235b3ad929ac715)   0 |
|  | No service. |
| #define | [BT\_TBS\_SIGNAL\_STRENGTH\_MAX](group__bt__tbs.md#gae619d9096b41690ba77ee3e7bd838be3)   100 |
|  | Maximum signal strength. |
| #define | [BT\_TBS\_SIGNAL\_STRENGTH\_UNKNOWN](group__bt__tbs.md#gab8a433da27a61cf1c7be2fc7b006e298)   255 |
|  | Signal strength is unknown. |
| Bearer Technology | |
| #define | [BT\_TBS\_TECHNOLOGY\_3G](group__bt__tbs.md#gaf125f3486c88517c9e1e218c6ce492e4)   0x01 |
|  | 3G |
| #define | [BT\_TBS\_TECHNOLOGY\_4G](group__bt__tbs.md#ga967b2b97a2e862f5ae235fc9b728b15c)   0x02 |
|  | 4G |
| #define | [BT\_TBS\_TECHNOLOGY\_LTE](group__bt__tbs.md#ga6962ce833da01b3a584528b2ce361447)   0x03 |
|  | Long-term evolution (LTE). |
| #define | [BT\_TBS\_TECHNOLOGY\_WIFI](group__bt__tbs.md#ga02af096f1153eed9623f7a7324956e86)   0x04 |
|  | Wifi. |
| #define | [BT\_TBS\_TECHNOLOGY\_5G](group__bt__tbs.md#ga28c1928de97f2b7f0e7e36bfe1a5bdde)   0x05 |
|  | 5G |
| #define | [BT\_TBS\_TECHNOLOGY\_GSM](group__bt__tbs.md#gad530e2c9b8b616a9674012ecc801421f)   0x06 |
|  | Global System for Mobile Communications (GSM). |
| #define | [BT\_TBS\_TECHNOLOGY\_CDMA](group__bt__tbs.md#gaeb6d5ed9dcdba0849f81413ef08570bc)   0x07 |
|  | Code-Division Multiple Access (CDMA). |
| #define | [BT\_TBS\_TECHNOLOGY\_2G](group__bt__tbs.md#gafcb1e805e56eb93f6a19b63f2cbf524c)   0x08 |
|  | 2G |
| #define | [BT\_TBS\_TECHNOLOGY\_WCDMA](group__bt__tbs.md#ga3b828481ce60034abbdab8aa4b1ae972)   0x09 |
|  | Wideband Code-Division Multiple Access (WCDMA). |
| Call status flags bitfield | |
| #define | [BT\_TBS\_STATUS\_FLAG\_INBAND\_RINGTONE](group__bt__tbs.md#gadc590b9f5813e190fa14644412aee25c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Inband ringtone enabled. |
| #define | [BT\_TBS\_STATUS\_FLAG\_SILENT\_MOD](group__bt__tbs.md#ga53dfa36830f8c562711d9c6f9111929e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Server is in silent mod. |
| Call flags bitfield | |
| #define | [BT\_TBS\_CALL\_FLAG\_OUTGOING](group__bt__tbs.md#ga74344c01327304f1d2da050ddc589735)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | If set, call is outgoing else incoming. |
| #define | [BT\_TBS\_CALL\_FLAG\_WITHHELD](group__bt__tbs.md#ga25ff3c36aaabc5e37b08acc62ac21be6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | If set call is withheld, else not withheld. |
| #define | [BT\_TBS\_CALL\_FLAG\_WITHHELD\_BY\_NETWORK](group__bt__tbs.md#ga466c1c3c50e82fee9e5c8323e89be414)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | If set call is withheld by network, else provided by network. |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_tbs\_originate\_call\_cb](group__bt__tbs.md#ga60e9e143f247bb7e668293f0233ce300)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index, const char \*uri) |
|  | Callback function for client originating a call. |
| typedef void(\* | [bt\_tbs\_terminate\_call\_cb](group__bt__tbs.md#ga69e93b48b2a48e8a6552882660b791cc)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Callback function for client terminating a call. |
| typedef void(\* | [bt\_tbs\_join\_calls\_cb](group__bt__tbs.md#gaa45b3f4837165d722c2df6f202a39058)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index\_count, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes) |
|  | Callback function for client joining calls. |
| typedef void(\* | [bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Callback function for client request call state change. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_tbs\_authorize\_cb](group__bt__tbs.md#ga1cc9e7140531b07bf6a8dedbc17f24c0)) (struct bt\_conn \*conn) |
|  | Callback function for authorizing a client. |
| typedef void(\* | [bt\_tbs\_client\_discover\_cb](group__bt__tbs.md#ga9cac11cc696be9fb387f2f7685e0d8a7)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tbs\_count, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) gtbs\_found) |
|  | Callback function for ccp\_discover. |
| typedef void(\* | [bt\_tbs\_client\_write\_value\_cb](group__bt__tbs.md#gaf77231168e4444da7aef203cc9eaca95)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Callback function for writing values to peer device. |
| typedef void(\* | [bt\_tbs\_client\_cp\_cb](group__bt__tbs.md#ga40b8b3d1b318a1b5c5524877bbc2f90f)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Callback function for the CCP call control functions. |
| typedef void(\* | [bt\_tbs\_client\_read\_string\_cb](group__bt__tbs.md#ga4d7632de7c2006e478880950076908a9)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, const char \*value) |
|  | Callback function for functions that read a string value. |
| typedef void(\* | [bt\_tbs\_client\_read\_value\_cb](group__bt__tbs.md#ga600051910ed538a2da823554df23dd20)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Callback function for functions that read an integer value. |
| typedef void(\* | [bt\_tbs\_client\_termination\_reason\_cb](group__bt__tbs.md#gab881b3caaaa4425e52afd84e53adee78)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Callback function for ccp\_read\_termination\_reason. |
| typedef void(\* | [bt\_tbs\_client\_current\_calls\_cb](group__bt__tbs.md#ga7b31e1c30fa96081a3ef38e1a481b64f)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_count, const struct [bt\_tbs\_client\_call](structbt__tbs__client__call.md) \*calls) |
|  | Callback function for ccp\_read\_current\_calls. |
| typedef void(\* | [bt\_tbs\_client\_call\_states\_cb](group__bt__tbs.md#ga262ca74b7ae2f0c52657066549fa4f92)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_count, const struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) \*call\_states) |
|  | Callback function for ccp\_read\_call\_state. |

| Functions | |
| --- | --- |
| int | [bt\_tbs\_accept](group__bt__tbs.md#ga1b942bcf8287641f9cd53824b4d6e77b) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Accept an alerting call. |
| int | [bt\_tbs\_hold](group__bt__tbs.md#gab72044a1f5466114b5efb88dfcd2f097) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Hold a call. |
| int | [bt\_tbs\_retrieve](group__bt__tbs.md#gad0b45af09b82d6cd66a8481c0e67e04e) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Retrieve a call. |
| int | [bt\_tbs\_terminate](group__bt__tbs.md#ga82553640882ac74f9af84bfe09ff47ee) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Terminate a call. |
| int | [bt\_tbs\_originate](group__bt__tbs.md#gadeae51d7cecd80abcdcde1195bb1dfba) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, char \*uri, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_index) |
|  | Originate a call. |
| int | [bt\_tbs\_join](group__bt__tbs.md#ga23226d41e3b98a53ec9a9c2fa346c9ac) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index\_cnt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes) |
|  | Join calls. |
| int | [bt\_tbs\_remote\_answer](group__bt__tbs.md#ga868b83450f7425e8a0c8cfb7c1de45d8) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Notify the server that the remote party answered the call. |
| int | [bt\_tbs\_remote\_hold](group__bt__tbs.md#ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Notify the server that the remote party held the call. |
| int | [bt\_tbs\_remote\_retrieve](group__bt__tbs.md#ga09a3e64040819b6b8b694b94d2f62ca0) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Notify the server that the remote party retrieved the call. |
| int | [bt\_tbs\_remote\_terminate](group__bt__tbs.md#ga52afc7b8a22b071dbac10057579f319c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Notify the server that the remote party terminated the call. |
| int | [bt\_tbs\_remote\_incoming](group__bt__tbs.md#ga47939f557e4d6503af9b7b85aff9d60f) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*to, const char \*from, const char \*friendly\_name) |
|  | Notify the server of an incoming call. |
| int | [bt\_tbs\_set\_bearer\_provider\_name](group__bt__tbs.md#ga5118db6b23b387956e75eda8aecd53d5) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*name) |
|  | Set a new bearer provider. |
| int | [bt\_tbs\_set\_bearer\_technology](group__bt__tbs.md#gaf4c576b8aa599f1bd9598964bc1b779f) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_technology) |
|  | Set a new bearer technology. |
| int | [bt\_tbs\_set\_signal\_strength](group__bt__tbs.md#gac316adedf7fda441ee55feb9d24d1a94) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_signal\_strength) |
|  | Update the signal strength reported by the server. |
| int | [bt\_tbs\_set\_status\_flags](group__bt__tbs.md#ga838e51a85f9833e0822090cd3df09e00) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) status\_flags) |
|  | Sets the feature and status value. |
| int | [bt\_tbs\_set\_uri\_scheme\_list](group__bt__tbs.md#ga90b3fb1d757fbb134649b0d7f9047123) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*\*uri\_list, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uri\_count) |
|  | Sets the URI scheme list of a bearer. |
| void | [bt\_tbs\_register\_cb](group__bt__tbs.md#ga76f120dba549225a6f2c2c22be08edfc) (struct [bt\_tbs\_cb](structbt__tbs__cb.md) \*cbs) |
|  | Register the callbacks for TBS. |
| int | [bt\_tbs\_register\_bearer](group__bt__tbs.md#ga970c970bedd6e94aa4c92479183554e9) (const struct [bt\_tbs\_register\_param](structbt__tbs__register__param.md) \*param) |
|  | Register a Telephone Bearer. |
| int | [bt\_tbs\_unregister\_bearer](group__bt__tbs.md#ga8edd4d31478ed9e0aedbd1a34bdfca96) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index) |
|  | Unregister a Telephone Bearer. |
| void | [bt\_tbs\_dbg\_print\_calls](group__bt__tbs.md#ga62f5008cbfba158fe399cfaf683d1d2e) (void) |
|  | Prints all calls of all services to the debug log. |
| int | [bt\_tbs\_client\_discover](group__bt__tbs.md#gac59f3dec092a14bdf234039e3dcd12eb) (struct bt\_conn \*conn) |
|  | Discover TBS for a connection. |
| int | [bt\_tbs\_client\_set\_outgoing\_uri](group__bt__tbs.md#ga3a71c51d464aa19fbfbd2d60fc4901bc) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, const char \*uri) |
|  | Set the outgoing URI for a TBS instance on the peer device. |
| int | [bt\_tbs\_client\_set\_signal\_strength\_interval](group__bt__tbs.md#gaa1dcb9908057d75a54fa447639826f3c) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval) |
|  | Set the signal strength reporting interval for a TBS instance. |
| int | [bt\_tbs\_client\_originate\_call](group__bt__tbs.md#ga0aac704008ffc92ce6609d3ffffc4523) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, const char \*uri) |
|  | Request to originate a call. |
| int | [bt\_tbs\_client\_terminate\_call](group__bt__tbs.md#ga25b803bb5cae2e1a8b0398bc48137d80) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Request to terminate a call. |
| int | [bt\_tbs\_client\_hold\_call](group__bt__tbs.md#ga23e825de6af71d4e456b63c3a621fb61) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Request to hold a call. |
| int | [bt\_tbs\_client\_accept\_call](group__bt__tbs.md#ga625fc73885c2bfd63f0f4b2d7f72eaef) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Accept an incoming call. |
| int | [bt\_tbs\_client\_retrieve\_call](group__bt__tbs.md#gabbe194a63da0b95dc1dca0337560a585) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Retrieve call from (local) hold. |
| int | [bt\_tbs\_client\_join\_calls](group__bt__tbs.md#gaae1925deb0b5865af601aa8278ffb10a) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count) |
|  | Join multiple calls. |
| int | [bt\_tbs\_client\_read\_bearer\_provider\_name](group__bt__tbs.md#ga2053a9eb7cf28f66febd365f0b682be0) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the bearer provider name of a TBS instance. |
| int | [bt\_tbs\_client\_read\_bearer\_uci](group__bt__tbs.md#gaba92039d3b44da9163a22400951fafa7) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the UCI of a TBS instance. |
| int | [bt\_tbs\_client\_read\_technology](group__bt__tbs.md#ga7684dbcb78e407f7002d44fbdb805e5d) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the technology of a TBS instance. |
| int | [bt\_tbs\_client\_read\_uri\_list](group__bt__tbs.md#gad19db25591c7ae5bd0b4c2bbaefc9bed) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the URI schemes list of a TBS instance. |
| int | [bt\_tbs\_client\_read\_signal\_strength](group__bt__tbs.md#gaabe97df55817b8e36c79de4bf30fc83f) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the current signal strength of a TBS instance. |
| int | [bt\_tbs\_client\_read\_signal\_interval](group__bt__tbs.md#ga38046c5c715d451b21a3076742268010) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the signal strength reporting interval of a TBS instance. |
| int | [bt\_tbs\_client\_read\_current\_calls](group__bt__tbs.md#ga895c7f54300e5452fb8d0c9d4b3306ae) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the list of current calls of a TBS instance. |
| int | [bt\_tbs\_client\_read\_ccid](group__bt__tbs.md#gac070ec0590df5820b7721d579ceeeb15) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the content ID of a TBS instance. |
| int | [bt\_tbs\_client\_read\_call\_uri](group__bt__tbs.md#ga4238a37b80b7d7ff611fe9b02b7cf54d) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the call target URI of a TBS instance. |
| int | [bt\_tbs\_client\_read\_status\_flags](group__bt__tbs.md#ga9fe91df1a31ce59401347fc0eac2b701) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the feature and status value of a TBS instance. |
| int | [bt\_tbs\_client\_read\_call\_state](group__bt__tbs.md#gafeaaaefb9d4eb773dd0cbdfebe26e0b7) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the states of the current calls of a TBS instance. |
| int | [bt\_tbs\_client\_read\_remote\_uri](group__bt__tbs.md#gab04f8355c32fce501bd757b75ee9d38a) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the remote URI of a TBS instance. |
| int | [bt\_tbs\_client\_read\_friendly\_name](group__bt__tbs.md#ga99549dd6244580e157006fb17772fd8f) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the friendly name of a call for a TBS instance. |
| int | [bt\_tbs\_client\_read\_optional\_opcodes](group__bt__tbs.md#gaf504e1a11352d77a36aa087b587e4ba8) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the supported opcode of a TBS instance. |
| int | [bt\_tbs\_client\_register\_cb](group__bt__tbs.md#gabe2251d4ea88306793dc68ae683886bb) (struct [bt\_tbs\_client\_cb](structbt__tbs__client__cb.md) \*cbs) |
|  | Register the callbacks for CCP. |
| struct bt\_tbs\_instance \* | [bt\_tbs\_client\_get\_by\_ccid](group__bt__tbs.md#gaadae501fa6f7771bb9661af829805a5f) (const struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid) |
|  | Look up Telephone Bearer Service instance by CCID. |

## Detailed Description

Public APIs for Bluetooth Telephone Bearer Service.

Copyright (c) 2020 Bose Corporation Copyright (c) 2021 Nordic Semiconductor ASA

SPDX-License-Identifier: Apache-2.0

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [tbs.h](tbs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
