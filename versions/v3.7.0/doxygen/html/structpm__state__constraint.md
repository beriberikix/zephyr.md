---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpm__state__constraint.html
original_path: doxygen/html/structpm__state__constraint.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm\_state\_constraint Struct Reference

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md) » [States](group__subsys__pm__states.md)

Power state information needed to lock a power state.
[More...](#details)

`#include <[state.h](state_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) | [state](#aabbdf004f6cbf8a5464f03cb63bb518e) |
|  | Power management state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [substate\_id](#a1007d7769f3529bb91db30fc503964ad) |
|  | Power management sub-state. |

## Detailed Description

Power state information needed to lock a power state.

## Field Documentation

## [◆ ](#aabbdf004f6cbf8a5464f03cb63bb518e)state

| enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) pm\_state\_constraint::state |
| --- |

Power management state.

See also
:   [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5 "Power management state.")

## [◆ ](#a1007d7769f3529bb91db30fc503964ad)substate\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pm\_state\_constraint::substate\_id |
| --- |

Power management sub-state.

See also
:   [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5 "Power management state.")

---

The documentation for this struct was generated from the following file:

- zephyr/pm/[state.h](state_8h_source.md)

- [pm\_state\_constraint](structpm__state__constraint.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
