---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__ext__adv__cb.html
original_path: doxygen/html/structbt__le__ext__adv__cb.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_ext\_adv\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Callback struct to notify about advertiser activity.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [sent](#a85b8887c9ef443d18b71e9561e7dde60) )(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) \*info) |
|  | The advertising set was disabled after reaching limit. |
| void(\* | [connected](#a7aad0fbd8e531e70f661500c338d870e) )(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md) \*info) |
|  | The advertising set has accepted a new connection. |
| void(\* | [scanned](#a277dc3269741d40b644ae3c777198fab) )(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md) \*info) |
|  | The advertising set has sent scan response data. |

## Detailed Description

Callback struct to notify about advertiser activity.

The [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md "bt_le_ext_adv_cb") struct contains callback functions that are invoked in response to various events related to the advertising set. These events include:

- Completion of advertising data transmission
- Acceptance of a new connection
- Transmission of scan response data
- If privacy is enabled:
  - Expiration of the advertising set's validity
- If PAwR (Periodic Advertising with Response) is enabled:
  - Readiness to send one or more PAwR subevents, namely the LE Periodic Advertising Subevent Data Request event
  - Response of synced devices to a periodic advertising subevent indication has been received, namely the LE Periodic Advertising Response Report event

Note
:   Must point to valid memory during the lifetime of the advertising set.
:   Used in [bt\_le\_ext\_adv\_create](group__bt__gap.md#gad02b855dd7a26e3910b247fa73f19297 "bt_le_ext_adv_create").

## Field Documentation

## [◆ ](#a7aad0fbd8e531e70f661500c338d870e)connected

| void(\* bt\_le\_ext\_adv\_cb::connected) (struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md) \*info) |
| --- |

The advertising set has accepted a new connection.

This callback notifies the application that the advertising set has accepted a new connection.

Parameters
:   | adv | The advertising set object. |
    | --- | --- |
    | info | Information about the connected event. |

## [◆ ](#a277dc3269741d40b644ae3c777198fab)scanned

| void(\* bt\_le\_ext\_adv\_cb::scanned) (struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md) \*info) |
| --- |

The advertising set has sent scan response data.

This callback notifies the application that the advertising set has has received a Scan Request packet, and has sent a Scan Response packet.

Parameters
:   | adv | The advertising set object. |
    | --- | --- |
    | info | Information about the scanned event, namely the address. |

## [◆ ](#a85b8887c9ef443d18b71e9561e7dde60)sent

| void(\* bt\_le\_ext\_adv\_cb::sent) (struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) \*info) |
| --- |

The advertising set was disabled after reaching limit.

This callback is invoked when the limit set in [bt\_le\_ext\_adv\_start\_param::timeout](structbt__le__ext__adv__start__param.md#a80bb1ef4316dd75ea1268241333f4346 "bt_le_ext_adv_start_param::timeout") or [bt\_le\_ext\_adv\_start\_param::num\_events](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f "bt_le_ext_adv_start_param::num_events") is reached.

Parameters
:   | adv | The advertising set object. |
    | --- | --- |
    | info | Information about the sent event. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
