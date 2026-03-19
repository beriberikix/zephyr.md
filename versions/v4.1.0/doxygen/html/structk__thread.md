---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__thread.html
original_path: doxygen/html/structk__thread.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_thread Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Thread APIs](group__thread__apis.md)

Thread Structure.
[More...](#details)

`#include <[thread.h](kernel_2thread_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct \_thread\_base | [base](#a09a988f143ab5c4df887894920ff9df8) |
| struct \_callee\_saved | [callee\_saved](#ae804efd7a191ed1022dd2cf5f588b0ef) |
|  | defined by the architecture, but all archs need these |
| void \* | [init\_data](#a315fe3ad42c5c4c15d4596e6ceaf0694) |
|  | static thread init data |
| \_wait\_q\_t | [join\_queue](#aa8c560f5fbaf6cd551be99d491e654f6) |
|  | threads waiting in [k\_thread\_join()](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233 "Sleep until a thread exits.") |
| struct \_\_thread\_entry | [entry](#a63d78888376893fe0bdb485c5f114e03) |
|  | thread entry and parameters description |
| struct [k\_thread](structk__thread.md) \* | [next\_thread](#a0f0bf272e21ad4709082631a34a8b240) |
|  | next item in list of all threads |
| void \* | [custom\_data](#a459150bfd58cfb97eca88730eab7f325) |
|  | crude thread-local storage |
| struct \_thread\_stack\_info | [stack\_info](#a8be452e7b016fc901adad8518d7fe518) |
|  | Stack Info. |
| struct \_mem\_domain\_info | [mem\_domain\_info](#ab2fe91c58940a2f9d9cb7a30aa91cc55) |
|  | memory domain info of the thread |
| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | [stack\_obj](#a40103270ef1e99a43e544b9a6737e96c) |
|  | Base address of thread stack. |
| void \* | [syscall\_frame](#a7a6114f1bf7993ad7f80a26f71e7a230) |
|  | current syscall frame pointer |
| int | [swap\_retval](#ae4cbe01f267cc15663c84c03d80aa3c1) |
|  | z\_swap() return value |
| void \* | [switch\_handle](#a351c093c8f32f66ab62f364b477128c4) |
|  | Context handle returned via [arch\_switch()](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025 "Cooperative context switch primitive."). |
| struct [k\_heap](structk__heap.md) \* | [resource\_pool](#a35b859bded3a270f25ccc40efece7583) |
|  | resource pool |
| \_wait\_q\_t | [halt\_queue](#ab74f57fca0665fdd599f4f7c51a5d004) |
|  | threads waiting in [k\_thread\_suspend()](group__thread__apis.md#ga66cf8682fb65870eceb5e57d667a8d4e "Suspend a thread.") |
| struct \_thread\_arch | [arch](#a0fa3dd64d03f6eef06320b51b0623301) |
|  | arch-specifics: must always be at the end |

## Detailed Description

Thread Structure.

## Field Documentation

## [◆ ](#a0fa3dd64d03f6eef06320b51b0623301)arch

| struct \_thread\_arch k\_thread::arch |
| --- |

arch-specifics: must always be at the end

## [◆ ](#a09a988f143ab5c4df887894920ff9df8)base

| struct \_thread\_base k\_thread::base |
| --- |

## [◆ ](#ae804efd7a191ed1022dd2cf5f588b0ef)callee\_saved

| struct \_callee\_saved k\_thread::callee\_saved |
| --- |

defined by the architecture, but all archs need these

## [◆ ](#a459150bfd58cfb97eca88730eab7f325)custom\_data

| void\* k\_thread::custom\_data |
| --- |

crude thread-local storage

## [◆ ](#a63d78888376893fe0bdb485c5f114e03)entry

| struct \_\_thread\_entry k\_thread::entry |
| --- |

thread entry and parameters description

## [◆ ](#ab74f57fca0665fdd599f4f7c51a5d004)halt\_queue

| \_wait\_q\_t k\_thread::halt\_queue |
| --- |

threads waiting in [k\_thread\_suspend()](group__thread__apis.md#ga66cf8682fb65870eceb5e57d667a8d4e "Suspend a thread.")

## [◆ ](#a315fe3ad42c5c4c15d4596e6ceaf0694)init\_data

| void\* k\_thread::init\_data |
| --- |

static thread init data

## [◆ ](#aa8c560f5fbaf6cd551be99d491e654f6)join\_queue

| \_wait\_q\_t k\_thread::join\_queue |
| --- |

threads waiting in [k\_thread\_join()](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233 "Sleep until a thread exits.")

## [◆ ](#ab2fe91c58940a2f9d9cb7a30aa91cc55)mem\_domain\_info

| struct \_mem\_domain\_info k\_thread::mem\_domain\_info |
| --- |

memory domain info of the thread

## [◆ ](#a0f0bf272e21ad4709082631a34a8b240)next\_thread

| struct [k\_thread](structk__thread.md)\* k\_thread::next\_thread |
| --- |

next item in list of all threads

## [◆ ](#a35b859bded3a270f25ccc40efece7583)resource\_pool

| struct [k\_heap](structk__heap.md)\* k\_thread::resource\_pool |
| --- |

resource pool

## [◆ ](#a8be452e7b016fc901adad8518d7fe518)stack\_info

| struct \_thread\_stack\_info k\_thread::stack\_info |
| --- |

Stack Info.

## [◆ ](#a40103270ef1e99a43e544b9a6737e96c)stack\_obj

| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)\* k\_thread::stack\_obj |
| --- |

Base address of thread stack.

If memory mapped stack (CONFIG\_THREAD\_STACK\_MEM\_MAPPED) is enabled, this is the physical address of the stack.

## [◆ ](#ae4cbe01f267cc15663c84c03d80aa3c1)swap\_retval

| int k\_thread::swap\_retval |
| --- |

z\_swap() return value

## [◆ ](#a351c093c8f32f66ab62f364b477128c4)switch\_handle

| void\* k\_thread::switch\_handle |
| --- |

Context handle returned via [arch\_switch()](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025 "Cooperative context switch primitive.").

## [◆ ](#a7a6114f1bf7993ad7f80a26f71e7a230)syscall\_frame

| void\* k\_thread::syscall\_frame |
| --- |

current syscall frame pointer

---

The documentation for this struct was generated from the following file:

- zephyr/kernel/[thread.h](kernel_2thread_8h_source.md)

- [k\_thread](structk__thread.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
