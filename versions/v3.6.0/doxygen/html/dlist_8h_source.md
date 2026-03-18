---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dlist_8h_source.html
original_path: doxygen/html/dlist_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dlist.h

[Go to the documentation of this file.](dlist_8h.md)

1/\*

2 \* Copyright (c) 2013-2015 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

24

25#ifndef ZEPHYR\_INCLUDE\_SYS\_DLIST\_H\_

26#define ZEPHYR\_INCLUDE\_SYS\_DLIST\_H\_

27

28#include <stddef.h>

29#include <[stdbool.h](stdbool_8h.md)>

30#include <[zephyr/toolchain.h](toolchain_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

36

37struct \_dnode {

38 union {

39 struct \_dnode \*head; /\* ptr to head of list (sys\_dlist\_t) \*/

40 struct \_dnode \*next; /\* ptr to next node (sys\_dnode\_t) \*/

41 };

42 union {

43 struct \_dnode \*tail; /\* ptr to tail of list (sys\_dlist\_t) \*/

44 struct \_dnode \*prev; /\* ptr to previous node (sys\_dnode\_t) \*/

45 };

46};

47

[ 51](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)typedef struct \_dnode [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683);

[ 55](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)typedef struct \_dnode [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98);

56

57

[ 73](group__doubly-linked-list__apis.md#ga3788b5bbd11acc885e7378800a8cf974)#define SYS\_DLIST\_FOR\_EACH\_NODE(\_\_dl, \_\_dn) \

74 for (\_\_dn = sys\_dlist\_peek\_head(\_\_dl); \_\_dn != NULL; \

75 \_\_dn = sys\_dlist\_peek\_next(\_\_dl, \_\_dn))

76

[ 97](group__doubly-linked-list__apis.md#ga2bda6ba927f32e1d0b71ad63781b9909)#define SYS\_DLIST\_ITERATE\_FROM\_NODE(\_\_dl, \_\_dn) \

98 for (\_\_dn = \_\_dn ? sys\_dlist\_peek\_next\_no\_check(\_\_dl, \_\_dn) \

99 : sys\_dlist\_peek\_head(\_\_dl); \

100 \_\_dn != NULL; \

101 \_\_dn = sys\_dlist\_peek\_next(\_\_dl, \_\_dn))

102

[ 119](group__doubly-linked-list__apis.md#ga21c5c7dc311eaba99f00fb2eeca736d9)#define SYS\_DLIST\_FOR\_EACH\_NODE\_SAFE(\_\_dl, \_\_dn, \_\_dns) \

120 for (\_\_dn = sys\_dlist\_peek\_head(\_\_dl), \

121 \_\_dns = sys\_dlist\_peek\_next(\_\_dl, \_\_dn); \

122 \_\_dn != NULL; \_\_dn = \_\_dns, \

123 \_\_dns = sys\_dlist\_peek\_next(\_\_dl, \_\_dn))

124

[ 133](group__doubly-linked-list__apis.md#ga33a8bf65e8095e3b4dcee0b005b79170)#define SYS\_DLIST\_CONTAINER(\_\_dn, \_\_cn, \_\_n) \

134 ((\_\_dn != NULL) ? CONTAINER\_OF(\_\_dn, \_\_typeof\_\_(\*\_\_cn), \_\_n) : NULL)

135

[ 142](group__doubly-linked-list__apis.md#ga6dc66f3e84d3b79fef461d30b56a0f7c)#define SYS\_DLIST\_PEEK\_HEAD\_CONTAINER(\_\_dl, \_\_cn, \_\_n) \

143 SYS\_DLIST\_CONTAINER(sys\_dlist\_peek\_head(\_\_dl), \_\_cn, \_\_n)

144

[ 152](group__doubly-linked-list__apis.md#gaffb72234c90286ecf382b93d4db50a19)#define SYS\_DLIST\_PEEK\_NEXT\_CONTAINER(\_\_dl, \_\_cn, \_\_n) \

153 ((\_\_cn != NULL) ? \

154 SYS\_DLIST\_CONTAINER(sys\_dlist\_peek\_next(\_\_dl, &(\_\_cn->\_\_n)), \

155 \_\_cn, \_\_n) : NULL)

156

[ 171](group__doubly-linked-list__apis.md#gaf9eeb36eef731248c2f57c603feb1b20)#define SYS\_DLIST\_FOR\_EACH\_CONTAINER(\_\_dl, \_\_cn, \_\_n) \

172 for (\_\_cn = SYS\_DLIST\_PEEK\_HEAD\_CONTAINER(\_\_dl, \_\_cn, \_\_n); \

173 \_\_cn != NULL; \

174 \_\_cn = SYS\_DLIST\_PEEK\_NEXT\_CONTAINER(\_\_dl, \_\_cn, \_\_n))

175

[ 191](group__doubly-linked-list__apis.md#gaf07e09986c950b0dd1a0c89d4348f858)#define SYS\_DLIST\_FOR\_EACH\_CONTAINER\_SAFE(\_\_dl, \_\_cn, \_\_cns, \_\_n) \

192 for (\_\_cn = SYS\_DLIST\_PEEK\_HEAD\_CONTAINER(\_\_dl, \_\_cn, \_\_n), \

193 \_\_cns = SYS\_DLIST\_PEEK\_NEXT\_CONTAINER(\_\_dl, \_\_cn, \_\_n); \

194 \_\_cn != NULL; \_\_cn = \_\_cns, \

195 \_\_cns = SYS\_DLIST\_PEEK\_NEXT\_CONTAINER(\_\_dl, \_\_cn, \_\_n))

196

202

[ 203](group__doubly-linked-list__apis.md#gaf05dbc7d7250990b971796300aaf6c53)static inline void [sys\_dlist\_init](group__doubly-linked-list__apis.md#gaf05dbc7d7250990b971796300aaf6c53)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

204{

205 list->head = ([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*)list;

206 list->tail = ([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*)list;

207}

208

[ 212](group__doubly-linked-list__apis.md#ga3681d4600f9cbd9237ea9ce6f67e508d)#define SYS\_DLIST\_STATIC\_INIT(ptr\_to\_list) { {(ptr\_to\_list)}, {(ptr\_to\_list)} }

213

219

[ 220](group__doubly-linked-list__apis.md#gadf15b39af330221921d24505280e7a32)static inline void [sys\_dnode\_init](group__doubly-linked-list__apis.md#gadf15b39af330221921d24505280e7a32)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

221{

222 node->next = NULL;

223 node->prev = NULL;

224}

225

233

[ 234](group__doubly-linked-list__apis.md#gac725da0c7e65c126a96a9405af84ca41)static inline bool [sys\_dnode\_is\_linked](group__doubly-linked-list__apis.md#gac725da0c7e65c126a96a9405af84ca41)(const [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

235{

236 return node->next != NULL;

237}

238

247

[ 248](group__doubly-linked-list__apis.md#ga78a2c3d2272ee91578eafbfba3840af4)static inline bool [sys\_dlist\_is\_head](group__doubly-linked-list__apis.md#ga78a2c3d2272ee91578eafbfba3840af4)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

249{

250 return list->head == node;

251}

252

261

[ 262](group__doubly-linked-list__apis.md#ga38b8cad6cd6535c8ddc65d623fa967db)static inline bool [sys\_dlist\_is\_tail](group__doubly-linked-list__apis.md#ga38b8cad6cd6535c8ddc65d623fa967db)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

263{

264 return list->tail == node;

265}

266

274

[ 275](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)static inline bool [sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

276{

277 return list->head == list;

278}

279

289

[ 290](group__doubly-linked-list__apis.md#ga05b1ed491829b98de0200eca523b7829)static inline bool [sys\_dlist\_has\_multiple\_nodes](group__doubly-linked-list__apis.md#ga05b1ed491829b98de0200eca523b7829)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

291{

292 return list->head != list->tail;

293}

294

302

[ 303](group__doubly-linked-list__apis.md#ga6fc11e4682311b6b368d849e1e421183)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_head](group__doubly-linked-list__apis.md#ga6fc11e4682311b6b368d849e1e421183)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

304{

305 return [sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)(list) ? NULL : list->head;

306}

307

317

[ 318](group__doubly-linked-list__apis.md#ga7196173f9d59400b52163c2850a22fee)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_head\_not\_empty](group__doubly-linked-list__apis.md#ga7196173f9d59400b52163c2850a22fee)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

319{

320 return list->head;

321}

322

333

[ 334](group__doubly-linked-list__apis.md#ga84863ceb4ef678a9d3500d0e876e6afb)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_next\_no\_check](group__doubly-linked-list__apis.md#ga84863ceb4ef678a9d3500d0e876e6afb)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list,

335 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

336{

337 return (node == list->tail) ? NULL : node->next;

338}

339

349

[ 350](group__doubly-linked-list__apis.md#ga76366019520dc4c2ce2735cf747c1a22)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_next](group__doubly-linked-list__apis.md#ga76366019520dc4c2ce2735cf747c1a22)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list,

351 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

352{

353 return (node != NULL) ? [sys\_dlist\_peek\_next\_no\_check](group__doubly-linked-list__apis.md#ga84863ceb4ef678a9d3500d0e876e6afb)(list, node) : NULL;

354}

355

367

[ 368](group__doubly-linked-list__apis.md#ga806259b974b7ea6e42feaeab3987f140)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_prev\_no\_check](group__doubly-linked-list__apis.md#ga806259b974b7ea6e42feaeab3987f140)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list,

369 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

370{

371 return (node == list->head) ? NULL : node->prev;

372}

373

384

[ 385](group__doubly-linked-list__apis.md#ga23b9f6a10a14c08ccf1fbb7d8518fc43)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_prev](group__doubly-linked-list__apis.md#ga23b9f6a10a14c08ccf1fbb7d8518fc43)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list,

386 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

387{

388 return (node != NULL) ? [sys\_dlist\_peek\_prev\_no\_check](group__doubly-linked-list__apis.md#ga806259b974b7ea6e42feaeab3987f140)(list, node) : NULL;

389}

390

398

[ 399](group__doubly-linked-list__apis.md#gac84d0d3aade5677f7840f51f3c65c095)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_tail](group__doubly-linked-list__apis.md#gac84d0d3aade5677f7840f51f3c65c095)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

400{

401 return [sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)(list) ? NULL : list->tail;

402}

403

412

[ 413](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3)static inline void [sys\_dlist\_append](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

414{

415 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const tail = list->tail;

416

417 node->next = list;

418 node->prev = tail;

419

420 tail->next = node;

421 list->tail = node;

422}

423

432

[ 433](group__doubly-linked-list__apis.md#ga6f21ba50e0de93f54bfefeaabe0c767f)static inline void [sys\_dlist\_prepend](group__doubly-linked-list__apis.md#ga6f21ba50e0de93f54bfefeaabe0c767f)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

434{

435 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const head = list->head;

436

437 node->next = head;

438 node->prev = list;

439

440 head->prev = node;

441 list->head = node;

442}

443

[ 452](group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071)static inline void [sys\_dlist\_insert](group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*successor, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

453{

454 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const prev = successor->prev;

455

456 node->prev = prev;

457 node->next = successor;

458 prev->next = node;

459 successor->prev = node;

460}

461

476

[ 477](group__doubly-linked-list__apis.md#ga667cee0bdd59d8ca3fc82a5bca2bcd48)static inline void [sys\_dlist\_insert\_at](group__doubly-linked-list__apis.md#ga667cee0bdd59d8ca3fc82a5bca2bcd48)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node,

478 int (\*cond)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node, void \*data), void \*data)

479{

480 if ([sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)(list)) {

481 [sys\_dlist\_append](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3)(list, node);

482 } else {

483 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*pos = [sys\_dlist\_peek\_head](group__doubly-linked-list__apis.md#ga6fc11e4682311b6b368d849e1e421183)(list);

484

485 while ((pos != NULL) && (cond(pos, data) == 0)) {

486 pos = [sys\_dlist\_peek\_next](group__doubly-linked-list__apis.md#ga76366019520dc4c2ce2735cf747c1a22)(list, pos);

487 }

488 if (pos != NULL) {

489 [sys\_dlist\_insert](group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071)(pos, node);

490 } else {

491 [sys\_dlist\_append](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3)(list, node);

492 }

493 }

494}

495

504

[ 505](group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e)static inline void [sys\_dlist\_remove](group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

506{

507 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const prev = node->prev;

508 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const next = node->next;

509

510 prev->next = next;

511 next->prev = prev;

512 [sys\_dnode\_init](group__doubly-linked-list__apis.md#gadf15b39af330221921d24505280e7a32)(node);

513}

514

524

[ 525](group__doubly-linked-list__apis.md#ga3032394541494771f980e7642ecbc287)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_get](group__doubly-linked-list__apis.md#ga3032394541494771f980e7642ecbc287)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

526{

527 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node = NULL;

528

529 if (![sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)(list)) {

530 node = list->head;

531 [sys\_dlist\_remove](group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e)(node);

532 }

533

534 return node;

535}

536

[ 544](group__doubly-linked-list__apis.md#ga9418e906cc333b6a57b092487592c563)static inline size\_t [sys\_dlist\_len](group__doubly-linked-list__apis.md#ga9418e906cc333b6a57b092487592c563)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

545{

546 size\_t len = 0;

547 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node = NULL;

548

549 [SYS\_DLIST\_FOR\_EACH\_NODE](group__doubly-linked-list__apis.md#ga3788b5bbd11acc885e7378800a8cf974)(list, node) {

550 len++;

551 }

552 return len;

553}

554

556

557#ifdef \_\_cplusplus

558}

559#endif

560

561#endif /\* ZEPHYR\_INCLUDE\_SYS\_DLIST\_H\_ \*/

[sys\_dlist\_has\_multiple\_nodes](group__doubly-linked-list__apis.md#ga05b1ed491829b98de0200eca523b7829)

static bool sys\_dlist\_has\_multiple\_nodes(sys\_dlist\_t \*list)

check if more than one node present

**Definition** dlist.h:290

[sys\_dlist\_remove](group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e)

static void sys\_dlist\_remove(sys\_dnode\_t \*node)

remove a specific node from a list

**Definition** dlist.h:505

[sys\_dlist\_append](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3)

static void sys\_dlist\_append(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

add node to tail of list

**Definition** dlist.h:413

[sys\_dlist\_peek\_prev](group__doubly-linked-list__apis.md#ga23b9f6a10a14c08ccf1fbb7d8518fc43)

static sys\_dnode\_t \* sys\_dlist\_peek\_prev(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

get a reference to the previous item in the list

**Definition** dlist.h:385

[sys\_dlist\_get](group__doubly-linked-list__apis.md#ga3032394541494771f980e7642ecbc287)

static sys\_dnode\_t \* sys\_dlist\_get(sys\_dlist\_t \*list)

get the first node in a list

**Definition** dlist.h:525

[SYS\_DLIST\_FOR\_EACH\_NODE](group__doubly-linked-list__apis.md#ga3788b5bbd11acc885e7378800a8cf974)

#define SYS\_DLIST\_FOR\_EACH\_NODE(\_\_dl, \_\_dn)

Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_dn should not be remov...

**Definition** dlist.h:73

[sys\_dlist\_is\_tail](group__doubly-linked-list__apis.md#ga38b8cad6cd6535c8ddc65d623fa967db)

static bool sys\_dlist\_is\_tail(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

check if a node is the list's tail

**Definition** dlist.h:262

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:55

[sys\_dlist\_insert\_at](group__doubly-linked-list__apis.md#ga667cee0bdd59d8ca3fc82a5bca2bcd48)

static void sys\_dlist\_insert\_at(sys\_dlist\_t \*list, sys\_dnode\_t \*node, int(\*cond)(sys\_dnode\_t \*node, void \*data), void \*data)

insert node at position

**Definition** dlist.h:477

[sys\_dlist\_prepend](group__doubly-linked-list__apis.md#ga6f21ba50e0de93f54bfefeaabe0c767f)

static void sys\_dlist\_prepend(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

add node to head of list

**Definition** dlist.h:433

[sys\_dlist\_peek\_head](group__doubly-linked-list__apis.md#ga6fc11e4682311b6b368d849e1e421183)

static sys\_dnode\_t \* sys\_dlist\_peek\_head(sys\_dlist\_t \*list)

get a reference to the head item in the list

**Definition** dlist.h:303

[sys\_dlist\_peek\_head\_not\_empty](group__doubly-linked-list__apis.md#ga7196173f9d59400b52163c2850a22fee)

static sys\_dnode\_t \* sys\_dlist\_peek\_head\_not\_empty(sys\_dlist\_t \*list)

get a reference to the head item in the list

**Definition** dlist.h:318

[sys\_dlist\_peek\_next](group__doubly-linked-list__apis.md#ga76366019520dc4c2ce2735cf747c1a22)

static sys\_dnode\_t \* sys\_dlist\_peek\_next(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

get a reference to the next item in the list

**Definition** dlist.h:350

[sys\_dlist\_is\_head](group__doubly-linked-list__apis.md#ga78a2c3d2272ee91578eafbfba3840af4)

static bool sys\_dlist\_is\_head(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

check if a node is the list's head

**Definition** dlist.h:248

[sys\_dlist\_peek\_prev\_no\_check](group__doubly-linked-list__apis.md#ga806259b974b7ea6e42feaeab3987f140)

static sys\_dnode\_t \* sys\_dlist\_peek\_prev\_no\_check(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

get a reference to the previous item in the list, node is not NULL

**Definition** dlist.h:368

[sys\_dlist\_peek\_next\_no\_check](group__doubly-linked-list__apis.md#ga84863ceb4ef678a9d3500d0e876e6afb)

static sys\_dnode\_t \* sys\_dlist\_peek\_next\_no\_check(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

get a reference to the next item in the list, node is not NULL

**Definition** dlist.h:334

[sys\_dlist\_len](group__doubly-linked-list__apis.md#ga9418e906cc333b6a57b092487592c563)

static size\_t sys\_dlist\_len(sys\_dlist\_t \*list)

Compute the size of the given list in O(n) time.

**Definition** dlist.h:544

[sys\_dlist\_insert](group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071)

static void sys\_dlist\_insert(sys\_dnode\_t \*successor, sys\_dnode\_t \*node)

Insert a node into a list.

**Definition** dlist.h:452

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:51

[sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)

static bool sys\_dlist\_is\_empty(sys\_dlist\_t \*list)

check if the list is empty

**Definition** dlist.h:275

[sys\_dnode\_is\_linked](group__doubly-linked-list__apis.md#gac725da0c7e65c126a96a9405af84ca41)

static bool sys\_dnode\_is\_linked(const sys\_dnode\_t \*node)

check if a node is a member of any list

**Definition** dlist.h:234

[sys\_dlist\_peek\_tail](group__doubly-linked-list__apis.md#gac84d0d3aade5677f7840f51f3c65c095)

static sys\_dnode\_t \* sys\_dlist\_peek\_tail(sys\_dlist\_t \*list)

get a reference to the tail item in the list

**Definition** dlist.h:399

[sys\_dnode\_init](group__doubly-linked-list__apis.md#gadf15b39af330221921d24505280e7a32)

static void sys\_dnode\_init(sys\_dnode\_t \*node)

initialize node to its state when not in a list

**Definition** dlist.h:220

[sys\_dlist\_init](group__doubly-linked-list__apis.md#gaf05dbc7d7250990b971796300aaf6c53)

static void sys\_dlist\_init(sys\_dlist\_t \*list)

initialize list to its empty state

**Definition** dlist.h:203

[stdbool.h](stdbool_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [dlist.h](dlist_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
