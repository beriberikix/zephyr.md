---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/vcp_8h.html
original_path: doxygen/html/vcp_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vcp.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/aics.h](aics_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/vocs.h](vocs_8h_source.md)>`

[Go to the source code of this file.](vcp_8h_source.md)

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
| #define | [BT\_VCP\_VOL\_REND\_VOCS\_CNT](group__bt__gatt__vcp.md#gae7195f4556ad2442bc45d8d43cdeedd0)   0 |
| #define | [BT\_VCP\_VOL\_REND\_AICS\_CNT](group__bt__gatt__vcp.md#ga571d7ff5a6a507fcd7cbdfa32a04643b)   0 |
| #define | [BT\_VCP\_ERR\_INVALID\_COUNTER](group__bt__gatt__vcp.md#gabb8bdfde60f1cbb31bab41fd61b3384b)   0x80 |
|  | Volume Control Service Error codes. |
| #define | [BT\_VCP\_ERR\_OP\_NOT\_SUPPORTED](group__bt__gatt__vcp.md#gad979c43e4d84f52009d9931fb74628e6)   0x81 |
| #define | [BT\_VCP\_STATE\_UNMUTED](group__bt__gatt__vcp.md#ga4660f938a16113f715dd8aec3ed3baf6)   0x00 |
|  | Volume Control Service Mute Values. |
| #define | [BT\_VCP\_STATE\_MUTED](group__bt__gatt__vcp.md#ga3d6ffdfb9e0d8d58073f4a130a8020b0)   0x01 |

| Functions | |
| --- | --- |
| int | [bt\_vcp\_vol\_rend\_included\_get](group__bt__gatt__vcp.md#ga1761d6618c48983e034cee5574c9c34f) (struct [bt\_vcp\_included](structbt__vcp__included.md) \*included) |
|  | Get Volume Control Service included services. |
| int | [bt\_vcp\_vol\_rend\_register](group__bt__gatt__vcp.md#ga752d8ff54a4b8c8c854a9c693617e64d) (struct [bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md) \*param) |
|  | Register the Volume Control Service. |
| int | [bt\_vcp\_vol\_rend\_set\_step](group__bt__gatt__vcp.md#ga56e0f99d2688fb6f9e0e4d9103de706c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume\_step) |
|  | Set the Volume Control Service volume step size. |
| int | [bt\_vcp\_vol\_rend\_get\_state](group__bt__gatt__vcp.md#ga9d1ac028abc88549ea18b6a0c585c781) (void) |
|  | Get the Volume Control Service volume state. |
| int | [bt\_vcp\_vol\_rend\_get\_flags](group__bt__gatt__vcp.md#ga1e6c9cfa0d012a4b701c99d8e6b5985d) (void) |
|  | Get the Volume Control Service flags. |
| int | [bt\_vcp\_vol\_rend\_vol\_down](group__bt__gatt__vcp.md#gaf3c622f151a21d1dd617e97917c5ff5e) (void) |
|  | Turn the volume down by one step on the server. |
| int | [bt\_vcp\_vol\_rend\_vol\_up](group__bt__gatt__vcp.md#ga6c10dd5a029b524994739f0b37a82c84) (void) |
|  | Turn the volume up by one step on the server. |
| int | [bt\_vcp\_vol\_rend\_unmute\_vol\_down](group__bt__gatt__vcp.md#ga3e6236a8679f95ba512181284a05923d) (void) |
|  | Turn the volume down and unmute the server. |
| int | [bt\_vcp\_vol\_rend\_unmute\_vol\_up](group__bt__gatt__vcp.md#gadf77729fee34f6605101c278fd2b7c46) (void) |
|  | Turn the volume up and unmute the server. |
| int | [bt\_vcp\_vol\_rend\_set\_vol](group__bt__gatt__vcp.md#ga61279baeba11152625cd3a87c5d973c9) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume) |
|  | Set the volume on the server. |
| int | [bt\_vcp\_vol\_rend\_unmute](group__bt__gatt__vcp.md#ga303d4b6b77987ab41cb1753ef861dd6c) (void) |
|  | Unmute the server. |
| int | [bt\_vcp\_vol\_rend\_mute](group__bt__gatt__vcp.md#ga0c6d0b6b015f069a9adc1332a32c79f9) (void) |
|  | Mute the server. |
| int | [bt\_vcp\_vol\_ctlr\_cb\_register](group__bt__gatt__vcp.md#ga7861d0c3426870c015106e8e170004a3) (struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) \*cb) |
|  | Registers the callbacks used by the Volume Controller. |
| int | [bt\_vcp\_vol\_ctlr\_cb\_unregister](group__bt__gatt__vcp.md#gae69e4730df4341bbb9bbbba1bea14005) (struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) \*cb) |
|  | Unregisters the callbacks used by the Volume Controller. |
| int | [bt\_vcp\_vol\_ctlr\_discover](group__bt__gatt__vcp.md#gac18d43a0785155c1131249f95554f2de) (struct bt\_conn \*conn, struct bt\_vcp\_vol\_ctlr \*\*vol\_ctlr) |
|  | Discover Volume Control Service and included services. |
| struct bt\_vcp\_vol\_ctlr \* | [bt\_vcp\_vol\_ctlr\_get\_by\_conn](group__bt__gatt__vcp.md#ga0c8faa95cc36950c70ff572c931eedee) (const struct bt\_conn \*conn) |
|  | Get the volume controller from a connection pointer. |
| int | [bt\_vcp\_vol\_ctlr\_conn\_get](group__bt__gatt__vcp.md#gab287197243191e3dbf162c6d16b6d726) (const struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, struct bt\_conn \*\*conn) |
|  | Get the connection pointer of a client instance. |
| int | [bt\_vcp\_vol\_ctlr\_included\_get](group__bt__gatt__vcp.md#gaaa748c49e103ff161f67df9663ea6330) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, struct [bt\_vcp\_included](structbt__vcp__included.md) \*included) |
|  | Get Volume Control Service included services. |
| int | [bt\_vcp\_vol\_ctlr\_read\_state](group__bt__gatt__vcp.md#ga68cab2f59c63542b6a7da33d555da0ab) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Read the volume state of a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_read\_flags](group__bt__gatt__vcp.md#gaefc226a5abb6bb1540d4b44ac4ddc236) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Read the volume flags of a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_vol\_down](group__bt__gatt__vcp.md#ga03e073e29920f4a530d2f8851b4b8df4) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Turn the volume down one step on a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_vol\_up](group__bt__gatt__vcp.md#ga908eb20727e1d68ed569badfd13ff896) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Turn the volume up one step on a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_unmute\_vol\_down](group__bt__gatt__vcp.md#ga20348b220988c700cabf356f7165d4d6) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Turn the volume down one step and unmute on a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_unmute\_vol\_up](group__bt__gatt__vcp.md#ga2defdeee7486eee22a3416db8aa7c251) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Turn the volume up one step and unmute on a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_set\_vol](group__bt__gatt__vcp.md#gaaa5b5cd9a11c0e1fcdabce690ba20616) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume) |
|  | Set the absolute volume on a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_unmute](group__bt__gatt__vcp.md#ga4e95c3fb071cb94fbe75f88e96d34b36) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Unmute a remote Volume Renderer. |
| int | [bt\_vcp\_vol\_ctlr\_mute](group__bt__gatt__vcp.md#ga106b7f826adec665b4f0ac3d5e82b867) (struct bt\_vcp\_vol\_ctlr \*vol\_ctlr) |
|  | Mute a remote Volume Renderer. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [vcp.h](vcp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
