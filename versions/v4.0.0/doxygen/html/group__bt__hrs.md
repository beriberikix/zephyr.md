---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__hrs.html
original_path: doxygen/html/group__bt__hrs.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Heart Rate Service (HRS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Heart Rate Service (HRS).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_hrs\_cb](structbt__hrs__cb.md) |
|  | Heart rate service callback structure. [More...](structbt__hrs__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_HRS\_CONTROL\_POINT\_RESET\_ENERGY\_EXPANDED\_REQ](#ga4ff20fff68b19602a8857d29f8dd822d)   0x01 |
|  | Server shall restart the accumulation of energy expended from zero. |

| Functions | |
| --- | --- |
| int | [bt\_hrs\_cb\_register](#ga4b250a12dc6e975589f21ca1391c5b38) (struct [bt\_hrs\_cb](structbt__hrs__cb.md) \*cb) |
|  | Heart rate service callback register. |
| int | [bt\_hrs\_cb\_unregister](#gad725bf460319ca796c166a5f91e38bb6) (struct [bt\_hrs\_cb](structbt__hrs__cb.md) \*cb) |
|  | Heart rate service callback unregister. |
| int | [bt\_hrs\_notify](#ga0e3d298d984e2504957ca655f142e45b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) heartrate) |
|  | Notify heart rate measurement. |

## Detailed Description

Heart Rate Service (HRS).

[Experimental] Users should note that the APIs can change as a part of ongoing development.

## Macro Definition Documentation

## [◆ ](#ga4ff20fff68b19602a8857d29f8dd822d)BT\_HRS\_CONTROL\_POINT\_RESET\_ENERGY\_EXPANDED\_REQ

| #define BT\_HRS\_CONTROL\_POINT\_RESET\_ENERGY\_EXPANDED\_REQ   0x01 |
| --- |

`#include <[hrs.h](hrs_8h.md)>`

Server shall restart the accumulation of energy expended from zero.

## Function Documentation

## [◆ ](#ga4b250a12dc6e975589f21ca1391c5b38)bt\_hrs\_cb\_register()

| int bt\_hrs\_cb\_register | ( | struct [bt\_hrs\_cb](structbt__hrs__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hrs.h](hrs_8h.md)>`

Heart rate service callback register.

This function will register callbacks that will be called in certain events related to Heart rate service.

Parameters
:   | cb | Pointer to callbacks structure. Must point to memory that remains valid until unregistered. |
    | --- | --- |

Returns
:   0 on success
:   -EINVAL in case `cb` is NULL

## [◆ ](#gad725bf460319ca796c166a5f91e38bb6)bt\_hrs\_cb\_unregister()

| int bt\_hrs\_cb\_unregister | ( | struct [bt\_hrs\_cb](structbt__hrs__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hrs.h](hrs_8h.md)>`

Heart rate service callback unregister.

This function will unregister callback from Heart rate service.

Parameters
:   | cb | Pointer to callbacks structure |
    | --- | --- |

Returns
:   0 on success
:   -EINVAL in case `cb` is NULL
:   -ENOENT in case the `cb` was not found in registered callbacks

## [◆ ](#ga0e3d298d984e2504957ca655f142e45b)bt\_hrs\_notify()

| int bt\_hrs\_notify | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *heartrate* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hrs.h](hrs_8h.md)>`

Notify heart rate measurement.

This will send a GATT notification to all current subscribers.

Parameters
:   | heartrate | The heartrate measurement in beats per minute. |
    | --- | --- |

Returns
:   Zero in case of success and error code in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
