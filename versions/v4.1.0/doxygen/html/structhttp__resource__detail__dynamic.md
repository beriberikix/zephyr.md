---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structhttp__resource__detail__dynamic.html
original_path: doxygen/html/structhttp__resource__detail__dynamic.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_resource\_detail\_dynamic Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP server API](group__http__server.md)

Representation of a dynamic server resource.
[More...](#details)

`#include <[server.h](server_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [http\_resource\_detail](structhttp__resource__detail.md) | [common](#aed22a9df2725eab8fc1032903cecacab) |
|  | Common resource details. |
| [http\_resource\_dynamic\_cb\_t](group__http__server.md#ga5b74095aacd9d8f6e203ff53d908a99f) | [cb](#a9f131e0302bbdff94ae6d5147413bec7) |
|  | Resource callback used by the server to interact with the application. |
| struct [http\_client\_ctx](structhttp__client__ctx.md) \* | [holder](#aa06123f6333e561d515a3d1468ec0856) |
|  | A pointer to the client currently processing resource, used to prevent concurrent access to the resource from multiple clients. |
| void \* | [user\_data](#a8b6170c4d98efa27616d1e3132c61cd4) |
|  | A pointer to the user data registered by the application. |

## Detailed Description

Representation of a dynamic server resource.

## Field Documentation

## [◆ ](#a9f131e0302bbdff94ae6d5147413bec7)cb

| [http\_resource\_dynamic\_cb\_t](group__http__server.md#ga5b74095aacd9d8f6e203ff53d908a99f) http\_resource\_detail\_dynamic::cb |
| --- |

Resource callback used by the server to interact with the application.

## [◆ ](#aed22a9df2725eab8fc1032903cecacab)common

| struct [http\_resource\_detail](structhttp__resource__detail.md) http\_resource\_detail\_dynamic::common |
| --- |

Common resource details.

## [◆ ](#aa06123f6333e561d515a3d1468ec0856)holder

| struct [http\_client\_ctx](structhttp__client__ctx.md)\* http\_resource\_detail\_dynamic::holder |
| --- |

A pointer to the client currently processing resource, used to prevent concurrent access to the resource from multiple clients.

## [◆ ](#a8b6170c4d98efa27616d1e3132c61cd4)user\_data

| void\* http\_resource\_detail\_dynamic::user\_data |
| --- |

A pointer to the user data registered by the application.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[server.h](server_8h_source.md)

- [http\_resource\_detail\_dynamic](structhttp__resource__detail__dynamic.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
