---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/rfcomm_8h.html
original_path: doxygen/html/rfcomm_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rfcomm.h File Reference

Bluetooth RFCOMM handling.
[More...](#details)

`#include <[zephyr/bluetooth/buf.h](buf_8h_source.md)>`  
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
| struct | [bt\_rfcomm\_rpn](structbt__rfcomm__rpn.md) |
|  | RFCOMM Remote Port Negotiation (RPN) structure. [More...](structbt__rfcomm__rpn.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_RFCOMM\_HDR\_MAX\_SIZE](group__bt__rfcomm.md#ga8d7b15c80fc69a25b105aadf6f3a6a6d)   4 |
|  | RFCOMM Maximum Header Size. |
| #define | [BT\_RFCOMM\_FCS\_SIZE](group__bt__rfcomm.md#gaea26fe8eac8c5792a4cb78404dc4f7c1)   1 |
|  | RFCOMM FCS Size. |
| #define | [BT\_RFCOMM\_BUF\_SIZE](group__bt__rfcomm.md#gabb568d7f32dbd0720f203538e3aa345c)(mtu) |
|  | Helper to calculate needed buffer size for RFCOMM PDUs. |
| #define | [BT\_RFCOMM\_SET\_LINE\_SETTINGS](group__bt__rfcomm.md#gacbb625b129afb33fceafe5ddf61c839a)(data, stop, parity) |
|  | Combine data bits, stop bits and parity into a single line settings byte. |
| #define | [BT\_RFCOMM\_RPN\_FLOW\_NONE](group__bt__rfcomm.md#gaef902e774d1a6279a117968a32cc5878)   0x00 |
| #define | [BT\_RFCOMM\_RPN\_XON\_CHAR](group__bt__rfcomm.md#ga90ab80687e32da0f8164292cd63b0623)   0x11 |
| #define | [BT\_RFCOMM\_RPN\_XOFF\_CHAR](group__bt__rfcomm.md#gacdca9e597689b3de20b1df3616ad523c)   0x13 |
| #define | [BT\_RFCOMM\_RPN\_PARAM\_MASK\_ALL](group__bt__rfcomm.md#ga71099379ed90d3d6ce9d4c1eed3be827)   0x3f7f |

| Typedefs | |
| --- | --- |
| typedef enum [bt\_rfcomm\_role](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2) | [bt\_rfcomm\_role\_t](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9) |
|  | Role of RFCOMM session and dlc. |

| Enumerations | |
| --- | --- |
| enum | {     [BT\_RFCOMM\_CHAN\_HFP\_HF](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4) = 1 , [BT\_RFCOMM\_CHAN\_HFP\_AG](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd) , [BT\_RFCOMM\_CHAN\_HSP\_AG](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b) , [BT\_RFCOMM\_CHAN\_HSP\_HS](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25) ,     [BT\_RFCOMM\_CHAN\_SPP](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495) , [BT\_RFCOMM\_CHAN\_DYNAMIC\_START](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302)   } |
| enum | [bt\_rfcomm\_role](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2) { [BT\_RFCOMM\_ROLE\_ACCEPTOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d) , [BT\_RFCOMM\_ROLE\_INITIATOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8) } |
|  | Role of RFCOMM session and dlc. [More...](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2) |
| enum | {     [BT\_RFCOMM\_RPN\_BAUD\_RATE\_2400](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3) = 0x0 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_4800](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60) = 0x1 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_7200](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593) = 0x2 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_9600](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9) = 0x3 ,     [BT\_RFCOMM\_RPN\_BAUD\_RATE\_19200](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c) = 0x4 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_38400](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5) = 0x5 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_57600](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048) = 0x6 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_115200](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33) = 0x7 ,     [BT\_RFCOMM\_RPN\_BAUD\_RATE\_230400](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760) = 0x8   } |
|  | RFCOMM RPN baud rate values. [More...](group__bt__rfcomm.md#ga61637d261987529c219dcd1179ed1711) |
| enum | { [BT\_RFCOMM\_RPN\_DATA\_BITS\_5](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1) = 0x0 , [BT\_RFCOMM\_RPN\_DATA\_BITS\_6](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc) = 0x1 , [BT\_RFCOMM\_RPN\_DATA\_BITS\_7](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867) = 0x2 , [BT\_RFCOMM\_RPN\_DATA\_BITS\_8](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83) = 0x3 } |
|  | RFCOMM RPN data bit values. [More...](group__bt__rfcomm.md#ga15600feb01d876e319e1d5f93991592b) |
| enum | { [BT\_RFCOMM\_RPN\_STOP\_BITS\_1](group__bt__rfcomm.md#ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339) = 0 , [BT\_RFCOMM\_RPN\_STOP\_BITS\_1\_5](group__bt__rfcomm.md#ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6) = 1 } |
|  | RFCOMM RPN stop bit values. [More...](group__bt__rfcomm.md#gabe97ddd372c3b0b44a9b78539ddf9ffc) |
| enum | {     [BT\_RFCOMM\_RPN\_PARITY\_NONE](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b) = 0x0 , [BT\_RFCOMM\_RPN\_PARITY\_ODD](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169) = 0x1 , [BT\_RFCOMM\_RPN\_PARITY\_EVEN](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18) = 0x3 , [BT\_RFCOMM\_RPN\_PARITY\_MARK](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9) = 0x5 ,     [BT\_RFCOMM\_RPN\_PARITY\_SPACE](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1) = 0x7   } |
|  | RFCOMM RPN parity bit values. [More...](group__bt__rfcomm.md#gad1794db284f7b39f4816f04f21ed3f4b) |

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
| int | [bt\_rfcomm\_send\_rpn\_cmd](group__bt__rfcomm.md#gab38378db71d7f4631e47742ce4a5c59d) (struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [bt\_rfcomm\_rpn](structbt__rfcomm__rpn.md) \*rpn) |
|  | Send Remote Port Negotiation command. |

## Detailed Description

Bluetooth RFCOMM handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [rfcomm.h](rfcomm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
