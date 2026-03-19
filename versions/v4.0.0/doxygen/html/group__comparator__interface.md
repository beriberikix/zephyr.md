---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__comparator__interface.html
original_path: doxygen/html/group__comparator__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Comparator Interface

[Device Driver APIs](group__io__interfaces.md)

Comparator Interface.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef void(\* | [comparator\_callback\_t](#ga409308b8ba2efdca4a6ec4bdc4d3bc31)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | Comparator callback template. |

| Enumerations | |
| --- | --- |
| enum | [comparator\_trigger](#gab02743771baf02ee0105aa1303931674) { [COMPARATOR\_TRIGGER\_NONE](#ggab02743771baf02ee0105aa1303931674aef8abb95e06470906323eb67a84274ab) = 0 , [COMPARATOR\_TRIGGER\_RISING\_EDGE](#ggab02743771baf02ee0105aa1303931674a2bd8d1afb67a68a0bbc6737d434d6b89) , [COMPARATOR\_TRIGGER\_FALLING\_EDGE](#ggab02743771baf02ee0105aa1303931674a762c9ea031595a909d2b70128adf9734) , [COMPARATOR\_TRIGGER\_BOTH\_EDGES](#ggab02743771baf02ee0105aa1303931674a65cb9e6aa70639b15d0ca3cf16777f97) } |
|  | Comparator trigger enumerations. [More...](#gab02743771baf02ee0105aa1303931674) |

| Functions | |
| --- | --- |
| int | [comparator\_get\_output](#ga89ea48c5d4a9d8c8ec44ee4c987309f3) (const struct [device](structdevice.md) \*dev) |
|  | Get comparator's output state. |
| int | [comparator\_set\_trigger](#ga964fab6458e020d8717ee7c47a84c1d0) (const struct [device](structdevice.md) \*dev, enum [comparator\_trigger](#gab02743771baf02ee0105aa1303931674) trigger) |
|  | Set comparator's trigger. |
| static int | [comparator\_set\_trigger\_callback](#ga1c9dc5dd46f5bb62b3cf4e2cfcd42509) (const struct [device](structdevice.md) \*dev, [comparator\_callback\_t](#ga409308b8ba2efdca4a6ec4bdc4d3bc31) callback, void \*user\_data) |
|  | Set comparator's trigger callback. |
| int | [comparator\_trigger\_is\_pending](#ga28aa27594c7c3cf5cd7306d47ebf53f9) (const struct [device](structdevice.md) \*dev) |
|  | Check if comparator's trigger is pending and clear it. |

## Detailed Description

Comparator Interface.

Since
:   4.0

Version
:   0.1.0

## Typedef Documentation

## [◆ ](#ga409308b8ba2efdca4a6ec4bdc4d3bc31)comparator\_callback\_t

| typedef void(\* comparator\_callback\_t) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
| --- |

`#include <[comparator.h](comparator_8h.md)>`

Comparator callback template.

## Enumeration Type Documentation

## [◆ ](#gab02743771baf02ee0105aa1303931674)comparator\_trigger

| enum [comparator\_trigger](#gab02743771baf02ee0105aa1303931674) |
| --- |

`#include <[comparator.h](comparator_8h.md)>`

Comparator trigger enumerations.

| Enumerator | |
| --- | --- |
| COMPARATOR\_TRIGGER\_NONE | No trigger. |
| COMPARATOR\_TRIGGER\_RISING\_EDGE | Trigger on rising edge of comparator output. |
| COMPARATOR\_TRIGGER\_FALLING\_EDGE | Trigger on falling edge of comparator output. |
| COMPARATOR\_TRIGGER\_BOTH\_EDGES | Trigger on both edges of comparator output. |

## Function Documentation

## [◆ ](#ga89ea48c5d4a9d8c8ec44ee4c987309f3)comparator\_get\_output()

| int comparator\_get\_output | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[comparator.h](comparator_8h.md)>`

Get comparator's output state.

Parameters
:   | dev | Comparator device |
    | --- | --- |

Return values
:   | 1 | Output state is high |
    | --- | --- |
    | 0 | Output state is low |
    | -errno | code Failure |

## [◆ ](#ga964fab6458e020d8717ee7c47a84c1d0)comparator\_set\_trigger()

| int comparator\_set\_trigger | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [comparator\_trigger](#gab02743771baf02ee0105aa1303931674) | *trigger* ) |

`#include <[comparator.h](comparator_8h.md)>`

Set comparator's trigger.

Parameters
:   | dev | Comparator device |
    | --- | --- |
    | trigger | Trigger for signal and callback |

Return values
:   | 0 | Successful |
    | --- | --- |
    | -errno | code Failure |

## [◆ ](#ga1c9dc5dd46f5bb62b3cf4e2cfcd42509)comparator\_set\_trigger\_callback()

| | int comparator\_set\_trigger\_callback | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [comparator\_callback\_t](#ga409308b8ba2efdca4a6ec4bdc4d3bc31) | *callback*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[comparator.h](comparator_8h.md)>`

Set comparator's trigger callback.

Parameters
:   | dev | Comparator device |
    | --- | --- |
    | callback | Trigger callback |
    | user\_data | User data passed to callback |

Return values
:   | 0 | Successful |
    | --- | --- |
    | -errno | code Failure |

Note
:   Set callback to NULL to disable callback
:   Callback is called immediately if trigger is pending

## [◆ ](#ga28aa27594c7c3cf5cd7306d47ebf53f9)comparator\_trigger\_is\_pending()

| int comparator\_trigger\_is\_pending | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[comparator.h](comparator_8h.md)>`

Check if comparator's trigger is pending and clear it.

Parameters
:   | dev | Comparator device |
    | --- | --- |

Return values
:   | 1 | Trigger was pending |
    | --- | --- |
    | 0 | Trigger was cleared |
    | -errno | code Failure |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
