---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__msgq__apis.html
original_path: doxygen/html/group__msgq__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Message Queue APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_msgq](structk__msgq.md) |
|  | Message Queue Structure. [More...](structk__msgq.md#details) |
| struct | [k\_msgq\_attrs](structk__msgq__attrs.md) |
|  | Message Queue Attributes. [More...](structk__msgq__attrs.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_MSGQ\_FLAG\_ALLOC](#ga4bb73f46fd0818f7f7a90860b792f7ce)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [K\_MSGQ\_DEFINE](#ga95ef93002766901511d09c8cd8f8293b)(q\_name, q\_msg\_size, q\_max\_msgs, q\_align) |
|  | Statically define and initialize a message queue. |

| Functions | |
| --- | --- |
| void | [k\_msgq\_init](#ga54a5cdcaea2236c383ace433fedc0d39) (struct [k\_msgq](structk__msgq.md) \*msgq, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_msgs) |
|  | Initialize a message queue. |
| int | [k\_msgq\_alloc\_init](#gabe7305b8f442ebdc147dbbc6e8cf92fc) (struct [k\_msgq](structk__msgq.md) \*msgq, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_msgs) |
|  | Initialize a message queue. |
| int | [k\_msgq\_cleanup](#gafda4399aa9b8f1e44bdf752e00ea787b) (struct [k\_msgq](structk__msgq.md) \*msgq) |
|  | Release allocated buffer for a queue. |
| int | [k\_msgq\_put](#ga54e96aaaea5462a1f963b7fd5ca82bfe) (struct [k\_msgq](structk__msgq.md) \*msgq, const void \*data, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Send a message to a message queue. |
| int | [k\_msgq\_get](#gae67f2ced2df1f9c290ae15dab9097cb7) (struct [k\_msgq](structk__msgq.md) \*msgq, void \*data, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Receive a message from a message queue. |
| int | [k\_msgq\_peek](#ga14f543472f2f63cfde0bdfa87b95c915) (struct [k\_msgq](structk__msgq.md) \*msgq, void \*data) |
|  | Peek/read a message from a message queue. |
| int | [k\_msgq\_peek\_at](#ga69b004a40ab4ca497de314a99960fb8e) (struct [k\_msgq](structk__msgq.md) \*msgq, void \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx) |
|  | Peek/read a message from a message queue at the specified index. |
| void | [k\_msgq\_purge](#gaa18875887773195ae44b7fe0972ee760) (struct [k\_msgq](structk__msgq.md) \*msgq) |
|  | Purge a message queue. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_msgq\_num\_free\_get](#ga7d154beb4f9c6227eddbef26d406ca24) (struct [k\_msgq](structk__msgq.md) \*msgq) |
|  | Get the amount of free space in a message queue. |
| void | [k\_msgq\_get\_attrs](#ga8f9d3eef67cbc9c0717a84190bbf7f41) (struct [k\_msgq](structk__msgq.md) \*msgq, struct [k\_msgq\_attrs](structk__msgq__attrs.md) \*attrs) |
|  | Get basic attributes of a message queue. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_msgq\_num\_used\_get](#ga458793a89f1d9f762bda3422918a9faa) (struct [k\_msgq](structk__msgq.md) \*msgq) |
|  | Get the number of messages in a message queue. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga95ef93002766901511d09c8cd8f8293b)K\_MSGQ\_DEFINE

| #define K\_MSGQ\_DEFINE | ( |  | *q\_name*, |
| --- | --- | --- | --- |
|  |  |  | *q\_msg\_size*, |
|  |  |  | *q\_max\_msgs*, |
|  |  |  | *q\_align* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

static char \_\_noinit \_\_aligned(q\_align) \

\_k\_fifo\_buf\_##q\_name[(q\_max\_msgs) \* (q\_msg\_size)]; \

STRUCT\_SECTION\_ITERABLE([k\_msgq](structk__msgq.md), q\_name) = \

Z\_MSGQ\_INITIALIZER(q\_name, \_k\_fifo\_buf\_##q\_name, \

(q\_msg\_size), (q\_max\_msgs))

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4402

Statically define and initialize a message queue.

The message queue's ring buffer contains space for *q\_max\_msgs* messages, each of which is *q\_msg\_size* bytes long. Alignment of the message queue's ring buffer is not necessary, setting *q\_align* to 1 is sufficient.

The message queue can be accessed outside the module where it is defined using:

extern struct [k\_msgq](structk__msgq.md) <name>;

Parameters
:   | q\_name | Name of the message queue. |
    | --- | --- |
    | q\_msg\_size | Message size (in bytes). |
    | q\_max\_msgs | Maximum number of messages that can be queued. |
    | q\_align | Alignment of the message queue's ring buffer (power of 2). |

## [◆ ](#ga4bb73f46fd0818f7f7a90860b792f7ce)K\_MSGQ\_FLAG\_ALLOC

| #define K\_MSGQ\_FLAG\_ALLOC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

## Function Documentation

## [◆ ](#gabe7305b8f442ebdc147dbbc6e8cf92fc)k\_msgq\_alloc\_init()

| int k\_msgq\_alloc\_init | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *msg\_size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *max\_msgs* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Initialize a message queue.

This routine initializes a message queue object, prior to its first use, allocating its internal ring buffer from the calling thread's resource pool.

Memory allocated for the ring buffer can be released by calling [k\_msgq\_cleanup()](#gafda4399aa9b8f1e44bdf752e00ea787b), or if userspace is enabled and the msgq object loses all of its references.

Parameters
:   | msgq | Address of the message queue. |
    | --- | --- |
    | msg\_size | Message size (in bytes). |
    | max\_msgs | Maximum number of messages that can be queued. |

Returns
:   0 on success, -ENOMEM if there was insufficient memory in the thread's resource pool, or -EINVAL if the size parameters cause an integer overflow.

## [◆ ](#gafda4399aa9b8f1e44bdf752e00ea787b)k\_msgq\_cleanup()

| int k\_msgq\_cleanup | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Release allocated buffer for a queue.

Releases memory allocated for the ring buffer.

Parameters
:   | msgq | message queue to cleanup |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EBUSY | Queue not empty |

## [◆ ](#gae67f2ced2df1f9c290ae15dab9097cb7)k\_msgq\_get()

| int k\_msgq\_get | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Receive a message from a message queue.

This routine receives a message from message queue *q* in a "first in,
first out" manner.

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | msgq | Address of the message queue. |
    | --- | --- |
    | data | Address of area to hold the received message. |
    | timeout | Waiting period to receive the message, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Message received. |
    | --- | --- |
    | -ENOMSG | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |

## [◆ ](#ga8f9d3eef67cbc9c0717a84190bbf7f41)k\_msgq\_get\_attrs()

| void k\_msgq\_get\_attrs | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq*, |
| --- | --- | --- | --- |
|  |  | struct [k\_msgq\_attrs](structk__msgq__attrs.md) \* | *attrs* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Get basic attributes of a message queue.

This routine fetches basic attributes of message queue into attr argument.

Parameters
:   | msgq | Address of the message queue. |
    | --- | --- |
    | attrs | pointer to message queue attribute structure. |

## [◆ ](#ga54a5cdcaea2236c383ace433fedc0d39)k\_msgq\_init()

| void k\_msgq\_init | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq*, |
| --- | --- | --- | --- |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *msg\_size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *max\_msgs* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Initialize a message queue.

This routine initializes a message queue object, prior to its first use.

The message queue's ring buffer must contain space for *max\_msgs* messages, each of which is *msg\_size* bytes long. Alignment of the message queue's ring buffer is not necessary.

Parameters
:   | msgq | Address of the message queue. |
    | --- | --- |
    | buffer | Pointer to ring buffer that holds queued messages. |
    | msg\_size | Message size (in bytes). |
    | max\_msgs | Maximum number of messages that can be queued. |

## [◆ ](#ga7d154beb4f9c6227eddbef26d406ca24)k\_msgq\_num\_free\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_msgq\_num\_free\_get | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Get the amount of free space in a message queue.

This routine returns the number of unused entries in a message queue's ring buffer.

Parameters
:   | msgq | Address of the message queue. |
    | --- | --- |

Returns
:   Number of unused ring buffer entries.

## [◆ ](#ga458793a89f1d9f762bda3422918a9faa)k\_msgq\_num\_used\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_msgq\_num\_used\_get | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Get the number of messages in a message queue.

This routine returns the number of messages in a message queue's ring buffer.

Parameters
:   | msgq | Address of the message queue. |
    | --- | --- |

Returns
:   Number of messages.

## [◆ ](#ga14f543472f2f63cfde0bdfa87b95c915)k\_msgq\_peek()

| int k\_msgq\_peek | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq*, |
| --- | --- | --- | --- |
|  |  | void \* | *data* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Peek/read a message from a message queue.

This routine reads a message from message queue *q* in a "first in,
first out" manner and leaves the message in the queue.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | msgq | Address of the message queue. |
    | --- | --- |
    | data | Address of area to hold the message read from the queue. |

Return values
:   | 0 | Message read. |
    | --- | --- |
    | -ENOMSG | Returned when the queue has no message. |

## [◆ ](#ga69b004a40ab4ca497de314a99960fb8e)k\_msgq\_peek\_at()

| int k\_msgq\_peek\_at | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *idx* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Peek/read a message from a message queue at the specified index.

This routine reads a message from message queue at the specified index and leaves the message in the queue. k\_msgq\_peek\_at(msgq, data, 0) is equivalent to k\_msgq\_peek(msgq, data)

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | msgq | Address of the message queue. |
    | --- | --- |
    | data | Address of area to hold the message read from the queue. |
    | idx | Message queue index at which to peek |

Return values
:   | 0 | Message read. |
    | --- | --- |
    | -ENOMSG | Returned when the queue has no message at index. |

## [◆ ](#gaa18875887773195ae44b7fe0972ee760)k\_msgq\_purge()

| void k\_msgq\_purge | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Purge a message queue.

This routine discards all unreceived messages in a message queue's ring buffer. Any threads that are blocked waiting to send a message to the message queue are unblocked and see an -ENOMSG error code.

Parameters
:   | msgq | Address of the message queue. |
    | --- | --- |

## [◆ ](#ga54e96aaaea5462a1f963b7fd5ca82bfe)k\_msgq\_put()

| int k\_msgq\_put | ( | struct [k\_msgq](structk__msgq.md) \* | *msgq*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Send a message to a message queue.

This routine sends a message to message queue *q*.

Note
:   The message content is copied from *data* into *msgq* and the *data* pointer is not retained, so the message content will not be modified by this function.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | msgq | Address of the message queue. |
    | --- | --- |
    | data | Pointer to the message. |
    | timeout | Non-negative waiting period to add the message, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Message sent. |
    | --- | --- |
    | -ENOMSG | Returned without waiting or queue purged. |
    | -EAGAIN | Waiting period timed out. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
