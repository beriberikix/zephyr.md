---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/p4wq_8h.html
original_path: doxygen/html/p4wq_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

p4wq.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](p4wq_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [k\_p4wq\_work](structk__p4wq__work.md) |
|  | P4 Queue Work Item. [More...](structk__p4wq__work.md#details) |
| struct | [k\_p4wq](structk__p4wq.md) |
|  | P4 Queue. [More...](structk__p4wq.md#details) |
| struct | [k\_p4wq\_initparam](structk__p4wq__initparam.md) |

| Macros | |
| --- | --- |
| #define | [K\_P4WQ\_QUEUE\_PER\_THREAD](#a8a2691219e517a0ac987aeb275b67487)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [K\_P4WQ\_DELAYED\_START](#a8e0b60ac0b95772b5f5875669b8d6d01)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [K\_P4WQ\_USER\_CPU\_MASK](#a9e6b81f7c3ae916bde3048575cf9708d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [K\_P4WQ\_DEFINE](#af37c37fe046571f9ed99e14325d7a321)(name, n\_threads, stack\_sz) |
|  | Statically initialize a P4 Work Queue. |
| #define | [K\_P4WQ\_ARRAY\_DEFINE](#af4511892a31c6bb3c315ddacd869eb31)(name, n\_threads, stack\_sz, flg) |
|  | Statically initialize an array of P4 Work Queues. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [k\_p4wq\_handler\_t](#aa164250d00319b0d71670e95201e45b0)) (struct [k\_p4wq\_work](structk__p4wq__work.md) \*work) |
|  | P4 Queue handler callback. |

| Functions | |
| --- | --- |
| void | [k\_p4wq\_init](#aa67be80b892cbe9bf9eab475ac5c2eff) (struct [k\_p4wq](structk__p4wq.md) \*queue) |
|  | Initialize P4 Queue. |
| void | [k\_p4wq\_add\_thread](#a73397b7f22a3b1f0f7660081f9824527) (struct [k\_p4wq](structk__p4wq.md) \*queue, struct [k\_thread](structk__thread.md) \*thread, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stack\_size) |
|  | Dynamically add a thread object to a P4 Queue pool. |
| void | [k\_p4wq\_submit](#a40e7660d999b94c517712d8b499dd157) (struct [k\_p4wq](structk__p4wq.md) \*queue, struct [k\_p4wq\_work](structk__p4wq__work.md) \*item) |
|  | Submit work item to a P4 queue. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_p4wq\_cancel](#aede724dfe684f0a4e93845dee342f830) (struct [k\_p4wq](structk__p4wq.md) \*queue, struct [k\_p4wq\_work](structk__p4wq__work.md) \*item) |
|  | Cancel submitted P4 work item. |
| int | [k\_p4wq\_wait](#a421ad1ac947495483b414ab89eb6996d) (struct [k\_p4wq\_work](structk__p4wq__work.md) \*work, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Regain ownership of the work item, wait for completion if it's synchronous. |
| void | [k\_p4wq\_enable\_static\_thread](#a6d22a84d473caff84684047e96ed70ac) (struct [k\_p4wq](structk__p4wq.md) \*queue, struct [k\_thread](structk__thread.md) \*thread, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cpu\_mask) |

## Macro Definition Documentation

## [◆ ](#af4511892a31c6bb3c315ddacd869eb31)K\_P4WQ\_ARRAY\_DEFINE

| #define K\_P4WQ\_ARRAY\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *n\_threads*, |
|  |  |  | *stack\_sz*, |
|  |  |  | *flg* ) |

**Value:**

static [K\_THREAD\_STACK\_ARRAY\_DEFINE](group__thread__stack__api.md#gaae2471b24bdc574382f083163fb42597)(\_p4stacks\_##name, \

n\_threads, stack\_sz); \

static struct [k\_thread](structk__thread.md) \_p4threads\_##name[n\_threads]; \

static struct [k\_p4wq](structk__p4wq.md) name[n\_threads]; \

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([k\_p4wq\_initparam](structk__p4wq__initparam.md), \

\_init\_##name) = { \

.num = n\_threads, \

.stack\_size = stack\_sz, \

.threads = \_p4threads\_##name, \

.stacks = &(\_p4stacks\_##name[0][0]), \

.queue = name, \

.[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = [K\_P4WQ\_QUEUE\_PER\_THREAD](#a8a2691219e517a0ac987aeb275b67487) | flg, \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[K\_THREAD\_STACK\_ARRAY\_DEFINE](group__thread__stack__api.md#gaae2471b24bdc574382f083163fb42597)

#define K\_THREAD\_STACK\_ARRAY\_DEFINE(sym, nmemb, size)

Define a toplevel array of thread stack memory regions.

**Definition** thread\_stack.h:588

[K\_P4WQ\_QUEUE\_PER\_THREAD](#a8a2691219e517a0ac987aeb275b67487)

#define K\_P4WQ\_QUEUE\_PER\_THREAD

**Definition** p4wq.h:46

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[k\_p4wq\_initparam](structk__p4wq__initparam.md)

**Definition** p4wq.h:79

[k\_p4wq](structk__p4wq.md)

P4 Queue.

**Definition** p4wq.h:55

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

Statically initialize an array of P4 Work Queues.

Statically defines an array of struct [k\_p4wq](structk__p4wq.md "P4 Queue.") objects with the specified number of threads which will be initialized at boot and ready for use on entry to main().

Parameters
:   | name | Symbol name of the struct [k\_p4wq](structk__p4wq.md "P4 Queue.") array that will be defined |
    | --- | --- |
    | n\_threads | Number of threads and work queues |
    | stack\_sz | Requested stack size of each thread, in bytes |
    | flg | Flags |

## [◆ ](#af37c37fe046571f9ed99e14325d7a321)K\_P4WQ\_DEFINE

| #define K\_P4WQ\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *n\_threads*, |
|  |  |  | *stack\_sz* ) |

**Value:**

static [K\_THREAD\_STACK\_ARRAY\_DEFINE](group__thread__stack__api.md#gaae2471b24bdc574382f083163fb42597)(\_p4stacks\_##name, \

n\_threads, stack\_sz); \

static struct [k\_thread](structk__thread.md) \_p4threads\_##name[n\_threads]; \

static struct [k\_p4wq](structk__p4wq.md) name; \

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([k\_p4wq\_initparam](structk__p4wq__initparam.md), \

\_init\_##name) = { \

.num = n\_threads, \

.stack\_size = stack\_sz, \

.threads = \_p4threads\_##name, \

.stacks = &(\_p4stacks\_##name[0][0]), \

.queue = &name, \

.[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = 0, \

}

Statically initialize a P4 Work Queue.

Statically defines a struct [k\_p4wq](structk__p4wq.md "P4 Queue.") object with the specified number of threads which will be initialized at boot and ready for use on entry to main().

Parameters
:   | name | Symbol name of the struct [k\_p4wq](structk__p4wq.md "P4 Queue.") that will be defined |
    | --- | --- |
    | n\_threads | Number of threads in the work queue pool |
    | stack\_sz | Requested stack size of each thread, in bytes |

## [◆ ](#a8e0b60ac0b95772b5f5875669b8d6d01)K\_P4WQ\_DELAYED\_START

| #define K\_P4WQ\_DELAYED\_START   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a8a2691219e517a0ac987aeb275b67487)K\_P4WQ\_QUEUE\_PER\_THREAD

| #define K\_P4WQ\_QUEUE\_PER\_THREAD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a9e6b81f7c3ae916bde3048575cf9708d)K\_P4WQ\_USER\_CPU\_MASK

| #define K\_P4WQ\_USER\_CPU\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## Typedef Documentation

## [◆ ](#aa164250d00319b0d71670e95201e45b0)k\_p4wq\_handler\_t

| typedef void(\* k\_p4wq\_handler\_t) (struct [k\_p4wq\_work](structk__p4wq__work.md) \*work) |
| --- |

P4 Queue handler callback.

## Function Documentation

## [◆ ](#a73397b7f22a3b1f0f7660081f9824527)k\_p4wq\_add\_thread()

| void k\_p4wq\_add\_thread | ( | struct [k\_p4wq](structk__p4wq.md) \* | *queue*, |
| --- | --- | --- | --- |
|  |  | struct [k\_thread](structk__thread.md) \* | *thread*, |
|  |  | [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | *stack*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *stack\_size* ) |

Dynamically add a thread object to a P4 Queue pool.

Adds a thread to the pool managed by a P4 queue. The thread object must not be in use. If [k\_thread\_create()](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367 "Create a thread.") has previously been called on it, it must be aborted before being given to the queue.

Parameters
:   | queue | P4 Queue to which to add the thread |
    | --- | --- |
    | thread | Uninitialized/aborted thread object to add |
    | stack | Thread stack memory |
    | stack\_size | Thread stack size |

## [◆ ](#aede724dfe684f0a4e93845dee342f830)k\_p4wq\_cancel()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_p4wq\_cancel | ( | struct [k\_p4wq](structk__p4wq.md) \* | *queue*, |
| --- | --- | --- | --- |
|  |  | struct [k\_p4wq\_work](structk__p4wq__work.md) \* | *item* ) |

Cancel submitted P4 work item.

Cancels a previously-submitted work item and removes it from the queue. Returns true if the item was found in the queue and removed. If the function returns false, either the item was never submitted, has already been executed, or is still running.

Returns
:   true if the item was successfully removed, otherwise false

## [◆ ](#a6d22a84d473caff84684047e96ed70ac)k\_p4wq\_enable\_static\_thread()

| void k\_p4wq\_enable\_static\_thread | ( | struct [k\_p4wq](structk__p4wq.md) \* | *queue*, |
| --- | --- | --- | --- |
|  |  | struct [k\_thread](structk__thread.md) \* | *thread*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cpu\_mask* ) |

## [◆ ](#aa67be80b892cbe9bf9eab475ac5c2eff)k\_p4wq\_init()

| void k\_p4wq\_init | ( | struct [k\_p4wq](structk__p4wq.md) \* | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize P4 Queue.

Initializes a P4 Queue object. These objects must be initialized via this function (or statically using K\_P4WQ\_DEFINE) before any other API calls are made on it.

Parameters
:   | queue | P4 Queue to initialize |
    | --- | --- |

## [◆ ](#a40e7660d999b94c517712d8b499dd157)k\_p4wq\_submit()

| void k\_p4wq\_submit | ( | struct [k\_p4wq](structk__p4wq.md) \* | *queue*, |
| --- | --- | --- | --- |
|  |  | struct [k\_p4wq\_work](structk__p4wq__work.md) \* | *item* ) |

Submit work item to a P4 queue.

Submits the specified work item to the queue. The caller must have already initialized the relevant fields of the struct. The queue will execute the handler when CPU time is available and when no higher-priority work items are available. The handler may be invoked on any CPU.

The caller must not mutate the struct while it is stored in the queue. The memory should remain unchanged until [k\_p4wq\_cancel()](#aede724dfe684f0a4e93845dee342f830) is called or until the entry to the handler function.

Note
:   This call is a scheduling point, so if the submitted item (or any other ready thread) has a higher priority than the current thread and the current thread has a preemptible priority then the caller will yield.

Parameters
:   | queue | P4 Queue to which to submit |
    | --- | --- |
    | item | P4 work item to be submitted |

## [◆ ](#a421ad1ac947495483b414ab89eb6996d)k\_p4wq\_wait()

| int k\_p4wq\_wait | ( | struct [k\_p4wq\_work](structk__p4wq__work.md) \* | *work*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

Regain ownership of the work item, wait for completion if it's synchronous.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [p4wq.h](p4wq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
