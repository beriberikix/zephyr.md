---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__if__addr__ipv4.html
original_path: doxygen/html/structnet__if__addr__ipv4.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if\_addr\_ipv4 Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Interface abstraction layer](group__net__if.md)

Network Interface unicast IPv4 address and netmask.
[More...](#details)

`#include <[net_if.h](net__if_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_if\_addr](structnet__if__addr.md) | [ipv4](#a9d8924e263cc7401569c934533a04b48) |
|  | IPv4 address. |
| struct [in\_addr](structin__addr.md) | [netmask](#ae1720720e7e36ccf38d0b282d3150774) |
|  | Netmask. |

## Detailed Description

Network Interface unicast IPv4 address and netmask.

Stores the unicast IPv4 address and related netmask.

## Field Documentation

## [◆ ](#a9d8924e263cc7401569c934533a04b48)ipv4

| struct [net\_if\_addr](structnet__if__addr.md) net\_if\_addr\_ipv4::ipv4 |
| --- |

IPv4 address.

## [◆ ](#ae1720720e7e36ccf38d0b282d3150774)netmask

| struct [in\_addr](structin__addr.md) net\_if\_addr\_ipv4::netmask |
| --- |

Netmask.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_if.h](net__if_8h_source.md)

- [net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
