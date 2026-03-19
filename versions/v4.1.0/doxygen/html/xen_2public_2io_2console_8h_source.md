---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xen_2public_2io_2console_8h_source.html
original_path: doxygen/html/xen_2public_2io_2console_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

console.h

[Go to the documentation of this file.](xen_2public_2io_2console_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4 \* console.h

5 \*

6 \* Console I/O interface for Xen guest OSes.

7 \*

8 \* Permission is hereby granted, free of charge, to any person obtaining a copy

9 \* of this software and associated documentation files (the "Software"), to

10 \* deal in the Software without restriction, including without limitation the

11 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

12 \* sell copies of the Software, and to permit persons to whom the Software is

13 \* furnished to do so, subject to the following conditions:

14 \*

15 \* The above copyright notice and this permission notice shall be included in

16 \* all copies or substantial portions of the Software.

17 \*

18 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

19 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

20 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

21 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

22 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

23 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

24 \* DEALINGS IN THE SOFTWARE.

25 \*

26 \* Copyright (c) 2005, Keir Fraser

27 \*/

28

29#ifndef \_\_XEN\_PUBLIC\_IO\_CONSOLE\_H\_\_

30#define \_\_XEN\_PUBLIC\_IO\_CONSOLE\_H\_\_

31

[ 32](xen_2public_2io_2console_8h.md#aa49f8668886bc6a29fee54402474f068)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [XENCONS\_RING\_IDX](xen_2public_2io_2console_8h.md#aa49f8668886bc6a29fee54402474f068);

33

[ 34](xen_2public_2io_2console_8h.md#a19ac5a1c26856ccdfbba6e6cbe86430a)#define MASK\_XENCONS\_IDX(idx, ring) ((idx) & (sizeof(ring)-1))

35

[ 36](structxencons__interface.md)struct [xencons\_interface](structxencons__interface.md) {

[ 37](structxencons__interface.md#a14233e2ff990cc8592a8f8ab64f14160) char [in](structxencons__interface.md#a14233e2ff990cc8592a8f8ab64f14160)[1024];

[ 38](structxencons__interface.md#a3fd4897533d042e1c3f6819946d65ea2) char [out](structxencons__interface.md#a3fd4897533d042e1c3f6819946d65ea2)[2048];

[ 39](structxencons__interface.md#aaf3058366352057c9376ebfbe22f0c7e) [XENCONS\_RING\_IDX](xen_2public_2io_2console_8h.md#aa49f8668886bc6a29fee54402474f068) [in\_cons](structxencons__interface.md#aaf3058366352057c9376ebfbe22f0c7e), [in\_prod](structxencons__interface.md#a8edf69249d3535a6b2a9d5884beb4d62);

[ 40](structxencons__interface.md#a97486890daa9956e020b1cb33f192391) [XENCONS\_RING\_IDX](xen_2public_2io_2console_8h.md#aa49f8668886bc6a29fee54402474f068) [out\_cons](structxencons__interface.md#a97486890daa9956e020b1cb33f192391), [out\_prod](structxencons__interface.md#acb6a82b3857702a16830e42fc7c498bd);

41};

42

43#ifdef XEN\_WANT\_FLEX\_CONSOLE\_RING

44#include "ring.h"

45DEFINE\_XEN\_FLEX\_RING(xencons);

46#endif

47

48#endif /\* \_\_XEN\_PUBLIC\_IO\_CONSOLE\_H\_\_ \*/

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[xencons\_interface](structxencons__interface.md)

**Definition** console.h:36

[xencons\_interface::in](structxencons__interface.md#a14233e2ff990cc8592a8f8ab64f14160)

char in[1024]

**Definition** console.h:37

[xencons\_interface::out](structxencons__interface.md#a3fd4897533d042e1c3f6819946d65ea2)

char out[2048]

**Definition** console.h:38

[xencons\_interface::in\_prod](structxencons__interface.md#a8edf69249d3535a6b2a9d5884beb4d62)

XENCONS\_RING\_IDX in\_prod

**Definition** console.h:39

[xencons\_interface::out\_cons](structxencons__interface.md#a97486890daa9956e020b1cb33f192391)

XENCONS\_RING\_IDX out\_cons

**Definition** console.h:40

[xencons\_interface::in\_cons](structxencons__interface.md#aaf3058366352057c9376ebfbe22f0c7e)

XENCONS\_RING\_IDX in\_cons

**Definition** console.h:39

[xencons\_interface::out\_prod](structxencons__interface.md#acb6a82b3857702a16830e42fc7c498bd)

XENCONS\_RING\_IDX out\_prod

**Definition** console.h:40

[XENCONS\_RING\_IDX](xen_2public_2io_2console_8h.md#aa49f8668886bc6a29fee54402474f068)

uint32\_t XENCONS\_RING\_IDX

**Definition** console.h:32

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [io](dir_78ec230a751ffdc5d7d32748ed18d356.md)
- [console.h](xen_2public_2io_2console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
