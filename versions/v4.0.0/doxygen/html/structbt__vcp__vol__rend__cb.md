---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__vcp__vol__rend__cb.html
original_path: doxygen/html/structbt__vcp__vol__rend__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_vcp\_vol\_rend\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Volume Control Profile (VCP)](group__bt__vcp.md)

Struct to hold the Volume Renderer callbacks.
[More...](#details)

`#include <[vcp.h](vcp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [state](#a05f84d8a2deedbc426ef22b89c87bd40) )(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute) |
|  | Callback function for Volume Control Service volume state. |
| void(\* | [flags](#a3413d33fa8c3362ded6ec81533c27c86) )(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Callback function for Volume Control Service flags. |

## Detailed Description

Struct to hold the Volume Renderer callbacks.

These can be registered for usage with [bt\_vcp\_vol\_rend\_register()](group__bt__vcp.md#ga752d8ff54a4b8c8c854a9c693617e64d "Register the Volume Control Service.").

## Field Documentation

## [◆ ](#a3413d33fa8c3362ded6ec81533c27c86)flags

| void(\* bt\_vcp\_vol\_rend\_cb::flags) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

Callback function for Volume Control Service flags.

Called when the value is locally read as the server. Called when the value is remotely read as the client. Called if the value is changed by either the server or client.

Parameters
:   | conn | Pointer to the connection to a remote device if the change was caused by it, otherwise NULL. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | [flags](#a3413d33fa8c3362ded6ec81533c27c86) | The flags of the Volume Control Service server. |

## [◆ ](#a05f84d8a2deedbc426ef22b89c87bd40)state

| void(\* bt\_vcp\_vol\_rend\_cb::state) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute) |
| --- |

Callback function for Volume Control Service volume state.

Called when the value is locally read with [bt\_vcp\_vol\_rend\_get\_state()](group__bt__vcp.md#ga9d1ac028abc88549ea18b6a0c585c781 "Get the Volume Control Service volume state."), or if the state is changed by either the Volume Renderer or a remote Volume Controller.

Parameters
:   | conn | Pointer to the connection to a remote device if the change was caused by it, otherwise NULL. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | volume | The volume of the Volume Control Service server. |
    | mute | The mute setting of the Volume Control Service server. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[vcp.h](vcp_8h_source.md)

- [bt\_vcp\_vol\_rend\_cb](structbt__vcp__vol__rend__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
