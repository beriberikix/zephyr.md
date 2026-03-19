---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__bap__scan__delegator__cb.html
original_path: doxygen/html/structbt__bap__scan__delegator__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_scan\_delegator\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Struct to hold the Basic Audio Profile Scan Delegator callbacks.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [recv\_state\_updated](#a5d95631d95ae1085071c9b795eca1a8e) )(struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state) |
|  | Receive state updated. |
| int(\* | [pa\_sync\_req](#a0ea55963f92361f35e68eadcf10306b1) )(struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) past\_avail, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pa\_interval) |
|  | Periodic advertising sync request. |
| int(\* | [pa\_sync\_term\_req](#a5b918538cfe0edaa69155f891981eeae) )(struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state) |
|  | Periodic advertising sync termination request. |
| void(\* | [broadcast\_code](#a78d011c817e60725a0ef14c68bd655cd) )(struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) broadcast\_code[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)]) |
|  | Broadcast code received. |
| int(\* | [bis\_sync\_req](#a959112080deec0ab2dcc2c09a6958874) )(struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bis\_sync\_req[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]) |
|  | Broadcast Isochronous Stream synchronize request. |
| void(\* | [scanning\_state](#ae41d499d75123a1b70b778e8e95edcc3) )(struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_scanning) |
|  | Broadcast Assistant scanning state callback. |

## Detailed Description

Struct to hold the Basic Audio Profile Scan Delegator callbacks.

These can be registered for usage with [bt\_bap\_scan\_delegator\_register()](group__bt__bap.md#ga7632ab444dbf99387871f7d0c90b11ba "Register the Basic Audio Profile Scan Delegator and BASS.").

## Field Documentation

## [◆ ](#a959112080deec0ab2dcc2c09a6958874)bis\_sync\_req

| int(\* bt\_bap\_scan\_delegator\_cb::bis\_sync\_req) (struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bis\_sync\_req[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]) |
| --- |

Broadcast Isochronous Stream synchronize request.

Request from Broadcast Assistant device to modify the Broadcast Isochronous Stream states. The request shall be fulfilled with accordance to the `bis_sync_req` within reasonable time. The Broadcast Assistant may also request fewer, or none, indexes to be synchronized.

Parameters
:   | [in] | conn | Pointer to the connection of the Broadcast Assistant requesting the sync. |
    | --- | --- | --- |
    | [in] | recv\_state | Pointer to the receive state that is being requested for the sync. |
    | [in] | [bis\_sync\_req](#a959112080deec0ab2dcc2c09a6958874) | Array of bitfields of which BIS indexes that is requested to sync for each subgroup by the Broadcast Assistant. A value of 0 indicates a request to terminate the BIG sync. |

Returns
:   0 in case of accept, or other value to reject.

## [◆ ](#a78d011c817e60725a0ef14c68bd655cd)broadcast\_code

| void(\* bt\_bap\_scan\_delegator\_cb::broadcast\_code) (struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) broadcast\_code[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)]) |
| --- |

Broadcast code received.

Broadcast code received from a broadcast assistant

Parameters
:   | conn | Pointer to the connection providing the broadcast code. |
    | --- | --- |
    | recv\_state | Pointer to the receive state the broadcast code is being provided for. |
    | [broadcast\_code](#a78d011c817e60725a0ef14c68bd655cd) | The 16-octet broadcast code |

## [◆ ](#a0ea55963f92361f35e68eadcf10306b1)pa\_sync\_req

| int(\* bt\_bap\_scan\_delegator\_cb::pa\_sync\_req) (struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) past\_avail, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pa\_interval) |
| --- |

Periodic advertising sync request.

Request from peer device to synchronize with the periodic advertiser denoted by the `recv_state`. To notify the Broadcast Assistant about any pending sync

Parameters
:   | conn | Pointer to the connection requesting the periodic advertising sync. |
    | --- | --- |
    | recv\_state | Pointer to the receive state that is being requested for periodic advertising sync. |
    | past\_avail | True if periodic advertising sync transfer is available. |
    | pa\_interval | The periodic advertising interval. |

Returns
:   0 in case of accept, or other value to reject.

## [◆ ](#a5b918538cfe0edaa69155f891981eeae)pa\_sync\_term\_req

| int(\* bt\_bap\_scan\_delegator\_cb::pa\_sync\_term\_req) (struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state) |
| --- |

Periodic advertising sync termination request.

Request from peer device to terminate the periodic advertiser sync denoted by the `recv_state`.

Parameters
:   | conn | Pointer to the connection requesting the periodic advertising sync termination. |
    | --- | --- |
    | recv\_state | Pointer to the receive state that is being requested for periodic advertising sync. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a5d95631d95ae1085071c9b795eca1a8e)recv\_state\_updated

| void(\* bt\_bap\_scan\_delegator\_cb::recv\_state\_updated) (struct bt\_conn \*conn, const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state) |
| --- |

Receive state updated.

Parameters
:   | conn | Pointer to the connection to a remote device if the change was caused by it, otherwise NULL. |
    | --- | --- |
    | recv\_state | Pointer to the receive state that was updated. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ae41d499d75123a1b70b778e8e95edcc3)scanning\_state

| void(\* bt\_bap\_scan\_delegator\_cb::scanning\_state) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_scanning) |
| --- |

Broadcast Assistant scanning state callback.

Callback triggered when a Broadcast Assistant notifies the Scan Delegator about the assistants scanning state.

Parameters
:   | conn | Pointer to the connection that initiated the scan. |
    | --- | --- |
    | is\_scanning | true if scanning started, false if scanning stopped. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
