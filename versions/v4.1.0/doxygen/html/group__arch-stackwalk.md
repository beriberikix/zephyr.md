---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__arch-stackwalk.html
original_path: doxygen/html/group__arch-stackwalk.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture-specific Stack Walk APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

To add API support to an architecture, [arch\_stack\_walk()](#ga7129c254277cfa162cd9c5778a7662c2) should be implemented and a non-user configurable Kconfig ARCH\_HAS\_STACKWALK that is default to y should be created in the architecture's top level Kconfig, with all the relevant dependencies.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [stack\_trace\_callback\_fn](#gaec9949df614728aa6d677f9f1fafd844)) (void \*cookie, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long addr) |
|  | [stack\_trace\_callback\_fn](#gaec9949df614728aa6d677f9f1fafd844) - Callback for [arch\_stack\_walk](#ga7129c254277cfa162cd9c5778a7662c2) |

| Functions | |
| --- | --- |
| void | [arch\_stack\_walk](#ga7129c254277cfa162cd9c5778a7662c2) ([stack\_trace\_callback\_fn](#gaec9949df614728aa6d677f9f1fafd844) callback\_fn, void \*cookie, const struct [k\_thread](structk__thread.md) \*thread, const struct [arch\_esf](structarch__esf.md) \*esf) |
|  | Architecture-specific function to walk the stack. |

## Detailed Description

To add API support to an architecture, [arch\_stack\_walk()](#ga7129c254277cfa162cd9c5778a7662c2) should be implemented and a non-user configurable Kconfig ARCH\_HAS\_STACKWALK that is default to y should be created in the architecture's top level Kconfig, with all the relevant dependencies.

## Typedef Documentation

## [◆ ](#gaec9949df614728aa6d677f9f1fafd844)stack\_trace\_callback\_fn

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* stack\_trace\_callback\_fn) (void \*cookie, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long addr) |
| --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

[stack\_trace\_callback\_fn](#gaec9949df614728aa6d677f9f1fafd844) - Callback for [arch\_stack\_walk](#ga7129c254277cfa162cd9c5778a7662c2)

Parameters
:   | cookie | Caller supplied pointer handed back by [arch\_stack\_walk](#ga7129c254277cfa162cd9c5778a7662c2) |
    | --- | --- |
    | addr | The stack entry address to consume |

Returns
:   True, if the entry was consumed or skipped. False, if there is no space left to store

## Function Documentation

## [◆ ](#ga7129c254277cfa162cd9c5778a7662c2)arch\_stack\_walk()

| void arch\_stack\_walk | ( | [stack\_trace\_callback\_fn](#gaec9949df614728aa6d677f9f1fafd844) | *callback\_fn*, |
| --- | --- | --- | --- |
|  |  | void \* | *cookie*, |
|  |  | const struct [k\_thread](structk__thread.md) \* | *thread*, |
|  |  | const struct [arch\_esf](structarch__esf.md) \* | *esf* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Architecture-specific function to walk the stack.

Parameters
:   | callback\_fn | Callback which is invoked by the architecture code for each entry. |
    | --- | --- |
    | cookie | Caller supplied pointer which is handed back to *callback\_fn* |
    | thread | Pointer to a [k\_thread](structk__thread.md "Thread Structure.") struct, can be NULL |
    | esf | Pointer to an [arch\_esf](structarch__esf.md "Exception Stack Frame.") struct, can be NULL |

============ ======= ============================================ thread esf ============ ======= ============================================ thread NULL Stack trace from thread (can be \_current) thread esf Stack trace starting on esf ============ ======= ============================================

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
