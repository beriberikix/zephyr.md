---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__conn__auth__cb.html
original_path: doxygen/html/structbt__conn__auth__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_auth\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Authenticated pairing callback structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff)(\* | [pairing\_accept](#a92391a172e158a42966f410d732424a7) )(struct bt\_conn \*conn, const struct [bt\_conn\_pairing\_feat](structbt__conn__pairing__feat.md) \*const feat) |
|  | Query to proceed incoming pairing or not. |
| void(\* | [passkey\_display](#a14074ca97fad6af4c58c43a00c503104) )(struct bt\_conn \*conn, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int passkey) |
|  | Display a passkey to the user. |
| void(\* | [passkey\_entry](#a10f9d22c89c95a6f3ffe0016f92445c0) )(struct bt\_conn \*conn) |
|  | Request the user to enter a passkey. |
| void(\* | [passkey\_confirm](#a2bb6c10666d111f675fd6de5ff51410a) )(struct bt\_conn \*conn, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int passkey) |
|  | Request the user to confirm a passkey. |
| void(\* | [oob\_data\_request](#aec9f6256607ea2cd1ce1b4cdb3052b42) )(struct bt\_conn \*conn, struct [bt\_conn\_oob\_info](structbt__conn__oob__info.md) \*info) |
|  | Request the user to provide Out of Band (OOB) data. |
| void(\* | [cancel](#af6eb01c252ba3e32ff8bf583aa6ca0a4) )(struct bt\_conn \*conn) |
|  | Cancel the ongoing user request. |
| void(\* | [pairing\_confirm](#af4f7d3ee570b3472ee79b014be01f76e) )(struct bt\_conn \*conn) |
|  | Request confirmation for an incoming pairing. |
| void(\* | [pincode\_entry](#ab6df1b1505dc22dd8dae0e946546c8bb) )(struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) highsec) |
|  | Request the user to enter a passkey. |

## Detailed Description

Authenticated pairing callback structure.

## Field Documentation

## [◆ ](#af6eb01c252ba3e32ff8bf583aa6ca0a4)cancel

| void(\* bt\_conn\_auth\_cb::cancel) (struct bt\_conn \*conn) |
| --- |

Cancel the ongoing user request.

This callback will be called to notify the application that it should cancel any previous user request (passkey display, entry or confirmation).

This may be set to NULL, but must always be provided whenever the passkey\_display, passkey\_entry passkey\_confirm or pairing\_confirm callback has been provided.

Parameters
:   | conn | Connection where pairing is currently active. |
    | --- | --- |

## [◆ ](#aec9f6256607ea2cd1ce1b4cdb3052b42)oob\_data\_request

| void(\* bt\_conn\_auth\_cb::oob\_data\_request) (struct bt\_conn \*conn, struct [bt\_conn\_oob\_info](structbt__conn__oob__info.md) \*info) |
| --- |

Request the user to provide Out of Band (OOB) data.

When called the user is expected to provide OOB data. The required data are indicated by the information structure.

For LE Secure Connections OOB pairing, the user should provide local OOB data, remote OOB data or both depending on their availability. Their value should be given to the stack using the [bt\_le\_oob\_set\_sc\_data()](group__bt__conn.md#gac365f9748ad0737f09142ee1de982503 "Set OOB data during LE Secure Connections (SC) pairing procedure.") API.

This callback must be set to non-NULL in order to support OOB pairing.

Parameters
:   | conn | Connection where pairing is currently active. |
    | --- | --- |
    | info | OOB pairing information. |

## [◆ ](#a92391a172e158a42966f410d732424a7)pairing\_accept

| enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff)(\* bt\_conn\_auth\_cb::pairing\_accept) (struct bt\_conn \*conn, const struct [bt\_conn\_pairing\_feat](structbt__conn__pairing__feat.md) \*const feat) |
| --- |

Query to proceed incoming pairing or not.

On any incoming pairing req/rsp this callback will be called for the application to decide whether to allow for the pairing to continue.

The pairing info received from the peer is passed to assist making the decision.

As this callback is synchronous the application should return a response value immediately. Otherwise it may affect the timing during pairing. Hence, this information should not be conveyed to the user to take action.

The remaining callbacks are not affected by this, but do notice that other callbacks can be called during the pairing. Eg. if pairing\_confirm is registered both will be called for Just-Works pairings.

This callback may be unregistered in which case pairing continues as if the Kconfig flag was not set.

This callback is not called for BR/EDR Secure Simple Pairing (SSP).

Parameters
:   | conn | Connection where pairing is initiated. |
    | --- | --- |
    | feat | Pairing req/resp info. |

## [◆ ](#af4f7d3ee570b3472ee79b014be01f76e)pairing\_confirm

| void(\* bt\_conn\_auth\_cb::pairing\_confirm) (struct bt\_conn \*conn) |
| --- |

Request confirmation for an incoming pairing.

This callback will be called to confirm an incoming pairing request where none of the other user callbacks is applicable.

If the user decides to accept the pairing the [bt\_conn\_auth\_pairing\_confirm()](group__bt__conn.md#ga3e15b9deb6787d3e415bbea35c9aa91d "Reply if incoming pairing was confirmed by user.") API should be called. If the user decides to reject the pairing the [bt\_conn\_auth\_cancel()](group__bt__conn.md#ga89e5fc4bcab3f5598d20a9cd8ace5f59 "Cancel ongoing authenticated pairing.") API should be called.

This callback may be set to NULL, which means that the local device lacks the ability to confirm a pairing request. If set to non-NULL the cancel callback must also be provided, since this is the only way the application can find out that it should stop requesting the user to confirm a pairing request.

Parameters
:   | conn | Connection where pairing is currently active. |
    | --- | --- |

## [◆ ](#a2bb6c10666d111f675fd6de5ff51410a)passkey\_confirm

| void(\* bt\_conn\_auth\_cb::passkey\_confirm) (struct bt\_conn \*conn, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int passkey) |
| --- |

Request the user to confirm a passkey.

When called the user is expected to confirm that the given passkey is also shown on the peer device.. The passkey will be in the range of 0 - 999999, and should be zero-padded to always be six digits (e.g. 37 would be shown as 000037).

Once the user has confirmed the passkey to match, the [bt\_conn\_auth\_passkey\_confirm()](group__bt__conn.md#gab8c3ecf2a3d68e54379917844a29d995 "Reply if passkey was confirmed to match by user.") API should be called. If the user concluded that the passkey doesn't match the [bt\_conn\_auth\_cancel()](group__bt__conn.md#ga89e5fc4bcab3f5598d20a9cd8ace5f59 "Cancel ongoing authenticated pairing.") API should be called.

This callback may be set to NULL, which means that the local device lacks the ability to confirm a passkey. If set to non-NULL the cancel callback must also be provided, since this is the only way the application can find out that it should stop requesting the user to confirm a passkey.

Parameters
:   | conn | Connection where pairing is currently active. |
    | --- | --- |
    | passkey | Passkey to be confirmed. |

## [◆ ](#a14074ca97fad6af4c58c43a00c503104)passkey\_display

| void(\* bt\_conn\_auth\_cb::passkey\_display) (struct bt\_conn \*conn, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int passkey) |
| --- |

Display a passkey to the user.

When called the application is expected to display the given passkey to the user, with the expectation that the passkey will then be entered on the peer device. The passkey will be in the range of 0 - 999999, and is expected to be padded with zeroes so that six digits are always shown. E.g. the value 37 should be shown as 000037.

This callback may be set to NULL, which means that the local device lacks the ability do display a passkey. If set to non-NULL the cancel callback must also be provided, since this is the only way the application can find out that it should stop displaying the passkey.

Parameters
:   | conn | Connection where pairing is currently active. |
    | --- | --- |
    | passkey | Passkey to show to the user. |

## [◆ ](#a10f9d22c89c95a6f3ffe0016f92445c0)passkey\_entry

| void(\* bt\_conn\_auth\_cb::passkey\_entry) (struct bt\_conn \*conn) |
| --- |

Request the user to enter a passkey.

When called the user is expected to enter a passkey. The passkey must be in the range of 0 - 999999, and should be expected to be zero-padded, as that's how the peer device will typically be showing it (e.g. 37 would be shown as 000037).

Once the user has entered the passkey its value should be given to the stack using the [bt\_conn\_auth\_passkey\_entry()](group__bt__conn.md#ga3906d8d3d192e8a6ad1bf6b7acc32ff0 "Reply with entered passkey.") API.

This callback may be set to NULL, which means that the local device lacks the ability to enter a passkey. If set to non-NULL the cancel callback must also be provided, since this is the only way the application can find out that it should stop requesting the user to enter a passkey.

Parameters
:   | conn | Connection where pairing is currently active. |
    | --- | --- |

## [◆ ](#ab6df1b1505dc22dd8dae0e946546c8bb)pincode\_entry

| void(\* bt\_conn\_auth\_cb::pincode\_entry) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) highsec) |
| --- |

Request the user to enter a passkey.

This callback will be called for a BR/EDR (Bluetooth Classic) connection where pairing is being performed. Once called the user is expected to enter a PIN code with a length between 1 and 16 digits. If the *highsec* parameter is set to true the PIN code must be 16 digits long.

Once entered, the PIN code should be given to the stack using the [bt\_conn\_auth\_pincode\_entry()](group__bt__conn.md#ga4002a1b092832807218afa8ad279ab98 "Reply with entered PIN code.") API.

This callback may be set to NULL, however in that case pairing over BR/EDR will not be possible. If provided, the cancel callback must be provided as well.

Parameters
:   | conn | Connection where pairing is currently active. |
    | --- | --- |
    | highsec | true if 16 digit PIN is required. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
