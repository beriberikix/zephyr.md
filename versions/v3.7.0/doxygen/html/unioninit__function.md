---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/unioninit__function.html
original_path: doxygen/html/unioninit__function.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

init\_function Union Reference

[Operating System Services](group__os__services.md) » [System Initialization](group__sys__init.md)

Initialization function for init entries.
[More...](#details)

`#include <[init.h](init_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [sys](#a147196ff078175284385ce2eb1448498) )(void) |
|  | System initialization function. |
| int(\* | [dev](#a074d663e90ecb3e3ffcd0b9f5f16eb08) )(const struct [device](structdevice.md) \*dev) |
|  | Device initialization function. |

## Detailed Description

Initialization function for init entries.

Init entries support both the system initialization and the device APIs. Each API has its own init function signature; hence, we have a union to cover both.

## Field Documentation

## [◆ ](#a074d663e90ecb3e3ffcd0b9f5f16eb08)dev

| int(\* init\_function::dev) (const struct [device](structdevice.md) \*dev) |
| --- |

Device initialization function.

Parameters
:   | [dev](#a074d663e90ecb3e3ffcd0b9f5f16eb08) | Device instance. |
    | --- | --- |

Return values
:   | 0 | On success |
    | --- | --- |
    | -errno | If device initialization fails. |

## [◆ ](#a147196ff078175284385ce2eb1448498)sys

| int(\* init\_function::sys) (void) |
| --- |

System initialization function.

Return values
:   | 0 | On success |
    | --- | --- |
    | -errno | If init fails. |

---

The documentation for this union was generated from the following file:

- zephyr/[init.h](init_8h_source.md)

- [init\_function](unioninit__function.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
