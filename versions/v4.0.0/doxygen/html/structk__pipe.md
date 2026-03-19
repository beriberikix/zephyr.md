---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structk__pipe.html
original_path: doxygen/html/structk__pipe.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_pipe Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Pipe APIs](group__pipe__apis.md)

Pipe Structure.
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \* | [buffer](#acb78995d6b7df28a5452f5d2e88b4dfb) |
|  | Pipe buffer: may be NULL. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#aca3472fb8d68f01af4e26b0b88736d64) |
|  | Buffer size. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bytes\_used](#a91bedad65285546734b8724811dc6eb8) |
|  | Number of bytes used in buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [read\_index](#ae40f81d9c1459fa42f179cbc728aadd0) |
|  | Where in buffer to read from. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [write\_index](#a8f46bd01da0e52e4ee918d9ebe6ad739) |
|  | Where in buffer to write. |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#aa2a367a9c8f0be89bcdf1bf6d3b0b875) |
|  | Synchronization lock. |
| struct { |  |
| \_wait\_q\_t   [readers](#a81ab4435d9ca7e5246164fc4fcd9ad59) |  |
|  | Reader wait queue. [More...](#a81ab4435d9ca7e5246164fc4fcd9ad59) |
| \_wait\_q\_t   [writers](#ac61ce23d990cf4cef44a1ecfc5047ccc) |  |
|  | Writer wait queue. [More...](#ac61ce23d990cf4cef44a1ecfc5047ccc) |
| } | [wait\_q](#a2b7ab1aceb3f380c4adfe740d57dbeed) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a2ed95fbe24ea20c4f292a66def1d4dde) |
|  | Wait queue. |

## Detailed Description

Pipe Structure.

## Field Documentation

## [◆ ](#acb78995d6b7df28a5452f5d2e88b4dfb)buffer

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char\* k\_pipe::buffer |
| --- |

Pipe buffer: may be NULL.

## [◆ ](#a91bedad65285546734b8724811dc6eb8)bytes\_used

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_pipe::bytes\_used |
| --- |

Number of bytes used in buffer.

## [◆ ](#a2ed95fbe24ea20c4f292a66def1d4dde)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) k\_pipe::flags |
| --- |

Wait queue.

Flags

## [◆ ](#aa2a367a9c8f0be89bcdf1bf6d3b0b875)lock

| struct [k\_spinlock](structk__spinlock.md) k\_pipe::lock |
| --- |

Synchronization lock.

## [◆ ](#ae40f81d9c1459fa42f179cbc728aadd0)read\_index

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_pipe::read\_index |
| --- |

Where in buffer to read from.

## [◆ ](#a81ab4435d9ca7e5246164fc4fcd9ad59)readers

| \_wait\_q\_t k\_pipe::readers |
| --- |

Reader wait queue.

## [◆ ](#aca3472fb8d68f01af4e26b0b88736d64)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_pipe::size |
| --- |

Buffer size.

## [◆ ](#a2b7ab1aceb3f380c4adfe740d57dbeed)[struct]

| struct { ... } k\_pipe::wait\_q |
| --- |

## [◆ ](#a8f46bd01da0e52e4ee918d9ebe6ad739)write\_index

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_pipe::write\_index |
| --- |

Where in buffer to write.

## [◆ ](#ac61ce23d990cf4cef44a1ecfc5047ccc)writers

| \_wait\_q\_t k\_pipe::writers |
| --- |

Writer wait queue.

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_pipe](structk__pipe.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
