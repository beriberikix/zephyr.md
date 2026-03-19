---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__avrcp__cb.html
original_path: doxygen/html/structbt__avrcp__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_avrcp\_cb Struct Reference

`#include <[avrcp.h](avrcp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#ac9b46b911f061a588cf87dd381364d0f) )(struct bt\_avrcp \*avrcp) |
|  | An AVRCP connection has been established. |
| void(\* | [disconnected](#acea85b2e1da11e0fd5835ce18c67ded1) )(struct bt\_avrcp \*avrcp) |
|  | An AVRCP connection has been disconnected. |
| void(\* | [unit\_info\_rsp](#ad2ea0d60add3fde24c291159cf365596) )(struct bt\_avrcp \*avrcp, struct [bt\_avrcp\_unit\_info\_rsp](structbt__avrcp__unit__info__rsp.md) \*rsp) |
|  | Callback function for [bt\_avrcp\_get\_unit\_info()](avrcp_8h.md#aba521a01fea4e7aee8b40ba72ca10bcf "Get AVRCP Unit Info."). |
| void(\* | [subunit\_info\_rsp](#a75343c9da504a3dfa12e5f1959c9c58b) )(struct bt\_avrcp \*avrcp, struct [bt\_avrcp\_subunit\_info\_rsp](structbt__avrcp__subunit__info__rsp.md) \*rsp) |
|  | Callback function for [bt\_avrcp\_get\_subunit\_info()](avrcp_8h.md#a127eaf05867a84fb5183e044fdfb55c0 "Get AVRCP Subunit Info."). |
| void(\* | [passthrough\_rsp](#a55be9880812b2e8fcc97480e1f0359dd) )(struct bt\_avrcp \*avrcp, struct [bt\_avrcp\_passthrough\_rsp](structbt__avrcp__passthrough__rsp.md) \*rsp) |
|  | Callback function for [bt\_avrcp\_passthrough()](avrcp_8h.md#afeea270bacac6a59af74c02fc1d98945 "Send AVRCP Pass Through command."). |

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

## [◆ ](#a55be9880812b2e8fcc97480e1f0359dd)passthrough\_rsp

| void(\* bt\_avrcp\_cb::passthrough\_rsp) (struct bt\_avrcp \*avrcp, struct [bt\_avrcp\_passthrough\_rsp](structbt__avrcp__passthrough__rsp.md) \*rsp) |
| --- |

Callback function for [bt\_avrcp\_passthrough()](avrcp_8h.md#afeea270bacac6a59af74c02fc1d98945 "Send AVRCP Pass Through command.").

Called when a passthrough response is received.

Parameters
:   | avrcp | AVRCP connection object. |
    | --- | --- |
    | rsp | The response for PASS THROUGH command. |

## [◆ ](#a75343c9da504a3dfa12e5f1959c9c58b)subunit\_info\_rsp

| void(\* bt\_avrcp\_cb::subunit\_info\_rsp) (struct bt\_avrcp \*avrcp, struct [bt\_avrcp\_subunit\_info\_rsp](structbt__avrcp__subunit__info__rsp.md) \*rsp) |
| --- |

Callback function for [bt\_avrcp\_get\_subunit\_info()](avrcp_8h.md#a127eaf05867a84fb5183e044fdfb55c0 "Get AVRCP Subunit Info.").

Called when the get subunit info process is completed.

Parameters
:   | avrcp | AVRCP connection object. |
    | --- | --- |
    | rsp | The response for SUBUNIT INFO command. |

## [◆ ](#ad2ea0d60add3fde24c291159cf365596)unit\_info\_rsp

| void(\* bt\_avrcp\_cb::unit\_info\_rsp) (struct bt\_avrcp \*avrcp, struct [bt\_avrcp\_unit\_info\_rsp](structbt__avrcp__unit__info__rsp.md) \*rsp) |
| --- |

Callback function for [bt\_avrcp\_get\_unit\_info()](avrcp_8h.md#aba521a01fea4e7aee8b40ba72ca10bcf "Get AVRCP Unit Info.").

Called when the get unit info process is completed.

Parameters
:   | avrcp | AVRCP connection object. |
    | --- | --- |
    | rsp | The response for UNIT INFO command. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[avrcp.h](avrcp_8h_source.md)

- [bt\_avrcp\_cb](structbt__avrcp__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
