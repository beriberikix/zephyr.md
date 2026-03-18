---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/psci_8h.html
original_path: doxygen/html/psci_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

psci.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/arch/arm64/arm-smccc.h](arm-smccc_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](psci_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PSCI\_VERSION\_MAJOR\_SHIFT](#aba5a843b7c3cd4ac675cd036b0048d25)   16 |
| #define | [PSCI\_VERSION\_MINOR\_MASK](#a119caefd53e8915d794c1e41da8c2057)   ((1U << [PSCI\_VERSION\_MAJOR\_SHIFT](#aba5a843b7c3cd4ac675cd036b0048d25)) - 1) |
| #define | [PSCI\_VERSION\_MAJOR\_MASK](#a27ec15f0330589ee26e3a5623a0ba15d)   ~[PSCI\_VERSION\_MINOR\_MASK](#a119caefd53e8915d794c1e41da8c2057) |
| #define | [PSCI\_VERSION\_MAJOR](#a1e6404a2f880eccc43566b399c1aded7)(ver) |
| #define | [PSCI\_VERSION\_MINOR](#affdc7b10fe33298091cfbfbd4ef290b0)(ver) |

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [psci\_version](#a1964266f31f19eb7e7e0acd4bb660f4c) (void) |

## Macro Definition Documentation

## [◆ ](#a1e6404a2f880eccc43566b399c1aded7)PSCI\_VERSION\_MAJOR

| #define PSCI\_VERSION\_MAJOR | ( |  | *ver* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((ver) & [PSCI\_VERSION\_MAJOR\_MASK](#a27ec15f0330589ee26e3a5623a0ba15d)) >> [PSCI\_VERSION\_MAJOR\_SHIFT](#aba5a843b7c3cd4ac675cd036b0048d25))

[PSCI\_VERSION\_MAJOR\_MASK](#a27ec15f0330589ee26e3a5623a0ba15d)

#define PSCI\_VERSION\_MAJOR\_MASK

**Definition** psci.h:23

[PSCI\_VERSION\_MAJOR\_SHIFT](#aba5a843b7c3cd4ac675cd036b0048d25)

#define PSCI\_VERSION\_MAJOR\_SHIFT

**Definition** psci.h:20

## [◆ ](#a27ec15f0330589ee26e3a5623a0ba15d)PSCI\_VERSION\_MAJOR\_MASK

| #define PSCI\_VERSION\_MAJOR\_MASK   ~[PSCI\_VERSION\_MINOR\_MASK](#a119caefd53e8915d794c1e41da8c2057) |
| --- |

## [◆ ](#aba5a843b7c3cd4ac675cd036b0048d25)PSCI\_VERSION\_MAJOR\_SHIFT

| #define PSCI\_VERSION\_MAJOR\_SHIFT   16 |
| --- |

## [◆ ](#affdc7b10fe33298091cfbfbd4ef290b0)PSCI\_VERSION\_MINOR

| #define PSCI\_VERSION\_MINOR | ( |  | *ver* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((ver) & [PSCI\_VERSION\_MINOR\_MASK](#a119caefd53e8915d794c1e41da8c2057))

[PSCI\_VERSION\_MINOR\_MASK](#a119caefd53e8915d794c1e41da8c2057)

#define PSCI\_VERSION\_MINOR\_MASK

**Definition** psci.h:21

## [◆ ](#a119caefd53e8915d794c1e41da8c2057)PSCI\_VERSION\_MINOR\_MASK

| #define PSCI\_VERSION\_MINOR\_MASK   ((1U << [PSCI\_VERSION\_MAJOR\_SHIFT](#aba5a843b7c3cd4ac675cd036b0048d25)) - 1) |
| --- |

## Function Documentation

## [◆ ](#a1964266f31f19eb7e7e0acd4bb660f4c)psci\_version()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) psci\_version | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pm\_cpu\_ops](dir_e793b4b61545b17399e4385df57fcbb6.md)
- [psci.h](psci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
