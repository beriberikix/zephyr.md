---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__fatal__apis.html
original_path: doxygen/html/group__fatal__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Fatal error APIs

[Kernel APIs](group__kernel__apis.md)

| Topics | |
| --- | --- |
|  | [Fatal error base types](group__fatal__types.md) |

| Functions | |
| --- | --- |
| FUNC\_NORETURN void | [k\_fatal\_halt](#gaa8c0b43a2360e5319d7910e8e0ceb951) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason) |
|  | Halt the system on a fatal error. |
| void | [k\_sys\_fatal\_error\_handler](#ga255cc816d227f0a5c0e80e61bfba11fa) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason, const struct [arch\_esf](structarch__esf.md) \*esf) |
|  | Fatal error policy handler. |

## Detailed Description

## Function Documentation

## [◆ ](#gaa8c0b43a2360e5319d7910e8e0ceb951)k\_fatal\_halt()

| FUNC\_NORETURN void k\_fatal\_halt | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reason* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fatal.h](fatal_8h.md)>`

Halt the system on a fatal error.

Invokes architecture-specific code to power off or halt the system in a low power state. Lacking that, lock interrupts and sit in an idle loop.

Parameters
:   | reason | Fatal exception reason code |
    | --- | --- |

## [◆ ](#ga255cc816d227f0a5c0e80e61bfba11fa)k\_sys\_fatal\_error\_handler()

| void k\_sys\_fatal\_error\_handler | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reason*, |
| --- | --- | --- | --- |
|  |  | const struct [arch\_esf](structarch__esf.md) \* | *esf* ) |

`#include <[fatal.h](fatal_8h.md)>`

Fatal error policy handler.

This function is not invoked by application code, but is declared as a weak symbol so that applications may introduce their own policy.

The default implementation of this function halts the system unconditionally. Depending on architecture support, this may be a simple infinite loop, power off the hardware, or exit an emulator.

If this function returns, then the currently executing thread will be aborted.

A few notes for custom implementations:

- If the error is determined to be unrecoverable, [LOG\_PANIC()](group__log__ctrl.md#ga9ee5a99e0487e3f1e6d289b12c19ad5a) should be invoked to flush any pending logging buffers.
- K\_ERR\_KERNEL\_PANIC indicates a severe unrecoverable error in the kernel itself, and should not be considered recoverable. There is an assertion in z\_fatal\_error() to enforce this.
- Even outside of a kernel panic, unless the fault occurred in user mode, the kernel itself may be in an inconsistent state, with API calls to kernel objects possibly exhibiting undefined behavior or triggering another exception.

Parameters
:   | reason | The reason for the fatal error |
    | --- | --- |
    | esf | Exception context, with details and partial or full register state when the error occurred. May in some cases be NULL. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
