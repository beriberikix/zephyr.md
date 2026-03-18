---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__socket__net__mgmt.html
original_path: doxygen/html/group__socket__net__mgmt.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Core Library

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
| #define | [NET\_MGMT\_EVENT\_PROTO](#gab2d2105917cbbeaed6c31b0c763da855)   0x01 |
| #define | [SOL\_NET\_MGMT\_BASE](#ga89dc8c08d137eab552835fdba3d32cb7)   100 |
| #define | [SOL\_NET\_MGMT\_RAW](#gadf2e70bb146e100d4546ab281f67741f)   ([SOL\_NET\_MGMT\_BASE](#ga89dc8c08d137eab552835fdba3d32cb7) + 1) |
| #define | [NET\_MGMT\_SOCKET\_VERSION\_1](#ga8ae9629a7869b3214f8b2f72aef545ee)   0x0001 |
|  | Version of the message is placed to the header. |

## Detailed Description

Socket NET\_MGMT library.

## Macro Definition Documentation

## [◆ ](#gab2d2105917cbbeaed6c31b0c763da855)NET\_MGMT\_EVENT\_PROTO

| #define NET\_MGMT\_EVENT\_PROTO   0x01 |
| --- |

`#include <[socket_net_mgmt.h](socket__net__mgmt_8h.md)>`

## [◆ ](#ga8ae9629a7869b3214f8b2f72aef545ee)NET\_MGMT\_SOCKET\_VERSION\_1

| #define NET\_MGMT\_SOCKET\_VERSION\_1   0x0001 |
| --- |

`#include <[socket_net_mgmt.h](socket__net__mgmt_8h.md)>`

Version of the message is placed to the header.

Currently we have following versions.

Network management message versions:

0x0001 : The net\_mgmt event info message follows directly after the header.

## [◆ ](#ga89dc8c08d137eab552835fdba3d32cb7)SOL\_NET\_MGMT\_BASE

| #define SOL\_NET\_MGMT\_BASE   100 |
| --- |

`#include <[socket_net_mgmt.h](socket__net__mgmt_8h.md)>`

## [◆ ](#gadf2e70bb146e100d4546ab281f67741f)SOL\_NET\_MGMT\_RAW

| #define SOL\_NET\_MGMT\_RAW   ([SOL\_NET\_MGMT\_BASE](#ga89dc8c08d137eab552835fdba3d32cb7) + 1) |
| --- |

`#include <[socket_net_mgmt.h](socket__net__mgmt_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
