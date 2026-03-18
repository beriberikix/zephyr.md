---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structpbuf__data.html
original_path: doxygen/html/structpbuf__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pbuf\_data Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [Packed Buffer API](group__pbuf.md)

Data block of the packed buffer.
[More...](#details)

`#include <[pbuf.h](pbuf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [wr\_idx](#ae5d497c293f1b84e7a8e801c5349a0b9) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rd\_idx](#aecb4e2462b1d308d43883b935e4648fe) |

## Detailed Description

Data block of the packed buffer.

The structure contains local copies of wr and rd indexes used by writer and reader respecitvely.

## Field Documentation

## [◆ ](#aecb4e2462b1d308d43883b935e4648fe)rd\_idx

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pbuf\_data::rd\_idx |
| --- |

## [◆ ](#ae5d497c293f1b84e7a8e801c5349a0b9)wr\_idx

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pbuf\_data::wr\_idx |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[pbuf.h](pbuf_8h_source.md)

- [pbuf\_data](structpbuf__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
