---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__vocs__cb.html
original_path: doxygen/html/structbt__vocs__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_vocs\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Volume Offset Control Service (VOCS)](group__bt__gatt__vocs.md)

Struct to hold the Volume Offset Control Service callbacks.
[More...](#details)

`#include <[vocs.h](vocs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_vocs\_state\_cb](group__bt__gatt__vocs.md#gaa329fd8931add8fd4f6c59b48c91ef75) | [state](#ae633c1f6cd8aa03d89287e783179460e) |
|  | The offset state has changed. |
| [bt\_vocs\_location\_cb](group__bt__gatt__vocs.md#ga84983707e04eae75f18017072b647115) | [location](#a50d1d429089456267b06d4450712b897) |
|  | The location has changed. |
| [bt\_vocs\_description\_cb](group__bt__gatt__vocs.md#gaa351c3ab631b16272e27cbb837d9e49c) | [description](#ac508b1e6dda00c607aa1cbe52423ec52) |
|  | The Description has changed. |
| [bt\_vocs\_discover\_cb](group__bt__gatt__vocs.md#gad50fd539190b5c64b5262d3830699365) | [discover](#a2ff42997b87d2a910325d4b04e67f4c5) |
|  | The discovery procedure has completed. |
| [bt\_vocs\_set\_offset\_cb](group__bt__gatt__vocs.md#ga2630344190f12f911bb2b01c4b95ded6) | [set\_offset](#a1b5a3359602ceea1a45ebe7aa79e6b3a) |
|  | The set offset procedure has completed. |

## Detailed Description

Struct to hold the Volume Offset Control Service callbacks.

These can be registered for usage with [bt\_vocs\_client\_cb\_register()](group__bt__gatt__vocs.md#gaace802556eca3d634a13dd8f2bf3c544 "Registers the callbacks for the Volume Offset Control Service client.") or [bt\_vocs\_register()](group__bt__gatt__vocs.md#gac011ddd93bb3240148a789f1ee9ef7da "Register the Volume Offset Control Service instance.") depending on the role.

## Field Documentation

## [◆ ](#ac508b1e6dda00c607aa1cbe52423ec52)description

| [bt\_vocs\_description\_cb](group__bt__gatt__vocs.md#gaa351c3ab631b16272e27cbb837d9e49c) bt\_vocs\_cb::description |
| --- |

The Description has changed.

## [◆ ](#a2ff42997b87d2a910325d4b04e67f4c5)discover

| [bt\_vocs\_discover\_cb](group__bt__gatt__vocs.md#gad50fd539190b5c64b5262d3830699365) bt\_vocs\_cb::discover |
| --- |

The discovery procedure has completed.

Only settable for the client and requires enabling `CONFIG_BT_VOCS_CLIENT` .

## [◆ ](#a50d1d429089456267b06d4450712b897)location

| [bt\_vocs\_location\_cb](group__bt__gatt__vocs.md#ga84983707e04eae75f18017072b647115) bt\_vocs\_cb::location |
| --- |

The location has changed.

## [◆ ](#a1b5a3359602ceea1a45ebe7aa79e6b3a)set\_offset

| [bt\_vocs\_set\_offset\_cb](group__bt__gatt__vocs.md#ga2630344190f12f911bb2b01c4b95ded6) bt\_vocs\_cb::set\_offset |
| --- |

The set offset procedure has completed.

Only settable for the client and requires enabling `CONFIG_BT_VOCS_CLIENT` .

## [◆ ](#ae633c1f6cd8aa03d89287e783179460e)state

| [bt\_vocs\_state\_cb](group__bt__gatt__vocs.md#gaa329fd8931add8fd4f6c59b48c91ef75) bt\_vocs\_cb::state |
| --- |

The offset state has changed.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[vocs.h](vocs_8h_source.md)

- [bt\_vocs\_cb](structbt__vocs__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
