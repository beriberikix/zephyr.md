---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__subsys__tracing__apis__heap.html
original_path: doxygen/html/group__subsys__tracing__apis__heap.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Heap Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Heap Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_heap\_init](#gaa9eb0a2ff9da8a892ab62e45fe4e4ddb)(h) |
|  | Trace initialization of Heap. |
| #define | [sys\_port\_trace\_k\_heap\_aligned\_alloc\_enter](#gaa49162a735def3b0389cc30bd4654533)(h, timeout) |
|  | Trace Heap aligned alloc attempt entry. |
| #define | [sys\_port\_trace\_k\_heap\_aligned\_alloc\_blocking](#gada1001c802bcc55437ffd8f4e2f23bef)(h, timeout) |
|  | Trace Heap align alloc attempt blocking. |
| #define | [sys\_port\_trace\_k\_heap\_aligned\_alloc\_exit](#ga3833f13065d967acafd50e3089556944)(h, timeout, ret) |
|  | Trace Heap align alloc attempt outcome. |
| #define | [sys\_port\_trace\_k\_heap\_alloc\_enter](#gadf8441b3c430499c8444a7c73bae1931)(h, timeout) |
|  | Trace Heap alloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_alloc\_exit](#gad696bba7ffe71beb01520ab27b483307)(h, timeout, ret) |
|  | Trace Heap alloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_free](#ga6f9c92a02d32af203752c59615e34096)(h) |
|  | Trace Heap free. |
| #define | [sys\_port\_trace\_k\_heap\_realloc\_enter](#ga5c7936b9c4f257e22638824c7ba6601e)(h, ptr, bytes, timeout) |
|  | Trace Heap realloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_realloc\_exit](#ga888b7ae4b7c29e4c2e877ca1c525d315)(h, ptr, bytes, timeout, ret) |
|  | Trace Heap realloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_enter](#ga12de856dc1fc2cb261497b3ef8b09e9e)(heap) |
|  | Trace System Heap aligned alloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_exit](#ga6d7a77c282f8229e0b366d57ba33ed04)(heap, ret) |
|  | Trace System Heap aligned alloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_enter](#ga478745a9e6cbc1a7b6bc9a2fc1763ca5)(heap) |
|  | Trace System Heap aligned alloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_exit](#ga4d612b7ec5d992c6e8170f35a1ce6c03)(heap, ret) |
|  | Trace System Heap aligned alloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_free\_enter](#gaf4dd86f13041c12cf18696fcff2ba9aa)(heap, heap\_ref) |
|  | Trace System Heap free entry. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_free\_exit](#gaf2865a12ffee2135e2d798bdf5fa9c98)(heap, heap\_ref) |
|  | Trace System Heap free exit. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_enter](#ga60e3dd5434ba9c912a4f2332f579318f)(heap) |
|  | Trace System heap calloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_exit](#ga6be2fe00eabc9bffaf635cfb14714e4a)(heap, ret) |
|  | Trace System heap calloc exit. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_realloc\_enter](#ga5c2e672b64f326b93aca9a4840ca5123)(heap, ptr) |
|  | Trace System heap realloc enter. |
| #define | [sys\_port\_trace\_k\_heap\_sys\_k\_realloc\_exit](#ga154dcc3e907ca4dbac41918cbb958e42)(heap, ptr, ret) |
|  | Trace System heap realloc exit. |

## Detailed Description

Heap Tracing APIs.

## Macro Definition Documentation

## [◆ ](#gada1001c802bcc55437ffd8f4e2f23bef)sys\_port\_trace\_k\_heap\_aligned\_alloc\_blocking

| #define sys\_port\_trace\_k\_heap\_aligned\_alloc\_blocking | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Heap align alloc attempt blocking.

Parameters
:   | h | Heap object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gaa49162a735def3b0389cc30bd4654533)sys\_port\_trace\_k\_heap\_aligned\_alloc\_enter

| #define sys\_port\_trace\_k\_heap\_aligned\_alloc\_enter | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Heap aligned alloc attempt entry.

Parameters
:   | h | Heap object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga3833f13065d967acafd50e3089556944)sys\_port\_trace\_k\_heap\_aligned\_alloc\_exit

| #define sys\_port\_trace\_k\_heap\_aligned\_alloc\_exit | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Heap align alloc attempt outcome.

Parameters
:   | h | Heap object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#gadf8441b3c430499c8444a7c73bae1931)sys\_port\_trace\_k\_heap\_alloc\_enter

| #define sys\_port\_trace\_k\_heap\_alloc\_enter | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Heap alloc enter.

Parameters
:   | h | Heap object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gad696bba7ffe71beb01520ab27b483307)sys\_port\_trace\_k\_heap\_alloc\_exit

| #define sys\_port\_trace\_k\_heap\_alloc\_exit | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Heap alloc exit.

Parameters
:   | h | Heap object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#ga6f9c92a02d32af203752c59615e34096)sys\_port\_trace\_k\_heap\_free

| #define sys\_port\_trace\_k\_heap\_free | ( |  | *h* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace Heap free.

Parameters
:   | h | Heap object |
    | --- | --- |

## [◆ ](#gaa9eb0a2ff9da8a892ab62e45fe4e4ddb)sys\_port\_trace\_k\_heap\_init

| #define sys\_port\_trace\_k\_heap\_init | ( |  | *h* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace initialization of Heap.

Parameters
:   | h | Heap object |
    | --- | --- |

## [◆ ](#ga5c7936b9c4f257e22638824c7ba6601e)sys\_port\_trace\_k\_heap\_realloc\_enter

| #define sys\_port\_trace\_k\_heap\_realloc\_enter | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *ptr*, |
|  |  |  | *bytes*, |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Heap realloc enter.

Parameters
:   | h | Heap object |
    | --- | --- |
    | ptr | Pointer to reallocate |
    | bytes | Bytes to reallocate |
    | timeout | Timeout period |

## [◆ ](#ga888b7ae4b7c29e4c2e877ca1c525d315)sys\_port\_trace\_k\_heap\_realloc\_exit

| #define sys\_port\_trace\_k\_heap\_realloc\_exit | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *ptr*, |
|  |  |  | *bytes*, |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace Heap realloc exit.

Parameters
:   | h | Heap object |
    | --- | --- |
    | ptr | Pointer to reallocate |
    | bytes | Bytes to reallocate |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#ga12de856dc1fc2cb261497b3ef8b09e9e)sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_enter

| #define sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_enter | ( |  | *heap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace System Heap aligned alloc enter.

Parameters
:   | heap | Heap object |
    | --- | --- |

## [◆ ](#ga6d7a77c282f8229e0b366d57ba33ed04)sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_exit

| #define sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_exit | ( |  | *heap*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace System Heap aligned alloc exit.

Parameters
:   | heap | Heap object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga60e3dd5434ba9c912a4f2332f579318f)sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_enter

| #define sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_enter | ( |  | *heap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace System heap calloc enter.

Parameters
:   | heap |  |
    | --- | --- |

## [◆ ](#ga6be2fe00eabc9bffaf635cfb14714e4a)sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_exit

| #define sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_exit | ( |  | *heap*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace System heap calloc exit.

Parameters
:   | heap | Heap object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaf4dd86f13041c12cf18696fcff2ba9aa)sys\_port\_trace\_k\_heap\_sys\_k\_free\_enter

| #define sys\_port\_trace\_k\_heap\_sys\_k\_free\_enter | ( |  | *heap*, |
| --- | --- | --- | --- |
|  |  |  | *heap\_ref* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace System Heap free entry.

Parameters
:   | heap | Heap object |
    | --- | --- |
    | heap\_ref | Heap reference |

## [◆ ](#gaf2865a12ffee2135e2d798bdf5fa9c98)sys\_port\_trace\_k\_heap\_sys\_k\_free\_exit

| #define sys\_port\_trace\_k\_heap\_sys\_k\_free\_exit | ( |  | *heap*, |
| --- | --- | --- | --- |
|  |  |  | *heap\_ref* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace System Heap free exit.

Parameters
:   | heap | Heap object |
    | --- | --- |
    | heap\_ref | Heap reference |

## [◆ ](#ga478745a9e6cbc1a7b6bc9a2fc1763ca5)sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_enter

| #define sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_enter | ( |  | *heap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace System Heap aligned alloc enter.

Parameters
:   | heap | Heap object |
    | --- | --- |

## [◆ ](#ga4d612b7ec5d992c6e8170f35a1ce6c03)sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_exit

| #define sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_exit | ( |  | *heap*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace System Heap aligned alloc exit.

Parameters
:   | heap | Heap object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga5c2e672b64f326b93aca9a4840ca5123)sys\_port\_trace\_k\_heap\_sys\_k\_realloc\_enter

| #define sys\_port\_trace\_k\_heap\_sys\_k\_realloc\_enter | ( |  | *heap*, |
| --- | --- | --- | --- |
|  |  |  | *ptr* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace System heap realloc enter.

Parameters
:   | heap |  |
    | --- | --- |
    | ptr |  |

## [◆ ](#ga154dcc3e907ca4dbac41918cbb958e42)sys\_port\_trace\_k\_heap\_sys\_k\_realloc\_exit

| #define sys\_port\_trace\_k\_heap\_sys\_k\_realloc\_exit | ( |  | *heap*, |
| --- | --- | --- | --- |
|  |  |  | *ptr*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace System heap realloc exit.

Parameters
:   | heap | Heap object |
    | --- | --- |
    | ptr | Memory pointer |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
