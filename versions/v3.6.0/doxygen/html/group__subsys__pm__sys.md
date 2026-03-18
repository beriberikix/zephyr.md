---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__pm__sys.html
original_path: doxygen/html/group__subsys__pm__sys.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

System

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md)

System Power Management API.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Hooks](group__subsys__pm__sys__hooks.md) |
|  | System Power Management Hooks. |
|  | [Policy](group__subsys__pm__sys__policy.md) |
|  | System Power Management Policy API. |

| Data Structures | |
| --- | --- |
| struct | [pm\_notifier](structpm__notifier.md) |
|  | Power management notifier struct. [More...](structpm__notifier.md#details) |

| Functions | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_state\_force](#ga075be307983f4efdcc93252a31a4258a) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu, const struct [pm\_state\_info](structpm__state__info.md) \*info) |
|  | Force usage of given power state. |
| void | [pm\_notifier\_register](#ga066945118b8f287ee56aacf41b677a78) (struct [pm\_notifier](structpm__notifier.md) \*notifier) |
|  | Register a power management notifier. |
| int | [pm\_notifier\_unregister](#gab0856d662e50a3847a1b70cb8370849a) (struct [pm\_notifier](structpm__notifier.md) \*notifier) |
|  | Unregister a power management notifier. |
| const struct [pm\_state\_info](structpm__state__info.md) \* | [pm\_state\_next\_get](#ga3861a1a0009b96d15de00059257848dd) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu) |
|  | Gets the next power state that will be used. |

## Detailed Description

System Power Management API.

## Function Documentation

## [◆ ](#ga066945118b8f287ee56aacf41b677a78)pm\_notifier\_register()

| void pm\_notifier\_register | ( | struct [pm\_notifier](structpm__notifier.md) \* | *notifier* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pm.h](pm_8h.md)>`

Register a power management notifier.

Register the given notifier from the power management notification list.

Parameters
:   | notifier | [pm\_notifier](structpm__notifier.md "Power management notifier struct.") object to be registered. |
    | --- | --- |

## [◆ ](#gab0856d662e50a3847a1b70cb8370849a)pm\_notifier\_unregister()

| int pm\_notifier\_unregister | ( | struct [pm\_notifier](structpm__notifier.md) \* | *notifier* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pm.h](pm_8h.md)>`

Unregister a power management notifier.

Remove the given notifier from the power management notification list. After that this object callbacks will not be called.

Parameters
:   | notifier | [pm\_notifier](structpm__notifier.md "Power management notifier struct.") object to be unregistered. |
    | --- | --- |

Returns
:   0 if the notifier was successfully removed, a negative value otherwise.

## [◆ ](#ga075be307983f4efdcc93252a31a4258a)pm\_state\_force()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_state\_force | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cpu*, |
| --- | --- | --- | --- |
|  |  | const struct [pm\_state\_info](structpm__state__info.md) \* | *info* ) |

`#include <[pm.h](pm_8h.md)>`

Force usage of given power state.

This function overrides decision made by PM policy forcing usage of given power state upon next entry of the idle thread.

Note
:   This function can only run in thread context

Parameters
:   | cpu | CPU index. |
    | --- | --- |
    | info | Power state which should be used in the ongoing suspend operation. |

## [◆ ](#ga3861a1a0009b96d15de00059257848dd)pm\_state\_next\_get()

| const struct [pm\_state\_info](structpm__state__info.md) \* pm\_state\_next\_get | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cpu* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pm.h](pm_8h.md)>`

Gets the next power state that will be used.

This function returns the next power state that will be used by the SoC.

Parameters
:   | cpu | CPU index. |
    | --- | --- |

Returns
:   next [pm\_state\_info](structpm__state__info.md "Information about a power management state.") that will be used

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
