---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlog__frontend__stmesp__demux__log.html
original_path: doxygen/html/structlog__frontend__stmesp__demux__log.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp\_demux\_log Struct Reference

[Trace and Debug Domain APIs](group__log__frontend__stmesp__apis.md) » [Logging frontend STMESP Demultiplexer API](group__log__frontend__stpesp__demux__apis.md)

Packet with logging message.
[More...](#details)

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h_source.md)>`

| Data Fields | |
| --- | --- |
|  | [MPSC\_PBUF\_HDR](#ad25f0378c2c3ba3d153a58a843704033) |
|  | Data for MPSC packet handling. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [type](#adb1b61bdca3a97df2c8ba2b34fc2ebff): 2 |
|  | Type. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [content\_invalid](#a84cf9f64d96e87cfd2bb9d859fed3886): 1 |
|  | Flag indicating if packet is valid. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timestamp](#af2b9820efce6f58d655b08a306c8d8d1): 59 |
|  | Timestamp. |
| struct [log\_frontend\_stmesp\_demux\_log\_header](structlog__frontend__stmesp__demux__log__header.md) | [hdr](#aa5b7175e05dbdcc41d75c5412ce30b15) |
|  | Logging header. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [padding](#ab063e3ed4d81cbdb4ec417508c55bd13) |
|  | Padding so that data is 8 bytes aligned. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#ae8c62ffd8a11fbcebce29ed934f52597) [] |
|  | Content. |

## Detailed Description

Packet with logging message.

## Field Documentation

## [◆ ](#a84cf9f64d96e87cfd2bb9d859fed3886)content\_invalid

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_log::content\_invalid |
| --- |

Flag indicating if packet is valid.

## [◆ ](#ae8c62ffd8a11fbcebce29ed934f52597)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_frontend\_stmesp\_demux\_log::data[] |
| --- |

Content.

## [◆ ](#aa5b7175e05dbdcc41d75c5412ce30b15)hdr

| struct [log\_frontend\_stmesp\_demux\_log\_header](structlog__frontend__stmesp__demux__log__header.md) log\_frontend\_stmesp\_demux\_log::hdr |
| --- |

Logging header.

## [◆ ](#ad25f0378c2c3ba3d153a58a843704033)MPSC\_PBUF\_HDR

| log\_frontend\_stmesp\_demux\_log::MPSC\_PBUF\_HDR |
| --- |

Data for MPSC packet handling.

## [◆ ](#ab063e3ed4d81cbdb4ec417508c55bd13)padding

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_stmesp\_demux\_log::padding |
| --- |

Padding so that data is 8 bytes aligned.

## [◆ ](#af2b9820efce6f58d655b08a306c8d8d1)timestamp

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_log::timestamp |
| --- |

Timestamp.

## [◆ ](#adb1b61bdca3a97df2c8ba2b34fc2ebff)type

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_log::type |
| --- |

Type.

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_frontend\_stmesp\_demux.h](log__frontend__stmesp__demux_8h_source.md)

- [log\_frontend\_stmesp\_demux\_log](structlog__frontend__stmesp__demux__log.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
