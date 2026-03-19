---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structppp__context.html
original_path: doxygen/html/structppp__context.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ppp\_context Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [PPP L2/driver Support Functions](group__ppp.md)

PPP L2 context specific to certain network interface.
[More...](#details)

`#include <[ppp.h](net_2ppp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [flags](#a6b327cafe07a0807163589471a9bdae8) |
|  | Flags representing PPP state, which are accessed from multiple threads. |
| struct [k\_work\_delayable](structk__work__delayable.md) | [startup](#a5671d7ba465c424004f0460e5ed0d3ba) |
|  | PPP startup worker. |
| struct { |  |
| struct [ppp\_fsm](structppp__fsm.md)   [fsm](#ac555024228a1e1d830c915a098428bc5) |  |
|  | Finite state machine for LCP. [More...](#ac555024228a1e1d830c915a098428bc5) |
| struct [lcp\_options](structlcp__options.md)   [my\_options](#a37f609192ee6b739d7018d5a07ce179f) |  |
|  | Options that we want to request. [More...](#a37f609192ee6b739d7018d5a07ce179f) |
| struct [lcp\_options](structlcp__options.md)   [peer\_options](#a80fffd30b145b0842e36299ac78d5da8) |  |
|  | Options that peer want to request. [More...](#a80fffd30b145b0842e36299ac78d5da8) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [magic](#a4d91bf9e6e36415b13be02ccf03d3e40) |  |
|  | Magic-Number value. [More...](#a4d91bf9e6e36415b13be02ccf03d3e40) |
| } | [lcp](#a7705aedba900cf1de66b02ad488b7161) |
|  | LCP options. |
| struct [net\_if](structnet__if.md) \* | [iface](#a3b0bfb9c3ceece34565b282efa74390e) |
|  | Network interface related to this PPP connection. |
| struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) | [mgmt\_evt\_cb](#a141cb0b4f4b99313de63a5bff2b7cafc) |
|  | Network management callback structure. |
| enum [ppp\_phase](group__ppp.md#ga284e237a6323f2daffc444a73a4b8b6b) | [phase](#a6afb964ef87696fdadb5cb0c714bd841) |
|  | Current phase of PPP link. |
| struct k\_sem | [wait\_ppp\_link\_terminated](#a1afa42c99b098407f8bba11e50178c84) |
|  | Signal when PPP link is terminated. |
| struct k\_sem | [wait\_ppp\_link\_down](#ae784688e2d78f7427c6672583e326d94) |
|  | Signal when PPP link is down. |
| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) | [ppp\_l2\_flags](#a1c6674bad19047abcc3097bf5ff5f31d) |
|  | This tells what features the PPP supports. |
| int | [network\_protos\_open](#a2e04c6e411fe5b07d9d2cda1a61db57f) |
|  | This tells how many network protocols are open. |
| int | [network\_protos\_up](#a9dd6e156897c53d488344bbbe05d4ae1) |
|  | This tells how many network protocols are up. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [is\_ready\_to\_serve](#a3d97c93b183ca455daf0e3bc2b9c25e1): 1 |
|  | Is PPP ready to receive packets. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [is\_enabled](#a7f103857c7412a6ee9471b6c67baea71): 1 |
|  | Is PPP L2 enabled or not. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [is\_enable\_done](#acdee16f229cb6aa0672630de1d3ee39b): 1 |
|  | PPP enable pending. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [is\_ipcp\_up](#a861216f943c5af5d5db58f10ba4263ac): 1 |
|  | IPCP status (up / down). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [is\_ipcp\_open](#a7ef9ac6bb1f86ea417032fe93fc7e8a0): 1 |
|  | IPCP open status (open / closed). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [is\_ipv6cp\_up](#a7b4ee6988626cb69c012a0b58c27bef5): 1 |
|  | IPV6CP status (up / down). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [is\_ipv6cp\_open](#ab139c8d6f1d16c702cb9ca92a7f82178): 1 |
|  | IPV6CP open status (open / closed). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [is\_pap\_up](#a52227a05ce8a63f3a4f7535e60fdf979): 1 |
|  | PAP status (up / down). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [is\_pap\_open](#a80c2c3248c47fac7fce8d463cfbc0c9f): 1 |
|  | PAP open status (open / closed). |

## Detailed Description

PPP L2 context specific to certain network interface.

## Field Documentation

## [◆ ](#a6b327cafe07a0807163589471a9bdae8)flags

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) ppp\_context::flags |
| --- |

Flags representing PPP state, which are accessed from multiple threads.

## [◆ ](#ac555024228a1e1d830c915a098428bc5)fsm

| struct [ppp\_fsm](structppp__fsm.md) ppp\_context::fsm |
| --- |

Finite state machine for LCP.

## [◆ ](#a3b0bfb9c3ceece34565b282efa74390e)iface

| struct [net\_if](structnet__if.md)\* ppp\_context::iface |
| --- |

Network interface related to this PPP connection.

## [◆ ](#acdee16f229cb6aa0672630de1d3ee39b)is\_enable\_done

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ppp\_context::is\_enable\_done |
| --- |

PPP enable pending.

## [◆ ](#a7f103857c7412a6ee9471b6c67baea71)is\_enabled

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ppp\_context::is\_enabled |
| --- |

Is PPP L2 enabled or not.

## [◆ ](#a7ef9ac6bb1f86ea417032fe93fc7e8a0)is\_ipcp\_open

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ppp\_context::is\_ipcp\_open |
| --- |

IPCP open status (open / closed).

## [◆ ](#a861216f943c5af5d5db58f10ba4263ac)is\_ipcp\_up

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ppp\_context::is\_ipcp\_up |
| --- |

IPCP status (up / down).

## [◆ ](#ab139c8d6f1d16c702cb9ca92a7f82178)is\_ipv6cp\_open

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ppp\_context::is\_ipv6cp\_open |
| --- |

IPV6CP open status (open / closed).

## [◆ ](#a7b4ee6988626cb69c012a0b58c27bef5)is\_ipv6cp\_up

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ppp\_context::is\_ipv6cp\_up |
| --- |

IPV6CP status (up / down).

## [◆ ](#a80c2c3248c47fac7fce8d463cfbc0c9f)is\_pap\_open

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ppp\_context::is\_pap\_open |
| --- |

PAP open status (open / closed).

## [◆ ](#a52227a05ce8a63f3a4f7535e60fdf979)is\_pap\_up

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ppp\_context::is\_pap\_up |
| --- |

PAP status (up / down).

## [◆ ](#a3d97c93b183ca455daf0e3bc2b9c25e1)is\_ready\_to\_serve

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ppp\_context::is\_ready\_to\_serve |
| --- |

Is PPP ready to receive packets.

## [◆ ](#a7705aedba900cf1de66b02ad488b7161)[struct]

| struct { ... } ppp\_context::lcp |
| --- |

LCP options.

## [◆ ](#a4d91bf9e6e36415b13be02ccf03d3e40)magic

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ppp\_context::magic |
| --- |

Magic-Number value.

## [◆ ](#a141cb0b4f4b99313de63a5bff2b7cafc)mgmt\_evt\_cb

| struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) ppp\_context::mgmt\_evt\_cb |
| --- |

Network management callback structure.

## [◆ ](#a37f609192ee6b739d7018d5a07ce179f)my\_options

| struct [lcp\_options](structlcp__options.md) ppp\_context::my\_options |
| --- |

Options that we want to request.

## [◆ ](#a2e04c6e411fe5b07d9d2cda1a61db57f)network\_protos\_open

| int ppp\_context::network\_protos\_open |
| --- |

This tells how many network protocols are open.

## [◆ ](#a9dd6e156897c53d488344bbbe05d4ae1)network\_protos\_up

| int ppp\_context::network\_protos\_up |
| --- |

This tells how many network protocols are up.

## [◆ ](#a80fffd30b145b0842e36299ac78d5da8)peer\_options

| struct [lcp\_options](structlcp__options.md) ppp\_context::peer\_options |
| --- |

Options that peer want to request.

## [◆ ](#a6afb964ef87696fdadb5cb0c714bd841)phase

| enum [ppp\_phase](group__ppp.md#ga284e237a6323f2daffc444a73a4b8b6b) ppp\_context::phase |
| --- |

Current phase of PPP link.

## [◆ ](#a1c6674bad19047abcc3097bf5ff5f31d)ppp\_l2\_flags

| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) ppp\_context::ppp\_l2\_flags |
| --- |

This tells what features the PPP supports.

## [◆ ](#a5671d7ba465c424004f0460e5ed0d3ba)startup

| struct [k\_work\_delayable](structk__work__delayable.md) ppp\_context::startup |
| --- |

PPP startup worker.

## [◆ ](#ae784688e2d78f7427c6672583e326d94)wait\_ppp\_link\_down

| struct k\_sem ppp\_context::wait\_ppp\_link\_down |
| --- |

Signal when PPP link is down.

## [◆ ](#a1afa42c99b098407f8bba11e50178c84)wait\_ppp\_link\_terminated

| struct k\_sem ppp\_context::wait\_ppp\_link\_terminated |
| --- |

Signal when PPP link is terminated.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ppp.h](net_2ppp_8h_source.md)

- [ppp\_context](structppp__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
