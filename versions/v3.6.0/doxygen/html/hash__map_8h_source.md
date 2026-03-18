---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hash__map_8h_source.html
original_path: doxygen/html/hash__map_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_map.h

[Go to the documentation of this file.](hash__map_8h.md)

1/\*

2 \* Copyright (c) 2022 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_H\_

14#define ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_H\_

15

16#include <[stdbool.h](stdbool_8h.md)>

17#include <stddef.h>

18#include <[stdint.h](stdint_8h.md)>

19

20#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

21#include <[zephyr/sys/hash\_map\_api.h](hash__map__api_8h.md)>

22#include <[zephyr/sys/hash\_map\_cxx.h](hash__map__cxx_8h.md)>

23#include <[zephyr/sys/hash\_map\_oa\_lp.h](hash__map__oa__lp_8h.md)>

24#include <[zephyr/sys/hash\_map\_sc.h](hash__map__sc_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 46](group__hashmap__apis.md#gab21c79f226ca02c0225014c77f5b53d6)#define SYS\_HASHMAP\_DEFINE\_ADVANCED(\_name, \_api, \_config\_type, \_data\_type, \_hash\_func, \

47 \_alloc\_func, ...) \

48 const struct \_config\_type \_name##\_config = \_\_VA\_ARGS\_\_; \

49 struct \_data\_type \_name##\_data; \

50 struct sys\_hashmap \_name = { \

51 .api = (const struct sys\_hashmap\_api \*)(\_api), \

52 .config = (const struct sys\_hashmap\_config \*)&\_name##\_config, \

53 .data = (struct sys\_hashmap\_data \*)&\_name##\_data, \

54 .hash\_func = (\_hash\_func), \

55 .alloc\_func = (\_alloc\_func), \

56 }

57

[ 74](group__hashmap__apis.md#gacd16dd5377fe160a2154053ba20fcbd7)#define SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED(\_name, \_api, \_config\_type, \_data\_type, \_hash\_func, \

75 \_alloc\_func, ...) \

76 static const struct \_config\_type \_name##\_config = \_\_VA\_ARGS\_\_; \

77 static struct \_data\_type \_name##\_data; \

78 static struct sys\_hashmap \_name = { \

79 .api = (const struct sys\_hashmap\_api \*)(\_api), \

80 .config = (const struct sys\_hashmap\_config \*)&\_name##\_config, \

81 .data = (struct sys\_hashmap\_data \*)&\_name##\_data, \

82 .hash\_func = (\_hash\_func), \

83 .alloc\_func = (\_alloc\_func), \

84 }

85

[ 93](group__hashmap__apis.md#ga2d2eb11eccb9a9040a1b5e0b6529d500)#define SYS\_HASHMAP\_DEFINE(\_name) SYS\_HASHMAP\_DEFAULT\_DEFINE(\_name)

94

[ 102](group__hashmap__apis.md#ga5e653d2dad44c32b42dfd15107f6ba3c)#define SYS\_HASHMAP\_DEFINE\_STATIC(\_name) SYS\_HASHMAP\_DEFAULT\_DEFINE\_STATIC(\_name)

103

104/\*

105 \* A safe wrapper for realloc(), invariant of which libc provides it.

106 \*/

[ 107](group__hashmap__apis.md#gad24a1d4e49b9ce811e1a5770480d00bd)static inline void \*[sys\_hashmap\_default\_allocator](group__hashmap__apis.md#gad24a1d4e49b9ce811e1a5770480d00bd)(void \*ptr, size\_t size)

108{

109 if (size == 0) {

110 [free](stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711)(ptr);

111 return NULL;

112 }

113

114 return [realloc](stdlib_8h.md#ad28fed1039f35d754710633141b4edf0)(ptr, size);

115}

116

[ 118](group__hashmap__apis.md#gadcb3c72b93993222ebfe8a5e58389308)#define SYS\_HASHMAP\_DEFAULT\_ALLOCATOR sys\_hashmap\_default\_allocator

119

[ 121](group__hashmap__apis.md#ga2f1e3b37ac9eb4c939883b1696c87b86)#define SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR 75

122

[ 124](structsys__hashmap.md)struct [sys\_hashmap](structsys__hashmap.md) {

[ 126](structsys__hashmap.md#a88b8b0e3773a5f388bd5362b7283c5a9) const struct [sys\_hashmap\_api](structsys__hashmap__api.md) \*[api](structsys__hashmap.md#a88b8b0e3773a5f388bd5362b7283c5a9);

[ 128](structsys__hashmap.md#ae52ee56fa68b011dc388a1ef0a01a7d2) const struct [sys\_hashmap\_config](structsys__hashmap__config.md) \*[config](structsys__hashmap.md#ae52ee56fa68b011dc388a1ef0a01a7d2);

[ 130](structsys__hashmap.md#a405d543f6015d0defa362e4285b0d6cd) struct [sys\_hashmap\_data](structsys__hashmap__data.md) \*[data](structsys__hashmap.md#a405d543f6015d0defa362e4285b0d6cd);

[ 132](structsys__hashmap.md#a56028566cb14b8722503e527445bbfc9) [sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad) [hash\_func](structsys__hashmap.md#a56028566cb14b8722503e527445bbfc9);

[ 134](structsys__hashmap.md#ad1cf742360a600ee20c89d68ea42b3f8) [sys\_hashmap\_allocator\_t](group__hashmap__apis.md#ga813a4f65e3672651ef37c06dccdcfebc) [alloc\_func](structsys__hashmap.md#ad1cf742360a600ee20c89d68ea42b3f8);

135};

136

[ 144](group__hashmap__apis.md#gadee4fa23549a92afbe89a71125a859cd)static inline void [sys\_hashmap\_foreach](group__hashmap__apis.md#gadee4fa23549a92afbe89a71125a859cd)(const struct [sys\_hashmap](structsys__hashmap.md) \*map, [sys\_hashmap\_callback\_t](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1) cb,

145 void \*cookie)

146{

147 struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) it = {0};

148

149 for ([map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[api](structsys__hashmap.md#a88b8b0e3773a5f388bd5362b7283c5a9)->[iter](structsys__hashmap__api.md#a1487c726730c010f286609d5cc77a109)([map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), &it); [sys\_hashmap\_iterator\_has\_next](group__hashmap__apis.md#ga15020630e76f826893c58faded3737ed)(&it);) {

150 it.[next](structsys__hashmap__iterator.md#a8c79527ba05d0dcfe2f13e0fe387efa4)(&it);

151 cb(it.[key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958), it.[value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24), cookie);

152 }

153}

154

[ 164](group__hashmap__apis.md#gad859ec4ac776c876874bb3a88071a8aa)static inline void [sys\_hashmap\_clear](group__hashmap__apis.md#gad859ec4ac776c876874bb3a88071a8aa)(struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), [sys\_hashmap\_callback\_t](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1) cb,

165 void \*cookie)

166{

167 [map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[api](structsys__hashmap.md#a88b8b0e3773a5f388bd5362b7283c5a9)->[clear](structsys__hashmap__api.md#a7b39c2920e8a65d7c4e01912a3ea4136)([map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), cb, cookie);

168}

169

[ 185](group__hashmap__apis.md#ga4868b88473fe8d160ec77bce495165cf)static inline int [sys\_hashmap\_insert](group__hashmap__apis.md#ga4868b88473fe8d160ec77bce495165cf)(struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24),

186 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*old\_value)

187{

188 return [map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[api](structsys__hashmap.md#a88b8b0e3773a5f388bd5362b7283c5a9)->[insert](structsys__hashmap__api.md#acdf4df23107858b3a1d891b3ce437dad)([map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), [key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958), [value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24), old\_value);

189}

190

[ 203](group__hashmap__apis.md#ga45db255d4a6108f8da789eda01184c0b)static inline bool [sys\_hashmap\_remove](group__hashmap__apis.md#ga45db255d4a6108f8da789eda01184c0b)(struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*[value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24))

204{

205 return [map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[api](structsys__hashmap.md#a88b8b0e3773a5f388bd5362b7283c5a9)->[remove](structsys__hashmap__api.md#a20443bacc5669e724ac74573539f0fb7)([map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), [key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958), [value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24));

206}

207

[ 220](group__hashmap__apis.md#ga51125854595615092330070f380cb231)static inline bool [sys\_hashmap\_get](group__hashmap__apis.md#ga51125854595615092330070f380cb231)(const struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*[value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24))

221{

222 return [map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[api](structsys__hashmap.md#a88b8b0e3773a5f388bd5362b7283c5a9)->[get](structsys__hashmap__api.md#af014aabea50f5b0568316104986de41d)([map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), [key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958), [value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24));

223}

224

[ 234](group__hashmap__apis.md#ga95e77f9fc362673a81bf287da20fcc38)static inline bool [sys\_hashmap\_contains\_key](group__hashmap__apis.md#ga95e77f9fc362673a81bf287da20fcc38)(const struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958))

235{

236 return [sys\_hashmap\_get](group__hashmap__apis.md#ga51125854595615092330070f380cb231)([map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), [key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958), NULL);

237}

238

[ 246](group__hashmap__apis.md#ga4957bc7166ed61e66002a81dcb93bffb)static inline size\_t [sys\_hashmap\_size](group__hashmap__apis.md#ga4957bc7166ed61e66002a81dcb93bffb)(const struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c))

247{

248 return [map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[data](structsys__hashmap.md#a405d543f6015d0defa362e4285b0d6cd)->[size](structsys__hashmap__data.md#ac453e2dc52f989617feebedc6eeb2929);

249}

250

[ 259](group__hashmap__apis.md#ga5f382228a7265d2b27b9678dad442849)static inline bool [sys\_hashmap\_is\_empty](group__hashmap__apis.md#ga5f382228a7265d2b27b9678dad442849)(const struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c))

260{

261 return [map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[data](structsys__hashmap.md#a405d543f6015d0defa362e4285b0d6cd)->[size](structsys__hashmap__data.md#ac453e2dc52f989617feebedc6eeb2929) == 0;

262}

263

[ 274](group__hashmap__apis.md#ga48e6e8e55744fe270dc158bb7f31e265)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_hashmap\_load\_factor](group__hashmap__apis.md#ga48e6e8e55744fe270dc158bb7f31e265)(const struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c))

275{

276 if ([map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[data](structsys__hashmap.md#a405d543f6015d0defa362e4285b0d6cd)->[n\_buckets](structsys__hashmap__data.md#a79892de2c54612860f0dd48bce88aeea) == 0) {

277 return 0;

278 }

279

280 return ([map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[data](structsys__hashmap.md#a405d543f6015d0defa362e4285b0d6cd)->[size](structsys__hashmap__data.md#ac453e2dc52f989617feebedc6eeb2929) \* 100) / [map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[data](structsys__hashmap.md#a405d543f6015d0defa362e4285b0d6cd)->[n\_buckets](structsys__hashmap__data.md#a79892de2c54612860f0dd48bce88aeea);

281}

282

[ 289](group__hashmap__apis.md#ga7527eff4dc4d0b1818cb7d9813f688b9)static inline size\_t [sys\_hashmap\_num\_buckets](group__hashmap__apis.md#ga7527eff4dc4d0b1818cb7d9813f688b9)(const struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c))

290{

291 return [map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)->[data](structsys__hashmap.md#a405d543f6015d0defa362e4285b0d6cd)->[n\_buckets](structsys__hashmap__data.md#a79892de2c54612860f0dd48bce88aeea);

292}

293

[ 315](group__hashmap__apis.md#gaee95e9b7494773f717028c764513d7ad)static inline bool [sys\_hashmap\_should\_rehash](group__hashmap__apis.md#gaee95e9b7494773f717028c764513d7ad)(const struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c), bool grow,

316 size\_t num\_reserved, size\_t \*new\_num\_buckets)

317{

318 size\_t [size](structsys__hashmap__iterator.md#a4145137c2d1c95a7658902287cea2096);

319 bool should\_grow;

320 size\_t n\_buckets;

321 bool should\_shrink;

322 const bool shrink = !grow;

323 struct [sys\_hashmap\_oa\_lp\_data](structsys__hashmap__oa__lp__data.md) \*const data = (struct [sys\_hashmap\_oa\_lp\_data](structsys__hashmap__oa__lp__data.md) \*)map->[data](structsys__hashmap.md#a405d543f6015d0defa362e4285b0d6cd);

324 const struct [sys\_hashmap\_config](structsys__hashmap__config.md) \*const config = map->[config](structsys__hashmap.md#ae52ee56fa68b011dc388a1ef0a01a7d2);

325

326 /\* All branchless calculations, so very cache-friendly \*/

327

328 /\* calculate new size \*/

329 size = data->[size](structsys__hashmap__oa__lp__data.md#a2a4c622b61b78989e66c831d6dc75988);

330 size += grow;

331 /\* maximum size imposed by the implementation \*/

332 \_\_ASSERT\_NO\_MSG(size < [SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f) / 100);

333

334 /\* calculate new number of buckets \*/

335 n\_buckets = data->[n\_buckets](structsys__hashmap__oa__lp__data.md#ac129a45aacac72b3c9974e6c7c7e19fd);

336 /\* initial number of buckets \*/

337 n\_buckets += grow \* (size == 1) \* config->[initial\_n\_buckets](structsys__hashmap__config.md#a0a9911024bfc4c55f4a1fc179eaa6e10);

338 /\* grow at a rate of 2x \*/

339 n\_buckets <<= grow \* (size != 1);

340 /\* shrink at a rate of 2x \*/

341 n\_buckets >>= shrink;

342

343 /\* shrink to zero if empty \*/

344 n\_buckets \*= (size != 0);

345

346 \_\_ASSERT\_NO\_MSG(new\_num\_buckets != NULL);

347 \_\_ASSERT\_NO\_MSG(new\_num\_buckets != &data->[n\_buckets](structsys__hashmap__oa__lp__data.md#ac129a45aacac72b3c9974e6c7c7e19fd));

348 \*new\_num\_buckets = n\_buckets;

349

350 should\_grow =

351 grow && (data->[n\_buckets](structsys__hashmap__oa__lp__data.md#ac129a45aacac72b3c9974e6c7c7e19fd) == 0 ||

352 (size + num\_reserved) \* 100 / data->[n\_buckets](structsys__hashmap__oa__lp__data.md#ac129a45aacac72b3c9974e6c7c7e19fd) > map->[config](structsys__hashmap.md#ae52ee56fa68b011dc388a1ef0a01a7d2)->[load\_factor](structsys__hashmap__config.md#a5a8683d82932ae397b92722269385baa));

353 should\_shrink =

354 shrink && (n\_buckets == 0 || (size \* 100) / n\_buckets <= map->[config](structsys__hashmap.md#ae52ee56fa68b011dc388a1ef0a01a7d2)->[load\_factor](structsys__hashmap__config.md#a5a8683d82932ae397b92722269385baa));

355

356 return should\_grow || should\_shrink;

357}

358

360

361#ifdef \_\_cplusplus

362}

363#endif

364

365#endif /\* ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_H\_ \*/

[sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad)

uint32\_t(\* sys\_hash\_func32\_t)(const void \*str, size\_t n)

32-bit Hash function interface

**Definition** hash\_function.h:41

[sys\_hashmap\_iterator\_has\_next](group__hashmap__apis.md#ga15020630e76f826893c58faded3737ed)

static bool sys\_hashmap\_iterator\_has\_next(const struct sys\_hashmap\_iterator \*it)

Check if a Hashmap iterator has a next entry.

**Definition** hash\_map\_api.h:68

[sys\_hashmap\_remove](group__hashmap__apis.md#ga45db255d4a6108f8da789eda01184c0b)

static bool sys\_hashmap\_remove(struct sys\_hashmap \*map, uint64\_t key, uint64\_t \*value)

Remove an entry from a sys\_hashmap.

**Definition** hash\_map.h:203

[sys\_hashmap\_insert](group__hashmap__apis.md#ga4868b88473fe8d160ec77bce495165cf)

static int sys\_hashmap\_insert(struct sys\_hashmap \*map, uint64\_t key, uint64\_t value, uint64\_t \*old\_value)

Insert a new entry into a sys\_hashmap.

**Definition** hash\_map.h:185

[sys\_hashmap\_load\_factor](group__hashmap__apis.md#ga48e6e8e55744fe270dc158bb7f31e265)

static uint8\_t sys\_hashmap\_load\_factor(const struct sys\_hashmap \*map)

Query the load factor of map.

**Definition** hash\_map.h:274

[sys\_hashmap\_size](group__hashmap__apis.md#ga4957bc7166ed61e66002a81dcb93bffb)

static size\_t sys\_hashmap\_size(const struct sys\_hashmap \*map)

Query the number of entries contained within map.

**Definition** hash\_map.h:246

[sys\_hashmap\_get](group__hashmap__apis.md#ga51125854595615092330070f380cb231)

static bool sys\_hashmap\_get(const struct sys\_hashmap \*map, uint64\_t key, uint64\_t \*value)

Get a value from a sys\_hashmap.

**Definition** hash\_map.h:220

[sys\_hashmap\_is\_empty](group__hashmap__apis.md#ga5f382228a7265d2b27b9678dad442849)

static bool sys\_hashmap\_is\_empty(const struct sys\_hashmap \*map)

Check if map is empty.

**Definition** hash\_map.h:259

[sys\_hashmap\_callback\_t](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1)

void(\* sys\_hashmap\_callback\_t)(uint64\_t key, uint64\_t value, void \*cookie)

Callback interface for sys\_hashmap.

**Definition** hash\_map\_api.h:106

[sys\_hashmap\_num\_buckets](group__hashmap__apis.md#ga7527eff4dc4d0b1818cb7d9813f688b9)

static size\_t sys\_hashmap\_num\_buckets(const struct sys\_hashmap \*map)

Query the number of buckets used in map.

**Definition** hash\_map.h:289

[sys\_hashmap\_allocator\_t](group__hashmap__apis.md#ga813a4f65e3672651ef37c06dccdcfebc)

void \*(\* sys\_hashmap\_allocator\_t)(void \*ptr, size\_t new\_size)

Allocator interface for sys\_hashmap.

**Definition** hash\_map\_api.h:84

[sys\_hashmap\_contains\_key](group__hashmap__apis.md#ga95e77f9fc362673a81bf287da20fcc38)

static bool sys\_hashmap\_contains\_key(const struct sys\_hashmap \*map, uint64\_t key)

Check if map contains a value associated with key.

**Definition** hash\_map.h:234

[sys\_hashmap\_default\_allocator](group__hashmap__apis.md#gad24a1d4e49b9ce811e1a5770480d00bd)

static void \* sys\_hashmap\_default\_allocator(void \*ptr, size\_t size)

**Definition** hash\_map.h:107

[sys\_hashmap\_clear](group__hashmap__apis.md#gad859ec4ac776c876874bb3a88071a8aa)

static void sys\_hashmap\_clear(struct sys\_hashmap \*map, sys\_hashmap\_callback\_t cb, void \*cookie)

Clear all entries contained in a sys\_hashmap.

**Definition** hash\_map.h:164

[sys\_hashmap\_foreach](group__hashmap__apis.md#gadee4fa23549a92afbe89a71125a859cd)

static void sys\_hashmap\_foreach(const struct sys\_hashmap \*map, sys\_hashmap\_callback\_t cb, void \*cookie)

Iterate over all values contained in a sys\_hashmap.

**Definition** hash\_map.h:144

[sys\_hashmap\_should\_rehash](group__hashmap__apis.md#gaee95e9b7494773f717028c764513d7ad)

static bool sys\_hashmap\_should\_rehash(const struct sys\_hashmap \*map, bool grow, size\_t num\_reserved, size\_t \*new\_num\_buckets)

Decide whether the Hashmap should be resized.

**Definition** hash\_map.h:315

[hash\_map\_api.h](hash__map__api_8h.md)

[hash\_map\_cxx.h](hash__map__cxx_8h.md)

C++ Hashmap.

[hash\_map\_oa\_lp.h](hash__map__oa__lp_8h.md)

Open-Addressing / Linear Probe Hashmap Implementation.

[hash\_map\_sc.h](hash__map__sc_8h.md)

Separate Chaining Hashmap Implementation.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[SIZE\_MAX](stdint_8h.md#a3c75bb398badb69c7577b21486f9963f)

#define SIZE\_MAX

**Definition** stdint.h:70

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[realloc](stdlib_8h.md#ad28fed1039f35d754710633141b4edf0)

void \* realloc(void \*ptr, size\_t size)

[free](stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711)

void free(void \*ptr)

[sys\_hashmap\_api](structsys__hashmap__api.md)

Generic Hashmap API.

**Definition** hash\_map\_api.h:168

[sys\_hashmap\_api::iter](structsys__hashmap__api.md#a1487c726730c010f286609d5cc77a109)

sys\_hashmap\_iterator\_t iter

Iterator constructor (in-place).

**Definition** hash\_map\_api.h:170

[sys\_hashmap\_api::remove](structsys__hashmap__api.md#a20443bacc5669e724ac74573539f0fb7)

sys\_hashmap\_remove\_t remove

Remove a key-value pair from the Hashmap.

**Definition** hash\_map\_api.h:176

[sys\_hashmap\_api::clear](structsys__hashmap__api.md#a7b39c2920e8a65d7c4e01912a3ea4136)

sys\_hashmap\_clear\_t clear

Clear the hash table, freeing all resources.

**Definition** hash\_map\_api.h:172

[sys\_hashmap\_api::insert](structsys__hashmap__api.md#acdf4df23107858b3a1d891b3ce437dad)

sys\_hashmap\_insert\_t insert

Insert a key-value pair into the Hashmap.

**Definition** hash\_map\_api.h:174

[sys\_hashmap\_api::get](structsys__hashmap__api.md#af014aabea50f5b0568316104986de41d)

sys\_hashmap\_get\_t get

Retrieve the value associated with a given key from the Hashmap.

**Definition** hash\_map\_api.h:178

[sys\_hashmap\_config](structsys__hashmap__config.md)

Generic Hashmap configuration.

**Definition** hash\_map\_api.h:197

[sys\_hashmap\_config::initial\_n\_buckets](structsys__hashmap__config.md#a0a9911024bfc4c55f4a1fc179eaa6e10)

uint8\_t initial\_n\_buckets

Initial number of buckets to allocate.

**Definition** hash\_map\_api.h:203

[sys\_hashmap\_config::load\_factor](structsys__hashmap__config.md#a5a8683d82932ae397b92722269385baa)

uint8\_t load\_factor

Maximum load factor expressed in hundredths.

**Definition** hash\_map\_api.h:201

[sys\_hashmap\_data](structsys__hashmap__data.md)

Generic Hashmap data.

**Definition** hash\_map\_api.h:225

[sys\_hashmap\_data::n\_buckets](structsys__hashmap__data.md#a79892de2c54612860f0dd48bce88aeea)

size\_t n\_buckets

The number of buckets currently allocated.

**Definition** hash\_map\_api.h:229

[sys\_hashmap\_data::size](structsys__hashmap__data.md#ac453e2dc52f989617feebedc6eeb2929)

size\_t size

The number of entries currently in the Hashmap.

**Definition** hash\_map\_api.h:231

[sys\_hashmap\_iterator](structsys__hashmap__iterator.md)

Generic Hashmap iterator interface.

**Definition** hash\_map\_api.h:44

[sys\_hashmap\_iterator::map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)

const struct sys\_hashmap \* map

Pointer to the associated Hashmap.

**Definition** hash\_map\_api.h:46

[sys\_hashmap\_iterator::size](structsys__hashmap__iterator.md#a4145137c2d1c95a7658902287cea2096)

const size\_t size

Number of entries in the map.

**Definition** hash\_map\_api.h:56

[sys\_hashmap\_iterator::key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958)

uint64\_t key

Key associated with the current entry.

**Definition** hash\_map\_api.h:52

[sys\_hashmap\_iterator::next](structsys__hashmap__iterator.md#a8c79527ba05d0dcfe2f13e0fe387efa4)

void(\* next)(struct sys\_hashmap\_iterator \*it)

Modify the iterator in-place to point to the next Hashmap entry.

**Definition** hash\_map\_api.h:48

[sys\_hashmap\_iterator::value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24)

uint64\_t value

Value associated with the current entry.

**Definition** hash\_map\_api.h:54

[sys\_hashmap\_oa\_lp\_data](structsys__hashmap__oa__lp__data.md)

**Definition** hash\_map\_oa\_lp.h:27

[sys\_hashmap\_oa\_lp\_data::size](structsys__hashmap__oa__lp__data.md#a2a4c622b61b78989e66c831d6dc75988)

size\_t size

**Definition** hash\_map\_oa\_lp.h:30

[sys\_hashmap\_oa\_lp\_data::n\_buckets](structsys__hashmap__oa__lp__data.md#ac129a45aacac72b3c9974e6c7c7e19fd)

size\_t n\_buckets

**Definition** hash\_map\_oa\_lp.h:29

[sys\_hashmap](structsys__hashmap.md)

Generic Hashmap.

**Definition** hash\_map.h:124

[sys\_hashmap::data](structsys__hashmap.md#a405d543f6015d0defa362e4285b0d6cd)

struct sys\_hashmap\_data \* data

Hashmap data.

**Definition** hash\_map.h:130

[sys\_hashmap::hash\_func](structsys__hashmap.md#a56028566cb14b8722503e527445bbfc9)

sys\_hash\_func32\_t hash\_func

Hash function.

**Definition** hash\_map.h:132

[sys\_hashmap::api](structsys__hashmap.md#a88b8b0e3773a5f388bd5362b7283c5a9)

const struct sys\_hashmap\_api \* api

Hashmap API.

**Definition** hash\_map.h:126

[sys\_hashmap::alloc\_func](structsys__hashmap.md#ad1cf742360a600ee20c89d68ea42b3f8)

sys\_hashmap\_allocator\_t alloc\_func

Allocator.

**Definition** hash\_map.h:134

[sys\_hashmap::config](structsys__hashmap.md#ae52ee56fa68b011dc388a1ef0a01a7d2)

const struct sys\_hashmap\_config \* config

Hashmap configuration.

**Definition** hash\_map.h:128

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_map.h](hash__map_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
