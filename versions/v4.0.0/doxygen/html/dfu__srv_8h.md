---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dfu__srv_8h.html
original_path: doxygen/html/dfu__srv_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfu\_srv.h File Reference

`#include <[zephyr/bluetooth/mesh/dfu.h](dfu_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/blob_srv.h](blob__srv_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/access.h](access_8h_source.md)>`

[Go to the source code of this file.](dfu__srv_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_dfu\_srv\_cb](structbt__mesh__dfu__srv__cb.md) |
|  | Firmware Update Server event callbacks. [More...](structbt__mesh__dfu__srv__cb.md#details) |
| struct | [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) |
|  | Firmware Update Server instance. [More...](structbt__mesh__dfu__srv.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_DFU\_SRV\_INIT](group__bt__mesh__dfu__srv.md#ga8467cd5241dfdcd7add718bbaae6fa60)(\_handlers, \_imgs, \_img\_count) |
|  | Initialization parameters for [Firmware Update Server model](group__bt__mesh__dfu__srv.md "Firmware Update Server model"). |
| #define | [BT\_MESH\_MODEL\_DFU\_SRV](group__bt__mesh__dfu__srv.md#gafdf78cc0f99668d38df4f29138392632)(\_srv) |
|  | Firmware Update Server model entry. |

| Functions | |
| --- | --- |
| void | [bt\_mesh\_dfu\_srv\_verified](group__bt__mesh__dfu__srv.md#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Accept the received DFU transfer. |
| void | [bt\_mesh\_dfu\_srv\_rejected](group__bt__mesh__dfu__srv.md#ga77142a1f3cfe2ff1d53332114f977b38) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Reject the received DFU transfer. |
| void | [bt\_mesh\_dfu\_srv\_cancel](group__bt__mesh__dfu__srv.md#gaf5a00dd89faf52cd7797c54c572e1211) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Cancel the ongoing DFU transfer. |
| void | [bt\_mesh\_dfu\_srv\_applied](group__bt__mesh__dfu__srv.md#ga45aef92fe1de4c45ccb5369c1f5222ee) (struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Confirm that the received DFU transfer was applied. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_dfu\_srv\_is\_busy](group__bt__mesh__dfu__srv.md#ga94107fb1ca9207fc6918eae1fb1b3755) (const struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Check if the Firmware Update Server is busy processing a transfer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_dfu\_srv\_progress](group__bt__mesh__dfu__srv.md#ga9f125ace97a40f060e0d8c59fd49f514) (const struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv) |
|  | Get the progress of the current DFU procedure, in percent. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfu\_srv.h](dfu__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
