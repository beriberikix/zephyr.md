---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__coap.html
original_path: doxygen/html/group__coap.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

COAP Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

COAP library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [coap\_resource](structcoap__resource.md) |
|  | Description of CoAP resource. [More...](structcoap__resource.md#details) |
| struct | [coap\_observer](structcoap__observer.md) |
|  | Represents a remote device that is observing a local resource. [More...](structcoap__observer.md#details) |
| struct | [coap\_packet](structcoap__packet.md) |
|  | Representation of a CoAP Packet. [More...](structcoap__packet.md#details) |
| struct | [coap\_option](structcoap__option.md) |
|  | Representation of a CoAP option. [More...](structcoap__option.md#details) |
| struct | [coap\_transmission\_parameters](structcoap__transmission__parameters.md) |
|  | CoAP transmission parameters. [More...](structcoap__transmission__parameters.md#details) |
| struct | [coap\_pending](structcoap__pending.md) |
|  | Represents a request awaiting for an acknowledgment (ACK). [More...](structcoap__pending.md#details) |
| struct | [coap\_reply](structcoap__reply.md) |
|  | Represents the handler for the reply of a request, it is also used when observing resources. [More...](structcoap__reply.md#details) |
| struct | [coap\_block\_context](structcoap__block__context.md) |
|  | Represents the current state of a block-wise transaction. [More...](structcoap__block__context.md#details) |
| struct | [coap\_core\_metadata](structcoap__core__metadata.md) |
|  | In case you want to add attributes to the resources included in the 'well-known/core' "virtual" resource, the 'user\_data' field should point to a valid [coap\_core\_metadata](structcoap__core__metadata.md "In case you want to add attributes to the resources included in the 'well-known/core' "virtual" resou...") structure. [More...](structcoap__core__metadata.md#details) |

| Macros | |
| --- | --- |
| #define | [COAP\_MAKE\_RESPONSE\_CODE](#gabdcc1f443e89bd035522cbab7dfee879)(class, det) |
|  | Utility macro to create a CoAP response code. |
| #define | [COAP\_WELL\_KNOWN\_CORE\_PATH](#ga09d2c727fc6fc76aa9d908b759a3f40b)   ((const char \* const[]) { ".well-known", "core", [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) }) |
|  | This resource should be added before all other resources that should be included in the responses of the .well-known/core resource if is to be used with coap\_well\_known\_core\_get. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [coap\_method\_t](#gaa509d49f06101342908a71f2f18f18fc)) (struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_packet](structcoap__packet.md) \*request, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len) |
|  | Type of the callback being called when a resource's method is invoked by the remote entity. |
| typedef void(\* | [coap\_notify\_t](#ga4180b2476430fbe4a5e0418fb628ea91)) (struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_observer](structcoap__observer.md) \*observer) |
|  | Type of the callback being called when a resource's has observers to be informed when an update happens. |
| typedef int(\* | [coap\_reply\_t](#ga556deaf757f3047eefc2f032d0d7e0bc)) (const struct [coap\_packet](structcoap__packet.md) \*response, struct [coap\_reply](structcoap__reply.md) \*reply, const struct [sockaddr](structsockaddr.md) \*from) |
|  | Helper function to be called when a response matches the a pending request. |

| Enumerations | |
| --- | --- |
| enum | [coap\_option\_num](#ga7b8b3041e2f4ae26e663ff7431a6e6e3) {     [COAP\_OPTION\_IF\_MATCH](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4c61e26d11841c76debe2f99de5e9756) = 1 , [COAP\_OPTION\_URI\_HOST](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a402bb0a642a07d951c35d69736fd3f33) = 3 , [COAP\_OPTION\_ETAG](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a0efdc30ce5551daffd093b2a8466978a) = 4 , [COAP\_OPTION\_IF\_NONE\_MATCH](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a07ea6f395818a7019bb9e6a6e34d2d74) = 5 ,     [COAP\_OPTION\_OBSERVE](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a06e91bbb4fa2144543d4148d3245ad25) = 6 , [COAP\_OPTION\_URI\_PORT](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a344707b9f4cb71310f2ccf5e8050d17a) = 7 , [COAP\_OPTION\_LOCATION\_PATH](#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae82be3591d43f0d1c7e89ab764d969bd) = 8 , [COAP\_OPTION\_URI\_PATH](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a96b5a15937e875b3087307cc5faab1af) = 11 ,     [COAP\_OPTION\_CONTENT\_FORMAT](#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac3166e67b5f5bf3cefee58c8ff58e5b8) = 12 , [COAP\_OPTION\_MAX\_AGE](#gga7b8b3041e2f4ae26e663ff7431a6e6e3ab4cda4d3732fd12b9f203a2475c20981) = 14 , [COAP\_OPTION\_URI\_QUERY](#gga7b8b3041e2f4ae26e663ff7431a6e6e3adb4d27052247b9a79ad7fcc0cc30c71c) = 15 , [COAP\_OPTION\_ACCEPT](#gga7b8b3041e2f4ae26e663ff7431a6e6e3afd0725f0ceb5ce22a6c7b390ca7efc9d) = 17 ,     [COAP\_OPTION\_LOCATION\_QUERY](#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac728800fc8f0d80e37dcf322e75eb27d) = 20 , [COAP\_OPTION\_BLOCK2](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972) = 23 , [COAP\_OPTION\_BLOCK1](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a8aaa54af114fd1db631566afa69f162d) = 27 , [COAP\_OPTION\_SIZE2](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a26c1bcd7af4fccd949e3de35fc2d88e6) = 28 ,     [COAP\_OPTION\_PROXY\_URI](#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae4d2c93b545708926813217cd36a96ac) = 35 , [COAP\_OPTION\_PROXY\_SCHEME](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a30da986503e1e15243b74a16b161901c) = 39 , [COAP\_OPTION\_SIZE1](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a53169a1c7b07c9e97f79dfc06af3eb51) = 60 , [COAP\_OPTION\_ECHO](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a620e8b59f67f89de8a38dc76c8fcc594) = 252 ,     [COAP\_OPTION\_NO\_RESPONSE](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a7984f2c4845610491bda964111a1c8e7) = 258 , [COAP\_OPTION\_REQUEST\_TAG](#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2a47428ec35972d256da05104ea6396f) = 292   } |
|  | Set of CoAP packet options we are aware of. [More...](#ga7b8b3041e2f4ae26e663ff7431a6e6e3) |
| enum | [coap\_method](#ga6a6547e3c755cf7a5033302c8294e0b7) {     [COAP\_METHOD\_GET](#gga6a6547e3c755cf7a5033302c8294e0b7a025300cb0dc4c4de8eb0b0e0b4eb5317) = 1 , [COAP\_METHOD\_POST](#gga6a6547e3c755cf7a5033302c8294e0b7aba51bcab79bf75080ccf75c1ec38a3d6) = 2 , [COAP\_METHOD\_PUT](#gga6a6547e3c755cf7a5033302c8294e0b7a91637ef7c9f57cdcc65d0118008251db) = 3 , [COAP\_METHOD\_DELETE](#gga6a6547e3c755cf7a5033302c8294e0b7adccbea1fe9a43433cf8471e32208a5ac) = 4 ,     [COAP\_METHOD\_FETCH](#gga6a6547e3c755cf7a5033302c8294e0b7afa4070fed5c01b28bb1a59e3f0c021f4) = 5 , [COAP\_METHOD\_PATCH](#gga6a6547e3c755cf7a5033302c8294e0b7adca55e3d2b4b41b249f6b2f67074d708) = 6 , [COAP\_METHOD\_IPATCH](#gga6a6547e3c755cf7a5033302c8294e0b7a78f97b895f29819bf3f8b0314967f20e) = 7   } |
|  | Available request methods. [More...](#ga6a6547e3c755cf7a5033302c8294e0b7) |
| enum | [coap\_msgtype](#ga3b375b7580246d1266293d09902f3d9f) { [COAP\_TYPE\_CON](#gga3b375b7580246d1266293d09902f3d9fa65c04ee4847d0c595238079ac9564e8d) = 0 , [COAP\_TYPE\_NON\_CON](#gga3b375b7580246d1266293d09902f3d9fa629a304bea0c85c7b2bf746b26216a4f) = 1 , [COAP\_TYPE\_ACK](#gga3b375b7580246d1266293d09902f3d9fa7b2fe2187018bce9132af2763b57307d) = 2 , [COAP\_TYPE\_RESET](#gga3b375b7580246d1266293d09902f3d9fa287b951159fd51b84a2e0491b012f84c) = 3 } |
|  | CoAP packets may be of one of these types. [More...](#ga3b375b7580246d1266293d09902f3d9f) |
| enum | [coap\_response\_code](#ga1ea81a365834e96f43ab7be573069d26) {     [COAP\_RESPONSE\_CODE\_OK](#gga1ea81a365834e96f43ab7be573069d26a0629da1898b934c3f699b98ff808c717) = ((2 << 5) | (0)) , [COAP\_RESPONSE\_CODE\_CREATED](#gga1ea81a365834e96f43ab7be573069d26ad2d9fe8dd5beda74b522377c0b76275b) = ((2 << 5) | (1)) , [COAP\_RESPONSE\_CODE\_DELETED](#gga1ea81a365834e96f43ab7be573069d26abf324915aa498c64a733a0098de4a082) = ((2 << 5) | (2)) , [COAP\_RESPONSE\_CODE\_VALID](#gga1ea81a365834e96f43ab7be573069d26aecaac4a0e9c821dfc20536951409dd48) = ((2 << 5) | (3)) ,     [COAP\_RESPONSE\_CODE\_CHANGED](#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3) = ((2 << 5) | (4)) , [COAP\_RESPONSE\_CODE\_CONTENT](#gga1ea81a365834e96f43ab7be573069d26adfd3e5e3c6ad5715127bb444c205fbce) = ((2 << 5) | (5)) , [COAP\_RESPONSE\_CODE\_CONTINUE](#gga1ea81a365834e96f43ab7be573069d26ae4e3ff451c626421b9b329790f019dd8) = ((2 << 5) | (31)) , [COAP\_RESPONSE\_CODE\_BAD\_REQUEST](#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5) = ((4 << 5) | (0)) ,     [COAP\_RESPONSE\_CODE\_UNAUTHORIZED](#gga1ea81a365834e96f43ab7be573069d26acb76dbf11b47477144cc4ece3357283c) = ((4 << 5) | (1)) , [COAP\_RESPONSE\_CODE\_BAD\_OPTION](#gga1ea81a365834e96f43ab7be573069d26a989a6528edc653c0b693ed875481e82d) = ((4 << 5) | (2)) , [COAP\_RESPONSE\_CODE\_FORBIDDEN](#gga1ea81a365834e96f43ab7be573069d26afeee555ef54f138db58b14ad2c328d04) = ((4 << 5) | (3)) , [COAP\_RESPONSE\_CODE\_NOT\_FOUND](#gga1ea81a365834e96f43ab7be573069d26a86c2bff8add69428d164431b3091a8e9) = ((4 << 5) | (4)) ,     [COAP\_RESPONSE\_CODE\_NOT\_ALLOWED](#gga1ea81a365834e96f43ab7be573069d26a301eb722445472dba93d5accd6e0dd31) = ((4 << 5) | (5)) , [COAP\_RESPONSE\_CODE\_NOT\_ACCEPTABLE](#gga1ea81a365834e96f43ab7be573069d26a4d77322514521e8dfea01f4a1a6e5886) = ((4 << 5) | (6)) , [COAP\_RESPONSE\_CODE\_INCOMPLETE](#gga1ea81a365834e96f43ab7be573069d26a671730c6d2f1a339fcd557c5452150af) = ((4 << 5) | (8)) , [COAP\_RESPONSE\_CODE\_CONFLICT](#gga1ea81a365834e96f43ab7be573069d26ab447505d233aed9fd8ad28070d317544) = ((4 << 5) | (9)) ,     [COAP\_RESPONSE\_CODE\_PRECONDITION\_FAILED](#gga1ea81a365834e96f43ab7be573069d26a289ade02833b57bffd915e648e050e52) = ((4 << 5) | (12)) , [COAP\_RESPONSE\_CODE\_REQUEST\_TOO\_LARGE](#gga1ea81a365834e96f43ab7be573069d26aaa43062a8146c1e2e09183228a540d2e) = ((4 << 5) | (13)) , [COAP\_RESPONSE\_CODE\_UNSUPPORTED\_CONTENT\_FORMAT](#gga1ea81a365834e96f43ab7be573069d26aef6b165b9d3f8f4b477431058815c16b) , [COAP\_RESPONSE\_CODE\_UNPROCESSABLE\_ENTITY](#gga1ea81a365834e96f43ab7be573069d26a5e5e31cc4647d5e0fdd1c8fe6cfa2661) = ((4 << 5) | (22)) ,     [COAP\_RESPONSE\_CODE\_TOO\_MANY\_REQUESTS](#gga1ea81a365834e96f43ab7be573069d26aabd72cff6669d382aa04c53e764d0b49) = ((4 << 5) | (29)) , [COAP\_RESPONSE\_CODE\_INTERNAL\_ERROR](#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499) = ((5 << 5) | (0)) , [COAP\_RESPONSE\_CODE\_NOT\_IMPLEMENTED](#gga1ea81a365834e96f43ab7be573069d26a85c04541bc8580c2ae915946fd677c15) = ((5 << 5) | (1)) , [COAP\_RESPONSE\_CODE\_BAD\_GATEWAY](#gga1ea81a365834e96f43ab7be573069d26a8de29a7ee6bb960a97d6b415217b4640) = ((5 << 5) | (2)) ,     [COAP\_RESPONSE\_CODE\_SERVICE\_UNAVAILABLE](#gga1ea81a365834e96f43ab7be573069d26afebd274586351951ffe9c8f26b270dec) = ((5 << 5) | (3)) , [COAP\_RESPONSE\_CODE\_GATEWAY\_TIMEOUT](#gga1ea81a365834e96f43ab7be573069d26af6d379fef704c269406b782c60772ecd) = ((5 << 5) | (4)) , [COAP\_RESPONSE\_CODE\_PROXYING\_NOT\_SUPPORTED](#gga1ea81a365834e96f43ab7be573069d26a5f49a566d37b2cda0c624d76aee08bd1)   } |
|  | Set of response codes available for a response packet. [More...](#ga1ea81a365834e96f43ab7be573069d26) |
| enum | [coap\_content\_format](#ga94a8f9956742d3928fc3c63b8d01ae73) {     [COAP\_CONTENT\_FORMAT\_TEXT\_PLAIN](#gga94a8f9956742d3928fc3c63b8d01ae73af068aa8d09032352799bc60868607997) = 0 , [COAP\_CONTENT\_FORMAT\_APP\_LINK\_FORMAT](#gga94a8f9956742d3928fc3c63b8d01ae73a1fbd90fd5cb309e2de6954f46174dc4f) = 40 , [COAP\_CONTENT\_FORMAT\_APP\_XML](#gga94a8f9956742d3928fc3c63b8d01ae73adb96bf55e914f4852e92dc65752c372a) = 41 , [COAP\_CONTENT\_FORMAT\_APP\_OCTET\_STREAM](#gga94a8f9956742d3928fc3c63b8d01ae73a88d952174bb3e4ffb9ab11a599952760) = 42 ,     [COAP\_CONTENT\_FORMAT\_APP\_EXI](#gga94a8f9956742d3928fc3c63b8d01ae73a483a382550b38468cc66bdce9f4743ea) = 47 , [COAP\_CONTENT\_FORMAT\_APP\_JSON](#gga94a8f9956742d3928fc3c63b8d01ae73a975381d286c1e9b998e41ef0a234d17a) = 50 , [COAP\_CONTENT\_FORMAT\_APP\_JSON\_PATCH\_JSON](#gga94a8f9956742d3928fc3c63b8d01ae73a141f183724ad6da14c3992c0990d6239) = 51 , [COAP\_CONTENT\_FORMAT\_APP\_MERGE\_PATCH\_JSON](#gga94a8f9956742d3928fc3c63b8d01ae73a2797149fb3811d706dab291e9edc9436) = 52 ,     [COAP\_CONTENT\_FORMAT\_APP\_CBOR](#gga94a8f9956742d3928fc3c63b8d01ae73a7ca73ff57a6c7fb1517b44f2ce17d3f9) = 60   } |
|  | Set of Content-Format option values for CoAP. [More...](#ga94a8f9956742d3928fc3c63b8d01ae73) |
| enum | [coap\_no\_response](#ga2a323287262bbb6a4932e7911ddb652c) { [COAP\_NO\_RESPONSE\_SUPPRESS\_2\_XX](#gga2a323287262bbb6a4932e7911ddb652caeeb51bb18780c20df5b25183d52d42de) = 0x02 , [COAP\_NO\_RESPONSE\_SUPPRESS\_4\_XX](#gga2a323287262bbb6a4932e7911ddb652cae8b0b1231d095b3e7a972ca4c86d8dce) = 0x08 , [COAP\_NO\_RESPONSE\_SUPPRESS\_5\_XX](#gga2a323287262bbb6a4932e7911ddb652ca19ebfb46899b440124322bb67c906cb3) = 0x10 , [COAP\_NO\_RESPONSE\_SUPPRESS\_ALL](#gga2a323287262bbb6a4932e7911ddb652ca21758021d7f3a36bf6ede06daa82dbf0) } |
|  | Set of No-Response option values for CoAP. [More...](#ga2a323287262bbb6a4932e7911ddb652c) |
| enum | [coap\_block\_size](#ga712c1468f936a3af7dc39a86a5961922) {     [COAP\_BLOCK\_16](#gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968) , [COAP\_BLOCK\_32](#gga712c1468f936a3af7dc39a86a5961922a1aaf8f841c18e281b176793bb331993d) , [COAP\_BLOCK\_64](#gga712c1468f936a3af7dc39a86a5961922a7266f448a391ea2a2763f1ded5397520) , [COAP\_BLOCK\_128](#gga712c1468f936a3af7dc39a86a5961922a147ddf4b0e5d1a8c11f0da2c71dee4d8) ,     [COAP\_BLOCK\_256](#gga712c1468f936a3af7dc39a86a5961922acfc37f84eabccdde4bd84b06c6a5e753) , [COAP\_BLOCK\_512](#gga712c1468f936a3af7dc39a86a5961922ad2052905aff08c58585dcf6c6caddc19) , [COAP\_BLOCK\_1024](#gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce)   } |
|  | Represents the size of each block that will be transferred using block-wise transfers [RFC7959]: [More...](#ga712c1468f936a3af7dc39a86a5961922) |

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [coap\_header\_get\_version](#gafd01c39fac8f173edc04337161e92264) (const struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Returns the version present in a CoAP packet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [coap\_header\_get\_type](#gaed883ea6cec3acc5eb570e152dc52e25) (const struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Returns the type of the CoAP packet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [coap\_header\_get\_token](#ga6a5049accfa0cd7106a3a6593c598545) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token) |
|  | Returns the token (if any) in the CoAP packet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [coap\_header\_get\_code](#gae4bf952fdf9e3d03ab0b0df4c3c0d054) (const struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Returns the code of the CoAP packet. |
| int | [coap\_header\_set\_code](#gafdaecca5ad26bab4fb7c9ee3477318f8) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code) |
|  | Modifies the code of the CoAP packet. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [coap\_header\_get\_id](#ga63388c629da5370d2e711cdc9aabd837) (const struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Returns the message id associated with the CoAP packet. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [coap\_packet\_get\_payload](#ga28ccf00fb1f5f13f747e61c2e3008b5c) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*len) |
|  | Returns the data pointer and length of the CoAP packet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_uri\_path\_match](#ga8b621232b740d8e8e1771fba24897121) (const char \*const \*path, struct [coap\_option](structcoap__option.md) \*options, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num) |
|  | Verify if CoAP URI path matches with provided options. |
| int | [coap\_packet\_parse](#ga27a58a69f632551aa7a2394ae2badacf) (struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, struct [coap\_option](structcoap__option.md) \*options, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num) |
|  | Parses the CoAP packet in data, validating it and initializing *cpkt*. |
| int | [coap\_packet\_set\_path](#gab8f9e9cdfa20920d5d25fb1507a2286d) (struct [coap\_packet](structcoap__packet.md) \*cpkt, const char \*path) |
|  | Parses provided coap path (with/without query) or query and appends that as options to the *cpkt*. |
| int | [coap\_packet\_init](#ga90e6aab174f8977f0a3b5fbe1a20297c) (struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ver, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | Creates a new CoAP Packet from input data. |
| int | [coap\_ack\_init](#gae6d93b1f93734302be75ee417813e5d1) (struct [coap\_packet](structcoap__packet.md) \*cpkt, const struct [coap\_packet](structcoap__packet.md) \*req, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code) |
|  | Create a new CoAP Acknowledgment message for given request. |
| int | [coap\_rst\_init](#ga9626781d73d18c1305f654ef4723e5db) (struct [coap\_packet](structcoap__packet.md) \*cpkt, const struct [coap\_packet](structcoap__packet.md) \*req, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_len) |
|  | Create a new CoAP Reset message for given request. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [coap\_next\_token](#ga66f986f8a1157236bea27133c2a2538b) (void) |
|  | Returns a randomly generated array of 8 bytes, that can be used as a message's token. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [coap\_next\_id](#gade5f4995c6419db03ce3e7ff7ca1cfcb) (void) |
|  | Helper to generate message ids. |
| int | [coap\_find\_options](#gaf006c8048ed7b863e70dbdd64bc3d608) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, struct [coap\_option](structcoap__option.md) \*options, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) veclen) |
|  | Return the values associated with the option of value *code*. |
| int | [coap\_packet\_append\_option](#ga2aa4140ee83ca4090a5604e34d1f1446) (struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Appends an option to the packet. |
| int | [coap\_packet\_remove\_option](#gaca300a216781d360d2cd64e8e9f1ae8f) (struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code) |
|  | Remove an option from the packet. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [coap\_option\_value\_to\_int](#ga2fd0613e61274ec4b9b7bab3ab11ccce) (const struct [coap\_option](structcoap__option.md) \*option) |
|  | Converts an option to its integer representation. |
| int | [coap\_append\_option\_int](#ga6bec94992ac450dca03436a6ad74efb4) (struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int val) |
|  | Appends an integer value option to the packet. |
| int | [coap\_packet\_append\_payload\_marker](#ga24000def8534acdcd2c61836dc690367) (struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Append payload marker to CoAP packet. |
| int | [coap\_packet\_append\_payload](#gadcd3a93a702a2a0b428f39b71dd67954) (struct [coap\_packet](structcoap__packet.md) \*cpkt, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) payload\_len) |
|  | Append payload to CoAP packet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_packet\_is\_request](#ga323644931c927b8988aafd89dacb993c) (const struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Check if a CoAP packet is a CoAP request. |
| int | [coap\_handle\_request\_len](#ga864a95bd0d095070200494c630f7e147) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_resource](structcoap__resource.md) \*resources, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) resources\_len, struct [coap\_option](structcoap__option.md) \*options, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len) |
|  | When a request is received, call the appropriate methods of the matching resources. |
| int | [coap\_handle\_request](#ga88a5f2c3915ef109eadfebaf82b53186) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_resource](structcoap__resource.md) \*resources, struct [coap\_option](structcoap__option.md) \*options, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len) |
|  | When a request is received, call the appropriate methods of the matching resources. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [coap\_block\_size\_to\_bytes](#gafffadd4a837e48fd72af20468ccd86f2) (enum [coap\_block\_size](#ga712c1468f936a3af7dc39a86a5961922) block\_size) |
|  | Helper for converting the enumeration to the size expressed in bytes. |
| static enum [coap\_block\_size](#ga712c1468f936a3af7dc39a86a5961922) | [coap\_bytes\_to\_block\_size](#ga27e3008b8511333e0c0115ba928017f3) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bytes) |
|  | Helper for converting block size in bytes to enumeration. |
| int | [coap\_block\_transfer\_init](#ga57486e764f0feb6544fa3b0d19935afd) (struct [coap\_block\_context](structcoap__block__context.md) \*ctx, enum [coap\_block\_size](#ga712c1468f936a3af7dc39a86a5961922) block\_size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) total\_size) |
|  | Initializes the context of a block-wise transfer. |
| int | [coap\_append\_descriptive\_block\_option](#ga8b5966a29054ace04cae81d4da588e72) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Append BLOCK1 or BLOCK2 option to the packet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_has\_descriptive\_block\_option](#gaabdfa8cf28cc2c3a14ae0af5fa7e7212) (struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Check if a descriptive block option is set in the packet. |
| int | [coap\_remove\_descriptive\_block\_option](#ga941ee9d68f1a628755aa79c249cbae58) (struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Remove BLOCK1 or BLOCK2 option from the packet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_block\_has\_more](#gafc61a6878d82f81565ab752ced0ce2be) (struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Check if BLOCK1 or BLOCK2 option has more flag set. |
| int | [coap\_append\_block1\_option](#ga518d5f4422ff45f2b4a296f249da89cd) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Append BLOCK1 option to the packet. |
| int | [coap\_append\_block2\_option](#ga361c17b698bdaa0fc529b7338efefd8c) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Append BLOCK2 option to the packet. |
| int | [coap\_append\_size1\_option](#ga3f66d5935dcacfeebcac2b3001d7b57a) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Append SIZE1 option to the packet. |
| int | [coap\_append\_size2\_option](#gafbc8c15ef03b762f9411c38b03aa403b) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Append SIZE2 option to the packet. |
| int | [coap\_get\_option\_int](#ga21b8f4ffeecc7900f6bf299836d2b5b3) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code) |
|  | Get the integer representation of a CoAP option. |
| int | [coap\_get\_block1\_option](#ga10c4a0d7e2052f3116fbf3b355fe75db) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*has\_more, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*block\_number) |
|  | Get the block size, more flag and block number from the CoAP block1 option. |
| int | [coap\_get\_block2\_option](#ga196390e6f016b72b3ae2ae9e69bed1b7) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*has\_more, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*block\_number) |
|  | Get values from CoAP block2 option. |
| int | [coap\_update\_from\_block](#ga3b0cc9bfabdddeffd98f36d7f15dd416) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Retrieves BLOCK{1,2} and SIZE{1,2} from *cpkt* and updates *ctx* accordingly. |
| int | [coap\_next\_block\_for\_option](#ga50f7837da003601479dbc470ba9898ae) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx, enum [coap\_option\_num](#ga7b8b3041e2f4ae26e663ff7431a6e6e3) option) |
|  | Updates *ctx* according to *option* set in *cpkt* so after this is called the current entry indicates the correct offset in the body of data being transferred. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [coap\_next\_block](#ga1244716ecf06fad1013131c42eab8c5c) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Updates *ctx* so after this is called the current entry indicates the correct offset in the body of data being transferred. |
| void | [coap\_observer\_init](#ga3d720b0d222cc35ce56cc260df1609a3) (struct [coap\_observer](structcoap__observer.md) \*observer, const struct [coap\_packet](structcoap__packet.md) \*request, const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Indicates that the remote device referenced by *addr*, with *request*, wants to observe a resource. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_register\_observer](#ga3c42861f8442e548f560acf3deca6baa) (struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_observer](structcoap__observer.md) \*observer) |
|  | After the observer is initialized, associate the observer with an resource. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_remove\_observer](#ga33c351ac06b5ae9217cd53d8cf330fbd) (struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_observer](structcoap__observer.md) \*observer) |
|  | Remove this observer from the list of registered observers of that resource. |
| struct [coap\_observer](structcoap__observer.md) \* | [coap\_find\_observer](#gaf9c1a55aee52588df2694ea947db5db4) (struct [coap\_observer](structcoap__observer.md) \*observers, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [sockaddr](structsockaddr.md) \*addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len) |
|  | Returns the observer that matches address *addr* and has token *token*. |
| struct [coap\_observer](structcoap__observer.md) \* | [coap\_find\_observer\_by\_addr](#ga427167161529c24f5cf8c9ed2023e321) (struct [coap\_observer](structcoap__observer.md) \*observers, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Returns the observer that matches address *addr*. |
| struct [coap\_observer](structcoap__observer.md) \* | [coap\_find\_observer\_by\_token](#gadeaa59fd7b6eab454d5930289b4e08f7) (struct [coap\_observer](structcoap__observer.md) \*observers, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len) |
|  | Returns the observer that has token *token*. |
| struct [coap\_observer](structcoap__observer.md) \* | [coap\_observer\_next\_unused](#ga2410e973bf3192244426df346230608b) (struct [coap\_observer](structcoap__observer.md) \*observers, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Returns the next available observer representation. |
| void | [coap\_reply\_init](#gacfe30c84434dc8adbf3d399ec0e51bec) (struct [coap\_reply](structcoap__reply.md) \*reply, const struct [coap\_packet](structcoap__packet.md) \*request) |
|  | Indicates that a reply is expected for *request*. |
| int | [coap\_pending\_init](#ga868f792abf555f01c28caa5413d9e84c) (struct [coap\_pending](structcoap__pending.md) \*pending, const struct [coap\_packet](structcoap__packet.md) \*request, const struct [sockaddr](structsockaddr.md) \*addr, const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params) |
|  | Initialize a pending request with a request. |
| struct [coap\_pending](structcoap__pending.md) \* | [coap\_pending\_next\_unused](#ga800831ddfe19b1a5637a5edd9e78c470) (struct [coap\_pending](structcoap__pending.md) \*pendings, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Returns the next available pending struct, that can be used to track the retransmission status of a request. |
| struct [coap\_reply](structcoap__reply.md) \* | [coap\_reply\_next\_unused](#ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e) (struct [coap\_reply](structcoap__reply.md) \*replies, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Returns the next available reply struct, so it can be used to track replies and notifications received. |
| struct [coap\_pending](structcoap__pending.md) \* | [coap\_pending\_received](#ga94ceba78cbd2440f91d9b30d6b06594d) (const struct [coap\_packet](structcoap__packet.md) \*response, struct [coap\_pending](structcoap__pending.md) \*pendings, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | After a response is received, returns if there is any matching pending request exits. |
| struct [coap\_reply](structcoap__reply.md) \* | [coap\_response\_received](#ga3da23a809504025a24bf03daea3e606b) (const struct [coap\_packet](structcoap__packet.md) \*response, const struct [sockaddr](structsockaddr.md) \*from, struct [coap\_reply](structcoap__reply.md) \*replies, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | After a response is received, call [coap\_reply\_t](#ga556deaf757f3047eefc2f032d0d7e0bc) handler registered in [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structure. |
| struct [coap\_pending](structcoap__pending.md) \* | [coap\_pending\_next\_to\_expire](#ga9d63518c701ebdb4c7f65c5368d00d27) (struct [coap\_pending](structcoap__pending.md) \*pendings, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Returns the next pending about to expire, pending->timeout informs how many ms to next expiration. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_pending\_cycle](#ga2bcfc7340ed2347862b0f003e1b00a4b) (struct [coap\_pending](structcoap__pending.md) \*pending) |
|  | After a request is sent, user may want to cycle the pending retransmission so the timeout is updated. |
| void | [coap\_pending\_clear](#ga03287eb3187aa28e0e83e0e0c72e2631) (struct [coap\_pending](structcoap__pending.md) \*pending) |
|  | Cancels the pending retransmission, so it again becomes available. |
| void | [coap\_pendings\_clear](#ga6e0947048052e733a3571fdc8955b2d7) (struct [coap\_pending](structcoap__pending.md) \*pendings, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Cancels all pending retransmissions, so they become available again. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [coap\_pendings\_count](#gad9db2ced9b882265c16e3039f893ca03) (struct [coap\_pending](structcoap__pending.md) \*pendings, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Count number of pending requests. |
| void | [coap\_reply\_clear](#ga37b58c38c150751d31207ece416529d8) (struct [coap\_reply](structcoap__reply.md) \*reply) |
|  | Cancels awaiting for this reply, so it becomes available again. |
| void | [coap\_replies\_clear](#gaddb02509934f5bac20b7c7f83aea4cd8) (struct [coap\_reply](structcoap__reply.md) \*replies, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Cancels all replies, so they become available again. |
| int | [coap\_resource\_notify](#gad0c738d308f9cca8ea5cdb79449282cb) (struct [coap\_resource](structcoap__resource.md) \*resource) |
|  | Indicates that this resource was updated and that the *notify* callback should be called for every registered observer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_request\_is\_observe](#ga46b315c30b642eec65bcb84e9c937ee7) (const struct [coap\_packet](structcoap__packet.md) \*request) |
|  | Returns if this request is enabling observing a resource. |
| struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) | [coap\_get\_transmission\_parameters](#ga1bd7be0a5390f0599e7bec0cbd79daf8) (void) |
|  | Get currently active CoAP transmission parameters. |
| void | [coap\_set\_transmission\_parameters](#gaf361fd233f1aa650650108ae1e205ede) (const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params) |
|  | Set CoAP transmission parameters. |
| int | [coap\_well\_known\_core\_get](#ga3f2eded87dbeb7408ff6f07e04afb30b) (struct [coap\_resource](structcoap__resource.md) \*resource, const struct [coap\_packet](structcoap__packet.md) \*request, struct [coap\_packet](structcoap__packet.md) \*response, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len) |
|  | Build a CoAP response for a .well-known/core CoAP request. |
| int | [coap\_well\_known\_core\_get\_len](#ga49d63f12b593d7509690a504b05da730) (struct [coap\_resource](structcoap__resource.md) \*resources, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) resources\_len, const struct [coap\_packet](structcoap__packet.md) \*request, struct [coap\_packet](structcoap__packet.md) \*response, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len) |
|  | Build a CoAP response for a .well-known/core CoAP request. |

## Detailed Description

COAP library.

Since
:   1.10

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#gabdcc1f443e89bd035522cbab7dfee879)COAP\_MAKE\_RESPONSE\_CODE

| #define COAP\_MAKE\_RESPONSE\_CODE | ( |  | *class*, |
| --- | --- | --- | --- |
|  |  |  | *det* ) |

`#include <[coap.h](coap_8h.md)>`

**Value:**

((class << 5) | (det))

Utility macro to create a CoAP response code.

Parameters
:   | class | Class of the response code (ex. 2, 4, 5, ...) |
    | --- | --- |
    | det | Detail of the response code |

Returns
:   Response code literal

## [◆ ](#ga09d2c727fc6fc76aa9d908b759a3f40b)COAP\_WELL\_KNOWN\_CORE\_PATH

| #define COAP\_WELL\_KNOWN\_CORE\_PATH   ((const char \* const[]) { ".well-known", "core", [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) }) |
| --- |

`#include <[coap_link_format.h](coap__link__format_8h.md)>`

This resource should be added before all other resources that should be included in the responses of the .well-known/core resource if is to be used with coap\_well\_known\_core\_get.

## Typedef Documentation

## [◆ ](#gaa509d49f06101342908a71f2f18f18fc)coap\_method\_t

| typedef int(\* coap\_method\_t) (struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_packet](structcoap__packet.md) \*request, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len) |
| --- |

`#include <[coap.h](coap_8h.md)>`

Type of the callback being called when a resource's method is invoked by the remote entity.

## [◆ ](#ga4180b2476430fbe4a5e0418fb628ea91)coap\_notify\_t

| typedef void(\* coap\_notify\_t) (struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_observer](structcoap__observer.md) \*observer) |
| --- |

`#include <[coap.h](coap_8h.md)>`

Type of the callback being called when a resource's has observers to be informed when an update happens.

## [◆ ](#ga556deaf757f3047eefc2f032d0d7e0bc)coap\_reply\_t

| typedef int(\* coap\_reply\_t) (const struct [coap\_packet](structcoap__packet.md) \*response, struct [coap\_reply](structcoap__reply.md) \*reply, const struct [sockaddr](structsockaddr.md) \*from) |
| --- |

`#include <[coap.h](coap_8h.md)>`

Helper function to be called when a response matches the a pending request.

When sending blocks, the callback is only executed when the reply of the last block is received. i.e. it is not called when the code of the reply is 'continue' (2.31).

## Enumeration Type Documentation

## [◆ ](#ga712c1468f936a3af7dc39a86a5961922)coap\_block\_size

| enum [coap\_block\_size](#ga712c1468f936a3af7dc39a86a5961922) |
| --- |

`#include <[coap.h](coap_8h.md)>`

Represents the size of each block that will be transferred using block-wise transfers [RFC7959]:

Each entry maps directly to the value that is used in the wire.

[https://tools.ietf.org/html/rfc7959](https://tools.ietf.org/html/rfc7959)

| Enumerator | |
| --- | --- |
| COAP\_BLOCK\_16 | 16-byte block size |
| COAP\_BLOCK\_32 | 32-byte block size |
| COAP\_BLOCK\_64 | 64-byte block size |
| COAP\_BLOCK\_128 | 128-byte block size |
| COAP\_BLOCK\_256 | 256-byte block size |
| COAP\_BLOCK\_512 | 512-byte block size |
| COAP\_BLOCK\_1024 | 1024-byte block size |

## [◆ ](#ga94a8f9956742d3928fc3c63b8d01ae73)coap\_content\_format

| enum [coap\_content\_format](#ga94a8f9956742d3928fc3c63b8d01ae73) |
| --- |

`#include <[coap.h](coap_8h.md)>`

Set of Content-Format option values for CoAP.

To be used when encoding or decoding a Content-Format option.

| Enumerator | |
| --- | --- |
| COAP\_CONTENT\_FORMAT\_TEXT\_PLAIN | text/plain;charset=utf-8 |
| COAP\_CONTENT\_FORMAT\_APP\_LINK\_FORMAT | application/link-format |
| COAP\_CONTENT\_FORMAT\_APP\_XML | application/xml |
| COAP\_CONTENT\_FORMAT\_APP\_OCTET\_STREAM | application/octet-stream |
| COAP\_CONTENT\_FORMAT\_APP\_EXI | application/exi |
| COAP\_CONTENT\_FORMAT\_APP\_JSON | application/json |
| COAP\_CONTENT\_FORMAT\_APP\_JSON\_PATCH\_JSON | application/json-patch+json |
| COAP\_CONTENT\_FORMAT\_APP\_MERGE\_PATCH\_JSON | application/merge-patch+json |
| COAP\_CONTENT\_FORMAT\_APP\_CBOR | application/cbor |

## [◆ ](#ga6a6547e3c755cf7a5033302c8294e0b7)coap\_method

| enum [coap\_method](#ga6a6547e3c755cf7a5033302c8294e0b7) |
| --- |

`#include <[coap.h](coap_8h.md)>`

Available request methods.

To be used when creating a request or a response.

| Enumerator | |
| --- | --- |
| COAP\_METHOD\_GET | GET. |
| COAP\_METHOD\_POST | POST. |
| COAP\_METHOD\_PUT | PUT. |
| COAP\_METHOD\_DELETE | DELETE. |
| COAP\_METHOD\_FETCH | FETCH. |
| COAP\_METHOD\_PATCH | PATCH. |
| COAP\_METHOD\_IPATCH | IPATCH. |

## [◆ ](#ga3b375b7580246d1266293d09902f3d9f)coap\_msgtype

| enum [coap\_msgtype](#ga3b375b7580246d1266293d09902f3d9f) |
| --- |

`#include <[coap.h](coap_8h.md)>`

CoAP packets may be of one of these types.

| Enumerator | |
| --- | --- |
| COAP\_TYPE\_CON | Confirmable message.  The packet is a request or response the destination end-point must acknowledge. |
| COAP\_TYPE\_NON\_CON | Non-confirmable message.  The packet is a request or response that doesn't require acknowledgements. |
| COAP\_TYPE\_ACK | Acknowledge.  Response to a confirmable message. |
| COAP\_TYPE\_RESET | Reset.  Rejecting a packet for any reason is done by sending a message of this type. |

## [◆ ](#ga2a323287262bbb6a4932e7911ddb652c)coap\_no\_response

| enum [coap\_no\_response](#ga2a323287262bbb6a4932e7911ddb652c) |
| --- |

`#include <[coap.h](coap_8h.md)>`

Set of No-Response option values for CoAP.

To be used when encoding or decoding a No-Response option defined in RFC 7967.

| Enumerator | |
| --- | --- |
| COAP\_NO\_RESPONSE\_SUPPRESS\_2\_XX |  |
| COAP\_NO\_RESPONSE\_SUPPRESS\_4\_XX |  |
| COAP\_NO\_RESPONSE\_SUPPRESS\_5\_XX |  |
| COAP\_NO\_RESPONSE\_SUPPRESS\_ALL |  |

## [◆ ](#ga7b8b3041e2f4ae26e663ff7431a6e6e3)coap\_option\_num

| enum [coap\_option\_num](#ga7b8b3041e2f4ae26e663ff7431a6e6e3) |
| --- |

`#include <[coap.h](coap_8h.md)>`

Set of CoAP packet options we are aware of.

Users may add options other than these to their packets, provided they know how to format them correctly. The only restriction is that all options must be added to a packet in numeric order.

Refer to RFC 7252, section 12.2 for more information.

| Enumerator | |
| --- | --- |
| COAP\_OPTION\_IF\_MATCH | If-Match. |
| COAP\_OPTION\_URI\_HOST | Uri-Host. |
| COAP\_OPTION\_ETAG | ETag. |
| COAP\_OPTION\_IF\_NONE\_MATCH | If-None-Match. |
| COAP\_OPTION\_OBSERVE | Observe (RFC 7641). |
| COAP\_OPTION\_URI\_PORT | Uri-Port. |
| COAP\_OPTION\_LOCATION\_PATH | Location-Path. |
| COAP\_OPTION\_URI\_PATH | Uri-Path. |
| COAP\_OPTION\_CONTENT\_FORMAT | Content-Format. |
| COAP\_OPTION\_MAX\_AGE | Max-Age. |
| COAP\_OPTION\_URI\_QUERY | Uri-Query. |
| COAP\_OPTION\_ACCEPT | Accept. |
| COAP\_OPTION\_LOCATION\_QUERY | Location-Query. |
| COAP\_OPTION\_BLOCK2 | Block2 (RFC 7959). |
| COAP\_OPTION\_BLOCK1 | Block1 (RFC 7959). |
| COAP\_OPTION\_SIZE2 | Size2 (RFC 7959). |
| COAP\_OPTION\_PROXY\_URI | Proxy-Uri. |
| COAP\_OPTION\_PROXY\_SCHEME | Proxy-Scheme. |
| COAP\_OPTION\_SIZE1 | Size1. |
| COAP\_OPTION\_ECHO | Echo (RFC 9175). |
| COAP\_OPTION\_NO\_RESPONSE | No-Response (RFC 7967). |
| COAP\_OPTION\_REQUEST\_TAG | Request-Tag (RFC 9175). |

## [◆ ](#ga1ea81a365834e96f43ab7be573069d26)coap\_response\_code

| enum [coap\_response\_code](#ga1ea81a365834e96f43ab7be573069d26) |
| --- |

`#include <[coap.h](coap_8h.md)>`

Set of response codes available for a response packet.

To be used when creating a response.

| Enumerator | |
| --- | --- |
| COAP\_RESPONSE\_CODE\_OK | 2.00 - OK |
| COAP\_RESPONSE\_CODE\_CREATED | 2.01 - Created |
| COAP\_RESPONSE\_CODE\_DELETED | 2.02 - Deleted |
| COAP\_RESPONSE\_CODE\_VALID | 2.03 - Valid |
| COAP\_RESPONSE\_CODE\_CHANGED | 2.04 - Changed |
| COAP\_RESPONSE\_CODE\_CONTENT | 2.05 - Content |
| COAP\_RESPONSE\_CODE\_CONTINUE | 2.31 - Continue |
| COAP\_RESPONSE\_CODE\_BAD\_REQUEST | 4.00 - Bad Request |
| COAP\_RESPONSE\_CODE\_UNAUTHORIZED | 4.01 - Unauthorized |
| COAP\_RESPONSE\_CODE\_BAD\_OPTION | 4.02 - Bad Option |
| COAP\_RESPONSE\_CODE\_FORBIDDEN | 4.03 - Forbidden |
| COAP\_RESPONSE\_CODE\_NOT\_FOUND | 4.04 - Not Found |
| COAP\_RESPONSE\_CODE\_NOT\_ALLOWED | 4.05 - Method Not Allowed |
| COAP\_RESPONSE\_CODE\_NOT\_ACCEPTABLE | 4.06 - Not Acceptable |
| COAP\_RESPONSE\_CODE\_INCOMPLETE | 4.08 - Request Entity Incomplete |
| COAP\_RESPONSE\_CODE\_CONFLICT | 4.12 - Precondition Failed |
| COAP\_RESPONSE\_CODE\_PRECONDITION\_FAILED | 4.12 - Precondition Failed |
| COAP\_RESPONSE\_CODE\_REQUEST\_TOO\_LARGE | 4.13 - Request Entity Too Large |
| COAP\_RESPONSE\_CODE\_UNSUPPORTED\_CONTENT\_FORMAT | 4.15 - Unsupported Content-Format |
| COAP\_RESPONSE\_CODE\_UNPROCESSABLE\_ENTITY | 4.22 - Unprocessable Entity |
| COAP\_RESPONSE\_CODE\_TOO\_MANY\_REQUESTS | 4.29 - Too Many Requests |
| COAP\_RESPONSE\_CODE\_INTERNAL\_ERROR | 5.00 - Internal Server Error |
| COAP\_RESPONSE\_CODE\_NOT\_IMPLEMENTED | 5.01 - Not Implemented |
| COAP\_RESPONSE\_CODE\_BAD\_GATEWAY | 5.02 - Bad Gateway |
| COAP\_RESPONSE\_CODE\_SERVICE\_UNAVAILABLE | 5.03 - Service Unavailable |
| COAP\_RESPONSE\_CODE\_GATEWAY\_TIMEOUT | 5.04 - Gateway Timeout |
| COAP\_RESPONSE\_CODE\_PROXYING\_NOT\_SUPPORTED | 5.05 - Proxying Not Supported |

## Function Documentation

## [◆ ](#gae6d93b1f93734302be75ee417813e5d1)coap\_ack\_init()

| int coap\_ack\_init | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | const struct [coap\_packet](structcoap__packet.md) \* | *req*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *max\_len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *code* ) |

`#include <[coap.h](coap_8h.md)>`

Create a new CoAP Acknowledgment message for given request.

This function works like [coap\_packet\_init](#ga90e6aab174f8977f0a3b5fbe1a20297c), filling CoAP header type, CoAP header token, and CoAP header message id fields according to acknowledgment rules.

Parameters
:   | cpkt | New packet to be initialized using the storage from *data*. |
    | --- | --- |
    | req | CoAP request packet that is being acknowledged |
    | data | Data that will contain a CoAP packet information |
    | max\_len | Maximum allowable length of data |
    | code | CoAP header code |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga518d5f4422ff45f2b4a296f249da89cd)coap\_append\_block1\_option()

| int coap\_append\_block1\_option | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_block\_context](structcoap__block__context.md) \* | *ctx* ) |

`#include <[coap.h](coap_8h.md)>`

Append BLOCK1 option to the packet.

Parameters
:   | cpkt | Packet to be updated |
    | --- | --- |
    | ctx | Block context from which to retrieve the information for the Block1 option |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga361c17b698bdaa0fc529b7338efefd8c)coap\_append\_block2\_option()

| int coap\_append\_block2\_option | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_block\_context](structcoap__block__context.md) \* | *ctx* ) |

`#include <[coap.h](coap_8h.md)>`

Append BLOCK2 option to the packet.

Parameters
:   | cpkt | Packet to be updated |
    | --- | --- |
    | ctx | Block context from which to retrieve the information for the Block2 option |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga8b5966a29054ace04cae81d4da588e72)coap\_append\_descriptive\_block\_option()

| int coap\_append\_descriptive\_block\_option | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_block\_context](structcoap__block__context.md) \* | *ctx* ) |

`#include <[coap.h](coap_8h.md)>`

Append BLOCK1 or BLOCK2 option to the packet.

If the CoAP packet is a request then BLOCK1 is appended otherwise BLOCK2 is appended.

Parameters
:   | cpkt | Packet to be updated |
    | --- | --- |
    | ctx | Block context from which to retrieve the information for the block option |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga6bec94992ac450dca03436a6ad74efb4)coap\_append\_option\_int()

| int coap\_append\_option\_int | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *code*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *val* ) |

`#include <[coap.h](coap_8h.md)>`

Appends an integer value option to the packet.

The option must be added in numeric order of their codes, and the least amount of bytes will be used to encode the value.

Parameters
:   | cpkt | Packet to be updated |
    | --- | --- |
    | code | Option code to add to the packet, see [coap\_option\_num](#ga7b8b3041e2f4ae26e663ff7431a6e6e3) |
    | val | Integer value to be added |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga3f66d5935dcacfeebcac2b3001d7b57a)coap\_append\_size1\_option()

| int coap\_append\_size1\_option | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_block\_context](structcoap__block__context.md) \* | *ctx* ) |

`#include <[coap.h](coap_8h.md)>`

Append SIZE1 option to the packet.

Parameters
:   | cpkt | Packet to be updated |
    | --- | --- |
    | ctx | Block context from which to retrieve the information for the Size1 option |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#gafbc8c15ef03b762f9411c38b03aa403b)coap\_append\_size2\_option()

| int coap\_append\_size2\_option | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_block\_context](structcoap__block__context.md) \* | *ctx* ) |

`#include <[coap.h](coap_8h.md)>`

Append SIZE2 option to the packet.

Parameters
:   | cpkt | Packet to be updated |
    | --- | --- |
    | ctx | Block context from which to retrieve the information for the Size2 option |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#gafc61a6878d82f81565ab752ced0ce2be)coap\_block\_has\_more()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coap\_block\_has\_more | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Check if BLOCK1 or BLOCK2 option has more flag set.

Parameters
:   | cpkt | Packet to be checked. |
    | --- | --- |

Returns
:   true If more flag is set in BLOCK1 or BLOCK2
:   false If MORE flag is not set or BLOCK header not found.

## [◆ ](#gafffadd4a837e48fd72af20468ccd86f2)coap\_block\_size\_to\_bytes()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_block\_size\_to\_bytes | ( | enum [coap\_block\_size](#ga712c1468f936a3af7dc39a86a5961922) | *block\_size* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Helper for converting the enumeration to the size expressed in bytes.

Parameters
:   | block\_size | The block size to be converted |
    | --- | --- |

Returns
:   The size in bytes that the block\_size represents

## [◆ ](#ga57486e764f0feb6544fa3b0d19935afd)coap\_block\_transfer\_init()

| int coap\_block\_transfer\_init | ( | struct [coap\_block\_context](structcoap__block__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | enum [coap\_block\_size](#ga712c1468f936a3af7dc39a86a5961922) | *block\_size*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *total\_size* ) |

`#include <[coap.h](coap_8h.md)>`

Initializes the context of a block-wise transfer.

Parameters
:   | ctx | The context to be initialized |
    | --- | --- |
    | block\_size | The size of the block |
    | total\_size | The total size of the transfer, if known |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga27e3008b8511333e0c0115ba928017f3)coap\_bytes\_to\_block\_size()

| | enum [coap\_block\_size](#ga712c1468f936a3af7dc39a86a5961922) coap\_bytes\_to\_block\_size | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *bytes* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Helper for converting block size in bytes to enumeration.

NOTE: Only valid CoAP block sizes map correctly.

Parameters
:   | bytes | CoAP block size in bytes. |
    | --- | --- |

Returns
:   enum [coap\_block\_size](#ga712c1468f936a3af7dc39a86a5961922)

## [◆ ](#gaf9c1a55aee52588df2694ea947db5db4)coap\_find\_observer()

| struct [coap\_observer](structcoap__observer.md) \* coap\_find\_observer | ( | struct [coap\_observer](structcoap__observer.md) \* | *observers*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *token*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *token\_len* ) |

`#include <[coap.h](coap_8h.md)>`

Returns the observer that matches address *addr* and has token *token*.

Parameters
:   | observers | Pointer to the array of observers |
    | --- | --- |
    | len | Size of the array of observers |
    | addr | Address of the endpoint observing a resource |
    | token | Pointer to the token |
    | token\_len | Length of valid bytes in the token |

Returns
:   A pointer to a observer if a match is found, NULL otherwise.

## [◆ ](#ga427167161529c24f5cf8c9ed2023e321)coap\_find\_observer\_by\_addr()

| struct [coap\_observer](structcoap__observer.md) \* coap\_find\_observer\_by\_addr | ( | struct [coap\_observer](structcoap__observer.md) \* | *observers*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr* ) |

`#include <[coap.h](coap_8h.md)>`

Returns the observer that matches address *addr*.

Parameters
:   | observers | Pointer to the array of observers |
    | --- | --- |
    | len | Size of the array of observers |
    | addr | Address of the endpoint observing a resource |

Note
:   The function [coap\_find\_observer()](#gaf9c1a55aee52588df2694ea947db5db4) should be preferred if both the observer's address and token are known.

Returns
:   A pointer to a observer if a match is found, NULL otherwise.

## [◆ ](#gadeaa59fd7b6eab454d5930289b4e08f7)coap\_find\_observer\_by\_token()

| struct [coap\_observer](structcoap__observer.md) \* coap\_find\_observer\_by\_token | ( | struct [coap\_observer](structcoap__observer.md) \* | *observers*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *token*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *token\_len* ) |

`#include <[coap.h](coap_8h.md)>`

Returns the observer that has token *token*.

Parameters
:   | observers | Pointer to the array of observers |
    | --- | --- |
    | len | Size of the array of observers |
    | token | Pointer to the token |
    | token\_len | Length of valid bytes in the token |

Note
:   The function [coap\_find\_observer()](#gaf9c1a55aee52588df2694ea947db5db4) should be preferred if both the observer's address and token are known.

Returns
:   A pointer to a observer if a match is found, NULL otherwise.

## [◆ ](#gaf006c8048ed7b863e70dbdd64bc3d608)coap\_find\_options()

| int coap\_find\_options | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *code*, |
|  |  | struct [coap\_option](structcoap__option.md) \* | *options*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *veclen* ) |

`#include <[coap.h](coap_8h.md)>`

Return the values associated with the option of value *code*.

Parameters
:   | cpkt | CoAP packet representation |
    | --- | --- |
    | code | Option number to look for |
    | options | Array of [coap\_option](structcoap__option.md "Representation of a CoAP option.") where to store the value of the options found |
    | veclen | Number of elements in the options array |

Returns
:   The number of options found in packet matching code, negative on error.

## [◆ ](#ga10c4a0d7e2052f3116fbf3b355fe75db)coap\_get\_block1\_option()

| int coap\_get\_block1\_option | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *has\_more*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *block\_number* ) |

`#include <[coap.h](coap_8h.md)>`

Get the block size, more flag and block number from the CoAP block1 option.

Parameters
:   | cpkt | Packet to be inspected |
    | --- | --- |
    | has\_more | Is set to the value of the more flag |
    | block\_number | Is set to the number of the block |

Returns
:   Integer value of the block size in case of success or negative in case of error.

## [◆ ](#ga196390e6f016b72b3ae2ae9e69bed1b7)coap\_get\_block2\_option()

| int coap\_get\_block2\_option | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *has\_more*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *block\_number* ) |

`#include <[coap.h](coap_8h.md)>`

Get values from CoAP block2 option.

Decode block number, more flag and block size from option.

Parameters
:   | cpkt | Packet to be inspected |
    | --- | --- |
    | has\_more | Is set to the value of the more flag |
    | block\_number | Is set to the number of the block |

Returns
:   Integer value of the block size in case of success or negative in case of error.

## [◆ ](#ga21b8f4ffeecc7900f6bf299836d2b5b3)coap\_get\_option\_int()

| int coap\_get\_option\_int | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *code* ) |

`#include <[coap.h](coap_8h.md)>`

Get the integer representation of a CoAP option.

Parameters
:   | cpkt | Packet to be inspected |
    | --- | --- |
    | code | CoAP option code |

Returns
:   Integer value >= 0 in case of success or negative in case of error.

## [◆ ](#ga1bd7be0a5390f0599e7bec0cbd79daf8)coap\_get\_transmission\_parameters()

| struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) coap\_get\_transmission\_parameters | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Get currently active CoAP transmission parameters.

Returns
:   CoAP transmission parameters structure.

## [◆ ](#ga88a5f2c3915ef109eadfebaf82b53186)coap\_handle\_request()

| int coap\_handle\_request | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_resource](structcoap__resource.md) \* | *resources*, |
|  |  | struct [coap\_option](structcoap__option.md) \* | *options*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *opt\_num*, |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addr\_len* ) |

`#include <[coap.h](coap_8h.md)>`

When a request is received, call the appropriate methods of the matching resources.

Parameters
:   | cpkt | Packet received |
    | --- | --- |
    | resources | Array of known resources (terminated with empty resource) |
    | options | Parsed options from [coap\_packet\_parse()](#ga27a58a69f632551aa7a2394ae2badacf) |
    | opt\_num | Number of options |
    | addr | Peer address |
    | addr\_len | Peer address length |

Return values
:   | >= | 0 in case of success. |
    | --- | --- |
    | -ENOTSUP | in case of invalid request code. |
    | -EPERM | in case resource handler is not implemented. |
    | -ENOENT | in case the resource is not found. |

## [◆ ](#ga864a95bd0d095070200494c630f7e147)coap\_handle\_request\_len()

| int coap\_handle\_request\_len | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_resource](structcoap__resource.md) \* | *resources*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *resources\_len*, |
|  |  | struct [coap\_option](structcoap__option.md) \* | *options*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *opt\_num*, |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addr\_len* ) |

`#include <[coap.h](coap_8h.md)>`

When a request is received, call the appropriate methods of the matching resources.

Parameters
:   | cpkt | Packet received |
    | --- | --- |
    | resources | Array of known resources |
    | resources\_len | Number of resources in the array |
    | options | Parsed options from [coap\_packet\_parse()](#ga27a58a69f632551aa7a2394ae2badacf) |
    | opt\_num | Number of options |
    | addr | Peer address |
    | addr\_len | Peer address length |

Return values
:   | >= | 0 in case of success. |
    | --- | --- |
    | -ENOTSUP | in case of invalid request code. |
    | -EPERM | in case resource handler is not implemented. |
    | -ENOENT | in case the resource is not found. |

## [◆ ](#gaabdfa8cf28cc2c3a14ae0af5fa7e7212)coap\_has\_descriptive\_block\_option()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coap\_has\_descriptive\_block\_option | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Check if a descriptive block option is set in the packet.

If the CoAP packet is a request then an available BLOCK1 option would be checked otherwise a BLOCK2 option would be checked.

Parameters
:   | cpkt | Packet to be checked. |
    | --- | --- |

Returns
:   true if the corresponding block option is set, false otherwise.

## [◆ ](#gae4bf952fdf9e3d03ab0b0df4c3c0d054)coap\_header\_get\_code()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_header\_get\_code | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Returns the code of the CoAP packet.

Parameters
:   | cpkt | CoAP packet representation |
    | --- | --- |

Returns
:   the code present in the packet

## [◆ ](#ga63388c629da5370d2e711cdc9aabd837)coap\_header\_get\_id()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_header\_get\_id | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Returns the message id associated with the CoAP packet.

Parameters
:   | cpkt | CoAP packet representation |
    | --- | --- |

Returns
:   the message id present in the packet

## [◆ ](#ga6a5049accfa0cd7106a3a6593c598545)coap\_header\_get\_token()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_header\_get\_token | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *token* ) |

`#include <[coap.h](coap_8h.md)>`

Returns the token (if any) in the CoAP packet.

Parameters
:   | cpkt | CoAP packet representation |
    | --- | --- |
    | token | Where to store the token, must point to a buffer containing at least COAP\_TOKEN\_MAX\_LEN bytes |

Returns
:   Token length in the CoAP packet (0 - COAP\_TOKEN\_MAX\_LEN).

## [◆ ](#gaed883ea6cec3acc5eb570e152dc52e25)coap\_header\_get\_type()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_header\_get\_type | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Returns the type of the CoAP packet.

Parameters
:   | cpkt | CoAP packet representation |
    | --- | --- |

Returns
:   the type of the packet

## [◆ ](#gafd01c39fac8f173edc04337161e92264)coap\_header\_get\_version()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) coap\_header\_get\_version | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Returns the version present in a CoAP packet.

Parameters
:   | cpkt | CoAP packet representation |
    | --- | --- |

Returns
:   the CoAP version in packet

## [◆ ](#gafdaecca5ad26bab4fb7c9ee3477318f8)coap\_header\_set\_code()

| int coap\_header\_set\_code | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *code* ) |

`#include <[coap.h](coap_8h.md)>`

Modifies the code of the CoAP packet.

Parameters
:   | cpkt | CoAP packet representation |
    | --- | --- |
    | code | CoAP code |

Returns
:   0 on success, -EINVAL on failure

## [◆ ](#ga1244716ecf06fad1013131c42eab8c5c)coap\_next\_block()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) coap\_next\_block | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_block\_context](structcoap__block__context.md) \* | *ctx* ) |

`#include <[coap.h](coap_8h.md)>`

Updates *ctx* so after this is called the current entry indicates the correct offset in the body of data being transferred.

Parameters
:   | cpkt | Packet in which to look for block-wise transfers options |
    | --- | --- |
    | ctx | Block context to be updated |

Returns
:   The offset in the block-wise transfer, 0 if the transfer has finished.

## [◆ ](#ga50f7837da003601479dbc470ba9898ae)coap\_next\_block\_for\_option()

| int coap\_next\_block\_for\_option | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_block\_context](structcoap__block__context.md) \* | *ctx*, |
|  |  | enum [coap\_option\_num](#ga7b8b3041e2f4ae26e663ff7431a6e6e3) | *option* ) |

`#include <[coap.h](coap_8h.md)>`

Updates *ctx* according to *option* set in *cpkt* so after this is called the current entry indicates the correct offset in the body of data being transferred.

Parameters
:   | cpkt | Packet in which to look for block-wise transfers options |
    | --- | --- |
    | ctx | Block context to be updated |
    | option | Either COAP\_OPTION\_BLOCK1 or COAP\_OPTION\_BLOCK2 |

Returns
:   The offset in the block-wise transfer, 0 if the transfer has finished or a negative value in case of an error.

## [◆ ](#gade5f4995c6419db03ce3e7ff7ca1cfcb)coap\_next\_id()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coap\_next\_id | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Helper to generate message ids.

Returns
:   a new message id

## [◆ ](#ga66f986f8a1157236bea27133c2a2538b)coap\_next\_token()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* coap\_next\_token | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Returns a randomly generated array of 8 bytes, that can be used as a message's token.

Returns
:   a 8-byte pseudo-random token.

## [◆ ](#ga3d720b0d222cc35ce56cc260df1609a3)coap\_observer\_init()

| void coap\_observer\_init | ( | struct [coap\_observer](structcoap__observer.md) \* | *observer*, |
| --- | --- | --- | --- |
|  |  | const struct [coap\_packet](structcoap__packet.md) \* | *request*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr* ) |

`#include <[coap.h](coap_8h.md)>`

Indicates that the remote device referenced by *addr*, with *request*, wants to observe a resource.

Parameters
:   | observer | Observer to be initialized |
    | --- | --- |
    | request | Request on which the observer will be based |
    | addr | Address of the remote device |

## [◆ ](#ga2410e973bf3192244426df346230608b)coap\_observer\_next\_unused()

| struct [coap\_observer](structcoap__observer.md) \* coap\_observer\_next\_unused | ( | struct [coap\_observer](structcoap__observer.md) \* | *observers*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[coap.h](coap_8h.md)>`

Returns the next available observer representation.

Parameters
:   | observers | Pointer to the array of observers |
    | --- | --- |
    | len | Size of the array of observers |

Returns
:   A pointer to a observer if there's an available observer, NULL otherwise.

## [◆ ](#ga2fd0613e61274ec4b9b7bab3ab11ccce)coap\_option\_value\_to\_int()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int coap\_option\_value\_to\_int | ( | const struct [coap\_option](structcoap__option.md) \* | *option* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Converts an option to its integer representation.

Assumes that the number is encoded in the network byte order in the option.

Parameters
:   | option | Pointer to the option value, retrieved by [coap\_find\_options()](#gaf006c8048ed7b863e70dbdd64bc3d608) |
    | --- | --- |

Returns
:   The integer representation of the option

## [◆ ](#ga2aa4140ee83ca4090a5604e34d1f1446)coap\_packet\_append\_option()

| int coap\_packet\_append\_option | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *code*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) |

`#include <[coap.h](coap_8h.md)>`

Appends an option to the packet.

Note: options can be added out of numeric order of their codes. But it's more efficient to add them in order.

Parameters
:   | cpkt | Packet to be updated |
    | --- | --- |
    | code | Option code to add to the packet, see [coap\_option\_num](#ga7b8b3041e2f4ae26e663ff7431a6e6e3) |
    | value | Pointer to the value of the option, will be copied to the packet |
    | len | Size of the data to be added |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#gadcd3a93a702a2a0b428f39b71dd67954)coap\_packet\_append\_payload()

| int coap\_packet\_append\_payload | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *payload*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *payload\_len* ) |

`#include <[coap.h](coap_8h.md)>`

Append payload to CoAP packet.

Parameters
:   | cpkt | Packet to append the payload |
    | --- | --- |
    | payload | CoAP packet payload |
    | payload\_len | CoAP packet payload len |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga24000def8534acdcd2c61836dc690367)coap\_packet\_append\_payload\_marker()

| int coap\_packet\_append\_payload\_marker | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Append payload marker to CoAP packet.

Parameters
:   | cpkt | Packet to append the payload marker (0xFF) |
    | --- | --- |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga28ccf00fb1f5f13f747e61c2e3008b5c)coap\_packet\_get\_payload()

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* coap\_packet\_get\_payload | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *len* ) |

`#include <[coap.h](coap_8h.md)>`

Returns the data pointer and length of the CoAP packet.

Parameters
:   | cpkt | CoAP packet representation |
    | --- | --- |
    | len | Total length of CoAP payload |

Returns
:   data pointer and length if payload exists NULL pointer and length set to 0 in case there is no payload

## [◆ ](#ga90e6aab174f8977f0a3b5fbe1a20297c)coap\_packet\_init()

| int coap\_packet\_init | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *max\_len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ver*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *type*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *token\_len*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *token*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *code*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id* ) |

`#include <[coap.h](coap_8h.md)>`

Creates a new CoAP Packet from input data.

Parameters
:   | cpkt | New packet to be initialized using the storage from *data*. |
    | --- | --- |
    | data | Data that will contain a CoAP packet information |
    | max\_len | Maximum allowable length of data |
    | ver | CoAP header version |
    | type | CoAP header type |
    | token\_len | CoAP header token length |
    | token | CoAP header token |
    | code | CoAP header code |
    | id | CoAP header message id |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga323644931c927b8988aafd89dacb993c)coap\_packet\_is\_request()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coap\_packet\_is\_request | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Check if a CoAP packet is a CoAP request.

Parameters
:   | cpkt | Packet to be checked. |
    | --- | --- |

Returns
:   true if the packet is a request, false otherwise.

## [◆ ](#ga27a58a69f632551aa7a2394ae2badacf)coap\_packet\_parse()

| int coap\_packet\_parse | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | struct [coap\_option](structcoap__option.md) \* | *options*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *opt\_num* ) |

`#include <[coap.h](coap_8h.md)>`

Parses the CoAP packet in data, validating it and initializing *cpkt*.

*data* must remain valid while *cpkt* is used.

Parameters
:   | cpkt | Packet to be initialized from received *data*. |
    | --- | --- |
    | data | Data containing a CoAP packet, its *data* pointer is positioned on the start of the CoAP packet. |
    | len | Length of the data |
    | options | Parse options and cache its details. |
    | opt\_num | Number of options |

Return values
:   | 0 | in case of success. |
    | --- | --- |
    | -EINVAL | in case of invalid input args. |
    | -EBADMSG | in case of malformed coap packet header. |
    | -EILSEQ | in case of malformed coap options. |

## [◆ ](#gaca300a216781d360d2cd64e8e9f1ae8f)coap\_packet\_remove\_option()

| int coap\_packet\_remove\_option | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *code* ) |

`#include <[coap.h](coap_8h.md)>`

Remove an option from the packet.

Parameters
:   | cpkt | Packet to be updated |
    | --- | --- |
    | code | Option code to remove from the packet, see [coap\_option\_num](#ga7b8b3041e2f4ae26e663ff7431a6e6e3) |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#gab8f9e9cdfa20920d5d25fb1507a2286d)coap\_packet\_set\_path()

| int coap\_packet\_set\_path | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | const char \* | *path* ) |

`#include <[coap.h](coap_8h.md)>`

Parses provided coap path (with/without query) or query and appends that as options to the *cpkt*.

Parameters
:   | cpkt | Packet to append path and query options for. |
    | --- | --- |
    | path | Null-terminated string of coap path, query or both. |

Return values
:   | 0 | in case of success or negative in case of error. |
    | --- | --- |

## [◆ ](#ga03287eb3187aa28e0e83e0e0c72e2631)coap\_pending\_clear()

| void coap\_pending\_clear | ( | struct [coap\_pending](structcoap__pending.md) \* | *pending* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Cancels the pending retransmission, so it again becomes available.

Parameters
:   | pending | Pending representation to be canceled |
    | --- | --- |

## [◆ ](#ga2bcfc7340ed2347862b0f003e1b00a4b)coap\_pending\_cycle()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coap\_pending\_cycle | ( | struct [coap\_pending](structcoap__pending.md) \* | *pending* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

After a request is sent, user may want to cycle the pending retransmission so the timeout is updated.

Parameters
:   | pending | Pending representation to have its timeout updated |
    | --- | --- |

Returns
:   false if this is the last retransmission.

## [◆ ](#ga868f792abf555f01c28caa5413d9e84c)coap\_pending\_init()

| int coap\_pending\_init | ( | struct [coap\_pending](structcoap__pending.md) \* | *pending*, |
| --- | --- | --- | --- |
|  |  | const struct [coap\_packet](structcoap__packet.md) \* | *request*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \* | *params* ) |

`#include <[coap.h](coap_8h.md)>`

Initialize a pending request with a request.

The request's fields are copied into the pending struct, so *request* doesn't have to live for as long as the pending struct lives, but "data" that needs to live for at least that long.

Parameters
:   | pending | Structure representing the waiting for a confirmation message, initialized with data from *request* |
    | --- | --- |
    | request | Message waiting for confirmation |
    | addr | Address to send the retransmission |
    | params | Pointer to the CoAP transmission parameters struct, or NULL to use default values |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga9d63518c701ebdb4c7f65c5368d00d27)coap\_pending\_next\_to\_expire()

| struct [coap\_pending](structcoap__pending.md) \* coap\_pending\_next\_to\_expire | ( | struct [coap\_pending](structcoap__pending.md) \* | *pendings*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[coap.h](coap_8h.md)>`

Returns the next pending about to expire, pending->timeout informs how many ms to next expiration.

Parameters
:   | pendings | Pointer to the array of [coap\_pending](structcoap__pending.md "Represents a request awaiting for an acknowledgment (ACK).") structures |
    | --- | --- |
    | len | Size of the array of [coap\_pending](structcoap__pending.md "Represents a request awaiting for an acknowledgment (ACK).") structures |

Returns
:   The next [coap\_pending](structcoap__pending.md "Represents a request awaiting for an acknowledgment (ACK).") to expire, NULL if none is about to expire.

## [◆ ](#ga800831ddfe19b1a5637a5edd9e78c470)coap\_pending\_next\_unused()

| struct [coap\_pending](structcoap__pending.md) \* coap\_pending\_next\_unused | ( | struct [coap\_pending](structcoap__pending.md) \* | *pendings*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[coap.h](coap_8h.md)>`

Returns the next available pending struct, that can be used to track the retransmission status of a request.

Parameters
:   | pendings | Pointer to the array of [coap\_pending](structcoap__pending.md "Represents a request awaiting for an acknowledgment (ACK).") structures |
    | --- | --- |
    | len | Size of the array of [coap\_pending](structcoap__pending.md "Represents a request awaiting for an acknowledgment (ACK).") structures |

Returns
:   pointer to a free [coap\_pending](structcoap__pending.md "Represents a request awaiting for an acknowledgment (ACK).") structure, NULL in case none could be found.

## [◆ ](#ga94ceba78cbd2440f91d9b30d6b06594d)coap\_pending\_received()

| struct [coap\_pending](structcoap__pending.md) \* coap\_pending\_received | ( | const struct [coap\_packet](structcoap__packet.md) \* | *response*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_pending](structcoap__pending.md) \* | *pendings*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[coap.h](coap_8h.md)>`

After a response is received, returns if there is any matching pending request exits.

User has to clear all pending retransmissions related to that response by calling [coap\_pending\_clear()](#ga03287eb3187aa28e0e83e0e0c72e2631).

Parameters
:   | response | The received response |
    | --- | --- |
    | pendings | Pointer to the array of [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structures |
    | len | Size of the array of [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structures |

Returns
:   pointer to the associated [coap\_pending](structcoap__pending.md "Represents a request awaiting for an acknowledgment (ACK).") structure, NULL in case none could be found.

## [◆ ](#ga6e0947048052e733a3571fdc8955b2d7)coap\_pendings\_clear()

| void coap\_pendings\_clear | ( | struct [coap\_pending](structcoap__pending.md) \* | *pendings*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[coap.h](coap_8h.md)>`

Cancels all pending retransmissions, so they become available again.

Parameters
:   | pendings | Pointer to the array of [coap\_pending](structcoap__pending.md "Represents a request awaiting for an acknowledgment (ACK).") structures |
    | --- | --- |
    | len | Size of the array of [coap\_pending](structcoap__pending.md "Represents a request awaiting for an acknowledgment (ACK).") structures |

## [◆ ](#gad9db2ced9b882265c16e3039f893ca03)coap\_pendings\_count()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) coap\_pendings\_count | ( | struct [coap\_pending](structcoap__pending.md) \* | *pendings*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[coap.h](coap_8h.md)>`

Count number of pending requests.

Parameters
:   | len | Number of elements in array. |
    | --- | --- |
    | pendings | Array of pending requests. |

Returns
:   count of elements where timeout is not zero.

## [◆ ](#ga3c42861f8442e548f560acf3deca6baa)coap\_register\_observer()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coap\_register\_observer | ( | struct [coap\_resource](structcoap__resource.md) \* | *resource*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_observer](structcoap__observer.md) \* | *observer* ) |

`#include <[coap.h](coap_8h.md)>`

After the observer is initialized, associate the observer with an resource.

Parameters
:   | resource | Resource to add an observer |
    | --- | --- |
    | observer | Observer to be added |

Returns
:   true if this is the first observer added to this resource.

## [◆ ](#ga941ee9d68f1a628755aa79c249cbae58)coap\_remove\_descriptive\_block\_option()

| int coap\_remove\_descriptive\_block\_option | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Remove BLOCK1 or BLOCK2 option from the packet.

If the CoAP packet is a request then BLOCK1 is removed otherwise BLOCK2 is removed.

Parameters
:   | cpkt | Packet to be updated. |
    | --- | --- |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga33c351ac06b5ae9217cd53d8cf330fbd)coap\_remove\_observer()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coap\_remove\_observer | ( | struct [coap\_resource](structcoap__resource.md) \* | *resource*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_observer](structcoap__observer.md) \* | *observer* ) |

`#include <[coap.h](coap_8h.md)>`

Remove this observer from the list of registered observers of that resource.

Parameters
:   | resource | Resource in which to remove the observer |
    | --- | --- |
    | observer | Observer to be removed |

Returns
:   true if the observer was found and removed.

## [◆ ](#gaddb02509934f5bac20b7c7f83aea4cd8)coap\_replies\_clear()

| void coap\_replies\_clear | ( | struct [coap\_reply](structcoap__reply.md) \* | *replies*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[coap.h](coap_8h.md)>`

Cancels all replies, so they become available again.

Parameters
:   | replies | Pointer to the array of [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structures |
    | --- | --- |
    | len | Size of the array of [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structures |

## [◆ ](#ga37b58c38c150751d31207ece416529d8)coap\_reply\_clear()

| void coap\_reply\_clear | ( | struct [coap\_reply](structcoap__reply.md) \* | *reply* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Cancels awaiting for this reply, so it becomes available again.

User responsibility to free the memory associated with data.

Parameters
:   | reply | The reply to be canceled |
    | --- | --- |

## [◆ ](#gacfe30c84434dc8adbf3d399ec0e51bec)coap\_reply\_init()

| void coap\_reply\_init | ( | struct [coap\_reply](structcoap__reply.md) \* | *reply*, |
| --- | --- | --- | --- |
|  |  | const struct [coap\_packet](structcoap__packet.md) \* | *request* ) |

`#include <[coap.h](coap_8h.md)>`

Indicates that a reply is expected for *request*.

Parameters
:   | reply | Reply structure to be initialized |
    | --- | --- |
    | request | Request from which *reply* will be based |

## [◆ ](#ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e)coap\_reply\_next\_unused()

| struct [coap\_reply](structcoap__reply.md) \* coap\_reply\_next\_unused | ( | struct [coap\_reply](structcoap__reply.md) \* | *replies*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[coap.h](coap_8h.md)>`

Returns the next available reply struct, so it can be used to track replies and notifications received.

Parameters
:   | replies | Pointer to the array of [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structures |
    | --- | --- |
    | len | Size of the array of [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structures |

Returns
:   pointer to a free [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structure, NULL in case none could be found.

## [◆ ](#ga46b315c30b642eec65bcb84e9c937ee7)coap\_request\_is\_observe()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coap\_request\_is\_observe | ( | const struct [coap\_packet](structcoap__packet.md) \* | *request* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Returns if this request is enabling observing a resource.

Parameters
:   | request | Request to be checked |
    | --- | --- |

Returns
:   True if the request is enabling observing a resource, False otherwise

## [◆ ](#gad0c738d308f9cca8ea5cdb79449282cb)coap\_resource\_notify()

| int coap\_resource\_notify | ( | struct [coap\_resource](structcoap__resource.md) \* | *resource* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Indicates that this resource was updated and that the *notify* callback should be called for every registered observer.

Parameters
:   | resource | Resource that was updated |
    | --- | --- |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga3da23a809504025a24bf03daea3e606b)coap\_response\_received()

| struct [coap\_reply](structcoap__reply.md) \* coap\_response\_received | ( | const struct [coap\_packet](structcoap__packet.md) \* | *response*, |
| --- | --- | --- | --- |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *from*, |
|  |  | struct [coap\_reply](structcoap__reply.md) \* | *replies*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[coap.h](coap_8h.md)>`

After a response is received, call [coap\_reply\_t](#ga556deaf757f3047eefc2f032d0d7e0bc) handler registered in [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structure.

Parameters
:   | response | A response received |
    | --- | --- |
    | from | Address from which the response was received |
    | replies | Pointer to the array of [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structures |
    | len | Size of the array of [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structures |

Returns
:   Pointer to the reply matching the packet received, NULL if none could be found.

## [◆ ](#ga9626781d73d18c1305f654ef4723e5db)coap\_rst\_init()

| int coap\_rst\_init | ( | struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | const struct [coap\_packet](structcoap__packet.md) \* | *req*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *max\_len* ) |

`#include <[coap.h](coap_8h.md)>`

Create a new CoAP Reset message for given request.

This function works like [coap\_packet\_init](#ga90e6aab174f8977f0a3b5fbe1a20297c), filling CoAP header type, and CoAP header message id fields.

Parameters
:   | cpkt | New packet to be initialized using the storage from *data*. |
    | --- | --- |
    | req | CoAP request packet that is being acknowledged |
    | data | Data that will contain a CoAP packet information |
    | max\_len | Maximum allowable length of data |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#gaf361fd233f1aa650650108ae1e205ede)coap\_set\_transmission\_parameters()

| void coap\_set\_transmission\_parameters | ( | const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \* | *params* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[coap.h](coap_8h.md)>`

Set CoAP transmission parameters.

Parameters
:   | params | Pointer to the transmission parameters structure. |
    | --- | --- |

## [◆ ](#ga3b0cc9bfabdddeffd98f36d7f15dd416)coap\_update\_from\_block()

| int coap\_update\_from\_block | ( | const struct [coap\_packet](structcoap__packet.md) \* | *cpkt*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_block\_context](structcoap__block__context.md) \* | *ctx* ) |

`#include <[coap.h](coap_8h.md)>`

Retrieves BLOCK{1,2} and SIZE{1,2} from *cpkt* and updates *ctx* accordingly.

Parameters
:   | cpkt | Packet in which to look for block-wise transfers options |
    | --- | --- |
    | ctx | Block context to be updated |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga8b621232b740d8e8e1771fba24897121)coap\_uri\_path\_match()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coap\_uri\_path\_match | ( | const char \*const \* | *path*, |
| --- | --- | --- | --- |
|  |  | struct [coap\_option](structcoap__option.md) \* | *options*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *opt\_num* ) |

`#include <[coap.h](coap_8h.md)>`

Verify if CoAP URI path matches with provided options.

Parameters
:   | path | Null-terminated array of strings. |
    | --- | --- |
    | options | Parsed options from [coap\_packet\_parse()](#ga27a58a69f632551aa7a2394ae2badacf) |
    | opt\_num | Number of options |

Returns
:   true if the CoAP URI path matches, false otherwise.

## [◆ ](#ga3f2eded87dbeb7408ff6f07e04afb30b)coap\_well\_known\_core\_get()

| int coap\_well\_known\_core\_get | ( | struct [coap\_resource](structcoap__resource.md) \* | *resource*, |
| --- | --- | --- | --- |
|  |  | const struct [coap\_packet](structcoap__packet.md) \* | *request*, |
|  |  | struct [coap\_packet](structcoap__packet.md) \* | *response*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data\_len* ) |

`#include <[coap_link_format.h](coap__link__format_8h.md)>`

Build a CoAP response for a .well-known/core CoAP request.

Parameters
:   | resource | Array of known resources, terminated with an empty resource |
    | --- | --- |
    | request | A pointer to the .well-known/core CoAP request |
    | response | A pointer to a CoAP response, will be initialized |
    | data | A data pointer to be used to build the CoAP response |
    | data\_len | The maximum length of the data buffer |

Returns
:   0 in case of success or negative in case of error.

## [◆ ](#ga49d63f12b593d7509690a504b05da730)coap\_well\_known\_core\_get\_len()

| int coap\_well\_known\_core\_get\_len | ( | struct [coap\_resource](structcoap__resource.md) \* | *resources*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *resources\_len*, |
|  |  | const struct [coap\_packet](structcoap__packet.md) \* | *request*, |
|  |  | struct [coap\_packet](structcoap__packet.md) \* | *response*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data\_len* ) |

`#include <[coap_link_format.h](coap__link__format_8h.md)>`

Build a CoAP response for a .well-known/core CoAP request.

Parameters
:   | resources | Array of known resources |
    | --- | --- |
    | resources\_len | Number of resources in the array |
    | request | A pointer to the .well-known/core CoAP request |
    | response | A pointer to a CoAP response, will be initialized |
    | data | A data pointer to be used to build the CoAP response |
    | data\_len | The maximum length of the data buffer |

Returns
:   0 in case of success or negative in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
