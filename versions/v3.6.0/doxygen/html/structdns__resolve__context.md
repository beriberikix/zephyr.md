---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structdns__resolve__context.html
original_path: doxygen/html/structdns__resolve__context.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dns\_resolve\_context Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [DNS Resolve Library](group__dns__resolve.md)

DNS resolve context structure.
[More...](#details)

`#include <[dns_resolve.h](dns__resolve_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md) |
|  | Result callbacks. [More...](structdns__resolve__context_1_1dns__pending__query.md#details) |

| Data Fields | |
| --- | --- |
| struct { |  |
| struct [sockaddr](structsockaddr.md)   [dns\_server](#ae54aa9bc3b76924193c0846976ee089b) |  |
|  | DNS server information. [More...](#ae54aa9bc3b76924193c0846976ee089b) |
| struct [net\_context](structnet__context.md) \*   [net\_ctx](#abdc166e878040d90362366251730e6df) |  |
|  | Connection to the DNS server. [More...](#abdc166e878040d90362366251730e6df) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [is\_mdns](#aa6c01844428450cf96c306feb35d491e): 1 |  |
|  | Is this server mDNS one. [More...](#aa6c01844428450cf96c306feb35d491e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [is\_llmnr](#a503502ac58538d54fddce34e7ae71f2e): 1 |  |
|  | Is this server LLMNR one. [More...](#a503502ac58538d54fddce34e7ae71f2e) |
| } | [servers](#aade0d00fa46d1567b94491733b268d99) [CONFIG\_DNS\_RESOLVER\_MAX\_SERVERS+DNS\_MAX\_MCAST\_SERVERS] |
| struct [k\_mutex](structk__mutex.md) | [lock](#a9d1ada3ab20399f750acfee94e8e6cd7) |
|  | Prevent concurrent access. |
| [k\_timeout\_t](structk__timeout__t.md) | [buf\_timeout](#a402a4a2adfe3859f8dab749b44b7d8e6) |
|  | This timeout is also used when a buffer is required from the buffer pools. |
| struct [dns\_resolve\_context::dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md) | [queries](#a3bec79837b0bce3fd99b29bfbe1da40d) [CONFIG\_DNS\_NUM\_CONCUR\_QUERIES] |
| enum [dns\_resolve\_context\_state](group__dns__resolve.md#gaf190da074df1b14130c0af6370bbd56c) | [state](#a88f6600061cdb8e9f34802fe2a0a7d5a) |
|  | Is this context in use. |

## Detailed Description

DNS resolve context structure.

## Field Documentation

## [◆ ](#a402a4a2adfe3859f8dab749b44b7d8e6)buf\_timeout

| [k\_timeout\_t](structk__timeout__t.md) dns\_resolve\_context::buf\_timeout |
| --- |

This timeout is also used when a buffer is required from the buffer pools.

## [◆ ](#ae54aa9bc3b76924193c0846976ee089b)dns\_server

| struct [sockaddr](structsockaddr.md) dns\_resolve\_context::dns\_server |
| --- |

DNS server information.

## [◆ ](#a503502ac58538d54fddce34e7ae71f2e)is\_llmnr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dns\_resolve\_context::is\_llmnr |
| --- |

Is this server LLMNR one.

## [◆ ](#aa6c01844428450cf96c306feb35d491e)is\_mdns

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dns\_resolve\_context::is\_mdns |
| --- |

Is this server mDNS one.

## [◆ ](#a9d1ada3ab20399f750acfee94e8e6cd7)lock

| struct [k\_mutex](structk__mutex.md) dns\_resolve\_context::lock |
| --- |

Prevent concurrent access.

## [◆ ](#abdc166e878040d90362366251730e6df)net\_ctx

| struct [net\_context](structnet__context.md)\* dns\_resolve\_context::net\_ctx |
| --- |

Connection to the DNS server.

## [◆ ](#a3bec79837b0bce3fd99b29bfbe1da40d)queries

| struct [dns\_resolve\_context::dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md) dns\_resolve\_context::queries[CONFIG\_DNS\_NUM\_CONCUR\_QUERIES] |
| --- |

## [◆ ](#aade0d00fa46d1567b94491733b268d99)[struct]

| struct { ... } dns\_resolve\_context::servers[CONFIG\_DNS\_RESOLVER\_MAX\_SERVERS + DNS\_MAX\_MCAST\_SERVERS] |
| --- |

## [◆ ](#a88f6600061cdb8e9f34802fe2a0a7d5a)state

| enum [dns\_resolve\_context\_state](group__dns__resolve.md#gaf190da074df1b14130c0af6370bbd56c) dns\_resolve\_context::state |
| --- |

Is this context in use.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dns\_resolve.h](dns__resolve_8h_source.md)

- [dns\_resolve\_context](structdns__resolve__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
