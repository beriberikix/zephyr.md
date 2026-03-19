---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__thread__apis.html
original_path: doxygen/html/group__thread__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Thread APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_thread](structk__thread.md) |
|  | Thread Structure. [More...](structk__thread.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_ESSENTIAL](#gad503fbcca905a9266b0e154e3ded258c)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0)) |
|  | system thread that must not abort |
| #define | [K\_FP\_IDX](#ga4b2378312ea9b410be025b40e8d6a395)   1 |
| #define | [K\_FP\_REGS](#gab18cf1e8728e7adf53db2ae4bbcdd951)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([K\_FP\_IDX](#ga4b2378312ea9b410be025b40e8d6a395))) |
|  | FPU registers are managed by context switch. |
| #define | [K\_USER](#gacb5340339892f22301e02697c6039ccc)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2)) |
|  | user mode thread |
| #define | [K\_INHERIT\_PERMS](#gaa1788a413a055745d1de71b4da7c2eb2)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3)) |
|  | Inherit Permissions. |
| #define | [K\_CALLBACK\_STATE](#gacbdb579370978fe07e4a863a84bd8bee)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4)) |
|  | Callback item state. |
| #define | [K\_DSP\_IDX](#gacbd163e5bc79fc0282def5ff4321fa30)   6 |
|  | DSP registers are managed by context switch. |
| #define | [K\_DSP\_REGS](#ga8e1aeb428a418ed23e17448b796363cb)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([K\_DSP\_IDX](#gacbd163e5bc79fc0282def5ff4321fa30))) |
| #define | [K\_AGU\_IDX](#gab01cfd20675ebef8f5e81d7d17e6babb)   7 |
|  | AGU registers are managed by context switch. |
| #define | [K\_AGU\_REGS](#ga718088c1a68f03fffa960164cab60b72)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([K\_AGU\_IDX](#gab01cfd20675ebef8f5e81d7d17e6babb))) |
| #define | [K\_SSE\_REGS](#gaa5b7de51b26773aa4485a711a041d9a7)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7)) |
|  | FP and SSE registers are managed by context switch on x86. |
| #define | [k\_thread\_access\_grant](#gafec540511e6d2e0a074a5bfb515c53b0)(thread, ...) |
|  | Grant a thread access to a set of kernel objects. |
| #define | [K\_THREAD\_DEFINE](#gab3ced58648ca35788a40676e8478ecd2)(name, stack\_size, entry, p1, p2, p3, prio, options, delay) |
|  | Statically define and initialize a thread. |
| #define | [K\_KERNEL\_THREAD\_DEFINE](#gae25853424ec969f8431862c46b3ec294)(name, stack\_size, entry, p1, p2, p3, prio, options, delay) |
|  | Statically define and initialize a thread intended to run only in kernel mode. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [k\_thread\_user\_cb\_t](#gaf9f23a6ff9dae76af56f25b373e74c75)) (const struct [k\_thread](structk__thread.md) \*thread, void \*user\_data) |

| Functions | |
| --- | --- |
| void | [k\_thread\_foreach](#gae2596d56800769b06fc03c194a126a97) ([k\_thread\_user\_cb\_t](#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data) |
|  | Iterate over all the threads in the system. |
| void | [k\_thread\_foreach\_filter\_by\_cpu](#ga82a83c2db36b34596dcb5afa5b28e41c) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cpu, [k\_thread\_user\_cb\_t](#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data) |
|  | Iterate over all the threads in running on specified cpu. |
| void | [k\_thread\_foreach\_unlocked](#ga30ef8b445a6c1b4a82651674dbb737fc) ([k\_thread\_user\_cb\_t](#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data) |
|  | Iterate over all the threads in the system without locking. |
| void | [k\_thread\_foreach\_unlocked\_filter\_by\_cpu](#gad908a1b9014aa048cf12997804ab7be2) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cpu, [k\_thread\_user\_cb\_t](#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data) |
|  | Iterate over the threads in running on current cpu without locking. |
| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | [k\_thread\_stack\_alloc](#gafe00cc70bac8a47ba6dda21bde508614) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Dynamically allocate a thread stack. |
| int | [k\_thread\_stack\_free](#ga95560cb85f6656b981a9a50ff2cd70b7) ([k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack) |
|  | Free a dynamically allocated thread stack. |
| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [k\_thread\_create](#gad5b0bff3102f1656089f5875d999a367) (struct [k\_thread](structk__thread.md) \*new\_thread, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stack\_size, [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) entry, void \*p1, void \*p2, void \*p3, int prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) options, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Create a thread. |
| FUNC\_NORETURN void | [k\_thread\_user\_mode\_enter](#ga3fbe1c8a5f3ef1c25382c7d6fca35764) ([k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) entry, void \*p1, void \*p2, void \*p3) |
|  | Drop a thread's privileges permanently to user mode. |
| static void | [k\_thread\_heap\_assign](#ga3f46c06833add2a2e0ddb7242f06702c) (struct [k\_thread](structk__thread.md) \*thread, struct [k\_heap](structk__heap.md) \*heap) |
|  | Assign a resource memory pool to a thread. |
| int | [k\_thread\_join](#ga40a733561eb1f64dcaae0e01b167d233) (struct [k\_thread](structk__thread.md) \*thread, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Sleep until a thread exits. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_sleep](#ga48d4b041790454da4d68ac8711f29657) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Put the current thread to sleep. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_msleep](#ga51307cdfe153ab3e918b18755d97c5d9) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ms) |
|  | Put the current thread to sleep. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_usleep](#gaeac56bb072ce295b9fdc372ab8cee67e) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) us) |
|  | Put the current thread to sleep with microsecond resolution. |
| void | [k\_busy\_wait](#ga550b642e071480323e589866abb99c22) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usec\_to\_wait) |
|  | Cause the current thread to busy wait. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_can\_yield](#ga366b9daa0be65b0a69dbc9f146064b68) (void) |
|  | Check whether it is possible to yield in the current context. |
| void | [k\_yield](#ga08a3484c33444ecedc2d71d78495a295) (void) |
|  | Yield the current thread. |
| void | [k\_wakeup](#ga9275a019c8ff3c7fe49a81f8c078157e) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Wake up a sleeping thread. |
| \_\_attribute\_const\_\_ [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [k\_sched\_current\_thread\_query](#gac3b994b90b5bccded0895304f6b20c5d) (void) |
|  | Query thread ID of the current thread. |
| static \_\_attribute\_const\_\_ [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [k\_current\_get](#ga7ef1ed0fb9513df8096ede1e52fc76b2) (void) |
|  | Get thread ID of the current thread. |
| void | [k\_thread\_abort](#ga1f44bb0307bea7a97227764ecd7bf963) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Abort a thread. |
| void | [k\_thread\_start](#ga88031bd9fcfcd4305bae4029a4d8416f) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Start an inactive thread. |
| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_thread\_timeout\_expires\_ticks](#gab0b1c85b847fe74170c04538fa9949ff) (const struct [k\_thread](structk__thread.md) \*thread) |
|  | Get time when a thread wakes up, in system ticks. |
| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_thread\_timeout\_remaining\_ticks](#ga4688c095c86e037a18594efdb9a5e9b9) (const struct [k\_thread](structk__thread.md) \*thread) |
|  | Get time remaining before a thread wakes up, in system ticks. |
| int | [k\_thread\_priority\_get](#ga3a46ed8ad2c3b12416fafe11325f82b3) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Get a thread's priority. |
| void | [k\_thread\_priority\_set](#ga24e50a60c524d1eb22fe21cdf269b6a6) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int prio) |
|  | Set a thread's priority. |
| void | [k\_thread\_deadline\_set](#gad887f16c1dd6f3247682a83beb22d1ce) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int deadline) |
|  | Set deadline expiration time for scheduler. |
| int | [k\_thread\_cpu\_mask\_clear](#ga80b9c58df6600c7e79f16756c128f44c) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Sets all CPU enable masks to zero. |
| int | [k\_thread\_cpu\_mask\_enable\_all](#gaedcfeb0964ae72611791241580b2119d) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Sets all CPU enable masks to one. |
| int | [k\_thread\_cpu\_mask\_enable](#ga306587604a7496db8059bd395fd90fc0) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu) |
|  | Enable thread to run on specified CPU. |
| int | [k\_thread\_cpu\_mask\_disable](#ga89e6c07ac112da75b2ef115d1a557d44) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu) |
|  | Prevent thread to run on specified CPU. |
| int | [k\_thread\_cpu\_pin](#gae9ebd9845e14ed02944ab9282a185c03) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu) |
|  | Pin a thread to a CPU. |
| void | [k\_thread\_suspend](#ga66cf8682fb65870eceb5e57d667a8d4e) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Suspend a thread. |
| void | [k\_thread\_resume](#ga117b26f8569ec3045ead1fad1851663d) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Resume a suspended thread. |
| void | [k\_sched\_time\_slice\_set](#ga877c1bfeffbf8f097d1656f9e10a66e8) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice, int prio) |
|  | Set time-slicing period and scope. |
| void | [k\_thread\_time\_slice\_set](#ga563928f292a4134acd4142029b60e631) (struct [k\_thread](structk__thread.md) \*th, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice\_ticks, [k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f) expired, void \*data) |
|  | Set thread time slice. |
| void | [k\_sched\_lock](#ga4f0c5d0b9f279b12a4ad97db0c116a5f) (void) |
|  | Lock the scheduler. |
| void | [k\_sched\_unlock](#ga7b26f64523cc4c36522cc828ccf85580) (void) |
|  | Unlock the scheduler. |
| void | [k\_thread\_custom\_data\_set](#ga4834d9b81ed60c00eee77b0d4f8ab9e4) (void \*value) |
|  | Set current thread's custom data. |
| void \* | [k\_thread\_custom\_data\_get](#ga19af063cff7b306ba28062996922740d) (void) |
|  | Get current thread's custom data. |
| int | [k\_thread\_name\_set](#ga23107333f134b9c9a8b692374211e841) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, const char \*str) |
|  | Set current thread name. |
| const char \* | [k\_thread\_name\_get](#gadebf45da56dee393164569742459dc0a) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Get thread name. |
| int | [k\_thread\_name\_copy](#ga07b59ade055c69929ccdc08a14361794) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Copy the thread name into a supplied buffer. |
| const char \* | [k\_thread\_state\_str](#ga0c6af32096dc7ca391ffe2522bae4cb6) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread\_id, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_size) |
|  | Get thread state string. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gab01cfd20675ebef8f5e81d7d17e6babb)K\_AGU\_IDX

| #define K\_AGU\_IDX   7 |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

AGU registers are managed by context switch.

This option indicates that the thread uses the ARC processor's XY memory and DSP feature. Often used with

```
CONFIG_ARC_AGU_SHARING
```

. No effect if

```
CONFIG_ARC_AGU_SHARING
```

is not enabled.

## [◆ ](#ga718088c1a68f03fffa960164cab60b72)K\_AGU\_REGS

| #define K\_AGU\_REGS   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([K\_AGU\_IDX](#gab01cfd20675ebef8f5e81d7d17e6babb))) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#gacbdb579370978fe07e4a863a84bd8bee)K\_CALLBACK\_STATE

| #define K\_CALLBACK\_STATE   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4)) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

Callback item state.

This is a single bit of state reserved for "callback manager" utilities (p4wq initially) who need to track operations invoked from within a user-provided callback they have been invoked. Effectively it serves as a tiny bit of zero-overhead TLS data.

## [◆ ](#gacbd163e5bc79fc0282def5ff4321fa30)K\_DSP\_IDX

| #define K\_DSP\_IDX   6 |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

DSP registers are managed by context switch.

This option indicates that the thread uses the CPU's DSP registers. This instructs the kernel to take additional steps to save and restore the contents of these registers when scheduling the thread. No effect if

```
CONFIG_DSP_SHARING
```

is not enabled.

## [◆ ](#ga8e1aeb428a418ed23e17448b796363cb)K\_DSP\_REGS

| #define K\_DSP\_REGS   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([K\_DSP\_IDX](#gacbd163e5bc79fc0282def5ff4321fa30))) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#gad503fbcca905a9266b0e154e3ded258c)K\_ESSENTIAL

| #define K\_ESSENTIAL   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0)) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

system thread that must not abort

## [◆ ](#ga4b2378312ea9b410be025b40e8d6a395)K\_FP\_IDX

| #define K\_FP\_IDX   1 |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## [◆ ](#gab18cf1e8728e7adf53db2ae4bbcdd951)K\_FP\_REGS

| #define K\_FP\_REGS   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([K\_FP\_IDX](#ga4b2378312ea9b410be025b40e8d6a395))) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

FPU registers are managed by context switch.

This option indicates that the thread uses the CPU's floating point registers. This instructs the kernel to take additional steps to save and restore the contents of these registers when scheduling the thread. No effect if

```
CONFIG_FPU_SHARING
```

is not enabled.

## [◆ ](#gaa1788a413a055745d1de71b4da7c2eb2)K\_INHERIT\_PERMS

| #define K\_INHERIT\_PERMS   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3)) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

Inherit Permissions.

Indicates that the thread being created should inherit all kernel object permissions from the thread that created it. No effect if

```
CONFIG_USERSPACE
```

is not enabled.

## [◆ ](#gae25853424ec969f8431862c46b3ec294)K\_KERNEL\_THREAD\_DEFINE

| #define K\_KERNEL\_THREAD\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *stack\_size*, |
|  |  |  | *entry*, |
|  |  |  | *p1*, |
|  |  |  | *p2*, |
|  |  |  | *p3*, |
|  |  |  | *prio*, |
|  |  |  | *options*, |
|  |  |  | *delay* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

[K\_KERNEL\_STACK\_DEFINE](group__thread__stack__api.md#ga9e05e3cb5aa5b72d6f19e2f327313271)(\_k\_thread\_stack\_##name, stack\_size); \

Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, entry, p1, p2, p3, \

prio, options, delay)

[K\_KERNEL\_STACK\_DEFINE](group__thread__stack__api.md#ga9e05e3cb5aa5b72d6f19e2f327313271)

#define K\_KERNEL\_STACK\_DEFINE(sym, size)

Define a toplevel kernel stack memory region.

**Definition** thread\_stack.h:214

Statically define and initialize a thread intended to run only in kernel mode.

The thread may be scheduled for immediate execution or a delayed start.

Thread options are architecture-specific, and can include K\_ESSENTIAL, K\_FP\_REGS, and K\_SSE\_REGS. Multiple options may be specified by separating them using "|" (the logical OR operator).

The ID of the thread can be accessed using:

extern const [k\_tid\_t <name>](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647);

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:380

Note
:   Threads defined by this can only run in kernel mode, and cannot be transformed into user thread via [k\_thread\_user\_mode\_enter()](#ga3fbe1c8a5f3ef1c25382c7d6fca35764).

Warning
:   Depending on the architecture, the stack size (`stack_size`) may need to be multiples of CONFIG\_MMU\_PAGE\_SIZE (if MMU) or in power-of-two size (if MPU).

Parameters
:   | name | Name of the thread. |
    | --- | --- |
    | stack\_size | Stack size in bytes. |
    | entry | Thread entry function. |
    | p1 | 1st entry point parameter. |
    | p2 | 2nd entry point parameter. |
    | p3 | 3rd entry point parameter. |
    | prio | Thread priority. |
    | options | Thread options. |
    | delay | Scheduling delay (in milliseconds), zero for no delay. |

## [◆ ](#gaa5b7de51b26773aa4485a711a041d9a7)K\_SSE\_REGS

| #define K\_SSE\_REGS   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7)) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

FP and SSE registers are managed by context switch on x86.

This option indicates that the thread uses the x86 CPU's floating point and SSE registers. This instructs the kernel to take additional steps to save and restore the contents of these registers when scheduling the thread. No effect if

```
CONFIG_X86_SSE
```

is not enabled.

## [◆ ](#gafec540511e6d2e0a074a5bfb515c53b0)k\_thread\_access\_grant

| #define k\_thread\_access\_grant | ( |  | *thread*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

[FOR\_EACH\_FIXED\_ARG](group__sys-util.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)([k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22), (;), (thread), \_\_VA\_ARGS\_\_)

[FOR\_EACH\_FIXED\_ARG](group__sys-util.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)

#define FOR\_EACH\_FIXED\_ARG(F, sep, fixed\_arg,...)

Call macro F on each provided argument, with an additional fixed argument as a parameter.

**Definition** util\_macro.h:601

[k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)

void k\_object\_access\_grant(const void \*object, struct k\_thread \*thread)

Grant a thread access to a kernel object.

Grant a thread access to a set of kernel objects.

This is a convenience function. For the provided thread, grant access to the remaining arguments, which must be pointers to kernel objects.

The thread object must be initialized (i.e. running). The objects don't need to be. Note that NULL shouldn't be passed as an argument.

Parameters
:   | thread | Thread to grant access to objects |
    | --- | --- |
    | ... | list of kernel object pointers |

## [◆ ](#gab3ced58648ca35788a40676e8478ecd2)K\_THREAD\_DEFINE

| #define K\_THREAD\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *stack\_size*, |
|  |  |  | *entry*, |
|  |  |  | *p1*, |
|  |  |  | *p2*, |
|  |  |  | *p3*, |
|  |  |  | *prio*, |
|  |  |  | *options*, |
|  |  |  | *delay* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

[K\_THREAD\_STACK\_DEFINE](group__thread__stack__api.md#gac5368ce24fdeab3863b5c8dee2ebd955)(\_k\_thread\_stack\_##name, stack\_size); \

Z\_THREAD\_COMMON\_DEFINE(name, stack\_size, entry, p1, p2, p3, \

prio, options, delay)

[K\_THREAD\_STACK\_DEFINE](group__thread__stack__api.md#gac5368ce24fdeab3863b5c8dee2ebd955)

#define K\_THREAD\_STACK\_DEFINE(sym, size)

Define a toplevel thread stack memory region.

**Definition** thread\_stack.h:516

Statically define and initialize a thread.

The thread may be scheduled for immediate execution or a delayed start.

Thread options are architecture-specific, and can include K\_ESSENTIAL, K\_FP\_REGS, and K\_SSE\_REGS. Multiple options may be specified by separating them using "|" (the logical OR operator).

The ID of the thread can be accessed using:

extern const [k\_tid\_t <name>](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647);

Parameters
:   | name | Name of the thread. |
    | --- | --- |
    | stack\_size | Stack size in bytes. |
    | entry | Thread entry function. |
    | p1 | 1st entry point parameter. |
    | p2 | 2nd entry point parameter. |
    | p3 | 3rd entry point parameter. |
    | prio | Thread priority. |
    | options | Thread options. |
    | delay | Scheduling delay (in milliseconds), zero for no delay. |

Note
:   Static threads with zero delay should not normally have MetaIRQ priority levels. This can preempt the system initialization handling (depending on the priority of the main thread) and cause surprising ordering side effects. It will not affect anything in the OS per se, but consider it bad practice. Use a [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") callback if you need to run code before entrance to the application main().

## [◆ ](#gacb5340339892f22301e02697c6039ccc)K\_USER

| #define K\_USER   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2)) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

user mode thread

This thread has dropped from supervisor mode to user mode and consequently has additional restrictions

## Typedef Documentation

## [◆ ](#gaf9f23a6ff9dae76af56f25b373e74c75)k\_thread\_user\_cb\_t

| typedef void(\* k\_thread\_user\_cb\_t) (const struct [k\_thread](structk__thread.md) \*thread, void \*user\_data) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

## Function Documentation

## [◆ ](#ga550b642e071480323e589866abb99c22)k\_busy\_wait()

| void k\_busy\_wait | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *usec\_to\_wait* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Cause the current thread to busy wait.

This routine causes the current thread to execute a "do nothing" loop for *usec\_to\_wait* microseconds.

Note
:   The clock used for the microsecond-resolution delay here may be skewed relative to the clock used for system timeouts like [k\_sleep()](#ga48d4b041790454da4d68ac8711f29657). For example k\_busy\_wait(1000) may take slightly more or less time than k\_sleep(K\_MSEC(1)), with the offset dependent on clock tolerances.
:   In case when

    ```
    CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE
    ```

    and

    ```
    CONFIG_PM
    ```

    options are enabled, this function may not work. The timer/clock used for delay processing may be disabled/inactive.

## [◆ ](#ga366b9daa0be65b0a69dbc9f146064b68)k\_can\_yield()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_can\_yield | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Check whether it is possible to yield in the current context.

This routine checks whether the kernel is in a state where it is possible to yield or call blocking API's. It should be used by code that needs to yield to perform correctly, but can feasibly be called from contexts where that is not possible. For example in the PRE\_KERNEL initialization step, or when being run from the idle thread.

Returns
:   True if it is possible to yield in the current context, false otherwise.

## [◆ ](#ga7ef1ed0fb9513df8096ede1e52fc76b2)k\_current\_get()

| | \_\_attribute\_const\_\_ [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) k\_current\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get thread ID of the current thread.

Returns
:   ID of current thread.

## [◆ ](#ga51307cdfe153ab3e918b18755d97c5d9)k\_msleep()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) k\_msleep | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *ms* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Put the current thread to sleep.

This routine puts the current thread to sleep for *duration* milliseconds.

Parameters
:   | ms | Number of milliseconds to sleep. |
    | --- | --- |

Returns
:   Zero if the requested time has elapsed or if the thread was woken up by the [k\_wakeup](#ga9275a019c8ff3c7fe49a81f8c078157e) call, the time left to sleep rounded up to the nearest millisecond.

## [◆ ](#gac3b994b90b5bccded0895304f6b20c5d)k\_sched\_current\_thread\_query()

| \_\_attribute\_const\_\_ [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) k\_sched\_current\_thread\_query | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Query thread ID of the current thread.

This unconditionally queries the kernel via a system call.

Note
:   Use [k\_current\_get()](#ga7ef1ed0fb9513df8096ede1e52fc76b2) unless absolutely sure this is necessary. This should only be used directly where the thread local variable cannot be used or may contain invalid values if thread local storage (TLS) is enabled. If TLS is not enabled, this is the same as [k\_current\_get()](#ga7ef1ed0fb9513df8096ede1e52fc76b2).

Returns
:   ID of current thread.

## [◆ ](#ga4f0c5d0b9f279b12a4ad97db0c116a5f)k\_sched\_lock()

| void k\_sched\_lock | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Lock the scheduler.

This routine prevents the current thread from being preempted by another thread by instructing the scheduler to treat it as a cooperative thread. If the thread subsequently performs an operation that makes it unready, it will be context switched out in the normal manner. When the thread again becomes the current thread, its non-preemptible status is maintained.

This routine can be called recursively.

Owing to clever implementation details, scheduler locks are extremely fast for non-userspace threads (just one byte inc/decrement in the thread struct).

Note
:   This works by elevating the thread priority temporarily to a cooperative priority, allowing cheap synchronization vs. other preemptible or cooperative threads running on the current CPU. It does not prevent preemption or asynchrony of other types. It does not prevent threads from running on other CPUs when CONFIG\_SMP=y. It does not prevent interrupts from happening, nor does it prevent threads with MetaIRQ priorities from preempting the current thread. In general this is a historical API not well-suited to modern applications, use with care.

## [◆ ](#ga877c1bfeffbf8f097d1656f9e10a66e8)k\_sched\_time\_slice\_set()

| void k\_sched\_time\_slice\_set | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *slice*, |
| --- | --- | --- | --- |
|  |  | int | *prio* ) |

`#include <[kernel.h](kernel_8h.md)>`

Set time-slicing period and scope.

This routine specifies how the scheduler will perform time slicing of preemptible threads.

To enable time slicing, *slice* must be non-zero. The scheduler ensures that no thread runs for more than the specified time limit before other threads of that priority are given a chance to execute. Any thread whose priority is higher than *prio* is exempted, and may execute as long as desired without being preempted due to time slicing.

Time slicing only limits the maximum amount of time a thread may continuously execute. Once the scheduler selects a thread for execution, there is no minimum guaranteed time the thread will execute before threads of greater or equal priority are scheduled.

When the current thread is the only one of that priority eligible for execution, this routine has no effect; the thread is immediately rescheduled after the slice period expires.

To disable timeslicing, set both *slice* and *prio* to zero.

Parameters
:   | slice | Maximum time slice length (in milliseconds). |
    | --- | --- |
    | prio | Highest thread priority level eligible for time slicing. |

## [◆ ](#ga7b26f64523cc4c36522cc828ccf85580)k\_sched\_unlock()

| void k\_sched\_unlock | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Unlock the scheduler.

This routine reverses the effect of a previous call to [k\_sched\_lock()](#ga4f0c5d0b9f279b12a4ad97db0c116a5f). A thread must call the routine once for each time it called [k\_sched\_lock()](#ga4f0c5d0b9f279b12a4ad97db0c116a5f) before the thread becomes preemptible.

## [◆ ](#ga48d4b041790454da4d68ac8711f29657)k\_sleep()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) k\_sleep | ( | [k\_timeout\_t](structk__timeout__t.md) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Put the current thread to sleep.

This routine puts the current thread to sleep for *duration*, specified as a [k\_timeout\_t](structk__timeout__t.md "Kernel timeout type.") object.

Note
:   if *timeout* is set to K\_FOREVER then the thread is suspended.

Parameters
:   | timeout | Desired duration of sleep. |
    | --- | --- |

Returns
:   Zero if the requested time has elapsed or if the thread was woken up by the [k\_wakeup](#ga9275a019c8ff3c7fe49a81f8c078157e) call, the time left to sleep rounded up to the nearest millisecond.

## [◆ ](#ga1f44bb0307bea7a97227764ecd7bf963)k\_thread\_abort()

| void k\_thread\_abort | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Abort a thread.

This routine permanently stops execution of *thread*. The thread is taken off all kernel queues it is part of (i.e. the ready queue, the timeout queue, or a kernel object wait queue). However, any kernel resources the thread might currently own (such as mutexes or memory blocks) are not released. It is the responsibility of the caller of this routine to ensure all necessary cleanup is performed.

After [k\_thread\_abort()](#ga1f44bb0307bea7a97227764ecd7bf963) returns, the thread is guaranteed not to be running or to become runnable anywhere on the system. Normally this is done via blocking the caller (in the same manner as [k\_thread\_join()](#ga40a733561eb1f64dcaae0e01b167d233)), but in interrupt context on SMP systems the implementation is required to spin for threads that are running on other CPUs.

Parameters
:   | thread | ID of thread to abort. |
    | --- | --- |

## [◆ ](#ga80b9c58df6600c7e79f16756c128f44c)k\_thread\_cpu\_mask\_clear()

| int k\_thread\_cpu\_mask\_clear | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Sets all CPU enable masks to zero.

After this returns, the thread will no longer be schedulable on any CPUs. The thread must not be currently runnable.

Note
:   You should enable

    ```
    CONFIG_SCHED_CPU_MASK
    ```

    in your project configuration.

Parameters
:   | thread | Thread to operate upon |
    | --- | --- |

Returns
:   Zero on success, otherwise error code

## [◆ ](#ga89e6c07ac112da75b2ef115d1a557d44)k\_thread\_cpu\_mask\_disable()

| int k\_thread\_cpu\_mask\_disable | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread*, |
| --- | --- | --- | --- |
|  |  | int | *cpu* ) |

`#include <[kernel.h](kernel_8h.md)>`

Prevent thread to run on specified CPU.

The thread must not be currently runnable.

Note
:   You should enable

    ```
    CONFIG_SCHED_CPU_MASK
    ```

    in your project configuration.

Parameters
:   | thread | Thread to operate upon |
    | --- | --- |
    | cpu | CPU index |

Returns
:   Zero on success, otherwise error code

## [◆ ](#ga306587604a7496db8059bd395fd90fc0)k\_thread\_cpu\_mask\_enable()

| int k\_thread\_cpu\_mask\_enable | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread*, |
| --- | --- | --- | --- |
|  |  | int | *cpu* ) |

`#include <[kernel.h](kernel_8h.md)>`

Enable thread to run on specified CPU.

The thread must not be currently runnable.

Note
:   You should enable

    ```
    CONFIG_SCHED_CPU_MASK
    ```

    in your project configuration.

Parameters
:   | thread | Thread to operate upon |
    | --- | --- |
    | cpu | CPU index |

Returns
:   Zero on success, otherwise error code

## [◆ ](#gaedcfeb0964ae72611791241580b2119d)k\_thread\_cpu\_mask\_enable\_all()

| int k\_thread\_cpu\_mask\_enable\_all | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Sets all CPU enable masks to one.

After this returns, the thread will be schedulable on any CPU. The thread must not be currently runnable.

Note
:   You should enable

    ```
    CONFIG_SCHED_CPU_MASK
    ```

    in your project configuration.

Parameters
:   | thread | Thread to operate upon |
    | --- | --- |

Returns
:   Zero on success, otherwise error code

## [◆ ](#gae9ebd9845e14ed02944ab9282a185c03)k\_thread\_cpu\_pin()

| int k\_thread\_cpu\_pin | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread*, |
| --- | --- | --- | --- |
|  |  | int | *cpu* ) |

`#include <[kernel.h](kernel_8h.md)>`

Pin a thread to a CPU.

Pin a thread to a CPU by first clearing the cpu mask and then enabling the thread on the selected CPU.

Parameters
:   | thread | Thread to operate upon |
    | --- | --- |
    | cpu | CPU index |

Returns
:   Zero on success, otherwise error code

## [◆ ](#gad5b0bff3102f1656089f5875d999a367)k\_thread\_create()

| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) k\_thread\_create | ( | struct [k\_thread](structk__thread.md) \* | *new\_thread*, |
| --- | --- | --- | --- |
|  |  | [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | *stack*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *stack\_size*, |
|  |  | [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) | *entry*, |
|  |  | void \* | *p1*, |
|  |  | void \* | *p2*, |
|  |  | void \* | *p3*, |
|  |  | int | *prio*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *options*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *delay* ) |

`#include <[kernel.h](kernel_8h.md)>`

Create a thread.

This routine initializes a thread, then schedules it for execution.

The new thread may be scheduled for immediate execution or a delayed start. If the newly spawned thread does not have a delayed start the kernel scheduler may preempt the current thread to allow the new thread to execute.

Thread options are architecture-specific, and can include K\_ESSENTIAL, K\_FP\_REGS, and K\_SSE\_REGS. Multiple options may be specified by separating them using "|" (the logical OR operator).

Stack objects passed to this function must be originally defined with either of these macros in order to be portable:

- [K\_THREAD\_STACK\_DEFINE()](group__thread__stack__api.md#gac5368ce24fdeab3863b5c8dee2ebd955 "Define a toplevel thread stack memory region.") - For stacks that may support either user or supervisor threads.
- [K\_KERNEL\_STACK\_DEFINE()](group__thread__stack__api.md#ga9e05e3cb5aa5b72d6f19e2f327313271 "Define a toplevel kernel stack memory region.") - For stacks that may support supervisor threads only. These stacks use less memory if CONFIG\_USERSPACE is enabled.

The stack\_size parameter has constraints. It must either be:

- The original size value passed to [K\_THREAD\_STACK\_DEFINE()](group__thread__stack__api.md#gac5368ce24fdeab3863b5c8dee2ebd955 "Define a toplevel thread stack memory region.") or [K\_KERNEL\_STACK\_DEFINE()](group__thread__stack__api.md#ga9e05e3cb5aa5b72d6f19e2f327313271 "Define a toplevel kernel stack memory region.")
- The return value of [K\_THREAD\_STACK\_SIZEOF(stack)](group__thread__stack__api.md#ga775f8e6b4144cfdd24f3261b6db64150 "Return the size in bytes of a stack memory region.") if the stack was defined with [K\_THREAD\_STACK\_DEFINE()](group__thread__stack__api.md#gac5368ce24fdeab3863b5c8dee2ebd955 "Define a toplevel thread stack memory region.")
- The return value of [K\_KERNEL\_STACK\_SIZEOF(stack)](group__thread__stack__api.md#ga57b3824b117c634dbb6052d47dc4301c) if the stack was defined with [K\_KERNEL\_STACK\_DEFINE()](group__thread__stack__api.md#ga9e05e3cb5aa5b72d6f19e2f327313271 "Define a toplevel kernel stack memory region.").

Using other values, or sizeof(stack) may produce undefined behavior.

Parameters
:   | new\_thread | Pointer to uninitialized struct [k\_thread](structk__thread.md "Thread Structure.") |
    | --- | --- |
    | stack | Pointer to the stack space. |
    | stack\_size | Stack size in bytes. |
    | entry | Thread entry function. |
    | p1 | 1st entry point parameter. |
    | p2 | 2nd entry point parameter. |
    | p3 | 3rd entry point parameter. |
    | prio | Thread priority. |
    | options | Thread options. |
    | delay | Scheduling delay, or K\_NO\_WAIT (for no delay). |

Returns
:   ID of new thread.

## [◆ ](#ga19af063cff7b306ba28062996922740d)k\_thread\_custom\_data\_get()

| void \* k\_thread\_custom\_data\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get current thread's custom data.

This routine returns the custom data for the current thread.

Returns
:   Current custom data value.

## [◆ ](#ga4834d9b81ed60c00eee77b0d4f8ab9e4)k\_thread\_custom\_data\_set()

| void k\_thread\_custom\_data\_set | ( | void \* | *value* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Set current thread's custom data.

This routine sets the custom data for the current thread to @ value.

Custom data is not used by the kernel itself, and is freely available for a thread to use as it sees fit. It can be used as a framework upon which to build thread-local storage.

Parameters
:   | value | New custom data value. |
    | --- | --- |

## [◆ ](#gad887f16c1dd6f3247682a83beb22d1ce)k\_thread\_deadline\_set()

| void k\_thread\_deadline\_set | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread*, |
| --- | --- | --- | --- |
|  |  | int | *deadline* ) |

`#include <[kernel.h](kernel_8h.md)>`

Set deadline expiration time for scheduler.

This sets the "deadline" expiration as a time delta from the current time, in the same units used by [k\_cycle\_get\_32()](group__clock__apis.md#ga208687de625e0036558343b4e66143d3 "Read the hardware clock."). The scheduler (when deadline scheduling is enabled) will choose the next expiring thread when selecting between threads at the same static priority. Threads at different priorities will be scheduled according to their static priority.

Note
:   Deadlines are stored internally using 32 bit unsigned integers. The number of cycles between the "first" deadline in the scheduler queue and the "last" deadline must be less than 2^31 (i.e a signed non-negative quantity). Failure to adhere to this rule may result in scheduled threads running in an incorrect deadline order.
:   Despite the API naming, the scheduler makes no guarantees the thread WILL be scheduled within that deadline, nor does it take extra metadata (like e.g. the "runtime" and "period" parameters in Linux sched\_setattr()) that allows the kernel to validate the scheduling for achievability. Such features could be implemented above this call, which is simply input to the priority selection logic.
:   You should enable

    ```
    CONFIG_SCHED_DEADLINE
    ```

    in your project configuration.

Parameters
:   | thread | A thread on which to set the deadline |
    | --- | --- |
    | deadline | A time delta, in cycle units |

## [◆ ](#gae2596d56800769b06fc03c194a126a97)k\_thread\_foreach()

| void k\_thread\_foreach | ( | [k\_thread\_user\_cb\_t](#gaf9f23a6ff9dae76af56f25b373e74c75) | *user\_cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[kernel.h](kernel_8h.md)>`

Iterate over all the threads in the system.

This routine iterates over all the threads in the system and calls the user\_cb function for each thread.

Parameters
:   | user\_cb | Pointer to the user callback function. |
    | --- | --- |
    | user\_data | Pointer to user data. |

Note
:   ```
    CONFIG_THREAD_MONITOR
    ```

    must be set for this function to be effective.
:   This API uses [k\_spin\_lock](group__spinlock__apis.md#gaac60da4347f5b29ff8c4e5f24c99b3bf "k_spin_lock") to protect the \_kernel.threads list which means creation of new threads and terminations of existing threads are blocked until this API returns.

## [◆ ](#ga82a83c2db36b34596dcb5afa5b28e41c)k\_thread\_foreach\_filter\_by\_cpu()

| void k\_thread\_foreach\_filter\_by\_cpu | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *cpu*, |
| --- | --- | --- | --- |
|  |  | [k\_thread\_user\_cb\_t](#gaf9f23a6ff9dae76af56f25b373e74c75) | *user\_cb*, |
|  |  | void \* | *user\_data* ) |

`#include <[kernel.h](kernel_8h.md)>`

Iterate over all the threads in running on specified cpu.

This function is does otherwise the same thing as [k\_thread\_foreach()](#gae2596d56800769b06fc03c194a126a97), but it only loops through the threads running on specified cpu only. If CONFIG\_SMP is not defined the implementation this is the same as [k\_thread\_foreach()](#gae2596d56800769b06fc03c194a126a97), with an assert cpu == 0.

Parameters
:   | cpu | The filtered cpu number |
    | --- | --- |
    | user\_cb | Pointer to the user callback function. |
    | user\_data | Pointer to user data. |

Note
:   ```
    CONFIG_THREAD_MONITOR
    ```

    must be set for this function to be effective.
:   This API uses [k\_spin\_lock](group__spinlock__apis.md#gaac60da4347f5b29ff8c4e5f24c99b3bf "k_spin_lock") to protect the \_kernel.threads list which means creation of new threads and terminations of existing threads are blocked until this API returns.

## [◆ ](#ga30ef8b445a6c1b4a82651674dbb737fc)k\_thread\_foreach\_unlocked()

| void k\_thread\_foreach\_unlocked | ( | [k\_thread\_user\_cb\_t](#gaf9f23a6ff9dae76af56f25b373e74c75) | *user\_cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[kernel.h](kernel_8h.md)>`

Iterate over all the threads in the system without locking.

This routine works exactly the same like [k\_thread\_foreach](#gae2596d56800769b06fc03c194a126a97) but unlocks interrupts when user\_cb is executed.

Parameters
:   | user\_cb | Pointer to the user callback function. |
    | --- | --- |
    | user\_data | Pointer to user data. |

Note
:   ```
    CONFIG_THREAD_MONITOR
    ```

    must be set for this function to be effective.
:   This API uses [k\_spin\_lock](group__spinlock__apis.md#gaac60da4347f5b29ff8c4e5f24c99b3bf "k_spin_lock") only when accessing the \_kernel.threads queue elements. It unlocks it during user callback function processing. If a new task is created when this `foreach` function is in progress, the added new task would not be included in the enumeration. If a task is aborted during this enumeration, there would be a race here and there is a possibility that this aborted task would be included in the enumeration.
:   If the task is aborted and the memory occupied by its `[k_thread](structk__thread.md "Thread Structure.")` structure is reused when this `k_thread_foreach_unlocked` is in progress it might even lead to the system behave unstable. This function may never return, as it would follow some `next` task pointers treating given pointer as a pointer to the [k\_thread](structk__thread.md "Thread Structure.") structure while it is something different right now. Do not reuse the memory that was occupied by [k\_thread](structk__thread.md "Thread Structure.") structure of aborted task if it was aborted after this function was called in any context.

## [◆ ](#gad908a1b9014aa048cf12997804ab7be2)k\_thread\_foreach\_unlocked\_filter\_by\_cpu()

| void k\_thread\_foreach\_unlocked\_filter\_by\_cpu | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *cpu*, |
| --- | --- | --- | --- |
|  |  | [k\_thread\_user\_cb\_t](#gaf9f23a6ff9dae76af56f25b373e74c75) | *user\_cb*, |
|  |  | void \* | *user\_data* ) |

`#include <[kernel.h](kernel_8h.md)>`

Iterate over the threads in running on current cpu without locking.

This function does otherwise the same thing as [k\_thread\_foreach\_unlocked()](#ga30ef8b445a6c1b4a82651674dbb737fc), but it only loops through the threads running on specified cpu. If CONFIG\_SMP is not defined the implementation this is the same as [k\_thread\_foreach\_unlocked()](#ga30ef8b445a6c1b4a82651674dbb737fc), with an assert requiring cpu == 0.

Parameters
:   | cpu | The filtered cpu number |
    | --- | --- |
    | user\_cb | Pointer to the user callback function. |
    | user\_data | Pointer to user data. |

Note
:   ```
    CONFIG_THREAD_MONITOR
    ```

    must be set for this function to be effective.
:   This API uses [k\_spin\_lock](group__spinlock__apis.md#gaac60da4347f5b29ff8c4e5f24c99b3bf "k_spin_lock") only when accessing the \_kernel.threads queue elements. It unlocks it during user callback function processing. If a new task is created when this `foreach` function is in progress, the added new task would not be included in the enumeration. If a task is aborted during this enumeration, there would be a race here and there is a possibility that this aborted task would be included in the enumeration.
:   If the task is aborted and the memory occupied by its `[k_thread](structk__thread.md "Thread Structure.")` structure is reused when this `k_thread_foreach_unlocked` is in progress it might even lead to the system behave unstable. This function may never return, as it would follow some `next` task pointers treating given pointer as a pointer to the [k\_thread](structk__thread.md "Thread Structure.") structure while it is something different right now. Do not reuse the memory that was occupied by [k\_thread](structk__thread.md "Thread Structure.") structure of aborted task if it was aborted after this function was called in any context.

## [◆ ](#ga3f46c06833add2a2e0ddb7242f06702c)k\_thread\_heap\_assign()

| | void k\_thread\_heap\_assign | ( | struct [k\_thread](structk__thread.md) \* | *thread*, | | --- | --- | --- | --- | |  |  | struct [k\_heap](structk__heap.md) \* | *heap* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Assign a resource memory pool to a thread.

By default, threads have no resource pool assigned unless their parent thread has a resource pool, in which case it is inherited. Multiple threads may be assigned to the same memory pool.

Changing a thread's resource pool will not migrate allocations from the previous pool.

Parameters
:   | thread | Target thread to assign a memory pool for resource requests. |
    | --- | --- |
    | heap | Heap object to use for resources, or NULL if the thread should no longer have a memory pool. |

## [◆ ](#ga40a733561eb1f64dcaae0e01b167d233)k\_thread\_join()

| int k\_thread\_join | ( | struct [k\_thread](structk__thread.md) \* | *thread*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](kernel_8h.md)>`

Sleep until a thread exits.

The caller will be put to sleep until the target thread exits, either due to being aborted, self-exiting, or taking a fatal error. This API returns immediately if the thread isn't running.

This API may only be called from ISRs with a K\_NO\_WAIT timeout, where it can be useful as a predicate to detect when a thread has aborted.

Parameters
:   | thread | Thread to wait to exit |
    | --- | --- |
    | timeout | upper bound time to wait for the thread to exit. |

Return values
:   | 0 | success, target thread has exited or wasn't running |
    | --- | --- |
    | -EBUSY | returned without waiting |
    | -EAGAIN | waiting period timed out |
    | -EDEADLK | target thread is joining on the caller, or target thread is the caller |

## [◆ ](#ga07b59ade055c69929ccdc08a14361794)k\_thread\_name\_copy()

| int k\_thread\_name\_copy | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread*, |
| --- | --- | --- | --- |
|  |  | char \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[kernel.h](kernel_8h.md)>`

Copy the thread name into a supplied buffer.

Parameters
:   | thread | Thread to obtain name information |
    | --- | --- |
    | buf | Destination buffer |
    | size | Destination buffer size |

Return values
:   | -ENOSPC | Destination buffer too small |
    | --- | --- |
    | -EFAULT | Memory access error |
    | -ENOSYS | Thread name feature not enabled |
    | 0 | Success |

## [◆ ](#gadebf45da56dee393164569742459dc0a)k\_thread\_name\_get()

| const char \* k\_thread\_name\_get | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get thread name.

Get the name of a thread

Parameters
:   | thread | Thread ID |
    | --- | --- |

Return values
:   | Thread | name, or NULL if configuration not enabled |
    | --- | --- |

## [◆ ](#ga23107333f134b9c9a8b692374211e841)k\_thread\_name\_set()

| int k\_thread\_name\_set | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread*, |
| --- | --- | --- | --- |
|  |  | const char \* | *str* ) |

`#include <[kernel.h](kernel_8h.md)>`

Set current thread name.

Set the name of the thread to be used when

```
CONFIG_THREAD_MONITOR
```

is enabled for tracing and debugging.

Parameters
:   | thread | Thread to set name, or NULL to set the current thread |
    | --- | --- |
    | str | Name string |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EFAULT | Memory access error with supplied string |
    | -ENOSYS | Thread name configuration option not enabled |
    | -EINVAL | Thread name too long |

## [◆ ](#ga3a46ed8ad2c3b12416fafe11325f82b3)k\_thread\_priority\_get()

| int k\_thread\_priority\_get | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get a thread's priority.

This routine gets the priority of *thread*.

Parameters
:   | thread | ID of thread whose priority is needed. |
    | --- | --- |

Returns
:   Priority of *thread*.

## [◆ ](#ga24e50a60c524d1eb22fe21cdf269b6a6)k\_thread\_priority\_set()

| void k\_thread\_priority\_set | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread*, |
| --- | --- | --- | --- |
|  |  | int | *prio* ) |

`#include <[kernel.h](kernel_8h.md)>`

Set a thread's priority.

This routine immediately changes the priority of *thread*.

Rescheduling can occur immediately depending on the priority *thread* is set to:

- If its priority is raised above the priority of a currently scheduled preemptible thread, *thread* will be scheduled in.
- If the caller lowers the priority of a currently scheduled preemptible thread below that of other threads in the system, the thread of the highest priority will be scheduled in.

Priority can be assigned in the range of -CONFIG\_NUM\_COOP\_PRIORITIES to CONFIG\_NUM\_PREEMPT\_PRIORITIES-1, where -CONFIG\_NUM\_COOP\_PRIORITIES is the highest priority.

Parameters
:   | thread | ID of thread whose priority is to be set. |
    | --- | --- |
    | prio | New priority. |

Warning
:   Changing the priority of a thread currently involved in mutex priority inheritance may result in undefined behavior.

## [◆ ](#ga117b26f8569ec3045ead1fad1851663d)k\_thread\_resume()

| void k\_thread\_resume | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Resume a suspended thread.

This routine allows the kernel scheduler to make *thread* the current thread, when it is next eligible for that role.

If *thread* is not currently suspended, the routine has no effect.

Parameters
:   | thread | ID of thread to resume. |
    | --- | --- |

## [◆ ](#gafe00cc70bac8a47ba6dda21bde508614)k\_thread\_stack\_alloc()

| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* k\_thread\_stack\_alloc | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
| --- | --- | --- | --- |
|  |  | int | *flags* ) |

`#include <[kernel.h](kernel_8h.md)>`

Dynamically allocate a thread stack.

Relevant stack creation flags include:

- [K\_USER](#gacb5340339892f22301e02697c6039ccc) allocate a userspace thread (requires CONFIG\_USERSPACE=y)

Parameters
:   | size | Stack size in bytes. |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Stack creation flags, or 0. |

Return values
:   | the | allocated thread stack on success. |
    | --- | --- |
    | NULL | on failure. |

See also
:   CONFIG\_DYNAMIC\_THREAD

## [◆ ](#ga95560cb85f6656b981a9a50ff2cd70b7)k\_thread\_stack\_free()

| int k\_thread\_stack\_free | ( | [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | *stack* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Free a dynamically allocated thread stack.

Parameters
:   | stack | Pointer to the thread stack. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EBUSY | if the thread stack is in use. |
    | -EINVAL | if `stack` is invalid. |
    | -ENOSYS | if dynamic thread stack allocation is disabled |

See also
:   CONFIG\_DYNAMIC\_THREAD

## [◆ ](#ga88031bd9fcfcd4305bae4029a4d8416f)k\_thread\_start()

| void k\_thread\_start | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Start an inactive thread.

If a thread was created with K\_FOREVER in the delay parameter, it will not be added to the scheduling queue until this function is called on it.

Parameters
:   | thread | thread to start |
    | --- | --- |

## [◆ ](#ga0c6af32096dc7ca391ffe2522bae4cb6)k\_thread\_state\_str()

| const char \* k\_thread\_state\_str | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread\_id*, |
| --- | --- | --- | --- |
|  |  | char \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buf\_size* ) |

`#include <[kernel.h](kernel_8h.md)>`

Get thread state string.

This routine generates a human friendly string containing the thread's state, and copies as much of it as possible into *buf*.

Parameters
:   | thread\_id | Thread ID |
    | --- | --- |
    | buf | Buffer into which to copy state strings |
    | buf\_size | Size of the buffer |

Return values
:   | Pointer | to *buf* if data was copied, else a pointer to "". |
    | --- | --- |

## [◆ ](#ga66cf8682fb65870eceb5e57d667a8d4e)k\_thread\_suspend()

| void k\_thread\_suspend | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Suspend a thread.

This routine prevents the kernel scheduler from making *thread* the current thread. All other internal operations on *thread* are still performed; for example, kernel objects it is waiting on are still handed to it. Note that any existing timeouts (e.g. [k\_sleep()](#ga48d4b041790454da4d68ac8711f29657), or a timeout argument to [k\_sem\_take()](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090 "Take a semaphore.") et. al.) will be canceled. On resume, the thread will begin running immediately and return from the blocked call.

When the target thread is active on another CPU, the caller will block until the target thread is halted (suspended or aborted). But if the caller is in an interrupt context, it will spin waiting for that target thread active on another CPU to halt.

If *thread* is already suspended, the routine has no effect.

Parameters
:   | thread | ID of thread to suspend. |
    | --- | --- |

## [◆ ](#ga563928f292a4134acd4142029b60e631)k\_thread\_time\_slice\_set()

| void k\_thread\_time\_slice\_set | ( | struct [k\_thread](structk__thread.md) \* | *th*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *slice\_ticks*, |
|  |  | [k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f) | *expired*, |
|  |  | void \* | *data* ) |

`#include <[kernel.h](kernel_8h.md)>`

Set thread time slice.

As for k\_sched\_time\_slice\_set, but (when CONFIG\_TIMESLICE\_PER\_THREAD=y) sets the timeslice for a specific thread. When non-zero, this timeslice will take precedence over the global value.

When such a thread's timeslice expires, the configured callback will be called before the thread is removed/re-added to the run queue. This callback will occur in interrupt context, and the specified thread is guaranteed to have been preempted by the currently-executing ISR. Such a callback is free to, for example, modify the thread priority or slice time for future execution, suspend the thread, etc...

Note
:   Unlike the older API, the time slice parameter here is specified in ticks, not milliseconds. Ticks have always been the internal unit, and not all platforms have integer conversions between the two.
:   Threads with a non-zero slice time set will be timesliced always, even if they are higher priority than the maximum timeslice priority set via [k\_sched\_time\_slice\_set()](#ga877c1bfeffbf8f097d1656f9e10a66e8).
:   The callback notification for slice expiration happens, as it must, while the thread is still "current", and thus it happens before any registered timeouts at this tick. This has the somewhat confusing side effect that the tick time (c.f. [k\_uptime\_get()](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69 "Get system uptime.")) does not yet reflect the expired ticks. Applications wishing to make fine-grained timing decisions within this callback should use the cycle API, or derived facilities like [k\_thread\_runtime\_stats\_get()](kernel_8h.md#a82d886a1c911b39c1b47c32200cedac6 "Get the runtime statistics of a thread.").

Parameters
:   | th | A valid, initialized thread |
    | --- | --- |
    | slice\_ticks | Maximum timeslice, in ticks |
    | expired | Callback function called on slice expiration |
    | data | Parameter for the expiration handler |

## [◆ ](#gab0b1c85b847fe74170c04538fa9949ff)k\_thread\_timeout\_expires\_ticks()

| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) k\_thread\_timeout\_expires\_ticks | ( | const struct [k\_thread](structk__thread.md) \* | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get time when a thread wakes up, in system ticks.

This routine computes the system uptime when a waiting thread next executes, in units of system ticks. If the thread is not waiting, it returns current system time.

## [◆ ](#ga4688c095c86e037a18594efdb9a5e9b9)k\_thread\_timeout\_remaining\_ticks()

| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) k\_thread\_timeout\_remaining\_ticks | ( | const struct [k\_thread](structk__thread.md) \* | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get time remaining before a thread wakes up, in system ticks.

This routine computes the time remaining before a waiting thread next executes, in units of system ticks. If the thread is not waiting, it returns zero.

## [◆ ](#ga3fbe1c8a5f3ef1c25382c7d6fca35764)k\_thread\_user\_mode\_enter()

| FUNC\_NORETURN void k\_thread\_user\_mode\_enter | ( | [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) | *entry*, |
| --- | --- | --- | --- |
|  |  | void \* | *p1*, |
|  |  | void \* | *p2*, |
|  |  | void \* | *p3* ) |

`#include <[kernel.h](kernel_8h.md)>`

Drop a thread's privileges permanently to user mode.

This allows a supervisor thread to be re-used as a user thread. This function does not return, but control will transfer to the provided entry point as if this was a new user thread.

The implementation ensures that the stack buffer contents are erased. Any thread-local storage will be reverted to a pristine state.

Memory domain membership, resource pool assignment, kernel object permissions, priority, and thread options are preserved.

A common use of this function is to re-use the main thread as a user thread once all supervisor mode-only tasks have been completed.

Parameters
:   | entry | Function to start executing from |
    | --- | --- |
    | p1 | 1st entry point parameter |
    | p2 | 2nd entry point parameter |
    | p3 | 3rd entry point parameter |

## [◆ ](#gaeac56bb072ce295b9fdc372ab8cee67e)k\_usleep()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) k\_usleep | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *us* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Put the current thread to sleep with microsecond resolution.

This function is unlikely to work as expected without kernel tuning. In particular, because the lower bound on the duration of a sleep is the duration of a tick,

```
CONFIG_SYS_CLOCK_TICKS_PER_SEC
```

must be adjusted to achieve the resolution desired. The implications of doing this must be understood before attempting to use [k\_usleep()](#gaeac56bb072ce295b9fdc372ab8cee67e). Use with caution.

Parameters
:   | us | Number of microseconds to sleep. |
    | --- | --- |

Returns
:   Zero if the requested time has elapsed or if the thread was woken up by the [k\_wakeup](#ga9275a019c8ff3c7fe49a81f8c078157e) call, the time left to sleep rounded up to the nearest microsecond.

## [◆ ](#ga9275a019c8ff3c7fe49a81f8c078157e)k\_wakeup()

| void k\_wakeup | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Wake up a sleeping thread.

This routine prematurely wakes up *thread* from sleeping.

If *thread* is not currently sleeping, the routine has no effect.

Parameters
:   | thread | ID of thread to wake. |
    | --- | --- |

## [◆ ](#ga08a3484c33444ecedc2d71d78495a295)k\_yield()

| void k\_yield | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Yield the current thread.

This routine causes the current thread to yield execution to another thread of the same or higher priority. If there are no other ready threads of the same or higher priority, the routine returns immediately.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
