---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structk__poll__event.html
original_path: doxygen/html/structk__poll__event.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_poll\_event Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Async polling APIs](group__poll__apis.md)

Poll Event.
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct z\_poller \* | [poller](#ad030c37b97f33e1bbb3361057180fa4f) |
|  | PRIVATE - DO NOT TOUCH. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tag](#a37c5f45deaa046b356d95af569220c70):8 |
|  | optional user-specified tag, opaque, untouched by the API |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [type](#a8f9e251aa8722eb4716f622e85be34ae):\_POLL\_NUM\_TYPES |
|  | bitfield of event types (bitwise-ORed K\_POLL\_TYPE\_xxx values) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [state](#aaf4f32852d799a406bfeea4e57891129):\_POLL\_NUM\_STATES |
|  | bitfield of event states (bitwise-ORed K\_POLL\_STATE\_xxx values) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mode](#acca81763486ef5ebcc911cb1cbd6c899):1 |
|  | mode of operation, from enum [k\_poll\_modes](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [unused](#a750ac48e7aa3c8fb70814b24e951fc85):(32 - (0 + 8 + \_POLL\_NUM\_TYPES + \_POLL\_NUM\_STATES + 1 )) |
|  | unused bits in 32-bit word |
| union { |  |
| void \*   [obj](#aeaf67f9bc91d59fb2939e1469a088f2d) |  |
| void \*   [typed\_K\_POLL\_TYPE\_IGNORE](#a0864cb03742d24d4638d5fbcb1166c5b) |  |
| struct [k\_poll\_signal](structk__poll__signal.md) \*   [signal](#a130aaff7a8908993ed6be737a94a52ab) |  |
| struct [k\_poll\_signal](structk__poll__signal.md) \*   [typed\_K\_POLL\_TYPE\_SIGNAL](#ad54cb4ae8d3603db02af37c833a73430) |  |
| struct k\_sem \*   [sem](#a9ed342b8a45884f985245f55b0e1c8cc) |  |
| struct k\_sem \*   [typed\_K\_POLL\_TYPE\_SEM\_AVAILABLE](#aaa57f5741e3e3a133cf8331cd68750f3) |  |
| struct [k\_fifo](structk__fifo.md) \*   [fifo](#a4ba07f42f4af03f30478ebf48a1653f7) |  |
| struct [k\_fifo](structk__fifo.md) \*   [typed\_K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE](#af578a9a6cd21412619d1482a17acb1ec) |  |
| struct [k\_queue](structk__queue.md) \*   [queue](#a6e30a6ce30702817895e66f22f0abedf) |  |
| struct [k\_queue](structk__queue.md) \*   [typed\_K\_POLL\_TYPE\_DATA\_AVAILABLE](#aa19a70be95e65636da3ebe6104a21dec) |  |
| struct [k\_msgq](structk__msgq.md) \*   [msgq](#a5bbe94482a70ec13c2106f89afd2d59c) |  |
| struct [k\_msgq](structk__msgq.md) \*   [typed\_K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE](#a038392f2f0fd314837005dc7fb57a714) |  |
| }; |  |
|  | per-type data |

## Detailed Description

Poll Event.

## Field Documentation

## [◆ ](#a9b3ecf7ad9ed6cb74b5364a321ec6233)[union]

| union { ... } [k\_poll\_event](structk__poll__event.md) |
| --- |

per-type data

## [◆ ](#a4ba07f42f4af03f30478ebf48a1653f7)fifo

| struct [k\_fifo](structk__fifo.md)\* k\_poll\_event::fifo |
| --- |

## [◆ ](#acca81763486ef5ebcc911cb1cbd6c899)mode

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_poll\_event::mode |
| --- |

mode of operation, from enum [k\_poll\_modes](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add)

## [◆ ](#a5bbe94482a70ec13c2106f89afd2d59c)msgq

| struct [k\_msgq](structk__msgq.md)\* k\_poll\_event::msgq |
| --- |

## [◆ ](#aeaf67f9bc91d59fb2939e1469a088f2d)obj

| void\* k\_poll\_event::obj |
| --- |

## [◆ ](#ad030c37b97f33e1bbb3361057180fa4f)poller

| struct z\_poller\* k\_poll\_event::poller |
| --- |

PRIVATE - DO NOT TOUCH.

## [◆ ](#a6e30a6ce30702817895e66f22f0abedf)queue

| struct [k\_queue](structk__queue.md)\* k\_poll\_event::queue |
| --- |

## [◆ ](#a9ed342b8a45884f985245f55b0e1c8cc)sem

| struct k\_sem\* k\_poll\_event::sem |
| --- |

## [◆ ](#a130aaff7a8908993ed6be737a94a52ab)signal

| struct [k\_poll\_signal](structk__poll__signal.md)\* k\_poll\_event::signal |
| --- |

## [◆ ](#aaf4f32852d799a406bfeea4e57891129)state

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_poll\_event::state |
| --- |

bitfield of event states (bitwise-ORed K\_POLL\_STATE\_xxx values)

## [◆ ](#a37c5f45deaa046b356d95af569220c70)tag

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_poll\_event::tag |
| --- |

optional user-specified tag, opaque, untouched by the API

## [◆ ](#a8f9e251aa8722eb4716f622e85be34ae)type

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_poll\_event::type |
| --- |

bitfield of event types (bitwise-ORed K\_POLL\_TYPE\_xxx values)

## [◆ ](#aa19a70be95e65636da3ebe6104a21dec)typed\_K\_POLL\_TYPE\_DATA\_AVAILABLE

| struct [k\_queue](structk__queue.md) \* k\_poll\_event::typed\_K\_POLL\_TYPE\_DATA\_AVAILABLE |
| --- |

## [◆ ](#af578a9a6cd21412619d1482a17acb1ec)typed\_K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE

| struct [k\_fifo](structk__fifo.md) \* k\_poll\_event::typed\_K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE |
| --- |

## [◆ ](#a0864cb03742d24d4638d5fbcb1166c5b)typed\_K\_POLL\_TYPE\_IGNORE

| void \* k\_poll\_event::typed\_K\_POLL\_TYPE\_IGNORE |
| --- |

## [◆ ](#a038392f2f0fd314837005dc7fb57a714)typed\_K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE

| struct [k\_msgq](structk__msgq.md) \* k\_poll\_event::typed\_K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE |
| --- |

## [◆ ](#aaa57f5741e3e3a133cf8331cd68750f3)typed\_K\_POLL\_TYPE\_SEM\_AVAILABLE

| struct k\_sem \* k\_poll\_event::typed\_K\_POLL\_TYPE\_SEM\_AVAILABLE |
| --- |

## [◆ ](#ad54cb4ae8d3603db02af37c833a73430)typed\_K\_POLL\_TYPE\_SIGNAL

| struct [k\_poll\_signal](structk__poll__signal.md) \* k\_poll\_event::typed\_K\_POLL\_TYPE\_SIGNAL |
| --- |

## [◆ ](#a750ac48e7aa3c8fb70814b24e951fc85)unused

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_poll\_event::unused |
| --- |

unused bits in 32-bit word

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_poll\_event](structk__poll__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
