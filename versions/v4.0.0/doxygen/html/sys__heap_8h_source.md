---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sys__heap_8h_source.html
original_path: doxygen/html/sys__heap_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_heap.h

[Go to the documentation of this file.](sys__heap_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_SYS\_SYS\_HEAP\_H\_

7#define ZEPHYR\_INCLUDE\_SYS\_SYS\_HEAP\_H\_

8

9#include <stddef.h>

10#include <[stdbool.h](stdbool_8h.md)>

11#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

12#include <[zephyr/sys/mem\_stats.h](mem__stats_8h.md)>

13#include <[zephyr/toolchain.h](toolchain_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19/\* Simple, fast heap implementation.

20 \*

21 \* A more or less conventional segregated fit allocator with

22 \* power-of-two buckets.

23 \*

24 \* Excellent space efficiency. Chunks can be split arbitrarily in 8

25 \* byte units. Overhead is only four bytes per allocated chunk (eight

26 \* bytes for heaps >256kb or on 64 bit systems), plus a log2-sized

27 \* array of 2-word bucket headers. No coarse alignment restrictions

28 \* on blocks, they can be split and merged (in units of 8 bytes)

29 \* arbitrarily.

30 \*

31 \* Simple API. Initialize at runtime with any blob of memory and not

32 \* a macro-generated, carefully aligned static array. Allocate and

33 \* free by user pointer and not an opaque block handle.

34 \*

35 \* Good fragmentation resistance. Freed blocks are always immediately

36 \* merged with adjacent free blocks. Allocations are attempted from a

37 \* sample of the smallest bucket that might fit, falling back rapidly

38 \* to the smallest block guaranteed to fit. Split memory remaining in

39 \* the chunk is always returned immediately to the heap for other

40 \* allocation.

41 \*

42 \* Excellent performance with firmly bounded runtime. All operations

43 \* are constant time (though there is a search of the smallest bucket

44 \* that has a compile-time-configurable upper bound, setting this to

45 \* extreme values results in an effectively linear search of the

46 \* list), objectively fast (~hundred instructions) and amenable to

47 \* locked operation.

48 \*/

49

50/\* Note: the init\_mem/bytes fields are for the static initializer to

51 \* have somewhere to put the arguments. The actual heap metadata at

52 \* runtime lives in the heap memory itself and this struct simply

53 \* functions as an opaque pointer. Would be good to clean this up and

54 \* put the two values somewhere else, though it would make

55 \* SYS\_HEAP\_DEFINE a little hairy to write.

56 \*/

[ 57](structsys__heap.md)struct [sys\_heap](structsys__heap.md) {

[ 58](structsys__heap.md#ac67ddabc4097bebe6fcd2068fd8cd5d9) struct z\_heap \*[heap](structsys__heap.md#ac67ddabc4097bebe6fcd2068fd8cd5d9);

[ 59](structsys__heap.md#af0764ddfe848b03712e3fe7164766ef5) void \*[init\_mem](structsys__heap.md#af0764ddfe848b03712e3fe7164766ef5);

[ 60](structsys__heap.md#a319a113212300c7bbb383a474af0793e) size\_t [init\_bytes](structsys__heap.md#a319a113212300c7bbb383a474af0793e);

61};

62

63struct z\_heap\_stress\_result {

64 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) total\_allocs;

65 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) successful\_allocs;

66 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) total\_frees;

67 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) accumulated\_in\_use\_bytes;

68};

69

75

76#ifdef CONFIG\_SYS\_HEAP\_RUNTIME\_STATS

77

85int sys\_heap\_runtime\_stats\_get(struct [sys\_heap](structsys__heap.md) \*heap,

86 struct [sys\_memory\_stats](structsys__memory__stats.md) \*stats);

87

97int sys\_heap\_runtime\_stats\_reset\_max(struct [sys\_heap](structsys__heap.md) \*heap);

98

99#endif

100

[ 109](group__low__level__heap__allocator.md#ga520768606a3c28b084cf11f8ec82fae6)void [sys\_heap\_init](group__low__level__heap__allocator.md#ga520768606a3c28b084cf11f8ec82fae6)(struct [sys\_heap](structsys__heap.md) \*heap, void \*mem, size\_t bytes);

110

[ 128](group__low__level__heap__allocator.md#ga6b8bdf02c9be5576fddbe711904a3aad)void \*[sys\_heap\_alloc](group__low__level__heap__allocator.md#ga6b8bdf02c9be5576fddbe711904a3aad)(struct [sys\_heap](structsys__heap.md) \*heap, size\_t bytes);

129

[ 143](group__low__level__heap__allocator.md#ga92a973158860c6863e1aba8516311076)void \*[sys\_heap\_aligned\_alloc](group__low__level__heap__allocator.md#ga92a973158860c6863e1aba8516311076)(struct [sys\_heap](structsys__heap.md) \*heap, size\_t align, size\_t bytes);

144

[ 158](group__low__level__heap__allocator.md#gab654da64adf74e67ae12f263eb420560)void [sys\_heap\_free](group__low__level__heap__allocator.md#gab654da64adf74e67ae12f263eb420560)(struct [sys\_heap](structsys__heap.md) \*heap, void \*mem);

159

[ 178](group__low__level__heap__allocator.md#ga16e1408c3ad5541daac756e46b33b612)void \*[sys\_heap\_aligned\_realloc](group__low__level__heap__allocator.md#ga16e1408c3ad5541daac756e46b33b612)(struct [sys\_heap](structsys__heap.md) \*heap, void \*ptr,

179 size\_t align, size\_t bytes);

180

[ 181](group__low__level__heap__allocator.md#ga0b6c4f17521a4ea996f5abf15883737a)#define sys\_heap\_realloc(heap, ptr, bytes) \

182 sys\_heap\_aligned\_realloc(heap, ptr, 0, bytes)

183

[ 198](group__low__level__heap__allocator.md#gaf8cb77365c04022181e2fc45e3fbce4a)size\_t [sys\_heap\_usable\_size](group__low__level__heap__allocator.md#gaf8cb77365c04022181e2fc45e3fbce4a)(struct [sys\_heap](structsys__heap.md) \*heap, void \*mem);

199

213#ifdef CONFIG\_SYS\_HEAP\_VALIDATE

214bool [sys\_heap\_validate](group__low__level__heap__allocator.md#ga81de9cc56f9fb88ae12ea70cc85d1db1)(struct [sys\_heap](structsys__heap.md) \*heap);

215#else

[ 216](group__low__level__heap__allocator.md#ga81de9cc56f9fb88ae12ea70cc85d1db1)static inline bool [sys\_heap\_validate](group__low__level__heap__allocator.md#ga81de9cc56f9fb88ae12ea70cc85d1db1)(struct [sys\_heap](structsys__heap.md) \*heap)

217{

218 ARG\_UNUSED(heap);

219 return true;

220}

221#endif

222

[ 252](group__low__level__heap__allocator.md#gae2f307f7b25e4927d3dbe650567b6308)void [sys\_heap\_stress](group__low__level__heap__allocator.md#gae2f307f7b25e4927d3dbe650567b6308)(void \*(\*alloc\_fn)(void \*arg, size\_t bytes),

253 void (\*free\_fn)(void \*arg, void \*p),

254 void \*arg, size\_t total\_bytes,

255 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op\_count,

256 void \*scratch\_mem, size\_t scratch\_bytes,

257 int target\_percent,

258 struct z\_heap\_stress\_result \*result);

259

[ 268](group__low__level__heap__allocator.md#gaf36db704bd892b657ccaa7a4cebc45e5)void [sys\_heap\_print\_info](group__low__level__heap__allocator.md#gaf36db704bd892b657ccaa7a4cebc45e5)(struct [sys\_heap](structsys__heap.md) \*heap, bool dump\_chunks);

269

273

274#ifdef \_\_cplusplus

275}

276#endif

277

278#endif /\* ZEPHYR\_INCLUDE\_SYS\_SYS\_HEAP\_H\_ \*/

[sys\_heap\_aligned\_realloc](group__low__level__heap__allocator.md#ga16e1408c3ad5541daac756e46b33b612)

void \* sys\_heap\_aligned\_realloc(struct sys\_heap \*heap, void \*ptr, size\_t align, size\_t bytes)

Expand the size of an existing allocation.

[sys\_heap\_init](group__low__level__heap__allocator.md#ga520768606a3c28b084cf11f8ec82fae6)

void sys\_heap\_init(struct sys\_heap \*heap, void \*mem, size\_t bytes)

Initialize sys\_heap.

[sys\_heap\_alloc](group__low__level__heap__allocator.md#ga6b8bdf02c9be5576fddbe711904a3aad)

void \* sys\_heap\_alloc(struct sys\_heap \*heap, size\_t bytes)

Allocate memory from a sys\_heap.

[sys\_heap\_validate](group__low__level__heap__allocator.md#ga81de9cc56f9fb88ae12ea70cc85d1db1)

static bool sys\_heap\_validate(struct sys\_heap \*heap)

Validate heap integrity.

**Definition** sys\_heap.h:216

[sys\_heap\_aligned\_alloc](group__low__level__heap__allocator.md#ga92a973158860c6863e1aba8516311076)

void \* sys\_heap\_aligned\_alloc(struct sys\_heap \*heap, size\_t align, size\_t bytes)

Allocate aligned memory from a sys\_heap.

[sys\_heap\_free](group__low__level__heap__allocator.md#gab654da64adf74e67ae12f263eb420560)

void sys\_heap\_free(struct sys\_heap \*heap, void \*mem)

Free memory into a sys\_heap.

[sys\_heap\_stress](group__low__level__heap__allocator.md#gae2f307f7b25e4927d3dbe650567b6308)

void sys\_heap\_stress(void \*(\*alloc\_fn)(void \*arg, size\_t bytes), void(\*free\_fn)(void \*arg, void \*p), void \*arg, size\_t total\_bytes, uint32\_t op\_count, void \*scratch\_mem, size\_t scratch\_bytes, int target\_percent, struct z\_heap\_stress\_result \*result)

sys\_heap stress test rig

[sys\_heap\_print\_info](group__low__level__heap__allocator.md#gaf36db704bd892b657ccaa7a4cebc45e5)

void sys\_heap\_print\_info(struct sys\_heap \*heap, bool dump\_chunks)

Print heap internal structure information to the console.

[sys\_heap\_usable\_size](group__low__level__heap__allocator.md#gaf8cb77365c04022181e2fc45e3fbce4a)

size\_t sys\_heap\_usable\_size(struct sys\_heap \*heap, void \*mem)

Return allocated memory size.

[types.h](include_2zephyr_2types_8h.md)

[mem\_stats.h](mem__stats_8h.md)

Memory Statistics.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[sys\_heap](structsys__heap.md)

**Definition** sys\_heap.h:57

[sys\_heap::init\_bytes](structsys__heap.md#a319a113212300c7bbb383a474af0793e)

size\_t init\_bytes

**Definition** sys\_heap.h:60

[sys\_heap::heap](structsys__heap.md#ac67ddabc4097bebe6fcd2068fd8cd5d9)

struct z\_heap \* heap

**Definition** sys\_heap.h:58

[sys\_heap::init\_mem](structsys__heap.md#af0764ddfe848b03712e3fe7164766ef5)

void \* init\_mem

**Definition** sys\_heap.h:59

[sys\_memory\_stats](structsys__memory__stats.md)

**Definition** mem\_stats.h:24

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [sys\_heap.h](sys__heap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
