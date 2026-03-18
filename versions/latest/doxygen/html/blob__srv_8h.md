---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/blob__srv_8h.html
original_path: doxygen/html/blob__srv_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

blob\_srv.h File Reference

`#include <[zephyr/bluetooth/mesh/access.h](access_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/blob.h](blob_8h_source.md)>`

[Go to the source code of this file.](blob__srv_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md) |
|  | BLOB Transfer Server model event handlers. [More...](structbt__mesh__blob__srv__cb.md#details) |
| struct | [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) |
|  | BLOB Transfer Server instance. [More...](structbt__mesh__blob__srv.md#details) |
| struct | [bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_BLOB\_BLOCKS\_MAX](group__bt__mesh__blob__srv.md#gaae3dfbf15f33739bc0a42c924de99cba)   1 |
|  | Max number of blocks in a single transfer. |
| #define | [BT\_MESH\_MODEL\_BLOB\_SRV](group__bt__mesh__blob__srv.md#gad9db3253c13d50cfb6c89dff881dbfe9)(\_srv) |
|  | BLOB Transfer Server model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_blob\_srv\_recv](group__bt__mesh__blob__srv.md#ga5d35f13eeb6f7a1fb252e8fb905e9cb3) (struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout\_base) |
|  | Prepare BLOB Transfer Server for an incoming transfer. |
| int | [bt\_mesh\_blob\_srv\_cancel](group__bt__mesh__blob__srv.md#gae8739e96f2157f588072e91b51891835) (struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv) |
|  | Cancel the current BLOB transfer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_blob\_srv\_is\_busy](group__bt__mesh__blob__srv.md#gaa7a253c9a577eaa1307bc0e6b93a3d66) (const struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv) |
|  | Get the current state of the BLOB Transfer Server. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_blob\_srv\_progress](group__bt__mesh__blob__srv.md#ga674b59ff721575539818ef74e8d1b91c) (const struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv) |
|  | Get the current progress of the active transfer in percent. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [blob\_srv.h](blob__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
