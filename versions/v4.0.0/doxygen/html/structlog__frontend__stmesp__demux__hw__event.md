---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlog__frontend__stmesp__demux__hw__event.html
original_path: doxygen/html/structlog__frontend__stmesp__demux__hw__event.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp\_demux\_hw\_event Struct Reference

[Trace and Debug Domain APIs](group__log__frontend__stmesp__apis.md) » [Logging frontend STMESP Demultiplexer API](group__log__frontend__stpesp__demux__apis.md)

Packet with HW event.
[More...](#details)

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h_source.md)>`

| Data Fields | |
| --- | --- |
|  | [MPSC\_PBUF\_HDR](#a6a060e7fbda81c47eaa8088f3e45052a) |
|  | Data for MPSC packet handling. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [type](#a5a781f1b681ef2499bf9ba2635261d4f): 2 |
|  | Type. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [content\_invalid](#ae6872dcd7e11eeb431e3d990ccdad243): 1 |
|  | Flag indicating if packet is valid. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timestamp](#a0766f3aa6163ea1a197d674eac00305b): 59 |
|  | Timestamp. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [evt](#a090039b38d646812a292510476d16644) |
|  | HW event ID. |

## Detailed Description

Packet with HW event.

## Field Documentation

## [◆ ](#ae6872dcd7e11eeb431e3d990ccdad243)content\_invalid

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_hw\_event::content\_invalid |
| --- |

Flag indicating if packet is valid.

## [◆ ](#a090039b38d646812a292510476d16644)evt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_frontend\_stmesp\_demux\_hw\_event::evt |
| --- |

HW event ID.

## [◆ ](#a6a060e7fbda81c47eaa8088f3e45052a)MPSC\_PBUF\_HDR

| log\_frontend\_stmesp\_demux\_hw\_event::MPSC\_PBUF\_HDR |
| --- |

Data for MPSC packet handling.

## [◆ ](#a0766f3aa6163ea1a197d674eac00305b)timestamp

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_hw\_event::timestamp |
| --- |

Timestamp.

## [◆ ](#a5a781f1b681ef2499bf9ba2635261d4f)type

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_hw\_event::type |
| --- |

Type.

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_frontend\_stmesp\_demux.h](log__frontend__stmesp__demux_8h_source.md)

- [log\_frontend\_stmesp\_demux\_hw\_event](structlog__frontend__stmesp__demux__hw__event.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
