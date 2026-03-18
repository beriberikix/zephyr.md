---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__buf__pool.html
original_path: doxygen/html/structnet__buf__pool.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_buf\_pool Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Buffer Library](group__net__buf.md)

Network buffer pool representation.
[More...](#details)

`#include <[buf.h](net_2buf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_lifo](structk__lifo.md) | [free](#a97e5b2e51238e859f93882a8008ba305) |
|  | LIFO to place the buffer into when free. |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#ae92fc3f3f51be63ccdeee9614d21cc34) |
|  | To prevent concurrent access/modifications. |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [buf\_count](#a55b57f4f573c7e752c3ccf2f92f25626) |
|  | Number of buffers in pool. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [uninit\_count](#a3fdf83b4c0b5acefbb761da285791ad2) |
|  | Number of uninitialized buffers. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [user\_data\_size](#a4718ecec19d7e2ccaf04b6ff61120975) |
|  | Size of user data allocated to this pool. |
| void(\*const | [destroy](#a2a9141d7cd20cd98818a92dc5bc99f56) )(struct [net\_buf](structnet__buf.md) \*buf) |
|  | Optional destroy callback when buffer is freed. |
| const struct net\_buf\_data\_alloc \* | [alloc](#a617bd8f77e55481d97183da8c0c62cc5) |
|  | Data allocation handlers. |

## Detailed Description

Network buffer pool representation.

This struct is used to represent a pool of network buffers.

## Field Documentation

## [◆ ](#a617bd8f77e55481d97183da8c0c62cc5)alloc

| const struct net\_buf\_data\_alloc\* net\_buf\_pool::alloc |
| --- |

Data allocation handlers.

## [◆ ](#a55b57f4f573c7e752c3ccf2f92f25626)buf\_count

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_pool::buf\_count |
| --- |

Number of buffers in pool.

## [◆ ](#a2a9141d7cd20cd98818a92dc5bc99f56)destroy

| void(\*const net\_buf\_pool::destroy) (struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

Optional destroy callback when buffer is freed.

## [◆ ](#a97e5b2e51238e859f93882a8008ba305)free

| struct [k\_lifo](structk__lifo.md) net\_buf\_pool::free |
| --- |

LIFO to place the buffer into when free.

## [◆ ](#ae92fc3f3f51be63ccdeee9614d21cc34)lock

| struct [k\_spinlock](structk__spinlock.md) net\_buf\_pool::lock |
| --- |

To prevent concurrent access/modifications.

## [◆ ](#a3fdf83b4c0b5acefbb761da285791ad2)uninit\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_pool::uninit\_count |
| --- |

Number of uninitialized buffers.

## [◆ ](#a4718ecec19d7e2ccaf04b6ff61120975)user\_data\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf\_pool::user\_data\_size |
| --- |

Size of user data allocated to this pool.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[buf.h](net_2buf_8h_source.md)

- [net\_buf\_pool](structnet__buf__pool.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
