---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__arch-coredump.html
original_path: doxygen/html/group__arch-coredump.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture-specific core dump APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Functions | |
| --- | --- |
| void | [arch\_coredump\_info\_dump](#gae997cb3dc249bec6d5166145f37d9292) (const struct [arch\_esf](structarch__esf.md) \*esf) |
|  | Architecture-specific handling during coredump. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [arch\_coredump\_tgt\_code\_get](#ga1d9b0c011a03434272ff9bec120f273d) (void) |
|  | Get the target code specified by the architecture. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [arch\_coredump\_stack\_ptr\_get](#gad53d55d1e9bf8c15137e204bc05d2732) (const struct [k\_thread](structk__thread.md) \*thread) |
|  | Get the stack pointer of the thread. |
| void | [arch\_coredump\_priv\_stack\_dump](#ga31bcb446604666c8f4d05ccfcbc00441) (struct [k\_thread](structk__thread.md) \*thread) |
|  | Architecture-specific handling of dumping privileged stack. |

## Detailed Description

## Function Documentation

## [◆ ](#gae997cb3dc249bec6d5166145f37d9292)arch\_coredump\_info\_dump()

| void arch\_coredump\_info\_dump | ( | const struct [arch\_esf](structarch__esf.md) \* | *esf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Architecture-specific handling during coredump.

This dumps architecture-specific information during coredump.

Parameters
:   | esf | Exception Stack Frame (arch-specific) |
    | --- | --- |

## [◆ ](#ga31bcb446604666c8f4d05ccfcbc00441)arch\_coredump\_priv\_stack\_dump()

| void arch\_coredump\_priv\_stack\_dump | ( | struct [k\_thread](structk__thread.md) \* | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Architecture-specific handling of dumping privileged stack.

This dumps the architecture-specific privileged stack during coredump.

Parameters
:   | thread | Pointer to thread object |
    | --- | --- |

## [◆ ](#gad53d55d1e9bf8c15137e204bc05d2732)arch\_coredump\_stack\_ptr\_get()

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arch\_coredump\_stack\_ptr\_get | ( | const struct [k\_thread](structk__thread.md) \* | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Get the stack pointer of the thread.

## [◆ ](#ga1d9b0c011a03434272ff9bec120f273d)arch\_coredump\_tgt\_code\_get()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) arch\_coredump\_tgt\_code\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Get the target code specified by the architecture.

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
