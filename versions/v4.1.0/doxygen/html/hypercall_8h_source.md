---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hypercall_8h_source.html
original_path: doxygen/html/hypercall_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hypercall.h

[Go to the documentation of this file.](hypercall_8h.md)

1/\* SPDX-License-Identifier: Apache-2.0 \*/

2/\*

3 \* Copyright (c) 2021-2023 EPAM Systems

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_HYPERCALL\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_HYPERCALL\_H\_

8

9/\* defined in hypercall.S by HYPERCALL(hypercall) \*/

[ 10](hypercall_8h.md#a122b9d9c3cba8c0339502e9b230acee4)int [HYPERVISOR\_console\_io](hypercall_8h.md#a122b9d9c3cba8c0339502e9b230acee4)(int op, int cnt, char \*str);

[ 11](hypercall_8h.md#a2493899aa03561ca6161f541093390a7)int [HYPERVISOR\_sched\_op](hypercall_8h.md#a2493899aa03561ca6161f541093390a7)(int op, void \*param);

[ 12](hypercall_8h.md#a5b16a018f61a14ecf292227b84bce133)int [HYPERVISOR\_event\_channel\_op](hypercall_8h.md#a5b16a018f61a14ecf292227b84bce133)(int op, void \*param);

[ 13](hypercall_8h.md#ab33fe3d856e5aaaf38eb4c707fd5a684)int [HYPERVISOR\_hvm\_op](hypercall_8h.md#ab33fe3d856e5aaaf38eb4c707fd5a684)(int op, void \*param);

[ 14](hypercall_8h.md#a49970e12da5e083aa26228880c23c1c2)int [HYPERVISOR\_memory\_op](hypercall_8h.md#a49970e12da5e083aa26228880c23c1c2)(int op, void \*param);

[ 15](hypercall_8h.md#aa13c544d327b7c24987fd54089f10e78)int [HYPERVISOR\_grant\_table\_op](hypercall_8h.md#aa13c544d327b7c24987fd54089f10e78)(int op, void \*uop, unsigned int count);

16

17#ifdef CONFIG\_XEN\_DOM0

18int HYPERVISOR\_domctl(void \*param);

19#endif

20

21#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_HYPERCALL\_H\_ \*/

[HYPERVISOR\_console\_io](hypercall_8h.md#a122b9d9c3cba8c0339502e9b230acee4)

int HYPERVISOR\_console\_io(int op, int cnt, char \*str)

[HYPERVISOR\_sched\_op](hypercall_8h.md#a2493899aa03561ca6161f541093390a7)

int HYPERVISOR\_sched\_op(int op, void \*param)

[HYPERVISOR\_memory\_op](hypercall_8h.md#a49970e12da5e083aa26228880c23c1c2)

int HYPERVISOR\_memory\_op(int op, void \*param)

[HYPERVISOR\_event\_channel\_op](hypercall_8h.md#a5b16a018f61a14ecf292227b84bce133)

int HYPERVISOR\_event\_channel\_op(int op, void \*param)

[HYPERVISOR\_grant\_table\_op](hypercall_8h.md#aa13c544d327b7c24987fd54089f10e78)

int HYPERVISOR\_grant\_table\_op(int op, void \*uop, unsigned int count)

[HYPERVISOR\_hvm\_op](hypercall_8h.md#ab33fe3d856e5aaaf38eb4c707fd5a684)

int HYPERVISOR\_hvm\_op(int op, void \*param)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [hypercall.h](hypercall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
