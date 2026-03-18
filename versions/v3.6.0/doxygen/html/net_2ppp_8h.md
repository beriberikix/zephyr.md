---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net_2ppp_8h.html
original_path: doxygen/html/net_2ppp_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ppp.h File Reference

`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/net_pkt.h](net__pkt_8h_source.md)>`  
`#include <[zephyr/net/net_stats.h](net__stats_8h_source.md)>`  
`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`

[Go to the source code of this file.](net_2ppp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ppp\_api](structppp__api.md) |
|  | PPP L2 API. [More...](structppp__api.md#details) |
| struct | [ppp\_fsm](structppp__fsm.md) |
|  | Generic PPP Finite State Machine. [More...](structppp__fsm.md#details) |
| struct | [ppp\_my\_option\_data](structppp__my__option__data.md) |
| struct | [lcp\_options](structlcp__options.md) |
| struct | [ipcp\_options](structipcp__options.md) |
| struct | [ipv6cp\_options](structipv6cp__options.md) |
| struct | [ppp\_context](structppp__context.md) |
|  | PPP L2 context specific to certain network interface. [More...](structppp__context.md#details) |

| Macros | |
| --- | --- |
| #define | [PPP\_MRU](group__ppp.md#gaec050624f0693600196068d8f5413e6f)   CONFIG\_NET\_PPP\_MTU\_MRU |
|  | PPP maximum receive unit (MRU). |
| #define | [PPP\_MTU](group__ppp.md#gacc51e91347721a8255ae891ddc43636b)   [PPP\_MRU](group__ppp.md#gaec050624f0693600196068d8f5413e6f) |
|  | PPP maximum transfer unit (MTU). |
| #define | [PPP\_MAX\_TERMINATE\_REASON\_LEN](group__ppp.md#ga2e5d0ae66bf076123cb29effc0a8e894)   32 |
|  | Max length of terminate description string. |
| #define | [PPP\_INTERFACE\_IDENTIFIER\_LEN](group__ppp.md#gaad7380b3a502f4b649348b733124f21a)   8 |
|  | Length of network interface identifier. |
| #define | [PPP\_MY\_OPTION\_ACKED](group__ppp.md#ga217fc7e6ec870657a0b2aae05daa03af)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [PPP\_MY\_OPTION\_REJECTED](group__ppp.md#ga584c13078881fd9604b062210785be75)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [IPCP\_NUM\_MY\_OPTIONS](group__ppp.md#gada07a9f2122fbf911f5d35a92e858c9d)   3 |
| #define | [IPV6CP\_NUM\_MY\_OPTIONS](group__ppp.md#ga580f383f3f33ba6e742a134e853b8411)   1 |

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_ppp\_lcp\_echo\_reply\_cb\_t](group__ppp.md#ga15afa05abc0446201c912c75644306bf)) (void \*user\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) user\_data\_len) |
|  | A callback function that can be called if a Echo-Reply needs to be received. |

| Enumerations | |
| --- | --- |
| enum | [ppp\_protocol\_type](group__ppp.md#ga8ad7cc0d142a6e7ea82c45bec2cc3670) {     [PPP\_IP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6) = 0x0021 , [PPP\_IPV6](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe) = 0x0057 , [PPP\_IPCP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21) = 0x8021 , [PPP\_ECP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44) = 0x8053 ,     [PPP\_IPV6CP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0) = 0x8057 , [PPP\_CCP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b) = 0x80FD , [PPP\_LCP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9) = 0xc021 , [PPP\_PAP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206) = 0xc023 ,     [PPP\_CHAP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25) = 0xc223 , [PPP\_EAP](group__ppp.md#gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2) = 0xc227   } |
|  | PPP protocol types. [More...](group__ppp.md#ga8ad7cc0d142a6e7ea82c45bec2cc3670) |
| enum | [ppp\_phase](group__ppp.md#ga284e237a6323f2daffc444a73a4b8b6b) {     [PPP\_DEAD](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d) , [PPP\_ESTABLISH](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4) , [PPP\_AUTH](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a) , [PPP\_NETWORK](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af) ,     [PPP\_RUNNING](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7) , [PPP\_TERMINATE](group__ppp.md#gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7)   } |
|  | PPP phases. [More...](group__ppp.md#ga284e237a6323f2daffc444a73a4b8b6b) |
| enum | [ppp\_state](group__ppp.md#ga6d4283a0ae63a227933d12d42318cf7c) {     [PPP\_INITIAL](group__ppp.md#gga6d4283a0ae63a227933d12d42318cf7cacab404bd828016b38f34c8128c72c605) , [PPP\_STARTING](group__ppp.md#gga6d4283a0ae63a227933d12d42318cf7ca632204028ea5f855831924eeba5be19b) , [PPP\_CLOSED](group__ppp.md#gga6d4283a0ae63a227933d12d42318cf7ca0fdfbc2f4448ad005284c319928034dd) , [PPP\_STOPPED](group__ppp.md#gga6d4283a0ae63a227933d12d42318cf7caca2412bb44a0304e094a75717ae59326) ,     [PPP\_CLOSING](group__ppp.md#gga6d4283a0ae63a227933d12d42318cf7ca23353ce5f2f06f3ed54e3490617c38fe) , [PPP\_STOPPING](group__ppp.md#gga6d4283a0ae63a227933d12d42318cf7cadad45283af72e570ed0acae6d35d3a9b) , [PPP\_REQUEST\_SENT](group__ppp.md#gga6d4283a0ae63a227933d12d42318cf7ca5f27d2e78dae0c937de8669be1a3698e) , [PPP\_ACK\_RECEIVED](group__ppp.md#gga6d4283a0ae63a227933d12d42318cf7caf3d5f2cb8bc8352ba3b9090b9b24fe69) ,     [PPP\_ACK\_SENT](group__ppp.md#gga6d4283a0ae63a227933d12d42318cf7caf9ada16d1bf148c67504252439e9a1d7) , [PPP\_OPENED](group__ppp.md#gga6d4283a0ae63a227933d12d42318cf7ca5acff74b583c0798cf4cb389d659fe0d)   } |
|  | PPP states, RFC 1661 ch. [More...](group__ppp.md#ga6d4283a0ae63a227933d12d42318cf7c) |
| enum | [ppp\_packet\_type](group__ppp.md#ga305eaed8ab120c7821de1618e10728cf) {     [PPP\_CONFIGURE\_REQ](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfab56e4bcefa0fea644739bd2208bdff62) = 1 , [PPP\_CONFIGURE\_ACK](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfa54a76789e1194fdbd753f78a674e1003) = 2 , [PPP\_CONFIGURE\_NACK](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfa013bc0c33d7afbca68ea157b33773703) = 3 , [PPP\_CONFIGURE\_REJ](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfacfd2485f57fcc1aea9435f70c96f7aed) = 4 ,     [PPP\_TERMINATE\_REQ](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfa0c0cc9b36c5b5b3902bddbd29fad8a9c) = 5 , [PPP\_TERMINATE\_ACK](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfa2e434ed0e64c4620aa4d8e41de31a0f6) = 6 , [PPP\_CODE\_REJ](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfa0fd2c7adbce3dadb1d95d29bd87924aa) = 7 , [PPP\_PROTOCOL\_REJ](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfad0cbd4c01c071faa17b4cc2528bbeb65) = 8 ,     [PPP\_ECHO\_REQ](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfaf15f00b023f761f71c8e41de6afef20b) = 9 , [PPP\_ECHO\_REPLY](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfa13f08a92a1b1ce1f7a0014fb7087a672) = 10 , [PPP\_DISCARD\_REQ](group__ppp.md#gga305eaed8ab120c7821de1618e10728cfaa1ea3fb1e422c5831d587113d786c927) = 11   } |
|  | PPP protocol operations from RFC 1661. [More...](group__ppp.md#ga305eaed8ab120c7821de1618e10728cf) |
| enum | [lcp\_option\_type](group__ppp.md#gac8f3d915c930d61831bcb13d6201b15c) {     [LCP\_OPTION\_RESERVED](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3) = 0 , [LCP\_OPTION\_MRU](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe) = 1 , [LCP\_OPTION\_ASYNC\_CTRL\_CHAR\_MAP](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef) = 2 , [LCP\_OPTION\_AUTH\_PROTO](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743) = 3 ,     [LCP\_OPTION\_QUALITY\_PROTO](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9) = 4 , [LCP\_OPTION\_MAGIC\_NUMBER](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8) = 5 , [LCP\_OPTION\_PROTO\_COMPRESS](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4) = 7 , [LCP\_OPTION\_ADDR\_CTRL\_COMPRESS](group__ppp.md#ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524) = 8   } |
|  | LCP option types from RFC 1661 ch. [More...](group__ppp.md#gac8f3d915c930d61831bcb13d6201b15c) |
| enum | [ipcp\_option\_type](group__ppp.md#ga1064e3d8c6aa3d3161e399d6937162b6) {     [IPCP\_OPTION\_RESERVED](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b) = 0 , [IPCP\_OPTION\_IP\_ADDRESSES](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b) = 1 , [IPCP\_OPTION\_IP\_COMP\_PROTO](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6) = 2 , [IPCP\_OPTION\_IP\_ADDRESS](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9) = 3 ,     [IPCP\_OPTION\_DNS1](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931) = 129 , [IPCP\_OPTION\_NBNS1](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552) = 130 , [IPCP\_OPTION\_DNS2](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964) = 131 , [IPCP\_OPTION\_NBNS2](group__ppp.md#gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad) = 132   } |
|  | IPCP option types from RFC 1332. [More...](group__ppp.md#ga1064e3d8c6aa3d3161e399d6937162b6) |
| enum | [ipv6cp\_option\_type](group__ppp.md#gaf30172a9fead40463d129a5afeaf1ac3) { [IPV6CP\_OPTION\_RESERVED](group__ppp.md#ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858) = 0 , [IPV6CP\_OPTION\_INTERFACE\_IDENTIFIER](group__ppp.md#ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7) = 1 } |
|  | IPV6CP option types from RFC 5072. [More...](group__ppp.md#gaf30172a9fead40463d129a5afeaf1ac3) |
| enum | [ppp\_flags](group__ppp.md#ga360dc50a25d0c19b99a15807bc40d971) { [PPP\_CARRIER\_UP](group__ppp.md#gga360dc50a25d0c19b99a15807bc40d971a78506697a8a37d20d486961501ec7715) } |

| Functions | |
| --- | --- |
| void | [net\_ppp\_init](group__ppp.md#gaabf883cfefc9910b9b9d8931e68b320c) (struct [net\_if](structnet__if.md) \*iface) |
|  | Initialize PPP L2 stack for a given interface. |
| static void | [ppp\_mgmt\_raise\_carrier\_on\_event](group__ppp.md#ga1436cf5cfcb6752e41c9e06a0ee30030) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise CARRIER\_ON event when PPP is connected. |
| static void | [ppp\_mgmt\_raise\_carrier\_off\_event](group__ppp.md#gad96b2c77cf6a066d55d78c5d63cb9bd0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise CARRIER\_OFF event when PPP is disconnected. |
| static void | [ppp\_mgmt\_raise\_phase\_running\_event](group__ppp.md#ga74e94e9fcae30bc386c5e3d951ed5882) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise PHASE\_RUNNING event when PPP reaching RUNNING phase. |
| static void | [ppp\_mgmt\_raise\_phase\_dead\_event](group__ppp.md#gad7f41d9012098ed1a04f897e252cc32d) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise PHASE\_DEAD event when PPP reaching DEAD phase. |
| static int | [net\_ppp\_ping](group__ppp.md#ga9893a7c93b3d23b96b4d83aa1204c500) (int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Send PPP Echo-Request to peer. |
| static struct [ppp\_context](structppp__context.md) \* | [net\_ppp\_context\_get](group__ppp.md#ga4f6104cff735f9829762b6552a7346bf) (int idx) |
|  | Get PPP context information. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ppp.h](net_2ppp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
