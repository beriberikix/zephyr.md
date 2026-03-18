---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__vcp__vol__ctlr__cb.html
original_path: doxygen/html/structbt__vcp__vol__ctlr__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_vcp\_vol\_ctlr\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Volume Control Profile (VCP)](group__bt__gatt__vcp.md)

Struct to hold the Volume Controller callbacks.
[More...](#details)

`#include <[vcp.h](vcp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [state](#ac3b89f35b79d35384f9ead31cf15ac4e) )(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mute](#aa2cd77992831eef7e59d3e4a01a0e542)) |
|  | Callback function for Volume Control Profile volume state. |
| void(\* | [flags](#a4df90987abe0e53894e4064b3487c2bb) )(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Callback function for Volume Control Profile volume flags. |
| void(\* | [discover](#ada8fe8d838d6d2c983d746e7e7ed1171) )(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vocs\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) aics\_count) |
|  | Callback function for [bt\_vcp\_vol\_ctlr\_discover()](group__bt__gatt__vcp.md#gac18d43a0785155c1131249f95554f2de "Discover Volume Control Service and included services."). |
| void(\* | [vol\_down](#ac986e0c5cb49395fe8581f5b1dae1a88) )(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
|  | Callback function for [bt\_vcp\_vol\_ctlr\_vol\_down()](group__bt__gatt__vcp.md#ga03e073e29920f4a530d2f8851b4b8df4 "Turn the volume down one step on a remote Volume Renderer."). |
| void(\* | [vol\_up](#ae1beaa5d0a61c630fa90b4a5236ce743) )(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
|  | Callback function for [bt\_vcp\_vol\_ctlr\_vol\_up()](group__bt__gatt__vcp.md#ga908eb20727e1d68ed569badfd13ff896 "Turn the volume up one step on a remote Volume Renderer."). |
| void(\* | [mute](#aa2cd77992831eef7e59d3e4a01a0e542) )(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
|  | Callback function for [bt\_vcp\_vol\_ctlr\_mute()](group__bt__gatt__vcp.md#ga106b7f826adec665b4f0ac3d5e82b867 "Mute a remote Volume Renderer."). |
| void(\* | [unmute](#a6a217e0d8cbcc56e5128d5b7acdaac6d) )(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
|  | Callback function for [bt\_vcp\_vol\_ctlr\_unmute()](group__bt__gatt__vcp.md#ga4e95c3fb071cb94fbe75f88e96d34b36 "Unmute a remote Volume Renderer."). |
| void(\* | [vol\_down\_unmute](#a770e300127b8357f1e76f0cca21b74e5) )(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
|  | Callback function for bt\_vcp\_vol\_ctlr\_vol\_down\_unmute(). |
| void(\* | [vol\_up\_unmute](#af4ca636d19c83694f9b86102404b0538) )(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
|  | Callback function for bt\_vcp\_vol\_ctlr\_vol\_up\_unmute(). |
| void(\* | [vol\_set](#abe7cf51858428db6b953a21a6ba40f83) )(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
|  | Callback function for bt\_vcp\_vol\_ctlr\_vol\_set(). |
| struct [bt\_vocs\_cb](structbt__vocs__cb.md) | [vocs\_cb](#af6407bb0652539608f0100f02cfaadd1) |
|  | Volume Offset Control Service callbacks. |
| struct [bt\_aics\_cb](structbt__aics__cb.md) | [aics\_cb](#a430b1ee27c9bf7d6c7f8498748d91b21) |
|  | Audio Input Control Service callbacks. |

## Detailed Description

Struct to hold the Volume Controller callbacks.

These can be registered for usage with [bt\_vcp\_vol\_ctlr\_cb\_register()](group__bt__gatt__vcp.md#ga7861d0c3426870c015106e8e170004a3 "Registers the callbacks used by the Volume Controller.").

## Field Documentation

## [◆ ](#a430b1ee27c9bf7d6c7f8498748d91b21)aics\_cb

| struct [bt\_aics\_cb](structbt__aics__cb.md) bt\_vcp\_vol\_ctlr\_cb::aics\_cb |
| --- |

Audio Input Control Service callbacks.

## [◆ ](#ada8fe8d838d6d2c983d746e7e7ed1171)discover

| void(\* bt\_vcp\_vol\_ctlr\_cb::discover) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vocs\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) aics\_count) |
| --- |

Callback function for [bt\_vcp\_vol\_ctlr\_discover()](group__bt__gatt__vcp.md#gac18d43a0785155c1131249f95554f2de "Discover Volume Control Service and included services.").

This callback is called once the discovery procedure is completed.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | vocs\_count | Number of Volume Offset Control Service instances on the remote Volume Renderer. |
    | aics\_count | Number of Audio Input Control Service instances the remote Volume Renderer. |

## [◆ ](#a4df90987abe0e53894e4064b3487c2bb)flags

| void(\* bt\_vcp\_vol\_ctlr\_cb::flags) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

Callback function for Volume Control Profile volume flags.

Called when the value is remotely read as the Volume Controller. Called if the value is changed by the Volume Renderer.

A non-zero value indicates the volume has been changed on the Volume Renderer since it was booted.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | [flags](#a4df90987abe0e53894e4064b3487c2bb) | The flags of the Volume Renderer. |

## [◆ ](#aa2cd77992831eef7e59d3e4a01a0e542)mute

| void(\* bt\_vcp\_vol\_ctlr\_cb::mute) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
| --- |

Callback function for [bt\_vcp\_vol\_ctlr\_mute()](group__bt__gatt__vcp.md#ga106b7f826adec665b4f0ac3d5e82b867 "Mute a remote Volume Renderer.").

Called when the mute procedure is completed.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |

## [◆ ](#ac3b89f35b79d35384f9ead31cf15ac4e)state

| void(\* bt\_vcp\_vol\_ctlr\_cb::state) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mute](#aa2cd77992831eef7e59d3e4a01a0e542)) |
| --- |

Callback function for Volume Control Profile volume state.

Called when the value is remotely read as the Volume Controller. Called if the value is changed by either the Volume Renderer or Volume Controller, and notified to the to Volume Controller.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | volume | The volume of the Volume Renderer. |
    | [mute](#aa2cd77992831eef7e59d3e4a01a0e542) | The mute setting of the Volume Renderer. |

## [◆ ](#a6a217e0d8cbcc56e5128d5b7acdaac6d)unmute

| void(\* bt\_vcp\_vol\_ctlr\_cb::unmute) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
| --- |

Callback function for [bt\_vcp\_vol\_ctlr\_unmute()](group__bt__gatt__vcp.md#ga4e95c3fb071cb94fbe75f88e96d34b36 "Unmute a remote Volume Renderer.").

Called when the unmute procedure is completed.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |

## [◆ ](#af6407bb0652539608f0100f02cfaadd1)vocs\_cb

| struct [bt\_vocs\_cb](structbt__vocs__cb.md) bt\_vcp\_vol\_ctlr\_cb::vocs\_cb |
| --- |

Volume Offset Control Service callbacks.

## [◆ ](#ac986e0c5cb49395fe8581f5b1dae1a88)vol\_down

| void(\* bt\_vcp\_vol\_ctlr\_cb::vol\_down) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
| --- |

Callback function for [bt\_vcp\_vol\_ctlr\_vol\_down()](group__bt__gatt__vcp.md#ga03e073e29920f4a530d2f8851b4b8df4 "Turn the volume down one step on a remote Volume Renderer.").

Called when the volume down procedure is completed.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |

## [◆ ](#a770e300127b8357f1e76f0cca21b74e5)vol\_down\_unmute

| void(\* bt\_vcp\_vol\_ctlr\_cb::vol\_down\_unmute) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
| --- |

Callback function for bt\_vcp\_vol\_ctlr\_vol\_down\_unmute().

Called when the volume down and unmute procedure is completed.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |

## [◆ ](#abe7cf51858428db6b953a21a6ba40f83)vol\_set

| void(\* bt\_vcp\_vol\_ctlr\_cb::vol\_set) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
| --- |

Callback function for bt\_vcp\_vol\_ctlr\_vol\_set().

Called when the set absolute volume procedure is completed.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |

## [◆ ](#ae1beaa5d0a61c630fa90b4a5236ce743)vol\_up

| void(\* bt\_vcp\_vol\_ctlr\_cb::vol\_up) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
| --- |

Callback function for [bt\_vcp\_vol\_ctlr\_vol\_up()](group__bt__gatt__vcp.md#ga908eb20727e1d68ed569badfd13ff896 "Turn the volume up one step on a remote Volume Renderer.").

Called when the volume up procedure is completed.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |

## [◆ ](#af4ca636d19c83694f9b86102404b0538)vol\_up\_unmute

| void(\* bt\_vcp\_vol\_ctlr\_cb::vol\_up\_unmute) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err) |
| --- |

Callback function for bt\_vcp\_vol\_ctlr\_vol\_up\_unmute().

Called when the volume up and unmute procedure is completed.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[vcp.h](vcp_8h_source.md)

- [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
