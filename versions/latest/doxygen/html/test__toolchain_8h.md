---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/test__toolchain_8h.html
original_path: doxygen/html/test__toolchain_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

test\_toolchain.h File Reference

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](test__toolchain_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TOOLCHAIN\_WARNING\_ALLOC\_SIZE\_LARGER\_THAN](#a46a35ee1419f878aff6c4502a82fdad4) |
|  | Toolchain-specific warning for allocations larger than a given size. |
| #define | [TOOLCHAIN\_WARNING\_DANGLING\_POINTER](#a41da25e145e8172cebcbbf31e0b79e17) |
|  | Toolchain-specific warning for dangling pointers. |
| #define | [TOOLCHAIN\_WARNING\_FORMAT\_TRUNCATION](#ad3a914654f83a6490de9a84d090af496) |
|  | Toolchain-specific warning for format truncation. |
| #define | [TOOLCHAIN\_WARNING\_INFINITE\_RECURSION](#a01fd2ae9418bafbedeaa4f3aeea9b3a3) |
|  | Toolchain-specific warning for infinite recursion. |
| #define | [TOOLCHAIN\_WARNING\_INTEGER\_OVERFLOW](#af1ec5706645d6b33ee0781b5e1127796) |
|  | Toolchain-specific warning for integer overflow. |
| #define | [TOOLCHAIN\_WARNING\_OVERFLOW](#a4c9cbe2de87a179f951f6d10d0d919fd) |
|  | Toolchain-specific warning for integer overflow. |
| #define | [TOOLCHAIN\_WARNING\_PRAGMAS](#a78adf404c8b66e41066126c0221bd334) |
|  | Toolchain-specific warning for unknown pragmas. |
| #define | [TOOLCHAIN\_WARNING\_SIZEOF\_ARRAY\_DECAY](#a056ed97bac0f04be423885dc21b9df00) |
|  | Toolchain-specific warning for sizeof array decay. |
| #define | [TOOLCHAIN\_WARNING\_STRINGOP\_OVERFLOW](#ac45e9e7740ee6c5e20e0ec813499dad5) |
|  | Toolchain-specific warning for stringop overflow. |
| #define | [TOOLCHAIN\_WARNING\_STRINGOP\_TRUNCATION](#a83c3c63db289d6024c809840492bce08) |
|  | Toolchain-specific warning for stringop truncation. |
| #define | [TOOLCHAIN\_WARNING\_UNUSED\_FUNCTION](#af90e0047b2708d02d3f69cd019a584df) |
|  | Toolchain-specific warning for unused function. |

## Macro Definition Documentation

## [◆ ](#a46a35ee1419f878aff6c4502a82fdad4)TOOLCHAIN\_WARNING\_ALLOC\_SIZE\_LARGER\_THAN

| #define TOOLCHAIN\_WARNING\_ALLOC\_SIZE\_LARGER\_THAN |
| --- |

Toolchain-specific warning for allocations larger than a given size.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a41da25e145e8172cebcbbf31e0b79e17)TOOLCHAIN\_WARNING\_DANGLING\_POINTER

| #define TOOLCHAIN\_WARNING\_DANGLING\_POINTER |
| --- |

Toolchain-specific warning for dangling pointers.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#ad3a914654f83a6490de9a84d090af496)TOOLCHAIN\_WARNING\_FORMAT\_TRUNCATION

| #define TOOLCHAIN\_WARNING\_FORMAT\_TRUNCATION |
| --- |

Toolchain-specific warning for format truncation.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a01fd2ae9418bafbedeaa4f3aeea9b3a3)TOOLCHAIN\_WARNING\_INFINITE\_RECURSION

| #define TOOLCHAIN\_WARNING\_INFINITE\_RECURSION |
| --- |

Toolchain-specific warning for infinite recursion.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#af1ec5706645d6b33ee0781b5e1127796)TOOLCHAIN\_WARNING\_INTEGER\_OVERFLOW

| #define TOOLCHAIN\_WARNING\_INTEGER\_OVERFLOW |
| --- |

Toolchain-specific warning for integer overflow.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a4c9cbe2de87a179f951f6d10d0d919fd)TOOLCHAIN\_WARNING\_OVERFLOW

| #define TOOLCHAIN\_WARNING\_OVERFLOW |
| --- |

Toolchain-specific warning for integer overflow.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a78adf404c8b66e41066126c0221bd334)TOOLCHAIN\_WARNING\_PRAGMAS

| #define TOOLCHAIN\_WARNING\_PRAGMAS |
| --- |

Toolchain-specific warning for unknown pragmas.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a056ed97bac0f04be423885dc21b9df00)TOOLCHAIN\_WARNING\_SIZEOF\_ARRAY\_DECAY

| #define TOOLCHAIN\_WARNING\_SIZEOF\_ARRAY\_DECAY |
| --- |

Toolchain-specific warning for sizeof array decay.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#ac45e9e7740ee6c5e20e0ec813499dad5)TOOLCHAIN\_WARNING\_STRINGOP\_OVERFLOW

| #define TOOLCHAIN\_WARNING\_STRINGOP\_OVERFLOW |
| --- |

Toolchain-specific warning for stringop overflow.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a83c3c63db289d6024c809840492bce08)TOOLCHAIN\_WARNING\_STRINGOP\_TRUNCATION

| #define TOOLCHAIN\_WARNING\_STRINGOP\_TRUNCATION |
| --- |

Toolchain-specific warning for stringop truncation.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#af90e0047b2708d02d3f69cd019a584df)TOOLCHAIN\_WARNING\_UNUSED\_FUNCTION

| #define TOOLCHAIN\_WARNING\_UNUSED\_FUNCTION |
| --- |

Toolchain-specific warning for unused function.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [test\_toolchain.h](test__toolchain_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
