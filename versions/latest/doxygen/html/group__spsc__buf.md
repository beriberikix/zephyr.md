---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__spsc__buf.html
original_path: doxygen/html/group__spsc__buf.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SPSC (Single producer, single consumer) packet buffer API

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Single producer, single consumer packet buffer API.
[More...](#details)

| Topics | |
| --- | --- |
|  | [SPSC packet buffer flags](group__SPSC__PBUF__FLAGS.md) |

| Data Structures | |
| --- | --- |
| struct | [spsc\_pbuf\_common](structspsc__pbuf__common.md) |
|  | First part of packet buffer control block. [More...](structspsc__pbuf__common.md#details) |
| struct | [spsc\_pbuf\_ext\_cache](structspsc__pbuf__ext__cache.md) |
|  | Remaining part of a packet buffer when cache is used. [More...](structspsc__pbuf__ext__cache.md#details) |
| struct | [spsc\_pbuf\_ext\_nocache](structspsc__pbuf__ext__nocache.md) |
|  | Remaining part of a packet buffer when cache is not used. [More...](structspsc__pbuf__ext__nocache.md#details) |
| struct | [spsc\_pbuf](structspsc__pbuf.md) |
|  | Single producer, single consumer packet buffer. [More...](structspsc__pbuf.md#details) |

| Macros | |
| --- | --- |
| #define | [CONFIG\_SPSC\_PBUF\_REMOTE\_DCACHE\_LINE](#ga01f1a8120df7afe197f5ed9d1c667370)   0 |
| #define | [SPSC\_PBUF\_MAX\_LEN](#gaec777dd30be52c1773dcf9e9ec1f6f9d)   0xFF00 |
|  | Maximum packet length. |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [spsc\_pbuf\_capacity](#ga02955c21404d71ac3ceeb9aa82cb18af) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb) |
|  | Get buffer capacity. |
| struct [spsc\_pbuf](structspsc__pbuf.md) \* | [spsc\_pbuf\_init](#ga6db38d6a0200a2468db02815cfe3bb6e) (void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) blen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Initialize the packet buffer. |
| int | [spsc\_pbuf\_write](#ga492c895f1723567445ce23c73ed3d0ef) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, const char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Write specified amount of data to the packet buffer. |
| int | [spsc\_pbuf\_alloc](#ga44485fd6756810f56c6bf7d41b3b447c) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, char \*\*buf) |
|  | Allocate space in the packet buffer. |
| void | [spsc\_pbuf\_commit](#ga664da6f26fd99e7f1ce76828273408a0) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Commit packet to the buffer. |
| int | [spsc\_pbuf\_read](#ga24d4cc2a41fd2c42c6085e106bf71c0c) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Read specified amount of data from the packet buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [spsc\_pbuf\_claim](#ga6727d38e40a780f9116d5d7b1c0ae8c4) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, char \*\*buf) |
|  | Claim packet from the buffer. |
| void | [spsc\_pbuf\_free](#ga28ea4f10fcab4d04f9e831f2057822ca) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Free the packet to the buffer. |
| int | [spsc\_pbuf\_get\_utilization](#gae3f455db53147709d40a7a86406a9311) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb) |
|  | Get maximum utilization of the packet buffer. |

## Detailed Description

Single producer, single consumer packet buffer API.

## Macro Definition Documentation

## [◆ ](#ga01f1a8120df7afe197f5ed9d1c667370)CONFIG\_SPSC\_PBUF\_REMOTE\_DCACHE\_LINE

| #define CONFIG\_SPSC\_PBUF\_REMOTE\_DCACHE\_LINE   0 |
| --- |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

## [◆ ](#gaec777dd30be52c1773dcf9e9ec1f6f9d)SPSC\_PBUF\_MAX\_LEN

| #define SPSC\_PBUF\_MAX\_LEN   0xFF00 |
| --- |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Maximum packet length.

## Function Documentation

## [◆ ](#ga44485fd6756810f56c6bf7d41b3b447c)spsc\_pbuf\_alloc()

| int spsc\_pbuf\_alloc | ( | struct [spsc\_pbuf](structspsc__pbuf.md) \* | *pb*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | char \*\* | *buf* ) |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Allocate space in the packet buffer.

This function attempts to allocate `len` bytes of continuous memory within the packet buffer. An internal padding is added at the end of the buffer, if wrapping occurred during allocation. Apart from padding, allocation does not change the state of the buffer so if after allocation packet is not needed a commit is not needed.

Allocated buffer must be committed ([spsc\_pbuf\_commit](#ga664da6f26fd99e7f1ce76828273408a0)) to make the packet available for reading.

Packet buffer ensures that allocated buffers are 32 bit word aligned.

Note
:   If data cache is used, it is the user responsibility to write back the new data.

Parameters
:   | [in] | pb | A buffer to which to write. |
    | --- | --- | --- |
    | [in] | len | Allocation length. Must be positive. If less than [SPSC\_PBUF\_MAX\_LEN](#gaec777dd30be52c1773dcf9e9ec1f6f9d) then if requested length cannot be allocated, an attempt to allocate largest possible is performed (which may include adding wrap padding). If [SPSC\_PBUF\_MAX\_LEN](#gaec777dd30be52c1773dcf9e9ec1f6f9d) is used then an attempt to allocate largest buffer without applying wrap padding is performed. |
    | [out] | buf | Location where buffer address is written on successful allocation. |

Return values
:   | non-negative | Amount of space that got allocated. Can be equal or smaller than p len. |
    | --- | --- |
    | -EINVAL | if `len` is forbidden. |

## [◆ ](#ga02955c21404d71ac3ceeb9aa82cb18af)spsc\_pbuf\_capacity()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spsc\_pbuf\_capacity | ( | struct [spsc\_pbuf](structspsc__pbuf.md) \* | *pb* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Get buffer capacity.

This value is the amount of data that is dedicated for storing packets. Since each packet is prefixed with 2 byte length header, longest possible packet is less than that.

Parameters
:   | pb | A buffer. |
    | --- | --- |

Returns
:   Packet buffer capacity.

## [◆ ](#ga6727d38e40a780f9116d5d7b1c0ae8c4)spsc\_pbuf\_claim()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) spsc\_pbuf\_claim | ( | struct [spsc\_pbuf](structspsc__pbuf.md) \* | *pb*, |
| --- | --- | --- | --- |
|  |  | char \*\* | *buf* ) |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Claim packet from the buffer.

It claims a single packet from the buffer in the order of the commitment by the [spsc\_pbuf\_commit](#ga664da6f26fd99e7f1ce76828273408a0) function. The first committed packet will be claimed first. The returned buffer is 32 bit word aligned and points to the continuous memory. Claimed packet must be freed using the [spsc\_pbuf\_free](#ga28ea4f10fcab4d04f9e831f2057822ca) function.

Note
:   If data cache is used, cache is invalidate on the packet.

Parameters
:   | [in] | pb | A buffer from which packet will be claimed. |
    | --- | --- | --- |
    | [in,out] | buf | A location where claimed packet address is written. It is 32 bit word aligned and points to the continuous memory. |

Return values
:   | 0 | No packets in the buffer. |
    | --- | --- |
    | positive | packet length. |

## [◆ ](#ga664da6f26fd99e7f1ce76828273408a0)spsc\_pbuf\_commit()

| void spsc\_pbuf\_commit | ( | struct [spsc\_pbuf](structspsc__pbuf.md) \* | *pb*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Commit packet to the buffer.

Commit a packet which was previously allocated ([spsc\_pbuf\_alloc](#ga44485fd6756810f56c6bf7d41b3b447c)). If cache is used, cache writeback is performed on the written data.

Parameters
:   | pb | A buffer to which to write. |
    | --- | --- |
    | len | Packet length. Must be equal or less than the length used for allocation. |

## [◆ ](#ga28ea4f10fcab4d04f9e831f2057822ca)spsc\_pbuf\_free()

| void spsc\_pbuf\_free | ( | struct [spsc\_pbuf](structspsc__pbuf.md) \* | *pb*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Free the packet to the buffer.

Packet must be claimed ([spsc\_pbuf\_claim](#ga6727d38e40a780f9116d5d7b1c0ae8c4)) before it can be freed.

Parameters
:   | pb | A packet buffer from which packet was claimed. |
    | --- | --- |
    | len | Claimed packet length. |

## [◆ ](#gae3f455db53147709d40a7a86406a9311)spsc\_pbuf\_get\_utilization()

| int spsc\_pbuf\_get\_utilization | ( | struct [spsc\_pbuf](structspsc__pbuf.md) \* | *pb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Get maximum utilization of the packet buffer.

Function can be used to tune the buffer size. Feature is enabled by CONFIG\_SPSC\_PBUF\_UTILIZATION. Utilization is updated by the consumer.

Parameters
:   | pb | A packet buffer. |
    | --- | --- |

Return values
:   | -ENOTSUP | Feature not enabled. |
    | --- | --- |
    | non-negative | Maximum utilization. |

## [◆ ](#ga6db38d6a0200a2468db02815cfe3bb6e)spsc\_pbuf\_init()

| struct [spsc\_pbuf](structspsc__pbuf.md) \* spsc\_pbuf\_init | ( | void \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *blen*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Initialize the packet buffer.

This function initializes the packet buffer on top of a dedicated memory region.

Parameters
:   | buf | Pointer to a memory region on which buffer is created. When cache is used it must be aligned to Z\_SPSC\_PBUF\_DCACHE\_LINE, otherwise it must be 32 bit word aligned. |
    | --- | --- |
    | blen | Length of the buffer. Must be large enough to contain the internal structure and at least two bytes of data (one is reserved for written messages length). |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Option flags. See [SPSC packet buffer flags](group__SPSC__PBUF__FLAGS.md "SPSC packet buffer flags"). |

Return values
:   | struct | spsc\_pbuf\* Pointer to the created buffer. The pointer points to the same address as buf. |
    | --- | --- |
    | NULL | Invalid buffer alignment. |

## [◆ ](#ga24d4cc2a41fd2c42c6085e106bf71c0c)spsc\_pbuf\_read()

| int spsc\_pbuf\_read | ( | struct [spsc\_pbuf](structspsc__pbuf.md) \* | *pb*, |
| --- | --- | --- | --- |
|  |  | char \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Read specified amount of data from the packet buffer.

Single read allows to read the message send by the single write. The provided p buf must be big enough to store the whole message.

It combines [spsc\_pbuf\_claim](#ga6727d38e40a780f9116d5d7b1c0ae8c4) and [spsc\_pbuf\_free](#ga28ea4f10fcab4d04f9e831f2057822ca) into a single call.

Parameters
:   | pb | A buffer from which data will be read. |
    | --- | --- |
    | buf | Data pointer to which read data will be written. If NULL, len of stored message is returned. |
    | len | Number of bytes to be read from the buffer. |

Return values
:   | int | Bytes read, negative error code on fail. Bytes to be read, if buf == NULL. -ENOMEM, if message can not fit in provided buf. -EAGAIN, if not whole message is ready yet. |
    | --- | --- |

## [◆ ](#ga492c895f1723567445ce23c73ed3d0ef)spsc\_pbuf\_write()

| int spsc\_pbuf\_write | ( | struct [spsc\_pbuf](structspsc__pbuf.md) \* | *pb*, |
| --- | --- | --- | --- |
|  |  | const char \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Write specified amount of data to the packet buffer.

It combines [spsc\_pbuf\_alloc](#ga44485fd6756810f56c6bf7d41b3b447c) and [spsc\_pbuf\_commit](#ga664da6f26fd99e7f1ce76828273408a0) into a single call.

Parameters
:   | pb | A buffer to which to write. |
    | --- | --- |
    | buf | Pointer to the data to be written to the buffer. |
    | len | Number of bytes to be written to the buffer. Must be positive but less than [SPSC\_PBUF\_MAX\_LEN](#gaec777dd30be52c1773dcf9e9ec1f6f9d). |

Return values
:   | int | Number of bytes written, negative error code on fail. -EINVAL, if len == 0. -ENOMEM, if len is bigger than the buffer can fit. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
