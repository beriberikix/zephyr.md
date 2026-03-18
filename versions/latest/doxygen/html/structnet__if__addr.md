---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__if__addr.html
original_path: doxygen/html/structnet__if__addr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if\_addr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

Network Interface unicast IP addresses.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_addr | [address](#a06b8d2e8b5ea6d8d671800d966163763) |
|  | IP address. |
| enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) | [addr\_type](#ab4fd41001cc24615803bfabb9d48e7eb) |
|  | How the IP address was set. |
| enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) | [addr\_state](#a3106fdcf0dd2479c95efafc586217a2c) |
|  | What is the current state of the address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_infinite](#a6e799428eb0633a25e4dc3c55e3a3b8c): 1 |
|  | Is the IP address valid forever. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_used](#aed4d91ba064d24ad0d53c0960cde0352): 1 |
|  | Is this IP address used or not. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_mesh\_local](#a1db7cc6c7566baf9340dab6771ca5010): 1 |
|  | Is this IP address usage limited to the subnet (mesh) or not. |

## Detailed Description

Network Interface unicast IP addresses.

Stores the unicast IP addresses assigned to this network interface.

## Field Documentation

## [◆ ](#a3106fdcf0dd2479c95efafc586217a2c)addr\_state

| enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) net\_if\_addr::addr\_state |
| --- |

What is the current state of the address.

## [◆ ](#ab4fd41001cc24615803bfabb9d48e7eb)addr\_type

| enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) net\_if\_addr::addr\_type |
| --- |

How the IP address was set.

## [◆ ](#a06b8d2e8b5ea6d8d671800d966163763)address

| struct net\_addr net\_if\_addr::address |
| --- |

IP address.

## [◆ ](#a6e799428eb0633a25e4dc3c55e3a3b8c)is\_infinite

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_addr::is\_infinite |
| --- |

Is the IP address valid forever.

## [◆ ](#a1db7cc6c7566baf9340dab6771ca5010)is\_mesh\_local

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_addr::is\_mesh\_local |
| --- |

Is this IP address usage limited to the subnet (mesh) or not.

## [◆ ](#aed4d91ba064d24ad0d53c0960cde0352)is\_used

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_addr::is\_used |
| --- |

Is this IP address used or not.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if\_addr](structnet__if__addr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
