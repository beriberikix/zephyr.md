---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structlog__frontend__stmesp__demux__packet__generic.html
original_path: doxygen/html/structlog__frontend__stmesp__demux__packet__generic.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp\_demux\_packet\_generic Struct Reference

[Trace and Debug Domain APIs](group__log__frontend__stmesp__apis.md) » [Logging frontend STMESP Demultiplexer API](group__log__frontend__stpesp__demux__apis.md)

Generic STP demux packet.
[More...](#details)

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h_source.md)>`

| Data Fields | |
| --- | --- |
|  | [MPSC\_PBUF\_HDR](#ac202cf6bc5bc8699a858e10de2c0c492) |
|  | Data for MPSC packet handling. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [type](#a7a86c5de5e5b33830d963add116c1feb): 2 |
|  | Type. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [content\_invalid](#a42d6b5192e0f9ba897a2986d645c6a6c): 1 |
|  | Flag indicating if packet is valid. |

## Detailed Description

Generic STP demux packet.

## Field Documentation

## [◆ ](#a42d6b5192e0f9ba897a2986d645c6a6c)content\_invalid

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_packet\_generic::content\_invalid |
| --- |

Flag indicating if packet is valid.

## [◆ ](#ac202cf6bc5bc8699a858e10de2c0c492)MPSC\_PBUF\_HDR

| log\_frontend\_stmesp\_demux\_packet\_generic::MPSC\_PBUF\_HDR |
| --- |

Data for MPSC packet handling.

## [◆ ](#a7a86c5de5e5b33830d963add116c1feb)type

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_packet\_generic::type |
| --- |

Type.

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_frontend\_stmesp\_demux.h](log__frontend__stmesp__demux_8h_source.md)

- [log\_frontend\_stmesp\_demux\_packet\_generic](structlog__frontend__stmesp__demux__packet__generic.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
