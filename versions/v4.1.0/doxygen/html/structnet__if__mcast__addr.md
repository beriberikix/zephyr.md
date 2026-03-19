---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__if__mcast__addr.html
original_path: doxygen/html/structnet__if__mcast__addr.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if\_mcast\_addr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

Network Interface multicast IP addresses.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_addr | [address](#a3e470fc2eb02ac9e5d3d7d0bea0aaa69) |
|  | IP address. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [rejoin\_node](#a74db1527b3a2b614509cc43fdf7d09ef) |
|  | Rejoining multicast groups list node. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_used](#abab3e6dba72e24ef522c033d277369ca): 1 |
|  | Is this multicast IP address used or not. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_joined](#a4af9009b2f9ccc0589a9ba6dac10927b): 1 |
|  | Did we join to this group. |

## Detailed Description

Network Interface multicast IP addresses.

Stores the multicast IP addresses assigned to this network interface.

## Field Documentation

## [◆ ](#a3e470fc2eb02ac9e5d3d7d0bea0aaa69)address

| struct net\_addr net\_if\_mcast\_addr::address |
| --- |

IP address.

## [◆ ](#a4af9009b2f9ccc0589a9ba6dac10927b)is\_joined

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_mcast\_addr::is\_joined |
| --- |

Did we join to this group.

## [◆ ](#abab3e6dba72e24ef522c033d277369ca)is\_used

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_mcast\_addr::is\_used |
| --- |

Is this multicast IP address used or not.

## [◆ ](#a74db1527b3a2b614509cc43fdf7d09ef)rejoin\_node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) net\_if\_mcast\_addr::rejoin\_node |
| --- |

Rejoining multicast groups list node.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if\_mcast\_addr](structnet__if__mcast__addr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
