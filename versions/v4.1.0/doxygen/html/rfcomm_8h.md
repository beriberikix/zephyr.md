---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rfcomm_8h.html
original_path: doxygen/html/rfcomm_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rfcomm.h File Reference

Bluetooth RFCOMM handling.
[More...](#details)

`#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/l2cap.h](l2cap_8h_source.md)>`

[Go to the source code of this file.](rfcomm_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_rfcomm\_dlc\_ops](structbt__rfcomm__dlc__ops.md) |
|  | RFCOMM DLC operations structure. [More...](structbt__rfcomm__dlc__ops.md#details) |
| struct | [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) |
|  | RFCOMM DLC structure. [More...](structbt__rfcomm__dlc.md#details) |
| struct | [bt\_rfcomm\_server](structbt__rfcomm__server.md) |

| Macros | |
| --- | --- |
| #define | [BT\_RFCOMM\_HDR\_MAX\_SIZE](group__bt__rfcomm.md#ga8d7b15c80fc69a25b105aadf6f3a6a6d)   4 |
|  | RFCOMM Maximum Header Size. |
| #define | [BT\_RFCOMM\_FCS\_SIZE](group__bt__rfcomm.md#gaea26fe8eac8c5792a4cb78404dc4f7c1)   1 |
|  | RFCOMM FCS Size. |
| #define | [BT\_RFCOMM\_BUF\_SIZE](group__bt__rfcomm.md#gabb568d7f32dbd0720f203538e3aa345c)(mtu) |
|  | Helper to calculate needed buffer size for RFCOMM PDUs. |

| Typedefs | |
| --- | --- |
| typedef enum [bt\_rfcomm\_role](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2) | [bt\_rfcomm\_role\_t](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9) |
|  | Role of RFCOMM session and dlc. |

| Enumerations | |
| --- | --- |
| enum | {     [BT\_RFCOMM\_CHAN\_HFP\_HF](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4) = 1 , [BT\_RFCOMM\_CHAN\_HFP\_AG](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd) , [BT\_RFCOMM\_CHAN\_HSP\_AG](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b) , [BT\_RFCOMM\_CHAN\_HSP\_HS](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25) ,     [BT\_RFCOMM\_CHAN\_SPP](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495) , [BT\_RFCOMM\_CHAN\_DYNAMIC\_START](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302)   } |
| enum | [bt\_rfcomm\_role](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2) { [BT\_RFCOMM\_ROLE\_ACCEPTOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d) , [BT\_RFCOMM\_ROLE\_INITIATOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8) } |
|  | Role of RFCOMM session and dlc. [More...](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2) |

| Functions | |
| --- | --- |
| int | [bt\_rfcomm\_server\_register](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401) (struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \*server) |
|  | Register RFCOMM server. |
| int | [bt\_rfcomm\_dlc\_connect](group__bt__rfcomm.md#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7) (struct bt\_conn \*conn, struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Connect RFCOMM channel. |
| int | [bt\_rfcomm\_dlc\_send](group__bt__rfcomm.md#ga593841aef52027598977b7b2bbd0237d) (struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send data to RFCOMM. |
| int | [bt\_rfcomm\_dlc\_disconnect](group__bt__rfcomm.md#ga998328b021ec53f7e291ab76856ffa18) (struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc) |
|  | Disconnect RFCOMM dlc. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_rfcomm\_create\_pdu](group__bt__rfcomm.md#gaed05e67dc975d94e1209372d5817077a) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool) |
|  | Allocate the buffer from pool after reserving head room for RFCOMM, L2CAP and ACL headers. |

## Detailed Description

Bluetooth RFCOMM handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [rfcomm.h](rfcomm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
