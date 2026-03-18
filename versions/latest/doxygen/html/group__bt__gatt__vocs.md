---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__gatt__vocs.html
original_path: doxygen/html/group__bt__gatt__vocs.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Volume Offset Control Service (VOCS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Volume Offset Control Service (VOCS).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_vocs\_register\_param](structbt__vocs__register__param.md) |
|  | Structure for registering a Volume Offset Control Service instance. [More...](structbt__vocs__register__param.md#details) |
| struct | [bt\_vocs\_discover\_param](structbt__vocs__discover__param.md) |
|  | Structure for discovering a Volume Offset Control Service instance. [More...](structbt__vocs__discover__param.md#details) |
| struct | [bt\_vocs\_cb](structbt__vocs__cb.md) |

| Macros | |
| --- | --- |
| #define | [BT\_VOCS\_ERR\_INVALID\_COUNTER](#ga17c81394b9b4d601768e72d8c360992f)   0x80 |
|  | Volume Offset Control Service Error codes. |
| #define | [BT\_VOCS\_ERR\_OP\_NOT\_SUPPORTED](#gadd01a04e3c4336a13a4760e2448131b1)   0x81 |
| #define | [BT\_VOCS\_ERR\_OUT\_OF\_RANGE](#ga2ecb7e0408bb1767c2d51c816f4b273d)   0x82 |
| #define | [BT\_VOCS\_MIN\_OFFSET](#ga64d4e32f9d92a58b3229b3aa2e8fcc4d)   -255 |
| #define | [BT\_VOCS\_MAX\_OFFSET](#ga800092562173fd37826b5537feaac3ae)   255 |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_vocs\_state\_cb](#gaa329fd8931add8fd4f6c59b48c91ef75)) (struct bt\_vocs \*inst, int err, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) offset) |
|  | Callback function for the offset state. |
| typedef void(\* | [bt\_vocs\_set\_offset\_cb](#ga2630344190f12f911bb2b01c4b95ded6)) (struct bt\_vocs \*inst, int err) |
|  | Callback function for setting offset. |
| typedef void(\* | [bt\_vocs\_location\_cb](#ga84983707e04eae75f18017072b647115)) (struct bt\_vocs \*inst, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) location) |
|  | Callback function for the location. |
| typedef void(\* | [bt\_vocs\_description\_cb](#gaa351c3ab631b16272e27cbb837d9e49c)) (struct bt\_vocs \*inst, int err, char \*description) |
|  | Callback function for the description. |
| typedef void(\* | [bt\_vocs\_discover\_cb](#gad50fd539190b5c64b5262d3830699365)) (struct bt\_vocs \*inst, int err) |
|  | Callback function for bt\_vocs\_discover. |

| Functions | |
| --- | --- |
| struct bt\_vocs \* | [bt\_vocs\_free\_instance\_get](#gadde50c3eb90ea7b7aa9b9c4b3672710f) (void) |
|  | Get a free service instance of Volume Offset Control Service from the pool. |
| void \* | [bt\_vocs\_svc\_decl\_get](#ga9f7ff4c0521686ded011758ddd8ea95e) (struct bt\_vocs \*vocs) |
|  | Get the service declaration attribute. |
| int | [bt\_vocs\_client\_conn\_get](#gafcf7ecea73c8c199b38c7291ce4a648f) (const struct bt\_vocs \*vocs, struct bt\_conn \*\*conn) |
|  | Get the connection pointer of a client instance. |
| int | [bt\_vocs\_register](#gac011ddd93bb3240148a789f1ee9ef7da) (struct bt\_vocs \*vocs, const struct [bt\_vocs\_register\_param](structbt__vocs__register__param.md) \*param) |
|  | Register the Volume Offset Control Service instance. |
| int | [bt\_vocs\_state\_get](#ga6c835234a5530bae3bb0f5bd03a0bdd7) (struct bt\_vocs \*inst) |
|  | Read the Volume Offset Control Service offset state. |
| int | [bt\_vocs\_state\_set](#ga28ea337e439b5872abab8f5b98719da4) (struct bt\_vocs \*inst, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) offset) |
|  | Set the Volume Offset Control Service offset state. |
| int | [bt\_vocs\_location\_get](#ga90ba394e6be138d6052b95d73ab2f409) (struct bt\_vocs \*inst) |
|  | Read the Volume Offset Control Service location. |
| int | [bt\_vocs\_location\_set](#ga02b036f060eee947c8924bbea846bc29) (struct bt\_vocs \*inst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) location) |
|  | Set the Volume Offset Control Service location. |
| int | [bt\_vocs\_description\_get](#gaac1c1292cae4c5845a376d2f4db3d661) (struct bt\_vocs \*inst) |
|  | Read the Volume Offset Control Service output description. |
| int | [bt\_vocs\_description\_set](#gac17cb7101233605834ec6b66d7417f91) (struct bt\_vocs \*inst, const char \*description) |
|  | Set the Volume Offset Control Service description. |
| void | [bt\_vocs\_client\_cb\_register](#gaace802556eca3d634a13dd8f2bf3c544) (struct bt\_vocs \*inst, struct [bt\_vocs\_cb](structbt__vocs__cb.md) \*cb) |
|  | Registers the callbacks for the Volume Offset Control Service client. |
| struct bt\_vocs \* | [bt\_vocs\_client\_free\_instance\_get](#ga6182120b1bece7f5851bb6295c81b562) (void) |
|  | Returns a pointer to a Volume Offset Control Service client instance. |
| int | [bt\_vocs\_discover](#ga45efa872e07ac8051379caf5aa8d0133) (struct bt\_conn \*conn, struct bt\_vocs \*inst, const struct [bt\_vocs\_discover\_param](structbt__vocs__discover__param.md) \*param) |
|  | Discover a Volume Offset Control Service. |

## Detailed Description

Volume Offset Control Service (VOCS).

The Volume Offset Control Service is a secondary service, and as such should not be used own its own, but rather in the context of another (primary) service.

This API implements both the server and client functionality. Note that the API abstracts away the change counter in the volume offset control state and will automatically handle any changes to that. If out of date, the client implementation will autonomously read the change counter value when executing a write request.

[Experimental] Users should note that the APIs can change as a part of ongoing development.

## Macro Definition Documentation

## [◆ ](#ga17c81394b9b4d601768e72d8c360992f)BT\_VOCS\_ERR\_INVALID\_COUNTER

| #define BT\_VOCS\_ERR\_INVALID\_COUNTER   0x80 |
| --- |

`#include <[vocs.h](vocs_8h.md)>`

Volume Offset Control Service Error codes.

## [◆ ](#gadd01a04e3c4336a13a4760e2448131b1)BT\_VOCS\_ERR\_OP\_NOT\_SUPPORTED

| #define BT\_VOCS\_ERR\_OP\_NOT\_SUPPORTED   0x81 |
| --- |

`#include <[vocs.h](vocs_8h.md)>`

## [◆ ](#ga2ecb7e0408bb1767c2d51c816f4b273d)BT\_VOCS\_ERR\_OUT\_OF\_RANGE

| #define BT\_VOCS\_ERR\_OUT\_OF\_RANGE   0x82 |
| --- |

`#include <[vocs.h](vocs_8h.md)>`

## [◆ ](#ga800092562173fd37826b5537feaac3ae)BT\_VOCS\_MAX\_OFFSET

| #define BT\_VOCS\_MAX\_OFFSET   255 |
| --- |

`#include <[vocs.h](vocs_8h.md)>`

## [◆ ](#ga64d4e32f9d92a58b3229b3aa2e8fcc4d)BT\_VOCS\_MIN\_OFFSET

| #define BT\_VOCS\_MIN\_OFFSET   -255 |
| --- |

`#include <[vocs.h](vocs_8h.md)>`

## Typedef Documentation

## [◆ ](#gaa351c3ab631b16272e27cbb837d9e49c)bt\_vocs\_description\_cb

| typedef void(\* bt\_vocs\_description\_cb) (struct bt\_vocs \*inst, int err, char \*description) |
| --- |

`#include <[vocs.h](vocs_8h.md)>`

Callback function for the description.

Called when the value is read, or if the value is changed by either the server or client.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. For notifications, this will always be 0. |
    | description | The description as an UTF-8 encoded string. |

## [◆ ](#gad50fd539190b5c64b5262d3830699365)bt\_vocs\_discover\_cb

| typedef void(\* bt\_vocs\_discover\_cb) (struct bt\_vocs \*inst, int err) |
| --- |

`#include <[vocs.h](vocs_8h.md)>`

Callback function for bt\_vocs\_discover.

This callback should be overwritten by the primary service that includes the Volume Control Offset Service client, and should thus not be set by the application.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. For notifications, this will always be 0. |

## [◆ ](#ga84983707e04eae75f18017072b647115)bt\_vocs\_location\_cb

| typedef void(\* bt\_vocs\_location\_cb) (struct bt\_vocs \*inst, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) location) |
| --- |

`#include <[vocs.h](vocs_8h.md)>`

Callback function for the location.

Called when the value is read, or if the value is changed by either the server or client.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. For notifications, this will always be 0. |
    | location | The location value. |

## [◆ ](#ga2630344190f12f911bb2b01c4b95ded6)bt\_vocs\_set\_offset\_cb

| typedef void(\* bt\_vocs\_set\_offset\_cb) (struct bt\_vocs \*inst, int err) |
| --- |

`#include <[vocs.h](vocs_8h.md)>`

Callback function for setting offset.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |

## [◆ ](#gaa329fd8931add8fd4f6c59b48c91ef75)bt\_vocs\_state\_cb

| typedef void(\* bt\_vocs\_state\_cb) (struct bt\_vocs \*inst, int err, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) offset) |
| --- |

`#include <[vocs.h](vocs_8h.md)>`

Callback function for the offset state.

Called when the value is read, or if the value is changed by either the server or client.

Parameters
:   | inst | The instance pointer. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. For notifications, this will always be 0. |
    | offset | The offset value. |

## Function Documentation

## [◆ ](#gaace802556eca3d634a13dd8f2bf3c544)bt\_vocs\_client\_cb\_register()

| void bt\_vocs\_client\_cb\_register | ( | struct bt\_vocs \* | *inst*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_vocs\_cb](structbt__vocs__cb.md) \* | *cb* ) |

`#include <[vocs.h](vocs_8h.md)>`

Registers the callbacks for the Volume Offset Control Service client.

Parameters
:   | inst | Pointer to the Volume Offset Control Service client instance. |
    | --- | --- |
    | cb | Pointer to the callback structure. |

## [◆ ](#gafcf7ecea73c8c199b38c7291ce4a648f)bt\_vocs\_client\_conn\_get()

| int bt\_vocs\_client\_conn\_get | ( | const struct bt\_vocs \* | *vocs*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \*\* | *conn* ) |

`#include <[vocs.h](vocs_8h.md)>`

Get the connection pointer of a client instance.

Get the Bluetooth connection pointer of a Audio Input Control Service client instance.

Parameters
:   | vocs | Audio Input Control Service client instance pointer. |
    | --- | --- |
    | conn | Connection pointer. |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga6182120b1bece7f5851bb6295c81b562)bt\_vocs\_client\_free\_instance\_get()

| struct bt\_vocs \* bt\_vocs\_client\_free\_instance\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vocs.h](vocs_8h.md)>`

Returns a pointer to a Volume Offset Control Service client instance.

Returns
:   Pointer to the instance, or NULL if no free instances are left.

## [◆ ](#gaac1c1292cae4c5845a376d2f4db3d661)bt\_vocs\_description\_get()

| int bt\_vocs\_description\_get | ( | struct bt\_vocs \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vocs.h](vocs_8h.md)>`

Read the Volume Offset Control Service output description.

The value is returned in the [bt\_vocs\_cb.description](structbt__vocs__cb.md#ac508b1e6dda00c607aa1cbe52423ec52) callback.

Parameters
:   | inst | Pointer to the Volume Offset Control Service instance. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#gac17cb7101233605834ec6b66d7417f91)bt\_vocs\_description\_set()

| int bt\_vocs\_description\_set | ( | struct bt\_vocs \* | *inst*, |
| --- | --- | --- | --- |
|  |  | const char \* | *description* ) |

`#include <[vocs.h](vocs_8h.md)>`

Set the Volume Offset Control Service description.

Parameters
:   | inst | Pointer to the Volume Offset Control Service instance. |
    | --- | --- |
    | description | The UTF-8 encoded string description to set. |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga45efa872e07ac8051379caf5aa8d0133)bt\_vocs\_discover()

| int bt\_vocs\_discover | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct bt\_vocs \* | *inst*, |
|  |  | const struct [bt\_vocs\_discover\_param](structbt__vocs__discover__param.md) \* | *param* ) |

`#include <[vocs.h](vocs_8h.md)>`

Discover a Volume Offset Control Service.

Attempts to discover a Volume Offset Control Service on a server given the `param`.

Parameters
:   | conn | Connection to the peer with the Volume Offset Control Service. |
    | --- | --- |
    | inst | Pointer to the Volume Offset Control Service client instance. |
    | param | Pointer to the parameters. |

Returns
:   0 on success, errno on fail.

## [◆ ](#gadde50c3eb90ea7b7aa9b9c4b3672710f)bt\_vocs\_free\_instance\_get()

| struct bt\_vocs \* bt\_vocs\_free\_instance\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vocs.h](vocs_8h.md)>`

Get a free service instance of Volume Offset Control Service from the pool.

Returns
:   Volume Offset Control Service instance in case of success or NULL in case of error.

## [◆ ](#ga90ba394e6be138d6052b95d73ab2f409)bt\_vocs\_location\_get()

| int bt\_vocs\_location\_get | ( | struct bt\_vocs \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vocs.h](vocs_8h.md)>`

Read the Volume Offset Control Service location.

The value is returned in the [bt\_vocs\_cb.location](structbt__vocs__cb.md#a50d1d429089456267b06d4450712b897) callback.

Parameters
:   | inst | Pointer to the Volume Offset Control Service instance. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga02b036f060eee947c8924bbea846bc29)bt\_vocs\_location\_set()

| int bt\_vocs\_location\_set | ( | struct bt\_vocs \* | *inst*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *location* ) |

`#include <[vocs.h](vocs_8h.md)>`

Set the Volume Offset Control Service location.

Parameters
:   | inst | Pointer to the Volume Offset Control Service instance. |
    | --- | --- |
    | location | The location to set. |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#gac011ddd93bb3240148a789f1ee9ef7da)bt\_vocs\_register()

| int bt\_vocs\_register | ( | struct bt\_vocs \* | *vocs*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_vocs\_register\_param](structbt__vocs__register__param.md) \* | *param* ) |

`#include <[vocs.h](vocs_8h.md)>`

Register the Volume Offset Control Service instance.

Parameters
:   | vocs | Volume Offset Control Service instance. |
    | --- | --- |
    | param | Volume Offset Control Service register parameters. |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga6c835234a5530bae3bb0f5bd03a0bdd7)bt\_vocs\_state\_get()

| int bt\_vocs\_state\_get | ( | struct bt\_vocs \* | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vocs.h](vocs_8h.md)>`

Read the Volume Offset Control Service offset state.

The value is returned in the [bt\_vocs\_cb.state](structbt__vocs__cb.md#ae633c1f6cd8aa03d89287e783179460e) callback.

Parameters
:   | inst | Pointer to the Volume Offset Control Service instance. |
    | --- | --- |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga28ea337e439b5872abab8f5b98719da4)bt\_vocs\_state\_set()

| int bt\_vocs\_state\_set | ( | struct bt\_vocs \* | *inst*, |
| --- | --- | --- | --- |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *offset* ) |

`#include <[vocs.h](vocs_8h.md)>`

Set the Volume Offset Control Service offset state.

Parameters
:   | inst | Pointer to the Volume Offset Control Service instance. |
    | --- | --- |
    | offset | The offset to set (-255 to 255). |

Returns
:   0 on success, GATT error value on fail.

## [◆ ](#ga9f7ff4c0521686ded011758ddd8ea95e)bt\_vocs\_svc\_decl\_get()

| void \* bt\_vocs\_svc\_decl\_get | ( | struct bt\_vocs \* | *vocs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vocs.h](vocs_8h.md)>`

Get the service declaration attribute.

The first service attribute returned can be included in any other GATT service.

Parameters
:   | vocs | Volume Offset Control Service instance. |
    | --- | --- |

Returns
:   Pointer to the attributes of the service.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
