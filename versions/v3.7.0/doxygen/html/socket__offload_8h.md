---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/socket__offload_8h.html
original_path: doxygen/html/socket__offload_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_offload.h File Reference

Socket Offload Redirect API.
[More...](#details)

`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](socket__offload_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [socket\_dns\_offload](structsocket__dns__offload.md) |
|  | An offloaded Socket DNS API interface. [More...](structsocket__dns__offload.md#details) |

| Functions | |
| --- | --- |
| void | [socket\_offload\_dns\_register](#a1b56446dd816af7101088bb0a474d0f4) (const struct [socket\_dns\_offload](structsocket__dns__offload.md) \*ops) |
|  | Register an offloaded socket DNS API interface. |

## Detailed Description

Socket Offload Redirect API.

## Function Documentation

## [◆ ](#a1b56446dd816af7101088bb0a474d0f4)socket\_offload\_dns\_register()

| void socket\_offload\_dns\_register | ( | const struct [socket\_dns\_offload](structsocket__dns__offload.md) \* | *ops* | ) |  |
| --- | --- | --- | --- | --- | --- |

Register an offloaded socket DNS API interface.

Parameters
:   | ops | A pointer to the offloaded socket DNS API interface. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_offload.h](socket__offload_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
