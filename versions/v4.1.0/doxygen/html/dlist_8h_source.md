---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dlist_8h_source.html
original_path: doxygen/html/dlist_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

35

36struct \_dnode {

37 union {

38 struct \_dnode \*head; /\* ptr to head of list (sys\_dlist\_t) \*/

39 struct \_dnode \*next; /\* ptr to next node (sys\_dnode\_t) \*/

40 };

41 union {

42 struct \_dnode \*tail; /\* ptr to tail of list (sys\_dlist\_t) \*/

43 struct \_dnode \*prev; /\* ptr to previous node (sys\_dnode\_t) \*/

44 };

45};

46

[ 50](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)typedef struct \_dnode [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683);

[ 54](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)typedef struct \_dnode [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98);

55

56

[ 72](group__doubly-linked-list__apis.md#ga3788b5bbd11acc885e7378800a8cf974)#define SYS\_DLIST\_FOR\_EACH\_NODE(\_\_dl, \_\_dn) \

73 for (\_\_dn = sys\_dlist\_peek\_head(\_\_dl); \_\_dn != NULL; \

74 \_\_dn = sys\_dlist\_peek\_next(\_\_dl, \_\_dn))

75

[ 96](group__doubly-linked-list__apis.md#ga2bda6ba927f32e1d0b71ad63781b9909)#define SYS\_DLIST\_ITERATE\_FROM\_NODE(\_\_dl, \_\_dn) \

97 for (\_\_dn = \_\_dn ? sys\_dlist\_peek\_next\_no\_check(\_\_dl, \_\_dn) \

98 : sys\_dlist\_peek\_head(\_\_dl); \

99 \_\_dn != NULL; \

100 \_\_dn = sys\_dlist\_peek\_next(\_\_dl, \_\_dn))

101

[ 118](group__doubly-linked-list__apis.md#ga21c5c7dc311eaba99f00fb2eeca736d9)#define SYS\_DLIST\_FOR\_EACH\_NODE\_SAFE(\_\_dl, \_\_dn, \_\_dns) \

119 for ((\_\_dn) = sys\_dlist\_peek\_head(\_\_dl), \

120 (\_\_dns) = sys\_dlist\_peek\_next((\_\_dl), (\_\_dn)); \

121 (\_\_dn) != NULL; (\_\_dn) = (\_\_dns), \

122 (\_\_dns) = sys\_dlist\_peek\_next(\_\_dl, \_\_dn))

123

[ 132](group__doubly-linked-list__apis.md#ga33a8bf65e8095e3b4dcee0b005b79170)#define SYS\_DLIST\_CONTAINER(\_\_dn, \_\_cn, \_\_n) \

133 (((\_\_dn) != NULL) ? CONTAINER\_OF(\_\_dn, \_\_typeof\_\_(\*(\_\_cn)), \_\_n) : NULL)

134

[ 141](group__doubly-linked-list__apis.md#ga6dc66f3e84d3b79fef461d30b56a0f7c)#define SYS\_DLIST\_PEEK\_HEAD\_CONTAINER(\_\_dl, \_\_cn, \_\_n) \

142 SYS\_DLIST\_CONTAINER(sys\_dlist\_peek\_head(\_\_dl), \_\_cn, \_\_n)

143

[ 151](group__doubly-linked-list__apis.md#gaffb72234c90286ecf382b93d4db50a19)#define SYS\_DLIST\_PEEK\_NEXT\_CONTAINER(\_\_dl, \_\_cn, \_\_n) \

152 (((\_\_cn) != NULL) ? \

153 SYS\_DLIST\_CONTAINER(sys\_dlist\_peek\_next((\_\_dl), &((\_\_cn)->\_\_n)), \

154 \_\_cn, \_\_n) : NULL)

155

[ 170](group__doubly-linked-list__apis.md#gaf9eeb36eef731248c2f57c603feb1b20)#define SYS\_DLIST\_FOR\_EACH\_CONTAINER(\_\_dl, \_\_cn, \_\_n) \

171 for ((\_\_cn) = SYS\_DLIST\_PEEK\_HEAD\_CONTAINER(\_\_dl, \_\_cn, \_\_n); \

172 (\_\_cn) != NULL; \

173 (\_\_cn) = SYS\_DLIST\_PEEK\_NEXT\_CONTAINER(\_\_dl, \_\_cn, \_\_n))

174

[ 190](group__doubly-linked-list__apis.md#gaf07e09986c950b0dd1a0c89d4348f858)#define SYS\_DLIST\_FOR\_EACH\_CONTAINER\_SAFE(\_\_dl, \_\_cn, \_\_cns, \_\_n) \

191 for ((\_\_cn) = SYS\_DLIST\_PEEK\_HEAD\_CONTAINER(\_\_dl, \_\_cn, \_\_n), \

192 (\_\_cns) = SYS\_DLIST\_PEEK\_NEXT\_CONTAINER(\_\_dl, \_\_cn, \_\_n); \

193 (\_\_cn) != NULL; (\_\_cn) = (\_\_cns), \

194 (\_\_cns) = SYS\_DLIST\_PEEK\_NEXT\_CONTAINER(\_\_dl, \_\_cn, \_\_n))

195

201

[ 202](group__doubly-linked-list__apis.md#gaf05dbc7d7250990b971796300aaf6c53)static inline void [sys\_dlist\_init](group__doubly-linked-list__apis.md#gaf05dbc7d7250990b971796300aaf6c53)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

203{

204 list->head = ([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*)list;

205 list->tail = ([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*)list;

206}

207

[ 211](group__doubly-linked-list__apis.md#ga3681d4600f9cbd9237ea9ce6f67e508d)#define SYS\_DLIST\_STATIC\_INIT(ptr\_to\_list) { {(ptr\_to\_list)}, {(ptr\_to\_list)} }

212

218

[ 219](group__doubly-linked-list__apis.md#gadf15b39af330221921d24505280e7a32)static inline void [sys\_dnode\_init](group__doubly-linked-list__apis.md#gadf15b39af330221921d24505280e7a32)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

220{

221 node->next = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

222 node->prev = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

223}

224

232

[ 233](group__doubly-linked-list__apis.md#gac725da0c7e65c126a96a9405af84ca41)static inline bool [sys\_dnode\_is\_linked](group__doubly-linked-list__apis.md#gac725da0c7e65c126a96a9405af84ca41)(const [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

234{

235 return node->next != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

236}

237

246

[ 247](group__doubly-linked-list__apis.md#ga78a2c3d2272ee91578eafbfba3840af4)static inline bool [sys\_dlist\_is\_head](group__doubly-linked-list__apis.md#ga78a2c3d2272ee91578eafbfba3840af4)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

248{

249 return list->head == node;

250}

251

260

[ 261](group__doubly-linked-list__apis.md#ga38b8cad6cd6535c8ddc65d623fa967db)static inline bool [sys\_dlist\_is\_tail](group__doubly-linked-list__apis.md#ga38b8cad6cd6535c8ddc65d623fa967db)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

262{

263 return list->tail == node;

264}

265

273

[ 274](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)static inline bool [sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

275{

276 return list->head == list;

277}

278

288

[ 289](group__doubly-linked-list__apis.md#ga05b1ed491829b98de0200eca523b7829)static inline bool [sys\_dlist\_has\_multiple\_nodes](group__doubly-linked-list__apis.md#ga05b1ed491829b98de0200eca523b7829)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

290{

291 return list->head != list->tail;

292}

293

301

[ 302](group__doubly-linked-list__apis.md#ga6fc11e4682311b6b368d849e1e421183)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_head](group__doubly-linked-list__apis.md#ga6fc11e4682311b6b368d849e1e421183)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

303{

304 return [sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)(list) ? [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) : list->head;

305}

306

316

[ 317](group__doubly-linked-list__apis.md#ga7196173f9d59400b52163c2850a22fee)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_head\_not\_empty](group__doubly-linked-list__apis.md#ga7196173f9d59400b52163c2850a22fee)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

318{

319 return list->head;

320}

321

332

[ 333](group__doubly-linked-list__apis.md#ga84863ceb4ef678a9d3500d0e876e6afb)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_next\_no\_check](group__doubly-linked-list__apis.md#ga84863ceb4ef678a9d3500d0e876e6afb)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list,

334 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

335{

336 return (node == list->tail) ? [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) : node->next;

337}

338

348

[ 349](group__doubly-linked-list__apis.md#ga76366019520dc4c2ce2735cf747c1a22)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_next](group__doubly-linked-list__apis.md#ga76366019520dc4c2ce2735cf747c1a22)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list,

350 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

351{

352 return (node != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) ? [sys\_dlist\_peek\_next\_no\_check](group__doubly-linked-list__apis.md#ga84863ceb4ef678a9d3500d0e876e6afb)(list, node) : [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

353}

354

366

[ 367](group__doubly-linked-list__apis.md#ga806259b974b7ea6e42feaeab3987f140)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_prev\_no\_check](group__doubly-linked-list__apis.md#ga806259b974b7ea6e42feaeab3987f140)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list,

368 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

369{

370 return (node == list->head) ? [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) : node->prev;

371}

372

383

[ 384](group__doubly-linked-list__apis.md#ga23b9f6a10a14c08ccf1fbb7d8518fc43)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_prev](group__doubly-linked-list__apis.md#ga23b9f6a10a14c08ccf1fbb7d8518fc43)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list,

385 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

386{

387 return (node != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) ? [sys\_dlist\_peek\_prev\_no\_check](group__doubly-linked-list__apis.md#ga806259b974b7ea6e42feaeab3987f140)(list, node) : [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

388}

389

397

[ 398](group__doubly-linked-list__apis.md#gac84d0d3aade5677f7840f51f3c65c095)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_peek\_tail](group__doubly-linked-list__apis.md#gac84d0d3aade5677f7840f51f3c65c095)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

399{

400 return [sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)(list) ? [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) : list->tail;

401}

402

411

[ 412](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3)static inline void [sys\_dlist\_append](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

413{

414 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const tail = list->tail;

415

416 node->next = list;

417 node->prev = tail;

418

419 tail->next = node;

420 list->tail = node;

421}

422

431

[ 432](group__doubly-linked-list__apis.md#ga6f21ba50e0de93f54bfefeaabe0c767f)static inline void [sys\_dlist\_prepend](group__doubly-linked-list__apis.md#ga6f21ba50e0de93f54bfefeaabe0c767f)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

433{

434 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const head = list->head;

435

436 node->next = head;

437 node->prev = list;

438

439 head->prev = node;

440 list->head = node;

441}

442

[ 451](group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071)static inline void [sys\_dlist\_insert](group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*successor, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

452{

453 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const prev = successor->prev;

454

455 node->prev = prev;

456 node->next = successor;

457 prev->next = node;

458 successor->prev = node;

459}

460

475

[ 476](group__doubly-linked-list__apis.md#ga667cee0bdd59d8ca3fc82a5bca2bcd48)static inline void [sys\_dlist\_insert\_at](group__doubly-linked-list__apis.md#ga667cee0bdd59d8ca3fc82a5bca2bcd48)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list, [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node,

477 int (\*cond)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node, void \*data), void \*data)

478{

479 if ([sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)(list)) {

480 [sys\_dlist\_append](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3)(list, node);

481 } else {

482 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*pos = [sys\_dlist\_peek\_head](group__doubly-linked-list__apis.md#ga6fc11e4682311b6b368d849e1e421183)(list);

483

484 while ((pos != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) && (cond(pos, data) == 0)) {

485 pos = [sys\_dlist\_peek\_next](group__doubly-linked-list__apis.md#ga76366019520dc4c2ce2735cf747c1a22)(list, pos);

486 }

487 if (pos != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

488 [sys\_dlist\_insert](group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071)(pos, node);

489 } else {

490 [sys\_dlist\_append](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3)(list, node);

491 }

492 }

493}

494

[ 509](group__doubly-linked-list__apis.md#gadf588e086301e31d70c4fc8de4b9d499)static inline void [sys\_dlist\_dequeue](group__doubly-linked-list__apis.md#gadf588e086301e31d70c4fc8de4b9d499)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

510{

511 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const prev = node->prev;

512 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const next = node->next;

513

514 prev->next = next;

515 next->prev = prev;

516}

517

526

[ 527](group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e)static inline void [sys\_dlist\_remove](group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e)([sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node)

528{

529 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const prev = node->prev;

530 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*const next = node->next;

531

532 prev->next = next;

533 next->prev = prev;

534 [sys\_dnode\_init](group__doubly-linked-list__apis.md#gadf15b39af330221921d24505280e7a32)(node);

535}

536

546

[ 547](group__doubly-linked-list__apis.md#ga3032394541494771f980e7642ecbc287)static inline [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[sys\_dlist\_get](group__doubly-linked-list__apis.md#ga3032394541494771f980e7642ecbc287)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

548{

549 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

550

551 if (![sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)(list)) {

552 node = list->head;

553 [sys\_dlist\_remove](group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e)(node);

554 }

555

556 return node;

557}

558

[ 566](group__doubly-linked-list__apis.md#ga9418e906cc333b6a57b092487592c563)static inline size\_t [sys\_dlist\_len](group__doubly-linked-list__apis.md#ga9418e906cc333b6a57b092487592c563)([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*list)

567{

568 size\_t len = 0;

569 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*node = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

570

571 [SYS\_DLIST\_FOR\_EACH\_NODE](group__doubly-linked-list__apis.md#ga3788b5bbd11acc885e7378800a8cf974)(list, node) {

572 len++;

573 }

574 return len;

575}

576

578

579#ifdef \_\_cplusplus

580}

581#endif

582

583#endif /\* ZEPHYR\_INCLUDE\_SYS\_DLIST\_H\_ \*/

[sys\_dlist\_has\_multiple\_nodes](group__doubly-linked-list__apis.md#ga05b1ed491829b98de0200eca523b7829)

static bool sys\_dlist\_has\_multiple\_nodes(sys\_dlist\_t \*list)

check if more than one node present

**Definition** dlist.h:289

[sys\_dlist\_remove](group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e)

static void sys\_dlist\_remove(sys\_dnode\_t \*node)

remove a specific node from a list

**Definition** dlist.h:527

[sys\_dlist\_append](group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3)

static void sys\_dlist\_append(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

add node to tail of list

**Definition** dlist.h:412

[sys\_dlist\_peek\_prev](group__doubly-linked-list__apis.md#ga23b9f6a10a14c08ccf1fbb7d8518fc43)

static sys\_dnode\_t \* sys\_dlist\_peek\_prev(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

get a reference to the previous item in the list

**Definition** dlist.h:384

[sys\_dlist\_get](group__doubly-linked-list__apis.md#ga3032394541494771f980e7642ecbc287)

static sys\_dnode\_t \* sys\_dlist\_get(sys\_dlist\_t \*list)

get the first node in a list

**Definition** dlist.h:547

[SYS\_DLIST\_FOR\_EACH\_NODE](group__doubly-linked-list__apis.md#ga3788b5bbd11acc885e7378800a8cf974)

#define SYS\_DLIST\_FOR\_EACH\_NODE(\_\_dl, \_\_dn)

Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_dn should not be remov...

**Definition** dlist.h:72

[sys\_dlist\_is\_tail](group__doubly-linked-list__apis.md#ga38b8cad6cd6535c8ddc65d623fa967db)

static bool sys\_dlist\_is\_tail(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

check if a node is the list's tail

**Definition** dlist.h:261

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:54

[sys\_dlist\_insert\_at](group__doubly-linked-list__apis.md#ga667cee0bdd59d8ca3fc82a5bca2bcd48)

static void sys\_dlist\_insert\_at(sys\_dlist\_t \*list, sys\_dnode\_t \*node, int(\*cond)(sys\_dnode\_t \*node, void \*data), void \*data)

insert node at position

**Definition** dlist.h:476

[sys\_dlist\_prepend](group__doubly-linked-list__apis.md#ga6f21ba50e0de93f54bfefeaabe0c767f)

static void sys\_dlist\_prepend(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

add node to head of list

**Definition** dlist.h:432

[sys\_dlist\_peek\_head](group__doubly-linked-list__apis.md#ga6fc11e4682311b6b368d849e1e421183)

static sys\_dnode\_t \* sys\_dlist\_peek\_head(sys\_dlist\_t \*list)

get a reference to the head item in the list

**Definition** dlist.h:302

[sys\_dlist\_peek\_head\_not\_empty](group__doubly-linked-list__apis.md#ga7196173f9d59400b52163c2850a22fee)

static sys\_dnode\_t \* sys\_dlist\_peek\_head\_not\_empty(sys\_dlist\_t \*list)

get a reference to the head item in the list

**Definition** dlist.h:317

[sys\_dlist\_peek\_next](group__doubly-linked-list__apis.md#ga76366019520dc4c2ce2735cf747c1a22)

static sys\_dnode\_t \* sys\_dlist\_peek\_next(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

get a reference to the next item in the list

**Definition** dlist.h:349

[sys\_dlist\_is\_head](group__doubly-linked-list__apis.md#ga78a2c3d2272ee91578eafbfba3840af4)

static bool sys\_dlist\_is\_head(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

check if a node is the list's head

**Definition** dlist.h:247

[sys\_dlist\_peek\_prev\_no\_check](group__doubly-linked-list__apis.md#ga806259b974b7ea6e42feaeab3987f140)

static sys\_dnode\_t \* sys\_dlist\_peek\_prev\_no\_check(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

get a reference to the previous item in the list, node is not NULL

**Definition** dlist.h:367

[sys\_dlist\_peek\_next\_no\_check](group__doubly-linked-list__apis.md#ga84863ceb4ef678a9d3500d0e876e6afb)

static sys\_dnode\_t \* sys\_dlist\_peek\_next\_no\_check(sys\_dlist\_t \*list, sys\_dnode\_t \*node)

get a reference to the next item in the list, node is not NULL

**Definition** dlist.h:333

[sys\_dlist\_len](group__doubly-linked-list__apis.md#ga9418e906cc333b6a57b092487592c563)

static size\_t sys\_dlist\_len(sys\_dlist\_t \*list)

Compute the size of the given list in O(n) time.

**Definition** dlist.h:566

[sys\_dlist\_insert](group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071)

static void sys\_dlist\_insert(sys\_dnode\_t \*successor, sys\_dnode\_t \*node)

Insert a node into a list.

**Definition** dlist.h:451

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:50

[sys\_dlist\_is\_empty](group__doubly-linked-list__apis.md#gaaa314b62d8d271071d5603075a961766)

static bool sys\_dlist\_is\_empty(sys\_dlist\_t \*list)

check if the list is empty

**Definition** dlist.h:274

[sys\_dnode\_is\_linked](group__doubly-linked-list__apis.md#gac725da0c7e65c126a96a9405af84ca41)

static bool sys\_dnode\_is\_linked(const sys\_dnode\_t \*node)

check if a node is a member of any list

**Definition** dlist.h:233

[sys\_dlist\_peek\_tail](group__doubly-linked-list__apis.md#gac84d0d3aade5677f7840f51f3c65c095)

static sys\_dnode\_t \* sys\_dlist\_peek\_tail(sys\_dlist\_t \*list)

get a reference to the tail item in the list

**Definition** dlist.h:398

[sys\_dnode\_init](group__doubly-linked-list__apis.md#gadf15b39af330221921d24505280e7a32)

static void sys\_dnode\_init(sys\_dnode\_t \*node)

initialize node to its state when not in a list

**Definition** dlist.h:219

[sys\_dlist\_dequeue](group__doubly-linked-list__apis.md#gadf588e086301e31d70c4fc8de4b9d499)

static void sys\_dlist\_dequeue(sys\_dnode\_t \*node)

remove a specific node from a list

**Definition** dlist.h:509

[sys\_dlist\_init](group__doubly-linked-list__apis.md#gaf05dbc7d7250990b971796300aaf6c53)

static void sys\_dlist\_init(sys\_dlist\_t \*list)

initialize list to its empty state

**Definition** dlist.h:202

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [dlist.h](dlist_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
