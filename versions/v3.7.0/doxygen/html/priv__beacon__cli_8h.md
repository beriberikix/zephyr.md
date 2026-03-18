---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/priv__beacon__cli_8h.html
original_path: doxygen/html/priv__beacon__cli_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

priv\_beacon\_cli.h File Reference

`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`

[Go to the source code of this file.](priv__beacon__cli_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) |
|  | Private Beacon. [More...](structbt__mesh__priv__beacon.md#details) |
| struct | [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) |
|  | Private Node Identity. [More...](structbt__mesh__priv__node__id.md#details) |
| struct | [bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md) |
|  | Private Beacon Client Status messages callbacks. [More...](structbt__mesh__priv__beacon__cli__cb.md#details) |
| struct | [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) |
|  | Mesh Private Beacon Client model. [More...](structbt__mesh__priv__beacon__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_PRIV\_BEACON\_CLI](group__bt__mesh__priv__beacon__cli.md#ga65008412f2fc89aa9f71c067ad3fe264)(cli\_data) |
|  | Private Beacon Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_priv\_beacon\_cli\_set](group__bt__mesh__priv__beacon__cli.md#ga8a535d31954d8871fed557808b6abc71) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*val, struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*rsp) |
|  | Set the target's Private Beacon state. |
| int | [bt\_mesh\_priv\_beacon\_cli\_get](group__bt__mesh__priv__beacon__cli.md#ga76d797a76d8f8fda31feacce840a6f9e) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*val) |
|  | Get the target's Private Beacon state. |
| int | [bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_set](group__bt__mesh__priv__beacon__cli.md#ga389626a517c1bb9cae31501663725483) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp) |
|  | Set the target's Private GATT Proxy state. |
| int | [bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_get](group__bt__mesh__priv__beacon__cli.md#ga838880ae8391b33d0481fba069ea921b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val) |
|  | Get the target's Private GATT Proxy state. |
| int | [bt\_mesh\_priv\_beacon\_cli\_node\_id\_set](group__bt__mesh__priv__beacon__cli.md#ga2a581e49b8812bd78604fc829bd1d79a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*val, struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*rsp) |
|  | Set the target's Private Node Identity state. |
| int | [bt\_mesh\_priv\_beacon\_cli\_node\_id\_get](group__bt__mesh__priv__beacon__cli.md#gadd6fc3321cd536771921566bbc650396) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*val) |
|  | Get the target's Private Node Identity state. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [priv\_beacon\_cli.h](priv__beacon__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
