---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__cpu__idle__apis.html
original_path: doxygen/html/group__cpu__idle__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CPU Idling APIs

[Kernel APIs](group__kernel__apis.md)

| Functions | |
| --- | --- |
| static void | [k\_cpu\_idle](#ga7b25e1bed511a813b32fbd0f91b09356) (void) |
|  | Make the CPU idle. |
| static void | [k\_cpu\_atomic\_idle](#gadf88ece6447b65b7d0d2f3a70ab4fe8f) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
|  | Make the CPU idle in an atomic fashion. |

## Detailed Description

## Function Documentation

## [◆ ](#gadf88ece6447b65b7d0d2f3a70ab4fe8f)k\_cpu\_atomic\_idle()

| | void k\_cpu\_atomic\_idle | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Make the CPU idle in an atomic fashion.

Similar to [k\_cpu\_idle()](#ga7b25e1bed511a813b32fbd0f91b09356), but must be called with interrupts locked.

Enabling interrupts and entering a low-power mode will be atomic, i.e. there will be no period of time where interrupts are enabled before the processor enters a low-power mode.

After waking up from the low-power mode, the interrupt lockout state will be restored as if by [irq\_unlock(key)](group__isr__apis.md#ga646045943b3b2a130738bcc48867bf57 "Unlock interrupts.").

Parameters
:   | key | Interrupt locking key obtained from [irq\_lock()](group__isr__apis.md#ga19fdde73c3b02fcca6cf1d1e67631228 "Lock interrupts."). |
    | --- | --- |

## [◆ ](#ga7b25e1bed511a813b32fbd0f91b09356)k\_cpu\_idle()

| | void k\_cpu\_idle | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Make the CPU idle.

This function makes the CPU idle until an event wakes it up.

In a regular system, the idle thread should be the only thread responsible for making the CPU idle and triggering any type of power management. However, in some more constrained systems, such as a single-threaded system, the only thread would be responsible for this if needed.

Note
:   In some architectures, before returning, the function unmasks interrupts unconditionally.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
