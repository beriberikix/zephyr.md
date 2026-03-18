---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__arch-threads.html
original_path: doxygen/html/group__arch-threads.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture thread APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Functions | |
| --- | --- |
| void | [arch\_new\_thread](#gade449838e445fa8201266e38215c616c) (struct [k\_thread](structk__thread.md) \*thread, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, char \*stack\_ptr, [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) entry, void \*p1, void \*p2, void \*p3) |
|  | Handle arch-specific logic for setting up new threads. |
| static void | [arch\_switch](#gab411d82ce5b60f062171f5a19e33e025) (void \*switch\_to, void \*\*switched\_from) |
|  | Cooperative context switch primitive. |
| void | [arch\_switch\_to\_main\_thread](#ga3ddd51635018a2e0235d5599401f5269) (struct [k\_thread](structk__thread.md) \*main\_thread, char \*stack\_ptr, [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) \_main) |
|  | Custom logic for entering main thread context at early boot. |
| int | [arch\_float\_disable](#ga7c2f0ee0bee6f9de0bd23a0aa321a46d) (struct [k\_thread](structk__thread.md) \*thread) |
|  | Disable floating point context preservation. |
| int | [arch\_float\_enable](#gacd40e26783f3dbd8a658fc1af512fb18) (struct [k\_thread](structk__thread.md) \*thread, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int options) |
|  | Enable floating point context preservation. |

## Detailed Description

## Function Documentation

## [◆ ](#ga7c2f0ee0bee6f9de0bd23a0aa321a46d)arch\_float\_disable()

| int arch\_float\_disable | ( | struct [k\_thread](structk__thread.md) \* | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Disable floating point context preservation.

The function is used to disable the preservation of floating point context information for a particular thread.

Note
:   For ARM architecture, disabling floating point preservation may only be requested for the current thread and cannot be requested in ISRs.

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EINVAL | If the floating point disabling could not be performed. |
    | -ENOTSUP | If the operation is not supported |

## [◆ ](#gacd40e26783f3dbd8a658fc1af512fb18)arch\_float\_enable()

| int arch\_float\_enable | ( | struct [k\_thread](structk__thread.md) \* | *thread*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *options* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Enable floating point context preservation.

The function is used to enable the preservation of floating point context information for a particular thread. This API depends on each architecture implementation. If the architecture does not support enabling, this API will always be failed.

The *options* parameter indicates which floating point register sets will be used by the specified thread. Currently it is used by x86 only.

Parameters
:   | thread | ID of thread. |
    | --- | --- |
    | options | architecture dependent options |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EINVAL | If the floating point enabling could not be performed. |
    | -ENOTSUP | If the operation is not supported |

## [◆ ](#gade449838e445fa8201266e38215c616c)arch\_new\_thread()

| void arch\_new\_thread | ( | struct [k\_thread](structk__thread.md) \* | *thread*, |
| --- | --- | --- | --- |
|  |  | [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | *stack*, |
|  |  | char \* | *stack\_ptr*, |
|  |  | [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) | *entry*, |
|  |  | void \* | *p1*, |
|  |  | void \* | *p2*, |
|  |  | void \* | *p3* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Handle arch-specific logic for setting up new threads.

The stack and arch-specific thread state variables must be set up such that a later attempt to switch to this thread will succeed and we will enter z\_thread\_entry with the requested thread and arguments as its parameters.

At some point in this function's implementation, z\_setup\_new\_thread() must be called with the true bounds of the available stack buffer within the thread's stack object.

The provided stack pointer is guaranteed to be properly aligned with respect to the CPU and ABI requirements. There may be space reserved between the stack pointer and the bounds of the stack buffer for initial stack pointer randomization and thread-local storage.

Fields in thread->base will be initialized when this is called.

Parameters
:   | thread | Pointer to uninitialized struct [k\_thread](structk__thread.md "Thread Structure.") |
    | --- | --- |
    | stack | Pointer to the stack object |
    | stack\_ptr | Aligned initial stack pointer |
    | entry | Thread entry function |
    | p1 | 1st entry point parameter |
    | p2 | 2nd entry point parameter |
    | p3 | 3rd entry point parameter |

## [◆ ](#gab411d82ce5b60f062171f5a19e33e025)arch\_switch()

| | void arch\_switch | ( | void \* | *switch\_to*, | | --- | --- | --- | --- | |  |  | void \*\* | *switched\_from* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Cooperative context switch primitive.

The action of [arch\_switch()](#gab411d82ce5b60f062171f5a19e33e025) should be to switch to a new context passed in the first argument, and save a pointer to the current context into the address passed in the second argument.

The actual type and interpretation of the switch handle is specified by the architecture. It is the same data structure stored in the "switch\_handle" field of a newly-created thread in [arch\_new\_thread()](#gade449838e445fa8201266e38215c616c), and passed to the kernel as the "interrupted" argument to z\_get\_next\_switch\_handle().

Note that on SMP systems, the kernel uses the store through the second pointer as a synchronization point to detect when a thread context is completely saved (so another CPU can know when it is safe to switch). This store must be done AFTER all relevant state is saved, and must include whatever memory barriers or cache management code is required to be sure another CPU will see the result correctly.

The simplest implementation of [arch\_switch()](#gab411d82ce5b60f062171f5a19e33e025) is generally to push state onto the thread stack and use the resulting stack pointer as the switch handle. Some architectures may instead decide to use a pointer into the thread struct as the "switch handle" type. These can legally assume that the second argument to [arch\_switch()](#gab411d82ce5b60f062171f5a19e33e025) is the address of the switch\_handle field of struct thread\_base and can use an offset on this value to find other parts of the thread struct. For example a (C pseudocode) implementation of [arch\_switch()](#gab411d82ce5b60f062171f5a19e33e025) might look like:

void [arch\_switch(void \*switch\_to, void \*\*switched\_from)](#gab411d82ce5b60f062171f5a19e33e025) { struct [k\_thread](structk__thread.md "Thread Structure.") \*new = switch\_to; struct [k\_thread](structk__thread.md "Thread Structure.") \*old = [CONTAINER\_OF(switched\_from, struct k\_thread,
switch\_handle)](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f "Get a pointer to a structure containing the element.");

// save old context... \*switched\_from = old; // restore new context... }

Note that the kernel manages the switch\_handle field for synchronization as described above. So it is not legal for architecture code to assume that it has any particular value at any other time. In particular it is not legal to read the field from the address passed in the second argument.

Parameters
:   | switch\_to | Incoming thread's switch handle |
    | --- | --- |
    | switched\_from | Pointer to outgoing thread's switch handle storage location, which must be updated. |

## [◆ ](#ga3ddd51635018a2e0235d5599401f5269)arch\_switch\_to\_main\_thread()

| void arch\_switch\_to\_main\_thread | ( | struct [k\_thread](structk__thread.md) \* | *main\_thread*, |
| --- | --- | --- | --- |
|  |  | char \* | *stack\_ptr*, |
|  |  | [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) | *\_main* ) |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Custom logic for entering main thread context at early boot.

Used by architectures where the typical trick of setting up a dummy thread in early boot context to "switch out" of isn't workable.

Parameters
:   | main\_thread | main thread object |
    | --- | --- |
    | stack\_ptr | Initial stack pointer |
    | \_main | Entry point for application main function. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
