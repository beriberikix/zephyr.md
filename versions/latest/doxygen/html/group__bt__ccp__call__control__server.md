---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__ccp__call__control__server.html
original_path: doxygen/html/group__bt__ccp__call__control__server.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CCP Call Control Server APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Call Control Profile (CCP)](group__bt__ccp.md)

| Functions | |
| --- | --- |
| int | [bt\_ccp\_call\_control\_server\_register\_bearer](#ga5e5acb90cc39b5f8a4e25d8ab8a11b10) (const struct [bt\_tbs\_register\_param](structbt__tbs__register__param.md) \*param, struct bt\_ccp\_call\_control\_server\_bearer \*\*bearer) |
|  | Register a Telephone Bearer. |
| int | [bt\_ccp\_call\_control\_server\_unregister\_bearer](#gaa2486dec8a47bd7f4cd4076477e8ac4a) (struct bt\_ccp\_call\_control\_server\_bearer \*bearer) |
|  | Unregister a Telephone Bearer. |

## Detailed Description

## Function Documentation

## [◆ ](#ga5e5acb90cc39b5f8a4e25d8ab8a11b10)bt\_ccp\_call\_control\_server\_register\_bearer()

| int bt\_ccp\_call\_control\_server\_register\_bearer | ( | const struct [bt\_tbs\_register\_param](structbt__tbs__register__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_ccp\_call\_control\_server\_bearer \*\* | *bearer* ) |

`#include <[ccp.h](ccp_8h.md)>`

Register a Telephone Bearer.

This will register a Telephone Bearer Service (TBS) (or a Generic Telephone Bearer service (GTBS)) with the provided parameters.

As per the TBS specification, the GTBS shall be instantiated for the feature, and as such a GTBS shall always be registered before any TBS can be registered. Similarly, all TBS shall be unregistered before the GTBS can be unregistered with [bt\_ccp\_call\_control\_server\_unregister\_bearer()](#gaa2486dec8a47bd7f4cd4076477e8ac4a).

Parameters
:   | [in] | param | The parameters to initialize the bearer. |
    | --- | --- | --- |
    | [out] | bearer | Pointer to the initialized bearer. |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `param` contains invalid data |
    | -EALREADY | `param.gtbs` is true and GTBS has already been registered |
    | -EAGAIN | `param.gtbs` is false and GTBS has not been registered |
    | -ENOMEM | `param.gtbs` is false and no more TBS can be registered (see `CONFIG_BT_TBS_BEARER_COUNT`) |
    | -ENOEXEC | The service failed to be registered |

## [◆ ](#gaa2486dec8a47bd7f4cd4076477e8ac4a)bt\_ccp\_call\_control\_server\_unregister\_bearer()

| int bt\_ccp\_call\_control\_server\_unregister\_bearer | ( | struct bt\_ccp\_call\_control\_server\_bearer \* | *bearer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccp.h](ccp_8h.md)>`

Unregister a Telephone Bearer.

This will unregister a Telephone Bearer Service (TBS) (or a Generic Telephone Bearer service (GTBS)) with the provided parameters. The bearer shall be registered first by [bt\_ccp\_call\_control\_server\_register\_bearer()](#ga5e5acb90cc39b5f8a4e25d8ab8a11b10) before it can be unregistered.

All TBS shall be unregistered before the GTBS can be unregistered with.

Parameters
:   | bearer | The bearer to unregister. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `bearer` is NULL |
    | -EALREADY | The bearer is not registered |
    | -ENOEXEC | The service failed to be unregistered |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
