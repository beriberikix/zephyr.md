---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__avrcp__cb.html
original_path: doxygen/html/structbt__avrcp__cb.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_avrcp\_cb Struct Reference

`#include <[zephyr/bluetooth/classic/avrcp.h](avrcp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#ac9b46b911f061a588cf87dd381364d0f) )(struct bt\_avrcp \*avrcp) |
|  | An AVRCP connection has been established. |
| void(\* | [disconnected](#acea85b2e1da11e0fd5835ce18c67ded1) )(struct bt\_avrcp \*avrcp) |
|  | An AVRCP connection has been disconnected. |
| void(\* | [get\_cap\_rsp](#a744937bf0dcd8e2759ff7134de7867ec) )(struct bt\_avrcp \*avrcp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid, const struct [bt\_avrcp\_get\_cap\_rsp](structbt__avrcp__get__cap__rsp.md) \*rsp) |
|  | Callback function for [bt\_avrcp\_get\_cap()](avrcp_8h.md#adb21554b69948d5994de8344f44c1179 "Get AVRCP Capabilities."). |
| void(\* | [unit\_info\_rsp](#aeb0840108e7439d9277a7be55bafcef3) )(struct bt\_avrcp \*avrcp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid, struct [bt\_avrcp\_unit\_info\_rsp](structbt__avrcp__unit__info__rsp.md) \*rsp) |
|  | Callback function for [bt\_avrcp\_get\_unit\_info()](avrcp_8h.md#a7d9faee722b04fb3133b1cf863e5f1c9 "Get AVRCP Unit Info."). |
| void(\* | [subunit\_info\_rsp](#a3626e3a9afca29ca316279df5b8e04d5) )(struct bt\_avrcp \*avrcp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid, struct [bt\_avrcp\_subunit\_info\_rsp](structbt__avrcp__subunit__info__rsp.md) \*rsp) |
|  | Callback function for [bt\_avrcp\_get\_subunit\_info()](avrcp_8h.md#a495525e5d5b9b743bc6eb13e4881b0f3 "Get AVRCP Subunit Info."). |
| void(\* | [passthrough\_rsp](#ac92103e695c40e36cb344824ec98fc1b) )(struct bt\_avrcp \*avrcp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid, [bt\_avrcp\_rsp\_t](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326) result, const struct [bt\_avrcp\_passthrough\_rsp](structbt__avrcp__passthrough__rsp.md) \*rsp) |
|  | Callback function for [bt\_avrcp\_passthrough()](avrcp_8h.md#abfe2bc60019a560ea90455d0df613392 "Send AVRCP Pass Through command."). |

## Field Documentation

## [◆ ](#ac9b46b911f061a588cf87dd381364d0f)connected

| void(\* bt\_avrcp\_cb::connected) (struct bt\_avrcp \*avrcp) |
| --- |

An AVRCP connection has been established.

This callback notifies the application of an avrcp connection, i.e., an AVCTP L2CAP connection.

Parameters
:   | avrcp | AVRCP connection object. |
    | --- | --- |

## [◆ ](#acea85b2e1da11e0fd5835ce18c67ded1)disconnected

| void(\* bt\_avrcp\_cb::disconnected) (struct bt\_avrcp \*avrcp) |
| --- |

An AVRCP connection has been disconnected.

This callback notifies the application that an avrcp connection has been disconnected.

Parameters
:   | avrcp | AVRCP connection object. |
    | --- | --- |

## [◆ ](#a744937bf0dcd8e2759ff7134de7867ec)get\_cap\_rsp

| void(\* bt\_avrcp\_cb::get\_cap\_rsp) (struct bt\_avrcp \*avrcp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid, const struct [bt\_avrcp\_get\_cap\_rsp](structbt__avrcp__get__cap__rsp.md) \*rsp) |
| --- |

Callback function for [bt\_avrcp\_get\_cap()](avrcp_8h.md#adb21554b69948d5994de8344f44c1179 "Get AVRCP Capabilities.").

Called when the get capabilities process is completed.

Parameters
:   | avrcp | AVRCP connection object. |
    | --- | --- |
    | tid | The transaction label of the response. |
    | rsp | The response for Get Capabilities command. |

## [◆ ](#ac92103e695c40e36cb344824ec98fc1b)passthrough\_rsp

| void(\* bt\_avrcp\_cb::passthrough\_rsp) (struct bt\_avrcp \*avrcp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid, [bt\_avrcp\_rsp\_t](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326) result, const struct [bt\_avrcp\_passthrough\_rsp](structbt__avrcp__passthrough__rsp.md) \*rsp) |
| --- |

Callback function for [bt\_avrcp\_passthrough()](avrcp_8h.md#abfe2bc60019a560ea90455d0df613392 "Send AVRCP Pass Through command.").

Called when a passthrough response is received.

Parameters
:   | avrcp | AVRCP connection object. |
    | --- | --- |
    | tid | The transaction label of the response. |
    | result | The result of the operation. |
    | rsp | The response for PASS THROUGH command. |

## [◆ ](#a3626e3a9afca29ca316279df5b8e04d5)subunit\_info\_rsp

| void(\* bt\_avrcp\_cb::subunit\_info\_rsp) (struct bt\_avrcp \*avrcp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid, struct [bt\_avrcp\_subunit\_info\_rsp](structbt__avrcp__subunit__info__rsp.md) \*rsp) |
| --- |

Callback function for [bt\_avrcp\_get\_subunit\_info()](avrcp_8h.md#a495525e5d5b9b743bc6eb13e4881b0f3 "Get AVRCP Subunit Info.").

Called when the get subunit info process is completed.

Parameters
:   | avrcp | AVRCP connection object. |
    | --- | --- |
    | tid | The transaction label of the response. |
    | rsp | The response for SUBUNIT INFO command. |

## [◆ ](#aeb0840108e7439d9277a7be55bafcef3)unit\_info\_rsp

| void(\* bt\_avrcp\_cb::unit\_info\_rsp) (struct bt\_avrcp \*avrcp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tid, struct [bt\_avrcp\_unit\_info\_rsp](structbt__avrcp__unit__info__rsp.md) \*rsp) |
| --- |

Callback function for [bt\_avrcp\_get\_unit\_info()](avrcp_8h.md#a7d9faee722b04fb3133b1cf863e5f1c9 "Get AVRCP Unit Info.").

Called when the get unit info process is completed.

Parameters
:   | avrcp | AVRCP connection object. |
    | --- | --- |
    | tid | The transaction label of the response. |
    | rsp | The response for UNIT INFO command. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[avrcp.h](avrcp_8h_source.md)

- [bt\_avrcp\_cb](structbt__avrcp__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
