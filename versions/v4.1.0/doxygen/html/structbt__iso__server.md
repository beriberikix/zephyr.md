---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__iso__server.html
original_path: doxygen/html/structbt__iso__server.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_server Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Server structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) | [sec\_level](#a43b53fd63d4deaa1c5599499eec29c99) |
|  | Required minimum security level. |
| int(\* | [accept](#ae67a000ae524cba53b6bda503568ba38) )(const struct [bt\_iso\_accept\_info](structbt__iso__accept__info.md) \*info, struct [bt\_iso\_chan](structbt__iso__chan.md) \*\*chan) |
|  | Server accept callback. |

## Detailed Description

ISO Server structure.

## Field Documentation

## [◆ ](#ae67a000ae524cba53b6bda503568ba38)accept

| int(\* bt\_iso\_server::accept) (const struct [bt\_iso\_accept\_info](structbt__iso__accept__info.md) \*info, struct [bt\_iso\_chan](structbt__iso__chan.md) \*\*chan) |
| --- |

Server accept callback.

This callback is called whenever a new incoming connection requires authorization.

Parameters
:   | info | The ISO accept information structure |
    | --- | --- |
    | chan | Pointer to receive the allocated channel |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a43b53fd63d4deaa1c5599499eec29c99)sec\_level

| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) bt\_iso\_server::sec\_level |
| --- |

Required minimum security level.

Only available when `CONFIG_BT_SMP` is enabled.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_server](structbt__iso__server.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
