---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/multi__heap_8h_source.html
original_path: doxygen/html/multi__heap_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

multi\_heap.h

[Go to the documentation of this file.](multi__heap_8h.md)

1/\* Copyright (c) 2021 Intel Corporation

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4

5#ifndef ZEPHYR\_INCLUDE\_SYS\_MULTI\_HEAP\_H\_

6#define ZEPHYR\_INCLUDE\_SYS\_MULTI\_HEAP\_H\_

7

8#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

9

[ 10](multi__heap_8h.md#a4baed7cc76ab2037f126508a48bf4b09)#define MAX\_MULTI\_HEAPS 8

11

27struct [sys\_multi\_heap](structsys__multi__heap.md);

28

[ 51](multi__heap_8h.md#a2d8ac07e590ef36ba6f35ae88235564e)typedef void \*(\*sys\_multi\_heap\_fn\_t)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg,

52 size\_t align, size\_t size);

53

54

[ 55](structsys__multi__heap__rec.md)struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) {

[ 56](structsys__multi__heap__rec.md#abced99d59a80e299a76c6ea29fcc18e8) struct [sys\_heap](structsys__heap.md) \*[heap](structsys__multi__heap__rec.md#abced99d59a80e299a76c6ea29fcc18e8);

[ 57](structsys__multi__heap__rec.md#ac6f27a9f92989284a852a24e01422be7) void \*[user\_data](structsys__multi__heap__rec.md#ac6f27a9f92989284a852a24e01422be7);

58};

59

[ 60](structsys__multi__heap.md)struct [sys\_multi\_heap](structsys__multi__heap.md) {

[ 61](structsys__multi__heap.md#a3830f646e39d16401cfe75099e2facc1) unsigned int [nheaps](structsys__multi__heap.md#a3830f646e39d16401cfe75099e2facc1);

[ 62](structsys__multi__heap.md#a01dd6ce40b1ab9c84c034475e70a4fa6) [sys\_multi\_heap\_fn\_t](multi__heap_8h.md#a2d8ac07e590ef36ba6f35ae88235564e) [choice](structsys__multi__heap.md#a01dd6ce40b1ab9c84c034475e70a4fa6);

[ 63](structsys__multi__heap.md#a36be24709ad7083957a65aad6100806e) struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) [heaps](structsys__multi__heap.md#a36be24709ad7083957a65aad6100806e)[[MAX\_MULTI\_HEAPS](multi__heap_8h.md#a4baed7cc76ab2037f126508a48bf4b09)];

64};

65

[ 87](multi__heap_8h.md#a50ded513b50c7aed7d89386bb8f425cc)void [sys\_multi\_heap\_init](multi__heap_8h.md#a50ded513b50c7aed7d89386bb8f425cc)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*[heap](structsys__multi__heap__rec.md#abced99d59a80e299a76c6ea29fcc18e8),

88 [sys\_multi\_heap\_fn\_t](multi__heap_8h.md#a2d8ac07e590ef36ba6f35ae88235564e) choice\_fn);

89

[ 102](multi__heap_8h.md#acd6b92e8090a56e1eb59a18166d659d1)void [sys\_multi\_heap\_add\_heap](multi__heap_8h.md#acd6b92e8090a56e1eb59a18166d659d1)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, struct [sys\_heap](structsys__heap.md) \*[heap](structsys__multi__heap__rec.md#abced99d59a80e299a76c6ea29fcc18e8), void \*[user\_data](structsys__multi__heap__rec.md#ac6f27a9f92989284a852a24e01422be7));

103

[ 117](multi__heap_8h.md#a050d7499b982ed62f85d5fc15f79548b)void \*[sys\_multi\_heap\_alloc](multi__heap_8h.md#a050d7499b982ed62f85d5fc15f79548b)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg, size\_t bytes);

118

[ 132](multi__heap_8h.md#a9f958dbfa86e12236b8e356375b8d04c)void \*[sys\_multi\_heap\_aligned\_alloc](multi__heap_8h.md#a9f958dbfa86e12236b8e356375b8d04c)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap,

133 void \*cfg, size\_t align, size\_t bytes);

134

[ 146](multi__heap_8h.md#ad98b78be5c0ed50e1e0715a15c289b3a)const struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) \*[sys\_multi\_heap\_get\_heap](multi__heap_8h.md#ad98b78be5c0ed50e1e0715a15c289b3a)(const struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap,

147 void \*addr);

148

[ 163](multi__heap_8h.md#ac6f913a3bbf247807ba80408a242db73)void [sys\_multi\_heap\_free](multi__heap_8h.md#ac6f913a3bbf247807ba80408a242db73)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*block);

164

165#endif /\* ZEPHYR\_INCLUDE\_SYS\_MULTI\_HEAP\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[sys\_multi\_heap\_alloc](multi__heap_8h.md#a050d7499b982ed62f85d5fc15f79548b)

void \* sys\_multi\_heap\_alloc(struct sys\_multi\_heap \*mheap, void \*cfg, size\_t bytes)

Allocate memory from multi heap.

[sys\_multi\_heap\_fn\_t](multi__heap_8h.md#a2d8ac07e590ef36ba6f35ae88235564e)

void \*(\* sys\_multi\_heap\_fn\_t)(struct sys\_multi\_heap \*mheap, void \*cfg, size\_t align, size\_t size)

Multi-heap choice function.

**Definition** multi\_heap.h:51

[MAX\_MULTI\_HEAPS](multi__heap_8h.md#a4baed7cc76ab2037f126508a48bf4b09)

#define MAX\_MULTI\_HEAPS

**Definition** multi\_heap.h:10

[sys\_multi\_heap\_init](multi__heap_8h.md#a50ded513b50c7aed7d89386bb8f425cc)

void sys\_multi\_heap\_init(struct sys\_multi\_heap \*heap, sys\_multi\_heap\_fn\_t choice\_fn)

Initialize multi-heap.

[sys\_multi\_heap\_aligned\_alloc](multi__heap_8h.md#a9f958dbfa86e12236b8e356375b8d04c)

void \* sys\_multi\_heap\_aligned\_alloc(struct sys\_multi\_heap \*mheap, void \*cfg, size\_t align, size\_t bytes)

Allocate aligned memory from multi heap.

[sys\_multi\_heap\_free](multi__heap_8h.md#ac6f913a3bbf247807ba80408a242db73)

void sys\_multi\_heap\_free(struct sys\_multi\_heap \*mheap, void \*block)

Free memory allocated from multi heap.

[sys\_multi\_heap\_add\_heap](multi__heap_8h.md#acd6b92e8090a56e1eb59a18166d659d1)

void sys\_multi\_heap\_add\_heap(struct sys\_multi\_heap \*mheap, struct sys\_heap \*heap, void \*user\_data)

Add sys\_heap to multi heap.

[sys\_multi\_heap\_get\_heap](multi__heap_8h.md#ad98b78be5c0ed50e1e0715a15c289b3a)

const struct sys\_multi\_heap\_rec \* sys\_multi\_heap\_get\_heap(const struct sys\_multi\_heap \*mheap, void \*addr)

Get a specific heap for provided address.

[sys\_heap](structsys__heap.md)

**Definition** sys\_heap.h:56

[sys\_multi\_heap\_rec](structsys__multi__heap__rec.md)

**Definition** multi\_heap.h:55

[sys\_multi\_heap\_rec::heap](structsys__multi__heap__rec.md#abced99d59a80e299a76c6ea29fcc18e8)

struct sys\_heap \* heap

**Definition** multi\_heap.h:56

[sys\_multi\_heap\_rec::user\_data](structsys__multi__heap__rec.md#ac6f27a9f92989284a852a24e01422be7)

void \* user\_data

**Definition** multi\_heap.h:57

[sys\_multi\_heap](structsys__multi__heap.md)

**Definition** multi\_heap.h:60

[sys\_multi\_heap::choice](structsys__multi__heap.md#a01dd6ce40b1ab9c84c034475e70a4fa6)

sys\_multi\_heap\_fn\_t choice

**Definition** multi\_heap.h:62

[sys\_multi\_heap::heaps](structsys__multi__heap.md#a36be24709ad7083957a65aad6100806e)

struct sys\_multi\_heap\_rec heaps[8]

**Definition** multi\_heap.h:63

[sys\_multi\_heap::nheaps](structsys__multi__heap.md#a3830f646e39d16401cfe75099e2facc1)

unsigned int nheaps

**Definition** multi\_heap.h:61

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [multi\_heap.h](multi__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
