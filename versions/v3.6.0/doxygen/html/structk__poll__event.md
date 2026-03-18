---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structk__poll__event.html
original_path: doxygen/html/structk__poll__event.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_poll\_event Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Async polling APIs](group__poll__apis.md)

Poll Event.
[More...](#details)

`#include <[kernel.h](include_2zephyr_2kernel_8h_source.md)>`

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
| struct [k\_poll\_signal](structk__poll__signal.md) \*   [signal](#a130aaff7a8908993ed6be737a94a52ab) |  |
| struct k\_sem \*   [sem](#a9ed342b8a45884f985245f55b0e1c8cc) |  |
| struct [k\_fifo](structk__fifo.md) \*   [fifo](#a4ba07f42f4af03f30478ebf48a1653f7) |  |
| struct [k\_queue](structk__queue.md) \*   [queue](#a6e30a6ce30702817895e66f22f0abedf) |  |
| struct [k\_msgq](structk__msgq.md) \*   [msgq](#a5bbe94482a70ec13c2106f89afd2d59c) |  |
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

## [◆ ](#a750ac48e7aa3c8fb70814b24e951fc85)unused

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_poll\_event::unused |
| --- |

unused bits in 32-bit word

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](include_2zephyr_2kernel_8h_source.md)

- [k\_poll\_event](structk__poll__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
