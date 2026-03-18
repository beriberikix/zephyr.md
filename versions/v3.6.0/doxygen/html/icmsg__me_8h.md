---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/icmsg__me_8h.html
original_path: doxygen/html/icmsg__me_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icmsg\_me.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/ipc/icmsg.h](icmsg_8h_source.md)>`  
`#include <[zephyr/ipc/ipc_service.h](ipc__service_8h_source.md)>`

[Go to the source code of this file.](icmsg__me_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [icmsg\_me\_data\_t](structicmsg__me__data__t.md) |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) |

| Functions | |
| --- | --- |
| int | [icmsg\_me\_init](group__ipc__icmsg__me__api.md#ga12cc5855f2fbca5506f647ced473c71f) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data) |
|  | Initialize an icmsg\_me instance. |
| int | [icmsg\_me\_open](group__ipc__icmsg__me__api.md#gabfd5487133994614cf3dd9b648279673) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, const struct [ipc\_service\_cb](structipc__service__cb.md) \*cb, void \*ctx) |
|  | Open an icmsg\_me instance. |
| void | [icmsg\_me\_wait\_for\_icmsg\_bind](group__ipc__icmsg__me__api.md#ga0f96e65e6b0f4ef05147a4afb1dc3184) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data) |
|  | Wait until the underlying icmsg instance calls bound callback. |
| void | [icmsg\_me\_icmsg\_bound](group__ipc__icmsg__me__api.md#ga5ddaefd30fdee07af3f80d0239e9cce0) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data) |
|  | Notify the icmsg\_me instance that the underlying icmsg was bound. |
| void | [icmsg\_me\_received\_data](group__ipc__icmsg__me__api.md#gad667798588efc1689c2eec81147a229e) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) id, const void \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Notify the icmsg\_me instance that data for an endpoint was received. |
| int | [icmsg\_me\_set\_empty\_ept\_cfg\_slot](group__ipc__icmsg__me__api.md#ga20ac43faf9803b14ed0bacefb527ee3f) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*ept\_cfg, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) \*id) |
|  | Set endpoint configuration in an empty endpoint slot. |
| int | [icmsg\_me\_set\_ept\_cfg](group__ipc__icmsg__me__api.md#gaf04015b3666ef8e2a923d4d63c093474) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) id, const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*ept\_cfg) |
|  | Set endpoint configuration in a selected endpoint slot. |
| int | [icmsg\_me\_get\_ept\_cfg](group__ipc__icmsg__me__api.md#ga6bece3eb1bef849200feca959fbb3d1b) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) id, const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*\*ept\_cfg) |
|  | Get endpoint configuration from a selected endpoint slot. |
| void | [icmsg\_me\_reset\_ept\_cfg](group__ipc__icmsg__me__api.md#ga8581afc32d8c68193f597754397f8964) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) id) |
|  | Reset endpoint configuration in a selected endpoint slot. |
| int | [icmsg\_me\_send](group__ipc__icmsg__me__api.md#ga617f05b24cccc8557ca447e94c3f2702) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](group__ipc__icmsg__me__api.md#gafb150656560c6e61291bae566ad3990a) id, const void \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send a message to the remote icmsg\_me endpoint. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [icmsg\_me.h](icmsg__me_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
