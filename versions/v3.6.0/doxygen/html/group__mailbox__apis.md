---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mailbox__apis.html
original_path: doxygen/html/group__mailbox__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Mailbox APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_mbox\_msg](structk__mbox__msg.md) |
|  | Mailbox Message Structure. [More...](structk__mbox__msg.md#details) |
| struct | [k\_mbox](structk__mbox.md) |
|  | Mailbox Structure. [More...](structk__mbox.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_MBOX\_DEFINE](#gab55cba898db47113a06641c01f3e3714)(name) |
|  | Statically define and initialize a mailbox. |

| Functions | |
| --- | --- |
| void | [k\_mbox\_init](#ga686f20c199a9e971822d8279d175d8c2) (struct [k\_mbox](structk__mbox.md) \*mbox) |
|  | Initialize a mailbox. |
| int | [k\_mbox\_put](#gaa1e5cdd992d8b9be11f82254e1886ed2) (struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*tx\_msg, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Send a mailbox message in a synchronous manner. |
| void | [k\_mbox\_async\_put](#gadd60f7b760371c0a141a1e4da253a0f0) (struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*tx\_msg, struct k\_sem \*sem) |
|  | Send a mailbox message in an asynchronous manner. |
| int | [k\_mbox\_get](#ga2ea91154620b139dbed1ad949b97c3ef) (struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*rx\_msg, void \*buffer, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Receive a mailbox message. |
| void | [k\_mbox\_data\_get](#ga3d19e648e67f109609259543c9a01d6e) (struct [k\_mbox\_msg](structk__mbox__msg.md) \*rx\_msg, void \*buffer) |
|  | Retrieve mailbox message data into a buffer. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gab55cba898db47113a06641c01f3e3714)K\_MBOX\_DEFINE

| #define K\_MBOX\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([k\_mbox](structk__mbox.md), name) = \

Z\_MBOX\_INITIALIZER(name) \

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[k\_mbox](structk__mbox.md)

Mailbox Structure.

**Definition** kernel.h:4716

Statically define and initialize a mailbox.

The mailbox is to be accessed outside the module where it is defined using:

extern struct [k\_mbox](structk__mbox.md) <name>;

Parameters
:   | name | Name of the mailbox. |
    | --- | --- |

## Function Documentation

## [◆ ](#gadd60f7b760371c0a141a1e4da253a0f0)k\_mbox\_async\_put()

| void k\_mbox\_async\_put | ( | struct [k\_mbox](structk__mbox.md) \* | *mbox*, |
| --- | --- | --- | --- |
|  |  | struct [k\_mbox\_msg](structk__mbox__msg.md) \* | *tx\_msg*, |
|  |  | struct k\_sem \* | *sem* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Send a mailbox message in an asynchronous manner.

This routine sends a message to *mbox* without waiting for a receiver to process it. The message data may be in a buffer or non-existent (i.e. an empty message). Optionally, the semaphore *sem* will be given when the message has been both received and completely processed by the receiver.

Parameters
:   | mbox | Address of the mailbox. |
    | --- | --- |
    | tx\_msg | Address of the transmit message descriptor. |
    | sem | Address of a semaphore, or NULL if none is needed. |

## [◆ ](#ga3d19e648e67f109609259543c9a01d6e)k\_mbox\_data\_get()

| void k\_mbox\_data\_get | ( | struct [k\_mbox\_msg](structk__mbox__msg.md) \* | *rx\_msg*, |
| --- | --- | --- | --- |
|  |  | void \* | *buffer* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Retrieve mailbox message data into a buffer.

This routine completes the processing of a received message by retrieving its data into a buffer, then disposing of the message.

Alternatively, this routine can be used to dispose of a received message without retrieving its data.

Parameters
:   | rx\_msg | Address of the receive message descriptor. |
    | --- | --- |
    | buffer | Address of the buffer to receive data, or NULL to discard the data. |

## [◆ ](#ga2ea91154620b139dbed1ad949b97c3ef)k\_mbox\_get()

| int k\_mbox\_get | ( | struct [k\_mbox](structk__mbox.md) \* | *mbox*, |
| --- | --- | --- | --- |
|  |  | struct [k\_mbox\_msg](structk__mbox__msg.md) \* | *rx\_msg*, |
|  |  | void \* | *buffer*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Receive a mailbox message.

This routine receives a message from *mbox*, then optionally retrieves its data and disposes of the message.

Parameters
:   | mbox | Address of the mailbox. |
    | --- | --- |
    | rx\_msg | Address of the receive message descriptor. |
    | buffer | Address of the buffer to receive data, or NULL to defer data retrieval and message disposal until later. |
    | timeout | Waiting period for a message to be received, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Message received. |
    | --- | --- |
    | -ENOMSG | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |

## [◆ ](#ga686f20c199a9e971822d8279d175d8c2)k\_mbox\_init()

| void k\_mbox\_init | ( | struct [k\_mbox](structk__mbox.md) \* | *mbox* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Initialize a mailbox.

This routine initializes a mailbox object, prior to its first use.

Parameters
:   | mbox | Address of the mailbox. |
    | --- | --- |

## [◆ ](#gaa1e5cdd992d8b9be11f82254e1886ed2)k\_mbox\_put()

| int k\_mbox\_put | ( | struct [k\_mbox](structk__mbox.md) \* | *mbox*, |
| --- | --- | --- | --- |
|  |  | struct [k\_mbox\_msg](structk__mbox__msg.md) \* | *tx\_msg*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Send a mailbox message in a synchronous manner.

This routine sends a message to *mbox* and waits for a receiver to both receive and process it. The message data may be in a buffer or non-existent (i.e. an empty message).

Parameters
:   | mbox | Address of the mailbox. |
    | --- | --- |
    | tx\_msg | Address of the transmit message descriptor. |
    | timeout | Waiting period for the message to be received, or one of the special values K\_NO\_WAIT and K\_FOREVER. Once the message has been received, this routine waits as long as necessary for the message to be completely processed. |

Return values
:   | 0 | Message sent. |
    | --- | --- |
    | -ENOMSG | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
