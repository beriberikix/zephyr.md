---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/pthread_8h.html
original_path: doxygen/html/pthread_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pthread.h File Reference

`#include <[stdlib.h](stdlib_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/posix/time.h](include_2zephyr_2posix_2time_8h_source.md)>`  
`#include <[zephyr/posix/unistd.h](unistd_8h_source.md)>`  
`#include <[zephyr/posix/sched.h](posix_2sched_8h_source.md)>`

[Go to the source code of this file.](pthread_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PTHREAD\_CREATE\_DETACHED](#a391c5eb0f6b5febc48710d0be3f62394)   1 |
| #define | [PTHREAD\_CREATE\_JOINABLE](#afb10d234d831c7b57768d62786748bc7)   0 |
| #define | [PTHREAD\_PROCESS\_PRIVATE](#a443f2f512de9324bf77625041ecb04f4)   0 |
| #define | [PTHREAD\_PROCESS\_SHARED](#a07f3670a510cdb93233e84e1a0b50e89)   1 |
| #define | [PTHREAD\_CANCELED](#a17ddda04a6c1ee32116c49c85e2ac4ae)   ((void \*)-1) |
| #define | [PTHREAD\_CANCEL\_ENABLE](#aaf18882a8a6b82c7b7849a645f4445ef)   0 |
| #define | [PTHREAD\_CANCEL\_DISABLE](#a6c661332f782dcebc87b878990424b4c)   1 |
| #define | [PTHREAD\_CANCEL\_DEFERRED](#a7559901d88e4d3b8100b407e164cd75e)   0 |
| #define | [PTHREAD\_CANCEL\_ASYNCHRONOUS](#aae774738da39ed214c9b01f342222686)   1 |
| #define | [PTHREAD\_SCOPE\_PROCESS](#aeab18be4f4ee13db4b0b65c6768fb539)   1 |
| #define | [PTHREAD\_SCOPE\_SYSTEM](#ab754f4339f76c46b8f57413c03e8ec65)   0 |
| #define | [PTHREAD\_INHERIT\_SCHED](#a470fccc57c4d7c3846e446a17cd23573)   0 |
| #define | [PTHREAD\_EXPLICIT\_SCHED](#ad45abe03c8232518b6995e73172fe053)   1 |
| #define | [PTHREAD\_ONCE\_INIT](#a59e22497b65fc305ddb5cea8b4990b51)   {0} |
| #define | [PTHREAD\_STACK\_MIN](#a8b3dc1c5c1a165d6143b1dce950e8266)   [K\_KERNEL\_STACK\_LEN](kernel_2thread__stack_8h.md#a12f78cb2d5b9bf83068e810bf1e31937)(0) |
| #define | [PTHREAD\_COND\_INITIALIZER](#aa7b867fe46f3660283fcb356c4fcbbf0)   (-1) |
|  | Declare a condition variable as initialized. |
| #define | [PTHREAD\_MUTEX\_INITIALIZER](#a84e55100366a6a8338a2af3b3f279686)   (-1) |
|  | Declare a mutex as initialized. |
| #define | [PTHREAD\_RWLOCK\_INITIALIZER](#aa92fd7b492a8a5b31b2f8b3b6039c622)   (-1) |
|  | Declare a rwlock as initialized. |
| #define | [PTHREAD\_MUTEX\_NORMAL](#aae4b650085c2599674938f503d6253cf)   0 |
| #define | [PTHREAD\_MUTEX\_RECURSIVE](#a715e9644a7183d98cb2c9dd41cb89645)   1 |
| #define | [PTHREAD\_MUTEX\_ERRORCHECK](#aaf502496651f95b06be861af7902cb23)   2 |
| #define | [PTHREAD\_MUTEX\_DEFAULT](#a2a9b96c0491ae490c17d0b400bc427b0)   [PTHREAD\_MUTEX\_NORMAL](#aae4b650085c2599674938f503d6253cf) |
| #define | [PTHREAD\_PRIO\_NONE](#a8c1426a72025b27d9726580ac0e8404f)   0 |
| #define | [PTHREAD\_BARRIER\_SERIAL\_THREAD](#a822c63bc662ad86cfb2dcec50edbb42b)   1 |
| #define | [PTHREAD\_PROCESS\_PRIVATE](#a7c56b94733c97109259266d9c1f60338)   0 |
| #define | [PTHREAD\_PROCESS\_PUBLIC](#afff2f9c2b019a07298f341cf70ee829d)   1 |
| #define | [pthread\_cleanup\_push](#a265bda35a73d502fe8b710dc34f421cc)(\_rtn, \_arg) |
| #define | [pthread\_cleanup\_pop](#a234ffab9eecdb6ae28198aeeedb4f10c)(\_ex) |

| Functions | |
| --- | --- |
| int | [pthread\_cond\_init](#a319a61cdb25d069c9d4504e8225fd0c3) ([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv, const pthread\_condattr\_t \*att) |
|  | POSIX threading compatibility API. |
| int | [pthread\_cond\_destroy](#a8d44e4eae235f675bbab1b9163a3bc1d) ([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv) |
|  | POSIX threading compatibility API. |
| int | [pthread\_cond\_signal](#add1fea97e50755b5dbf4bd9a83b710dd) ([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv) |
|  | POSIX threading compatibility API. |
| int | [pthread\_cond\_broadcast](#a91ff7fff67462ce9216d299c89683119) ([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv) |
|  | POSIX threading compatibility API. |
| int | [pthread\_cond\_wait](#a61a1bf88d32de361e82ef4ea99b47322) ([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv, [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*mut) |
|  | POSIX threading compatibility API. |
| int | [pthread\_cond\_timedwait](#aecea498fbd2df02942790e5ccd7d78b2) ([pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \*cv, [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*mut, const struct [timespec](structtimespec.md) \*abstime) |
|  | POSIX threading compatibility API. |
| int | [pthread\_condattr\_init](#a01159da320b2317ee286a7e92d713f16) (pthread\_condattr\_t \*att) |
|  | POSIX threading compatibility API. |
| int | [pthread\_condattr\_destroy](#af37eaf73f0d83989d8efc06e676909f1) (pthread\_condattr\_t \*att) |
|  | POSIX threading compatibility API. |
| int | [pthread\_condattr\_getclock](#a77376b018eec6db2986939b847915a3c) (const pthread\_condattr\_t \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) att, [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) clock\_id) |
|  | POSIX threading compatibility API. |
| int | [pthread\_condattr\_setclock](#ac0b4f6d49deeab0ddb269a23ee303156) (pthread\_condattr\_t \*att, [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) clock\_id) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutex\_destroy](#af89d9cfa300f33b46720a96eac83d175) ([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutex\_lock](#afd70d6f2c50e22b996c926fb9d6ad291) ([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutex\_unlock](#a02a3c64dac70730e226c31c0e7dbb45c) ([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutex\_timedlock](#abbec44a62531009629601fbb34f1027c) ([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m, const struct [timespec](structtimespec.md) \*abstime) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutex\_trylock](#acc1ccbaf3d76572da85a8030bba1ede4) ([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutex\_init](#a7948bc0ea8a33439aece34d0fb3daf8b) ([pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \*m, const pthread\_mutexattr\_t \*att) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutexattr\_setprotocol](#ae7e6584c2b2cf9b9ff061115d2342bb5) (pthread\_mutexattr\_t \*attr, int protocol) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutexattr\_settype](#a8387c80e660e9426f801ac0217ecfae5) (pthread\_mutexattr\_t \*attr, int type) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutexattr\_getprotocol](#a200fcbc9157e6183376f83bc0e5937dd) (const pthread\_mutexattr\_t \*attr, int \*protocol) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutexattr\_gettype](#a7f064a4db96a009a5a9a7c7e5cc03599) (const pthread\_mutexattr\_t \*attr, int \*type) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutexattr\_init](#af98f6b6c483077a39d1400b1de1577b8) (pthread\_mutexattr\_t \*attr) |
|  | POSIX threading compatibility API. |
| int | [pthread\_mutexattr\_destroy](#a2321aabf58224b06021185708d0f9658) (pthread\_mutexattr\_t \*attr) |
|  | POSIX threading compatibility API. |
| int | [pthread\_barrier\_wait](#af786372165ba080986ae4143928c5436) ([pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \*b) |
|  | POSIX threading compatibility API. |
| int | [pthread\_barrier\_init](#aecc6c99901aac517072970e153863296) ([pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \*b, const [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*attr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int count) |
|  | POSIX threading compatibility API. |
| int | [pthread\_barrier\_destroy](#ab05ae13769e61dea9c53ca7894743c8f) ([pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \*b) |
|  | POSIX threading compatibility API. |
| int | [pthread\_barrierattr\_init](#ad540451ab679ace869b51c7cbb7b8486) ([pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*b) |
|  | POSIX threading compatibility API. |
| int | [pthread\_barrierattr\_destroy](#a5e27d4773f3d0552e36f2ff3b922a988) ([pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*b) |
|  | POSIX threading compatibility API. |
| int | [pthread\_barrierattr\_setpshared](#aa9c3c335f5bcf702fe85a1c12dcdc70e) ([pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*attr, int pshared) |
|  | POSIX threading compatibility API. |
| int | [pthread\_barrierattr\_getpshared](#a54e367403c0524680115b780ccfbc586) (const [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) attr, int \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) pshared) |
|  | POSIX threading compatibility API. |
| [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | [pthread\_self](#a4c4f5f3b4f8f45d9d897847d53b11aaa) (void) |
|  | Obtain ID of the calling thread. |
| int | [pthread\_equal](#a2a460fe3d4e4518057366f6ead455f4a) ([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pt1, [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pt2) |
|  | Compare thread IDs. |
| int | [pthread\_rwlockattr\_destroy](#a78a54e67f0afe2601dbda0a904fa0bdf) ([pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr) |
|  | Destroy the read-write lock attributes object. |
| int | [pthread\_rwlockattr\_init](#a9d831af0179ed16d1b6cbeba0304810b) ([pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr) |
|  | initialize the read-write lock attributes object. |
| int | [pthread\_rwlockattr\_getpshared](#a5ca1dea9ea7d3cfb34a9c8561e47cf02) (const [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) attr, int \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) pshared) |
| int | [pthread\_rwlockattr\_setpshared](#ae6550aa6aede71f618bb7457f3e50524) ([pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr, int pshared) |
| int | [pthread\_attr\_getguardsize](#abee3ae43d1f00b597111f6f82b0416a1) (const pthread\_attr\_t \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) guardsize) |
| int | [pthread\_attr\_getstacksize](#ae23600d4670359ab12bfba20db2c9a37) (const pthread\_attr\_t \*attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*stacksize) |
| int | [pthread\_attr\_setguardsize](#a532b31c11a9d87663053c5342400758c) (pthread\_attr\_t \*attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) guardsize) |
| int | [pthread\_attr\_setstacksize](#a812a9a455ae2ef2bb0dca4fff201a281) (pthread\_attr\_t \*attr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stacksize) |
| int | [pthread\_attr\_setschedpolicy](#a79b4c9e71486a87ef3014f1c660b33eb) (pthread\_attr\_t \*attr, int policy) |
| int | [pthread\_attr\_getschedpolicy](#af032906f326f3c209c7eed6bb248ebee) (const pthread\_attr\_t \*attr, int \*policy) |
| int | [pthread\_attr\_setdetachstate](#ae6ee78c307d8467b34a9b0c330993a54) (pthread\_attr\_t \*attr, int detachstate) |
| int | [pthread\_attr\_getdetachstate](#a391c34da42e68ddd24f5ee0c070d5c4f) (const pthread\_attr\_t \*attr, int \*detachstate) |
| int | [pthread\_attr\_init](#a0b85ebb1e3aac081a4c0a5e85ae3cbe9) (pthread\_attr\_t \*attr) |
| int | [pthread\_attr\_destroy](#a4bcdbf47c17c7dcc51e9f05f5cb56d81) (pthread\_attr\_t \*attr) |
| int | [pthread\_attr\_getschedparam](#abcd67baa86ff65d7ce65985d8b50d579) (const pthread\_attr\_t \*attr, struct sched\_param \*schedparam) |
| int | [pthread\_getschedparam](#ac60393667965dbd06670d3d280b65757) ([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pthread, int \*policy, struct sched\_param \*param) |
| int | [pthread\_attr\_getstack](#aec19ad460995a9fe8aeb4eaf2bb1ed1d) (const pthread\_attr\_t \*attr, void \*\*stackaddr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*stacksize) |
| int | [pthread\_attr\_setstack](#a94ede89b99a3a4fa17e516d30aaf3409) (pthread\_attr\_t \*attr, void \*stackaddr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stacksize) |
| int | [pthread\_attr\_getscope](#ad3fe01698c4fad85bb5cc3f9a2e82ea3) (const pthread\_attr\_t \*attr, int \*contentionscope) |
| int | [pthread\_attr\_setscope](#a6d8d320a882ba044a064975dddcf9ced) (pthread\_attr\_t \*attr, int contentionscope) |
| int | [pthread\_attr\_getinheritsched](#a79a77b688c30213e5e52e6be178cde4e) (const pthread\_attr\_t \*attr, int \*inheritsched) |
| int | [pthread\_attr\_setinheritsched](#ad437fe8caa3ef9f0cb7d69f6f6479df9) (pthread\_attr\_t \*attr, int inheritsched) |
| FUNC\_NORETURN void | [pthread\_exit](#ab9a027122b38833e8c2e1c0e733da3e6) (void \*retval) |
| int | [pthread\_join](#a6e4d503c2b358be5c98330f9006b3417) ([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, void \*\*status) |
| int | [pthread\_cancel](#a66a8f4bac5afe05538794218ff7c85ea) ([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pthread) |
| int | [pthread\_detach](#a7c275c509c26566b6dd95a2de1668a2f) ([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread) |
| int | [pthread\_create](#acb010e074930d81533ed20d319ca80b1) ([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) \*newthread, const pthread\_attr\_t \*attr, void \*(\*threadroutine)(void \*), void \*arg) |
| int | [pthread\_setcancelstate](#a37075410fbbaad7ee93c95375fc86e0e) (int [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), int \*oldstate) |
| int | [pthread\_setcanceltype](#aab579bcfcf0662a0c1e35fd82162e61d) (int type, int \*oldtype) |
| void | [pthread\_testcancel](#af1c95282ab2bea25f0888a19652cd41f) (void) |
| int | [pthread\_attr\_setschedparam](#a18b9aa91fe20481a25650df20c567ff5) (pthread\_attr\_t \*attr, const struct sched\_param \*schedparam) |
| int | [pthread\_setschedparam](#ad8e89d31b56c88d632ba9aeb956fa043) ([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pthread, int policy, const struct sched\_param \*param) |
| int | [pthread\_setschedprio](#a7a23cbcfc21a4e3edf531ed65f022370) ([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, int prio) |
| int | [pthread\_rwlock\_destroy](#a79839f0f4f4a768bf6d218faf377c209) ([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock) |
| int | [pthread\_rwlock\_init](#a1596a13569ec35ee66cc867586fd643d) ([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock, const [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*attr) |
| int | [pthread\_rwlock\_rdlock](#acc16fb32464b480d31bc69cce4e206c9) ([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock) |
| int | [pthread\_rwlock\_timedrdlock](#ad791558625e69852e4a435b7c1580468) ([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock, const struct [timespec](structtimespec.md) \*abstime) |
| int | [pthread\_rwlock\_timedwrlock](#a16c935f2f6146a95f9adbca71e0455e7) ([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock, const struct [timespec](structtimespec.md) \*abstime) |
| int | [pthread\_rwlock\_tryrdlock](#aae52fb1d3e6d03b18fa5731d0b49d197) ([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock) |
| int | [pthread\_rwlock\_trywrlock](#a065b618f7b786ed9bc7dddef4490cefb) ([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock) |
| int | [pthread\_rwlock\_unlock](#a7d3b987d99117fc10c4ef97230011983) ([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock) |
| int | [pthread\_rwlock\_wrlock](#a5ddd4cc028257f9baa9e23c2337abe3b) ([pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \*rwlock) |
| int | [pthread\_key\_create](#af4b7ced8ecff505380fe8216244a3764) (pthread\_key\_t \*key, void(\*destructor)(void \*)) |
| int | [pthread\_key\_delete](#aee96306dc79294927ee840bb4de2244b) (pthread\_key\_t key) |
| int | [pthread\_setspecific](#a2187333dd46ce08d9d2e044f79fad705) (pthread\_key\_t key, const void \*value) |
| void \* | [pthread\_getspecific](#acdf9f73a16ea40eba1bc174d38e76ca5) (pthread\_key\_t key) |
| int | [pthread\_atfork](#a80008474c3d68e9880da960a53d2f430) (void(\*prepare)(void), void(\*parent)(void), void(\*child)(void)) |
| int | [pthread\_getconcurrency](#afb4344ea91774ba279ea5df3cb656ebc) (void) |
| int | [pthread\_setconcurrency](#a46064892e8c4622e0a3ebe22d9792b92) (int new\_level) |
| int | [pthread\_setname\_np](#aa21465e084e7185bfbb94bb50d60cd08) ([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, const char \*name) |
|  | Set name of POSIX thread. |
| int | [pthread\_getname\_np](#a8d55a60492c979991dc1a361b5453813) ([pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) thread, char \*name, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Get name of POSIX thread and store in name buffer that is of size len. |

## Macro Definition Documentation

## [◆ ](#a822c63bc662ad86cfb2dcec50edbb42b)PTHREAD\_BARRIER\_SERIAL\_THREAD

| #define PTHREAD\_BARRIER\_SERIAL\_THREAD   1 |
| --- |

## [◆ ](#aae774738da39ed214c9b01f342222686)PTHREAD\_CANCEL\_ASYNCHRONOUS

| #define PTHREAD\_CANCEL\_ASYNCHRONOUS   1 |
| --- |

## [◆ ](#a7559901d88e4d3b8100b407e164cd75e)PTHREAD\_CANCEL\_DEFERRED

| #define PTHREAD\_CANCEL\_DEFERRED   0 |
| --- |

## [◆ ](#a6c661332f782dcebc87b878990424b4c)PTHREAD\_CANCEL\_DISABLE

| #define PTHREAD\_CANCEL\_DISABLE   1 |
| --- |

## [◆ ](#aaf18882a8a6b82c7b7849a645f4445ef)PTHREAD\_CANCEL\_ENABLE

| #define PTHREAD\_CANCEL\_ENABLE   0 |
| --- |

## [◆ ](#a17ddda04a6c1ee32116c49c85e2ac4ae)PTHREAD\_CANCELED

| #define PTHREAD\_CANCELED   ((void \*)-1) |
| --- |

## [◆ ](#a234ffab9eecdb6ae28198aeeedb4f10c)pthread\_cleanup\_pop

| #define pthread\_cleanup\_pop | ( |  | *\_ex* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_z\_pthread\_cleanup\_pop(\_ex); \

} /\* enforce '}'-like behaviour \*/ while (0)

## [◆ ](#a265bda35a73d502fe8b710dc34f421cc)pthread\_cleanup\_push

| #define pthread\_cleanup\_push | ( |  | *\_rtn*, |
| --- | --- | --- | --- |
|  |  |  | *\_arg* ) |

**Value:**

do /\* enforce '{'-like behaviour \*/ { \

void \*\_z\_pthread\_cleanup[3]; \

\_\_z\_pthread\_cleanup\_push(\_z\_pthread\_cleanup, \_rtn, \_arg)

## [◆ ](#aa7b867fe46f3660283fcb356c4fcbbf0)PTHREAD\_COND\_INITIALIZER

| #define PTHREAD\_COND\_INITIALIZER   (-1) |
| --- |

Declare a condition variable as initialized.

Initialize a condition variable with the default condition variable attributes.

## [◆ ](#a391c5eb0f6b5febc48710d0be3f62394)PTHREAD\_CREATE\_DETACHED

| #define PTHREAD\_CREATE\_DETACHED   1 |
| --- |

## [◆ ](#afb10d234d831c7b57768d62786748bc7)PTHREAD\_CREATE\_JOINABLE

| #define PTHREAD\_CREATE\_JOINABLE   0 |
| --- |

## [◆ ](#ad45abe03c8232518b6995e73172fe053)PTHREAD\_EXPLICIT\_SCHED

| #define PTHREAD\_EXPLICIT\_SCHED   1 |
| --- |

## [◆ ](#a470fccc57c4d7c3846e446a17cd23573)PTHREAD\_INHERIT\_SCHED

| #define PTHREAD\_INHERIT\_SCHED   0 |
| --- |

## [◆ ](#a2a9b96c0491ae490c17d0b400bc427b0)PTHREAD\_MUTEX\_DEFAULT

| #define PTHREAD\_MUTEX\_DEFAULT   [PTHREAD\_MUTEX\_NORMAL](#aae4b650085c2599674938f503d6253cf) |
| --- |

## [◆ ](#aaf502496651f95b06be861af7902cb23)PTHREAD\_MUTEX\_ERRORCHECK

| #define PTHREAD\_MUTEX\_ERRORCHECK   2 |
| --- |

## [◆ ](#a84e55100366a6a8338a2af3b3f279686)PTHREAD\_MUTEX\_INITIALIZER

| #define PTHREAD\_MUTEX\_INITIALIZER   (-1) |
| --- |

Declare a mutex as initialized.

Initialize a mutex with the default mutex attributes.

## [◆ ](#aae4b650085c2599674938f503d6253cf)PTHREAD\_MUTEX\_NORMAL

| #define PTHREAD\_MUTEX\_NORMAL   0 |
| --- |

## [◆ ](#a715e9644a7183d98cb2c9dd41cb89645)PTHREAD\_MUTEX\_RECURSIVE

| #define PTHREAD\_MUTEX\_RECURSIVE   1 |
| --- |

## [◆ ](#a59e22497b65fc305ddb5cea8b4990b51)PTHREAD\_ONCE\_INIT

| #define PTHREAD\_ONCE\_INIT   {0} |
| --- |

## [◆ ](#a8c1426a72025b27d9726580ac0e8404f)PTHREAD\_PRIO\_NONE

| #define PTHREAD\_PRIO\_NONE   0 |
| --- |

## [◆ ](#a7c56b94733c97109259266d9c1f60338)PTHREAD\_PROCESS\_PRIVATE [1/2]

| #define PTHREAD\_PROCESS\_PRIVATE   0 |
| --- |

## [◆ ](#a443f2f512de9324bf77625041ecb04f4)PTHREAD\_PROCESS\_PRIVATE [2/2]

| #define PTHREAD\_PROCESS\_PRIVATE   0 |
| --- |

## [◆ ](#afff2f9c2b019a07298f341cf70ee829d)PTHREAD\_PROCESS\_PUBLIC

| #define PTHREAD\_PROCESS\_PUBLIC   1 |
| --- |

## [◆ ](#a07f3670a510cdb93233e84e1a0b50e89)PTHREAD\_PROCESS\_SHARED

| #define PTHREAD\_PROCESS\_SHARED   1 |
| --- |

## [◆ ](#aa92fd7b492a8a5b31b2f8b3b6039c622)PTHREAD\_RWLOCK\_INITIALIZER

| #define PTHREAD\_RWLOCK\_INITIALIZER   (-1) |
| --- |

Declare a rwlock as initialized.

Initialize a rwlock with the default rwlock attributes.

## [◆ ](#aeab18be4f4ee13db4b0b65c6768fb539)PTHREAD\_SCOPE\_PROCESS

| #define PTHREAD\_SCOPE\_PROCESS   1 |
| --- |

## [◆ ](#ab754f4339f76c46b8f57413c03e8ec65)PTHREAD\_SCOPE\_SYSTEM

| #define PTHREAD\_SCOPE\_SYSTEM   0 |
| --- |

## [◆ ](#a8b3dc1c5c1a165d6143b1dce950e8266)PTHREAD\_STACK\_MIN

| #define PTHREAD\_STACK\_MIN   [K\_KERNEL\_STACK\_LEN](kernel_2thread__stack_8h.md#a12f78cb2d5b9bf83068e810bf1e31937)(0) |
| --- |

## Function Documentation

## [◆ ](#a80008474c3d68e9880da960a53d2f430)pthread\_atfork()

| int pthread\_atfork | ( | void(\* | *prepare*)(void), |
| --- | --- | --- | --- |
|  |  | void(\* | *parent*)(void), |
|  |  | void(\* | *child*)(void) ) |

## [◆ ](#a4bcdbf47c17c7dcc51e9f05f5cb56d81)pthread\_attr\_destroy()

| int pthread\_attr\_destroy | ( | pthread\_attr\_t \* | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a391c34da42e68ddd24f5ee0c070d5c4f)pthread\_attr\_getdetachstate()

| int pthread\_attr\_getdetachstate | ( | const pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int \* | *detachstate* ) |

## [◆ ](#abee3ae43d1f00b597111f6f82b0416a1)pthread\_attr\_getguardsize()

| int pthread\_attr\_getguardsize | ( | const pthread\_attr\_t \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *attr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *guardsize* ) |

## [◆ ](#a79a77b688c30213e5e52e6be178cde4e)pthread\_attr\_getinheritsched()

| int pthread\_attr\_getinheritsched | ( | const pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int \* | *inheritsched* ) |

## [◆ ](#abcd67baa86ff65d7ce65985d8b50d579)pthread\_attr\_getschedparam()

| int pthread\_attr\_getschedparam | ( | const pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | struct sched\_param \* | *schedparam* ) |

## [◆ ](#af032906f326f3c209c7eed6bb248ebee)pthread\_attr\_getschedpolicy()

| int pthread\_attr\_getschedpolicy | ( | const pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int \* | *policy* ) |

## [◆ ](#ad3fe01698c4fad85bb5cc3f9a2e82ea3)pthread\_attr\_getscope()

| int pthread\_attr\_getscope | ( | const pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int \* | *contentionscope* ) |

## [◆ ](#aec19ad460995a9fe8aeb4eaf2bb1ed1d)pthread\_attr\_getstack()

| int pthread\_attr\_getstack | ( | const pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | void \*\* | *stackaddr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *stacksize* ) |

## [◆ ](#ae23600d4670359ab12bfba20db2c9a37)pthread\_attr\_getstacksize()

| int pthread\_attr\_getstacksize | ( | const pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *stacksize* ) |

## [◆ ](#a0b85ebb1e3aac081a4c0a5e85ae3cbe9)pthread\_attr\_init()

| int pthread\_attr\_init | ( | pthread\_attr\_t \* | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae6ee78c307d8467b34a9b0c330993a54)pthread\_attr\_setdetachstate()

| int pthread\_attr\_setdetachstate | ( | pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int | *detachstate* ) |

## [◆ ](#a532b31c11a9d87663053c5342400758c)pthread\_attr\_setguardsize()

| int pthread\_attr\_setguardsize | ( | pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *guardsize* ) |

## [◆ ](#ad437fe8caa3ef9f0cb7d69f6f6479df9)pthread\_attr\_setinheritsched()

| int pthread\_attr\_setinheritsched | ( | pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int | *inheritsched* ) |

## [◆ ](#a18b9aa91fe20481a25650df20c567ff5)pthread\_attr\_setschedparam()

| int pthread\_attr\_setschedparam | ( | pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | const struct sched\_param \* | *schedparam* ) |

## [◆ ](#a79b4c9e71486a87ef3014f1c660b33eb)pthread\_attr\_setschedpolicy()

| int pthread\_attr\_setschedpolicy | ( | pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int | *policy* ) |

## [◆ ](#a6d8d320a882ba044a064975dddcf9ced)pthread\_attr\_setscope()

| int pthread\_attr\_setscope | ( | pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int | *contentionscope* ) |

## [◆ ](#a94ede89b99a3a4fa17e516d30aaf3409)pthread\_attr\_setstack()

| int pthread\_attr\_setstack | ( | pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | void \* | *stackaddr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *stacksize* ) |

## [◆ ](#a812a9a455ae2ef2bb0dca4fff201a281)pthread\_attr\_setstacksize()

| int pthread\_attr\_setstacksize | ( | pthread\_attr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *stacksize* ) |

## [◆ ](#ab05ae13769e61dea9c53ca7894743c8f)pthread\_barrier\_destroy()

| int pthread\_barrier\_destroy | ( | [pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \* | *b* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#aecc6c99901aac517072970e153863296)pthread\_barrier\_init()

| int pthread\_barrier\_init | ( | [pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \* | *b*, |
| --- | --- | --- | --- |
|  |  | const [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \* | *attr*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *count* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#af786372165ba080986ae4143928c5436)pthread\_barrier\_wait()

| int pthread\_barrier\_wait | ( | [pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2) \* | *b* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a5e27d4773f3d0552e36f2ff3b922a988)pthread\_barrierattr\_destroy()

| int pthread\_barrierattr\_destroy | ( | [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \* | *b* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a54e367403c0524680115b780ccfbc586)pthread\_barrierattr\_getpshared()

| int pthread\_barrierattr\_getpshared | ( | const [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *attr*, |
| --- | --- | --- | --- |
|  |  | int \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *pshared* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#ad540451ab679ace869b51c7cbb7b8486)pthread\_barrierattr\_init()

| int pthread\_barrierattr\_init | ( | [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \* | *b* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#aa9c3c335f5bcf702fe85a1c12dcdc70e)pthread\_barrierattr\_setpshared()

| int pthread\_barrierattr\_setpshared | ( | [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b) \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int | *pshared* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a66a8f4bac5afe05538794218ff7c85ea)pthread\_cancel()

| int pthread\_cancel | ( | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | *pthread* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a91ff7fff67462ce9216d299c89683119)pthread\_cond\_broadcast()

| int pthread\_cond\_broadcast | ( | [pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \* | *cv* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a8d44e4eae235f675bbab1b9163a3bc1d)pthread\_cond\_destroy()

| int pthread\_cond\_destroy | ( | [pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \* | *cv* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a319a61cdb25d069c9d4504e8225fd0c3)pthread\_cond\_init()

| int pthread\_cond\_init | ( | [pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \* | *cv*, |
| --- | --- | --- | --- |
|  |  | const pthread\_condattr\_t \* | *att* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#add1fea97e50755b5dbf4bd9a83b710dd)pthread\_cond\_signal()

| int pthread\_cond\_signal | ( | [pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \* | *cv* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#aecea498fbd2df02942790e5ccd7d78b2)pthread\_cond\_timedwait()

| int pthread\_cond\_timedwait | ( | [pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \* | *cv*, |
| --- | --- | --- | --- |
|  |  | [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \* | *mut*, |
|  |  | const struct [timespec](structtimespec.md) \* | *abstime* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a61a1bf88d32de361e82ef4ea99b47322)pthread\_cond\_wait()

| int pthread\_cond\_wait | ( | [pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e) \* | *cv*, |
| --- | --- | --- | --- |
|  |  | [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \* | *mut* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#af37eaf73f0d83989d8efc06e676909f1)pthread\_condattr\_destroy()

| int pthread\_condattr\_destroy | ( | pthread\_condattr\_t \* | *att* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a77376b018eec6db2986939b847915a3c)pthread\_condattr\_getclock()

| int pthread\_condattr\_getclock | ( | const pthread\_condattr\_t \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *att*, |
| --- | --- | --- | --- |
|  |  | [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *clock\_id* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a01159da320b2317ee286a7e92d713f16)pthread\_condattr\_init()

| int pthread\_condattr\_init | ( | pthread\_condattr\_t \* | *att* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1.

## [◆ ](#ac0b4f6d49deeab0ddb269a23ee303156)pthread\_condattr\_setclock()

| int pthread\_condattr\_setclock | ( | pthread\_condattr\_t \* | *att*, |
| --- | --- | --- | --- |
|  |  | [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) | *clock\_id* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#acb010e074930d81533ed20d319ca80b1)pthread\_create()

| int pthread\_create | ( | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) \* | *newthread*, |
| --- | --- | --- | --- |
|  |  | const pthread\_attr\_t \* | *attr*, |
|  |  | void \*(\* | *threadroutine*)(void \*), |
|  |  | void \* | *arg* ) |

## [◆ ](#a7c275c509c26566b6dd95a2de1668a2f)pthread\_detach()

| int pthread\_detach | ( | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a2a460fe3d4e4518057366f6ead455f4a)pthread\_equal()

| int pthread\_equal | ( | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | *pt1*, |
| --- | --- | --- | --- |
|  |  | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | *pt2* ) |

Compare thread IDs.

See IEEE 1003.1

## [◆ ](#ab9a027122b38833e8c2e1c0e733da3e6)pthread\_exit()

| FUNC\_NORETURN void pthread\_exit | ( | void \* | *retval* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#afb4344ea91774ba279ea5df3cb656ebc)pthread\_getconcurrency()

| int pthread\_getconcurrency | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a8d55a60492c979991dc1a361b5453813)pthread\_getname\_np()

| int pthread\_getname\_np | ( | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | *thread*, |
| --- | --- | --- | --- |
|  |  | char \* | *name*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

Get name of POSIX thread and store in name buffer that is of size len.

Non-portable, extension function that conforms with most other definitions of this function.

Parameters
:   | thread | POSIX thread to obtain name information |
    | --- | --- |
    | name | Destination buffer |
    | len | Destination buffer size |

Return values
:   | 0 | Success |
    | --- | --- |
    | [ESRCH](group__system__errno.md#ga462e47a8af6288232a5df548221ada4c "No such context.") | Thread does not exist |
    | [EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4 "Invalid argument.") | Name buffer is NULL |
    | Negative | value if kernel function error |

## [◆ ](#ac60393667965dbd06670d3d280b65757)pthread\_getschedparam()

| int pthread\_getschedparam | ( | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | *pthread*, |
| --- | --- | --- | --- |
|  |  | int \* | *policy*, |
|  |  | struct sched\_param \* | *param* ) |

## [◆ ](#acdf9f73a16ea40eba1bc174d38e76ca5)pthread\_getspecific()

| void \* pthread\_getspecific | ( | pthread\_key\_t | *key* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a6e4d503c2b358be5c98330f9006b3417)pthread\_join()

| int pthread\_join | ( | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | *thread*, |
| --- | --- | --- | --- |
|  |  | void \*\* | *status* ) |

## [◆ ](#af4b7ced8ecff505380fe8216244a3764)pthread\_key\_create()

| int pthread\_key\_create | ( | pthread\_key\_t \* | *key*, |
| --- | --- | --- | --- |
|  |  | void(\* | *destructor*)(void \*) ) |

## [◆ ](#aee96306dc79294927ee840bb4de2244b)pthread\_key\_delete()

| int pthread\_key\_delete | ( | pthread\_key\_t | *key* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#af89d9cfa300f33b46720a96eac83d175)pthread\_mutex\_destroy()

| int pthread\_mutex\_destroy | ( | [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \* | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a7948bc0ea8a33439aece34d0fb3daf8b)pthread\_mutex\_init()

| int pthread\_mutex\_init | ( | [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \* | *m*, |
| --- | --- | --- | --- |
|  |  | const pthread\_mutexattr\_t \* | *att* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#afd70d6f2c50e22b996c926fb9d6ad291)pthread\_mutex\_lock()

| int pthread\_mutex\_lock | ( | [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \* | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#abbec44a62531009629601fbb34f1027c)pthread\_mutex\_timedlock()

| int pthread\_mutex\_timedlock | ( | [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \* | *m*, |
| --- | --- | --- | --- |
|  |  | const struct [timespec](structtimespec.md) \* | *abstime* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#acc1ccbaf3d76572da85a8030bba1ede4)pthread\_mutex\_trylock()

| int pthread\_mutex\_trylock | ( | [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \* | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a02a3c64dac70730e226c31c0e7dbb45c)pthread\_mutex\_unlock()

| int pthread\_mutex\_unlock | ( | [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e) \* | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a2321aabf58224b06021185708d0f9658)pthread\_mutexattr\_destroy()

| int pthread\_mutexattr\_destroy | ( | pthread\_mutexattr\_t \* | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

Note that pthread attribute structs are currently noops in Zephyr.

## [◆ ](#a200fcbc9157e6183376f83bc0e5937dd)pthread\_mutexattr\_getprotocol()

| int pthread\_mutexattr\_getprotocol | ( | const pthread\_mutexattr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int \* | *protocol* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a7f064a4db96a009a5a9a7c7e5cc03599)pthread\_mutexattr\_gettype()

| int pthread\_mutexattr\_gettype | ( | const pthread\_mutexattr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int \* | *type* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#af98f6b6c483077a39d1400b1de1577b8)pthread\_mutexattr\_init()

| int pthread\_mutexattr\_init | ( | pthread\_mutexattr\_t \* | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

POSIX threading compatibility API.

See IEEE 1003.1

Note that pthread attribute structs are currently noops in Zephyr.

## [◆ ](#ae7e6584c2b2cf9b9ff061115d2342bb5)pthread\_mutexattr\_setprotocol()

| int pthread\_mutexattr\_setprotocol | ( | pthread\_mutexattr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int | *protocol* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a8387c80e660e9426f801ac0217ecfae5)pthread\_mutexattr\_settype()

| int pthread\_mutexattr\_settype | ( | pthread\_mutexattr\_t \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int | *type* ) |

POSIX threading compatibility API.

See IEEE 1003.1

## [◆ ](#a79839f0f4f4a768bf6d218faf377c209)pthread\_rwlock\_destroy()

| int pthread\_rwlock\_destroy | ( | [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \* | *rwlock* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a1596a13569ec35ee66cc867586fd643d)pthread\_rwlock\_init()

| int pthread\_rwlock\_init | ( | [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \* | *rwlock*, |
| --- | --- | --- | --- |
|  |  | const [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \* | *attr* ) |

## [◆ ](#acc16fb32464b480d31bc69cce4e206c9)pthread\_rwlock\_rdlock()

| int pthread\_rwlock\_rdlock | ( | [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \* | *rwlock* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ad791558625e69852e4a435b7c1580468)pthread\_rwlock\_timedrdlock()

| int pthread\_rwlock\_timedrdlock | ( | [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \* | *rwlock*, |
| --- | --- | --- | --- |
|  |  | const struct [timespec](structtimespec.md) \* | *abstime* ) |

## [◆ ](#a16c935f2f6146a95f9adbca71e0455e7)pthread\_rwlock\_timedwrlock()

| int pthread\_rwlock\_timedwrlock | ( | [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \* | *rwlock*, |
| --- | --- | --- | --- |
|  |  | const struct [timespec](structtimespec.md) \* | *abstime* ) |

## [◆ ](#aae52fb1d3e6d03b18fa5731d0b49d197)pthread\_rwlock\_tryrdlock()

| int pthread\_rwlock\_tryrdlock | ( | [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \* | *rwlock* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a065b618f7b786ed9bc7dddef4490cefb)pthread\_rwlock\_trywrlock()

| int pthread\_rwlock\_trywrlock | ( | [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \* | *rwlock* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a7d3b987d99117fc10c4ef97230011983)pthread\_rwlock\_unlock()

| int pthread\_rwlock\_unlock | ( | [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \* | *rwlock* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a5ddd4cc028257f9baa9e23c2337abe3b)pthread\_rwlock\_wrlock()

| int pthread\_rwlock\_wrlock | ( | [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6) \* | *rwlock* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a78a54e67f0afe2601dbda0a904fa0bdf)pthread\_rwlockattr\_destroy()

| int pthread\_rwlockattr\_destroy | ( | [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \* | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

Destroy the read-write lock attributes object.

See IEEE 1003.1

## [◆ ](#a5ca1dea9ea7d3cfb34a9c8561e47cf02)pthread\_rwlockattr\_getpshared()

| int pthread\_rwlockattr\_getpshared | ( | const [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *attr*, |
| --- | --- | --- | --- |
|  |  | int \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *pshared* ) |

## [◆ ](#a9d831af0179ed16d1b6cbeba0304810b)pthread\_rwlockattr\_init()

| int pthread\_rwlockattr\_init | ( | [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \* | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

initialize the read-write lock attributes object.

See IEEE 1003.1

## [◆ ](#ae6550aa6aede71f618bb7457f3e50524)pthread\_rwlockattr\_setpshared()

| int pthread\_rwlockattr\_setpshared | ( | [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f) \* | *attr*, |
| --- | --- | --- | --- |
|  |  | int | *pshared* ) |

## [◆ ](#a4c4f5f3b4f8f45d9d897847d53b11aaa)pthread\_self()

| [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) pthread\_self | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Obtain ID of the calling thread.

The results of calling this API from threads not created with [pthread\_create()](#acb010e074930d81533ed20d319ca80b1) are undefined.

See IEEE 1003.1

## [◆ ](#a37075410fbbaad7ee93c95375fc86e0e)pthread\_setcancelstate()

| int pthread\_setcancelstate | ( | int | *state*, |
| --- | --- | --- | --- |
|  |  | int \* | *oldstate* ) |

## [◆ ](#aab579bcfcf0662a0c1e35fd82162e61d)pthread\_setcanceltype()

| int pthread\_setcanceltype | ( | int | *type*, |
| --- | --- | --- | --- |
|  |  | int \* | *oldtype* ) |

## [◆ ](#a46064892e8c4622e0a3ebe22d9792b92)pthread\_setconcurrency()

| int pthread\_setconcurrency | ( | int | *new\_level* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aa21465e084e7185bfbb94bb50d60cd08)pthread\_setname\_np()

| int pthread\_setname\_np | ( | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | *thread*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name* ) |

Set name of POSIX thread.

Non-portable, extension function that conforms with most other definitions of this function.

Parameters
:   | thread | POSIX thread to set name |
    | --- | --- |
    | name | Name string |

Return values
:   | 0 | Success |
    | --- | --- |
    | [ESRCH](group__system__errno.md#ga462e47a8af6288232a5df548221ada4c "No such context.") | Thread does not exist |
    | [EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4 "Invalid argument.") | Name buffer is NULL |
    | Negative | value if kernel function error |

## [◆ ](#ad8e89d31b56c88d632ba9aeb956fa043)pthread\_setschedparam()

| int pthread\_setschedparam | ( | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | *pthread*, |
| --- | --- | --- | --- |
|  |  | int | *policy*, |
|  |  | const struct sched\_param \* | *param* ) |

## [◆ ](#a7a23cbcfc21a4e3edf531ed65f022370)pthread\_setschedprio()

| int pthread\_setschedprio | ( | [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec) | *thread*, |
| --- | --- | --- | --- |
|  |  | int | *prio* ) |

## [◆ ](#a2187333dd46ce08d9d2e044f79fad705)pthread\_setspecific()

| int pthread\_setspecific | ( | pthread\_key\_t | *key*, |
| --- | --- | --- | --- |
|  |  | const void \* | *value* ) |

## [◆ ](#af1c95282ab2bea25f0888a19652cd41f)pthread\_testcancel()

| void pthread\_testcancel | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [pthread.h](pthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
