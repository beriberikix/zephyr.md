---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/smp__client_8h.html
original_path: doxygen/html/smp__client_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_client.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <mgmt/mcumgr/transport/smp_internal.h>`  
`#include <[zephyr/mgmt/mcumgr/smp/smp.h](mgmt_2mcumgr_2smp_2smp_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/transport/smp.h](mgmt_2mcumgr_2transport_2smp_8h_source.md)>`

[Go to the source code of this file.](smp__client_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [smp\_client\_object](structsmp__client__object.md) |
|  | SMP client object. [More...](structsmp__client__object.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [smp\_client\_res\_fn](group__mcumgr__smp__client.md#gae7974bf0e951403f6dfe8b33a2547acc)) (struct [net\_buf](structnet__buf.md) \*nb, void \*user\_data) |
|  | Response callback for SMP send. |

| Functions | |
| --- | --- |
| int | [smp\_client\_object\_init](group__mcumgr__smp__client.md#ga07f36d0ac230d158c2959e8010444e47) (struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, int smp\_type) |
|  | Initialize a SMP client object. |
| int | [smp\_client\_single\_response](group__mcumgr__smp__client.md#ga42022a3ea929da134644996c4414cfce) (struct [net\_buf](structnet__buf.md) \*nb, const struct smp\_hdr \*res\_hdr) |
|  | SMP client response handler. |
| struct [net\_buf](structnet__buf.md) \* | [smp\_client\_buf\_allocation](group__mcumgr__smp__client.md#ga57ec028fc6bcb3591298815b1d9b8a3b) (struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [group](structgroup.md), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) command\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) op, enum [smp\_mcumgr\_version\_t](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00ed) version) |
|  | Allocate buffer and initialize with SMP header. |
| void | [smp\_client\_buf\_free](group__mcumgr__smp__client.md#gace302f95e5f45076db72fbecf190f0f5) (struct [net\_buf](structnet__buf.md) \*nb) |
|  | Free a SMP client buffer. |
| int | [smp\_client\_send\_cmd](group__mcumgr__smp__client.md#gaeb20d13ddf14ddb924b0a84a014abda5) (struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, struct [net\_buf](structnet__buf.md) \*nb, [smp\_client\_res\_fn](group__mcumgr__smp__client.md#gae7974bf0e951403f6dfe8b33a2547acc) cb, void \*user\_data, int timeout\_in\_sec) |
|  | SMP client data send request. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [smp](dir_e62cfe388532d436a5daefec152a780b.md)
- [smp\_client.h](smp__client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
