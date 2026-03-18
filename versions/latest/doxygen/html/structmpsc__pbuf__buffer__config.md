---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structmpsc__pbuf__buffer__config.html
original_path: doxygen/html/structmpsc__pbuf__buffer__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc\_pbuf\_buffer\_config Struct Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [MPSC (Multi producer, single consumer) packet buffer API](group__mpsc__buf.md)

MPSC packet buffer configuration.
[More...](#details)

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [buf](#a2090b3da5dc85c68601fd7bdb54f6174) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [size](#aa321ccd5bcec6359ed329418c24e5260) |
| [mpsc\_pbuf\_notify\_drop](group__mpsc__buf.md#ga87f3795770880fb552316a8cac7b85ae) | [notify\_drop](#a2c0ed75bc95a03bb3a9ebfa55ca54227) |
| [mpsc\_pbuf\_get\_wlen](group__mpsc__buf.md#ga00b0a1839bc466c623928a29921d76b8) | [get\_wlen](#a43ea61f310a062f4460ab1b085276265) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a88c3049ff8d7942e834fed28ede234b1) |

## Detailed Description

MPSC packet buffer configuration.

## Field Documentation

## [◆ ](#a2090b3da5dc85c68601fd7bdb54f6174)buf

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* mpsc\_pbuf\_buffer\_config::buf |
| --- |

## [◆ ](#a88c3049ff8d7942e834fed28ede234b1)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_buffer\_config::flags |
| --- |

## [◆ ](#a43ea61f310a062f4460ab1b085276265)get\_wlen

| [mpsc\_pbuf\_get\_wlen](group__mpsc__buf.md#ga00b0a1839bc466c623928a29921d76b8) mpsc\_pbuf\_buffer\_config::get\_wlen |
| --- |

## [◆ ](#a2c0ed75bc95a03bb3a9ebfa55ca54227)notify\_drop

| [mpsc\_pbuf\_notify\_drop](group__mpsc__buf.md#ga87f3795770880fb552316a8cac7b85ae) mpsc\_pbuf\_buffer\_config::notify\_drop |
| --- |

## [◆ ](#aa321ccd5bcec6359ed329418c24e5260)size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mpsc\_pbuf\_buffer\_config::size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[mpsc\_pbuf.h](mpsc__pbuf_8h_source.md)

- [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
