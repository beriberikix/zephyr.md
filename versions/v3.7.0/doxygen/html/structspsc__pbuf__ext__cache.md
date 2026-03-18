---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structspsc__pbuf__ext__cache.html
original_path: doxygen/html/structspsc__pbuf__ext__cache.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spsc\_pbuf\_ext\_cache Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [SPSC (Single producer, single consumer) packet buffer API](group__spsc__buf.md)

Remaining part of a packet buffer when cache is used.
[More...](#details)

`#include <[spsc_pbuf.h](spsc__pbuf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved](#af8da453c98a365ad7de52991487d681f) [[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(0, [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(0, [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(CPU, d\_cache\_line\_size, 0)) -(int) [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [spsc\_pbuf\_common](structspsc__pbuf__common.md)))] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [wr\_idx](#a513b3ec0f7e3c670c8ddd9a787ed500a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#acd6006164d2724afcc2b609d149f3aa1) [] |

## Detailed Description

Remaining part of a packet buffer when cache is used.

It contains data that is only changed by the writer. A gap is added to ensure that it is in different cache line than the data changed by the reader.

## Field Documentation

## [◆ ](#acd6006164d2724afcc2b609d149f3aa1)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) spsc\_pbuf\_ext\_cache::data[] |
| --- |

## [◆ ](#af8da453c98a365ad7de52991487d681f)reserved

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) spsc\_pbuf\_ext\_cache::reserved[[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(0, [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(0, [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(CPU, d\_cache\_line\_size, 0)) -(int) [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [spsc\_pbuf\_common](structspsc__pbuf__common.md)))] |
| --- |

## [◆ ](#a513b3ec0f7e3c670c8ddd9a787ed500a)wr\_idx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spsc\_pbuf\_ext\_cache::wr\_idx |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[spsc\_pbuf.h](spsc__pbuf_8h_source.md)

- [spsc\_pbuf\_ext\_cache](structspsc__pbuf__ext__cache.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
