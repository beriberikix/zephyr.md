---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__le__per__adv__sync__cb.html
original_path: doxygen/html/structbt__le__per__adv__sync__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [synced](#a815be4343ab589df433a551663c5f4a1) )(struct bt\_le\_per\_adv\_sync \*sync, struct [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md) \*info) |
|  | The periodic advertising has been successfully synced. |
| void(\* | [term](#acbd565a39918e5dfe7603a020e73daec) )(struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md) \*info) |
|  | The periodic advertising sync has been terminated. |
| void(\* | [recv](#a5576248e2eaef2afebe606e05e55f05f) )(struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md) \*info, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Periodic advertising data received. |
| void(\* | [state\_changed](#a656b4802f79d4a472c2367ade144d72e) )(struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md) \*info) |
|  | The periodic advertising sync state has changed. |
| void(\* | [biginfo](#aa44efa17bc28da1952785063a9baf6a9) )(struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_iso\_biginfo](structbt__iso__biginfo.md) \*biginfo) |
|  | BIGInfo advertising report received. |
| void(\* | [cte\_report\_cb](#ad2dc168696fbd22f7e3a089ac56f62d7) )(struct bt\_le\_per\_adv\_sync \*sync, struct [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md) const \*info) |
|  | Callback for IQ samples report collected when sampling CTE received with periodic advertising PDU. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a1977d27941063773c953a5f1dfa9ca76) |

## Field Documentation

## [◆ ](#aa44efa17bc28da1952785063a9baf6a9)biginfo

| void(\* bt\_le\_per\_adv\_sync\_cb::biginfo) (struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_iso\_biginfo](structbt__iso__biginfo.md) \*biginfo) |
| --- |

BIGInfo advertising report received.

This callback notifies the application of a BIGInfo advertising report. This is received if the advertiser is broadcasting isochronous streams in a BIG. See [iso.h](iso_8h.md "Bluetooth ISO handling.") for more information.

Parameters
:   | sync | The advertising set object. |
    | --- | --- |
    | [biginfo](#aa44efa17bc28da1952785063a9baf6a9) | The BIGInfo report. |

## [◆ ](#ad2dc168696fbd22f7e3a089ac56f62d7)cte\_report\_cb

| void(\* bt\_le\_per\_adv\_sync\_cb::cte\_report\_cb) (struct bt\_le\_per\_adv\_sync \*sync, struct [bt\_df\_per\_adv\_sync\_iq\_samples\_report](structbt__df__per__adv__sync__iq__samples__report.md) const \*info) |
| --- |

Callback for IQ samples report collected when sampling CTE received with periodic advertising PDU.

Parameters
:   | sync | The periodic advertising sync object. |
    | --- | --- |
    | info | Information about the sync event. |

## [◆ ](#a1977d27941063773c953a5f1dfa9ca76)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_le\_per\_adv\_sync\_cb::node |
| --- |

## [◆ ](#a5576248e2eaef2afebe606e05e55f05f)recv

| void(\* bt\_le\_per\_adv\_sync\_cb::recv) (struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md) \*info, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

Periodic advertising data received.

This callback notifies the application of an periodic advertising report.

Parameters
:   | sync | The advertising set object. |
    | --- | --- |
    | info | Information about the periodic advertising event. |
    | buf | Buffer containing the periodic advertising data. NULL if the controller failed to receive a subevent indication. Only happens if `CONFIG_BT_PER_ADV_SYNC_RSP` is enabled. |

## [◆ ](#a656b4802f79d4a472c2367ade144d72e)state\_changed

| void(\* bt\_le\_per\_adv\_sync\_cb::state\_changed) (struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md) \*info) |
| --- |

The periodic advertising sync state has changed.

This callback notifies the application about changes to the sync state. Initialize sync and termination is handled by their individual callbacks, and won't be notified here.

Parameters
:   | sync | The periodic advertising sync object. |
    | --- | --- |
    | info | Information about the state change. |

## [◆ ](#a815be4343ab589df433a551663c5f4a1)synced

| void(\* bt\_le\_per\_adv\_sync\_cb::synced) (struct bt\_le\_per\_adv\_sync \*sync, struct [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md) \*info) |
| --- |

The periodic advertising has been successfully synced.

This callback notifies the application that the periodic advertising set has been successfully synced, and will now start to receive periodic advertising reports.

Parameters
:   | sync | The periodic advertising sync object. |
    | --- | --- |
    | info | Information about the sync event. |

## [◆ ](#acbd565a39918e5dfe7603a020e73daec)term

| void(\* bt\_le\_per\_adv\_sync\_cb::term) (struct bt\_le\_per\_adv\_sync \*sync, const struct [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md) \*info) |
| --- |

The periodic advertising sync has been terminated.

This callback notifies the application that the periodic advertising sync has been terminated, either by local request, remote request or because due to missing data, e.g. by being out of range or sync.

Parameters
:   | sync | The periodic advertising sync object. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
