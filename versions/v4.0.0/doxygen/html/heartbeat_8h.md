---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/heartbeat_8h.html
original_path: doxygen/html/heartbeat_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

heartbeat.h File Reference

Heartbeat APIs.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](heartbeat_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md) |
|  | Heartbeat Publication parameters. [More...](structbt__mesh__hb__pub.md#details) |
| struct | [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) |
|  | Heartbeat Subscription parameters. [More...](structbt__mesh__hb__sub.md#details) |
| struct | [bt\_mesh\_hb\_cb](structbt__mesh__hb__cb.md) |
|  | Heartbeat callback structure. [More...](structbt__mesh__hb__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_HB\_CB\_DEFINE](group__bt__mesh__heartbeat.md#ga517f009151a7eeaa898a853fd0d7a93a)(\_name) |
|  | Register a callback structure for Heartbeat events. |

| Functions | |
| --- | --- |
| void | [bt\_mesh\_hb\_pub\_get](group__bt__mesh__heartbeat.md#ga2e95d8f9d75f1bea13a9584d201fd713) (struct [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md) \*get) |
|  | Get the current Heartbeat publication parameters. |
| void | [bt\_mesh\_hb\_sub\_get](group__bt__mesh__heartbeat.md#ga3013c3da6cc1a34b0c98c56fba7e7877) (struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) \*get) |
|  | Get the current Heartbeat subscription parameters. |

## Detailed Description

Heartbeat APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [heartbeat.h](heartbeat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
