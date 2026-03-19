---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ztest__ztress.html
original_path: doxygen/html/group__ztest__ztress.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ztest ztress macros

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md)

This module provides test stress when using Ztest.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ztress\_context\_data](structztress__context__data.md) |

| Macros | |
| --- | --- |
| #define | [ZTRESS\_TIMER](#gabab05b8db44a7024ce23cb34bf999e42)(handler, user\_data, exec\_cnt, init\_timeout) |
|  | Descriptor of a k\_timer handler execution context. |
| #define | [ZTRESS\_THREAD](#gaed561641541e8ced6866f2f1227f21c0)(handler, user\_data, exec\_cnt, preempt\_cnt, init\_timeout) |
|  | Descriptor of a thread execution context. |
| #define | [ZTRESS\_CONTEXT\_INITIALIZER](#gab5e8bbcecd77db06e7a90631fc0c202b)(\_handler, \_user\_data, \_exec\_cnt, \_preempt\_cnt, \_t) |
|  | Initialize context structure. |
| #define | [ZTRESS\_EXECUTE](#ga6acc3a50e0eff7360873006482f5c8e9)(...) |
|  | Setup and run stress test. |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [ztress\_handler](#ga633439263754bf08baee06c37dddab40)) (void \*user\_data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last, int prio) |
|  | User handler called in one of the configured contexts. |

| Functions | |
| --- | --- |
| int | [ztress\_execute](#gaf706f1af4c42f5925d7545dadf5548fd) (struct [ztress\_context\_data](structztress__context__data.md) \*timer\_data, struct [ztress\_context\_data](structztress__context__data.md) \*thread\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cnt) |
|  | Execute contexts. |
| void | [ztress\_abort](#ga57f171e230fba462b3dea6b2d3cf71f6) (void) |
|  | Abort ongoing stress test. |
| void | [ztress\_set\_timeout](#ga5b3069bb2aa35ddc64c46c18d2e30091) ([k\_timeout\_t](structk__timeout__t.md) t) |
|  | Set test timeout. |
| void | [ztress\_report](#gaf4db2092eee17d863c9810333ba4c870) (void) |
|  | Print last test report. |
| int | [ztress\_exec\_count](#ga99eeabcc672fc5ec0b83ce5b8fb4ec5b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Get number of executions of a given context in the last test. |
| int | [ztress\_preempt\_count](#ga4406b828d170bc19065aaf65aeb4613e) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Get number of preemptions of a given context in the last test. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ztress\_optimized\_ticks](#gacbbdb8e7bad532d6dd20c486b3256e21) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Get optimized timeout base of a given context in the last test. |

## Detailed Description

This module provides test stress when using Ztest.

## Macro Definition Documentation

## [◆ ](#gab5e8bbcecd77db06e7a90631fc0c202b)ZTRESS\_CONTEXT\_INITIALIZER

| #define ZTRESS\_CONTEXT\_INITIALIZER | ( |  | *\_handler*, |
| --- | --- | --- | --- |
|  |  |  | *\_user\_data*, |
|  |  |  | *\_exec\_cnt*, |
|  |  |  | *\_preempt\_cnt*, |
|  |  |  | *\_t* ) |

`#include <[ztress.h](ztress_8h.md)>`

**Value:**

{ \

.handler = (\_handler), \

.user\_data = (\_user\_data), \

.exec\_cnt = (\_exec\_cnt), \

.preempt\_cnt = (\_preempt\_cnt), \

.t = (\_t) \

}

Initialize context structure.

For argument types see [ztress\_context\_data](structztress__context__data.md "ztress_context_data"). For more details see [ZTRESS\_THREAD](#gaed561641541e8ced6866f2f1227f21c0).

Parameters
:   | \_handler | Handler. |
    | --- | --- |
    | \_user\_data | User data passed to the handler. |
    | \_exec\_cnt | Execution count limit. |
    | \_preempt\_cnt | Preemption count limit. |
    | \_t | Initial timeout. |

## [◆ ](#ga6acc3a50e0eff7360873006482f5c8e9)ZTRESS\_EXECUTE

| #define ZTRESS\_EXECUTE | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztress.h](ztress_8h.md)>`

**Value:**

do { \

Z\_ZTRESS\_TIMER\_CONTEXT\_VALIDATE(\_\_VA\_ARGS\_\_); \

int has\_timer = Z\_ZTRESS\_HAS\_TIMER(\_\_VA\_ARGS\_\_); \

struct [ztress\_context\_data](structztress__context__data.md) \_ctx\_data1[] = { \

FOR\_EACH(Z\_ZTRESS\_GET\_HANDLER\_DATA, (,), \_\_VA\_ARGS\_\_) \

}; \

size\_t cnt = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_ctx\_data1) - has\_timer; \

static struct [ztress\_context\_data](structztress__context__data.md) \_ctx\_data[[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_ctx\_data1)]; \

for (size\_t i = 0; i < [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_ctx\_data1); i++) { \

\_ctx\_data[i] = \_ctx\_data1[i]; \

} \

int exec\_err = [ztress\_execute](#gaf706f1af4c42f5925d7545dadf5548fd)(has\_timer ? &\_ctx\_data[0] : [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), \

&\_ctx\_data[has\_timer], cnt); \

\

zassert\_equal(exec\_err, 0, "ztress\_execute failed (err: %d)", exec\_err); \

} while (0)

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:120

[ztress\_execute](#gaf706f1af4c42f5925d7545dadf5548fd)

int ztress\_execute(struct ztress\_context\_data \*timer\_data, struct ztress\_context\_data \*thread\_data, size\_t cnt)

Execute contexts.

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[ztress\_context\_data](structztress__context__data.md)

**Definition** ztress.h:100

Setup and run stress test.

It initialises all contexts and calls [ztress\_execute](#gaf706f1af4c42f5925d7545dadf5548fd).

Parameters
:   | ... | List of contexts. Contexts are configured using [ZTRESS\_TIMER](#gabab05b8db44a7024ce23cb34bf999e42) and [ZTRESS\_THREAD](#gaed561641541e8ced6866f2f1227f21c0) macros. [ZTRESS\_TIMER](#gabab05b8db44a7024ce23cb34bf999e42) must be the first argument if used. Each thread context has an assigned priority. The priority is assigned in a descending order (first listed thread context has the highest priority). The maximum number of supported thread contexts, including the timer context, is configurable in Kconfig (ZTRESS\_MAX\_THREADS). |
    | --- | --- |

## [◆ ](#gaed561641541e8ced6866f2f1227f21c0)ZTRESS\_THREAD

| #define ZTRESS\_THREAD | ( |  | *handler*, |
| --- | --- | --- | --- |
|  |  |  | *user\_data*, |
|  |  |  | *exec\_cnt*, |
|  |  |  | *preempt\_cnt*, |
|  |  |  | *init\_timeout* ) |

`#include <[ztress.h](ztress_8h.md)>`

**Value:**

([ZTRESS\_ID\_THREAD](ztress_8h.md#a8752d529cfc4d77b1dd71c4572fd63c3), handler, user\_data, exec\_cnt, preempt\_cnt, init\_timeout)

[ZTRESS\_ID\_THREAD](ztress_8h.md#a8752d529cfc4d77b1dd71c4572fd63c3)

#define ZTRESS\_ID\_THREAD

**Definition** ztress.h:24

Descriptor of a thread execution context.

The handler is executed in the thread context. The priority of the thread is determined based on the order in which contexts are listed in [ZTRESS\_EXECUTE](#ga6acc3a50e0eff7360873006482f5c8e9).

Note
:   thread sleeps for random amount of time. Additionally, the thread busy-waits for a random length of time to further increase randomization in the test.

Parameters
:   | handler | User handler of type [ztress\_handler](#ga633439263754bf08baee06c37dddab40). |
    | --- | --- |
    | user\_data | User data passed to the `handler`. |
    | exec\_cnt | Number of handler executions to complete the test. If 0 then this is not included in completion criteria. |
    | preempt\_cnt | Number of preemptions of that context to complete the test. If 0 then this is not included in completion criteria. |
    | init\_timeout | Initial backoff time base (given in [k\_timeout\_t](structk__timeout__t.md "k_timeout_t")). It is adjusted during the test to optimize CPU load. The actual timeout used for sleeping is randomized. |

## [◆ ](#gabab05b8db44a7024ce23cb34bf999e42)ZTRESS\_TIMER

| #define ZTRESS\_TIMER | ( |  | *handler*, |
| --- | --- | --- | --- |
|  |  |  | *user\_data*, |
|  |  |  | *exec\_cnt*, |
|  |  |  | *init\_timeout* ) |

`#include <[ztress.h](ztress_8h.md)>`

**Value:**

([ZTRESS\_ID\_K\_TIMER](ztress_8h.md#a937803e1398db7d0e10ea60c9c9ef642), handler, user\_data, exec\_cnt, 0, init\_timeout)

[ZTRESS\_ID\_K\_TIMER](ztress_8h.md#a937803e1398db7d0e10ea60c9c9ef642)

#define ZTRESS\_ID\_K\_TIMER

**Definition** ztress.h:25

Descriptor of a k\_timer handler execution context.

The handler is executed in the k\_timer handler context which typically means interrupt context. This context will preempt any other used in the set.

Note
:   There can only be up to one k\_timer context in the set and it must be the first argument of [ZTRESS\_EXECUTE](#ga6acc3a50e0eff7360873006482f5c8e9).

Parameters
:   | handler | User handler of type [ztress\_handler](#ga633439263754bf08baee06c37dddab40). |
    | --- | --- |
    | user\_data | User data passed to the `handler`. |
    | exec\_cnt | Number of handler executions to complete the test. If 0 then this is not included in completion criteria. |
    | init\_timeout | Initial backoff time base (given in [k\_timeout\_t](structk__timeout__t.md "k_timeout_t")). It is adjusted during the test to optimize CPU load. The actual timeout used for the timer is randomized. |

## Typedef Documentation

## [◆ ](#ga633439263754bf08baee06c37dddab40)ztress\_handler

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* ztress\_handler) (void \*user\_data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last, int prio) |
| --- |

`#include <[ztress.h](ztress_8h.md)>`

User handler called in one of the configured contexts.

Parameters
:   | user\_data | User data provided in the context descriptor. |
    | --- | --- |
    | cnt | Current execution counter. Counted from 0. |
    | last | Flag set to true indicates that it is the last execution because completion criteria are met, test timed out or was aborted. |
    | prio | Context priority counting from 0 which indicates the highest priority. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | continue test. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | stop executing the current context. |

## Function Documentation

## [◆ ](#ga57f171e230fba462b3dea6b2d3cf71f6)ztress\_abort()

| void ztress\_abort | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztress.h](ztress_8h.md)>`

Abort ongoing stress test.

## [◆ ](#ga99eeabcc672fc5ec0b83ce5b8fb4ec5b)ztress\_exec\_count()

| int ztress\_exec\_count | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztress.h](ztress_8h.md)>`

Get number of executions of a given context in the last test.

Parameters
:   | id | Context id. 0 means the highest priority. |
    | --- | --- |

Returns
:   Number of executions.

## [◆ ](#gaf706f1af4c42f5925d7545dadf5548fd)ztress\_execute()

| int ztress\_execute | ( | struct [ztress\_context\_data](structztress__context__data.md) \* | *timer\_data*, |
| --- | --- | --- | --- |
|  |  | struct [ztress\_context\_data](structztress__context__data.md) \* | *thread\_data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *cnt* ) |

`#include <[ztress.h](ztress_8h.md)>`

Execute contexts.

The test runs until all completion requirements are met or until the test times out (use [ztress\_set\_timeout](#ga5b3069bb2aa35ddc64c46c18d2e30091) to configure timeout) or until the test is aborted ([ztress\_abort](#ga57f171e230fba462b3dea6b2d3cf71f6)).

on test completion a report is printed ([ztress\_report](#gaf4db2092eee17d863c9810333ba4c870) is called internally).

Parameters
:   | timer\_data | Timer context. NULL if timer context is not used. |
    | --- | --- |
    | thread\_data | List of thread contexts descriptors in priority descending order. |
    | cnt | Number of thread contexts. |

Return values
:   | -EINVAL | If configuration is invalid. |
    | --- | --- |
    | 0 | if test is successfully performed. |

## [◆ ](#gacbbdb8e7bad532d6dd20c486b3256e21)ztress\_optimized\_ticks()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ztress\_optimized\_ticks | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztress.h](ztress_8h.md)>`

Get optimized timeout base of a given context in the last test.

Optimized value can be used to update initial value. It will improve the test since optimal CPU load will be reach immediately.

Parameters
:   | id | Context id. 0 means the highest priority. |
    | --- | --- |

Returns
:   Optimized timeout base.

## [◆ ](#ga4406b828d170bc19065aaf65aeb4613e)ztress\_preempt\_count()

| int ztress\_preempt\_count | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztress.h](ztress_8h.md)>`

Get number of preemptions of a given context in the last test.

Parameters
:   | id | Context id. 0 means the highest priority. |
    | --- | --- |

Returns
:   Number of preemptions.

## [◆ ](#gaf4db2092eee17d863c9810333ba4c870)ztress\_report()

| void ztress\_report | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztress.h](ztress_8h.md)>`

Print last test report.

Report contains number of executions and preemptions for each context, initial and adjusted timeouts and CPU load during the test.

## [◆ ](#ga5b3069bb2aa35ddc64c46c18d2e30091)ztress\_set\_timeout()

| void ztress\_set\_timeout | ( | [k\_timeout\_t](structk__timeout__t.md) | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztress.h](ztress_8h.md)>`

Set test timeout.

Test is terminated after timeout disregarding completion criteria. Setting is persistent between executions.

Parameters
:   | t | Timeout. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
