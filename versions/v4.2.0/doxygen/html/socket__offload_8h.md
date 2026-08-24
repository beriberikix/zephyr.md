---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/socket__offload_8h.html
original_path: doxygen/html/socket__offload_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

| Macros | |
| --- | --- |
| #define | [socket\_offload\_dns\_is\_enabled](#af341a4e569196545165962e17544d2c9)() |
|  | Check if DNS offloading is enabled. |

| Functions | |
| --- | --- |
| void | [socket\_offload\_dns\_register](#a1b56446dd816af7101088bb0a474d0f4) (const struct [socket\_dns\_offload](structsocket__dns__offload.md) \*ops) |
|  | Register an offloaded socket DNS API interface. |
| int | [socket\_offload\_dns\_deregister](#a87f67b6c07b7271778e919ccc88b6d7b) (const struct [socket\_dns\_offload](structsocket__dns__offload.md) \*ops) |
|  | Deregister an offloaded socket DNS API interface. |
| void | [socket\_offload\_dns\_enable](#a0d0123d234cd292282a272cb2e2eeb3c) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable/disable DNS offloading at runtime. |

## Detailed Description

Socket Offload Redirect API.

## Macro Definition Documentation

## [◆ ](#af341a4e569196545165962e17544d2c9)socket\_offload\_dns\_is\_enabled

| #define socket\_offload\_dns\_is\_enabled | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

false

Check if DNS offloading is enabled.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | DNS offloaded API is registered and enabled. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | DNS offloading is disabled. |

## Function Documentation

## [◆ ](#a87f67b6c07b7271778e919ccc88b6d7b)socket\_offload\_dns\_deregister()

| int socket\_offload\_dns\_deregister | ( | const struct [socket\_dns\_offload](structsocket__dns__offload.md) \* | *ops* | ) |  |
| --- | --- | --- | --- | --- | --- |

Deregister an offloaded socket DNS API interface.

Parameters
:   | ops | A pointer to the offloaded socket DNS API interface. |
    | --- | --- |

Return values
:   | 0 | On success |
    | --- | --- |
    | -EINVAL | Offloaded DNS API was not regsitered. |

## [◆ ](#a0d0123d234cd292282a272cb2e2eeb3c)socket\_offload\_dns\_enable()

| void socket\_offload\_dns\_enable | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable/disable DNS offloading at runtime.

Parameters
:   | enable | Whether to enable or disable the DNS offloading. |
    | --- | --- |

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
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
