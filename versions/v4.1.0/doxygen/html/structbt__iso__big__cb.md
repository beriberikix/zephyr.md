---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__iso__big__cb.html
original_path: doxygen/html/structbt__iso__big__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_big\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

Struct to hold the Broadcast Isochronous Group callbacks.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [started](#ac84e00545dbb330311482eb5abd4a78b) )(struct bt\_iso\_big \*big) |
|  | The BIG has started and all of the streams are ready for data. |
| void(\* | [stopped](#a43d6ee745f7852460f843ced33c777c2) )(struct bt\_iso\_big \*big, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | The BIG has stopped and none of the streams are ready for data. |

## Detailed Description

Struct to hold the Broadcast Isochronous Group callbacks.

These can be registered for usage with [bt\_iso\_big\_register\_cb()](group__bt__iso.md#ga8a01a56e4a4555ed65a67065facfca76 "Registers callbacks for Broadcast Sources.").

## Field Documentation

## [◆ ](#ac84e00545dbb330311482eb5abd4a78b)started

| void(\* bt\_iso\_big\_cb::started) (struct bt\_iso\_big \*big) |
| --- |

The BIG has started and all of the streams are ready for data.

Parameters
:   | big | The started BIG |
    | --- | --- |

## [◆ ](#a43d6ee745f7852460f843ced33c777c2)stopped

| void(\* bt\_iso\_big\_cb::stopped) (struct bt\_iso\_big \*big, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

The BIG has stopped and none of the streams are ready for data.

Parameters
:   | big | The stopped BIG |
    | --- | --- |
    | reason | The reason why the BIG stopped (see the BT\_HCI\_ERR\_\* values) |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_big\_cb](structbt__iso__big__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
