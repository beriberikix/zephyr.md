---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__gatt__vcp.html
original_path: doxygen/html/group__bt__gatt__vcp.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Volume Control Profile (VCP)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Volume Control Profile (VCP).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md) |
|  | Register structure for Volume Control Service. [More...](structbt__vcp__vol__rend__register__param.md#details) |
| struct | [bt\_vcp\_included](structbt__vcp__included.md) |
|  | Volume Control Service included services. [More...](structbt__vcp__included.md#details) |
| struct | [bt\_vcp\_vol\_rend\_cb](structbt__vcp__vol__rend__cb.md) |
| struct | [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) |

| Macros | |
| --- | --- |
| #define | [BT\_VCP\_VOL\_REND\_VOCS\_CNT](#gae7195f4556ad2442bc45d8d43cdeedd0)   0 |
| #define | [BT\_VCP\_VOL\_REND\_AICS\_CNT](#ga571d7ff5a6a507fcd7cbdfa32a04643b)   0 |
| #define | [BT\_VCP\_ERR\_INVALID\_COUNTER](#gabb8bdfde60f1cbb31bab41fd61b3384b)   0x80 |
|  | Volume Control Service Error codes. |
| #define | [BT\_VCP\_ERR\_OP\_NOT\_SUPPORTED](#gad979c43e4d84f52009d9931fb74628e6)   0x81 |
| #define | [BT\_VCP\_STATE\_UNMUTED](#ga4660f938a16113f715dd8aec3ed3baf6)   0x00 |
|  | Volume Control Service Mute Values. |
| #define | [BT\_VCP\_STATE\_MUTED](#ga3d6ffdfb9e0d8d58073f4a130a8020b0)   0x01 |

| Functions | |
| --- | --- |
| int | [bt\_vcp\_vol\_rend\_included\_get](#ga1761d6618c48983e034cee5574c9c34f) (struct [bt\_vcp\_included](structbt__vcp__included.md) \*included) |
|  | Get Volume Control Service included services. |
| int | [bt\_vcp\_vol\_rend\_register](#ga752d8ff54a4b8c8c854a9c693617e64d) (struct [bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md) \*param) |
|  | Register the Volume Control Service. |
| int | [bt\_vcp\_vol\_rend\_set\_step](#ga56e0f99d2688fb6f9e0e4d9103de706c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume\_step) |
|  | Set the Volume Control Service volume step size. |
| int | [bt\_vcp\_vol\_rend\_get\_state](#ga9d1ac028abc88549ea18b6a0c585c781) (void) |
|  | Get the Volume Control Service volume state. |
| int | [bt\_vcp\_vol\_rend\_get\_flags](#ga1e6c9cfa0d012a4b701c99d8e6b5985d) (void) |
|  | Get the Volume Control Service flags. |
| int | [bt\_vcp\_vol\_rend\_vol\_down](#gaf3c622f151a21d1dd617e97917c5ff5e) (void) |
|  | Turn the volume down by one step on the server. |
| int | [bt\_vcp\_vol\_rend\_vol\_up](#ga6c10dd5a029b524994739f0b37a82c84) (void) |
|  | Turn the volume up by one step on the server. |
| int | [bt\_vcp\_vol\_rend\_unmute\_vol\_down](#ga3e6236a8679f95ba512181284a05923d) (void) |
|  | Turn the volume down and unmute the server. |
| int | [bt\_vcp\_vol\_rend\_unmute\_vol\_up](#gadf77729fee34f6605101c278fd2b7c46) (void) |
|  | Turn the volume up and unmute the server. |
| int | [bt\_vcp\_vol\_rend\_set\_vol](#ga61279baeba11152625cd3a87c5d973c9) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume) |
|  | Set the volume on the server. |
| int | [bt\_vcp\_vol\_rend\_unmute](#ga303d4b6b77987ab41cb1753ef861dd6c) (void) |
|  | Unmute the server. |
| int | [bt\_vcp\_vol\_rend\_mute](#ga0c6d0b6b015f069a9adc1332a32c79f9) (void) |
|  | Mute the server. |
| int | [bt\_vcp\_vol\_ctlr\_cb\_register](#ga7861d0c3426870c015106e8e170004a3) (struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) \*cb) |
|  | Registers the callbacks used by the Volume Controller. |
| int | [bt\_vcp\_vol\_ctlr\_cb\_unregister](#gae69e4730df4341bbb9bbbba1bea14005) (struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) \*cb) |
|  | Unregisters the callbacks used by the Volume Controller. |
| int | [bt\_vcp\_vol\_ctlr\_discover](#gac18d43a0785155c1131249f95554f2de) (struct bt\_conn \*conn, struct bt\_vcp\_vol\_ctlr \*\*vol\_ctlr) |
|  | Discover Volume Control Service and included services. |
| struct bt\_vcp\_vol\_ctlr \* | [bt\_vcp\_vol\_ctlr\_get\_by\_conn](#ga0c8faa95cc36950c70ff572c931eedee) (const struct bt\_conn \*conn) |
|  | Get the volume controller from a connection pointer. |
| int | [bt\_vcp\_vol\_ctlr\_conn\_get](#gab287197243191e3dbf162c6d16b6d726) (const struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, struct bt\_conn \*\*conn) |
|  | Get the connection pointer of a client instance. |
| int | [bt\_vcp\_vol\_ctlr\_included\_get](#gaaa748c49e103ff161f67df9663ea6330) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, struct [bt\_vcp\_included](structbt__vcp__included.md) \*included) |
|  | Get Volume Control Service included services. |
| int | [bt\_vcp\_vol\_ctlr\_read\_state](#ga68cab2f59c63542b6a7da33d555da0ab) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Read the volume state of a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_read\_flags](#gaefc226a5abb6bb1540d4b44ac4ddc236) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Read the volume flags of a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_vol\_down](#ga03e073e29920f4a530d2f8851b4b8df4) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Turn the volume down one step on a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_vol\_up](#ga908eb20727e1d68ed569badfd13ff896) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Turn the volume up one step on a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_unmute\_vol\_down](#ga20348b220988c700cabf356f7165d4d6) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Turn the volume down one step and unmute on a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_unmute\_vol\_up](#ga2defdeee7486eee22a3416db8aa7c251) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Turn the volume up one step and unmute on a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_set\_vol](#gaaa5b5cd9a11c0e1fcdabce690ba20616) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume) |
|  | Set the absolute volume on a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_unmute](#ga4e95c3fb071cb94fbe75f88e96d34b36) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Unmute a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_mute](#ga106b7f826adec665b4f0ac3d5e82b867) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Mute a remote Volume Renderer. |

## Detailed Description

Volume Control Profile (VCP).

[Experimental] Users should note that the APIs can change as a part of ongoing development.

## Macro Definition Documentation

## [◆ ](#gabb8bdfde60f1cbb31bab41fd61b3384b)BT\_VCP\_ERR\_INVALID\_COUNTER

| #define BT\_VCP\_ERR\_INVALID\_COUNTER   0x80 |
| --- |

`#include <[vcp.h](vcp_8h.md)>`

Volume Control Service Error codes.

## [◆ ](#gad979c43e4d84f52009d9931fb74628e6)BT\_VCP\_ERR\_OP\_NOT\_SUPPORTED

| #define BT\_VCP\_ERR\_OP\_NOT\_SUPPORTED   0x81 |
| --- |

`#include <[vcp.h](vcp_8h.md)>`

## [◆ ](#ga3d6ffdfb9e0d8d58073f4a130a8020b0)BT\_VCP\_STATE\_MUTED

| #define BT\_VCP\_STATE\_MUTED   0x01 |
| --- |

`#include <[vcp.h](vcp_8h.md)>`

## [◆ ](#ga4660f938a16113f715dd8aec3ed3baf6)BT\_VCP\_STATE\_UNMUTED

| #define BT\_VCP\_STATE\_UNMUTED   0x00 |
| --- |

`#include <[vcp.h](vcp_8h.md)>`

Volume Control Service Mute Values.

## [◆ ](#ga571d7ff5a6a507fcd7cbdfa32a04643b)BT\_VCP\_VOL\_REND\_AICS\_CNT

| #define BT\_VCP\_VOL\_REND\_AICS\_CNT   0 |
| --- |

`#include <[vcp.h](vcp_8h.md)>`

## [◆ ](#gae7195f4556ad2442bc45d8d43cdeedd0)BT\_VCP\_VOL\_REND\_VOCS\_CNT

| #define BT\_VCP\_VOL\_REND\_VOCS\_CNT   0 |
| --- |

`#include <[vcp.h](vcp_8h.md)>`

## Function Documentation

## [◆ ](#ga7861d0c3426870c015106e8e170004a3)bt\_vcp\_vol\_ctlr\_cb\_register()

| int bt\_vcp\_vol\_ctlr\_cb\_register | ( | struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Registers the callbacks used by the Volume Controller.

Parameters
:   | cb | The callback structure. |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | if `cb` is NULL |
    | -EALREADY | if `cb` was already registered |

## [◆ ](#gae69e4730df4341bbb9bbbba1bea14005)bt\_vcp\_vol\_ctlr\_cb\_unregister()

| int bt\_vcp\_vol\_ctlr\_cb\_unregister | ( | struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Unregisters the callbacks used by the Volume Controller.

Parameters
:   | cb | The callback structure. |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | if `cb` is NULL |
    | -EALREADY | if `cb` was not registered |

## [◆ ](#gab287197243191e3dbf162c6d16b6d726)bt\_vcp\_vol\_ctlr\_conn\_get()

| int bt\_vcp\_vol\_ctlr\_conn\_get | ( | const struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \*\* | *conn* ) |

`#include <[vcp.h](vcp_8h.md)>`

Get the connection pointer of a client instance.

Get the Bluetooth connection pointer of a Volume Control Service client instance.

Parameters
:   |  | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- | --- |
    | [out] | conn | Connection pointer. |

Returns
:   0 if success, errno on failure.

## [◆ ](#gac18d43a0785155c1131249f95554f2de)bt\_vcp\_vol\_ctlr\_discover()

| int bt\_vcp\_vol\_ctlr\_discover | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct bt\_vcp\_vol\_ctlr \*\* | *vol\_ctlr* ) |

`#include <[vcp.h](vcp_8h.md)>`

Discover Volume Control Service and included services.

This will start a GATT discovery and setup handles and subscriptions. This shall be called once before any other actions can be executed for the peer device, and the [bt\_vcp\_vol\_ctlr\_cb::discover](structbt__vcp__vol__ctlr__cb.md#ada8fe8d838d6d2c983d746e7e7ed1171 "bt_vcp_vol_ctlr_cb::discover") callback will notify when it is possible to start remote operations.

This shall only be done as the client,

Parameters
:   |  | conn | The connection to discover Volume Control Service for. |
    | --- | --- | --- |
    | [out] | vol\_ctlr | Valid remote instance object on success. |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga0c8faa95cc36950c70ff572c931eedee)bt\_vcp\_vol\_ctlr\_get\_by\_conn()

| struct bt\_vcp\_vol\_ctlr \* bt\_vcp\_vol\_ctlr\_get\_by\_conn | ( | const struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Get the volume controller from a connection pointer.

Get the Volume Control Profile Volume Controller pointer from a connection pointer. Only volume controllers that have been initiated via [bt\_vcp\_vol\_ctlr\_discover()](#gac18d43a0785155c1131249f95554f2de) can be retrieved.

Parameters
:   | conn | Connection pointer. |
    | --- | --- |

Return values
:   | Pointer | to a Volume Control Profile Volume Controller instance |
    | --- | --- |
    | NULL | if `conn` is NULL or if the connection has not done discovery yet |

## [◆ ](#gaaa748c49e103ff161f67df9663ea6330)bt\_vcp\_vol\_ctlr\_included\_get()

| int bt\_vcp\_vol\_ctlr\_included\_get | ( | struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_vcp\_included](structbt__vcp__included.md) \* | *included* ) |

`#include <[vcp.h](vcp_8h.md)>`

Get Volume Control Service included services.

Returns a pointer to a struct that contains information about the Volume Control Service included service instances, such as pointers to the Volume Offset Control Service (Volume Offset Control Service) or Audio Input Control Service (AICS) instances.

Requires that `CONFIG_BT_VCP_VOL_CTLR_VOCS` or `CONFIG_BT_VCP_VOL_CTLR_AICS` is enabled.

Parameters
:   |  | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- | --- |
    | [out] | included | Pointer to store the result in. |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga106b7f826adec665b4f0ac3d5e82b867)bt\_vcp\_vol\_ctlr\_mute()

| int bt\_vcp\_vol\_ctlr\_mute | ( | struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Mute a remote Volume Renderer.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaefc226a5abb6bb1540d4b44ac4ddc236)bt\_vcp\_vol\_ctlr\_read\_flags()

| int bt\_vcp\_vol\_ctlr\_read\_flags | ( | struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Read the volume flags of a remote Volume Renderer.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga68cab2f59c63542b6a7da33d555da0ab)bt\_vcp\_vol\_ctlr\_read\_state()

| int bt\_vcp\_vol\_ctlr\_read\_state | ( | struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Read the volume state of a remote Volume Renderer.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaaa5b5cd9a11c0e1fcdabce690ba20616)bt\_vcp\_vol\_ctlr\_set\_vol()

| int bt\_vcp\_vol\_ctlr\_set\_vol | ( | struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *volume* ) |

`#include <[vcp.h](vcp_8h.md)>`

Set the absolute volume on a remote Volume Renderer.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |
    | volume | The absolute volume to set. |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga4e95c3fb071cb94fbe75f88e96d34b36)bt\_vcp\_vol\_ctlr\_unmute()

| int bt\_vcp\_vol\_ctlr\_unmute | ( | struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Unmute a remote Volume Renderer.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga20348b220988c700cabf356f7165d4d6)bt\_vcp\_vol\_ctlr\_unmute\_vol\_down()

| int bt\_vcp\_vol\_ctlr\_unmute\_vol\_down | ( | struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Turn the volume down one step and unmute on a remote Volume Renderer.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga2defdeee7486eee22a3416db8aa7c251)bt\_vcp\_vol\_ctlr\_unmute\_vol\_up()

| int bt\_vcp\_vol\_ctlr\_unmute\_vol\_up | ( | struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Turn the volume up one step and unmute on a remote Volume Renderer.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga03e073e29920f4a530d2f8851b4b8df4)bt\_vcp\_vol\_ctlr\_vol\_down()

| int bt\_vcp\_vol\_ctlr\_vol\_down | ( | struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Turn the volume down one step on a remote Volume Renderer.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga908eb20727e1d68ed569badfd13ff896)bt\_vcp\_vol\_ctlr\_vol\_up()

| int bt\_vcp\_vol\_ctlr\_vol\_up | ( | struct bt\_vcp\_vol\_ctlr \* | *vol\_ctlr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Turn the volume up one step on a remote Volume Renderer.

Parameters
:   | vol\_ctlr | Volume Controller instance pointer. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga1e6c9cfa0d012a4b701c99d8e6b5985d)bt\_vcp\_vol\_rend\_get\_flags()

| int bt\_vcp\_vol\_rend\_get\_flags | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Get the Volume Control Service flags.

Returns
:   0 if success, errno on failure.

## [◆ ](#ga9d1ac028abc88549ea18b6a0c585c781)bt\_vcp\_vol\_rend\_get\_state()

| int bt\_vcp\_vol\_rend\_get\_state | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Get the Volume Control Service volume state.

Returns
:   0 if success, errno on failure.

## [◆ ](#ga1761d6618c48983e034cee5574c9c34f)bt\_vcp\_vol\_rend\_included\_get()

| int bt\_vcp\_vol\_rend\_included\_get | ( | struct [bt\_vcp\_included](structbt__vcp__included.md) \* | *included* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Get Volume Control Service included services.

Returns a pointer to a struct that contains information about the Volume Control Service included service instances, such as pointers to the Volume Offset Control Service (Volume Offset Control Service) or Audio Input Control Service (AICS) instances.

Parameters
:   | [out] | included | Pointer to store the result in. |
    | --- | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga0c6d0b6b015f069a9adc1332a32c79f9)bt\_vcp\_vol\_rend\_mute()

| int bt\_vcp\_vol\_rend\_mute | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Mute the server.

Returns
:   0 if success, errno on failure.

## [◆ ](#ga752d8ff54a4b8c8c854a9c693617e64d)bt\_vcp\_vol\_rend\_register()

| int bt\_vcp\_vol\_rend\_register | ( | struct [bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Register the Volume Control Service.

This will register and enable the service and make it discoverable by clients.

Parameters
:   | param | Volume Control Service register parameters. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga56e0f99d2688fb6f9e0e4d9103de706c)bt\_vcp\_vol\_rend\_set\_step()

| int bt\_vcp\_vol\_rend\_set\_step | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *volume\_step* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Set the Volume Control Service volume step size.

Set the value that the volume changes, when changed relatively with e.g. [bt\_vcp\_vol\_rend\_vol\_down](#gaf3c622f151a21d1dd617e97917c5ff5e) or [bt\_vcp\_vol\_rend\_vol\_up](#ga6c10dd5a029b524994739f0b37a82c84).

This can only be done as the server.

Parameters
:   | volume\_step | The volume step size (1-255). |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga61279baeba11152625cd3a87c5d973c9)bt\_vcp\_vol\_rend\_set\_vol()

| int bt\_vcp\_vol\_rend\_set\_vol | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *volume* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Set the volume on the server.

Parameters
:   | volume | The absolute volume to set. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga303d4b6b77987ab41cb1753ef861dd6c)bt\_vcp\_vol\_rend\_unmute()

| int bt\_vcp\_vol\_rend\_unmute | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Unmute the server.

Returns
:   0 if success, errno on failure.

## [◆ ](#ga3e6236a8679f95ba512181284a05923d)bt\_vcp\_vol\_rend\_unmute\_vol\_down()

| int bt\_vcp\_vol\_rend\_unmute\_vol\_down | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Turn the volume down and unmute the server.

Returns
:   0 if success, errno on failure.

## [◆ ](#gadf77729fee34f6605101c278fd2b7c46)bt\_vcp\_vol\_rend\_unmute\_vol\_up()

| int bt\_vcp\_vol\_rend\_unmute\_vol\_up | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Turn the volume up and unmute the server.

Returns
:   0 if success, errno on failure.

## [◆ ](#gaf3c622f151a21d1dd617e97917c5ff5e)bt\_vcp\_vol\_rend\_vol\_down()

| int bt\_vcp\_vol\_rend\_vol\_down | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Turn the volume down by one step on the server.

Returns
:   0 if success, errno on failure.

## [◆ ](#ga6c10dd5a029b524994739f0b37a82c84)bt\_vcp\_vol\_rend\_vol\_up()

| int bt\_vcp\_vol\_rend\_vol\_up | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vcp.h](vcp_8h.md)>`

Turn the volume up by one step on the server.

Returns
:   0 if success, errno on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
