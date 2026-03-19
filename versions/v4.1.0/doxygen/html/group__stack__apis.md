---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__stack__apis.html
original_path: doxygen/html/group__stack__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Stack APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [K\_STACK\_DEFINE](#ga8c9ca77e5de3c9757dcd4ecb55797835)(name, stack\_num\_entries) |
|  | Statically define and initialize a stack. |

| Functions | |
| --- | --- |
| void | [k\_stack\_init](#ga4400a39ef48289305cf66a092d5c6c7d) (struct k\_stack \*stack, stack\_data\_t \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_entries) |
|  | Initialize a stack. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_stack\_alloc\_init](#gab97d924db1aef3f6adade156a107d45c) (struct k\_stack \*stack, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_entries) |
|  | Initialize a stack. |
| int | [k\_stack\_cleanup](#ga819f4e7b2cf11cf2e1b80933fdcb67ea) (struct k\_stack \*stack) |
|  | Release a stack's allocated buffer. |
| int | [k\_stack\_push](#gaa6180f4db6ec93ee84149cba054d3e53) (struct k\_stack \*stack, stack\_data\_t data) |
|  | Push an element onto a stack. |
| int | [k\_stack\_pop](#ga36ce6ceb9ea3d5c36d22b10430789480) (struct k\_stack \*stack, stack\_data\_t \*data, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Pop an element from a stack. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga8c9ca77e5de3c9757dcd4ecb55797835)K\_STACK\_DEFINE

| #define K\_STACK\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *stack\_num\_entries* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

stack\_data\_t \_\_noinit \

\_k\_stack\_buf\_##name[stack\_num\_entries]; \

STRUCT\_SECTION\_ITERABLE(k\_stack, name) = \

Z\_STACK\_INITIALIZER(name, \_k\_stack\_buf\_##name, \

stack\_num\_entries)

Statically define and initialize a stack.

The stack can be accessed outside the module where it is defined using:

extern struct k\_stack <name>;

Parameters
:   | name | Name of the stack. |
    | --- | --- |
    | stack\_num\_entries | Maximum number of values that can be stacked. |

## Function Documentation

## [◆ ](#gab97d924db1aef3f6adade156a107d45c)k\_stack\_alloc\_init()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) k\_stack\_alloc\_init | ( | struct k\_stack \* | *stack*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_entries* ) |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a stack.

This routine initializes a stack object, prior to its first use. Internal buffers will be allocated from the calling thread's resource pool. This memory will be released if [k\_stack\_cleanup()](#ga819f4e7b2cf11cf2e1b80933fdcb67ea) is called, or userspace is enabled and the stack object loses all references to it.

Parameters
:   | stack | Address of the stack. |
    | --- | --- |
    | num\_entries | Maximum number of values that can be stacked. |

Returns
:   -ENOMEM if memory couldn't be allocated

## [◆ ](#ga819f4e7b2cf11cf2e1b80933fdcb67ea)k\_stack\_cleanup()

| int k\_stack\_cleanup | ( | struct k\_stack \* | *stack* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Release a stack's allocated buffer.

If a stack object was given a dynamically allocated buffer via [k\_stack\_alloc\_init()](#gab97d924db1aef3f6adade156a107d45c), this will free it. This function does nothing if the buffer wasn't dynamically allocated.

Parameters
:   | stack | Address of the stack. |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EAGAIN | when object is still in use |

## [◆ ](#ga4400a39ef48289305cf66a092d5c6c7d)k\_stack\_init()

| void k\_stack\_init | ( | struct k\_stack \* | *stack*, |
| --- | --- | --- | --- |
|  |  | stack\_data\_t \* | *buffer*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_entries* ) |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a stack.

This routine initializes a stack object, prior to its first use.

Parameters
:   | stack | Address of the stack. |
    | --- | --- |
    | buffer | Address of array used to hold stacked values. |
    | num\_entries | Maximum number of values that can be stacked. |

## [◆ ](#ga36ce6ceb9ea3d5c36d22b10430789480)k\_stack\_pop()

| | int k\_stack\_pop | ( | struct k\_stack \* | *stack*, | | --- | --- | --- | --- | |  |  | stack\_data\_t \* | *data*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Pop an element from a stack.

This routine removes a stack\_data\_t value from *stack* in a "last in,
first out" manner and stores the value in *data*.

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.

Function properties (list may not be complete)

Parameters
:   | stack | Address of the stack. |
    | --- | --- |
    | data | Address of area to hold the value popped from the stack. |
    | timeout | Waiting period to obtain a value, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Element popped from stack. |
    | --- | --- |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |

## [◆ ](#gaa6180f4db6ec93ee84149cba054d3e53)k\_stack\_push()

| | int k\_stack\_push | ( | struct k\_stack \* | *stack*, | | --- | --- | --- | --- | |  |  | stack\_data\_t | *data* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Push an element onto a stack.

This routine adds a stack\_data\_t value *data* to *stack*.

Function properties (list may not be complete)

Parameters
:   | stack | Address of the stack. |
    | --- | --- |
    | data | Value to push onto the stack. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOMEM | if stack is full |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
