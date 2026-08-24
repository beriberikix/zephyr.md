---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/min__heap_8h_source.html
original_path: doxygen/html/min__heap_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

min\_heap.h

[Go to the documentation of this file.](min__heap_8h.md)

1/\*

2 \* Copyright (c) 2025 Aerlync Labs Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_MIN\_HEAP\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_MIN\_HEAP\_H\_

9

10#include <[zephyr/sys/util.h](sys_2util_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 38](group__min__heap__apis.md#ga638b9c8b6023ec281b1adcb9ca6ba814)typedef int (\*[min\_heap\_cmp\_t](group__min__heap__apis.md#ga638b9c8b6023ec281b1adcb9ca6ba814))(const void \*a,

39 const void \*b);

40

[ 49](group__min__heap__apis.md#gab17087bc7c433bb85e94d4c88ad4ffbb)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[min\_heap\_eq\_t](group__min__heap__apis.md#gab17087bc7c433bb85e94d4c88ad4ffbb))(const void \*node,

50 const void \*other);

51

[ 55](structmin__heap.md)struct [min\_heap](structmin__heap.md) {

[ 57](structmin__heap.md#a6e4bb0c9a3687938a8630f7cc93b728b) void \*[storage](structmin__heap.md#a6e4bb0c9a3687938a8630f7cc93b728b);

[ 59](structmin__heap.md#afb0062bd8818c9184cd8469a3f95dc6d) size\_t [capacity](structmin__heap.md#afb0062bd8818c9184cd8469a3f95dc6d);

[ 61](structmin__heap.md#ab9d4b3b1a91fecef152576a47a1a0b10) size\_t [elem\_size](structmin__heap.md#ab9d4b3b1a91fecef152576a47a1a0b10);

[ 63](structmin__heap.md#a74824c3cda1d0e85f1712d9d9182922d) size\_t [size](structmin__heap.md#a74824c3cda1d0e85f1712d9d9182922d);

[ 65](structmin__heap.md#a1cde8c1bad1239b7a78b51c79b8f608d) [min\_heap\_cmp\_t](group__min__heap__apis.md#ga638b9c8b6023ec281b1adcb9ca6ba814) [cmp](structmin__heap.md#a1cde8c1bad1239b7a78b51c79b8f608d);

66};

67

[ 77](group__min__heap__apis.md#ga2363fb8ce4cd36e21ae5100e62d450c4)#define MIN\_HEAP\_DEFINE(name, cap, elem\_sz, align, cmp\_func) \

78 static uint8\_t name##\_storage[(cap) \* (elem\_sz)] \_\_aligned(align); \

79 struct min\_heap name = {.storage = name##\_storage, \

80 .capacity = (cap), \

81 .elem\_size = (elem\_sz), \

82 .size = 0, \

83 .cmp = (cmp\_func)}

84

[ 94](group__min__heap__apis.md#gab4b10202a0a9f63608061b2ce35d902c)#define MIN\_HEAP\_DEFINE\_STATIC(name, cap, elem\_sz, align, cmp\_func) \

95 static uint8\_t name##\_storage[(cap) \* (elem\_sz)] \_\_aligned(align); \

96 static struct min\_heap name = { \

97 .storage = name##\_storage, \

98 .capacity = (cap), \

99 .elem\_size = (elem\_sz), \

100 .size = 0, \

101 .cmp = (cmp\_func) \

102 }

103

[ 120](group__min__heap__apis.md#ga675aa066413418b51e2210331f5d352b)void [min\_heap\_init](group__min__heap__apis.md#ga675aa066413418b51e2210331f5d352b)(struct [min\_heap](structmin__heap.md) \*heap, void \*storage, size\_t cap,

121 size\_t elem\_size, [min\_heap\_cmp\_t](group__min__heap__apis.md#ga638b9c8b6023ec281b1adcb9ca6ba814) cmp);

122

[ 135](group__min__heap__apis.md#ga4cb5ee2bf40ab6f1ba557f8fa3927ba3)int [min\_heap\_push](group__min__heap__apis.md#ga4cb5ee2bf40ab6f1ba557f8fa3927ba3)(struct [min\_heap](structmin__heap.md) \*heap, const void \*item);

136

[ 146](group__min__heap__apis.md#ga022a40c2cd09b925118a157ba05bfc2f)void \*[min\_heap\_peek](group__min__heap__apis.md#ga022a40c2cd09b925118a157ba05bfc2f)(const struct [min\_heap](structmin__heap.md) \*heap);

147

[ 163](group__min__heap__apis.md#gab65afad260840bff650977b137404c7c)bool [min\_heap\_remove](group__min__heap__apis.md#gab65afad260840bff650977b137404c7c)(struct [min\_heap](structmin__heap.md) \*heap, size\_t id, void \*out\_buf);

164

[ 174](group__min__heap__apis.md#ga808c35eebd9e18aadeba4f5b2a4db827)static inline bool [min\_heap\_is\_empty](group__min__heap__apis.md#ga808c35eebd9e18aadeba4f5b2a4db827)(struct [min\_heap](structmin__heap.md) \*heap)

175{

176 \_\_ASSERT\_NO\_MSG(heap != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

177

178 return (heap->[size](structmin__heap.md#a74824c3cda1d0e85f1712d9d9182922d) == 0);

179}

180

[ 193](group__min__heap__apis.md#gacd04b6cd038669e229c69f60c25af9e0)bool [min\_heap\_pop](group__min__heap__apis.md#gacd04b6cd038669e229c69f60c25af9e0)(struct [min\_heap](structmin__heap.md) \*heap, void \*out\_buf);

194

[ 205](group__min__heap__apis.md#ga246f404f179c6c4c8ebeec6e15b2e3c2)void \*[min\_heap\_find](group__min__heap__apis.md#ga246f404f179c6c4c8ebeec6e15b2e3c2)(struct [min\_heap](structmin__heap.md) \*heap, [min\_heap\_eq\_t](group__min__heap__apis.md#gab17087bc7c433bb85e94d4c88ad4ffbb) eq,

206 const void \*other, size\_t \*out\_id);

207

[ 216](group__min__heap__apis.md#gac0f633e80405d5e47f8bd8eb09d952c6)static inline void \*[min\_heap\_get\_element](group__min__heap__apis.md#gac0f633e80405d5e47f8bd8eb09d952c6)(const struct [min\_heap](structmin__heap.md) \*heap,

217 size\_t index)

218{

219 \_\_ASSERT\_NO\_MSG(heap != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

220

221 return (void \*)(([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))heap->[storage](structmin__heap.md#a6e4bb0c9a3687938a8630f7cc93b728b) + index \* heap->[elem\_size](structmin__heap.md#ab9d4b3b1a91fecef152576a47a1a0b10));

222}

223

[ 238](group__min__heap__apis.md#ga73c54e30b56717ee7498141488504137)#define MIN\_HEAP\_FOREACH(heap, node\_var) \

239 for (size\_t \_i = 0; \

240 \_i < (heap)->size && (((node\_var) = min\_heap\_get\_element((heap), \_i)) || true); ++\_i)

241

245

246#ifdef \_\_cplusplus

247}

248#endif

249

250#endif /\* ZEPHYR\_INCLUDE\_SYS\_MIN\_HEAP\_H\_ \*/

[min\_heap\_peek](group__min__heap__apis.md#ga022a40c2cd09b925118a157ba05bfc2f)

void \* min\_heap\_peek(const struct min\_heap \*heap)

Peek at the top element of the min-heap.

[min\_heap\_find](group__min__heap__apis.md#ga246f404f179c6c4c8ebeec6e15b2e3c2)

void \* min\_heap\_find(struct min\_heap \*heap, min\_heap\_eq\_t eq, const void \*other, size\_t \*out\_id)

Search for a node in the heap matching a condition.

[min\_heap\_push](group__min__heap__apis.md#ga4cb5ee2bf40ab6f1ba557f8fa3927ba3)

int min\_heap\_push(struct min\_heap \*heap, const void \*item)

Push an element into the min-heap.

[min\_heap\_cmp\_t](group__min__heap__apis.md#ga638b9c8b6023ec281b1adcb9ca6ba814)

int(\* min\_heap\_cmp\_t)(const void \*a, const void \*b)

Comparator function type for min-heap ordering.

**Definition** min\_heap.h:38

[min\_heap\_init](group__min__heap__apis.md#ga675aa066413418b51e2210331f5d352b)

void min\_heap\_init(struct min\_heap \*heap, void \*storage, size\_t cap, size\_t elem\_size, min\_heap\_cmp\_t cmp)

Initialize a min-heap instance at runtime.

[min\_heap\_is\_empty](group__min__heap__apis.md#ga808c35eebd9e18aadeba4f5b2a4db827)

static bool min\_heap\_is\_empty(struct min\_heap \*heap)

Check if the min heap is empty.

**Definition** min\_heap.h:174

[min\_heap\_eq\_t](group__min__heap__apis.md#gab17087bc7c433bb85e94d4c88ad4ffbb)

bool(\* min\_heap\_eq\_t)(const void \*node, const void \*other)

Equality function for finding a node in the heap.

**Definition** min\_heap.h:49

[min\_heap\_remove](group__min__heap__apis.md#gab65afad260840bff650977b137404c7c)

bool min\_heap\_remove(struct min\_heap \*heap, size\_t id, void \*out\_buf)

Remove a specific element from the min-heap.

[min\_heap\_get\_element](group__min__heap__apis.md#gac0f633e80405d5e47f8bd8eb09d952c6)

static void \* min\_heap\_get\_element(const struct min\_heap \*heap, size\_t index)

Get a pointer to the element at the specified index.

**Definition** min\_heap.h:216

[min\_heap\_pop](group__min__heap__apis.md#gacd04b6cd038669e229c69f60c25af9e0)

bool min\_heap\_pop(struct min\_heap \*heap, void \*out\_buf)

Remove and return the highest priority element in the heap.

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[kernel.h](kernel_8h.md)

Public kernel APIs.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[min\_heap](structmin__heap.md)

min-heap data structure with user-provided comparator.

**Definition** min\_heap.h:55

[min\_heap::cmp](structmin__heap.md#a1cde8c1bad1239b7a78b51c79b8f608d)

min\_heap\_cmp\_t cmp

Comparator function.

**Definition** min\_heap.h:65

[min\_heap::storage](structmin__heap.md#a6e4bb0c9a3687938a8630f7cc93b728b)

void \* storage

Raw pointer to contiguous memory for elements.

**Definition** min\_heap.h:57

[min\_heap::size](structmin__heap.md#a74824c3cda1d0e85f1712d9d9182922d)

size\_t size

Current elements count.

**Definition** min\_heap.h:63

[min\_heap::elem\_size](structmin__heap.md#ab9d4b3b1a91fecef152576a47a1a0b10)

size\_t elem\_size

Size of each element.

**Definition** min\_heap.h:61

[min\_heap::capacity](structmin__heap.md#afb0062bd8818c9184cd8469a3f95dc6d)

size\_t capacity

Maximum number of elements.

**Definition** min\_heap.h:59

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [min\_heap.h](min__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
