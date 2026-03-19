---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__tbs.html
original_path: doxygen/html/group__bt__tbs.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Telephone Bearer Service (TBS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Telephone Bearer Service (TBS).
[More...](#details)

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
| #define | [BT\_TBS\_GTBS\_INDEX](#ga25aa807f2e3a01d030edf4f064a4fbfd)   0xFF |
|  | The GTBS index denotes whenever a callback is from a Generic Telephone Bearer Service (GTBS) instance, or whenever the client should perform on action on the GTBS instance of the server, rather than any of the specific Telephone Bearer Service instances. |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_tbs\_originate\_call\_cb](#ga60e9e143f247bb7e668293f0233ce300)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index, const char \*uri) |
|  | Callback function for client originating a call. |
| typedef void(\* | [bt\_tbs\_terminate\_call\_cb](#ga69e93b48b2a48e8a6552882660b791cc)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Callback function for client terminating a call. |
| typedef void(\* | [bt\_tbs\_join\_calls\_cb](#gaa45b3f4837165d722c2df6f202a39058)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index\_count, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes) |
|  | Callback function for client joining calls. |
| typedef void(\* | [bt\_tbs\_call\_change\_cb](#ga2fa85f3cd96f25f6bb4f449fc9210fa1)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Callback function for client request call state change. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_tbs\_authorize\_cb](#ga1cc9e7140531b07bf6a8dedbc17f24c0)) (struct bt\_conn \*conn) |
|  | Callback function for authorizing a client. |
| typedef void(\* | [bt\_tbs\_client\_discover\_cb](#ga9cac11cc696be9fb387f2f7685e0d8a7)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tbs\_count, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) gtbs\_found) |
|  | Callback function for ccp\_discover. |
| typedef void(\* | [bt\_tbs\_client\_write\_value\_cb](#gaf77231168e4444da7aef203cc9eaca95)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Callback function for writing values to peer device. |
| typedef void(\* | [bt\_tbs\_client\_cp\_cb](#ga40b8b3d1b318a1b5c5524877bbc2f90f)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Callback function for the CCP call control functions. |
| typedef void(\* | [bt\_tbs\_client\_read\_string\_cb](#ga4d7632de7c2006e478880950076908a9)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, const char \*value) |
|  | Callback function for functions that read a string value. |
| typedef void(\* | [bt\_tbs\_client\_read\_value\_cb](#ga600051910ed538a2da823554df23dd20)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Callback function for functions that read an integer value. |
| typedef void(\* | [bt\_tbs\_client\_termination\_reason\_cb](#gab881b3caaaa4425e52afd84e53adee78)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Callback function for ccp\_read\_termination\_reason. |
| typedef void(\* | [bt\_tbs\_client\_current\_calls\_cb](#ga7b31e1c30fa96081a3ef38e1a481b64f)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_count, const struct [bt\_tbs\_client\_call](structbt__tbs__client__call.md) \*calls) |
|  | Callback function for ccp\_read\_current\_calls. |
| typedef void(\* | [bt\_tbs\_client\_call\_states\_cb](#ga262ca74b7ae2f0c52657066549fa4f92)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_count, const struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) \*call\_states) |
|  | Callback function for ccp\_read\_call\_state. |

| Functions | |
| --- | --- |
| int | [bt\_tbs\_accept](#ga1b942bcf8287641f9cd53824b4d6e77b) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Accept an alerting call. |
| int | [bt\_tbs\_hold](#gab72044a1f5466114b5efb88dfcd2f097) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Hold a call. |
| int | [bt\_tbs\_retrieve](#gad0b45af09b82d6cd66a8481c0e67e04e) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Retrieve a call. |
| int | [bt\_tbs\_terminate](#ga82553640882ac74f9af84bfe09ff47ee) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Terminate a call. |
| int | [bt\_tbs\_originate](#gadeae51d7cecd80abcdcde1195bb1dfba) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, char \*uri, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_index) |
|  | Originate a call. |
| int | [bt\_tbs\_join](#ga23226d41e3b98a53ec9a9c2fa346c9ac) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index\_cnt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes) |
|  | Join calls. |
| int | [bt\_tbs\_remote\_answer](#ga868b83450f7425e8a0c8cfb7c1de45d8) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Notify the server that the remote party answered the call. |
| int | [bt\_tbs\_remote\_hold](#ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Notify the server that the remote party held the call. |
| int | [bt\_tbs\_remote\_retrieve](#ga09a3e64040819b6b8b694b94d2f62ca0) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Notify the server that the remote party retrieved the call. |
| int | [bt\_tbs\_remote\_terminate](#ga52afc7b8a22b071dbac10057579f319c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Notify the server that the remote party terminated the call. |
| int | [bt\_tbs\_remote\_incoming](#ga47939f557e4d6503af9b7b85aff9d60f) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*to, const char \*from, const char \*friendly\_name) |
|  | Notify the server of an incoming call. |
| int | [bt\_tbs\_set\_bearer\_provider\_name](#ga5118db6b23b387956e75eda8aecd53d5) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*name) |
|  | Set a new bearer provider. |
| int | [bt\_tbs\_set\_bearer\_technology](#gaf4c576b8aa599f1bd9598964bc1b779f) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_technology) |
|  | Set a new bearer technology. |
| int | [bt\_tbs\_set\_signal\_strength](#gac316adedf7fda441ee55feb9d24d1a94) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_signal\_strength) |
|  | Update the signal strength reported by the server. |
| int | [bt\_tbs\_set\_status\_flags](#ga838e51a85f9833e0822090cd3df09e00) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) status\_flags) |
|  | Sets the feature and status value. |
| int | [bt\_tbs\_set\_uri\_scheme\_list](#ga90b3fb1d757fbb134649b0d7f9047123) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index, const char \*\*uri\_list, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uri\_count) |
|  | Sets the URI scheme list of a bearer. |
| void | [bt\_tbs\_register\_cb](#ga76f120dba549225a6f2c2c22be08edfc) (struct [bt\_tbs\_cb](structbt__tbs__cb.md) \*cbs) |
|  | Register the callbacks for TBS. |
| int | [bt\_tbs\_register\_bearer](#ga970c970bedd6e94aa4c92479183554e9) (const struct [bt\_tbs\_register\_param](structbt__tbs__register__param.md) \*param) |
|  | Register a Telephone Bearer. |
| int | [bt\_tbs\_unregister\_bearer](#ga8edd4d31478ed9e0aedbd1a34bdfca96) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bearer\_index) |
|  | Unregister a Telephone Bearer. |
| void | [bt\_tbs\_dbg\_print\_calls](#ga62f5008cbfba158fe399cfaf683d1d2e) (void) |
|  | Prints all calls of all services to the debug log. |
| int | [bt\_tbs\_client\_discover](#gac59f3dec092a14bdf234039e3dcd12eb) (struct bt\_conn \*conn) |
|  | Discover TBS for a connection. |
| int | [bt\_tbs\_client\_set\_outgoing\_uri](#ga3a71c51d464aa19fbfbd2d60fc4901bc) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, const char \*uri) |
|  | Set the outgoing URI for a TBS instance on the peer device. |
| int | [bt\_tbs\_client\_set\_signal\_strength\_interval](#gaa1dcb9908057d75a54fa447639826f3c) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval) |
|  | Set the signal strength reporting interval for a TBS instance. |
| int | [bt\_tbs\_client\_originate\_call](#ga0aac704008ffc92ce6609d3ffffc4523) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, const char \*uri) |
|  | Request to originate a call. |
| int | [bt\_tbs\_client\_terminate\_call](#ga25b803bb5cae2e1a8b0398bc48137d80) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Request to terminate a call. |
| int | [bt\_tbs\_client\_hold\_call](#ga23e825de6af71d4e456b63c3a621fb61) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Request to hold a call. |
| int | [bt\_tbs\_client\_accept\_call](#ga625fc73885c2bfd63f0f4b2d7f72eaef) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Accept an incoming call. |
| int | [bt\_tbs\_client\_retrieve\_call](#gabbe194a63da0b95dc1dca0337560a585) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
|  | Retrieve call from (local) hold. |
| int | [bt\_tbs\_client\_join\_calls](#gaae1925deb0b5865af601aa8278ffb10a) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count) |
|  | Join multiple calls. |
| int | [bt\_tbs\_client\_read\_bearer\_provider\_name](#ga2053a9eb7cf28f66febd365f0b682be0) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the bearer provider name of a TBS instance. |
| int | [bt\_tbs\_client\_read\_bearer\_uci](#gaba92039d3b44da9163a22400951fafa7) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the UCI of a TBS instance. |
| int | [bt\_tbs\_client\_read\_technology](#ga7684dbcb78e407f7002d44fbdb805e5d) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the technology of a TBS instance. |
| int | [bt\_tbs\_client\_read\_uri\_list](#gad19db25591c7ae5bd0b4c2bbaefc9bed) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the URI schemes list of a TBS instance. |
| int | [bt\_tbs\_client\_read\_signal\_strength](#gaabe97df55817b8e36c79de4bf30fc83f) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the current signal strength of a TBS instance. |
| int | [bt\_tbs\_client\_read\_signal\_interval](#ga38046c5c715d451b21a3076742268010) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the signal strength reporting interval of a TBS instance. |
| int | [bt\_tbs\_client\_read\_current\_calls](#ga895c7f54300e5452fb8d0c9d4b3306ae) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the list of current calls of a TBS instance. |
| int | [bt\_tbs\_client\_read\_ccid](#gac070ec0590df5820b7721d579ceeeb15) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the content ID of a TBS instance. |
| int | [bt\_tbs\_client\_read\_call\_uri](#ga4238a37b80b7d7ff611fe9b02b7cf54d) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the call target URI of a TBS instance. |
| int | [bt\_tbs\_client\_read\_status\_flags](#ga9fe91df1a31ce59401347fc0eac2b701) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the feature and status value of a TBS instance. |
| int | [bt\_tbs\_client\_read\_call\_state](#gafeaaaefb9d4eb773dd0cbdfebe26e0b7) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the states of the current calls of a TBS instance. |
| int | [bt\_tbs\_client\_read\_remote\_uri](#gab04f8355c32fce501bd757b75ee9d38a) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the remote URI of a TBS instance. |
| int | [bt\_tbs\_client\_read\_friendly\_name](#ga99549dd6244580e157006fb17772fd8f) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the friendly name of a call for a TBS instance. |
| int | [bt\_tbs\_client\_read\_optional\_opcodes](#gaf504e1a11352d77a36aa087b587e4ba8) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
|  | Read the supported opcode of a TBS instance. |
| int | [bt\_tbs\_client\_register\_cb](#gabe2251d4ea88306793dc68ae683886bb) (struct [bt\_tbs\_client\_cb](structbt__tbs__client__cb.md) \*cbs) |
|  | Register the callbacks for CCP. |
| struct bt\_tbs\_instance \* | [bt\_tbs\_client\_get\_by\_ccid](#gaadae501fa6f7771bb9661af829805a5f) (const struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid) |
|  | Look up Telephone Bearer Service instance by CCID. |

| Call States | |
| --- | --- |
| #define | [BT\_TBS\_CALL\_STATE\_INCOMING](#ga829309945831c0e8ac36c3dd79ae26f3)   0x00 |
|  | A remote party is calling (incoming call). |
| #define | [BT\_TBS\_CALL\_STATE\_DIALING](#ga482f9627308cad1e56a4a5a5906c2308)   0x01 |
|  | The process to call the remote party has started on the server, but the remote party is not being alerted (outgoing call). |
| #define | [BT\_TBS\_CALL\_STATE\_ALERTING](#gada61fd749f2119452429dd712d283dad)   0x02 |
|  | A remote party is being alerted (outgoing call). |
| #define | [BT\_TBS\_CALL\_STATE\_ACTIVE](#ga3100ab7a7db823d86198847ec0df4adc)   0x03 |
|  | The call is in an active conversation. |
| #define | [BT\_TBS\_CALL\_STATE\_LOCALLY\_HELD](#gac900fe331fe5b81d7ed0b21796d3e16c)   0x04 |
|  | The call is connected but held locally. |
| #define | [BT\_TBS\_CALL\_STATE\_REMOTELY\_HELD](#ga76acd3539931a32361fd0deb3bbe8243)   0x05 |
|  | The call is connected but held remotely. |
| #define | [BT\_TBS\_CALL\_STATE\_LOCALLY\_AND\_REMOTELY\_HELD](#ga0d28984faadc6904f72068df6ab6c97d)   0x06 |
|  | The call is connected but held both locally and remotely. |

| Terminate Reason | |
| --- | --- |
| #define | [BT\_TBS\_REASON\_BAD\_REMOTE\_URI](#gaf7f2abd7e794806ab6b119bee47db6c6)   0x00 |
|  | The URI value used to originate a call was formed improperly. |
| #define | [BT\_TBS\_REASON\_CALL\_FAILED](#gacd5a09f5786e01662e29d49aa5307046)   0x01 |
|  | The call failed. |
| #define | [BT\_TBS\_REASON\_REMOTE\_ENDED\_CALL](#ga4bc073b85c6eca1f0a4b0757e1050dde)   0x02 |
|  | The remote party ended the call. |
| #define | [BT\_TBS\_REASON\_SERVER\_ENDED\_CALL](#gaa4f89b5fa61dcc4ee7e4fb6ae0e12384)   0x03 |
|  | The call ended from the server. |
| #define | [BT\_TBS\_REASON\_LINE\_BUSY](#ga3105e7b0b91b71eb55c1ea5c3bfd6df3)   0x04 |
|  | The line was busy. |
| #define | [BT\_TBS\_REASON\_NETWORK\_CONGESTED](#gae195db56d2cd949a29d261c5473eea89)   0x05 |
|  | Network congestion. |
| #define | [BT\_TBS\_REASON\_CLIENT\_TERMINATED](#ga614adc266444030ac83dc6f4d2e89563)   0x06 |
|  | The client terminated the call. |
| #define | [BT\_TBS\_REASON\_NO\_SERVICE](#ga137b813cf902c8209a624c6ae8d4a93b)   0x07 |
|  | No service. |
| #define | [BT\_TBS\_REASON\_NO\_ANSWER](#ga893d3c79ca62c5e5487d7ca7cd403ce2)   0x08 |
|  | No answer. |
| #define | [BT\_TBS\_REASON\_UNSPECIFIED](#gaa4dab0b5c08dcf092a125986519a7d55)   0x09 |
|  | Unspecified. |

| Control point error codes | |
| --- | --- |
| #define | [BT\_TBS\_RESULT\_CODE\_SUCCESS](#gaa92fdb19227ee0b268f2395f3f6a5f63)   0x00 |
|  | The opcode write was successful. |
| #define | [BT\_TBS\_RESULT\_CODE\_OPCODE\_NOT\_SUPPORTED](#gafac3c970b36f37c815c4370dfef89f09)   0x01 |
|  | An invalid opcode was used for the Call Control Point write. |
| #define | [BT\_TBS\_RESULT\_CODE\_OPERATION\_NOT\_POSSIBLE](#gae83a73a5a0474a62dfbcb5ced6eb3f78)   0x02 |
|  | The requested operation cannot be completed. |
| #define | [BT\_TBS\_RESULT\_CODE\_INVALID\_CALL\_INDEX](#gadc371a3a898b3ecac56d8778109f315d)   0x03 |
|  | The Call Index used for the Call Control Point write is invalid. |
| #define | [BT\_TBS\_RESULT\_CODE\_STATE\_MISMATCH](#ga3fa49179525369502018912115c1ccce)   0x04 |
|  | The opcode written to the Call Control Point was received when the current Call State for the Call Index was not in the expected state. |
| #define | [BT\_TBS\_RESULT\_CODE\_OUT\_OF\_RESOURCES](#ga148585f5cfe8b1cd7f8db404dac91cdd)   0x05 |
|  | Lack of internal resources to complete the requested action. |
| #define | [BT\_TBS\_RESULT\_CODE\_INVALID\_URI](#gaa60f75b90f461246b2f470930a60efc2)   0x06 |
|  | The Outgoing URI is incorrect or invalid when an Originate opcode is sent. |

| Optional feature bits | |
| --- | --- |
| Optional features that can be supported.  See [bt\_tbs\_client\_read\_optional\_opcodes()](#gaf504e1a11352d77a36aa087b587e4ba8) on how to read these from a remote device | |
| #define | [BT\_TBS\_FEATURE\_HOLD](#gabb6c3b57d7c48620b0f019992c55e585)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Local Hold and Local Retrieve Call Control Point Opcodes supported. |
| #define | [BT\_TBS\_FEATURE\_JOIN](#ga962ce8d27abbdc48adbc01b2c68cb042)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Join Call Control Point Opcode supported. |
| #define | [BT\_TBS\_FEATURE\_ALL](#gadd72fdfd22c6a3abca8a270aae6a689a)   ([BT\_TBS\_FEATURE\_HOLD](#gabb6c3b57d7c48620b0f019992c55e585) | [BT\_TBS\_FEATURE\_JOIN](#ga962ce8d27abbdc48adbc01b2c68cb042)) |
|  | All Control Point Opcodes supported. |

| Signal strength value limits | |
| --- | --- |
| #define | [BT\_TBS\_SIGNAL\_STRENGTH\_NO\_SERVICE](#ga310c1cdffee350fe5235b3ad929ac715)   0 |
|  | No service. |
| #define | [BT\_TBS\_SIGNAL\_STRENGTH\_MAX](#gae619d9096b41690ba77ee3e7bd838be3)   100 |
|  | Maximum signal strength. |
| #define | [BT\_TBS\_SIGNAL\_STRENGTH\_UNKNOWN](#gab8a433da27a61cf1c7be2fc7b006e298)   255 |
|  | Signal strength is unknown. |

| Bearer Technology | |
| --- | --- |
| #define | [BT\_TBS\_TECHNOLOGY\_3G](#gaf125f3486c88517c9e1e218c6ce492e4)   0x01 |
|  | 3G |
| #define | [BT\_TBS\_TECHNOLOGY\_4G](#ga967b2b97a2e862f5ae235fc9b728b15c)   0x02 |
|  | 4G |
| #define | [BT\_TBS\_TECHNOLOGY\_LTE](#ga6962ce833da01b3a584528b2ce361447)   0x03 |
|  | Long-term evolution (LTE). |
| #define | [BT\_TBS\_TECHNOLOGY\_WIFI](#ga02af096f1153eed9623f7a7324956e86)   0x04 |
|  | Wifi. |
| #define | [BT\_TBS\_TECHNOLOGY\_5G](#ga28c1928de97f2b7f0e7e36bfe1a5bdde)   0x05 |
|  | 5G |
| #define | [BT\_TBS\_TECHNOLOGY\_GSM](#gad530e2c9b8b616a9674012ecc801421f)   0x06 |
|  | Global System for Mobile Communications (GSM). |
| #define | [BT\_TBS\_TECHNOLOGY\_CDMA](#gaeb6d5ed9dcdba0849f81413ef08570bc)   0x07 |
|  | Code-Division Multiple Access (CDMA). |
| #define | [BT\_TBS\_TECHNOLOGY\_2G](#gafcb1e805e56eb93f6a19b63f2cbf524c)   0x08 |
|  | 2G |
| #define | [BT\_TBS\_TECHNOLOGY\_WCDMA](#ga3b828481ce60034abbdab8aa4b1ae972)   0x09 |
|  | Wideband Code-Division Multiple Access (WCDMA). |

| Call status flags bitfield | |
| --- | --- |
| #define | [BT\_TBS\_STATUS\_FLAG\_INBAND\_RINGTONE](#gadc590b9f5813e190fa14644412aee25c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Inband ringtone enabled. |
| #define | [BT\_TBS\_STATUS\_FLAG\_SILENT\_MOD](#ga53dfa36830f8c562711d9c6f9111929e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Server is in silent mod. |

| Call flags bitfield | |
| --- | --- |
| #define | [BT\_TBS\_CALL\_FLAG\_OUTGOING](#ga74344c01327304f1d2da050ddc589735)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | If set, call is outgoing else incoming. |
| #define | [BT\_TBS\_CALL\_FLAG\_WITHHELD](#ga25ff3c36aaabc5e37b08acc62ac21be6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | If set call is withheld, else not withheld. |
| #define | [BT\_TBS\_CALL\_FLAG\_WITHHELD\_BY\_NETWORK](#ga466c1c3c50e82fee9e5c8323e89be414)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | If set call is withheld by network, else provided by network. |

## Detailed Description

Telephone Bearer Service (TBS).

Since
:   3.0

Version
:   0.8.0

The Telephone Bearer Service (TBS) provide procedures to discover telephone bearers and control calls.

## Macro Definition Documentation

## [◆ ](#ga74344c01327304f1d2da050ddc589735)BT\_TBS\_CALL\_FLAG\_OUTGOING

| #define BT\_TBS\_CALL\_FLAG\_OUTGOING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

If set, call is outgoing else incoming.

## [◆ ](#ga25ff3c36aaabc5e37b08acc62ac21be6)BT\_TBS\_CALL\_FLAG\_WITHHELD

| #define BT\_TBS\_CALL\_FLAG\_WITHHELD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

If set call is withheld, else not withheld.

## [◆ ](#ga466c1c3c50e82fee9e5c8323e89be414)BT\_TBS\_CALL\_FLAG\_WITHHELD\_BY\_NETWORK

| #define BT\_TBS\_CALL\_FLAG\_WITHHELD\_BY\_NETWORK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

If set call is withheld by network, else provided by network.

## [◆ ](#ga3100ab7a7db823d86198847ec0df4adc)BT\_TBS\_CALL\_STATE\_ACTIVE

| #define BT\_TBS\_CALL\_STATE\_ACTIVE   0x03 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The call is in an active conversation.

## [◆ ](#gada61fd749f2119452429dd712d283dad)BT\_TBS\_CALL\_STATE\_ALERTING

| #define BT\_TBS\_CALL\_STATE\_ALERTING   0x02 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

A remote party is being alerted (outgoing call).

## [◆ ](#ga482f9627308cad1e56a4a5a5906c2308)BT\_TBS\_CALL\_STATE\_DIALING

| #define BT\_TBS\_CALL\_STATE\_DIALING   0x01 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The process to call the remote party has started on the server, but the remote party is not being alerted (outgoing call).

## [◆ ](#ga829309945831c0e8ac36c3dd79ae26f3)BT\_TBS\_CALL\_STATE\_INCOMING

| #define BT\_TBS\_CALL\_STATE\_INCOMING   0x00 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

A remote party is calling (incoming call).

## [◆ ](#ga0d28984faadc6904f72068df6ab6c97d)BT\_TBS\_CALL\_STATE\_LOCALLY\_AND\_REMOTELY\_HELD

| #define BT\_TBS\_CALL\_STATE\_LOCALLY\_AND\_REMOTELY\_HELD   0x06 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The call is connected but held both locally and remotely.

## [◆ ](#gac900fe331fe5b81d7ed0b21796d3e16c)BT\_TBS\_CALL\_STATE\_LOCALLY\_HELD

| #define BT\_TBS\_CALL\_STATE\_LOCALLY\_HELD   0x04 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The call is connected but held locally.

Locally Held implies that either the server or the client can affect the state.

## [◆ ](#ga76acd3539931a32361fd0deb3bbe8243)BT\_TBS\_CALL\_STATE\_REMOTELY\_HELD

| #define BT\_TBS\_CALL\_STATE\_REMOTELY\_HELD   0x05 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The call is connected but held remotely.

Remotely Held means that the state is controlled by the remote party of a call.

## [◆ ](#gadd72fdfd22c6a3abca8a270aae6a689a)BT\_TBS\_FEATURE\_ALL

| #define BT\_TBS\_FEATURE\_ALL   ([BT\_TBS\_FEATURE\_HOLD](#gabb6c3b57d7c48620b0f019992c55e585) | [BT\_TBS\_FEATURE\_JOIN](#ga962ce8d27abbdc48adbc01b2c68cb042)) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

All Control Point Opcodes supported.

## [◆ ](#gabb6c3b57d7c48620b0f019992c55e585)BT\_TBS\_FEATURE\_HOLD

| #define BT\_TBS\_FEATURE\_HOLD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Local Hold and Local Retrieve Call Control Point Opcodes supported.

## [◆ ](#ga962ce8d27abbdc48adbc01b2c68cb042)BT\_TBS\_FEATURE\_JOIN

| #define BT\_TBS\_FEATURE\_JOIN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Join Call Control Point Opcode supported.

## [◆ ](#ga25aa807f2e3a01d030edf4f064a4fbfd)BT\_TBS\_GTBS\_INDEX

| #define BT\_TBS\_GTBS\_INDEX   0xFF |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The GTBS index denotes whenever a callback is from a Generic Telephone Bearer Service (GTBS) instance, or whenever the client should perform on action on the GTBS instance of the server, rather than any of the specific Telephone Bearer Service instances.

## [◆ ](#gaf7f2abd7e794806ab6b119bee47db6c6)BT\_TBS\_REASON\_BAD\_REMOTE\_URI

| #define BT\_TBS\_REASON\_BAD\_REMOTE\_URI   0x00 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The URI value used to originate a call was formed improperly.

## [◆ ](#gacd5a09f5786e01662e29d49aa5307046)BT\_TBS\_REASON\_CALL\_FAILED

| #define BT\_TBS\_REASON\_CALL\_FAILED   0x01 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The call failed.

## [◆ ](#ga614adc266444030ac83dc6f4d2e89563)BT\_TBS\_REASON\_CLIENT\_TERMINATED

| #define BT\_TBS\_REASON\_CLIENT\_TERMINATED   0x06 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The client terminated the call.

## [◆ ](#ga3105e7b0b91b71eb55c1ea5c3bfd6df3)BT\_TBS\_REASON\_LINE\_BUSY

| #define BT\_TBS\_REASON\_LINE\_BUSY   0x04 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The line was busy.

## [◆ ](#gae195db56d2cd949a29d261c5473eea89)BT\_TBS\_REASON\_NETWORK\_CONGESTED

| #define BT\_TBS\_REASON\_NETWORK\_CONGESTED   0x05 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Network congestion.

## [◆ ](#ga893d3c79ca62c5e5487d7ca7cd403ce2)BT\_TBS\_REASON\_NO\_ANSWER

| #define BT\_TBS\_REASON\_NO\_ANSWER   0x08 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

No answer.

## [◆ ](#ga137b813cf902c8209a624c6ae8d4a93b)BT\_TBS\_REASON\_NO\_SERVICE

| #define BT\_TBS\_REASON\_NO\_SERVICE   0x07 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

No service.

## [◆ ](#ga4bc073b85c6eca1f0a4b0757e1050dde)BT\_TBS\_REASON\_REMOTE\_ENDED\_CALL

| #define BT\_TBS\_REASON\_REMOTE\_ENDED\_CALL   0x02 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The remote party ended the call.

## [◆ ](#gaa4f89b5fa61dcc4ee7e4fb6ae0e12384)BT\_TBS\_REASON\_SERVER\_ENDED\_CALL

| #define BT\_TBS\_REASON\_SERVER\_ENDED\_CALL   0x03 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The call ended from the server.

## [◆ ](#gaa4dab0b5c08dcf092a125986519a7d55)BT\_TBS\_REASON\_UNSPECIFIED

| #define BT\_TBS\_REASON\_UNSPECIFIED   0x09 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Unspecified.

## [◆ ](#gadc371a3a898b3ecac56d8778109f315d)BT\_TBS\_RESULT\_CODE\_INVALID\_CALL\_INDEX

| #define BT\_TBS\_RESULT\_CODE\_INVALID\_CALL\_INDEX   0x03 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The Call Index used for the Call Control Point write is invalid.

## [◆ ](#gaa60f75b90f461246b2f470930a60efc2)BT\_TBS\_RESULT\_CODE\_INVALID\_URI

| #define BT\_TBS\_RESULT\_CODE\_INVALID\_URI   0x06 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The Outgoing URI is incorrect or invalid when an Originate opcode is sent.

## [◆ ](#gafac3c970b36f37c815c4370dfef89f09)BT\_TBS\_RESULT\_CODE\_OPCODE\_NOT\_SUPPORTED

| #define BT\_TBS\_RESULT\_CODE\_OPCODE\_NOT\_SUPPORTED   0x01 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

An invalid opcode was used for the Call Control Point write.

## [◆ ](#gae83a73a5a0474a62dfbcb5ced6eb3f78)BT\_TBS\_RESULT\_CODE\_OPERATION\_NOT\_POSSIBLE

| #define BT\_TBS\_RESULT\_CODE\_OPERATION\_NOT\_POSSIBLE   0x02 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The requested operation cannot be completed.

## [◆ ](#ga148585f5cfe8b1cd7f8db404dac91cdd)BT\_TBS\_RESULT\_CODE\_OUT\_OF\_RESOURCES

| #define BT\_TBS\_RESULT\_CODE\_OUT\_OF\_RESOURCES   0x05 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Lack of internal resources to complete the requested action.

## [◆ ](#ga3fa49179525369502018912115c1ccce)BT\_TBS\_RESULT\_CODE\_STATE\_MISMATCH

| #define BT\_TBS\_RESULT\_CODE\_STATE\_MISMATCH   0x04 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The opcode written to the Call Control Point was received when the current Call State for the Call Index was not in the expected state.

## [◆ ](#gaa92fdb19227ee0b268f2395f3f6a5f63)BT\_TBS\_RESULT\_CODE\_SUCCESS

| #define BT\_TBS\_RESULT\_CODE\_SUCCESS   0x00 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

The opcode write was successful.

## [◆ ](#gae619d9096b41690ba77ee3e7bd838be3)BT\_TBS\_SIGNAL\_STRENGTH\_MAX

| #define BT\_TBS\_SIGNAL\_STRENGTH\_MAX   100 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Maximum signal strength.

## [◆ ](#ga310c1cdffee350fe5235b3ad929ac715)BT\_TBS\_SIGNAL\_STRENGTH\_NO\_SERVICE

| #define BT\_TBS\_SIGNAL\_STRENGTH\_NO\_SERVICE   0 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

No service.

## [◆ ](#gab8a433da27a61cf1c7be2fc7b006e298)BT\_TBS\_SIGNAL\_STRENGTH\_UNKNOWN

| #define BT\_TBS\_SIGNAL\_STRENGTH\_UNKNOWN   255 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Signal strength is unknown.

## [◆ ](#gadc590b9f5813e190fa14644412aee25c)BT\_TBS\_STATUS\_FLAG\_INBAND\_RINGTONE

| #define BT\_TBS\_STATUS\_FLAG\_INBAND\_RINGTONE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Inband ringtone enabled.

## [◆ ](#ga53dfa36830f8c562711d9c6f9111929e)BT\_TBS\_STATUS\_FLAG\_SILENT\_MOD

| #define BT\_TBS\_STATUS\_FLAG\_SILENT\_MOD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Server is in silent mod.

## [◆ ](#gafcb1e805e56eb93f6a19b63f2cbf524c)BT\_TBS\_TECHNOLOGY\_2G

| #define BT\_TBS\_TECHNOLOGY\_2G   0x08 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

2G

## [◆ ](#gaf125f3486c88517c9e1e218c6ce492e4)BT\_TBS\_TECHNOLOGY\_3G

| #define BT\_TBS\_TECHNOLOGY\_3G   0x01 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

3G

## [◆ ](#ga967b2b97a2e862f5ae235fc9b728b15c)BT\_TBS\_TECHNOLOGY\_4G

| #define BT\_TBS\_TECHNOLOGY\_4G   0x02 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

4G

## [◆ ](#ga28c1928de97f2b7f0e7e36bfe1a5bdde)BT\_TBS\_TECHNOLOGY\_5G

| #define BT\_TBS\_TECHNOLOGY\_5G   0x05 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

5G

## [◆ ](#gaeb6d5ed9dcdba0849f81413ef08570bc)BT\_TBS\_TECHNOLOGY\_CDMA

| #define BT\_TBS\_TECHNOLOGY\_CDMA   0x07 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Code-Division Multiple Access (CDMA).

## [◆ ](#gad530e2c9b8b616a9674012ecc801421f)BT\_TBS\_TECHNOLOGY\_GSM

| #define BT\_TBS\_TECHNOLOGY\_GSM   0x06 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Global System for Mobile Communications (GSM).

## [◆ ](#ga6962ce833da01b3a584528b2ce361447)BT\_TBS\_TECHNOLOGY\_LTE

| #define BT\_TBS\_TECHNOLOGY\_LTE   0x03 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Long-term evolution (LTE).

## [◆ ](#ga3b828481ce60034abbdab8aa4b1ae972)BT\_TBS\_TECHNOLOGY\_WCDMA

| #define BT\_TBS\_TECHNOLOGY\_WCDMA   0x09 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Wideband Code-Division Multiple Access (WCDMA).

## [◆ ](#ga02af096f1153eed9623f7a7324956e86)BT\_TBS\_TECHNOLOGY\_WIFI

| #define BT\_TBS\_TECHNOLOGY\_WIFI   0x04 |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Wifi.

## Typedef Documentation

## [◆ ](#ga1cc9e7140531b07bf6a8dedbc17f24c0)bt\_tbs\_authorize\_cb

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_tbs\_authorize\_cb) (struct bt\_conn \*conn) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for authorizing a client.

Parameters
:   | conn | The connection used. |
    | --- | --- |

Returns
:   true if authorized, false otherwise

## [◆ ](#ga2fa85f3cd96f25f6bb4f449fc9210fa1)bt\_tbs\_call\_change\_cb

| typedef void(\* bt\_tbs\_call\_change\_cb) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for client request call state change.

Parameters
:   | conn | The connection used. |
    | --- | --- |
    | call\_index | The call index. |

## [◆ ](#ga262ca74b7ae2f0c52657066549fa4f92)bt\_tbs\_client\_call\_states\_cb

| typedef void(\* bt\_tbs\_client\_call\_states\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_count, const struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) \*call\_states) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for ccp\_read\_call\_state.

Parameters
:   | conn | The connection used in the function. |
    | --- | --- |
    | err | Error value. BT\_TBS\_CLIENT\_RESULT\_CODE\_\*, GATT error or errno value. |
    | inst\_index | The index of the TBS instance that was updated. |
    | call\_count | Number of call states read. |
    | call\_states | Array of call states. The array is not kept by the client, so must be copied to be saved. |

## [◆ ](#ga40b8b3d1b318a1b5c5524877bbc2f90f)bt\_tbs\_client\_cp\_cb

| typedef void(\* bt\_tbs\_client\_cp\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for the CCP call control functions.

Parameters
:   | conn | The connection used in the function. |
    | --- | --- |
    | err | Error value. BT\_TBS\_CLIENT\_RESULT\_CODE\_\*, GATT error or errno value. |
    | inst\_index | The index of the TBS instance that was updated. |
    | call\_index | The call index. For [bt\_tbs\_client\_originate\_call](#ga0aac704008ffc92ce6609d3ffffc4523) this will always be 0, and does not reflect the actual call index. |

## [◆ ](#ga7b31e1c30fa96081a3ef38e1a481b64f)bt\_tbs\_client\_current\_calls\_cb

| typedef void(\* bt\_tbs\_client\_current\_calls\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_count, const struct [bt\_tbs\_client\_call](structbt__tbs__client__call.md) \*calls) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for ccp\_read\_current\_calls.

Parameters
:   | conn | The connection used in the function. |
    | --- | --- |
    | err | Error value. BT\_TBS\_CLIENT\_RESULT\_CODE\_\*, GATT error or errno value. |
    | inst\_index | The index of the TBS instance that was updated. |
    | call\_count | Number of calls read. |
    | calls | Array of calls. The array is not kept by the client, so must be copied to be saved. |

## [◆ ](#ga9cac11cc696be9fb387f2f7685e0d8a7)bt\_tbs\_client\_discover\_cb

| typedef void(\* bt\_tbs\_client\_discover\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tbs\_count, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) gtbs\_found) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for ccp\_discover.

Parameters
:   | conn | The connection that was used to discover CCP for a device. |
    | --- | --- |
    | err | Error value. BT\_TBS\_CLIENT\_RESULT\_CODE\_\*, GATT error or errno value. |
    | tbs\_count | Number of TBS instances on peer device. |
    | gtbs\_found | Whether or not the server has a Generic TBS instance. |

## [◆ ](#ga4d7632de7c2006e478880950076908a9)bt\_tbs\_client\_read\_string\_cb

| typedef void(\* bt\_tbs\_client\_read\_string\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, const char \*value) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for functions that read a string value.

Parameters
:   | conn | The connection used in the function. |
    | --- | --- |
    | err | Error value. BT\_TBS\_CLIENT\_RESULT\_CODE\_\*, GATT error or errno value. |
    | inst\_index | The index of the TBS instance that was updated. |
    | value | The Null-terminated string value. The value is not kept by the client, so must be copied to be saved. |

## [◆ ](#ga600051910ed538a2da823554df23dd20)bt\_tbs\_client\_read\_value\_cb

| typedef void(\* bt\_tbs\_client\_read\_value\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for functions that read an integer value.

Parameters
:   | conn | The connection used in the function. |
    | --- | --- |
    | err | Error value. BT\_TBS\_CLIENT\_RESULT\_CODE\_\*, GATT error or errno value. |
    | inst\_index | The index of the TBS instance that was updated. |
    | value | The integer value. |

## [◆ ](#gab881b3caaaa4425e52afd84e53adee78)bt\_tbs\_client\_termination\_reason\_cb

| typedef void(\* bt\_tbs\_client\_termination\_reason\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for ccp\_read\_termination\_reason.

Parameters
:   | conn | The connection used in the function. |
    | --- | --- |
    | err | Error value. BT\_TBS\_CLIENT\_RESULT\_CODE\_\*, GATT error or errno value. |
    | inst\_index | The index of the TBS instance that was updated. |
    | call\_index | The call index. |
    | reason | The termination reason. |

## [◆ ](#gaf77231168e4444da7aef203cc9eaca95)bt\_tbs\_client\_write\_value\_cb

| typedef void(\* bt\_tbs\_client\_write\_value\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) inst\_index) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for writing values to peer device.

Parameters
:   | conn | The connection used in the function. |
    | --- | --- |
    | err | Error value. BT\_TBS\_CLIENT\_RESULT\_CODE\_\*, GATT error or errno value. |
    | inst\_index | The index of the TBS instance that was updated. |

## [◆ ](#gaa45b3f4837165d722c2df6f202a39058)bt\_tbs\_join\_calls\_cb

| typedef void(\* bt\_tbs\_join\_calls\_cb) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index\_count, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*call\_indexes) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for client joining calls.

Parameters
:   | conn | The connection used. |
    | --- | --- |
    | call\_index\_count | The number of call indexes to join. |
    | call\_indexes | The call indexes. |

## [◆ ](#ga60e9e143f247bb7e668293f0233ce300)bt\_tbs\_originate\_call\_cb

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_tbs\_originate\_call\_cb) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index, const char \*uri) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for client originating a call.

Parameters
:   | conn | The connection used. |
    | --- | --- |
    | call\_index | The call index. |
    | uri | The URI. The value may change, so should be copied if persistence is wanted. |

Returns
:   true if the call request was accepted and remote party is alerted.

## [◆ ](#ga69e93b48b2a48e8a6552882660b791cc)bt\_tbs\_terminate\_call\_cb

| typedef void(\* bt\_tbs\_terminate\_call\_cb) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) call\_index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

`#include <[tbs.h](tbs_8h.md)>`

Callback function for client terminating a call.

The call may be either terminated by the client or the server.

Parameters
:   | conn | The connection used. |
    | --- | --- |
    | call\_index | The call index. |
    | reason | The termination BT\_TBS\_REASON\_\* reason. |

## Function Documentation

## [◆ ](#ga1b942bcf8287641f9cd53824b4d6e77b)bt\_tbs\_accept()

| int bt\_tbs\_accept | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Accept an alerting call.

Parameters
:   | call\_index | The index of the call that will be accepted. |
    | --- | --- |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#ga625fc73885c2bfd63f0f4b2d7f72eaef)bt\_tbs\_client\_accept\_call()

| int bt\_tbs\_client\_accept\_call | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Accept an incoming call.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |
    | call\_index | The call index to accept. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_ACCEPT_CALL
    ```

    must be set for this function to be effective.

## [◆ ](#gac59f3dec092a14bdf234039e3dcd12eb)bt\_tbs\_client\_discover()

| int bt\_tbs\_client\_discover | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Discover TBS for a connection.

This will start a GATT discover and setup handles and subscriptions.

Parameters
:   | conn | The connection to discover TBS for. |
    | --- | --- |

Returns
:   int 0 on success, GATT error value on fail.

## [◆ ](#gaadae501fa6f7771bb9661af829805a5f)bt\_tbs\_client\_get\_by\_ccid()

| struct bt\_tbs\_instance \* bt\_tbs\_client\_get\_by\_ccid | ( | const struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ccid* ) |

`#include <[tbs.h](tbs_8h.md)>`

Look up Telephone Bearer Service instance by CCID.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | ccid | The CCID to lookup a service instance for. |

Returns
:   Pointer to a Telephone Bearer Service instance if found else NULL.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_CCID
    ```

    must be set for this function to be effective.

## [◆ ](#ga23e825de6af71d4e456b63c3a621fb61)bt\_tbs\_client\_hold\_call()

| int bt\_tbs\_client\_hold\_call | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Request to hold a call.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |
    | call\_index | The call index to place on hold. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_HOLD_CALL
    ```

    must be set for this function to be effective.

## [◆ ](#gaae1925deb0b5865af601aa8278ffb10a)bt\_tbs\_client\_join\_calls()

| int bt\_tbs\_client\_join\_calls | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *call\_indexes*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *count* ) |

`#include <[tbs.h](tbs_8h.md)>`

Join multiple calls.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |
    | call\_indexes | Array of call indexes. |
    | count | Number of call indexes in the call\_indexes array. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_JOIN_CALLS
    ```

    must be set for this function to be effective.

## [◆ ](#ga0aac704008ffc92ce6609d3ffffc4523)bt\_tbs\_client\_originate\_call()

| int bt\_tbs\_client\_originate\_call | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index*, |
|  |  | const char \* | *uri* ) |

`#include <[tbs.h](tbs_8h.md)>`

Request to originate a call.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |
    | uri | The URI of the callee. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL
    ```

    must be set for this function to be effective.

## [◆ ](#ga2053a9eb7cf28f66febd365f0b682be0)bt\_tbs\_client\_read\_bearer\_provider\_name()

| int bt\_tbs\_client\_read\_bearer\_provider\_name | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the bearer provider name of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME
    ```

    must be set for this function to be effective.

## [◆ ](#gaba92039d3b44da9163a22400951fafa7)bt\_tbs\_client\_read\_bearer\_uci()

| int bt\_tbs\_client\_read\_bearer\_uci | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the UCI of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_BEARER_UCI
    ```

    must be set for this function to be effective.

## [◆ ](#gafeaaaefb9d4eb773dd0cbdfebe26e0b7)bt\_tbs\_client\_read\_call\_state()

| int bt\_tbs\_client\_read\_call\_state | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the states of the current calls of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

## [◆ ](#ga4238a37b80b7d7ff611fe9b02b7cf54d)bt\_tbs\_client\_read\_call\_uri()

| int bt\_tbs\_client\_read\_call\_uri | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the call target URI of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_INCOMING_URI
    ```

    must be set for this function to be effective.

## [◆ ](#gac070ec0590df5820b7721d579ceeeb15)bt\_tbs\_client\_read\_ccid()

| int bt\_tbs\_client\_read\_ccid | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the content ID of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_CCID
    ```

    must be set for this function to be effective.

## [◆ ](#ga895c7f54300e5452fb8d0c9d4b3306ae)bt\_tbs\_client\_read\_current\_calls()

| int bt\_tbs\_client\_read\_current\_calls | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the list of current calls of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_BEARER_LIST_CURRENT_CALLS
    ```

    must be set for this function to be effective.

## [◆ ](#ga99549dd6244580e157006fb17772fd8f)bt\_tbs\_client\_read\_friendly\_name()

| int bt\_tbs\_client\_read\_friendly\_name | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the friendly name of a call for a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_CALL_FRIENDLY_NAME
    ```

    must be set for this function to be effective.

## [◆ ](#gaf504e1a11352d77a36aa087b587e4ba8)bt\_tbs\_client\_read\_optional\_opcodes()

| int bt\_tbs\_client\_read\_optional\_opcodes | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the supported opcode of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_OPTIONAL_OPCODES
    ```

    must be set for this function to be effective.

## [◆ ](#gab04f8355c32fce501bd757b75ee9d38a)bt\_tbs\_client\_read\_remote\_uri()

| int bt\_tbs\_client\_read\_remote\_uri | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the remote URI of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_INCOMING_CALL
    ```

    must be set for this function to be effective.

## [◆ ](#ga38046c5c715d451b21a3076742268010)bt\_tbs\_client\_read\_signal\_interval()

| int bt\_tbs\_client\_read\_signal\_interval | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the signal strength reporting interval of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_READ_BEARER_SIGNAL_INTERVAL
    ```

    must be set for this function to be effective.

## [◆ ](#gaabe97df55817b8e36c79de4bf30fc83f)bt\_tbs\_client\_read\_signal\_strength()

| int bt\_tbs\_client\_read\_signal\_strength | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the current signal strength of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_BEARER_SIGNAL_STRENGTH
    ```

    must be set for this function to be effective.

## [◆ ](#ga9fe91df1a31ce59401347fc0eac2b701)bt\_tbs\_client\_read\_status\_flags()

| int bt\_tbs\_client\_read\_status\_flags | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the feature and status value of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_STATUS_FLAGS
    ```

    must be set for this function to be effective.

## [◆ ](#ga7684dbcb78e407f7002d44fbdb805e5d)bt\_tbs\_client\_read\_technology()

| int bt\_tbs\_client\_read\_technology | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the technology of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY
    ```

    must be set for this function to be effective.

## [◆ ](#gad19db25591c7ae5bd0b4c2bbaefc9bed)bt\_tbs\_client\_read\_uri\_list()

| int bt\_tbs\_client\_read\_uri\_list | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Read the URI schemes list of a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST
    ```

    must be set for this function to be effective.

## [◆ ](#gabe2251d4ea88306793dc68ae683886bb)bt\_tbs\_client\_register\_cb()

| int bt\_tbs\_client\_register\_cb | ( | struct [bt\_tbs\_client\_cb](structbt__tbs__client__cb.md) \* | *cbs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Register the callbacks for CCP.

Parameters
:   | cbs | Pointer to the callback structure. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `cbs` is NULL |
    | -EEXIST | `cbs` is already registered |

## [◆ ](#gabbe194a63da0b95dc1dca0337560a585)bt\_tbs\_client\_retrieve\_call()

| int bt\_tbs\_client\_retrieve\_call | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Retrieve call from (local) hold.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |
    | call\_index | The call index to retrieve. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL
    ```

    must be set for this function to be effective.

## [◆ ](#ga3a71c51d464aa19fbfbd2d60fc4901bc)bt\_tbs\_client\_set\_outgoing\_uri()

| int bt\_tbs\_client\_set\_outgoing\_uri | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index*, |
|  |  | const char \* | *uri* ) |

`#include <[tbs.h](tbs_8h.md)>`

Set the outgoing URI for a TBS instance on the peer device.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |
    | uri | The Null-terminated URI string. |

Returns
:   int 0 on success, errno value on fail.

## [◆ ](#gaa1dcb9908057d75a54fa447639826f3c)bt\_tbs\_client\_set\_signal\_strength\_interval()

| int bt\_tbs\_client\_set\_signal\_strength\_interval | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *interval* ) |

`#include <[tbs.h](tbs_8h.md)>`

Set the signal strength reporting interval for a TBS instance.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |
    | interval | The interval to write (0-255 seconds). |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_SET_BEARER_SIGNAL_INTERVAL
    ```

    must be set for this function to be effective.

## [◆ ](#ga25b803bb5cae2e1a8b0398bc48137d80)bt\_tbs\_client\_terminate\_call()

| int bt\_tbs\_client\_terminate\_call | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *inst\_index*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Request to terminate a call.

Parameters
:   | conn | The connection to the TBS server. |
    | --- | --- |
    | inst\_index | The index of the TBS instance. |
    | call\_index | The call index to terminate. |

Returns
:   int 0 on success, errno value on fail.

Note
:   ```
    CONFIG_BT_TBS_CLIENT_TERMINATE_CALL
    ```

    must be set for this function to be effective.

## [◆ ](#ga62f5008cbfba158fe399cfaf683d1d2e)bt\_tbs\_dbg\_print\_calls()

| void bt\_tbs\_dbg\_print\_calls | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Prints all calls of all services to the debug log.

## [◆ ](#gab72044a1f5466114b5efb88dfcd2f097)bt\_tbs\_hold()

| int bt\_tbs\_hold | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Hold a call.

Parameters
:   | call\_index | The index of the call that will be held. |
    | --- | --- |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#ga23226d41e3b98a53ec9a9c2fa346c9ac)bt\_tbs\_join()

| int bt\_tbs\_join | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index\_cnt*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *call\_indexes* ) |

`#include <[tbs.h](tbs_8h.md)>`

Join calls.

Parameters
:   | call\_index\_cnt | The number of call indexes to join |
    | --- | --- |
    | call\_indexes | Array of call indexes to join. |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#gadeae51d7cecd80abcdcde1195bb1dfba)bt\_tbs\_originate()

| int bt\_tbs\_originate | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bearer\_index*, |
| --- | --- | --- | --- |
|  |  | char \* | *uri*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *call\_index* ) |

`#include <[tbs.h](tbs_8h.md)>`

Originate a call.

Parameters
:   | [in] | bearer\_index | The index of the Telephone Bearer. |
    | --- | --- | --- |
    | [in] | uri | The remote URI. |
    | [out] | call\_index | Pointer to a value where the new call\_index will be stored. |

Returns
:   int A call index on success (positive value), errno value on fail.

## [◆ ](#ga970c970bedd6e94aa4c92479183554e9)bt\_tbs\_register\_bearer()

| int bt\_tbs\_register\_bearer | ( | const struct [bt\_tbs\_register\_param](structbt__tbs__register__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Register a Telephone Bearer.

This will register a Telephone Bearer Service (TBS) (or a Generic Telephone Bearer service (GTBS)) with the provided parameters.

As per the TBS specification, the GTBS shall be instantiated for the feature, and as such a GTBS shall always be registered before any TBS can be registered. Similarly, all TBS shall be unregistered before the GTBS can be unregistered with [bt\_tbs\_unregister\_bearer()](#ga8edd4d31478ed9e0aedbd1a34bdfca96).

Parameters
:   | param | The parameters to initialize the bearer. |
    | --- | --- |

Return values
:   | index | The bearer index if return value is >= 0 |
    | --- | --- |
    | -EINVAL | `param` contains invalid data |
    | -EALREADY | `param.gtbs` is true and GTBS has already been registered |
    | -EAGAIN | `param.gtbs` is false and GTBS has not been registered |
    | -ENOMEM | `param.gtbs` is false and no more TBS can be registered (see  ``` CONFIG_BT_TBS_BEARER_COUNT ```  ) |
    | -ENOEXEC | The service failed to be registered |

## [◆ ](#ga76f120dba549225a6f2c2c22be08edfc)bt\_tbs\_register\_cb()

| void bt\_tbs\_register\_cb | ( | struct [bt\_tbs\_cb](structbt__tbs__cb.md) \* | *cbs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Register the callbacks for TBS.

Parameters
:   | cbs | Pointer to the callback structure. |
    | --- | --- |

## [◆ ](#ga868b83450f7425e8a0c8cfb7c1de45d8)bt\_tbs\_remote\_answer()

| int bt\_tbs\_remote\_answer | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Notify the server that the remote party answered the call.

Parameters
:   | call\_index | The index of the call that was answered. |
    | --- | --- |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e)bt\_tbs\_remote\_hold()

| int bt\_tbs\_remote\_hold | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Notify the server that the remote party held the call.

Parameters
:   | call\_index | The index of the call that was held. |
    | --- | --- |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#ga47939f557e4d6503af9b7b85aff9d60f)bt\_tbs\_remote\_incoming()

| int bt\_tbs\_remote\_incoming | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bearer\_index*, |
| --- | --- | --- | --- |
|  |  | const char \* | *to*, |
|  |  | const char \* | *from*, |
|  |  | const char \* | *friendly\_name* ) |

`#include <[tbs.h](tbs_8h.md)>`

Notify the server of an incoming call.

Parameters
:   | bearer\_index | The index of the Telephone Bearer. |
    | --- | --- |
    | to | The URI that is receiving the call. |
    | from | The URI of the remote caller. |
    | friendly\_name | The friendly name of the remote caller. |

Returns
:   int New call index if positive or 0, errno value if negative.

## [◆ ](#ga09a3e64040819b6b8b694b94d2f62ca0)bt\_tbs\_remote\_retrieve()

| int bt\_tbs\_remote\_retrieve | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Notify the server that the remote party retrieved the call.

Parameters
:   | call\_index | The index of the call that was retrieved. |
    | --- | --- |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#ga52afc7b8a22b071dbac10057579f319c)bt\_tbs\_remote\_terminate()

| int bt\_tbs\_remote\_terminate | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Notify the server that the remote party terminated the call.

Parameters
:   | call\_index | The index of the call that was terminated. |
    | --- | --- |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#gad0b45af09b82d6cd66a8481c0e67e04e)bt\_tbs\_retrieve()

| int bt\_tbs\_retrieve | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Retrieve a call.

Parameters
:   | call\_index | The index of the call that will be retrieved. |
    | --- | --- |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#ga5118db6b23b387956e75eda8aecd53d5)bt\_tbs\_set\_bearer\_provider\_name()

| int bt\_tbs\_set\_bearer\_provider\_name | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bearer\_index*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name* ) |

`#include <[tbs.h](tbs_8h.md)>`

Set a new bearer provider.

Parameters
:   | bearer\_index | The index of the Telephone Bearer or BT\_TBS\_GTBS\_INDEX for GTBS. |
    | --- | --- |
    | name | The new bearer provider name. |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#gaf4c576b8aa599f1bd9598964bc1b779f)bt\_tbs\_set\_bearer\_technology()

| int bt\_tbs\_set\_bearer\_technology | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bearer\_index*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *new\_technology* ) |

`#include <[tbs.h](tbs_8h.md)>`

Set a new bearer technology.

Parameters
:   | bearer\_index | The index of the Telephone Bearer or BT\_TBS\_GTBS\_INDEX for GTBS. |
    | --- | --- |
    | new\_technology | The new bearer technology. |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#gac316adedf7fda441ee55feb9d24d1a94)bt\_tbs\_set\_signal\_strength()

| int bt\_tbs\_set\_signal\_strength | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bearer\_index*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *new\_signal\_strength* ) |

`#include <[tbs.h](tbs_8h.md)>`

Update the signal strength reported by the server.

Parameters
:   | bearer\_index | The index of the Telephone Bearer or BT\_TBS\_GTBS\_INDEX for GTBS. |
    | --- | --- |
    | new\_signal\_strength | The new signal strength. |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#ga838e51a85f9833e0822090cd3df09e00)bt\_tbs\_set\_status\_flags()

| int bt\_tbs\_set\_status\_flags | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bearer\_index*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *status\_flags* ) |

`#include <[tbs.h](tbs_8h.md)>`

Sets the feature and status value.

Parameters
:   | bearer\_index | The index of the Telephone Bearer or BT\_TBS\_GTBS\_INDEX for GTBS. |
    | --- | --- |
    | status\_flags | The new feature and status value. |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#ga90b3fb1d757fbb134649b0d7f9047123)bt\_tbs\_set\_uri\_scheme\_list()

| int bt\_tbs\_set\_uri\_scheme\_list | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bearer\_index*, |
| --- | --- | --- | --- |
|  |  | const char \*\* | *uri\_list*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *uri\_count* ) |

`#include <[tbs.h](tbs_8h.md)>`

Sets the URI scheme list of a bearer.

Parameters
:   | bearer\_index | The index of the Telephone Bearer. |
    | --- | --- |
    | uri\_list | List of URI prefixes (e.g. {"skype", "tel"}). |
    | uri\_count | Number of URI prefixies in `uri_list`. |

Returns
:   BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#ga82553640882ac74f9af84bfe09ff47ee)bt\_tbs\_terminate()

| int bt\_tbs\_terminate | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *call\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Terminate a call.

Parameters
:   | call\_index | The index of the call that will be terminated. |
    | --- | --- |

Returns
:   int BT\_TBS\_RESULT\_CODE\_\* if positive or 0, errno value if negative.

## [◆ ](#ga8edd4d31478ed9e0aedbd1a34bdfca96)bt\_tbs\_unregister\_bearer()

| int bt\_tbs\_unregister\_bearer | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bearer\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tbs.h](tbs_8h.md)>`

Unregister a Telephone Bearer.

This will unregister a Telephone Bearer Service (TBS) (or a Generic Telephone Bearer service (GTBS)) with the provided parameters. The bearer shall be registered first by [bt\_tbs\_register\_bearer()](#ga970c970bedd6e94aa4c92479183554e9) before it can be unregistered.

Similarly, all TBS shall be unregistered before the GTBS can be unregistered with.

Parameters
:   | bearer\_index | The index of the bearer to unregister. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `bearer_index` is invalid |
    | -EALREADY | The bearer identified by `bearer_index` is not registered |
    | -EAGAIN | The bearer identified by `bearer_index` is GTBS and there are TBS instances registered. |
    | -ENOEXEC | The service failed to be unregistered |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
