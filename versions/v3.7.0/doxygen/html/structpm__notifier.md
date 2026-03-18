---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpm__notifier.html
original_path: doxygen/html/structpm__notifier.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm\_notifier Struct Reference

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md) » [System](group__subsys__pm__sys.md)

Power management notifier struct.
[More...](#details)

`#include <[pm.h](pm_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [state\_entry](#ab84353bcc32f4262ea1a34f316d21278) )(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Application defined function for doing any target specific operations for power state entry. |
| void(\* | [state\_exit](#aeb6bcf67d2d4c5342d8d81cea3728ec5) )(enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Application defined function for doing any target specific operations for power state exit. |

## Detailed Description

Power management notifier struct.

This struct contains callbacks that are called when the target enters and exits power states.

As currently implemented the entry callback is invoked when transitioning from PM\_STATE\_ACTIVE to another state, and the exit callback is invoked when transitioning from a non-active state to PM\_STATE\_ACTIVE. This behavior may change in the future.

Note
:   These callbacks can be called from the ISR of the event that caused the kernel exit from idling.
:   It is not allowed to call [pm\_notifier\_unregister](group__subsys__pm__sys.md#gab0856d662e50a3847a1b70cb8370849a "pm_notifier_unregister") or [pm\_notifier\_register](group__subsys__pm__sys.md#ga066945118b8f287ee56aacf41b677a78 "pm_notifier_register") from these callbacks because they are called with the spin locked in those functions.

## Field Documentation

## [◆ ](#ab84353bcc32f4262ea1a34f316d21278)state\_entry

| void(\* pm\_notifier::state\_entry) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Application defined function for doing any target specific operations for power state entry.

## [◆ ](#aeb6bcf67d2d4c5342d8d81cea3728ec5)state\_exit

| void(\* pm\_notifier::state\_exit) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Application defined function for doing any target specific operations for power state exit.

---

The documentation for this struct was generated from the following file:

- zephyr/pm/[pm.h](pm_8h_source.md)

- [pm\_notifier](structpm__notifier.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
