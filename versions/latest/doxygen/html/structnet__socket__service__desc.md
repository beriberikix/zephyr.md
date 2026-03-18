---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__socket__service__desc.html
original_path: doxygen/html/structnet__socket__service__desc.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_socket\_service\_desc Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD socket service API](group__bsd__socket__service.md)

Main structure holding socket service configuration information.
[More...](#details)

`#include <[socket_service.h](socket__service_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [owner](#a08da5714fafa3f678771ea3d5204971a) |
|  | Owner name. |
| struct [k\_work\_q](structk__work__q.md) \* | [work\_q](#a6cabae5e1fa0fd56c626932c7c1beca3) |
|  | Workqueue where the work is submitted. |
| struct [net\_socket\_service\_event](structnet__socket__service__event.md) \* | [pev](#a62104a9136d2abd88c25480eee2b187a) |
|  | Pointer to the list of services that we are listening. |
| int | [pev\_len](#a5c958339cbc98e7c4490952ce1e9fbc9) |
|  | Length of the pollable socket array for this service. |
| int \* | [idx](#a480b960a8d130ded4668f355a8e5fd83) |
|  | Where are my pollfd entries in the global list. |

## Detailed Description

Main structure holding socket service configuration information.

The [k\_work](structk__work.md "A structure used to submit work.") item is created so that when there is data coming to those fds, the [k\_work](structk__work.md "A structure used to submit work.") callback is then called. The workqueue can be set NULL in which case system workqueue is used. The service descriptor should be created at built time, and then used as a parameter to register the sockets to be monitored. User should create needed sockets and then setup the poll struct and then register the sockets to be monitored at runtime.

## Field Documentation

## [◆ ](#a480b960a8d130ded4668f355a8e5fd83)idx

| int\* net\_socket\_service\_desc::idx |
| --- |

Where are my pollfd entries in the global list.

## [◆ ](#a08da5714fafa3f678771ea3d5204971a)owner

| const char\* net\_socket\_service\_desc::owner |
| --- |

Owner name.

This can be used in debugging to see who has registered this service.

## [◆ ](#a62104a9136d2abd88c25480eee2b187a)pev

| struct [net\_socket\_service\_event](structnet__socket__service__event.md)\* net\_socket\_service\_desc::pev |
| --- |

Pointer to the list of services that we are listening.

## [◆ ](#a5c958339cbc98e7c4490952ce1e9fbc9)pev\_len

| int net\_socket\_service\_desc::pev\_len |
| --- |

Length of the pollable socket array for this service.

## [◆ ](#a6cabae5e1fa0fd56c626932c7c1beca3)work\_q

| struct [k\_work\_q](structk__work__q.md)\* net\_socket\_service\_desc::work\_q |
| --- |

Workqueue where the work is submitted.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket\_service.h](socket__service_8h_source.md)

- [net\_socket\_service\_desc](structnet__socket__service__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
