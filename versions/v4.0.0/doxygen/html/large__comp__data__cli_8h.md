---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/large__comp__data__cli_8h.html
original_path: doxygen/html/large__comp__data__cli_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

large\_comp\_data\_cli.h File Reference

`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`

[Go to the source code of this file.](large__comp__data__cli_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) |
|  | Large Composition Data response. [More...](structbt__mesh__large__comp__data__rsp.md#details) |
| struct | [bt\_mesh\_large\_comp\_data\_cli\_cb](structbt__mesh__large__comp__data__cli__cb.md) |
|  | Large Composition Data Status messages callbacks. [More...](structbt__mesh__large__comp__data__cli__cb.md#details) |
| struct | [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md) |
|  | Large Composition Data Client model context. [More...](structbt__mesh__large__comp__data__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_LARGE\_COMP\_DATA\_CLI](group__bt__mesh__large__comp__data__cli.md#ga5860da397d1cd830e8010946c5b32f1e)(cli\_data) |
|  | Large Composition Data Client model Composition Data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_large\_comp\_data\_get](group__bt__mesh__large__comp__data__cli.md#gaf505ee14246746fc245a34328443d1c6) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp) |
|  | Send Large Composition Data Get message. |
| int | [bt\_mesh\_models\_metadata\_get](group__bt__mesh__large__comp__data__cli.md#ga4073eb48c43460804705d80ac0919864) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp) |
|  | Send Models Metadata Get message. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [large\_comp\_data\_cli.h](large__comp__data__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
