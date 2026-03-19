---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hvm__op_8h_source.html
original_path: doxygen/html/hvm__op_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hvm\_op.h

[Go to the documentation of this file.](hvm__op_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\*

4 \* Permission is hereby granted, free of charge, to any person obtaining a copy

5 \* of this software and associated documentation files (the "Software"), to

6 \* deal in the Software without restriction, including without limitation the

7 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

8 \* sell copies of the Software, and to permit persons to whom the Software is

9 \* furnished to do so, subject to the following conditions:

10 \*

11 \* The above copyright notice and this permission notice shall be included in

12 \* all copies or substantial portions of the Software.

13 \*

14 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

15 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

16 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

17 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

18 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

19 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

20 \* DEALINGS IN THE SOFTWARE.

21 \*

22 \* Copyright (c) 2007, Keir Fraser

23 \*/

24

25#ifndef \_\_XEN\_PUBLIC\_HVM\_HVM\_OP\_H\_\_

26#define \_\_XEN\_PUBLIC\_HVM\_HVM\_OP\_H\_\_

27

28#include "[../xen.h](xen_8h.md)"

29

30/\* Get/set subcommands: extra argument == pointer to xen\_hvm\_param struct. \*/

[ 31](hvm__op_8h.md#a9714e13adc338e97a811ac1beba162bd)#define HVMOP\_set\_param 0

[ 32](hvm__op_8h.md#a96465a9f2e2437aa398c72bfc357d928)#define HVMOP\_get\_param 1

[ 33](structxen__hvm__param.md)struct [xen\_hvm\_param](structxen__hvm__param.md) {

[ 34](structxen__hvm__param.md#aaa84c40385f1b9f7734cd4c83aaba508) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [domid](structxen__hvm__param.md#aaa84c40385f1b9f7734cd4c83aaba508); /\* IN \*/

[ 35](structxen__hvm__param.md#a013cc99760c5da40de9205117243a3ea) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pad](structxen__hvm__param.md#a013cc99760c5da40de9205117243a3ea);

[ 36](structxen__hvm__param.md#a04b163e0b69751dba0159cb6e85bbc9a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [index](structxen__hvm__param.md#a04b163e0b69751dba0159cb6e85bbc9a); /\* IN \*/

[ 37](structxen__hvm__param.md#aac9d3547914c44d58fcedfd83b856a3a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [value](structxen__hvm__param.md#aac9d3547914c44d58fcedfd83b856a3a); /\* IN/OUT \*/

38};

[ 39](hvm__op_8h.md#af8a7ad2e0c2c0be2175f3fc396e41a0e)typedef struct [xen\_hvm\_param](structxen__hvm__param.md) [xen\_hvm\_param\_t](hvm__op_8h.md#af8a7ad2e0c2c0be2175f3fc396e41a0e);

[ 40](hvm__op_8h.md#a6d8f5f9367028a68a627d0bc78c47450)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([xen\_hvm\_param\_t](hvm__op_8h.md#af8a7ad2e0c2c0be2175f3fc396e41a0e));

41

42#endif /\* \_\_XEN\_PUBLIC\_HVM\_HVM\_OP\_H\_\_ \*/

[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)

#define DEFINE\_XEN\_GUEST\_HANDLE(name)

**Definition** arch-arm.h:192

[xen\_hvm\_param\_t](hvm__op_8h.md#af8a7ad2e0c2c0be2175f3fc396e41a0e)

struct xen\_hvm\_param xen\_hvm\_param\_t

**Definition** hvm\_op.h:39

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[xen\_hvm\_param](structxen__hvm__param.md)

**Definition** hvm\_op.h:33

[xen\_hvm\_param::pad](structxen__hvm__param.md#a013cc99760c5da40de9205117243a3ea)

uint16\_t pad

**Definition** hvm\_op.h:35

[xen\_hvm\_param::index](structxen__hvm__param.md#a04b163e0b69751dba0159cb6e85bbc9a)

uint32\_t index

**Definition** hvm\_op.h:36

[xen\_hvm\_param::domid](structxen__hvm__param.md#aaa84c40385f1b9f7734cd4c83aaba508)

domid\_t domid

**Definition** hvm\_op.h:34

[xen\_hvm\_param::value](structxen__hvm__param.md#aac9d3547914c44d58fcedfd83b856a3a)

uint64\_t value

**Definition** hvm\_op.h:37

[xen.h](xen_8h.md)

[domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)

uint16\_t domid\_t

**Definition** xen.h:217

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [hvm](dir_18c76ebef650877b932e646710239d41.md)
- [hvm\_op.h](hvm__op_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
