---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__thread__stack__api.html
original_path: doxygen/html/group__thread__stack__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Thread Stack APIs

[Kernel APIs](group__kernel__apis.md)

Thread Stack APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [K\_KERNEL\_STACK\_DECLARE](#ga1ba82b0f3abe9c573930ea73e9ed528e)(sym, size) |
|  | Declare a reference to a thread stack. |
| #define | [K\_KERNEL\_STACK\_ARRAY\_DECLARE](#gae7562ba4ce258964c7f28eb0611d1b75)(sym, nmemb, size) |
|  | Declare a reference to a thread stack array. |
| #define | [K\_KERNEL\_PINNED\_STACK\_ARRAY\_DECLARE](#gaaf146fa0dc43938d7ac4a8d2e79b673d)(sym, nmemb, size) |
|  | Declare a reference to a pinned thread stack array. |
| #define | [K\_KERNEL\_STACK\_DEFINE](#ga9e05e3cb5aa5b72d6f19e2f327313271)(sym, size) |
|  | Define a toplevel kernel stack memory region. |
| #define | [K\_KERNEL\_PINNED\_STACK\_DEFINE](#ga7f6a9e1bd5f99b5240c69d372bfd4aa0)(sym, size) |
|  | Define a toplevel kernel stack memory region in pinned section. |
| #define | [K\_KERNEL\_STACK\_ARRAY\_DEFINE](#gaf05127bd2ab7e8a0aeb394f18cbd923a)(sym, nmemb, size) |
|  | Define a toplevel array of kernel stack memory regions. |
| #define | [K\_KERNEL\_PINNED\_STACK\_ARRAY\_DEFINE](#ga628f79ffde2cc43cf7b5525e5f4276df)(sym, nmemb, size) |
|  | Define a toplevel array of kernel stack memory regions in pinned section. |
| #define | [K\_KERNEL\_STACK\_MEMBER](#ga600162959def399e70310b944834711f)(sym, size) |
|  | Define an embedded stack memory region. |
| #define | [K\_KERNEL\_STACK\_SIZEOF](#ga57b3824b117c634dbb6052d47dc4301c)(sym) |
| #define | [K\_THREAD\_STACK\_DECLARE](#gab42c634630b892599bdf797e65563a83)(sym, size) |
|  | Declare a reference to a thread stack. |
| #define | [K\_THREAD\_STACK\_ARRAY\_DECLARE](#ga9c7578df16dfbd9067ee2a6ec5fc0ab6)(sym, nmemb, size) |
|  | Declare a reference to a thread stack array. |
| #define | [K\_THREAD\_STACK\_SIZEOF](#ga775f8e6b4144cfdd24f3261b6db64150)(sym) |
|  | Return the size in bytes of a stack memory region. |
| #define | [K\_THREAD\_STACK\_DEFINE](#gac5368ce24fdeab3863b5c8dee2ebd955)(sym, size) |
|  | Define a toplevel thread stack memory region. |
| #define | [K\_THREAD\_PINNED\_STACK\_DEFINE](#ga7227f78410cf126deb5b185a0534f7f3)(sym, size) |
|  | Define a toplevel thread stack memory region in pinned section. |
| #define | [K\_THREAD\_STACK\_LEN](#ga72fa31a9d8e28ccabd6e5e908a24ec00)(size) |
|  | Calculate size of stacks to be allocated in a stack array. |
| #define | [K\_THREAD\_STACK\_ARRAY\_DEFINE](#gaae2471b24bdc574382f083163fb42597)(sym, nmemb, size) |
|  | Define a toplevel array of thread stack memory regions. |
| #define | [K\_THREAD\_PINNED\_STACK\_ARRAY\_DEFINE](#gaa2e5014926e11e2241141cdd82888b09)(sym, nmemb, size) |
|  | Define a toplevel array of thread stack memory regions in pinned section. |

## Detailed Description

Thread Stack APIs.

## Macro Definition Documentation

## [◆ ](#gaaf146fa0dc43938d7ac4a8d2e79b673d)K\_KERNEL\_PINNED\_STACK\_ARRAY\_DECLARE

| #define K\_KERNEL\_PINNED\_STACK\_ARRAY\_DECLARE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *nmemb*, |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

extern struct z\_thread\_stack\_element \

sym[nmemb][[K\_KERNEL\_STACK\_LEN](kernel_2thread__stack_8h.md#a12f78cb2d5b9bf83068e810bf1e31937)(size)]

[K\_KERNEL\_STACK\_LEN](kernel_2thread__stack_8h.md#a12f78cb2d5b9bf83068e810bf1e31937)

#define K\_KERNEL\_STACK\_LEN(size)

**Definition** thread\_stack.h:107

Declare a reference to a pinned thread stack array.

This macro declares the symbol of a pinned thread stack array defined elsewhere in the current scope.

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | nmemb | Number of stacks defined |
    | size | Size of the stack memory region |

## [◆ ](#ga628f79ffde2cc43cf7b5525e5f4276df)K\_KERNEL\_PINNED\_STACK\_ARRAY\_DEFINE

| #define K\_KERNEL\_PINNED\_STACK\_ARRAY\_DEFINE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *nmemb*, |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

Z\_KERNEL\_STACK\_ARRAY\_DEFINE\_IN(sym, nmemb, size, \_\_kstackmem)

Define a toplevel array of kernel stack memory regions in pinned section.

See [K\_KERNEL\_STACK\_ARRAY\_DEFINE()](#gaf05127bd2ab7e8a0aeb394f18cbd923a) for more information and constraints.

This puts the stack into the pinned noinit linker section if CONFIG\_LINKER\_USE\_PINNED\_SECTION is enabled, or else it would put the stack into the same section as [K\_KERNEL\_STACK\_ARRAY\_DEFINE()](#gaf05127bd2ab7e8a0aeb394f18cbd923a).

Parameters
:   | sym | Kernel stack array symbol name |
    | --- | --- |
    | nmemb | Number of stacks to define |
    | size | Size of the stack memory region |

## [◆ ](#ga7f6a9e1bd5f99b5240c69d372bfd4aa0)K\_KERNEL\_PINNED\_STACK\_DEFINE

| #define K\_KERNEL\_PINNED\_STACK\_DEFINE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

Z\_KERNEL\_STACK\_DEFINE\_IN(sym, size, \_\_kstackmem)

Define a toplevel kernel stack memory region in pinned section.

See [K\_KERNEL\_STACK\_DEFINE()](#ga9e05e3cb5aa5b72d6f19e2f327313271) for more information and constraints.

This puts the stack into the pinned noinit linker section if CONFIG\_LINKER\_USE\_PINNED\_SECTION is enabled, or else it would put the stack into the same section as [K\_KERNEL\_STACK\_DEFINE()](#ga9e05e3cb5aa5b72d6f19e2f327313271).

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | size | Size of the stack memory region |

## [◆ ](#gae7562ba4ce258964c7f28eb0611d1b75)K\_KERNEL\_STACK\_ARRAY\_DECLARE

| #define K\_KERNEL\_STACK\_ARRAY\_DECLARE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *nmemb*, |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

extern struct z\_thread\_stack\_element \

sym[nmemb][[K\_KERNEL\_STACK\_LEN](kernel_2thread__stack_8h.md#a12f78cb2d5b9bf83068e810bf1e31937)(size)]

Declare a reference to a thread stack array.

This macro declares the symbol of a thread stack array defined elsewhere in the current scope.

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | nmemb | Number of stacks defined |
    | size | Size of the stack memory region |

## [◆ ](#gaf05127bd2ab7e8a0aeb394f18cbd923a)K\_KERNEL\_STACK\_ARRAY\_DEFINE

| #define K\_KERNEL\_STACK\_ARRAY\_DEFINE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *nmemb*, |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

Z\_KERNEL\_STACK\_ARRAY\_DEFINE\_IN(sym, nmemb, size, \_\_kstackmem)

Define a toplevel array of kernel stack memory regions.

Stacks defined with this macro may not host user mode threads.

Parameters
:   | sym | Kernel stack array symbol name |
    | --- | --- |
    | nmemb | Number of stacks to define |
    | size | Size of the stack memory region |

## [◆ ](#ga1ba82b0f3abe9c573930ea73e9ed528e)K\_KERNEL\_STACK\_DECLARE

| #define K\_KERNEL\_STACK\_DECLARE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

extern struct z\_thread\_stack\_element \

sym[[K\_KERNEL\_STACK\_LEN](kernel_2thread__stack_8h.md#a12f78cb2d5b9bf83068e810bf1e31937)(size)]

Declare a reference to a thread stack.

This macro declares the symbol of a thread stack defined elsewhere in the current scope.

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | size | Size of the stack memory region |

## [◆ ](#ga9e05e3cb5aa5b72d6f19e2f327313271)K\_KERNEL\_STACK\_DEFINE

| #define K\_KERNEL\_STACK\_DEFINE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

Z\_KERNEL\_STACK\_DEFINE\_IN(sym, size, \_\_kstackmem)

Define a toplevel kernel stack memory region.

This defines a region of memory for use as a thread stack, for threads that exclusively run in supervisor mode. This is also suitable for declaring special stacks for interrupt or exception handling.

Stacks defined with this macro may not host user mode threads.

It is legal to precede this definition with the 'static' keyword.

It is NOT legal to take the sizeof(sym) and pass that to the stackSize parameter of [k\_thread\_create()](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "Create a thread."), it may not be the same as the 'size' parameter. Use [K\_KERNEL\_STACK\_SIZEOF()](#ga57b3824b117c634dbb6052d47dc4301c) instead.

The total amount of memory allocated may be increased to accommodate fixed-size stack overflow guards.

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | size | Size of the stack memory region |

## [◆ ](#ga600162959def399e70310b944834711f)K\_KERNEL\_STACK\_MEMBER

| #define K\_KERNEL\_STACK\_MEMBER | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

Z\_KERNEL\_STACK\_DEFINE\_IN(sym, size,)

Define an embedded stack memory region.

Used for kernel stacks embedded within other data structures.

Stacks defined with this macro may not host user mode threads.

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | size | Size of the stack memory region |

## [◆ ](#ga57b3824b117c634dbb6052d47dc4301c)K\_KERNEL\_STACK\_SIZEOF

| #define K\_KERNEL\_STACK\_SIZEOF | ( |  | *sym* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

(sizeof(sym) - [K\_KERNEL\_STACK\_RESERVED](kernel_2thread__stack_8h.md#aa66525a4ec83e91d97ec4699acaa72fd))

[K\_KERNEL\_STACK\_RESERVED](kernel_2thread__stack_8h.md#aa66525a4ec83e91d97ec4699acaa72fd)

#define K\_KERNEL\_STACK\_RESERVED

**Definition** thread\_stack.h:94

## [◆ ](#gaa2e5014926e11e2241141cdd82888b09)K\_THREAD\_PINNED\_STACK\_ARRAY\_DEFINE

| #define K\_THREAD\_PINNED\_STACK\_ARRAY\_DEFINE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *nmemb*, |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

[K\_THREAD\_STACK\_ARRAY\_DEFINE](#gaae2471b24bdc574382f083163fb42597)(sym, nmemb, size)

[K\_THREAD\_STACK\_ARRAY\_DEFINE](#gaae2471b24bdc574382f083163fb42597)

#define K\_THREAD\_STACK\_ARRAY\_DEFINE(sym, nmemb, size)

Define a toplevel array of thread stack memory regions.

**Definition** thread\_stack.h:587

Define a toplevel array of thread stack memory regions in pinned section.

Create an array of equally sized stacks. See K\_THREAD\_STACK\_DEFINE definition for additional details and constraints.

This is the generic, historical definition. Align to Z\_THREAD\_STACK\_OBJ\_ALIGN and put in 'noinit' section so that it isn't zeroed at boot

This puts the stack into the pinned noinit linker section if CONFIG\_LINKER\_USE\_PINNED\_SECTION is enabled, or else it would put the stack into the same section as [K\_THREAD\_STACK\_DEFINE()](#gac5368ce24fdeab3863b5c8dee2ebd955).

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | nmemb | Number of stacks to define |
    | size | Size of the stack memory region |

## [◆ ](#ga7227f78410cf126deb5b185a0534f7f3)K\_THREAD\_PINNED\_STACK\_DEFINE

| #define K\_THREAD\_PINNED\_STACK\_DEFINE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

[K\_THREAD\_STACK\_DEFINE](#gac5368ce24fdeab3863b5c8dee2ebd955)(sym, size)

[K\_THREAD\_STACK\_DEFINE](#gac5368ce24fdeab3863b5c8dee2ebd955)

#define K\_THREAD\_STACK\_DEFINE(sym, size)

Define a toplevel thread stack memory region.

**Definition** thread\_stack.h:516

Define a toplevel thread stack memory region in pinned section.

This defines a region of memory suitable for use as a thread's stack.

This is the generic, historical definition. Align to Z\_THREAD\_STACK\_OBJ\_ALIGN and put in 'noinit' section so that it isn't zeroed at boot

The defined symbol will always be a [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1 "Typedef of struct z_thread_stack_element.") which can be passed to [k\_thread\_create()](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "Create a thread."), but should otherwise not be manipulated. If the buffer inside needs to be examined, examine thread->stack\_info for the associated thread object to obtain the boundaries.

It is legal to precede this definition with the 'static' keyword.

It is NOT legal to take the sizeof(sym) and pass that to the stackSize parameter of [k\_thread\_create()](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "Create a thread."), it may not be the same as the 'size' parameter. Use [K\_THREAD\_STACK\_SIZEOF()](#ga775f8e6b4144cfdd24f3261b6db64150) instead.

Some arches may round the size of the usable stack region up to satisfy alignment constraints. [K\_THREAD\_STACK\_SIZEOF()](#ga775f8e6b4144cfdd24f3261b6db64150) will return the aligned size.

This puts the stack into the pinned noinit linker section if CONFIG\_LINKER\_USE\_PINNED\_SECTION is enabled, or else it would put the stack into the same section as [K\_THREAD\_STACK\_DEFINE()](#gac5368ce24fdeab3863b5c8dee2ebd955).

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | size | Size of the stack memory region |

## [◆ ](#ga9c7578df16dfbd9067ee2a6ec5fc0ab6)K\_THREAD\_STACK\_ARRAY\_DECLARE

| #define K\_THREAD\_STACK\_ARRAY\_DECLARE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *nmemb*, |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

extern struct z\_thread\_stack\_element \

sym[nmemb][[K\_THREAD\_STACK\_LEN](#ga72fa31a9d8e28ccabd6e5e908a24ec00)(size)]

[K\_THREAD\_STACK\_LEN](#ga72fa31a9d8e28ccabd6e5e908a24ec00)

#define K\_THREAD\_STACK\_LEN(size)

Calculate size of stacks to be allocated in a stack array.

**Definition** thread\_stack.h:570

Declare a reference to a thread stack array.

This macro declares the symbol of a thread stack array defined elsewhere in the current scope.

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | nmemb | Number of stacks defined |
    | size | Size of the stack memory region |

## [◆ ](#gaae2471b24bdc574382f083163fb42597)K\_THREAD\_STACK\_ARRAY\_DEFINE

| #define K\_THREAD\_STACK\_ARRAY\_DEFINE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *nmemb*, |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

Z\_THREAD\_STACK\_ARRAY\_DEFINE\_IN(sym, nmemb, size, \_\_stackmem)

Define a toplevel array of thread stack memory regions.

Create an array of equally sized stacks. See K\_THREAD\_STACK\_DEFINE definition for additional details and constraints.

This is the generic, historical definition. Align to Z\_THREAD\_STACK\_OBJ\_ALIGN and put in 'noinit' section so that it isn't zeroed at boot

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | nmemb | Number of stacks to define |
    | size | Size of the stack memory region |

## [◆ ](#gab42c634630b892599bdf797e65563a83)K\_THREAD\_STACK\_DECLARE

| #define K\_THREAD\_STACK\_DECLARE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

extern struct z\_thread\_stack\_element \

sym[[K\_THREAD\_STACK\_LEN](#ga72fa31a9d8e28ccabd6e5e908a24ec00)(size)]

Declare a reference to a thread stack.

This macro declares the symbol of a thread stack defined elsewhere in the current scope.

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | size | Size of the stack memory region |

## [◆ ](#gac5368ce24fdeab3863b5c8dee2ebd955)K\_THREAD\_STACK\_DEFINE

| #define K\_THREAD\_STACK\_DEFINE | ( |  | *sym*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

Z\_THREAD\_STACK\_DEFINE\_IN(sym, size, \_\_stackmem)

Define a toplevel thread stack memory region.

This defines a region of memory suitable for use as a thread's stack.

This is the generic, historical definition. Align to Z\_THREAD\_STACK\_OBJ\_ALIGN and put in 'noinit' section so that it isn't zeroed at boot

The defined symbol will always be a [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1 "Typedef of struct z_thread_stack_element.") which can be passed to [k\_thread\_create()](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "Create a thread."), but should otherwise not be manipulated. If the buffer inside needs to be examined, examine thread->stack\_info for the associated thread object to obtain the boundaries.

It is legal to precede this definition with the 'static' keyword.

It is NOT legal to take the sizeof(sym) and pass that to the stackSize parameter of [k\_thread\_create()](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "Create a thread."), it may not be the same as the 'size' parameter. Use [K\_THREAD\_STACK\_SIZEOF()](#ga775f8e6b4144cfdd24f3261b6db64150) instead.

Some arches may round the size of the usable stack region up to satisfy alignment constraints. [K\_THREAD\_STACK\_SIZEOF()](#ga775f8e6b4144cfdd24f3261b6db64150) will return the aligned size.

Parameters
:   | sym | Thread stack symbol name |
    | --- | --- |
    | size | Size of the stack memory region |

## [◆ ](#ga72fa31a9d8e28ccabd6e5e908a24ec00)K\_THREAD\_STACK\_LEN

| #define K\_THREAD\_STACK\_LEN | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(Z\_THREAD\_STACK\_SIZE\_ADJUST(size), \

Z\_THREAD\_STACK\_OBJ\_ALIGN(size))

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:322

Calculate size of stacks to be allocated in a stack array.

This macro calculates the size to be allocated for the stacks inside a stack array. It accepts the indicated "size" as a parameter and if required, pads some extra bytes (e.g. for MPU scenarios). Refer K\_THREAD\_STACK\_ARRAY\_DEFINE definition to see how this is used. The returned size ensures each array member will be aligned to the required stack base alignment.

Parameters
:   | size | Size of the stack memory region |
    | --- | --- |

Returns
:   Appropriate size for an array member

## [◆ ](#ga775f8e6b4144cfdd24f3261b6db64150)K\_THREAD\_STACK\_SIZEOF

| #define K\_THREAD\_STACK\_SIZEOF | ( |  | *sym* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[thread_stack.h](kernel_2thread__stack_8h.md)>`

**Value:**

(sizeof(sym) - [K\_THREAD\_STACK\_RESERVED](kernel_2thread__stack_8h.md#a025b257739ad52fe7106585b51468e49))

[K\_THREAD\_STACK\_RESERVED](kernel_2thread__stack_8h.md#a025b257739ad52fe7106585b51468e49)

#define K\_THREAD\_STACK\_RESERVED

Indicate how much additional memory is reserved for stack objects.

**Definition** thread\_stack.h:321

Return the size in bytes of a stack memory region.

Convenience macro for passing the desired stack size to [k\_thread\_create()](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "Create a thread.") since the underlying implementation may actually create something larger (for instance a guard area).

The value returned here is not guaranteed to match the 'size' parameter passed to K\_THREAD\_STACK\_DEFINE and may be larger, but is always safe to pass to [k\_thread\_create()](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "Create a thread.") for the associated stack object.

Parameters
:   | sym | Stack memory symbol |
    | --- | --- |

Returns
:   Size of the stack buffer

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
