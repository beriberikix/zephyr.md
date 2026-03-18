---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structipc__ept.html
original_path: doxygen/html/structipc__ept.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_ept Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [IPC service APIs](group__ipc__service__api.md)

Endpoint instance.
[More...](#details)

`#include <[ipc_service.h](ipc__service_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [instance](#a4f043fd1ed7df3e1774ba7639c2caf1d) |
|  | Instance this endpoint belongs to. |
| void \* | [token](#a234002020af2b8a2f31ff3727ecf0964) |
|  | Backend-specific token used to identify an endpoint in an instance. |

## Detailed Description

Endpoint instance.

Token is not important for user of the API. It is implemented in a specific backend.

## Field Documentation

## [◆ ](#a4f043fd1ed7df3e1774ba7639c2caf1d)instance

| const struct [device](structdevice.md)\* ipc\_ept::instance |
| --- |

Instance this endpoint belongs to.

## [◆ ](#a234002020af2b8a2f31ff3727ecf0964)token

| void\* ipc\_ept::token |
| --- |

Backend-specific token used to identify an endpoint in an instance.

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[ipc\_service.h](ipc__service_8h_source.md)

- [ipc\_ept](structipc__ept.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
