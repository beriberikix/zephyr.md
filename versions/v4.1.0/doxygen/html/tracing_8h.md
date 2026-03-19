---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tracing_8h.html
original_path: doxygen/html/tracing_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tracing.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include "[tracking.h](tracking_8h_source.md)"`

[Go to the source code of this file.](tracing_8h_source.md)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_thread\_foreach\_enter](group__subsys__tracing__apis__thread.md#ga05f9560547bb1415c809d718f9bd03c8)() |
|  | Called when entering a k\_thread\_foreach call. |
| #define | [sys\_port\_trace\_k\_thread\_foreach\_exit](group__subsys__tracing__apis__thread.md#ga0848db275a35dd5f840221d2a91d75fb)() |
|  | Called when exiting a k\_thread\_foreach call. |
| #define | [sys\_port\_trace\_k\_thread\_foreach\_unlocked\_enter](group__subsys__tracing__apis__thread.md#gaf1136b18d6408da4fd9b1e8d767e390d)() |
|  | Called when entering a k\_thread\_foreach\_unlocked. |
| #define | [sys\_port\_trace\_k\_thread\_foreach\_unlocked\_exit](group__subsys__tracing__apis__thread.md#gaa6f8160940e24df5483268949d0ca402)() |
|  | Called when exiting a k\_thread\_foreach\_unlocked. |
| #define | [sys\_port\_trace\_k\_thread\_create](group__subsys__tracing__apis__thread.md#ga6140a4ec9c7b31d907b08793deb44ca7)(new\_thread) |
|  | Trace creating a Thread. |
| #define | [sys\_port\_trace\_k\_thread\_user\_mode\_enter](group__subsys__tracing__apis__thread.md#ga4ca28fdba0a95bcceddadba86412f736)() |
|  | Trace Thread entering user mode. |
| #define | [sys\_port\_trace\_k\_thread\_join\_enter](group__subsys__tracing__apis__thread.md#gabbad785e65db935917e4f1224893c9c1)(thread, timeout) |
|  | Called when entering a k\_thread\_join. |
| #define | [sys\_port\_trace\_k\_thread\_join\_blocking](group__subsys__tracing__apis__thread.md#ga057858c554e988474ae0097dc1ccf83f)(thread, timeout) |
|  | Called when k\_thread\_join blocks. |
| #define | [sys\_port\_trace\_k\_thread\_join\_exit](group__subsys__tracing__apis__thread.md#gabf77c5d93899ee85b4b4edd0c4c18490)(thread, timeout, ret) |
|  | Called when exiting k\_thread\_join. |
| #define | [sys\_port\_trace\_k\_thread\_sleep\_enter](group__subsys__tracing__apis__thread.md#ga44cac2602a3b638fbf04eb0322b33736)(timeout) |
|  | Called when entering k\_thread\_sleep. |
| #define | [sys\_port\_trace\_k\_thread\_sleep\_exit](group__subsys__tracing__apis__thread.md#ga91f7abaae3dcd7eec7ee001f8653cda6)(timeout, ret) |
|  | Called when exiting k\_thread\_sleep. |
| #define | [sys\_port\_trace\_k\_thread\_msleep\_enter](group__subsys__tracing__apis__thread.md#ga9bd09050cedc7213b90d486dc672d6d6)(ms) |
|  | Called when entering k\_thread\_msleep. |
| #define | [sys\_port\_trace\_k\_thread\_msleep\_exit](group__subsys__tracing__apis__thread.md#ga625bde038098aa8170e80205b4f3a15c)(ms, ret) |
|  | Called when exiting k\_thread\_msleep. |
| #define | [sys\_port\_trace\_k\_thread\_usleep\_enter](group__subsys__tracing__apis__thread.md#ga55a7f87fac6b2a7eff7f18ba1ffa1559)(us) |
|  | Called when entering k\_thread\_usleep. |
| #define | [sys\_port\_trace\_k\_thread\_usleep\_exit](group__subsys__tracing__apis__thread.md#ga41a7e55fa70047d242ebe403d3baa15a)(us, ret) |
|  | Called when exiting k\_thread\_usleep. |
| #define | [sys\_port\_trace\_k\_thread\_busy\_wait\_enter](group__subsys__tracing__apis__thread.md#gada94114ae74457c1082f2453d6fd9be5)(usec\_to\_wait) |
|  | Called when entering k\_thread\_busy\_wait. |
| #define | [sys\_port\_trace\_k\_thread\_busy\_wait\_exit](group__subsys__tracing__apis__thread.md#gaf8d4d01e8e662c9255f925ba64cdbd31)(usec\_to\_wait) |
|  | Called when exiting k\_thread\_busy\_wait. |
| #define | [sys\_port\_trace\_k\_thread\_yield](group__subsys__tracing__apis__thread.md#ga24f6d9958154d7e424a1af95e59e797f)() |
|  | Called when a thread yields. |
| #define | [sys\_port\_trace\_k\_thread\_wakeup](group__subsys__tracing__apis__thread.md#ga1676b0fe2f2b19bef646e73f129089db)(thread) |
|  | Called when a thread wakes up. |
| #define | [sys\_port\_trace\_k\_thread\_start](group__subsys__tracing__apis__thread.md#ga097debbc4ba4f332a2728ad04152df1a)(thread) |
|  | Called when a thread is started. |
| #define | [sys\_port\_trace\_k\_thread\_abort](group__subsys__tracing__apis__thread.md#gab0b43ffbe1ab9bb1ce962bab6c55c911)(thread) |
|  | Called when a thread is being aborted. |
| #define | [sys\_port\_trace\_k\_thread\_abort\_enter](group__subsys__tracing__apis__thread.md#ga3d147d97bbca426b7f74f1418c6ff16b)(thread) |
|  | Called when a thread enters the k\_thread\_abort routine. |
| #define | [sys\_port\_trace\_k\_thread\_abort\_exit](group__subsys__tracing__apis__thread.md#ga3e7c042978bd25ea41ed48addc3259bf)(thread) |
|  | Called when a thread exits the k\_thread\_abort routine. |
| #define | [sys\_port\_trace\_k\_thread\_priority\_set](group__subsys__tracing__apis__thread.md#ga09ddf88b7d825dd02db8a1058dda66eb)(thread) |
|  | Called when setting priority of a thread. |
| #define | [sys\_port\_trace\_k\_thread\_suspend\_enter](group__subsys__tracing__apis__thread.md#ga63bf5f0162d8596beae754cd614e2452)(thread) |
|  | Called when a thread enters the k\_thread\_suspend function. |
| #define | [sys\_port\_trace\_k\_thread\_suspend\_exit](group__subsys__tracing__apis__thread.md#gaedc07c84df5eb7d4cbdf86560ec72bdd)(thread) |
|  | Called when a thread exits the k\_thread\_suspend function. |
| #define | [sys\_port\_trace\_k\_thread\_resume\_enter](group__subsys__tracing__apis__thread.md#gaa04064835552055fc5c0d808a38cdc41)(thread) |
|  | Called when a thread enters the resume from suspension function. |
| #define | [sys\_port\_trace\_k\_thread\_resume\_exit](group__subsys__tracing__apis__thread.md#ga38841a0e40592e49de6a24690905388e)(thread) |
|  | Called when a thread exits the resumed from suspension function. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_lock](group__subsys__tracing__apis__thread.md#gadbd1fcca37d68a7a7b4c7061f3583764)() |
|  | Called when the thread scheduler is locked. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_unlock](group__subsys__tracing__apis__thread.md#ga7d5ee7a2fd30678128def82112245741)() |
|  | Called when the thread scheduler is unlocked. |
| #define | [sys\_port\_trace\_k\_thread\_name\_set](group__subsys__tracing__apis__thread.md#ga31ef5d08ff84619432b2dda7d239c479)(thread, ret) |
|  | Called when a thread name is set. |
| #define | [sys\_port\_trace\_k\_thread\_switched\_out](group__subsys__tracing__apis__thread.md#ga61a5063e1543789c16add724fad5aef1)() |
|  | Called before a thread has been selected to run. |
| #define | [sys\_port\_trace\_k\_thread\_switched\_in](group__subsys__tracing__apis__thread.md#ga89f53bfff5816ea7a1e4128677254634)() |
|  | Called after a thread has been selected to run. |
| #define | [sys\_port\_trace\_k\_thread\_ready](group__subsys__tracing__apis__thread.md#ga6fe6a019530b96e308c751d7c3732d83)(thread) |
|  | Called when a thread is ready to run. |
| #define | [sys\_port\_trace\_k\_thread\_pend](group__subsys__tracing__apis__thread.md#ga0b19ca107363fd060183cbb7b83927e8)(thread) |
|  | Called when a thread is pending. |
| #define | [sys\_port\_trace\_k\_thread\_info](group__subsys__tracing__apis__thread.md#gaffe80c4e32e27089b4ccb99fd11205ea)(thread) |
|  | Provide information about specific thread. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_wakeup](group__subsys__tracing__apis__thread.md#ga9f4b710eb3cc5ef0dabfadc9ad1cc448)(thread) |
|  | Trace implicit thread wakeup invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_abort](group__subsys__tracing__apis__thread.md#gaa2213012f5c2650301f2467dc0e36e17)(thread) |
|  | Trace implicit thread abort invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_priority\_set](group__subsys__tracing__apis__thread.md#ga906c658681af75d52d228fef96a39a92)(thread, prio) |
|  | Trace implicit thread set priority invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_ready](group__subsys__tracing__apis__thread.md#ga1f5990be25a0c0eb348d788e5aaf04cb)(thread) |
|  | Trace implicit thread ready invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_pend](group__subsys__tracing__apis__thread.md#gae857728d8f72259b6d282cb0b0bdb2ca)(thread) |
|  | Trace implicit thread pend invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_resume](group__subsys__tracing__apis__thread.md#ga81d84b861192fa664be54e7a77f0cea4)(thread) |
|  | Trace implicit thread resume invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_suspend](group__subsys__tracing__apis__thread.md#gaef5455dbd090fd7cf065d3fd8a8d3d1b)(thread) |
|  | Trace implicit thread suspend invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_work\_init](group__subsys__tracing__apis__work.md#gab31f3a43ff4a836a28ba0c21a24370e7)(work) |
|  | Trace initialisation of a Work structure. |
| #define | [sys\_port\_trace\_k\_work\_submit\_to\_queue\_enter](group__subsys__tracing__apis__work.md#gac4ec7fb1a85aaf608d0b46734fabc812)(queue, work) |
|  | Trace submit work to work queue call entry. |
| #define | [sys\_port\_trace\_k\_work\_submit\_to\_queue\_exit](group__subsys__tracing__apis__work.md#ga8807dc91f2f025f400a4e3a435b13588)(queue, work, ret) |
|  | Trace submit work to work queue call exit. |
| #define | [sys\_port\_trace\_k\_work\_submit\_enter](group__subsys__tracing__apis__work.md#ga597a2efeb4fc680149a51e7abceba2a7)(work) |
|  | Trace submit work to system work queue call entry. |
| #define | [sys\_port\_trace\_k\_work\_submit\_exit](group__subsys__tracing__apis__work.md#ga4996ec4ae496a2a55dd756f6e4474107)(work, ret) |
|  | Trace submit work to system work queue call exit. |
| #define | [sys\_port\_trace\_k\_work\_flush\_enter](group__subsys__tracing__apis__work.md#ga20f5d05e4c1be9a21e42072291272fc9)(work) |
|  | Trace flush work call entry. |
| #define | [sys\_port\_trace\_k\_work\_flush\_blocking](group__subsys__tracing__apis__work.md#gae21005546cf2025ac4eff76e09da4d0e)(work, timeout) |
|  | Trace flush work call blocking. |
| #define | [sys\_port\_trace\_k\_work\_flush\_exit](group__subsys__tracing__apis__work.md#gaa50f5a34b4cdc0ba46a4d153f0d48b39)(work, ret) |
|  | Trace flush work call exit. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_enter](group__subsys__tracing__apis__work.md#gaa2ffb1718ddc49a4f3a727e15d3e1f11)(work) |
|  | Trace cancel work call entry. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_exit](group__subsys__tracing__apis__work.md#ga9a2aa3433ec4a0a2fceb8d1c5ce682f3)(work, ret) |
|  | Trace cancel work call exit. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_sync\_enter](group__subsys__tracing__apis__work.md#ga8f2b37c2740c6883939a94ae6aa3ea51)(work, sync) |
|  | Trace cancel sync work call entry. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_sync\_blocking](group__subsys__tracing__apis__work.md#ga9d05cb22b905b5ae99174fe8523a8033)(work, sync) |
|  | Trace cancel sync work call blocking. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_sync\_exit](group__subsys__tracing__apis__work.md#gae59b7476b056d828bbf269c3f60e5687)(work, sync, ret) |
|  | Trace cancel sync work call exit. |
| #define | [sys\_port\_trace\_k\_work\_queue\_init](group__subsys__tracing__apis__work__q.md#ga9e25524cb89a9cabd6ad70459e8bd641)(queue) |
|  | Trace initialisation of a Work Queue structure. |
| #define | [sys\_port\_trace\_k\_work\_queue\_start\_enter](group__subsys__tracing__apis__work__q.md#ga79eba7247bd2c52480ac09e6ecef8635)(queue) |
|  | Trace start of a Work Queue call entry. |
| #define | [sys\_port\_trace\_k\_work\_queue\_start\_exit](group__subsys__tracing__apis__work__q.md#gae25756a58b450b2d1e8c3475cbfc1758)(queue) |
|  | Trace start of a Work Queue call exit. |
| #define | [sys\_port\_trace\_k\_work\_queue\_stop\_enter](group__subsys__tracing__apis__work__q.md#ga97f548366e687d22af6db208c754e6f8)(queue, timeout) |
|  | Trace stop of a Work Queue call entry. |
| #define | [sys\_port\_trace\_k\_work\_queue\_stop\_blocking](group__subsys__tracing__apis__work__q.md#gaf6c1bf6d59104b7382d0938cc2247b54)(queue, timeout) |
|  | Trace stop of a Work Queue call blocking. |
| #define | [sys\_port\_trace\_k\_work\_queue\_stop\_exit](group__subsys__tracing__apis__work__q.md#ga3200afa981681bdd5b51c0aaecd04620)(queue, timeout, ret) |
|  | Trace stop of a Work Queue call exit. |
| #define | [sys\_port\_trace\_k\_work\_queue\_drain\_enter](group__subsys__tracing__apis__work__q.md#ga88af757f4867f3c65f2d0eff605e0736)(queue) |
|  | Trace Work Queue drain call entry. |
| #define | [sys\_port\_trace\_k\_work\_queue\_drain\_exit](group__subsys__tracing__apis__work__q.md#ga24ca38662182a01185c9815f3cc87385)(queue, ret) |
|  | Trace Work Queue drain call exit. |
| #define | [sys\_port\_trace\_k\_work\_queue\_unplug\_enter](group__subsys__tracing__apis__work__q.md#ga1ca826910efe678127cdc1f9fdae75e7)(queue) |
|  | Trace Work Queue unplug call entry. |
| #define | [sys\_port\_trace\_k\_work\_queue\_unplug\_exit](group__subsys__tracing__apis__work__q.md#gaae2cf0379cbcf040f36fbba39821be2f)(queue, ret) |
|  | Trace Work Queue unplug call exit. |
| #define | [sys\_port\_trace\_k\_work\_delayable\_init](group__subsys__tracing__apis__work__delayable.md#ga2b7d8ad2173665808061ccc1afd52a06)(dwork) |
|  | Trace initialisation of a Delayable Work structure. |
| #define | [sys\_port\_trace\_k\_work\_schedule\_for\_queue\_enter](group__subsys__tracing__apis__work__delayable.md#gab71fd0042892d3e6c3e486cee63c9564)(queue, dwork, delay) |
|  | Trace schedule delayable work for queue enter. |
| #define | [sys\_port\_trace\_k\_work\_schedule\_for\_queue\_exit](group__subsys__tracing__apis__work__delayable.md#ga4d2160569df2886318039bfdae69d979)(queue, dwork, delay, ret) |
|  | Trace schedule delayable work for queue exit. |
| #define | [sys\_port\_trace\_k\_work\_schedule\_enter](group__subsys__tracing__apis__work__delayable.md#gacda1641af1768d815d3cc3e83c1e2456)(dwork, delay) |
|  | Trace schedule delayable work for system work queue enter. |
| #define | [sys\_port\_trace\_k\_work\_schedule\_exit](group__subsys__tracing__apis__work__delayable.md#ga8c5b232168b9bede0cd73f20513e081c)(dwork, delay, ret) |
|  | Trace schedule delayable work for system work queue exit. |
| #define | [sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_enter](group__subsys__tracing__apis__work__delayable.md#ga8d6e93ed7d85a17ffdb651e3399b0e16)(queue, dwork, delay) |
|  | Trace reschedule delayable work for queue enter. |
| #define | [sys\_port\_trace\_k\_work\_reschedule\_for\_queue\_exit](group__subsys__tracing__apis__work__delayable.md#ga636e418e8baf90aaffe3e86b86b3b047)(queue, dwork, delay, ret) |
|  | Trace reschedule delayable work for queue exit. |
| #define | [sys\_port\_trace\_k\_work\_reschedule\_enter](group__subsys__tracing__apis__work__delayable.md#gafe5b13e8aae388e9b855081450a065e1)(dwork, delay) |
|  | Trace reschedule delayable work for system queue enter. |
| #define | [sys\_port\_trace\_k\_work\_reschedule\_exit](group__subsys__tracing__apis__work__delayable.md#gaf7789cfa1a943b58e6ee93e8ec9dee57)(dwork, delay, ret) |
|  | Trace reschedule delayable work for system queue exit. |
| #define | [sys\_port\_trace\_k\_work\_flush\_delayable\_enter](group__subsys__tracing__apis__work__delayable.md#ga949c751bc5226d1b46fbf7478c1ee5a3)(dwork, sync) |
|  | Trace delayable work flush enter. |
| #define | [sys\_port\_trace\_k\_work\_flush\_delayable\_exit](group__subsys__tracing__apis__work__delayable.md#gab62f6bce942728370aefa0903a8b79a0)(dwork, sync, ret) |
|  | Trace delayable work flush exit. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_delayable\_enter](group__subsys__tracing__apis__work__delayable.md#gae80301ae580a3de83f239d9973b3829d)(dwork) |
|  | Trace delayable work cancel enter. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_delayable\_exit](group__subsys__tracing__apis__work__delayable.md#gaef6b739acf79e63e94d172e6667269ce)(dwork, ret) |
|  | Trace delayable work cancel enter. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_enter](group__subsys__tracing__apis__work__delayable.md#gaaa466d5bd2529b6a8ec5672a0054b8f7)(dwork, sync) |
|  | Trace delayable work cancel sync enter. |
| #define | [sys\_port\_trace\_k\_work\_cancel\_delayable\_sync\_exit](group__subsys__tracing__apis__work__delayable.md#ga7f2934c863c45a5bb71d1ba0401a9fe9)(dwork, sync, ret) |
|  | Trace delayable work cancel sync enter. |
| #define | [sys\_port\_trace\_k\_work\_poll\_init\_enter](group__subsys__tracing__apis__work__poll.md#gab720957a26a7e34d06af38200965b809)(work) |
|  | Trace initialisation of a Work Poll structure enter. |
| #define | [sys\_port\_trace\_k\_work\_poll\_init\_exit](group__subsys__tracing__apis__work__poll.md#gab3f6f18ab804f82386fbf478e6f1925d)(work) |
|  | Trace initialisation of a Work Poll structure exit. |
| #define | [sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_enter](group__subsys__tracing__apis__work__poll.md#gad81098506ed138f835230dec3af15076)(work\_q, work, timeout) |
|  | Trace work poll submit to queue enter. |
| #define | [sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_blocking](group__subsys__tracing__apis__work__poll.md#gabfe31b99d03a49d4b2a5cb9e0403fed9)(work\_q, work, timeout) |
|  | Trace work poll submit to queue blocking. |
| #define | [sys\_port\_trace\_k\_work\_poll\_submit\_to\_queue\_exit](group__subsys__tracing__apis__work__poll.md#ga7605f1925f1f0e86d890c896586d8776)(work\_q, work, timeout, ret) |
|  | Trace work poll submit to queue exit. |
| #define | [sys\_port\_trace\_k\_work\_poll\_submit\_enter](group__subsys__tracing__apis__work__poll.md#ga44a78c45b0bae26008d9ae5b410753b7)(work, timeout) |
|  | Trace work poll submit to system queue enter. |
| #define | [sys\_port\_trace\_k\_work\_poll\_submit\_exit](group__subsys__tracing__apis__work__poll.md#ga5917fef8383ffdb6fb3f02a42f940059)(work, timeout, ret) |
|  | Trace work poll submit to system queue exit. |
| #define | [sys\_port\_trace\_k\_work\_poll\_cancel\_enter](group__subsys__tracing__apis__work__poll.md#ga57e8e57814797b50e7e87e06503dc1f9)(work) |
|  | Trace work poll cancel enter. |
| #define | [sys\_port\_trace\_k\_work\_poll\_cancel\_exit](group__subsys__tracing__apis__work__poll.md#ga3045330b53fa50489a2d3a17b14aa295)(work, ret) |
|  | Trace work poll cancel exit. |
| #define | [sys\_port\_trace\_k\_poll\_api\_event\_init](group__subsys__tracing__apis__poll.md#ga83053d6bfc7ad8b070741f38d6606bc1)(event) |
|  | Trace initialisation of a Poll Event. |
| #define | [sys\_port\_trace\_k\_poll\_api\_poll\_enter](group__subsys__tracing__apis__poll.md#gac44ecc90dc3b407b09e2d45590496e17)(events) |
|  | Trace Polling call start. |
| #define | [sys\_port\_trace\_k\_poll\_api\_poll\_exit](group__subsys__tracing__apis__poll.md#gaf8794133d6ddc29740dfc73b9edbee12)(events, ret) |
|  | Trace Polling call outcome. |
| #define | [sys\_port\_trace\_k\_poll\_api\_signal\_init](group__subsys__tracing__apis__poll.md#gaab0dc4527d89c0e0b41d21a76ecfb120)([signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)) |
|  | Trace initialisation of a Poll Signal. |
| #define | [sys\_port\_trace\_k\_poll\_api\_signal\_reset](group__subsys__tracing__apis__poll.md#ga5addc3fa68d6afe454ad7721c8fa17c4)([signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)) |
|  | Trace resetting of Poll Signal. |
| #define | [sys\_port\_trace\_k\_poll\_api\_signal\_check](group__subsys__tracing__apis__poll.md#ga336dab8d86b07908e641e9845d75be70)([signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)) |
|  | Trace checking of Poll Signal. |
| #define | [sys\_port\_trace\_k\_poll\_api\_signal\_raise](group__subsys__tracing__apis__poll.md#gaeb1f753becfbe92f089eed23825acb4b)([signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69), ret) |
|  | Trace raising of Poll Signal. |
| #define | [sys\_port\_trace\_k\_sem\_init](group__subsys__tracing__apis__sem.md#gace327a058d058a940df14c95b031795b)(sem, ret) |
|  | Trace initialisation of a Semaphore. |
| #define | [sys\_port\_trace\_k\_sem\_give\_enter](group__subsys__tracing__apis__sem.md#ga552d549c1e8346dbe1445a93e7fc17e9)(sem) |
|  | Trace giving a Semaphore entry. |
| #define | [sys\_port\_trace\_k\_sem\_give\_exit](group__subsys__tracing__apis__sem.md#ga70d31e53b6e72d2343aa009fa5a98054)(sem) |
|  | Trace giving a Semaphore exit. |
| #define | [sys\_port\_trace\_k\_sem\_take\_enter](group__subsys__tracing__apis__sem.md#ga216fe8bc373edbb0b48fc4ca7b1816c9)(sem, timeout) |
|  | Trace taking a Semaphore attempt start. |
| #define | [sys\_port\_trace\_k\_sem\_take\_blocking](group__subsys__tracing__apis__sem.md#gade7546e098a12ce6d935b39f4978ac8d)(sem, timeout) |
|  | Trace taking a Semaphore attempt blocking. |
| #define | [sys\_port\_trace\_k\_sem\_take\_exit](group__subsys__tracing__apis__sem.md#ga8085db47b86d539e65c107bb33469ee2)(sem, timeout, ret) |
|  | Trace taking a Semaphore attempt outcome. |
| #define | [sys\_port\_trace\_k\_sem\_reset](group__subsys__tracing__apis__sem.md#ga1300af0463f93de0b29751b7a20307cb)(sem) |
|  | Trace resetting a Semaphore. |
| #define | [sys\_port\_trace\_k\_mutex\_init](group__subsys__tracing__apis__mutex.md#gaefe38feb9aa638b35fd4e723afcebf37)(mutex, ret) |
|  | Trace initialization of Mutex. |
| #define | [sys\_port\_trace\_k\_mutex\_lock\_enter](group__subsys__tracing__apis__mutex.md#ga5ed2f76aec9c128f163a2e3159e29c80)(mutex, timeout) |
|  | Trace Mutex lock attempt start. |
| #define | [sys\_port\_trace\_k\_mutex\_lock\_blocking](group__subsys__tracing__apis__mutex.md#gaae15023daa241367414afaab085acd2c)(mutex, timeout) |
|  | Trace Mutex lock attempt blocking. |
| #define | [sys\_port\_trace\_k\_mutex\_lock\_exit](group__subsys__tracing__apis__mutex.md#ga31bdc51723303de3bc93d41b36149e57)(mutex, timeout, ret) |
|  | Trace Mutex lock attempt outcome. |
| #define | [sys\_port\_trace\_k\_mutex\_unlock\_enter](group__subsys__tracing__apis__mutex.md#ga39611be3e36741442a62a98adeef9ee7)(mutex) |
|  | Trace Mutex unlock entry. |
| #define | [sys\_port\_trace\_k\_mutex\_unlock\_exit](group__subsys__tracing__apis__mutex.md#ga53c7bd3fc251865ae1a6e79da7a001b1)(mutex, ret) |
|  | Trace Mutex unlock exit. |
| #define | [sys\_port\_trace\_k\_condvar\_init](group__subsys__tracing__apis__condvar.md#gab9d1ce42bb6e6c2a762ed242ba364fa8)(condvar, ret) |
|  | Trace initialization of Conditional Variable. |
| #define | [sys\_port\_trace\_k\_condvar\_signal\_enter](group__subsys__tracing__apis__condvar.md#ga4b0f79f49b710928a38dc10ce22039e5)(condvar) |
|  | Trace Conditional Variable signaling start. |
| #define | [sys\_port\_trace\_k\_condvar\_signal\_blocking](group__subsys__tracing__apis__condvar.md#gab946fada5e51a069a13a21736a500669)(condvar, timeout) |
|  | Trace Conditional Variable signaling blocking. |
| #define | [sys\_port\_trace\_k\_condvar\_signal\_exit](group__subsys__tracing__apis__condvar.md#ga3992a8afdc375a4ecaa83cac302c7198)(condvar, ret) |
|  | Trace Conditional Variable signaling outcome. |
| #define | [sys\_port\_trace\_k\_condvar\_broadcast\_enter](group__subsys__tracing__apis__condvar.md#gadd5affb8afb73b5f76e24477d3d853bb)(condvar) |
|  | Trace Conditional Variable broadcast enter. |
| #define | [sys\_port\_trace\_k\_condvar\_broadcast\_exit](group__subsys__tracing__apis__condvar.md#ga9a013d5ab1bdd0752ec9bafb2ef4f370)(condvar, ret) |
|  | Trace Conditional Variable broadcast exit. |
| #define | [sys\_port\_trace\_k\_condvar\_wait\_enter](group__subsys__tracing__apis__condvar.md#ga30572aefa29d161af4e9e1841c59d98c)(condvar) |
|  | Trace Conditional Variable wait enter. |
| #define | [sys\_port\_trace\_k\_condvar\_wait\_exit](group__subsys__tracing__apis__condvar.md#ga07e95689443fb483886695a1533a5b08)(condvar, ret) |
|  | Trace Conditional Variable wait exit. |
| #define | [sys\_port\_trace\_k\_queue\_init](group__subsys__tracing__apis__queue.md#ga40e74ce284e349d9e6fbe948c29d574f)(queue) |
|  | Trace initialization of Queue. |
| #define | [sys\_port\_trace\_k\_queue\_cancel\_wait](group__subsys__tracing__apis__queue.md#ga8df6412be1cd3350c2b1976c7f7c8f4c)(queue) |
|  | Trace Queue cancel wait. |
| #define | [sys\_port\_trace\_k\_queue\_queue\_insert\_enter](group__subsys__tracing__apis__queue.md#ga0e38a81f47c44e1be515b375f384a2d2)(queue, alloc) |
|  | Trace Queue insert attempt entry. |
| #define | [sys\_port\_trace\_k\_queue\_queue\_insert\_blocking](group__subsys__tracing__apis__queue.md#ga3e51a4120f2ff7560ad494620c801886)(queue, alloc, timeout) |
|  | Trace Queue insert attempt blocking. |
| #define | [sys\_port\_trace\_k\_queue\_queue\_insert\_exit](group__subsys__tracing__apis__queue.md#ga9fe7ee8315505734bf33d71083190533)(queue, alloc, ret) |
|  | Trace Queue insert attempt outcome. |
| #define | [sys\_port\_trace\_k\_queue\_append\_enter](group__subsys__tracing__apis__queue.md#ga541411a2d9856fe01ed2e532a7e33db4)(queue) |
|  | Trace Queue append enter. |
| #define | [sys\_port\_trace\_k\_queue\_append\_exit](group__subsys__tracing__apis__queue.md#ga1c1a038ffa1da2efd495f769f12bc685)(queue) |
|  | Trace Queue append exit. |
| #define | [sys\_port\_trace\_k\_queue\_alloc\_append\_enter](group__subsys__tracing__apis__queue.md#ga5ef57f07d5ff8c730893f96b174f967a)(queue) |
|  | Trace Queue alloc append enter. |
| #define | [sys\_port\_trace\_k\_queue\_alloc\_append\_exit](group__subsys__tracing__apis__queue.md#ga54601544ad750fb6a5afa725a19ce269)(queue, ret) |
|  | Trace Queue alloc append exit. |
| #define | [sys\_port\_trace\_k\_queue\_prepend\_enter](group__subsys__tracing__apis__queue.md#ga90f15dc66fffd87e2b4fb66fb8bae4b1)(queue) |
|  | Trace Queue prepend enter. |
| #define | [sys\_port\_trace\_k\_queue\_prepend\_exit](group__subsys__tracing__apis__queue.md#ga023a6fee85616ae5f32b5fa4b29d29e5)(queue) |
|  | Trace Queue prepend exit. |
| #define | [sys\_port\_trace\_k\_queue\_alloc\_prepend\_enter](group__subsys__tracing__apis__queue.md#gaae4196d40be1a74439a1b7010626da17)(queue) |
|  | Trace Queue alloc prepend enter. |
| #define | [sys\_port\_trace\_k\_queue\_alloc\_prepend\_exit](group__subsys__tracing__apis__queue.md#ga2d7ff756f5c017d7b3f10787716b5684)(queue, ret) |
|  | Trace Queue alloc prepend exit. |
| #define | [sys\_port\_trace\_k\_queue\_insert\_enter](group__subsys__tracing__apis__queue.md#ga4e78ca5d7d927b912e09829b51e7330c)(queue) |
|  | Trace Queue insert attempt entry. |
| #define | [sys\_port\_trace\_k\_queue\_insert\_blocking](group__subsys__tracing__apis__queue.md#gaad04f21122c554c33ef0cb394abf6df1)(queue, timeout) |
|  | Trace Queue insert attempt blocking. |
| #define | [sys\_port\_trace\_k\_queue\_insert\_exit](group__subsys__tracing__apis__queue.md#ga69ca963f74777d9d351c9d20fe9dff62)(queue) |
|  | Trace Queue insert attempt exit. |
| #define | [sys\_port\_trace\_k\_queue\_append\_list\_enter](group__subsys__tracing__apis__queue.md#ga777cfd6ee6ad016c2bbc519a490c0672)(queue) |
|  | Trace Queue append list enter. |
| #define | [sys\_port\_trace\_k\_queue\_append\_list\_exit](group__subsys__tracing__apis__queue.md#ga215aca3523a17e31d4d36d3d95f28544)(queue, ret) |
|  | Trace Queue append list exit. |
| #define | [sys\_port\_trace\_k\_queue\_merge\_slist\_enter](group__subsys__tracing__apis__queue.md#ga888a4a39d0c33fab4243c64e42011856)(queue) |
|  | Trace Queue merge slist enter. |
| #define | [sys\_port\_trace\_k\_queue\_merge\_slist\_exit](group__subsys__tracing__apis__queue.md#ga87336faf8e19c64bcbf188452e336639)(queue, ret) |
|  | Trace Queue merge slist exit. |
| #define | [sys\_port\_trace\_k\_queue\_get\_enter](group__subsys__tracing__apis__queue.md#ga59c1bac1a34c950c7ca324fc8d853acb)(queue, timeout) |
|  | Trace Queue get attempt enter. |
| #define | [sys\_port\_trace\_k\_queue\_get\_blocking](group__subsys__tracing__apis__queue.md#gad83deb664f66df825b290b17f97156c7)(queue, timeout) |
|  | Trace Queue get attempt blockings. |
| #define | [sys\_port\_trace\_k\_queue\_get\_exit](group__subsys__tracing__apis__queue.md#ga8afd074bab6b31d60169a72db51ef76c)(queue, timeout, ret) |
|  | Trace Queue get attempt outcome. |
| #define | [sys\_port\_trace\_k\_queue\_remove\_enter](group__subsys__tracing__apis__queue.md#gacc2e453e717c654318dfd02e09288636)(queue) |
|  | Trace Queue remove enter. |
| #define | [sys\_port\_trace\_k\_queue\_remove\_exit](group__subsys__tracing__apis__queue.md#ga1df298e35d176ca79924a9b534bb115c)(queue, ret) |
|  | Trace Queue remove exit. |
| #define | [sys\_port\_trace\_k\_queue\_unique\_append\_enter](group__subsys__tracing__apis__queue.md#ga2842e4d5e778016ea70d5b860f217421)(queue) |
|  | Trace Queue unique append enter. |
| #define | [sys\_port\_trace\_k\_queue\_unique\_append\_exit](group__subsys__tracing__apis__queue.md#ga830dfc12a35c0c001abfe2cbf89387aa)(queue, ret) |
|  | Trace Queue unique append exit. |
| #define | [sys\_port\_trace\_k\_queue\_peek\_head](group__subsys__tracing__apis__queue.md#ga1cb5384c1eccc5d40c3e748dd1990cce)(queue, ret) |
|  | Trace Queue peek head. |
| #define | [sys\_port\_trace\_k\_queue\_peek\_tail](group__subsys__tracing__apis__queue.md#gac28c33f0457d7e8f99e20d0fc55427ee)(queue, ret) |
|  | Trace Queue peek tail. |
| #define | [sys\_port\_trace\_k\_fifo\_init\_enter](group__subsys__tracing__apis__fifo.md#gac0da5eca137a970c67b7b94a568c93e6)(fifo) |
|  | Trace initialization of FIFO Queue entry. |
| #define | [sys\_port\_trace\_k\_fifo\_init\_exit](group__subsys__tracing__apis__fifo.md#gaaf6c7c710377f449d52c5d6f5f7103c8)(fifo) |
|  | Trace initialization of FIFO Queue exit. |
| #define | [sys\_port\_trace\_k\_fifo\_cancel\_wait\_enter](group__subsys__tracing__apis__fifo.md#ga81e706aff605468683a96b14940745e7)(fifo) |
|  | Trace FIFO Queue cancel wait entry. |
| #define | [sys\_port\_trace\_k\_fifo\_cancel\_wait\_exit](group__subsys__tracing__apis__fifo.md#ga03ccb2bb3141c2842959ba77e4cd7337)(fifo) |
|  | Trace FIFO Queue cancel wait exit. |
| #define | [sys\_port\_trace\_k\_fifo\_put\_enter](group__subsys__tracing__apis__fifo.md#gaac5f6b9e77dad9de4652d24502ab46d0)(fifo, data) |
|  | Trace FIFO Queue put entry. |
| #define | [sys\_port\_trace\_k\_fifo\_put\_exit](group__subsys__tracing__apis__fifo.md#ga7a1d15a538f23d2b7f290435803cd73e)(fifo, data) |
|  | Trace FIFO Queue put exit. |
| #define | [sys\_port\_trace\_k\_fifo\_alloc\_put\_enter](group__subsys__tracing__apis__fifo.md#ga9c433ad8dc99ac38b8d5b4755da05c67)(fifo, data) |
|  | Trace FIFO Queue alloc put entry. |
| #define | [sys\_port\_trace\_k\_fifo\_alloc\_put\_exit](group__subsys__tracing__apis__fifo.md#gad9871fb1487a387a4f73e94bccb99a6d)(fifo, data, ret) |
|  | Trace FIFO Queue alloc put exit. |
| #define | [sys\_port\_trace\_k\_fifo\_put\_list\_enter](group__subsys__tracing__apis__fifo.md#gace20fdce59a99b92c8ac3711c4085b28)(fifo, head, tail) |
|  | Trace FIFO Queue put list entry. |
| #define | [sys\_port\_trace\_k\_fifo\_put\_list\_exit](group__subsys__tracing__apis__fifo.md#ga739360e2cefa158f22ce20a1e9369aea)(fifo, head, tail) |
|  | Trace FIFO Queue put list exit. |
| #define | [sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_enter](group__subsys__tracing__apis__fifo.md#gaf975d817bdefc64b9329330f6cd88d21)(fifo, list) |
|  | Trace FIFO Queue put slist entry. |
| #define | [sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_exit](group__subsys__tracing__apis__fifo.md#gae1c620ec17a1f7a899a1e5cba996644e)(fifo, list) |
|  | Trace FIFO Queue put slist exit. |
| #define | [sys\_port\_trace\_k\_fifo\_get\_enter](group__subsys__tracing__apis__fifo.md#gaa3539eea74888c6257c5f5d456748155)(fifo, timeout) |
|  | Trace FIFO Queue get entry. |
| #define | [sys\_port\_trace\_k\_fifo\_get\_exit](group__subsys__tracing__apis__fifo.md#gae6f06386f224063ee756e8ff0000dfe4)(fifo, timeout, ret) |
|  | Trace FIFO Queue get exit. |
| #define | [sys\_port\_trace\_k\_fifo\_peek\_head\_enter](group__subsys__tracing__apis__fifo.md#gab0fea5751e0296e623606e54efe5687b)(fifo) |
|  | Trace FIFO Queue peek head entry. |
| #define | [sys\_port\_trace\_k\_fifo\_peek\_head\_exit](group__subsys__tracing__apis__fifo.md#ga06b74415be416b137092cb72187c1fb6)(fifo, ret) |
|  | Trace FIFO Queue peek head exit. |
| #define | [sys\_port\_trace\_k\_fifo\_peek\_tail\_enter](group__subsys__tracing__apis__fifo.md#gad9f9b3193ed2c7270030036aef8d343d)(fifo) |
|  | Trace FIFO Queue peek tail entry. |
| #define | [sys\_port\_trace\_k\_fifo\_peek\_tail\_exit](group__subsys__tracing__apis__fifo.md#gae33baafbaac06ada7d6b53026a973d81)(fifo, ret) |
|  | Trace FIFO Queue peek tail exit. |
| #define | [sys\_port\_trace\_k\_lifo\_init\_enter](group__subsys__tracing__apis__lifo.md#gaad81b60363467b56d887baee8c8b5bf2)(lifo) |
|  | Trace initialization of LIFO Queue entry. |
| #define | [sys\_port\_trace\_k\_lifo\_init\_exit](group__subsys__tracing__apis__lifo.md#ga4f08168ded97456265abb3a903585ecf)(lifo) |
|  | Trace initialization of LIFO Queue exit. |
| #define | [sys\_port\_trace\_k\_lifo\_put\_enter](group__subsys__tracing__apis__lifo.md#gafd9c45a171a2fb146defa356ff0bc0f5)(lifo, data) |
|  | Trace LIFO Queue put entry. |
| #define | [sys\_port\_trace\_k\_lifo\_put\_exit](group__subsys__tracing__apis__lifo.md#ga0e5372c37bdd3a47adf11ab9d3a5e22d)(lifo, data) |
|  | Trace LIFO Queue put exit. |
| #define | [sys\_port\_trace\_k\_lifo\_alloc\_put\_enter](group__subsys__tracing__apis__lifo.md#ga0d9717f4b43e344518cc451a2fe9d224)(lifo, data) |
|  | Trace LIFO Queue alloc put entry. |
| #define | [sys\_port\_trace\_k\_lifo\_alloc\_put\_exit](group__subsys__tracing__apis__lifo.md#ga19bb748367aba8f576e72cdc30834ab1)(lifo, data, ret) |
|  | Trace LIFO Queue alloc put exit. |
| #define | [sys\_port\_trace\_k\_lifo\_get\_enter](group__subsys__tracing__apis__lifo.md#ga61556928453492dc6ed4efc999668f01)(lifo, timeout) |
|  | Trace LIFO Queue get entry. |
| #define | [sys\_port\_trace\_k\_lifo\_get\_exit](group__subsys__tracing__apis__lifo.md#ga2f7e8e680cac03844ca5dbab0438a754)(lifo, timeout, ret) |
|  | Trace LIFO Queue get exit. |
| #define | [sys\_port\_trace\_k\_stack\_init](group__subsys__tracing__apis__stack.md#ga5bb95f74d8bc3eed2525be20c444824f)(stack) |
|  | Trace initialization of Stack. |
| #define | [sys\_port\_trace\_k\_stack\_alloc\_init\_enter](group__subsys__tracing__apis__stack.md#gaa10d6cb275914bb25ad6ffad12807480)(stack) |
|  | Trace Stack alloc init attempt entry. |
| #define | [sys\_port\_trace\_k\_stack\_alloc\_init\_exit](group__subsys__tracing__apis__stack.md#gabaabe367b83b39248112eadb07bdf714)(stack, ret) |
|  | Trace Stack alloc init outcome. |
| #define | [sys\_port\_trace\_k\_stack\_cleanup\_enter](group__subsys__tracing__apis__stack.md#gaf8357d3d9a2cb8de7ba0b3473c5b063c)(stack) |
|  | Trace Stack cleanup attempt entry. |
| #define | [sys\_port\_trace\_k\_stack\_cleanup\_exit](group__subsys__tracing__apis__stack.md#ga2225cab95abdd8188087e6a98641ec0c)(stack, ret) |
|  | Trace Stack cleanup outcome. |
| #define | [sys\_port\_trace\_k\_stack\_push\_enter](group__subsys__tracing__apis__stack.md#gad6a42d93265b53540baab5c59f55fbf6)(stack) |
|  | Trace Stack push attempt entry. |
| #define | [sys\_port\_trace\_k\_stack\_push\_exit](group__subsys__tracing__apis__stack.md#ga203d32ef138d041aa0c20db8a75ccd6a)(stack, ret) |
|  | Trace Stack push attempt outcome. |
| #define | [sys\_port\_trace\_k\_stack\_pop\_enter](group__subsys__tracing__apis__stack.md#gaaf9ac378b0bbf09af91c1987dc5b777e)(stack, timeout) |
|  | Trace Stack pop attempt entry. |
| #define | [sys\_port\_trace\_k\_stack\_pop\_blocking](group__subsys__tracing__apis__stack.md#gacbdaf326a104d3bdcd4ceb5ec72c9b4f)(stack, timeout) |
|  | Trace Stack pop attempt blocking. |
| #define | [sys\_port\_trace\_k\_stack\_pop\_exit](group__subsys__tracing__apis__stack.md#ga11280d48a97cca4b65210791f9d8c591)(stack, timeout, ret) |
|  | Trace Stack pop attempt outcome. |
| #define | [sys\_port\_trace\_k\_msgq\_init](group__subsys__tracing__apis__msgq.md#ga94eae512e590d61c1c74f5d7eb552d50)(msgq) |
|  | Trace initialization of Message Queue. |
| #define | [sys\_port\_trace\_k\_msgq\_alloc\_init\_enter](group__subsys__tracing__apis__msgq.md#ga392ac9fe978d78ee1ca23c27f93e5053)(msgq) |
|  | Trace Message Queue alloc init attempt entry. |
| #define | [sys\_port\_trace\_k\_msgq\_alloc\_init\_exit](group__subsys__tracing__apis__msgq.md#ga60973fcaae9be0a6b292bf2a5dfb4fb2)(msgq, ret) |
|  | Trace Message Queue alloc init attempt outcome. |
| #define | [sys\_port\_trace\_k\_msgq\_cleanup\_enter](group__subsys__tracing__apis__msgq.md#ga370c16cd808037db5dc605e91d3c21b8)(msgq) |
|  | Trace Message Queue cleanup attempt entry. |
| #define | [sys\_port\_trace\_k\_msgq\_cleanup\_exit](group__subsys__tracing__apis__msgq.md#gaff32cb729fd32c7b008191cac1e2c881)(msgq, ret) |
|  | Trace Message Queue cleanup attempt outcome. |
| #define | [sys\_port\_trace\_k\_msgq\_put\_enter](group__subsys__tracing__apis__msgq.md#ga829e2b0d3420079777362f0b78f28d50)(msgq, timeout) |
|  | Trace Message Queue put attempt entry. |
| #define | [sys\_port\_trace\_k\_msgq\_put\_blocking](group__subsys__tracing__apis__msgq.md#gaead1e1b345e029017b1951a3d112554f)(msgq, timeout) |
|  | Trace Message Queue put attempt blocking. |
| #define | [sys\_port\_trace\_k\_msgq\_put\_exit](group__subsys__tracing__apis__msgq.md#gab4794be3e4a68af3ada3667d98286747)(msgq, timeout, ret) |
|  | Trace Message Queue put attempt outcome. |
| #define | [sys\_port\_trace\_k\_msgq\_get\_enter](group__subsys__tracing__apis__msgq.md#ga1d79dbc50b8ddd0d3db803b7c747ede5)(msgq, timeout) |
|  | Trace Message Queue get attempt entry. |
| #define | [sys\_port\_trace\_k\_msgq\_get\_blocking](group__subsys__tracing__apis__msgq.md#ga448baf7df9ec1abc4ec3a12609400b68)(msgq, timeout) |
|  | Trace Message Queue get attempt blockings. |
| #define | [sys\_port\_trace\_k\_msgq\_get\_exit](group__subsys__tracing__apis__msgq.md#ga2a549f567cda0646b853a9cb0b7e1eb2)(msgq, timeout, ret) |
|  | Trace Message Queue get attempt outcome. |
| #define | [sys\_port\_trace\_k\_msgq\_peek](group__subsys__tracing__apis__msgq.md#gad11e9f22177bf004f95d23750a2046a3)(msgq, ret) |
|  | Trace Message Queue peek. |
| #define | [sys\_port\_trace\_k\_msgq\_purge](group__subsys__tracing__apis__msgq.md#ga91530d1c6d10ce72cc5c9319c28b5e32)(msgq) |
|  | Trace Message Queue purge. |
| #define | [sys\_port\_trace\_k\_mbox\_init](group__subsys__tracing__apis__mbox.md#ga67187d636152a34614c4213c47ea7509)(mbox) |
|  | Trace initialization of Mailbox. |
| #define | [sys\_port\_trace\_k\_mbox\_message\_put\_enter](group__subsys__tracing__apis__mbox.md#gac7b683e1e33c42e3e04f84a2c2b19811)(mbox, timeout) |
|  | Trace Mailbox message put attempt entry. |
| #define | [sys\_port\_trace\_k\_mbox\_message\_put\_blocking](group__subsys__tracing__apis__mbox.md#ga6a04c6ea1072d7c858a23c845e76565d)(mbox, timeout) |
|  | Trace Mailbox message put attempt blocking. |
| #define | [sys\_port\_trace\_k\_mbox\_message\_put\_exit](group__subsys__tracing__apis__mbox.md#ga2ab3697623a198ea15ad644ce19335fb)(mbox, timeout, ret) |
|  | Trace Mailbox message put attempt outcome. |
| #define | [sys\_port\_trace\_k\_mbox\_put\_enter](group__subsys__tracing__apis__mbox.md#gaba437af59b1a8c663fa7d39eafa78ee6)(mbox, timeout) |
|  | Trace Mailbox put attempt entry. |
| #define | [sys\_port\_trace\_k\_mbox\_put\_exit](group__subsys__tracing__apis__mbox.md#ga07148a910c33c881d531ed495b23c081)(mbox, timeout, ret) |
|  | Trace Mailbox put attempt blocking. |
| #define | [sys\_port\_trace\_k\_mbox\_async\_put\_enter](group__subsys__tracing__apis__mbox.md#ga7dd281ffa54a3d32c7380e294e18ef5d)(mbox, sem) |
|  | Trace Mailbox async put entry. |
| #define | [sys\_port\_trace\_k\_mbox\_async\_put\_exit](group__subsys__tracing__apis__mbox.md#gab39d7bfdfc0c5ed394e7819a3048741e)(mbox, sem) |
|  | Trace Mailbox async put exit. |
| #define | [sys\_port\_trace\_k\_mbox\_get\_enter](group__subsys__tracing__apis__mbox.md#ga30ad94a6f1267931ff8d401fb4a75be3)(mbox, timeout) |
|  | Trace Mailbox get attempt entry. |
| #define | [sys\_port\_trace\_k\_mbox\_get\_blocking](group__subsys__tracing__apis__mbox.md#ga4977171638fed999e4485cc035016c10)(mbox, timeout) |
|  | Trace Mailbox get attempt blocking. |
| #define | [sys\_port\_trace\_k\_mbox\_get\_exit](group__subsys__tracing__apis__mbox.md#gaaa8261b9fa07c97308b46a9b7100aee6)(mbox, timeout, ret) |
|  | Trace Mailbox get attempt outcome. |
| #define | [sys\_port\_trace\_k\_mbox\_data\_get](group__subsys__tracing__apis__mbox.md#gacef2016dc5620371401e55e7005a18c3)(rx\_msg) |
|  | Trace Mailbox data get. |
| #define | [sys\_port\_trace\_k\_pipe\_init](group__subsys__tracing__apis__pipe.md#ga8b22ee35dfa2c4be5cf9772fe92dd731)(pipe, buffer, size) |
|  | Trace initialization of Pipe. |
| #define | [sys\_port\_trace\_k\_pipe\_reset\_enter](group__subsys__tracing__apis__pipe.md#ga9168b8fbacac753adc76b5fa341ba5f3)(pipe) |
|  | Trace Pipe reset entry. |
| #define | [sys\_port\_trace\_k\_pipe\_reset\_exit](group__subsys__tracing__apis__pipe.md#gad880e5655d35441e83bada3e950924cc)(pipe) |
|  | Trace Pipe reset exit. |
| #define | [sys\_port\_trace\_k\_pipe\_close\_enter](group__subsys__tracing__apis__pipe.md#gad9913c3eaa2711e501f4d3a071ee2304)(pipe) |
|  | Trace Pipe close entry. |
| #define | [sys\_port\_trace\_k\_pipe\_close\_exit](group__subsys__tracing__apis__pipe.md#ga42029311eeb46b06d8a4cdd3ca12b2fe)(pipe) |
|  | Trace Pipe close exit. |
| #define | [sys\_port\_trace\_k\_pipe\_write\_enter](group__subsys__tracing__apis__pipe.md#gae1d79d1472bfb3905f107159b297d50b)(pipe, data, len, timeout) |
|  | Trace Pipe write attempt entry. |
| #define | [sys\_port\_trace\_k\_pipe\_write\_blocking](group__subsys__tracing__apis__pipe.md#ga566b7428e665bf086beaac4884bee3b6)(pipe, timeout) |
|  | Trace Pipe write attempt blocking. |
| #define | [sys\_port\_trace\_k\_pipe\_write\_exit](group__subsys__tracing__apis__pipe.md#gacb4b01b7c27ac7ad875f054038832d3a)(pipe, ret) |
|  | Trace Pipe write attempt outcome. |
| #define | [sys\_port\_trace\_k\_pipe\_read\_enter](group__subsys__tracing__apis__pipe.md#ga35d3ebbc09e2690a9b01707663c9f4cc)(pipe, data, len, timeout) |
|  | Trace Pipe read attempt entry. |
| #define | [sys\_port\_trace\_k\_pipe\_read\_blocking](group__subsys__tracing__apis__pipe.md#ga94f7c8eb46b23be75eb9341ec52bfeb1)(pipe, timeout) |
|  | Trace Pipe read attempt blocking. |
| #define | [sys\_port\_trace\_k\_pipe\_read\_exit](group__subsys__tracing__apis__pipe.md#gaa43afb60d07428049dd13c12a7fcab88)(pipe, ret) |
|  | Trace Pipe read attempt outcome. |
| #define | [sys\_port\_trace\_k\_pipe\_cleanup\_enter](group__subsys__tracing__apis__pipe.md#ga63bc37ca2dbcf84fc87e13fdb2f21834)(pipe) |
|  | Trace Pipe cleanup entry. |
| #define | [sys\_port\_trace\_k\_pipe\_cleanup\_exit](group__subsys__tracing__apis__pipe.md#gaa367f4e1019380dde77ee881f22ab278)(pipe, ret) |
|  | Trace Pipe cleanup exit. |
| #define | [sys\_port\_trace\_k\_pipe\_alloc\_init\_enter](group__subsys__tracing__apis__pipe.md#ga6fdcad7deb3be98acd88cd8febd39247)(pipe) |
|  | Trace Pipe alloc init entry. |
| #define | [sys\_port\_trace\_k\_pipe\_alloc\_init\_exit](group__subsys__tracing__apis__pipe.md#ga011af7de686c1b360f0696a7dd1b173f)(pipe, ret) |
|  | Trace Pipe alloc init exit. |
| #define | [sys\_port\_trace\_k\_pipe\_flush\_enter](group__subsys__tracing__apis__pipe.md#ga9e3f6058f2370488cfb4d57676c3d5cd)(pipe) |
|  | Trace Pipe flush entry. |
| #define | [sys\_port\_trace\_k\_pipe\_flush\_exit](group__subsys__tracing__apis__pipe.md#gafdba63af20781901576344ef198da8a4)(pipe) |
|  | Trace Pipe flush exit. |
| #define | [sys\_port\_trace\_k\_pipe\_buffer\_flush\_enter](group__subsys__tracing__apis__pipe.md#gaa81b667947689ac7edb866cb7c5beb81)(pipe) |
|  | Trace Pipe buffer flush entry. |
| #define | [sys\_port\_trace\_k\_pipe\_buffer\_flush\_exit](group__subsys__tracing__apis__pipe.md#ga47d9a997d8daff89a1c4a41ac4bb327e)(pipe) |
|  | Trace Pipe buffer flush exit. |
| #define | [sys\_port\_trace\_k\_pipe\_put\_enter](group__subsys__tracing__apis__pipe.md#gad16f0673669f9700ebd3e4fc0b1466d8)(pipe, timeout) |
|  | Trace Pipe put attempt entry. |
| #define | [sys\_port\_trace\_k\_pipe\_put\_blocking](group__subsys__tracing__apis__pipe.md#ga314cffd927b410d3670f39a774a42206)(pipe, timeout) |
|  | Trace Pipe put attempt blocking. |
| #define | [sys\_port\_trace\_k\_pipe\_put\_exit](group__subsys__tracing__apis__pipe.md#ga20a131258373e32379273dd0ff08a672)(pipe, timeout, ret) |
|  | Trace Pipe put attempt outcome. |
| #define | [sys\_port\_trace\_k\_pipe\_get\_enter](group__subsys__tracing__apis__pipe.md#gaafa10362c5042f0f2e02b40b79768dbb)(pipe, timeout) |
|  | Trace Pipe get attempt entry. |
| #define | [sys\_port\_trace\_k\_pipe\_get\_blocking](group__subsys__tracing__apis__pipe.md#ga2dfb7cfd0b08beac72d254ac3063d42c)(pipe, timeout) |
|  | Trace Pipe get attempt blocking. |
| #define | [sys\_port\_trace\_k\_pipe\_get\_exit](group__subsys__tracing__apis__pipe.md#ga192cb7bafd2d04898b13e30aa96d483d)(pipe, timeout, ret) |
|  | Trace Pipe get attempt outcome. |
| #define | [sys\_port\_trace\_k\_heap\_init](group__subsys__tracing__apis__heap.md#gaa9eb0a2ff9da8a892ab62e45fe4e4ddb)(h) |
|  | Trace initialization of Heap. |
| #define | [sys\_port\_trace\_k\_heap\_aligned\_alloc\_enter](group__subsys__tracing__apis__heap.md#gaa49162a735def3b0389cc30bd4654533)(h, timeout) |
|  | Trace Heap aligned alloc attempt entry. |
| #define | [sys\_port\_trace\_k\_heap\_aligned\_alloc\_blocking](group__subsys__tracing__apis__heap.md#gada1001c802bcc55437ffd8f4e2f23bef)(h, timeout) |
|  | Trace Heap align alloc attempt blocking. |
| #define | [sys\_port\_trace\_k\_heap\_aligned\_alloc\_exit](group__subsys__tracing__apis__heap.md#ga3833f13065d967acafd50e3089556944)(h, timeout, ret) |
|  | Trace Heap align alloc attempt outcome. |
| #define | [sys\_port\_trace\_k\_heap\_alloc\_enter](group__subsys__tracing__apis__heap.md#gadf8441b3c430499c8444a7c73bae1931)(h, timeout) |
|  | Trace Heap alloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_alloc\_exit](group__subsys__tracing__apis__heap.md#gad696bba7ffe71beb01520ab27b483307)(h, timeout, ret) |
|  | Trace Heap alloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_calloc\_enter](group__subsys__tracing__apis__heap.md#gac5982869d3ec94331b5b8efb3fafbc59)(h, timeout) |
|  | Trace Heap calloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_calloc\_exit](group__subsys__tracing__apis__heap.md#ga7c9fd0cf63be9b591adc7e59af0803d4)(h, timeout, ret) |
|  | Trace Heap calloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_free](group__subsys__tracing__apis__heap.md#ga6f9c92a02d32af203752c59615e34096)(h) |
|  | Trace Heap free. |
| #define | [sys\_port\_trace\_k\_heap\_realloc\_enter](group__subsys__tracing__apis__heap.md#ga5c7936b9c4f257e22638824c7ba6601e)(h, ptr, bytes, timeout) |
|  | Trace Heap realloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_realloc\_exit](group__subsys__tracing__apis__heap.md#ga888b7ae4b7c29e4c2e877ca1c525d315)(h, ptr, bytes, timeout, ret) |
|  | Trace Heap realloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_enter](group__subsys__tracing__apis__heap.md#ga12de856dc1fc2cb261497b3ef8b09e9e)(heap) |
|  | Trace System Heap aligned alloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_exit](group__subsys__tracing__apis__heap.md#ga6d7a77c282f8229e0b366d57ba33ed04)(heap, ret) |
|  | Trace System Heap aligned alloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_enter](group__subsys__tracing__apis__heap.md#ga478745a9e6cbc1a7b6bc9a2fc1763ca5)(heap) |
|  | Trace System Heap aligned alloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_exit](group__subsys__tracing__apis__heap.md#ga4d612b7ec5d992c6e8170f35a1ce6c03)(heap, ret) |
|  | Trace System Heap aligned alloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_free\_enter](group__subsys__tracing__apis__heap.md#gaf4dd86f13041c12cf18696fcff2ba9aa)(heap, heap\_ref) |
|  | Trace System Heap free entry. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_free\_exit](group__subsys__tracing__apis__heap.md#gaf2865a12ffee2135e2d798bdf5fa9c98)(heap, heap\_ref) |
|  | Trace System Heap free exit. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_enter](group__subsys__tracing__apis__heap.md#ga60e3dd5434ba9c912a4f2332f579318f)(heap) |
|  | Trace System heap calloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_exit](group__subsys__tracing__apis__heap.md#ga6be2fe00eabc9bffaf635cfb14714e4a)(heap, ret) |
|  | Trace System heap calloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_realloc\_enter](group__subsys__tracing__apis__heap.md#ga5c2e672b64f326b93aca9a4840ca5123)(heap, ptr) |
|  | Trace System heap realloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_realloc\_exit](group__subsys__tracing__apis__heap.md#ga154dcc3e907ca4dbac41918cbb958e42)(heap, ptr, ret) |
|  | Trace System heap realloc exit. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_init](group__subsys__tracing__apis__mslab.md#ga5a769fffc7611a57c8490b3f5c6047a5)(slab, rc) |
|  | Trace initialization of Memory Slab. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_alloc\_enter](group__subsys__tracing__apis__mslab.md#gac1ac5f1393b87ea84c2d53f08c251ff2)(slab, timeout) |
|  | Trace Memory Slab alloc attempt entry. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_alloc\_blocking](group__subsys__tracing__apis__mslab.md#gaea77ffa2dbbfad9ff2fec0041b0dbc59)(slab, timeout) |
|  | Trace Memory Slab alloc attempt blocking. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_alloc\_exit](group__subsys__tracing__apis__mslab.md#ga237bb89733ca9c483ef6b9ab6dd920a4)(slab, timeout, ret) |
|  | Trace Memory Slab alloc attempt outcome. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_free\_enter](group__subsys__tracing__apis__mslab.md#ga22fc4609185f6ddffd0abc85f3976914)(slab) |
|  | Trace Memory Slab free entry. |
| #define | [sys\_port\_trace\_k\_mem\_slab\_free\_exit](group__subsys__tracing__apis__mslab.md#ga81dd030d4052e3092479e19616b4baec)(slab) |
|  | Trace Memory Slab free exit. |
| #define | [sys\_port\_trace\_k\_timer\_init](group__subsys__tracing__apis__timer.md#ga03a70d84ea0227829fb9528b0156c147)(timer) |
|  | Trace initialization of Timer. |
| #define | [sys\_port\_trace\_k\_timer\_start](group__subsys__tracing__apis__timer.md#ga95b998ea6bf00692cb654a18787ab185)(timer, duration, period) |
|  | Trace Timer start. |
| #define | [sys\_port\_trace\_k\_timer\_stop](group__subsys__tracing__apis__timer.md#ga81b6cba81190cc61cdd33f4ddb6f4550)(timer) |
|  | Trace Timer stop. |
| #define | [sys\_port\_trace\_k\_timer\_status\_sync\_enter](group__subsys__tracing__apis__timer.md#ga0adf7e6ca5bdd89b7676836101ef37df)(timer) |
|  | Trace Timer status sync entry. |
| #define | [sys\_port\_trace\_k\_timer\_status\_sync\_blocking](group__subsys__tracing__apis__timer.md#gaa3cd4ca118fd987560ae1855c904e1aa)(timer, timeout) |
|  | Trace Timer Status sync blocking. |
| #define | [sys\_port\_trace\_k\_timer\_status\_sync\_exit](group__subsys__tracing__apis__timer.md#gab51aa6682136eb86a4fd141f61ece779)(timer, result) |
|  | Trace Time Status sync outcome. |
| #define | [sys\_port\_trace\_k\_event\_init](group__subsys__tracing__apis__event.md#gae212c1b330d476613629501d62be0994)(event) |
|  | Trace initialisation of an Event. |
| #define | [sys\_port\_trace\_k\_event\_post\_enter](group__subsys__tracing__apis__event.md#ga20092082696c6c9fe3b8870bd3523b52)(event, events, events\_mask) |
|  | Trace posting of an Event call entry. |
| #define | [sys\_port\_trace\_k\_event\_post\_exit](group__subsys__tracing__apis__event.md#gac58a047db800cca608087d6b2cec37f9)(event, events, events\_mask) |
|  | Trace posting of an Event call exit. |
| #define | [sys\_port\_trace\_k\_event\_wait\_enter](group__subsys__tracing__apis__event.md#ga6b01461ff2fa0cf2c3c19dbed2f8c4c3)(event, events, options, timeout) |
|  | Trace waiting of an Event call entry. |
| #define | [sys\_port\_trace\_k\_event\_wait\_blocking](group__subsys__tracing__apis__event.md#ga008a96d80f3f90dcffbc74f43d66b9be)(event, events, options, timeout) |
|  | Trace waiting of an Event call exit. |
| #define | [sys\_port\_trace\_k\_event\_wait\_exit](group__subsys__tracing__apis__event.md#ga874698f8eff5237fefacc1be761b2661)(event, events, ret) |
|  | Trace waiting of an Event call exit. |
| #define | [sys\_port\_trace\_pm\_system\_suspend\_enter](group__subsys__tracing__apis__pm__system.md#ga1d8c01fe22ef0f7ac8fdfb47de55f58e)(ticks) |
|  | Trace system suspend call entry. |
| #define | [sys\_port\_trace\_pm\_system\_suspend\_exit](group__subsys__tracing__apis__pm__system.md#gaabc547256f20c5da3b25a14dbd047014)(ticks, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Trace system suspend call exit. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_get\_enter](group__subsys__tracing__apis__pm__device__runtime.md#ga31c463cfc6794a9d454adbe19c0eff96)(dev) |
|  | Trace getting a device call entry. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_get\_exit](group__subsys__tracing__apis__pm__device__runtime.md#ga6f9dfe29417ecc3c80b457b3b1ca5ad2)(dev, ret) |
|  | Trace getting a device call exit. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_put\_enter](group__subsys__tracing__apis__pm__device__runtime.md#gae077ffd9acdc7f4a9b8eff7edca7c5fe)(dev) |
|  | Trace putting a device call entry. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_put\_exit](group__subsys__tracing__apis__pm__device__runtime.md#ga5670d2d13a291224a8600de54ca475dd)(dev, ret) |
|  | Trace putting a device call exit. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_put\_async\_enter](group__subsys__tracing__apis__pm__device__runtime.md#gab25dc434aa5ce819f295256effa4cd1a)(dev, delay) |
|  | Trace putting a device (asynchronously) call entry. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_put\_async\_exit](group__subsys__tracing__apis__pm__device__runtime.md#gae2cb1246d1028a962282c28611c6df11)(dev, delay, ret) |
|  | Trace putting a device (asynchronously) call exit. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_enable\_enter](group__subsys__tracing__apis__pm__device__runtime.md#ga6653c737e964963541a60aec29120ac0)(dev) |
|  | Trace enabling device runtime PM call entry. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_enable\_exit](group__subsys__tracing__apis__pm__device__runtime.md#ga0ade92830387457ccc60661325d3f426)(dev, ret) |
|  | Trace enabling device runtime PM call exit. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_disable\_enter](group__subsys__tracing__apis__pm__device__runtime.md#gaeb479059715af42498f1b1936561f207)(dev) |
|  | Trace disabling device runtime PM call entry. |
| #define | [sys\_port\_trace\_pm\_device\_runtime\_disable\_exit](group__subsys__tracing__apis__pm__device__runtime.md#ga88606e2073fb35283b06500743ebfeb0)(dev, ret) |
|  | Trace disabling device runtime PM call exit. |
| #define | [sys\_port\_trace\_net\_recv\_data\_enter](group__subsys__tracing__apis__net.md#gab39c341e9aad487268cc934dd6104fc6)(iface, pkt) |
|  | Trace network data receive. |
| #define | [sys\_port\_trace\_net\_recv\_data\_exit](group__subsys__tracing__apis__net.md#ga4c0ba70ff0eef209005eb47c76e11682)(iface, pkt, ret) |
|  | Trace network data receive attempt. |
| #define | [sys\_port\_trace\_net\_send\_data\_enter](group__subsys__tracing__apis__net.md#ga9738aa7cefef4038974523bdf6d1a672)(pkt) |
|  | Trace network data send. |
| #define | [sys\_port\_trace\_net\_send\_data\_exit](group__subsys__tracing__apis__net.md#gaf3dde1664303355401f0765271dfedb4)(pkt, ret) |
|  | Trace network data send attempt. |
| #define | [sys\_port\_trace\_net\_rx\_time](group__subsys__tracing__apis__net.md#gace8a76a44fc01a1f14633c3a758d2811)(pkt, end\_time) |
|  | Trace network data receive time. |
| #define | [sys\_port\_trace\_net\_tx\_time](group__subsys__tracing__apis__net.md#ga1db4323543a538b3911b44f65ecf7d50)(pkt, end\_time) |
|  | Trace network data sent time. |
| #define | [sys\_port\_trace\_socket\_init](group__subsys__tracing__apis__socket.md#ga9d4f7402bb41321dc86fe521b8ac61c4)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), family, type, proto) |
|  | Trace init of network sockets. |
| #define | [sys\_port\_trace\_socket\_close\_enter](group__subsys__tracing__apis__socket.md#gaf8e8b1245a3bc053cc1b2ceb2b50aca6)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a)) |
|  | Trace close of network sockets. |
| #define | [sys\_port\_trace\_socket\_close\_exit](group__subsys__tracing__apis__socket.md#ga43248f800666043e02a206c402137e39)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), ret) |
|  | Trace network socket close attempt. |
| #define | [sys\_port\_trace\_socket\_shutdown\_enter](group__subsys__tracing__apis__socket.md#gaaee4b59afd78be034bc933b0f4cb80c4)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), how) |
|  | Trace shutdown of network sockets. |
| #define | [sys\_port\_trace\_socket\_shutdown\_exit](group__subsys__tracing__apis__socket.md#ga708c4791bc53315afd08b42b83e2c828)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), ret) |
|  | Trace network socket shutdown attempt. |
| #define | [sys\_port\_trace\_socket\_bind\_enter](group__subsys__tracing__apis__socket.md#ga8f719e0ef0e5a13922cc54d48ab63410)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), addr, addrlen) |
|  | Trace bind of network sockets. |
| #define | [sys\_port\_trace\_socket\_bind\_exit](group__subsys__tracing__apis__socket.md#gab909132830f1c37eb335ff59c39e47df)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), ret) |
|  | Trace network socket bind attempt. |
| #define | [sys\_port\_trace\_socket\_connect\_enter](group__subsys__tracing__apis__socket.md#gaabb7458048b7cac6c1cab12e66883bed)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), addr, addrlen) |
|  | Trace connect of network sockets. |
| #define | [sys\_port\_trace\_socket\_connect\_exit](group__subsys__tracing__apis__socket.md#ga3504da7dcabcb07cdc0f759ea5964d67)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), ret) |
|  | Trace network socket connect attempt. |
| #define | [sys\_port\_trace\_socket\_listen\_enter](group__subsys__tracing__apis__socket.md#ga4d56bf430d8c25d3c9b132c7ee492586)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), backlog) |
|  | Trace listen of network sockets. |
| #define | [sys\_port\_trace\_socket\_listen\_exit](group__subsys__tracing__apis__socket.md#gac0b0a343ec19cd483ef0b52648d4f107)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), ret) |
|  | Trace network socket listen attempt. |
| #define | [sys\_port\_trace\_socket\_accept\_enter](group__subsys__tracing__apis__socket.md#ga02ef099cede7c64bb17737a0080e4410)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a)) |
|  | Trace accept of network sockets. |
| #define | [sys\_port\_trace\_socket\_accept\_exit](group__subsys__tracing__apis__socket.md#gace86c4fb481474b73750445b2a11e6f2)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), addr, addrlen, ret) |
|  | Trace network socket accept attempt. |
| #define | [sys\_port\_trace\_socket\_sendto\_enter](group__subsys__tracing__apis__socket.md#gabafa02418677bec9f3137dadc1b50133)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), dest\_addr, addrlen) |
|  | Trace sendto of network sockets. |
| #define | [sys\_port\_trace\_socket\_sendto\_exit](group__subsys__tracing__apis__socket.md#gad88e16f737503a18166680b0b992be7d)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), ret) |
|  | Trace network socket sendto attempt. |
| #define | [sys\_port\_trace\_socket\_sendmsg\_enter](group__subsys__tracing__apis__socket.md#ga6905a1e8dec1362837ca5c9fab41886f)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), msg, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace sendmsg of network sockets. |
| #define | [sys\_port\_trace\_socket\_sendmsg\_exit](group__subsys__tracing__apis__socket.md#ga9ca50f9d8b57aa65300c241043889061)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), ret) |
|  | Trace network socket sendmsg attempt. |
| #define | [sys\_port\_trace\_socket\_recvfrom\_enter](group__subsys__tracing__apis__socket.md#gafb8183b4148421feac195cf418d2aab3)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), max\_len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), addr, addrlen) |
|  | Trace recvfrom of network sockets. |
| #define | [sys\_port\_trace\_socket\_recvfrom\_exit](group__subsys__tracing__apis__socket.md#ga94c64423eb1a08bddc570eb1cc32c152)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), src\_addr, addrlen, ret) |
|  | Trace network socket recvfrom attempt. |
| #define | [sys\_port\_trace\_socket\_recvmsg\_enter](group__subsys__tracing__apis__socket.md#gac11782e26568641c6eb35a278c42dc6a)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), msg, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace recvmsg of network sockets. |
| #define | [sys\_port\_trace\_socket\_recvmsg\_exit](group__subsys__tracing__apis__socket.md#ga4a7840ae28ca908b8bfa707db7bae514)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), msg, ret) |
|  | Trace network socket recvmsg attempt. |
| #define | [sys\_port\_trace\_socket\_fcntl\_enter](group__subsys__tracing__apis__socket.md#ga27365b99cfe408830a5d057cee944acb)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace fcntl of network sockets. |
| #define | [sys\_port\_trace\_socket\_fcntl\_exit](group__subsys__tracing__apis__socket.md#gacb1376cd3c51f9c92d42315e4a2d0373)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), ret) |
|  | Trace network socket fcntl attempt. |
| #define | [sys\_port\_trace\_socket\_ioctl\_enter](group__subsys__tracing__apis__socket.md#ga1d62829f2c8109b396a758ff1ed4ae43)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), req) |
|  | Trace ioctl of network sockets. |
| #define | [sys\_port\_trace\_socket\_ioctl\_exit](group__subsys__tracing__apis__socket.md#ga0ddadc07cdbdd88fddd98ca80ce97e89)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), ret) |
|  | Trace network socket ioctl attempt. |
| #define | [sys\_port\_trace\_socket\_poll\_enter](group__subsys__tracing__apis__socket.md#ga8f21c61500b256bee9b9c1d902c75dc0)(fds, nfds, timeout) |
|  | Trace polling of network sockets. |
| #define | [sys\_port\_trace\_socket\_poll\_exit](group__subsys__tracing__apis__socket.md#ga968df5694eb381b9c1778824806e7561)(fds, nfds, ret) |
|  | Trace network socket poll attempt. |
| #define | [sys\_port\_trace\_socket\_getsockopt\_enter](group__subsys__tracing__apis__socket.md#ga485c1877467ba763181f273e0aedcb7e)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), level, optname) |
|  | Trace getsockopt of network sockets. |
| #define | [sys\_port\_trace\_socket\_getsockopt\_exit](group__subsys__tracing__apis__socket.md#ga0144d5f6276eaa117431293e2ee46e74)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), level, optname, optval, optlen, ret) |
|  | Trace network socket getsockopt attempt. |
| #define | [sys\_port\_trace\_socket\_setsockopt\_enter](group__subsys__tracing__apis__socket.md#gacbe9848da97e63c84a618ef5b7b8a673)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), level, optname, optval, optlen) |
|  | Trace setsockopt of network sockets. |
| #define | [sys\_port\_trace\_socket\_setsockopt\_exit](group__subsys__tracing__apis__socket.md#gaebe7a021e6f714f364adc76eadc2220a)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), ret) |
|  | Trace network socket setsockopt attempt. |
| #define | [sys\_port\_trace\_socket\_getpeername\_enter](group__subsys__tracing__apis__socket.md#ga307c3e4b2f25f5a20e362418bfff4012)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a)) |
|  | Trace getpeername of network sockets. |
| #define | [sys\_port\_trace\_socket\_getpeername\_exit](group__subsys__tracing__apis__socket.md#ga0136f94380ec088be2981d35e74be3c6)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), addr, addrlen, ret) |
|  | Trace network socket getpeername attempt. |
| #define | [sys\_port\_trace\_socket\_getsockname\_enter](group__subsys__tracing__apis__socket.md#gae9baf2d36c52bd458b60d2d8296c4a6d)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a)) |
|  | Trace getsockname of network sockets. |
| #define | [sys\_port\_trace\_socket\_getsockname\_exit](group__subsys__tracing__apis__socket.md#gaa2831098447ab830d9470005a1ead43a)([socket](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a), addr, addrlen, ret) |
|  | Trace network socket getsockname attempt. |
| #define | [sys\_port\_trace\_socket\_socketpair\_enter](group__subsys__tracing__apis__socket.md#ga1b639ef77d5d26e80bd863a5dfdf6350)(family, type, proto, sv) |
|  | Trace socketpair enter call. |
| #define | [sys\_port\_trace\_socket\_socketpair\_exit](group__subsys__tracing__apis__socket.md#gae7623cda74ce67a3282185466be0333f)(socket\_A, socket\_B, ret) |
|  | Trace network socketpair open attempt. |
| #define | [sys\_trace\_named\_event](group__subsys__tracing__apis__named.md#ga205bc648bdf0152f8652f04f15cf48af)(name, arg0, arg1) |
| #define | [sys\_port\_trace\_gpio\_pin\_interrupt\_configure\_enter](group__subsys__tracing__apis__gpio.md#ga136247e36d2f518d15bf332d8ba5d035)(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace GPIO pin interrupt configure enter call. |
| #define | [sys\_port\_trace\_gpio\_pin\_interrupt\_configure\_exit](group__subsys__tracing__apis__gpio.md#ga78b6201756dc8889aed4dbe2f5e5df08)(port, pin, ret) |
|  | Trace GPIO pin interrupt configure exit call. |
| #define | [sys\_port\_trace\_gpio\_pin\_configure\_enter](group__subsys__tracing__apis__gpio.md#ga9975f3c53f4cfa2fb4b699691811289d)(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace GPIO single pin configure enter call. |
| #define | [sys\_port\_trace\_gpio\_pin\_configure\_exit](group__subsys__tracing__apis__gpio.md#gad116e0fee008064fa859fcb660735420)(port, pin, ret) |
|  | Trace GPIO single pin configure exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_get\_direction\_enter](group__subsys__tracing__apis__gpio.md#ga20672a060ed09777729bc417eb4ac726)(port, map, inputs, outputs) |
|  | Trace GPIO port get direction enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_get\_direction\_exit](group__subsys__tracing__apis__gpio.md#gade6194699050e060dc48fa0de50fc930)(port, ret) |
|  | Trace GPIO port get direction exit call. |
| #define | [sys\_port\_trace\_gpio\_pin\_get\_config\_enter](group__subsys__tracing__apis__gpio.md#gac5592dce31daf0c8cfcfa09db50fc9e4)(port, pin, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace GPIO pin gent config enter call. |
| #define | [sys\_port\_trace\_gpio\_pin\_get\_config\_exit](group__subsys__tracing__apis__gpio.md#ga92ada0c9043f9b00803e33c5537abe05)(port, pin, ret) |
|  | Trace GPIO pin get config exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_get\_raw\_enter](group__subsys__tracing__apis__gpio.md#gabeea324bb6ee389a6f4f739918e43328)(port, value) |
|  | Trace GPIO port get raw enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_get\_raw\_exit](group__subsys__tracing__apis__gpio.md#ga1cbebfa0804f10c410622bb17c02bdb5)(port, ret) |
|  | Trace GPIO port get raw exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_set\_masked\_raw\_enter](group__subsys__tracing__apis__gpio.md#ga6ddcc9a973b2c938fa67ba9d9de90b43)(port, mask, value) |
|  | Trace GPIO port set masked raw enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_set\_masked\_raw\_exit](group__subsys__tracing__apis__gpio.md#gacc4328675df61fc4d6aea6406328fec6)(port, ret) |
|  | Trace GPIO port set masked raw exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_set\_bits\_raw\_enter](group__subsys__tracing__apis__gpio.md#gae312b54e7983e48519e60be101d2f6cb)(port, pins) |
|  | Trace GPIO port set bits raw enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_set\_bits\_raw\_exit](group__subsys__tracing__apis__gpio.md#ga273a91c09bb777d3f436eab91ae69969)(port, ret) |
|  | Trace GPIO port set bits raw exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_clear\_bits\_raw\_enter](group__subsys__tracing__apis__gpio.md#ga8873f6d6af038b43a9f37c0912775608)(port, pins) |
|  | Trace GPIO port clear bits raw enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_clear\_bits\_raw\_exit](group__subsys__tracing__apis__gpio.md#ga4a4b88d5a585c0f772dbc8892b801efd)(port, ret) |
|  | Trace GPIO port clear bits raw exit call. |
| #define | [sys\_port\_trace\_gpio\_port\_toggle\_bits\_enter](group__subsys__tracing__apis__gpio.md#gaf5d4ac1b95410aa6ba7e543868e59928)(port, pins) |
|  | Trace GPIO port toggle bits enter call. |
| #define | [sys\_port\_trace\_gpio\_port\_toggle\_bits\_exit](group__subsys__tracing__apis__gpio.md#ga70f76ddf530aafa81488ca30d6ea4fb7)(port, ret) |
|  | Trace GPIO port toggle bits exit call. |
| #define | [sys\_port\_trace\_gpio\_init\_callback\_enter](group__subsys__tracing__apis__gpio.md#ga3c173c0b612671a9f44fd54efd288ac2)(callback, handler, pin\_mask) |
|  | Trace GPIO init callback enter call. |
| #define | [sys\_port\_trace\_gpio\_init\_callback\_exit](group__subsys__tracing__apis__gpio.md#ga4c130cd12803687e6b8dde1d82aa1d37)(callback) |
|  | Trace GPIO init callback exit call. |
| #define | [sys\_port\_trace\_gpio\_add\_callback\_enter](group__subsys__tracing__apis__gpio.md#ga70cacc72e4696340ed8d53578a13a325)(port, callback) |
|  | Trace GPIO add callback enter call. |
| #define | [sys\_port\_trace\_gpio\_add\_callback\_exit](group__subsys__tracing__apis__gpio.md#gaadca093d8a88c53f7f23ef80300b455a)(port, ret) |
|  | Trace GPIO add callback exit call. |
| #define | [sys\_port\_trace\_gpio\_remove\_callback\_enter](group__subsys__tracing__apis__gpio.md#ga2a756f3d1c60c51708492cbb08c9c3b3)(port, callback) |
|  | Trace GPIO remove callback enter call. |
| #define | [sys\_port\_trace\_gpio\_remove\_callback\_exit](group__subsys__tracing__apis__gpio.md#gaa7cb1d5a8b2205e610df66ee51dee39b)(port, ret) |
|  | Trace GPIO remove callback exit call. |
| #define | [sys\_port\_trace\_gpio\_get\_pending\_int\_enter](group__subsys__tracing__apis__gpio.md#ga29d20db6e85ac27181b697eeff1a405c)(dev) |
|  | Trace GPIO get pending interrupt enter call. |
| #define | [sys\_port\_trace\_gpio\_get\_pending\_int\_exit](group__subsys__tracing__apis__gpio.md#ga118077a21a3037e353fa9ff4ba404be6)(dev, ret) |
|  | Trace GPIO get pending interrupt exit call. |
| #define | [sys\_port\_trace\_gpio\_fire\_callbacks\_enter](group__subsys__tracing__apis__gpio.md#ga9cf081771e5f4724b02de3a89eec339c)(list, port, pins) |
| #define | [sys\_port\_trace\_gpio\_fire\_callback](group__subsys__tracing__apis__gpio.md#gaed3026e592853a9a97c0900a0687974b)(port, callback) |
| #define | [sys\_trace\_sys\_init\_enter](group__subsys__tracing__apis.md#ga9b5a02fc57b86d38f857597c7a2553f6)(entry, level) |
|  | Called when entering an init function. |
| #define | [sys\_trace\_sys\_init\_exit](group__subsys__tracing__apis.md#gacd56f9b376b4639cbe21e12055ca74c7)(entry, level, result) |
|  | Called when exiting an init function. |

| Functions | |
| --- | --- |
| void | [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4) (void) |
|  | Called when entering an ISR. |
| void | [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be) (void) |
|  | Called when exiting an ISR. |
| void | [sys\_trace\_isr\_exit\_to\_scheduler](group__subsys__tracing__apis.md#ga303fe60fd4de8ddcc02c6920656e326d) (void) |
|  | Called when exiting an ISR and switching to scheduler. |
| void | [sys\_trace\_idle](group__subsys__tracing__apis.md#gac9b542f78ed796b4b572de19d295c824) (void) |
|  | Called when the cpu enters the idle state. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [tracing](dir_c5f5a3ad31e756e37640fc6557a06392.md)
- [tracing.h](tracing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
