---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structipc__rpmsg__ept.html
original_path: doxygen/html/structipc__rpmsg__ept.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_rpmsg\_ept Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [IPC service RPMsg API](group__ipc__service__rpmsg__api.md)

Endpoint structure.
[More...](#details)

`#include <[ipc_rpmsg.h](ipc__rpmsg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct rpmsg\_endpoint | [ep](#a43d1c7fc6091bc5ce1d782af1828a76a) |
|  | RPMsg endpoint. |
| char | [name](#a052045f7e5cfdcc83a5d3545b41ac18a) [RPMSG\_NAME\_SIZE] |
|  | Name of the endpoint. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dest](#ad6bf7b86ee9a9a739f0b46ee51276f28) |
|  | Destination endpoint. |
| volatile [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bound](#a8159e224bc1a4ceb17081eea1c16d44d) |
|  | Bound flag. |
| const struct [ipc\_service\_cb](structipc__service__cb.md) \* | [cb](#a5029a16ddadb1a6809f28e0c94826ece) |
|  | Callbacks. |
| void \* | [priv](#ad4f964f88d2cb7498b843f2c6b2804e3) |
|  | Private data to be passed to the endpoint callbacks. |

## Detailed Description

Endpoint structure.

Used to define an endpoint to be encapsulated in an RPMsg instance.

## Field Documentation

## [◆ ](#a8159e224bc1a4ceb17081eea1c16d44d)bound

| volatile [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ipc\_rpmsg\_ept::bound |
| --- |

Bound flag.

## [◆ ](#a5029a16ddadb1a6809f28e0c94826ece)cb

| const struct [ipc\_service\_cb](structipc__service__cb.md)\* ipc\_rpmsg\_ept::cb |
| --- |

Callbacks.

## [◆ ](#ad6bf7b86ee9a9a739f0b46ee51276f28)dest

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ipc\_rpmsg\_ept::dest |
| --- |

Destination endpoint.

## [◆ ](#a43d1c7fc6091bc5ce1d782af1828a76a)ep

| struct rpmsg\_endpoint ipc\_rpmsg\_ept::ep |
| --- |

RPMsg endpoint.

## [◆ ](#a052045f7e5cfdcc83a5d3545b41ac18a)name

| char ipc\_rpmsg\_ept::name[RPMSG\_NAME\_SIZE] |
| --- |

Name of the endpoint.

## [◆ ](#ad4f964f88d2cb7498b843f2c6b2804e3)priv

| void\* ipc\_rpmsg\_ept::priv |
| --- |

Private data to be passed to the endpoint callbacks.

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[ipc\_rpmsg.h](ipc__rpmsg_8h_source.md)

- [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
