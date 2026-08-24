---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/include_2zephyr_2toolchain_2gcc_8h.html
original_path: doxygen/html/include_2zephyr_2toolchain_2gcc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gcc.h File Reference

GCC toolchain abstraction.
[More...](#details)

[Go to the source code of this file.](include_2zephyr_2toolchain_2gcc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TOOLCHAIN\_GCC\_VERSION](#acbf8a21b471b2086cbe276789c5061d5)   ((\_\_GNUC\_\_ \* 10000) + (\_\_GNUC\_MINOR\_\_ \* 100) + \_\_GNUC\_PATCHLEVEL\_\_) |
| #define | [TOOLCHAIN\_HAS\_ZLA](#a90e5fd6ed234d1494c7f156635c2e6e1)   1 |
| #define | [TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER](#aef9c3722dc2b189226eb2e6223c080bf)   "-Waddress-of-packed-member" |
| #define | [TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS](#a8b81dbfdc3dde900a58540709a4f1dff)   "-Warray-bounds" |
| #define | [TOOLCHAIN\_WARNING\_ATTRIBUTES](#a5f5fef9bda4762c368f26c9028cdd34a)   "-Wattributes" |
| #define | [TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR](#a003b55bfd0a8b95a4e57e419eb980a39)   "-Wdelete-non-virtual-dtor" |
| #define | [TOOLCHAIN\_WARNING\_EXTRA](#a64d8f26c21ee3639e82d93783e09387e)   "-Wextra" |
| #define | [TOOLCHAIN\_WARNING\_NONNULL](#af990df9b277505b97d4c9c2549fffa9f)   "-Wnonnull" |
| #define | [TOOLCHAIN\_WARNING\_SHADOW](#ae917ae1adad468956fa5d28a50d10670)   "-Wshadow" |
| #define | [TOOLCHAIN\_WARNING\_UNUSED\_LABEL](#a49dfbc1f801e1f3ae9a0dfaee4b1b5c9)   "-Wunused-label" |
| #define | [TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE](#ac567335f987f8f89640e22bd8e3e9385)   "-Wunused-variable" |
| #define | [TOOLCHAIN\_DISABLE\_WARNING](#a1f08471f8dba6ce2a3e0f38bea73d7b5)(warning) |
| #define | [TOOLCHAIN\_ENABLE\_WARNING](#a5365fdbb6323f48ddca9ab4149e9a561)(warning) |

## Detailed Description

GCC toolchain abstraction.

Macros to abstract compiler capabilities for GCC toolchain.

## Macro Definition Documentation

## [◆ ](#a1f08471f8dba6ce2a3e0f38bea73d7b5)TOOLCHAIN\_DISABLE\_WARNING

| #define TOOLCHAIN\_DISABLE\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_TOOLCHAIN\_DISABLE\_WARNING(GCC, warning)

## [◆ ](#a5365fdbb6323f48ddca9ab4149e9a561)TOOLCHAIN\_ENABLE\_WARNING

| #define TOOLCHAIN\_ENABLE\_WARNING | ( |  | *warning* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_TOOLCHAIN\_ENABLE\_WARNING(GCC, warning)

## [◆ ](#acbf8a21b471b2086cbe276789c5061d5)TOOLCHAIN\_GCC\_VERSION

| #define TOOLCHAIN\_GCC\_VERSION   ((\_\_GNUC\_\_ \* 10000) + (\_\_GNUC\_MINOR\_\_ \* 100) + \_\_GNUC\_PATCHLEVEL\_\_) |
| --- |

## [◆ ](#a90e5fd6ed234d1494c7f156635c2e6e1)TOOLCHAIN\_HAS\_ZLA

| #define TOOLCHAIN\_HAS\_ZLA   1 |
| --- |

## [◆ ](#aef9c3722dc2b189226eb2e6223c080bf)TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER

| #define TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER   "-Waddress-of-packed-member" |
| --- |

## [◆ ](#a8b81dbfdc3dde900a58540709a4f1dff)TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS

| #define TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS   "-Warray-bounds" |
| --- |

## [◆ ](#a5f5fef9bda4762c368f26c9028cdd34a)TOOLCHAIN\_WARNING\_ATTRIBUTES

| #define TOOLCHAIN\_WARNING\_ATTRIBUTES   "-Wattributes" |
| --- |

## [◆ ](#a003b55bfd0a8b95a4e57e419eb980a39)TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR

| #define TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR   "-Wdelete-non-virtual-dtor" |
| --- |

## [◆ ](#a64d8f26c21ee3639e82d93783e09387e)TOOLCHAIN\_WARNING\_EXTRA

| #define TOOLCHAIN\_WARNING\_EXTRA   "-Wextra" |
| --- |

## [◆ ](#af990df9b277505b97d4c9c2549fffa9f)TOOLCHAIN\_WARNING\_NONNULL

| #define TOOLCHAIN\_WARNING\_NONNULL   "-Wnonnull" |
| --- |

## [◆ ](#ae917ae1adad468956fa5d28a50d10670)TOOLCHAIN\_WARNING\_SHADOW

| #define TOOLCHAIN\_WARNING\_SHADOW   "-Wshadow" |
| --- |

## [◆ ](#a49dfbc1f801e1f3ae9a0dfaee4b1b5c9)TOOLCHAIN\_WARNING\_UNUSED\_LABEL

| #define TOOLCHAIN\_WARNING\_UNUSED\_LABEL   "-Wunused-label" |
| --- |

## [◆ ](#ac567335f987f8f89640e22bd8e3e9385)TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE

| #define TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE   "-Wunused-variable" |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [gcc.h](include_2zephyr_2toolchain_2gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
