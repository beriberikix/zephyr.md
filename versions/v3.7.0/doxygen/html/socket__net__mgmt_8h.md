---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/socket__net__mgmt_8h.html
original_path: doxygen/html/socket__net__mgmt_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_net\_mgmt.h File Reference

NET\_MGMT socket definitions.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`

[Go to the source code of this file.](socket__net__mgmt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sockaddr\_nm](structsockaddr__nm.md) |
|  | struct [sockaddr\_nm](structsockaddr__nm.md "struct sockaddr_nm - The sockaddr structure for NET_MGMT sockets") - The sockaddr structure for NET\_MGMT sockets [More...](structsockaddr__nm.md#details) |
| struct | [net\_mgmt\_msghdr](structnet__mgmt__msghdr.md) |
|  | Each network management message is prefixed with this header. [More...](structnet__mgmt__msghdr.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_MGMT\_SOCKET\_VERSION\_1](group__socket__net__mgmt.md#ga8ae9629a7869b3214f8b2f72aef545ee)   0x0001 |
|  | Version of the message is placed to the header. |

## Detailed Description

NET\_MGMT socket definitions.

Definitions for NET\_MGMT socket support.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_net\_mgmt.h](socket__net__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
