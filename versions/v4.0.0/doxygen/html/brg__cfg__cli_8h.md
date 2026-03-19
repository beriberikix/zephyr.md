---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/brg__cfg__cli_8h.html
original_path: doxygen/html/brg__cfg__cli_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

brg\_cfg\_cli.h File Reference

`#include <[zephyr/bluetooth/mesh/brg_cfg.h](brg__cfg_8h_source.md)>`

[Go to the source code of this file.](brg__cfg__cli_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_brg\_cfg\_cli\_cb](structbt__mesh__brg__cfg__cli__cb.md) |
|  | Mesh Bridge Configuration Client Status messages callback. [More...](structbt__mesh__brg__cfg__cli__cb.md#details) |
| struct | [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) |
|  | Bridge Configuration Client Model Context. [More...](structbt__mesh__brg__cfg__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_BRG\_CFG\_CLI](group__bt__mesh__brg__cfg__cli.md#ga4cf994be4732bd99b2c8a4642f670efe)(\_cli) |
|  | Bridge Configuration Client model Composition Data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_brg\_cfg\_cli\_get](group__bt__mesh__brg__cfg__cli.md#ga6a4507190e425013a9d21ea0a1be1b5c) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) \*status) |
|  | Sends a Subnet Bridge Get message to the given destination address. |
| int | [bt\_mesh\_brg\_cfg\_cli\_set](group__bt__mesh__brg__cfg__cli.md#ga6643d4d043af4b0cb30470a5c9a46f38) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) val, enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) \*status) |
|  | Sends a Subnet Bridge Set message to the given destination address with the given parameters. |
| int | [bt\_mesh\_brg\_cfg\_cli\_table\_size\_get](group__bt__mesh__brg__cfg__cli.md#ga99951987bd6787e3e1348d8e51e64fe5) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*size) |
|  | Sends a Bridging Table Size Get message to the given destination address with the given parameters. |
| int | [bt\_mesh\_brg\_cfg\_cli\_table\_add](group__bt__mesh__brg__cfg__cli.md#ga8f055e8ee384e8ea4887a56720959b26) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md) \*entry, struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \*rsp) |
|  | Sends a Bridging Table Add message to the given destination address with the given parameters. |
| int | [bt\_mesh\_brg\_cfg\_cli\_table\_remove](group__bt__mesh__brg__cfg__cli.md#gabdb919dcf177b8d5c8a28b057469bf18) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx1, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr1, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr2, struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \*rsp) |
|  | Sends a Bridging Table Remove message to the given destination address with the given parameters. |
| int | [bt\_mesh\_brg\_cfg\_cli\_subnets\_get](group__bt__mesh__brg__cfg__cli.md#ga04bb227d14d4f478e4f32a8ca87d2c38) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md) filter\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_idx, struct [bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md) \*rsp) |
|  | Sends a Bridged Subnets Get message to the given destination address with the given parameters. |
| int | [bt\_mesh\_brg\_cfg\_cli\_table\_get](group__bt__mesh__brg__cfg__cli.md#gacd3811be7b87d2d9187aed6c50945b85) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx1, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_idx, struct [bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md) \*rsp) |
|  | Sends a Bridging Table Get message to the given destination address with the given parameters. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_brg\_cfg\_cli\_timeout\_get](group__bt__mesh__brg__cfg__cli.md#ga252994dd3119387703af45c0932ef253) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_brg\_cfg\_cli\_timeout\_set](group__bt__mesh__brg__cfg__cli.md#gad30102a29983545ec79f178b1390ce74) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [brg\_cfg\_cli.h](brg__cfg__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
