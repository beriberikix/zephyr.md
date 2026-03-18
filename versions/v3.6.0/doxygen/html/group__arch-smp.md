---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__arch-smp.html
original_path: doxygen/html/group__arch-smp.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture-specific SMP APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [arch\_cpustart\_t](#ga4a9ac90ba7cc7c403472bfdaf3369ed2)) (void \*data) |
|  | Per-cpu entry function. |

| Functions | |
| --- | --- |
| void | [arch\_start\_cpu](#gad25e65419116c6bb3e6d6362e780fb83) (int cpu\_num, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, int sz, [arch\_cpustart\_t](#ga4a9ac90ba7cc7c403472bfdaf3369ed2) fn, void \*arg) |
|  | Start a numbered CPU on a MP-capable system. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_cpu\_active](#ga5a7f0198ee061551c300129bffe64717) (int cpu\_num) |
|  | Return CPU power status. |
| static struct \_cpu \* | [arch\_curr\_cpu](#gad42138d41dff6a4aad8abf7d77fcd8b2) (void) |
|  | Return the CPU struct for the currently executing CPU. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_proc\_id](#gad628c89816128546501e3c26eaaf9dea) (void) |
|  | Processor hardware ID. |
| void | [arch\_sched\_ipi](#gadd3d6c84e3c57babc859314718e0f231) (void) |
|  | Broadcast an interrupt to all CPUs. |
| int | [arch\_smp\_init](#ga6ffc01f86f4541d1092ee4b277a07ac6) (void) |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arch\_num\_cpus](#ga078e9bf1a4a557d1321ddc4848092cbe) (void) |
|  | Returns the number of CPUs. |

## Detailed Description

## Typedef Documentation

## [◆ ](#ga4a9ac90ba7cc7c403472bfdaf3369ed2)arch\_cpustart\_t

| typedef void(\* arch\_cpustart\_t) (void \*data) |
| --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Per-cpu entry function.

Parameters
:   | data | context parameter, implementation specific |
    | --- | --- |

## Function Documentation

## [◆ ](#ga5a7f0198ee061551c300129bffe64717)arch\_cpu\_active()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_cpu\_active | ( | int | *cpu\_num* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Return CPU power status.

Parameters
:   | cpu\_num | Integer number of the CPU |
    | --- | --- |

## [◆ ](#gad42138d41dff6a4aad8abf7d77fcd8b2)arch\_curr\_cpu()

| | struct \_cpu \* arch\_curr\_cpu | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Return the CPU struct for the currently executing CPU.

## [◆ ](#ga078e9bf1a4a557d1321ddc4848092cbe)arch\_num\_cpus()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_num\_cpus | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Returns the number of CPUs.

For most systems this will be the same as CONFIG\_MP\_MAX\_NUM\_CPUS, however some systems may determine this at runtime instead.

Returns
:   the number of CPUs

## [◆ ](#gad628c89816128546501e3c26eaaf9dea)arch\_proc\_id()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_proc\_id | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Processor hardware ID.

Most multiprocessor architectures have a low-level unique ID value associated with the current CPU that can be retrieved rapidly and efficiently in kernel context. Note that while the numbering of the CPUs is guaranteed to be unique, the values are platform-defined. In particular, they are not guaranteed to match Zephyr's own sequential CPU IDs (even though on some platforms they do).

Note
:   There is an inherent race with this API: the system may preempt the current thread and migrate it to another CPU before the value is used. Safe usage requires knowing the migration is impossible (e.g. because the code is in interrupt context, holds a spinlock, or cannot migrate due to k\_cpu\_mask state).

Returns
:   Unique ID for currently-executing CPU

## [◆ ](#gadd3d6c84e3c57babc859314718e0f231)arch\_sched\_ipi()

| void arch\_sched\_ipi | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Broadcast an interrupt to all CPUs.

This will invoke z\_sched\_ipi() on other CPUs in the system.

## [◆ ](#ga6ffc01f86f4541d1092ee4b277a07ac6)arch\_smp\_init()

| int arch\_smp\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

## [◆ ](#gad25e65419116c6bb3e6d6362e780fb83)arch\_start\_cpu()

| void arch\_start\_cpu | ( | int | *cpu\_num*, |
| --- | --- | --- | --- |
|  |  | [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | *stack*, |
|  |  | int | *sz*, |
|  |  | [arch\_cpustart\_t](#ga4a9ac90ba7cc7c403472bfdaf3369ed2) | *fn*, |
|  |  | void \* | *arg* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Start a numbered CPU on a MP-capable system.

This starts and initializes a specific CPU. The main thread on startup is running on CPU zero, other processors are numbered sequentially. On return from this function, the CPU is known to have begun operating and will enter the provided function. Its interrupts will be initialized but disabled such that [irq\_unlock()](group__isr__apis.md#ga646045943b3b2a130738bcc48867bf57 "Unlock interrupts.") with the provided key will work to enable them.

Normally, in SMP mode this function will be called by the kernel initialization and should not be used as a user API. But it is defined here for special-purpose apps which want Zephyr running on one core and to use others for design-specific processing.

Parameters
:   | cpu\_num | Integer number of the CPU |
    | --- | --- |
    | stack | Stack memory for the CPU |
    | sz | Stack buffer size, in bytes |
    | fn | Function to begin running on the CPU. |
    | arg | Untyped argument to be passed to "fn" |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
