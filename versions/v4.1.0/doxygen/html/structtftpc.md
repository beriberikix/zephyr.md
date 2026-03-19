---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structtftpc.html
original_path: doxygen/html/structtftpc.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tftpc Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [TFTP Client library](group__tftp__client.md)

TFTP client definition to maintain information relevant to the client.
[More...](#details)

`#include <[tftp.h](tftp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sockaddr](structsockaddr.md) | [server](#a8ff9317a6bbdfac895cb1e408ae72cd9) |
|  | Socket address pointing to the remote TFTP server. |
| [tftp\_callback\_t](group__tftp__client.md#gafc2d0fd730046b0d3781362263e68ddc) | [callback](#a39a04978a6cf3826ef19993989400b60) |
|  | Event notification callback. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tftp\_buf](#a23f6f3d19493edbdc050df6d75441f92) [(512+4)] |
|  | Buffer for internal usage. |

## Detailed Description

TFTP client definition to maintain information relevant to the client.

Note
:   Application must initialize [server](#a8ff9317a6bbdfac895cb1e408ae72cd9) and [callback](#a39a04978a6cf3826ef19993989400b60) before calling GET or PUT API with the [tftpc](structtftpc.md "TFTP client definition to maintain information relevant to the client.") structure.

## Field Documentation

## [◆ ](#a39a04978a6cf3826ef19993989400b60)callback

| [tftp\_callback\_t](group__tftp__client.md#gafc2d0fd730046b0d3781362263e68ddc) tftpc::callback |
| --- |

Event notification callback.

No notification if NULL

## [◆ ](#a8ff9317a6bbdfac895cb1e408ae72cd9)server

| struct [sockaddr](structsockaddr.md) tftpc::server |
| --- |

Socket address pointing to the remote TFTP server.

## [◆ ](#a23f6f3d19493edbdc050df6d75441f92)tftp\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tftpc::tftp\_buf[(512+4)] |
| --- |

Buffer for internal usage.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[tftp.h](tftp_8h_source.md)

- [tftpc](structtftpc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
