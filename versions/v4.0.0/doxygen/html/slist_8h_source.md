---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/slist_8h_source.html
original_path: doxygen/html/slist_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

slist.h

[Go to the documentation of this file.](slist_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

19

20#ifndef ZEPHYR\_INCLUDE\_SYS\_SLIST\_H\_

21#define ZEPHYR\_INCLUDE\_SYS\_SLIST\_H\_

22

23#include <stddef.h>

24#include <[stdbool.h](stdbool_8h.md)>

25#include "[list\_gen.h](list__gen_8h.md)"

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

31

33struct \_snode {

34 struct \_snode \*next;

35};

37

[ 39](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)typedef struct \_snode [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493);

40

42struct \_slist {

43 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*head;

44 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*tail;

45};

47

[ 49](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)typedef struct \_slist [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8);

50

[ 66](group__single-linked-list__apis.md#gaf32ac0f222186e497d3f6180b6c26352)#define SYS\_SLIST\_FOR\_EACH\_NODE(\_\_sl, \_\_sn) \

67 Z\_GENLIST\_FOR\_EACH\_NODE(slist, \_\_sl, \_\_sn)

68

[ 89](group__single-linked-list__apis.md#ga1740075b07ec67635c1934dcbe1b5cee)#define SYS\_SLIST\_ITERATE\_FROM\_NODE(\_\_sl, \_\_sn) \

90 Z\_GENLIST\_ITERATE\_FROM\_NODE(slist, \_\_sl, \_\_sn)

91

[ 108](group__single-linked-list__apis.md#gad6f1014e26d6cf9925d00b4f53076116)#define SYS\_SLIST\_FOR\_EACH\_NODE\_SAFE(\_\_sl, \_\_sn, \_\_sns) \

109 Z\_GENLIST\_FOR\_EACH\_NODE\_SAFE(slist, \_\_sl, \_\_sn, \_\_sns)

110

[ 119](group__single-linked-list__apis.md#ga07e4257835751e18a6c06bfa5f9c25e8)#define SYS\_SLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n) \

120 Z\_GENLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n)

121

[ 129](group__single-linked-list__apis.md#ga8fdb1e6baa7ba061dc1bd35f73a2fff1)#define SYS\_SLIST\_PEEK\_HEAD\_CONTAINER(\_\_sl, \_\_cn, \_\_n) \

130 Z\_GENLIST\_PEEK\_HEAD\_CONTAINER(slist, \_\_sl, \_\_cn, \_\_n)

131

[ 139](group__single-linked-list__apis.md#ga709c87e180d48c782c1583d7fb7629b3)#define SYS\_SLIST\_PEEK\_TAIL\_CONTAINER(\_\_sl, \_\_cn, \_\_n) \

140 Z\_GENLIST\_PEEK\_TAIL\_CONTAINER(slist, \_\_sl, \_\_cn, \_\_n)

141

[ 148](group__single-linked-list__apis.md#ga5d1c9ee21f75da485ba12aa56471e699)#define SYS\_SLIST\_PEEK\_NEXT\_CONTAINER(\_\_cn, \_\_n) \

149 Z\_GENLIST\_PEEK\_NEXT\_CONTAINER(slist, \_\_cn, \_\_n)

150

[ 165](group__single-linked-list__apis.md#gacd97d2f1044c0560d96c9f9a6f26d2f6)#define SYS\_SLIST\_FOR\_EACH\_CONTAINER(\_\_sl, \_\_cn, \_\_n) \

166 Z\_GENLIST\_FOR\_EACH\_CONTAINER(slist, \_\_sl, \_\_cn, \_\_n)

167

[ 183](group__single-linked-list__apis.md#gacf3aaf32a6a3389229b548588c6d655e)#define SYS\_SLIST\_FOR\_EACH\_CONTAINER\_SAFE(\_\_sl, \_\_cn, \_\_cns, \_\_n) \

184 Z\_GENLIST\_FOR\_EACH\_CONTAINER\_SAFE(slist, \_\_sl, \_\_cn, \_\_cns, \_\_n)

185

186

187/\*

188 \* Required function definitions for the list\_gen.h interface

189 \*

190 \* These are the only functions that do not treat the list/node pointers

191 \* as completely opaque types.

192 \*/

193

[ 199](group__single-linked-list__apis.md#ga913aea7661b4ab3b4b50a8efc0d70428)static inline void [sys\_slist\_init](group__single-linked-list__apis.md#ga913aea7661b4ab3b4b50a8efc0d70428)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list)

200{

201 list->head = NULL;

202 list->tail = NULL;

203}

204

[ 209](group__single-linked-list__apis.md#ga7f4710125f45643b7acdaa58dbfff225)#define SYS\_SLIST\_STATIC\_INIT(ptr\_to\_list) {NULL, NULL}

210

211static inline [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*z\_snode\_next\_peek([sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node)

212{

213 return node->next;

214}

215

216static inline void z\_snode\_next\_set([sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*parent, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*child)

217{

218 parent->next = child;

219}

220

221static inline void z\_slist\_head\_set([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node)

222{

223 list->head = node;

224}

225

226static inline void z\_slist\_tail\_set([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node)

227{

228 list->tail = node;

229}

230

[ 238](group__single-linked-list__apis.md#ga1af7fbf228545d591ef8961fa5f6a8f1)static inline [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*[sys\_slist\_peek\_head](group__single-linked-list__apis.md#ga1af7fbf228545d591ef8961fa5f6a8f1)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list)

239{

240 return list->head;

241}

242

[ 250](group__single-linked-list__apis.md#ga49975721fa11c48000669d2c4ec0877f)static inline [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*[sys\_slist\_peek\_tail](group__single-linked-list__apis.md#ga49975721fa11c48000669d2c4ec0877f)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list)

251{

252 return list->tail;

253}

254

255/\*

256 \* Derived, generated APIs

257 \*/

258

266static inline bool [sys\_slist\_is\_empty](group__single-linked-list__apis.md#ga7d729bbb7bba57c5784ad0d2c341670a)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list);

267

[ 268](group__single-linked-list__apis.md#ga7d729bbb7bba57c5784ad0d2c341670a)Z\_GENLIST\_IS\_EMPTY(slist)

269

270

279static inline [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*[sys\_slist\_peek\_next\_no\_check](group__single-linked-list__apis.md#ga58d001a256f28278f0e7c0b96b9cc492)([sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node);

280

[ 281](group__single-linked-list__apis.md#ga58d001a256f28278f0e7c0b96b9cc492)Z\_GENLIST\_PEEK\_NEXT\_NO\_CHECK(slist, snode)

282

283

290static inline [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*[sys\_slist\_peek\_next](group__single-linked-list__apis.md#ga729cbf8cafdbc34261db9274195ac5df)([sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node);

291

[ 292](group__single-linked-list__apis.md#ga729cbf8cafdbc34261db9274195ac5df)Z\_GENLIST\_PEEK\_NEXT(slist, snode)

293

294

302static inline void [sys\_slist\_prepend](group__single-linked-list__apis.md#gac962e3ec8440e4adb2ba6682dbf186ff)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list,

303 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node);

304

[ 305](group__single-linked-list__apis.md#gac962e3ec8440e4adb2ba6682dbf186ff)Z\_GENLIST\_PREPEND(slist, snode)

306

307

315static inline void [sys\_slist\_append](group__single-linked-list__apis.md#ga829fd7b6f1944dc38e10685e861e62b5)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list,

316 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node);

317

[ 318](group__single-linked-list__apis.md#ga829fd7b6f1944dc38e10685e861e62b5)Z\_GENLIST\_APPEND(slist, snode)

319

320

333static inline void [sys\_slist\_append\_list](group__single-linked-list__apis.md#gaaf7393c6bbf6d5cbd303173d95269481)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list,

334 void \*head, void \*tail);

335

[ 336](group__single-linked-list__apis.md#gaaf7393c6bbf6d5cbd303173d95269481)Z\_GENLIST\_APPEND\_LIST(slist, snode)

337

338

347static inline void [sys\_slist\_merge\_slist](group__single-linked-list__apis.md#ga0c00bbb3dc6903f386fdb1e37fdd3b66)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list,

348 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list\_to\_append);

349

[ 350](group__single-linked-list__apis.md#ga0c00bbb3dc6903f386fdb1e37fdd3b66)Z\_GENLIST\_MERGE\_LIST(slist, snode)

351

352

361static inline void [sys\_slist\_insert](group__single-linked-list__apis.md#gadcbef5c013861fdfd325bae357c37b85)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list,

362 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*prev,

363 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node);

364

[ 365](group__single-linked-list__apis.md#gadcbef5c013861fdfd325bae357c37b85)Z\_GENLIST\_INSERT(slist, snode)

366

367

377static inline [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*[sys\_slist\_get\_not\_empty](group__single-linked-list__apis.md#ga036a65b86f101a7867a83cdd1617ba33)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list);

378

[ 379](group__single-linked-list__apis.md#ga036a65b86f101a7867a83cdd1617ba33)Z\_GENLIST\_GET\_NOT\_EMPTY(slist, snode)

380

381

390static inline [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*[sys\_slist\_get](group__single-linked-list__apis.md#ga497d7e9069c08e25a03ebc212ef8bbb3)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list);

391

[ 392](group__single-linked-list__apis.md#ga497d7e9069c08e25a03ebc212ef8bbb3)Z\_GENLIST\_GET(slist, snode)

393

394

404static inline void [sys\_slist\_remove](group__single-linked-list__apis.md#gaee6957483d4fbe3b824f7a495d56030f)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list,

405 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*prev\_node,

406 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node);

407

[ 408](group__single-linked-list__apis.md#gaee6957483d4fbe3b824f7a495d56030f)Z\_GENLIST\_REMOVE(slist, snode)

409

410

420static inline bool [sys\_slist\_find\_and\_remove](group__single-linked-list__apis.md#ga296560229ffdfd0054c9c7b0602825a6)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list,

421 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node);

422

434static inline bool [sys\_slist\_find](group__single-linked-list__apis.md#gaca24163d9f029c1b78e4637349d2ef92)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*node,

435 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \*\*prev);

[ 436](group__single-linked-list__apis.md#gaca24163d9f029c1b78e4637349d2ef92)Z\_GENLIST\_FIND(slist, snode)

437

438

445static inline size\_t [sys\_slist\_len](group__single-linked-list__apis.md#ga02a4d013fa37aca2943effe3afa0567b)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list);

446

[ 447](group__single-linked-list__apis.md#ga02a4d013fa37aca2943effe3afa0567b)Z\_GENLIST\_LEN(slist, snode)

448

449

[ 450](group__single-linked-list__apis.md#ga296560229ffdfd0054c9c7b0602825a6)Z\_GENLIST\_FIND\_AND\_REMOVE(slist, snode)

451

452#ifdef \_\_cplusplus

453}

454#endif

455

456#endif /\* ZEPHYR\_INCLUDE\_SYS\_SLIST\_H\_ \*/

[sys\_slist\_len](group__single-linked-list__apis.md#ga02a4d013fa37aca2943effe3afa0567b)

static size\_t sys\_slist\_len(sys\_slist\_t \*list)

Compute the size of the given list in O(n) time.

**Definition** slist.h:447

[sys\_slist\_get\_not\_empty](group__single-linked-list__apis.md#ga036a65b86f101a7867a83cdd1617ba33)

static sys\_snode\_t \* sys\_slist\_get\_not\_empty(sys\_slist\_t \*list)

Fetch and remove the first node of the given list.

**Definition** slist.h:379

[sys\_slist\_merge\_slist](group__single-linked-list__apis.md#ga0c00bbb3dc6903f386fdb1e37fdd3b66)

static void sys\_slist\_merge\_slist(sys\_slist\_t \*list, sys\_slist\_t \*list\_to\_append)

merge two slists, appending the second one to the first

**Definition** slist.h:350

[sys\_slist\_peek\_head](group__single-linked-list__apis.md#ga1af7fbf228545d591ef8961fa5f6a8f1)

static sys\_snode\_t \* sys\_slist\_peek\_head(sys\_slist\_t \*list)

Peek the first node from the list.

**Definition** slist.h:238

[sys\_slist\_find\_and\_remove](group__single-linked-list__apis.md#ga296560229ffdfd0054c9c7b0602825a6)

static bool sys\_slist\_find\_and\_remove(sys\_slist\_t \*list, sys\_snode\_t \*node)

Find and remove a node from a list.

**Definition** slist.h:450

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_slist\_get](group__single-linked-list__apis.md#ga497d7e9069c08e25a03ebc212ef8bbb3)

static sys\_snode\_t \* sys\_slist\_get(sys\_slist\_t \*list)

Fetch and remove the first node of the given list.

**Definition** slist.h:392

[sys\_slist\_peek\_tail](group__single-linked-list__apis.md#ga49975721fa11c48000669d2c4ec0877f)

static sys\_snode\_t \* sys\_slist\_peek\_tail(sys\_slist\_t \*list)

Peek the last node from the list.

**Definition** slist.h:250

[sys\_slist\_peek\_next\_no\_check](group__single-linked-list__apis.md#ga58d001a256f28278f0e7c0b96b9cc492)

static sys\_snode\_t \* sys\_slist\_peek\_next\_no\_check(sys\_snode\_t \*node)

Peek the next node from current node, node is not NULL.

**Definition** slist.h:281

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[sys\_slist\_peek\_next](group__single-linked-list__apis.md#ga729cbf8cafdbc34261db9274195ac5df)

static sys\_snode\_t \* sys\_slist\_peek\_next(sys\_snode\_t \*node)

Peek the next node from current node.

**Definition** slist.h:292

[sys\_slist\_is\_empty](group__single-linked-list__apis.md#ga7d729bbb7bba57c5784ad0d2c341670a)

static bool sys\_slist\_is\_empty(sys\_slist\_t \*list)

Test if the given list is empty.

**Definition** slist.h:268

[sys\_slist\_append](group__single-linked-list__apis.md#ga829fd7b6f1944dc38e10685e861e62b5)

static void sys\_slist\_append(sys\_slist\_t \*list, sys\_snode\_t \*node)

Append a node to the given list.

**Definition** slist.h:318

[sys\_slist\_init](group__single-linked-list__apis.md#ga913aea7661b4ab3b4b50a8efc0d70428)

static void sys\_slist\_init(sys\_slist\_t \*list)

Initialize a list.

**Definition** slist.h:199

[sys\_slist\_append\_list](group__single-linked-list__apis.md#gaaf7393c6bbf6d5cbd303173d95269481)

static void sys\_slist\_append\_list(sys\_slist\_t \*list, void \*head, void \*tail)

Append a list to the given list.

**Definition** slist.h:336

[sys\_slist\_prepend](group__single-linked-list__apis.md#gac962e3ec8440e4adb2ba6682dbf186ff)

static void sys\_slist\_prepend(sys\_slist\_t \*list, sys\_snode\_t \*node)

Prepend a node to the given list.

**Definition** slist.h:305

[sys\_slist\_find](group__single-linked-list__apis.md#gaca24163d9f029c1b78e4637349d2ef92)

static bool sys\_slist\_find(sys\_slist\_t \*list, sys\_snode\_t \*node, sys\_snode\_t \*\*prev)

Find if a node is already linked in a singly linked list.

**Definition** slist.h:436

[sys\_slist\_insert](group__single-linked-list__apis.md#gadcbef5c013861fdfd325bae357c37b85)

static void sys\_slist\_insert(sys\_slist\_t \*list, sys\_snode\_t \*prev, sys\_snode\_t \*node)

Insert a node to the given list.

**Definition** slist.h:365

[sys\_slist\_remove](group__single-linked-list__apis.md#gaee6957483d4fbe3b824f7a495d56030f)

static void sys\_slist\_remove(sys\_slist\_t \*list, sys\_snode\_t \*prev\_node, sys\_snode\_t \*node)

Remove a node.

**Definition** slist.h:408

[list\_gen.h](list__gen_8h.md)

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [slist.h](slist_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
