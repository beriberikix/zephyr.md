---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__fifo__apis.html
original_path: doxygen/html/group__fifo__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FIFO APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [k\_fifo\_init](#gaeebf6ef54d4be61e19408f44a734a159)(fifo) |
|  | Initialize a FIFO queue. |
| #define | [k\_fifo\_cancel\_wait](#gab744080af449e093df8dd4982e013e16)(fifo) |
|  | Cancel waiting on a FIFO queue. |
| #define | [k\_fifo\_put](#ga3addb10f86f19e245c23362433d5c913)(fifo, data) |
|  | Add an element to a FIFO queue. |
| #define | [k\_fifo\_alloc\_put](#gab1c5212040d12cbb92cede5cf54928ba)(fifo, data) |
|  | Add an element to a FIFO queue. |
| #define | [k\_fifo\_put\_list](#ga1bf5f52290c83e54ba14358cbbb4051b)(fifo, head, tail) |
|  | Atomically add a list of elements to a FIFO. |
| #define | [k\_fifo\_put\_slist](#ga4cdc286a7a6f0d43acab63a4846815e7)(fifo, list) |
|  | Atomically add a list of elements to a FIFO queue. |
| #define | [k\_fifo\_get](#ga1e2c480e2124116af97e94e7b4435de6)(fifo, timeout) |
|  | Get an element from a FIFO queue. |
| #define | [k\_fifo\_is\_empty](#gab7cec4adc128ed1fd2d194ba6cd8c640)(fifo) |
|  | Query a FIFO queue to see if it has data available. |
| #define | [k\_fifo\_peek\_head](#ga2e0c8608f095a929740fa94c94a4f389)(fifo) |
|  | Peek element at the head of a FIFO queue. |
| #define | [k\_fifo\_peek\_tail](#gafbe2ce9a6437b886cf149016187ba92f)(fifo) |
|  | Peek element at the tail of FIFO queue. |
| #define | [K\_FIFO\_DEFINE](#ga230b02a526ecb0ae1598be75cb9a8274)(name) |
|  | Statically define and initialize a FIFO queue. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gab1c5212040d12cbb92cede5cf54928ba)k\_fifo\_alloc\_put

| #define k\_fifo\_alloc\_put | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_fifo](structk__fifo.md), alloc\_put, fifo, data); \

int fap\_ret = [k\_queue\_alloc\_append](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)(&(fifo)->\_queue, data); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_fifo](structk__fifo.md), alloc\_put, fifo, data, fap\_ret); \

fap\_ret; \

})

[k\_queue\_alloc\_append](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a)

int32\_t k\_queue\_alloc\_append(struct k\_queue \*queue, void \*data)

Append an element to a queue.

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

Add an element to a FIFO queue.

This routine adds a data item to *fifo*. There is an implicit memory allocation to create an additional temporary bookkeeping data structure from the calling thread's resource pool, which is automatically freed when the item is removed. The data itself is not copied.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | fifo | Address of the FIFO. |
    | --- | --- |
    | data | Address of the data item. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOMEM | if there isn't sufficient RAM in the caller's resource pool |

## [◆ ](#gab744080af449e093df8dd4982e013e16)k\_fifo\_cancel\_wait

| #define k\_fifo\_cancel\_wait | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_fifo](structk__fifo.md), cancel\_wait, fifo); \

k\_queue\_cancel\_wait(&(fifo)->\_queue); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_fifo](structk__fifo.md), cancel\_wait, fifo); \

})

Cancel waiting on a FIFO queue.

This routine causes first thread pending on *fifo*, if any, to return from [k\_fifo\_get()](#ga1e2c480e2124116af97e94e7b4435de6) call with NULL value (as if timeout expired).

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | fifo | Address of the FIFO queue. |
    | --- | --- |

## [◆ ](#ga230b02a526ecb0ae1598be75cb9a8274)K\_FIFO\_DEFINE

| #define K\_FIFO\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([k\_fifo](structk__fifo.md), name) = \

Z\_FIFO\_INITIALIZER(name)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Statically define and initialize a FIFO queue.

The FIFO queue can be accessed outside the module where it is defined using:

extern struct [k\_fifo](structk__fifo.md) <name>;

Parameters
:   | name | Name of the FIFO queue. |
    | --- | --- |

## [◆ ](#ga1e2c480e2124116af97e94e7b4435de6)k\_fifo\_get

| #define k\_fifo\_get | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_fifo](structk__fifo.md), get, fifo, timeout); \

void \*fg\_ret = [k\_queue\_get](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)(&(fifo)->\_queue, timeout); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_fifo](structk__fifo.md), get, fifo, timeout, fg\_ret); \

fg\_ret; \

})

[k\_queue\_get](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)

void \* k\_queue\_get(struct k\_queue \*queue, k\_timeout\_t timeout)

Get an element from a queue.

Get an element from a FIFO queue.

This routine removes a data item from *fifo* in a "first in, first out" manner. The first word of the data item is reserved for the kernel's use.

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | fifo | Address of the FIFO queue. |
    | --- | --- |
    | timeout | Waiting period to obtain a data item, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Returns
:   Address of the data item if successful; NULL if returned without waiting, or waiting period timed out.

## [◆ ](#gaeebf6ef54d4be61e19408f44a734a159)k\_fifo\_init

| #define k\_fifo\_init | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_fifo](structk__fifo.md), init, fifo); \

k\_queue\_init(&(fifo)->\_queue); \

K\_OBJ\_CORE\_INIT([K\_OBJ\_CORE](group__obj__core__apis.md#ga2bd0c2c121afc09448926a3648c7d814)(fifo), \_obj\_type\_fifo); \

K\_OBJ\_CORE\_LINK([K\_OBJ\_CORE](group__obj__core__apis.md#ga2bd0c2c121afc09448926a3648c7d814)(fifo)); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_fifo](structk__fifo.md), init, fifo); \

})

[K\_OBJ\_CORE](group__obj__core__apis.md#ga2bd0c2c121afc09448926a3648c7d814)

#define K\_OBJ\_CORE(kobj)

Convert kernel object pointer into its object core pointer.

**Definition** obj\_core.h:21

Initialize a FIFO queue.

This routine initializes a FIFO queue, prior to its first use.

Parameters
:   | fifo | Address of the FIFO queue. |
    | --- | --- |

## [◆ ](#gab7cec4adc128ed1fd2d194ba6cd8c640)k\_fifo\_is\_empty

| #define k\_fifo\_is\_empty | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

[k\_queue\_is\_empty](group__queue__apis.md#gadb2bb8088868b3c5801c72b320389ca9)(&(fifo)->\_queue)

[k\_queue\_is\_empty](group__queue__apis.md#gadb2bb8088868b3c5801c72b320389ca9)

int k\_queue\_is\_empty(struct k\_queue \*queue)

Query a queue to see if it has data available.

Query a FIFO queue to see if it has data available.

Note that the data might be already gone by the time this function returns if other threads is also trying to read from the FIFO.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | fifo | Address of the FIFO queue. |
    | --- | --- |

Returns
:   Non-zero if the FIFO queue is empty.
:   0 if data is available.

## [◆ ](#ga2e0c8608f095a929740fa94c94a4f389)k\_fifo\_peek\_head

| #define k\_fifo\_peek\_head | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_fifo](structk__fifo.md), peek\_head, fifo); \

void \*fph\_ret = [k\_queue\_peek\_head](group__queue__apis.md#ga8ccd5137690c127a0f7d67619b88a52b)(&(fifo)->\_queue); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_fifo](structk__fifo.md), peek\_head, fifo, fph\_ret); \

fph\_ret; \

})

[k\_queue\_peek\_head](group__queue__apis.md#ga8ccd5137690c127a0f7d67619b88a52b)

void \* k\_queue\_peek\_head(struct k\_queue \*queue)

Peek element at the head of queue.

Peek element at the head of a FIFO queue.

Return element from the head of FIFO queue without removing it. A usecase for this is if elements of the FIFO object are themselves containers. Then on each iteration of processing, a head container will be peeked, and some data processed out of it, and only if the container is empty, it will be completely remove from the FIFO queue.

Parameters
:   | fifo | Address of the FIFO queue. |
    | --- | --- |

Returns
:   Head element, or NULL if the FIFO queue is empty.

## [◆ ](#gafbe2ce9a6437b886cf149016187ba92f)k\_fifo\_peek\_tail

| #define k\_fifo\_peek\_tail | ( |  | *fifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_fifo](structk__fifo.md), peek\_tail, fifo); \

void \*fpt\_ret = [k\_queue\_peek\_tail](group__queue__apis.md#ga27a460c42836d8b093ad9274c14bb176)(&(fifo)->\_queue); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_fifo](structk__fifo.md), peek\_tail, fifo, fpt\_ret); \

fpt\_ret; \

})

[k\_queue\_peek\_tail](group__queue__apis.md#ga27a460c42836d8b093ad9274c14bb176)

void \* k\_queue\_peek\_tail(struct k\_queue \*queue)

Peek element at the tail of queue.

Peek element at the tail of FIFO queue.

Return element from the tail of FIFO queue (without removing it). A usecase for this is if elements of the FIFO queue are themselves containers. Then it may be useful to add more data to the last container in a FIFO queue.

Parameters
:   | fifo | Address of the FIFO queue. |
    | --- | --- |

Returns
:   Tail element, or NULL if a FIFO queue is empty.

## [◆ ](#ga3addb10f86f19e245c23362433d5c913)k\_fifo\_put

| #define k\_fifo\_put | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_fifo](structk__fifo.md), put, fifo, data); \

k\_queue\_append(&(fifo)->\_queue, data); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_fifo](structk__fifo.md), put, fifo, data); \

})

Add an element to a FIFO queue.

This routine adds a data item to *fifo*. A FIFO data item must be aligned on a word boundary, and the first word of the item is reserved for the kernel's use.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | fifo | Address of the FIFO. |
    | --- | --- |
    | data | Address of the data item. |

## [◆ ](#ga1bf5f52290c83e54ba14358cbbb4051b)k\_fifo\_put\_list

| #define k\_fifo\_put\_list | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *head*, |
|  |  |  | *tail* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_fifo](structk__fifo.md), put\_list, fifo, head, tail); \

k\_queue\_append\_list(&(fifo)->\_queue, head, tail); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_fifo](structk__fifo.md), put\_list, fifo, head, tail); \

})

Atomically add a list of elements to a FIFO.

This routine adds a list of data items to *fifo* in one operation. The data items must be in a singly-linked list, with the first word of each data item pointing to the next data item; the list must be NULL-terminated.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | fifo | Address of the FIFO queue. |
    | --- | --- |
    | head | Pointer to first node in singly-linked list. |
    | tail | Pointer to last node in singly-linked list. |

## [◆ ](#ga4cdc286a7a6f0d43acab63a4846815e7)k\_fifo\_put\_slist

| #define k\_fifo\_put\_slist | ( |  | *fifo*, |
| --- | --- | --- | --- |
|  |  |  | *list* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_fifo](structk__fifo.md), put\_slist, fifo, list); \

k\_queue\_merge\_slist(&(fifo)->\_queue, list); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_fifo](structk__fifo.md), put\_slist, fifo, list); \

})

Atomically add a list of elements to a FIFO queue.

This routine adds a list of data items to *fifo* in one operation. The data items must be in a singly-linked list implemented using a [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8 "Single-linked list structure.") object. Upon completion, the [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8 "Single-linked list structure.") object is invalid and must be re-initialized via [sys\_slist\_init()](group__single-linked-list__apis.md#ga913aea7661b4ab3b4b50a8efc0d70428 "Initialize a list.").

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | fifo | Address of the FIFO queue. |
    | --- | --- |
    | list | Pointer to [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8 "Single-linked list structure.") object. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
