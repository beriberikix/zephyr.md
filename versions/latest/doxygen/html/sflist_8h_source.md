---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/sflist_8h_source.html
original_path: doxygen/html/sflist_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

28#include <[stdint.h](stdint_8h.md)>

29#include <[stdbool.h](stdbool_8h.md)>

30#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

31#include "[list\_gen.h](list__gen_8h.md)"

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

38struct \_sfnode {

39 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) next\_and\_flags;

40};

42

[ 44](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7)typedef struct \_sfnode [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7);

45

47struct \_sflist {

48 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*head;

49 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*tail;

50};

52

[ 54](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66)typedef struct \_sflist [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66);

55

[ 71](group__flagged-single-linked-list__apis.md#gaa3e9a3eeef7ecca012b0926fb2758c01)#define SYS\_SFLIST\_FOR\_EACH\_NODE(\_\_sl, \_\_sn) \

72 Z\_GENLIST\_FOR\_EACH\_NODE(sflist, \_\_sl, \_\_sn)

73

[ 94](group__flagged-single-linked-list__apis.md#ga0470a27a54ed20eec35baa6cacd6a5ff)#define SYS\_SFLIST\_ITERATE\_FROM\_NODE(\_\_sl, \_\_sn) \

95 Z\_GENLIST\_ITERATE\_FROM\_NODE(sflist, \_\_sl, \_\_sn)

96

[ 113](group__flagged-single-linked-list__apis.md#gabe867ebba43f1f0ebd2441147a9e3d3d)#define SYS\_SFLIST\_FOR\_EACH\_NODE\_SAFE(\_\_sl, \_\_sn, \_\_sns) \

114 Z\_GENLIST\_FOR\_EACH\_NODE\_SAFE(sflist, \_\_sl, \_\_sn, \_\_sns)

115

[ 124](group__flagged-single-linked-list__apis.md#ga68dae6db03b52bc27777a2b8c274a852)#define SYS\_SFLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n) \

125 Z\_GENLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n)

126

[ 134](group__flagged-single-linked-list__apis.md#ga2c339b75ed80f3a94b0419ac73f18682)#define SYS\_SFLIST\_PEEK\_HEAD\_CONTAINER(\_\_sl, \_\_cn, \_\_n) \

135 Z\_GENLIST\_PEEK\_HEAD\_CONTAINER(sflist, \_\_sl, \_\_cn, \_\_n)

136

[ 144](group__flagged-single-linked-list__apis.md#ga73760da17d0daefe655bbd750a3ce3e8)#define SYS\_SFLIST\_PEEK\_TAIL\_CONTAINER(\_\_sl, \_\_cn, \_\_n) \

145 Z\_GENLIST\_PEEK\_TAIL\_CONTAINER(sflist, \_\_sl, \_\_cn, \_\_n)

146

[ 153](group__flagged-single-linked-list__apis.md#ga0ba4b870acea3a10a1be066fb1d769c8)#define SYS\_SFLIST\_PEEK\_NEXT\_CONTAINER(\_\_cn, \_\_n) \

154 Z\_GENLIST\_PEEK\_NEXT\_CONTAINER(sflist, \_\_cn, \_\_n)

155

[ 170](group__flagged-single-linked-list__apis.md#ga1db228cdfd8004738fc6c4d2430be0cc)#define SYS\_SFLIST\_FOR\_EACH\_CONTAINER(\_\_sl, \_\_cn, \_\_n) \

171 Z\_GENLIST\_FOR\_EACH\_CONTAINER(sflist, \_\_sl, \_\_cn, \_\_n)

172

[ 188](group__flagged-single-linked-list__apis.md#ga6b33a7b2be024c0e243f5bbccf900e81)#define SYS\_SFLIST\_FOR\_EACH\_CONTAINER\_SAFE(\_\_sl, \_\_cn, \_\_cns, \_\_n) \

189 Z\_GENLIST\_FOR\_EACH\_CONTAINER\_SAFE(sflist, \_\_sl, \_\_cn, \_\_cns, \_\_n)

190

191

192/\*

193 \* Required function definitions for the list\_gen.h interface

194 \*

195 \* These are the only functions that do not treat the list/node pointers

196 \* as completely opaque types.

197 \*/

198

[ 204](group__flagged-single-linked-list__apis.md#ga9597045ad20485fd88a0fec83fe1ffe1)static inline void [sys\_sflist\_init](group__flagged-single-linked-list__apis.md#ga9597045ad20485fd88a0fec83fe1ffe1)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list)

205{

206 list->head = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

207 list->tail = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

208}

209

[ 214](group__flagged-single-linked-list__apis.md#ga892d5c9ce2d89b04f0ce15a88eefed71)#define SYS\_SFLIST\_STATIC\_INIT(ptr\_to\_list) {NULL, NULL}

215

216/\* Flag bits are stored in unused LSB of the sys\_sfnode\_t pointer \*/

[ 217](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2)#define SYS\_SFLIST\_FLAGS\_MASK ((uintptr\_t)(\_\_alignof\_\_(sys\_sfnode\_t) - 1))

218/\* At least 2 available flag bits are expected \*/

219BUILD\_ASSERT([SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2) >= 0x3);

220

221static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*z\_sfnode\_next\_peek(const [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node)

222{

223 return ([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*)(node->next\_and\_flags & [~SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2));

224}

225

226static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_sfnode\_flags\_get](group__flagged-single-linked-list__apis.md#gac37d689834e258c4f113204f574c1c9c)(const [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

227

228static inline void z\_sfnode\_next\_set([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*parent,

229 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*child)

230{

231 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cur\_flags = [sys\_sfnode\_flags\_get](group__flagged-single-linked-list__apis.md#gac37d689834e258c4f113204f574c1c9c)(parent);

232

233 parent->next\_and\_flags = cur\_flags | ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))child;

234}

235

236static inline void z\_sflist\_head\_set([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node)

237{

238 list->head = node;

239}

240

241static inline void z\_sflist\_tail\_set([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list, [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node)

242{

243 list->tail = node;

244}

245

[ 253](group__flagged-single-linked-list__apis.md#gaa21d0f39228534840c81ac518c82541c)static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_peek\_head](group__flagged-single-linked-list__apis.md#gaa21d0f39228534840c81ac518c82541c)(const [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list)

254{

255 return list->head;

256}

257

[ 265](group__flagged-single-linked-list__apis.md#ga89f8bbced2992a84bae32db74e544788)static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_peek\_tail](group__flagged-single-linked-list__apis.md#ga89f8bbced2992a84bae32db74e544788)(const [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list)

266{

267 return list->tail;

268}

269

270/\*

271 \* APIs specific to sflist type

272 \*/

273

[ 281](group__flagged-single-linked-list__apis.md#gac37d689834e258c4f113204f574c1c9c)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_sfnode\_flags\_get](group__flagged-single-linked-list__apis.md#gac37d689834e258c4f113204f574c1c9c)(const [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node)

282{

283 return node->next\_and\_flags & [SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2);

284}

285

[ 300](group__flagged-single-linked-list__apis.md#gae56469b67ad7a92363d04ac726e326ea)static inline void [sys\_sfnode\_init](group__flagged-single-linked-list__apis.md#gae56469b67ad7a92363d04ac726e326ea)([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

301{

302 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ~[SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2)) == 0UL, "flags too large");

303 node->next\_and\_flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

304}

305

[ 317](group__flagged-single-linked-list__apis.md#ga85d82a3a5927f79a5f5655cb3405ce95)static inline void [sys\_sfnode\_flags\_set](group__flagged-single-linked-list__apis.md#ga85d82a3a5927f79a5f5655cb3405ce95)([sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

318{

319 \_\_ASSERT(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & ~[SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2)) == 0UL, "flags too large");

320 node->next\_and\_flags = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))(z\_sfnode\_next\_peek(node)) | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

321}

322

323/\*

324 \* Derived, generated APIs

325 \*/

326

334static inline bool [sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#ga039ad5d35670e5d18acb38a174258a7e)(const [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list);

335

[ 336](group__flagged-single-linked-list__apis.md#ga039ad5d35670e5d18acb38a174258a7e)Z\_GENLIST\_IS\_EMPTY(sflist)

337

338

347static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_peek\_next\_no\_check](group__flagged-single-linked-list__apis.md#ga45c613fd20a67fb120d94a915ce68618)(const [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

348

[ 349](group__flagged-single-linked-list__apis.md#ga45c613fd20a67fb120d94a915ce68618)Z\_GENLIST\_PEEK\_NEXT\_NO\_CHECK(sflist, sfnode)

350

351

358static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_peek\_next](group__flagged-single-linked-list__apis.md#gaa9013d3a0b241dc63d038f49f822c0f8)(const [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

359

[ 360](group__flagged-single-linked-list__apis.md#gaa9013d3a0b241dc63d038f49f822c0f8)Z\_GENLIST\_PEEK\_NEXT(sflist, sfnode)

361

362

370static inline void [sys\_sflist\_prepend](group__flagged-single-linked-list__apis.md#ga824ff283c821b6f392ebd81516b65712)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

371 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

372

[ 373](group__flagged-single-linked-list__apis.md#ga824ff283c821b6f392ebd81516b65712)Z\_GENLIST\_PREPEND(sflist, sfnode)

374

375

383static inline void [sys\_sflist\_append](group__flagged-single-linked-list__apis.md#ga77733972e39b7db9fc3dcc998261fb2d)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

384 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

385

[ 386](group__flagged-single-linked-list__apis.md#ga77733972e39b7db9fc3dcc998261fb2d)Z\_GENLIST\_APPEND(sflist, sfnode)

387

388

399static inline void [sys\_sflist\_append\_list](group__flagged-single-linked-list__apis.md#gaaf9512d6c4432f34347771c9887e678a)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

400 void \*head, void \*tail);

401

[ 402](group__flagged-single-linked-list__apis.md#gaaf9512d6c4432f34347771c9887e678a)Z\_GENLIST\_APPEND\_LIST(sflist, sfnode)

403

404

413static inline void [sys\_sflist\_merge\_sflist](group__flagged-single-linked-list__apis.md#ga6c68678fceb6127a34760fb04ddef8b0)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

414 [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list\_to\_append);

415

[ 416](group__flagged-single-linked-list__apis.md#ga6c68678fceb6127a34760fb04ddef8b0)Z\_GENLIST\_MERGE\_LIST(sflist, sfnode)

417

418

427static inline void [sys\_sflist\_insert](group__flagged-single-linked-list__apis.md#ga8983c5704eb149b0941f1fb19f79b8c1)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

428 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*prev,

429 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

430

[ 431](group__flagged-single-linked-list__apis.md#ga8983c5704eb149b0941f1fb19f79b8c1)Z\_GENLIST\_INSERT(sflist, sfnode)

432

433

443static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_get\_not\_empty](group__flagged-single-linked-list__apis.md#ga065a7968e8082b65f9344a6331b424fc)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list);

444

[ 445](group__flagged-single-linked-list__apis.md#ga065a7968e8082b65f9344a6331b424fc)Z\_GENLIST\_GET\_NOT\_EMPTY(sflist, sfnode)

446

447

456static inline [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*[sys\_sflist\_get](group__flagged-single-linked-list__apis.md#ga124d4dbb8d6d554071cb5eac2585b4ac)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list);

457

[ 458](group__flagged-single-linked-list__apis.md#ga124d4dbb8d6d554071cb5eac2585b4ac)Z\_GENLIST\_GET(sflist, sfnode)

459

460

470static inline void [sys\_sflist\_remove](group__flagged-single-linked-list__apis.md#ga66c716ef7495fcb04ea60aac340dc5ed)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

471 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*prev\_node,

472 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

473

[ 474](group__flagged-single-linked-list__apis.md#ga66c716ef7495fcb04ea60aac340dc5ed)Z\_GENLIST\_REMOVE(sflist, sfnode)

475

476

486static inline bool [sys\_sflist\_find\_and\_remove](group__flagged-single-linked-list__apis.md#gad66348fe7677cca76a547e09c8354322)([sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list,

487 [sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7) \*node);

488

[ 489](group__flagged-single-linked-list__apis.md#gad66348fe7677cca76a547e09c8354322)Z\_GENLIST\_FIND\_AND\_REMOVE(sflist, sfnode)

490

491

498static inline size\_t [sys\_sflist\_len](group__flagged-single-linked-list__apis.md#ga46a75676d66c97f0f8be694342b3c660)(const [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) \*list);

499

[ 500](group__flagged-single-linked-list__apis.md#ga46a75676d66c97f0f8be694342b3c660)Z\_GENLIST\_LEN(sflist, sfnode)

501

502

503

504#ifdef \_\_cplusplus

505}

506#endif

507

508#endif /\* ZEPHYR\_INCLUDE\_SYS\_SFLIST\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[sys\_sfnode\_t](group__flagged-single-linked-list__apis.md#ga02dabbe35036cbc11fbbefa99a129cc7)

struct \_sfnode sys\_sfnode\_t

Flagged single-linked list node structure.

**Definition** sflist.h:44

[sys\_sflist\_is\_empty](group__flagged-single-linked-list__apis.md#ga039ad5d35670e5d18acb38a174258a7e)

static bool sys\_sflist\_is\_empty(const sys\_sflist\_t \*list)

Test if the given list is empty.

**Definition** sflist.h:336

[sys\_sflist\_get\_not\_empty](group__flagged-single-linked-list__apis.md#ga065a7968e8082b65f9344a6331b424fc)

static sys\_sfnode\_t \* sys\_sflist\_get\_not\_empty(sys\_sflist\_t \*list)

Fetch and remove the first node of the given list.

**Definition** sflist.h:445

[sys\_sflist\_get](group__flagged-single-linked-list__apis.md#ga124d4dbb8d6d554071cb5eac2585b4ac)

static sys\_sfnode\_t \* sys\_sflist\_get(sys\_sflist\_t \*list)

Fetch and remove the first node of the given list.

**Definition** sflist.h:458

[sys\_sflist\_peek\_next\_no\_check](group__flagged-single-linked-list__apis.md#ga45c613fd20a67fb120d94a915ce68618)

static sys\_sfnode\_t \* sys\_sflist\_peek\_next\_no\_check(const sys\_sfnode\_t \*node)

Peek the next node from current node, node is not NULL.

**Definition** sflist.h:349

[sys\_sflist\_len](group__flagged-single-linked-list__apis.md#ga46a75676d66c97f0f8be694342b3c660)

static size\_t sys\_sflist\_len(const sys\_sflist\_t \*list)

Compute the size of the given list in O(n) time.

**Definition** sflist.h:500

[SYS\_SFLIST\_FLAGS\_MASK](group__flagged-single-linked-list__apis.md#ga46e57329036b76ab03267d2e9258d5c2)

#define SYS\_SFLIST\_FLAGS\_MASK

**Definition** sflist.h:217

[sys\_sflist\_remove](group__flagged-single-linked-list__apis.md#ga66c716ef7495fcb04ea60aac340dc5ed)

static void sys\_sflist\_remove(sys\_sflist\_t \*list, sys\_sfnode\_t \*prev\_node, sys\_sfnode\_t \*node)

Remove a node.

**Definition** sflist.h:474

[sys\_sflist\_merge\_sflist](group__flagged-single-linked-list__apis.md#ga6c68678fceb6127a34760fb04ddef8b0)

static void sys\_sflist\_merge\_sflist(sys\_sflist\_t \*list, sys\_sflist\_t \*list\_to\_append)

merge two sflists, appending the second one to the first

**Definition** sflist.h:416

[sys\_sflist\_append](group__flagged-single-linked-list__apis.md#ga77733972e39b7db9fc3dcc998261fb2d)

static void sys\_sflist\_append(sys\_sflist\_t \*list, sys\_sfnode\_t \*node)

Append a node to the given list.

**Definition** sflist.h:386

[sys\_sflist\_prepend](group__flagged-single-linked-list__apis.md#ga824ff283c821b6f392ebd81516b65712)

static void sys\_sflist\_prepend(sys\_sflist\_t \*list, sys\_sfnode\_t \*node)

Prepend a node to the given list.

**Definition** sflist.h:373

[sys\_sfnode\_flags\_set](group__flagged-single-linked-list__apis.md#ga85d82a3a5927f79a5f5655cb3405ce95)

static void sys\_sfnode\_flags\_set(sys\_sfnode\_t \*node, uint8\_t flags)

Set flags value for an sflist node.

**Definition** sflist.h:317

[sys\_sflist\_insert](group__flagged-single-linked-list__apis.md#ga8983c5704eb149b0941f1fb19f79b8c1)

static void sys\_sflist\_insert(sys\_sflist\_t \*list, sys\_sfnode\_t \*prev, sys\_sfnode\_t \*node)

Insert a node to the given list.

**Definition** sflist.h:431

[sys\_sflist\_peek\_tail](group__flagged-single-linked-list__apis.md#ga89f8bbced2992a84bae32db74e544788)

static sys\_sfnode\_t \* sys\_sflist\_peek\_tail(const sys\_sflist\_t \*list)

Peek the last node from the list.

**Definition** sflist.h:265

[sys\_sflist\_init](group__flagged-single-linked-list__apis.md#ga9597045ad20485fd88a0fec83fe1ffe1)

static void sys\_sflist\_init(sys\_sflist\_t \*list)

Initialize a list.

**Definition** sflist.h:204

[sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66)

struct \_sflist sys\_sflist\_t

Flagged single-linked list structure.

**Definition** sflist.h:54

[sys\_sflist\_peek\_head](group__flagged-single-linked-list__apis.md#gaa21d0f39228534840c81ac518c82541c)

static sys\_sfnode\_t \* sys\_sflist\_peek\_head(const sys\_sflist\_t \*list)

Peek the first node from the list.

**Definition** sflist.h:253

[sys\_sflist\_peek\_next](group__flagged-single-linked-list__apis.md#gaa9013d3a0b241dc63d038f49f822c0f8)

static sys\_sfnode\_t \* sys\_sflist\_peek\_next(const sys\_sfnode\_t \*node)

Peek the next node from current node.

**Definition** sflist.h:360

[sys\_sflist\_append\_list](group__flagged-single-linked-list__apis.md#gaaf9512d6c4432f34347771c9887e678a)

static void sys\_sflist\_append\_list(sys\_sflist\_t \*list, void \*head, void \*tail)

Append a list to the given list.

**Definition** sflist.h:402

[sys\_sfnode\_flags\_get](group__flagged-single-linked-list__apis.md#gac37d689834e258c4f113204f574c1c9c)

static uint8\_t sys\_sfnode\_flags\_get(const sys\_sfnode\_t \*node)

Fetch flags value for a particular sfnode.

**Definition** sflist.h:281

[sys\_sflist\_find\_and\_remove](group__flagged-single-linked-list__apis.md#gad66348fe7677cca76a547e09c8354322)

static bool sys\_sflist\_find\_and\_remove(sys\_sflist\_t \*list, sys\_sfnode\_t \*node)

Find and remove a node from a list.

**Definition** sflist.h:489

[sys\_sfnode\_init](group__flagged-single-linked-list__apis.md#gae56469b67ad7a92363d04ac726e326ea)

static void sys\_sfnode\_init(sys\_sfnode\_t \*node, uint8\_t flags)

Initialize an sflist node.

**Definition** sflist.h:300

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[list\_gen.h](list__gen_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [sflist.h](sflist_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
