---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ipc__static__vrings_8h.html
original_path: doxygen/html/ipc__static__vrings_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_static\_vrings.h File Reference

`#include <[zephyr/ipc/ipc_service.h](ipc__service_8h_source.md)>`  
`#include <openamp/open_amp.h>`  
`#include <metal/device.h>`

[Go to the source code of this file.](ipc__static__vrings_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ipc\_static\_vrings](structipc__static__vrings.md) |
|  | Static VRINGs structure. [More...](structipc__static__vrings.md#details) |

| Macros | |
| --- | --- |
| #define | [VRING\_COUNT](group__ipc__service__static__vrings__api.md#ga2b05772c325881ba650dc01f3e6e2834)   (2) |
|  | Number of used VRING buffers. |
| #define | [MEM\_ALIGNMENT](group__ipc__service__static__vrings__api.md#ga97343214666ee6dcb18c0bd77b441ea7)   CONFIG\_IPC\_SERVICE\_STATIC\_VRINGS\_MEM\_ALIGNMENT |
|  | Memory alignment. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [ipc\_notify\_cb](group__ipc__service__static__vrings__api.md#ga70026ad72cd08d42461e1489c4ddfc9b)) (struct virtqueue \*vq, void \*priv) |
|  | Define the notify callback. |

| Functions | |
| --- | --- |
| int | [ipc\_static\_vrings\_init](group__ipc__service__static__vrings__api.md#ga5cab9a9a9ade1e61eb02592aa23dc0bc) (struct [ipc\_static\_vrings](structipc__static__vrings.md) \*vr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int role) |
|  | Init the static VRINGs. |
| int | [ipc\_static\_vrings\_deinit](group__ipc__service__static__vrings__api.md#ga90680ce6a8cc4dae9cabba8fad6e939a) (struct [ipc\_static\_vrings](structipc__static__vrings.md) \*vr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int role) |
|  | Deinitialise the static VRINGs. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [ipc\_static\_vrings.h](ipc__static__vrings_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
