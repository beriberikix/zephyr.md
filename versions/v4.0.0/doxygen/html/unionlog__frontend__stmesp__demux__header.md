---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/unionlog__frontend__stmesp__demux__header.html
original_path: doxygen/html/unionlog__frontend__stmesp__demux__header.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp\_demux\_header Union Reference

[Trace and Debug Domain APIs](group__log__frontend__stmesp__apis.md) » [Logging frontend STMESP Demultiplexer API](group__log__frontend__stpesp__demux__apis.md)

Union for writing raw data to the logging message header.
[More...](#details)

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [log\_frontend\_stmesp\_demux\_log\_header](structlog__frontend__stmesp__demux__log__header.md) | [log](#ae94bab609a4f5c51eef7886db712420d) |
|  | Log header structure. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [raw](#ae868e8f2e8b0623781d3f9377490c72a) |
|  | Raw word. |

## Detailed Description

Union for writing raw data to the logging message header.

## Field Documentation

## [◆ ](#ae94bab609a4f5c51eef7886db712420d)log

| struct [log\_frontend\_stmesp\_demux\_log\_header](structlog__frontend__stmesp__demux__log__header.md) log\_frontend\_stmesp\_demux\_header::log |
| --- |

Log header structure.

## [◆ ](#ae868e8f2e8b0623781d3f9377490c72a)raw

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_stmesp\_demux\_header::raw |
| --- |

Raw word.

---

The documentation for this union was generated from the following file:

- zephyr/logging/[log\_frontend\_stmesp\_demux.h](log__frontend__stmesp__demux_8h_source.md)

- [log\_frontend\_stmesp\_demux\_header](unionlog__frontend__stmesp__demux__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
