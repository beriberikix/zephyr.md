---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__ias.html
original_path: doxygen/html/group__bt__ias.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Immediate Alert Service (IAS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Immediate Alert Service (IAS).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_ias\_cb](structbt__ias__cb.md) |
|  | Immediate Alert Service callback structure. [More...](structbt__ias__cb.md#details) |
| struct | [bt\_ias\_client\_cb](structbt__ias__client__cb.md) |

| Macros | |
| --- | --- |
| #define | [BT\_IAS\_CB\_DEFINE](#ga5dee0ec206e8ddbb9bc33c8df824fcb0)(\_name) |
|  | Register a callback structure for immediate alert events. |

| Enumerations | |
| --- | --- |
| enum | [bt\_ias\_alert\_lvl](#gabdaf2045e939bc71c060ee195494c9f0) { [BT\_IAS\_ALERT\_LVL\_NO\_ALERT](#ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997) , [BT\_IAS\_ALERT\_LVL\_MILD\_ALERT](#ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd) , [BT\_IAS\_ALERT\_LVL\_HIGH\_ALERT](#ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653) } |

| Functions | |
| --- | --- |
| int | [bt\_ias\_local\_alert\_stop](#gad810c9d74701dc48c12e4545bded95a4) (void) |
|  | Method for stopping alert locally. |
| int | [bt\_ias\_client\_alert\_write](#ga040ef37207ddca54edb9839c721ca2f2) (struct bt\_conn \*conn, enum [bt\_ias\_alert\_lvl](#gabdaf2045e939bc71c060ee195494c9f0)) |
|  | Set alert level. |
| int | [bt\_ias\_discover](#ga2628386523390e044e4a32fb2cf3e7b5) (struct bt\_conn \*conn) |
|  | Discover Immediate Alert Service. |
| int | [bt\_ias\_client\_cb\_register](#ga481a20cbe9b3f128f8737f75535d2bfe) (const struct [bt\_ias\_client\_cb](structbt__ias__client__cb.md) \*cb) |
|  | Register Immediate Alert Client callbacks. |

## Detailed Description

Immediate Alert Service (IAS).

[Experimental] Users should note that the APIs can change as a part of ongoing development.

## Macro Definition Documentation

## [◆ ](#ga5dee0ec206e8ddbb9bc33c8df824fcb0)BT\_IAS\_CB\_DEFINE

| #define BT\_IAS\_CB\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ias.h](ias_8h.md)>`

**Value:**

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([bt\_ias\_cb](structbt__ias__cb.md), \_CONCAT(bt\_ias\_cb\_, \_name))

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[bt\_ias\_cb](structbt__ias__cb.md)

Immediate Alert Service callback structure.

**Definition** ias.h:39

Register a callback structure for immediate alert events.

Parameters
:   | \_name | Name of callback structure. |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#gabdaf2045e939bc71c060ee195494c9f0)bt\_ias\_alert\_lvl

| enum [bt\_ias\_alert\_lvl](#gabdaf2045e939bc71c060ee195494c9f0) |
| --- |

`#include <[ias.h](ias_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_IAS\_ALERT\_LVL\_NO\_ALERT | No alerting should be done on device. |
| BT\_IAS\_ALERT\_LVL\_MILD\_ALERT | Device shall alert. |
| BT\_IAS\_ALERT\_LVL\_HIGH\_ALERT | Device should alert in strongest possible way. |

## Function Documentation

## [◆ ](#ga040ef37207ddca54edb9839c721ca2f2)bt\_ias\_client\_alert\_write()

| int bt\_ias\_client\_alert\_write | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum | *bt\_ias\_alert\_lvl* ) |

`#include <[ias.h](ias_8h.md)>`

Set alert level.

Parameters
:   | conn | Bluetooth connection object |
    | --- | --- |
    | [bt\_ias\_alert\_lvl](#gabdaf2045e939bc71c060ee195494c9f0) | Level of alert to write |

Returns
:   Zero in case of success and error code in case of error.

## [◆ ](#ga481a20cbe9b3f128f8737f75535d2bfe)bt\_ias\_client\_cb\_register()

| int bt\_ias\_client\_cb\_register | ( | const struct [bt\_ias\_client\_cb](structbt__ias__client__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ias.h](ias_8h.md)>`

Register Immediate Alert Client callbacks.

Parameters
:   | cb | The callback structure |
    | --- | --- |

Returns
:   Zero in case of success and error code in case of error.

## [◆ ](#ga2628386523390e044e4a32fb2cf3e7b5)bt\_ias\_discover()

| int bt\_ias\_discover | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ias.h](ias_8h.md)>`

Discover Immediate Alert Service.

Parameters
:   | conn | Bluetooth connection object |
    | --- | --- |

Returns
:   Zero in case of success and error code in case of error.

## [◆ ](#gad810c9d74701dc48c12e4545bded95a4)bt\_ias\_local\_alert\_stop()

| int bt\_ias\_local\_alert\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ias.h](ias_8h.md)>`

Method for stopping alert locally.

Returns
:   Zero in case of success and error code in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
