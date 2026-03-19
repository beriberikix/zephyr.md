---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__mesh__heartbeat.html
original_path: doxygen/html/group__bt__mesh__heartbeat.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Heartbeat

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Heartbeat.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md) |
|  | Heartbeat Publication parameters. [More...](structbt__mesh__hb__pub.md#details) |
| struct | [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) |
|  | Heartbeat Subscription parameters. [More...](structbt__mesh__hb__sub.md#details) |
| struct | [bt\_mesh\_hb\_cb](structbt__mesh__hb__cb.md) |
|  | Heartbeat callback structure. [More...](structbt__mesh__hb__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_HB\_CB\_DEFINE](#ga517f009151a7eeaa898a853fd0d7a93a)(\_name) |
|  | Register a callback structure for Heartbeat events. |

| Functions | |
| --- | --- |
| void | [bt\_mesh\_hb\_pub\_get](#ga2e95d8f9d75f1bea13a9584d201fd713) (struct [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md) \*get) |
|  | Get the current Heartbeat publication parameters. |
| void | [bt\_mesh\_hb\_sub\_get](#ga3013c3da6cc1a34b0c98c56fba7e7877) (struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) \*get) |
|  | Get the current Heartbeat subscription parameters. |

## Detailed Description

Heartbeat.

## Macro Definition Documentation

## [◆ ](#ga517f009151a7eeaa898a853fd0d7a93a)BT\_MESH\_HB\_CB\_DEFINE

| #define BT\_MESH\_HB\_CB\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[heartbeat.h](heartbeat_8h.md)>`

**Value:**

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([bt\_mesh\_hb\_cb](structbt__mesh__hb__cb.md), \_name)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[bt\_mesh\_hb\_cb](structbt__mesh__hb__cb.md)

Heartbeat callback structure.

**Definition** heartbeat.h:79

Register a callback structure for Heartbeat events.

Registers a callback structure that will be called whenever Heartbeat events occur

Parameters
:   | \_name | Name of callback structure. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga2e95d8f9d75f1bea13a9584d201fd713)bt\_mesh\_hb\_pub\_get()

| void bt\_mesh\_hb\_pub\_get | ( | struct [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md) \* | *get* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[heartbeat.h](heartbeat_8h.md)>`

Get the current Heartbeat publication parameters.

Parameters
:   | get | Heartbeat publication parameters return buffer. |
    | --- | --- |

## [◆ ](#ga3013c3da6cc1a34b0c98c56fba7e7877)bt\_mesh\_hb\_sub\_get()

| void bt\_mesh\_hb\_sub\_get | ( | struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) \* | *get* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[heartbeat.h](heartbeat_8h.md)>`

Get the current Heartbeat subscription parameters.

Parameters
:   | get | Heartbeat subscription parameters return buffer. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
