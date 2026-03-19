---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/icmsg_8h.html
original_path: doxygen/html/icmsg_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icmsg.h File Reference

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/drivers/mbox.h](drivers_2mbox_8h_source.md)>`  
`#include <[zephyr/ipc/ipc_service.h](ipc__service_8h_source.md)>`  
`#include <[zephyr/ipc/pbuf.h](pbuf_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`

[Go to the source code of this file.](icmsg_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [icmsg\_config\_t](structicmsg__config__t.md) |
| struct | [icmsg\_data\_t](structicmsg__data__t.md) |

| Enumerations | |
| --- | --- |
| enum | [icmsg\_state](group__ipc__icmsg__api.md#gab26905275fd20a113d1f05d03761f910) {     [ICMSG\_STATE\_OFF](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a7167bae7aee28ffa39494cb0ca1175b6) , [ICMSG\_STATE\_INITIALIZING\_SID\_DISABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a6108f7fe29d982a2f52653c4e97205b6) , [ICMSG\_STATE\_INITIALIZING\_SID\_ENABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910ae9e45a00a479eb8be2d82ea2ac848dc7) , [ICMSG\_STATE\_INITIALIZING\_SID\_DETECT](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a6795026f474f701d404e38f5ad4766eb) ,     [ICMSG\_STATE\_DISCONNECTED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a1e95d66a57e9f7bd2dd818ea8182b2dd) , [ICMSG\_STATE\_CONNECTED\_SID\_DISABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910ac9b07c0dd80a5e4f5029a3984d552bab) , [ICMSG\_STATE\_CONNECTED\_SID\_ENABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a32fba02984cec57994a5ae94c4e2ab87)   } |
| enum | [icmsg\_unbound\_mode](group__ipc__icmsg__api.md#gae14e0b81c90a4bb4fc140a48a48d1b5f) { [ICMSG\_UNBOUND\_MODE\_DISABLE](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fac688a38231634863b4f3a5baa73de57a) = ICMSG\_STATE\_INITIALIZING\_SID\_DISABLED , [ICMSG\_UNBOUND\_MODE\_ENABLE](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fa644f1bdb89f1e3940909a0269c9fca07) = ICMSG\_STATE\_INITIALIZING\_SID\_ENABLED , [ICMSG\_UNBOUND\_MODE\_DETECT](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fa3dbd2f53889c3d5a40948700df4d5f75) = ICMSG\_STATE\_INITIALIZING\_SID\_DETECT } |

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
