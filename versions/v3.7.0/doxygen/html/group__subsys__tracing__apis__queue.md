---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__subsys__tracing__apis__queue.html
original_path: doxygen/html/group__subsys__tracing__apis__queue.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Queue Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Queue Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_queue\_init](#ga40e74ce284e349d9e6fbe948c29d574f)(queue) |
|  | Trace initialization of Queue. |
| #define | [sys\_port\_trace\_k\_queue\_cancel\_wait](#ga8df6412be1cd3350c2b1976c7f7c8f4c)(queue) |
|  | Trace Queue cancel wait. |
| #define | [sys\_port\_trace\_k\_queue\_queue\_insert\_enter](#ga0e38a81f47c44e1be515b375f384a2d2)(queue, alloc) |
|  | Trace Queue insert attempt entry. |
| #define | [sys\_port\_trace\_k\_queue\_queue\_insert\_blocking](#ga3e51a4120f2ff7560ad494620c801886)(queue, alloc, timeout) |
|  | Trace Queue insert attempt blocking. |
| #define | [sys\_port\_trace\_k\_queue\_queue\_insert\_exit](#ga9fe7ee8315505734bf33d71083190533)(queue, alloc, ret) |
|  | Trace Queue insert attempt outcome. |
| #define | [sys\_port\_trace\_k\_queue\_append\_enter](#ga541411a2d9856fe01ed2e532a7e33db4)(queue) |
|  | Trace Queue append enter. |
| #define | [sys\_port\_trace\_k\_queue\_append\_exit](#ga1c1a038ffa1da2efd495f769f12bc685)(queue) |
|  | Trace Queue append exit. |
| #define | [sys\_port\_trace\_k\_queue\_alloc\_append\_enter](#ga5ef57f07d5ff8c730893f96b174f967a)(queue) |
|  | Trace Queue alloc append enter. |
| #define | [sys\_port\_trace\_k\_queue\_alloc\_append\_exit](#ga54601544ad750fb6a5afa725a19ce269)(queue, ret) |
|  | Trace Queue alloc append exit. |
| #define | [sys\_port\_trace\_k\_queue\_prepend\_enter](#ga90f15dc66fffd87e2b4fb66fb8bae4b1)(queue) |
|  | Trace Queue prepend enter. |
| #define | [sys\_port\_trace\_k\_queue\_prepend\_exit](#ga023a6fee85616ae5f32b5fa4b29d29e5)(queue) |
|  | Trace Queue prepend exit. |
| #define | [sys\_port\_trace\_k\_queue\_alloc\_prepend\_enter](#gaae4196d40be1a74439a1b7010626da17)(queue) |
|  | Trace Queue alloc prepend enter. |
| #define | [sys\_port\_trace\_k\_queue\_alloc\_prepend\_exit](#ga2d7ff756f5c017d7b3f10787716b5684)(queue, ret) |
|  | Trace Queue alloc prepend exit. |
| #define | [sys\_port\_trace\_k\_queue\_insert\_enter](#ga4e78ca5d7d927b912e09829b51e7330c)(queue) |
|  | Trace Queue insert attempt entry. |
| #define | [sys\_port\_trace\_k\_queue\_insert\_blocking](#gaad04f21122c554c33ef0cb394abf6df1)(queue, timeout) |
|  | Trace Queue insert attempt blocking. |
| #define | [sys\_port\_trace\_k\_queue\_insert\_exit](#ga69ca963f74777d9d351c9d20fe9dff62)(queue) |
|  | Trace Queue insert attempt exit. |
| #define | [sys\_port\_trace\_k\_queue\_append\_list\_enter](#ga777cfd6ee6ad016c2bbc519a490c0672)(queue) |
|  | Trace Queue append list enter. |
| #define | [sys\_port\_trace\_k\_queue\_append\_list\_exit](#ga215aca3523a17e31d4d36d3d95f28544)(queue, ret) |
|  | Trace Queue append list exit. |
| #define | [sys\_port\_trace\_k\_queue\_merge\_slist\_enter](#ga888a4a39d0c33fab4243c64e42011856)(queue) |
|  | Trace Queue merge slist enter. |
| #define | [sys\_port\_trace\_k\_queue\_merge\_slist\_exit](#ga87336faf8e19c64bcbf188452e336639)(queue, ret) |
|  | Trace Queue merge slist exit. |
| #define | [sys\_port\_trace\_k\_queue\_get\_enter](#ga59c1bac1a34c950c7ca324fc8d853acb)(queue, timeout) |
|  | Trace Queue get attempt enter. |
| #define | [sys\_port\_trace\_k\_queue\_get\_blocking](#gad83deb664f66df825b290b17f97156c7)(queue, timeout) |
|  | Trace Queue get attempt blockings. |
| #define | [sys\_port\_trace\_k\_queue\_get\_exit](#ga8afd074bab6b31d60169a72db51ef76c)(queue, timeout, ret) |
|  | Trace Queue get attempt outcome. |
| #define | [sys\_port\_trace\_k\_queue\_remove\_enter](#gacc2e453e717c654318dfd02e09288636)(queue) |
|  | Trace Queue remove enter. |
| #define | [sys\_port\_trace\_k\_queue\_remove\_exit](#ga1df298e35d176ca79924a9b534bb115c)(queue, ret) |
|  | Trace Queue remove exit. |
| #define | [sys\_port\_trace\_k\_queue\_unique\_append\_enter](#ga2842e4d5e778016ea70d5b860f217421)(queue) |
|  | Trace Queue unique append enter. |
| #define | [sys\_port\_trace\_k\_queue\_unique\_append\_exit](#ga830dfc12a35c0c001abfe2cbf89387aa)(queue, ret) |
|  | Trace Queue unique append exit. |
| #define | [sys\_port\_trace\_k\_queue\_peek\_head](#ga1cb5384c1eccc5d40c3e748dd1990cce)(queue, ret) |
|  | Trace Queue peek head. |
| #define | [sys\_port\_trace\_k\_queue\_peek\_tail](#gac28c33f0457d7e8f99e20d0fc55427ee)(queue, ret) |
|  | Trace Queue peek tail. |

## Detailed Description

Queue Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga5ef57f07d5ff8c730893f96b174f967a)sys\_port\_trace\_k\_queue\_alloc\_append\_enter

| #define sys\_port\_trace\_k\_queue\_alloc\_append\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue alloc append enter.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga54601544ad750fb6a5afa725a19ce269)sys\_port\_trace\_k\_queue\_alloc\_append\_exit

| #define sys\_port\_trace\_k\_queue\_alloc\_append\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue alloc append exit.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaae4196d40be1a74439a1b7010626da17)sys\_port\_trace\_k\_queue\_alloc\_prepend\_enter

| #define sys\_port\_trace\_k\_queue\_alloc\_prepend\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue alloc prepend enter.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga2d7ff756f5c017d7b3f10787716b5684)sys\_port\_trace\_k\_queue\_alloc\_prepend\_exit

| #define sys\_port\_trace\_k\_queue\_alloc\_prepend\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue alloc prepend exit.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga541411a2d9856fe01ed2e532a7e33db4)sys\_port\_trace\_k\_queue\_append\_enter

| #define sys\_port\_trace\_k\_queue\_append\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue append enter.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga1c1a038ffa1da2efd495f769f12bc685)sys\_port\_trace\_k\_queue\_append\_exit

| #define sys\_port\_trace\_k\_queue\_append\_exit | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue append exit.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga777cfd6ee6ad016c2bbc519a490c0672)sys\_port\_trace\_k\_queue\_append\_list\_enter

| #define sys\_port\_trace\_k\_queue\_append\_list\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue append list enter.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga215aca3523a17e31d4d36d3d95f28544)sys\_port\_trace\_k\_queue\_append\_list\_exit

| #define sys\_port\_trace\_k\_queue\_append\_list\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue append list exit.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga8df6412be1cd3350c2b1976c7f7c8f4c)sys\_port\_trace\_k\_queue\_cancel\_wait

| #define sys\_port\_trace\_k\_queue\_cancel\_wait | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue cancel wait.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#gad83deb664f66df825b290b17f97156c7)sys\_port\_trace\_k\_queue\_get\_blocking

| #define sys\_port\_trace\_k\_queue\_get\_blocking | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue get attempt blockings.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga59c1bac1a34c950c7ca324fc8d853acb)sys\_port\_trace\_k\_queue\_get\_enter

| #define sys\_port\_trace\_k\_queue\_get\_enter | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue get attempt enter.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga8afd074bab6b31d60169a72db51ef76c)sys\_port\_trace\_k\_queue\_get\_exit

| #define sys\_port\_trace\_k\_queue\_get\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue get attempt outcome.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#ga40e74ce284e349d9e6fbe948c29d574f)sys\_port\_trace\_k\_queue\_init

| #define sys\_port\_trace\_k\_queue\_init | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialization of Queue.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#gaad04f21122c554c33ef0cb394abf6df1)sys\_port\_trace\_k\_queue\_insert\_blocking

| #define sys\_port\_trace\_k\_queue\_insert\_blocking | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue insert attempt blocking.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga4e78ca5d7d927b912e09829b51e7330c)sys\_port\_trace\_k\_queue\_insert\_enter

| #define sys\_port\_trace\_k\_queue\_insert\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue insert attempt entry.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga69ca963f74777d9d351c9d20fe9dff62)sys\_port\_trace\_k\_queue\_insert\_exit

| #define sys\_port\_trace\_k\_queue\_insert\_exit | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue insert attempt exit.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga888a4a39d0c33fab4243c64e42011856)sys\_port\_trace\_k\_queue\_merge\_slist\_enter

| #define sys\_port\_trace\_k\_queue\_merge\_slist\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue merge slist enter.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga87336faf8e19c64bcbf188452e336639)sys\_port\_trace\_k\_queue\_merge\_slist\_exit

| #define sys\_port\_trace\_k\_queue\_merge\_slist\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue merge slist exit.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga1cb5384c1eccc5d40c3e748dd1990cce)sys\_port\_trace\_k\_queue\_peek\_head

| #define sys\_port\_trace\_k\_queue\_peek\_head | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue peek head.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gac28c33f0457d7e8f99e20d0fc55427ee)sys\_port\_trace\_k\_queue\_peek\_tail

| #define sys\_port\_trace\_k\_queue\_peek\_tail | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue peek tail.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga90f15dc66fffd87e2b4fb66fb8bae4b1)sys\_port\_trace\_k\_queue\_prepend\_enter

| #define sys\_port\_trace\_k\_queue\_prepend\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue prepend enter.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga023a6fee85616ae5f32b5fa4b29d29e5)sys\_port\_trace\_k\_queue\_prepend\_exit

| #define sys\_port\_trace\_k\_queue\_prepend\_exit | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue prepend exit.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga3e51a4120f2ff7560ad494620c801886)sys\_port\_trace\_k\_queue\_queue\_insert\_blocking

| #define sys\_port\_trace\_k\_queue\_queue\_insert\_blocking | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *alloc*, |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue insert attempt blocking.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | alloc | Allocation flag |
    | timeout | Timeout period |

## [◆ ](#ga0e38a81f47c44e1be515b375f384a2d2)sys\_port\_trace\_k\_queue\_queue\_insert\_enter

| #define sys\_port\_trace\_k\_queue\_queue\_insert\_enter | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *alloc* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue insert attempt entry.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | alloc | Allocation flag |

## [◆ ](#ga9fe7ee8315505734bf33d71083190533)sys\_port\_trace\_k\_queue\_queue\_insert\_exit

| #define sys\_port\_trace\_k\_queue\_queue\_insert\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *alloc*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue insert attempt outcome.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | alloc | Allocation flag |
    | ret | Return value |

## [◆ ](#gacc2e453e717c654318dfd02e09288636)sys\_port\_trace\_k\_queue\_remove\_enter

| #define sys\_port\_trace\_k\_queue\_remove\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue remove enter.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga1df298e35d176ca79924a9b534bb115c)sys\_port\_trace\_k\_queue\_remove\_exit

| #define sys\_port\_trace\_k\_queue\_remove\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue remove exit.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga2842e4d5e778016ea70d5b860f217421)sys\_port\_trace\_k\_queue\_unique\_append\_enter

| #define sys\_port\_trace\_k\_queue\_unique\_append\_enter | ( |  | *queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue unique append enter.

Parameters
:   | queue | Queue object |
    | --- | --- |

## [◆ ](#ga830dfc12a35c0c001abfe2cbf89387aa)sys\_port\_trace\_k\_queue\_unique\_append\_exit

| #define sys\_port\_trace\_k\_queue\_unique\_append\_exit | ( |  | *queue*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Queue unique append exit.

Parameters
:   | queue | Queue object |
    | --- | --- |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
