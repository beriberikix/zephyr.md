---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/icmsg_8h.html
original_path: doxygen/html/icmsg_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icmsg.h File Reference

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/drivers/mbox.h](drivers_2mbox_8h_source.md)>`  
`#include <[zephyr/ipc/ipc_service.h](ipc__service_8h_source.md)>`  
`#include <[zephyr/ipc/pbuf.h](pbuf_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](atomic_8h_source.md)>`

[Go to the source code of this file.](icmsg_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [icmsg\_config\_t](structicmsg__config__t.md) |
| struct | [icmsg\_data\_t](structicmsg__data__t.md) |

| Enumerations | |
| --- | --- |
| enum | [icmsg\_state](group__ipc__icmsg__api.md#gab26905275fd20a113d1f05d03761f910) { [ICMSG\_STATE\_OFF](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a7167bae7aee28ffa39494cb0ca1175b6) , [ICMSG\_STATE\_BUSY](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a21a71b0c9a3b35e1cf7fe07fff4165c7) , [ICMSG\_STATE\_READY](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a318b7d8e3a9e2a2ddfa3bc37ff57581f) } |

| Functions | |
| --- | --- |
| int | [icmsg\_open](group__ipc__icmsg__api.md#ga6017af391a3135c02cec7929620789e8) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data, const struct [ipc\_service\_cb](structipc__service__cb.md) \*cb, void \*ctx) |
|  | Open an icmsg instance. |
| int | [icmsg\_close](group__ipc__icmsg__api.md#ga0d8f5626406ca660e616de131f54e29d) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data) |
|  | Close an icmsg instance. |
| int | [icmsg\_send](group__ipc__icmsg__api.md#ga13b8669034ee51044df7f0623907c03b) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data, const void \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send a message to the remote icmsg instance. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [icmsg.h](icmsg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
