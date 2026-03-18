---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmpsc__pbuf__hdr.html
original_path: doxygen/html/structmpsc__pbuf__hdr.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc\_pbuf\_hdr Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [MPSC (Multi producer, single consumer) packet buffer API](group__mpsc__buf.md) » [MPSC (Multi producer, single consumer) packet header](group__mpsc__packet.md)

Generic packet header.
[More...](#details)

`#include <[mpsc_packet.h](mpsc__packet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [valid](#a246f604d40160841142d9307ca35575a): 1 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [busy](#a83666ac11d7c4271186b67966c3729b4): 1 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [data](#a7a19c1ed5035b095160e946fd989e1c6): 32 - 2 |

## Detailed Description

Generic packet header.

## Field Documentation

## [◆ ](#a83666ac11d7c4271186b67966c3729b4)busy

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_hdr::busy |
| --- |

## [◆ ](#a7a19c1ed5035b095160e946fd989e1c6)data

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_hdr::data |
| --- |

## [◆ ](#a246f604d40160841142d9307ca35575a)valid

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_hdr::valid |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[mpsc\_packet.h](mpsc__packet_8h_source.md)

- [mpsc\_pbuf\_hdr](structmpsc__pbuf__hdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
