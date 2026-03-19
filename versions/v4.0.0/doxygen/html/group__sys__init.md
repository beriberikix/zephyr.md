---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__sys__init.html
original_path: doxygen/html/group__sys__init.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

System Initialization

[Operating System Services](group__os__services.md)

Zephyr offers an infrastructure to call initialization code before main.
[More...](#details)

| Data Structures | |
| --- | --- |
| union | [init\_function](unioninit__function.md) |
|  | Initialization function for init entries. [More...](unioninit__function.md#details) |
| struct | [init\_entry](structinit__entry.md) |
|  | Structure to store initialization entry information. [More...](structinit__entry.md#details) |

| Macros | |
| --- | --- |
| #define | [INIT\_LEVEL\_ORD](#ga3025b426a99f8351d4b483205f437e48)(level) |
|  | Obtain the ordinal for an init level. |
| #define | [SYS\_INIT](#gaf507cc0613add8113c41896bd631254f)(init\_fn, level, prio) |
|  | Register an initialization function. |
| #define | [SYS\_INIT\_NAMED](#gae862feb31eb4628b8ec95b471e5d4c54)(name, init\_fn\_, level, prio) |
|  | Register an initialization function (named). |

## Detailed Description

Zephyr offers an infrastructure to call initialization code before main.

Such initialization calls can be registered using [SYS\_INIT()](#gaf507cc0613add8113c41896bd631254f) or [SYS\_INIT\_NAMED()](#gae862feb31eb4628b8ec95b471e5d4c54) macros. By using a combination of initialization levels and priorities init sequence can be adjusted as needed. The available initialization levels are described, in order, below:

- EARLY: Used very early in the boot process, right after entering the C domain (z\_cstart()). This can be used in architectures and SoCs that extend or implement architecture code and use drivers or system services that have to be initialized before the Kernel calls any architecture specific initialization code.
- PRE\_KERNEL\_1: Executed in Kernel's initialization context, which uses the interrupt stack. At this point Kernel services are not yet available.
- PRE\_KERNEL\_2: Same as PRE\_KERNEL\_1.
- POST\_KERNEL: Executed after Kernel is alive. From this point on, Kernel primitives can be used.
- APPLICATION: Executed just before application code (main).
- SMP: Only available if

  ```
  CONFIG_SMP
  ```

  is enabled, specific for SMP.

Initialization priority can take a value in the range of 0 to 99.

Note
:   The same infrastructure is used by devices.

## Macro Definition Documentation

## [◆ ](#ga3025b426a99f8351d4b483205f437e48)INIT\_LEVEL\_ORD

| #define INIT\_LEVEL\_ORD | ( |  | *level* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[init.h](init_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(Z\_INIT\_EARLY\_##level, (Z\_INIT\_ORD\_EARLY), \

([COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(Z\_INIT\_PRE\_KERNEL\_1\_##level, (Z\_INIT\_ORD\_PRE\_KERNEL\_1), \

([COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(Z\_INIT\_PRE\_KERNEL\_2\_##level, (Z\_INIT\_ORD\_PRE\_KERNEL\_2), \

([COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(Z\_INIT\_POST\_KERNEL\_##level, (Z\_INIT\_ORD\_POST\_KERNEL), \

([COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(Z\_INIT\_APPLICATION\_##level, (Z\_INIT\_ORD\_APPLICATION), \

([COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(Z\_INIT\_SMP\_##level, (Z\_INIT\_ORD\_SMP), \

([ZERO\_OR\_COMPILE\_ERROR](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)(0)))))))))))))

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

[ZERO\_OR\_COMPILE\_ERROR](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)

#define ZERO\_OR\_COMPILE\_ERROR(cond)

0 if cond is true-ish; causes a compile error otherwise.

**Definition** util.h:90

Obtain the ordinal for an init level.

Parameters
:   | level | Init level (EARLY, PRE\_KERNEL\_1, PRE\_KERNEL\_2, POST\_KERNEL, APPLICATION, SMP). |
    | --- | --- |

Returns
:   Init level ordinal.

## [◆ ](#gaf507cc0613add8113c41896bd631254f)SYS\_INIT

| #define SYS\_INIT | ( |  | *init\_fn*, |
| --- | --- | --- | --- |
|  |  |  | *level*, |
|  |  |  | *prio* ) |

`#include <[init.h](init_8h.md)>`

**Value:**

[SYS\_INIT\_NAMED](#gae862feb31eb4628b8ec95b471e5d4c54)(init\_fn, init\_fn, level, prio)

[SYS\_INIT\_NAMED](#gae862feb31eb4628b8ec95b471e5d4c54)

#define SYS\_INIT\_NAMED(name, init\_fn\_, level, prio)

Register an initialization function (named).

**Definition** init.h:238

Register an initialization function.

The function will be called during system initialization according to the given level and priority.

Parameters
:   | init\_fn | Initialization function. |
    | --- | --- |
    | level | Initialization level. Allowed tokens: EARLY, PRE\_KERNEL\_1, PRE\_KERNEL\_2, POST\_KERNEL, APPLICATION and SMP if  ``` CONFIG_SMP ```  is enabled. |
    | prio | Initialization priority within `_level`. Note that it must be a decimal integer literal without leading zeroes or sign (e.g. 32), or an equivalent symbolic name (e.g. #define MY\_INIT\_PRIO 32); symbolic expressions are **not** permitted (e.g. CONFIG\_KERNEL\_INIT\_PRIORITY\_DEFAULT + 5). |

## [◆ ](#gae862feb31eb4628b8ec95b471e5d4c54)SYS\_INIT\_NAMED

| #define SYS\_INIT\_NAMED | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn\_*, |
|  |  |  | *level*, |
|  |  |  | *prio* ) |

`#include <[init.h](init_8h.md)>`

**Value:**

static const Z\_DECL\_ALIGN(struct [init\_entry](structinit__entry.md)) \

Z\_INIT\_ENTRY\_SECTION(level, prio, 0) \_\_used \_\_noasan \

Z\_INIT\_ENTRY\_NAME(name) = {.init\_fn = {.sys = (init\_fn\_)}, \

Z\_INIT\_SYS\_INIT\_DEV\_NULL}

[init\_entry](structinit__entry.md)

Structure to store initialization entry information.

**Definition** init.h:103

Register an initialization function (named).

Note
:   This macro can be used for cases where the multiple init calls use the same init function.

Parameters
:   | name | Unique name for SYS\_INIT entry. |
    | --- | --- |
    | init\_fn\_ | See [SYS\_INIT()](#gaf507cc0613add8113c41896bd631254f). |
    | level | See [SYS\_INIT()](#gaf507cc0613add8113c41896bd631254f). |
    | prio | See [SYS\_INIT()](#gaf507cc0613add8113c41896bd631254f). |

See also
:   [SYS\_INIT()](#gaf507cc0613add8113c41896bd631254f)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
