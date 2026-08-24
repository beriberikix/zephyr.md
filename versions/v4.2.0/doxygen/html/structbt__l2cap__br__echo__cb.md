---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__l2cap__br__echo__cb.html
original_path: doxygen/html/structbt__l2cap__br__echo__cb.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_l2cap\_br\_echo\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [L2CAP](group__bt__l2cap.md)

ECHO request/response callback structure.
[More...](#details)

`#include <[zephyr/bluetooth/classic/l2cap_br.h](l2cap__br_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [req](#abc56aa16213b05fb9d330e4b0147066b) )(struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) identifier, struct [net\_buf](structnet__buf.md) \*buf) |
|  | A ECHO request has been received. |
| void(\* | [rsp](#aee34c139bbfb03796aa162bf31687d6c) )(struct bt\_conn \*conn, struct [net\_buf](structnet__buf.md) \*buf) |
|  | A ECHO response has been received. |

## Detailed Description

ECHO request/response callback structure.

This structure is used for tracking the ECHO request/response signaling packets of L2CAP BR. It is registered with the help of the [bt\_l2cap\_br\_echo\_cb\_register()](group__bt__l2cap.md#ga62c0115185f5026c1a842848dc5336ce "Register ECHO callbacks.") API. It's permissible to register multiple instances of this [bt\_l2cap\_br\_echo\_cb](structbt__l2cap__br__echo__cb.md "bt_l2cap_br_echo_cb") type, in case different modules of an application are interested in tracking the ECHO request/response signaling packets. If a callback is not of interest for an instance, it may be set to NULL and will as a consequence not be used for that instance.

## Field Documentation

## [◆ ](#abc56aa16213b05fb9d330e4b0147066b)req

| void(\* bt\_l2cap\_br\_echo\_cb::req) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) identifier, struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

A ECHO request has been received.

This callback notifies the application of a ECHO request has been received. The ECHO response should be performed by calling the [bt\_l2cap\_br\_echo\_rsp()](group__bt__l2cap.md#ga8ebf537cc7e4c0a68a320f9c65c94b05 "Send ECHO data through ECHO response.") API.

Parameters
:   | conn | The ACL connection object. |
    | --- | --- |
    | identifier | The identifier of the ECHO request. |
    | buf | Received ECHO data. |

## [◆ ](#aee34c139bbfb03796aa162bf31687d6c)rsp

| void(\* bt\_l2cap\_br\_echo\_cb::rsp) (struct bt\_conn \*conn, struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

A ECHO response has been received.

This callback notifies the application of a ECHO response has been received.

Parameters
:   | conn | The ACL connection object. |
    | --- | --- |
    | buf | Received ECHO data. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[l2cap\_br.h](l2cap__br_8h_source.md)

- [bt\_l2cap\_br\_echo\_cb](structbt__l2cap__br__echo__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
