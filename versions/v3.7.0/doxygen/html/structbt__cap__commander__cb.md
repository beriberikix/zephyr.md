---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__cap__commander__cb.html
original_path: doxygen/html/structbt__cap__commander__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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
| void(\* | [discovery\_complete](#af989b3ebe7e5cc83a1ca4b2ef080e14d) )(struct bt\_conn \*conn, int err, const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member, const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst) |
|  | Callback for [bt\_cap\_initiator\_unicast\_discover()](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d "Discovers audio support on a remote device."). |
| void(\* | [volume\_changed](#a3a7777603c23c14bc9d01cf29bc70ef7) )(struct bt\_conn \*conn, int err) |
|  | Callback for [bt\_cap\_commander\_change\_volume()](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6 "Change the volume on one or more Common Audio Profile Acceptors."). |
| void(\* | [volume\_mute\_changed](#acc9fcedf7f7abe86e055d48e6df124c7) )(struct bt\_conn \*conn, int err) |
|  | Callback for [bt\_cap\_commander\_change\_volume\_mute\_state()](group__bt__cap.md#gac5f94baa82fa6deade6f83346a56b5e4 "Change the volume mute state on one or more Common Audio Profile Acceptors."). |
| void(\* | [volume\_offset\_changed](#a3bacfffef8d122db4574463777dfd507) )(struct bt\_conn \*conn, int err) |
|  | Callback for [bt\_cap\_commander\_change\_volume\_offset()](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa "Change the volume offset on one or more Common Audio Profile Acceptors."). |
| void(\* | [microphone\_mute\_changed](#aa49e7eaf5c45d70c800f28b81f9967e5) )(struct bt\_conn \*conn, int err) |
|  | Callback for [bt\_cap\_commander\_change\_microphone\_mute\_state()](group__bt__cap.md#ga19cc7ed5992a528a7795b76e7add6d54 "Change the microphone mute state on one or more Common Audio Profile Acceptors."). |
| void(\* | [microphone\_gain\_changed](#a1e83872924e1aa1293c499184ade9173) )(struct bt\_conn \*conn, int err) |
|  | Callback for [bt\_cap\_commander\_change\_microphone\_gain\_setting()](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b "Change the microphone gain setting on one or more Common Audio Profile Acceptors."). |
| void(\* | [broadcast\_reception\_start](#a14f6a51db5a76aac015a5de617712af3) )(struct bt\_conn \*conn, int err) |
|  | Callback for [bt\_cap\_commander\_broadcast\_reception\_start()](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9 "Starts the reception of broadcast audio on one or more remote Common Audio Profile Acceptors."). |

## Detailed Description

Callback structure for CAP procedures.

## Field Documentation

## [◆ ](#a14f6a51db5a76aac015a5de617712af3)broadcast\_reception\_start

| void(\* bt\_cap\_commander\_cb::broadcast\_reception\_start) (struct bt\_conn \*conn, int err) |
| --- |

Callback for [bt\_cap\_commander\_broadcast\_reception\_start()](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9 "Starts the reception of broadcast audio on one or more remote Common Audio Profile Acceptors.").

Parameters
:   | conn | Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure.") |
    | --- | --- |
    | err | 0 on success, [BT\_GATT\_ERR()](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "Construct error return value for attribute read and write callbacks.") with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure."). |

## [◆ ](#af989b3ebe7e5cc83a1ca4b2ef080e14d)discovery\_complete

| void(\* bt\_cap\_commander\_cb::discovery\_complete) (struct bt\_conn \*conn, int err, const struct [bt\_csip\_set\_coordinator\_set\_member](structbt__csip__set__coordinator__set__member.md) \*member, const struct [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md) \*csis\_inst) |
| --- |

Callback for [bt\_cap\_initiator\_unicast\_discover()](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d "Discovers audio support on a remote device.").

Parameters
:   | conn | The connection pointer supplied to [bt\_cap\_initiator\_unicast\_discover()](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d "Discovers audio support on a remote device."). |
    | --- | --- |
    | err | 0 if Common Audio Service was found else -ENODATA. |
    | member | Pointer to the set member. NULL if err != 0. |
    | csis\_inst | The Coordinated Set Identification Service if Common Audio Service was found and includes a Coordinated Set Identification Service. NULL on error or if remote device does not include Coordinated Set Identification Service. NULL if err != 0. |

## [◆ ](#a1e83872924e1aa1293c499184ade9173)microphone\_gain\_changed

| void(\* bt\_cap\_commander\_cb::microphone\_gain\_changed) (struct bt\_conn \*conn, int err) |
| --- |

Callback for [bt\_cap\_commander\_change\_microphone\_gain\_setting()](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b "Change the microphone gain setting on one or more Common Audio Profile Acceptors.").

Parameters
:   | conn | Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure.") |
    | --- | --- |
    | err | 0 on success, [BT\_GATT\_ERR()](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "Construct error return value for attribute read and write callbacks.") with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure."). |

## [◆ ](#aa49e7eaf5c45d70c800f28b81f9967e5)microphone\_mute\_changed

| void(\* bt\_cap\_commander\_cb::microphone\_mute\_changed) (struct bt\_conn \*conn, int err) |
| --- |

Callback for [bt\_cap\_commander\_change\_microphone\_mute\_state()](group__bt__cap.md#ga19cc7ed5992a528a7795b76e7add6d54 "Change the microphone mute state on one or more Common Audio Profile Acceptors.").

Parameters
:   | conn | Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure.") |
    | --- | --- |
    | err | 0 on success, [BT\_GATT\_ERR()](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "Construct error return value for attribute read and write callbacks.") with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure."). |

## [◆ ](#a3a7777603c23c14bc9d01cf29bc70ef7)volume\_changed

| void(\* bt\_cap\_commander\_cb::volume\_changed) (struct bt\_conn \*conn, int err) |
| --- |

Callback for [bt\_cap\_commander\_change\_volume()](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6 "Change the volume on one or more Common Audio Profile Acceptors.").

Parameters
:   | conn | Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure.") |
    | --- | --- |
    | err | 0 on success, [BT\_GATT\_ERR()](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "Construct error return value for attribute read and write callbacks.") with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure."). |

## [◆ ](#acc9fcedf7f7abe86e055d48e6df124c7)volume\_mute\_changed

| void(\* bt\_cap\_commander\_cb::volume\_mute\_changed) (struct bt\_conn \*conn, int err) |
| --- |

Callback for [bt\_cap\_commander\_change\_volume\_mute\_state()](group__bt__cap.md#gac5f94baa82fa6deade6f83346a56b5e4 "Change the volume mute state on one or more Common Audio Profile Acceptors.").

Parameters
:   | conn | Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure.") |
    | --- | --- |
    | err | 0 on success, [BT\_GATT\_ERR()](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "Construct error return value for attribute read and write callbacks.") with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure."). |

## [◆ ](#a3bacfffef8d122db4574463777dfd507)volume\_offset\_changed

| void(\* bt\_cap\_commander\_cb::volume\_offset\_changed) (struct bt\_conn \*conn, int err) |
| --- |

Callback for [bt\_cap\_commander\_change\_volume\_offset()](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa "Change the volume offset on one or more Common Audio Profile Acceptors.").

Parameters
:   | conn | Pointer to the connection where the error occurred. NULL if `err` is 0 or if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure.") |
    | --- | --- |
    | err | 0 on success, [BT\_GATT\_ERR()](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "Construct error return value for attribute read and write callbacks.") with a specific ATT (BT\_ATT\_ERR\_\*) error code or -ECANCELED if cancelled by [bt\_cap\_commander\_cancel()](group__bt__cap.md#ga7abf029533fed391930257605f3c752c "Cancel any current Common Audio Profile commander procedure."). |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
