---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/public_2memory_8h.html
original_path: doxygen/html/public_2memory_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory.h File Reference

`#include "[xen.h](xen_8h_source.md)"`

[Go to the source code of this file.](public_2memory_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [xen\_memory\_reservation](structxen__memory__reservation.md) |
| struct | [xen\_add\_to\_physmap\_batch](structxen__add__to__physmap__batch.md) |
| struct | [xen\_add\_to\_physmap](structxen__add__to__physmap.md) |
| struct | [xen\_remove\_from\_physmap](structxen__remove__from__physmap.md) |

| Macros | |
| --- | --- |
| #define | [XENMEM\_populate\_physmap](#a6ec885dfced1bae6da54202b3d63ecaf)   6 |
| #define | [XENMEM\_add\_to\_physmap\_batch](#a7d95089177a14df927c60432925acbfa)   23 |
| #define | [XENMAPSPACE\_shared\_info](#a4369cb99e8d27ca45dc163373d103309)   0 /\* shared info page \*/ |
| #define | [XENMAPSPACE\_grant\_table](#ad115b9759532e6d0358cc704409c6270)   1 /\* grant table page \*/ |
| #define | [XENMAPSPACE\_gmfn](#a5675ec2efeed7e5c40dda7483b10d569)   2 /\* GMFN \*/ |
| #define | [XENMAPSPACE\_gmfn\_range](#a2c34663ef8ef5bd369e2d73520649e50)   3 |
| #define | [XENMAPSPACE\_gmfn\_foreign](#a565fab9b43c0a1be2866b9aa934841ba)   4 |
| #define | [XENMAPSPACE\_dev\_mmio](#acb4d47c69fee4afe3c722cb6ee8d61b6)   5 |
| #define | [XENMEM\_add\_to\_physmap](#a1475409f6e69603d9797b94efc148b4d)   7 |
| #define | [XENMAPIDX\_grant\_table\_status](#a203b04fe93d4686b1c12337bc3973747)   0x80000000 |
| #define | [XENMEM\_remove\_from\_physmap](#a684c3081ab104b422ea40c68fc421c1c)   15 |

| Typedefs | |
| --- | --- |
| typedef struct [xen\_memory\_reservation](structxen__memory__reservation.md) | [xen\_memory\_reservation\_t](#a2328386982b62de8d81d891e257cab9b) |
| typedef struct [xen\_add\_to\_physmap\_batch](structxen__add__to__physmap__batch.md) | [xen\_add\_to\_physmap\_batch\_t](#a7d0453db07f6593afa9ea5657ddf8815) |
| typedef struct [xen\_add\_to\_physmap](structxen__add__to__physmap.md) | [xen\_add\_to\_physmap\_t](#afe3890ecc3ae521c121d3bcdf1e4b39b) |
| typedef struct [xen\_remove\_from\_physmap](structxen__remove__from__physmap.md) | [xen\_remove\_from\_physmap\_t](#a7ac5899f2de1e9d6d775142c9ee4616b) |

| Functions | |
| --- | --- |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#acc691af99a28d99e4f6101403dfda8fc) ([xen\_memory\_reservation\_t](#a2328386982b62de8d81d891e257cab9b)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a527825096ff8c47a16a6e911cc7c6cd4) ([xen\_add\_to\_physmap\_batch\_t](#a7d0453db07f6593afa9ea5657ddf8815)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a2fcb0b67b88e3de8a1dd66d5eeaa7df5) ([xen\_add\_to\_physmap\_t](#afe3890ecc3ae521c121d3bcdf1e4b39b)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a96fd5cc1e36746fa9ad613912d519f4b) ([xen\_remove\_from\_physmap\_t](#a7ac5899f2de1e9d6d775142c9ee4616b)) |

## Macro Definition Documentation

## [◆ ](#a203b04fe93d4686b1c12337bc3973747)XENMAPIDX\_grant\_table\_status

| #define XENMAPIDX\_grant\_table\_status   0x80000000 |
| --- |

## [◆ ](#acb4d47c69fee4afe3c722cb6ee8d61b6)XENMAPSPACE\_dev\_mmio

| #define XENMAPSPACE\_dev\_mmio   5 |
| --- |

## [◆ ](#a5675ec2efeed7e5c40dda7483b10d569)XENMAPSPACE\_gmfn

| #define XENMAPSPACE\_gmfn   2 /\* GMFN \*/ |
| --- |

## [◆ ](#a565fab9b43c0a1be2866b9aa934841ba)XENMAPSPACE\_gmfn\_foreign

| #define XENMAPSPACE\_gmfn\_foreign   4 |
| --- |

## [◆ ](#a2c34663ef8ef5bd369e2d73520649e50)XENMAPSPACE\_gmfn\_range

| #define XENMAPSPACE\_gmfn\_range   3 |
| --- |

## [◆ ](#ad115b9759532e6d0358cc704409c6270)XENMAPSPACE\_grant\_table

| #define XENMAPSPACE\_grant\_table   1 /\* grant table page \*/ |
| --- |

## [◆ ](#a4369cb99e8d27ca45dc163373d103309)XENMAPSPACE\_shared\_info

| #define XENMAPSPACE\_shared\_info   0 /\* shared info page \*/ |
| --- |

## [◆ ](#a1475409f6e69603d9797b94efc148b4d)XENMEM\_add\_to\_physmap

| #define XENMEM\_add\_to\_physmap   7 |
| --- |

## [◆ ](#a7d95089177a14df927c60432925acbfa)XENMEM\_add\_to\_physmap\_batch

| #define XENMEM\_add\_to\_physmap\_batch   23 |
| --- |

## [◆ ](#a6ec885dfced1bae6da54202b3d63ecaf)XENMEM\_populate\_physmap

| #define XENMEM\_populate\_physmap   6 |
| --- |

## [◆ ](#a684c3081ab104b422ea40c68fc421c1c)XENMEM\_remove\_from\_physmap

| #define XENMEM\_remove\_from\_physmap   15 |
| --- |

## Typedef Documentation

## [◆ ](#a7d0453db07f6593afa9ea5657ddf8815)xen\_add\_to\_physmap\_batch\_t

| typedef struct [xen\_add\_to\_physmap\_batch](structxen__add__to__physmap__batch.md) [xen\_add\_to\_physmap\_batch\_t](#a7d0453db07f6593afa9ea5657ddf8815) |
| --- |

## [◆ ](#afe3890ecc3ae521c121d3bcdf1e4b39b)xen\_add\_to\_physmap\_t

| typedef struct [xen\_add\_to\_physmap](structxen__add__to__physmap.md) [xen\_add\_to\_physmap\_t](#afe3890ecc3ae521c121d3bcdf1e4b39b) |
| --- |

## [◆ ](#a2328386982b62de8d81d891e257cab9b)xen\_memory\_reservation\_t

| typedef struct [xen\_memory\_reservation](structxen__memory__reservation.md) [xen\_memory\_reservation\_t](#a2328386982b62de8d81d891e257cab9b) |
| --- |

## [◆ ](#a7ac5899f2de1e9d6d775142c9ee4616b)xen\_remove\_from\_physmap\_t

| typedef struct [xen\_remove\_from\_physmap](structxen__remove__from__physmap.md) [xen\_remove\_from\_physmap\_t](#a7ac5899f2de1e9d6d775142c9ee4616b) |
| --- |

## Function Documentation

## [◆ ](#a527825096ff8c47a16a6e911cc7c6cd4)DEFINE\_XEN\_GUEST\_HANDLE() [1/4]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [xen\_add\_to\_physmap\_batch\_t](#a7d0453db07f6593afa9ea5657ddf8815) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a2fcb0b67b88e3de8a1dd66d5eeaa7df5)DEFINE\_XEN\_GUEST\_HANDLE() [2/4]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [xen\_add\_to\_physmap\_t](#afe3890ecc3ae521c121d3bcdf1e4b39b) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#acc691af99a28d99e4f6101403dfda8fc)DEFINE\_XEN\_GUEST\_HANDLE() [3/4]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [xen\_memory\_reservation\_t](#a2328386982b62de8d81d891e257cab9b) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a96fd5cc1e36746fa9ad613912d519f4b)DEFINE\_XEN\_GUEST\_HANDLE() [4/4]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [xen\_remove\_from\_physmap\_t](#a7ac5899f2de1e9d6d775142c9ee4616b) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [memory.h](public_2memory_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
