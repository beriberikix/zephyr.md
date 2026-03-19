---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsocketcan__filter.html
original_path: doxygen/html/structsocketcan__filter.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socketcan\_filter Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [SocketCAN library](group__socket__can.md)

CAN filter for Linux SocketCAN compatibility.
[More...](#details)

`#include <[socketcan.h](socketcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) | [can\_id](#a9217950edb190dc70783d9b87676ae47) |
|  | The CAN identifier to match. |
| [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) | [can\_mask](#a841857f05f1e1a887be50d8e507a03f9) |
|  | The mask applied to *can\_id* for matching. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a84abbc2f8a18bfe2d53cacf582f9fa10) |
|  | Additional flags for FD frame filter. |

## Detailed Description

CAN filter for Linux SocketCAN compatibility.

A filter is considered a match when received\_can\_id & mask == [can\_id](#a9217950edb190dc70783d9b87676ae47) & [can\_mask](#a841857f05f1e1a887be50d8e507a03f9).

## Field Documentation

## [◆ ](#a9217950edb190dc70783d9b87676ae47)can\_id

| [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) socketcan\_filter::can\_id |
| --- |

The CAN identifier to match.

## [◆ ](#a841857f05f1e1a887be50d8e507a03f9)can\_mask

| [socketcan\_id\_t](group__socket__can.md#ga35a7941726d1e22defd8c3098391ca8e) socketcan\_filter::can\_mask |
| --- |

The mask applied to *can\_id* for matching.

## [◆ ](#a84abbc2f8a18bfe2d53cacf582f9fa10)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) socketcan\_filter::flags |
| --- |

Additional flags for FD frame filter.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socketcan.h](socketcan_8h_source.md)

- [socketcan\_filter](structsocketcan__filter.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
