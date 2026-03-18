---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/generic_8h_source.html
original_path: doxygen/html/generic_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

generic.h

[Go to the documentation of this file.](generic_8h.md)

1/\*

2 \* Copyright (c) 2021 EPAM Systems

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef \_\_XEN\_GENERIC\_H\_\_

7#define \_\_XEN\_GENERIC\_H\_\_

8

9#include <[zephyr/xen/public/xen.h](xen_8h.md)>

10

[ 11](generic_8h.md#ab22c00daf7a13fcd6f71fd389fad3919)#define XEN\_PAGE\_SIZE 4096

[ 12](generic_8h.md#acbc96e1185d1c2fab047d87da44c0308)#define XEN\_PAGE\_SHIFT 12

13

[ 14](generic_8h.md#a87e8ebaed995d91a2fd87f34e3a37843)#define XEN\_PFN\_UP(x) (unsigned long)(((x) + XEN\_PAGE\_SIZE-1) >> XEN\_PAGE\_SHIFT)

[ 15](generic_8h.md#a8d089e7267f000ef6ce2cf98939d0df2)#define XEN\_PFN\_DOWN(x) (unsigned long)((x) >> XEN\_PAGE\_SHIFT)

[ 16](generic_8h.md#a0a87f9a4f97c5d40e583285fb97f97a0)#define XEN\_PFN\_PHYS(x) ((unsigned long)(x) << XEN\_PAGE\_SHIFT)

[ 17](generic_8h.md#afffd6c194994740f2ad3f49dac48c6d3)#define XEN\_PHYS\_PFN(x) (unsigned long)((x) >> XEN\_PAGE\_SHIFT)

18

[ 19](generic_8h.md#a171a7e1bdc51851bf22c6f33d99a66d5)#define xen\_to\_phys(x) ((unsigned long) (x))

[ 20](generic_8h.md#a00320c3072ff8655017aa8e28367e864)#define xen\_to\_virt(x) ((void \*) (x))

21

[ 22](generic_8h.md#aea05f25a15fca2bf161790935426e406)#define xen\_virt\_to\_gfn(\_virt) (XEN\_PFN\_DOWN(xen\_to\_phys(\_virt)))

[ 23](generic_8h.md#ac5ffaa30256542b5e2ee53e5bf66dced)#define xen\_gfn\_to\_virt(\_gfn) (xen\_to\_virt(XEN\_PFN\_PHYS(\_gfn)))

24

25/\*

26 \* Atomically exchange value on "ptr" position. If value on "ptr" contains

27 \* "old", then store and return "new". Otherwise, return the "old" value.

28 \*/

[ 29](generic_8h.md#a8b4a100e92b54856a2a46c9362c595f7)#define synch\_cmpxchg(ptr, old, new) \

30({ \_\_typeof\_\_(\*ptr) stored = old; \

31 \_\_atomic\_compare\_exchange\_n(ptr, &stored, new, 0, \_\_ATOMIC\_SEQ\_CST, \

32 \_\_ATOMIC\_SEQ\_CST) ? new : old; \

33})

34

35#endif /\* \_\_XEN\_GENERIC\_H\_\_ \*/

[xen.h](xen_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [generic.h](generic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
