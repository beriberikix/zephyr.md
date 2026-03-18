---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mpsc__packet.html
original_path: doxygen/html/group__mpsc__packet.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MPSC (Multi producer, single consumer) packet header

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [MPSC (Multi producer, single consumer) packet buffer API](group__mpsc__buf.md)

Multi producer, single consumer packet header.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mpsc\_pbuf\_hdr](structmpsc__pbuf__hdr.md) |
|  | Generic packet header. [More...](structmpsc__pbuf__hdr.md#details) |
| struct | [mpsc\_pbuf\_skip](structmpsc__pbuf__skip.md) |
|  | Skip packet used internally by the packet buffer. [More...](structmpsc__pbuf__skip.md#details) |
| union | [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) |
|  | Generic packet header. [More...](unionmpsc__pbuf__generic.md#details) |

| Macros | |
| --- | --- |
| #define | [MPSC\_PBUF\_HDR\_BITS](#gadb02a97032e41897ae6644a23d163849)   2 |
|  | Number of bits in the first word which are used by the buffer. |
| #define | [MPSC\_PBUF\_HDR](#ga643932633f40ecdcfb9120662221d828) |
|  | Header that must be added to the first word in each packet. |

## Detailed Description

Multi producer, single consumer packet header.

## Macro Definition Documentation

## [◆ ](#ga643932633f40ecdcfb9120662221d828)MPSC\_PBUF\_HDR

| #define MPSC\_PBUF\_HDR |
| --- |

`#include <[mpsc_packet.h](mpsc__packet_8h.md)>`

**Value:**

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) valid: 1; \

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) busy: 1

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Header that must be added to the first word in each packet.

This fields are controlled by the packet buffer and unless specified must not be used. Fields must be added at the top of the packet header structure.

## [◆ ](#gadb02a97032e41897ae6644a23d163849)MPSC\_PBUF\_HDR\_BITS

| #define MPSC\_PBUF\_HDR\_BITS   2 |
| --- |

`#include <[mpsc_packet.h](mpsc__packet_8h.md)>`

Number of bits in the first word which are used by the buffer.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
