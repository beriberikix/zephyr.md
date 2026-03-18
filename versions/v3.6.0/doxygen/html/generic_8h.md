---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/generic_8h.html
original_path: doxygen/html/generic_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

generic.h File Reference

`#include <[zephyr/xen/public/xen.h](xen_8h_source.md)>`

[Go to the source code of this file.](generic_8h_source.md)

| Macros | |
| --- | --- |
| #define | [XEN\_PAGE\_SIZE](#ab22c00daf7a13fcd6f71fd389fad3919)   4096 |
| #define | [XEN\_PAGE\_SHIFT](#acbc96e1185d1c2fab047d87da44c0308)   12 |
| #define | [XEN\_PFN\_UP](#a87e8ebaed995d91a2fd87f34e3a37843)(x) |
| #define | [XEN\_PFN\_DOWN](#a8d089e7267f000ef6ce2cf98939d0df2)(x) |
| #define | [XEN\_PFN\_PHYS](#a0a87f9a4f97c5d40e583285fb97f97a0)(x) |
| #define | [XEN\_PHYS\_PFN](#afffd6c194994740f2ad3f49dac48c6d3)(x) |
| #define | [xen\_to\_phys](#a171a7e1bdc51851bf22c6f33d99a66d5)(x) |
| #define | [xen\_to\_virt](#a00320c3072ff8655017aa8e28367e864)(x) |
| #define | [xen\_virt\_to\_gfn](#aea05f25a15fca2bf161790935426e406)(\_virt) |
| #define | [xen\_gfn\_to\_virt](#ac5ffaa30256542b5e2ee53e5bf66dced)(\_gfn) |
| #define | [synch\_cmpxchg](#a8b4a100e92b54856a2a46c9362c595f7)(ptr, old, new) |

## Macro Definition Documentation

## [◆ ](#a8b4a100e92b54856a2a46c9362c595f7)synch\_cmpxchg

| #define synch\_cmpxchg | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *old*, |
|  |  |  | *new* ) |

**Value:**

({ \_\_typeof\_\_(\*ptr) stored = old; \

\_\_atomic\_compare\_exchange\_n(ptr, &stored, new, 0, \_\_ATOMIC\_SEQ\_CST, \

\_\_ATOMIC\_SEQ\_CST) ? new : old; \

})

## [◆ ](#ac5ffaa30256542b5e2ee53e5bf66dced)xen\_gfn\_to\_virt

| #define xen\_gfn\_to\_virt | ( |  | *\_gfn* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([xen\_to\_virt](#a00320c3072ff8655017aa8e28367e864)([XEN\_PFN\_PHYS](#a0a87f9a4f97c5d40e583285fb97f97a0)(\_gfn)))

[xen\_to\_virt](#a00320c3072ff8655017aa8e28367e864)

#define xen\_to\_virt(x)

**Definition** generic.h:20

[XEN\_PFN\_PHYS](#a0a87f9a4f97c5d40e583285fb97f97a0)

#define XEN\_PFN\_PHYS(x)

**Definition** generic.h:16

## [◆ ](#acbc96e1185d1c2fab047d87da44c0308)XEN\_PAGE\_SHIFT

| #define XEN\_PAGE\_SHIFT   12 |
| --- |

## [◆ ](#ab22c00daf7a13fcd6f71fd389fad3919)XEN\_PAGE\_SIZE

| #define XEN\_PAGE\_SIZE   4096 |
| --- |

## [◆ ](#a8d089e7267f000ef6ce2cf98939d0df2)XEN\_PFN\_DOWN

| #define XEN\_PFN\_DOWN | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(unsigned long)((x) >> [XEN\_PAGE\_SHIFT](#acbc96e1185d1c2fab047d87da44c0308))

[XEN\_PAGE\_SHIFT](#acbc96e1185d1c2fab047d87da44c0308)

#define XEN\_PAGE\_SHIFT

**Definition** generic.h:12

## [◆ ](#a0a87f9a4f97c5d40e583285fb97f97a0)XEN\_PFN\_PHYS

| #define XEN\_PFN\_PHYS | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((unsigned long)(x) << [XEN\_PAGE\_SHIFT](#acbc96e1185d1c2fab047d87da44c0308))

## [◆ ](#a87e8ebaed995d91a2fd87f34e3a37843)XEN\_PFN\_UP

| #define XEN\_PFN\_UP | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(unsigned long)(((x) + [XEN\_PAGE\_SIZE](#ab22c00daf7a13fcd6f71fd389fad3919)-1) >> [XEN\_PAGE\_SHIFT](#acbc96e1185d1c2fab047d87da44c0308))

[XEN\_PAGE\_SIZE](#ab22c00daf7a13fcd6f71fd389fad3919)

#define XEN\_PAGE\_SIZE

**Definition** generic.h:11

## [◆ ](#afffd6c194994740f2ad3f49dac48c6d3)XEN\_PHYS\_PFN

| #define XEN\_PHYS\_PFN | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(unsigned long)((x) >> [XEN\_PAGE\_SHIFT](#acbc96e1185d1c2fab047d87da44c0308))

## [◆ ](#a171a7e1bdc51851bf22c6f33d99a66d5)xen\_to\_phys

| #define xen\_to\_phys | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((unsigned long) (x))

## [◆ ](#a00320c3072ff8655017aa8e28367e864)xen\_to\_virt

| #define xen\_to\_virt | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((void \*) (x))

## [◆ ](#aea05f25a15fca2bf161790935426e406)xen\_virt\_to\_gfn

| #define xen\_virt\_to\_gfn | ( |  | *\_virt* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([XEN\_PFN\_DOWN](#a8d089e7267f000ef6ce2cf98939d0df2)([xen\_to\_phys](#a171a7e1bdc51851bf22c6f33d99a66d5)(\_virt)))

[xen\_to\_phys](#a171a7e1bdc51851bf22c6f33d99a66d5)

#define xen\_to\_phys(x)

**Definition** generic.h:19

[XEN\_PFN\_DOWN](#a8d089e7267f000ef6ce2cf98939d0df2)

#define XEN\_PFN\_DOWN(x)

**Definition** generic.h:15

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [generic.h](generic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
