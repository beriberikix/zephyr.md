---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/multi__heap_8h_source.html
original_path: doxygen/html/multi__heap_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

17

33struct [sys\_multi\_heap](structsys__multi__heap.md);

34

[ 57](group__multi__heap__wrapper.md#ga2d8ac07e590ef36ba6f35ae88235564e)typedef void \*(\*sys\_multi\_heap\_fn\_t)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg,

58 size\_t align, size\_t size);

59

60

[ 61](structsys__multi__heap__rec.md)struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) {

[ 62](structsys__multi__heap__rec.md#abced99d59a80e299a76c6ea29fcc18e8) struct [sys\_heap](structsys__heap.md) \*[heap](structsys__multi__heap__rec.md#abced99d59a80e299a76c6ea29fcc18e8);

[ 63](structsys__multi__heap__rec.md#ac6f27a9f92989284a852a24e01422be7) void \*[user\_data](structsys__multi__heap__rec.md#ac6f27a9f92989284a852a24e01422be7);

64};

65

[ 66](structsys__multi__heap.md)struct [sys\_multi\_heap](structsys__multi__heap.md) {

[ 67](structsys__multi__heap.md#a3830f646e39d16401cfe75099e2facc1) unsigned int [nheaps](structsys__multi__heap.md#a3830f646e39d16401cfe75099e2facc1);

[ 68](structsys__multi__heap.md#a01dd6ce40b1ab9c84c034475e70a4fa6) [sys\_multi\_heap\_fn\_t](group__multi__heap__wrapper.md#ga2d8ac07e590ef36ba6f35ae88235564e) [choice](structsys__multi__heap.md#a01dd6ce40b1ab9c84c034475e70a4fa6);

[ 69](structsys__multi__heap.md#a36be24709ad7083957a65aad6100806e) struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) [heaps](structsys__multi__heap.md#a36be24709ad7083957a65aad6100806e)[[MAX\_MULTI\_HEAPS](multi__heap_8h.md#a4baed7cc76ab2037f126508a48bf4b09)];

70};

71

[ 93](group__multi__heap__wrapper.md#ga50ded513b50c7aed7d89386bb8f425cc)void [sys\_multi\_heap\_init](group__multi__heap__wrapper.md#ga50ded513b50c7aed7d89386bb8f425cc)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*[heap](structsys__multi__heap__rec.md#abced99d59a80e299a76c6ea29fcc18e8),

94 [sys\_multi\_heap\_fn\_t](group__multi__heap__wrapper.md#ga2d8ac07e590ef36ba6f35ae88235564e) choice\_fn);

95

[ 108](group__multi__heap__wrapper.md#gacd6b92e8090a56e1eb59a18166d659d1)void [sys\_multi\_heap\_add\_heap](group__multi__heap__wrapper.md#gacd6b92e8090a56e1eb59a18166d659d1)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, struct [sys\_heap](structsys__heap.md) \*[heap](structsys__multi__heap__rec.md#abced99d59a80e299a76c6ea29fcc18e8), void \*[user\_data](structsys__multi__heap__rec.md#ac6f27a9f92989284a852a24e01422be7));

109

[ 123](group__multi__heap__wrapper.md#ga050d7499b982ed62f85d5fc15f79548b)void \*[sys\_multi\_heap\_alloc](group__multi__heap__wrapper.md#ga050d7499b982ed62f85d5fc15f79548b)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*cfg, size\_t bytes);

124

[ 138](group__multi__heap__wrapper.md#ga9f958dbfa86e12236b8e356375b8d04c)void \*[sys\_multi\_heap\_aligned\_alloc](group__multi__heap__wrapper.md#ga9f958dbfa86e12236b8e356375b8d04c)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap,

139 void \*cfg, size\_t align, size\_t bytes);

140

[ 152](group__multi__heap__wrapper.md#gad98b78be5c0ed50e1e0715a15c289b3a)const struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) \*[sys\_multi\_heap\_get\_heap](group__multi__heap__wrapper.md#gad98b78be5c0ed50e1e0715a15c289b3a)(const struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap,

153 void \*addr);

154

[ 169](group__multi__heap__wrapper.md#gac6f913a3bbf247807ba80408a242db73)void [sys\_multi\_heap\_free](group__multi__heap__wrapper.md#gac6f913a3bbf247807ba80408a242db73)(struct [sys\_multi\_heap](structsys__multi__heap.md) \*mheap, void \*block);

170

174

175#endif /\* ZEPHYR\_INCLUDE\_SYS\_MULTI\_HEAP\_H\_ \*/

[sys\_multi\_heap\_alloc](group__multi__heap__wrapper.md#ga050d7499b982ed62f85d5fc15f79548b)

void \* sys\_multi\_heap\_alloc(struct sys\_multi\_heap \*mheap, void \*cfg, size\_t bytes)

Allocate memory from multi heap.

[sys\_multi\_heap\_fn\_t](group__multi__heap__wrapper.md#ga2d8ac07e590ef36ba6f35ae88235564e)

void \*(\* sys\_multi\_heap\_fn\_t)(struct sys\_multi\_heap \*mheap, void \*cfg, size\_t align, size\_t size)

Multi-heap choice function.

**Definition** multi\_heap.h:57

[sys\_multi\_heap\_init](group__multi__heap__wrapper.md#ga50ded513b50c7aed7d89386bb8f425cc)

void sys\_multi\_heap\_init(struct sys\_multi\_heap \*heap, sys\_multi\_heap\_fn\_t choice\_fn)

Initialize multi-heap.

[sys\_multi\_heap\_aligned\_alloc](group__multi__heap__wrapper.md#ga9f958dbfa86e12236b8e356375b8d04c)

void \* sys\_multi\_heap\_aligned\_alloc(struct sys\_multi\_heap \*mheap, void \*cfg, size\_t align, size\_t bytes)

Allocate aligned memory from multi heap.

[sys\_multi\_heap\_free](group__multi__heap__wrapper.md#gac6f913a3bbf247807ba80408a242db73)

void sys\_multi\_heap\_free(struct sys\_multi\_heap \*mheap, void \*block)

Free memory allocated from multi heap.

[sys\_multi\_heap\_add\_heap](group__multi__heap__wrapper.md#gacd6b92e8090a56e1eb59a18166d659d1)

void sys\_multi\_heap\_add\_heap(struct sys\_multi\_heap \*mheap, struct sys\_heap \*heap, void \*user\_data)

Add sys\_heap to multi heap.

[sys\_multi\_heap\_get\_heap](group__multi__heap__wrapper.md#gad98b78be5c0ed50e1e0715a15c289b3a)

const struct sys\_multi\_heap\_rec \* sys\_multi\_heap\_get\_heap(const struct sys\_multi\_heap \*mheap, void \*addr)

Get a specific heap for provided address.

[types.h](include_2zephyr_2types_8h.md)

[MAX\_MULTI\_HEAPS](multi__heap_8h.md#a4baed7cc76ab2037f126508a48bf4b09)

#define MAX\_MULTI\_HEAPS

**Definition** multi\_heap.h:10

[sys\_heap](structsys__heap.md)

**Definition** sys\_heap.h:56

[sys\_multi\_heap\_rec](structsys__multi__heap__rec.md)

**Definition** multi\_heap.h:61

[sys\_multi\_heap\_rec::heap](structsys__multi__heap__rec.md#abced99d59a80e299a76c6ea29fcc18e8)

struct sys\_heap \* heap

**Definition** multi\_heap.h:62

[sys\_multi\_heap\_rec::user\_data](structsys__multi__heap__rec.md#ac6f27a9f92989284a852a24e01422be7)

void \* user\_data

**Definition** multi\_heap.h:63

[sys\_multi\_heap](structsys__multi__heap.md)

**Definition** multi\_heap.h:66

[sys\_multi\_heap::choice](structsys__multi__heap.md#a01dd6ce40b1ab9c84c034475e70a4fa6)

sys\_multi\_heap\_fn\_t choice

**Definition** multi\_heap.h:68

[sys\_multi\_heap::heaps](structsys__multi__heap.md#a36be24709ad7083957a65aad6100806e)

struct sys\_multi\_heap\_rec heaps[8]

**Definition** multi\_heap.h:69

[sys\_multi\_heap::nheaps](structsys__multi__heap.md#a3830f646e39d16401cfe75099e2facc1)

unsigned int nheaps

**Definition** multi\_heap.h:67

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [multi\_heap.h](multi__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
