---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__socket__service__event.html
original_path: doxygen/html/structnet__socket__service__event.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_socket\_service\_event Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD socket service API](group__bsd__socket__service.md)

This struct contains information which socket triggered calls to the callback function.
[More...](#details)

`#include <[socket_service.h](socket__service_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [net\_socket\_service\_handler\_t](group__bsd__socket__service.md#ga5d9495470c1ade51791df56c59cfb1f5) | [callback](#a82695b0eaa7c563033fce4afde33cab9) |
|  | Callback to be called for desired socket activity. |
| struct [zsock\_pollfd](structzsock__pollfd.md) | [event](#a8246a87e2171474eb214bb8f909cb9bf) |
|  | Socket information that triggered this event. |
| void \* | [user\_data](#aa11bb43a2cc48d167bf8995d860fd638) |
|  | User data. |
| struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \* | [svc](#a7052fad6a65c5a1b610a69e16fc72785) |
|  | Service back pointer. |

## Detailed Description

This struct contains information which socket triggered calls to the callback function.

## Field Documentation

## [◆ ](#a82695b0eaa7c563033fce4afde33cab9)callback

| [net\_socket\_service\_handler\_t](group__bsd__socket__service.md#ga5d9495470c1ade51791df56c59cfb1f5) net\_socket\_service\_event::callback |
| --- |

Callback to be called for desired socket activity.

## [◆ ](#a8246a87e2171474eb214bb8f909cb9bf)event

| struct [zsock\_pollfd](structzsock__pollfd.md) net\_socket\_service\_event::event |
| --- |

Socket information that triggered this event.

## [◆ ](#a7052fad6a65c5a1b610a69e16fc72785)svc

| struct [net\_socket\_service\_desc](structnet__socket__service__desc.md)\* net\_socket\_service\_event::svc |
| --- |

Service back pointer.

## [◆ ](#aa11bb43a2cc48d167bf8995d860fd638)user\_data

| void\* net\_socket\_service\_event::user\_data |
| --- |

User data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket\_service.h](socket__service_8h_source.md)

- [net\_socket\_service\_event](structnet__socket__service__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
