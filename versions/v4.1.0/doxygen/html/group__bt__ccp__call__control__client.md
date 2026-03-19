---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__ccp__call__control__client.html
original_path: doxygen/html/group__bt__ccp__call__control__client.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CCP Call Control Client APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Call Control Profile (CCP)](group__bt__ccp.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_ccp\_call\_control\_client\_bearers](structbt__ccp__call__control__client__bearers.md) |
|  | Struct with information about bearers of a client. [More...](structbt__ccp__call__control__client__bearers.md#details) |
| struct | [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) |
|  | Struct to hold the Telephone Bearer Service client callbacks. [More...](structbt__ccp__call__control__client__cb.md#details) |

| Functions | |
| --- | --- |
| int | [bt\_ccp\_call\_control\_client\_discover](#ga2a5bce65e39ba05625423308f996021d) (struct bt\_conn \*conn, struct bt\_ccp\_call\_control\_client \*\*out\_client) |
|  | Discovers the Telephone Bearer Service (TBS) support on a remote device. |
| int | [bt\_ccp\_call\_control\_client\_register\_cb](#ga8c5c3907759fe02745339b9456cca05f) (struct [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) \*cb) |
|  | Register callbacks for the Call Control Client. |
| int | [bt\_ccp\_call\_control\_client\_unregister\_cb](#ga534a15db3e87d63942de6ba4bd8377db) (struct [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) \*cb) |
|  | Unregister callbacks for the Call Control Client. |

## Detailed Description

## Function Documentation

## [◆ ](#ga2a5bce65e39ba05625423308f996021d)bt\_ccp\_call\_control\_client\_discover()

| int bt\_ccp\_call\_control\_client\_discover | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct bt\_ccp\_call\_control\_client \*\* | *out\_client* ) |

`#include <[ccp.h](ccp_8h.md)>`

Discovers the Telephone Bearer Service (TBS) support on a remote device.

This will discover the Telephone Bearer Service (TBS) and Generic Telephone Bearer Service (GTBS) on the remote device.

Attention
:   Available only when the following Kconfig option is enabled: `CONFIG_BT_CCP_CALL_CONTROL_CLIENT`..

Parameters
:   | conn | Connection to a remote server. |
    | --- | --- |
    | out\_client | Pointer to client instance on success |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `conn` or `out_client` is NULL |
    | -ENOTCONN | `conn` is not connected |
    | -ENOMEM | Could not allocated memory for the request |
    | -EBUSY | Already doing discovery for `conn` |
    | -ENOEXEC | Rejected by the GATT layer |

## [◆ ](#ga8c5c3907759fe02745339b9456cca05f)bt\_ccp\_call\_control\_client\_register\_cb()

| int bt\_ccp\_call\_control\_client\_register\_cb | ( | struct [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccp.h](ccp_8h.md)>`

Register callbacks for the Call Control Client.

Parameters
:   | cb | The callback struct |
    | --- | --- |

Return values
:   | 0 | Succsss |
    | --- | --- |
    | -EINVAL | `cb` is NULL |
    | -EEXISTS | `cb` is already registered |

## [◆ ](#ga534a15db3e87d63942de6ba4bd8377db)bt\_ccp\_call\_control\_client\_unregister\_cb()

| int bt\_ccp\_call\_control\_client\_unregister\_cb | ( | struct [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccp.h](ccp_8h.md)>`

Unregister callbacks for the Call Control Client.

Parameters
:   | cb | The callback struct |
    | --- | --- |

Return values
:   | 0 | Succsss |
    | --- | --- |
    | -EINVAL | `cb` is NULL |
    | -EALREADY | `cb` is not registered |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
