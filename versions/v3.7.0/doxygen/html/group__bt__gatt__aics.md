---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__gatt__aics.html
original_path: doxygen/html/group__bt__gatt__aics.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Audio Input Control Service (AICS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Audio Input Control Service (AICS).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_aics\_register\_param](structbt__aics__register__param.md) |
|  | Structure for initializing a Audio Input Control Service instance. [More...](structbt__aics__register__param.md#details) |
| struct | [bt\_aics\_discover\_param](structbt__aics__discover__param.md) |
|  | Structure for discovering a Audio Input Control Service instance. [More...](structbt__aics__discover__param.md#details) |
| struct | [bt\_aics\_cb](structbt__aics__cb.md) |
|  | Struct to hold callbacks for the Audio Input Control Service. [More...](structbt__aics__cb.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_aics\_write\_cb](#ga36991fe1dee5168db618518d094d80ef)) (struct bt\_aics \*inst, int err) |
|  | Callback function for writes. |
| typedef void(\* | [bt\_aics\_state\_cb](#ga2e851f49f9c7e71a18376468a13fdf4f)) (struct bt\_aics \*inst, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) gain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode) |
|  | Callback function for the input state. |
| typedef void(\* | [bt\_aics\_gain\_setting\_cb](#ga11da08c010f4aa849c2e3725dc5cbaeb)) (struct bt\_aics \*inst, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) units, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) minimum, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) maximum) |
|  | Callback function for the gain settings. |
| typedef void(\* | [bt\_aics\_type\_cb](#ga6e76b9f2de4cdbcd7539c76f6a347fa5)) (struct bt\_aics \*inst, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type) |
|  | Callback function for the input type. |
| typedef void(\* | [bt\_aics\_status\_cb](#ga044d92a4273c6537a9cdf20922352ed6)) (struct bt\_aics \*inst, int err, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) active) |
|  | Callback function for the input status. |
| typedef void(\* | [bt\_aics\_description\_cb](#ga98b142ea7a66de5577c44aa90d507930)) (struct bt\_aics \*inst, int err, char \*description) |
|  | Callback function for the description. |
| typedef void(\* | [bt\_aics\_discover\_cb](#ga9fda39f8410308e05eb928eeb7267e83)) (struct bt\_aics \*inst, int err) |
|  | Callback function for bt\_aics\_discover. |

| Functions | |
| --- | --- |
| struct bt\_aics \* | [bt\_aics\_free\_instance\_get](#gab10ad3599f5b602cdf5504bc92508109) (void) |
|  | Get a free instance of Audio Input Control Service from the pool. |
| void \* | [bt\_aics\_svc\_decl\_get](#ga8b415343e7ecf399ecfd0dcaa49bd1ee) (struct bt\_aics \*aics) |
|  | Get the service declaration attribute. |
| int | [bt\_aics\_client\_conn\_get](#ga0e088e26cf73f1f3b918660d4acdebb9) (const struct bt\_aics \*aics, struct bt\_conn \*\*conn) |
|  | Get the connection pointer of a client instance. |
| int | [bt\_aics\_register](#ga008ef5cebfcb9b4a3084f411fa81238e) (struct bt\_aics \*aics, struct [bt\_aics\_register\_param](structbt__aics__register__param.md) \*param) |
|  | Initialize the Audio Input Control Service instance. |
| int | [bt\_aics\_discover](#gad16d296462af2f61a893bda8d25cc9de) (struct bt\_conn \*conn, struct bt\_aics \*inst, const struct [bt\_aics\_discover\_param](structbt__aics__discover__param.md) \*param) |
|  | Discover a Audio Input Control Service. |
| int | [bt\_aics\_deactivate](#ga4be4c4e3c74aa55fbf599157aa1c2098) (struct bt\_aics \*inst) |
|  | Deactivates a Audio Input Control Service instance. |
| int | [bt\_aics\_activate](#gac46268949fa7cbbb827d149a3a904daa) (struct bt\_aics \*inst) |
|  | Activates a Audio Input Control Service instance. |
| int | [bt\_aics\_state\_get](#ga23bbc1393d21fe38f501813935b25b3d) (struct bt\_aics \*inst) |
|  | Read the Audio Input Control Service input state. |
| int | [bt\_aics\_gain\_setting\_get](#ga38d7131397d7762d3bd53e152a6c6130) (struct bt\_aics \*inst) |
|  | Read the Audio Input Control Service gain settings. |
| int | [bt\_aics\_type\_get](#gaf57896e2096a5e96ec46a56cdf216159) (struct bt\_aics \*inst) |
|  | Read the Audio Input Control Service input type. |
| int | [bt\_aics\_status\_get](#gade387c52d201ce10b39ef52157dae83d) (struct bt\_aics \*inst) |
|  | Read the Audio Input Control Service input status. |
| int | [bt\_aics\_disable\_mute](#ga5a1ad98afe45da9ffbb7247671385d40) (struct bt\_aics \*inst) |
|  | Disable mute in the Audio Input Control Service. |
| int | [bt\_aics\_unmute](#ga43396d2d4b3bd9cdd0c82275fafeadfc) (struct bt\_aics \*inst) |
|  | Unmute the Audio Input Control Service input. |
| int | [bt\_aics\_mute](#ga5345254eaf099560e609d97044b39a97) (struct bt\_aics \*inst) |
|  | Mute the Audio Input Control Service input. |
| int | [bt\_aics\_gain\_set\_manual\_only](#ga0460e82d4277a2c4b14964799ad5f2b0) (struct bt\_aics \*inst) |
|  | Set manual only gain mode in Audio Input Control Service. |
| int | [bt\_aics\_gain\_set\_auto\_only](#ga22869d8a62eb59bc4aad25946da8f9cf) (struct bt\_aics \*inst) |
|  | Set automatic only gain mode in Audio Input Control Service. |
| int | [bt\_aics\_manual\_gain\_set](#ga7ddb93125f6275fc7c99fbf448e24f0c) (struct bt\_aics \*inst) |
|  | Set input gain to manual. |
| int | [bt\_aics\_automatic\_gain\_set](#ga759712886cd3c4c025ea360dcb663c59) (struct bt\_aics \*inst) |
|  | Set the input gain to automatic. |
| int | [bt\_aics\_gain\_set](#ga20f3a178788ec6aef593034159793b94) (struct bt\_aics \*inst, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) gain) |
|  | Set the input gain. |
| int | [bt\_aics\_description\_get](#gaf0b659698aa6a6a79143d4f591f67e09) (struct bt\_aics \*inst) |
|  | Read the Audio Input Control Service description. |
| int | [bt\_aics\_description\_set](#ga7de5ffd2eb61ca562b9773b37470ebd9) (struct bt\_aics \*inst, const char \*description) |
|  | Set the Audio Input Control Service description. |
| struct bt\_aics \* | [bt\_aics\_client\_free\_instance\_get](#ga913838aa0d5bff239c2faef4d8a8b36b) (void) |
|  | Get a new Audio Input Control Service client instance. |
| void | [bt\_aics\_client\_cb\_register](#gabd6bdcdad0dd5a4c509f9e7cabb3e601) (struct bt\_aics \*inst, struct [bt\_aics\_cb](structbt__aics__cb.md) \*cb) |
|  | Registers the callbacks for the Audio Input Control Service client. |

| Audio Input Control Service mute states | |
| --- | --- |
| #define | [BT\_AICS\_STATE\_UNMUTED](#ga47436e2df23067ce86dc761d77ed14b7)   0x00 |
|  | The mute state is unmuted. |
| #define | [BT\_AICS\_STATE\_MUTED](#ga1572eaaffea5412b496eb714d64aa981)   0x01 |
|  | The mute state is muted. |
| #define | [BT\_AICS\_STATE\_MUTE\_DISABLED](#gad0063d0e0b622b4093607e5485897214)   0x02 |
|  | The mute state is disabled. |

| Audio Input Control Service input modes | |
| --- | --- |
| #define | [BT\_AICS\_MODE\_MANUAL\_ONLY](#gaecb9365a5e390111311d1b415a2cee79)   0x00 |
|  | The gain mode is manual only and cannot be changed to automatic. |
| #define | [BT\_AICS\_MODE\_AUTO\_ONLY](#ga6b536bdcab602ccaccfafe3b37258890)   0x01 |
|  | The gain mode is automatic only and cannot be changed to manual. |
| #define | [BT\_AICS\_MODE\_MANUAL](#ga7cf0508dd7407ec3bb92dec71cc00816)   0x02 |
|  | The gain mode is manual. |
| #define | [BT\_AICS\_MODE\_AUTO](#ga0ac3a583dd7ca58a0d356d9f60797517)   0x03 |
|  | The gain mode is automatic. |

| Audio Input Control Service input types | |
| --- | --- |
| #define | [BT\_AICS\_INPUT\_TYPE\_UNSPECIFIED](#ga2204f35b5f1aa41c27f62b8f0dcf74b6)   0x00 |
|  | The input is unspecified. |
| #define | [BT\_AICS\_INPUT\_TYPE\_BLUETOOTH](#gac8ebf643f9a4101ea8da18827577bf5d)   0x01 |
|  | The input is a Bluetooth Audio Stream. |
| #define | [BT\_AICS\_INPUT\_TYPE\_MICROPHONE](#ga7fcb5aefacb641a8ef7db4e9a554a65d)   0x02 |
|  | The input is a microphone. |
| #define | [BT\_AICS\_INPUT\_TYPE\_ANALOG](#ga525b361d1d555f20d292cf1aded0d046)   0x03 |
|  | The input is analog. |
| #define | [BT\_AICS\_INPUT\_TYPE\_DIGITAL](#ga688605eb9eb5b27ca62fac9b85fde472)   0x04 |
|  | The input is digital. |
| #define | [BT\_AICS\_INPUT\_TYPE\_RADIO](#ga3b878b41ab30067bceefc0cd72340376)   0x05 |
|  | The input is a radio (AM/FM/XM/etc.). |
| #define | [BT\_AICS\_INPUT\_TYPE\_STREAMING](#ga43a02e2025e3cb3e10bc2ee2128ee877)   0x06 |
|  | The input is a Streaming Audio Source. |
| #define | [BT\_AICS\_INPUT\_TYPE\_AMBIENT](#gaacf259f2bc3d341c8d2857de5d412219)   0x07 |
|  | The input is transparent / pass-through. |

| Audio Input Control Service Error codes | |
| --- | --- |
| #define | [BT\_AICS\_ERR\_INVALID\_COUNTER](#gae54199f78ff7d7380353f3950bd03a39)   0x80 |
|  | The Change\_Counter operand value does not match the Change\_Counter field value of the Audio Input State characteristic. |
| #define | [BT\_AICS\_ERR\_OP\_NOT\_SUPPORTED](#ga00c0942dab2bf25c680278927aa49af8)   0x81 |
|  | An invalid opcode has been used in a control point procedure. |
| #define | [BT\_AICS\_ERR\_MUTE\_DISABLED](#ga1efb1f6a4c24c2a20fc7136928abac6b)   0x82 |
|  | Mute/unmute commands are disabled. |
| #define | [BT\_AICS\_ERR\_OUT\_OF\_RANGE](#ga2f3806b8056ea8ed43b2a7cd52ffa4f3)   0x83 |
|  | An operand value used in a control point procedure is outside the permissible range. |
| #define | [BT\_AICS\_ERR\_GAIN\_MODE\_NOT\_ALLOWED](#ga6673570f7679322bfa4719bf6e41e299)   0x84 |
|  | A requested gain mode change is not allowed. |

## Detailed Description

Audio Input Control Service (AICS).

Since
:   2.6

Version
:   0.8.0

The Audio Input Control Service is a secondary service, and as such should not be used on its own, but rather in the context of another (primary) service.

This API implements both the server and client functionality. Note that the API abstracts away the change counter in the audio input control state and will automatically handle any changes to that. If out of date, the client implementation will autonomously read the change counter value when executing a write request.

## Macro Definition Documentation

## [◆ ](#ga6673570f7679322bfa4719bf6e41e299)BT\_AICS\_ERR\_GAIN\_MODE\_NOT\_ALLOWED

| #define BT\_AICS\_ERR\_GAIN\_MODE\_NOT\_ALLOWED   0x84 |
| --- |

`#include <[aics.h](aics_8h.md)>`

A requested gain mode change is not allowed.

## [◆ ](#gae54199f78ff7d7380353f3950bd03a39)BT\_AICS\_ERR\_INVALID\_COUNTER

| #define BT\_AICS\_ERR\_INVALID\_COUNTER   0x80 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The Change\_Counter operand value does not match the Change\_Counter field value of the Audio Input State characteristic.

## [◆ ](#ga1efb1f6a4c24c2a20fc7136928abac6b)BT\_AICS\_ERR\_MUTE\_DISABLED

| #define BT\_AICS\_ERR\_MUTE\_DISABLED   0x82 |
| --- |

`#include <[aics.h](aics_8h.md)>`

Mute/unmute commands are disabled.

(see [BT\_AICS\_STATE\_MUTE\_DISABLED](#gad0063d0e0b622b4093607e5485897214))

## [◆ ](#ga00c0942dab2bf25c680278927aa49af8)BT\_AICS\_ERR\_OP\_NOT\_SUPPORTED

| #define BT\_AICS\_ERR\_OP\_NOT\_SUPPORTED   0x81 |
| --- |

`#include <[aics.h](aics_8h.md)>`

An invalid opcode has been used in a control point procedure.

## [◆ ](#ga2f3806b8056ea8ed43b2a7cd52ffa4f3)BT\_AICS\_ERR\_OUT\_OF\_RANGE

| #define BT\_AICS\_ERR\_OUT\_OF\_RANGE   0x83 |
| --- |

`#include <[aics.h](aics_8h.md)>`

An operand value used in a control point procedure is outside the permissible range.

## [◆ ](#gaacf259f2bc3d341c8d2857de5d412219)BT\_AICS\_INPUT\_TYPE\_AMBIENT

| #define BT\_AICS\_INPUT\_TYPE\_AMBIENT   0x07 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The input is transparent / pass-through.

## [◆ ](#ga525b361d1d555f20d292cf1aded0d046)BT\_AICS\_INPUT\_TYPE\_ANALOG

| #define BT\_AICS\_INPUT\_TYPE\_ANALOG   0x03 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The input is analog.

## [◆ ](#gac8ebf643f9a4101ea8da18827577bf5d)BT\_AICS\_INPUT\_TYPE\_BLUETOOTH

| #define BT\_AICS\_INPUT\_TYPE\_BLUETOOTH   0x01 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The input is a Bluetooth Audio Stream.

## [◆ ](#ga688605eb9eb5b27ca62fac9b85fde472)BT\_AICS\_INPUT\_TYPE\_DIGITAL

| #define BT\_AICS\_INPUT\_TYPE\_DIGITAL   0x04 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The input is digital.

## [◆ ](#ga7fcb5aefacb641a8ef7db4e9a554a65d)BT\_AICS\_INPUT\_TYPE\_MICROPHONE

| #define BT\_AICS\_INPUT\_TYPE\_MICROPHONE   0x02 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The input is a microphone.

## [◆ ](#ga3b878b41ab30067bceefc0cd72340376)BT\_AICS\_INPUT\_TYPE\_RADIO

| #define BT\_AICS\_INPUT\_TYPE\_RADIO   0x05 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The input is a radio (AM/FM/XM/etc.).

## [◆ ](#ga43a02e2025e3cb3e10bc2ee2128ee877)BT\_AICS\_INPUT\_TYPE\_STREAMING

| #define BT\_AICS\_INPUT\_TYPE\_STREAMING   0x06 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The input is a Streaming Audio Source.

## [◆ ](#ga2204f35b5f1aa41c27f62b8f0dcf74b6)BT\_AICS\_INPUT\_TYPE\_UNSPECIFIED

| #define BT\_AICS\_INPUT\_TYPE\_UNSPECIFIED   0x00 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The input is unspecified.

## [◆ ](#ga0ac3a583dd7ca58a0d356d9f60797517)BT\_AICS\_MODE\_AUTO

| #define BT\_AICS\_MODE\_AUTO   0x03 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The gain mode is automatic.

The gain cannot be controlled by the client.

## [◆ ](#ga6b536bdcab602ccaccfafe3b37258890)BT\_AICS\_MODE\_AUTO\_ONLY

| #define BT\_AICS\_MODE\_AUTO\_ONLY   0x01 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The gain mode is automatic only and cannot be changed to manual.

The gain cannot be controlled by the client.

## [◆ ](#ga7cf0508dd7407ec3bb92dec71cc00816)BT\_AICS\_MODE\_MANUAL

| #define BT\_AICS\_MODE\_MANUAL   0x02 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The gain mode is manual.

The gain can be controlled by the client.

## [◆ ](#gaecb9365a5e390111311d1b415a2cee79)BT\_AICS\_MODE\_MANUAL\_ONLY

| #define BT\_AICS\_MODE\_MANUAL\_ONLY   0x00 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The gain mode is manual only and cannot be changed to automatic.

The gain can be controlled by the client.

## [◆ ](#gad0063d0e0b622b4093607e5485897214)BT\_AICS\_STATE\_MUTE\_DISABLED

| #define BT\_AICS\_STATE\_MUTE\_DISABLED   0x02 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The mute state is disabled.

## [◆ ](#ga1572eaaffea5412b496eb714d64aa981)BT\_AICS\_STATE\_MUTED

| #define BT\_AICS\_STATE\_MUTED   0x01 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The mute state is muted.

## [◆ ](#ga47436e2df23067ce86dc761d77ed14b7)BT\_AICS\_STATE\_UNMUTED

| #define BT\_AICS\_STATE\_UNMUTED   0x00 |
| --- |

`#include <[aics.h](aics_8h.md)>`

The mute state is unmuted.

## Typedef Documentation

## [◆ ](#ga98b142ea7a66de5577c44aa90d507930)bt\_aics\_description\_cb

| typedef void(\* bt\_aics\_description\_cb) (struct bt\_aics \*inst, int err, char \*description) |
| --- |

`#include <[aics.h](aics_8h.md)>`

Callback function for the description.

Called when the value is read, or if the value is changed by either the server or client.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. For notifications, this will always be 0. |
    | description | The description as an UTF-8 encoded string (may have been clipped). |

## [◆ ](#ga9fda39f8410308e05eb928eeb7267e83)bt\_aics\_discover\_cb

| typedef void(\* bt\_aics\_discover\_cb) (struct bt\_aics \*inst, int err) |
| --- |

`#include <[aics.h](aics_8h.md)>`

Callback function for bt\_aics\_discover.

This callback will usually be overwritten by the primary service that includes the Audio Input Control Service client.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. For notifications, this will always be 0. |

## [◆ ](#ga11da08c010f4aa849c2e3725dc5cbaeb)bt\_aics\_gain\_setting\_cb

| typedef void(\* bt\_aics\_gain\_setting\_cb) (struct bt\_aics \*inst, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) units, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) minimum, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) maximum) |
| --- |

`#include <[aics.h](aics_8h.md)>`

Callback function for the gain settings.

Called when the value is read, or if the value is changed by either the server or client.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. For notifications, this will always be 0. |
    | units | The value that reflect the size of a single increment or decrement of the Gain Setting value in 0.1 decibel units. |
    | minimum | The minimum gain allowed for the gain setting. |
    | maximum | The maximum gain allowed for the gain setting. |

## [◆ ](#ga2e851f49f9c7e71a18376468a13fdf4f)bt\_aics\_state\_cb

| typedef void(\* bt\_aics\_state\_cb) (struct bt\_aics \*inst, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) gain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode) |
| --- |

`#include <[aics.h](aics_8h.md)>`

Callback function for the input state.

Called when the value is read, or if the value is changed by either the server or client.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. For notifications, this will always be 0. |
    | gain | The gain setting value. |
    | mute | The mute value. |
    | mode | The mode value. |

## [◆ ](#ga044d92a4273c6537a9cdf20922352ed6)bt\_aics\_status\_cb

| typedef void(\* bt\_aics\_status\_cb) (struct bt\_aics \*inst, int err, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) active) |
| --- |

`#include <[aics.h](aics_8h.md)>`

Callback function for the input status.

Called when the value is read, or if the value is changed by either the server or client.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. For notifications, this will always be 0. |
    | active | Whether the instance is active or inactive. |

## [◆ ](#ga6e76b9f2de4cdbcd7539c76f6a347fa5)bt\_aics\_type\_cb

| typedef void(\* bt\_aics\_type\_cb) (struct bt\_aics \*inst, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type) |
| --- |

`#include <[aics.h](aics_8h.md)>`

Callback function for the input type.

Called when the value is read, or if the value is changed by either the server or client.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. For notifications, this will always be 0. |
    | type | The input type. |

## [◆ ](#ga36991fe1dee5168db618518d094d80ef)bt\_aics\_write\_cb

| typedef void(\* bt\_aics\_write\_cb) (struct bt\_aics \*inst, int err) |
| --- |

`#include <[aics.h](aics_8h.md)>`

Callback function for writes.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |

## Function Documentation

## [◆ ](#gac46268949fa7cbbb827d149a3a904daa)bt\_aics\_activate()

| int bt\_aics\_activate | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Activates a Audio Input Control Service instance.

Audio Input Control Services are activated by default, but this will allow the server reactivate a Audio Input Control Service instance after it has been deactivated with [bt\_aics\_deactivate](#ga4be4c4e3c74aa55fbf599157aa1c2098).

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga759712886cd3c4c025ea360dcb663c59)bt\_aics\_automatic\_gain\_set()

| int bt\_aics\_automatic\_gain\_set | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Set the input gain to automatic.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#gabd6bdcdad0dd5a4c509f9e7cabb3e601)bt\_aics\_client\_cb\_register()

| void bt\_aics\_client\_cb\_register | ( | struct bt\_aics \* | *inst*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_aics\_cb](structbt__aics__cb.md) \* | *cb* ) |

`#include <[aics.h](aics_8h.md)>`

Registers the callbacks for the Audio Input Control Service client.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | cb | Pointer to the callback structure. |

## [◆ ](#ga0e088e26cf73f1f3b918660d4acdebb9)bt\_aics\_client\_conn\_get()

| int bt\_aics\_client\_conn\_get | ( | const struct bt\_aics \* | *aics*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \*\* | *conn* ) |

`#include <[aics.h](aics_8h.md)>`

Get the connection pointer of a client instance.

Get the Bluetooth connection pointer of a Audio Input Control Service client instance.

Parameters
:   | aics | Audio Input Control Service client instance pointer. |
    | --- | --- |
    | conn | Connection pointer. |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga913838aa0d5bff239c2faef4d8a8b36b)bt\_aics\_client\_free\_instance\_get()

| struct bt\_aics \* bt\_aics\_client\_free\_instance\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Get a new Audio Input Control Service client instance.

Returns
:   Pointer to the instance, or NULL if no free instances are left.

## [◆ ](#ga4be4c4e3c74aa55fbf599157aa1c2098)bt\_aics\_deactivate()

| int bt\_aics\_deactivate | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Deactivates a Audio Input Control Service instance.

Audio Input Control Services are activated by default, but this will allow the server to deactivate an Audio Input Control Service.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaf0b659698aa6a6a79143d4f591f67e09)bt\_aics\_description\_get()

| int bt\_aics\_description\_get | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Read the Audio Input Control Service description.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga7de5ffd2eb61ca562b9773b37470ebd9)bt\_aics\_description\_set()

| int bt\_aics\_description\_set | ( | struct bt\_aics \* | *inst*, |
| --- | --- | --- | --- |
|  |  | const char \* | *description* ) |

`#include <[aics.h](aics_8h.md)>`

Set the Audio Input Control Service description.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | description | The description as an UTF-8 encoded string. |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga5a1ad98afe45da9ffbb7247671385d40)bt\_aics\_disable\_mute()

| int bt\_aics\_disable\_mute | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Disable mute in the Audio Input Control Service.

Calling [bt\_aics\_unmute()](#ga43396d2d4b3bd9cdd0c82275fafeadfc) or [bt\_aics\_mute()](#ga5345254eaf099560e609d97044b39a97) will enable mute again and set the mute state to either unmuted or muted.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, errno value on fail.

## [◆ ](#gad16d296462af2f61a893bda8d25cc9de)bt\_aics\_discover()

| int bt\_aics\_discover | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct bt\_aics \* | *inst*, |
|  |  | const struct [bt\_aics\_discover\_param](structbt__aics__discover__param.md) \* | *param* ) |

`#include <[aics.h](aics_8h.md)>`

Discover a Audio Input Control Service.

Attempts to discover a Audio Input Control Service on a server given the `param`.

Parameters
:   | conn | Connection to the peer with the Audio Input Control Service. |
    | --- | --- |
    | inst | The instance pointer. |
    | param | Pointer to the parameters. |

Returns
:   0 on success, errno on fail.

## [◆ ](#gab10ad3599f5b602cdf5504bc92508109)bt\_aics\_free\_instance\_get()

| struct bt\_aics \* bt\_aics\_free\_instance\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Get a free instance of Audio Input Control Service from the pool.

Returns
:   Audio Input Control Service instance in case of success or NULL in case of error.

## [◆ ](#ga20f3a178788ec6aef593034159793b94)bt\_aics\_gain\_set()

| int bt\_aics\_gain\_set | ( | struct bt\_aics \* | *inst*, |
| --- | --- | --- | --- |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *gain* ) |

`#include <[aics.h](aics_8h.md)>`

Set the input gain.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | gain | The gain to set (-128 to 127) in gain setting units (see [bt\_aics\_gain\_setting\_cb](#ga11da08c010f4aa849c2e3725dc5cbaeb)). |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga22869d8a62eb59bc4aad25946da8f9cf)bt\_aics\_gain\_set\_auto\_only()

| int bt\_aics\_gain\_set\_auto\_only | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Set automatic only gain mode in Audio Input Control Service.

Using this function and enabling automatic only gain disables setting the gain with bt\_aics\_gain\_set

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, errno value on fail.

## [◆ ](#ga0460e82d4277a2c4b14964799ad5f2b0)bt\_aics\_gain\_set\_manual\_only()

| int bt\_aics\_gain\_set\_manual\_only | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Set manual only gain mode in Audio Input Control Service.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, errno value on fail.

## [◆ ](#ga38d7131397d7762d3bd53e152a6c6130)bt\_aics\_gain\_setting\_get()

| int bt\_aics\_gain\_setting\_get | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Read the Audio Input Control Service gain settings.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga7ddb93125f6275fc7c99fbf448e24f0c)bt\_aics\_manual\_gain\_set()

| int bt\_aics\_manual\_gain\_set | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Set input gain to manual.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga5345254eaf099560e609d97044b39a97)bt\_aics\_mute()

| int bt\_aics\_mute | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Mute the Audio Input Control Service input.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga008ef5cebfcb9b4a3084f411fa81238e)bt\_aics\_register()

| int bt\_aics\_register | ( | struct bt\_aics \* | *aics*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_aics\_register\_param](structbt__aics__register__param.md) \* | *param* ) |

`#include <[aics.h](aics_8h.md)>`

Initialize the Audio Input Control Service instance.

Parameters
:   | aics | Audio Input Control Service instance. |
    | --- | --- |
    | param | Audio Input Control Service register parameters. |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga23bbc1393d21fe38f501813935b25b3d)bt\_aics\_state\_get()

| int bt\_aics\_state\_get | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Read the Audio Input Control Service input state.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#gade387c52d201ce10b39ef52157dae83d)bt\_aics\_status\_get()

| int bt\_aics\_status\_get | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Read the Audio Input Control Service input status.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga8b415343e7ecf399ecfd0dcaa49bd1ee)bt\_aics\_svc\_decl\_get()

| void \* bt\_aics\_svc\_decl\_get | ( | struct bt\_aics \* | *aics* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Get the service declaration attribute.

The first service attribute returned can be included in any other GATT service.

Parameters
:   | aics | Audio Input Control Service instance. |
    | --- | --- |

Returns
:   Pointer to the attributes of the service.

## [◆ ](#gaf57896e2096a5e96ec46a56cdf216159)bt\_aics\_type\_get()

| int bt\_aics\_type\_get | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Read the Audio Input Control Service input type.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga43396d2d4b3bd9cdd0c82275fafeadfc)bt\_aics\_unmute()

| int bt\_aics\_unmute | ( | struct bt\_aics \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[aics.h](aics_8h.md)>`

Unmute the Audio Input Control Service input.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
