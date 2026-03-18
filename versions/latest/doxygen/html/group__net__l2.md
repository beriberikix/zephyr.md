---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__net__l2.html
original_path: doxygen/html/group__net__l2.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network L2 Abstraction Layer

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network Layer 2 abstraction layer.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_l2](structnet__l2.md) |
|  | Network L2 structure. [More...](structnet__l2.md#details) |

| Enumerations | |
| --- | --- |
| enum | [net\_l2\_flags](#gac7db0cc6c56d371a5803873074ec2516) { [NET\_L2\_MULTICAST](#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231) = BIT(0) , [NET\_L2\_MULTICAST\_SKIP\_JOIN\_SOLICIT\_NODE](#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1) = BIT(1) , [NET\_L2\_PROMISC\_MODE](#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8) = BIT(2) , [NET\_L2\_POINT\_TO\_POINT](#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1) = BIT(3) } |
|  | L2 flags. [More...](#gac7db0cc6c56d371a5803873074ec2516) |

## Detailed Description

Network Layer 2 abstraction layer.

## Enumeration Type Documentation

## [◆ ](#gac7db0cc6c56d371a5803873074ec2516)net\_l2\_flags

| enum [net\_l2\_flags](#gac7db0cc6c56d371a5803873074ec2516) |
| --- |

`#include <[net_l2.h](net__l2_8h.md)>`

L2 flags.

| Enumerator | |
| --- | --- |
| NET\_L2\_MULTICAST | IP multicast supported. |
| NET\_L2\_MULTICAST\_SKIP\_JOIN\_SOLICIT\_NODE | Do not join solicited node multicast group. |
| NET\_L2\_PROMISC\_MODE | Is promiscuous mode supported. |
| NET\_L2\_POINT\_TO\_POINT | Is this L2 point-to-point with tunneling so no need to have IP address etc to network interface. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
