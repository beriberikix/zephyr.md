---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__socket__service__event.html
original_path: doxygen/html/structnet__socket__service__event.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| struct [k\_work](structk__work.md) | [work](#a0bf2c9e1fc2b8125db3fd907ed6ea27c) |
|  | [k\_work](structk__work.md "A structure used to submit work.") that is done when there is desired activity in file descriptor. |
| [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) | [callback](#a1af4ca9e8076f0725d90f535fbbb94c4) |
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

## [◆ ](#a1af4ca9e8076f0725d90f535fbbb94c4)callback

| [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) net\_socket\_service\_event::callback |
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

## [◆ ](#a0bf2c9e1fc2b8125db3fd907ed6ea27c)work

| struct [k\_work](structk__work.md) net\_socket\_service\_event::work |
| --- |

[k\_work](structk__work.md "A structure used to submit work.") that is done when there is desired activity in file descriptor.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket\_service.h](socket__service_8h_source.md)

- [net\_socket\_service\_event](structnet__socket__service__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
