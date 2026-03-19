---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stats_2stats_8h.html
original_path: doxygen/html/stats_2stats_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stats.h File Reference

Statistics.
[More...](#details)

`#include <stddef.h>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](stats_2stats_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [stats\_name\_map](structstats__name__map.md) |
| struct | [stats\_hdr](structstats__hdr.md) |

| Macros | |
| --- | --- |
| #define | [STATS\_SECT\_DECL](#a21af7c98ccb9abb9464b9ef9358be880)(group\_\_) |
|  | Declares a stat group struct. |
| #define | [STATS\_SECT\_END](#a4124f8c0a9ffb78d8be608a780676785)   } |
|  | Ends a stats group struct definition. |
| #define | [STATS\_SECT\_START](#ae8e85c3ce2d901f4668d7237b19999fe)(group\_\_) |
| #define | [STATS\_SECT\_ENTRY](#afe8558503af10039b08a11f89c722783)(var\_\_) |
| #define | [STATS\_SECT\_ENTRY16](#a681ab1b4b39cb753e362eedbd78943a9)(var\_\_) |
| #define | [STATS\_SECT\_ENTRY32](#a592329613cc77cfa5dee3e1d3b16dd93)(var\_\_) |
| #define | [STATS\_SECT\_ENTRY64](#a589764c7a1e7d60fe0285b839c6c36b4)(var\_\_) |
| #define | [STATS\_RESET](#ae0ec8d3d690545650c06db95bea1a9c7)(var\_\_) |
| #define | [STATS\_SIZE\_INIT\_PARMS](#a9fdb886ee0a9b207a89ccd56a727f6b3)(group\_\_, size\_\_) |
| #define | [STATS\_INCN](#ac5d5050e8684027a3efb5a8e7a830be6)(group\_\_, var\_\_, n\_\_) |
| #define | [STATS\_INC](#a725e1bf6b2c486de9603954974d6315a)(group\_\_, var\_\_) |
| #define | [STATS\_SET](#a106def612fe69b2d4cbc2e5c3e6f1993)(group\_\_, var\_\_) |
| #define | [STATS\_CLEAR](#a1cce9ba94338a7fb027c78b32e638da5)(group\_\_, var\_\_) |
| #define | [STATS\_INIT\_AND\_REG](#a7a3f6d5dc044e6948998b8bc19efa493)(group\_\_, size\_\_, name\_\_) |
| #define | [STATS\_NAME\_START](#abd76143ad82eea7aded01af8cb7bc9ae)(name\_\_) |
| #define | [STATS\_NAME](#a30648b154e6da64aa39551fac123dd1b)(name\_\_, entry\_\_) |
| #define | [STATS\_NAME\_END](#a0de61377bb7c254b68cb39a9b5105e4f)(name\_\_) |
| #define | [STATS\_NAME\_INIT\_PARMS](#ad1a94bded5ab34ac48c0dfd4cbdc168f)(name\_\_) |

## Detailed Description

Statistics.

Statistics are per-module event counters for troubleshooting, maintenance, and usage monitoring. Statistics are organized into named "groups", with each group consisting of a set of "entries". An entry corresponds to an individual counter. Each entry can optionally be named if the STATS\_NAMES setting is enabled. Statistics can be retrieved with the mcumgr management subsystem.

There are two, largely duplicated, statistics sections here, in order to provide the optional ability to name statistics.

STATS\_SECT\_START/END actually declare the statistics structure definition, [STATS\_SECT\_DECL()](#a21af7c98ccb9abb9464b9ef9358be880) creates the structure declaration so you can declare these statistics as a global structure, and STATS\_NAME\_START/END are how you name the statistics themselves.

Statistics entries can be declared as any of several integer types. However, all statistics in a given structure must be of the same size, and they are all unsigned.

- [STATS\_SECT\_ENTRY()](#afe8558503af10039b08a11f89c722783): default statistic entry, 32-bits.
- [STATS\_SECT\_ENTRY16()](#a681ab1b4b39cb753e362eedbd78943a9): 16-bits. Smaller statistics if you need to fit into specific RAM or code size numbers.
- [STATS\_SECT\_ENTRY32()](#a592329613cc77cfa5dee3e1d3b16dd93): 32-bits.
- [STATS\_SECT\_ENTRY64()](#a589764c7a1e7d60fe0285b839c6c36b4): 64-bits. Useful for storing chunks of data.

Following the static entry declaration is the statistic names declaration. This is compiled out when the CONFIGURE\_STATS\_NAME setting is undefined.

When CONFIG\_STATS\_NAMES is defined, the statistics names are stored and returned to the management APIs. When the setting is undefined, temporary names are generated as needed with the following format:

```
s<stat-idx>
```

E.g., "s0", "s1", etc.

## Macro Definition Documentation

## [◆ ](#a1cce9ba94338a7fb027c78b32e638da5)STATS\_CLEAR

| #define STATS\_CLEAR | ( |  | *group\_\_*, |
| --- | --- | --- | --- |
|  |  |  | *var\_\_* ) |

## [◆ ](#a725e1bf6b2c486de9603954974d6315a)STATS\_INC

| #define STATS\_INC | ( |  | *group\_\_*, |
| --- | --- | --- | --- |
|  |  |  | *var\_\_* ) |

## [◆ ](#ac5d5050e8684027a3efb5a8e7a830be6)STATS\_INCN

| #define STATS\_INCN | ( |  | *group\_\_*, |
| --- | --- | --- | --- |
|  |  |  | *var\_\_*, |
|  |  |  | *n\_\_* ) |

## [◆ ](#a7a3f6d5dc044e6948998b8bc19efa493)STATS\_INIT\_AND\_REG

| #define STATS\_INIT\_AND\_REG | ( |  | *group\_\_*, |
| --- | --- | --- | --- |
|  |  |  | *size\_\_*, |
|  |  |  | *name\_\_* ) |

**Value:**

(0)

## [◆ ](#a30648b154e6da64aa39551fac123dd1b)STATS\_NAME

| #define STATS\_NAME | ( |  | *name\_\_*, |
| --- | --- | --- | --- |
|  |  |  | *entry\_\_* ) |

## [◆ ](#a0de61377bb7c254b68cb39a9b5105e4f)STATS\_NAME\_END

| #define STATS\_NAME\_END | ( |  | *name\_\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ad1a94bded5ab34ac48c0dfd4cbdc168f)STATS\_NAME\_INIT\_PARMS

| #define STATS\_NAME\_INIT\_PARMS | ( |  | *name\_\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

NULL, 0

## [◆ ](#abd76143ad82eea7aded01af8cb7bc9ae)STATS\_NAME\_START

| #define STATS\_NAME\_START | ( |  | *name\_\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae0ec8d3d690545650c06db95bea1a9c7)STATS\_RESET

| #define STATS\_RESET | ( |  | *var\_\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a21af7c98ccb9abb9464b9ef9358be880)STATS\_SECT\_DECL

| #define STATS\_SECT\_DECL | ( |  | *group\_\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

struct stats\_ ## group\_\_

Declares a stat group struct.

Parameters
:   | group\_\_ | The name to assign to the structure tag. |
    | --- | --- |

## [◆ ](#a4124f8c0a9ffb78d8be608a780676785)STATS\_SECT\_END

| #define STATS\_SECT\_END   } |
| --- |

Ends a stats group struct definition.

## [◆ ](#afe8558503af10039b08a11f89c722783)STATS\_SECT\_ENTRY

| #define STATS\_SECT\_ENTRY | ( |  | *var\_\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a681ab1b4b39cb753e362eedbd78943a9)STATS\_SECT\_ENTRY16

| #define STATS\_SECT\_ENTRY16 | ( |  | *var\_\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a592329613cc77cfa5dee3e1d3b16dd93)STATS\_SECT\_ENTRY32

| #define STATS\_SECT\_ENTRY32 | ( |  | *var\_\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a589764c7a1e7d60fe0285b839c6c36b4)STATS\_SECT\_ENTRY64

| #define STATS\_SECT\_ENTRY64 | ( |  | *var\_\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae8e85c3ce2d901f4668d7237b19999fe)STATS\_SECT\_START

| #define STATS\_SECT\_START | ( |  | *group\_\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STATS\_SECT\_DECL](#a21af7c98ccb9abb9464b9ef9358be880)(group\_\_) {

[STATS\_SECT\_DECL](#a21af7c98ccb9abb9464b9ef9358be880)

#define STATS\_SECT\_DECL(group\_\_)

Declares a stat group struct.

**Definition** stats.h:83

## [◆ ](#a106def612fe69b2d4cbc2e5c3e6f1993)STATS\_SET

| #define STATS\_SET | ( |  | *group\_\_*, |
| --- | --- | --- | --- |
|  |  |  | *var\_\_* ) |

## [◆ ](#a9fdb886ee0a9b207a89ccd56a727f6b3)STATS\_SIZE\_INIT\_PARMS

| #define STATS\_SIZE\_INIT\_PARMS | ( |  | *group\_\_*, |
| --- | --- | --- | --- |
|  |  |  | *size\_\_* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [stats](dir_5f661b5f7a66b36130669509de91835d.md)
- [stats.h](stats_2stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
