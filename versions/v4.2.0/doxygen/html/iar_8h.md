---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/iar_8h.html
original_path: doxygen/html/iar_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iar.h File Reference

[Go to the source code of this file.](iar_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TOOLCHAIN\_HAS\_PRAGMA\_DIAG](#a763b60a74b3b8917b8a91614f1d443e4) |
| #define | [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5)(warning) |
| #define | [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561)(warning) |
| #define | [TOOLCHAIN\_DISABLE\_IAR\_WARNING](#aace39dc11f4da885c3a75210519cff13)(warning) |
| #define | [TOOLCHAIN\_ENABLE\_IAR\_WARNING](#a8a1fc59f2665be53c4e183d295d91e15)(warning) |
| #define | [TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER](#aef9c3722dc2b189226eb2e6223c080bf)   Pa039 |
|  | Toolchain-specific warning for taking the address of a packed member. |
| #define | [TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS](#a8b81dbfdc3dde900a58540709a4f1dff)   Pe001 |
|  | Toolchain-specific warning for array bounds violations. |
| #define | [TOOLCHAIN\_WARNING\_ATTRIBUTES](#a5f5fef9bda4762c368f26c9028cdd34a)   Pe1097 |
|  | Toolchain-specific warning for unknown attributes. |
| #define | [TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR](#a003b55bfd0a8b95a4e57e419eb980a39)   Pe001 |
|  | Toolchain-specific warning for deleting a pointer to an object with a non-virtual destructor. |
| #define | [TOOLCHAIN\_WARNING\_EXTRA](#a64d8f26c21ee3639e82d93783e09387e)   Pe001 |
|  | Toolchain-specific warning for extra warnings. |
| #define | [TOOLCHAIN\_WARNING\_NONNULL](#af990df9b277505b97d4c9c2549fffa9f)   Pe001 |
|  | Toolchain-specific warning for null pointer arguments to functions marked with "nonnull". |
| #define | [TOOLCHAIN\_WARNING\_POINTER\_ARITH](#a9c83552055a1817801dedc6655fc0cbf)   Pe1143 |
|  | Toolchain-specific warning for pointer arithmetic. |
| #define | [TOOLCHAIN\_WARNING\_SHADOW](#ae917ae1adad468956fa5d28a50d10670)   Pe001 |
|  | Toolchain-specific warning for shadow variables. |
| #define | [TOOLCHAIN\_WARNING\_UNUSED\_LABEL](#a49dfbc1f801e1f3ae9a0dfaee4b1b5c9)   Pe001 |
|  | Toolchain-specific warning for unused labels. |
| #define | [TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE](#ac567335f987f8f89640e22bd8e3e9385)   Pe001 |
|  | Toolchain-specific warning for unused variables. |
| #define | [TOOLCHAIN\_WARNING\_UNUSED\_FUNCTION](#af90e0047b2708d02d3f69cd019a584df)   Pe001 |

## Macro Definition Documentation

## [◆ ](#aace39dc11f4da885c3a75210519cff13)TOOLCHAIN\_DISABLE\_IAR\_WARNING

| #define TOOLCHAIN\_DISABLE\_IAR\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_TOOLCHAIN\_DISABLE\_WARNING(warning)

## [◆ ](#a1f08471f8dba6ce2a3e0f38bea73d7b5)TOOLCHAIN\_DISABLE\_WARNING

| #define TOOLCHAIN\_DISABLE\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_TOOLCHAIN\_DISABLE\_WARNING(warning)

## [◆ ](#a8a1fc59f2665be53c4e183d295d91e15)TOOLCHAIN\_ENABLE\_IAR\_WARNING

| #define TOOLCHAIN\_ENABLE\_IAR\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_TOOLCHAIN\_ENABLE\_WARNING(warning)

## [◆ ](#a5365fdbb6323f48ddca9ab4149e9a561)TOOLCHAIN\_ENABLE\_WARNING

| #define TOOLCHAIN\_ENABLE\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_TOOLCHAIN\_ENABLE\_WARNING(warning)

## [◆ ](#a763b60a74b3b8917b8a91614f1d443e4)TOOLCHAIN\_HAS\_PRAGMA\_DIAG

| #define TOOLCHAIN\_HAS\_PRAGMA\_DIAG |
| --- |

## [◆ ](#aef9c3722dc2b189226eb2e6223c080bf)TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER

| #define TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER   Pa039 |
| --- |

Toolchain-specific warning for taking the address of a packed member.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a8b81dbfdc3dde900a58540709a4f1dff)TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS

| #define TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS   Pe001 |
| --- |

Toolchain-specific warning for array bounds violations.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a5f5fef9bda4762c368f26c9028cdd34a)TOOLCHAIN\_WARNING\_ATTRIBUTES

| #define TOOLCHAIN\_WARNING\_ATTRIBUTES   Pe1097 |
| --- |

Toolchain-specific warning for unknown attributes.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a003b55bfd0a8b95a4e57e419eb980a39)TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR

| #define TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR   Pe001 |
| --- |

Toolchain-specific warning for deleting a pointer to an object with a non-virtual destructor.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a64d8f26c21ee3639e82d93783e09387e)TOOLCHAIN\_WARNING\_EXTRA

| #define TOOLCHAIN\_WARNING\_EXTRA   Pe001 |
| --- |

Toolchain-specific warning for extra warnings.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#af990df9b277505b97d4c9c2549fffa9f)TOOLCHAIN\_WARNING\_NONNULL

| #define TOOLCHAIN\_WARNING\_NONNULL   Pe001 |
| --- |

Toolchain-specific warning for null pointer arguments to functions marked with "nonnull".

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#a9c83552055a1817801dedc6655fc0cbf)TOOLCHAIN\_WARNING\_POINTER\_ARITH

| #define TOOLCHAIN\_WARNING\_POINTER\_ARITH   Pe1143 |
| --- |

Toolchain-specific warning for pointer arithmetic.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#ae917ae1adad468956fa5d28a50d10670)TOOLCHAIN\_WARNING\_SHADOW

| #define TOOLCHAIN\_WARNING\_SHADOW   Pe001 |
| --- |

Toolchain-specific warning for shadow variables.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#af90e0047b2708d02d3f69cd019a584df)TOOLCHAIN\_WARNING\_UNUSED\_FUNCTION

| #define TOOLCHAIN\_WARNING\_UNUSED\_FUNCTION   Pe001 |
| --- |

## [◆ ](#a49dfbc1f801e1f3ae9a0dfaee4b1b5c9)TOOLCHAIN\_WARNING\_UNUSED\_LABEL

| #define TOOLCHAIN\_WARNING\_UNUSED\_LABEL   Pe001 |
| --- |

Toolchain-specific warning for unused labels.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

## [◆ ](#ac567335f987f8f89640e22bd8e3e9385)TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE

| #define TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE   Pe001 |
| --- |

Toolchain-specific warning for unused variables.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5 "TOOLCHAIN_DISABLE_WARNING") and [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561 "TOOLCHAIN_ENABLE_WARNING") family of macros.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [iar.h](iar_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
