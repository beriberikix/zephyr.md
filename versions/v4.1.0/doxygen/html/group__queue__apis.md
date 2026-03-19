---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__queue__apis.html
original_path: doxygen/html/group__queue__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Queue APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [K\_QUEUE\_DEFINE](#gacd0bc309f0147d4669f65fafa87e0e70)(name) |
|  | Statically define and initialize a queue. |

| Functions | |
| --- | --- |
| void | [k\_queue\_init](#ga0236222d42768c2bf00942f328146c21) (struct [k\_queue](structk__queue.md) \*queue) |
|  | Initialize a queue. |
| void | [k\_queue\_cancel\_wait](#ga7c39d86cc6509f59ff9223cac3ea5071) (struct [k\_queue](structk__queue.md) \*queue) |
|  | Cancel waiting on a queue. |
| void | [k\_queue\_append](#gaa84522a5ace6e7f8ba61033baca6972f) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Append an element to the end of a queue. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_queue\_alloc\_append](#ga690f3a1450e946d75f31b3e499d1d06a) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Append an element to a queue. |
| void | [k\_queue\_prepend](#ga8ce013d8a037d4be5078797e0050e9c6) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Prepend an element to a queue. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_queue\_alloc\_prepend](#gacf3dba40125073c11075e5a134919f88) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Prepend an element to a queue. |
| void | [k\_queue\_insert](#gad47336f27e433a52600a3b67ab89556a) (struct [k\_queue](structk__queue.md) \*queue, void \*prev, void \*data) |
|  | Inserts an element to a queue. |
| int | [k\_queue\_append\_list](#ga91d1a144fc2aeb3dd655accc94ca43aa) (struct [k\_queue](structk__queue.md) \*queue, void \*head, void \*tail) |
|  | Atomically append a list of elements to a queue. |
| int | [k\_queue\_merge\_slist](#ga4eee0da7442d60572b05d60a9996e69d) (struct [k\_queue](structk__queue.md) \*queue, [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Atomically add a list of elements to a queue. |
| void \* | [k\_queue\_get](#ga0a77d8556e7d253319275de034f01619) (struct [k\_queue](structk__queue.md) \*queue, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get an element from a queue. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_queue\_remove](#ga4bff929ed1d366a06e00865a5bbe2544) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Remove an element from a queue. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_queue\_unique\_append](#ga287a2d81e2e3041be1cd45164e72f127) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Append an element to a queue only if it's not present already. |
| int | [k\_queue\_is\_empty](#gadb2bb8088868b3c5801c72b320389ca9) (struct [k\_queue](structk__queue.md) \*queue) |
|  | Query a queue to see if it has data available. |
| void \* | [k\_queue\_peek\_head](#ga8ccd5137690c127a0f7d67619b88a52b) (struct [k\_queue](structk__queue.md) \*queue) |
|  | Peek element at the head of queue. |
| void \* | [k\_queue\_peek\_tail](#ga27a460c42836d8b093ad9274c14bb176) (struct [k\_queue](structk__queue.md) \*queue) |
|  | Peek element at the tail of queue. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gacd0bc309f0147d4669f65fafa87e0e70)K\_QUEUE\_DEFINE

| #define K\_QUEUE\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([k\_queue](structk__queue.md), name) = \

Z\_QUEUE\_INITIALIZER(name)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[k\_queue](structk__queue.md)

**Definition** kernel.h:1957

Statically define and initialize a queue.

The queue can be accessed outside the module where it is defined using:

extern struct [k\_queue](structk__queue.md) <name>;

Parameters
:   | name | Name of the queue. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga690f3a1450e946d75f31b3e499d1d06a)k\_queue\_alloc\_append()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) k\_queue\_alloc\_append | ( | struct [k\_queue](structk__queue.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | void \* | *data* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Append an element to a queue.

This routine appends a data item to *queue*. There is an implicit memory allocation to create an additional temporary bookkeeping data structure from the calling thread's resource pool, which is automatically freed when the item is removed. The data itself is not copied.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |
    | data | Address of the data item. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOMEM | if there isn't sufficient RAM in the caller's resource pool |

## [◆ ](#gacf3dba40125073c11075e5a134919f88)k\_queue\_alloc\_prepend()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) k\_queue\_alloc\_prepend | ( | struct [k\_queue](structk__queue.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | void \* | *data* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Prepend an element to a queue.

This routine prepends a data item to *queue*. There is an implicit memory allocation to create an additional temporary bookkeeping data structure from the calling thread's resource pool, which is automatically freed when the item is removed. The data itself is not copied.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |
    | data | Address of the data item. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOMEM | if there isn't sufficient RAM in the caller's resource pool |

## [◆ ](#gaa84522a5ace6e7f8ba61033baca6972f)k\_queue\_append()

| | void k\_queue\_append | ( | struct [k\_queue](structk__queue.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | void \* | *data* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Append an element to the end of a queue.

This routine appends a data item to *queue*. A queue data item must be aligned on a word boundary, and the first word of the item is reserved for the kernel's use.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |
    | data | Address of the data item. |

## [◆ ](#ga91d1a144fc2aeb3dd655accc94ca43aa)k\_queue\_append\_list()

| | int k\_queue\_append\_list | ( | struct [k\_queue](structk__queue.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | void \* | *head*, | |  |  | void \* | *tail* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Atomically append a list of elements to a queue.

This routine adds a list of data items to *queue* in one operation. The data items must be in a singly-linked list, with the first word in each data item pointing to the next data item; the list must be NULL-terminated.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |
    | head | Pointer to first node in singly-linked list. |
    | tail | Pointer to last node in singly-linked list. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | on invalid supplied data |

## [◆ ](#ga7c39d86cc6509f59ff9223cac3ea5071)k\_queue\_cancel\_wait()

| | void k\_queue\_cancel\_wait | ( | struct [k\_queue](structk__queue.md) \* | *queue* | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Cancel waiting on a queue.

This routine causes first thread pending on *queue*, if any, to return from [k\_queue\_get()](#ga0a77d8556e7d253319275de034f01619) call with NULL value (as if timeout expired). If the queue is being waited on by [k\_poll()](group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db "Wait for one or many of multiple poll events to occur."), it will return with -EINTR and K\_POLL\_STATE\_CANCELLED state (and per above, subsequent [k\_queue\_get()](#ga0a77d8556e7d253319275de034f01619) will return NULL).

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |

## [◆ ](#ga0a77d8556e7d253319275de034f01619)k\_queue\_get()

| | void \* k\_queue\_get | ( | struct [k\_queue](structk__queue.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get an element from a queue.

This routine removes first data item from *queue*. The first word of the data item is reserved for the kernel's use.

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |
    | timeout | Waiting period to obtain a data item, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Returns
:   Address of the data item if successful; NULL if returned without waiting, or waiting period timed out.

## [◆ ](#ga0236222d42768c2bf00942f328146c21)k\_queue\_init()

| void k\_queue\_init | ( | struct [k\_queue](structk__queue.md) \* | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a queue.

This routine initializes a queue object, prior to its first use.

Parameters
:   | queue | Address of the queue. |
    | --- | --- |

## [◆ ](#gad47336f27e433a52600a3b67ab89556a)k\_queue\_insert()

| | void k\_queue\_insert | ( | struct [k\_queue](structk__queue.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | void \* | *prev*, | |  |  | void \* | *data* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Inserts an element to a queue.

This routine inserts a data item to *queue* after previous item. A queue data item must be aligned on a word boundary, and the first word of the item is reserved for the kernel's use.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |
    | prev | Address of the previous data item. |
    | data | Address of the data item. |

## [◆ ](#gadb2bb8088868b3c5801c72b320389ca9)k\_queue\_is\_empty()

| | int k\_queue\_is\_empty | ( | struct [k\_queue](structk__queue.md) \* | *queue* | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Query a queue to see if it has data available.

Note that the data might be already gone by the time this function returns if other threads are also trying to read from the queue.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |

Returns
:   Non-zero if the queue is empty.
:   0 if data is available.

## [◆ ](#ga4eee0da7442d60572b05d60a9996e69d)k\_queue\_merge\_slist()

| | int k\_queue\_merge\_slist | ( | struct [k\_queue](structk__queue.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \* | *list* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Atomically add a list of elements to a queue.

This routine adds a list of data items to *queue* in one operation. The data items must be in a singly-linked list implemented using a [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8 "Single-linked list structure.") object. Upon completion, the original list is empty.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |
    | list | Pointer to [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8 "Single-linked list structure.") object. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | on invalid data |

## [◆ ](#ga8ccd5137690c127a0f7d67619b88a52b)k\_queue\_peek\_head()

| void \* k\_queue\_peek\_head | ( | struct [k\_queue](structk__queue.md) \* | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Peek element at the head of queue.

Return element from the head of queue without removing it.

Parameters
:   | queue | Address of the queue. |
    | --- | --- |

Returns
:   Head element, or NULL if queue is empty.

## [◆ ](#ga27a460c42836d8b093ad9274c14bb176)k\_queue\_peek\_tail()

| void \* k\_queue\_peek\_tail | ( | struct [k\_queue](structk__queue.md) \* | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Peek element at the tail of queue.

Return element from the tail of queue without removing it.

Parameters
:   | queue | Address of the queue. |
    | --- | --- |

Returns
:   Tail element, or NULL if queue is empty.

## [◆ ](#ga8ce013d8a037d4be5078797e0050e9c6)k\_queue\_prepend()

| | void k\_queue\_prepend | ( | struct [k\_queue](structk__queue.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | void \* | *data* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Prepend an element to a queue.

This routine prepends a data item to *queue*. A queue data item must be aligned on a word boundary, and the first word of the item is reserved for the kernel's use.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |
    | data | Address of the data item. |

## [◆ ](#ga4bff929ed1d366a06e00865a5bbe2544)k\_queue\_remove()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_queue\_remove | ( | struct [k\_queue](structk__queue.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | void \* | *data* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Remove an element from a queue.

This routine removes data item from *queue*. The first word of the data item is reserved for the kernel's use. Removing elements from [k\_queue](structk__queue.md) rely on sys\_slist\_find\_and\_remove which is not a constant time operation.

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |
    | data | Address of the data item. |

Returns
:   true if data item was removed

## [◆ ](#ga287a2d81e2e3041be1cd45164e72f127)k\_queue\_unique\_append()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_queue\_unique\_append | ( | struct [k\_queue](structk__queue.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | void \* | *data* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Append an element to a queue only if it's not present already.

This routine appends data item to *queue*. The first word of the data item is reserved for the kernel's use. Appending elements to [k\_queue](structk__queue.md) relies on sys\_slist\_is\_node\_in\_list which is not a constant time operation.

Function properties (list may not be complete)

Parameters
:   | queue | Address of the queue. |
    | --- | --- |
    | data | Address of the data item. |

Returns
:   true if data item was added, false if not

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
