---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__arch-userspace.html
original_path: doxygen/html/group__arch-userspace.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture-specific userspace APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Functions | |
| --- | --- |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke0](#ga5e9ab24b9c980e327903fbe3f5bd97f3) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 0 arguments. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke1](#ga4cfb3b2b38e5afca889e8b9765d6c3df) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 1 argument. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke2](#ga1e78f1022aaf10e88727b142b56d4ef0) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 2 arguments. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke3](#gaacb1c66a1b7bf2293fea269f6b5e1c7e) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 3 arguments. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke4](#ga0ba3ae2290827385b226ebdbf3de3b53) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 4 arguments. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke5](#ga9971c78bc8f579a0dadf84225dc0c3ff) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 5 arguments. |
| static [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_syscall\_invoke6](#gac6cae2197637993a86b6ec6803b5742b) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) call\_id) |
|  | Invoke a system call with 6 arguments. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_is\_user\_context](#ga89ab53a218add419e37f89c1f5fd955f) (void) |
|  | Indicate whether we are currently running in user mode. |
| int | [arch\_mem\_domain\_max\_partitions\_get](#ga71542fcc679a94ad9ea60d7ac46da361) (void) |
|  | Get the maximum number of partitions for a memory domain. |
| int | [arch\_buffer\_validate](#ga1532ef5705aa71f0f93899abca0939da) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, int write) |
|  | Check memory region permissions. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_virt\_region\_align](#ga48be2412ba65ec550ded63e2f1a0470f) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Get the optimal virtual region alignment to optimize the MMU table layout. |
| FUNC\_NORETURN void | [arch\_user\_mode\_enter](#ga447daa0454a90a7a3a247de01e522567) ([k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) user\_entry, void \*p1, void \*p2, void \*p3) |
|  | Perform a one-way transition from supervisor to user mode. |
| FUNC\_NORETURN void | [arch\_syscall\_oops](#gad53908f229d7e2c333574b009493644b) (void \*ssf) |
|  | Induce a kernel oops that appears to come from a specific location. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [arch\_user\_string\_nlen](#ga174c4f356fe315c523cefbf513858c9c) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) maxsize, int \*err) |
|  | Safely take the length of a potentially bad string. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_mem\_coherent](#ga8c6bb0f6730c115689452b016ac1761f) (void \*ptr) |
|  | Detect memory coherence type. |
| static void | [arch\_cohere\_stacks](#ga306e9d0e5f8094cb75686f1c43d068a9) (struct [k\_thread](structk__thread.md) \*old\_thread, void \*old\_switch\_handle, struct [k\_thread](structk__thread.md) \*new\_thread) |
|  | Ensure cache coherence prior to context switch. |

## Detailed Description

## Function Documentation

## [◆ ](#ga1532ef5705aa71f0f93899abca0939da)arch\_buffer\_validate()

| int arch\_buffer\_validate | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | int | *write* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Check memory region permissions.

Given a memory region, return whether the current memory management hardware configuration would allow a user thread to read/write that region. Used by system calls to validate buffers coming in from userspace.

Notes: The function is guaranteed to never return validation success, if the entire buffer area is not user accessible.

The function is guaranteed to correctly validate the permissions of the supplied buffer, if the user access permissions of the entire buffer are enforced by a single, enabled memory management region.

In some architectures the validation will always return failure if the supplied memory buffer spans multiple enabled memory management regions (even if all such regions permit user access).

Warning
:   Buffer of size zero (0) has undefined behavior.

Parameters
:   | addr | start address of the buffer |
    | --- | --- |
    | size | the size of the buffer |
    | write | If non-zero, additionally check if the area is writable. Otherwise, just check if the memory can be read. |

Returns
:   nonzero if the permissions don't match.

## [◆ ](#ga306e9d0e5f8094cb75686f1c43d068a9)arch\_cohere\_stacks()

| | void arch\_cohere\_stacks | ( | struct [k\_thread](structk__thread.md) \* | *old\_thread*, | | --- | --- | --- | --- | |  |  | void \* | *old\_switch\_handle*, | |  |  | struct [k\_thread](structk__thread.md) \* | *new\_thread* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Ensure cache coherence prior to context switch.

Required when ARCH\_HAS\_COHERENCE is true. On cache-incoherent multiprocessor architectures, thread stacks are cached by default for performance reasons. They must therefore be flushed appropriately on context switch. The rules are:

1. The region containing live data in the old stack (generally the bytes between the current stack pointer and the top of the stack memory) must be flushed to underlying storage so a new CPU that runs the same thread sees the correct data. This must happen before the assignment of the switch\_handle field in the thread struct which signals the completion of context switch.
2. Any data areas to be read from the new stack (generally the same as the live region when it was saved) should be invalidated (and NOT flushed!) in the data cache. This is because another CPU may have run or re-initialized the thread since this CPU suspended it, and any data present in cache will be stale.

Note
:   The kernel will call this function during interrupt exit when a new thread has been chosen to run, and also immediately before entering [arch\_switch()](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025 "Cooperative context switch primitive.") to effect a code-driven context switch. In the latter case, it is very likely that more data will be written to the old\_thread stack region after this function returns but before the completion of the switch. Simply flushing naively here is not sufficient on many architectures and coordination with the [arch\_switch()](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025 "Cooperative context switch primitive.") implementation is likely required.

Parameters
:   | old\_thread | The old thread to be flushed before being allowed to run on other CPUs. |
    | --- | --- |
    | old\_switch\_handle | The switch handle to be stored into old\_thread (it will not be valid until the cache is flushed so is not present yet). This will be NULL if inside z\_swap() (because the [arch\_switch()](group__arch-threads.md#gab411d82ce5b60f062171f5a19e33e025 "Cooperative context switch primitive.") has not saved it yet). |
    | new\_thread | The new thread to be invalidated before it runs locally. |

## [◆ ](#ga89ab53a218add419e37f89c1f5fd955f)arch\_is\_user\_context()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_is\_user\_context | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Indicate whether we are currently running in user mode.

Returns
:   True if the CPU is currently running with user permissions

## [◆ ](#ga8c6bb0f6730c115689452b016ac1761f)arch\_mem\_coherent()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_mem\_coherent | ( | void \* | *ptr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Detect memory coherence type.

Required when ARCH\_HAS\_COHERENCE is true. This function returns true if the byte pointed to lies within an architecture-defined "coherence region" (typically implemented with uncached memory) and can safely be used in multiprocessor code without explicit flush or invalidate operations.

Note
:   The result is for only the single byte at the specified address, this API is not required to check region boundaries or to expect aligned pointers. The expectation is that the code above will have queried the appropriate address(es).

## [◆ ](#ga71542fcc679a94ad9ea60d7ac46da361)arch\_mem\_domain\_max\_partitions\_get()

| int arch\_mem\_domain\_max\_partitions\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Get the maximum number of partitions for a memory domain.

Returns
:   Max number of partitions, or -1 if there is no limit

## [◆ ](#ga5e9ab24b9c980e327903fbe3f5bd97f3)arch\_syscall\_invoke0()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke0 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Invoke a system call with 0 arguments.

No general-purpose register state other than return value may be preserved when transitioning from supervisor mode back down to user mode for security reasons.

It is required that all arguments be stored in registers when elevating privileges from user to supervisor mode.

Processing of the syscall takes place on a separate kernel stack. Interrupts should be enabled when invoking the system call marshallers from the dispatch table. Thread preemption may occur when handling system calls.

Call IDs are untrusted and must be bounds-checked, as the value is used to index the system call dispatch table, containing function pointers to the specific system call code.

Parameters
:   | call\_id | System call ID |
    | --- | --- |

Returns
:   Return value of the system call. Void system calls return 0 here.

## [◆ ](#ga4cfb3b2b38e5afca889e8b9765d6c3df)arch\_syscall\_invoke1()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke1 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Invoke a system call with 1 argument.

See also
:   [arch\_syscall\_invoke0()](#ga5e9ab24b9c980e327903fbe3f5bd97f3)

Parameters
:   | arg1 | First argument to the system call. |
    | --- | --- |
    | call\_id | System call ID, will be bounds-checked and used to reference kernel-side dispatch table |

Returns
:   Return value of the system call. Void system calls return 0 here.

## [◆ ](#ga1e78f1022aaf10e88727b142b56d4ef0)arch\_syscall\_invoke2()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke2 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Invoke a system call with 2 arguments.

See also
:   [arch\_syscall\_invoke0()](#ga5e9ab24b9c980e327903fbe3f5bd97f3)

Parameters
:   | arg1 | First argument to the system call. |
    | --- | --- |
    | arg2 | Second argument to the system call. |
    | call\_id | System call ID, will be bounds-checked and used to reference kernel-side dispatch table |

Returns
:   Return value of the system call. Void system calls return 0 here.

## [◆ ](#gaacb1c66a1b7bf2293fea269f6b5e1c7e)arch\_syscall\_invoke3()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke3 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Invoke a system call with 3 arguments.

See also
:   [arch\_syscall\_invoke0()](#ga5e9ab24b9c980e327903fbe3f5bd97f3)

Parameters
:   | arg1 | First argument to the system call. |
    | --- | --- |
    | arg2 | Second argument to the system call. |
    | arg3 | Third argument to the system call. |
    | call\_id | System call ID, will be bounds-checked and used to reference kernel-side dispatch table |

Returns
:   Return value of the system call. Void system calls return 0 here.

## [◆ ](#ga0ba3ae2290827385b226ebdbf3de3b53)arch\_syscall\_invoke4()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke4 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg4*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Invoke a system call with 4 arguments.

See also
:   [arch\_syscall\_invoke0()](#ga5e9ab24b9c980e327903fbe3f5bd97f3)

Parameters
:   | arg1 | First argument to the system call. |
    | --- | --- |
    | arg2 | Second argument to the system call. |
    | arg3 | Third argument to the system call. |
    | arg4 | Fourth argument to the system call. |
    | call\_id | System call ID, will be bounds-checked and used to reference kernel-side dispatch table |

Returns
:   Return value of the system call. Void system calls return 0 here.

## [◆ ](#ga9971c78bc8f579a0dadf84225dc0c3ff)arch\_syscall\_invoke5()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke5 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg4*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg5*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Invoke a system call with 5 arguments.

See also
:   [arch\_syscall\_invoke0()](#ga5e9ab24b9c980e327903fbe3f5bd97f3)

Parameters
:   | arg1 | First argument to the system call. |
    | --- | --- |
    | arg2 | Second argument to the system call. |
    | arg3 | Third argument to the system call. |
    | arg4 | Fourth argument to the system call. |
    | arg5 | Fifth argument to the system call. |
    | call\_id | System call ID, will be bounds-checked and used to reference kernel-side dispatch table |

Returns
:   Return value of the system call. Void system calls return 0 here.

## [◆ ](#gac6cae2197637993a86b6ec6803b5742b)arch\_syscall\_invoke6()

| | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_syscall\_invoke6 | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg1*, | | --- | --- | --- | --- | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg2*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg3*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg4*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg5*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *arg6*, | |  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *call\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Invoke a system call with 6 arguments.

See also
:   [arch\_syscall\_invoke0()](#ga5e9ab24b9c980e327903fbe3f5bd97f3)

Parameters
:   | arg1 | First argument to the system call. |
    | --- | --- |
    | arg2 | Second argument to the system call. |
    | arg3 | Third argument to the system call. |
    | arg4 | Fourth argument to the system call. |
    | arg5 | Fifth argument to the system call. |
    | arg6 | Sixth argument to the system call. |
    | call\_id | System call ID, will be bounds-checked and used to reference kernel-side dispatch table |

Returns
:   Return value of the system call. Void system calls return 0 here.

## [◆ ](#gad53908f229d7e2c333574b009493644b)arch\_syscall\_oops()

| FUNC\_NORETURN void arch\_syscall\_oops | ( | void \* | *ssf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Induce a kernel oops that appears to come from a specific location.

Normally, [k\_oops()](include_2zephyr_2kernel_8h.md#abde5aa8ca5e64a045b25b88f91370dcd "Fatally terminate a thread.") generates an exception that appears to come from the call site of the [k\_oops()](include_2zephyr_2kernel_8h.md#abde5aa8ca5e64a045b25b88f91370dcd "Fatally terminate a thread.") itself.

However, when validating arguments to a system call, if there are problems we want the oops to appear to come from where the system call was invoked and not inside the validation function.

Parameters
:   | ssf | System call stack frame pointer. This gets passed as an argument to \_k\_syscall\_handler\_t functions and its contents are completely architecture specific. |
    | --- | --- |

## [◆ ](#ga447daa0454a90a7a3a247de01e522567)arch\_user\_mode\_enter()

| FUNC\_NORETURN void arch\_user\_mode\_enter | ( | [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) | *user\_entry*, |
| --- | --- | --- | --- |
|  |  | void \* | *p1*, |
|  |  | void \* | *p2*, |
|  |  | void \* | *p3* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Perform a one-way transition from supervisor to user mode.

Implementations of this function must do the following:

- Reset the thread's stack pointer to a suitable initial value. We do not need any prior context since this is a one-way operation.
- Set up any kernel stack region for the CPU to use during privilege elevation
- Put the CPU in whatever its equivalent of user mode is
- Transfer execution to [arch\_new\_thread()](group__arch-threads.md#gade449838e445fa8201266e38215c616c "Handle arch-specific logic for setting up new threads.") passing along all the supplied arguments, in user mode.

Parameters
:   | user\_entry | Entry point to start executing as a user thread |
    | --- | --- |
    | p1 | 1st parameter to user thread |
    | p2 | 2nd parameter to user thread |
    | p3 | 3rd parameter to user thread |

## [◆ ](#ga174c4f356fe315c523cefbf513858c9c)arch\_user\_string\_nlen()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) arch\_user\_string\_nlen | ( | const char \* | *s*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *maxsize*, |
|  |  | int \* | *err* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Safely take the length of a potentially bad string.

This must not fault, instead the `err` parameter must have -1 written to it. This function otherwise should work exactly like libc [strnlen()](string_8h.md#afc92d2231e45d19988c7894aa2a07f0c). On success `err` should be set to 0.

Parameters
:   | [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) | String to measure |
    | --- | --- |
    | maxsize | Max length of the string |
    | err | Error value to write |

Returns
:   Length of the string, not counting NULL byte, up to maxsize

## [◆ ](#ga48be2412ba65ec550ded63e2f1a0470f)arch\_virt\_region\_align()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) arch\_virt\_region\_align | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *phys*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Get the optimal virtual region alignment to optimize the MMU table layout.

Some MMU HW requires some region to be aligned to some of the intermediate block alignment in order to reduce table usage. This call returns the optimal virtual address alignment in order to permit such optimization in the following MMU mapping call.

Parameters
:   | [in] | phys | Physical address of region to be mapped, aligned to `CONFIG_MMU_PAGE_SIZE` |
    | --- | --- | --- |
    | [in] | size | Size of region to be mapped, aligned to `CONFIG_MMU_PAGE_SIZE` |

Returns
:   Alignment to apply on the virtual address of this region

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
