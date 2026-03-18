---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__lldp.html
original_path: doxygen/html/group__lldp.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Link Layer Discovery Protocol definitions and helpers

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

LLDP definitions and helpers.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_lldp\_chassis\_tlv](structnet__lldp__chassis__tlv.md) |
|  | Chassis ID TLV, see chapter 8.5.2 in IEEE 802.1AB. [More...](structnet__lldp__chassis__tlv.md#details) |
| struct | [net\_lldp\_port\_tlv](structnet__lldp__port__tlv.md) |
|  | Port ID TLV, see chapter 8.5.3 in IEEE 802.1AB. [More...](structnet__lldp__port__tlv.md#details) |
| struct | [net\_lldp\_time\_to\_live\_tlv](structnet__lldp__time__to__live__tlv.md) |
|  | Time To Live TLV, see chapter 8.5.4 in IEEE 802.1AB. [More...](structnet__lldp__time__to__live__tlv.md#details) |
| struct | [net\_lldpdu](structnet__lldpdu.md) |
|  | LLDP Data Unit (LLDPDU) shall contain the following ordered TLVs as stated in "8.2 LLDPDU format" from the IEEE 802.1AB. [More...](structnet__lldpdu.md#details) |

| Macros | |
| --- | --- |
| #define | [net\_lldp\_set\_lldpdu](#ga961bc59567ffa2d5a4d21290d1d78407)(iface) |
|  | Set LLDP protocol data unit (LLDPDU) for the network interface. |
| #define | [net\_lldp\_unset\_lldpdu](#gafdd1b4cea9f560597c31a0e42d5341e0)(iface) |
|  | Unset LLDP protocol data unit (LLDPDU) for the network interface. |

| Typedefs | |
| --- | --- |
| typedef enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* | [net\_lldp\_recv\_cb\_t](#ga1e9fb662d7cdfc3c4c68cfd0312987cf)) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | LLDP Receive packet callback. |

| Enumerations | |
| --- | --- |
| enum | [net\_lldp\_tlv\_type](#gadd4273e4fe55757729008ce081771899) {     [LLDP\_TLV\_END\_LLDPDU](#ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a) = 0 , [LLDP\_TLV\_CHASSIS\_ID](#ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6) = 1 , [LLDP\_TLV\_PORT\_ID](#ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45) = 2 , [LLDP\_TLV\_TTL](#ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c) = 3 ,     [LLDP\_TLV\_PORT\_DESC](#ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0) = 4 , [LLDP\_TLV\_SYSTEM\_NAME](#ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9) = 5 , [LLDP\_TLV\_SYSTEM\_DESC](#ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782) = 6 , [LLDP\_TLV\_SYSTEM\_CAPABILITIES](#ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521) = 7 ,     [LLDP\_TLV\_MANAGEMENT\_ADDR](#ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5) = 8 , [LLDP\_TLV\_ORG\_SPECIFIC](#ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad) = 127   } |
|  | TLV Types. [More...](#gadd4273e4fe55757729008ce081771899) |

| Functions | |
| --- | --- |
| int | [net\_lldp\_config](#ga0efa1813c537dcf02e021db60049c284) (struct [net\_if](structnet__if.md) \*iface, const struct [net\_lldpdu](structnet__lldpdu.md) \*lldpdu) |
|  | Set the LLDP data unit for a network interface. |
| int | [net\_lldp\_config\_optional](#ga9702175375a71eaab20f450291cb51ad) (struct [net\_if](structnet__if.md) \*iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tlv, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Set the Optional LLDP TLVs for a network interface. |
| void | [net\_lldp\_init](#ga38f3eff9da2f06e10defddb1776cdb37) (void) |
|  | Initialize LLDP engine. |
| int | [net\_lldp\_register\_callback](#ga61845c96c65d6df83f422a68e31162cf) (struct [net\_if](structnet__if.md) \*iface, [net\_lldp\_recv\_cb\_t](#ga1e9fb662d7cdfc3c4c68cfd0312987cf) cb) |
|  | Register LLDP Rx callback function. |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) | [net\_lldp\_recv](#gafde82841435942b1ce7cc91083c9a06f) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Parse LLDP packet. |

## Detailed Description

LLDP definitions and helpers.

## Macro Definition Documentation

## [◆ ](#ga961bc59567ffa2d5a4d21290d1d78407)net\_lldp\_set\_lldpdu

| #define net\_lldp\_set\_lldpdu | ( |  | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lldp.h](lldp_8h.md)>`

Set LLDP protocol data unit (LLDPDU) for the network interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   <0 if error, index in lldp array if iface is found there

## [◆ ](#gafdd1b4cea9f560597c31a0e42d5341e0)net\_lldp\_unset\_lldpdu

| #define net\_lldp\_unset\_lldpdu | ( |  | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lldp.h](lldp_8h.md)>`

Unset LLDP protocol data unit (LLDPDU) for the network interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

## Typedef Documentation

## [◆ ](#ga1e9fb662d7cdfc3c4c68cfd0312987cf)net\_lldp\_recv\_cb\_t

| typedef enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* net\_lldp\_recv\_cb\_t) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

`#include <[lldp.h](lldp_8h.md)>`

LLDP Receive packet callback.

Callback gets called upon receiving packet. It is responsible for freeing packet or indicating to the stack that it needs to free packet by returning correct [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896 "Net Verdict.").

Returns:

- NET\_DROP, if packet was invalid, rejected or we want the stack to free it. In this case the core stack will free the packet.
- NET\_OK, if the packet was accepted, in this case the ownership of the [net\_pkt](structnet__pkt.md "Network packet.") goes to callback and core network stack will forget it.

## Enumeration Type Documentation

## [◆ ](#gadd4273e4fe55757729008ce081771899)net\_lldp\_tlv\_type

| enum [net\_lldp\_tlv\_type](#gadd4273e4fe55757729008ce081771899) |
| --- |

`#include <[lldp.h](lldp_8h.md)>`

TLV Types.

Please refer to table 8-1 from IEEE 802.1AB standard.

| Enumerator | |
| --- | --- |
| LLDP\_TLV\_END\_LLDPDU | End Of LLDPDU (optional). |
| LLDP\_TLV\_CHASSIS\_ID | Chassis ID (mandatory). |
| LLDP\_TLV\_PORT\_ID | Port ID (mandatory). |
| LLDP\_TLV\_TTL | Time To Live (mandatory). |
| LLDP\_TLV\_PORT\_DESC | Port Description (optional). |
| LLDP\_TLV\_SYSTEM\_NAME | System Name (optional). |
| LLDP\_TLV\_SYSTEM\_DESC | System Description (optional). |
| LLDP\_TLV\_SYSTEM\_CAPABILITIES | System Capability (optional). |
| LLDP\_TLV\_MANAGEMENT\_ADDR | Management Address (optional). |
| LLDP\_TLV\_ORG\_SPECIFIC | Org specific TLVs (optional). |

## Function Documentation

## [◆ ](#ga0efa1813c537dcf02e021db60049c284)net\_lldp\_config()

| int net\_lldp\_config | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [net\_lldpdu](structnet__lldpdu.md) \* | *lldpdu* ) |

`#include <[lldp.h](lldp_8h.md)>`

Set the LLDP data unit for a network interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | lldpdu | LLDP data unit struct |

Returns
:   0 if ok, <0 if error

## [◆ ](#ga9702175375a71eaab20f450291cb51ad)net\_lldp\_config\_optional()

| int net\_lldp\_config\_optional | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *tlv*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[lldp.h](lldp_8h.md)>`

Set the Optional LLDP TLVs for a network interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | tlv | LLDP optional TLVs following mandatory part |
    | len | Length of the optional TLVs |

Returns
:   0 if ok, <0 if error

## [◆ ](#ga38f3eff9da2f06e10defddb1776cdb37)net\_lldp\_init()

| void net\_lldp\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lldp.h](lldp_8h.md)>`

Initialize LLDP engine.

## [◆ ](#gafde82841435942b1ce7cc91083c9a06f)net\_lldp\_recv()

| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) net\_lldp\_recv | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt* ) |

`#include <[lldp.h](lldp_8h.md)>`

Parse LLDP packet.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | pkt | Network packet |

Returns
:   Return the policy for network buffer

## [◆ ](#ga61845c96c65d6df83f422a68e31162cf)net\_lldp\_register\_callback()

| int net\_lldp\_register\_callback | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [net\_lldp\_recv\_cb\_t](#ga1e9fb662d7cdfc3c4c68cfd0312987cf) | *cb* ) |

`#include <[lldp.h](lldp_8h.md)>`

Register LLDP Rx callback function.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | cb | Callback function |

Returns
:   0 if ok, < 0 if error

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
