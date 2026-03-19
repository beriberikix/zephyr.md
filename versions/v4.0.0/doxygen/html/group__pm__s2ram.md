---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__pm__s2ram.html
original_path: doxygen/html/group__pm__s2ram.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

S2RAM APIs

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md)

| Typedefs | |
| --- | --- |
| typedef int(\* | [pm\_s2ram\_system\_off\_fn\_t](#ga61b569a4b9053443c9b82b0ea1bfae53)) (void) |
|  | System off function. |

| Functions | |
| --- | --- |
| int | [arch\_pm\_s2ram\_suspend](#ga6b82cf263c595b0d5cb353759000615c) ([pm\_s2ram\_system\_off\_fn\_t](#ga61b569a4b9053443c9b82b0ea1bfae53) system\_off) |
|  | Save CPU context on suspend. |
| void | [pm\_s2ram\_mark\_set](#ga88bb5cb4d2eb2c6014f0bad0e891ae1f) (void) |
|  | Mark that core is entering suspend-to-RAM state. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_s2ram\_mark\_check\_and\_clear](#ga93f351a7dafa34ccdffd7e97763ab34b) (void) |
|  | Check suspend-to-RAM marking and clear its state. |

## Detailed Description

## Typedef Documentation

## [◆ ](#ga61b569a4b9053443c9b82b0ea1bfae53)pm\_s2ram\_system\_off\_fn\_t

| typedef int(\* pm\_s2ram\_system\_off\_fn\_t) (void) |
| --- |

`#include <[pm_s2ram.h](pm__s2ram_8h.md)>`

System off function.

This function is passed as argument and called by [arch\_pm\_s2ram\_suspend](#ga6b82cf263c595b0d5cb353759000615c) to power the system off after the CPU context has been saved.

This function never returns if the system is powered off. If the operation cannot be performed a proper value is returned and the code must take care of restoring the system in a fully operational state before returning.

Return values
:   | none | The system is powered off. |
    | --- | --- |
    | -EBUSY | The system is busy and cannot be powered off at this time. |
    | -errno | Other error codes. |

## Function Documentation

## [◆ ](#ga6b82cf263c595b0d5cb353759000615c)arch\_pm\_s2ram\_suspend()

| int arch\_pm\_s2ram\_suspend | ( | [pm\_s2ram\_system\_off\_fn\_t](#ga61b569a4b9053443c9b82b0ea1bfae53) | *system\_off* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pm_s2ram.h](pm__s2ram_8h.md)>`

Save CPU context on suspend.

This function is used on suspend-to-RAM (S2RAM) to save the CPU context in (retained) RAM before powering the system off using the provided function. This function is usually called from the PM subsystem / hooks.

The CPU context is usually the minimum set of CPU registers which content must be restored on resume to let the platform resume its execution from the point it left at the time of suspension.

Parameters
:   | system\_off | Function to power off the system. |
    | --- | --- |

Return values
:   | 0 | The CPU context was successfully saved and restored. |
    | --- | --- |
    | -EBUSY | The system is busy and cannot be suspended at this time. |
    | -errno | Negative errno code in case of failure. |

## [◆ ](#ga93f351a7dafa34ccdffd7e97763ab34b)pm\_s2ram\_mark\_check\_and\_clear()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_s2ram\_mark\_check\_and\_clear | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pm_s2ram.h](pm__s2ram_8h.md)>`

Check suspend-to-RAM marking and clear its state.

Function is used to determine if resuming after suspend-to-RAM shall be performed or standard boot code shall be executed.

Default implementation is checking a magic word in RAM. CONFIG\_PM\_S2RAM\_CUSTOM\_MARKING allows custom implementation. The following requirements must be fulfilled:

- the function cannot use stack (most likely asm function)
- the content of the R1 and R4 registers must remain unchanged
- the function's return value is passed by R0 register
- returning from the function should be performed with the bx lr instruction

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if marking is found which indicates resuming after suspend-to-RAM. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if marking is not found which indicates standard boot. |

## [◆ ](#ga88bb5cb4d2eb2c6014f0bad0e891ae1f)pm\_s2ram\_mark\_set()

| void pm\_s2ram\_mark\_set | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pm_s2ram.h](pm__s2ram_8h.md)>`

Mark that core is entering suspend-to-RAM state.

Function is called when system state is stored to RAM, just before going to system off.

Default implementation is setting a magic word in RAM. CONFIG\_PM\_S2RAM\_CUSTOM\_MARKING allows custom implementation. The following requirements must be fulfilled:

- the function cannot use stack (asm function or function with 'naked' attribute)
- the content of the R1 and R4 registers must remain unchanged
- returning from the function should be performed with the bx lr instruction

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
