---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__cap__initiator__cb.html
original_path: doxygen/html/structbt__cap__initiator__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_initiator\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Callback structure for CAP procedures.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [unicast\_discovery\_complete](#a642a2f48e8f870bb1681ba58aa119de9) )(struct bt\_conn \*conn, int err, const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member, const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst) |
|  | Callback for [bt\_cap\_initiator\_unicast\_discover()](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d "Discovers audio support on a remote device."). |
| void(\* | [unicast\_start\_complete](#aa70de1dda73ffdcbb8287f8f174984ea) )(int err, struct bt\_conn \*conn) |
|  | Callback for [bt\_cap\_initiator\_unicast\_audio\_start()](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184 "Setup and start unicast audio streams for a set of devices."). |
| void(\* | [unicast\_update\_complete](#a95266741841fca83cd2769c76652154e) )(int err, struct bt\_conn \*conn) |
|  | Callback for [bt\_cap\_initiator\_unicast\_audio\_update()](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639 "Update unicast audio streams."). |
| void(\* | [unicast\_stop\_complete](#a2e910a82209d144878b6c69c1b2723ba) )(int err, struct bt\_conn \*conn) |
|  | Callback for [bt\_cap\_initiator\_unicast\_audio\_stop()](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f "Stop unicast audio streams."). |

## Detailed Description

Callback structure for CAP procedures.

## Field Documentation

## [◆ ](#a642a2f48e8f870bb1681ba58aa119de9)unicast\_discovery\_complete

| void(\* bt\_cap\_initiator\_cb::unicast\_discovery\_complete) (struct bt\_conn \*conn, int err, const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member, const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst) |
| --- |

Callback for [bt\_cap\_initiator\_unicast\_discover()](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d "Discovers audio support on a remote device.").

Parameters
:   | conn | The connection pointer supplied to [bt\_cap\_initiator\_unicast\_discover()](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d "Discovers audio support on a remote device."). |
    | --- | --- |
    | err | 0 if Common Audio Service was found else -ENODATA. |
    | member | Pointer to the set member. NULL if err != 0. |
    | csis\_inst | The Coordinated Set Identification Service if Common Audio Service was found and includes a Coordinated Set Identification Service. NULL on error or if remote device does not include Coordinated Set Identification Service. NULL if err != 0. |

## [◆ ](#aa70de1dda73ffdcbb8287f8f174984ea)unicast\_start\_complete

| void(\* bt\_cap\_initiator\_cb::unicast\_start\_complete) (int err, struct bt\_conn \*conn) |
| --- |

Callback for [bt\_cap\_initiator\_unicast\_audio\_start()](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184 "Setup and start unicast audio streams for a set of devices.").

Parameters
:   | err | 0 if success, [BT\_GATT\_ERR()](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "Construct error return value for attribute read and write callbacks.") with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f "Cancel any current Common Audio Profile procedure."). |
    | --- | --- |
    | conn | Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f "Cancel any current Common Audio Profile procedure.") |

## [◆ ](#a2e910a82209d144878b6c69c1b2723ba)unicast\_stop\_complete

| void(\* bt\_cap\_initiator\_cb::unicast\_stop\_complete) (int err, struct bt\_conn \*conn) |
| --- |

Callback for [bt\_cap\_initiator\_unicast\_audio\_stop()](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f "Stop unicast audio streams.").

Parameters
:   | err | 0 if success, [BT\_GATT\_ERR()](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "Construct error return value for attribute read and write callbacks.") with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f "Cancel any current Common Audio Profile procedure."). |
    | --- | --- |
    | conn | Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f "Cancel any current Common Audio Profile procedure.") |

## [◆ ](#a95266741841fca83cd2769c76652154e)unicast\_update\_complete

| void(\* bt\_cap\_initiator\_cb::unicast\_update\_complete) (int err, struct bt\_conn \*conn) |
| --- |

Callback for [bt\_cap\_initiator\_unicast\_audio\_update()](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639 "Update unicast audio streams.").

Parameters
:   | err | 0 if success, [BT\_GATT\_ERR()](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "Construct error return value for attribute read and write callbacks.") with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f "Cancel any current Common Audio Profile procedure."). |
    | --- | --- |
    | conn | Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_initiator\_unicast\_audio\_cancel()](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f "Cancel any current Common Audio Profile procedure.") |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
