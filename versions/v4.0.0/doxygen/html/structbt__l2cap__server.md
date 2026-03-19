---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__l2cap__server.html
original_path: doxygen/html/structbt__l2cap__server.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_l2cap\_server Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [L2CAP](group__bt__l2cap.md)

L2CAP Server structure.
[More...](#details)

`#include <[l2cap.h](l2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [psm](#a07925dda8566ee7518b1809725e1b110) |
|  | Server PSM. |
| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) | [sec\_level](#a9f082abf679a397264a7b51fa4400852) |
|  | Required minimum security level. |
| int(\* | [accept](#ad31a1908f7dc733f9497164ccabba2af) )(struct bt\_conn \*conn, struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server, struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chan) |
|  | Server accept callback. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a76b478140d6a57038eb389eac91442c0) |

## Detailed Description

L2CAP Server structure.

## Field Documentation

## [◆ ](#ad31a1908f7dc733f9497164ccabba2af)accept

| int(\* bt\_l2cap\_server::accept) (struct bt\_conn \*conn, struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server, struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chan) |
| --- |

Server accept callback.

This callback is called whenever a new incoming connection requires authorization.

Warning
:   It is the responsibility of this callback to zero out the parent of the chan object.

Parameters
:   | conn | The connection that is requesting authorization |
    | --- | --- |
    | server | Pointer to the server structure this callback relates to |
    | chan | Pointer to received the allocated channel |

Returns
:   0 in case of success or negative value in case of error.
:   -ENOMEM if no available space for new channel.
:   -EACCES if application did not authorize the connection.
:   -EPERM if encryption key size is too short.

## [◆ ](#a76b478140d6a57038eb389eac91442c0)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_l2cap\_server::node |
| --- |

## [◆ ](#a07925dda8566ee7518b1809725e1b110)psm

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_server::psm |
| --- |

Server PSM.

Possible values: 0 A dynamic value will be auto-allocated when [bt\_l2cap\_server\_register()](group__bt__l2cap.md#ga1a5e8c81c086872d7fb8da5329f982c6 "Register L2CAP server.") is called.

0x0001-0x007f Standard, Bluetooth SIG-assigned fixed values.

0x0080-0x00ff Dynamically allocated. May be pre-set by the application before server registration (not recommended however), or auto-allocated by the stack if the app gave 0 as the value.

## [◆ ](#a9f082abf679a397264a7b51fa4400852)sec\_level

| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) bt\_l2cap\_server::sec\_level |
| --- |

Required minimum security level.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[l2cap.h](l2cap_8h_source.md)

- [bt\_l2cap\_server](structbt__l2cap__server.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
