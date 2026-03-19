---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mpsc__buf.html
original_path: doxygen/html/group__mpsc__buf.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MPSC (Multi producer, single consumer) packet buffer API

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Multi producer, single consumer packet buffer API.
[More...](#details)

| Topics | |
| --- | --- |
|  | [MPSC (Multi producer, single consumer) packet header](group__mpsc__packet.md) |
|  | Multi producer, single consumer packet header. |
|  | [MPSC packet buffer flags](group__MPSC__PBUF__FLAGS.md) |

| Data Structures | |
| --- | --- |
| struct | [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) |
|  | MPSC packet buffer structure. [More...](structmpsc__pbuf__buffer.md#details) |
| struct | [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) |
|  | MPSC packet buffer configuration. [More...](structmpsc__pbuf__buffer__config.md#details) |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [mpsc\_pbuf\_get\_wlen](#ga00b0a1839bc466c623928a29921d76b8)) (const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet) |
|  | Callback prototype for getting length of a packet. |
| typedef void(\* | [mpsc\_pbuf\_notify\_drop](#ga87f3795770880fb552316a8cac7b85ae)) (const struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet) |
|  | Callback called when packet is dropped. |

| Functions | |
| --- | --- |
| void | [mpsc\_pbuf\_init](#ga5152b9ae9c0da98fde3f8b73afac52b8) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) \*config) |
|  | Initialize a packet buffer. |
| union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* | [mpsc\_pbuf\_alloc](#ga398dd24464a5da03e80a3fc7d728dddd) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wlen, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a packet. |
| void | [mpsc\_pbuf\_commit](#gaa537b9e73ca4fda26a92dc56b960270e) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet) |
|  | Commit a packet. |
| void | [mpsc\_pbuf\_put\_word](#gabc366638ec262c7ec41b320f0dcc6a87) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) word) |
|  | Put single word packet into a buffer. |
| void | [mpsc\_pbuf\_put\_word\_ext](#ga7f4df1864fad89ec9557b6f0e18c9589) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) word, const void \*data) |
|  | Put a packet consisting of a word and a pointer. |
| void | [mpsc\_pbuf\_put\_data](#ga7b52261bac98a7a0c6bae2a838f23316) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wlen) |
|  | Put a packet into a buffer. |
| const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* | [mpsc\_pbuf\_claim](#ga9642d07deca00bc25cea2ae253ec7d76) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer) |
|  | Claim the first pending packet. |
| void | [mpsc\_pbuf\_free](#ga54f8705fa262a6cda75f1feecde5e57e) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet) |
|  | Free a packet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [mpsc\_pbuf\_is\_pending](#ga2c8ac7f489fba611a2bca25bb2bbb5fb) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer) |
|  | Check if there are any message pending. |
| void | [mpsc\_pbuf\_get\_utilization](#ga73be0efc020500865cfa07c45494f4a5) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*now) |
|  | Get current memory utilization. |
| int | [mpsc\_pbuf\_get\_max\_utilization](#ga8ee7fd071effaca18797862d423279d7) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*max) |
|  | Get maximum memory utilization. |

## Detailed Description

Multi producer, single consumer packet buffer API.

## Typedef Documentation

## [◆ ](#ga00b0a1839bc466c623928a29921d76b8)mpsc\_pbuf\_get\_wlen

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* mpsc\_pbuf\_get\_wlen) (const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet) |
| --- |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Callback prototype for getting length of a packet.

Parameters
:   | packet | User packet. |
    | --- | --- |

Returns
:   Size of the packet in 32 bit words.

## [◆ ](#ga87f3795770880fb552316a8cac7b85ae)mpsc\_pbuf\_notify\_drop

| typedef void(\* mpsc\_pbuf\_notify\_drop) (const struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet) |
| --- |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Callback called when packet is dropped.

Parameters
:   | buffer | Packet buffer. |
    | --- | --- |
    | packet | Packet that is being dropped. |

## Function Documentation

## [◆ ](#ga398dd24464a5da03e80a3fc7d728dddd)mpsc\_pbuf\_alloc()

| union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* mpsc\_pbuf\_alloc | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *wlen*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Allocate a packet.

If a buffer is configured to overwrite mode then if there is no space to allocate a new buffer, oldest packets are dropped. Otherwise allocation fails and null pointer is returned.

Parameters
:   | buffer | Buffer. |
    | --- | --- |
    | wlen | Number of words to allocate. |
    | timeout | Timeout. If called from thread context it will pend for given timeout if packet cannot be allocated before dropping the oldest or returning null. |

Returns
:   Pointer to the allocated space or null if it cannot be allocated.

## [◆ ](#ga9642d07deca00bc25cea2ae253ec7d76)mpsc\_pbuf\_claim()

| const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* mpsc\_pbuf\_claim | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Claim the first pending packet.

Parameters
:   | buffer | Buffer. |
    | --- | --- |

Returns
:   Pointer to the claimed packet or null if none available.

## [◆ ](#gaa537b9e73ca4fda26a92dc56b960270e)mpsc\_pbuf\_commit()

| void mpsc\_pbuf\_commit | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* | *packet* ) |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Commit a packet.

Parameters
:   | buffer | Buffer. |
    | --- | --- |
    | packet | Pointer to a packet allocated by [mpsc\_pbuf\_alloc](#ga398dd24464a5da03e80a3fc7d728dddd). |

## [◆ ](#ga54f8705fa262a6cda75f1feecde5e57e)mpsc\_pbuf\_free()

| void mpsc\_pbuf\_free | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* | *packet* ) |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Free a packet.

Parameters
:   | buffer | Buffer. |
    | --- | --- |
    | packet | Packet. |

## [◆ ](#ga8ee7fd071effaca18797862d423279d7)mpsc\_pbuf\_get\_max\_utilization()

| int mpsc\_pbuf\_get\_max\_utilization | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *max* ) |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Get maximum memory utilization.

Parameters
:   | [in,out] | buffer | Buffer. |
    | --- | --- | --- |
    | [out] | max | Maximum buffer usage in bytes. |

retval 0 if utilization data collected successfully. retval -ENOTSUP if Collecting utilization data is not supported.

## [◆ ](#ga73be0efc020500865cfa07c45494f4a5)mpsc\_pbuf\_get\_utilization()

| void mpsc\_pbuf\_get\_utilization | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *now* ) |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Get current memory utilization.

Parameters
:   | [in,out] | buffer | Buffer. |
    | --- | --- | --- |
    | [out] | size | Buffer size in bytes. |
    | [out] | now | Current buffer usage in bytes. |

## [◆ ](#ga5152b9ae9c0da98fde3f8b73afac52b8)mpsc\_pbuf\_init()

| void mpsc\_pbuf\_init | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) \* | *config* ) |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Initialize a packet buffer.

Parameters
:   | buffer | Buffer. |
    | --- | --- |
    | config | Configuration. |

## [◆ ](#ga2c8ac7f489fba611a2bca25bb2bbb5fb)mpsc\_pbuf\_is\_pending()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mpsc\_pbuf\_is\_pending | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Check if there are any message pending.

Parameters
:   | buffer | Buffer. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if pending. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if no message is pending. |

## [◆ ](#ga7b52261bac98a7a0c6bae2a838f23316)mpsc\_pbuf\_put\_data()

| void mpsc\_pbuf\_put\_data | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *wlen* ) |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Put a packet into a buffer.

Copy data into a buffer. Note that 2 bits of a first word is used by the buffer.

Parameters
:   | buffer | Buffer. |
    | --- | --- |
    | data | First word of data must contain MPSC\_PBUF\_HDR with valid bit set. |
    | wlen | Packet size in words. |

## [◆ ](#gabc366638ec262c7ec41b320f0dcc6a87)mpsc\_pbuf\_put\_word()

| void mpsc\_pbuf\_put\_word | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) | *word* ) |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Put single word packet into a buffer.

Function is optimized for storing a packet which fit into a single word. Note that 2 bits of that word is used by the buffer.

Parameters
:   | buffer | Buffer. |
    | --- | --- |
    | word | Packet content consisting of MPSC\_PBUF\_HDR with valid bit set and data on remaining bits. |

## [◆ ](#ga7f4df1864fad89ec9557b6f0e18c9589)mpsc\_pbuf\_put\_word\_ext()

| void mpsc\_pbuf\_put\_word\_ext | ( | struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) | *word*, |
|  |  | const void \* | *data* ) |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Put a packet consisting of a word and a pointer.

- Function is optimized for storing packet consisting of a word and a pointer. Note that 2 bits of a first word is used by the buffer.

Parameters
:   | buffer | Buffer. |
    | --- | --- |
    | word | First word of a packet consisting of MPSC\_PBUF\_HDR with valid bit set and data on remaining bits. |
    | data | User data. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
