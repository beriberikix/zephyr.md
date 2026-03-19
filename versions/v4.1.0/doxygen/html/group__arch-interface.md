---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__arch-interface.html
original_path: doxygen/html/group__arch-interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture Interface

[Internal and System API](group__internal__api.md)

Internal kernel APIs with public scope.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Architecture thread APIs](group__arch-threads.md) |
|  |  |
|  | [Architecture timing APIs](group__arch-timing.md) |
|  | [Architecture-specific IRQ APIs](group__arch-irq.md) |
|  |  |
|  | [Architecture-specific SMP APIs](group__arch-smp.md) |
|  |  |
|  | [Architecture-specific Stack Walk APIs](group__arch-stackwalk.md) |
|  | To add API support to an architecture, [arch\_stack\_walk()](group__arch-stackwalk.md#ga7129c254277cfa162cd9c5778a7662c2 "Architecture-specific function to walk the stack.") should be implemented and a non-user configurable Kconfig ARCH\_HAS\_STACKWALK that is default to y should be created in the architecture's top level Kconfig, with all the relevant dependencies. |
|  | [Architecture-specific Thread Local Storage APIs](group__arch-tls.md) |
|  | [Architecture-specific core dump APIs](group__arch-coredump.md) |
|  | [Architecture-specific gdbstub APIs](group__arch-gdbstub.md) |
|  | [Architecture-specific memory-mapping APIs](group__arch-mmu.md) |
|  | [Architecture-specific power management APIs](group__arch-pm.md) |
|  |  |
|  | [Architecture-specific userspace APIs](group__arch-userspace.md) |
|  | [Miscellaneous architecture APIs](group__arch-misc.md) |
|  | [Xtensa APIs](group__xtensa__apis.md) |

## Detailed Description

Internal kernel APIs with public scope.

Any public kernel APIs that are implemented as inline functions and need to call architecture-specific API so will have the prototypes for the architecture-specific APIs here. Architecture APIs that aren't used in this way go in [kernel/include/kernel\_arch\_interface.h](kernel__arch__interface_8h.md "Internal kernel APIs implemented at the architecture layer.").

The set of architecture-specific APIs used internally by public macros and inline functions in public headers are also specified and documented.

For all macros and inline function prototypes described herein, <[arch/cpu.h](cpu_8h.md)> must eventually pull in full definitions for all of them (the actual macro defines and inline function bodies)

include/kernel.h and other public headers depend on definitions in this header.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
