---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__spsc__lockfree.html
original_path: doxygen/html/group__spsc__lockfree.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SPSC API

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Single Producer Single Consumer (SPSC) Lockfree Queue API.
[More...](#details)

| Files | |
| --- | --- |
| file | [spsc\_lockfree.h](spsc__lockfree_8h.md) |
|  | A lock-free and type safe power of 2 fixed sized single producer single consumer (SPSC) queue using a ringbuffer and atomics to ensure coherency. |

| Macros | |
| --- | --- |
| #define | [SPSC\_INITIALIZER](#ga18aecd57468b7e6b3779c86952647238)(sz, buf) |
|  | Statically initialize an spsc. |
| #define | [SPSC\_DECLARE](#gaef8a80e3a9bc0d30e1e3b29ff7b6ba85)(name, type) |
|  | Declare an anonymous struct type for an spsc. |
| #define | [SPSC\_DEFINE](#ga8d1ccd780f9e0656fffc59ffc828fd1f)(name, type, sz) |
|  | Define an spsc with a fixed size. |
| #define | [spsc\_size](#ga4b191cf95a0fdae8a197037ab252a58c)(spsc) |
|  | Size of the SPSC queue. |
| #define | [spsc\_reset](#gaca6733f19cd9d05ff27176d3ef813490)(spsc) |
|  | Initialize/reset a spsc such that its empty. |
| #define | [spsc\_acquire](#gaa9e6c12ab0d83759b1387be9d299462d)(spsc) |
|  | Acquire an element to produce from the SPSC. |
| #define | [spsc\_produce](#ga8f3308d2e1ef28d29f9eabd46ed90bde)(spsc) |
|  | Produce one previously acquired element to the SPSC. |
| #define | [spsc\_produce\_all](#ga971fea8aa902ccaac6a3ac787046d0cd)(spsc) |
|  | Produce all previously acquired elements to the SPSC. |
| #define | [spsc\_drop\_all](#ga30f61cd259725e8a06b920517d23df01)(spsc) |
|  | Drop all previously acquired elements. |
| #define | [spsc\_consume](#gacca4ce3da7128ecadb861b47bd55bf9b)(spsc) |
|  | Consume an element from the spsc. |
| #define | [spsc\_release](#ga4d20e781b0f811a08334375664d74726)(spsc) |
|  | Release a consumed element. |
| #define | [spsc\_release\_all](#ga624be14173fbb26c8b09e50e9e0d46a2)(spsc) |
|  | Release all consumed elements. |
| #define | [spsc\_acquirable](#ga2bed9808d75ed0617e4442fd6d69244c)(spsc) |
|  | Count of acquirable in spsc. |
| #define | [spsc\_consumable](#gae2b68434c49078b1a55930b4a99aacdf)(spsc) |
|  | Count of consumables in spsc. |
| #define | [spsc\_peek](#gac382c3a75dbc1df5d6d40df8c7d54266)(spsc) |
|  | Peek at the first available item in queue. |
| #define | [spsc\_next](#gaba7acaae1e0a8a9b82b73ed15acf89a9)(spsc, item) |
|  | Peek at the next item in the queue from a given one. |
| #define | [spsc\_prev](#gabdcbd5a0dc5ea88811967494361c0bfc)(spsc, item) |
|  | Get the previous item in the queue from a given one. |

## Detailed Description

Single Producer Single Consumer (SPSC) Lockfree Queue API.

## Macro Definition Documentation

## [◆ ](#ga2bed9808d75ed0617e4442fd6d69244c)spsc\_acquirable

| #define spsc\_acquirable | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

({ (((spsc)->\_spsc.in + (spsc)->\_spsc.acquire) - (spsc)->\_spsc.out) - [spsc\_size](#ga4b191cf95a0fdae8a197037ab252a58c)(spsc); })

[spsc\_size](#ga4b191cf95a0fdae8a197037ab252a58c)

#define spsc\_size(spsc)

Size of the SPSC queue.

**Definition** spsc\_lockfree.h:124

Count of acquirable in spsc.

Parameters
:   | spsc | SPSC to get item count for |
    | --- | --- |

## [◆ ](#gaa9e6c12ab0d83759b1387be9d299462d)spsc\_acquire

| #define spsc\_acquire | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

({ \

unsigned long idx = z\_spsc\_in(spsc) + (spsc)->\_spsc.acquire; \

bool spsc\_acq = (idx - z\_spsc\_out(spsc)) < [spsc\_size](#ga4b191cf95a0fdae8a197037ab252a58c)(spsc); \

if (spsc\_acq) { \

(spsc)->\_spsc.acquire += 1; \

} \

spsc\_acq ? &((spsc)->buffer[z\_spsc\_mask(spsc, idx)]) : NULL; \

})

Acquire an element to produce from the SPSC.

Parameters
:   | spsc | SPSC to acquire an element from for producing |
    | --- | --- |

Returns
:   A pointer to the acquired element or null if the spsc is full

## [◆ ](#gae2b68434c49078b1a55930b4a99aacdf)spsc\_consumable

| #define spsc\_consumable | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

({ (spsc)->\_spsc.in - (spsc)->\_spsc.out - (spsc)->\_spsc.consume; })

Count of consumables in spsc.

Parameters
:   | spsc | SPSC to get item count for |
    | --- | --- |

## [◆ ](#gacca4ce3da7128ecadb861b47bd55bf9b)spsc\_consume

| #define spsc\_consume | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

({ \

unsigned long idx = z\_spsc\_out(spsc) + (spsc)->\_spsc.consume; \

bool has\_consumable = (idx != z\_spsc\_in(spsc)); \

if (has\_consumable) { \

(spsc)->\_spsc.consume += 1; \

} \

has\_consumable ? &((spsc)->buffer[z\_spsc\_mask(spsc, idx)]) : NULL; \

})

Consume an element from the spsc.

Parameters
:   | spsc | Spsc to consume from |
    | --- | --- |

Returns
:   Pointer to element or null if no consumable elements left

## [◆ ](#gaef8a80e3a9bc0d30e1e3b29ff7b6ba85)SPSC\_DECLARE

| #define SPSC\_DECLARE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *type* ) |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

static struct spsc\_##name { \

struct spsc \_spsc; \

type \* const buffer; \

}

Declare an anonymous struct type for an spsc.

Parameters
:   | name | Name of the spsc symbol to be provided |
    | --- | --- |
    | type | Type stored in the spsc |

## [◆ ](#ga8d1ccd780f9e0656fffc59ffc828fd1f)SPSC\_DEFINE

| #define SPSC\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *type*, |
|  |  |  | *sz* ) |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

BUILD\_ASSERT([IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)(sz)); \

static type \_\_spsc\_buf\_##name[sz]; \

SPSC\_DECLARE(name, type) name = [SPSC\_INITIALIZER](#ga18aecd57468b7e6b3779c86952647238)(sz, \_\_spsc\_buf\_##name);

[SPSC\_INITIALIZER](#ga18aecd57468b7e6b3779c86952647238)

#define SPSC\_INITIALIZER(sz, buf)

Statically initialize an spsc.

**Definition** spsc\_lockfree.h:82

[IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)

#define IS\_POWER\_OF\_TWO(x)

Check if a x is a power of two.

**Definition** util\_macro.h:77

Define an spsc with a fixed size.

Parameters
:   | name | Name of the spsc symbol to be provided |
    | --- | --- |
    | type | Type stored in the spsc |
    | sz | Size of the spsc, must be power of 2 (ex: 2, 4, 8) |

## [◆ ](#ga30f61cd259725e8a06b920517d23df01)spsc\_drop\_all

| #define spsc\_drop\_all | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

do { \

(spsc)->\_spsc.acquire = 0; \

} while (false)

Drop all previously acquired elements.

This makes all previous acquired elements available to be acquired again

Parameters
:   | spsc | SPSC to drop all previously acquired elements or do nothing |
    | --- | --- |

## [◆ ](#ga18aecd57468b7e6b3779c86952647238)SPSC\_INITIALIZER

| #define SPSC\_INITIALIZER | ( |  | *sz*, |
| --- | --- | --- | --- |
|  |  |  | *buf* ) |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

{ \

.\_spsc = \

{ \

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

Statically initialize an spsc.

Parameters
:   | sz | Size of the spsc, must be power of 2 (ex: 2, 4, 8) |
    | --- | --- |
    | buf | Buffer pointer |

## [◆ ](#gaba7acaae1e0a8a9b82b73ed15acf89a9)spsc\_next

| #define spsc\_next | ( |  | *spsc*, |
| --- | --- | --- | --- |
|  |  |  | *item* ) |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

({ \

unsigned long idx = ((item) - (spsc)->buffer); \

bool has\_next = \

z\_spsc\_mask(spsc, (idx + 1)) != (z\_spsc\_mask(spsc, z\_spsc\_in(spsc))); \

has\_next ? &((spsc)->buffer[z\_spsc\_mask((spsc), idx + 1)]) : NULL; \

})

Peek at the next item in the queue from a given one.

Parameters
:   | spsc | SPSC to peek at |
    | --- | --- |
    | item | Pointer to an item in the queue |

Returns
:   Pointer to element or null if none left

## [◆ ](#gac382c3a75dbc1df5d6d40df8c7d54266)spsc\_peek

| #define spsc\_peek | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

({ \

unsigned long idx = z\_spsc\_out(spsc) + (spsc)->\_spsc.consume; \

bool has\_consumable = (idx != z\_spsc\_in(spsc)); \

has\_consumable ? &((spsc)->buffer[z\_spsc\_mask(spsc, idx)]) : NULL; \

})

Peek at the first available item in queue.

Parameters
:   | spsc | Spsc to peek into |
    | --- | --- |

Returns
:   Pointer to element or null if no consumable elements left

## [◆ ](#gabdcbd5a0dc5ea88811967494361c0bfc)spsc\_prev

| #define spsc\_prev | ( |  | *spsc*, |
| --- | --- | --- | --- |
|  |  |  | *item* ) |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

({ \

unsigned long idx = ((item) - &(spsc)->buffer[0]) / sizeof((spsc)->buffer[0]); \

bool has\_prev = idx != z\_spsc\_mask(spsc, z\_spsc\_out(spsc)); \

has\_prev ? &((spsc)->buffer[z\_spsc\_mask(spsc, idx - 1)]) : NULL; \

})

Get the previous item in the queue from a given one.

Parameters
:   | spsc | SPSC to peek at |
    | --- | --- |
    | item | Pointer to an item in the queue |

Returns
:   Pointer to element or null if none left

## [◆ ](#ga8f3308d2e1ef28d29f9eabd46ed90bde)spsc\_produce

| #define spsc\_produce | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

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

## [◆ ](#ga971fea8aa902ccaac6a3ac787046d0cd)spsc\_produce\_all

| #define spsc\_produce\_all | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

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

## [◆ ](#ga4d20e781b0f811a08334375664d74726)spsc\_release

| #define spsc\_release | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

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

## [◆ ](#ga624be14173fbb26c8b09e50e9e0d46a2)spsc\_release\_all

| #define spsc\_release\_all | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

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

## [◆ ](#gaca6733f19cd9d05ff27176d3ef813490)spsc\_reset

| #define spsc\_reset | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

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

## [◆ ](#ga4b191cf95a0fdae8a197037ab252a58c)spsc\_size

| #define spsc\_size | ( |  | *spsc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_lockfree.h](spsc__lockfree_8h.md)>`

**Value:**

((spsc)->\_spsc.mask + 1)

Size of the SPSC queue.

Parameters
:   | spsc | SPSC reference |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
