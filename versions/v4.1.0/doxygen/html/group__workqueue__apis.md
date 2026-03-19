---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__workqueue__apis.html
original_path: doxygen/html/group__workqueue__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Work Queue APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_work](structk__work.md) |
|  | A structure used to submit work. [More...](structk__work.md#details) |
| struct | [k\_work\_delayable](structk__work__delayable.md) |
|  | A structure used to submit work after a delay. [More...](structk__work__delayable.md#details) |
| struct | [k\_work\_sync](structk__work__sync.md) |
|  | A structure holding internal state for a pending synchronous operation on a work item or queue. [More...](structk__work__sync.md#details) |
| struct | [k\_work\_queue\_config](structk__work__queue__config.md) |
|  | A structure holding optional configuration items for a work queue. [More...](structk__work__queue__config.md#details) |
| struct | [k\_work\_q](structk__work__q.md) |
|  | A structure used to hold work until it can be processed. [More...](structk__work__q.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_WORK\_DELAYABLE\_DEFINE](#ga893b281f3d2bc0088650536899e17903)(work, work\_handler) |
|  | Initialize a statically-defined delayable work item. |
| #define | [K\_WORK\_USER\_DEFINE](#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)(work, work\_handler) |
|  | Initialize a statically-defined user work item. |
| #define | [K\_WORK\_DEFINE](#gaf8e003eefa5dd66ba883688f9d39c333)(work, work\_handler) |
|  | Initialize a statically-defined work item. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [k\_work\_handler\_t](#ga5add9ef0dce306a08413c4140fc0bdda)) (struct [k\_work](structk__work.md) \*work) |
|  | The signature for a work item handler function. |
| typedef void(\* | [k\_work\_user\_handler\_t](#gaafa4dfac323cab570da1ee31c07d11bc)) (struct k\_work\_user \*work) |
|  | Work item handler function type for user work queues. |

| Enumerations | |
| --- | --- |
| enum | {     [K\_WORK\_RUNNING](#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165) = BIT(K\_WORK\_RUNNING\_BIT) , [K\_WORK\_CANCELING](#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732) = BIT(K\_WORK\_CANCELING\_BIT) , [K\_WORK\_QUEUED](#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85) = BIT(K\_WORK\_QUEUED\_BIT) , [K\_WORK\_DELAYED](#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed) = BIT(K\_WORK\_DELAYED\_BIT) ,     [K\_WORK\_FLUSHING](#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601) = BIT(K\_WORK\_FLUSHING\_BIT)   } |

| Functions | |
| --- | --- |
| void | [k\_work\_init](#gaf20080884a2893d39cd8e862b34a2a30) (struct [k\_work](structk__work.md) \*work, [k\_work\_handler\_t](#ga5add9ef0dce306a08413c4140fc0bdda) handler) |
|  | Initialize a (non-delayable) work structure. |
| int | [k\_work\_busy\_get](#gaba8a8734768d768b433f9d8490e7df7b) (const struct [k\_work](structk__work.md) \*work) |
|  | Busy state flags from the work item. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_is\_pending](#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0) (const struct [k\_work](structk__work.md) \*work) |
|  | Test whether a work item is currently pending. |
| int | [k\_work\_submit\_to\_queue](#ga5353e76f73db070614f50d06d292d05c) (struct [k\_work\_q](structk__work__q.md) \*queue, struct [k\_work](structk__work.md) \*work) |
|  | Submit a work item to a queue. |
| int | [k\_work\_submit](#gace61b59575093d7442f39ccb7be686d7) (struct [k\_work](structk__work.md) \*work) |
|  | Submit a work item to the system queue. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_flush](#gabd1cda459bab538fb2d6dfd84a73b253) (struct [k\_work](structk__work.md) \*work, struct [k\_work\_sync](structk__work__sync.md) \*sync) |
|  | Wait for last-submitted instance to complete. |
| int | [k\_work\_cancel](#ga389fe2a8fb20f9bd593cf8d990727078) (struct [k\_work](structk__work.md) \*work) |
|  | Cancel a work item. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_cancel\_sync](#gab2b05cfe3af08f7d32c3946fa1c808f9) (struct [k\_work](structk__work.md) \*work, struct [k\_work\_sync](structk__work__sync.md) \*sync) |
|  | Cancel a work item and wait for it to complete. |
| void | [k\_work\_queue\_init](#gada77d818ea9e4d07c14a960872ed5492) (struct [k\_work\_q](structk__work__q.md) \*queue) |
|  | Initialize a work queue structure. |
| void | [k\_work\_queue\_start](#gadfc56554f9bfe7b52309d79660188593) (struct [k\_work\_q](structk__work__q.md) \*queue, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stack\_size, int prio, const struct [k\_work\_queue\_config](structk__work__queue__config.md) \*cfg) |
|  | Initialize a work queue. |
| static [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [k\_work\_queue\_thread\_get](#ga0b8b496f7e7bd82d08590a07293e38d7) (struct [k\_work\_q](structk__work__q.md) \*queue) |
|  | Access the thread that animates a work queue. |
| int | [k\_work\_queue\_drain](#ga0fefe3e0225ac99b47b250849f6cd863) (struct [k\_work\_q](structk__work__q.md) \*queue, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) plug) |
|  | Wait until the work queue has drained, optionally plugging it. |
| int | [k\_work\_queue\_unplug](#gaa0463bb79af3ec470f7d3be02052139f) (struct [k\_work\_q](structk__work__q.md) \*queue) |
|  | Release a work queue to accept new submissions. |
| int | [k\_work\_queue\_stop](#ga1fd2fce94eb731ccb0838ec763e62f5c) (struct [k\_work\_q](structk__work__q.md) \*queue, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Stop a work queue. |
| void | [k\_work\_init\_delayable](#ga2876c5d82fb2340a093bc4d689a55465) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, [k\_work\_handler\_t](#ga5add9ef0dce306a08413c4140fc0bdda) handler) |
|  | Initialize a delayable work structure. |
| static struct [k\_work\_delayable](structk__work__delayable.md) \* | [k\_work\_delayable\_from\_work](#gabcb822a03ce7ea9ee1ed046afe31ffca) (struct [k\_work](structk__work.md) \*work) |
|  | Get the parent delayable work structure from a work pointer. |
| int | [k\_work\_delayable\_busy\_get](#ga1b76969667844f0981d348c9c671bc9f) (const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork) |
|  | Busy state flags from the delayable work item. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_delayable\_is\_pending](#ga66e598dbc73f653cbfec03c21168df2e) (const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork) |
|  | Test whether a delayed work item is currently pending. |
| static [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_work\_delayable\_expires\_get](#ga1772c37bc62b86180d5cf48fe3037624) (const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork) |
|  | Get the absolute tick count at which a scheduled delayable work will be submitted. |
| static [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_work\_delayable\_remaining\_get](#gabce78598a014f3ed87730fe6a9fe61b4) (const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork) |
|  | Get the number of ticks until a scheduled delayable work will be submitted. |
| int | [k\_work\_schedule\_for\_queue](#ga17f863c9f6ff2fb41dc0f3b7de4fdf23) (struct [k\_work\_q](structk__work__q.md) \*queue, struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Submit an idle work item to a queue after a delay. |
| int | [k\_work\_schedule](#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Submit an idle work item to the system work queue after a delay. |
| int | [k\_work\_reschedule\_for\_queue](#gabf5db091eac19b19a4e12c0cb381f0a8) (struct [k\_work\_q](structk__work__q.md) \*queue, struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Reschedule a work item to a queue after a delay. |
| int | [k\_work\_reschedule](#gaacaab408fb7c848d466ad1f069dfa648) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Reschedule a work item to the system work queue after a delay. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_flush\_delayable](#gad47d54e513030304be2600d75b1a965f) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, struct [k\_work\_sync](structk__work__sync.md) \*sync) |
|  | Flush delayable work. |
| int | [k\_work\_cancel\_delayable](#ga92355914ee178d4c3e848a1946bed3e4) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork) |
|  | Cancel delayable work. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_cancel\_delayable\_sync](#ga7e7ec237648556fc16bfda8d35f7cd86) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, struct [k\_work\_sync](structk__work__sync.md) \*sync) |
|  | Cancel delayable work and wait. |
| static void | [k\_work\_user\_init](#ga9de9c7a7f13cc6b325e5453e34afe62d) (struct k\_work\_user \*work, [k\_work\_user\_handler\_t](#gaafa4dfac323cab570da1ee31c07d11bc) handler) |
|  | Initialize a userspace work item. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_user\_is\_pending](#ga58d05d4127e4cd51104a1f1a87f626cd) (struct k\_work\_user \*work) |
|  | Check if a userspace work item is pending. |
| static int | [k\_work\_user\_submit\_to\_queue](#ga50ae1f6f74c0bc0a41dbbf789fff8856) (struct k\_work\_user\_q \*work\_q, struct k\_work\_user \*work) |
|  | Submit a work item to a user mode workqueue. |
| void | [k\_work\_user\_queue\_start](#ga3091bc8fab5311252e41634a97a18589) (struct k\_work\_user\_q \*work\_q, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stack\_size, int prio, const char \*name) |
|  | Start a workqueue in user mode. |
| static [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [k\_work\_user\_queue\_thread\_get](#gab487068e9564cd77b6bdbac3d5670923) (struct k\_work\_user\_q \*work\_q) |
|  | Access the user mode thread that animates a work queue. |
| void | [k\_work\_poll\_init](#ga371dab33a40622bea19b07d852863443) (struct k\_work\_poll \*work, [k\_work\_handler\_t](#ga5add9ef0dce306a08413c4140fc0bdda) handler) |
|  | Initialize a triggered work item. |
| int | [k\_work\_poll\_submit\_to\_queue](#ga0abafd7f851e42fd3572c8438e600a53) (struct [k\_work\_q](structk__work__q.md) \*work\_q, struct k\_work\_poll \*work, struct [k\_poll\_event](structk__poll__event.md) \*events, int num\_events, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Submit a triggered work item. |
| int | [k\_work\_poll\_submit](#gad9f222e46d72c4f98739395a0c8bb4ea) (struct k\_work\_poll \*work, struct [k\_poll\_event](structk__poll__event.md) \*events, int num\_events, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Submit a triggered work item to the system workqueue. |
| int | [k\_work\_poll\_cancel](#ga2a19547d04dc1a202e80b752e3177215) (struct k\_work\_poll \*work) |
|  | Cancel a triggered work item. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaf8e003eefa5dd66ba883688f9d39c333)K\_WORK\_DEFINE

| #define K\_WORK\_DEFINE | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *work\_handler* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

struct [k\_work](structk__work.md) work = Z\_WORK\_INITIALIZER(work\_handler)

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:4006

Initialize a statically-defined work item.

This macro can be used to initialize a statically-defined workqueue work item, prior to its first use. For example,

static [K\_WORK\_DEFINE](#gaf8e003eefa5dd66ba883688f9d39c333)(<work>, <work\_handler>);

[K\_WORK\_DEFINE](#gaf8e003eefa5dd66ba883688f9d39c333)

#define K\_WORK\_DEFINE(work, work\_handler)

Initialize a statically-defined work item.

**Definition** kernel.h:4434

Parameters
:   | work | Symbol name for work item object |
    | --- | --- |
    | work\_handler | Function to invoke each time work item is processed. |

## [◆ ](#ga893b281f3d2bc0088650536899e17903)K\_WORK\_DELAYABLE\_DEFINE

| #define K\_WORK\_DELAYABLE\_DEFINE | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *work\_handler* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

struct [k\_work\_delayable](structk__work__delayable.md) work \

= Z\_WORK\_DELAYABLE\_INITIALIZER(work\_handler)

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4034

Initialize a statically-defined delayable work item.

This macro can be used to initialize a statically-defined delayable work item, prior to its first use. For example,

static [K\_WORK\_DELAYABLE\_DEFINE](#ga893b281f3d2bc0088650536899e17903)(<dwork>, <work\_handler>);

[K\_WORK\_DELAYABLE\_DEFINE](#ga893b281f3d2bc0088650536899e17903)

#define K\_WORK\_DELAYABLE\_DEFINE(work, work\_handler)

Initialize a statically-defined delayable work item.

**Definition** kernel.h:4068

Note that if the runtime dependencies support initialization with [k\_work\_init\_delayable()](#ga2876c5d82fb2340a093bc4d689a55465) using that will eliminate the initialized object in ROM that is produced by this macro and copied in at system startup.

Parameters
:   | work | Symbol name for delayable work item object |
    | --- | --- |
    | work\_handler | Function to invoke each time work item is processed. |

## [◆ ](#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)K\_WORK\_USER\_DEFINE

| #define K\_WORK\_USER\_DEFINE | ( |  | *work*, |
| --- | --- | --- | --- |
|  |  |  | *work\_handler* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

struct k\_work\_user work = Z\_WORK\_USER\_INITIALIZER(work\_handler)

Initialize a statically-defined user work item.

This macro can be used to initialize a statically-defined user work item, prior to its first use. For example,

static [K\_WORK\_USER\_DEFINE](#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)(<work>, <work\_handler>);

[K\_WORK\_USER\_DEFINE](#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)

#define K\_WORK\_USER\_DEFINE(work, work\_handler)

Initialize a statically-defined user work item.

**Definition** kernel.h:4280

Parameters
:   | work | Symbol name for work item object |
    | --- | --- |
    | work\_handler | Function to invoke each time work item is processed. |

## Typedef Documentation

## [◆ ](#ga5add9ef0dce306a08413c4140fc0bdda)k\_work\_handler\_t

| typedef void(\* k\_work\_handler\_t) (struct [k\_work](structk__work.md) \*work) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

The signature for a work item handler function.

The function will be invoked by the thread animating a work queue.

Parameters
:   | work | the work item that provided the handler. |
    | --- | --- |

## [◆ ](#gaafa4dfac323cab570da1ee31c07d11bc)k\_work\_user\_handler\_t

| typedef void(\* k\_work\_user\_handler\_t) (struct k\_work\_user \*work) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

Work item handler function type for user work queues.

A work item's handler function is executed by a user workqueue's thread when the work item is processed by the workqueue.

Parameters
:   | work | Address of the work item. |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#gae539da4c3f3d31b039bc49b9e76744eb)anonymous enum

| anonymous enum |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

| Enumerator | |
| --- | --- |
| K\_WORK\_RUNNING | Flag indicating a work item that is running under a work queue thread.  Accessed via [k\_work\_busy\_get()](#gaba8a8734768d768b433f9d8490e7df7b). May co-occur with other flags. |
| K\_WORK\_CANCELING | Flag indicating a work item that is being canceled.  Accessed via [k\_work\_busy\_get()](#gaba8a8734768d768b433f9d8490e7df7b). May co-occur with other flags. |
| K\_WORK\_QUEUED | Flag indicating a work item that has been submitted to a queue but has not started running.  Accessed via [k\_work\_busy\_get()](#gaba8a8734768d768b433f9d8490e7df7b). May co-occur with other flags. |
| K\_WORK\_DELAYED | Flag indicating a delayed work item that is scheduled for submission to a queue.  Accessed via [k\_work\_busy\_get()](#gaba8a8734768d768b433f9d8490e7df7b). May co-occur with other flags. |
| K\_WORK\_FLUSHING | Flag indicating a synced work item that is being flushed.  Accessed via [k\_work\_busy\_get()](#gaba8a8734768d768b433f9d8490e7df7b). May co-occur with other flags. |

## Function Documentation

## [◆ ](#gaba8a8734768d768b433f9d8490e7df7b)k\_work\_busy\_get()

| | int k\_work\_busy\_get | ( | const struct [k\_work](structk__work.md) \* | *work* | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Busy state flags from the work item.

A zero return value indicates the work item appears to be idle.

Note
:   This is a live snapshot of state, which may change before the result is checked. Use locks where appropriate.

Function properties (list may not be complete)

Parameters
:   | work | pointer to the work item. |
    | --- | --- |

Returns
:   a mask of flags K\_WORK\_DELAYED, K\_WORK\_QUEUED, K\_WORK\_RUNNING, K\_WORK\_CANCELING, and K\_WORK\_FLUSHING.

## [◆ ](#ga389fe2a8fb20f9bd593cf8d990727078)k\_work\_cancel()

| | int k\_work\_cancel | ( | struct [k\_work](structk__work.md) \* | *work* | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Cancel a work item.

This attempts to prevent a pending (non-delayable) work item from being processed by removing it from the work queue. If the item is being processed, the work item will continue to be processed, but resubmissions are rejected until cancellation completes.

If this returns zero cancellation is complete, otherwise something (probably a work queue thread) is still referencing the item.

See also [k\_work\_cancel\_sync()](#gab2b05cfe3af08f7d32c3946fa1c808f9).

Function properties (list may not be complete)

Parameters
:   | work | pointer to the work item. |
    | --- | --- |

Returns
:   the [k\_work\_busy\_get()](#gaba8a8734768d768b433f9d8490e7df7b) status indicating the state of the item after all cancellation steps performed by this call are completed.

## [◆ ](#ga92355914ee178d4c3e848a1946bed3e4)k\_work\_cancel\_delayable()

| | int k\_work\_cancel\_delayable | ( | struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork* | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Cancel delayable work.

Similar to [k\_work\_cancel()](#ga389fe2a8fb20f9bd593cf8d990727078) but for delayable work. If the work is scheduled or submitted it is canceled. This function does not wait for the cancellation to complete.

Note
:   The work may still be running when this returns. Use [k\_work\_flush\_delayable()](#gad47d54e513030304be2600d75b1a965f) or [k\_work\_cancel\_delayable\_sync()](#ga7e7ec237648556fc16bfda8d35f7cd86) to ensure it is not running.
:   Canceling delayable work does not prevent rescheduling it. It does prevent submitting it until the cancellation completes.

Function properties (list may not be complete)

Parameters
:   | dwork | pointer to the delayable work item. |
    | --- | --- |

Returns
:   the [k\_work\_delayable\_busy\_get()](#ga1b76969667844f0981d348c9c671bc9f) status indicating the state of the item after all cancellation steps performed by this call are completed.

## [◆ ](#ga7e7ec237648556fc16bfda8d35f7cd86)k\_work\_cancel\_delayable\_sync()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_work\_cancel\_delayable\_sync | ( | struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork*, |
| --- | --- | --- | --- |
|  |  | struct [k\_work\_sync](structk__work__sync.md) \* | *sync* ) |

`#include <[kernel.h](kernel_8h.md)>`

Cancel delayable work and wait.

Like [k\_work\_cancel\_delayable()](#ga92355914ee178d4c3e848a1946bed3e4) but waits until the work becomes idle.

Note
:   Canceling delayable work does not prevent rescheduling it. It does prevent submitting it until the cancellation completes.
:   Be careful of caller and work queue thread relative priority. If this function sleeps it will not return until the work queue thread completes the tasks that allow this thread to resume.
:   Behavior is undefined if this function is invoked on `dwork` from a work queue running `dwork`.

Parameters
:   | dwork | pointer to the delayable work item. |
    | --- | --- |
    | sync | pointer to an opaque item containing state related to the pending cancellation. The object must persist until the call returns, and be accessible from both the caller thread and the work queue thread. The object must not be used for any other flush or cancel operation until this one completes. On architectures with CONFIG\_KERNEL\_COHERENCE the object must be allocated in coherent memory. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if work was not idle (call had to wait for cancellation of a running handler to complete, or scheduled or submitted operations were cancelled); |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | otherwise |

## [◆ ](#gab2b05cfe3af08f7d32c3946fa1c808f9)k\_work\_cancel\_sync()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_work\_cancel\_sync | ( | struct [k\_work](structk__work.md) \* | *work*, |
| --- | --- | --- | --- |
|  |  | struct [k\_work\_sync](structk__work__sync.md) \* | *sync* ) |

`#include <[kernel.h](kernel_8h.md)>`

Cancel a work item and wait for it to complete.

Same as [k\_work\_cancel()](#ga389fe2a8fb20f9bd593cf8d990727078) but does not return until cancellation is complete. This can be invoked by a thread after [k\_work\_cancel()](#ga389fe2a8fb20f9bd593cf8d990727078) to synchronize with a previous cancellation.

On return the work structure will be idle unless something submits it after the cancellation was complete.

Note
:   Be careful of caller and work queue thread relative priority. If this function sleeps it will not return until the work queue thread completes the tasks that allow this thread to resume.
:   Behavior is undefined if this function is invoked on `work` from a work queue running `work`.

Parameters
:   | work | pointer to the work item. |
    | --- | --- |
    | sync | pointer to an opaque item containing state related to the pending cancellation. The object must persist until the call returns, and be accessible from both the caller thread and the work queue thread. The object must not be used for any other flush or cancel operation until this one completes. On architectures with CONFIG\_KERNEL\_COHERENCE the object must be allocated in coherent memory. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if work was pending (call had to wait for cancellation of a running handler to complete, or scheduled or submitted operations were cancelled); |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | otherwise |

## [◆ ](#ga1b76969667844f0981d348c9c671bc9f)k\_work\_delayable\_busy\_get()

| | int k\_work\_delayable\_busy\_get | ( | const struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork* | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Busy state flags from the delayable work item.

Function properties (list may not be complete)

Note
:   This is a live snapshot of state, which may change before the result can be inspected. Use locks where appropriate.

Parameters
:   | dwork | pointer to the delayable work item. |
    | --- | --- |

Returns
:   a mask of flags K\_WORK\_DELAYED, K\_WORK\_QUEUED, K\_WORK\_RUNNING, K\_WORK\_CANCELING, and K\_WORK\_FLUSHING. A zero return value indicates the work item appears to be idle.

## [◆ ](#ga1772c37bc62b86180d5cf48fe3037624)k\_work\_delayable\_expires\_get()

| | [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) k\_work\_delayable\_expires\_get | ( | const struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get the absolute tick count at which a scheduled delayable work will be submitted.

Note
:   This is a live snapshot of state, which may change before the result can be inspected. Use locks where appropriate.

Function properties (list may not be complete)

Parameters
:   | dwork | pointer to the delayable work item. |
    | --- | --- |

Returns
:   the tick count when the timer that will schedule the work item will expire, or the current tick count if the work is not scheduled.

## [◆ ](#gabcb822a03ce7ea9ee1ed046afe31ffca)k\_work\_delayable\_from\_work()

| | struct [k\_work\_delayable](structk__work__delayable.md) \* k\_work\_delayable\_from\_work | ( | struct [k\_work](structk__work.md) \* | *work* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get the parent delayable work structure from a work pointer.

This function is necessary when a `[k_work_handler_t](#ga5add9ef0dce306a08413c4140fc0bdda)` function is passed to [k\_work\_schedule\_for\_queue()](#ga17f863c9f6ff2fb41dc0f3b7de4fdf23) and the handler needs to access data from the container of the containing [k\_work\_delayable](structk__work__delayable.md "A structure used to submit work after a delay.").

Parameters
:   | work | Address passed to the work handler |
    | --- | --- |

Returns
:   Address of the containing `[k_work_delayable](structk__work__delayable.md "A structure used to submit work after a delay.")` structure.

## [◆ ](#ga66e598dbc73f653cbfec03c21168df2e)k\_work\_delayable\_is\_pending()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_work\_delayable\_is\_pending | ( | const struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Test whether a delayed work item is currently pending.

Wrapper to determine whether a delayed work item is in a non-idle state.

Note
:   This is a live snapshot of state, which may change before the result can be inspected. Use locks where appropriate.

Function properties (list may not be complete)

Parameters
:   | dwork | pointer to the delayable work item. |
    | --- | --- |

Returns
:   true if and only if [k\_work\_delayable\_busy\_get()](#ga1b76969667844f0981d348c9c671bc9f) returns a non-zero value.

## [◆ ](#gabce78598a014f3ed87730fe6a9fe61b4)k\_work\_delayable\_remaining\_get()

| | [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) k\_work\_delayable\_remaining\_get | ( | const struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get the number of ticks until a scheduled delayable work will be submitted.

Note
:   This is a live snapshot of state, which may change before the result can be inspected. Use locks where appropriate.

Function properties (list may not be complete)

Parameters
:   | dwork | pointer to the delayable work item. |
    | --- | --- |

Returns
:   the number of ticks until the timer that will schedule the work item will expire, or zero if the item is not scheduled.

## [◆ ](#gabd1cda459bab538fb2d6dfd84a73b253)k\_work\_flush()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_work\_flush | ( | struct [k\_work](structk__work.md) \* | *work*, |
| --- | --- | --- | --- |
|  |  | struct [k\_work\_sync](structk__work__sync.md) \* | *sync* ) |

`#include <[kernel.h](kernel_8h.md)>`

Wait for last-submitted instance to complete.

Resubmissions may occur while waiting, including chained submissions (from within the handler).

Note
:   Be careful of caller and work queue thread relative priority. If this function sleeps it will not return until the work queue thread completes the tasks that allow this thread to resume.
:   Behavior is undefined if this function is invoked on `work` from a work queue running `work`.

Parameters
:   | work | pointer to the work item. |
    | --- | --- |
    | sync | pointer to an opaque item containing state related to the pending cancellation. The object must persist until the call returns, and be accessible from both the caller thread and the work queue thread. The object must not be used for any other flush or cancel operation until this one completes. On architectures with CONFIG\_KERNEL\_COHERENCE the object must be allocated in coherent memory. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if call had to wait for completion |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if work was already idle |

## [◆ ](#gad47d54e513030304be2600d75b1a965f)k\_work\_flush\_delayable()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_work\_flush\_delayable | ( | struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork*, |
| --- | --- | --- | --- |
|  |  | struct [k\_work\_sync](structk__work__sync.md) \* | *sync* ) |

`#include <[kernel.h](kernel_8h.md)>`

Flush delayable work.

If the work is scheduled, it is immediately submitted. Then the caller blocks until the work completes, as with [k\_work\_flush()](#gabd1cda459bab538fb2d6dfd84a73b253).

Note
:   Be careful of caller and work queue thread relative priority. If this function sleeps it will not return until the work queue thread completes the tasks that allow this thread to resume.
:   Behavior is undefined if this function is invoked on `dwork` from a work queue running `dwork`.

Parameters
:   | dwork | pointer to the delayable work item. |
    | --- | --- |
    | sync | pointer to an opaque item containing state related to the pending cancellation. The object must persist until the call returns, and be accessible from both the caller thread and the work queue thread. The object must not be used for any other flush or cancel operation until this one completes. On architectures with CONFIG\_KERNEL\_COHERENCE the object must be allocated in coherent memory. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if call had to wait for completion |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if work was already idle |

## [◆ ](#gaf20080884a2893d39cd8e862b34a2a30)k\_work\_init()

| | void k\_work\_init | ( | struct [k\_work](structk__work.md) \* | *work*, | | --- | --- | --- | --- | |  |  | [k\_work\_handler\_t](#ga5add9ef0dce306a08413c4140fc0bdda) | *handler* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a (non-delayable) work structure.

This must be invoked before submitting a work structure for the first time. It need not be invoked again on the same work structure. It can be re-invoked to change the associated handler, but this must be done when the work item is idle.

Function properties (list may not be complete)

Parameters
:   | work | the work structure to be initialized. |
    | --- | --- |
    | handler | the handler to be invoked by the work item. |

## [◆ ](#ga2876c5d82fb2340a093bc4d689a55465)k\_work\_init\_delayable()

| | void k\_work\_init\_delayable | ( | struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork*, | | --- | --- | --- | --- | |  |  | [k\_work\_handler\_t](#ga5add9ef0dce306a08413c4140fc0bdda) | *handler* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a delayable work structure.

This must be invoked before scheduling a delayable work structure for the first time. It need not be invoked again on the same work structure. It can be re-invoked to change the associated handler, but this must be done when the work item is idle.

Function properties (list may not be complete)

Parameters
:   | dwork | the delayable work structure to be initialized. |
    | --- | --- |
    | handler | the handler to be invoked by the work item. |

## [◆ ](#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0)k\_work\_is\_pending()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_work\_is\_pending | ( | const struct [k\_work](structk__work.md) \* | *work* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Test whether a work item is currently pending.

Wrapper to determine whether a work item is in a non-idle state.

Note
:   This is a live snapshot of state, which may change before the result is checked. Use locks where appropriate.

Function properties (list may not be complete)

Parameters
:   | work | pointer to the work item. |
    | --- | --- |

Returns
:   true if and only if [k\_work\_busy\_get()](#gaba8a8734768d768b433f9d8490e7df7b) returns a non-zero value.

## [◆ ](#ga2a19547d04dc1a202e80b752e3177215)k\_work\_poll\_cancel()

| | int k\_work\_poll\_cancel | ( | struct k\_work\_poll \* | *work* | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Cancel a triggered work item.

This routine cancels the submission of triggered work item *work*. A triggered work item can only be canceled if no event triggered work submission.

Function properties (list may not be complete)

Parameters
:   | work | Address of delayed work item. |
    | --- | --- |

Return values
:   | 0 | Work item canceled. |
    | --- | --- |
    | -EINVAL | Work item is being processed or has completed its work. |

## [◆ ](#ga371dab33a40622bea19b07d852863443)k\_work\_poll\_init()

| void k\_work\_poll\_init | ( | struct k\_work\_poll \* | *work*, |
| --- | --- | --- | --- |
|  |  | [k\_work\_handler\_t](#ga5add9ef0dce306a08413c4140fc0bdda) | *handler* ) |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a triggered work item.

This routine initializes a workqueue triggered work item, prior to its first use.

Parameters
:   | work | Address of triggered work item. |
    | --- | --- |
    | handler | Function to invoke each time work item is processed. |

## [◆ ](#gad9f222e46d72c4f98739395a0c8bb4ea)k\_work\_poll\_submit()

| | int k\_work\_poll\_submit | ( | struct k\_work\_poll \* | *work*, | | --- | --- | --- | --- | |  |  | struct [k\_poll\_event](structk__poll__event.md) \* | *events*, | |  |  | int | *num\_events*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Submit a triggered work item to the system workqueue.

This routine schedules work item *work* to be processed by system workqueue when one of the given *events* is signaled. The routine initiates internal poller for the work item and then returns to the caller. Only when one of the watched events happen the work item is actually submitted to the workqueue and becomes pending.

Submitting a previously submitted triggered work item that is still waiting for the event cancels the existing submission and reschedules it the using the new event list. Note that this behavior is inherently subject to race conditions with the pre-existing triggered work item and work queue, so care must be taken to synchronize such resubmissions externally.

Function properties (list may not be complete)

Warning
:   Provided array of events as well as a triggered work item must not be modified until the item has been processed by the workqueue.

Parameters
:   | work | Address of delayed work item. |
    | --- | --- |
    | events | An array of events which trigger the work. |
    | num\_events | The number of events in the array. |
    | timeout | Timeout after which the work will be scheduled for execution even if not triggered. |

Return values
:   | 0 | Work item started watching for events. |
    | --- | --- |
    | -EINVAL | Work item is being processed or has completed its work. |
    | -EADDRINUSE | Work item is pending on a different workqueue. |

## [◆ ](#ga0abafd7f851e42fd3572c8438e600a53)k\_work\_poll\_submit\_to\_queue()

| | int k\_work\_poll\_submit\_to\_queue | ( | struct [k\_work\_q](structk__work__q.md) \* | *work\_q*, | | --- | --- | --- | --- | |  |  | struct k\_work\_poll \* | *work*, | |  |  | struct [k\_poll\_event](structk__poll__event.md) \* | *events*, | |  |  | int | *num\_events*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Submit a triggered work item.

This routine schedules work item *work* to be processed by workqueue *work\_q* when one of the given *events* is signaled. The routine initiates internal poller for the work item and then returns to the caller. Only when one of the watched events happen the work item is actually submitted to the workqueue and becomes pending.

Submitting a previously submitted triggered work item that is still waiting for the event cancels the existing submission and reschedules it the using the new event list. Note that this behavior is inherently subject to race conditions with the pre-existing triggered work item and work queue, so care must be taken to synchronize such resubmissions externally.

Function properties (list may not be complete)

Warning
:   Provided array of events as well as a triggered work item must be placed in persistent memory (valid until work handler execution or work cancellation) and cannot be modified after submission.

Parameters
:   | work\_q | Address of workqueue. |
    | --- | --- |
    | work | Address of delayed work item. |
    | events | An array of events which trigger the work. |
    | num\_events | The number of events in the array. |
    | timeout | Timeout after which the work will be scheduled for execution even if not triggered. |

Return values
:   | 0 | Work item started watching for events. |
    | --- | --- |
    | -EINVAL | Work item is being processed or has completed its work. |
    | -EADDRINUSE | Work item is pending on a different workqueue. |

## [◆ ](#ga0fefe3e0225ac99b47b250849f6cd863)k\_work\_queue\_drain()

| int k\_work\_queue\_drain | ( | struct [k\_work\_q](structk__work__q.md) \* | *queue*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *plug* ) |

`#include <[kernel.h](kernel_8h.md)>`

Wait until the work queue has drained, optionally plugging it.

This blocks submission to the work queue except when coming from queue thread, and blocks the caller until no more work items are available in the queue.

If `plug` is true then submission will continue to be blocked after the drain operation completes until [k\_work\_queue\_unplug()](#gaa0463bb79af3ec470f7d3be02052139f) is invoked.

Note that work items that are delayed are not yet associated with their work queue. They must be cancelled externally if a goal is to ensure the work queue remains empty. The `plug` feature can be used to prevent delayed items from being submitted after the drain completes.

Parameters
:   | queue | pointer to the queue structure. |
    | --- | --- |
    | plug | if true the work queue will continue to block new submissions after all items have drained. |

Return values
:   | 1 | if call had to wait for the drain to complete |
    | --- | --- |
    | 0 | if call did not have to wait |
    | negative | if wait was interrupted or failed |

## [◆ ](#gada77d818ea9e4d07c14a960872ed5492)k\_work\_queue\_init()

| | void k\_work\_queue\_init | ( | struct [k\_work\_q](structk__work__q.md) \* | *queue* | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a work queue structure.

This must be invoked before starting a work queue structure for the first time. It need not be invoked again on the same work queue structure.

Function properties (list may not be complete)

Parameters
:   | queue | the queue structure to be initialized. |
    | --- | --- |

## [◆ ](#gadfc56554f9bfe7b52309d79660188593)k\_work\_queue\_start()

| void k\_work\_queue\_start | ( | struct [k\_work\_q](structk__work__q.md) \* | *queue*, |
| --- | --- | --- | --- |
|  |  | [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | *stack*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *stack\_size*, |
|  |  | int | *prio*, |
|  |  | const struct [k\_work\_queue\_config](structk__work__queue__config.md) \* | *cfg* ) |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a work queue.

This configures the work queue thread and starts it running. The function should not be re-invoked on a queue.

Parameters
:   | queue | pointer to the queue structure. It must be initialized in zeroed/bss memory or with [k\_work\_queue\_init](#gada77d818ea9e4d07c14a960872ed5492) before use. |
    | --- | --- |
    | stack | pointer to the work thread stack area. |
    | stack\_size | size of the work thread stack area, in bytes. |
    | prio | initial thread priority |
    | cfg | optional additional configuration parameters. Pass `NULL` if not required, to use the defaults documented in [k\_work\_queue\_config](structk__work__queue__config.md "A structure holding optional configuration items for a work queue."). |

## [◆ ](#ga1fd2fce94eb731ccb0838ec763e62f5c)k\_work\_queue\_stop()

| int k\_work\_queue\_stop | ( | struct [k\_work\_q](structk__work__q.md) \* | *queue*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](kernel_8h.md)>`

Stop a work queue.

Stops the work queue thread and ensures that no further work will be processed. This call is blocking and guarantees that the work queue thread has terminated cleanly if successful, no work will be processed past this point.

Parameters
:   | queue | Pointer to the queue structure. |
    | --- | --- |
    | timeout | Maximum time to wait for the work queue to stop. |

Return values
:   | 0 | if the work queue was stopped |
    | --- | --- |
    | -EALREADY | if the work queue was not started (or already stopped) |
    | -EBUSY | if the work queue is actively processing work items |
    | -ETIMEDOUT | if the work queue did not stop within the stipulated timeout |

## [◆ ](#ga0b8b496f7e7bd82d08590a07293e38d7)k\_work\_queue\_thread\_get()

| | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) k\_work\_queue\_thread\_get | ( | struct [k\_work\_q](structk__work__q.md) \* | *queue* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Access the thread that animates a work queue.

This is necessary to grant a work queue thread access to things the work items it will process are expected to use.

Parameters
:   | queue | pointer to the queue structure. |
    | --- | --- |

Returns
:   the thread associated with the work queue.

## [◆ ](#gaa0463bb79af3ec470f7d3be02052139f)k\_work\_queue\_unplug()

| | int k\_work\_queue\_unplug | ( | struct [k\_work\_q](structk__work__q.md) \* | *queue* | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Release a work queue to accept new submissions.

This releases the block on new submissions placed when [k\_work\_queue\_drain()](#ga0fefe3e0225ac99b47b250849f6cd863) is invoked with the `plug` option enabled. If this is invoked before the drain completes new items may be submitted as soon as the drain completes.

Function properties (list may not be complete)

Parameters
:   | queue | pointer to the queue structure. |
    | --- | --- |

Return values
:   | 0 | if successfully unplugged |
    | --- | --- |
    | -EALREADY | if the work queue was not plugged. |

## [◆ ](#gaacaab408fb7c848d466ad1f069dfa648)k\_work\_reschedule()

| int k\_work\_reschedule | ( | struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *delay* ) |

`#include <[kernel.h](kernel_8h.md)>`

Reschedule a work item to the system work queue after a delay.

This is a thin wrapper around [k\_work\_reschedule\_for\_queue()](#gabf5db091eac19b19a4e12c0cb381f0a8), with all the API characteristics of that function.

Parameters
:   | dwork | pointer to the delayable work item. |
    | --- | --- |
    | delay | the time to wait before submitting the work item. |

Returns
:   as with [k\_work\_reschedule\_for\_queue()](#gabf5db091eac19b19a4e12c0cb381f0a8).

## [◆ ](#gabf5db091eac19b19a4e12c0cb381f0a8)k\_work\_reschedule\_for\_queue()

| | int k\_work\_reschedule\_for\_queue | ( | struct [k\_work\_q](structk__work__q.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *delay* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Reschedule a work item to a queue after a delay.

Unlike [k\_work\_schedule\_for\_queue()](#ga17f863c9f6ff2fb41dc0f3b7de4fdf23) this function can change the deadline of a scheduled work item, and will schedule a work item that is in any state (e.g. is idle, submitted, or running). This function does not affect ("unsubmit") a work item that has been submitted to a queue.

Function properties (list may not be complete)

Parameters
:   | queue | the queue on which the work item should be submitted after the delay. |
    | --- | --- |
    | dwork | pointer to the delayable work item. |
    | delay | the time to wait before submitting the work item. If `K_NO_WAIT` this is equivalent to [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c) after canceling any previous scheduled submission. |

Note
:   If delay is `K_NO_WAIT` ("no delay") the return values are as with [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c).

Return values
:   | 0 | if delay is `K_NO_WAIT` and work was already on a queue |
    | --- | --- |
    | 1 | if  - delay is `K_NO_WAIT` and work was not submitted but has now been queued to `queue`; or - delay not `K_NO_WAIT` and work has been scheduled |
    | 2 | if delay is `K_NO_WAIT` and work was running and has been queued to the queue that was running it |
    | -EBUSY | if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c) fails with this code. |
    | -EINVAL | if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c) fails with this code. |
    | -ENODEV | if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c) fails with this code. |

## [◆ ](#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3)k\_work\_schedule()

| int k\_work\_schedule | ( | struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *delay* ) |

`#include <[kernel.h](kernel_8h.md)>`

Submit an idle work item to the system work queue after a delay.

This is a thin wrapper around [k\_work\_schedule\_for\_queue()](#ga17f863c9f6ff2fb41dc0f3b7de4fdf23), with all the API characteristics of that function.

Parameters
:   | dwork | pointer to the delayable work item. |
    | --- | --- |
    | delay | the time to wait before submitting the work item. If `K_NO_WAIT` this is equivalent to [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c). |

Returns
:   as with [k\_work\_schedule\_for\_queue()](#ga17f863c9f6ff2fb41dc0f3b7de4fdf23).

## [◆ ](#ga17f863c9f6ff2fb41dc0f3b7de4fdf23)k\_work\_schedule\_for\_queue()

| | int k\_work\_schedule\_for\_queue | ( | struct [k\_work\_q](structk__work__q.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | struct [k\_work\_delayable](structk__work__delayable.md) \* | *dwork*, | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *delay* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Submit an idle work item to a queue after a delay.

Unlike [k\_work\_reschedule\_for\_queue()](#gabf5db091eac19b19a4e12c0cb381f0a8) this is a no-op if the work item is already scheduled or submitted, even if `delay` is `K_NO_WAIT`.

Function properties (list may not be complete)

Parameters
:   | queue | the queue on which the work item should be submitted after the delay. |
    | --- | --- |
    | dwork | pointer to the delayable work item. |
    | delay | the time to wait before submitting the work item. If `K_NO_WAIT` and the work is not pending this is equivalent to [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c). |

Return values
:   | 0 | if work was already scheduled or submitted. |
    | --- | --- |
    | 1 | if work has been scheduled. |
    | 2 | if `delay` is `K_NO_WAIT` and work was running and has been queued to the queue that was running it. |
    | -EBUSY | if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c) fails with this code. |
    | -EINVAL | if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c) fails with this code. |
    | -ENODEV | if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c) fails with this code. |

## [◆ ](#gace61b59575093d7442f39ccb7be686d7)k\_work\_submit()

| | int k\_work\_submit | ( | struct [k\_work](structk__work.md) \* | *work* | ) |  | | --- | --- | --- | --- | --- | --- | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Submit a work item to the system queue.

Function properties (list may not be complete)

Parameters
:   | work | pointer to the work item. |
    | --- | --- |

Returns
:   as with [k\_work\_submit\_to\_queue()](#ga5353e76f73db070614f50d06d292d05c).

## [◆ ](#ga5353e76f73db070614f50d06d292d05c)k\_work\_submit\_to\_queue()

| | int k\_work\_submit\_to\_queue | ( | struct [k\_work\_q](structk__work__q.md) \* | *queue*, | | --- | --- | --- | --- | |  |  | struct [k\_work](structk__work.md) \* | *work* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Submit a work item to a queue.

Parameters
:   | queue | pointer to the work queue on which the item should run. If NULL the queue from the most recent submission will be used. |
    | --- | --- |

Function properties (list may not be complete)

Parameters
:   | work | pointer to the work item. |
    | --- | --- |

Return values
:   | 0 | if work was already submitted to a queue |
    | --- | --- |
    | 1 | if work was not submitted and has been queued to `queue` |
    | 2 | if work was running and has been queued to the queue that was running it |
    | -EBUSY | - if work submission was rejected because the work item is cancelling; or - `queue` is draining; or - `queue` is plugged. |
    | -EINVAL | if `queue` is null and the work item has never been run. |
    | -ENODEV | if `queue` has not been started. |

## [◆ ](#ga9de9c7a7f13cc6b325e5453e34afe62d)k\_work\_user\_init()

| | void k\_work\_user\_init | ( | struct k\_work\_user \* | *work*, | | --- | --- | --- | --- | |  |  | [k\_work\_user\_handler\_t](#gaafa4dfac323cab570da1ee31c07d11bc) | *handler* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a userspace work item.

This routine initializes a user workqueue work item, prior to its first use.

Parameters
:   | work | Address of work item. |
    | --- | --- |
    | handler | Function to invoke each time work item is processed. |

## [◆ ](#ga58d05d4127e4cd51104a1f1a87f626cd)k\_work\_user\_is\_pending()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_work\_user\_is\_pending | ( | struct k\_work\_user \* | *work* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Check if a userspace work item is pending.

This routine indicates if user work item *work* is pending in a workqueue's queue.

Note
:   Checking if the work is pending gives no guarantee that the work will still be pending when this information is used. It is up to the caller to make sure that this information is used in a safe manner.

Function properties (list may not be complete)

Parameters
:   | work | Address of work item. |
    | --- | --- |

Returns
:   true if work item is pending, or false if it is not pending.

## [◆ ](#ga3091bc8fab5311252e41634a97a18589)k\_work\_user\_queue\_start()

| void k\_work\_user\_queue\_start | ( | struct k\_work\_user\_q \* | *work\_q*, |
| --- | --- | --- | --- |
|  |  | [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | *stack*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *stack\_size*, |
|  |  | int | *prio*, |
|  |  | const char \* | *name* ) |

`#include <[kernel.h](kernel_8h.md)>`

Start a workqueue in user mode.

This works identically to [k\_work\_queue\_start()](#gadfc56554f9bfe7b52309d79660188593) except it is callable from user mode, and the worker thread created will run in user mode. The caller must have permissions granted on both the work\_q parameter's thread and queue objects, and the same restrictions on priority apply as [k\_thread\_create()](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "Create a thread.").

Parameters
:   | work\_q | Address of workqueue. |
    | --- | --- |
    | stack | Pointer to work queue thread's stack space, as defined by [K\_THREAD\_STACK\_DEFINE()](group__thread__stack__api.md#gac5368ce24fdeab3863b5c8dee2ebd955 "Define a toplevel thread stack memory region.") |
    | stack\_size | Size of the work queue thread's stack (in bytes), which should either be the same constant passed to [K\_THREAD\_STACK\_DEFINE()](group__thread__stack__api.md#gac5368ce24fdeab3863b5c8dee2ebd955 "Define a toplevel thread stack memory region.") or the value of [K\_THREAD\_STACK\_SIZEOF()](group__thread__stack__api.md#ga775f8e6b4144cfdd24f3261b6db64150 "Return the size in bytes of a stack memory region."). |
    | prio | Priority of the work queue's thread. |
    | name | optional thread name. If not null a copy is made into the thread's name buffer. |

## [◆ ](#gab487068e9564cd77b6bdbac3d5670923)k\_work\_user\_queue\_thread\_get()

| | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) k\_work\_user\_queue\_thread\_get | ( | struct k\_work\_user\_q \* | *work\_q* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Access the user mode thread that animates a work queue.

This is necessary to grant a user mode work queue thread access to things the work items it will process are expected to use.

Parameters
:   | work\_q | pointer to the user mode queue structure. |
    | --- | --- |

Returns
:   the user mode thread associated with the work queue.

## [◆ ](#ga50ae1f6f74c0bc0a41dbbf789fff8856)k\_work\_user\_submit\_to\_queue()

| | int k\_work\_user\_submit\_to\_queue | ( | struct k\_work\_user\_q \* | *work\_q*, | | --- | --- | --- | --- | |  |  | struct k\_work\_user \* | *work* ) | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Submit a work item to a user mode workqueue.

Submits a work item to a workqueue that runs in user mode. A temporary memory allocation is made from the caller's resource pool which is freed once the worker thread consumes the [k\_work](structk__work.md "A structure used to submit work.") item. The workqueue thread must have memory access to the [k\_work](structk__work.md "A structure used to submit work.") item being submitted. The caller must have permission granted on the work\_q parameter's queue object.

Function properties (list may not be complete)

Parameters
:   | work\_q | Address of workqueue. |
    | --- | --- |
    | work | Address of work item. |

Return values
:   | -EBUSY | if the work item was already in some workqueue |
    | --- | --- |
    | -ENOMEM | if no memory for thread resource pool allocation |
    | 0 | Success |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
