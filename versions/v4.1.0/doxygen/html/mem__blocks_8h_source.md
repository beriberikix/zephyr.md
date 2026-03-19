---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mem__blocks_8h_source.html
original_path: doxygen/html/mem__blocks_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_blocks.h

[Go to the documentation of this file.](mem__blocks_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_SYS\_MEM\_BLOCKS\_H\_

14#define ZEPHYR\_INCLUDE\_SYS\_MEM\_BLOCKS\_H\_

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20#include <stddef.h>

21#include <[stdint.h](stdint_8h.md)>

22

23#include <[zephyr/kernel.h](kernel_8h.md)>

24#include <[zephyr/math/ilog2.h](ilog2_8h.md)>

25#include <[zephyr/sys/bitarray.h](bitarray_8h.md)>

26#include <[zephyr/sys/mem\_stats.h](mem__stats_8h.md)>

27

[ 28](mem__blocks_8h.md#a0a18ac0266ab6532cdd93302ca012112)#define MAX\_MULTI\_ALLOCATORS 8

29

35

39struct sys\_mem\_blocks;

40

44struct sys\_multi\_mem\_blocks;

45

[ 51](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074)typedef struct sys\_mem\_blocks [sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074);

52

[ 58](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8)typedef struct sys\_multi\_mem\_blocks [sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8);

59

[ 78](group__mem__blocks__apis.md#ga2e58484681d0d9629af9a8c7c14453d9)typedef [sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*(\*sys\_multi\_mem\_blocks\_choice\_fn\_t)

79 (struct sys\_multi\_mem\_blocks \*[group](structgroup.md), void \*cfg);

80

84

85struct sys\_mem\_blocks\_info {

86 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks; /\* Total number of blocks \*/

87 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) blk\_sz\_shift; /\* Bit shift for block size \*/

88#ifdef CONFIG\_SYS\_MEM\_BLOCKS\_RUNTIME\_STATS

89 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) used\_blocks; /\* Current number of blocks in use \*/

90 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_used\_blocks; /\* Maximum number of blocks in use \*/

91#endif

92};

93

94struct sys\_mem\_blocks {

95 struct sys\_mem\_blocks\_info info;

96

97 /\* Memory block buffer \*/

98 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer;

99

100 /\* Bitmap of allocated blocks \*/

101 [sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitmap;

102

103#ifdef CONFIG\_SYS\_MEM\_BLOCKS\_RUNTIME\_STATS

104 /\* Spinlock guarding access to memory block internals \*/

105 struct k\_spinlock lock;

106#endif

107#ifdef CONFIG\_OBJ\_CORE\_SYS\_MEM\_BLOCKS

108 struct k\_obj\_core obj\_core;

109#endif

110};

111

112struct sys\_multi\_mem\_blocks {

113 /\* Number of allocators in this group \*/

114 int num\_allocators;

115 [sys\_multi\_mem\_blocks\_choice\_fn\_t](group__mem__blocks__apis.md#ga2e58484681d0d9629af9a8c7c14453d9) choice\_fn;

116 [sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*allocators[[MAX\_MULTI\_ALLOCATORS](mem__blocks_8h.md#a0a18ac0266ab6532cdd93302ca012112)];

117};

118

128#define \_SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, blk\_sz, num\_blks, buf, mbmod) \

129 \_SYS\_BITARRAY\_DEFINE(\_sys\_mem\_blocks\_bitmap\_##name, \

130 num\_blks, mbmod); \

131 mbmod struct sys\_mem\_blocks name = { \

132 .info = {num\_blks, ilog2(blk\_sz)}, \

133 .buffer = buf, \

134 .bitmap = &\_sys\_mem\_blocks\_bitmap\_##name, \

135 }; \

136 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(sys\_mem\_blocks\_ptr, \

137 sys\_mem\_blocks \*, \

138 \_\_##name##\_ptr) = &name; \

139 LINKER\_KEEP(\_\_##name##\_ptr);

140

150#define \_SYS\_MEM\_BLOCKS\_DEFINE(name, blk\_sz, num\_blks, balign, mbmod) \

151 mbmod uint8\_t \_\_noinit\_named(sys\_mem\_blocks\_buf\_##name) \

152 \_\_aligned(WB\_UP(balign)) \

153 \_sys\_mem\_blocks\_buf\_##name[num\_blks \* WB\_UP(blk\_sz)]; \

154 \_SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, blk\_sz, num\_blks, \

155 \_sys\_mem\_blocks\_buf\_##name, \

156 mbmod);

157

161

[ 170](group__mem__blocks__apis.md#gab49fdcd86522d318051ca6a6ddf41c7c)#define SYS\_MEM\_BLOCKS\_DEFINE(name, blk\_sz, num\_blks, buf\_align) \

171 \_SYS\_MEM\_BLOCKS\_DEFINE(name, blk\_sz, num\_blks, buf\_align,)

172

[ 181](group__mem__blocks__apis.md#gaa6b90846448323837dab3a17c3065359)#define SYS\_MEM\_BLOCKS\_DEFINE\_STATIC(name, blk\_sz, num\_blks, buf\_align) \

182 \_SYS\_MEM\_BLOCKS\_DEFINE(name, blk\_sz, num\_blks, buf\_align, static)

183

184

[ 193](group__mem__blocks__apis.md#gae6b688b2925308c9007071bab681dcdd)#define SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, blk\_sz, num\_blks, buf) \

194 \_SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, blk\_sz, num\_blks, buf,)

195

[ 204](group__mem__blocks__apis.md#gaad3cfb34553bd97290b388bec910b8cc)#define SYS\_MEM\_BLOCKS\_DEFINE\_STATIC\_WITH\_EXT\_BUF(name, blk\_sz, num\_blks, buf) \

205 \_SYS\_MEM\_BLOCKS\_DEFINE\_WITH\_EXT\_BUF(name, blk\_sz, num\_blks, buf, static)

206

[ 223](group__mem__blocks__apis.md#ga3e53a5c65bb0e88fbf20e66b016c1dff)int [sys\_mem\_blocks\_alloc](group__mem__blocks__apis.md#ga3e53a5c65bb0e88fbf20e66b016c1dff)([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, size\_t count,

224 void \*\*out\_blocks);

225

[ 240](group__mem__blocks__apis.md#ga72614d0c120f40209837b77d0333bb23)int [sys\_mem\_blocks\_alloc\_contiguous](group__mem__blocks__apis.md#ga72614d0c120f40209837b77d0333bb23)([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, size\_t count,

241 void \*\*out\_block);

242

[ 259](group__mem__blocks__apis.md#ga0ae169fbe2b3d3a68815ba0898ef5338)int [sys\_mem\_blocks\_get](group__mem__blocks__apis.md#ga0ae169fbe2b3d3a68815ba0898ef5338)([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, void \*in\_block, size\_t count);

260

[ 271](group__mem__blocks__apis.md#ga7a8ff3370747ae382ed24ad7b8b34746)int [sys\_mem\_blocks\_is\_region\_free](group__mem__blocks__apis.md#ga7a8ff3370747ae382ed24ad7b8b34746)([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, void \*in\_block, size\_t count);

272

[ 287](group__mem__blocks__apis.md#gadd799f4f2423277ed5daf08a0d150b9c)int [sys\_mem\_blocks\_free](group__mem__blocks__apis.md#gadd799f4f2423277ed5daf08a0d150b9c)([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, size\_t count,

288 void \*\*in\_blocks);

289

[ 303](group__mem__blocks__apis.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)int [sys\_mem\_blocks\_free\_contiguous](group__mem__blocks__apis.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block, void \*block, size\_t count);

304

305#ifdef CONFIG\_SYS\_MEM\_BLOCKS\_RUNTIME\_STATS

317int sys\_mem\_blocks\_runtime\_stats\_get([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block,

318 struct [sys\_memory\_stats](structsys__memory__stats.md) \*stats);

319

330int sys\_mem\_blocks\_runtime\_stats\_reset\_max([sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*mem\_block);

331#endif

332

[ 344](group__mem__blocks__apis.md#gad39867e3cd1e1e69e6fb3746c05abed0)void [sys\_multi\_mem\_blocks\_init](group__mem__blocks__apis.md#gad39867e3cd1e1e69e6fb3746c05abed0)([sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8) \*[group](structgroup.md),

345 [sys\_multi\_mem\_blocks\_choice\_fn\_t](group__mem__blocks__apis.md#ga2e58484681d0d9629af9a8c7c14453d9) choice\_fn);

346

[ 356](group__mem__blocks__apis.md#ga03967e8b917a1592638586c9cfbba4bb)void [sys\_multi\_mem\_blocks\_add\_allocator](group__mem__blocks__apis.md#ga03967e8b917a1592638586c9cfbba4bb)([sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8) \*[group](structgroup.md),

357 [sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074) \*alloc);

358

[ 380](group__mem__blocks__apis.md#gafa96b1567b57c4466c9640fd1f5408b2)int [sys\_multi\_mem\_blocks\_alloc](group__mem__blocks__apis.md#gafa96b1567b57c4466c9640fd1f5408b2)([sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8) \*[group](structgroup.md),

381 void \*cfg, size\_t count,

382 void \*\*out\_blocks,

383 size\_t \*blk\_size);

384

[ 400](group__mem__blocks__apis.md#ga8dedc28ed45e9e6350b584b1082b4d4f)int [sys\_multi\_mem\_blocks\_free](group__mem__blocks__apis.md#ga8dedc28ed45e9e6350b584b1082b4d4f)([sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8) \*[group](structgroup.md),

401 size\_t count, void \*\*in\_blocks);

402

404

405#ifdef \_\_cplusplus

406}

407#endif

408

409#endif /\* ZEPHYR\_INCLUDE\_SYS\_MEM\_BLOCKS\_H\_ \*/

[bitarray.h](bitarray_8h.md)

[sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841)

struct sys\_bitarray sys\_bitarray\_t

Bitarray structure.

**Definition** bitarray.h:48

[sys\_multi\_mem\_blocks\_t](group__mem__blocks__apis.md#ga00d9c0bafe800dffa3676d37983499a8)

struct sys\_multi\_mem\_blocks sys\_multi\_mem\_blocks\_t

Multi Memory Blocks Allocator.

**Definition** mem\_blocks.h:58

[sys\_multi\_mem\_blocks\_add\_allocator](group__mem__blocks__apis.md#ga03967e8b917a1592638586c9cfbba4bb)

void sys\_multi\_mem\_blocks\_add\_allocator(sys\_multi\_mem\_blocks\_t \*group, sys\_mem\_blocks\_t \*alloc)

Add an allocator to an allocator group.

[sys\_mem\_blocks\_get](group__mem__blocks__apis.md#ga0ae169fbe2b3d3a68815ba0898ef5338)

int sys\_mem\_blocks\_get(sys\_mem\_blocks\_t \*mem\_block, void \*in\_block, size\_t count)

Force allocation of a specified blocks in a memory block object.

[sys\_multi\_mem\_blocks\_choice\_fn\_t](group__mem__blocks__apis.md#ga2e58484681d0d9629af9a8c7c14453d9)

sys\_mem\_blocks\_t \*(\* sys\_multi\_mem\_blocks\_choice\_fn\_t)(struct sys\_multi\_mem\_blocks \*group, void \*cfg)

Multi memory blocks allocator choice function.

**Definition** mem\_blocks.h:79

[sys\_mem\_blocks\_free\_contiguous](group__mem__blocks__apis.md#ga39e7f8dfe3bda8eabc2372f9a1e87342)

int sys\_mem\_blocks\_free\_contiguous(sys\_mem\_blocks\_t \*mem\_block, void \*block, size\_t count)

Free contiguous multiple memory blocks.

[sys\_mem\_blocks\_alloc](group__mem__blocks__apis.md#ga3e53a5c65bb0e88fbf20e66b016c1dff)

int sys\_mem\_blocks\_alloc(sys\_mem\_blocks\_t \*mem\_block, size\_t count, void \*\*out\_blocks)

Allocate multiple memory blocks.

[sys\_mem\_blocks\_t](group__mem__blocks__apis.md#ga5748df756d2f9aa10fddf2f39bf8a074)

struct sys\_mem\_blocks sys\_mem\_blocks\_t

Memory Blocks Allocator.

**Definition** mem\_blocks.h:51

[sys\_mem\_blocks\_alloc\_contiguous](group__mem__blocks__apis.md#ga72614d0c120f40209837b77d0333bb23)

int sys\_mem\_blocks\_alloc\_contiguous(sys\_mem\_blocks\_t \*mem\_block, size\_t count, void \*\*out\_block)

Allocate a contiguous set of memory blocks.

[sys\_mem\_blocks\_is\_region\_free](group__mem__blocks__apis.md#ga7a8ff3370747ae382ed24ad7b8b34746)

int sys\_mem\_blocks\_is\_region\_free(sys\_mem\_blocks\_t \*mem\_block, void \*in\_block, size\_t count)

check if the region is free

[sys\_multi\_mem\_blocks\_free](group__mem__blocks__apis.md#ga8dedc28ed45e9e6350b584b1082b4d4f)

int sys\_multi\_mem\_blocks\_free(sys\_multi\_mem\_blocks\_t \*group, size\_t count, void \*\*in\_blocks)

Free memory allocated from multi memory blocks allocator group.

[sys\_multi\_mem\_blocks\_init](group__mem__blocks__apis.md#gad39867e3cd1e1e69e6fb3746c05abed0)

void sys\_multi\_mem\_blocks\_init(sys\_multi\_mem\_blocks\_t \*group, sys\_multi\_mem\_blocks\_choice\_fn\_t choice\_fn)

Initialize multi memory blocks allocator group.

[sys\_mem\_blocks\_free](group__mem__blocks__apis.md#gadd799f4f2423277ed5daf08a0d150b9c)

int sys\_mem\_blocks\_free(sys\_mem\_blocks\_t \*mem\_block, size\_t count, void \*\*in\_blocks)

Free multiple memory blocks.

[sys\_multi\_mem\_blocks\_alloc](group__mem__blocks__apis.md#gafa96b1567b57c4466c9640fd1f5408b2)

int sys\_multi\_mem\_blocks\_alloc(sys\_multi\_mem\_blocks\_t \*group, void \*cfg, size\_t count, void \*\*out\_blocks, size\_t \*blk\_size)

Allocate memory from multi memory blocks allocator group.

[ilog2.h](ilog2_8h.md)

Provide ilog2() function.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[MAX\_MULTI\_ALLOCATORS](mem__blocks_8h.md#a0a18ac0266ab6532cdd93302ca012112)

#define MAX\_MULTI\_ALLOCATORS

**Definition** mem\_blocks.h:28

[mem\_stats.h](mem__stats_8h.md)

Memory Statistics.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[group](structgroup.md)

Group structure.

**Definition** grp.h:18

[sys\_memory\_stats](structsys__memory__stats.md)

**Definition** mem\_stats.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mem\_blocks.h](mem__blocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
