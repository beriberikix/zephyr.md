---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__rtio__spsc.html
original_path: doxygen/html/group__rtio__spsc.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

RTIO SPSC API

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

RTIO Single Producer Single Consumer (SPSC) Queue API.
[More...](#details)

| Files | |
| --- | --- |
| file | [rtio\_spsc.h](rtio__spsc_8h.md) |
|  | A lock-free and type safe power of 2 fixed sized single producer single consumer (SPSC) queue using a ringbuffer and atomics to ensure coherency. |

| Macros | |
| --- | --- |
| #define | [RTIO\_SPSC\_INITIALIZER](#ga54a199d7030fad8387acf057539f2854)(sz, buf) |
|  | Statically initialize an rtio\_spsc. |
| #define | [RTIO\_SPSC\_DECLARE](#ga6d1f8fb2f7caf60680e434557b1947ad)(name, type) |
|  | Declare an anonymous struct type for an rtio\_spsc. |
| #define | [RTIO\_SPSC\_DEFINE](#ga03de50debdf6a3acca9f02f4bc9b7ad9)(name, type, sz) |
|  | Define an rtio\_spsc with a fixed size. |
| #define | [rtio\_spsc\_size](#gad47e0fcf59138828b74b29f7c59c55c2)(spsc) |
|  | Size of the SPSC queue. |
| #define | [rtio\_spsc\_reset](#ga803ff0ddddc3ca3fc37b6e39e9b65746)(spsc) |
|  | Initialize/reset a spsc such that its empty. |
| #define | [rtio\_spsc\_acquire](#ga31521b366a5ab60852b799dfa8d1fca4)(spsc) |
|  | Acquire an element to produce from the SPSC. |
| #define | [rtio\_spsc\_produce](#gaf7ac949ed6a896b2cb39141109f43f2f)(spsc) |
|  | Produce one previously acquired element to the SPSC. |
| #define | [rtio\_spsc\_produce\_all](#ga9eb327619c7dc567d5a70d538db95f2c)(spsc) |
|  | Produce all previously acquired elements to the SPSC. |
| #define | [rtio\_spsc\_drop\_all](#ga4f2be93f9b094269db5a844a0038b582)(spsc) |
|  | Drop all previously acquired elements. |
| #define | [rtio\_spsc\_consume](#ga163a7a6eedff934a2bc7b093c0bc8de5)(spsc) |
|  | Consume an element from the spsc. |
| #define | [rtio\_spsc\_release](#gad6e8916b9bdd9dbd00fddacec39b8898)(spsc) |
|  | Release a consumed element. |
| #define | [rtio\_spsc\_release\_all](#ga3d0ab7e1a3e777c22c60e711350e9d4a)(spsc) |
|  | Release all consumed elements. |
| #define | [rtio\_spsc\_acquirable](#gaa214fb1ca3172d16ba6b6c07fb1d0053)(spsc) |
|  | Count of acquirable in spsc. |
| #define | [rtio\_spsc\_consumable](#ga69cdbead4d23d77d952490ab6045c046)(spsc) |
|  | Count of consumables in spsc. |
| #define | [rtio\_spsc\_peek](#ga614c7cc6abc2222735e2a9581b5b347f)(spsc) |
|  | Peek at the first available item in queue. |
| #define | [rtio\_spsc\_next](#ga91e8862b750c8bdad27b93023d484b68)(spsc, item) |
|  | Peek at the next item in the queue from a given one. |
| #define | [rtio\_spsc\_prev](#gaf02b036e6131ca3a320e085221e665b9)(spsc, item) |
|  | Get the previous item in the queue from a given one. |

## Detailed Description

RTIO Single Producer Single Consumer (SPSC) Queue API.

## Macro Definition Documentation

## [◆ ](#gaa214fb1ca3172d16ba6b6c07fb1d0053)rtio\_spsc\_acquirable

| #define rtio\_spsc\_acquirable | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

(((spsc)->\_spsc.in + (spsc)->\_spsc.acquire) - (spsc)->\_spsc.out) - \

[rtio\_spsc\_size](#gad47e0fcf59138828b74b29f7c59c55c2)(spsc); \

})

[rtio\_spsc\_size](#gad47e0fcf59138828b74b29f7c59c55c2)

#define rtio\_spsc\_size(spsc)

Size of the SPSC queue.

**Definition** rtio\_spsc.h:124

Count of acquirable in spsc.

Parameters
:   | spsc | SPSC to get item count for |
    | --- | --- |

## [◆ ](#ga31521b366a5ab60852b799dfa8d1fca4)rtio\_spsc\_acquire

| #define rtio\_spsc\_acquire | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

unsigned long idx = z\_rtio\_spsc\_in(spsc) + (spsc)->\_spsc.acquire; \

bool spsc\_acq = (idx - z\_rtio\_spsc\_out(spsc)) < [rtio\_spsc\_size](#gad47e0fcf59138828b74b29f7c59c55c2)(spsc); \

if (spsc\_acq) { \

(spsc)->\_spsc.acquire += 1; \

} \

spsc\_acq ? &((spsc)->buffer[z\_rtio\_spsc\_mask(spsc, idx)]) : NULL; \

})

Acquire an element to produce from the SPSC.

Parameters
:   | spsc | SPSC to acquire an element from for producing |
    | --- | --- |

Returns
:   A pointer to the acquired element or null if the spsc is full

## [◆ ](#ga69cdbead4d23d77d952490ab6045c046)rtio\_spsc\_consumable

| #define rtio\_spsc\_consumable | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ (spsc)->\_spsc.in - (spsc)->\_spsc.out - (spsc)->\_spsc.consume; })

Count of consumables in spsc.

Parameters
:   | spsc | SPSC to get item count for |
    | --- | --- |

## [◆ ](#ga163a7a6eedff934a2bc7b093c0bc8de5)rtio\_spsc\_consume

| #define rtio\_spsc\_consume | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

unsigned long idx = z\_rtio\_spsc\_out(spsc) + (spsc)->\_spsc.consume; \

bool has\_consumable = (idx != z\_rtio\_spsc\_in(spsc)); \

if (has\_consumable) { \

(spsc)->\_spsc.consume += 1; \

} \

has\_consumable ? &((spsc)->buffer[z\_rtio\_spsc\_mask(spsc, idx)]) : NULL; \

})

Consume an element from the spsc.

Parameters
:   | spsc | Spsc to consume from |
    | --- | --- |

Returns
:   Pointer to element or null if no consumable elements left

## [◆ ](#ga6d1f8fb2f7caf60680e434557b1947ad)RTIO\_SPSC\_DECLARE

| #define RTIO\_SPSC\_DECLARE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *type* ) |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

static struct rtio\_spsc\_##name { \

struct rtio\_spsc \_spsc; \

type \* const buffer; \

}

Declare an anonymous struct type for an rtio\_spsc.

Parameters
:   | name | Name of the spsc symbol to be provided |
    | --- | --- |
    | type | Type stored in the spsc |

## [◆ ](#ga03de50debdf6a3acca9f02f4bc9b7ad9)RTIO\_SPSC\_DEFINE

| #define RTIO\_SPSC\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *type*, |
|  |  |  | *sz* ) |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

BUILD\_ASSERT([IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)(sz)); \

static type \_\_spsc\_buf\_##name[sz]; \

RTIO\_SPSC\_DECLARE(name, type) name = [RTIO\_SPSC\_INITIALIZER](#ga54a199d7030fad8387acf057539f2854)(sz, \_\_spsc\_buf\_##name);

[RTIO\_SPSC\_INITIALIZER](#ga54a199d7030fad8387acf057539f2854)

#define RTIO\_SPSC\_INITIALIZER(sz, buf)

Statically initialize an rtio\_spsc.

**Definition** rtio\_spsc.h:83

[IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)

#define IS\_POWER\_OF\_TWO(x)

Check if a x is a power of two.

**Definition** util\_macro.h:77

Define an rtio\_spsc with a fixed size.

Parameters
:   | name | Name of the spsc symbol to be provided |
    | --- | --- |
    | type | Type stored in the spsc |
    | sz | Size of the spsc, must be power of 2 (ex: 2, 4, 8) |

## [◆ ](#ga4f2be93f9b094269db5a844a0038b582)rtio\_spsc\_drop\_all

| #define rtio\_spsc\_drop\_all | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

do { \

(spsc)->\_spsc.acquire = 0; \

} while (false)

Drop all previously acquired elements.

This makes all previous acquired elements available to be acquired again

Parameters
:   | spsc | SPSC to drop all previously acquired elements or do nothing |
    | --- | --- |

## [◆ ](#ga54a199d7030fad8387acf057539f2854)RTIO\_SPSC\_INITIALIZER

| #define RTIO\_SPSC\_INITIALIZER | ( |  | *sz*, |
| --- | --- | --- | --- |
|  |  |  | *buf* ) |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

{ \

.\_spsc = { \

.acquire = 0, \

.consume = 0, \

.in = [ATOMIC\_INIT](group__atomic__apis.md#gaadfbba86627ee7eeb07e04f712550f73)(0), \

.out = [ATOMIC\_INIT](group__atomic__apis.md#gaadfbba86627ee7eeb07e04f712550f73)(0), \

.mask = sz - 1, \

}, \

.buffer = buf, \

}

[ATOMIC\_INIT](group__atomic__apis.md#gaadfbba86627ee7eeb07e04f712550f73)

#define ATOMIC\_INIT(i)

Initialize an atomic variable.

**Definition** atomic.h:59

Statically initialize an rtio\_spsc.

Parameters
:   | sz | Size of the spsc, must be power of 2 (ex: 2, 4, 8) |
    | --- | --- |
    | buf | Buffer pointer |

## [◆ ](#ga91e8862b750c8bdad27b93023d484b68)rtio\_spsc\_next

| #define rtio\_spsc\_next | ( |  | *spsc*, |
| --- | --- | --- | --- |
|  |  |  | *item* ) |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

unsigned long idx = ((item) - (spsc)->buffer); \

bool has\_next = z\_rtio\_spsc\_mask(spsc, (idx + 1)) != \

(z\_rtio\_spsc\_mask(spsc, z\_rtio\_spsc\_in(spsc))); \

has\_next ? &((spsc)->buffer[z\_rtio\_spsc\_mask((spsc), idx + 1)]) : NULL; \

})

Peek at the next item in the queue from a given one.

Parameters
:   | spsc | SPSC to peek at |
    | --- | --- |
    | item | Pointer to an item in the queue |

Returns
:   Pointer to element or null if none left

## [◆ ](#ga614c7cc6abc2222735e2a9581b5b347f)rtio\_spsc\_peek

| #define rtio\_spsc\_peek | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

unsigned long idx = z\_rtio\_spsc\_out(spsc) + (spsc)->\_spsc.consume; \

bool has\_consumable = (idx != z\_rtio\_spsc\_in(spsc)); \

has\_consumable ? &((spsc)->buffer[z\_rtio\_spsc\_mask(spsc, idx)]) : NULL; \

})

Peek at the first available item in queue.

Parameters
:   | spsc | Spsc to peek into |
    | --- | --- |

Returns
:   Pointer to element or null if no consumable elements left

## [◆ ](#gaf02b036e6131ca3a320e085221e665b9)rtio\_spsc\_prev

| #define rtio\_spsc\_prev | ( |  | *spsc*, |
| --- | --- | --- | --- |
|  |  |  | *item* ) |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

unsigned long idx = ((item) - &(spsc)->buffer[0]) / sizeof((spsc)->buffer[0]); \

bool has\_prev = idx != z\_rtio\_spsc\_mask(spsc, z\_rtio\_spsc\_out(spsc)); \

has\_prev ? &((spsc)->buffer[z\_rtio\_spsc\_mask(spsc, idx - 1)]) : NULL; \

})

Get the previous item in the queue from a given one.

Parameters
:   | spsc | SPSC to peek at |
    | --- | --- |
    | item | Pointer to an item in the queue |

Returns
:   Pointer to element or null if none left

## [◆ ](#gaf7ac949ed6a896b2cb39141109f43f2f)rtio\_spsc\_produce

| #define rtio\_spsc\_produce | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

if ((spsc)->\_spsc.acquire > 0) { \

(spsc)->\_spsc.acquire -= 1; \

atomic\_add(&(spsc)->\_spsc.in, 1); \

} \

})

Produce one previously acquired element to the SPSC.

This makes one element available to the consumer immediately

Parameters
:   | spsc | SPSC to produce the previously acquired element or do nothing |
    | --- | --- |

## [◆ ](#ga9eb327619c7dc567d5a70d538db95f2c)rtio\_spsc\_produce\_all

| #define rtio\_spsc\_produce\_all | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

if ((spsc)->\_spsc.acquire > 0) { \

unsigned long acquired = (spsc)->\_spsc.acquire; \

(spsc)->\_spsc.acquire = 0; \

atomic\_add(&(spsc)->\_spsc.in, acquired); \

} \

})

Produce all previously acquired elements to the SPSC.

This makes all previous acquired elements available to the consumer immediately

Parameters
:   | spsc | SPSC to produce all previously acquired elements or do nothing |
    | --- | --- |

## [◆ ](#gad6e8916b9bdd9dbd00fddacec39b8898)rtio\_spsc\_release

| #define rtio\_spsc\_release | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

if ((spsc)->\_spsc.consume > 0) { \

(spsc)->\_spsc.consume -= 1; \

atomic\_add(&(spsc)->\_spsc.out, 1); \

} \

})

Release a consumed element.

Parameters
:   | spsc | SPSC to release consumed element or do nothing |
    | --- | --- |

## [◆ ](#ga3d0ab7e1a3e777c22c60e711350e9d4a)rtio\_spsc\_release\_all

| #define rtio\_spsc\_release\_all | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

if ((spsc)->\_spsc.consume > 0) { \

unsigned long consumed = (spsc)->\_spsc.consume; \

(spsc)->\_spsc.consume = 0; \

atomic\_add(&(spsc)->\_spsc.out, consumed); \

} \

})

Release all consumed elements.

Parameters
:   | spsc | SPSC to release consumed elements or do nothing |
    | --- | --- |

## [◆ ](#ga803ff0ddddc3ca3fc37b6e39e9b65746)rtio\_spsc\_reset

| #define rtio\_spsc\_reset | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

({ \

(spsc)->\_spsc.consume = 0; \

(spsc)->\_spsc.acquire = 0; \

atomic\_set(&(spsc)->\_spsc.in, 0); \

atomic\_set(&(spsc)->\_spsc.out, 0); \

})

Initialize/reset a spsc such that its empty.

Note that this is not safe to do while being used in a producer/consumer situation with multiple calling contexts (isrs/threads).

Parameters
:   | spsc | SPSC to initialize/reset |
    | --- | --- |

## [◆ ](#gad47e0fcf59138828b74b29f7c59c55c2)rtio\_spsc\_size

| #define rtio\_spsc\_size | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio_spsc.h](rtio__spsc_8h.md)>`

**Value:**

((spsc)->\_spsc.mask + 1)

Size of the SPSC queue.

Parameters
:   | spsc | SPSC reference |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
