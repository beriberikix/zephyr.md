---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__l2.html
original_path: doxygen/html/structnet__l2.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_l2 Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network L2 Abstraction Layer](group__net__l2.md)

Network L2 structure.
[More...](#details)

`#include <[net_l2.h](net__l2_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* | [recv](#a1faa6e5b0c9228dd52c64fc7f2fd8036) )(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | This function is used by net core to get iface's L2 layer parsing what's relevant to itself. |
| int(\* | [send](#a17d649732c3bb6bf9cc77a4939eb8801) )(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | This function is used by net core to push a packet to lower layer (interface's L2), which in turn might work on the packet relevantly. |
| int(\* | [enable](#a5d42c51eb8dc4d6a990aa9ff88a66b94) )(struct [net\_if](structnet__if.md) \*iface, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | This function is used to enable/disable traffic over a network interface. |
| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)(\* | [get\_flags](#a492c5c75801b9c8784c9322805869334) )(struct [net\_if](structnet__if.md) \*iface) |
|  | Return L2 flags for the network interface. |

## Detailed Description

Network L2 structure.

Used to provide an interface to lower network stack.

## Field Documentation

## [◆ ](#a5d42c51eb8dc4d6a990aa9ff88a66b94)enable

| int(\* net\_l2::enable) (struct [net\_if](structnet__if.md) \*iface, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

This function is used to enable/disable traffic over a network interface.

The function returns <0 if error and >=0 if no error.

## [◆ ](#a492c5c75801b9c8784c9322805869334)get\_flags

| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516)(\* net\_l2::get\_flags) (struct [net\_if](structnet__if.md) \*iface) |
| --- |

Return L2 flags for the network interface.

## [◆ ](#a1faa6e5b0c9228dd52c64fc7f2fd8036)recv

| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* net\_l2::recv) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

This function is used by net core to get iface's L2 layer parsing what's relevant to itself.

## [◆ ](#a17d649732c3bb6bf9cc77a4939eb8801)send

| int(\* net\_l2::send) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

This function is used by net core to push a packet to lower layer (interface's L2), which in turn might work on the packet relevantly.

(adding proper header etc...) Returns a negative error code, or the number of bytes sent otherwise.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_l2.h](net__l2_8h_source.md)

- [net\_l2](structnet__l2.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
