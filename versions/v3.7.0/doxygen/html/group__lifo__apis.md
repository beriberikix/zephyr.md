---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__lifo__apis.html
original_path: doxygen/html/group__lifo__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LIFO APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [k\_lifo\_init](#ga69fb19716a9014f7de79f8e524d64a3e)(lifo) |
|  | Initialize a LIFO queue. |
| #define | [k\_lifo\_put](#gad662e36b1df8b9013e2dc61f9dfe3a8b)(lifo, data) |
|  | Add an element to a LIFO queue. |
| #define | [k\_lifo\_alloc\_put](#ga96d885a6a36fcfcb5eaa65898eee0965)(lifo, data) |
|  | Add an element to a LIFO queue. |
| #define | [k\_lifo\_get](#gad5f1775947b07a2a77f667aa9e41db5a)(lifo, timeout) |
|  | Get an element from a LIFO queue. |
| #define | [K\_LIFO\_DEFINE](#gaebd450d4181f22491623ea0aed6ee576)(name) |
|  | Statically define and initialize a LIFO queue. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga96d885a6a36fcfcb5eaa65898eee0965)k\_lifo\_alloc\_put

| #define k\_lifo\_alloc\_put | ( |  | *lifo*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_lifo](structk__lifo.md), alloc\_put, lifo, data); \

int lap\_ret = [k\_queue\_alloc\_prepend](group__queue__apis.md#gacf3dba40125073c11075e5a134919f88)(&(lifo)->\_queue, data); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_lifo](structk__lifo.md), alloc\_put, lifo, data, lap\_ret); \

lap\_ret; \

})

[k\_queue\_alloc\_prepend](group__queue__apis.md#gacf3dba40125073c11075e5a134919f88)

int32\_t k\_queue\_alloc\_prepend(struct k\_queue \*queue, void \*data)

Prepend an element to a queue.

[k\_lifo](structk__lifo.md)

**Definition** kernel.h:2630

Add an element to a LIFO queue.

This routine adds a data item to *lifo*. There is an implicit memory allocation to create an additional temporary bookkeeping data structure from the calling thread's resource pool, which is automatically freed when the item is removed. The data itself is not copied.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | lifo | Address of the LIFO. |
    | --- | --- |
    | data | Address of the data item. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOMEM | if there isn't sufficient RAM in the caller's resource pool |

## [◆ ](#gaebd450d4181f22491623ea0aed6ee576)K\_LIFO\_DEFINE

| #define K\_LIFO\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([k\_lifo](structk__lifo.md), name) = \

Z\_LIFO\_INITIALIZER(name)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Statically define and initialize a LIFO queue.

The LIFO queue can be accessed outside the module where it is defined using:

extern struct [k\_lifo](structk__lifo.md) <name>;

Parameters
:   | name | Name of the fifo. |
    | --- | --- |

## [◆ ](#gad5f1775947b07a2a77f667aa9e41db5a)k\_lifo\_get

| #define k\_lifo\_get | ( |  | *lifo*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_lifo](structk__lifo.md), get, lifo, timeout); \

void \*lg\_ret = [k\_queue\_get](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)(&(lifo)->\_queue, timeout); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_lifo](structk__lifo.md), get, lifo, timeout, lg\_ret); \

lg\_ret; \

})

[k\_queue\_get](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619)

void \* k\_queue\_get(struct k\_queue \*queue, k\_timeout\_t timeout)

Get an element from a queue.

Get an element from a LIFO queue.

This routine removes a data item from *LIFO* in a "last in, first out" manner. The first word of the data item is reserved for the kernel's use.

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | lifo | Address of the LIFO queue. |
    | --- | --- |
    | timeout | Waiting period to obtain a data item, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Returns
:   Address of the data item if successful; NULL if returned without waiting, or waiting period timed out.

## [◆ ](#ga69fb19716a9014f7de79f8e524d64a3e)k\_lifo\_init

| #define k\_lifo\_init | ( |  | *lifo* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_lifo](structk__lifo.md), init, lifo); \

k\_queue\_init(&(lifo)->\_queue); \

K\_OBJ\_CORE\_INIT([K\_OBJ\_CORE](group__obj__core__apis.md#ga2bd0c2c121afc09448926a3648c7d814)(lifo), \_obj\_type\_lifo); \

K\_OBJ\_CORE\_LINK([K\_OBJ\_CORE](group__obj__core__apis.md#ga2bd0c2c121afc09448926a3648c7d814)(lifo)); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_lifo](structk__lifo.md), init, lifo); \

})

[K\_OBJ\_CORE](group__obj__core__apis.md#ga2bd0c2c121afc09448926a3648c7d814)

#define K\_OBJ\_CORE(kobj)

Convert kernel object pointer into its object core pointer.

**Definition** obj\_core.h:21

Initialize a LIFO queue.

This routine initializes a LIFO queue object, prior to its first use.

Parameters
:   | lifo | Address of the LIFO queue. |
    | --- | --- |

## [◆ ](#gad662e36b1df8b9013e2dc61f9dfe3a8b)k\_lifo\_put

| #define k\_lifo\_put | ( |  | *lifo*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

({ \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER([k\_lifo](structk__lifo.md), put, lifo, data); \

k\_queue\_prepend(&(lifo)->\_queue, data); \

SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT([k\_lifo](structk__lifo.md), put, lifo, data); \

})

Add an element to a LIFO queue.

This routine adds a data item to *lifo*. A LIFO queue data item must be aligned on a word boundary, and the first word of the item is reserved for the kernel's use.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | lifo | Address of the LIFO queue. |
    | --- | --- |
    | data | Address of the data item. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
