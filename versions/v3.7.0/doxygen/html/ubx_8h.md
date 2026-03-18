---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ubx_8h.html
original_path: doxygen/html/ubx_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ubx.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/modem/pipe.h](pipe_8h_source.md)>`

[Go to the source code of this file.](ubx_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ubx\_frame](structubx__frame.md) |
| struct | [modem\_ubx\_script](structmodem__ubx__script.md) |
| struct | [modem\_ubx](structmodem__ubx.md) |
| struct | [modem\_ubx\_config](structmodem__ubx__config.md) |

| Macros | |
| --- | --- |
| #define | [UBX\_FRM\_HEADER\_SZ](group__modem__ubx.md#ga703255ca4aee83952007115eb74aba50)   6 |
| #define | [UBX\_FRM\_FOOTER\_SZ](group__modem__ubx.md#ga36bcc1dda3daf89377b9cde87f642ecb)   2 |
| #define | [UBX\_FRM\_SZ\_WITHOUT\_PAYLOAD](group__modem__ubx.md#ga76c616ef547947b5aed71cf516db69e9)   ([UBX\_FRM\_HEADER\_SZ](group__modem__ubx.md#ga703255ca4aee83952007115eb74aba50) + [UBX\_FRM\_FOOTER\_SZ](group__modem__ubx.md#ga36bcc1dda3daf89377b9cde87f642ecb)) |
| #define | [UBX\_FRM\_SZ](group__modem__ubx.md#ga658ec1be18701eeb8464e36690719ddf)(payload\_size) |
| #define | [UBX\_PREAMBLE\_SYNC\_CHAR\_1](group__modem__ubx.md#ga1693f3584605a0197076cba71c79b0df)   0xB5 |
| #define | [UBX\_PREAMBLE\_SYNC\_CHAR\_2](group__modem__ubx.md#gad8d6229db563db619d4f0a9f225fb640)   0x62 |
| #define | [UBX\_FRM\_PREAMBLE\_SYNC\_CHAR\_1\_IDX](group__modem__ubx.md#ga56b16b79385bffdb4a46f1c09b80eb73)   0 |
| #define | [UBX\_FRM\_PREAMBLE\_SYNC\_CHAR\_2\_IDX](group__modem__ubx.md#gaf72f72cd97e07540452342fdd1868dff)   1 |
| #define | [UBX\_FRM\_MSG\_CLASS\_IDX](group__modem__ubx.md#ga258a47c93ef596c2807aaf0e7b810cd0)   2 |
| #define | [UBX\_FRM\_MSG\_ID\_IDX](group__modem__ubx.md#ga9c2428d2a7867b94638aa2108e23ec55)   3 |
| #define | [UBX\_FRM\_PAYLOAD\_SZ\_L\_IDX](group__modem__ubx.md#ga500d87a31bc1a34cb50997b0d754bf91)   4 |
| #define | [UBX\_FRM\_PAYLOAD\_SZ\_H\_IDX](group__modem__ubx.md#gaab0afee791670adfa80410bad0147482)   5 |
| #define | [UBX\_FRM\_PAYLOAD\_IDX](group__modem__ubx.md#ga0fbb8dfbf14547637c9f5dd4ed9e9762)   6 |
| #define | [UBX\_FRM\_CHECKSUM\_START\_IDX](group__modem__ubx.md#gac5f7efa1d5c4bc4b7d9e48a41ad412a2)   2 |
| #define | [UBX\_FRM\_CHECKSUM\_STOP\_IDX](group__modem__ubx.md#gab29f0a6e9d33f39c57b598a75695146f)(frame\_len) |
| #define | [UBX\_PAYLOAD\_SZ\_MAX](group__modem__ubx.md#ga9c66cd27732153c56d0872339bc3deae)   256 |
| #define | [UBX\_FRM\_SZ\_MAX](group__modem__ubx.md#gae3aeb2a4570fce67fda95961335ee30c)   [UBX\_FRM\_SZ](group__modem__ubx.md#ga658ec1be18701eeb8464e36690719ddf)([UBX\_PAYLOAD\_SZ\_MAX](group__modem__ubx.md#ga9c66cd27732153c56d0872339bc3deae)) |

| Functions | |
| --- | --- |
| int | [modem\_ubx\_attach](group__modem__ubx.md#ga4e459f955e34c9059702c3d7f9794948) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct modem\_pipe \*pipe) |
|  | Attach pipe to Modem Ubx. |
| void | [modem\_ubx\_release](group__modem__ubx.md#ga68210f4afd5880c532d82fd0bac1d933) (struct [modem\_ubx](structmodem__ubx.md) \*ubx) |
|  | Release pipe from Modem Ubx instance. |
| int | [modem\_ubx\_init](group__modem__ubx.md#gaf49363fb4decb4656566b508a061212f) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [modem\_ubx\_config](structmodem__ubx__config.md) \*config) |
|  | Initialize Modem Ubx instance. |
| int | [modem\_ubx\_run\_script](group__modem__ubx.md#ga25319c784f0293c25c38b494cf9d2a53) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [modem\_ubx\_script](structmodem__ubx__script.md) \*script) |
|  | Writes the ubx frame in script.request and reads back its response (if available). |
| int | [modem\_ubx\_create\_frame](group__modem__ubx.md#ga5d6b36f127836c5b06cde37f098c8775) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ubx\_frame](structubx__frame.md), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ubx\_frame\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) msg\_cls, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) msg\_id, const void \*payload, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) payload\_size) |
|  | Initialize ubx frame. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ubx.h](ubx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
