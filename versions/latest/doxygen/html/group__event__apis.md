---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__event__apis.html
original_path: doxygen/html/group__event__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Event APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_event](structk__event.md) |
|  | Event Structure. [More...](structk__event.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_EVENT\_DEFINE](#ga093449cc6686d3235944f3faad284893)(name) |
|  | Statically define and initialize an event object. |

| Functions | |
| --- | --- |
| void | [k\_event\_init](#gacf803590b39b095056f2b1c5090c4019) (struct [k\_event](structk__event.md) \*event) |
|  | Initialize an event object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_post](#gac88d17410a71642a903890e420d23d76) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events) |
|  | Post one or more events to an event object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_set](#gac22e9d768d003246e68b4b0b64e60f49) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events) |
|  | Set the events in an event object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_set\_masked](#ga29b3ec1022b12a8c34884da3559c5864) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events\_mask) |
|  | Set or clear the events in an event object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_clear](#gad6bfd7bfd0587bc70d3aa0b988010376) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events) |
|  | Clear the events in an event object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_wait](#ga0f83f5f034e13bab65149fb90b87a753) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reset, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for any of the specified events. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_wait\_all](#gaddd60a99de5ac3d84f643c9433b744c1) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reset, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for all of the specified events. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_test](#ga81e66be0959e8cb0414d9772056a6264) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events\_mask) |
|  | Test the events currently tracked in the event object. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga093449cc6686d3235944f3faad284893)K\_EVENT\_DEFINE

| #define K\_EVENT\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([k\_event](structk__event.md), name) = \

Z\_EVENT\_INITIALIZER(name);

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[k\_event](structk__event.md)

Event Structure.

**Definition** kernel.h:2207

Statically define and initialize an event object.

The event can be accessed outside the module where it is defined using:

extern struct [k\_event](structk__event.md) <name>;

Parameters
:   | name | Name of the event object. |
    | --- | --- |

## Function Documentation

## [◆ ](#gad6bfd7bfd0587bc70d3aa0b988010376)k\_event\_clear()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_event\_clear | ( | struct [k\_event](structk__event.md) \* | *event*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *events* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Clear the events in an event object.

This routine clears (resets) the specified events stored in an event object.

Parameters
:   | event | Address of the event object |
    | --- | --- |
    | events | Set of events to clear in *event* |

Return values
:   | Previous | value of the events in *event* |
    | --- | --- |

## [◆ ](#gacf803590b39b095056f2b1c5090c4019)k\_event\_init()

| void k\_event\_init | ( | struct [k\_event](structk__event.md) \* | *event* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Initialize an event object.

This routine initializes an event object, prior to its first use.

Parameters
:   | event | Address of the event object. |
    | --- | --- |

## [◆ ](#gac88d17410a71642a903890e420d23d76)k\_event\_post()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_event\_post | ( | struct [k\_event](structk__event.md) \* | *event*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *events* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Post one or more events to an event object.

This routine posts one or more events to an event object. All tasks waiting on the event object *event* whose waiting conditions become met by this posting immediately unpend.

Posting differs from setting in that posted events are merged together with the current set of events tracked by the event object.

Parameters
:   | event | Address of the event object |
    | --- | --- |
    | events | Set of events to post to *event* |

Return values
:   | Previous | value of the events in *event* |
    | --- | --- |

## [◆ ](#gac22e9d768d003246e68b4b0b64e60f49)k\_event\_set()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_event\_set | ( | struct [k\_event](structk__event.md) \* | *event*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *events* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Set the events in an event object.

This routine sets the events stored in event object to the specified value. All tasks waiting on the event object *event* whose waiting conditions become met by this immediately unpend.

Setting differs from posting in that set events replace the current set of events tracked by the event object.

Parameters
:   | event | Address of the event object |
    | --- | --- |
    | events | Set of events to set in *event* |

Return values
:   | Previous | value of the events in *event* |
    | --- | --- |

## [◆ ](#ga29b3ec1022b12a8c34884da3559c5864)k\_event\_set\_masked()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_event\_set\_masked | ( | struct [k\_event](structk__event.md) \* | *event*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *events*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *events\_mask* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Set or clear the events in an event object.

This routine sets the events stored in event object to the specified value. All tasks waiting on the event object *event* whose waiting conditions become met by this immediately unpend. Unlike [k\_event\_set](#gac22e9d768d003246e68b4b0b64e60f49), this routine allows specific event bits to be set and cleared as determined by the mask.

Parameters
:   | event | Address of the event object |
    | --- | --- |
    | events | Set of events to set/clear in *event* |
    | events\_mask | Mask to be applied to *events* |

Return values
:   | Previous | value of the events in *events\_mask* |
    | --- | --- |

## [◆ ](#ga81e66be0959e8cb0414d9772056a6264)k\_event\_test()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_event\_test | ( | struct [k\_event](structk__event.md) \* | *event*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *events\_mask* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Test the events currently tracked in the event object.

Parameters
:   | event | Address of the event object |
    | --- | --- |
    | events\_mask | Set of desired events to test |

Return values
:   | Current | value of events in *events\_mask* |
    | --- | --- |

## [◆ ](#ga0f83f5f034e13bab65149fb90b87a753)k\_event\_wait()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_event\_wait | ( | struct [k\_event](structk__event.md) \* | *event*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *events*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *reset*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Wait for any of the specified events.

This routine waits on event object *event* until any of the specified events have been delivered to the event object, or the maximum wait time *timeout* has expired. A thread may wait on up to 32 distinctly numbered events that are expressed as bits in a single 32-bit word.

Note
:   The caller must be careful when resetting if there are multiple threads waiting for the event object *event*.

Parameters
:   | event | Address of the event object |
    | --- | --- |
    | events | Set of desired events on which to wait |
    | reset | If true, clear the set of events tracked by the event object before waiting. If false, do not clear the events. |
    | timeout | Waiting period for the desired set of events or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | set | of matching events upon success |
    | --- | --- |
    | 0 | if matching events were not received within the specified time |

## [◆ ](#gaddd60a99de5ac3d84f643c9433b744c1)k\_event\_wait\_all()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_event\_wait\_all | ( | struct [k\_event](structk__event.md) \* | *event*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *events*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *reset*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Wait for all of the specified events.

This routine waits on event object *event* until all of the specified events have been delivered to the event object, or the maximum wait time *timeout* has expired. A thread may wait on up to 32 distinctly numbered events that are expressed as bits in a single 32-bit word.

Note
:   The caller must be careful when resetting if there are multiple threads waiting for the event object *event*.

Parameters
:   | event | Address of the event object |
    | --- | --- |
    | events | Set of desired events on which to wait |
    | reset | If true, clear the set of events tracked by the event object before waiting. If false, do not clear the events. |
    | timeout | Waiting period for the desired set of events or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | set | of matching events upon success |
    | --- | --- |
    | 0 | if matching events were not received within the specified time |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
