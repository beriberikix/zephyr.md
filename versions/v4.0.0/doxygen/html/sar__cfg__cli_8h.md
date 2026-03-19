---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sar__cfg__cli_8h.html
original_path: doxygen/html/sar__cfg__cli_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sar\_cfg\_cli.h File Reference

Bluetooth Mesh SAR Configuration Client Model APIs.
[More...](#details)

`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/sar_cfg.h](sar__cfg_8h_source.md)>`

[Go to the source code of this file.](sar__cfg__cli_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_sar\_cfg\_cli](structbt__mesh__sar__cfg__cli.md) |
|  | Mesh SAR Configuration Client Model Context. [More...](structbt__mesh__sar__cfg__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_SAR\_CFG\_CLI](group__bt__mesh__sar__cfg__cli.md#ga742d31e7175e472f1a096ffa6a5acdc5)(\_cli) |
|  | SAR Configuration Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_sar\_cfg\_cli\_transmitter\_get](group__bt__mesh__sar__cfg__cli.md#ga893ef5861708bec12f87b9f9cc64b9fc) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \*rsp) |
|  | Get the SAR Transmitter state of the target node. |
| int | [bt\_mesh\_sar\_cfg\_cli\_transmitter\_set](group__bt__mesh__sar__cfg__cli.md#ga32e2a580b24a41761911e88413e9664e) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \*set, struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \*rsp) |
|  | Set the SAR Transmitter state of the target node. |
| int | [bt\_mesh\_sar\_cfg\_cli\_receiver\_get](group__bt__mesh__sar__cfg__cli.md#ga444c99254ef2ccdd10dac08a94219d79) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \*rsp) |
|  | Get the SAR Receiver state of the target node. |
| int | [bt\_mesh\_sar\_cfg\_cli\_receiver\_set](group__bt__mesh__sar__cfg__cli.md#ga884025b2baf8559950ba6dc83e9ef486) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \*set, struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \*rsp) |
|  | Set the SAR Receiver state of the target node. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_sar\_cfg\_cli\_timeout\_get](group__bt__mesh__sar__cfg__cli.md#ga998846e5735676dc5f79b387d02630d4) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_sar\_cfg\_cli\_timeout\_set](group__bt__mesh__sar__cfg__cli.md#ga57d7c6a973b35f53689cbf8a065a538f) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

## Detailed Description

Bluetooth Mesh SAR Configuration Client Model APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [sar\_cfg\_cli.h](sar__cfg__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
