---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structspsc__pbuf.html
original_path: doxygen/html/structspsc__pbuf.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spsc\_pbuf Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [SPSC (Single producer, single consumer) packet buffer API](group__spsc__buf.md)

Single producer, single consumer packet buffer.
[More...](#details)

`#include <[spsc_pbuf.h](spsc__pbuf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [spsc\_pbuf\_common](structspsc__pbuf__common.md) | [common](#a0f2e4726ed93b9132b6429adf45a98cb) |
| union { |  |
| struct [spsc\_pbuf\_ext\_cache](structspsc__pbuf__ext__cache.md)   [cache](#adc8af418a006b9761ff28ceb76a3f1af) |  |
| struct [spsc\_pbuf\_ext\_nocache](structspsc__pbuf__ext__nocache.md)   [nocache](#a8e851fc5b99dbbba53522b1d3aa23c25) |  |
| } | [ext](#a1319cdcb211031b9bb79f8b9cb0a3765) |

## Detailed Description

Single producer, single consumer packet buffer.

The SPSC packet buffer implements lightweight unidirectional packet buffer with read/write semantics on top of a memory region shared by the reader and writer. It optionally embeds cache and memory barrier management to ensure correct data access.

This structure supports single writer and reader. Data stored in the buffer is encapsulated to a message (with length header).

## Field Documentation

## [◆ ](#adc8af418a006b9761ff28ceb76a3f1af)cache

| struct [spsc\_pbuf\_ext\_cache](structspsc__pbuf__ext__cache.md) spsc\_pbuf::cache |
| --- |

## [◆ ](#a0f2e4726ed93b9132b6429adf45a98cb)common

| struct [spsc\_pbuf\_common](structspsc__pbuf__common.md) spsc\_pbuf::common |
| --- |

## [◆ ](#a1319cdcb211031b9bb79f8b9cb0a3765)[union]

| union { ... } spsc\_pbuf::ext |
| --- |

## [◆ ](#a8e851fc5b99dbbba53522b1d3aa23c25)nocache

| struct [spsc\_pbuf\_ext\_nocache](structspsc__pbuf__ext__nocache.md) spsc\_pbuf::nocache |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[spsc\_pbuf.h](spsc__pbuf_8h_source.md)

- [spsc\_pbuf](structspsc__pbuf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
