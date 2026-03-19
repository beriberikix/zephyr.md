---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structdns__resolve__context_1_1dns__server.html
original_path: doxygen/html/structdns__resolve__context_1_1dns__server.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dns\_resolve\_context::dns\_server Struct Reference

List of configured DNS servers.
[More...](#details)

`#include <[dns_resolve.h](dns__resolve_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sockaddr](structsockaddr.md) | [dns\_server](#a266b91e051fd7c1b1e434e1a3ab4b5dc) |
|  | DNS server information. |
| int | [sock](#a762f6cbc4fabe1809966f62d7aa760a6) |
|  | Connection to the DNS server. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_mdns](#aaa3606fb80fa171a3b4b91fa0441129f): 1 |
|  | Is this server mDNS one. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_llmnr](#af60096f20c95a112caf4f946d898ec70): 1 |
|  | Is this server LLMNR one. |

## Detailed Description

List of configured DNS servers.

## Field Documentation

## [◆ ](#a266b91e051fd7c1b1e434e1a3ab4b5dc)dns\_server

| struct [sockaddr](structsockaddr.md) dns\_resolve\_context::dns\_server::dns\_server |
| --- |

DNS server information.

## [◆ ](#af60096f20c95a112caf4f946d898ec70)is\_llmnr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dns\_resolve\_context::dns\_server::is\_llmnr |
| --- |

Is this server LLMNR one.

## [◆ ](#aaa3606fb80fa171a3b4b91fa0441129f)is\_mdns

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dns\_resolve\_context::dns\_server::is\_mdns |
| --- |

Is this server mDNS one.

## [◆ ](#a762f6cbc4fabe1809966f62d7aa760a6)sock

| int dns\_resolve\_context::dns\_server::sock |
| --- |

Connection to the DNS server.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dns\_resolve.h](dns__resolve_8h_source.md)

- [dns\_resolve\_context](structdns__resolve__context.md)
- [dns\_server](structdns__resolve__context_1_1dns__server.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
