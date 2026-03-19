---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/health__srv_8h.html
original_path: doxygen/html/health__srv_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

health\_srv.h File Reference

Health Server Model APIs.
[More...](#details)

`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`  
`#include <[zephyr/bluetooth/byteorder.h](bluetooth_2byteorder_8h_source.md)>`

[Go to the source code of this file.](health__srv_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md) |
|  | Callback function for the Health Server model. [More...](structbt__mesh__health__srv__cb.md#details) |
| struct | [bt\_mesh\_health\_srv](structbt__mesh__health__srv.md) |
|  | Mesh Health Server Model Context. [More...](structbt__mesh__health__srv.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_HEALTH\_PUB\_DEFINE](group__bt__mesh__health__srv.md#ga35c500e915092ec365862b11e76f92ad)(\_name, \_max\_faults) |
|  | A helper to define a health publication context. |
| #define | [BT\_MESH\_MODEL\_HEALTH\_SRV](group__bt__mesh__health__srv.md#gafcab7a9c9264c52f42b5409ccad1c931)(srv, pub, ...) |
|  | Define a new health server model. |
| #define | [BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA\_ID](group__bt__mesh__health__srv.md#ga240e4632cdf7c425d4beec3c6a290306)   0x0000 |
|  | Health Test Information Metadata ID. |
| #define | [BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA](group__bt__mesh__health__srv.md#ga37a52318699187a92de82d45dccf325d)(tests) |
| #define | [BT\_MESH\_HEALTH\_TEST\_INFO](group__bt__mesh__health__srv.md#ga29ca643e811a2c4f03eca7fed8d1cf4d)(cid, tests...) |
|  | Define a Health Test Info Metadata array. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_health\_srv\_fault\_update](group__bt__mesh__health__srv.md#gad04789eb167b61d5ff19827c560ceb6e) (const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*elem) |
|  | Notify the stack that the fault array state of the given element has changed. |

## Detailed Description

Health Server Model APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [health\_srv.h](health__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
