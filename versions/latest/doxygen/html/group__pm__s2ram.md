---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__pm__s2ram.html
original_path: doxygen/html/group__pm__s2ram.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
