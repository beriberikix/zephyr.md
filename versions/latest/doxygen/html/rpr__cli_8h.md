---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rpr__cli_8h.html
original_path: doxygen/html/rpr__cli_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpr\_cli.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/access.h](access_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/rpr.h](rpr_8h_source.md)>`

[Go to the source code of this file.](rpr__cli_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) |
|  | Scan status response. [More...](structbt__mesh__rpr__scan__status.md#details) |
| struct | [bt\_mesh\_rpr\_caps](structbt__mesh__rpr__caps.md) |
|  | Remote Provisioning Server scanning capabilities. [More...](structbt__mesh__rpr__caps.md#details) |
| struct | [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) |
|  | Remote Provisioning Client model instance. [More...](structbt__mesh__rpr__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_RPR\_SCAN\_MAX\_DEVS\_ANY](group__bt__mesh__rpr__cli.md#gafa00eb1bff764a4ab723bb978b459297)   0 |
|  | Special value for the `max_devs` parameter of [bt\_mesh\_rpr\_scan\_start](group__bt__mesh__rpr__cli.md#gaf404922f2340442490f1ab29191f43e3 "bt_mesh_rpr_scan_start"). |
| #define | [BT\_MESH\_MODEL\_RPR\_CLI](group__bt__mesh__rpr__cli.md#ga83d18bb8d1108db9f7e54cd2cad32a99)(\_cli) |
|  | Remote Provisioning Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_rpr\_scan\_caps\_get](group__bt__mesh__rpr__cli.md#ga1cfef51b2d6389fb4b125cba4d21d739) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, struct [bt\_mesh\_rpr\_caps](structbt__mesh__rpr__caps.md) \*caps) |
|  | Get scanning capabilities of Remote Provisioning Server. |
| int | [bt\_mesh\_rpr\_scan\_get](group__bt__mesh__rpr__cli.md#ga03602b651a5bf1c88dac810e272ea142) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \*status) |
|  | Get current scanning state of Remote Provisioning Server. |
| int | [bt\_mesh\_rpr\_scan\_start](group__bt__mesh__rpr__cli.md#gaf404922f2340442490f1ab29191f43e3) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) timeout, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_devs, struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \*status) |
|  | Start scanning for unprovisioned devices. |
| int | [bt\_mesh\_rpr\_scan\_start\_ext](group__bt__mesh__rpr__cli.md#ga934104e6ee33ba8c228fde4c68e752e1) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) timeout, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ad\_types, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ad\_count) |
|  | Start extended scanning for unprovisioned devices. |
| int | [bt\_mesh\_rpr\_scan\_stop](group__bt__mesh__rpr__cli.md#ga007aa9b409d1370ed04c45efccdf0408) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \*status) |
|  | Stop any ongoing scanning on the Remote Provisioning Server. |
| int | [bt\_mesh\_rpr\_link\_get](group__bt__mesh__rpr__cli.md#ga36de5bfca8ba9b03a99625fbc1734839) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, struct [bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md) \*rsp) |
|  | Get the current link status of the Remote Provisioning Server. |
| int | [bt\_mesh\_rpr\_link\_close](group__bt__mesh__rpr__cli.md#gaa240b465a1ed5796b190d241e484d467) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, struct [bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md) \*rsp) |
|  | Close any open link on the Remote Provisioning Server. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_rpr\_cli\_timeout\_get](group__bt__mesh__rpr__cli.md#ga93aca19586795801eefa04ffc4635533) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_rpr\_cli\_timeout\_set](group__bt__mesh__rpr__cli.md#ga5ad2a2f6f0b9a3f27ef8174cd15b8818) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [rpr\_cli.h](rpr__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
