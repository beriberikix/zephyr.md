---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__csip__set__member__cb.html
original_path: doxygen/html/structbt__csip__set__member__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_csip\_set\_member\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Coordinated Set Identification Profile (CSIP)](group__bt__csip.md)

Callback structure for the Coordinated Set Identification Service.
[More...](#details)

`#include <[csip.h](csip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [lock\_changed](#a46e18120caf78788f0928ada2c92ca5c) )(struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) locked) |
|  | Callback whenever the lock changes on the server. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [sirk\_read\_req](#a30b2f68aff4b75ffcc8e9d7e2de2afd9) )(struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst) |
|  | Request from a peer device to read the sirk. |

## Detailed Description

Callback structure for the Coordinated Set Identification Service.

## Field Documentation

## [◆ ](#a46e18120caf78788f0928ada2c92ca5c)lock\_changed

| void(\* bt\_csip\_set\_member\_cb::lock\_changed) (struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) locked) |
| --- |

Callback whenever the lock changes on the server.

Parameters
:   | conn | The connection to the client that changed the lock. NULL if server changed it, either by calling [bt\_csip\_set\_member\_lock()](group__bt__csip.md#ga95e2ba4b65ec42eedb26bf5ad181b606 "Locks a specific Coordinated Set Identification Service instance on the server.") or by timeout. |
    | --- | --- |
    | svc\_inst | Pointer to the Coordinated Set Identification Service. |
    | locked | Whether the lock was locked or released. |

## [◆ ](#a30b2f68aff4b75ffcc8e9d7e2de2afd9)sirk\_read\_req

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* bt\_csip\_set\_member\_cb::sirk\_read\_req) (struct bt\_conn \*conn, struct bt\_csip\_set\_member\_svc\_inst \*svc\_inst) |
| --- |

Request from a peer device to read the sirk.

If this callback is not set, all clients will be allowed to read the SIRK unencrypted.

Parameters
:   | conn | The connection to the client that requested to read the SIRK. |
    | --- | --- |
    | svc\_inst | Pointer to the Coordinated Set Identification Service. |

Returns
:   A BT\_CSIP\_READ\_SIRK\_REQ\_RSP\_\* response code.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[csip.h](csip_8h_source.md)

- [bt\_csip\_set\_member\_cb](structbt__csip__set__member__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
