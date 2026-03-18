---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsocketcan__frame.html
original_path: doxygen/html/structsocketcan__frame.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socketcan\_frame Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Core Library](group__socket__can.md)

CAN frame for Linux SocketCAN compatibility.
[More...](#details)

`#include <[socketcan.h](socketcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) | [can\_id](#a43511a491c9b8cf63b4ff592eb77a6e6) |
|  | 32-bit CAN ID + EFF/RTR/ERR flags. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#aa21e8007363ab0183c7b9d6c59cb4731) |
|  | Frame payload length in bytes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#af9ddb322cdc3d886182cce65f673177d) |
|  | Additional flags for CAN FD. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a4ab22ff419e3c7397c64a1309cbdb623) [8U] |
|  | The payload data. |

## Detailed Description

CAN frame for Linux SocketCAN compatibility.

## Field Documentation

## [◆ ](#a43511a491c9b8cf63b4ff592eb77a6e6)can\_id

| [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) socketcan\_frame::can\_id |
| --- |

32-bit CAN ID + EFF/RTR/ERR flags.

## [◆ ](#a4ab22ff419e3c7397c64a1309cbdb623)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) socketcan\_frame::data[8U] |
| --- |

The payload data.

## [◆ ](#af9ddb322cdc3d886182cce65f673177d)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) socketcan\_frame::flags |
| --- |

Additional flags for CAN FD.

## [◆ ](#aa21e8007363ab0183c7b9d6c59cb4731)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) socketcan\_frame::len |
| --- |

Frame payload length in bytes.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socketcan.h](socketcan_8h_source.md)

- [socketcan\_frame](structsocketcan__frame.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
