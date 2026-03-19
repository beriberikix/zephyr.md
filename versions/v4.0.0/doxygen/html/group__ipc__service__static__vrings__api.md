---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ipc__service__static__vrings__api.html
original_path: doxygen/html/group__ipc__service__static__vrings__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IPC service static VRINGs API

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md)

IPC service static VRINGs API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ipc\_static\_vrings](structipc__static__vrings.md) |
|  | Static VRINGs structure. [More...](structipc__static__vrings.md#details) |

| Macros | |
| --- | --- |
| #define | [VRING\_COUNT](#ga2b05772c325881ba650dc01f3e6e2834)   (2) |
|  | Number of used VRING buffers. |
| #define | [MEM\_ALIGNMENT](#ga97343214666ee6dcb18c0bd77b441ea7)   CONFIG\_IPC\_SERVICE\_STATIC\_VRINGS\_MEM\_ALIGNMENT |
|  | Memory alignment. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [ipc\_notify\_cb](#ga70026ad72cd08d42461e1489c4ddfc9b)) (struct virtqueue \*vq, void \*priv) |
|  | Define the notify callback. |

| Functions | |
| --- | --- |
| int | [ipc\_static\_vrings\_init](#ga5cab9a9a9ade1e61eb02592aa23dc0bc) (struct [ipc\_static\_vrings](structipc__static__vrings.md) \*vr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int role) |
|  | Init the static VRINGs. |
| int | [ipc\_static\_vrings\_deinit](#ga90680ce6a8cc4dae9cabba8fad6e939a) (struct [ipc\_static\_vrings](structipc__static__vrings.md) \*vr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int role) |
|  | Deinitialise the static VRINGs. |

## Detailed Description

IPC service static VRINGs API.

## Macro Definition Documentation

## [◆ ](#ga97343214666ee6dcb18c0bd77b441ea7)MEM\_ALIGNMENT

| #define MEM\_ALIGNMENT   CONFIG\_IPC\_SERVICE\_STATIC\_VRINGS\_MEM\_ALIGNMENT |
| --- |

`#include <[ipc_static_vrings.h](ipc__static__vrings_8h.md)>`

Memory alignment.

This should take into account the cache line if the cache is enabled, otherwise it should be naturally aligned to the machine word size.

## [◆ ](#ga2b05772c325881ba650dc01f3e6e2834)VRING\_COUNT

| #define VRING\_COUNT   (2) |
| --- |

`#include <[ipc_static_vrings.h](ipc__static__vrings_8h.md)>`

Number of used VRING buffers.

## Typedef Documentation

## [◆ ](#ga70026ad72cd08d42461e1489c4ddfc9b)ipc\_notify\_cb

| typedef void(\* ipc\_notify\_cb) (struct virtqueue \*vq, void \*priv) |
| --- |

`#include <[ipc_static_vrings.h](ipc__static__vrings_8h.md)>`

Define the notify callback.

This callback is defined at instance level and it is called on virtqueue notify.

Parameters
:   | vq | Virtqueue. |
    | --- | --- |
    | priv | Priv data. |

## Function Documentation

## [◆ ](#ga90680ce6a8cc4dae9cabba8fad6e939a)ipc\_static\_vrings\_deinit()

| int ipc\_static\_vrings\_deinit | ( | struct [ipc\_static\_vrings](structipc__static__vrings.md) \* | *vr*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *role* ) |

`#include <[ipc_static_vrings.h](ipc__static__vrings_8h.md)>`

Deinitialise the static VRINGs.

Deinitialise VRINGs and Virtqueues of an OpenAMP / RPMsg instance.

Parameters
:   | vr | Pointer to the VRINGs instance struct. |
    | --- | --- |
    | role | Host / Remote role. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Other | errno codes depending on the OpenAMP implementation. |

## [◆ ](#ga5cab9a9a9ade1e61eb02592aa23dc0bc)ipc\_static\_vrings\_init()

| int ipc\_static\_vrings\_init | ( | struct [ipc\_static\_vrings](structipc__static__vrings.md) \* | *vr*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *role* ) |

`#include <[ipc_static_vrings.h](ipc__static__vrings_8h.md)>`

Init the static VRINGs.

Init VRINGs and Virtqueues of an OpenAMP / RPMsg instance.

Parameters
:   | vr | Pointer to the VRINGs instance struct. |
    | --- | --- |
    | role | Host / Remote role. |

Return values
:   | -EINVAL | When some parameter is missing. |
    | --- | --- |
    | -ENOMEM | When memory is not enough for VQs allocation. |
    | 0 | If successful. |
    | Other | errno codes depending on the OpenAMP implementation. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
