---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/od__priv__proxy__cli_8h.html
original_path: doxygen/html/od__priv__proxy__cli_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

od\_priv\_proxy\_cli.h File Reference

`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`

[Go to the source code of this file.](od__priv__proxy__cli_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_od\_priv\_proxy\_cli](structbt__mesh__od__priv__proxy__cli.md) |
|  | On-Demand Private Proxy Client Model Context. [More...](structbt__mesh__od__priv__proxy__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_OD\_PRIV\_PROXY\_CLI](group__bt__mesh__od__priv__proxy__cli.md#ga037391820efab2b953805f6373431ca9)(cli\_data) |
|  | On-Demand Private Proxy Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_od\_priv\_proxy\_cli\_get](group__bt__mesh__od__priv__proxy__cli.md#ga11357595b2d837f6172a2ec98d1e9973) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val\_rsp) |
|  | Get the target's On-Demand Private GATT Proxy state. |
| int | [bt\_mesh\_od\_priv\_proxy\_cli\_set](group__bt__mesh__od__priv__proxy__cli.md#ga9b239c221f8c74108e2a7e5276122e1f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val\_rsp) |
|  | Set the target's On-Demand Private GATT Proxy state. |
| void | [bt\_mesh\_od\_priv\_proxy\_cli\_timeout\_set](group__bt__mesh__od__priv__proxy__cli.md#gad613c78e708f0df5aabda9e16fae6a2c) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [od\_priv\_proxy\_cli.h](od__priv__proxy__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
