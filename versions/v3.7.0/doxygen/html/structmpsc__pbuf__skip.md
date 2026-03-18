---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmpsc__pbuf__skip.html
original_path: doxygen/html/structmpsc__pbuf__skip.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc\_pbuf\_skip Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [MPSC (Multi producer, single consumer) packet buffer API](group__mpsc__buf.md) » [MPSC (Multi producer, single consumer) packet header](group__mpsc__packet.md)

Skip packet used internally by the packet buffer.
[More...](#details)

`#include <[mpsc_packet.h](mpsc__packet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [valid](#ae2de17f804dd76bbd6efaa30a53a83b6): 1 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [busy](#a71106c8d9ec492ef788973996c9cba15): 1 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#af28d9ee25b93377519f625edd14d4078): 32 - 2 |

## Detailed Description

Skip packet used internally by the packet buffer.

## Field Documentation

## [◆ ](#a71106c8d9ec492ef788973996c9cba15)busy

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_skip::busy |
| --- |

## [◆ ](#af28d9ee25b93377519f625edd14d4078)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_skip::len |
| --- |

## [◆ ](#ae2de17f804dd76bbd6efaa30a53a83b6)valid

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_skip::valid |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[mpsc\_packet.h](mpsc__packet_8h_source.md)

- [mpsc\_pbuf\_skip](structmpsc__pbuf__skip.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
