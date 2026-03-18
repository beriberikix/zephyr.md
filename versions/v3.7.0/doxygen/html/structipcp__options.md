---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structipcp__options.html
original_path: doxygen/html/structipcp__options.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipcp\_options Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [PPP L2/driver Support Functions](group__ppp.md)

IPv4 control protocol options.
[More...](#details)

`#include <[ppp.h](net_2ppp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in\_addr](structin__addr.md) | [address](#a2d4a41b74c4a319551c003210c1e6f3d) |
|  | IPv4 address. |
| struct [in\_addr](structin__addr.md) | [dns1\_address](#a5c2b153ee9103393159a7090357df5a1) |
|  | Primary DNS server address. |
| struct [in\_addr](structin__addr.md) | [dns2\_address](#a4e9825d9c161fa318cb538ebc231dd44) |
|  | Secondary DNS server address. |

## Detailed Description

IPv4 control protocol options.

## Field Documentation

## [◆ ](#a2d4a41b74c4a319551c003210c1e6f3d)address

| struct [in\_addr](structin__addr.md) ipcp\_options::address |
| --- |

IPv4 address.

## [◆ ](#a5c2b153ee9103393159a7090357df5a1)dns1\_address

| struct [in\_addr](structin__addr.md) ipcp\_options::dns1\_address |
| --- |

Primary DNS server address.

## [◆ ](#a4e9825d9c161fa318cb538ebc231dd44)dns2\_address

| struct [in\_addr](structin__addr.md) ipcp\_options::dns2\_address |
| --- |

Secondary DNS server address.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ppp.h](net_2ppp_8h_source.md)

- [ipcp\_options](structipcp__options.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
