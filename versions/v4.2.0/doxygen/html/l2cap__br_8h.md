---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/l2cap__br_8h.html
original_path: doxygen/html/l2cap__br_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

l2cap\_br.h File Reference

Bluetooth L2CAP BR/EDR handling.
[More...](#details)

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/buf.h](buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci.h](hci_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`

[Go to the source code of this file.](l2cap__br_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_l2cap\_br\_echo\_cb](structbt__l2cap__br__echo__cb.md) |
|  | ECHO request/response callback structure. [More...](structbt__l2cap__br__echo__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_L2CAP\_BR\_ECHO\_REQ\_RESERVE](group__bt__l2cap.md#ga12c146741591a55dc50d7d07f0755daa)   [BT\_L2CAP\_BUF\_SIZE](group__bt__l2cap.md#gab95b119de4757588074e367a90a7136a)(4) |
|  | Headroom needed for outgoing L2CAP ECHO REQ PDUs. |
| #define | [BT\_L2CAP\_BR\_ECHO\_RSP\_RESERVE](group__bt__l2cap.md#ga2961971c1f80aa6168f6cd47b991bf4d)   [BT\_L2CAP\_BUF\_SIZE](group__bt__l2cap.md#gab95b119de4757588074e367a90a7136a)(4) |
|  | Headroom needed for outgoing L2CAP ECHO RSP PDUs. |

| Functions | |
| --- | --- |
| int | [bt\_l2cap\_br\_echo\_cb\_register](group__bt__l2cap.md#ga62c0115185f5026c1a842848dc5336ce) (struct [bt\_l2cap\_br\_echo\_cb](structbt__l2cap__br__echo__cb.md) \*cb) |
|  | Register ECHO callbacks. |
| int | [bt\_l2cap\_br\_echo\_cb\_unregister](group__bt__l2cap.md#ga00ef7d0a42d8e544b195172af44b88b2) (struct [bt\_l2cap\_br\_echo\_cb](structbt__l2cap__br__echo__cb.md) \*cb) |
|  | Unregister ECHO callbacks. |
| int | [bt\_l2cap\_br\_echo\_req](group__bt__l2cap.md#ga3c6ad17ba18f5c00e39a379ed735de21) (struct bt\_conn \*conn, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send ECHO data through ECHO request. |
| int | [bt\_l2cap\_br\_echo\_rsp](group__bt__l2cap.md#ga8ebf537cc7e4c0a68a320f9c65c94b05) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) identifier, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send ECHO data through ECHO response. |

## Detailed Description

Bluetooth L2CAP BR/EDR handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [l2cap\_br.h](l2cap__br_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
