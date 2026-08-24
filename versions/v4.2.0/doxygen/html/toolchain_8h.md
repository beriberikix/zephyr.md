---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/toolchain_8h.html
original_path: doxygen/html/toolchain_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

toolchain.h File Reference

Macros to abstract toolchain specific capabilities.
[More...](#details)

[Go to the source code of this file.](toolchain_8h_source.md)

| Macros | |
| --- | --- |
| #define | [HAS\_BUILTIN](#a474a719388efd0578c7c98a0961e23dd)(x) |
|  | Check if the compiler supports the built-in function *x*. |
| #define | [TOOLCHAIN\_GCC\_VERSION](#acbf8a21b471b2086cbe276789c5061d5)   0 |
|  | GCC version in xxyyzz for xx.yy.zz. |
| #define | [TOOLCHAIN\_CLANG\_VERSION](#acdbda8f5e81a320dfdbc32bda1b33fad)   0 |
|  | Clang version in xxyyzz for xx.yy.zz. |
| #define | [TOOLCHAIN\_HAS\_PRAGMA\_DIAG](#a763b60a74b3b8917b8a91614f1d443e4)   0 |
|  | Indicate if toolchain supports #pragma diagnostics. |
| #define | [TOOLCHAIN\_HAS\_C\_GENERIC](#a49263980cf39cd330a9e9976dccb4c90)   0 |
|  | Indicate if toolchain supports C Generic. |
| #define | [TOOLCHAIN\_HAS\_C\_AUTO\_TYPE](#a9502cad506e0dfb7c3a7b51b5eeb5eeb)   0 |
|  | Indicate if toolchain supports C \_\_auto\_type. |
| #define | [TOOLCHAIN\_HAS\_ZLA](#a90e5fd6ed234d1494c7f156635c2e6e1)   0 |
|  | Indicate if toolchain supports Zero Length Arrays. |
| #define | [TOOLCHAIN\_PRAGMA](#a4bd2473c4ecff861c6bc3e187b0fee12)(x) |
|  | Helper for using pragma in macros. |
| #define | [TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER](#aef9c3722dc2b189226eb2e6223c080bf) |
|  | Toolchain-specific warning for taking the address of a packed member. |
| #define | [TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS](#a8b81dbfdc3dde900a58540709a4f1dff) |
|  | Toolchain-specific warning for array bounds violations. |
| #define | [TOOLCHAIN\_WARNING\_ATTRIBUTES](#a5f5fef9bda4762c368f26c9028cdd34a) |
|  | Toolchain-specific warning for unknown attributes. |
| #define | [TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR](#a003b55bfd0a8b95a4e57e419eb980a39) |
|  | Toolchain-specific warning for deleting a pointer to an object with a non-virtual destructor. |
| #define | [TOOLCHAIN\_WARNING\_EXTRA](#a64d8f26c21ee3639e82d93783e09387e) |
|  | Toolchain-specific warning for extra warnings. |
| #define | [TOOLCHAIN\_WARNING\_NONNULL](#af990df9b277505b97d4c9c2549fffa9f) |
|  | Toolchain-specific warning for null pointer arguments to functions marked with "nonnull". |
| #define | [TOOLCHAIN\_WARNING\_POINTER\_ARITH](#a9c83552055a1817801dedc6655fc0cbf) |
|  | Toolchain-specific warning for pointer arithmetic. |
| #define | [TOOLCHAIN\_WARNING\_SHADOW](#ae917ae1adad468956fa5d28a50d10670) |
|  | Toolchain-specific warning for shadow variables. |
| #define | [TOOLCHAIN\_WARNING\_UNUSED\_LABEL](#a49dfbc1f801e1f3ae9a0dfaee4b1b5c9) |
|  | Toolchain-specific warning for unused labels. |
| #define | [TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE](#ac567335f987f8f89640e22bd8e3e9385) |
|  | Toolchain-specific warning for unused variables. |
| #define | [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5)(warning) |
|  | Disable the specified compiler warning for all compilers. |
| #define | [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561)(warning) |
|  | Re-enable the specified compiler warning for all compilers. |
| #define | [TOOLCHAIN\_DISABLE\_CLANG\_WARNING](#ac4bfe24556e3dd2bfb093434a4e98517)(warning) |
|  | Disable the specified compiler warning for clang. |
| #define | [TOOLCHAIN\_ENABLE\_CLANG\_WARNING](#a35eaaf7a69eae890687c196e81304667)(warning) |
|  | Re-enable the specified compiler warning for clang. |
| #define | [TOOLCHAIN\_DISABLE\_GCC\_WARNING](#a245aa1544cf704ac88da3904e0982f05)(warning) |
|  | Disable the specified compiler warning for gcc. |
| #define | [TOOLCHAIN\_ENABLE\_GCC\_WARNING](#a57a000da2786521299f7bc9460977c60)(warning) |
|  | Re-enable the specified compiler warning for gcc. |
| #define | [TOOLCHAIN\_DISABLE\_IAR\_WARNING](#aace39dc11f4da885c3a75210519cff13)(warning) |
|  | Disable the specified compiler warning for IAR compilers. |
| #define | [TOOLCHAIN\_ENABLE\_IAR\_WARNING](#a8a1fc59f2665be53c4e183d295d91e15)(warning) |
|  | Re-enable the specified compiler warning for IAR compilers. |

## Detailed Description

Macros to abstract toolchain specific capabilities.

This file contains various macros to abstract compiler capabilities that utilize toolchain specific attributes and/or pragmas.

## Macro Definition Documentation

## [◆ ](#a474a719388efd0578c7c98a0961e23dd)HAS\_BUILTIN

| #define HAS\_BUILTIN | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

HAS\_BUILTIN\_##x

Check if the compiler supports the built-in function *x*.

This macro is for use with conditional compilation to enable code using a builtin function that may not be available in every compiler.

## [◆ ](#acdbda8f5e81a320dfdbc32bda1b33fad)TOOLCHAIN\_CLANG\_VERSION

| #define TOOLCHAIN\_CLANG\_VERSION   0 |
| --- |

Clang version in xxyyzz for xx.yy.zz.

Zero if not Clang compatible.

## [◆ ](#ac4bfe24556e3dd2bfb093434a4e98517)TOOLCHAIN\_DISABLE\_CLANG\_WARNING

| #define TOOLCHAIN\_DISABLE\_CLANG\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable the specified compiler warning for clang.

## [◆ ](#a245aa1544cf704ac88da3904e0982f05)TOOLCHAIN\_DISABLE\_GCC\_WARNING

| #define TOOLCHAIN\_DISABLE\_GCC\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable the specified compiler warning for gcc.

## [◆ ](#aace39dc11f4da885c3a75210519cff13)TOOLCHAIN\_DISABLE\_IAR\_WARNING

| #define TOOLCHAIN\_DISABLE\_IAR\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable the specified compiler warning for IAR compilers.

## [◆ ](#a1f08471f8dba6ce2a3e0f38bea73d7b5)TOOLCHAIN\_DISABLE\_WARNING

| #define TOOLCHAIN\_DISABLE\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable the specified compiler warning for all compilers.

## [◆ ](#a35eaaf7a69eae890687c196e81304667)TOOLCHAIN\_ENABLE\_CLANG\_WARNING

| #define TOOLCHAIN\_ENABLE\_CLANG\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

Re-enable the specified compiler warning for clang.

Can only be used after a call to [TOOLCHAIN\_DISABLE\_CLANG\_WARNING](#ac4bfe24556e3dd2bfb093434a4e98517).

## [◆ ](#a57a000da2786521299f7bc9460977c60)TOOLCHAIN\_ENABLE\_GCC\_WARNING

| #define TOOLCHAIN\_ENABLE\_GCC\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

Re-enable the specified compiler warning for gcc.

Can only be used after a call to [TOOLCHAIN\_DISABLE\_GCC\_WARNING](#a245aa1544cf704ac88da3904e0982f05).

## [◆ ](#a8a1fc59f2665be53c4e183d295d91e15)TOOLCHAIN\_ENABLE\_IAR\_WARNING

| #define TOOLCHAIN\_ENABLE\_IAR\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

Re-enable the specified compiler warning for IAR compilers.

Can only be used after a call to [TOOLCHAIN\_DISABLE\_IAR\_WARNING](#aace39dc11f4da885c3a75210519cff13).

## [◆ ](#a5365fdbb6323f48ddca9ab4149e9a561)TOOLCHAIN\_ENABLE\_WARNING

| #define TOOLCHAIN\_ENABLE\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

Re-enable the specified compiler warning for all compilers.

Can only be used after a call to [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5).

## [◆ ](#acbf8a21b471b2086cbe276789c5061d5)TOOLCHAIN\_GCC\_VERSION

| #define TOOLCHAIN\_GCC\_VERSION   0 |
| --- |

GCC version in xxyyzz for xx.yy.zz.

Zero if not GCC compatible.

## [◆ ](#a9502cad506e0dfb7c3a7b51b5eeb5eeb)TOOLCHAIN\_HAS\_C\_AUTO\_TYPE

| #define TOOLCHAIN\_HAS\_C\_AUTO\_TYPE   0 |
| --- |

Indicate if toolchain supports C \_\_auto\_type.

## [◆ ](#a49263980cf39cd330a9e9976dccb4c90)TOOLCHAIN\_HAS\_C\_GENERIC

| #define TOOLCHAIN\_HAS\_C\_GENERIC   0 |
| --- |

Indicate if toolchain supports C Generic.

## [◆ ](#a763b60a74b3b8917b8a91614f1d443e4)TOOLCHAIN\_HAS\_PRAGMA\_DIAG

| #define TOOLCHAIN\_HAS\_PRAGMA\_DIAG   0 |
| --- |

Indicate if toolchain supports #pragma diagnostics.

## [◆ ](#a90e5fd6ed234d1494c7f156635c2e6e1)TOOLCHAIN\_HAS\_ZLA

| #define TOOLCHAIN\_HAS\_ZLA   0 |
| --- |

Indicate if toolchain supports Zero Length Arrays.

## [◆ ](#a4bd2473c4ecff861c6bc3e187b0fee12)TOOLCHAIN\_PRAGMA

| #define TOOLCHAIN\_PRAGMA | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_Pragma(#x)

Helper for using pragma in macros.

## [◆ ](#aef9c3722dc2b189226eb2e6223c080bf)TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER

| #define TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER |
| --- |

Toolchain-specific warning for taking the address of a packed member.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5) and [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561) family of macros.

## [◆ ](#a8b81dbfdc3dde900a58540709a4f1dff)TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS

| #define TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS |
| --- |

Toolchain-specific warning for array bounds violations.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5) and [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561) family of macros.

## [◆ ](#a5f5fef9bda4762c368f26c9028cdd34a)TOOLCHAIN\_WARNING\_ATTRIBUTES

| #define TOOLCHAIN\_WARNING\_ATTRIBUTES |
| --- |

Toolchain-specific warning for unknown attributes.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5) and [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561) family of macros.

## [◆ ](#a003b55bfd0a8b95a4e57e419eb980a39)TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR

| #define TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR |
| --- |

Toolchain-specific warning for deleting a pointer to an object with a non-virtual destructor.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5) and [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561) family of macros.

## [◆ ](#a64d8f26c21ee3639e82d93783e09387e)TOOLCHAIN\_WARNING\_EXTRA

| #define TOOLCHAIN\_WARNING\_EXTRA |
| --- |

Toolchain-specific warning for extra warnings.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5) and [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561) family of macros.

## [◆ ](#af990df9b277505b97d4c9c2549fffa9f)TOOLCHAIN\_WARNING\_NONNULL

| #define TOOLCHAIN\_WARNING\_NONNULL |
| --- |

Toolchain-specific warning for null pointer arguments to functions marked with "nonnull".

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5) and [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561) family of macros.

## [◆ ](#a9c83552055a1817801dedc6655fc0cbf)TOOLCHAIN\_WARNING\_POINTER\_ARITH

| #define TOOLCHAIN\_WARNING\_POINTER\_ARITH |
| --- |

Toolchain-specific warning for pointer arithmetic.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5) and [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561) family of macros.

## [◆ ](#ae917ae1adad468956fa5d28a50d10670)TOOLCHAIN\_WARNING\_SHADOW

| #define TOOLCHAIN\_WARNING\_SHADOW |
| --- |

Toolchain-specific warning for shadow variables.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5) and [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561) family of macros.

## [◆ ](#a49dfbc1f801e1f3ae9a0dfaee4b1b5c9)TOOLCHAIN\_WARNING\_UNUSED\_LABEL

| #define TOOLCHAIN\_WARNING\_UNUSED\_LABEL |
| --- |

Toolchain-specific warning for unused labels.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5) and [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561) family of macros.

## [◆ ](#ac567335f987f8f89640e22bd8e3e9385)TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE

| #define TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE |
| --- |

Toolchain-specific warning for unused variables.

Use this as an argument to the [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5) and [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561) family of macros.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain.h](toolchain_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
