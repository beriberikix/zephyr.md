---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__le__ext__adv__cb.html
original_path: doxygen/html/structbt__le__ext__adv__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_ext\_adv\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [sent](#a85b8887c9ef443d18b71e9561e7dde60) )(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) \*info) |
|  | The advertising set has finished sending adv data. |
| void(\* | [connected](#a7aad0fbd8e531e70f661500c338d870e) )(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md) \*info) |
|  | The advertising set has accepted a new connection. |
| void(\* | [scanned](#a277dc3269741d40b644ae3c777198fab) )(struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md) \*info) |
|  | The advertising set has sent scan response data. |

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
    | addr | Information about the scanned event. |

## [◆ ](#a85b8887c9ef443d18b71e9561e7dde60)sent

| void(\* bt\_le\_ext\_adv\_cb::sent) (struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) \*info) |
| --- |

The advertising set has finished sending adv data.

This callback notifies the application that the advertising set has finished sending advertising data. The advertising set can either have been stopped by a timeout or because the specified number of advertising events has been reached.

Parameters
:   | adv | The advertising set object. |
    | --- | --- |
    | info | Information about the sent event. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_8h_source.md)

- [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
