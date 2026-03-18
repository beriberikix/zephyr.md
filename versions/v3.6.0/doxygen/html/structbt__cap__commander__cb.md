---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__cap__commander__cb.html
original_path: doxygen/html/structbt__cap__commander__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Callback structure for CAP procedures.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [discovery\_complete](#af891c2a8a9a39bd081cd9d4f5eb3a468) )(struct bt\_conn \*conn, int err, const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst) |
|  | Callback for [bt\_cap\_initiator\_unicast\_discover()](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d "Discovers audio support on a remote device."). |

## Detailed Description

Callback structure for CAP procedures.

## Field Documentation

## [◆ ](#af891c2a8a9a39bd081cd9d4f5eb3a468)discovery\_complete

| void(\* bt\_cap\_commander\_cb::discovery\_complete) (struct bt\_conn \*conn, int err, const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst) |
| --- |

Callback for [bt\_cap\_initiator\_unicast\_discover()](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d "Discovers audio support on a remote device.").

Parameters
:   | conn | The connection pointer supplied to [bt\_cap\_initiator\_unicast\_discover()](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d "Discovers audio support on a remote device."). |
    | --- | --- |
    | err | 0 if Common Audio Service was found else -ENODATA. |
    | csis\_inst | The Coordinated Set Identification Service if Common Audio Service was found and includes a Coordinated Set Identification Service. NULL on error or if remote device does not include Coordinated Set Identification Service. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
