---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structhttp__resource__detail__websocket.html
original_path: doxygen/html/structhttp__resource__detail__websocket.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_resource\_detail\_websocket Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP server API](group__http__server.md)

Representation of a websocket server resource.
[More...](#details)

`#include <[server.h](server_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [http\_resource\_detail](structhttp__resource__detail.md) | [common](#acd10efe8ca1f82fb6e0557512f18d9ee) |
|  | Common resource details. |
| int | [ws\_sock](#adbfb331ad424fac889f5e53bb1240ed8) |
|  | Websocket socket value. |
| [http\_resource\_websocket\_cb\_t](group__http__server.md#gaa51ec52c8960a37566d2ac77d624be93) | [cb](#ad3a18df78d4ab4443bba2fbf00a0cbc0) |
|  | Resource callback used by the server to interact with the application. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data\_buffer](#af9c3292e2d450b70831812cb9d084e3c) |
|  | Data buffer used to exchanged data between server and the, application. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [data\_buffer\_len](#a512b5da3bdc20eca57c060160c823117) |
|  | Length of the data in the data buffer. |
| void \* | [user\_data](#a8f6ceaee3ccae18974fbc2c6498737c8) |
|  | A pointer to the user data registered by the application. |

## Detailed Description

Representation of a websocket server resource.

## Field Documentation

## [◆ ](#ad3a18df78d4ab4443bba2fbf00a0cbc0)cb

| [http\_resource\_websocket\_cb\_t](group__http__server.md#gaa51ec52c8960a37566d2ac77d624be93) http\_resource\_detail\_websocket::cb |
| --- |

Resource callback used by the server to interact with the application.

## [◆ ](#acd10efe8ca1f82fb6e0557512f18d9ee)common

| struct [http\_resource\_detail](structhttp__resource__detail.md) http\_resource\_detail\_websocket::common |
| --- |

Common resource details.

## [◆ ](#af9c3292e2d450b70831812cb9d084e3c)data\_buffer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* http\_resource\_detail\_websocket::data\_buffer |
| --- |

Data buffer used to exchanged data between server and the, application.

## [◆ ](#a512b5da3bdc20eca57c060160c823117)data\_buffer\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_resource\_detail\_websocket::data\_buffer\_len |
| --- |

Length of the data in the data buffer.

## [◆ ](#a8f6ceaee3ccae18974fbc2c6498737c8)user\_data

| void\* http\_resource\_detail\_websocket::user\_data |
| --- |

A pointer to the user data registered by the application.

## [◆ ](#adbfb331ad424fac889f5e53bb1240ed8)ws\_sock

| int http\_resource\_detail\_websocket::ws\_sock |
| --- |

Websocket socket value.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[server.h](server_8h_source.md)

- [http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
