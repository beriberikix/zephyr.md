---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__subsys__pm__sys__hooks.html
original_path: doxygen/html/group__subsys__pm__sys__hooks.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Hooks

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md) » [System](group__subsys__pm__sys.md)

System Power Management Hooks.
[More...](#details)

| Functions | |
| --- | --- |
| void | [pm\_state\_set](#gaa5c707f5c9c14494a388c6c2144e8f61) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) substate\_id) |
|  | Put processor into a power state. |
| void | [pm\_state\_exit\_post\_ops](#ga7594e7e9b41c180ac760b7b0c47673b2) (enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) substate\_id) |
|  | Do any SoC or architecture specific post ops after sleep state exits. |

## Detailed Description

System Power Management Hooks.

## Function Documentation

## [◆ ](#ga7594e7e9b41c180ac760b7b0c47673b2)pm\_state\_exit\_post\_ops()

| void pm\_state\_exit\_post\_ops | ( | enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) | *state*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *substate\_id* ) |

`#include <[pm.h](pm_8h.md)>`

Do any SoC or architecture specific post ops after sleep state exits.

This function is a place holder to do any operations that may be needed to be done after sleep state exits. Currently it enables interrupts after resuming from sleep state. In future, the enabling of interrupts may be moved into the kernel.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Power state. |
    | --- | --- |
    | substate\_id | Power substate id. |

## [◆ ](#gaa5c707f5c9c14494a388c6c2144e8f61)pm\_state\_set()

| void pm\_state\_set | ( | enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) | *state*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *substate\_id* ) |

`#include <[pm.h](pm_8h.md)>`

Put processor into a power state.

This function implements the SoC specific details necessary to put the processor into available power states.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Power state. |
    | --- | --- |
    | substate\_id | Power substate id. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
