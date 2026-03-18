---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__arch-coredump.html
original_path: doxygen/html/group__arch-coredump.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture-specific core dump APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Functions | |
| --- | --- |
| void | [arch\_coredump\_info\_dump](#ga081b713e38ca635184f5f07bd7fd7a16) (const z\_arch\_esf\_t \*esf) |
|  | Architecture-specific handling during coredump. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [arch\_coredump\_tgt\_code\_get](#ga1d9b0c011a03434272ff9bec120f273d) (void) |
|  | Get the target code specified by the architecture. |

## Detailed Description

## Function Documentation

## [◆ ](#ga081b713e38ca635184f5f07bd7fd7a16)arch\_coredump\_info\_dump()

| void arch\_coredump\_info\_dump | ( | const z\_arch\_esf\_t \* | *esf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Architecture-specific handling during coredump.

This dumps architecture-specific information during coredump.

Parameters
:   | esf | Exception Stack Frame (arch-specific) |
    | --- | --- |

## [◆ ](#ga1d9b0c011a03434272ff9bec120f273d)arch\_coredump\_tgt\_code\_get()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) arch\_coredump\_tgt\_code\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Get the target code specified by the architecture.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
