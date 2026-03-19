---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__heap__listener__apis.html
original_path: doxygen/html/group__heap__listener__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Heap Listener APIs

[Operating System Services](group__os__services.md) » [Heap Management](group__heaps.md)

| Data Structures | |
| --- | --- |
| struct | [heap\_listener](structheap__listener.md) |

| Macros | |
| --- | --- |
| #define | [HEAP\_ID\_FROM\_POINTER](#ga77e603053a5b69caae2a49e441a525c0)(heap\_pointer) |
|  | Construct heap identifier from heap pointer. |
| #define | [HEAP\_ID\_LIBC](#ga7627d1b500bb7e833770c99071f9255d)   (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))0) |
|  | Libc heap identifier. |
| #define | [HEAP\_LISTENER\_ALLOC\_DEFINE](#ga1854b23cbd41dec0d8262e8f122ebd5d)(name, \_heap\_id, \_alloc\_cb) |
|  | Define heap event listener node for allocation event. |
| #define | [HEAP\_LISTENER\_FREE\_DEFINE](#ga7e5822ebd4c08235b01cf99cd6fe10e8)(name, \_heap\_id, \_free\_cb) |
|  | Define heap event listener node for free event. |
| #define | [HEAP\_LISTENER\_RESIZE\_DEFINE](#gaa4fa9685749e050ca06e7cdc99b7c970)(name, \_heap\_id, \_resize\_cb) |
|  | Define heap event listener node for resize event. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [heap\_listener\_resize\_cb\_t](#gad8addd23bfb3f303c10c13024a8c29ce)) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*old\_heap\_end, void \*new\_heap\_end) |
|  | Callback used when heap is resized. |
| typedef void(\* | [heap\_listener\_alloc\_cb\_t](#ga325f3d6679f9bc6d6d1b2e98c8efd2f6)) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Callback used when there is heap allocation. |
| typedef void(\* | [heap\_listener\_free\_cb\_t](#ga8a2e3c13b898647618ba93cd592e406f)) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Callback used when memory is freed from heap. |

| Enumerations | |
| --- | --- |
| enum | [heap\_event\_types](#ga9679320e1c32dcbad726789946565510) {     [HEAP\_EVT\_UNKNOWN](#gga9679320e1c32dcbad726789946565510ae82b3e0225bde5553f472c5f00985b18) = 0 , [HEAP\_RESIZE](#gga9679320e1c32dcbad726789946565510a198aa2475e58078a46cf79ffb0914408) , [HEAP\_ALLOC](#gga9679320e1c32dcbad726789946565510a23ece0bd476a164e251ebd1af61f0008) , [HEAP\_FREE](#gga9679320e1c32dcbad726789946565510a82e2137ada931f068fa36d40245f5a80) ,     [HEAP\_REALLOC](#gga9679320e1c32dcbad726789946565510aa64f229b21eedbca9a581b60e3da5a50) , [HEAP\_MAX\_EVENTS](#gga9679320e1c32dcbad726789946565510afb3a6f56a29d74c35db90fbeaa61a3b6)   } |

| Functions | |
| --- | --- |
| void | [heap\_listener\_register](#ga63d5470d9ca312ccc80d35c7f8dea200) (struct [heap\_listener](structheap__listener.md) \*listener) |
|  | Register heap event listener. |
| void | [heap\_listener\_unregister](#ga872e123af0a5349e45fcedfd8b83b508) (struct [heap\_listener](structheap__listener.md) \*listener) |
|  | Unregister heap event listener. |
| void | [heap\_listener\_notify\_alloc](#gaebe49e01cba6d327c635da4795e37e22) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Notify listeners of heap allocation event. |
| void | [heap\_listener\_notify\_free](#ga8fd3dc5b65e3bc8bbc1dadaa741d47fc) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Notify listeners of heap free event. |
| void | [heap\_listener\_notify\_resize](#ga9d3062fbcdc10edc3839193e8ea79654) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*old\_heap\_end, void \*new\_heap\_end) |
|  | Notify listeners of heap resize event. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga77e603053a5b69caae2a49e441a525c0)HEAP\_ID\_FROM\_POINTER

| #define HEAP\_ID\_FROM\_POINTER | ( |  | *heap\_pointer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[heap_listener.h](heap__listener_8h.md)>`

**Value:**

(([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))heap\_pointer)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

Construct heap identifier from heap pointer.

Construct a heap identifier from a pointer to the heap object, such as [sys\_heap](structsys__heap.md).

Parameters
:   | heap\_pointer | Pointer to the heap object |
    | --- | --- |

## [◆ ](#ga7627d1b500bb7e833770c99071f9255d)HEAP\_ID\_LIBC

| #define HEAP\_ID\_LIBC   (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))0) |
| --- |

`#include <[heap_listener.h](heap__listener_8h.md)>`

Libc heap identifier.

Identifier of the global libc heap.

## [◆ ](#ga1854b23cbd41dec0d8262e8f122ebd5d)HEAP\_LISTENER\_ALLOC\_DEFINE

| #define HEAP\_LISTENER\_ALLOC\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *\_heap\_id*, |
|  |  |  | *\_alloc\_cb* ) |

`#include <[heap_listener.h](heap__listener_8h.md)>`

**Value:**

struct [heap\_listener](structheap__listener.md) name = { \

.heap\_id = \_heap\_id, \

.event = [HEAP\_ALLOC](#gga9679320e1c32dcbad726789946565510a23ece0bd476a164e251ebd1af61f0008), \

{ \

.alloc\_cb = \_alloc\_cb \

}, \

}

[HEAP\_ALLOC](#gga9679320e1c32dcbad726789946565510a23ece0bd476a164e251ebd1af61f0008)

@ HEAP\_ALLOC

**Definition** heap\_listener.h:34

[heap\_listener](structheap__listener.md)

**Definition** heap\_listener.h:93

Define heap event listener node for allocation event.

Sample usage:

void on\_heap\_alloc([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, size\_t bytes)

{

[LOG\_INF](group__log__api.md#ga9c338f3170acf38a8532d1181d26704e)("Memory allocated at %p, size %ld", mem, bytes);

}

[HEAP\_LISTENER\_ALLOC\_DEFINE](#ga1854b23cbd41dec0d8262e8f122ebd5d)(my\_listener, [HEAP\_ID\_LIBC](#ga7627d1b500bb7e833770c99071f9255d), on\_heap\_alloc);

[HEAP\_LISTENER\_ALLOC\_DEFINE](#ga1854b23cbd41dec0d8262e8f122ebd5d)

#define HEAP\_LISTENER\_ALLOC\_DEFINE(name, \_heap\_id, \_alloc\_cb)

Define heap event listener node for allocation event.

**Definition** heap\_listener.h:208

[HEAP\_ID\_LIBC](#ga7627d1b500bb7e833770c99071f9255d)

#define HEAP\_ID\_LIBC

Libc heap identifier.

**Definition** heap\_listener.h:189

[LOG\_INF](group__log__api.md#ga9c338f3170acf38a8532d1181d26704e)

#define LOG\_INF(...)

Writes an INFO level message to the log.

**Definition** log.h:65

Parameters
:   | name | Name of the heap event listener object |
    | --- | --- |
    | \_heap\_id | Identifier of the heap to be listened |
    | \_alloc\_cb | Function to be called for allocation event |

## [◆ ](#ga7e5822ebd4c08235b01cf99cd6fe10e8)HEAP\_LISTENER\_FREE\_DEFINE

| #define HEAP\_LISTENER\_FREE\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *\_heap\_id*, |
|  |  |  | *\_free\_cb* ) |

`#include <[heap_listener.h](heap__listener_8h.md)>`

**Value:**

struct [heap\_listener](structheap__listener.md) name = { \

.heap\_id = \_heap\_id, \

.event = [HEAP\_FREE](#gga9679320e1c32dcbad726789946565510a82e2137ada931f068fa36d40245f5a80), \

{ \

.free\_cb = \_free\_cb \

}, \

}

[HEAP\_FREE](#gga9679320e1c32dcbad726789946565510a82e2137ada931f068fa36d40245f5a80)

@ HEAP\_FREE

**Definition** heap\_listener.h:35

Define heap event listener node for free event.

Sample usage:

void on\_heap\_free([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, size\_t bytes)

{

[LOG\_INF](group__log__api.md#ga9c338f3170acf38a8532d1181d26704e)("Memory freed at %p, size %ld", mem, bytes);

}

[HEAP\_LISTENER\_FREE\_DEFINE](#ga7e5822ebd4c08235b01cf99cd6fe10e8)(my\_listener, [HEAP\_ID\_LIBC](#ga7627d1b500bb7e833770c99071f9255d), on\_heap\_free);

[HEAP\_LISTENER\_FREE\_DEFINE](#ga7e5822ebd4c08235b01cf99cd6fe10e8)

#define HEAP\_LISTENER\_FREE\_DEFINE(name, \_heap\_id, \_free\_cb)

Define heap event listener node for free event.

**Definition** heap\_listener.h:234

Parameters
:   | name | Name of the heap event listener object |
    | --- | --- |
    | \_heap\_id | Identifier of the heap to be listened |
    | \_free\_cb | Function to be called for free event |

## [◆ ](#gaa4fa9685749e050ca06e7cdc99b7c970)HEAP\_LISTENER\_RESIZE\_DEFINE

| #define HEAP\_LISTENER\_RESIZE\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *\_heap\_id*, |
|  |  |  | *\_resize\_cb* ) |

`#include <[heap_listener.h](heap__listener_8h.md)>`

**Value:**

struct [heap\_listener](structheap__listener.md) name = { \

.heap\_id = \_heap\_id, \

.event = [HEAP\_RESIZE](#gga9679320e1c32dcbad726789946565510a198aa2475e58078a46cf79ffb0914408), \

{ \

.resize\_cb = \_resize\_cb \

}, \

}

[HEAP\_RESIZE](#gga9679320e1c32dcbad726789946565510a198aa2475e58078a46cf79ffb0914408)

@ HEAP\_RESIZE

**Definition** heap\_listener.h:33

Define heap event listener node for resize event.

Sample usage:

void on\_heap\_resized([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*old\_heap\_end, void \*new\_heap\_end)

{

[LOG\_INF](group__log__api.md#ga9c338f3170acf38a8532d1181d26704e)("Libc heap end moved from %p to %p", old\_heap\_end, new\_heap\_end);

}

[HEAP\_LISTENER\_RESIZE\_DEFINE](#gaa4fa9685749e050ca06e7cdc99b7c970)(my\_listener, [HEAP\_ID\_LIBC](#ga7627d1b500bb7e833770c99071f9255d), on\_heap\_resized);

[HEAP\_LISTENER\_RESIZE\_DEFINE](#gaa4fa9685749e050ca06e7cdc99b7c970)

#define HEAP\_LISTENER\_RESIZE\_DEFINE(name, \_heap\_id, \_resize\_cb)

Define heap event listener node for resize event.

**Definition** heap\_listener.h:260

Parameters
:   | name | Name of the heap event listener object |
    | --- | --- |
    | \_heap\_id | Identifier of the heap to be listened |
    | \_resize\_cb | Function to be called when the listened heap is resized |

## Typedef Documentation

## [◆ ](#ga325f3d6679f9bc6d6d1b2e98c8efd2f6)heap\_listener\_alloc\_cb\_t

| typedef void(\* heap\_listener\_alloc\_cb\_t) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
| --- |

`#include <[heap_listener.h](heap__listener_8h.md)>`

Callback used when there is heap allocation.

Note
:   Heaps managed by libraries outside of code in Zephyr main code repository may not emit this event.
:   The number of bytes allocated may not match exactly to the request to the allocation function. Internal mechanism of the heap may allocate more than requested.

Parameters
:   | heap\_id | Heap identifier |
    | --- | --- |
    | mem | Pointer to the allocated memory |
    | bytes | Size of allocated memory |

## [◆ ](#ga8a2e3c13b898647618ba93cd592e406f)heap\_listener\_free\_cb\_t

| typedef void(\* heap\_listener\_free\_cb\_t) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
| --- |

`#include <[heap_listener.h](heap__listener_8h.md)>`

Callback used when memory is freed from heap.

Note
:   Heaps managed by libraries outside of code in Zephyr main code repository may not emit this event.
:   The number of bytes freed may not match exactly to the request to the allocation function. Internal mechanism of the heap dictates how memory is allocated or freed.

Parameters
:   | heap\_id | Heap identifier |
    | --- | --- |
    | mem | Pointer to the freed memory |
    | bytes | Size of freed memory |

## [◆ ](#gad8addd23bfb3f303c10c13024a8c29ce)heap\_listener\_resize\_cb\_t

| typedef void(\* heap\_listener\_resize\_cb\_t) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*old\_heap\_end, void \*new\_heap\_end) |
| --- |

`#include <[heap_listener.h](heap__listener_8h.md)>`

Callback used when heap is resized.

Note
:   Minimal C library does not emit this event.

Parameters
:   | heap\_id | Identifier of heap being resized |
    | --- | --- |
    | old\_heap\_end | Pointer to end of heap before resize |
    | new\_heap\_end | Pointer to end of heap after resize |

## Enumeration Type Documentation

## [◆ ](#ga9679320e1c32dcbad726789946565510)heap\_event\_types

| enum [heap\_event\_types](#ga9679320e1c32dcbad726789946565510) |
| --- |

`#include <[heap_listener.h](heap__listener_8h.md)>`

| Enumerator | |
| --- | --- |
| HEAP\_EVT\_UNKNOWN |  |
| HEAP\_RESIZE |  |
| HEAP\_ALLOC |  |
| HEAP\_FREE |  |
| HEAP\_REALLOC |  |
| HEAP\_MAX\_EVENTS |  |

## Function Documentation

## [◆ ](#gaebe49e01cba6d327c635da4795e37e22)heap\_listener\_notify\_alloc()

| void heap\_listener\_notify\_alloc | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *heap\_id*, |
| --- | --- | --- | --- |
|  |  | void \* | *mem*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[heap_listener.h](heap__listener_8h.md)>`

Notify listeners of heap allocation event.

Notify registered heap event listeners with matching heap identifier that an allocation has been done on heap

Parameters
:   | heap\_id | Heap identifier |
    | --- | --- |
    | mem | Pointer to the allocated memory |
    | bytes | Size of allocated memory |

## [◆ ](#ga8fd3dc5b65e3bc8bbc1dadaa741d47fc)heap\_listener\_notify\_free()

| void heap\_listener\_notify\_free | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *heap\_id*, |
| --- | --- | --- | --- |
|  |  | void \* | *mem*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes* ) |

`#include <[heap_listener.h](heap__listener_8h.md)>`

Notify listeners of heap free event.

Notify registered heap event listeners with matching heap identifier that memory is freed on heap

Parameters
:   | heap\_id | Heap identifier |
    | --- | --- |
    | mem | Pointer to the freed memory |
    | bytes | Size of freed memory |

## [◆ ](#ga9d3062fbcdc10edc3839193e8ea79654)heap\_listener\_notify\_resize()

| void heap\_listener\_notify\_resize | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *heap\_id*, |
| --- | --- | --- | --- |
|  |  | void \* | *old\_heap\_end*, |
|  |  | void \* | *new\_heap\_end* ) |

`#include <[heap_listener.h](heap__listener_8h.md)>`

Notify listeners of heap resize event.

Notify registered heap event listeners with matching heap identifier that the heap has been resized.

Parameters
:   | heap\_id | Heap identifier |
    | --- | --- |
    | old\_heap\_end | Address of the heap end before the change |
    | new\_heap\_end | Address of the heap end after the change |

## [◆ ](#ga63d5470d9ca312ccc80d35c7f8dea200)heap\_listener\_register()

| void heap\_listener\_register | ( | struct [heap\_listener](structheap__listener.md) \* | *listener* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[heap_listener.h](heap__listener_8h.md)>`

Register heap event listener.

Add the listener to the global list of heap listeners that can be notified by different heap implementations upon certain events related to the heap usage.

Parameters
:   | listener | Pointer to the [heap\_listener](structheap__listener.md) object |
    | --- | --- |

## [◆ ](#ga872e123af0a5349e45fcedfd8b83b508)heap\_listener\_unregister()

| void heap\_listener\_unregister | ( | struct [heap\_listener](structheap__listener.md) \* | *listener* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[heap_listener.h](heap__listener_8h.md)>`

Unregister heap event listener.

Remove the listener from the global list of heap listeners that can be notified by different heap implementations upon certain events related to the heap usage.

Parameters
:   | listener | Pointer to the [heap\_listener](structheap__listener.md) object |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
