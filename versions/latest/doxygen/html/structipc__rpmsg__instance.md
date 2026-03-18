---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structipc__rpmsg__instance.html
original_path: doxygen/html/structipc__rpmsg__instance.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_rpmsg\_instance Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [IPC service RPMsg API](group__ipc__service__rpmsg__api.md)

RPMsg instance structure.
[More...](#details)

`#include <[ipc_rpmsg.h](ipc__rpmsg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) | [endpoint](#afd5e2760bead6932c052c03c1f7f29e5) [CONFIG\_IPC\_SERVICE\_BACKEND\_RPMSG\_NUM\_ENDPOINTS\_PER\_INSTANCE] |
|  | Endpoints in the instance. |
| struct rpmsg\_virtio\_device | [rvdev](#a8017686ab6afc36ff589d6e89dda9feb) |
|  | RPMsg virtIO device. |
| struct rpmsg\_virtio\_shm\_pool | [shm\_pool](#a33da8a446e07b0000405a7381b1db4fb) |
|  | SHM pool. |
| [rpmsg\_ept\_bound\_cb](group__ipc__service__rpmsg__api.md#gad313c1e25e158bd91a0b0c3050012803) | [bound\_cb](#a59125783afdf4a879e85ef7abaeb6f55) |
|  | EPT (instance) bound callback. |
| rpmsg\_ept\_cb | [cb](#a43f8aeddef2d8e1c5b03a0ebc93f252d) |
|  | EPT (instance) callback. |
| struct [k\_mutex](structk__mutex.md) | [mtx](#aac59ce6875ce277c9cbb1f2a1b61e732) |
|  | Mutex for the instance. |

## Detailed Description

RPMsg instance structure.

Struct representation of an RPMsg instance.

## Field Documentation

## [◆ ](#a59125783afdf4a879e85ef7abaeb6f55)bound\_cb

| [rpmsg\_ept\_bound\_cb](group__ipc__service__rpmsg__api.md#gad313c1e25e158bd91a0b0c3050012803) ipc\_rpmsg\_instance::bound\_cb |
| --- |

EPT (instance) bound callback.

## [◆ ](#a43f8aeddef2d8e1c5b03a0ebc93f252d)cb

| rpmsg\_ept\_cb ipc\_rpmsg\_instance::cb |
| --- |

EPT (instance) callback.

## [◆ ](#afd5e2760bead6932c052c03c1f7f29e5)endpoint

| struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) ipc\_rpmsg\_instance::endpoint[CONFIG\_IPC\_SERVICE\_BACKEND\_RPMSG\_NUM\_ENDPOINTS\_PER\_INSTANCE] |
| --- |

Endpoints in the instance.

## [◆ ](#aac59ce6875ce277c9cbb1f2a1b61e732)mtx

| struct [k\_mutex](structk__mutex.md) ipc\_rpmsg\_instance::mtx |
| --- |

Mutex for the instance.

## [◆ ](#a8017686ab6afc36ff589d6e89dda9feb)rvdev

| struct rpmsg\_virtio\_device ipc\_rpmsg\_instance::rvdev |
| --- |

RPMsg virtIO device.

## [◆ ](#a33da8a446e07b0000405a7381b1db4fb)shm\_pool

| struct rpmsg\_virtio\_shm\_pool ipc\_rpmsg\_instance::shm\_pool |
| --- |

SHM pool.

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[ipc\_rpmsg.h](ipc__rpmsg_8h_source.md)

- [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
