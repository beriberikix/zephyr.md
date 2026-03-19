---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/op__agg__cli_8h.html
original_path: doxygen/html/op__agg__cli_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

op\_agg\_cli.h File Reference

`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`

[Go to the source code of this file.](op__agg__cli_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_OP\_AGG\_CLI](group__bt__mesh__op__agg__cli.md#ga0a8dec4b4f53d1ec95db1efc4ab22f69) |
|  | Opcodes Aggregator Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_op\_agg\_cli\_seq\_start](group__bt__mesh__op__agg__cli.md#gac1905d778362faf442a9538adca34a8c) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr) |
|  | Configure Opcodes Aggregator context. |
| int | [bt\_mesh\_op\_agg\_cli\_seq\_send](group__bt__mesh__op__agg__cli.md#gab151f44fcb5d3f3f0f1dafaf90f05c18) (void) |
|  | Opcodes Aggregator message send. |
| void | [bt\_mesh\_op\_agg\_cli\_seq\_abort](group__bt__mesh__op__agg__cli.md#ga00b5e695503ba169a1b5ec626413b322) (void) |
|  | Abort Opcodes Aggregator context. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_op\_agg\_cli\_seq\_is\_started](group__bt__mesh__op__agg__cli.md#gadbc347b2dc3d78a4ac71d424f0623b6f) (void) |
|  | Check if Opcodes Aggregator Sequence context is started. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bt\_mesh\_op\_agg\_cli\_seq\_tailroom](group__bt__mesh__op__agg__cli.md#ga4269bc6118371e2af0967841b18a02dd) (void) |
|  | Get Opcodes Aggregator context tailroom. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_op\_agg\_cli\_timeout\_get](group__bt__mesh__op__agg__cli.md#ga83e44b062babcf0bdb343455e3eddf5f) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_op\_agg\_cli\_timeout\_set](group__bt__mesh__op__agg__cli.md#gaf70cebae8dbd6eb4ef6402585a90e0d5) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [op\_agg\_cli.h](op__agg__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
