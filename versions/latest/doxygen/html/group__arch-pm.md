---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__arch-pm.html
original_path: doxygen/html/group__arch-pm.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture-specific power management APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Functions | |
| --- | --- |
| FUNC\_NORETURN void | [arch\_system\_halt](#gada83bf3beb5004a39a1f9c8c7ce35348) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason) |
|  | Halt the system, optionally propagating a reason code. |
| void | [arch\_cpu\_idle](#ga6ce051203e6cc091d0fb42a15f662a48) (void) |
|  | Power save idle routine. |
| void | [arch\_cpu\_atomic\_idle](#ga4d0297717c23a3cc5df434549e26924d) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
|  | Atomically re-enable interrupts and enter low power mode. |

## Detailed Description

## Function Documentation

## [◆ ](#ga4d0297717c23a3cc5df434549e26924d)arch\_cpu\_atomic\_idle()

| void arch\_cpu\_atomic\_idle | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Atomically re-enable interrupts and enter low power mode.

The requirements for [arch\_cpu\_atomic\_idle()](#ga4d0297717c23a3cc5df434549e26924d) are as follows:

1. Enabling interrupts and entering a low-power mode needs to be atomic, i.e. there should be no period of time where interrupts are enabled before the processor enters a low-power mode. See the comments in [k\_lifo\_get()](group__lifo__apis.md#gad5f1775947b07a2a77f667aa9e41db5a "Get an element from a LIFO queue."), for example, of the race condition that occurs if this requirement is not met.
2. After waking up from the low-power mode, the interrupt lockout state must be restored as indicated in the 'key' input parameter.

See also
:   [k\_cpu\_atomic\_idle()](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f "Make the CPU idle in an atomic fashion.")

Parameters
:   | key | Lockout key returned by previous invocation of [arch\_irq\_lock()](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38 "Lock interrupts on the current CPU.") |
    | --- | --- |

## [◆ ](#ga6ce051203e6cc091d0fb42a15f662a48)arch\_cpu\_idle()

| void arch\_cpu\_idle | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Power save idle routine.

This function will be called by the kernel idle loop or possibly within an implementation of z\_pm\_save\_idle in the kernel when the '\_pm\_save\_flag' variable is non-zero.

Architectures that do not implement power management instructions may immediately return, otherwise a power-saving instruction should be issued to wait for an interrupt.

Note
:   The function is expected to return after the interrupt that has caused the CPU to exit power-saving mode has been serviced, although this is not a firm requirement.

See also
:   [k\_cpu\_idle()](group__cpu__idle__apis.md#ga7b25e1bed511a813b32fbd0f91b09356 "Make the CPU idle.")

## [◆ ](#gada83bf3beb5004a39a1f9c8c7ce35348)arch\_system\_halt()

| FUNC\_NORETURN void arch\_system\_halt | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reason* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Halt the system, optionally propagating a reason code.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
