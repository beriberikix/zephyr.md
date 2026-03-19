---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi3c__ibi__work.html
original_path: doxygen/html/structi3c__ibi__work.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ibi\_work Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C In-Band Interrupts](group__i3c__ibi.md)

Node about a queued IBI.
[More...](#details)

`#include <[ibi.h](ibi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a66ece8f194350c94f8991eaf1ee5bc0b) |
| struct [k\_work](structk__work.md) | [work](#a4a0373423ababe549d00ee13fe657315) |
|  | [k\_work](structk__work.md "A structure used to submit work.") struct. |
| enum [i3c\_ibi\_type](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b) | [type](#a3ec8e089facfbb187342e9bf9a525e50) |
|  | IBI type. |
| union { |  |
| const struct [device](structdevice.md) \*   [controller](#a195e49bd7db79d0f1f45803e42e963ca) |  |
|  | Use for. [More...](#a195e49bd7db79d0f1f45803e42e963ca) |
| struct [i3c\_device\_desc](structi3c__device__desc.md) \*   [target](#a6c75e0b678fee04f3357c2c1aa9e7376) |  |
|  | Use for. [More...](#a6c75e0b678fee04f3357c2c1aa9e7376) |
| }; |  |
| union { |  |
| struct [i3c\_ibi\_payload](structi3c__ibi__payload.md)   [payload](#a08531106055235eaf85cb8fae690235c) |  |
|  | IBI payload. [More...](#a08531106055235eaf85cb8fae690235c) |
| [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda)   [work\_cb](#a6a3dfd49762d96b591b5e248f9ce1668) |  |
|  | Generic workqueue callback when type is I3C\_IBI\_WORKQUEUE\_CB. [More...](#a6a3dfd49762d96b591b5e248f9ce1668) |
| }; |  |

## Detailed Description

Node about a queued IBI.

## Field Documentation

## [◆ ](#a984ca59a1102dcec0f4ecb15283c4263)[union]

| union { ... } [i3c\_ibi\_work](structi3c__ibi__work.md) |
| --- |

## [◆ ](#a40639251a0ebf1447daa3a7e5b925936)[union]

| union { ... } [i3c\_ibi\_work](structi3c__ibi__work.md) |
| --- |

## [◆ ](#a195e49bd7db79d0f1f45803e42e963ca)controller

| const struct [device](structdevice.md)\* i3c\_ibi\_work::controller |
| --- |

Use for.

See also
:   [I3C\_IBI\_HOTJOIN](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f "Hot Join Request.").

## [◆ ](#a66ece8f194350c94f8991eaf1ee5bc0b)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) i3c\_ibi\_work::node |
| --- |

## [◆ ](#a08531106055235eaf85cb8fae690235c)payload

| struct [i3c\_ibi\_payload](structi3c__ibi__payload.md) i3c\_ibi\_work::payload |
| --- |

IBI payload.

## [◆ ](#a6c75e0b678fee04f3357c2c1aa9e7376)target

| struct [i3c\_device\_desc](structi3c__device__desc.md)\* i3c\_ibi\_work::target |
| --- |

Use for.

See also
:   [I3C\_IBI\_TARGET\_INTR](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba368e8ad08a003ebf197add6d73ffd43d "Target interrupt."), and
:   [I3C\_IBI\_CONTROLLER\_ROLE\_REQUEST](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba00235d326559f945d54638b0c0558815 "Controller Role Request.").

## [◆ ](#a3ec8e089facfbb187342e9bf9a525e50)type

| enum [i3c\_ibi\_type](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b) i3c\_ibi\_work::type |
| --- |

IBI type.

## [◆ ](#a4a0373423ababe549d00ee13fe657315)work

| struct [k\_work](structk__work.md) i3c\_ibi\_work::work |
| --- |

[k\_work](structk__work.md "A structure used to submit work.") struct.

## [◆ ](#a6a3dfd49762d96b591b5e248f9ce1668)work\_cb

| [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) i3c\_ibi\_work::work\_cb |
| --- |

Generic workqueue callback when type is I3C\_IBI\_WORKQUEUE\_CB.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ibi.h](ibi_8h_source.md)

- [i3c\_ibi\_work](structi3c__ibi__work.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
