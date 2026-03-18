---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hvm_8h_source.html
original_path: doxygen/html/hvm_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hvm.h

[Go to the documentation of this file.](hvm_8h.md)

1/\*

2 \* Copyright (c) 2021 EPAM Systems

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef \_\_XEN\_HVM\_H\_\_

7#define \_\_XEN\_HVM\_H\_\_

8

9#include <[zephyr/xen/public/hvm/hvm\_op.h](hvm__op_8h.md)>

10#include <[zephyr/xen/public/hvm/params.h](params_8h.md)>

11

12#include <[zephyr/kernel.h](kernel_8h.md)>

13

[ 14](hvm_8h.md#ae375499424094b2f6f8059160456b53e)int [hvm\_set\_parameter](hvm_8h.md#ae375499424094b2f6f8059160456b53e)(int idx, int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value);

[ 15](hvm_8h.md#aa4c66d130a846c3effc5ec3052d95f82)int [hvm\_get\_parameter](hvm_8h.md#aa4c66d130a846c3effc5ec3052d95f82)(int idx, int domid, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

16

17#endif /\* \_\_XEN\_HVM\_H\_\_ \*/

[hvm\_get\_parameter](hvm_8h.md#aa4c66d130a846c3effc5ec3052d95f82)

int hvm\_get\_parameter(int idx, int domid, uint64\_t \*value)

[hvm\_set\_parameter](hvm_8h.md#ae375499424094b2f6f8059160456b53e)

int hvm\_set\_parameter(int idx, int domid, uint64\_t value)

[hvm\_op.h](hvm__op_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[params.h](params_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [hvm.h](hvm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
