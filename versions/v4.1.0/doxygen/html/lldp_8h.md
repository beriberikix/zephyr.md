---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lldp_8h.html
original_path: doxygen/html/lldp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lldp.h File Reference

LLDP definitions and handler.
[More...](#details)

[Go to the source code of this file.](lldp_8h_source.md)

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
| #define | [net\_lldp\_set\_lldpdu](group__lldp.md#ga961bc59567ffa2d5a4d21290d1d78407)(iface) |
|  | Set LLDP protocol data unit (LLDPDU) for the network interface. |
| #define | [net\_lldp\_unset\_lldpdu](group__lldp.md#gafdd1b4cea9f560597c31a0e42d5341e0)(iface) |
|  | Unset LLDP protocol data unit (LLDPDU) for the network interface. |

| Typedefs | |
| --- | --- |
| typedef enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* | [net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf)) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | LLDP Receive packet callback. |

| Enumerations | |
| --- | --- |
| enum | [net\_lldp\_tlv\_type](group__lldp.md#gadd4273e4fe55757729008ce081771899) {     [LLDP\_TLV\_END\_LLDPDU](group__lldp.md#ggadd4273e4fe55757729008ce081771899a2b7c2a5f9f23b3bd6361e09d190c859a) = 0 , [LLDP\_TLV\_CHASSIS\_ID](group__lldp.md#ggadd4273e4fe55757729008ce081771899acd8e886391d4356096db264cba5383e6) = 1 , [LLDP\_TLV\_PORT\_ID](group__lldp.md#ggadd4273e4fe55757729008ce081771899a247164e4394c67b5ebe8da8fd71dae45) = 2 , [LLDP\_TLV\_TTL](group__lldp.md#ggadd4273e4fe55757729008ce081771899af6c7e7e44b7c0a9b1466c4c124f2c12c) = 3 ,     [LLDP\_TLV\_PORT\_DESC](group__lldp.md#ggadd4273e4fe55757729008ce081771899a848167601f7bb7a21ce25bd1a79836c0) = 4 , [LLDP\_TLV\_SYSTEM\_NAME](group__lldp.md#ggadd4273e4fe55757729008ce081771899abb2ebbce9ab2e6234d443dbaa246b6d9) = 5 , [LLDP\_TLV\_SYSTEM\_DESC](group__lldp.md#ggadd4273e4fe55757729008ce081771899ab99a55a2b6620c3d77cb0aeedf135782) = 6 , [LLDP\_TLV\_SYSTEM\_CAPABILITIES](group__lldp.md#ggadd4273e4fe55757729008ce081771899a9c81c35102ccc8baa15797f69ef95521) = 7 ,     [LLDP\_TLV\_MANAGEMENT\_ADDR](group__lldp.md#ggadd4273e4fe55757729008ce081771899ab0219acd11fad13967aec8a30054cae5) = 8 , [LLDP\_TLV\_ORG\_SPECIFIC](group__lldp.md#ggadd4273e4fe55757729008ce081771899a07dee140b7ee13ec88a271fc292887ad) = 127   } |
|  | TLV Types. [More...](group__lldp.md#gadd4273e4fe55757729008ce081771899) |

| Functions | |
| --- | --- |
| int | [net\_lldp\_config](group__lldp.md#ga0efa1813c537dcf02e021db60049c284) (struct [net\_if](structnet__if.md) \*iface, const struct [net\_lldpdu](structnet__lldpdu.md) \*lldpdu) |
|  | Set the LLDP data unit for a network interface. |
| int | [net\_lldp\_config\_optional](group__lldp.md#ga9702175375a71eaab20f450291cb51ad) (struct [net\_if](structnet__if.md) \*iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tlv, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Set the Optional LLDP TLVs for a network interface. |
| void | [net\_lldp\_init](group__lldp.md#ga38f3eff9da2f06e10defddb1776cdb37) (void) |
|  | Initialize LLDP engine. |
| int | [net\_lldp\_register\_callback](group__lldp.md#ga61845c96c65d6df83f422a68e31162cf) (struct [net\_if](structnet__if.md) \*iface, [net\_lldp\_recv\_cb\_t](group__lldp.md#ga1e9fb662d7cdfc3c4c68cfd0312987cf) cb) |
|  | Register LLDP Rx callback function. |

## Detailed Description

LLDP definitions and handler.

This is not to be included by the application.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [lldp.h](lldp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
