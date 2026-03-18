---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpbuf.html
original_path: doxygen/html/structpbuf.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pbuf Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [Packed Buffer API](group__pbuf.md)

Scure packed buffer.
[More...](#details)

`#include <[pbuf.h](pbuf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [pbuf\_cfg](structpbuf__cfg.md) \*const | [cfg](#aa69c940d23b73b1292f5e8a6e1537494) |
| struct [pbuf\_data](structpbuf__data.md) | [data](#acbfdc9861d79dcd26bc73bfef5835e7e) |

## Detailed Description

Scure packed buffer.

The packet buffer implements lightweight unidirectional packet buffer with read/write semantics on top of a memory region shared by the reader and writer. It embeds cache and memory barrier management to ensure correct data access.

This structure supports single writer and reader. Data stored in the buffer is encapsulated to a message (with length header). The read/write API is written in a way to protect the data from being corrupted.

## Field Documentation

## [◆ ](#aa69c940d23b73b1292f5e8a6e1537494)cfg

| const struct [pbuf\_cfg](structpbuf__cfg.md)\* const pbuf::cfg |
| --- |

## [◆ ](#acbfdc9861d79dcd26bc73bfef5835e7e)data

| struct [pbuf\_data](structpbuf__data.md) pbuf::data |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[pbuf.h](pbuf_8h_source.md)

- [pbuf](structpbuf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
