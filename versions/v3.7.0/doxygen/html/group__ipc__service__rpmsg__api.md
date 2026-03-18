---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__ipc__service__rpmsg__api.html
original_path: doxygen/html/group__ipc__service__rpmsg__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IPC service RPMsg API

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md)

IPC service RPMsg API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) |
|  | Endpoint structure. [More...](structipc__rpmsg__ept.md#details) |
| struct | [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) |
|  | RPMsg instance structure. [More...](structipc__rpmsg__instance.md#details) |

| Macros | |
| --- | --- |
| #define | [NUM\_ENDPOINTS](#gada0274bbd763278066d01de34c4e7072)   CONFIG\_IPC\_SERVICE\_BACKEND\_RPMSG\_NUM\_ENDPOINTS\_PER\_INSTANCE |
|  | Number of endpoints. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [rpmsg\_ept\_bound\_cb](#gad313c1e25e158bd91a0b0c3050012803)) (struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) \*ept) |
|  | Define the bound callback. |

| Functions | |
| --- | --- |
| int | [ipc\_rpmsg\_init](#ga08e97e91d3512a3fe28aa80116c51ddf) (struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \*instance, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int role, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int buffer\_size, struct metal\_io\_region \*shm\_io, struct virtio\_device \*vdev, void \*shb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, rpmsg\_ns\_bind\_cb ns\_bind\_cb) |
|  | Init an RPMsg instance. |
| int | [ipc\_rpmsg\_deinit](#gaef3a7306082f88deb394f85a4bb5758b) (struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \*instance, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int role) |
|  | Deinit an RPMsg instance. |
| int | [ipc\_rpmsg\_register\_ept](#ga9c8124e81f385155e3e1338d2ef4a78d) (struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \*instance, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int role, struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) \*ept) |
|  | Register an endpoint. |

## Detailed Description

IPC service RPMsg API.

## Macro Definition Documentation

## [◆ ](#gada0274bbd763278066d01de34c4e7072)NUM\_ENDPOINTS

| #define NUM\_ENDPOINTS   CONFIG\_IPC\_SERVICE\_BACKEND\_RPMSG\_NUM\_ENDPOINTS\_PER\_INSTANCE |
| --- |

`#include <[ipc_rpmsg.h](ipc__rpmsg_8h.md)>`

Number of endpoints.

## Typedef Documentation

## [◆ ](#gad313c1e25e158bd91a0b0c3050012803)rpmsg\_ept\_bound\_cb

| typedef void(\* rpmsg\_ept\_bound\_cb) (struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) \*ept) |
| --- |

`#include <[ipc_rpmsg.h](ipc__rpmsg_8h.md)>`

Define the bound callback.

This callback is defined at instance level and it is called when an endpoint of the instance is bound.

Parameters
:   | ept | Endpoint of the instance just bound. |
    | --- | --- |

## Function Documentation

## [◆ ](#gaef3a7306082f88deb394f85a4bb5758b)ipc\_rpmsg\_deinit()

| int ipc\_rpmsg\_deinit | ( | struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \* | *instance*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *role* ) |

`#include <[ipc_rpmsg.h](ipc__rpmsg_8h.md)>`

Deinit an RPMsg instance.

Parameters
:   | instance | Pointer to the RPMsg instance struct. |
    | --- | --- |
    | role | Host / Remote role. |

Return values
:   | -EINVAL | When some parameter is missing |
    | --- | --- |
    | 0 | If successful |

## [◆ ](#ga08e97e91d3512a3fe28aa80116c51ddf)ipc\_rpmsg\_init()

| int ipc\_rpmsg\_init | ( | struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \* | *instance*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *role*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *buffer\_size*, |
|  |  | struct metal\_io\_region \* | *shm\_io*, |
|  |  | struct virtio\_device \* | *vdev*, |
|  |  | void \* | *shb*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | rpmsg\_ns\_bind\_cb | *ns\_bind\_cb* ) |

`#include <[ipc_rpmsg.h](ipc__rpmsg_8h.md)>`

Init an RPMsg instance.

Init an RPMsg instance.

Parameters
:   | instance | Pointer to the RPMsg instance struct. |
    | --- | --- |
    | role | Host / Remote role. |
    | buffer\_size | Size of the buffer used to send data between host and remote. |
    | shm\_io | SHM IO region pointer. |
    | vdev | VirtIO device pointer. |
    | shb | Shared memory region pointer. |
    | size | Size of the shared memory region. |
    | ns\_bind\_cb | callback handler for name service announcement without local endpoints waiting to bind. If NULL the implementation falls back to the internal implementation. |

Return values
:   | -EINVAL | When some parameter is missing. |
    | --- | --- |
    | 0 | If successful. |
    | Other | errno codes depending on the OpenAMP implementation. |

## [◆ ](#ga9c8124e81f385155e3e1338d2ef4a78d)ipc\_rpmsg\_register\_ept()

| int ipc\_rpmsg\_register\_ept | ( | struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \* | *instance*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *role*, |
|  |  | struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) \* | *ept* ) |

`#include <[ipc_rpmsg.h](ipc__rpmsg_8h.md)>`

Register an endpoint.

Register an endpoint to a provided RPMsg instance.

Parameters
:   | instance | Pointer to the RPMsg instance struct. |
    | --- | --- |
    | role | Host / Remote role. |
    | ept | Endpoint to register. |

Return values
:   | -EINVAL | When some parameter is missing. |
    | --- | --- |
    | 0 | If successful. |
    | Other | errno codes depending on the OpenAMP implementation. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
