---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmpsc__pbuf__buffer.html
original_path: doxygen/html/structmpsc__pbuf__buffer.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc\_pbuf\_buffer Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [MPSC (Multi producer, single consumer) packet buffer API](group__mpsc__buf.md)

MPSC packet buffer structure.
[More...](#details)

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tmp\_wr\_idx](#a55df06357be70a3b633213199d987e71) |
|  | Temporary write index. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [wr\_idx](#a3f292f281f08b97d10183f9248ee7c4d) |
|  | Write index. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tmp\_rd\_idx](#aeea63b40d7b24e4396fa228bcf2a171f) |
|  | Temporary read index. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rd\_idx](#af9340dd31ea8e37b4d609898b126497a) |
|  | Read index. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a10e9152b8c85be62eac0a3828e3b1e2a) |
|  | Flags. |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#a1a986b86547aa644747b9a79a982b780) |
|  | Lock. |
| [mpsc\_pbuf\_notify\_drop](group__mpsc__buf.md#ga87f3795770880fb552316a8cac7b85ae) | [notify\_drop](#acdebdb6e7175ea3f39f484885ff6bec2) |
|  | User callback called whenever packet is dropped. |
| [mpsc\_pbuf\_get\_wlen](group__mpsc__buf.md#ga00b0a1839bc466c623928a29921d76b8) | [get\_wlen](#ad87f240d978605258cb03d7d1e5e006f) |
|  | Callback for getting packet length. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [buf](#a2b5cb8a3c7f4d41cf587318ccf6b0a76) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [size](#a917ecd5a37f6c1560091a7a63c50fd2c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_usage](#adad43580b7a632877cf7b577585a495a) |
| struct k\_sem | [sem](#ae860724c0784ae560e7d03b1b6389fa0) |

## Detailed Description

MPSC packet buffer structure.

## Field Documentation

## [◆ ](#a2b5cb8a3c7f4d41cf587318ccf6b0a76)buf

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* mpsc\_pbuf\_buffer::buf |
| --- |

## [◆ ](#a10e9152b8c85be62eac0a3828e3b1e2a)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_buffer::flags |
| --- |

Flags.

## [◆ ](#ad87f240d978605258cb03d7d1e5e006f)get\_wlen

| [mpsc\_pbuf\_get\_wlen](group__mpsc__buf.md#ga00b0a1839bc466c623928a29921d76b8) mpsc\_pbuf\_buffer::get\_wlen |
| --- |

Callback for getting packet length.

## [◆ ](#a1a986b86547aa644747b9a79a982b780)lock

| struct [k\_spinlock](structk__spinlock.md) mpsc\_pbuf\_buffer::lock |
| --- |

Lock.

## [◆ ](#adad43580b7a632877cf7b577585a495a)max\_usage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_buffer::max\_usage |
| --- |

## [◆ ](#acdebdb6e7175ea3f39f484885ff6bec2)notify\_drop

| [mpsc\_pbuf\_notify\_drop](group__mpsc__buf.md#ga87f3795770880fb552316a8cac7b85ae) mpsc\_pbuf\_buffer::notify\_drop |
| --- |

User callback called whenever packet is dropped.

May be NULL if unneeded.

## [◆ ](#af9340dd31ea8e37b4d609898b126497a)rd\_idx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_buffer::rd\_idx |
| --- |

Read index.

## [◆ ](#ae860724c0784ae560e7d03b1b6389fa0)sem

| struct k\_sem mpsc\_pbuf\_buffer::sem |
| --- |

## [◆ ](#a917ecd5a37f6c1560091a7a63c50fd2c)size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_buffer::size |
| --- |

## [◆ ](#aeea63b40d7b24e4396fa228bcf2a171f)tmp\_rd\_idx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_buffer::tmp\_rd\_idx |
| --- |

Temporary read index.

## [◆ ](#a55df06357be70a3b633213199d987e71)tmp\_wr\_idx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_buffer::tmp\_wr\_idx |
| --- |

Temporary write index.

## [◆ ](#a3f292f281f08b97d10183f9248ee7c4d)wr\_idx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_buffer::wr\_idx |
| --- |

Write index.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[mpsc\_pbuf.h](mpsc__pbuf_8h_source.md)

- [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
