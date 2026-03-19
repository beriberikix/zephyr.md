---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arch-arm_8h.html
original_path: doxygen/html/arch-arm_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch-arm.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](arch-arm_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arch\_vcpu\_info](structarch__vcpu__info.md) |
| struct | [arch\_shared\_info](structarch__shared__info.md) |
| struct | [xen\_pmu\_arch](structxen__pmu__arch.md) |

| Macros | |
| --- | --- |
| #define | [XEN\_HYPERCALL\_TAG](#aa5e158f6f21dcc54391239d9ac71f32b)   0XEA1 |
| #define | [int64\_aligned\_t](#a8e346fda4301d9806f5b97d796af4d0c)   [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \_\_aligned(8) |
| #define | [uint64\_aligned\_t](#ac94f3cee60964f8609932e5042590128)   [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \_\_aligned(8) |
| #define | [DEFINE\_XEN\_GUEST\_HANDLE](#ae74e9f15fb9a0b53b9d10a529b84e121)(name) |
| #define | [XEN\_GUEST\_HANDLE](#a59eac5b471e486c9cdb4743017fdfc20)(name) |
| #define | [XEN\_GUEST\_HANDLE\_PARAM](#a2d269ec4cb445d086e8fca4d4288f7ce)(name) |
| #define | [set\_xen\_guest\_handle\_raw](#a3d4d2c27792e69e7f925e2a4e3390091)(hnd, val) |
| #define | [set\_xen\_guest\_handle](#a393eef7cbafc7f0e2d64ba971e0c8079)(hnd, val) |
| #define | [PRI\_xen\_pfn](#a4a9cdcf7a527951f75cf8b8c2b6eb828)   [PRIx64](inttypes_8h.md#aba38357387a474f439428dee1984fc5a) |
| #define | [PRIu\_xen\_pfn](#acc5c5e4cd20a58ea2246de620bed79fe)   [PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) |
| #define | [XEN\_LEGACY\_MAX\_VCPUS](#a57246b966cc182f34ca4f9bfa101e449)   1 |
| #define | [PRI\_xen\_ulong](#ae5fed872d1684ca8fb200bd02927766c)   [PRIx64](inttypes_8h.md#aba38357387a474f439428dee1984fc5a) |

| Typedefs | |
| --- | --- |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [xen\_pfn\_t](#a564b8052e6905461f66db791246d2226) |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [xen\_ulong\_t](#a9dd3dbb4741d391e0fff3f0e7d55cccc) |
| typedef struct [arch\_vcpu\_info](structarch__vcpu__info.md) | [arch\_vcpu\_info\_t](#a396e630cfa073f7d4e9e983c43c7f7e3) |
| typedef struct [arch\_shared\_info](structarch__shared__info.md) | [arch\_shared\_info\_t](#a7b797b4c17d2f2ec9fdf06f5dc69d016) |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [xen\_callback\_t](#a85d47e7eb51075f257e76067ef337526) |
| typedef struct [xen\_pmu\_arch](structxen__pmu__arch.md) | [xen\_pmu\_arch\_t](#a9d6716569cd8ef7c541527df22dd767c) |

## Macro Definition Documentation

## [◆ ](#ae74e9f15fb9a0b53b9d10a529b84e121)DEFINE\_XEN\_GUEST\_HANDLE

| #define DEFINE\_XEN\_GUEST\_HANDLE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_DEFINE\_XEN\_GUEST\_HANDLE(name, name)

## [◆ ](#a8e346fda4301d9806f5b97d796af4d0c)int64\_aligned\_t

| #define int64\_aligned\_t   [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \_\_aligned(8) |
| --- |

## [◆ ](#a4a9cdcf7a527951f75cf8b8c2b6eb828)PRI\_xen\_pfn

| #define PRI\_xen\_pfn   [PRIx64](inttypes_8h.md#aba38357387a474f439428dee1984fc5a) |
| --- |

## [◆ ](#ae5fed872d1684ca8fb200bd02927766c)PRI\_xen\_ulong

| #define PRI\_xen\_ulong   [PRIx64](inttypes_8h.md#aba38357387a474f439428dee1984fc5a) |
| --- |

## [◆ ](#acc5c5e4cd20a58ea2246de620bed79fe)PRIu\_xen\_pfn

| #define PRIu\_xen\_pfn   [PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) |
| --- |

## [◆ ](#a393eef7cbafc7f0e2d64ba971e0c8079)set\_xen\_guest\_handle

| #define set\_xen\_guest\_handle | ( |  | *hnd*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

[set\_xen\_guest\_handle\_raw](#a3d4d2c27792e69e7f925e2a4e3390091)(hnd, val)

[set\_xen\_guest\_handle\_raw](#a3d4d2c27792e69e7f925e2a4e3390091)

#define set\_xen\_guest\_handle\_raw(hnd, val)

**Definition** arch-arm.h:196

## [◆ ](#a3d4d2c27792e69e7f925e2a4e3390091)set\_xen\_guest\_handle\_raw

| #define set\_xen\_guest\_handle\_raw | ( |  | *hnd*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

do { \

\_\_typeof\_\_(&(hnd)) \_sxghr\_tmp = &(hnd); \

\_sxghr\_tmp->q = 0; \

\_sxghr\_tmp->p = val; \

} while (0)

## [◆ ](#ac94f3cee60964f8609932e5042590128)uint64\_aligned\_t

| #define uint64\_aligned\_t   [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \_\_aligned(8) |
| --- |

## [◆ ](#a59eac5b471e486c9cdb4743017fdfc20)XEN\_GUEST\_HANDLE

| #define XEN\_GUEST\_HANDLE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_XEN\_GUEST\_HANDLE(name)

## [◆ ](#a2d269ec4cb445d086e8fca4d4288f7ce)XEN\_GUEST\_HANDLE\_PARAM

| #define XEN\_GUEST\_HANDLE\_PARAM | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_guest\_handle\_ ## name

## [◆ ](#aa5e158f6f21dcc54391239d9ac71f32b)XEN\_HYPERCALL\_TAG

| #define XEN\_HYPERCALL\_TAG   0XEA1 |
| --- |

## [◆ ](#a57246b966cc182f34ca4f9bfa101e449)XEN\_LEGACY\_MAX\_VCPUS

| #define XEN\_LEGACY\_MAX\_VCPUS   1 |
| --- |

## Typedef Documentation

## [◆ ](#a7b797b4c17d2f2ec9fdf06f5dc69d016)arch\_shared\_info\_t

| typedef struct [arch\_shared\_info](structarch__shared__info.md) [arch\_shared\_info\_t](#a7b797b4c17d2f2ec9fdf06f5dc69d016) |
| --- |

## [◆ ](#a396e630cfa073f7d4e9e983c43c7f7e3)arch\_vcpu\_info\_t

| typedef struct [arch\_vcpu\_info](structarch__vcpu__info.md) [arch\_vcpu\_info\_t](#a396e630cfa073f7d4e9e983c43c7f7e3) |
| --- |

## [◆ ](#a85d47e7eb51075f257e76067ef337526)xen\_callback\_t

| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [xen\_callback\_t](#a85d47e7eb51075f257e76067ef337526) |
| --- |

## [◆ ](#a564b8052e6905461f66db791246d2226)xen\_pfn\_t

| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [xen\_pfn\_t](#a564b8052e6905461f66db791246d2226) |
| --- |

## [◆ ](#a9d6716569cd8ef7c541527df22dd767c)xen\_pmu\_arch\_t

| typedef struct [xen\_pmu\_arch](structxen__pmu__arch.md) [xen\_pmu\_arch\_t](#a9d6716569cd8ef7c541527df22dd767c) |
| --- |

## [◆ ](#a9dd3dbb4741d391e0fff3f0e7d55cccc)xen\_ulong\_t

| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [xen\_ulong\_t](#a9dd3dbb4741d391e0fff3f0e7d55cccc) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [arch-arm.h](arch-arm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
