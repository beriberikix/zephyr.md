---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structspsc__pbuf__ext__nocache.html
original_path: doxygen/html/structspsc__pbuf__ext__nocache.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spsc\_pbuf\_ext\_nocache Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [SPSC (Single producer, single consumer) packet buffer API](group__spsc__buf.md)

Remaining part of a packet buffer when cache is not used.
[More...](#details)

`#include <[spsc_pbuf.h](spsc__pbuf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [wr\_idx](#af287a5f0150ed97536427b73ea8a46b8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a3e0722d5d153bc3fc9af25ac64a539c5) [] |

## Detailed Description

Remaining part of a packet buffer when cache is not used.

## Field Documentation

## [◆ ](#a3e0722d5d153bc3fc9af25ac64a539c5)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) spsc\_pbuf\_ext\_nocache::data[] |
| --- |

## [◆ ](#af287a5f0150ed97536427b73ea8a46b8)wr\_idx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spsc\_pbuf\_ext\_nocache::wr\_idx |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[spsc\_pbuf.h](spsc__pbuf_8h_source.md)

- [spsc\_pbuf\_ext\_nocache](structspsc__pbuf__ext__nocache.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
