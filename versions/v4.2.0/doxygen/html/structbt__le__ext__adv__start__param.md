---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__ext__adv__start__param.html
original_path: doxygen/html/structbt__le__ext__adv__start__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_ext\_adv\_start\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Parameters for starting an extended advertising session.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout](#a80bb1ef4316dd75ea1268241333f4346) |
|  | Maximum advertising set duration (N \* 10 ms). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_events](#ab45ae0bfdb144071efcc64c30648388f) |
|  | Maximum number of extended advertising events to be sent. |

## Detailed Description

Parameters for starting an extended advertising session.

This struct provides the parameters to control the behavior of an extended advertising session, including the timeout and the number of advertising events to send. The timeout is specified in units of 10 ms, and the number of events determines how many times the advertising will be sent before stopping. If either the timeout or number of events is reached, the advertising session will be stopped, and the application will be notified via the advertiser sent callback. If both parameters are provided, the advertising session will stop when either limit is reached.

Note
:   Used in [bt\_le\_ext\_adv\_start](group__bt__gap.md#gaf0f436c55482d9429f674303ae3aa815 "bt_le_ext_adv_start") function.

## Field Documentation

## [◆ ](#ab45ae0bfdb144071efcc64c30648388f)num\_events

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_ext\_adv\_start\_param::num\_events |
| --- |

Maximum number of extended advertising events to be sent.

The advertiser can be automatically disabled once the whole advertisement (i.e. extended advertising event) has been sent a certain number of times. The number of advertising PDUs sent may be higher and is not relevant.

Set to zero for no limit.

When the advertising set is automatically disabled because of this limit, [bt\_le\_ext\_adv\_cb::sent](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60 "bt_le_ext_adv_cb::sent") will be called.

For background information, see parameter "Max\_Extended\_Advertising\_Events" in Bluetooth Core Specification Version 6.0 Vol. 4 Part E, Section 7.8.56.

## [◆ ](#a80bb1ef4316dd75ea1268241333f4346)timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_ext\_adv\_start\_param::timeout |
| --- |

Maximum advertising set duration (N \* 10 ms).

The advertising set can be automatically disabled after a certain amount of time has passed since it first appeared on air.

Set to zero for no limit. Set in units of 10 ms.

When the advertising set is automatically disabled because of this limit, [bt\_le\_ext\_adv\_cb::sent](structbt__le__ext__adv__cb.md#a85b8887c9ef443d18b71e9561e7dde60 "bt_le_ext_adv_cb::sent") will be called.

When using high duty cycle directed connectable advertising then this parameters must be set to a non-zero value less than or equal to the maximum of [BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT](group__bt__gap__defines.md#gabe483d4dd601b11ac3eea570c962b1ec "BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT").

If privacy `CONFIG_BT_PRIVACY` is enabled then the timeout must be less than `CONFIG_BT_RPA_TIMEOUT`.

For background information, see parameter "Duration" in Bluetooth Core Specification Version 6.0 Vol. 4 Part E, Section 7.8.56.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
