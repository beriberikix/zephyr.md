---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__poll__apis.html
original_path: doxygen/html/group__poll__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Async polling APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_poll\_signal](structk__poll__signal.md) |
| struct | [k\_poll\_event](structk__poll__event.md) |
|  | Poll Event. [More...](structk__poll__event.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_POLL\_TYPE\_IGNORE](#gafd5d801eb9e9cf6097b2c08b4933998e)   0 |
| #define | [K\_POLL\_TYPE\_SIGNAL](#ga144d8eb34d85f6053e454410a10bf56a)   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SIGNAL) |
| #define | [K\_POLL\_TYPE\_SEM\_AVAILABLE](#ga0fd7605bdffd43dff7480a90a603ffde)   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SEM\_AVAILABLE) |
| #define | [K\_POLL\_TYPE\_DATA\_AVAILABLE](#ga58d656f73f031a39b8a936133fe5504f)   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE](#ga71734fee18c523cf70276260118afb91)   [K\_POLL\_TYPE\_DATA\_AVAILABLE](#ga58d656f73f031a39b8a936133fe5504f) |
| #define | [K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE](#gaa83509b54175fb6c98324422a928d5e1)   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE](#ga14e113201a3b3ad768c6a5ce917d1912)   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_STATE\_NOT\_READY](#ga522822c5e06a89b22ce4dcefd10c66aa)   0 |
| #define | [K\_POLL\_STATE\_SIGNALED](#ga478aae7fe4fb5c7b7c76ed216c22a7f1)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SIGNALED) |
| #define | [K\_POLL\_STATE\_SEM\_AVAILABLE](#gae9e3eefd5a29a538d22f53592578bb37)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SEM\_AVAILABLE) |
| #define | [K\_POLL\_STATE\_DATA\_AVAILABLE](#gac166d9919d591bace163c5211e7b41f4)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_STATE\_FIFO\_DATA\_AVAILABLE](#gabd5ac3341698534f39ded718079d6168)   [K\_POLL\_STATE\_DATA\_AVAILABLE](#gac166d9919d591bace163c5211e7b41f4) |
| #define | [K\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE](#gac236074cd43f59f28b803fe2c4a4f6f7)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE](#ga9028d6868ee964ca25931ed9170068dd)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_STATE\_CANCELLED](#gadaf4b4c8e13afb54114af72d133e1fdb)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_CANCELLED) |
| #define | [K\_POLL\_SIGNAL\_INITIALIZER](#ga6d6321e189afca73a276cd671ec531ae)(obj) |
| #define | [K\_POLL\_EVENT\_INITIALIZER](#ga8e3889f2bac281a6e65e31068e58047e)(\_event\_type, \_event\_mode, \_event\_obj) |
| #define | [K\_POLL\_EVENT\_STATIC\_INITIALIZER](#gada2366896d913dc916b3c28642648b63)(\_event\_type, \_event\_mode, \_event\_obj, event\_tag) |

| Enumerations | |
| --- | --- |
| enum | [k\_poll\_modes](#ga36d7978872a83191dd3cc16d62165add) { [K\_POLL\_MODE\_NOTIFY\_ONLY](#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681) = 0 , [K\_POLL\_NUM\_MODES](#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c) } |

| Functions | |
| --- | --- |
| void | [k\_poll\_event\_init](#gaa06bddd93a024fc5326d93187d80eb03) (struct [k\_poll\_event](structk__poll__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type, int mode, void \*obj) |
|  | Initialize one struct [k\_poll\_event](structk__poll__event.md "Poll Event.") instance. |
| int | [k\_poll](#gac550dc93662ce164fb22a5a91d6830db) (struct [k\_poll\_event](structk__poll__event.md) \*events, int num\_events, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for one or many of multiple poll events to occur. |
| void | [k\_poll\_signal\_init](#gaee3090c2a912b93b6a5855e3018c3551) (struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Initialize a poll signal object. |
| void | [k\_poll\_signal\_reset](#ga02d899d1455ae1f3f55ffe8f1ebd6994) (struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Reset a poll signal object's state to unsignaled. |
| void | [k\_poll\_signal\_check](#ga69dae11c7cb2c669caa411c3e7001311) (struct [k\_poll\_signal](structk__poll__signal.md) \*sig, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \*signaled, int \*result) |
|  | Fetch the signaled state and result value of a poll signal. |
| int | [k\_poll\_signal\_raise](#gad0bf3825f828ec3ca37481bf3cbd6723) (struct [k\_poll\_signal](structk__poll__signal.md) \*sig, int result) |
|  | Signal a poll signal object. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga8e3889f2bac281a6e65e31068e58047e)K\_POLL\_EVENT\_INITIALIZER

| #define K\_POLL\_EVENT\_INITIALIZER | ( |  | *\_event\_type*, |
| --- | --- | --- | --- |
|  |  |  | *\_event\_mode*, |
|  |  |  | *\_event\_obj* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

{ \

.poller = NULL, \

.type = \_event\_type, \

.state = [K\_POLL\_STATE\_NOT\_READY](#ga522822c5e06a89b22ce4dcefd10c66aa), \

.mode = \_event\_mode, \

.unused = 0, \

{ \

.typed\_##\_event\_type = \_event\_obj, \

}, \

}

[K\_POLL\_STATE\_NOT\_READY](#ga522822c5e06a89b22ce4dcefd10c66aa)

#define K\_POLL\_STATE\_NOT\_READY

**Definition** kernel.h:5758

## [◆ ](#gada2366896d913dc916b3c28642648b63)K\_POLL\_EVENT\_STATIC\_INITIALIZER

| #define K\_POLL\_EVENT\_STATIC\_INITIALIZER | ( |  | *\_event\_type*, |
| --- | --- | --- | --- |
|  |  |  | *\_event\_mode*, |
|  |  |  | *\_event\_obj*, |
|  |  |  | *event\_tag* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

{ \

.tag = event\_tag, \

.type = \_event\_type, \

.state = [K\_POLL\_STATE\_NOT\_READY](#ga522822c5e06a89b22ce4dcefd10c66aa), \

.mode = \_event\_mode, \

.unused = 0, \

{ \

.typed\_##\_event\_type = \_event\_obj, \

}, \

}

## [◆ ](#ga6d6321e189afca73a276cd671ec531ae)K\_POLL\_SIGNAL\_INITIALIZER

| #define K\_POLL\_SIGNAL\_INITIALIZER | ( |  | *obj* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

{ \

.poll\_events = [SYS\_DLIST\_STATIC\_INIT](group__doubly-linked-list__apis.md#ga3681d4600f9cbd9237ea9ce6f67e508d)(&obj.poll\_events), \

.signaled = 0, \

.result = 0, \

}

[SYS\_DLIST\_STATIC\_INIT](group__doubly-linked-list__apis.md#ga3681d4600f9cbd9237ea9ce6f67e508d)

#define SYS\_DLIST\_STATIC\_INIT(ptr\_to\_list)

Static initializer for a doubly-linked list.

**Definition** dlist.h:211

## [◆ ](#gadaf4b4c8e13afb54114af72d133e1fdb)K\_POLL\_STATE\_CANCELLED

| #define K\_POLL\_STATE\_CANCELLED   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_CANCELLED) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#gac166d9919d591bace163c5211e7b41f4)K\_POLL\_STATE\_DATA\_AVAILABLE

| #define K\_POLL\_STATE\_DATA\_AVAILABLE   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_DATA\_AVAILABLE) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#gabd5ac3341698534f39ded718079d6168)K\_POLL\_STATE\_FIFO\_DATA\_AVAILABLE

| #define K\_POLL\_STATE\_FIFO\_DATA\_AVAILABLE   [K\_POLL\_STATE\_DATA\_AVAILABLE](#gac166d9919d591bace163c5211e7b41f4) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#gac236074cd43f59f28b803fe2c4a4f6f7)K\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE

| #define K\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#ga522822c5e06a89b22ce4dcefd10c66aa)K\_POLL\_STATE\_NOT\_READY

| #define K\_POLL\_STATE\_NOT\_READY   0 |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#ga9028d6868ee964ca25931ed9170068dd)K\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE

| #define K\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#gae9e3eefd5a29a538d22f53592578bb37)K\_POLL\_STATE\_SEM\_AVAILABLE

| #define K\_POLL\_STATE\_SEM\_AVAILABLE   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SEM\_AVAILABLE) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#ga478aae7fe4fb5c7b7c76ed216c22a7f1)K\_POLL\_STATE\_SIGNALED

| #define K\_POLL\_STATE\_SIGNALED   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SIGNALED) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#ga58d656f73f031a39b8a936133fe5504f)K\_POLL\_TYPE\_DATA\_AVAILABLE

| #define K\_POLL\_TYPE\_DATA\_AVAILABLE   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_DATA\_AVAILABLE) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#ga71734fee18c523cf70276260118afb91)K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE

| #define K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE   [K\_POLL\_TYPE\_DATA\_AVAILABLE](#ga58d656f73f031a39b8a936133fe5504f) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#gafd5d801eb9e9cf6097b2c08b4933998e)K\_POLL\_TYPE\_IGNORE

| #define K\_POLL\_TYPE\_IGNORE   0 |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#gaa83509b54175fb6c98324422a928d5e1)K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE

| #define K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#ga14e113201a3b3ad768c6a5ce917d1912)K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE

| #define K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#ga0fd7605bdffd43dff7480a90a603ffde)K\_POLL\_TYPE\_SEM\_AVAILABLE

| #define K\_POLL\_TYPE\_SEM\_AVAILABLE   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SEM\_AVAILABLE) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#ga144d8eb34d85f6053e454410a10bf56a)K\_POLL\_TYPE\_SIGNAL

| #define K\_POLL\_TYPE\_SIGNAL   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SIGNAL) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga36d7978872a83191dd3cc16d62165add)k\_poll\_modes

| enum [k\_poll\_modes](#ga36d7978872a83191dd3cc16d62165add) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

| Enumerator | |
| --- | --- |
| K\_POLL\_MODE\_NOTIFY\_ONLY |  |
| K\_POLL\_NUM\_MODES |  |

## Function Documentation

## [◆ ](#gac550dc93662ce164fb22a5a91d6830db)k\_poll()

| int k\_poll | ( | struct [k\_poll\_event](structk__poll__event.md) \* | *events*, |
| --- | --- | --- | --- |
|  |  | int | *num\_events*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](kernel_8h.md)>`

Wait for one or many of multiple poll events to occur.

This routine allows a thread to wait concurrently for one or many of multiple poll events to have occurred. Such events can be a kernel object being available, like a semaphore, or a poll signal event.

When an event notifies that a kernel object is available, the kernel object is not "given" to the thread calling [k\_poll()](#gac550dc93662ce164fb22a5a91d6830db): it merely signals the fact that the object was available when the [k\_poll()](#gac550dc93662ce164fb22a5a91d6830db) call was in effect. Also, all threads trying to acquire an object the regular way, i.e. by pending on the object, have precedence over the thread polling on the object. This means that the polling thread will never get the poll event on an object until the object becomes available and its pend queue is empty. For this reason, the [k\_poll()](#gac550dc93662ce164fb22a5a91d6830db) call is more effective when the objects being polled only have one thread, the polling thread, trying to acquire them.

When [k\_poll()](#gac550dc93662ce164fb22a5a91d6830db) returns 0, the caller should loop on all the events that were passed to [k\_poll()](#gac550dc93662ce164fb22a5a91d6830db) and check the state field for the values that were expected and take the associated actions.

Before being reused for another call to [k\_poll()](#gac550dc93662ce164fb22a5a91d6830db), the user has to reset the state field to K\_POLL\_STATE\_NOT\_READY.

When called from user mode, a temporary memory allocation is required from the caller's resource pool.

Parameters
:   | events | An array of events to be polled for. |
    | --- | --- |
    | num\_events | The number of events in the array. |
    | timeout | Waiting period for an event to be ready, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | One or more events are ready. |
    | --- | --- |
    | -EAGAIN | Waiting period timed out. |
    | -EINTR | Polling has been interrupted, e.g. with [k\_queue\_cancel\_wait()](group__queue__apis.md#ga7c39d86cc6509f59ff9223cac3ea5071 "Cancel waiting on a queue."). All output events are still set and valid, cancelled event(s) will be set to K\_POLL\_STATE\_CANCELLED. In other words, -EINTR status means that at least one of output events is K\_POLL\_STATE\_CANCELLED. |
    | -ENOMEM | Thread resource pool insufficient memory (user mode only) |
    | -EINVAL | Bad parameters (user mode only) |

## [◆ ](#gaa06bddd93a024fc5326d93187d80eb03)k\_poll\_event\_init()

| void k\_poll\_event\_init | ( | struct [k\_poll\_event](structk__poll__event.md) \* | *event*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *type*, |
|  |  | int | *mode*, |
|  |  | void \* | *obj* ) |

`#include <[kernel.h](kernel_8h.md)>`

Initialize one struct [k\_poll\_event](structk__poll__event.md "Poll Event.") instance.

After this routine is called on a poll event, the event it ready to be placed in an event array to be passed to [k\_poll()](#gac550dc93662ce164fb22a5a91d6830db).

Parameters
:   | event | The event to initialize. |
    | --- | --- |
    | type | A bitfield of the types of event, from the K\_POLL\_TYPE\_xxx values. Only values that apply to the same object being polled can be used together. Choosing K\_POLL\_TYPE\_IGNORE disables the event. |
    | mode | Future. Use K\_POLL\_MODE\_NOTIFY\_ONLY. |
    | obj | Kernel object or poll signal. |

## [◆ ](#ga69dae11c7cb2c669caa411c3e7001311)k\_poll\_signal\_check()

| void k\_poll\_signal\_check | ( | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \* | *signaled*, |
|  |  | int \* | *result* ) |

`#include <[kernel.h](kernel_8h.md)>`

Fetch the signaled state and result value of a poll signal.

Parameters
:   | sig | A poll signal object |
    | --- | --- |
    | signaled | An integer buffer which will be written nonzero if the object was signaled |
    | result | An integer destination buffer which will be written with the result value if the object was signaled, or an undefined value if it was not. |

## [◆ ](#gaee3090c2a912b93b6a5855e3018c3551)k\_poll\_signal\_init()

| void k\_poll\_signal\_init | ( | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a poll signal object.

Ready a poll signal object to be signaled via [k\_poll\_signal\_raise()](#gad0bf3825f828ec3ca37481bf3cbd6723).

Parameters
:   | sig | A poll signal. |
    | --- | --- |

## [◆ ](#gad0bf3825f828ec3ca37481bf3cbd6723)k\_poll\_signal\_raise()

| int k\_poll\_signal\_raise | ( | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig*, |
| --- | --- | --- | --- |
|  |  | int | *result* ) |

`#include <[kernel.h](kernel_8h.md)>`

Signal a poll signal object.

This routine makes ready a poll signal, which is basically a poll event of type K\_POLL\_TYPE\_SIGNAL. If a thread was polling on that event, it will be made ready to run. A *result* value can be specified.

The poll signal contains a 'signaled' field that, when set by [k\_poll\_signal\_raise()](#gad0bf3825f828ec3ca37481bf3cbd6723), stays set until the user sets it back to 0 with [k\_poll\_signal\_reset()](#ga02d899d1455ae1f3f55ffe8f1ebd6994). It thus has to be reset by the user before being passed again to [k\_poll()](#gac550dc93662ce164fb22a5a91d6830db) or [k\_poll()](#gac550dc93662ce164fb22a5a91d6830db) will consider it being signaled, and will return immediately.

Note
:   The result is stored and the 'signaled' field is set even if this function returns an error indicating that an expiring poll was not notified. The next [k\_poll()](#gac550dc93662ce164fb22a5a91d6830db) will detect the missed raise.

Parameters
:   | sig | A poll signal. |
    | --- | --- |
    | result | The value to store in the result field of the signal. |

Return values
:   | 0 | The signal was delivered successfully. |
    | --- | --- |
    | -EAGAIN | The polling thread's timeout is in the process of expiring. |

## [◆ ](#ga02d899d1455ae1f3f55ffe8f1ebd6994)k\_poll\_signal\_reset()

| void k\_poll\_signal\_reset | ( | struct [k\_poll\_signal](structk__poll__signal.md) \* | *sig* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Reset a poll signal object's state to unsignaled.

Parameters
:   | sig | A poll signal object |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
