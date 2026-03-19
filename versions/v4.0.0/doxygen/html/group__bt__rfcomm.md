---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__rfcomm.html
original_path: doxygen/html/group__bt__rfcomm.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

| Typedefs | |
| --- | --- |
| typedef enum [bt\_rfcomm\_role](#gaa70d7971435dc7e6421372d7385811b2) | [bt\_rfcomm\_role\_t](#ga11f290d34ad631afaa10caf2cefd72b9) |
|  | Role of RFCOMM session and dlc. |

| Enumerations | |
| --- | --- |
| enum | {     [BT\_RFCOMM\_CHAN\_HFP\_HF](#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4) = 1 , [BT\_RFCOMM\_CHAN\_HFP\_AG](#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd) , [BT\_RFCOMM\_CHAN\_HSP\_AG](#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b) , [BT\_RFCOMM\_CHAN\_HSP\_HS](#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25) ,     [BT\_RFCOMM\_CHAN\_SPP](#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495)   } |
| enum | [bt\_rfcomm\_role](#gaa70d7971435dc7e6421372d7385811b2) { [BT\_RFCOMM\_ROLE\_ACCEPTOR](#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d) , [BT\_RFCOMM\_ROLE\_INITIATOR](#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8) } |
|  | Role of RFCOMM session and dlc. [More...](#gaa70d7971435dc7e6421372d7385811b2) |

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

## Detailed Description

RFCOMM.

## Typedef Documentation

## [◆ ](#ga11f290d34ad631afaa10caf2cefd72b9)bt\_rfcomm\_role\_t

| typedef enum [bt\_rfcomm\_role](#gaa70d7971435dc7e6421372d7385811b2) [bt\_rfcomm\_role\_t](#ga11f290d34ad631afaa10caf2cefd72b9) |
| --- |

`#include <[rfcomm.h](rfcomm_8h.md)>`

Role of RFCOMM session and dlc.

Used only by internal APIs

## Enumeration Type Documentation

## [◆ ](#gafccaaeb8f4d4f3e3834f358ccfdfb86b)anonymous enum

| anonymous enum |
| --- |

`#include <[rfcomm.h](rfcomm_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_RFCOMM\_CHAN\_HFP\_HF |  |
| BT\_RFCOMM\_CHAN\_HFP\_AG |  |
| BT\_RFCOMM\_CHAN\_HSP\_AG |  |
| BT\_RFCOMM\_CHAN\_HSP\_HS |  |
| BT\_RFCOMM\_CHAN\_SPP |  |

## [◆ ](#gaa70d7971435dc7e6421372d7385811b2)bt\_rfcomm\_role

| enum [bt\_rfcomm\_role](#gaa70d7971435dc7e6421372d7385811b2) |
| --- |

`#include <[rfcomm.h](rfcomm_8h.md)>`

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

`#include <[rfcomm.h](rfcomm_8h.md)>`

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

`#include <[rfcomm.h](rfcomm_8h.md)>`

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

`#include <[rfcomm.h](rfcomm_8h.md)>`

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

`#include <[rfcomm.h](rfcomm_8h.md)>`

Send data to RFCOMM.

Send data from buffer to the dlc. Length should be less than or equal to mtu.

Parameters
:   | dlc | Dlc object. |
    | --- | --- |
    | buf | Data buffer. |

Returns
:   Bytes sent in case of success or negative value in case of error.

## [◆ ](#gafd0ffcff41e233f74dc2726e889f5401)bt\_rfcomm\_server\_register()

| int bt\_rfcomm\_server\_register | ( | struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \* | *server* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rfcomm.h](rfcomm_8h.md)>`

Register RFCOMM server.

Register RFCOMM server for a channel, each new connection is authorized using the [accept()](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb "POSIX wrapper for zsock_accept.") callback which in case of success shall allocate the dlc structure to be used by the new connection.

Parameters
:   | server | Server structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
