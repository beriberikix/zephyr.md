---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structipc__ept__cfg.html
original_path: doxygen/html/structipc__ept__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_ept\_cfg Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [IPC service APIs](group__ipc__service__api.md)

Endpoint configuration structure.
[More...](#details)

`#include <[ipc_service.h](ipc__service_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#a6008673337256dc8a71052e121d2d0c6) |
|  | Name of the endpoint. |
| int | [prio](#a8a85a116e7c0069121d4ef5dc9b55a4d) |
|  | Endpoint priority. |
| struct [ipc\_service\_cb](structipc__service__cb.md) | [cb](#a0cd24dc49dbfe7f8cda02ee37d36529c) |
|  | Event callback structure. |
| void \* | [priv](#a4b14515e74e5429d62e13c0478070893) |
|  | Private user data. |

## Detailed Description

Endpoint configuration structure.

## Field Documentation

## [◆ ](#a0cd24dc49dbfe7f8cda02ee37d36529c)cb

| struct [ipc\_service\_cb](structipc__service__cb.md) ipc\_ept\_cfg::cb |
| --- |

Event callback structure.

## [◆ ](#a6008673337256dc8a71052e121d2d0c6)name

| const char\* ipc\_ept\_cfg::name |
| --- |

Name of the endpoint.

## [◆ ](#a8a85a116e7c0069121d4ef5dc9b55a4d)prio

| int ipc\_ept\_cfg::prio |
| --- |

Endpoint priority.

If the backend supports priorities.

## [◆ ](#a4b14515e74e5429d62e13c0478070893)priv

| void\* ipc\_ept\_cfg::priv |
| --- |

Private user data.

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[ipc\_service.h](ipc__service_8h_source.md)

- [ipc\_ept\_cfg](structipc__ept__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
