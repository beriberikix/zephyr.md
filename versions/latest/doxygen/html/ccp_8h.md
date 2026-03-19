---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ccp_8h.html
original_path: doxygen/html/ccp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ccp.h File Reference

Bluetooth Call Control Profile (CCP) APIs.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <zephyr/autoconf.h>`  
`#include <[zephyr/bluetooth/audio/tbs.h](tbs_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](ccp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_ccp\_call\_control\_client\_bearers](structbt__ccp__call__control__client__bearers.md) |
|  | Struct with information about bearers of a client. [More...](structbt__ccp__call__control__client__bearers.md#details) |
| struct | [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) |
|  | Struct to hold the Telephone Bearer Service client callbacks. [More...](structbt__ccp__call__control__client__cb.md#details) |

| Functions | |
| --- | --- |
| int | [bt\_ccp\_call\_control\_server\_register\_bearer](group__bt__ccp__call__control__server.md#ga5e5acb90cc39b5f8a4e25d8ab8a11b10) (const struct [bt\_tbs\_register\_param](structbt__tbs__register__param.md) \*param, struct bt\_ccp\_call\_control\_server\_bearer \*\*bearer) |
|  | Register a Telephone Bearer. |
| int | [bt\_ccp\_call\_control\_server\_unregister\_bearer](group__bt__ccp__call__control__server.md#gaa2486dec8a47bd7f4cd4076477e8ac4a) (struct bt\_ccp\_call\_control\_server\_bearer \*bearer) |
|  | Unregister a Telephone Bearer. |
| int | [bt\_ccp\_call\_control\_client\_discover](group__bt__ccp__call__control__client.md#ga2a5bce65e39ba05625423308f996021d) (struct bt\_conn \*conn, struct bt\_ccp\_call\_control\_client \*\*out\_client) |
|  | Discovers the Telephone Bearer Service (TBS) support on a remote device. |
| int | [bt\_ccp\_call\_control\_client\_register\_cb](group__bt__ccp__call__control__client.md#ga8c5c3907759fe02745339b9456cca05f) (struct [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) \*cb) |
|  | Register callbacks for the Call Control Client. |
| int | [bt\_ccp\_call\_control\_client\_unregister\_cb](group__bt__ccp__call__control__client.md#ga534a15db3e87d63942de6ba4bd8377db) (struct [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) \*cb) |
|  | Unregister callbacks for the Call Control Client. |

## Detailed Description

Bluetooth Call Control Profile (CCP) APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [ccp.h](ccp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
