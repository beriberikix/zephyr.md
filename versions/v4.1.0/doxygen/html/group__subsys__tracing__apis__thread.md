---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__subsys__tracing__apis__thread.html
original_path: doxygen/html/group__subsys__tracing__apis__thread.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Thread Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Thread Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_thread\_foreach\_enter](#ga05f9560547bb1415c809d718f9bd03c8)() |
|  | Called when entering a k\_thread\_foreach call. |
| #define | [sys\_port\_trace\_k\_thread\_foreach\_exit](#ga0848db275a35dd5f840221d2a91d75fb)() |
|  | Called when exiting a k\_thread\_foreach call. |
| #define | [sys\_port\_trace\_k\_thread\_foreach\_unlocked\_enter](#gaf1136b18d6408da4fd9b1e8d767e390d)() |
|  | Called when entering a k\_thread\_foreach\_unlocked. |
| #define | [sys\_port\_trace\_k\_thread\_foreach\_unlocked\_exit](#gaa6f8160940e24df5483268949d0ca402)() |
|  | Called when exiting a k\_thread\_foreach\_unlocked. |
| #define | [sys\_port\_trace\_k\_thread\_create](#ga6140a4ec9c7b31d907b08793deb44ca7)(new\_thread) |
|  | Trace creating a Thread. |
| #define | [sys\_port\_trace\_k\_thread\_user\_mode\_enter](#ga4ca28fdba0a95bcceddadba86412f736)() |
|  | Trace Thread entering user mode. |
| #define | [sys\_port\_trace\_k\_thread\_join\_enter](#gabbad785e65db935917e4f1224893c9c1)(thread, timeout) |
|  | Called when entering a k\_thread\_join. |
| #define | [sys\_port\_trace\_k\_thread\_join\_blocking](#ga057858c554e988474ae0097dc1ccf83f)(thread, timeout) |
|  | Called when k\_thread\_join blocks. |
| #define | [sys\_port\_trace\_k\_thread\_join\_exit](#gabf77c5d93899ee85b4b4edd0c4c18490)(thread, timeout, ret) |
|  | Called when exiting k\_thread\_join. |
| #define | [sys\_port\_trace\_k\_thread\_sleep\_enter](#ga44cac2602a3b638fbf04eb0322b33736)(timeout) |
|  | Called when entering k\_thread\_sleep. |
| #define | [sys\_port\_trace\_k\_thread\_sleep\_exit](#ga91f7abaae3dcd7eec7ee001f8653cda6)(timeout, ret) |
|  | Called when exiting k\_thread\_sleep. |
| #define | [sys\_port\_trace\_k\_thread\_msleep\_enter](#ga9bd09050cedc7213b90d486dc672d6d6)(ms) |
|  | Called when entering k\_thread\_msleep. |
| #define | [sys\_port\_trace\_k\_thread\_msleep\_exit](#ga625bde038098aa8170e80205b4f3a15c)(ms, ret) |
|  | Called when exiting k\_thread\_msleep. |
| #define | [sys\_port\_trace\_k\_thread\_usleep\_enter](#ga55a7f87fac6b2a7eff7f18ba1ffa1559)(us) |
|  | Called when entering k\_thread\_usleep. |
| #define | [sys\_port\_trace\_k\_thread\_usleep\_exit](#ga41a7e55fa70047d242ebe403d3baa15a)(us, ret) |
|  | Called when exiting k\_thread\_usleep. |
| #define | [sys\_port\_trace\_k\_thread\_busy\_wait\_enter](#gada94114ae74457c1082f2453d6fd9be5)(usec\_to\_wait) |
|  | Called when entering k\_thread\_busy\_wait. |
| #define | [sys\_port\_trace\_k\_thread\_busy\_wait\_exit](#gaf8d4d01e8e662c9255f925ba64cdbd31)(usec\_to\_wait) |
|  | Called when exiting k\_thread\_busy\_wait. |
| #define | [sys\_port\_trace\_k\_thread\_yield](#ga24f6d9958154d7e424a1af95e59e797f)() |
|  | Called when a thread yields. |
| #define | [sys\_port\_trace\_k\_thread\_wakeup](#ga1676b0fe2f2b19bef646e73f129089db)(thread) |
|  | Called when a thread wakes up. |
| #define | [sys\_port\_trace\_k\_thread\_start](#ga097debbc4ba4f332a2728ad04152df1a)(thread) |
|  | Called when a thread is started. |
| #define | [sys\_port\_trace\_k\_thread\_abort](#gab0b43ffbe1ab9bb1ce962bab6c55c911)(thread) |
|  | Called when a thread is being aborted. |
| #define | [sys\_port\_trace\_k\_thread\_abort\_enter](#ga3d147d97bbca426b7f74f1418c6ff16b)(thread) |
|  | Called when a thread enters the k\_thread\_abort routine. |
| #define | [sys\_port\_trace\_k\_thread\_abort\_exit](#ga3e7c042978bd25ea41ed48addc3259bf)(thread) |
|  | Called when a thread exits the k\_thread\_abort routine. |
| #define | [sys\_port\_trace\_k\_thread\_priority\_set](#ga09ddf88b7d825dd02db8a1058dda66eb)(thread) |
|  | Called when setting priority of a thread. |
| #define | [sys\_port\_trace\_k\_thread\_suspend\_enter](#ga63bf5f0162d8596beae754cd614e2452)(thread) |
|  | Called when a thread enters the k\_thread\_suspend function. |
| #define | [sys\_port\_trace\_k\_thread\_suspend\_exit](#gaedc07c84df5eb7d4cbdf86560ec72bdd)(thread) |
|  | Called when a thread exits the k\_thread\_suspend function. |
| #define | [sys\_port\_trace\_k\_thread\_resume\_enter](#gaa04064835552055fc5c0d808a38cdc41)(thread) |
|  | Called when a thread enters the resume from suspension function. |
| #define | [sys\_port\_trace\_k\_thread\_resume\_exit](#ga38841a0e40592e49de6a24690905388e)(thread) |
|  | Called when a thread exits the resumed from suspension function. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_lock](#gadbd1fcca37d68a7a7b4c7061f3583764)() |
|  | Called when the thread scheduler is locked. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_unlock](#ga7d5ee7a2fd30678128def82112245741)() |
|  | Called when the thread scheduler is unlocked. |
| #define | [sys\_port\_trace\_k\_thread\_name\_set](#ga31ef5d08ff84619432b2dda7d239c479)(thread, ret) |
|  | Called when a thread name is set. |
| #define | [sys\_port\_trace\_k\_thread\_switched\_out](#ga61a5063e1543789c16add724fad5aef1)() |
|  | Called before a thread has been selected to run. |
| #define | [sys\_port\_trace\_k\_thread\_switched\_in](#ga89f53bfff5816ea7a1e4128677254634)() |
|  | Called after a thread has been selected to run. |
| #define | [sys\_port\_trace\_k\_thread\_ready](#ga6fe6a019530b96e308c751d7c3732d83)(thread) |
|  | Called when a thread is ready to run. |
| #define | [sys\_port\_trace\_k\_thread\_pend](#ga0b19ca107363fd060183cbb7b83927e8)(thread) |
|  | Called when a thread is pending. |
| #define | [sys\_port\_trace\_k\_thread\_info](#gaffe80c4e32e27089b4ccb99fd11205ea)(thread) |
|  | Provide information about specific thread. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_wakeup](#ga9f4b710eb3cc5ef0dabfadc9ad1cc448)(thread) |
|  | Trace implicit thread wakeup invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_abort](#gaa2213012f5c2650301f2467dc0e36e17)(thread) |
|  | Trace implicit thread abort invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_priority\_set](#ga906c658681af75d52d228fef96a39a92)(thread, prio) |
|  | Trace implicit thread set priority invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_ready](#ga1f5990be25a0c0eb348d788e5aaf04cb)(thread) |
|  | Trace implicit thread ready invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_pend](#gae857728d8f72259b6d282cb0b0bdb2ca)(thread) |
|  | Trace implicit thread pend invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_resume](#ga81d84b861192fa664be54e7a77f0cea4)(thread) |
|  | Trace implicit thread resume invocation by the scheduler. |
| #define | [sys\_port\_trace\_k\_thread\_sched\_suspend](#gaef5455dbd090fd7cf065d3fd8a8d3d1b)(thread) |
|  | Trace implicit thread suspend invocation by the scheduler. |

## Detailed Description

Thread Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gab0b43ffbe1ab9bb1ce962bab6c55c911)sys\_port\_trace\_k\_thread\_abort

| #define sys\_port\_trace\_k\_thread\_abort | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread is being aborted.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga3d147d97bbca426b7f74f1418c6ff16b)sys\_port\_trace\_k\_thread\_abort\_enter

| #define sys\_port\_trace\_k\_thread\_abort\_enter | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread enters the k\_thread\_abort routine.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga3e7c042978bd25ea41ed48addc3259bf)sys\_port\_trace\_k\_thread\_abort\_exit

| #define sys\_port\_trace\_k\_thread\_abort\_exit | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread exits the k\_thread\_abort routine.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#gada94114ae74457c1082f2453d6fd9be5)sys\_port\_trace\_k\_thread\_busy\_wait\_enter

| #define sys\_port\_trace\_k\_thread\_busy\_wait\_enter | ( |  | *usec\_to\_wait* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when entering k\_thread\_busy\_wait.

Parameters
:   | usec\_to\_wait | Duration in microseconds |
    | --- | --- |

## [◆ ](#gaf8d4d01e8e662c9255f925ba64cdbd31)sys\_port\_trace\_k\_thread\_busy\_wait\_exit

| #define sys\_port\_trace\_k\_thread\_busy\_wait\_exit | ( |  | *usec\_to\_wait* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when exiting k\_thread\_busy\_wait.

Parameters
:   | usec\_to\_wait | Duration in microseconds |
    | --- | --- |

## [◆ ](#ga6140a4ec9c7b31d907b08793deb44ca7)sys\_port\_trace\_k\_thread\_create

| #define sys\_port\_trace\_k\_thread\_create | ( |  | *new\_thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace creating a Thread.

Parameters
:   | new\_thread | Thread object |
    | --- | --- |

## [◆ ](#ga05f9560547bb1415c809d718f9bd03c8)sys\_port\_trace\_k\_thread\_foreach\_enter

| #define sys\_port\_trace\_k\_thread\_foreach\_enter | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when entering a k\_thread\_foreach call.

## [◆ ](#ga0848db275a35dd5f840221d2a91d75fb)sys\_port\_trace\_k\_thread\_foreach\_exit

| #define sys\_port\_trace\_k\_thread\_foreach\_exit | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when exiting a k\_thread\_foreach call.

## [◆ ](#gaf1136b18d6408da4fd9b1e8d767e390d)sys\_port\_trace\_k\_thread\_foreach\_unlocked\_enter

| #define sys\_port\_trace\_k\_thread\_foreach\_unlocked\_enter | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when entering a k\_thread\_foreach\_unlocked.

## [◆ ](#gaa6f8160940e24df5483268949d0ca402)sys\_port\_trace\_k\_thread\_foreach\_unlocked\_exit

| #define sys\_port\_trace\_k\_thread\_foreach\_unlocked\_exit | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when exiting a k\_thread\_foreach\_unlocked.

## [◆ ](#gaffe80c4e32e27089b4ccb99fd11205ea)sys\_port\_trace\_k\_thread\_info

| #define sys\_port\_trace\_k\_thread\_info | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Provide information about specific thread.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga057858c554e988474ae0097dc1ccf83f)sys\_port\_trace\_k\_thread\_join\_blocking

| #define sys\_port\_trace\_k\_thread\_join\_blocking | ( |  | *thread*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Called when k\_thread\_join blocks.

Parameters
:   | thread | Thread object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gabbad785e65db935917e4f1224893c9c1)sys\_port\_trace\_k\_thread\_join\_enter

| #define sys\_port\_trace\_k\_thread\_join\_enter | ( |  | *thread*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Called when entering a k\_thread\_join.

Parameters
:   | thread | Thread object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gabf77c5d93899ee85b4b4edd0c4c18490)sys\_port\_trace\_k\_thread\_join\_exit

| #define sys\_port\_trace\_k\_thread\_join\_exit | ( |  | *thread*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Called when exiting k\_thread\_join.

Parameters
:   | thread | Thread object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#ga9bd09050cedc7213b90d486dc672d6d6)sys\_port\_trace\_k\_thread\_msleep\_enter

| #define sys\_port\_trace\_k\_thread\_msleep\_enter | ( |  | *ms* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when entering k\_thread\_msleep.

Parameters
:   | ms | Duration in milliseconds |
    | --- | --- |

## [◆ ](#ga625bde038098aa8170e80205b4f3a15c)sys\_port\_trace\_k\_thread\_msleep\_exit

| #define sys\_port\_trace\_k\_thread\_msleep\_exit | ( |  | *ms*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Called when exiting k\_thread\_msleep.

Parameters
:   | ms | Duration in milliseconds |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga31ef5d08ff84619432b2dda7d239c479)sys\_port\_trace\_k\_thread\_name\_set

| #define sys\_port\_trace\_k\_thread\_name\_set | ( |  | *thread*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread name is set.

Parameters
:   | thread | Thread object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga0b19ca107363fd060183cbb7b83927e8)sys\_port\_trace\_k\_thread\_pend

| #define sys\_port\_trace\_k\_thread\_pend | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread is pending.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga09ddf88b7d825dd02db8a1058dda66eb)sys\_port\_trace\_k\_thread\_priority\_set

| #define sys\_port\_trace\_k\_thread\_priority\_set | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when setting priority of a thread.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga6fe6a019530b96e308c751d7c3732d83)sys\_port\_trace\_k\_thread\_ready

| #define sys\_port\_trace\_k\_thread\_ready | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread is ready to run.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#gaa04064835552055fc5c0d808a38cdc41)sys\_port\_trace\_k\_thread\_resume\_enter

| #define sys\_port\_trace\_k\_thread\_resume\_enter | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread enters the resume from suspension function.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga38841a0e40592e49de6a24690905388e)sys\_port\_trace\_k\_thread\_resume\_exit

| #define sys\_port\_trace\_k\_thread\_resume\_exit | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread exits the resumed from suspension function.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#gaa2213012f5c2650301f2467dc0e36e17)sys\_port\_trace\_k\_thread\_sched\_abort

| #define sys\_port\_trace\_k\_thread\_sched\_abort | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace implicit thread abort invocation by the scheduler.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#gadbd1fcca37d68a7a7b4c7061f3583764)sys\_port\_trace\_k\_thread\_sched\_lock

| #define sys\_port\_trace\_k\_thread\_sched\_lock | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when the thread scheduler is locked.

## [◆ ](#gae857728d8f72259b6d282cb0b0bdb2ca)sys\_port\_trace\_k\_thread\_sched\_pend

| #define sys\_port\_trace\_k\_thread\_sched\_pend | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace implicit thread pend invocation by the scheduler.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga906c658681af75d52d228fef96a39a92)sys\_port\_trace\_k\_thread\_sched\_priority\_set

| #define sys\_port\_trace\_k\_thread\_sched\_priority\_set | ( |  | *thread*, |
| --- | --- | --- | --- |
|  |  |  | *prio* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace implicit thread set priority invocation by the scheduler.

Parameters
:   | thread | Thread object |
    | --- | --- |
    | prio | Thread priority |

## [◆ ](#ga1f5990be25a0c0eb348d788e5aaf04cb)sys\_port\_trace\_k\_thread\_sched\_ready

| #define sys\_port\_trace\_k\_thread\_sched\_ready | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace implicit thread ready invocation by the scheduler.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga81d84b861192fa664be54e7a77f0cea4)sys\_port\_trace\_k\_thread\_sched\_resume

| #define sys\_port\_trace\_k\_thread\_sched\_resume | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace implicit thread resume invocation by the scheduler.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#gaef5455dbd090fd7cf065d3fd8a8d3d1b)sys\_port\_trace\_k\_thread\_sched\_suspend

| #define sys\_port\_trace\_k\_thread\_sched\_suspend | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace implicit thread suspend invocation by the scheduler.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga7d5ee7a2fd30678128def82112245741)sys\_port\_trace\_k\_thread\_sched\_unlock

| #define sys\_port\_trace\_k\_thread\_sched\_unlock | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when the thread scheduler is unlocked.

## [◆ ](#ga9f4b710eb3cc5ef0dabfadc9ad1cc448)sys\_port\_trace\_k\_thread\_sched\_wakeup

| #define sys\_port\_trace\_k\_thread\_sched\_wakeup | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace implicit thread wakeup invocation by the scheduler.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga44cac2602a3b638fbf04eb0322b33736)sys\_port\_trace\_k\_thread\_sleep\_enter

| #define sys\_port\_trace\_k\_thread\_sleep\_enter | ( |  | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when entering k\_thread\_sleep.

Parameters
:   | timeout | Timeout period |
    | --- | --- |

## [◆ ](#ga91f7abaae3dcd7eec7ee001f8653cda6)sys\_port\_trace\_k\_thread\_sleep\_exit

| #define sys\_port\_trace\_k\_thread\_sleep\_exit | ( |  | *timeout*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Called when exiting k\_thread\_sleep.

Parameters
:   | timeout | Timeout period |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga097debbc4ba4f332a2728ad04152df1a)sys\_port\_trace\_k\_thread\_start

| #define sys\_port\_trace\_k\_thread\_start | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread is started.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga63bf5f0162d8596beae754cd614e2452)sys\_port\_trace\_k\_thread\_suspend\_enter

| #define sys\_port\_trace\_k\_thread\_suspend\_enter | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread enters the k\_thread\_suspend function.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#gaedc07c84df5eb7d4cbdf86560ec72bdd)sys\_port\_trace\_k\_thread\_suspend\_exit

| #define sys\_port\_trace\_k\_thread\_suspend\_exit | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread exits the k\_thread\_suspend function.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga89f53bfff5816ea7a1e4128677254634)sys\_port\_trace\_k\_thread\_switched\_in

| #define sys\_port\_trace\_k\_thread\_switched\_in | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called after a thread has been selected to run.

## [◆ ](#ga61a5063e1543789c16add724fad5aef1)sys\_port\_trace\_k\_thread\_switched\_out

| #define sys\_port\_trace\_k\_thread\_switched\_out | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called before a thread has been selected to run.

## [◆ ](#ga4ca28fdba0a95bcceddadba86412f736)sys\_port\_trace\_k\_thread\_user\_mode\_enter

| #define sys\_port\_trace\_k\_thread\_user\_mode\_enter | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Thread entering user mode.

## [◆ ](#ga55a7f87fac6b2a7eff7f18ba1ffa1559)sys\_port\_trace\_k\_thread\_usleep\_enter

| #define sys\_port\_trace\_k\_thread\_usleep\_enter | ( |  | *us* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when entering k\_thread\_usleep.

Parameters
:   | us | Duration in microseconds |
    | --- | --- |

## [◆ ](#ga41a7e55fa70047d242ebe403d3baa15a)sys\_port\_trace\_k\_thread\_usleep\_exit

| #define sys\_port\_trace\_k\_thread\_usleep\_exit | ( |  | *us*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Called when exiting k\_thread\_usleep.

Parameters
:   | us | Duration in microseconds |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga1676b0fe2f2b19bef646e73f129089db)sys\_port\_trace\_k\_thread\_wakeup

| #define sys\_port\_trace\_k\_thread\_wakeup | ( |  | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread wakes up.

Parameters
:   | thread | Thread object |
    | --- | --- |

## [◆ ](#ga24f6d9958154d7e424a1af95e59e797f)sys\_port\_trace\_k\_thread\_yield

| #define sys\_port\_trace\_k\_thread\_yield | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Called when a thread yields.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
