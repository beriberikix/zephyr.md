---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sflist_8h_source.html
original_path: doxygen/html/sflist_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sflist.h

[Go to the documentation of this file.](sflist_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

24

25#ifndef ZEPHYR\_INCLUDE\_SYS\_SFLIST\_H\_

26#define ZEPHYR\_INCLUDE\_SYS\_SFLIST\_H\_

27

28#include <stddef.h>

29#include <[stdbool.h](stdbool_8h.md)>

30#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

31#include "[list\_gen.h](list__gen_8h.md)"

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

37#ifdef \_\_LP64\_\_

38typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [unative\_t](group__flagged-single-linked-list__apis.md#ga5f0d5529e0d52d1a0d3c9594fadff48c);

39#else

[ 40](group__flagged-single-linked-list__apis.md#ga5f0d5529e0d52d1a0d3c9594fadff48c)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unative\_t](group__flagged-single-linked-list__apis.md#ga5f0d5529e0d52d1a0d3c9594fadff48c);

41#endif

42

44struct \_sfnode {

45 [unative\_t](group__flagged-single-linked-list__apis.md#ga5f0d5529e0d52d1a0d3c9594fadff48c) next\_and\_flags;

46};

48

[ 50](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7)typedef struct \_sfnode [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7);

51

53struct \_sflist {

54 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*head;

55 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*tail;

56};

58

[ 60](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66)typedef struct \_sflist [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66);

61

[ 77](group__flagged-single-linked-list__apis.md#gaa3e9a3eeef7ecca012b0926fb2758c01)#define SYS\_SFLIST\_FOR\_EACH\_NODE(\_\_sl, \_\_sn) \

78 Z\_GENLIST\_FOR\_EACH\_NODE(sflist, \_\_sl, \_\_sn)

79

[ 100](group__flagged-single-linked-list__apis.md#ga0470a27a54ed20eec35baa6cacd6a5ff)#define SYS\_SFLIST\_ITERATE\_FROM\_NODE(\_\_sl, \_\_sn) \

101 Z\_GENLIST\_ITERATE\_FROM\_NODE(sflist, \_\_sl, \_\_sn)

102

[ 119](group__flagged-single-linked-list__apis.md#gabe867ebba43f1f0ebd2441147a9e3d3d)#define SYS\_SFLIST\_FOR\_EACH\_NODE\_SAFE(\_\_sl, \_\_sn, \_\_sns) \

120 Z\_GENLIST\_FOR\_EACH\_NODE\_SAFE(sflist, \_\_sl, \_\_sn, \_\_sns)

121

[ 130](group__flagged-single-linked-list__apis.md#ga68dae6db03b52bc27777a2b8c274a852)#define SYS\_SFLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n) \

131 Z\_GENLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n)

132

[ 140](group__flagged-single-linked-list__apis.md#ga2c339b75ed80f3a94b0419ac73f18682)#define SYS\_SFLIST\_PEEK\_HEAD\_CONTAINER(\_\_sl, \_\_cn, \_\_n) \

141 Z\_GENLIST\_PEEK\_HEAD\_CONTAINER(sflist, \_\_sl, \_\_cn, \_\_n)

142

[ 150](group__flagged-single-linked-list__apis.md#ga73760da17d0daefe655bbd750a3ce3e8)#define SYS\_SFLIST\_PEEK\_TAIL\_CONTAINER(\_\_sl, \_\_cn, \_\_n) \

151 Z\_GENLIST\_PEEK\_TAIL\_CONTAINER(sflist, \_\_sl, \_\_cn, \_\_n)

152

[ 159](group__flagged-single-linked-list__apis.md#ga0ba4b870acea3a10a1be066fb1d769c8)#define SYS\_SFLIST\_PEEK\_NEXT\_CONTAINER(\_\_cn, \_\_n) \

160 Z\_GENLIST\_PEEK\_NEXT\_CONTAINER(sflist, \_\_cn, \_\_n)

161

[ 176](group__flagged-single-linked-list__apis.md#ga1db228cdfd8004738fc6c4d2430be0cc)#define SYS\_SFLIST\_FOR\_EACH\_CONTAINER(\_\_sl, \_\_cn, \_\_n) \

177 Z\_GENLIST\_FOR\_EACH\_CONTAINER(sflist, \_\_sl, \_\_cn, \_\_n)

178

[ 194](group__flagged-single-linked-list__apis.md#ga6b33a7b2be024c0e243f5bbccf900e81)#define SYS\_SFLIST\_FOR\_EACH\_CONTAINER\_SAFE(\_\_sl, \_\_cn, \_\_cns, \_\_n) \

195 Z\_GENLIST\_FOR\_EACH\_CONTAINER\_SAFE(sflist, \_\_sl, \_\_cn, \_\_cns, \_\_n)

196

197

198/\*

199 \* Required function definitions for the list\_gen.h interface

200 \*

201 \* These are the only functions that do not treat the list/node pointers

202 \* as completely opaque types.

203 \*/

204

[ 210](group__flagged-single-linked-list__apis.md#ga9597045ad20485fd88a0fec83fe1ffe1)static inline void [sys\_sflist\_init](group__flagged-single-linked-list__apis.md#ga9597045ad20485fd88a0fec83fe1ffe1)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list)

211{

212 list->head = NULL;

213 list->tail = NULL;

214}

215

[ 220](group__flagged-single-linked-list__apis.md#ga892d5c9ce2d89b04f0ce15a88eefed71)#define SYS\_SFLIST\_STATIC\_INIT(ptr\_to\_list) {NULL, NULL}

[ 221](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2)#define SYS\_SFLIST\_FLAGS\_MASK 0x3UL

222

223static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*z\_sfnode\_next\_peek([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node)

224{

225 return ([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*)(node->next\_and\_flags & [~SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2));

226}

227

228static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_sfnode\_flags\_get](group__flagged-single-linked-list__apis.md#ga0e258c1faa3cbaee48c29e8f2c11132b)([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

229

230static inline void z\_sfnode\_next\_set([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*parent,

231 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*child)

232{

233 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cur\_flags = [sys\_sfnode\_flags\_get](group__flagged-single-linked-list__apis.md#ga0e258c1faa3cbaee48c29e8f2c11132b)(parent);

234

235 parent->next\_and\_flags = cur\_flags | ([unative\_t](group__flagged-single-linked-list__apis.md#ga5f0d5529e0d52d1a0d3c9594fadff48c))child;

236}

237

238static inline void z\_sflist\_head\_set([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node)

239{

240 list->head = node;

241}

242

243static inline void z\_sflist\_tail\_set([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node)

244{

245 list->tail = node;

246}

247

[ 255](group__flagged-single-linked-list__apis.md#ga6c993728bebb604f966cdc944939642e)static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_peek\_head](group__flagged-single-linked-list__apis.md#ga6c993728bebb604f966cdc944939642e)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list)

256{

257 return list->head;

258}

259

[ 267](group__flagged-single-linked-list__apis.md#gabf278ac7912180fc50a25c0ebddc093c)static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_peek\_tail](group__flagged-single-linked-list__apis.md#gabf278ac7912180fc50a25c0ebddc093c)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list)

268{

269 return list->tail;

270}

271

272/\*

273 \* APIs specific to sflist type

274 \*/

275

[ 282](group__flagged-single-linked-list__apis.md#ga0e258c1faa3cbaee48c29e8f2c11132b)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_sfnode\_flags\_get](group__flagged-single-linked-list__apis.md#ga0e258c1faa3cbaee48c29e8f2c11132b)([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node)

283{

284 return node->next\_and\_flags & [SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2);

285}

286

[ 300](group__flagged-single-linked-list__apis.md#gae56469b67ad7a92363d04ac726e326ea)static inline void [sys\_sfnode\_init](group__flagged-single-linked-list__apis.md#gae56469b67ad7a92363d04ac726e326ea)([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

301{

302 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ~[SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2)) == 0UL, "flags too large");

303 node->next\_and\_flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

304}

305

[ 316](group__flagged-single-linked-list__apis.md#ga85d82a3a5927f79a5f5655cb3405ce95)static inline void [sys\_sfnode\_flags\_set](group__flagged-single-linked-list__apis.md#ga85d82a3a5927f79a5f5655cb3405ce95)([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

317{

318 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ~[SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2)) == 0UL, "flags too large");

319 node->next\_and\_flags = ([unative\_t](group__flagged-single-linked-list__apis.md#ga5f0d5529e0d52d1a0d3c9594fadff48c))(z\_sfnode\_next\_peek(node)) | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

320}

321

322/\*

323 \* Derived, generated APIs

324 \*/

325

333static inline bool [sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#gac506235a9df89a7a52631e9990ceaad5)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list);

334

[ 335](group__flagged-single-linked-list__apis.md#gac506235a9df89a7a52631e9990ceaad5)Z\_GENLIST\_IS\_EMPTY(sflist)

336

337

346static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_peek\_next\_no\_check](group__flagged-single-linked-list__apis.md#gaa67d15dd4fb28dbbc64f4b0e8e21455e)([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

347

[ 348](group__flagged-single-linked-list__apis.md#gaa67d15dd4fb28dbbc64f4b0e8e21455e)Z\_GENLIST\_PEEK\_NEXT\_NO\_CHECK(sflist, sfnode)

349

350

357static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_peek\_next](group__flagged-single-linked-list__apis.md#ga514b41f1af89f3f08e216cfede7d5605)([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

358

[ 359](group__flagged-single-linked-list__apis.md#ga514b41f1af89f3f08e216cfede7d5605)Z\_GENLIST\_PEEK\_NEXT(sflist, sfnode)

360

361

369static inline void [sys\_sflist\_prepend](group__flagged-single-linked-list__apis.md#ga824ff283c821b6f392ebd81516b65712)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

370 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

371

[ 372](group__flagged-single-linked-list__apis.md#ga824ff283c821b6f392ebd81516b65712)Z\_GENLIST\_PREPEND(sflist, sfnode)

373

374

382static inline void [sys\_sflist\_append](group__flagged-single-linked-list__apis.md#ga77733972e39b7db9fc3dcc998261fb2d)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

383 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

384

[ 385](group__flagged-single-linked-list__apis.md#ga77733972e39b7db9fc3dcc998261fb2d)Z\_GENLIST\_APPEND(sflist, sfnode)

386

387

400static inline void [sys\_sflist\_append\_list](group__flagged-single-linked-list__apis.md#gaaf9512d6c4432f34347771c9887e678a)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

401 void \*head, void \*tail);

402

[ 403](group__flagged-single-linked-list__apis.md#gaaf9512d6c4432f34347771c9887e678a)Z\_GENLIST\_APPEND\_LIST(sflist, sfnode)

404

405

414static inline void [sys\_sflist\_merge\_sflist](group__flagged-single-linked-list__apis.md#ga6c68678fceb6127a34760fb04ddef8b0)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

415 [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list\_to\_append);

416

[ 417](group__flagged-single-linked-list__apis.md#ga6c68678fceb6127a34760fb04ddef8b0)Z\_GENLIST\_MERGE\_LIST(sflist, sfnode)

418

419

428static inline void [sys\_sflist\_insert](group__flagged-single-linked-list__apis.md#ga8983c5704eb149b0941f1fb19f79b8c1)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

429 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*prev,

430 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

431

[ 432](group__flagged-single-linked-list__apis.md#ga8983c5704eb149b0941f1fb19f79b8c1)Z\_GENLIST\_INSERT(sflist, sfnode)

433

434

444static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_get\_not\_empty](group__flagged-single-linked-list__apis.md#ga065a7968e8082b65f9344a6331b424fc)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list);

445

[ 446](group__flagged-single-linked-list__apis.md#ga065a7968e8082b65f9344a6331b424fc)Z\_GENLIST\_GET\_NOT\_EMPTY(sflist, sfnode)

447

448

457static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_get](group__flagged-single-linked-list__apis.md#ga124d4dbb8d6d554071cb5eac2585b4ac)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list);

458

[ 459](group__flagged-single-linked-list__apis.md#ga124d4dbb8d6d554071cb5eac2585b4ac)Z\_GENLIST\_GET(sflist, sfnode)

460

461

471static inline void [sys\_sflist\_remove](group__flagged-single-linked-list__apis.md#ga66c716ef7495fcb04ea60aac340dc5ed)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

472 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*prev\_node,

473 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

474

[ 475](group__flagged-single-linked-list__apis.md#ga66c716ef7495fcb04ea60aac340dc5ed)Z\_GENLIST\_REMOVE(sflist, sfnode)

476

477

487static inline bool [sys\_sflist\_find\_and\_remove](group__flagged-single-linked-list__apis.md#gad66348fe7677cca76a547e09c8354322)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

488 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

489

[ 490](group__flagged-single-linked-list__apis.md#gad66348fe7677cca76a547e09c8354322)Z\_GENLIST\_FIND\_AND\_REMOVE(sflist, sfnode)

491

492

499static inline size\_t [sys\_sflist\_len](group__flagged-single-linked-list__apis.md#gaa2d7de9f2366bf638c409b34c26aa871)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list);

500

[ 501](group__flagged-single-linked-list__apis.md#gaa2d7de9f2366bf638c409b34c26aa871)Z\_GENLIST\_LEN(sflist, sfnode)

502

503

504

505#ifdef \_\_cplusplus

506}

507#endif

508

509#endif /\* ZEPHYR\_INCLUDE\_SYS\_SFLIST\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7)

struct \_sfnode sys\_sfnode\_t

Flagged single-linked list node structure.

**Definition** sflist.h:50

[sys\_sflist\_get\_not\_empty](group__flagged-single-linked-list__apis.md#ga065a7968e8082b65f9344a6331b424fc)

static sys\_sfnode\_t \* sys\_sflist\_get\_not\_empty(sys\_sflist\_t \*list)

Fetch and remove the first node of the given list.

**Definition** sflist.h:446

[sys\_sfnode\_flags\_get](group__flagged-single-linked-list__apis.md#ga0e258c1faa3cbaee48c29e8f2c11132b)

static uint8\_t sys\_sfnode\_flags\_get(sys\_sfnode\_t \*node)

Fetch flags value for a particular sfnode.

**Definition** sflist.h:282

[sys\_sflist\_get](group__flagged-single-linked-list__apis.md#ga124d4dbb8d6d554071cb5eac2585b4ac)

static sys\_sfnode\_t \* sys\_sflist\_get(sys\_sflist\_t \*list)

Fetch and remove the first node of the given list.

**Definition** sflist.h:459

[SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2)

#define SYS\_SFLIST\_FLAGS\_MASK

**Definition** sflist.h:221

[sys\_sflist\_peek\_next](group__flagged-single-linked-list__apis.md#ga514b41f1af89f3f08e216cfede7d5605)

static sys\_sfnode\_t \* sys\_sflist\_peek\_next(sys\_sfnode\_t \*node)

Peek the next node from current node.

**Definition** sflist.h:359

[unative\_t](group__flagged-single-linked-list__apis.md#ga5f0d5529e0d52d1a0d3c9594fadff48c)

uint32\_t unative\_t

**Definition** sflist.h:40

[sys\_sflist\_remove](group__flagged-single-linked-list__apis.md#ga66c716ef7495fcb04ea60aac340dc5ed)

static void sys\_sflist\_remove(sys\_sflist\_t \*list, sys\_sfnode\_t \*prev\_node, sys\_sfnode\_t \*node)

Remove a node.

**Definition** sflist.h:475

[sys\_sflist\_merge\_sflist](group__flagged-single-linked-list__apis.md#ga6c68678fceb6127a34760fb04ddef8b0)

static void sys\_sflist\_merge\_sflist(sys\_sflist\_t \*list, sys\_sflist\_t \*list\_to\_append)

merge two sflists, appending the second one to the first

**Definition** sflist.h:417

[sys\_sflist\_peek\_head](group__flagged-single-linked-list__apis.md#ga6c993728bebb604f966cdc944939642e)

static sys\_sfnode\_t \* sys\_sflist\_peek\_head(sys\_sflist\_t \*list)

Peek the first node from the list.

**Definition** sflist.h:255

[sys\_sflist\_append](group__flagged-single-linked-list__apis.md#ga77733972e39b7db9fc3dcc998261fb2d)

static void sys\_sflist\_append(sys\_sflist\_t \*list, sys\_sfnode\_t \*node)

Append a node to the given list.

**Definition** sflist.h:385

[sys\_sflist\_prepend](group__flagged-single-linked-list__apis.md#ga824ff283c821b6f392ebd81516b65712)

static void sys\_sflist\_prepend(sys\_sflist\_t \*list, sys\_sfnode\_t \*node)

Prepend a node to the given list.

**Definition** sflist.h:372

[sys\_sfnode\_flags\_set](group__flagged-single-linked-list__apis.md#ga85d82a3a5927f79a5f5655cb3405ce95)

static void sys\_sfnode\_flags\_set(sys\_sfnode\_t \*node, uint8\_t flags)

Set flags value for an sflist node.

**Definition** sflist.h:316

[sys\_sflist\_insert](group__flagged-single-linked-list__apis.md#ga8983c5704eb149b0941f1fb19f79b8c1)

static void sys\_sflist\_insert(sys\_sflist\_t \*list, sys\_sfnode\_t \*prev, sys\_sfnode\_t \*node)

Insert a node to the given list.

**Definition** sflist.h:432

[sys\_sflist\_init](group__flagged-single-linked-list__apis.md#ga9597045ad20485fd88a0fec83fe1ffe1)

static void sys\_sflist\_init(sys\_sflist\_t \*list)

Initialize a list.

**Definition** sflist.h:210

[sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66)

struct \_sflist sys\_sflist\_t

Flagged single-linked list structure.

**Definition** sflist.h:60

[sys\_sflist\_len](group__flagged-single-linked-list__apis.md#gaa2d7de9f2366bf638c409b34c26aa871)

static size\_t sys\_sflist\_len(sys\_sflist\_t \*list)

Compute the size of the given list in O(n) time.

**Definition** sflist.h:501

[sys\_sflist\_peek\_next\_no\_check](group__flagged-single-linked-list__apis.md#gaa67d15dd4fb28dbbc64f4b0e8e21455e)

static sys\_sfnode\_t \* sys\_sflist\_peek\_next\_no\_check(sys\_sfnode\_t \*node)

Peek the next node from current node, node is not NULL.

**Definition** sflist.h:348

[sys\_sflist\_append\_list](group__flagged-single-linked-list__apis.md#gaaf9512d6c4432f34347771c9887e678a)

static void sys\_sflist\_append\_list(sys\_sflist\_t \*list, void \*head, void \*tail)

Append a list to the given list.

**Definition** sflist.h:403

[sys\_sflist\_peek\_tail](group__flagged-single-linked-list__apis.md#gabf278ac7912180fc50a25c0ebddc093c)

static sys\_sfnode\_t \* sys\_sflist\_peek\_tail(sys\_sflist\_t \*list)

Peek the last node from the list.

**Definition** sflist.h:267

[sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#gac506235a9df89a7a52631e9990ceaad5)

static bool sys\_sflist\_is\_empty(sys\_sflist\_t \*list)

Test if the given list is empty.

**Definition** sflist.h:335

[sys\_sflist\_find\_and\_remove](group__flagged-single-linked-list__apis.md#gad66348fe7677cca76a547e09c8354322)

static bool sys\_sflist\_find\_and\_remove(sys\_sflist\_t \*list, sys\_sfnode\_t \*node)

Find and remove a node from a list.

**Definition** sflist.h:490

[sys\_sfnode\_init](group__flagged-single-linked-list__apis.md#gae56469b67ad7a92363d04ac726e326ea)

static void sys\_sfnode\_init(sys\_sfnode\_t \*node, uint8\_t flags)

Initialize an sflist node.

**Definition** sflist.h:300

[list\_gen.h](list__gen_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [sflist.h](sflist_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
