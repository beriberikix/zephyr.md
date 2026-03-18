---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/coap_8h.html
original_path: doxygen/html/coap_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap.h File Reference

CoAP implementation for Zephyr.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/sys/math_extras.h](math__extras_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](coap_8h_source.md)

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

| Macros | |
| --- | --- |
| #define | [COAP\_MAKE\_RESPONSE\_CODE](group__coap.md#gabdcc1f443e89bd035522cbab7dfee879)(class, det) |
|  | Utility macro to create a CoAP response code. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc)) (struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_packet](structcoap__packet.md) \*request, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len) |
|  | Type of the callback being called when a resource's method is invoked by the remote entity. |
| typedef void(\* | [coap\_notify\_t](group__coap.md#ga4180b2476430fbe4a5e0418fb628ea91)) (struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_observer](structcoap__observer.md) \*observer) |
|  | Type of the callback being called when a resource's has observers to be informed when an update happens. |
| typedef int(\* | [coap\_reply\_t](group__coap.md#ga556deaf757f3047eefc2f032d0d7e0bc)) (const struct [coap\_packet](structcoap__packet.md) \*response, struct [coap\_reply](structcoap__reply.md) \*reply, const struct [sockaddr](structsockaddr.md) \*from) |
|  | Helper function to be called when a response matches the a pending request. |

| Enumerations | |
| --- | --- |
| enum | [coap\_option\_num](group__coap.md#ga7b8b3041e2f4ae26e663ff7431a6e6e3) {     [COAP\_OPTION\_IF\_MATCH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4c61e26d11841c76debe2f99de5e9756) = 1 , [COAP\_OPTION\_URI\_HOST](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a402bb0a642a07d951c35d69736fd3f33) = 3 , [COAP\_OPTION\_ETAG](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a0efdc30ce5551daffd093b2a8466978a) = 4 , [COAP\_OPTION\_IF\_NONE\_MATCH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a07ea6f395818a7019bb9e6a6e34d2d74) = 5 ,     [COAP\_OPTION\_OBSERVE](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a06e91bbb4fa2144543d4148d3245ad25) = 6 , [COAP\_OPTION\_URI\_PORT](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a344707b9f4cb71310f2ccf5e8050d17a) = 7 , [COAP\_OPTION\_LOCATION\_PATH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae82be3591d43f0d1c7e89ab764d969bd) = 8 , [COAP\_OPTION\_URI\_PATH](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a96b5a15937e875b3087307cc5faab1af) = 11 ,     [COAP\_OPTION\_CONTENT\_FORMAT](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac3166e67b5f5bf3cefee58c8ff58e5b8) = 12 , [COAP\_OPTION\_MAX\_AGE](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ab4cda4d3732fd12b9f203a2475c20981) = 14 , [COAP\_OPTION\_URI\_QUERY](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3adb4d27052247b9a79ad7fcc0cc30c71c) = 15 , [COAP\_OPTION\_ACCEPT](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3afd0725f0ceb5ce22a6c7b390ca7efc9d) = 17 ,     [COAP\_OPTION\_LOCATION\_QUERY](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac728800fc8f0d80e37dcf322e75eb27d) = 20 , [COAP\_OPTION\_BLOCK2](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972) = 23 , [COAP\_OPTION\_BLOCK1](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a8aaa54af114fd1db631566afa69f162d) = 27 , [COAP\_OPTION\_SIZE2](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a26c1bcd7af4fccd949e3de35fc2d88e6) = 28 ,     [COAP\_OPTION\_PROXY\_URI](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae4d2c93b545708926813217cd36a96ac) = 35 , [COAP\_OPTION\_PROXY\_SCHEME](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a30da986503e1e15243b74a16b161901c) = 39 , [COAP\_OPTION\_SIZE1](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a53169a1c7b07c9e97f79dfc06af3eb51) = 60 , [COAP\_OPTION\_ECHO](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a620e8b59f67f89de8a38dc76c8fcc594) = 252 ,     [COAP\_OPTION\_REQUEST\_TAG](group__coap.md#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2a47428ec35972d256da05104ea6396f) = 292   } |
|  | Set of CoAP packet options we are aware of. [More...](group__coap.md#ga7b8b3041e2f4ae26e663ff7431a6e6e3) |
| enum | [coap\_method](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7) {     [COAP\_METHOD\_GET](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a025300cb0dc4c4de8eb0b0e0b4eb5317) = 1 , [COAP\_METHOD\_POST](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7aba51bcab79bf75080ccf75c1ec38a3d6) = 2 , [COAP\_METHOD\_PUT](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a91637ef7c9f57cdcc65d0118008251db) = 3 , [COAP\_METHOD\_DELETE](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7adccbea1fe9a43433cf8471e32208a5ac) = 4 ,     [COAP\_METHOD\_FETCH](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7afa4070fed5c01b28bb1a59e3f0c021f4) = 5 , [COAP\_METHOD\_PATCH](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7adca55e3d2b4b41b249f6b2f67074d708) = 6 , [COAP\_METHOD\_IPATCH](group__coap.md#gga6a6547e3c755cf7a5033302c8294e0b7a78f97b895f29819bf3f8b0314967f20e) = 7   } |
|  | Available request methods. [More...](group__coap.md#ga6a6547e3c755cf7a5033302c8294e0b7) |
| enum | [coap\_msgtype](group__coap.md#ga3b375b7580246d1266293d09902f3d9f) { [COAP\_TYPE\_CON](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa65c04ee4847d0c595238079ac9564e8d) = 0 , [COAP\_TYPE\_NON\_CON](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa629a304bea0c85c7b2bf746b26216a4f) = 1 , [COAP\_TYPE\_ACK](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa7b2fe2187018bce9132af2763b57307d) = 2 , [COAP\_TYPE\_RESET](group__coap.md#gga3b375b7580246d1266293d09902f3d9fa287b951159fd51b84a2e0491b012f84c) = 3 } |
|  | CoAP packets may be of one of these types. [More...](group__coap.md#ga3b375b7580246d1266293d09902f3d9f) |
| enum | [coap\_response\_code](group__coap.md#ga1ea81a365834e96f43ab7be573069d26) {     [COAP\_RESPONSE\_CODE\_OK](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a0629da1898b934c3f699b98ff808c717) = ((2 << 5) | (0)) , [COAP\_RESPONSE\_CODE\_CREATED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ad2d9fe8dd5beda74b522377c0b76275b) = ((2 << 5) | (1)) , [COAP\_RESPONSE\_CODE\_DELETED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26abf324915aa498c64a733a0098de4a082) = ((2 << 5) | (2)) , [COAP\_RESPONSE\_CODE\_VALID](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aecaac4a0e9c821dfc20536951409dd48) = ((2 << 5) | (3)) ,     [COAP\_RESPONSE\_CODE\_CHANGED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3) = ((2 << 5) | (4)) , [COAP\_RESPONSE\_CODE\_CONTENT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26adfd3e5e3c6ad5715127bb444c205fbce) = ((2 << 5) | (5)) , [COAP\_RESPONSE\_CODE\_CONTINUE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ae4e3ff451c626421b9b329790f019dd8) = ((2 << 5) | (31)) , [COAP\_RESPONSE\_CODE\_BAD\_REQUEST](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5) = ((4 << 5) | (0)) ,     [COAP\_RESPONSE\_CODE\_UNAUTHORIZED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26acb76dbf11b47477144cc4ece3357283c) = ((4 << 5) | (1)) , [COAP\_RESPONSE\_CODE\_BAD\_OPTION](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a989a6528edc653c0b693ed875481e82d) = ((4 << 5) | (2)) , [COAP\_RESPONSE\_CODE\_FORBIDDEN](group__coap.md#gga1ea81a365834e96f43ab7be573069d26afeee555ef54f138db58b14ad2c328d04) = ((4 << 5) | (3)) , [COAP\_RESPONSE\_CODE\_NOT\_FOUND](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a86c2bff8add69428d164431b3091a8e9) = ((4 << 5) | (4)) ,     [COAP\_RESPONSE\_CODE\_NOT\_ALLOWED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a301eb722445472dba93d5accd6e0dd31) = ((4 << 5) | (5)) , [COAP\_RESPONSE\_CODE\_NOT\_ACCEPTABLE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a4d77322514521e8dfea01f4a1a6e5886) = ((4 << 5) | (6)) , [COAP\_RESPONSE\_CODE\_INCOMPLETE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a671730c6d2f1a339fcd557c5452150af) = ((4 << 5) | (8)) , [COAP\_RESPONSE\_CODE\_CONFLICT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26ab447505d233aed9fd8ad28070d317544) = ((4 << 5) | (9)) ,     [COAP\_RESPONSE\_CODE\_PRECONDITION\_FAILED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a289ade02833b57bffd915e648e050e52) = ((4 << 5) | (12)) , [COAP\_RESPONSE\_CODE\_REQUEST\_TOO\_LARGE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aaa43062a8146c1e2e09183228a540d2e) = ((4 << 5) | (13)) , [COAP\_RESPONSE\_CODE\_UNSUPPORTED\_CONTENT\_FORMAT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aef6b165b9d3f8f4b477431058815c16b) , [COAP\_RESPONSE\_CODE\_UNPROCESSABLE\_ENTITY](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a5e5e31cc4647d5e0fdd1c8fe6cfa2661) = ((4 << 5) | (22)) ,     [COAP\_RESPONSE\_CODE\_TOO\_MANY\_REQUESTS](group__coap.md#gga1ea81a365834e96f43ab7be573069d26aabd72cff6669d382aa04c53e764d0b49) = ((4 << 5) | (29)) , [COAP\_RESPONSE\_CODE\_INTERNAL\_ERROR](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499) = ((5 << 5) | (0)) , [COAP\_RESPONSE\_CODE\_NOT\_IMPLEMENTED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a85c04541bc8580c2ae915946fd677c15) = ((5 << 5) | (1)) , [COAP\_RESPONSE\_CODE\_BAD\_GATEWAY](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a8de29a7ee6bb960a97d6b415217b4640) = ((5 << 5) | (2)) ,     [COAP\_RESPONSE\_CODE\_SERVICE\_UNAVAILABLE](group__coap.md#gga1ea81a365834e96f43ab7be573069d26afebd274586351951ffe9c8f26b270dec) = ((5 << 5) | (3)) , [COAP\_RESPONSE\_CODE\_GATEWAY\_TIMEOUT](group__coap.md#gga1ea81a365834e96f43ab7be573069d26af6d379fef704c269406b782c60772ecd) = ((5 << 5) | (4)) , [COAP\_RESPONSE\_CODE\_PROXYING\_NOT\_SUPPORTED](group__coap.md#gga1ea81a365834e96f43ab7be573069d26a5f49a566d37b2cda0c624d76aee08bd1)   } |
|  | Set of response codes available for a response packet. [More...](group__coap.md#ga1ea81a365834e96f43ab7be573069d26) |
| enum | [coap\_content\_format](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73) {     [COAP\_CONTENT\_FORMAT\_TEXT\_PLAIN](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73af068aa8d09032352799bc60868607997) = 0 , [COAP\_CONTENT\_FORMAT\_APP\_LINK\_FORMAT](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a1fbd90fd5cb309e2de6954f46174dc4f) = 40 , [COAP\_CONTENT\_FORMAT\_APP\_XML](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73adb96bf55e914f4852e92dc65752c372a) = 41 , [COAP\_CONTENT\_FORMAT\_APP\_OCTET\_STREAM](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a88d952174bb3e4ffb9ab11a599952760) = 42 ,     [COAP\_CONTENT\_FORMAT\_APP\_EXI](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a483a382550b38468cc66bdce9f4743ea) = 47 , [COAP\_CONTENT\_FORMAT\_APP\_JSON](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a975381d286c1e9b998e41ef0a234d17a) = 50 , [COAP\_CONTENT\_FORMAT\_APP\_JSON\_PATCH\_JSON](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a141f183724ad6da14c3992c0990d6239) = 51 , [COAP\_CONTENT\_FORMAT\_APP\_MERGE\_PATCH\_JSON](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a2797149fb3811d706dab291e9edc9436) = 52 ,     [COAP\_CONTENT\_FORMAT\_APP\_CBOR](group__coap.md#gga94a8f9956742d3928fc3c63b8d01ae73a7ca73ff57a6c7fb1517b44f2ce17d3f9) = 60   } |
|  | Set of Content-Format option values for CoAP. [More...](group__coap.md#ga94a8f9956742d3928fc3c63b8d01ae73) |
| enum | [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) {     [COAP\_BLOCK\_16](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968) , [COAP\_BLOCK\_32](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a1aaf8f841c18e281b176793bb331993d) , [COAP\_BLOCK\_64](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a7266f448a391ea2a2763f1ded5397520) , [COAP\_BLOCK\_128](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a147ddf4b0e5d1a8c11f0da2c71dee4d8) ,     [COAP\_BLOCK\_256](group__coap.md#gga712c1468f936a3af7dc39a86a5961922acfc37f84eabccdde4bd84b06c6a5e753) , [COAP\_BLOCK\_512](group__coap.md#gga712c1468f936a3af7dc39a86a5961922ad2052905aff08c58585dcf6c6caddc19) , [COAP\_BLOCK\_1024](group__coap.md#gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce)   } |
|  | Represents the size of each block that will be transferred using block-wise transfers [RFC7959]: [More...](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) |

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [coap\_header\_get\_version](group__coap.md#gafd01c39fac8f173edc04337161e92264) (const struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Returns the version present in a CoAP packet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [coap\_header\_get\_type](group__coap.md#gaed883ea6cec3acc5eb570e152dc52e25) (const struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Returns the type of the CoAP packet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [coap\_header\_get\_token](group__coap.md#ga6a5049accfa0cd7106a3a6593c598545) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token) |
|  | Returns the token (if any) in the CoAP packet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [coap\_header\_get\_code](group__coap.md#gae4bf952fdf9e3d03ab0b0df4c3c0d054) (const struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Returns the code of the CoAP packet. |
| int | [coap\_header\_set\_code](group__coap.md#gafdaecca5ad26bab4fb7c9ee3477318f8) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code) |
|  | Modifies the code of the CoAP packet. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [coap\_header\_get\_id](group__coap.md#ga63388c629da5370d2e711cdc9aabd837) (const struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Returns the message id associated with the CoAP packet. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [coap\_packet\_get\_payload](group__coap.md#ga28ccf00fb1f5f13f747e61c2e3008b5c) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*len) |
|  | Returns the data pointer and length of the CoAP packet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_uri\_path\_match](group__coap.md#ga8b621232b740d8e8e1771fba24897121) (const char \*const \*path, struct [coap\_option](structcoap__option.md) \*options, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num) |
|  | Verify if CoAP URI path matches with provided options. |
| int | [coap\_packet\_parse](group__coap.md#ga27a58a69f632551aa7a2394ae2badacf) (struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, struct [coap\_option](structcoap__option.md) \*options, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num) |
|  | Parses the CoAP packet in data, validating it and initializing *cpkt*. |
| int | [coap\_packet\_set\_path](group__coap.md#gab8f9e9cdfa20920d5d25fb1507a2286d) (struct [coap\_packet](structcoap__packet.md) \*cpkt, const char \*path) |
|  | Parses provided coap path (with/without query) or query and appends that as options to the *cpkt*. |
| int | [coap\_packet\_init](group__coap.md#ga90e6aab174f8977f0a3b5fbe1a20297c) (struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ver, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | Creates a new CoAP Packet from input data. |
| int | [coap\_ack\_init](group__coap.md#gae6d93b1f93734302be75ee417813e5d1) (struct [coap\_packet](structcoap__packet.md) \*cpkt, const struct [coap\_packet](structcoap__packet.md) \*req, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) code) |
|  | Create a new CoAP Acknowledgment message for given request. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [coap\_next\_token](group__coap.md#ga66f986f8a1157236bea27133c2a2538b) (void) |
|  | Returns a randomly generated array of 8 bytes, that can be used as a message's token. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [coap\_next\_id](group__coap.md#gade5f4995c6419db03ce3e7ff7ca1cfcb) (void) |
|  | Helper to generate message ids. |
| int | [coap\_find\_options](group__coap.md#gaf006c8048ed7b863e70dbdd64bc3d608) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, struct [coap\_option](structcoap__option.md) \*options, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) veclen) |
|  | Return the values associated with the option of value *code*. |
| int | [coap\_packet\_append\_option](group__coap.md#ga2aa4140ee83ca4090a5604e34d1f1446) (struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Appends an option to the packet. |
| int | [coap\_packet\_remove\_option](group__coap.md#gaca300a216781d360d2cd64e8e9f1ae8f) (struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code) |
|  | Remove an option from the packet. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [coap\_option\_value\_to\_int](group__coap.md#ga2fd0613e61274ec4b9b7bab3ab11ccce) (const struct [coap\_option](structcoap__option.md) \*option) |
|  | Converts an option to its integer representation. |
| int | [coap\_append\_option\_int](group__coap.md#ga6bec94992ac450dca03436a6ad74efb4) (struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int val) |
|  | Appends an integer value option to the packet. |
| int | [coap\_packet\_append\_payload\_marker](group__coap.md#ga24000def8534acdcd2c61836dc690367) (struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Append payload marker to CoAP packet. |
| int | [coap\_packet\_append\_payload](group__coap.md#gadcd3a93a702a2a0b428f39b71dd67954) (struct [coap\_packet](structcoap__packet.md) \*cpkt, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) payload\_len) |
|  | Append payload to CoAP packet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_packet\_is\_request](group__coap.md#ga323644931c927b8988aafd89dacb993c) (const struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Check if a CoAP packet is a CoAP request. |
| int | [coap\_handle\_request\_len](group__coap.md#ga864a95bd0d095070200494c630f7e147) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_resource](structcoap__resource.md) \*resources, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) resources\_len, struct [coap\_option](structcoap__option.md) \*options, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len) |
|  | When a request is received, call the appropriate methods of the matching resources. |
| int | [coap\_handle\_request](group__coap.md#ga88a5f2c3915ef109eadfebaf82b53186) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_resource](structcoap__resource.md) \*resources, struct [coap\_option](structcoap__option.md) \*options, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt\_num, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len) |
|  | When a request is received, call the appropriate methods of the matching resources. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [coap\_block\_size\_to\_bytes](group__coap.md#gafffadd4a837e48fd72af20468ccd86f2) (enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) block\_size) |
|  | Helper for converting the enumeration to the size expressed in bytes. |
| static enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) | [coap\_bytes\_to\_block\_size](group__coap.md#ga27e3008b8511333e0c0115ba928017f3) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bytes) |
|  | Helper for converting block size in bytes to enumeration. |
| int | [coap\_block\_transfer\_init](group__coap.md#ga57486e764f0feb6544fa3b0d19935afd) (struct [coap\_block\_context](structcoap__block__context.md) \*ctx, enum [coap\_block\_size](group__coap.md#ga712c1468f936a3af7dc39a86a5961922) block\_size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) total\_size) |
|  | Initializes the context of a block-wise transfer. |
| int | [coap\_append\_descriptive\_block\_option](group__coap.md#ga8b5966a29054ace04cae81d4da588e72) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Append BLOCK1 or BLOCK2 option to the packet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_has\_descriptive\_block\_option](group__coap.md#gaabdfa8cf28cc2c3a14ae0af5fa7e7212) (struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Check if a descriptive block option is set in the packet. |
| int | [coap\_remove\_descriptive\_block\_option](group__coap.md#ga941ee9d68f1a628755aa79c249cbae58) (struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Remove BLOCK1 or BLOCK2 option from the packet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_block\_has\_more](group__coap.md#gafc61a6878d82f81565ab752ced0ce2be) (struct [coap\_packet](structcoap__packet.md) \*cpkt) |
|  | Check if BLOCK1 or BLOCK2 option has more flag set. |
| int | [coap\_append\_block1\_option](group__coap.md#ga518d5f4422ff45f2b4a296f249da89cd) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Append BLOCK1 option to the packet. |
| int | [coap\_append\_block2\_option](group__coap.md#ga361c17b698bdaa0fc529b7338efefd8c) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Append BLOCK2 option to the packet. |
| int | [coap\_append\_size1\_option](group__coap.md#ga3f66d5935dcacfeebcac2b3001d7b57a) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Append SIZE1 option to the packet. |
| int | [coap\_append\_size2\_option](group__coap.md#gafbc8c15ef03b762f9411c38b03aa403b) (struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Append SIZE2 option to the packet. |
| int | [coap\_get\_option\_int](group__coap.md#ga21b8f4ffeecc7900f6bf299836d2b5b3) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code) |
|  | Get the integer representation of a CoAP option. |
| int | [coap\_get\_block1\_option](group__coap.md#ga796c9fcf9f447ccf7def2da091e7e5f5) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*has\_more, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*block\_number) |
|  | Get the block size, more flag and block number from the CoAP block1 option. |
| int | [coap\_get\_block2\_option](group__coap.md#ga161875609f4a1ce5806625f97cd90a39) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*block\_number) |
|  | Get values from CoAP block2 option. |
| int | [coap\_update\_from\_block](group__coap.md#ga3b0cc9bfabdddeffd98f36d7f15dd416) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Retrieves BLOCK{1,2} and SIZE{1,2} from *cpkt* and updates *ctx* accordingly. |
| int | [coap\_next\_block\_for\_option](group__coap.md#ga50f7837da003601479dbc470ba9898ae) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx, enum [coap\_option\_num](group__coap.md#ga7b8b3041e2f4ae26e663ff7431a6e6e3) option) |
|  | Updates *ctx* according to *option* set in *cpkt* so after this is called the current entry indicates the correct offset in the body of data being transferred. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [coap\_next\_block](group__coap.md#ga1244716ecf06fad1013131c42eab8c5c) (const struct [coap\_packet](structcoap__packet.md) \*cpkt, struct [coap\_block\_context](structcoap__block__context.md) \*ctx) |
|  | Updates *ctx* so after this is called the current entry indicates the correct offset in the body of data being transferred. |
| void | [coap\_observer\_init](group__coap.md#ga3d720b0d222cc35ce56cc260df1609a3) (struct [coap\_observer](structcoap__observer.md) \*observer, const struct [coap\_packet](structcoap__packet.md) \*request, const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Indicates that the remote device referenced by *addr*, with *request*, wants to observe a resource. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_register\_observer](group__coap.md#ga3c42861f8442e548f560acf3deca6baa) (struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_observer](structcoap__observer.md) \*observer) |
|  | After the observer is initialized, associate the observer with an resource. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_remove\_observer](group__coap.md#ga33c351ac06b5ae9217cd53d8cf330fbd) (struct [coap\_resource](structcoap__resource.md) \*resource, struct [coap\_observer](structcoap__observer.md) \*observer) |
|  | Remove this observer from the list of registered observers of that resource. |
| struct [coap\_observer](structcoap__observer.md) \* | [coap\_find\_observer](group__coap.md#gaf9c1a55aee52588df2694ea947db5db4) (struct [coap\_observer](structcoap__observer.md) \*observers, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [sockaddr](structsockaddr.md) \*addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len) |
|  | Returns the observer that matches address *addr* and has token *token*. |
| struct [coap\_observer](structcoap__observer.md) \* | [coap\_find\_observer\_by\_addr](group__coap.md#ga427167161529c24f5cf8c9ed2023e321) (struct [coap\_observer](structcoap__observer.md) \*observers, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Returns the observer that matches address *addr*. |
| struct [coap\_observer](structcoap__observer.md) \* | [coap\_find\_observer\_by\_token](group__coap.md#gadeaa59fd7b6eab454d5930289b4e08f7) (struct [coap\_observer](structcoap__observer.md) \*observers, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len) |
|  | Returns the observer that has token *token*. |
| struct [coap\_observer](structcoap__observer.md) \* | [coap\_observer\_next\_unused](group__coap.md#ga2410e973bf3192244426df346230608b) (struct [coap\_observer](structcoap__observer.md) \*observers, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Returns the next available observer representation. |
| void | [coap\_reply\_init](group__coap.md#gacfe30c84434dc8adbf3d399ec0e51bec) (struct [coap\_reply](structcoap__reply.md) \*reply, const struct [coap\_packet](structcoap__packet.md) \*request) |
|  | Indicates that a reply is expected for *request*. |
| int | [coap\_pending\_init](group__coap.md#ga868f792abf555f01c28caa5413d9e84c) (struct [coap\_pending](structcoap__pending.md) \*pending, const struct [coap\_packet](structcoap__packet.md) \*request, const struct [sockaddr](structsockaddr.md) \*addr, const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params) |
|  | Initialize a pending request with a request. |
| struct [coap\_pending](structcoap__pending.md) \* | [coap\_pending\_next\_unused](group__coap.md#ga800831ddfe19b1a5637a5edd9e78c470) (struct [coap\_pending](structcoap__pending.md) \*pendings, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Returns the next available pending struct, that can be used to track the retransmission status of a request. |
| struct [coap\_reply](structcoap__reply.md) \* | [coap\_reply\_next\_unused](group__coap.md#ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e) (struct [coap\_reply](structcoap__reply.md) \*replies, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Returns the next available reply struct, so it can be used to track replies and notifications received. |
| struct [coap\_pending](structcoap__pending.md) \* | [coap\_pending\_received](group__coap.md#ga94ceba78cbd2440f91d9b30d6b06594d) (const struct [coap\_packet](structcoap__packet.md) \*response, struct [coap\_pending](structcoap__pending.md) \*pendings, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | After a response is received, returns if there is any matching pending request exits. |
| struct [coap\_reply](structcoap__reply.md) \* | [coap\_response\_received](group__coap.md#ga3da23a809504025a24bf03daea3e606b) (const struct [coap\_packet](structcoap__packet.md) \*response, const struct [sockaddr](structsockaddr.md) \*from, struct [coap\_reply](structcoap__reply.md) \*replies, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | After a response is received, call [coap\_reply\_t](group__coap.md#ga556deaf757f3047eefc2f032d0d7e0bc "Helper function to be called when a response matches the a pending request.") handler registered in [coap\_reply](structcoap__reply.md "Represents the handler for the reply of a request, it is also used when observing resources.") structure. |
| struct [coap\_pending](structcoap__pending.md) \* | [coap\_pending\_next\_to\_expire](group__coap.md#ga9d63518c701ebdb4c7f65c5368d00d27) (struct [coap\_pending](structcoap__pending.md) \*pendings, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Returns the next pending about to expire, pending->timeout informs how many ms to next expiration. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_pending\_cycle](group__coap.md#ga2bcfc7340ed2347862b0f003e1b00a4b) (struct [coap\_pending](structcoap__pending.md) \*pending) |
|  | After a request is sent, user may want to cycle the pending retransmission so the timeout is updated. |
| void | [coap\_pending\_clear](group__coap.md#ga03287eb3187aa28e0e83e0e0c72e2631) (struct [coap\_pending](structcoap__pending.md) \*pending) |
|  | Cancels the pending retransmission, so it again becomes available. |
| void | [coap\_pendings\_clear](group__coap.md#ga6e0947048052e733a3571fdc8955b2d7) (struct [coap\_pending](structcoap__pending.md) \*pendings, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Cancels all pending retransmissions, so they become available again. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [coap\_pendings\_count](group__coap.md#gad9db2ced9b882265c16e3039f893ca03) (struct [coap\_pending](structcoap__pending.md) \*pendings, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Count number of pending requests. |
| void | [coap\_reply\_clear](group__coap.md#ga37b58c38c150751d31207ece416529d8) (struct [coap\_reply](structcoap__reply.md) \*reply) |
|  | Cancels awaiting for this reply, so it becomes available again. |
| void | [coap\_replies\_clear](group__coap.md#gaddb02509934f5bac20b7c7f83aea4cd8) (struct [coap\_reply](structcoap__reply.md) \*replies, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Cancels all replies, so they become available again. |
| int | [coap\_resource\_notify](group__coap.md#gad0c738d308f9cca8ea5cdb79449282cb) (struct [coap\_resource](structcoap__resource.md) \*resource) |
|  | Indicates that this resource was updated and that the *notify* callback should be called for every registered observer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coap\_request\_is\_observe](group__coap.md#ga46b315c30b642eec65bcb84e9c937ee7) (const struct [coap\_packet](structcoap__packet.md) \*request) |
|  | Returns if this request is enabling observing a resource. |
| struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) | [coap\_get\_transmission\_parameters](group__coap.md#ga1bd7be0a5390f0599e7bec0cbd79daf8) (void) |
|  | Get currently active CoAP transmission parameters. |
| void | [coap\_set\_transmission\_parameters](group__coap.md#gaf361fd233f1aa650650108ae1e205ede) (const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params) |
|  | Set CoAP transmission parameters. |

## Detailed Description

CoAP implementation for Zephyr.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap.h](coap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
