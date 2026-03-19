---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html
original_path: doxygen/html/structlog__frontend__stmesp__demux__trace__point.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp\_demux\_trace\_point Struct Reference

[Trace and Debug Domain APIs](group__log__frontend__stmesp__apis.md) » [Logging frontend STMESP Demultiplexer API](group__log__frontend__stpesp__demux__apis.md)

Packet with trace point.
[More...](#details)

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h_source.md)>`

| Data Fields | |
| --- | --- |
|  | [MPSC\_PBUF\_HDR](#ae3e776e4a470ccb3abd8f6a73ce7b21b) |
|  | Data for MPSC packet handling. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [type](#ab250b6782df720df3d1cdb37ab25a024): 2 |
|  | Type. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [content\_invalid](#a300adc8bd0882810ae4a5759a76857ce): 1 |
|  | Flag indicating if packet is valid. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [has\_data](#a0bdc2a3e1afb5748e08e68617f2ccbb6): 1 |
|  | Flag indicating if trace point includes data. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timestamp](#a6e1892f15fa3149f8161a1792420ba73): 58 |
|  | Timestamp. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [major](#a0105db760c6fac7b2eebd92047a7d760) |
|  | Major ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [id](#aeb86bfae01245a4778d08ac9c1ee138a) |
|  | ID. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [data](#ada954ed2971c2fc720a1d1f2634c0e2a) |
|  | Content. |

## Detailed Description

Packet with trace point.

## Field Documentation

## [◆ ](#a300adc8bd0882810ae4a5759a76857ce)content\_invalid

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_trace\_point::content\_invalid |
| --- |

Flag indicating if packet is valid.

## [◆ ](#ada954ed2971c2fc720a1d1f2634c0e2a)data

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_stmesp\_demux\_trace\_point::data |
| --- |

Content.

## [◆ ](#a0bdc2a3e1afb5748e08e68617f2ccbb6)has\_data

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_trace\_point::has\_data |
| --- |

Flag indicating if trace point includes data.

## [◆ ](#aeb86bfae01245a4778d08ac9c1ee138a)id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) log\_frontend\_stmesp\_demux\_trace\_point::id |
| --- |

ID.

## [◆ ](#a0105db760c6fac7b2eebd92047a7d760)major

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) log\_frontend\_stmesp\_demux\_trace\_point::major |
| --- |

Major ID.

## [◆ ](#ae3e776e4a470ccb3abd8f6a73ce7b21b)MPSC\_PBUF\_HDR

| log\_frontend\_stmesp\_demux\_trace\_point::MPSC\_PBUF\_HDR |
| --- |

Data for MPSC packet handling.

## [◆ ](#a6e1892f15fa3149f8161a1792420ba73)timestamp

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_trace\_point::timestamp |
| --- |

Timestamp.

## [◆ ](#ab250b6782df720df3d1cdb37ab25a024)type

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_frontend\_stmesp\_demux\_trace\_point::type |
| --- |

Type.

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_frontend\_stmesp\_demux.h](log__frontend__stmesp__demux_8h_source.md)

- [log\_frontend\_stmesp\_demux\_trace\_point](structlog__frontend__stmesp__demux__trace__point.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
