---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__ccp__call__control__client__cb.html
original_path: doxygen/html/structbt__ccp__call__control__client__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_ccp\_call\_control\_client\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Call Control Profile (CCP)](group__bt__ccp.md) » [CCP Call Control Client APIs](group__bt__ccp__call__control__client.md)

Struct to hold the Telephone Bearer Service client callbacks.
[More...](#details)

`#include <[ccp.h](ccp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [discover](#a322f75bc9d28efc74f9a4571e952ed5e) )(struct bt\_ccp\_call\_control\_client \*client, int err, struct [bt\_ccp\_call\_control\_client\_bearers](structbt__ccp__call__control__client__bearers.md) \*bearers) |
|  | Callback function for [bt\_ccp\_call\_control\_client\_discover()](group__bt__ccp__call__control__client.md#ga2a5bce65e39ba05625423308f996021d "Discovers the Telephone Bearer Service (TBS) support on a remote device."). |

## Detailed Description

Struct to hold the Telephone Bearer Service client callbacks.

These can be registered for usage with [bt\_tbs\_client\_register\_cb()](group__bt__tbs.md#gabe2251d4ea88306793dc68ae683886bb "Register the callbacks for CCP.").

## Field Documentation

## [◆ ](#a322f75bc9d28efc74f9a4571e952ed5e)discover

| void(\* bt\_ccp\_call\_control\_client\_cb::discover) (struct bt\_ccp\_call\_control\_client \*client, int err, struct [bt\_ccp\_call\_control\_client\_bearers](structbt__ccp__call__control__client__bearers.md) \*bearers) |
| --- |

Callback function for [bt\_ccp\_call\_control\_client\_discover()](group__bt__ccp__call__control__client.md#ga2a5bce65e39ba05625423308f996021d "Discovers the Telephone Bearer Service (TBS) support on a remote device.").

This callback is called once the discovery procedure is completed.

Parameters
:   | client | Call Control Client pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | bearers | The bearers found. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[ccp.h](ccp_8h_source.md)

- [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
