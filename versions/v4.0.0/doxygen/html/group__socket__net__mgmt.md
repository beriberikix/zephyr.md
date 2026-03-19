---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__socket__net__mgmt.html
original_path: doxygen/html/group__socket__net__mgmt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Socket NET\_MGMT library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Socket NET\_MGMT library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [sockaddr\_nm](structsockaddr__nm.md) |
|  | struct [sockaddr\_nm](structsockaddr__nm.md "struct sockaddr_nm - The sockaddr structure for NET_MGMT sockets") - The sockaddr structure for NET\_MGMT sockets [More...](structsockaddr__nm.md#details) |
| struct | [net\_mgmt\_msghdr](structnet__mgmt__msghdr.md) |
|  | Each network management message is prefixed with this header. [More...](structnet__mgmt__msghdr.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_MGMT\_SOCKET\_VERSION\_1](#ga8ae9629a7869b3214f8b2f72aef545ee)   0x0001 |
|  | Version of the message is placed to the header. |

## Detailed Description

Socket NET\_MGMT library.

Since
:   2.0

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga8ae9629a7869b3214f8b2f72aef545ee)NET\_MGMT\_SOCKET\_VERSION\_1

| #define NET\_MGMT\_SOCKET\_VERSION\_1   0x0001 |
| --- |

`#include <[socket_net_mgmt.h](socket__net__mgmt_8h.md)>`

Version of the message is placed to the header.

Currently we have following versions.

Network management message versions:

0x0001 : The net\_mgmt event info message follows directly after the header.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
