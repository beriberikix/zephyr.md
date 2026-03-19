---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structlog__frontend__stmesp__demux__log__header.html
original_path: doxygen/html/structlog__frontend__stmesp__demux__log__header.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp\_demux\_log\_header Struct Reference

[Trace and Debug Domain APIs](group__log__frontend__stmesp__apis.md) » [Logging frontend STMESP Demultiplexer API](group__log__frontend__stpesp__demux__apis.md)

Logging message header.
[More...](#details)

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [major](#acec1720948196deb1f09ab1ea443ecb9): 3 |
|  | Major index. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [level](#a3b1474632ab446d8c9d590fb4bd8e420): 3 |
|  | Severity level. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [total\_len](#a138b653d76c50c0454210b7a1d7ec60b): 16 |
|  | Total length excluding this header. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [package\_len](#a0a378b7740a3def454bf34fe54927aa1): 10 |
|  | Hexdump data length. |

## Detailed Description

Logging message header.

## Field Documentation

## [◆ ](#a3b1474632ab446d8c9d590fb4bd8e420)level

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_stmesp\_demux\_log\_header::level |
| --- |

Severity level.

## [◆ ](#acec1720948196deb1f09ab1ea443ecb9)major

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_stmesp\_demux\_log\_header::major |
| --- |

Major index.

## [◆ ](#a0a378b7740a3def454bf34fe54927aa1)package\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_stmesp\_demux\_log\_header::package\_len |
| --- |

Hexdump data length.

## [◆ ](#a138b653d76c50c0454210b7a1d7ec60b)total\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_stmesp\_demux\_log\_header::total\_len |
| --- |

Total length excluding this header.

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_frontend\_stmesp\_demux.h](log__frontend__stmesp__demux_8h_source.md)

- [log\_frontend\_stmesp\_demux\_log\_header](structlog__frontend__stmesp__demux__log__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
