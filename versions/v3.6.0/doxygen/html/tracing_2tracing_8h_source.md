---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/tracing_2tracing_8h_source.html
original_path: doxygen/html/tracing_2tracing_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tracing.h

[Go to the documentation of this file.](tracing_2tracing_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_TRACING\_TRACING\_H\_

7#define ZEPHYR\_INCLUDE\_TRACING\_TRACING\_H\_

8

9#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

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

[ 434](group__subsys__tracing__apis__work__q.md#ga88af757f4867f3c65f2d0eff605e0736)#define sys\_port\_trace\_k\_work\_queue\_drain\_enter(queue)

435

[ 441](group__subsys__tracing__apis__work__q.md#ga24ca38662182a01185c9815f3cc87385)#define sys\_port\_trace\_k\_work\_queue\_drain\_exit(queue, ret)

442

[ 447](group__subsys__tracing__apis__work__q.md#ga1ca826910efe678127cdc1f9fdae75e7)#define sys\_port\_trace\_k\_work\_queue\_unplug\_enter(queue)

448

[ 454](group__subsys__tracing__apis__work__q.md#gaae2cf0379cbcf040f36fbba39821be2f)#define sys\_port\_trace\_k\_work\_queue\_unplug\_exit(queue, ret)

455 /\* end of subsys\_tracing\_apis\_work\_q \*/

457

463

[ 468](group__subsys__tracing__apis__work__delayable.md#ga2b7d8ad2173665808061ccc1afd52a06)#define sys\_port\_trace\_k\_work\_delayable\_init(dwork)

469

[ 476](group__subsys__tracing__apis__work__delayable.md#gab71fd0042892d3e6c3e486cee63c9564)#define sys\_port\_trace\_k\_work\_schedule\_for\_queue\_enter(queue, dwork, delay)

477

[ 485](group__subsys__tracing__apis__work__delayable.md#ga4d2160569df2886318039bfdae69d979)#define sys\_port\_trace\_k\_work\_schedule\_for\_queue\_exit(queue, dwork, delay, ret)

486

[ 492](group__subsys__tracing__apis__work__delayable.md#gacda1641af1768d815d3cc3e83c1e2456)#define sys\_port\_trace\_k\_work\_schedule\_enter(dwork, delay)

493

[ 500](group__subsys__tracing__apis__work__delayable.md#ga8c5b232168b9bede0cd73f20513e081c)#define sys\_port\_trace\_k\_work\_schedule\_exit(dwork, delay, ret)

501

[ 508](group__subsys__tracing__apis__work__delayable.md#ga8d6e93ed7d85a17ffdb651e3399b0e16)#define sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_enter(queue, dwork, delay)

509

[ 517](group__subsys__tracing__apis__work__delayable.md#ga636e418e8baf90aaffe3e86b86b3b047)#define sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_exit(queue, dwork, delay, ret)

518

[ 524](group__subsys__tracing__apis__work__delayable.md#gafe5b13e8aae388e9b855081450a065e1)#define sys\_port\_trace\_k\_work\_reschedule\_enter(dwork, delay)

525

[ 532](group__subsys__tracing__apis__work__delayable.md#gaf7789cfa1a943b58e6ee93e8ec9dee57)#define sys\_port\_trace\_k\_work\_reschedule\_exit(dwork, delay, ret)

533

[ 539](group__subsys__tracing__apis__work__delayable.md#ga949c751bc5226d1b46fbf7478c1ee5a3)#define sys\_port\_trace\_k\_work\_flush\_delayable\_enter(dwork, sync)

540

[ 547](group__subsys__tracing__apis__work__delayable.md#gab62f6bce942728370aefa0903a8b79a0)#define sys\_port\_trace\_k\_work\_flush\_delayable\_exit(dwork, sync, ret)

548

[ 553](group__subsys__tracing__apis__work__delayable.md#gae80301ae580a3de83f239d9973b3829d)#define sys\_port\_trace\_k\_work\_cancel\_delayable\_enter(dwork)

554

[ 560](group__subsys__tracing__apis__work__delayable.md#gaef6b739acf79e63e94d172e6667269ce)#define sys\_port\_trace\_k\_work\_cancel\_delayable\_exit(dwork, ret)

561

[ 567](group__subsys__tracing__apis__work__delayable.md#gaaa466d5bd2529b6a8ec5672a0054b8f7)#define sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_enter(dwork, sync)

568

[ 575](group__subsys__tracing__apis__work__delayable.md#ga7f2934c863c45a5bb71d1ba0401a9fe9)#define sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_exit(dwork, sync, ret)

576 /\* end of subsys\_tracing\_apis\_work\_delayable \*/

578

584

[ 589](group__subsys__tracing__apis__work__poll.md#gab720957a26a7e34d06af38200965b809)#define sys\_port\_trace\_k\_work\_poll\_init\_enter(work)

590

[ 595](group__subsys__tracing__apis__work__poll.md#gab3f6f18ab804f82386fbf478e6f1925d)#define sys\_port\_trace\_k\_work\_poll\_init\_exit(work)

596

[ 603](group__subsys__tracing__apis__work__poll.md#gad81098506ed138f835230dec3af15076)#define sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_enter(work\_q, work, timeout)

604

[ 611](group__subsys__tracing__apis__work__poll.md#gabfe31b99d03a49d4b2a5cb9e0403fed9)#define sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_blocking(work\_q, work, timeout)

612

[ 620](group__subsys__tracing__apis__work__poll.md#ga7605f1925f1f0e86d890c896586d8776)#define sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_exit(work\_q, work, timeout, ret)

621

[ 627](group__subsys__tracing__apis__work__poll.md#ga44a78c45b0bae26008d9ae5b410753b7)#define sys\_port\_trace\_k\_work\_poll\_submit\_enter(work, timeout)

628

[ 635](group__subsys__tracing__apis__work__poll.md#ga5917fef8383ffdb6fb3f02a42f940059)#define sys\_port\_trace\_k\_work\_poll\_submit\_exit(work, timeout, ret)

636

[ 641](group__subsys__tracing__apis__work__poll.md#ga57e8e57814797b50e7e87e06503dc1f9)#define sys\_port\_trace\_k\_work\_poll\_cancel\_enter(work)

642

[ 648](group__subsys__tracing__apis__work__poll.md#ga3045330b53fa50489a2d3a17b14aa295)#define sys\_port\_trace\_k\_work\_poll\_cancel\_exit(work, ret)

649 /\* end of subsys\_tracing\_apis\_work\_poll \*/

651

657

[ 662](group__subsys__tracing__apis__poll.md#ga83053d6bfc7ad8b070741f38d6606bc1)#define sys\_port\_trace\_k\_poll\_api\_event\_init(event)

663

[ 668](group__subsys__tracing__apis__poll.md#gac44ecc90dc3b407b09e2d45590496e17)#define sys\_port\_trace\_k\_poll\_api\_poll\_enter(events)

669

[ 675](group__subsys__tracing__apis__poll.md#gaf8794133d6ddc29740dfc73b9edbee12)#define sys\_port\_trace\_k\_poll\_api\_poll\_exit(events, ret)

676

[ 681](group__subsys__tracing__apis__poll.md#gaab0dc4527d89c0e0b41d21a76ecfb120)#define sys\_port\_trace\_k\_poll\_api\_signal\_init(signal)

682

[ 687](group__subsys__tracing__apis__poll.md#ga5addc3fa68d6afe454ad7721c8fa17c4)#define sys\_port\_trace\_k\_poll\_api\_signal\_reset(signal)

688

[ 693](group__subsys__tracing__apis__poll.md#ga336dab8d86b07908e641e9845d75be70)#define sys\_port\_trace\_k\_poll\_api\_signal\_check(signal)

694

[ 700](group__subsys__tracing__apis__poll.md#gaeb1f753becfbe92f089eed23825acb4b)#define sys\_port\_trace\_k\_poll\_api\_signal\_raise(signal, ret)

701 /\* end of subsys\_tracing\_apis\_poll \*/

703

709

[ 715](group__subsys__tracing__apis__sem.md#gace327a058d058a940df14c95b031795b)#define sys\_port\_trace\_k\_sem\_init(sem, ret)

716

[ 721](group__subsys__tracing__apis__sem.md#ga552d549c1e8346dbe1445a93e7fc17e9)#define sys\_port\_trace\_k\_sem\_give\_enter(sem)

722

[ 727](group__subsys__tracing__apis__sem.md#ga70d31e53b6e72d2343aa009fa5a98054)#define sys\_port\_trace\_k\_sem\_give\_exit(sem)

728

[ 734](group__subsys__tracing__apis__sem.md#ga216fe8bc373edbb0b48fc4ca7b1816c9)#define sys\_port\_trace\_k\_sem\_take\_enter(sem, timeout)

735

[ 741](group__subsys__tracing__apis__sem.md#gade7546e098a12ce6d935b39f4978ac8d)#define sys\_port\_trace\_k\_sem\_take\_blocking(sem, timeout)

742

[ 749](group__subsys__tracing__apis__sem.md#ga8085db47b86d539e65c107bb33469ee2)#define sys\_port\_trace\_k\_sem\_take\_exit(sem, timeout, ret)

750

[ 755](group__subsys__tracing__apis__sem.md#ga1300af0463f93de0b29751b7a20307cb)#define sys\_port\_trace\_k\_sem\_reset(sem)

756 /\* end of subsys\_tracing\_apis\_sem \*/

758

764

[ 770](group__subsys__tracing__apis__mutex.md#gaefe38feb9aa638b35fd4e723afcebf37)#define sys\_port\_trace\_k\_mutex\_init(mutex, ret)

771

[ 777](group__subsys__tracing__apis__mutex.md#ga5ed2f76aec9c128f163a2e3159e29c80)#define sys\_port\_trace\_k\_mutex\_lock\_enter(mutex, timeout)

778

[ 784](group__subsys__tracing__apis__mutex.md#gaae15023daa241367414afaab085acd2c)#define sys\_port\_trace\_k\_mutex\_lock\_blocking(mutex, timeout)

785

[ 792](group__subsys__tracing__apis__mutex.md#ga31bdc51723303de3bc93d41b36149e57)#define sys\_port\_trace\_k\_mutex\_lock\_exit(mutex, timeout, ret)

793

[ 798](group__subsys__tracing__apis__mutex.md#ga39611be3e36741442a62a98adeef9ee7)#define sys\_port\_trace\_k\_mutex\_unlock\_enter(mutex)

799

[ 803](group__subsys__tracing__apis__mutex.md#ga53c7bd3fc251865ae1a6e79da7a001b1)#define sys\_port\_trace\_k\_mutex\_unlock\_exit(mutex, ret)

804 /\* end of subsys\_tracing\_apis\_mutex \*/

806

812

[ 818](group__subsys__tracing__apis__condvar.md#gab9d1ce42bb6e6c2a762ed242ba364fa8)#define sys\_port\_trace\_k\_condvar\_init(condvar, ret)

819

[ 824](group__subsys__tracing__apis__condvar.md#ga4b0f79f49b710928a38dc10ce22039e5)#define sys\_port\_trace\_k\_condvar\_signal\_enter(condvar)

825

[ 831](group__subsys__tracing__apis__condvar.md#gab946fada5e51a069a13a21736a500669)#define sys\_port\_trace\_k\_condvar\_signal\_blocking(condvar, timeout)

832

[ 838](group__subsys__tracing__apis__condvar.md#ga3992a8afdc375a4ecaa83cac302c7198)#define sys\_port\_trace\_k\_condvar\_signal\_exit(condvar, ret)

839

[ 844](group__subsys__tracing__apis__condvar.md#gadd5affb8afb73b5f76e24477d3d853bb)#define sys\_port\_trace\_k\_condvar\_broadcast\_enter(condvar)

845

[ 851](group__subsys__tracing__apis__condvar.md#ga9a013d5ab1bdd0752ec9bafb2ef4f370)#define sys\_port\_trace\_k\_condvar\_broadcast\_exit(condvar, ret)

852

[ 857](group__subsys__tracing__apis__condvar.md#ga30572aefa29d161af4e9e1841c59d98c)#define sys\_port\_trace\_k\_condvar\_wait\_enter(condvar)

858

[ 864](group__subsys__tracing__apis__condvar.md#ga07e95689443fb483886695a1533a5b08)#define sys\_port\_trace\_k\_condvar\_wait\_exit(condvar, ret)

865 /\* end of subsys\_tracing\_apis\_condvar \*/

867

873

[ 878](group__subsys__tracing__apis__queue.md#ga40e74ce284e349d9e6fbe948c29d574f)#define sys\_port\_trace\_k\_queue\_init(queue)

879

[ 884](group__subsys__tracing__apis__queue.md#ga8df6412be1cd3350c2b1976c7f7c8f4c)#define sys\_port\_trace\_k\_queue\_cancel\_wait(queue)

885

[ 891](group__subsys__tracing__apis__queue.md#ga0e38a81f47c44e1be515b375f384a2d2)#define sys\_port\_trace\_k\_queue\_queue\_insert\_enter(queue, alloc)

892

[ 899](group__subsys__tracing__apis__queue.md#ga3e51a4120f2ff7560ad494620c801886)#define sys\_port\_trace\_k\_queue\_queue\_insert\_blocking(queue, alloc, timeout)

900

[ 907](group__subsys__tracing__apis__queue.md#ga9fe7ee8315505734bf33d71083190533)#define sys\_port\_trace\_k\_queue\_queue\_insert\_exit(queue, alloc, ret)

908

[ 913](group__subsys__tracing__apis__queue.md#ga541411a2d9856fe01ed2e532a7e33db4)#define sys\_port\_trace\_k\_queue\_append\_enter(queue)

914

[ 919](group__subsys__tracing__apis__queue.md#ga1c1a038ffa1da2efd495f769f12bc685)#define sys\_port\_trace\_k\_queue\_append\_exit(queue)

920

[ 925](group__subsys__tracing__apis__queue.md#ga5ef57f07d5ff8c730893f96b174f967a)#define sys\_port\_trace\_k\_queue\_alloc\_append\_enter(queue)

926

[ 932](group__subsys__tracing__apis__queue.md#ga54601544ad750fb6a5afa725a19ce269)#define sys\_port\_trace\_k\_queue\_alloc\_append\_exit(queue, ret)

933

[ 938](group__subsys__tracing__apis__queue.md#ga90f15dc66fffd87e2b4fb66fb8bae4b1)#define sys\_port\_trace\_k\_queue\_prepend\_enter(queue)

939

[ 944](group__subsys__tracing__apis__queue.md#ga023a6fee85616ae5f32b5fa4b29d29e5)#define sys\_port\_trace\_k\_queue\_prepend\_exit(queue)

945

[ 950](group__subsys__tracing__apis__queue.md#gaae4196d40be1a74439a1b7010626da17)#define sys\_port\_trace\_k\_queue\_alloc\_prepend\_enter(queue)

951

[ 957](group__subsys__tracing__apis__queue.md#ga2d7ff756f5c017d7b3f10787716b5684)#define sys\_port\_trace\_k\_queue\_alloc\_prepend\_exit(queue, ret)

958

[ 963](group__subsys__tracing__apis__queue.md#ga4e78ca5d7d927b912e09829b51e7330c)#define sys\_port\_trace\_k\_queue\_insert\_enter(queue)

964

[ 970](group__subsys__tracing__apis__queue.md#gaad04f21122c554c33ef0cb394abf6df1)#define sys\_port\_trace\_k\_queue\_insert\_blocking(queue, timeout)

971

[ 976](group__subsys__tracing__apis__queue.md#ga69ca963f74777d9d351c9d20fe9dff62)#define sys\_port\_trace\_k\_queue\_insert\_exit(queue)

977

[ 982](group__subsys__tracing__apis__queue.md#ga777cfd6ee6ad016c2bbc519a490c0672)#define sys\_port\_trace\_k\_queue\_append\_list\_enter(queue)

983

[ 989](group__subsys__tracing__apis__queue.md#ga215aca3523a17e31d4d36d3d95f28544)#define sys\_port\_trace\_k\_queue\_append\_list\_exit(queue, ret)

990

[ 995](group__subsys__tracing__apis__queue.md#ga888a4a39d0c33fab4243c64e42011856)#define sys\_port\_trace\_k\_queue\_merge\_slist\_enter(queue)

996

[ 1002](group__subsys__tracing__apis__queue.md#ga87336faf8e19c64bcbf188452e336639)#define sys\_port\_trace\_k\_queue\_merge\_slist\_exit(queue, ret)

1003

[ 1009](group__subsys__tracing__apis__queue.md#ga59c1bac1a34c950c7ca324fc8d853acb)#define sys\_port\_trace\_k\_queue\_get\_enter(queue, timeout)

1010

[ 1016](group__subsys__tracing__apis__queue.md#gad83deb664f66df825b290b17f97156c7)#define sys\_port\_trace\_k\_queue\_get\_blocking(queue, timeout)

1017

[ 1024](group__subsys__tracing__apis__queue.md#ga8afd074bab6b31d60169a72db51ef76c)#define sys\_port\_trace\_k\_queue\_get\_exit(queue, timeout, ret)

1025

[ 1030](group__subsys__tracing__apis__queue.md#gacc2e453e717c654318dfd02e09288636)#define sys\_port\_trace\_k\_queue\_remove\_enter(queue)

1031

[ 1037](group__subsys__tracing__apis__queue.md#ga1df298e35d176ca79924a9b534bb115c)#define sys\_port\_trace\_k\_queue\_remove\_exit(queue, ret)

1038

[ 1043](group__subsys__tracing__apis__queue.md#ga2842e4d5e778016ea70d5b860f217421)#define sys\_port\_trace\_k\_queue\_unique\_append\_enter(queue)

1044

[ 1051](group__subsys__tracing__apis__queue.md#ga830dfc12a35c0c001abfe2cbf89387aa)#define sys\_port\_trace\_k\_queue\_unique\_append\_exit(queue, ret)

1052

[ 1058](group__subsys__tracing__apis__queue.md#ga1cb5384c1eccc5d40c3e748dd1990cce)#define sys\_port\_trace\_k\_queue\_peek\_head(queue, ret)

1059

[ 1065](group__subsys__tracing__apis__queue.md#gac28c33f0457d7e8f99e20d0fc55427ee)#define sys\_port\_trace\_k\_queue\_peek\_tail(queue, ret)

1066 /\* end of subsys\_tracing\_apis\_queue \*/

1068

1074

[ 1079](group__subsys__tracing__apis__fifo.md#gac0da5eca137a970c67b7b94a568c93e6)#define sys\_port\_trace\_k\_fifo\_init\_enter(fifo)

1080

[ 1085](group__subsys__tracing__apis__fifo.md#gaaf6c7c710377f449d52c5d6f5f7103c8)#define sys\_port\_trace\_k\_fifo\_init\_exit(fifo)

1086

[ 1091](group__subsys__tracing__apis__fifo.md#ga81e706aff605468683a96b14940745e7)#define sys\_port\_trace\_k\_fifo\_cancel\_wait\_enter(fifo)

1092

[ 1097](group__subsys__tracing__apis__fifo.md#ga03ccb2bb3141c2842959ba77e4cd7337)#define sys\_port\_trace\_k\_fifo\_cancel\_wait\_exit(fifo)

1098

[ 1104](group__subsys__tracing__apis__fifo.md#gaac5f6b9e77dad9de4652d24502ab46d0)#define sys\_port\_trace\_k\_fifo\_put\_enter(fifo, data)

1105

[ 1111](group__subsys__tracing__apis__fifo.md#ga7a1d15a538f23d2b7f290435803cd73e)#define sys\_port\_trace\_k\_fifo\_put\_exit(fifo, data)

1112

[ 1118](group__subsys__tracing__apis__fifo.md#ga9c433ad8dc99ac38b8d5b4755da05c67)#define sys\_port\_trace\_k\_fifo\_alloc\_put\_enter(fifo, data)

1119

[ 1126](group__subsys__tracing__apis__fifo.md#gad9871fb1487a387a4f73e94bccb99a6d)#define sys\_port\_trace\_k\_fifo\_alloc\_put\_exit(fifo, data, ret)

1127

[ 1134](group__subsys__tracing__apis__fifo.md#gace20fdce59a99b92c8ac3711c4085b28)#define sys\_port\_trace\_k\_fifo\_put\_list\_enter(fifo, head, tail)

1135

[ 1142](group__subsys__tracing__apis__fifo.md#ga739360e2cefa158f22ce20a1e9369aea)#define sys\_port\_trace\_k\_fifo\_put\_list\_exit(fifo, head, tail)

1143

[ 1149](group__subsys__tracing__apis__fifo.md#gaf975d817bdefc64b9329330f6cd88d21)#define sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_enter(fifo, list)

1150

[ 1156](group__subsys__tracing__apis__fifo.md#gae1c620ec17a1f7a899a1e5cba996644e)#define sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_exit(fifo, list)

1157

[ 1163](group__subsys__tracing__apis__fifo.md#gaa3539eea74888c6257c5f5d456748155)#define sys\_port\_trace\_k\_fifo\_get\_enter(fifo, timeout)

1164

[ 1171](group__subsys__tracing__apis__fifo.md#gae6f06386f224063ee756e8ff0000dfe4)#define sys\_port\_trace\_k\_fifo\_get\_exit(fifo, timeout, ret)

1172

[ 1177](group__subsys__tracing__apis__fifo.md#gab0fea5751e0296e623606e54efe5687b)#define sys\_port\_trace\_k\_fifo\_peek\_head\_enter(fifo)

1178

[ 1184](group__subsys__tracing__apis__fifo.md#ga06b74415be416b137092cb72187c1fb6)#define sys\_port\_trace\_k\_fifo\_peek\_head\_exit(fifo, ret)

1185

[ 1190](group__subsys__tracing__apis__fifo.md#gad9f9b3193ed2c7270030036aef8d343d)#define sys\_port\_trace\_k\_fifo\_peek\_tail\_enter(fifo)

1191

[ 1197](group__subsys__tracing__apis__fifo.md#gae33baafbaac06ada7d6b53026a973d81)#define sys\_port\_trace\_k\_fifo\_peek\_tail\_exit(fifo, ret)

1198 /\* end of subsys\_tracing\_apis\_fifo \*/

1200

1206

[ 1211](group__subsys__tracing__apis__lifo.md#gaad81b60363467b56d887baee8c8b5bf2)#define sys\_port\_trace\_k\_lifo\_init\_enter(lifo)

1212

[ 1217](group__subsys__tracing__apis__lifo.md#ga4f08168ded97456265abb3a903585ecf)#define sys\_port\_trace\_k\_lifo\_init\_exit(lifo)

1218

[ 1224](group__subsys__tracing__apis__lifo.md#gafd9c45a171a2fb146defa356ff0bc0f5)#define sys\_port\_trace\_k\_lifo\_put\_enter(lifo, data)

1225

[ 1231](group__subsys__tracing__apis__lifo.md#ga0e5372c37bdd3a47adf11ab9d3a5e22d)#define sys\_port\_trace\_k\_lifo\_put\_exit(lifo, data)

1232

[ 1238](group__subsys__tracing__apis__lifo.md#ga0d9717f4b43e344518cc451a2fe9d224)#define sys\_port\_trace\_k\_lifo\_alloc\_put\_enter(lifo, data)

1239

[ 1246](group__subsys__tracing__apis__lifo.md#ga19bb748367aba8f576e72cdc30834ab1)#define sys\_port\_trace\_k\_lifo\_alloc\_put\_exit(lifo, data, ret)

1247

[ 1253](group__subsys__tracing__apis__lifo.md#ga61556928453492dc6ed4efc999668f01)#define sys\_port\_trace\_k\_lifo\_get\_enter(lifo, timeout)

1254

[ 1261](group__subsys__tracing__apis__lifo.md#ga2f7e8e680cac03844ca5dbab0438a754)#define sys\_port\_trace\_k\_lifo\_get\_exit(lifo, timeout, ret)

1262 /\* end of subsys\_tracing\_apis\_lifo \*/

1264

1270

[ 1275](group__subsys__tracing__apis__stack.md#ga5bb95f74d8bc3eed2525be20c444824f)#define sys\_port\_trace\_k\_stack\_init(stack)

1276

[ 1281](group__subsys__tracing__apis__stack.md#gaa10d6cb275914bb25ad6ffad12807480)#define sys\_port\_trace\_k\_stack\_alloc\_init\_enter(stack)

1282

[ 1288](group__subsys__tracing__apis__stack.md#gabaabe367b83b39248112eadb07bdf714)#define sys\_port\_trace\_k\_stack\_alloc\_init\_exit(stack, ret)

1289

[ 1294](group__subsys__tracing__apis__stack.md#gaf8357d3d9a2cb8de7ba0b3473c5b063c)#define sys\_port\_trace\_k\_stack\_cleanup\_enter(stack)

1295

[ 1301](group__subsys__tracing__apis__stack.md#ga2225cab95abdd8188087e6a98641ec0c)#define sys\_port\_trace\_k\_stack\_cleanup\_exit(stack, ret)

1302

[ 1307](group__subsys__tracing__apis__stack.md#gad6a42d93265b53540baab5c59f55fbf6)#define sys\_port\_trace\_k\_stack\_push\_enter(stack)

1308

[ 1314](group__subsys__tracing__apis__stack.md#ga203d32ef138d041aa0c20db8a75ccd6a)#define sys\_port\_trace\_k\_stack\_push\_exit(stack, ret)

1315

[ 1321](group__subsys__tracing__apis__stack.md#gaaf9ac378b0bbf09af91c1987dc5b777e)#define sys\_port\_trace\_k\_stack\_pop\_enter(stack, timeout)

1322

[ 1328](group__subsys__tracing__apis__stack.md#gacbdaf326a104d3bdcd4ceb5ec72c9b4f)#define sys\_port\_trace\_k\_stack\_pop\_blocking(stack, timeout)

1329

[ 1336](group__subsys__tracing__apis__stack.md#ga11280d48a97cca4b65210791f9d8c591)#define sys\_port\_trace\_k\_stack\_pop\_exit(stack, timeout, ret)

1337 /\* end of subsys\_tracing\_apis\_stack \*/

1339

1345

[ 1350](group__subsys__tracing__apis__msgq.md#ga94eae512e590d61c1c74f5d7eb552d50)#define sys\_port\_trace\_k\_msgq\_init(msgq)

1351

[ 1356](group__subsys__tracing__apis__msgq.md#ga392ac9fe978d78ee1ca23c27f93e5053)#define sys\_port\_trace\_k\_msgq\_alloc\_init\_enter(msgq)

1357

[ 1363](group__subsys__tracing__apis__msgq.md#ga60973fcaae9be0a6b292bf2a5dfb4fb2)#define sys\_port\_trace\_k\_msgq\_alloc\_init\_exit(msgq, ret)

1364

[ 1369](group__subsys__tracing__apis__msgq.md#ga370c16cd808037db5dc605e91d3c21b8)#define sys\_port\_trace\_k\_msgq\_cleanup\_enter(msgq)

1370

[ 1376](group__subsys__tracing__apis__msgq.md#gaff32cb729fd32c7b008191cac1e2c881)#define sys\_port\_trace\_k\_msgq\_cleanup\_exit(msgq, ret)

1377

[ 1383](group__subsys__tracing__apis__msgq.md#ga829e2b0d3420079777362f0b78f28d50)#define sys\_port\_trace\_k\_msgq\_put\_enter(msgq, timeout)

1384

[ 1390](group__subsys__tracing__apis__msgq.md#gaead1e1b345e029017b1951a3d112554f)#define sys\_port\_trace\_k\_msgq\_put\_blocking(msgq, timeout)

1391

[ 1398](group__subsys__tracing__apis__msgq.md#gab4794be3e4a68af3ada3667d98286747)#define sys\_port\_trace\_k\_msgq\_put\_exit(msgq, timeout, ret)

1399

[ 1405](group__subsys__tracing__apis__msgq.md#ga1d79dbc50b8ddd0d3db803b7c747ede5)#define sys\_port\_trace\_k\_msgq\_get\_enter(msgq, timeout)

1406

[ 1412](group__subsys__tracing__apis__msgq.md#ga448baf7df9ec1abc4ec3a12609400b68)#define sys\_port\_trace\_k\_msgq\_get\_blocking(msgq, timeout)

1413

[ 1420](group__subsys__tracing__apis__msgq.md#ga2a549f567cda0646b853a9cb0b7e1eb2)#define sys\_port\_trace\_k\_msgq\_get\_exit(msgq, timeout, ret)

1421

[ 1427](group__subsys__tracing__apis__msgq.md#gad11e9f22177bf004f95d23750a2046a3)#define sys\_port\_trace\_k\_msgq\_peek(msgq, ret)

1428

[ 1433](group__subsys__tracing__apis__msgq.md#ga91530d1c6d10ce72cc5c9319c28b5e32)#define sys\_port\_trace\_k\_msgq\_purge(msgq)

1434 /\* end of subsys\_tracing\_apis\_msgq \*/

1436

1442

[ 1447](group__subsys__tracing__apis__mbox.md#ga67187d636152a34614c4213c47ea7509)#define sys\_port\_trace\_k\_mbox\_init(mbox)

1448

[ 1454](group__subsys__tracing__apis__mbox.md#gac7b683e1e33c42e3e04f84a2c2b19811)#define sys\_port\_trace\_k\_mbox\_message\_put\_enter(mbox, timeout)

1455

[ 1461](group__subsys__tracing__apis__mbox.md#ga6a04c6ea1072d7c858a23c845e76565d)#define sys\_port\_trace\_k\_mbox\_message\_put\_blocking(mbox, timeout)

1462

[ 1469](group__subsys__tracing__apis__mbox.md#ga2ab3697623a198ea15ad644ce19335fb)#define sys\_port\_trace\_k\_mbox\_message\_put\_exit(mbox, timeout, ret)

1470

[ 1476](group__subsys__tracing__apis__mbox.md#gaba437af59b1a8c663fa7d39eafa78ee6)#define sys\_port\_trace\_k\_mbox\_put\_enter(mbox, timeout)

1477

[ 1484](group__subsys__tracing__apis__mbox.md#ga07148a910c33c881d531ed495b23c081)#define sys\_port\_trace\_k\_mbox\_put\_exit(mbox, timeout, ret)

1485

[ 1491](group__subsys__tracing__apis__mbox.md#ga7dd281ffa54a3d32c7380e294e18ef5d)#define sys\_port\_trace\_k\_mbox\_async\_put\_enter(mbox, sem)

1492

[ 1498](group__subsys__tracing__apis__mbox.md#gab39d7bfdfc0c5ed394e7819a3048741e)#define sys\_port\_trace\_k\_mbox\_async\_put\_exit(mbox, sem)

1499

[ 1505](group__subsys__tracing__apis__mbox.md#ga30ad94a6f1267931ff8d401fb4a75be3)#define sys\_port\_trace\_k\_mbox\_get\_enter(mbox, timeout)

1506

[ 1512](group__subsys__tracing__apis__mbox.md#ga4977171638fed999e4485cc035016c10)#define sys\_port\_trace\_k\_mbox\_get\_blocking(mbox, timeout)

1513

[ 1520](group__subsys__tracing__apis__mbox.md#gaaa8261b9fa07c97308b46a9b7100aee6)#define sys\_port\_trace\_k\_mbox\_get\_exit(mbox, timeout, ret)

1521

[ 1526](group__subsys__tracing__apis__mbox.md#gacef2016dc5620371401e55e7005a18c3)#define sys\_port\_trace\_k\_mbox\_data\_get(rx\_msg)

1527 /\* end of subsys\_tracing\_apis\_mbox \*/

1529

1535

[ 1540](group__subsys__tracing__apis__pipe.md#ga1d51dc4110aba7c23de9b8f47e7ad5a8)#define sys\_port\_trace\_k\_pipe\_init(pipe)

1541

[ 1546](group__subsys__tracing__apis__pipe.md#ga63bc37ca2dbcf84fc87e13fdb2f21834)#define sys\_port\_trace\_k\_pipe\_cleanup\_enter(pipe)

1547

[ 1553](group__subsys__tracing__apis__pipe.md#gaa367f4e1019380dde77ee881f22ab278)#define sys\_port\_trace\_k\_pipe\_cleanup\_exit(pipe, ret)

1554

[ 1559](group__subsys__tracing__apis__pipe.md#ga6fdcad7deb3be98acd88cd8febd39247)#define sys\_port\_trace\_k\_pipe\_alloc\_init\_enter(pipe)

1560

[ 1566](group__subsys__tracing__apis__pipe.md#ga011af7de686c1b360f0696a7dd1b173f)#define sys\_port\_trace\_k\_pipe\_alloc\_init\_exit(pipe, ret)

1567

[ 1572](group__subsys__tracing__apis__pipe.md#ga9e3f6058f2370488cfb4d57676c3d5cd)#define sys\_port\_trace\_k\_pipe\_flush\_enter(pipe)

1573

[ 1578](group__subsys__tracing__apis__pipe.md#gafdba63af20781901576344ef198da8a4)#define sys\_port\_trace\_k\_pipe\_flush\_exit(pipe)

1579

[ 1584](group__subsys__tracing__apis__pipe.md#gaa81b667947689ac7edb866cb7c5beb81)#define sys\_port\_trace\_k\_pipe\_buffer\_flush\_enter(pipe)

1585

[ 1590](group__subsys__tracing__apis__pipe.md#ga47d9a997d8daff89a1c4a41ac4bb327e)#define sys\_port\_trace\_k\_pipe\_buffer\_flush\_exit(pipe)

1591

[ 1597](group__subsys__tracing__apis__pipe.md#gad16f0673669f9700ebd3e4fc0b1466d8)#define sys\_port\_trace\_k\_pipe\_put\_enter(pipe, timeout)

1598

[ 1604](group__subsys__tracing__apis__pipe.md#ga314cffd927b410d3670f39a774a42206)#define sys\_port\_trace\_k\_pipe\_put\_blocking(pipe, timeout)

1605

[ 1612](group__subsys__tracing__apis__pipe.md#ga20a131258373e32379273dd0ff08a672)#define sys\_port\_trace\_k\_pipe\_put\_exit(pipe, timeout, ret)

1613

[ 1619](group__subsys__tracing__apis__pipe.md#gaafa10362c5042f0f2e02b40b79768dbb)#define sys\_port\_trace\_k\_pipe\_get\_enter(pipe, timeout)

1620

[ 1626](group__subsys__tracing__apis__pipe.md#ga2dfb7cfd0b08beac72d254ac3063d42c)#define sys\_port\_trace\_k\_pipe\_get\_blocking(pipe, timeout)

1627

[ 1634](group__subsys__tracing__apis__pipe.md#ga192cb7bafd2d04898b13e30aa96d483d)#define sys\_port\_trace\_k\_pipe\_get\_exit(pipe, timeout, ret)

1635 /\* end of subsys\_tracing\_apis\_pipe \*/

1637

1643

[ 1648](group__subsys__tracing__apis__heap.md#gaa9eb0a2ff9da8a892ab62e45fe4e4ddb)#define sys\_port\_trace\_k\_heap\_init(h)

1649

[ 1655](group__subsys__tracing__apis__heap.md#gaa49162a735def3b0389cc30bd4654533)#define sys\_port\_trace\_k\_heap\_aligned\_alloc\_enter(h, timeout)

1656

[ 1662](group__subsys__tracing__apis__heap.md#gada1001c802bcc55437ffd8f4e2f23bef)#define sys\_port\_trace\_k\_heap\_aligned\_alloc\_blocking(h, timeout)

1663

[ 1670](group__subsys__tracing__apis__heap.md#ga3833f13065d967acafd50e3089556944)#define sys\_port\_trace\_k\_heap\_aligned\_alloc\_exit(h, timeout, ret)

1671

[ 1677](group__subsys__tracing__apis__heap.md#gadf8441b3c430499c8444a7c73bae1931)#define sys\_port\_trace\_k\_heap\_alloc\_enter(h, timeout)

1678

[ 1685](group__subsys__tracing__apis__heap.md#gad696bba7ffe71beb01520ab27b483307)#define sys\_port\_trace\_k\_heap\_alloc\_exit(h, timeout, ret)

1686

[ 1691](group__subsys__tracing__apis__heap.md#ga6f9c92a02d32af203752c59615e34096)#define sys\_port\_trace\_k\_heap\_free(h)

1692

[ 1697](group__subsys__tracing__apis__heap.md#ga12de856dc1fc2cb261497b3ef8b09e9e)#define sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_enter(heap)

1698

[ 1704](group__subsys__tracing__apis__heap.md#ga6d7a77c282f8229e0b366d57ba33ed04)#define sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_exit(heap, ret)

1705

[ 1710](group__subsys__tracing__apis__heap.md#ga478745a9e6cbc1a7b6bc9a2fc1763ca5)#define sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_enter(heap)

1711

[ 1717](group__subsys__tracing__apis__heap.md#ga4d612b7ec5d992c6e8170f35a1ce6c03)#define sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_exit(heap, ret)

1718

[ 1724](group__subsys__tracing__apis__heap.md#gaf4dd86f13041c12cf18696fcff2ba9aa)#define sys\_port\_trace\_k\_heap\_sys\_k\_free\_enter(heap, heap\_ref)

1725

[ 1731](group__subsys__tracing__apis__heap.md#gaf2865a12ffee2135e2d798bdf5fa9c98)#define sys\_port\_trace\_k\_heap\_sys\_k\_free\_exit(heap, heap\_ref)

1732

[ 1737](group__subsys__tracing__apis__heap.md#ga60e3dd5434ba9c912a4f2332f579318f)#define sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_enter(heap)

1738

[ 1744](group__subsys__tracing__apis__heap.md#ga6be2fe00eabc9bffaf635cfb14714e4a)#define sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_exit(heap, ret)

1745 /\* end of subsys\_tracing\_apis\_heap \*/

1747

1753

[ 1759](group__subsys__tracing__apis__mslab.md#ga5a769fffc7611a57c8490b3f5c6047a5)#define sys\_port\_trace\_k\_mem\_slab\_init(slab, rc)

1760

[ 1766](group__subsys__tracing__apis__mslab.md#gac1ac5f1393b87ea84c2d53f08c251ff2)#define sys\_port\_trace\_k\_mem\_slab\_alloc\_enter(slab, timeout)

1767

[ 1773](group__subsys__tracing__apis__mslab.md#gaea77ffa2dbbfad9ff2fec0041b0dbc59)#define sys\_port\_trace\_k\_mem\_slab\_alloc\_blocking(slab, timeout)

1774

[ 1781](group__subsys__tracing__apis__mslab.md#ga237bb89733ca9c483ef6b9ab6dd920a4)#define sys\_port\_trace\_k\_mem\_slab\_alloc\_exit(slab, timeout, ret)

1782

[ 1787](group__subsys__tracing__apis__mslab.md#ga22fc4609185f6ddffd0abc85f3976914)#define sys\_port\_trace\_k\_mem\_slab\_free\_enter(slab)

1788

[ 1793](group__subsys__tracing__apis__mslab.md#ga81dd030d4052e3092479e19616b4baec)#define sys\_port\_trace\_k\_mem\_slab\_free\_exit(slab)

1794 /\* end of subsys\_tracing\_apis\_mslab \*/

1796

1802

[ 1807](group__subsys__tracing__apis__timer.md#ga03a70d84ea0227829fb9528b0156c147)#define sys\_port\_trace\_k\_timer\_init(timer)

1808

[ 1815](group__subsys__tracing__apis__timer.md#ga95b998ea6bf00692cb654a18787ab185)#define sys\_port\_trace\_k\_timer\_start(timer, duration, period)

1816

[ 1821](group__subsys__tracing__apis__timer.md#ga81b6cba81190cc61cdd33f4ddb6f4550)#define sys\_port\_trace\_k\_timer\_stop(timer)

1822

[ 1827](group__subsys__tracing__apis__timer.md#ga0adf7e6ca5bdd89b7676836101ef37df)#define sys\_port\_trace\_k\_timer\_status\_sync\_enter(timer)

1828

[ 1834](group__subsys__tracing__apis__timer.md#gaa3cd4ca118fd987560ae1855c904e1aa)#define sys\_port\_trace\_k\_timer\_status\_sync\_blocking(timer, timeout)

1835

[ 1841](group__subsys__tracing__apis__timer.md#gab51aa6682136eb86a4fd141f61ece779)#define sys\_port\_trace\_k\_timer\_status\_sync\_exit(timer, result)

1842 /\* end of subsys\_tracing\_apis\_timer \*/

1844

1850

[ 1855](group__subsys__tracing__apis__event.md#gae212c1b330d476613629501d62be0994)#define sys\_port\_trace\_k\_event\_init(event)

1856

[ 1863](group__subsys__tracing__apis__event.md#ga20092082696c6c9fe3b8870bd3523b52)#define sys\_port\_trace\_k\_event\_post\_enter(event, events, events\_mask)

1864

[ 1871](group__subsys__tracing__apis__event.md#gac58a047db800cca608087d6b2cec37f9)#define sys\_port\_trace\_k\_event\_post\_exit(event, events, events\_mask)

1872

[ 1880](group__subsys__tracing__apis__event.md#ga6b01461ff2fa0cf2c3c19dbed2f8c4c3)#define sys\_port\_trace\_k\_event\_wait\_enter(event, events, options, timeout)

1881

[ 1889](group__subsys__tracing__apis__event.md#ga008a96d80f3f90dcffbc74f43d66b9be)#define sys\_port\_trace\_k\_event\_wait\_blocking(event, events, options, timeout)

1890

[ 1897](group__subsys__tracing__apis__event.md#ga874698f8eff5237fefacc1be761b2661)#define sys\_port\_trace\_k\_event\_wait\_exit(event, events, ret)

1898 /\* end of subsys\_tracing\_apis\_event \*/

1900

1906

[ 1911](group__subsys__tracing__apis__pm__system.md#ga1d8c01fe22ef0f7ac8fdfb47de55f58e)#define sys\_port\_trace\_pm\_system\_suspend\_enter(ticks)

1912

[ 1918](group__subsys__tracing__apis__pm__system.md#gaabc547256f20c5da3b25a14dbd047014)#define sys\_port\_trace\_pm\_system\_suspend\_exit(ticks, state)

1919 /\* end of subsys\_tracing\_apis\_pm\_system \*/

1921

1927

[ 1932](group__subsys__tracing__apis__pm__device__runtime.md#ga31c463cfc6794a9d454adbe19c0eff96)#define sys\_port\_trace\_pm\_device\_runtime\_get\_enter(dev)

1933

[ 1939](group__subsys__tracing__apis__pm__device__runtime.md#ga6f9dfe29417ecc3c80b457b3b1ca5ad2)#define sys\_port\_trace\_pm\_device\_runtime\_get\_exit(dev, ret)

1940

[ 1945](group__subsys__tracing__apis__pm__device__runtime.md#gae077ffd9acdc7f4a9b8eff7edca7c5fe)#define sys\_port\_trace\_pm\_device\_runtime\_put\_enter(dev)

1946

[ 1952](group__subsys__tracing__apis__pm__device__runtime.md#ga5670d2d13a291224a8600de54ca475dd)#define sys\_port\_trace\_pm\_device\_runtime\_put\_exit(dev, ret)

1953

[ 1959](group__subsys__tracing__apis__pm__device__runtime.md#gab25dc434aa5ce819f295256effa4cd1a)#define sys\_port\_trace\_pm\_device\_runtime\_put\_async\_enter(dev, delay)

1960

[ 1967](group__subsys__tracing__apis__pm__device__runtime.md#gae2cb1246d1028a962282c28611c6df11)#define sys\_port\_trace\_pm\_device\_runtime\_put\_async\_exit(dev, delay, ret)

1968

[ 1973](group__subsys__tracing__apis__pm__device__runtime.md#ga6653c737e964963541a60aec29120ac0)#define sys\_port\_trace\_pm\_device\_runtime\_enable\_enter(dev)

1974

[ 1980](group__subsys__tracing__apis__pm__device__runtime.md#ga0ade92830387457ccc60661325d3f426)#define sys\_port\_trace\_pm\_device\_runtime\_enable\_exit(dev, ret)

1981

[ 1986](group__subsys__tracing__apis__pm__device__runtime.md#gaeb479059715af42498f1b1936561f207)#define sys\_port\_trace\_pm\_device\_runtime\_disable\_enter(dev)

1987

[ 1993](group__subsys__tracing__apis__pm__device__runtime.md#ga88606e2073fb35283b06500743ebfeb0)#define sys\_port\_trace\_pm\_device\_runtime\_disable\_exit(dev, ret)

1994 /\* end of subsys\_tracing\_apis\_pm\_device\_runtime \*/

1996

1997#if defined(CONFIG\_PERCEPIO\_TRACERECORDER)

1998#include "tracing\_tracerecorder.h"

1999#else

[ 2003](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)void [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)(void);

2004

[ 2008](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)void [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)(void);

2009

[ 2013](group__subsys__tracing__apis.md#ga303fe60fd4de8ddcc02c6920656e326d)void [sys\_trace\_isr\_exit\_to\_scheduler](group__subsys__tracing__apis.md#ga303fe60fd4de8ddcc02c6920656e326d)(void);

2014

[ 2018](group__subsys__tracing__apis.md#gac9b542f78ed796b4b572de19d295c824)void [sys\_trace\_idle](group__subsys__tracing__apis.md#gac9b542f78ed796b4b572de19d295c824)(void);

2019#endif /\* CONFIG\_PERCEPIO\_TRACERECORDER \*/

2020 /\* end of subsys\_tracing\_apis \*/

2022 /\* end of subsys\_tracing \*/

2024

2025#endif

2026#endif /\* ZEPHYR\_INCLUDE\_TRACING\_TRACING\_H\_ \*/

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

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[tracking.h](tracking_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [tracing](dir_c5f5a3ad31e756e37640fc6557a06392.md)
- [tracing.h](tracing_2tracing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
