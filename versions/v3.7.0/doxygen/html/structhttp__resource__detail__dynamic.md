---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structhttp__resource__detail__dynamic.html
original_path: doxygen/html/structhttp__resource__detail__dynamic.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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
| [http\_resource\_dynamic\_cb\_t](group__http__server.md#gace7ba97c942714d81f47c7ba860a0de2) | [cb](#a9f131e0302bbdff94ae6d5147413bec7) |
|  | Resource callback used by the server to interact with the application. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data\_buffer](#a42d25c2ca98ad617b7bddfa3669abbb6) |
|  | Data buffer used to exchanged data between server and the, application. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [data\_buffer\_len](#a75cbd941e330017ca2243087d4770f76) |
|  | Length of the data in the data buffer. |
| struct [http\_client\_ctx](structhttp__client__ctx.md) \* | [holder](#aa06123f6333e561d515a3d1468ec0856) |
|  | A pointer to the client currently processing resource, used to prevent concurrent access to the resource from multiple clients. |
| void \* | [user\_data](#a8b6170c4d98efa27616d1e3132c61cd4) |
|  | A pointer to the user data registered by the application. |

## Detailed Description

Representation of a dynamic server resource.

## Field Documentation

## [◆ ](#a9f131e0302bbdff94ae6d5147413bec7)cb

| [http\_resource\_dynamic\_cb\_t](group__http__server.md#gace7ba97c942714d81f47c7ba860a0de2) http\_resource\_detail\_dynamic::cb |
| --- |

Resource callback used by the server to interact with the application.

## [◆ ](#aed22a9df2725eab8fc1032903cecacab)common

| struct [http\_resource\_detail](structhttp__resource__detail.md) http\_resource\_detail\_dynamic::common |
| --- |

Common resource details.

## [◆ ](#a42d25c2ca98ad617b7bddfa3669abbb6)data\_buffer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* http\_resource\_detail\_dynamic::data\_buffer |
| --- |

Data buffer used to exchanged data between server and the, application.

## [◆ ](#a75cbd941e330017ca2243087d4770f76)data\_buffer\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_resource\_detail\_dynamic::data\_buffer\_len |
| --- |

Length of the data in the data buffer.

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
