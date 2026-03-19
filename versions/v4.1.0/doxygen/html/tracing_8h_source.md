---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tracing_8h_source.html
original_path: doxygen/html/tracing_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tracing.h

[Go to the documentation of this file.](tracing_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_TRACING\_TRACING\_H\_

7#define ZEPHYR\_INCLUDE\_TRACING\_TRACING\_H\_

8

9#include <[zephyr/kernel.h](kernel_8h.md)>

10

11#include "[tracking.h](tracking_8h.md)"

12

13#if defined CONFIG\_SEGGER\_SYSTEMVIEW

14#include "tracing\_sysview.h"

15#elif defined CONFIG\_TRACING\_CTF

16#include "tracing\_ctf.h"

17#elif defined CONFIG\_TRACING\_TEST

18#include "tracing\_test.h"

19#elif defined CONFIG\_TRACING\_USER

20#include "tracing\_user.h"

21#else

33

39

45

[ 49](group__subsys__tracing__apis__thread.md#ga05f9560547bb1415c809d718f9bd03c8)#define sys\_port\_trace\_k\_thread\_foreach\_enter()

50

[ 54](group__subsys__tracing__apis__thread.md#ga0848db275a35dd5f840221d2a91d75fb)#define sys\_port\_trace\_k\_thread\_foreach\_exit()

55

[ 59](group__subsys__tracing__apis__thread.md#gaf1136b18d6408da4fd9b1e8d767e390d)#define sys\_port\_trace\_k\_thread\_foreach\_unlocked\_enter()

60

[ 64](group__subsys__tracing__apis__thread.md#gaa6f8160940e24df5483268949d0ca402)#define sys\_port\_trace\_k\_thread\_foreach\_unlocked\_exit()

65

[ 70](group__subsys__tracing__apis__thread.md#ga6140a4ec9c7b31d907b08793deb44ca7)#define sys\_port\_trace\_k\_thread\_create(new\_thread)

71

[ 75](group__subsys__tracing__apis__thread.md#ga4ca28fdba0a95bcceddadba86412f736)#define sys\_port\_trace\_k\_thread\_user\_mode\_enter()

76

[ 82](group__subsys__tracing__apis__thread.md#gabbad785e65db935917e4f1224893c9c1)#define sys\_port\_trace\_k\_thread\_join\_enter(thread, timeout)

83

[ 89](group__subsys__tracing__apis__thread.md#ga057858c554e988474ae0097dc1ccf83f)#define sys\_port\_trace\_k\_thread\_join\_blocking(thread, timeout)

90

[ 97](group__subsys__tracing__apis__thread.md#gabf77c5d93899ee85b4b4edd0c4c18490)#define sys\_port\_trace\_k\_thread\_join\_exit(thread, timeout, ret)

98

[ 103](group__subsys__tracing__apis__thread.md#ga44cac2602a3b638fbf04eb0322b33736)#define sys\_port\_trace\_k\_thread\_sleep\_enter(timeout)

104

[ 110](group__subsys__tracing__apis__thread.md#ga91f7abaae3dcd7eec7ee001f8653cda6)#define sys\_port\_trace\_k\_thread\_sleep\_exit(timeout, ret)

111

[ 116](group__subsys__tracing__apis__thread.md#ga9bd09050cedc7213b90d486dc672d6d6)#define sys\_port\_trace\_k\_thread\_msleep\_enter(ms)

117

[ 123](group__subsys__tracing__apis__thread.md#ga625bde038098aa8170e80205b4f3a15c)#define sys\_port\_trace\_k\_thread\_msleep\_exit(ms, ret)

124

[ 129](group__subsys__tracing__apis__thread.md#ga55a7f87fac6b2a7eff7f18ba1ffa1559)#define sys\_port\_trace\_k\_thread\_usleep\_enter(us)

130

[ 136](group__subsys__tracing__apis__thread.md#ga41a7e55fa70047d242ebe403d3baa15a)#define sys\_port\_trace\_k\_thread\_usleep\_exit(us, ret)

137

[ 142](group__subsys__tracing__apis__thread.md#gada94114ae74457c1082f2453d6fd9be5)#define sys\_port\_trace\_k\_thread\_busy\_wait\_enter(usec\_to\_wait)

143

[ 148](group__subsys__tracing__apis__thread.md#gaf8d4d01e8e662c9255f925ba64cdbd31)#define sys\_port\_trace\_k\_thread\_busy\_wait\_exit(usec\_to\_wait)

149

[ 153](group__subsys__tracing__apis__thread.md#ga24f6d9958154d7e424a1af95e59e797f)#define sys\_port\_trace\_k\_thread\_yield()

154

[ 159](group__subsys__tracing__apis__thread.md#ga1676b0fe2f2b19bef646e73f129089db)#define sys\_port\_trace\_k\_thread\_wakeup(thread)

160

[ 165](group__subsys__tracing__apis__thread.md#ga097debbc4ba4f332a2728ad04152df1a)#define sys\_port\_trace\_k\_thread\_start(thread)

166

[ 171](group__subsys__tracing__apis__thread.md#gab0b43ffbe1ab9bb1ce962bab6c55c911)#define sys\_port\_trace\_k\_thread\_abort(thread)

172

[ 177](group__subsys__tracing__apis__thread.md#ga3d147d97bbca426b7f74f1418c6ff16b)#define sys\_port\_trace\_k\_thread\_abort\_enter(thread)

178

[ 183](group__subsys__tracing__apis__thread.md#ga3e7c042978bd25ea41ed48addc3259bf)#define sys\_port\_trace\_k\_thread\_abort\_exit(thread)

184

[ 189](group__subsys__tracing__apis__thread.md#ga09ddf88b7d825dd02db8a1058dda66eb)#define sys\_port\_trace\_k\_thread\_priority\_set(thread)

190

[ 196](group__subsys__tracing__apis__thread.md#ga63bf5f0162d8596beae754cd614e2452)#define sys\_port\_trace\_k\_thread\_suspend\_enter(thread)

197

[ 203](group__subsys__tracing__apis__thread.md#gaedc07c84df5eb7d4cbdf86560ec72bdd)#define sys\_port\_trace\_k\_thread\_suspend\_exit(thread)

204

[ 210](group__subsys__tracing__apis__thread.md#gaa04064835552055fc5c0d808a38cdc41)#define sys\_port\_trace\_k\_thread\_resume\_enter(thread)

211

[ 217](group__subsys__tracing__apis__thread.md#ga38841a0e40592e49de6a24690905388e)#define sys\_port\_trace\_k\_thread\_resume\_exit(thread)

218

[ 222](group__subsys__tracing__apis__thread.md#gadbd1fcca37d68a7a7b4c7061f3583764)#define sys\_port\_trace\_k\_thread\_sched\_lock()

223

[ 227](group__subsys__tracing__apis__thread.md#ga7d5ee7a2fd30678128def82112245741)#define sys\_port\_trace\_k\_thread\_sched\_unlock()

228

[ 234](group__subsys__tracing__apis__thread.md#ga31ef5d08ff84619432b2dda7d239c479)#define sys\_port\_trace\_k\_thread\_name\_set(thread, ret)

235

[ 239](group__subsys__tracing__apis__thread.md#ga61a5063e1543789c16add724fad5aef1)#define sys\_port\_trace\_k\_thread\_switched\_out()

240

[ 244](group__subsys__tracing__apis__thread.md#ga89f53bfff5816ea7a1e4128677254634)#define sys\_port\_trace\_k\_thread\_switched\_in()

245

[ 250](group__subsys__tracing__apis__thread.md#ga6fe6a019530b96e308c751d7c3732d83)#define sys\_port\_trace\_k\_thread\_ready(thread)

251

[ 256](group__subsys__tracing__apis__thread.md#ga0b19ca107363fd060183cbb7b83927e8)#define sys\_port\_trace\_k\_thread\_pend(thread)

257

[ 262](group__subsys__tracing__apis__thread.md#gaffe80c4e32e27089b4ccb99fd11205ea)#define sys\_port\_trace\_k\_thread\_info(thread)

263

[ 268](group__subsys__tracing__apis__thread.md#ga9f4b710eb3cc5ef0dabfadc9ad1cc448)#define sys\_port\_trace\_k\_thread\_sched\_wakeup(thread)

269

[ 274](group__subsys__tracing__apis__thread.md#gaa2213012f5c2650301f2467dc0e36e17)#define sys\_port\_trace\_k\_thread\_sched\_abort(thread)

275

[ 281](group__subsys__tracing__apis__thread.md#ga906c658681af75d52d228fef96a39a92)#define sys\_port\_trace\_k\_thread\_sched\_priority\_set(thread, prio)

282

[ 287](group__subsys__tracing__apis__thread.md#ga1f5990be25a0c0eb348d788e5aaf04cb)#define sys\_port\_trace\_k\_thread\_sched\_ready(thread)

288

[ 293](group__subsys__tracing__apis__thread.md#gae857728d8f72259b6d282cb0b0bdb2ca)#define sys\_port\_trace\_k\_thread\_sched\_pend(thread)

294

[ 299](group__subsys__tracing__apis__thread.md#ga81d84b861192fa664be54e7a77f0cea4)#define sys\_port\_trace\_k\_thread\_sched\_resume(thread)

300

[ 305](group__subsys__tracing__apis__thread.md#gaef5455dbd090fd7cf065d3fd8a8d3d1b)#define sys\_port\_trace\_k\_thread\_sched\_suspend(thread)

306 /\* end of subsys\_tracing\_apis\_thread \*/

308

314

[ 319](group__subsys__tracing__apis__work.md#gab31f3a43ff4a836a28ba0c21a24370e7)#define sys\_port\_trace\_k\_work\_init(work)

320

[ 326](group__subsys__tracing__apis__work.md#gac4ec7fb1a85aaf608d0b46734fabc812)#define sys\_port\_trace\_k\_work\_submit\_to\_queue\_enter(queue, work)

327

[ 334](group__subsys__tracing__apis__work.md#ga8807dc91f2f025f400a4e3a435b13588)#define sys\_port\_trace\_k\_work\_submit\_to\_queue\_exit(queue, work, ret)

335

[ 340](group__subsys__tracing__apis__work.md#ga597a2efeb4fc680149a51e7abceba2a7)#define sys\_port\_trace\_k\_work\_submit\_enter(work)

341

[ 347](group__subsys__tracing__apis__work.md#ga4996ec4ae496a2a55dd756f6e4474107)#define sys\_port\_trace\_k\_work\_submit\_exit(work, ret)

348

[ 353](group__subsys__tracing__apis__work.md#ga20f5d05e4c1be9a21e42072291272fc9)#define sys\_port\_trace\_k\_work\_flush\_enter(work)

354

[ 360](group__subsys__tracing__apis__work.md#gae21005546cf2025ac4eff76e09da4d0e)#define sys\_port\_trace\_k\_work\_flush\_blocking(work, timeout)

361

[ 367](group__subsys__tracing__apis__work.md#gaa50f5a34b4cdc0ba46a4d153f0d48b39)#define sys\_port\_trace\_k\_work\_flush\_exit(work, ret)

368

[ 373](group__subsys__tracing__apis__work.md#gaa2ffb1718ddc49a4f3a727e15d3e1f11)#define sys\_port\_trace\_k\_work\_cancel\_enter(work)

374

[ 380](group__subsys__tracing__apis__work.md#ga9a2aa3433ec4a0a2fceb8d1c5ce682f3)#define sys\_port\_trace\_k\_work\_cancel\_exit(work, ret)

381

[ 387](group__subsys__tracing__apis__work.md#ga8f2b37c2740c6883939a94ae6aa3ea51)#define sys\_port\_trace\_k\_work\_cancel\_sync\_enter(work, sync)

388

[ 394](group__subsys__tracing__apis__work.md#ga9d05cb22b905b5ae99174fe8523a8033)#define sys\_port\_trace\_k\_work\_cancel\_sync\_blocking(work, sync)

395

[ 402](group__subsys__tracing__apis__work.md#gae59b7476b056d828bbf269c3f60e5687)#define sys\_port\_trace\_k\_work\_cancel\_sync\_exit(work, sync, ret)

403 /\* end of subsys\_tracing\_apis\_work \*/

405

411

[ 416](group__subsys__tracing__apis__work__q.md#ga9e25524cb89a9cabd6ad70459e8bd641)#define sys\_port\_trace\_k\_work\_queue\_init(queue)

417

[ 422](group__subsys__tracing__apis__work__q.md#ga79eba7247bd2c52480ac09e6ecef8635)#define sys\_port\_trace\_k\_work\_queue\_start\_enter(queue)

423

[ 428](group__subsys__tracing__apis__work__q.md#gae25756a58b450b2d1e8c3475cbfc1758)#define sys\_port\_trace\_k\_work\_queue\_start\_exit(queue)

429

[ 435](group__subsys__tracing__apis__work__q.md#ga97f548366e687d22af6db208c754e6f8)#define sys\_port\_trace\_k\_work\_queue\_stop\_enter(queue, timeout)

436

[ 442](group__subsys__tracing__apis__work__q.md#gaf6c1bf6d59104b7382d0938cc2247b54)#define sys\_port\_trace\_k\_work\_queue\_stop\_blocking(queue, timeout)

443

[ 450](group__subsys__tracing__apis__work__q.md#ga3200afa981681bdd5b51c0aaecd04620)#define sys\_port\_trace\_k\_work\_queue\_stop\_exit(queue, timeout, ret)

451

[ 456](group__subsys__tracing__apis__work__q.md#ga88af757f4867f3c65f2d0eff605e0736)#define sys\_port\_trace\_k\_work\_queue\_drain\_enter(queue)

457

[ 463](group__subsys__tracing__apis__work__q.md#ga24ca38662182a01185c9815f3cc87385)#define sys\_port\_trace\_k\_work\_queue\_drain\_exit(queue, ret)

464

[ 469](group__subsys__tracing__apis__work__q.md#ga1ca826910efe678127cdc1f9fdae75e7)#define sys\_port\_trace\_k\_work\_queue\_unplug\_enter(queue)

470

[ 476](group__subsys__tracing__apis__work__q.md#gaae2cf0379cbcf040f36fbba39821be2f)#define sys\_port\_trace\_k\_work\_queue\_unplug\_exit(queue, ret)

477 /\* end of subsys\_tracing\_apis\_work\_q \*/

479

485

[ 490](group__subsys__tracing__apis__work__delayable.md#ga2b7d8ad2173665808061ccc1afd52a06)#define sys\_port\_trace\_k\_work\_delayable\_init(dwork)

491

[ 498](group__subsys__tracing__apis__work__delayable.md#gab71fd0042892d3e6c3e486cee63c9564)#define sys\_port\_trace\_k\_work\_schedule\_for\_queue\_enter(queue, dwork, delay)

499

[ 507](group__subsys__tracing__apis__work__delayable.md#ga4d2160569df2886318039bfdae69d979)#define sys\_port\_trace\_k\_work\_schedule\_for\_queue\_exit(queue, dwork, delay, ret)

508

[ 514](group__subsys__tracing__apis__work__delayable.md#gacda1641af1768d815d3cc3e83c1e2456)#define sys\_port\_trace\_k\_work\_schedule\_enter(dwork, delay)

515

[ 522](group__subsys__tracing__apis__work__delayable.md#ga8c5b232168b9bede0cd73f20513e081c)#define sys\_port\_trace\_k\_work\_schedule\_exit(dwork, delay, ret)

523

[ 530](group__subsys__tracing__apis__work__delayable.md#ga8d6e93ed7d85a17ffdb651e3399b0e16)#define sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_enter(queue, dwork, delay)

531

[ 539](group__subsys__tracing__apis__work__delayable.md#ga636e418e8baf90aaffe3e86b86b3b047)#define sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_exit(queue, dwork, delay, ret)

540

[ 546](group__subsys__tracing__apis__work__delayable.md#gafe5b13e8aae388e9b855081450a065e1)#define sys\_port\_trace\_k\_work\_reschedule\_enter(dwork, delay)

547

[ 554](group__subsys__tracing__apis__work__delayable.md#gaf7789cfa1a943b58e6ee93e8ec9dee57)#define sys\_port\_trace\_k\_work\_reschedule\_exit(dwork, delay, ret)

555

[ 561](group__subsys__tracing__apis__work__delayable.md#ga949c751bc5226d1b46fbf7478c1ee5a3)#define sys\_port\_trace\_k\_work\_flush\_delayable\_enter(dwork, sync)

562

[ 569](group__subsys__tracing__apis__work__delayable.md#gab62f6bce942728370aefa0903a8b79a0)#define sys\_port\_trace\_k\_work\_flush\_delayable\_exit(dwork, sync, ret)

570

[ 575](group__subsys__tracing__apis__work__delayable.md#gae80301ae580a3de83f239d9973b3829d)#define sys\_port\_trace\_k\_work\_cancel\_delayable\_enter(dwork)

576

[ 582](group__subsys__tracing__apis__work__delayable.md#gaef6b739acf79e63e94d172e6667269ce)#define sys\_port\_trace\_k\_work\_cancel\_delayable\_exit(dwork, ret)

583

[ 589](group__subsys__tracing__apis__work__delayable.md#gaaa466d5bd2529b6a8ec5672a0054b8f7)#define sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_enter(dwork, sync)

590

[ 597](group__subsys__tracing__apis__work__delayable.md#ga7f2934c863c45a5bb71d1ba0401a9fe9)#define sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_exit(dwork, sync, ret)

598 /\* end of subsys\_tracing\_apis\_work\_delayable \*/

600

606

[ 611](group__subsys__tracing__apis__work__poll.md#gab720957a26a7e34d06af38200965b809)#define sys\_port\_trace\_k\_work\_poll\_init\_enter(work)

612

[ 617](group__subsys__tracing__apis__work__poll.md#gab3f6f18ab804f82386fbf478e6f1925d)#define sys\_port\_trace\_k\_work\_poll\_init\_exit(work)

618

[ 625](group__subsys__tracing__apis__work__poll.md#gad81098506ed138f835230dec3af15076)#define sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_enter(work\_q, work, timeout)

626

[ 633](group__subsys__tracing__apis__work__poll.md#gabfe31b99d03a49d4b2a5cb9e0403fed9)#define sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_blocking(work\_q, work, timeout)

634

[ 642](group__subsys__tracing__apis__work__poll.md#ga7605f1925f1f0e86d890c896586d8776)#define sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_exit(work\_q, work, timeout, ret)

643

[ 649](group__subsys__tracing__apis__work__poll.md#ga44a78c45b0bae26008d9ae5b410753b7)#define sys\_port\_trace\_k\_work\_poll\_submit\_enter(work, timeout)

650

[ 657](group__subsys__tracing__apis__work__poll.md#ga5917fef8383ffdb6fb3f02a42f940059)#define sys\_port\_trace\_k\_work\_poll\_submit\_exit(work, timeout, ret)

658

[ 663](group__subsys__tracing__apis__work__poll.md#ga57e8e57814797b50e7e87e06503dc1f9)#define sys\_port\_trace\_k\_work\_poll\_cancel\_enter(work)

664

[ 670](group__subsys__tracing__apis__work__poll.md#ga3045330b53fa50489a2d3a17b14aa295)#define sys\_port\_trace\_k\_work\_poll\_cancel\_exit(work, ret)

671 /\* end of subsys\_tracing\_apis\_work\_poll \*/

673

679

[ 684](group__subsys__tracing__apis__poll.md#ga83053d6bfc7ad8b070741f38d6606bc1)#define sys\_port\_trace\_k\_poll\_api\_event\_init(event)

685

[ 690](group__subsys__tracing__apis__poll.md#gac44ecc90dc3b407b09e2d45590496e17)#define sys\_port\_trace\_k\_poll\_api\_poll\_enter(events)

691

[ 697](group__subsys__tracing__apis__poll.md#gaf8794133d6ddc29740dfc73b9edbee12)#define sys\_port\_trace\_k\_poll\_api\_poll\_exit(events, ret)

698

[ 703](group__subsys__tracing__apis__poll.md#gaab0dc4527d89c0e0b41d21a76ecfb120)#define sys\_port\_trace\_k\_poll\_api\_signal\_init(signal)

704

[ 709](group__subsys__tracing__apis__poll.md#ga5addc3fa68d6afe454ad7721c8fa17c4)#define sys\_port\_trace\_k\_poll\_api\_signal\_reset(signal)

710

[ 715](group__subsys__tracing__apis__poll.md#ga336dab8d86b07908e641e9845d75be70)#define sys\_port\_trace\_k\_poll\_api\_signal\_check(signal)

716

[ 722](group__subsys__tracing__apis__poll.md#gaeb1f753becfbe92f089eed23825acb4b)#define sys\_port\_trace\_k\_poll\_api\_signal\_raise(signal, ret)

723 /\* end of subsys\_tracing\_apis\_poll \*/

725

731

[ 737](group__subsys__tracing__apis__sem.md#gace327a058d058a940df14c95b031795b)#define sys\_port\_trace\_k\_sem\_init(sem, ret)

738

[ 743](group__subsys__tracing__apis__sem.md#ga552d549c1e8346dbe1445a93e7fc17e9)#define sys\_port\_trace\_k\_sem\_give\_enter(sem)

744

[ 749](group__subsys__tracing__apis__sem.md#ga70d31e53b6e72d2343aa009fa5a98054)#define sys\_port\_trace\_k\_sem\_give\_exit(sem)

750

[ 756](group__subsys__tracing__apis__sem.md#ga216fe8bc373edbb0b48fc4ca7b1816c9)#define sys\_port\_trace\_k\_sem\_take\_enter(sem, timeout)

757

[ 763](group__subsys__tracing__apis__sem.md#gade7546e098a12ce6d935b39f4978ac8d)#define sys\_port\_trace\_k\_sem\_take\_blocking(sem, timeout)

764

[ 771](group__subsys__tracing__apis__sem.md#ga8085db47b86d539e65c107bb33469ee2)#define sys\_port\_trace\_k\_sem\_take\_exit(sem, timeout, ret)

772

[ 777](group__subsys__tracing__apis__sem.md#ga1300af0463f93de0b29751b7a20307cb)#define sys\_port\_trace\_k\_sem\_reset(sem)

778 /\* end of subsys\_tracing\_apis\_sem \*/

780

786

[ 792](group__subsys__tracing__apis__mutex.md#gaefe38feb9aa638b35fd4e723afcebf37)#define sys\_port\_trace\_k\_mutex\_init(mutex, ret)

793

[ 799](group__subsys__tracing__apis__mutex.md#ga5ed2f76aec9c128f163a2e3159e29c80)#define sys\_port\_trace\_k\_mutex\_lock\_enter(mutex, timeout)

800

[ 806](group__subsys__tracing__apis__mutex.md#gaae15023daa241367414afaab085acd2c)#define sys\_port\_trace\_k\_mutex\_lock\_blocking(mutex, timeout)

807

[ 814](group__subsys__tracing__apis__mutex.md#ga31bdc51723303de3bc93d41b36149e57)#define sys\_port\_trace\_k\_mutex\_lock\_exit(mutex, timeout, ret)

815

[ 820](group__subsys__tracing__apis__mutex.md#ga39611be3e36741442a62a98adeef9ee7)#define sys\_port\_trace\_k\_mutex\_unlock\_enter(mutex)

821

[ 825](group__subsys__tracing__apis__mutex.md#ga53c7bd3fc251865ae1a6e79da7a001b1)#define sys\_port\_trace\_k\_mutex\_unlock\_exit(mutex, ret)

826 /\* end of subsys\_tracing\_apis\_mutex \*/

828

834

[ 840](group__subsys__tracing__apis__condvar.md#gab9d1ce42bb6e6c2a762ed242ba364fa8)#define sys\_port\_trace\_k\_condvar\_init(condvar, ret)

841

[ 846](group__subsys__tracing__apis__condvar.md#ga4b0f79f49b710928a38dc10ce22039e5)#define sys\_port\_trace\_k\_condvar\_signal\_enter(condvar)

847

[ 853](group__subsys__tracing__apis__condvar.md#gab946fada5e51a069a13a21736a500669)#define sys\_port\_trace\_k\_condvar\_signal\_blocking(condvar, timeout)

854

[ 860](group__subsys__tracing__apis__condvar.md#ga3992a8afdc375a4ecaa83cac302c7198)#define sys\_port\_trace\_k\_condvar\_signal\_exit(condvar, ret)

861

[ 866](group__subsys__tracing__apis__condvar.md#gadd5affb8afb73b5f76e24477d3d853bb)#define sys\_port\_trace\_k\_condvar\_broadcast\_enter(condvar)

867

[ 873](group__subsys__tracing__apis__condvar.md#ga9a013d5ab1bdd0752ec9bafb2ef4f370)#define sys\_port\_trace\_k\_condvar\_broadcast\_exit(condvar, ret)

874

[ 879](group__subsys__tracing__apis__condvar.md#ga30572aefa29d161af4e9e1841c59d98c)#define sys\_port\_trace\_k\_condvar\_wait\_enter(condvar)

880

[ 886](group__subsys__tracing__apis__condvar.md#ga07e95689443fb483886695a1533a5b08)#define sys\_port\_trace\_k\_condvar\_wait\_exit(condvar, ret)

887 /\* end of subsys\_tracing\_apis\_condvar \*/

889

895

[ 900](group__subsys__tracing__apis__queue.md#ga40e74ce284e349d9e6fbe948c29d574f)#define sys\_port\_trace\_k\_queue\_init(queue)

901

[ 906](group__subsys__tracing__apis__queue.md#ga8df6412be1cd3350c2b1976c7f7c8f4c)#define sys\_port\_trace\_k\_queue\_cancel\_wait(queue)

907

[ 913](group__subsys__tracing__apis__queue.md#ga0e38a81f47c44e1be515b375f384a2d2)#define sys\_port\_trace\_k\_queue\_queue\_insert\_enter(queue, alloc)

914

[ 921](group__subsys__tracing__apis__queue.md#ga3e51a4120f2ff7560ad494620c801886)#define sys\_port\_trace\_k\_queue\_queue\_insert\_blocking(queue, alloc, timeout)

922

[ 929](group__subsys__tracing__apis__queue.md#ga9fe7ee8315505734bf33d71083190533)#define sys\_port\_trace\_k\_queue\_queue\_insert\_exit(queue, alloc, ret)

930

[ 935](group__subsys__tracing__apis__queue.md#ga541411a2d9856fe01ed2e532a7e33db4)#define sys\_port\_trace\_k\_queue\_append\_enter(queue)

936

[ 941](group__subsys__tracing__apis__queue.md#ga1c1a038ffa1da2efd495f769f12bc685)#define sys\_port\_trace\_k\_queue\_append\_exit(queue)

942

[ 947](group__subsys__tracing__apis__queue.md#ga5ef57f07d5ff8c730893f96b174f967a)#define sys\_port\_trace\_k\_queue\_alloc\_append\_enter(queue)

948

[ 954](group__subsys__tracing__apis__queue.md#ga54601544ad750fb6a5afa725a19ce269)#define sys\_port\_trace\_k\_queue\_alloc\_append\_exit(queue, ret)

955

[ 960](group__subsys__tracing__apis__queue.md#ga90f15dc66fffd87e2b4fb66fb8bae4b1)#define sys\_port\_trace\_k\_queue\_prepend\_enter(queue)

961

[ 966](group__subsys__tracing__apis__queue.md#ga023a6fee85616ae5f32b5fa4b29d29e5)#define sys\_port\_trace\_k\_queue\_prepend\_exit(queue)

967

[ 972](group__subsys__tracing__apis__queue.md#gaae4196d40be1a74439a1b7010626da17)#define sys\_port\_trace\_k\_queue\_alloc\_prepend\_enter(queue)

973

[ 979](group__subsys__tracing__apis__queue.md#ga2d7ff756f5c017d7b3f10787716b5684)#define sys\_port\_trace\_k\_queue\_alloc\_prepend\_exit(queue, ret)

980

[ 985](group__subsys__tracing__apis__queue.md#ga4e78ca5d7d927b912e09829b51e7330c)#define sys\_port\_trace\_k\_queue\_insert\_enter(queue)

986

[ 992](group__subsys__tracing__apis__queue.md#gaad04f21122c554c33ef0cb394abf6df1)#define sys\_port\_trace\_k\_queue\_insert\_blocking(queue, timeout)

993

[ 998](group__subsys__tracing__apis__queue.md#ga69ca963f74777d9d351c9d20fe9dff62)#define sys\_port\_trace\_k\_queue\_insert\_exit(queue)

999

[ 1004](group__subsys__tracing__apis__queue.md#ga777cfd6ee6ad016c2bbc519a490c0672)#define sys\_port\_trace\_k\_queue\_append\_list\_enter(queue)

1005

[ 1011](group__subsys__tracing__apis__queue.md#ga215aca3523a17e31d4d36d3d95f28544)#define sys\_port\_trace\_k\_queue\_append\_list\_exit(queue, ret)

1012

[ 1017](group__subsys__tracing__apis__queue.md#ga888a4a39d0c33fab4243c64e42011856)#define sys\_port\_trace\_k\_queue\_merge\_slist\_enter(queue)

1018

[ 1024](group__subsys__tracing__apis__queue.md#ga87336faf8e19c64bcbf188452e336639)#define sys\_port\_trace\_k\_queue\_merge\_slist\_exit(queue, ret)

1025

[ 1031](group__subsys__tracing__apis__queue.md#ga59c1bac1a34c950c7ca324fc8d853acb)#define sys\_port\_trace\_k\_queue\_get\_enter(queue, timeout)

1032

[ 1038](group__subsys__tracing__apis__queue.md#gad83deb664f66df825b290b17f97156c7)#define sys\_port\_trace\_k\_queue\_get\_blocking(queue, timeout)

1039

[ 1046](group__subsys__tracing__apis__queue.md#ga8afd074bab6b31d60169a72db51ef76c)#define sys\_port\_trace\_k\_queue\_get\_exit(queue, timeout, ret)

1047

[ 1052](group__subsys__tracing__apis__queue.md#gacc2e453e717c654318dfd02e09288636)#define sys\_port\_trace\_k\_queue\_remove\_enter(queue)

1053

[ 1059](group__subsys__tracing__apis__queue.md#ga1df298e35d176ca79924a9b534bb115c)#define sys\_port\_trace\_k\_queue\_remove\_exit(queue, ret)

1060

[ 1065](group__subsys__tracing__apis__queue.md#ga2842e4d5e778016ea70d5b860f217421)#define sys\_port\_trace\_k\_queue\_unique\_append\_enter(queue)

1066

[ 1073](group__subsys__tracing__apis__queue.md#ga830dfc12a35c0c001abfe2cbf89387aa)#define sys\_port\_trace\_k\_queue\_unique\_append\_exit(queue, ret)

1074

[ 1080](group__subsys__tracing__apis__queue.md#ga1cb5384c1eccc5d40c3e748dd1990cce)#define sys\_port\_trace\_k\_queue\_peek\_head(queue, ret)

1081

[ 1087](group__subsys__tracing__apis__queue.md#gac28c33f0457d7e8f99e20d0fc55427ee)#define sys\_port\_trace\_k\_queue\_peek\_tail(queue, ret)

1088 /\* end of subsys\_tracing\_apis\_queue \*/

1090

1096

[ 1101](group__subsys__tracing__apis__fifo.md#gac0da5eca137a970c67b7b94a568c93e6)#define sys\_port\_trace\_k\_fifo\_init\_enter(fifo)

1102

[ 1107](group__subsys__tracing__apis__fifo.md#gaaf6c7c710377f449d52c5d6f5f7103c8)#define sys\_port\_trace\_k\_fifo\_init\_exit(fifo)

1108

[ 1113](group__subsys__tracing__apis__fifo.md#ga81e706aff605468683a96b14940745e7)#define sys\_port\_trace\_k\_fifo\_cancel\_wait\_enter(fifo)

1114

[ 1119](group__subsys__tracing__apis__fifo.md#ga03ccb2bb3141c2842959ba77e4cd7337)#define sys\_port\_trace\_k\_fifo\_cancel\_wait\_exit(fifo)

1120

[ 1126](group__subsys__tracing__apis__fifo.md#gaac5f6b9e77dad9de4652d24502ab46d0)#define sys\_port\_trace\_k\_fifo\_put\_enter(fifo, data)

1127

[ 1133](group__subsys__tracing__apis__fifo.md#ga7a1d15a538f23d2b7f290435803cd73e)#define sys\_port\_trace\_k\_fifo\_put\_exit(fifo, data)

1134

[ 1140](group__subsys__tracing__apis__fifo.md#ga9c433ad8dc99ac38b8d5b4755da05c67)#define sys\_port\_trace\_k\_fifo\_alloc\_put\_enter(fifo, data)

1141

[ 1148](group__subsys__tracing__apis__fifo.md#gad9871fb1487a387a4f73e94bccb99a6d)#define sys\_port\_trace\_k\_fifo\_alloc\_put\_exit(fifo, data, ret)

1149

[ 1156](group__subsys__tracing__apis__fifo.md#gace20fdce59a99b92c8ac3711c4085b28)#define sys\_port\_trace\_k\_fifo\_put\_list\_enter(fifo, head, tail)

1157

[ 1164](group__subsys__tracing__apis__fifo.md#ga739360e2cefa158f22ce20a1e9369aea)#define sys\_port\_trace\_k\_fifo\_put\_list\_exit(fifo, head, tail)

1165

[ 1171](group__subsys__tracing__apis__fifo.md#gaf975d817bdefc64b9329330f6cd88d21)#define sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_enter(fifo, list)

1172

[ 1178](group__subsys__tracing__apis__fifo.md#gae1c620ec17a1f7a899a1e5cba996644e)#define sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_exit(fifo, list)

1179

[ 1185](group__subsys__tracing__apis__fifo.md#gaa3539eea74888c6257c5f5d456748155)#define sys\_port\_trace\_k\_fifo\_get\_enter(fifo, timeout)

1186

[ 1193](group__subsys__tracing__apis__fifo.md#gae6f06386f224063ee756e8ff0000dfe4)#define sys\_port\_trace\_k\_fifo\_get\_exit(fifo, timeout, ret)

1194

[ 1199](group__subsys__tracing__apis__fifo.md#gab0fea5751e0296e623606e54efe5687b)#define sys\_port\_trace\_k\_fifo\_peek\_head\_enter(fifo)

1200

[ 1206](group__subsys__tracing__apis__fifo.md#ga06b74415be416b137092cb72187c1fb6)#define sys\_port\_trace\_k\_fifo\_peek\_head\_exit(fifo, ret)

1207

[ 1212](group__subsys__tracing__apis__fifo.md#gad9f9b3193ed2c7270030036aef8d343d)#define sys\_port\_trace\_k\_fifo\_peek\_tail\_enter(fifo)

1213

[ 1219](group__subsys__tracing__apis__fifo.md#gae33baafbaac06ada7d6b53026a973d81)#define sys\_port\_trace\_k\_fifo\_peek\_tail\_exit(fifo, ret)

1220 /\* end of subsys\_tracing\_apis\_fifo \*/

1222

1228

[ 1233](group__subsys__tracing__apis__lifo.md#gaad81b60363467b56d887baee8c8b5bf2)#define sys\_port\_trace\_k\_lifo\_init\_enter(lifo)

1234

[ 1239](group__subsys__tracing__apis__lifo.md#ga4f08168ded97456265abb3a903585ecf)#define sys\_port\_trace\_k\_lifo\_init\_exit(lifo)

1240

[ 1246](group__subsys__tracing__apis__lifo.md#gafd9c45a171a2fb146defa356ff0bc0f5)#define sys\_port\_trace\_k\_lifo\_put\_enter(lifo, data)

1247

[ 1253](group__subsys__tracing__apis__lifo.md#ga0e5372c37bdd3a47adf11ab9d3a5e22d)#define sys\_port\_trace\_k\_lifo\_put\_exit(lifo, data)

1254

[ 1260](group__subsys__tracing__apis__lifo.md#ga0d9717f4b43e344518cc451a2fe9d224)#define sys\_port\_trace\_k\_lifo\_alloc\_put\_enter(lifo, data)

1261

[ 1268](group__subsys__tracing__apis__lifo.md#ga19bb748367aba8f576e72cdc30834ab1)#define sys\_port\_trace\_k\_lifo\_alloc\_put\_exit(lifo, data, ret)

1269

[ 1275](group__subsys__tracing__apis__lifo.md#ga61556928453492dc6ed4efc999668f01)#define sys\_port\_trace\_k\_lifo\_get\_enter(lifo, timeout)

1276

[ 1283](group__subsys__tracing__apis__lifo.md#ga2f7e8e680cac03844ca5dbab0438a754)#define sys\_port\_trace\_k\_lifo\_get\_exit(lifo, timeout, ret)

1284 /\* end of subsys\_tracing\_apis\_lifo \*/

1286

1292

[ 1297](group__subsys__tracing__apis__stack.md#ga5bb95f74d8bc3eed2525be20c444824f)#define sys\_port\_trace\_k\_stack\_init(stack)

1298

[ 1303](group__subsys__tracing__apis__stack.md#gaa10d6cb275914bb25ad6ffad12807480)#define sys\_port\_trace\_k\_stack\_alloc\_init\_enter(stack)

1304

[ 1310](group__subsys__tracing__apis__stack.md#gabaabe367b83b39248112eadb07bdf714)#define sys\_port\_trace\_k\_stack\_alloc\_init\_exit(stack, ret)

1311

[ 1316](group__subsys__tracing__apis__stack.md#gaf8357d3d9a2cb8de7ba0b3473c5b063c)#define sys\_port\_trace\_k\_stack\_cleanup\_enter(stack)

1317

[ 1323](group__subsys__tracing__apis__stack.md#ga2225cab95abdd8188087e6a98641ec0c)#define sys\_port\_trace\_k\_stack\_cleanup\_exit(stack, ret)

1324

[ 1329](group__subsys__tracing__apis__stack.md#gad6a42d93265b53540baab5c59f55fbf6)#define sys\_port\_trace\_k\_stack\_push\_enter(stack)

1330

[ 1336](group__subsys__tracing__apis__stack.md#ga203d32ef138d041aa0c20db8a75ccd6a)#define sys\_port\_trace\_k\_stack\_push\_exit(stack, ret)

1337

[ 1343](group__subsys__tracing__apis__stack.md#gaaf9ac378b0bbf09af91c1987dc5b777e)#define sys\_port\_trace\_k\_stack\_pop\_enter(stack, timeout)

1344

[ 1350](group__subsys__tracing__apis__stack.md#gacbdaf326a104d3bdcd4ceb5ec72c9b4f)#define sys\_port\_trace\_k\_stack\_pop\_blocking(stack, timeout)

1351

[ 1358](group__subsys__tracing__apis__stack.md#ga11280d48a97cca4b65210791f9d8c591)#define sys\_port\_trace\_k\_stack\_pop\_exit(stack, timeout, ret)

1359 /\* end of subsys\_tracing\_apis\_stack \*/

1361

1367

[ 1372](group__subsys__tracing__apis__msgq.md#ga94eae512e590d61c1c74f5d7eb552d50)#define sys\_port\_trace\_k\_msgq\_init(msgq)

1373

[ 1378](group__subsys__tracing__apis__msgq.md#ga392ac9fe978d78ee1ca23c27f93e5053)#define sys\_port\_trace\_k\_msgq\_alloc\_init\_enter(msgq)

1379

[ 1385](group__subsys__tracing__apis__msgq.md#ga60973fcaae9be0a6b292bf2a5dfb4fb2)#define sys\_port\_trace\_k\_msgq\_alloc\_init\_exit(msgq, ret)

1386

[ 1391](group__subsys__tracing__apis__msgq.md#ga370c16cd808037db5dc605e91d3c21b8)#define sys\_port\_trace\_k\_msgq\_cleanup\_enter(msgq)

1392

[ 1398](group__subsys__tracing__apis__msgq.md#gaff32cb729fd32c7b008191cac1e2c881)#define sys\_port\_trace\_k\_msgq\_cleanup\_exit(msgq, ret)

1399

[ 1405](group__subsys__tracing__apis__msgq.md#ga829e2b0d3420079777362f0b78f28d50)#define sys\_port\_trace\_k\_msgq\_put\_enter(msgq, timeout)

1406

[ 1412](group__subsys__tracing__apis__msgq.md#gaead1e1b345e029017b1951a3d112554f)#define sys\_port\_trace\_k\_msgq\_put\_blocking(msgq, timeout)

1413

[ 1420](group__subsys__tracing__apis__msgq.md#gab4794be3e4a68af3ada3667d98286747)#define sys\_port\_trace\_k\_msgq\_put\_exit(msgq, timeout, ret)

1421

[ 1427](group__subsys__tracing__apis__msgq.md#ga1d79dbc50b8ddd0d3db803b7c747ede5)#define sys\_port\_trace\_k\_msgq\_get\_enter(msgq, timeout)

1428

[ 1434](group__subsys__tracing__apis__msgq.md#ga448baf7df9ec1abc4ec3a12609400b68)#define sys\_port\_trace\_k\_msgq\_get\_blocking(msgq, timeout)

1435

[ 1442](group__subsys__tracing__apis__msgq.md#ga2a549f567cda0646b853a9cb0b7e1eb2)#define sys\_port\_trace\_k\_msgq\_get\_exit(msgq, timeout, ret)

1443

[ 1449](group__subsys__tracing__apis__msgq.md#gad11e9f22177bf004f95d23750a2046a3)#define sys\_port\_trace\_k\_msgq\_peek(msgq, ret)

1450

[ 1455](group__subsys__tracing__apis__msgq.md#ga91530d1c6d10ce72cc5c9319c28b5e32)#define sys\_port\_trace\_k\_msgq\_purge(msgq)

1456 /\* end of subsys\_tracing\_apis\_msgq \*/

1458

1464

[ 1469](group__subsys__tracing__apis__mbox.md#ga67187d636152a34614c4213c47ea7509)#define sys\_port\_trace\_k\_mbox\_init(mbox)

1470

[ 1476](group__subsys__tracing__apis__mbox.md#gac7b683e1e33c42e3e04f84a2c2b19811)#define sys\_port\_trace\_k\_mbox\_message\_put\_enter(mbox, timeout)

1477

[ 1483](group__subsys__tracing__apis__mbox.md#ga6a04c6ea1072d7c858a23c845e76565d)#define sys\_port\_trace\_k\_mbox\_message\_put\_blocking(mbox, timeout)

1484

[ 1491](group__subsys__tracing__apis__mbox.md#ga2ab3697623a198ea15ad644ce19335fb)#define sys\_port\_trace\_k\_mbox\_message\_put\_exit(mbox, timeout, ret)

1492

[ 1498](group__subsys__tracing__apis__mbox.md#gaba437af59b1a8c663fa7d39eafa78ee6)#define sys\_port\_trace\_k\_mbox\_put\_enter(mbox, timeout)

1499

[ 1506](group__subsys__tracing__apis__mbox.md#ga07148a910c33c881d531ed495b23c081)#define sys\_port\_trace\_k\_mbox\_put\_exit(mbox, timeout, ret)

1507

[ 1513](group__subsys__tracing__apis__mbox.md#ga7dd281ffa54a3d32c7380e294e18ef5d)#define sys\_port\_trace\_k\_mbox\_async\_put\_enter(mbox, sem)

1514

[ 1520](group__subsys__tracing__apis__mbox.md#gab39d7bfdfc0c5ed394e7819a3048741e)#define sys\_port\_trace\_k\_mbox\_async\_put\_exit(mbox, sem)

1521

[ 1527](group__subsys__tracing__apis__mbox.md#ga30ad94a6f1267931ff8d401fb4a75be3)#define sys\_port\_trace\_k\_mbox\_get\_enter(mbox, timeout)

1528

[ 1534](group__subsys__tracing__apis__mbox.md#ga4977171638fed999e4485cc035016c10)#define sys\_port\_trace\_k\_mbox\_get\_blocking(mbox, timeout)

1535

[ 1542](group__subsys__tracing__apis__mbox.md#gaaa8261b9fa07c97308b46a9b7100aee6)#define sys\_port\_trace\_k\_mbox\_get\_exit(mbox, timeout, ret)

1543

[ 1548](group__subsys__tracing__apis__mbox.md#gacef2016dc5620371401e55e7005a18c3)#define sys\_port\_trace\_k\_mbox\_data\_get(rx\_msg)

1549 /\* end of subsys\_tracing\_apis\_mbox \*/

1551

1557

[ 1564](group__subsys__tracing__apis__pipe.md#ga8b22ee35dfa2c4be5cf9772fe92dd731)#define sys\_port\_trace\_k\_pipe\_init(pipe, buffer, size)

1565

[ 1570](group__subsys__tracing__apis__pipe.md#ga9168b8fbacac753adc76b5fa341ba5f3)#define sys\_port\_trace\_k\_pipe\_reset\_enter(pipe)

1571

[ 1576](group__subsys__tracing__apis__pipe.md#gad880e5655d35441e83bada3e950924cc)#define sys\_port\_trace\_k\_pipe\_reset\_exit(pipe)

1577

[ 1582](group__subsys__tracing__apis__pipe.md#gad9913c3eaa2711e501f4d3a071ee2304)#define sys\_port\_trace\_k\_pipe\_close\_enter(pipe)

1583

[ 1588](group__subsys__tracing__apis__pipe.md#ga42029311eeb46b06d8a4cdd3ca12b2fe)#define sys\_port\_trace\_k\_pipe\_close\_exit(pipe)

1589

[ 1597](group__subsys__tracing__apis__pipe.md#gae1d79d1472bfb3905f107159b297d50b)#define sys\_port\_trace\_k\_pipe\_write\_enter(pipe, data, len, timeout)

1598

[ 1604](group__subsys__tracing__apis__pipe.md#ga566b7428e665bf086beaac4884bee3b6)#define sys\_port\_trace\_k\_pipe\_write\_blocking(pipe, timeout)

1605

[ 1611](group__subsys__tracing__apis__pipe.md#gacb4b01b7c27ac7ad875f054038832d3a)#define sys\_port\_trace\_k\_pipe\_write\_exit(pipe, ret)

1612

[ 1620](group__subsys__tracing__apis__pipe.md#ga35d3ebbc09e2690a9b01707663c9f4cc)#define sys\_port\_trace\_k\_pipe\_read\_enter(pipe, data, len, timeout)

1621

[ 1627](group__subsys__tracing__apis__pipe.md#ga94f7c8eb46b23be75eb9341ec52bfeb1)#define sys\_port\_trace\_k\_pipe\_read\_blocking(pipe, timeout)

1628

[ 1634](group__subsys__tracing__apis__pipe.md#gaa43afb60d07428049dd13c12a7fcab88)#define sys\_port\_trace\_k\_pipe\_read\_exit(pipe, ret)

1635

[ 1640](group__subsys__tracing__apis__pipe.md#ga63bc37ca2dbcf84fc87e13fdb2f21834)#define sys\_port\_trace\_k\_pipe\_cleanup\_enter(pipe)

1641

[ 1647](group__subsys__tracing__apis__pipe.md#gaa367f4e1019380dde77ee881f22ab278)#define sys\_port\_trace\_k\_pipe\_cleanup\_exit(pipe, ret)

1648

[ 1653](group__subsys__tracing__apis__pipe.md#ga6fdcad7deb3be98acd88cd8febd39247)#define sys\_port\_trace\_k\_pipe\_alloc\_init\_enter(pipe)

1654

[ 1660](group__subsys__tracing__apis__pipe.md#ga011af7de686c1b360f0696a7dd1b173f)#define sys\_port\_trace\_k\_pipe\_alloc\_init\_exit(pipe, ret)

1661

[ 1666](group__subsys__tracing__apis__pipe.md#ga9e3f6058f2370488cfb4d57676c3d5cd)#define sys\_port\_trace\_k\_pipe\_flush\_enter(pipe)

1667

[ 1672](group__subsys__tracing__apis__pipe.md#gafdba63af20781901576344ef198da8a4)#define sys\_port\_trace\_k\_pipe\_flush\_exit(pipe)

1673

[ 1678](group__subsys__tracing__apis__pipe.md#gaa81b667947689ac7edb866cb7c5beb81)#define sys\_port\_trace\_k\_pipe\_buffer\_flush\_enter(pipe)

1679

[ 1684](group__subsys__tracing__apis__pipe.md#ga47d9a997d8daff89a1c4a41ac4bb327e)#define sys\_port\_trace\_k\_pipe\_buffer\_flush\_exit(pipe)

1685

[ 1691](group__subsys__tracing__apis__pipe.md#gad16f0673669f9700ebd3e4fc0b1466d8)#define sys\_port\_trace\_k\_pipe\_put\_enter(pipe, timeout)

1692

[ 1698](group__subsys__tracing__apis__pipe.md#ga314cffd927b410d3670f39a774a42206)#define sys\_port\_trace\_k\_pipe\_put\_blocking(pipe, timeout)

1699

[ 1706](group__subsys__tracing__apis__pipe.md#ga20a131258373e32379273dd0ff08a672)#define sys\_port\_trace\_k\_pipe\_put\_exit(pipe, timeout, ret)

1707

[ 1713](group__subsys__tracing__apis__pipe.md#gaafa10362c5042f0f2e02b40b79768dbb)#define sys\_port\_trace\_k\_pipe\_get\_enter(pipe, timeout)

1714

[ 1720](group__subsys__tracing__apis__pipe.md#ga2dfb7cfd0b08beac72d254ac3063d42c)#define sys\_port\_trace\_k\_pipe\_get\_blocking(pipe, timeout)

1721

[ 1728](group__subsys__tracing__apis__pipe.md#ga192cb7bafd2d04898b13e30aa96d483d)#define sys\_port\_trace\_k\_pipe\_get\_exit(pipe, timeout, ret)

1729 /\* end of subsys\_tracing\_apis\_pipe \*/

1731

1737

[ 1742](group__subsys__tracing__apis__heap.md#gaa9eb0a2ff9da8a892ab62e45fe4e4ddb)#define sys\_port\_trace\_k\_heap\_init(h)

1743

[ 1749](group__subsys__tracing__apis__heap.md#gaa49162a735def3b0389cc30bd4654533)#define sys\_port\_trace\_k\_heap\_aligned\_alloc\_enter(h, timeout)

1750

[ 1756](group__subsys__tracing__apis__heap.md#gada1001c802bcc55437ffd8f4e2f23bef)#define sys\_port\_trace\_k\_heap\_aligned\_alloc\_blocking(h, timeout)

1757

[ 1764](group__subsys__tracing__apis__heap.md#ga3833f13065d967acafd50e3089556944)#define sys\_port\_trace\_k\_heap\_aligned\_alloc\_exit(h, timeout, ret)

1765

[ 1771](group__subsys__tracing__apis__heap.md#gadf8441b3c430499c8444a7c73bae1931)#define sys\_port\_trace\_k\_heap\_alloc\_enter(h, timeout)

1772

[ 1779](group__subsys__tracing__apis__heap.md#gad696bba7ffe71beb01520ab27b483307)#define sys\_port\_trace\_k\_heap\_alloc\_exit(h, timeout, ret)

1780

[ 1786](group__subsys__tracing__apis__heap.md#gac5982869d3ec94331b5b8efb3fafbc59)#define sys\_port\_trace\_k\_heap\_calloc\_enter(h, timeout)

1787

[ 1794](group__subsys__tracing__apis__heap.md#ga7c9fd0cf63be9b591adc7e59af0803d4)#define sys\_port\_trace\_k\_heap\_calloc\_exit(h, timeout, ret)

1795

[ 1800](group__subsys__tracing__apis__heap.md#ga6f9c92a02d32af203752c59615e34096)#define sys\_port\_trace\_k\_heap\_free(h)

1801

[ 1809](group__subsys__tracing__apis__heap.md#ga5c7936b9c4f257e22638824c7ba6601e)#define sys\_port\_trace\_k\_heap\_realloc\_enter(h, ptr, bytes, timeout)

1810

[ 1819](group__subsys__tracing__apis__heap.md#ga888b7ae4b7c29e4c2e877ca1c525d315)#define sys\_port\_trace\_k\_heap\_realloc\_exit(h, ptr, bytes, timeout, ret)

1820

[ 1825](group__subsys__tracing__apis__heap.md#ga12de856dc1fc2cb261497b3ef8b09e9e)#define sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_enter(heap)

1826

[ 1832](group__subsys__tracing__apis__heap.md#ga6d7a77c282f8229e0b366d57ba33ed04)#define sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_exit(heap, ret)

1833

[ 1838](group__subsys__tracing__apis__heap.md#ga478745a9e6cbc1a7b6bc9a2fc1763ca5)#define sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_enter(heap)

1839

[ 1845](group__subsys__tracing__apis__heap.md#ga4d612b7ec5d992c6e8170f35a1ce6c03)#define sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_exit(heap, ret)

1846

[ 1852](group__subsys__tracing__apis__heap.md#gaf4dd86f13041c12cf18696fcff2ba9aa)#define sys\_port\_trace\_k\_heap\_sys\_k\_free\_enter(heap, heap\_ref)

1853

[ 1859](group__subsys__tracing__apis__heap.md#gaf2865a12ffee2135e2d798bdf5fa9c98)#define sys\_port\_trace\_k\_heap\_sys\_k\_free\_exit(heap, heap\_ref)

1860

[ 1865](group__subsys__tracing__apis__heap.md#ga60e3dd5434ba9c912a4f2332f579318f)#define sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_enter(heap)

1866

[ 1872](group__subsys__tracing__apis__heap.md#ga6be2fe00eabc9bffaf635cfb14714e4a)#define sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_exit(heap, ret)

1873

[ 1879](group__subsys__tracing__apis__heap.md#ga5c2e672b64f326b93aca9a4840ca5123)#define sys\_port\_trace\_k\_heap\_sys\_k\_realloc\_enter(heap, ptr)

1880

[ 1887](group__subsys__tracing__apis__heap.md#ga154dcc3e907ca4dbac41918cbb958e42)#define sys\_port\_trace\_k\_heap\_sys\_k\_realloc\_exit(heap, ptr, ret)

1888 /\* end of subsys\_tracing\_apis\_heap \*/

1890

1896

[ 1902](group__subsys__tracing__apis__mslab.md#ga5a769fffc7611a57c8490b3f5c6047a5)#define sys\_port\_trace\_k\_mem\_slab\_init(slab, rc)

1903

[ 1909](group__subsys__tracing__apis__mslab.md#gac1ac5f1393b87ea84c2d53f08c251ff2)#define sys\_port\_trace\_k\_mem\_slab\_alloc\_enter(slab, timeout)

1910

[ 1916](group__subsys__tracing__apis__mslab.md#gaea77ffa2dbbfad9ff2fec0041b0dbc59)#define sys\_port\_trace\_k\_mem\_slab\_alloc\_blocking(slab, timeout)

1917

[ 1924](group__subsys__tracing__apis__mslab.md#ga237bb89733ca9c483ef6b9ab6dd920a4)#define sys\_port\_trace\_k\_mem\_slab\_alloc\_exit(slab, timeout, ret)

1925

[ 1930](group__subsys__tracing__apis__mslab.md#ga22fc4609185f6ddffd0abc85f3976914)#define sys\_port\_trace\_k\_mem\_slab\_free\_enter(slab)

1931

[ 1936](group__subsys__tracing__apis__mslab.md#ga81dd030d4052e3092479e19616b4baec)#define sys\_port\_trace\_k\_mem\_slab\_free\_exit(slab)

1937 /\* end of subsys\_tracing\_apis\_mslab \*/

1939

1945

[ 1950](group__subsys__tracing__apis__timer.md#ga03a70d84ea0227829fb9528b0156c147)#define sys\_port\_trace\_k\_timer\_init(timer)

1951

[ 1958](group__subsys__tracing__apis__timer.md#ga95b998ea6bf00692cb654a18787ab185)#define sys\_port\_trace\_k\_timer\_start(timer, duration, period)

1959

[ 1964](group__subsys__tracing__apis__timer.md#ga81b6cba81190cc61cdd33f4ddb6f4550)#define sys\_port\_trace\_k\_timer\_stop(timer)

1965

[ 1970](group__subsys__tracing__apis__timer.md#ga0adf7e6ca5bdd89b7676836101ef37df)#define sys\_port\_trace\_k\_timer\_status\_sync\_enter(timer)

1971

[ 1977](group__subsys__tracing__apis__timer.md#gaa3cd4ca118fd987560ae1855c904e1aa)#define sys\_port\_trace\_k\_timer\_status\_sync\_blocking(timer, timeout)

1978

[ 1984](group__subsys__tracing__apis__timer.md#gab51aa6682136eb86a4fd141f61ece779)#define sys\_port\_trace\_k\_timer\_status\_sync\_exit(timer, result)

1985 /\* end of subsys\_tracing\_apis\_timer \*/

1987

1993

[ 1998](group__subsys__tracing__apis__event.md#gae212c1b330d476613629501d62be0994)#define sys\_port\_trace\_k\_event\_init(event)

1999

[ 2006](group__subsys__tracing__apis__event.md#ga20092082696c6c9fe3b8870bd3523b52)#define sys\_port\_trace\_k\_event\_post\_enter(event, events, events\_mask)

2007

[ 2014](group__subsys__tracing__apis__event.md#gac58a047db800cca608087d6b2cec37f9)#define sys\_port\_trace\_k\_event\_post\_exit(event, events, events\_mask)

2015

[ 2023](group__subsys__tracing__apis__event.md#ga6b01461ff2fa0cf2c3c19dbed2f8c4c3)#define sys\_port\_trace\_k\_event\_wait\_enter(event, events, options, timeout)

2024

[ 2032](group__subsys__tracing__apis__event.md#ga008a96d80f3f90dcffbc74f43d66b9be)#define sys\_port\_trace\_k\_event\_wait\_blocking(event, events, options, timeout)

2033

[ 2040](group__subsys__tracing__apis__event.md#ga874698f8eff5237fefacc1be761b2661)#define sys\_port\_trace\_k\_event\_wait\_exit(event, events, ret)

2041 /\* end of subsys\_tracing\_apis\_event \*/

2043

2049

[ 2054](group__subsys__tracing__apis__pm__system.md#ga1d8c01fe22ef0f7ac8fdfb47de55f58e)#define sys\_port\_trace\_pm\_system\_suspend\_enter(ticks)

2055

[ 2061](group__subsys__tracing__apis__pm__system.md#gaabc547256f20c5da3b25a14dbd047014)#define sys\_port\_trace\_pm\_system\_suspend\_exit(ticks, state)

2062 /\* end of subsys\_tracing\_apis\_pm\_system \*/

2064

2070

[ 2075](group__subsys__tracing__apis__pm__device__runtime.md#ga31c463cfc6794a9d454adbe19c0eff96)#define sys\_port\_trace\_pm\_device\_runtime\_get\_enter(dev)

2076

[ 2082](group__subsys__tracing__apis__pm__device__runtime.md#ga6f9dfe29417ecc3c80b457b3b1ca5ad2)#define sys\_port\_trace\_pm\_device\_runtime\_get\_exit(dev, ret)

2083

[ 2088](group__subsys__tracing__apis__pm__device__runtime.md#gae077ffd9acdc7f4a9b8eff7edca7c5fe)#define sys\_port\_trace\_pm\_device\_runtime\_put\_enter(dev)

2089

[ 2095](group__subsys__tracing__apis__pm__device__runtime.md#ga5670d2d13a291224a8600de54ca475dd)#define sys\_port\_trace\_pm\_device\_runtime\_put\_exit(dev, ret)

2096

[ 2102](group__subsys__tracing__apis__pm__device__runtime.md#gab25dc434aa5ce819f295256effa4cd1a)#define sys\_port\_trace\_pm\_device\_runtime\_put\_async\_enter(dev, delay)

2103

[ 2110](group__subsys__tracing__apis__pm__device__runtime.md#gae2cb1246d1028a962282c28611c6df11)#define sys\_port\_trace\_pm\_device\_runtime\_put\_async\_exit(dev, delay, ret)

2111

[ 2116](group__subsys__tracing__apis__pm__device__runtime.md#ga6653c737e964963541a60aec29120ac0)#define sys\_port\_trace\_pm\_device\_runtime\_enable\_enter(dev)

2117

[ 2123](group__subsys__tracing__apis__pm__device__runtime.md#ga0ade92830387457ccc60661325d3f426)#define sys\_port\_trace\_pm\_device\_runtime\_enable\_exit(dev, ret)

2124

[ 2129](group__subsys__tracing__apis__pm__device__runtime.md#gaeb479059715af42498f1b1936561f207)#define sys\_port\_trace\_pm\_device\_runtime\_disable\_enter(dev)

2130

[ 2136](group__subsys__tracing__apis__pm__device__runtime.md#ga88606e2073fb35283b06500743ebfeb0)#define sys\_port\_trace\_pm\_device\_runtime\_disable\_exit(dev, ret)

2137 /\* end of subsys\_tracing\_apis\_pm\_device\_runtime \*/

2139

2145

[ 2151](group__subsys__tracing__apis__net.md#gab39c341e9aad487268cc934dd6104fc6)#define sys\_port\_trace\_net\_recv\_data\_enter(iface, pkt)

2152

[ 2159](group__subsys__tracing__apis__net.md#ga4c0ba70ff0eef209005eb47c76e11682)#define sys\_port\_trace\_net\_recv\_data\_exit(iface, pkt, ret)

2160

[ 2165](group__subsys__tracing__apis__net.md#ga9738aa7cefef4038974523bdf6d1a672)#define sys\_port\_trace\_net\_send\_data\_enter(pkt)

2166

[ 2172](group__subsys__tracing__apis__net.md#gaf3dde1664303355401f0765271dfedb4)#define sys\_port\_trace\_net\_send\_data\_exit(pkt, ret)

2173

[ 2179](group__subsys__tracing__apis__net.md#gace8a76a44fc01a1f14633c3a758d2811)#define sys\_port\_trace\_net\_rx\_time(pkt, end\_time)

2180

[ 2186](group__subsys__tracing__apis__net.md#ga1db4323543a538b3911b44f65ecf7d50)#define sys\_port\_trace\_net\_tx\_time(pkt, end\_time)

2187 /\* end of subsys\_tracing\_apis\_net \*/

2189

2195

[ 2203](group__subsys__tracing__apis__socket.md#ga9d4f7402bb41321dc86fe521b8ac61c4)#define sys\_port\_trace\_socket\_init(socket, family, type, proto)

2204

[ 2209](group__subsys__tracing__apis__socket.md#gaf8e8b1245a3bc053cc1b2ceb2b50aca6)#define sys\_port\_trace\_socket\_close\_enter(socket)

2210

[ 2216](group__subsys__tracing__apis__socket.md#ga43248f800666043e02a206c402137e39)#define sys\_port\_trace\_socket\_close\_exit(socket, ret)

2217

[ 2223](group__subsys__tracing__apis__socket.md#gaaee4b59afd78be034bc933b0f4cb80c4)#define sys\_port\_trace\_socket\_shutdown\_enter(socket, how)

2224

[ 2230](group__subsys__tracing__apis__socket.md#ga708c4791bc53315afd08b42b83e2c828)#define sys\_port\_trace\_socket\_shutdown\_exit(socket, ret)

2231

[ 2238](group__subsys__tracing__apis__socket.md#ga8f719e0ef0e5a13922cc54d48ab63410)#define sys\_port\_trace\_socket\_bind\_enter(socket, addr, addrlen)

2239

[ 2245](group__subsys__tracing__apis__socket.md#gab909132830f1c37eb335ff59c39e47df)#define sys\_port\_trace\_socket\_bind\_exit(socket, ret)

2246

[ 2253](group__subsys__tracing__apis__socket.md#gaabb7458048b7cac6c1cab12e66883bed)#define sys\_port\_trace\_socket\_connect\_enter(socket, addr, addrlen)

2254

[ 2260](group__subsys__tracing__apis__socket.md#ga3504da7dcabcb07cdc0f759ea5964d67)#define sys\_port\_trace\_socket\_connect\_exit(socket, ret)

2261

[ 2267](group__subsys__tracing__apis__socket.md#ga4d56bf430d8c25d3c9b132c7ee492586)#define sys\_port\_trace\_socket\_listen\_enter(socket, backlog)

2268

[ 2274](group__subsys__tracing__apis__socket.md#gac0b0a343ec19cd483ef0b52648d4f107)#define sys\_port\_trace\_socket\_listen\_exit(socket, ret)

2275

[ 2280](group__subsys__tracing__apis__socket.md#ga02ef099cede7c64bb17737a0080e4410)#define sys\_port\_trace\_socket\_accept\_enter(socket)

2281

[ 2289](group__subsys__tracing__apis__socket.md#gace86c4fb481474b73750445b2a11e6f2)#define sys\_port\_trace\_socket\_accept\_exit(socket, addr, addrlen, ret)

2290

[ 2299](group__subsys__tracing__apis__socket.md#gabafa02418677bec9f3137dadc1b50133)#define sys\_port\_trace\_socket\_sendto\_enter(socket, len, flags, dest\_addr, addrlen)

2300

[ 2306](group__subsys__tracing__apis__socket.md#gad88e16f737503a18166680b0b992be7d)#define sys\_port\_trace\_socket\_sendto\_exit(socket, ret)

2307

[ 2314](group__subsys__tracing__apis__socket.md#ga6905a1e8dec1362837ca5c9fab41886f)#define sys\_port\_trace\_socket\_sendmsg\_enter(socket, msg, flags)

2315

[ 2321](group__subsys__tracing__apis__socket.md#ga9ca50f9d8b57aa65300c241043889061)#define sys\_port\_trace\_socket\_sendmsg\_exit(socket, ret)

2322

[ 2331](group__subsys__tracing__apis__socket.md#gafb8183b4148421feac195cf418d2aab3)#define sys\_port\_trace\_socket\_recvfrom\_enter(socket, max\_len, flags, addr, addrlen)

2332

[ 2340](group__subsys__tracing__apis__socket.md#ga94c64423eb1a08bddc570eb1cc32c152)#define sys\_port\_trace\_socket\_recvfrom\_exit(socket, src\_addr, addrlen, ret)

2341

[ 2348](group__subsys__tracing__apis__socket.md#gac11782e26568641c6eb35a278c42dc6a)#define sys\_port\_trace\_socket\_recvmsg\_enter(socket, msg, flags)

2349

[ 2356](group__subsys__tracing__apis__socket.md#ga4a7840ae28ca908b8bfa707db7bae514)#define sys\_port\_trace\_socket\_recvmsg\_exit(socket, msg, ret)

2357

[ 2364](group__subsys__tracing__apis__socket.md#ga27365b99cfe408830a5d057cee944acb)#define sys\_port\_trace\_socket\_fcntl\_enter(socket, cmd, flags)

2365

[ 2371](group__subsys__tracing__apis__socket.md#gacb1376cd3c51f9c92d42315e4a2d0373)#define sys\_port\_trace\_socket\_fcntl\_exit(socket, ret)

2372

[ 2378](group__subsys__tracing__apis__socket.md#ga1d62829f2c8109b396a758ff1ed4ae43)#define sys\_port\_trace\_socket\_ioctl\_enter(socket, req)

2379

[ 2385](group__subsys__tracing__apis__socket.md#ga0ddadc07cdbdd88fddd98ca80ce97e89)#define sys\_port\_trace\_socket\_ioctl\_exit(socket, ret)

2386

[ 2393](group__subsys__tracing__apis__socket.md#ga8f21c61500b256bee9b9c1d902c75dc0)#define sys\_port\_trace\_socket\_poll\_enter(fds, nfds, timeout)

2394

[ 2401](group__subsys__tracing__apis__socket.md#ga968df5694eb381b9c1778824806e7561)#define sys\_port\_trace\_socket\_poll\_exit(fds, nfds, ret)

2402

[ 2409](group__subsys__tracing__apis__socket.md#ga485c1877467ba763181f273e0aedcb7e)#define sys\_port\_trace\_socket\_getsockopt\_enter(socket, level, optname)

2410

[ 2420](group__subsys__tracing__apis__socket.md#ga0144d5f6276eaa117431293e2ee46e74)#define sys\_port\_trace\_socket\_getsockopt\_exit(socket, level, optname, optval, optlen, ret)

2421

[ 2430](group__subsys__tracing__apis__socket.md#gacbe9848da97e63c84a618ef5b7b8a673)#define sys\_port\_trace\_socket\_setsockopt\_enter(socket, level, optname, optval, optlen)

2431

[ 2437](group__subsys__tracing__apis__socket.md#gaebe7a021e6f714f364adc76eadc2220a)#define sys\_port\_trace\_socket\_setsockopt\_exit(socket, ret)

2438

[ 2443](group__subsys__tracing__apis__socket.md#ga307c3e4b2f25f5a20e362418bfff4012)#define sys\_port\_trace\_socket\_getpeername\_enter(socket)

2444

[ 2452](group__subsys__tracing__apis__socket.md#ga0136f94380ec088be2981d35e74be3c6)#define sys\_port\_trace\_socket\_getpeername\_exit(socket, addr, addrlen, ret)

2453

[ 2458](group__subsys__tracing__apis__socket.md#gae9baf2d36c52bd458b60d2d8296c4a6d)#define sys\_port\_trace\_socket\_getsockname\_enter(socket)

2459

[ 2467](group__subsys__tracing__apis__socket.md#gaa2831098447ab830d9470005a1ead43a)#define sys\_port\_trace\_socket\_getsockname\_exit(socket, addr, addrlen, ret)

2468

[ 2476](group__subsys__tracing__apis__socket.md#ga1b639ef77d5d26e80bd863a5dfdf6350)#define sys\_port\_trace\_socket\_socketpair\_enter(family, type, proto, sv)

2477

[ 2484](group__subsys__tracing__apis__socket.md#gae7623cda74ce67a3282185466be0333f)#define sys\_port\_trace\_socket\_socketpair\_exit(socket\_A, socket\_B, ret)

2485 /\* end of subsys\_tracing\_apis\_socket \*/

2487

2493

2494/\*

2495 \* @brief Called by user to generate named events

2496 \*

2497 \* @param name name of event. Tracing subsystems may place a limit on

2498 \* the length of this string

2499 \* @param arg0 arbitrary user-provided data for this event

2500 \* @param arg1 arbitrary user-provided data for this event

2501 \*/

[ 2502](group__subsys__tracing__apis__named.md#ga205bc648bdf0152f8652f04f15cf48af)#define sys\_trace\_named\_event(name, arg0, arg1)

2503 /\* end of subsys\_tracing\_apis\_named \*/

2505

2511

[ 2518](group__subsys__tracing__apis__gpio.md#ga136247e36d2f518d15bf332d8ba5d035)#define sys\_port\_trace\_gpio\_pin\_interrupt\_configure\_enter(port, pin, flags)

2519

[ 2526](group__subsys__tracing__apis__gpio.md#ga78b6201756dc8889aed4dbe2f5e5df08)#define sys\_port\_trace\_gpio\_pin\_interrupt\_configure\_exit(port, pin, ret)

2527

[ 2534](group__subsys__tracing__apis__gpio.md#ga9975f3c53f4cfa2fb4b699691811289d)#define sys\_port\_trace\_gpio\_pin\_configure\_enter(port, pin, flags)

2535

[ 2542](group__subsys__tracing__apis__gpio.md#gad116e0fee008064fa859fcb660735420)#define sys\_port\_trace\_gpio\_pin\_configure\_exit(port, pin, ret)

2543

[ 2551](group__subsys__tracing__apis__gpio.md#ga20672a060ed09777729bc417eb4ac726)#define sys\_port\_trace\_gpio\_port\_get\_direction\_enter(port, map, inputs, outputs)

2552

[ 2558](group__subsys__tracing__apis__gpio.md#gade6194699050e060dc48fa0de50fc930)#define sys\_port\_trace\_gpio\_port\_get\_direction\_exit(port, ret)

2559

[ 2566](group__subsys__tracing__apis__gpio.md#gac5592dce31daf0c8cfcfa09db50fc9e4)#define sys\_port\_trace\_gpio\_pin\_get\_config\_enter(port, pin, flags)

2567

[ 2574](group__subsys__tracing__apis__gpio.md#ga92ada0c9043f9b00803e33c5537abe05)#define sys\_port\_trace\_gpio\_pin\_get\_config\_exit(port, pin, ret)

2575

[ 2581](group__subsys__tracing__apis__gpio.md#gabeea324bb6ee389a6f4f739918e43328)#define sys\_port\_trace\_gpio\_port\_get\_raw\_enter(port, value)

2582

[ 2588](group__subsys__tracing__apis__gpio.md#ga1cbebfa0804f10c410622bb17c02bdb5)#define sys\_port\_trace\_gpio\_port\_get\_raw\_exit(port, ret)

2589

[ 2596](group__subsys__tracing__apis__gpio.md#ga6ddcc9a973b2c938fa67ba9d9de90b43)#define sys\_port\_trace\_gpio\_port\_set\_masked\_raw\_enter(port, mask, value)

2597

[ 2603](group__subsys__tracing__apis__gpio.md#gacc4328675df61fc4d6aea6406328fec6)#define sys\_port\_trace\_gpio\_port\_set\_masked\_raw\_exit(port, ret)

2604

[ 2610](group__subsys__tracing__apis__gpio.md#gae312b54e7983e48519e60be101d2f6cb)#define sys\_port\_trace\_gpio\_port\_set\_bits\_raw\_enter(port, pins)

2611

[ 2617](group__subsys__tracing__apis__gpio.md#ga273a91c09bb777d3f436eab91ae69969)#define sys\_port\_trace\_gpio\_port\_set\_bits\_raw\_exit(port, ret)

2618

[ 2624](group__subsys__tracing__apis__gpio.md#ga8873f6d6af038b43a9f37c0912775608)#define sys\_port\_trace\_gpio\_port\_clear\_bits\_raw\_enter(port, pins)

2625

[ 2631](group__subsys__tracing__apis__gpio.md#ga4a4b88d5a585c0f772dbc8892b801efd)#define sys\_port\_trace\_gpio\_port\_clear\_bits\_raw\_exit(port, ret)

2632

[ 2638](group__subsys__tracing__apis__gpio.md#gaf5d4ac1b95410aa6ba7e543868e59928)#define sys\_port\_trace\_gpio\_port\_toggle\_bits\_enter(port, pins)

2639

[ 2645](group__subsys__tracing__apis__gpio.md#ga70f76ddf530aafa81488ca30d6ea4fb7)#define sys\_port\_trace\_gpio\_port\_toggle\_bits\_exit(port, ret)

2646

[ 2653](group__subsys__tracing__apis__gpio.md#ga3c173c0b612671a9f44fd54efd288ac2)#define sys\_port\_trace\_gpio\_init\_callback\_enter(callback, handler, pin\_mask)

2654

[ 2659](group__subsys__tracing__apis__gpio.md#ga4c130cd12803687e6b8dde1d82aa1d37)#define sys\_port\_trace\_gpio\_init\_callback\_exit(callback)

2660

[ 2666](group__subsys__tracing__apis__gpio.md#ga70cacc72e4696340ed8d53578a13a325)#define sys\_port\_trace\_gpio\_add\_callback\_enter(port, callback)

2667

[ 2673](group__subsys__tracing__apis__gpio.md#gaadca093d8a88c53f7f23ef80300b455a)#define sys\_port\_trace\_gpio\_add\_callback\_exit(port, ret)

2674

[ 2680](group__subsys__tracing__apis__gpio.md#ga2a756f3d1c60c51708492cbb08c9c3b3)#define sys\_port\_trace\_gpio\_remove\_callback\_enter(port, callback)

2681

[ 2687](group__subsys__tracing__apis__gpio.md#gaa7cb1d5a8b2205e610df66ee51dee39b)#define sys\_port\_trace\_gpio\_remove\_callback\_exit(port, ret)

2688

[ 2693](group__subsys__tracing__apis__gpio.md#ga29d20db6e85ac27181b697eeff1a405c)#define sys\_port\_trace\_gpio\_get\_pending\_int\_enter(dev)

2694

[ 2700](group__subsys__tracing__apis__gpio.md#ga118077a21a3037e353fa9ff4ba404be6)#define sys\_port\_trace\_gpio\_get\_pending\_int\_exit(dev, ret)

2701

[ 2708](group__subsys__tracing__apis__gpio.md#ga9cf081771e5f4724b02de3a89eec339c)#define sys\_port\_trace\_gpio\_fire\_callbacks\_enter(list, port, pins)

2709

[ 2715](group__subsys__tracing__apis__gpio.md#gaed3026e592853a9a97c0900a0687974b)#define sys\_port\_trace\_gpio\_fire\_callback(port, callback)

2716 /\* end of subsys\_tracing\_apis\_gpio \*/

2718

2719#if defined(CONFIG\_PERCEPIO\_TRACERECORDER)

2720#include "tracing\_tracerecorder.h"

2721#else

[ 2725](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)void [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)(void);

2726

[ 2730](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)void [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)(void);

2731

[ 2735](group__subsys__tracing__apis.md#ga303fe60fd4de8ddcc02c6920656e326d)void [sys\_trace\_isr\_exit\_to\_scheduler](group__subsys__tracing__apis.md#ga303fe60fd4de8ddcc02c6920656e326d)(void);

2736

[ 2740](group__subsys__tracing__apis.md#gac9b542f78ed796b4b572de19d295c824)void [sys\_trace\_idle](group__subsys__tracing__apis.md#gac9b542f78ed796b4b572de19d295c824)(void);

2741#endif /\* CONFIG\_PERCEPIO\_TRACERECORDER \*/

2742

[ 2746](group__subsys__tracing__apis.md#ga9b5a02fc57b86d38f857597c7a2553f6)#define sys\_trace\_sys\_init\_enter(entry, level)

2747

[ 2751](group__subsys__tracing__apis.md#gacd56f9b376b4639cbe21e12055ca74c7)#define sys\_trace\_sys\_init\_exit(entry, level, result)

2752 /\* end of subsys\_tracing\_apis \*/

2754 /\* end of subsys\_tracing \*/

2756

2757#endif

2758#endif /\* ZEPHYR\_INCLUDE\_TRACING\_TRACING\_H\_ \*/

[sys\_trace\_isr\_exit\_to\_scheduler](group__subsys__tracing__apis.md#ga303fe60fd4de8ddcc02c6920656e326d)

void sys\_trace\_isr\_exit\_to\_scheduler(void)

Called when exiting an ISR and switching to scheduler.

[sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)

void sys\_trace\_isr\_enter(void)

Called when entering an ISR.

[sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)

void sys\_trace\_isr\_exit(void)

Called when exiting an ISR.

[sys\_trace\_idle](group__subsys__tracing__apis.md#gac9b542f78ed796b4b572de19d295c824)

void sys\_trace\_idle(void)

Called when the cpu enters the idle state.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[tracking.h](tracking_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [tracing](dir_c5f5a3ad31e756e37640fc6557a06392.md)
- [tracing.h](tracing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
