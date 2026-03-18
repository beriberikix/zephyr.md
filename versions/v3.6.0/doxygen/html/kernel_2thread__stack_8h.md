---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kernel_2thread__stack_8h.html
original_path: doxygen/html/kernel_2thread__stack_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_stack.h File Reference

Macros for declaring thread stacks.
[More...](#details)

`#include <zephyr/arch/cpu.h>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](kernel_2thread__stack_8h_source.md)

| Macros | |
| --- | --- |
| #define | [K\_KERNEL\_STACK\_RESERVED](#aa66525a4ec83e91d97ec4699acaa72fd)   (([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9))0) |
| #define | [K\_KERNEL\_STACK\_DECLARE](group__thread__stack__api.md#ga1ba82b0f3abe9c573930ea73e9ed528e)(sym, size) |
|  | Declare a reference to a thread stack. |
| #define | [K\_KERNEL\_STACK\_ARRAY\_DECLARE](group__thread__stack__api.md#gae7562ba4ce258964c7f28eb0611d1b75)(sym, nmemb, size) |
|  | Declare a reference to a thread stack array. |
| #define | [K\_KERNEL\_PINNED\_STACK\_ARRAY\_DECLARE](group__thread__stack__api.md#gaaf146fa0dc43938d7ac4a8d2e79b673d)(sym, nmemb, size) |
|  | Declare a reference to a pinned thread stack array. |
| #define | [K\_KERNEL\_STACK\_DEFINE](group__thread__stack__api.md#ga9e05e3cb5aa5b72d6f19e2f327313271)(sym, size) |
|  | Define a toplevel kernel stack memory region. |
| #define | [K\_KERNEL\_PINNED\_STACK\_DEFINE](group__thread__stack__api.md#ga7f6a9e1bd5f99b5240c69d372bfd4aa0)(sym, size) |
|  | Define a toplevel kernel stack memory region in pinned section. |
| #define | [K\_KERNEL\_STACK\_ARRAY\_DEFINE](group__thread__stack__api.md#gaf05127bd2ab7e8a0aeb394f18cbd923a)(sym, nmemb, size) |
|  | Define a toplevel array of kernel stack memory regions. |
| #define | [K\_KERNEL\_PINNED\_STACK\_ARRAY\_DEFINE](group__thread__stack__api.md#ga628f79ffde2cc43cf7b5525e5f4276df)(sym, nmemb, size) |
|  | Define a toplevel array of kernel stack memory regions in pinned section. |
| #define | [K\_KERNEL\_STACK\_MEMBER](group__thread__stack__api.md#ga600162959def399e70310b944834711f)(sym, size) |
|  | Define an embedded stack memory region. |
| #define | [K\_KERNEL\_STACK\_SIZEOF](group__thread__stack__api.md#ga57b3824b117c634dbb6052d47dc4301c)(sym) |
| #define | [K\_THREAD\_STACK\_RESERVED](#a025b257739ad52fe7106585b51468e49)   (([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9))0U) |
|  | Indicate how much additional memory is reserved for stack objects. |
| #define | [K\_THREAD\_STACK\_DECLARE](group__thread__stack__api.md#gab42c634630b892599bdf797e65563a83)(sym, size) |
|  | Declare a reference to a thread stack. |
| #define | [K\_THREAD\_STACK\_ARRAY\_DECLARE](group__thread__stack__api.md#ga9c7578df16dfbd9067ee2a6ec5fc0ab6)(sym, nmemb, size) |
|  | Declare a reference to a thread stack array. |
| #define | [K\_THREAD\_STACK\_SIZEOF](group__thread__stack__api.md#ga775f8e6b4144cfdd24f3261b6db64150)(sym) |
|  | Return the size in bytes of a stack memory region. |
| #define | [K\_THREAD\_STACK\_DEFINE](group__thread__stack__api.md#gac5368ce24fdeab3863b5c8dee2ebd955)(sym, size) |
|  | Define a toplevel thread stack memory region. |
| #define | [K\_THREAD\_PINNED\_STACK\_DEFINE](group__thread__stack__api.md#ga7227f78410cf126deb5b185a0534f7f3)(sym, size) |
|  | Define a toplevel thread stack memory region in pinned section. |
| #define | [K\_THREAD\_STACK\_LEN](group__thread__stack__api.md#ga72fa31a9d8e28ccabd6e5e908a24ec00)(size) |
|  | Calculate size of stacks to be allocated in a stack array. |
| #define | [K\_THREAD\_STACK\_ARRAY\_DEFINE](group__thread__stack__api.md#gaae2471b24bdc574382f083163fb42597)(sym, nmemb, size) |
|  | Define a toplevel array of thread stack memory regions. |
| #define | [K\_THREAD\_PINNED\_STACK\_ARRAY\_DEFINE](group__thread__stack__api.md#gaa2e5014926e11e2241141cdd82888b09)(sym, nmemb, size) |
|  | Define a toplevel array of thread stack memory regions in pinned section. |
| #define | [K\_THREAD\_STACK\_MEMBER](group__thread__stack__api.md#ga753188e7f124f0ee03ed0fa1dad8ecfb)(sym, size) |
|  | Define an embedded stack memory region. |

## Detailed Description

Macros for declaring thread stacks.

## Macro Definition Documentation

## [◆ ](#aa66525a4ec83e91d97ec4699acaa72fd)K\_KERNEL\_STACK\_RESERVED

| #define K\_KERNEL\_STACK\_RESERVED   (([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9))0) |
| --- |

## [◆ ](#a025b257739ad52fe7106585b51468e49)K\_THREAD\_STACK\_RESERVED

| #define K\_THREAD\_STACK\_RESERVED   (([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9))0U) |
| --- |

Indicate how much additional memory is reserved for stack objects.

Any given stack declaration may have additional memory in it for guard areas, supervisor mode stacks, or platform-specific data. This macro indicates how much space is reserved for this.

This value only indicates memory that is permanently reserved in the stack object. Memory that is "borrowed" from the thread's stack buffer is never accounted for here.

Reserved memory is at the beginning of the stack object. The reserved area must be appropriately sized such that the stack buffer immediately following it is correctly aligned.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [thread\_stack.h](kernel_2thread__stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
