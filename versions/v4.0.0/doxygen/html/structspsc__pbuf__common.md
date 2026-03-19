---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structspsc__pbuf__common.html
original_path: doxygen/html/structspsc__pbuf__common.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spsc\_pbuf\_common Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [SPSC (Single producer, single consumer) packet buffer API](group__spsc__buf.md)

First part of packet buffer control block.
[More...](#details)

`#include <[spsc_pbuf.h](spsc__pbuf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#a7e6a0859238d5abc92ce48cb8dafb89c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#aeeaddf75caa7d899120d9ff4bf39432c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rd\_idx](#af396b2cb886441c56ddd3c866bb6637a) |

## Detailed Description

First part of packet buffer control block.

This part contains only data set during the initialization and data touched by the reader. If packet is shared between to cores then data changed by the reader should be on different cache line than the data changed by the writer.

## Field Documentation

## [◆ ](#aeeaddf75caa7d899120d9ff4bf39432c)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spsc\_pbuf\_common::flags |
| --- |

## [◆ ](#a7e6a0859238d5abc92ce48cb8dafb89c)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spsc\_pbuf\_common::len |
| --- |

## [◆ ](#af396b2cb886441c56ddd3c866bb6637a)rd\_idx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spsc\_pbuf\_common::rd\_idx |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[spsc\_pbuf.h](spsc__pbuf_8h_source.md)

- [spsc\_pbuf\_common](structspsc__pbuf__common.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
