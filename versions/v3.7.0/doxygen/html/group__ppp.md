---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__ppp.html
original_path: doxygen/html/group__ppp.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PPP L2/driver Support Functions

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Point-to-point (PPP) L2/driver support functions.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ppp\_api](structppp__api.md) |
|  | PPP L2 API. [More...](structppp__api.md#details) |
| struct | [ppp\_fsm](structppp__fsm.md) |
|  | Generic PPP Finite State Machine. [More...](structppp__fsm.md#details) |
| struct | [lcp\_options](structlcp__options.md) |
|  | Link control protocol options. [More...](structlcp__options.md#details) |
| struct | [ipcp\_options](structipcp__options.md) |
|  | IPv4 control protocol options. [More...](structipcp__options.md#details) |
| struct | [ipv6cp\_options](structipv6cp__options.md) |
|  | IPv6 control protocol options. [More...](structipv6cp__options.md#details) |
| struct | [ppp\_context](structppp__context.md) |
|  | PPP L2 context specific to certain network interface. [More...](structppp__context.md#details) |

| Macros | |
| --- | --- |
| #define | [PPP\_MRU](#gaec050624f0693600196068d8f5413e6f)   CONFIG\_NET\_PPP\_MTU\_MRU |
|  | PPP maximum receive unit (MRU). |
| #define | [PPP\_MTU](#gacc51e91347721a8255ae891ddc43636b)   [PPP\_MRU](#gaec050624f0693600196068d8f5413e6f) |
|  | PPP maximum transfer unit (MTU). |
| #define | [PPP\_MAX\_TERMINATE\_REASON\_LEN](#ga2e5d0ae66bf076123cb29effc0a8e894)   32 |
|  | Max length of terminate description string. |
| #define | [PPP\_INTERFACE\_IDENTIFIER\_LEN](#gaad7380b3a502f4b649348b733124f21a)   8 |
|  | Length of network interface identifier. |
| #define | [NET\_EVENT\_PPP\_CARRIER\_ON](#ga17c4e8cc92e0e9261d0b2dcc704b2f93)   (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_CARRIER\_ON) |
|  | Event emitted when PPP carrier is on. |
| #define | [NET\_EVENT\_PPP\_CARRIER\_OFF](#ga2b3c11bbdc7b36d4381811b210340e45)   (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_CARRIER\_OFF) |
|  | Event emitted when PPP carrier is off. |
| #define | [NET\_EVENT\_PPP\_PHASE\_RUNNING](#ga4853534532ac4875321785a70c5a1b19)   (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_PHASE\_RUNNING) |
|  | Event emitted when PPP goes into running phase. |
| #define | [NET\_EVENT\_PPP\_PHASE\_DEAD](#ga7aa5d07daa3f8bb45cf1bd0c30c6fc7a)   (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_PHASE\_DEAD) |
|  | Event emitted when PPP goes into dead phase. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_ppp\_lcp\_echo\_reply\_cb\_t](#ga15afa05abc0446201c912c75644306bf)) (void \*user\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) user\_data\_len) |
|  | A callback function that can be called if a Echo-Reply needs to be received. |

| Enumerations | |
| --- | --- |
| enum | [ppp\_protocol\_type](#ga8ad7cc0d142a6e7ea82c45bec2cc3670) {     [PPP\_IP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0b974fd7b99c28a8d06f096be1ed9cc6) = 0x0021 , [PPP\_IPV6](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a0a9da56ae134b701f5a8b31c3f1c9bfe) = 0x0057 , [PPP\_IPCP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a25f326220ab531e93140b7c6bddd0d21) = 0x8021 , [PPP\_ECP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a40b5032dabf9c697e761aa2cff0b2e44) = 0x8053 ,     [PPP\_IPV6CP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670ab17a70f864ac04b8b52f8ca1edc4d2e0) = 0x8057 , [PPP\_CCP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a4cdde6fe10fcfa862742751e1152887b) = 0x80FD , [PPP\_LCP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a22dae8ee345f9664042eef54086f4de9) = 0xc021 , [PPP\_PAP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670ac66b190ff6dd0884dfba62da40ee2206) = 0xc023 ,     [PPP\_CHAP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a1b311302ecabb507c34b1f77cba36f25) = 0xc223 , [PPP\_EAP](#gga8ad7cc0d142a6e7ea82c45bec2cc3670a7a51ef2d8d979ded98e0aad680f1b6e2) = 0xc227   } |
|  | PPP protocol types. [More...](#ga8ad7cc0d142a6e7ea82c45bec2cc3670) |
| enum | [ppp\_phase](#ga284e237a6323f2daffc444a73a4b8b6b) {     [PPP\_DEAD](#gga284e237a6323f2daffc444a73a4b8b6babdff682a09630e713867c3241d56954d) , [PPP\_ESTABLISH](#gga284e237a6323f2daffc444a73a4b8b6ba647d283023ee50299c1d9ca376cce4f4) , [PPP\_AUTH](#gga284e237a6323f2daffc444a73a4b8b6ba0492bfbaebc3f126327c74dbe56ce76a) , [PPP\_NETWORK](#gga284e237a6323f2daffc444a73a4b8b6ba621902d0a6ca3efa0aa20c43c32164af) ,     [PPP\_RUNNING](#gga284e237a6323f2daffc444a73a4b8b6ba51a5c6e5d16fbb607597f0d2f6a12af7) , [PPP\_TERMINATE](#gga284e237a6323f2daffc444a73a4b8b6bac1f10a2aa5edcb826621304de596a5b7)   } |
|  | PPP phases. [More...](#ga284e237a6323f2daffc444a73a4b8b6b) |
| enum | [lcp\_option\_type](#gac8f3d915c930d61831bcb13d6201b15c) {     [LCP\_OPTION\_RESERVED](#ggac8f3d915c930d61831bcb13d6201b15caa702a3993d2a8f7d7878e1c6f43772d3) = 0 , [LCP\_OPTION\_MRU](#ggac8f3d915c930d61831bcb13d6201b15cabedb2479b9edd3fcefe7a84d2deb41fe) = 1 , [LCP\_OPTION\_ASYNC\_CTRL\_CHAR\_MAP](#ggac8f3d915c930d61831bcb13d6201b15ca01e51712c002e5ce746d93376b4f2cef) = 2 , [LCP\_OPTION\_AUTH\_PROTO](#ggac8f3d915c930d61831bcb13d6201b15cae36a806e93ebdacd7c3ad3f536c03743) = 3 ,     [LCP\_OPTION\_QUALITY\_PROTO](#ggac8f3d915c930d61831bcb13d6201b15ca3ed6d42c4b65271955a308c4e7a437a9) = 4 , [LCP\_OPTION\_MAGIC\_NUMBER](#ggac8f3d915c930d61831bcb13d6201b15ca59c791ebec909b03a42659d08be2bcf8) = 5 , [LCP\_OPTION\_PROTO\_COMPRESS](#ggac8f3d915c930d61831bcb13d6201b15cab135e1ef16bb071e1490d77b51de3bd4) = 7 , [LCP\_OPTION\_ADDR\_CTRL\_COMPRESS](#ggac8f3d915c930d61831bcb13d6201b15ca3c37fd8819b98caa7f9b3b94aff53524) = 8   } |
|  | LCP option types from RFC 1661 ch. [More...](#gac8f3d915c930d61831bcb13d6201b15c) |
| enum | [ipcp\_option\_type](#ga1064e3d8c6aa3d3161e399d6937162b6) {     [IPCP\_OPTION\_RESERVED](#gga1064e3d8c6aa3d3161e399d6937162b6a7319a35a35044ca3f5fcc1ed6460fb3b) = 0 , [IPCP\_OPTION\_IP\_ADDRESSES](#gga1064e3d8c6aa3d3161e399d6937162b6a80771bc5d12ab8dcf78f87c872b0f41b) = 1 , [IPCP\_OPTION\_IP\_COMP\_PROTO](#gga1064e3d8c6aa3d3161e399d6937162b6a3913e2668196db10d17f8d7ffa86c6a6) = 2 , [IPCP\_OPTION\_IP\_ADDRESS](#gga1064e3d8c6aa3d3161e399d6937162b6a124bafb002549c2de4cb293f5e158fd9) = 3 ,     [IPCP\_OPTION\_DNS1](#gga1064e3d8c6aa3d3161e399d6937162b6af156d53ee18de3907210c910667e8931) = 129 , [IPCP\_OPTION\_NBNS1](#gga1064e3d8c6aa3d3161e399d6937162b6a7d154ff3643ba4de8cf358bd81361552) = 130 , [IPCP\_OPTION\_DNS2](#gga1064e3d8c6aa3d3161e399d6937162b6a176055a8c0483c7c8b6b0d416b676964) = 131 , [IPCP\_OPTION\_NBNS2](#gga1064e3d8c6aa3d3161e399d6937162b6a3b315dc4f10305923bba2bfbe2fa05ad) = 132   } |
|  | IPCP option types from RFC 1332. [More...](#ga1064e3d8c6aa3d3161e399d6937162b6) |
| enum | [ipv6cp\_option\_type](#gaf30172a9fead40463d129a5afeaf1ac3) { [IPV6CP\_OPTION\_RESERVED](#ggaf30172a9fead40463d129a5afeaf1ac3ac291788404cda3f6c30130d097d43858) = 0 , [IPV6CP\_OPTION\_INTERFACE\_IDENTIFIER](#ggaf30172a9fead40463d129a5afeaf1ac3a0448dc4b9a89736d6878a4e99e6e61b7) = 1 } |
|  | IPV6CP option types from RFC 5072. [More...](#gaf30172a9fead40463d129a5afeaf1ac3) |

| Functions | |
| --- | --- |
| void | [net\_ppp\_init](#gaabf883cfefc9910b9b9d8931e68b320c) (struct [net\_if](structnet__if.md) \*iface) |
|  | Initialize PPP L2 stack for a given interface. |
| static void | [ppp\_mgmt\_raise\_carrier\_on\_event](#ga1436cf5cfcb6752e41c9e06a0ee30030) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise CARRIER\_ON event when PPP is connected. |
| static void | [ppp\_mgmt\_raise\_carrier\_off\_event](#gad96b2c77cf6a066d55d78c5d63cb9bd0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise CARRIER\_OFF event when PPP is disconnected. |
| static void | [ppp\_mgmt\_raise\_phase\_running\_event](#ga74e94e9fcae30bc386c5e3d951ed5882) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise PHASE\_RUNNING event when PPP reaching RUNNING phase. |
| static void | [ppp\_mgmt\_raise\_phase\_dead\_event](#gad7f41d9012098ed1a04f897e252cc32d) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise PHASE\_DEAD event when PPP reaching DEAD phase. |
| static int | [net\_ppp\_ping](#ga9893a7c93b3d23b96b4d83aa1204c500) (int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Send PPP Echo-Request to peer. |
| static struct [ppp\_context](structppp__context.md) \* | [net\_ppp\_context\_get](#ga4f6104cff735f9829762b6552a7346bf) (int idx) |
|  | Get PPP context information. |

## Detailed Description

Point-to-point (PPP) L2/driver support functions.

## Macro Definition Documentation

## [◆ ](#ga2b3c11bbdc7b36d4381811b210340e45)NET\_EVENT\_PPP\_CARRIER\_OFF

| #define NET\_EVENT\_PPP\_CARRIER\_OFF   (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_CARRIER\_OFF) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Event emitted when PPP carrier is off.

## [◆ ](#ga17c4e8cc92e0e9261d0b2dcc704b2f93)NET\_EVENT\_PPP\_CARRIER\_ON

| #define NET\_EVENT\_PPP\_CARRIER\_ON   (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_CARRIER\_ON) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Event emitted when PPP carrier is on.

## [◆ ](#ga7aa5d07daa3f8bb45cf1bd0c30c6fc7a)NET\_EVENT\_PPP\_PHASE\_DEAD

| #define NET\_EVENT\_PPP\_PHASE\_DEAD   (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_PHASE\_DEAD) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Event emitted when PPP goes into dead phase.

## [◆ ](#ga4853534532ac4875321785a70c5a1b19)NET\_EVENT\_PPP\_PHASE\_RUNNING

| #define NET\_EVENT\_PPP\_PHASE\_RUNNING   (\_NET\_PPP\_EVENT | NET\_EVENT\_PPP\_CMD\_PHASE\_RUNNING) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Event emitted when PPP goes into running phase.

## [◆ ](#gaad7380b3a502f4b649348b733124f21a)PPP\_INTERFACE\_IDENTIFIER\_LEN

| #define PPP\_INTERFACE\_IDENTIFIER\_LEN   8 |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Length of network interface identifier.

## [◆ ](#ga2e5d0ae66bf076123cb29effc0a8e894)PPP\_MAX\_TERMINATE\_REASON\_LEN

| #define PPP\_MAX\_TERMINATE\_REASON\_LEN   32 |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Max length of terminate description string.

## [◆ ](#gaec050624f0693600196068d8f5413e6f)PPP\_MRU

| #define PPP\_MRU   CONFIG\_NET\_PPP\_MTU\_MRU |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

PPP maximum receive unit (MRU).

## [◆ ](#gacc51e91347721a8255ae891ddc43636b)PPP\_MTU

| #define PPP\_MTU   [PPP\_MRU](#gaec050624f0693600196068d8f5413e6f) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

PPP maximum transfer unit (MTU).

## Typedef Documentation

## [◆ ](#ga15afa05abc0446201c912c75644306bf)net\_ppp\_lcp\_echo\_reply\_cb\_t

| typedef void(\* net\_ppp\_lcp\_echo\_reply\_cb\_t) (void \*user\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) user\_data\_len) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

A callback function that can be called if a Echo-Reply needs to be received.

Parameters
:   | user\_data | User settable data that is passed to the callback function. |
    | --- | --- |
    | user\_data\_len | Length of the user data. |

## Enumeration Type Documentation

## [◆ ](#ga1064e3d8c6aa3d3161e399d6937162b6)ipcp\_option\_type

| enum [ipcp\_option\_type](#ga1064e3d8c6aa3d3161e399d6937162b6) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

IPCP option types from RFC 1332.

| Enumerator | |
| --- | --- |
| IPCP\_OPTION\_RESERVED | Reserved IPCP option value (do not use). |
| IPCP\_OPTION\_IP\_ADDRESSES | IP Addresses. |
| IPCP\_OPTION\_IP\_COMP\_PROTO | IP Compression Protocol. |
| IPCP\_OPTION\_IP\_ADDRESS | IP Address. |
| IPCP\_OPTION\_DNS1 | Primary DNS Server Address. |
| IPCP\_OPTION\_NBNS1 | Primary NBNS Server Address. |
| IPCP\_OPTION\_DNS2 | Secondary DNS Server Address. |
| IPCP\_OPTION\_NBNS2 | Secondary NBNS Server Address. |

## [◆ ](#gaf30172a9fead40463d129a5afeaf1ac3)ipv6cp\_option\_type

| enum [ipv6cp\_option\_type](#gaf30172a9fead40463d129a5afeaf1ac3) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

IPV6CP option types from RFC 5072.

| Enumerator | |
| --- | --- |
| IPV6CP\_OPTION\_RESERVED | Reserved IPV6CP option value (do not use). |
| IPV6CP\_OPTION\_INTERFACE\_IDENTIFIER | Interface identifier. |

## [◆ ](#gac8f3d915c930d61831bcb13d6201b15c)lcp\_option\_type

| enum [lcp\_option\_type](#gac8f3d915c930d61831bcb13d6201b15c) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

LCP option types from RFC 1661 ch.

6

| Enumerator | |
| --- | --- |
| LCP\_OPTION\_RESERVED | Reserved option value (do not use). |
| LCP\_OPTION\_MRU | Maximum-Receive-Unit. |
| LCP\_OPTION\_ASYNC\_CTRL\_CHAR\_MAP | Async-Control-Character-Map. |
| LCP\_OPTION\_AUTH\_PROTO | Authentication-Protocol. |
| LCP\_OPTION\_QUALITY\_PROTO | Quality-Protocol. |
| LCP\_OPTION\_MAGIC\_NUMBER | Magic-Number. |
| LCP\_OPTION\_PROTO\_COMPRESS | Protocol-Field-Compression. |
| LCP\_OPTION\_ADDR\_CTRL\_COMPRESS | Address-and-Control-Field-Compression. |

## [◆ ](#ga284e237a6323f2daffc444a73a4b8b6b)ppp\_phase

| enum [ppp\_phase](#ga284e237a6323f2daffc444a73a4b8b6b) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

PPP phases.

| Enumerator | |
| --- | --- |
| PPP\_DEAD | Physical-layer not ready. |
| PPP\_ESTABLISH | Link is being established. |
| PPP\_AUTH | Link authentication with peer. |
| PPP\_NETWORK | Network connection establishment. |
| PPP\_RUNNING | Network running. |
| PPP\_TERMINATE | Link termination. |

## [◆ ](#ga8ad7cc0d142a6e7ea82c45bec2cc3670)ppp\_protocol\_type

| enum [ppp\_protocol\_type](#ga8ad7cc0d142a6e7ea82c45bec2cc3670) |
| --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

PPP protocol types.

See [https://www.iana.org/assignments/ppp-numbers/ppp-numbers.xhtml](https://www.iana.org/assignments/ppp-numbers/ppp-numbers.xhtml) for details.

| Enumerator | |
| --- | --- |
| PPP\_IP | RFC 1332. |
| PPP\_IPV6 | RFC 5072. |
| PPP\_IPCP | RFC 1332. |
| PPP\_ECP | RFC 1968. |
| PPP\_IPV6CP | RFC 5072. |
| PPP\_CCP | RFC 1962. |
| PPP\_LCP | RFC 1661. |
| PPP\_PAP | RFC 1334. |
| PPP\_CHAP | RFC 1334. |
| PPP\_EAP | RFC 2284. |

## Function Documentation

## [◆ ](#ga4f6104cff735f9829762b6552a7346bf)net\_ppp\_context\_get()

| | struct [ppp\_context](structppp__context.md) \* net\_ppp\_context\_get | ( | int | *idx* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Get PPP context information.

This is only used by net-shell to print information about PPP.

Parameters
:   | idx | PPP network interface index |
    | --- | --- |

Returns
:   PPP context or NULL if idx is invalid.

## [◆ ](#gaabf883cfefc9910b9b9d8931e68b320c)net\_ppp\_init()

| void net\_ppp\_init | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Initialize PPP L2 stack for a given interface.

Parameters
:   | iface | A valid pointer to a network interface |
    | --- | --- |

## [◆ ](#ga9893a7c93b3d23b96b4d83aa1204c500)net\_ppp\_ping()

| | int net\_ppp\_ping | ( | int | *idx*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Send PPP Echo-Request to peer.

We expect to receive Echo-Reply back.

Parameters
:   | idx | PPP network interface index |
    | --- | --- |
    | timeout | Amount of time to wait Echo-Reply. The value is in milliseconds. |

Returns
:   0 if Echo-Reply was received, < 0 if there is a timeout or network index is not a valid PPP network index.

## [◆ ](#gad96b2c77cf6a066d55d78c5d63cb9bd0)ppp\_mgmt\_raise\_carrier\_off\_event()

| | void ppp\_mgmt\_raise\_carrier\_off\_event | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Raise CARRIER\_OFF event when PPP is disconnected.

Parameters
:   | iface | PPP network interface. |
    | --- | --- |

## [◆ ](#ga1436cf5cfcb6752e41c9e06a0ee30030)ppp\_mgmt\_raise\_carrier\_on\_event()

| | void ppp\_mgmt\_raise\_carrier\_on\_event | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Raise CARRIER\_ON event when PPP is connected.

Parameters
:   | iface | PPP network interface. |
    | --- | --- |

## [◆ ](#gad7f41d9012098ed1a04f897e252cc32d)ppp\_mgmt\_raise\_phase\_dead\_event()

| | void ppp\_mgmt\_raise\_phase\_dead\_event | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Raise PHASE\_DEAD event when PPP reaching DEAD phase.

Parameters
:   | iface | PPP network interface. |
    | --- | --- |

## [◆ ](#ga74e94e9fcae30bc386c5e3d951ed5882)ppp\_mgmt\_raise\_phase\_running\_event()

| | void ppp\_mgmt\_raise\_phase\_running\_event | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ppp.h](net_2ppp_8h.md)>`

Raise PHASE\_RUNNING event when PPP reaching RUNNING phase.

Parameters
:   | iface | PPP network interface. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
