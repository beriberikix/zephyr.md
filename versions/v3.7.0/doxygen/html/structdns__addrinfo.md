---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structdns__addrinfo.html
original_path: doxygen/html/structdns__addrinfo.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dns\_addrinfo Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [DNS Resolve Library](group__dns__resolve.md)

Address info struct is passed to callback that gets all the results.
[More...](#details)

`#include <[dns_resolve.h](dns__resolve_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sockaddr](structsockaddr.md) | [ai\_addr](#a254fcceb59e65cb425c19825b28c3d37) |
|  | IP address information. |
| [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | [ai\_addrlen](#ad70149a624f91ec49ac4121aba5d3799) |
|  | Length of the ai\_addr field. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ai\_family](#af9a9458751ddb65219f3b5f6730df558) |
|  | Address family of the address information. |
| char | [ai\_canonname](#a21db6675aef2f8bafb83846343eae9ce) [20+1] |
|  | Canonical name of the address. |

## Detailed Description

Address info struct is passed to callback that gets all the results.

## Field Documentation

## [◆ ](#a254fcceb59e65cb425c19825b28c3d37)ai\_addr

| struct [sockaddr](structsockaddr.md) dns\_addrinfo::ai\_addr |
| --- |

IP address information.

## [◆ ](#ad70149a624f91ec49ac4121aba5d3799)ai\_addrlen

| [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) dns\_addrinfo::ai\_addrlen |
| --- |

Length of the ai\_addr field.

## [◆ ](#a21db6675aef2f8bafb83846343eae9ce)ai\_canonname

| char dns\_addrinfo::ai\_canonname[20+1] |
| --- |

Canonical name of the address.

## [◆ ](#af9a9458751ddb65219f3b5f6730df558)ai\_family

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dns\_addrinfo::ai\_family |
| --- |

Address family of the address information.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dns\_resolve.h](dns__resolve_8h_source.md)

- [dns\_addrinfo](structdns__addrinfo.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
