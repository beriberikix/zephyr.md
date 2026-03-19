---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsockaddr__can.html
original_path: doxygen/html/structsockaddr__can.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sockaddr\_can Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [SocketCAN library](group__socket__can.md)

struct [sockaddr\_can](structsockaddr__can.md "struct sockaddr_can - The sockaddr structure for CAN sockets") - The sockaddr structure for CAN sockets
[More...](#details)

`#include <[socketcan.h](socketcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | [can\_family](#ae9d8c789193e516c282a707d5a118ebc) |
|  | Address family. |
| int | [can\_ifindex](#af1586f4d4c039a7941f07c0d746a73a7) |
|  | SocketCAN network interface index. |

## Detailed Description

struct [sockaddr\_can](structsockaddr__can.md "struct sockaddr_can - The sockaddr structure for CAN sockets") - The sockaddr structure for CAN sockets

## Field Documentation

## [◆ ](#ae9d8c789193e516c282a707d5a118ebc)can\_family

| [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) sockaddr\_can::can\_family |
| --- |

Address family.

## [◆ ](#af1586f4d4c039a7941f07c0d746a73a7)can\_ifindex

| int sockaddr\_can::can\_ifindex |
| --- |

SocketCAN network interface index.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socketcan.h](socketcan_8h_source.md)

- [sockaddr\_can](structsockaddr__can.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
