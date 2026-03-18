---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structdns__resolve__context.html
original_path: doxygen/html/structdns__resolve__context.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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
| struct | [dns\_server](structdns__resolve__context_1_1dns__server.md) |
|  | List of configured DNS servers. [More...](structdns__resolve__context_1_1dns__server.md#details) |
| struct | [dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md) |
|  | Result callbacks. [More...](structdns__resolve__context_1_1dns__pending__query.md#details) |

| Data Fields | |
| --- | --- |
| struct [dns\_resolve\_context::dns\_server](structdns__resolve__context_1_1dns__server.md) | [servers](#a81becba86317bbd32d384ff2e677c829) [DNS\_RESOLVER\_MAX\_POLL] |
| struct [k\_mutex](structk__mutex.md) | [lock](#a9d1ada3ab20399f750acfee94e8e6cd7) |
|  | Prevent concurrent access. |
| [k\_timeout\_t](structk__timeout__t.md) | [buf\_timeout](#a402a4a2adfe3859f8dab749b44b7d8e6) |
|  | This timeout is also used when a buffer is required from the buffer pools. |
| struct [dns\_resolve\_context::dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md) | [queries](#a596053473b44be4977947632a1abb51e) [DNS\_NUM\_CONCUR\_QUERIES] |
| enum dns\_resolve\_context\_state | [state](#a88f6600061cdb8e9f34802fe2a0a7d5a) |
|  | Is this context in use. |

## Detailed Description

DNS resolve context structure.

## Field Documentation

## [◆ ](#a402a4a2adfe3859f8dab749b44b7d8e6)buf\_timeout

| [k\_timeout\_t](structk__timeout__t.md) dns\_resolve\_context::buf\_timeout |
| --- |

This timeout is also used when a buffer is required from the buffer pools.

## [◆ ](#a9d1ada3ab20399f750acfee94e8e6cd7)lock

| struct [k\_mutex](structk__mutex.md) dns\_resolve\_context::lock |
| --- |

Prevent concurrent access.

## [◆ ](#a596053473b44be4977947632a1abb51e)queries

| struct [dns\_resolve\_context::dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md) dns\_resolve\_context::queries[DNS\_NUM\_CONCUR\_QUERIES] |
| --- |

## [◆ ](#a81becba86317bbd32d384ff2e677c829)servers

| struct [dns\_resolve\_context::dns\_server](structdns__resolve__context_1_1dns__server.md) dns\_resolve\_context::servers[DNS\_RESOLVER\_MAX\_POLL] |
| --- |

## [◆ ](#a88f6600061cdb8e9f34802fe2a0a7d5a)state

| enum dns\_resolve\_context\_state dns\_resolve\_context::state |
| --- |

Is this context in use.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dns\_resolve.h](dns__resolve_8h_source.md)

- [dns\_resolve\_context](structdns__resolve__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
