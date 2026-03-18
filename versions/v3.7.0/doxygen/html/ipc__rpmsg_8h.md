---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ipc__rpmsg_8h.html
original_path: doxygen/html/ipc__rpmsg_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_rpmsg.h File Reference

`#include <[zephyr/ipc/ipc_service.h](ipc__service_8h_source.md)>`  
`#include <openamp/open_amp.h>`  
`#include <metal/device.h>`

[Go to the source code of this file.](ipc__rpmsg_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) |
|  | Endpoint structure. [More...](structipc__rpmsg__ept.md#details) |
| struct | [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) |
|  | RPMsg instance structure. [More...](structipc__rpmsg__instance.md#details) |

| Macros | |
| --- | --- |
| #define | [NUM\_ENDPOINTS](group__ipc__service__rpmsg__api.md#gada0274bbd763278066d01de34c4e7072)   CONFIG\_IPC\_SERVICE\_BACKEND\_RPMSG\_NUM\_ENDPOINTS\_PER\_INSTANCE |
|  | Number of endpoints. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [rpmsg\_ept\_bound\_cb](group__ipc__service__rpmsg__api.md#gad313c1e25e158bd91a0b0c3050012803)) (struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) \*ept) |
|  | Define the bound callback. |

| Functions | |
| --- | --- |
| int | [ipc\_rpmsg\_init](group__ipc__service__rpmsg__api.md#ga08e97e91d3512a3fe28aa80116c51ddf) (struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \*instance, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int role, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int buffer\_size, struct metal\_io\_region \*shm\_io, struct virtio\_device \*vdev, void \*shb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, rpmsg\_ns\_bind\_cb ns\_bind\_cb) |
|  | Init an RPMsg instance. |
| int | [ipc\_rpmsg\_deinit](group__ipc__service__rpmsg__api.md#gaef3a7306082f88deb394f85a4bb5758b) (struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \*instance, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int role) |
|  | Deinit an RPMsg instance. |
| int | [ipc\_rpmsg\_register\_ept](group__ipc__service__rpmsg__api.md#ga9c8124e81f385155e3e1338d2ef4a78d) (struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \*instance, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int role, struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) \*ept) |
|  | Register an endpoint. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [ipc\_rpmsg.h](ipc__rpmsg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
