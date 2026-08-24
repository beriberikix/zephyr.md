---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__bt__rfcomm.html
original_path: doxygen/html/group__bt__rfcomm.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

RFCOMM

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

RFCOMM.
[More...](#details)

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
| #define | [BT\_RFCOMM\_HDR\_MAX\_SIZE](#ga8d7b15c80fc69a25b105aadf6f3a6a6d)   4 |
|  | RFCOMM Maximum Header Size. |
| #define | [BT\_RFCOMM\_FCS\_SIZE](#gaea26fe8eac8c5792a4cb78404dc4f7c1)   1 |
|  | RFCOMM FCS Size. |
| #define | [BT\_RFCOMM\_BUF\_SIZE](#gabb568d7f32dbd0720f203538e3aa345c)(mtu) |
|  | Helper to calculate needed buffer size for RFCOMM PDUs. |
| #define | [BT\_RFCOMM\_SET\_LINE\_SETTINGS](#gacbb625b129afb33fceafe5ddf61c839a)(data, stop, parity) |
|  | Combine data bits, stop bits and parity into a single line settings byte. |
| #define | [BT\_RFCOMM\_RPN\_FLOW\_NONE](#gaef902e774d1a6279a117968a32cc5878)   0x00 |
| #define | [BT\_RFCOMM\_RPN\_XON\_CHAR](#ga90ab80687e32da0f8164292cd63b0623)   0x11 |
| #define | [BT\_RFCOMM\_RPN\_XOFF\_CHAR](#gacdca9e597689b3de20b1df3616ad523c)   0x13 |
| #define | [BT\_RFCOMM\_RPN\_PARAM\_MASK\_ALL](#ga71099379ed90d3d6ce9d4c1eed3be827)   0x3f7f |

| Typedefs | |
| --- | --- |
| typedef enum [bt\_rfcomm\_role](#gaa70d7971435dc7e6421372d7385811b2) | [bt\_rfcomm\_role\_t](#ga11f290d34ad631afaa10caf2cefd72b9) |
|  | Role of RFCOMM session and dlc. |

| Enumerations | |
| --- | --- |
| enum | {     [BT\_RFCOMM\_CHAN\_HFP\_HF](#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4) = 1 , [BT\_RFCOMM\_CHAN\_HFP\_AG](#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd) , [BT\_RFCOMM\_CHAN\_HSP\_AG](#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b) , [BT\_RFCOMM\_CHAN\_HSP\_HS](#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25) ,     [BT\_RFCOMM\_CHAN\_SPP](#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495) , [BT\_RFCOMM\_CHAN\_DYNAMIC\_START](#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302)   } |
| enum | [bt\_rfcomm\_role](#gaa70d7971435dc7e6421372d7385811b2) { [BT\_RFCOMM\_ROLE\_ACCEPTOR](#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d) , [BT\_RFCOMM\_ROLE\_INITIATOR](#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8) } |
|  | Role of RFCOMM session and dlc. [More...](#gaa70d7971435dc7e6421372d7385811b2) |
| enum | {     [BT\_RFCOMM\_RPN\_BAUD\_RATE\_2400](#gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3) = 0x0 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_4800](#gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60) = 0x1 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_7200](#gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593) = 0x2 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_9600](#gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9) = 0x3 ,     [BT\_RFCOMM\_RPN\_BAUD\_RATE\_19200](#gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c) = 0x4 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_38400](#gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5) = 0x5 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_57600](#gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048) = 0x6 , [BT\_RFCOMM\_RPN\_BAUD\_RATE\_115200](#gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33) = 0x7 ,     [BT\_RFCOMM\_RPN\_BAUD\_RATE\_230400](#gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760) = 0x8   } |
|  | RFCOMM RPN baud rate values. [More...](#ga61637d261987529c219dcd1179ed1711) |
| enum | { [BT\_RFCOMM\_RPN\_DATA\_BITS\_5](#gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1) = 0x0 , [BT\_RFCOMM\_RPN\_DATA\_BITS\_6](#gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc) = 0x1 , [BT\_RFCOMM\_RPN\_DATA\_BITS\_7](#gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867) = 0x2 , [BT\_RFCOMM\_RPN\_DATA\_BITS\_8](#gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83) = 0x3 } |
|  | RFCOMM RPN data bit values. [More...](#ga15600feb01d876e319e1d5f93991592b) |
| enum | { [BT\_RFCOMM\_RPN\_STOP\_BITS\_1](#ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339) = 0 , [BT\_RFCOMM\_RPN\_STOP\_BITS\_1\_5](#ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6) = 1 } |
|  | RFCOMM RPN stop bit values. [More...](#gabe97ddd372c3b0b44a9b78539ddf9ffc) |
| enum | {     [BT\_RFCOMM\_RPN\_PARITY\_NONE](#ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b) = 0x0 , [BT\_RFCOMM\_RPN\_PARITY\_ODD](#ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169) = 0x1 , [BT\_RFCOMM\_RPN\_PARITY\_EVEN](#ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18) = 0x3 , [BT\_RFCOMM\_RPN\_PARITY\_MARK](#ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9) = 0x5 ,     [BT\_RFCOMM\_RPN\_PARITY\_SPACE](#ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1) = 0x7   } |
|  | RFCOMM RPN parity bit values. [More...](#gad1794db284f7b39f4816f04f21ed3f4b) |

| Functions | |
| --- | --- |
| int | [bt\_rfcomm\_server\_register](#gafd0ffcff41e233f74dc2726e889f5401) (struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \*server) |
|  | Register RFCOMM server. |
| int | [bt\_rfcomm\_dlc\_connect](#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7) (struct bt\_conn \*conn, struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Connect RFCOMM channel. |
| int | [bt\_rfcomm\_dlc\_send](#ga593841aef52027598977b7b2bbd0237d) (struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send data to RFCOMM. |
| int | [bt\_rfcomm\_dlc\_disconnect](#ga998328b021ec53f7e291ab76856ffa18) (struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc) |
|  | Disconnect RFCOMM dlc. |
| struct [net\_buf](structnet__buf.md) \* | [bt\_rfcomm\_create\_pdu](#gaed05e67dc975d94e1209372d5817077a) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool) |
|  | Allocate the buffer from pool after reserving head room for RFCOMM, L2CAP and ACL headers. |
| int | [bt\_rfcomm\_send\_rpn\_cmd](#gab38378db71d7f4631e47742ce4a5c59d) (struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [bt\_rfcomm\_rpn](structbt__rfcomm__rpn.md) \*rpn) |
|  | Send Remote Port Negotiation command. |

## Detailed Description

RFCOMM.

## Macro Definition Documentation

## [◆ ](#gabb568d7f32dbd0720f203538e3aa345c)BT\_RFCOMM\_BUF\_SIZE

| #define BT\_RFCOMM\_BUF\_SIZE | ( |  | *mtu* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

**Value:**

[BT\_L2CAP\_BUF\_SIZE](group__bt__l2cap.md#gab95b119de4757588074e367a90a7136a)([BT\_RFCOMM\_HDR\_MAX\_SIZE](#ga8d7b15c80fc69a25b105aadf6f3a6a6d) + [BT\_RFCOMM\_FCS\_SIZE](#gaea26fe8eac8c5792a4cb78404dc4f7c1) + (mtu))

[BT\_L2CAP\_BUF\_SIZE](group__bt__l2cap.md#gab95b119de4757588074e367a90a7136a)

#define BT\_L2CAP\_BUF\_SIZE(mtu)

Helper to calculate needed buffer size for L2CAP PDUs.

**Definition** l2cap.h:54

[BT\_RFCOMM\_HDR\_MAX\_SIZE](#ga8d7b15c80fc69a25b105aadf6f3a6a6d)

#define BT\_RFCOMM\_HDR\_MAX\_SIZE

RFCOMM Maximum Header Size.

**Definition** rfcomm.h:29

[BT\_RFCOMM\_FCS\_SIZE](#gaea26fe8eac8c5792a4cb78404dc4f7c1)

#define BT\_RFCOMM\_FCS\_SIZE

RFCOMM FCS Size.

**Definition** rfcomm.h:31

Helper to calculate needed buffer size for RFCOMM PDUs.

Useful for creating buffer pools.

Parameters
:   | mtu | Needed RFCOMM PDU MTU. |
    | --- | --- |

Returns
:   Needed buffer size to match the requested RFCOMM PDU MTU.

## [◆ ](#gaea26fe8eac8c5792a4cb78404dc4f7c1)BT\_RFCOMM\_FCS\_SIZE

| #define BT\_RFCOMM\_FCS\_SIZE   1 |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

RFCOMM FCS Size.

## [◆ ](#ga8d7b15c80fc69a25b105aadf6f3a6a6d)BT\_RFCOMM\_HDR\_MAX\_SIZE

| #define BT\_RFCOMM\_HDR\_MAX\_SIZE   4 |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

RFCOMM Maximum Header Size.

The length could be 2 bytes, it depends on information length.

## [◆ ](#gaef902e774d1a6279a117968a32cc5878)BT\_RFCOMM\_RPN\_FLOW\_NONE

| #define BT\_RFCOMM\_RPN\_FLOW\_NONE   0x00 |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

## [◆ ](#ga71099379ed90d3d6ce9d4c1eed3be827)BT\_RFCOMM\_RPN\_PARAM\_MASK\_ALL

| #define BT\_RFCOMM\_RPN\_PARAM\_MASK\_ALL   0x3f7f |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

## [◆ ](#gacdca9e597689b3de20b1df3616ad523c)BT\_RFCOMM\_RPN\_XOFF\_CHAR

| #define BT\_RFCOMM\_RPN\_XOFF\_CHAR   0x13 |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

## [◆ ](#ga90ab80687e32da0f8164292cd63b0623)BT\_RFCOMM\_RPN\_XON\_CHAR

| #define BT\_RFCOMM\_RPN\_XON\_CHAR   0x11 |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

## [◆ ](#gacbb625b129afb33fceafe5ddf61c839a)BT\_RFCOMM\_SET\_LINE\_SETTINGS

| #define BT\_RFCOMM\_SET\_LINE\_SETTINGS | ( |  | *data*, |
| --- | --- | --- | --- |
|  |  |  | *stop*, |
|  |  |  | *parity* ) |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

**Value:**

((data & 0x3) | \

((stop & 0x1) << 2) | \

((parity & 0x7) << 3))

Combine data bits, stop bits and parity into a single line settings byte.

Parameters
:   | data | Data bits value (0-3) |
    | --- | --- |
    | stop | Stop bits value (0-1) |
    | parity | Parity value (0-7) |

Returns
:   Combined line settings byte

## Typedef Documentation

## [◆ ](#ga11f290d34ad631afaa10caf2cefd72b9)bt\_rfcomm\_role\_t

| typedef enum [bt\_rfcomm\_role](#gaa70d7971435dc7e6421372d7385811b2) [bt\_rfcomm\_role\_t](#ga11f290d34ad631afaa10caf2cefd72b9) |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

Role of RFCOMM session and dlc.

Used only by internal APIs

## Enumeration Type Documentation

## [◆ ](#ga61637d261987529c219dcd1179ed1711)anonymous enum

| anonymous enum |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

RFCOMM RPN baud rate values.

| Enumerator | |
| --- | --- |
| BT\_RFCOMM\_RPN\_BAUD\_RATE\_2400 |  |
| BT\_RFCOMM\_RPN\_BAUD\_RATE\_4800 |  |
| BT\_RFCOMM\_RPN\_BAUD\_RATE\_7200 |  |
| BT\_RFCOMM\_RPN\_BAUD\_RATE\_9600 |  |
| BT\_RFCOMM\_RPN\_BAUD\_RATE\_19200 |  |
| BT\_RFCOMM\_RPN\_BAUD\_RATE\_38400 |  |
| BT\_RFCOMM\_RPN\_BAUD\_RATE\_57600 |  |
| BT\_RFCOMM\_RPN\_BAUD\_RATE\_115200 |  |
| BT\_RFCOMM\_RPN\_BAUD\_RATE\_230400 |  |

## [◆ ](#ga15600feb01d876e319e1d5f93991592b)anonymous enum

| anonymous enum |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

RFCOMM RPN data bit values.

| Enumerator | |
| --- | --- |
| BT\_RFCOMM\_RPN\_DATA\_BITS\_5 |  |
| BT\_RFCOMM\_RPN\_DATA\_BITS\_6 |  |
| BT\_RFCOMM\_RPN\_DATA\_BITS\_7 |  |
| BT\_RFCOMM\_RPN\_DATA\_BITS\_8 |  |

## [◆ ](#gafccaaeb8f4d4f3e3834f358ccfdfb86b)anonymous enum

| anonymous enum |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_RFCOMM\_CHAN\_HFP\_HF |  |
| BT\_RFCOMM\_CHAN\_HFP\_AG |  |
| BT\_RFCOMM\_CHAN\_HSP\_AG |  |
| BT\_RFCOMM\_CHAN\_HSP\_HS |  |
| BT\_RFCOMM\_CHAN\_SPP |  |
| BT\_RFCOMM\_CHAN\_DYNAMIC\_START |  |

## [◆ ](#gad1794db284f7b39f4816f04f21ed3f4b)anonymous enum

| anonymous enum |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

RFCOMM RPN parity bit values.

| Enumerator | |
| --- | --- |
| BT\_RFCOMM\_RPN\_PARITY\_NONE |  |
| BT\_RFCOMM\_RPN\_PARITY\_ODD |  |
| BT\_RFCOMM\_RPN\_PARITY\_EVEN |  |
| BT\_RFCOMM\_RPN\_PARITY\_MARK |  |
| BT\_RFCOMM\_RPN\_PARITY\_SPACE |  |

## [◆ ](#gabe97ddd372c3b0b44a9b78539ddf9ffc)anonymous enum

| anonymous enum |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

RFCOMM RPN stop bit values.

| Enumerator | |
| --- | --- |
| BT\_RFCOMM\_RPN\_STOP\_BITS\_1 |  |
| BT\_RFCOMM\_RPN\_STOP\_BITS\_1\_5 |  |

## [◆ ](#gaa70d7971435dc7e6421372d7385811b2)bt\_rfcomm\_role

| enum [bt\_rfcomm\_role](#gaa70d7971435dc7e6421372d7385811b2) |
| --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

Role of RFCOMM session and dlc.

Used only by internal APIs

| Enumerator | |
| --- | --- |
| BT\_RFCOMM\_ROLE\_ACCEPTOR |  |
| BT\_RFCOMM\_ROLE\_INITIATOR |  |

## Function Documentation

## [◆ ](#gaed05e67dc975d94e1209372d5817077a)bt\_rfcomm\_create\_pdu()

| struct [net\_buf](structnet__buf.md) \* bt\_rfcomm\_create\_pdu | ( | struct [net\_buf\_pool](structnet__buf__pool.md) \* | *pool* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

Allocate the buffer from pool after reserving head room for RFCOMM, L2CAP and ACL headers.

Parameters
:   | pool | Which pool to take the buffer from. |
    | --- | --- |

Returns
:   New buffer.

## [◆ ](#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)bt\_rfcomm\_dlc\_connect()

| int bt\_rfcomm\_dlc\_connect | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \* | *dlc*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel* ) |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

Connect RFCOMM channel.

Connect RFCOMM dlc by channel, once the connection is completed dlc connected() callback will be called. If the connection is rejected disconnected() callback is called instead.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | dlc | Dlc object. |
    | channel | Server channel to connect to. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga998328b021ec53f7e291ab76856ffa18)bt\_rfcomm\_dlc\_disconnect()

| int bt\_rfcomm\_dlc\_disconnect | ( | struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \* | *dlc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

Disconnect RFCOMM dlc.

Disconnect RFCOMM dlc, if the connection is pending it will be canceled and as a result the dlc disconnected() callback is called.

Parameters
:   | dlc | Dlc object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga593841aef52027598977b7b2bbd0237d)bt\_rfcomm\_dlc\_send()

| int bt\_rfcomm\_dlc\_send | ( | struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \* | *dlc*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf* ) |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

Send data to RFCOMM.

Send data from buffer to the dlc. Length should be less than or equal to mtu.

Parameters
:   | dlc | Dlc object. |
    | --- | --- |
    | buf | Data buffer. |

Returns
:   Bytes sent in case of success or negative value in case of error.

## [◆ ](#gab38378db71d7f4631e47742ce4a5c59d)bt\_rfcomm\_send\_rpn\_cmd()

| int bt\_rfcomm\_send\_rpn\_cmd | ( | struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \* | *dlc*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_rfcomm\_rpn](structbt__rfcomm__rpn.md) \* | *rpn* ) |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

Send Remote Port Negotiation command.

Parameters
:   | dlc | Pointer to the RFCOMM DLC |
    | --- | --- |
    | rpn | Pointer to the RPN parameters to send |

Returns
:   0 on success, negative error code on failure

## [◆ ](#gafd0ffcff41e233f74dc2726e889f5401)bt\_rfcomm\_server\_register()

| int bt\_rfcomm\_server\_register | ( | struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \* | *server* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h.md)>`

Register RFCOMM server.

Register RFCOMM server for a channel, each new connection is authorized using the [accept()](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864) callback which in case of success shall allocate the dlc structure to be used by the new connection.

Parameters
:   | server | Server structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
