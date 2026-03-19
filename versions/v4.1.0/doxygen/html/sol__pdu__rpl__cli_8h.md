---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sol__pdu__rpl__cli_8h.html
original_path: doxygen/html/sol__pdu__rpl__cli_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sol\_pdu\_rpl\_cli.h File Reference

`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`

[Go to the source code of this file.](sol__pdu__rpl__cli_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_sol\_pdu\_rpl\_cli](structbt__mesh__sol__pdu__rpl__cli.md) |
|  | Solicitation PDU RPL Client Model Context. [More...](structbt__mesh__sol__pdu__rpl__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_CLI](group__bt__mesh__sol__pdu__rpl__cli.md#gac5969e20994b07977484391ac2d7bacb)(cli\_data) |
|  | Solicitation PDU RPL Client model composition data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_sol\_pdu\_rpl\_clear](group__bt__mesh__sol__pdu__rpl__cli.md#gae7e8a0e364c6695a467a64cd89627d81) (struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) range\_start, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) range\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*start\_rsp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*len\_rsp) |
|  | Remove entries from Solicitation PDU RPL of addresses in given range. |
| int | [bt\_mesh\_sol\_pdu\_rpl\_clear\_unack](group__bt__mesh__sol__pdu__rpl__cli.md#ga68fb70fbfb87e76ef6fdb5ac8a1a9506) (struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) range\_start, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) range\_len) |
|  | Remove entries from Solicitation PDU RPL of addresses in given range (unacked). |
| void | [bt\_mesh\_sol\_pdu\_rpl\_cli\_timeout\_set](group__bt__mesh__sol__pdu__rpl__cli.md#gadabdbd95f39a498307e3ca9e50acfeb9) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [sol\_pdu\_rpl\_cli.h](sol__pdu__rpl__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
