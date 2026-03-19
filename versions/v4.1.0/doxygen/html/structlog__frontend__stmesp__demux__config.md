---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structlog__frontend__stmesp__demux__config.html
original_path: doxygen/html/structlog__frontend__stmesp__demux__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp\_demux\_config Struct Reference

[Trace and Debug Domain APIs](group__log__frontend__stmesp__apis.md) » [Logging frontend STMESP Demultiplexer API](group__log__frontend__stpesp__demux__apis.md)

Demultiplexer configuration.
[More...](#details)

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | [m\_ids](#ada2f243b112324e99a53b831211cabce) |
|  | Array with expected major ID's. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [m\_ids\_cnt](#ad248eabec1eee58f5ef689004d5c7017) |
|  | Array length. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [source\_id\_buf](#aca85e1b671127e8803423f22b2d45a33) |
|  | Buffer for storing source ID's. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [source\_id\_buf\_len](#a643b5bd780342bf1944e5a63274aa305) |
|  | It must be multiple of number of major ID's count. |

## Detailed Description

Demultiplexer configuration.

## Field Documentation

## [◆ ](#ada2f243b112324e99a53b831211cabce)m\_ids

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)\* log\_frontend\_stmesp\_demux\_config::m\_ids |
| --- |

Array with expected major ID's.

## [◆ ](#ad248eabec1eee58f5ef689004d5c7017)m\_ids\_cnt

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_stmesp\_demux\_config::m\_ids\_cnt |
| --- |

Array length.

Must be not bigger than [LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_MAX](group__log__frontend__stpesp__demux__apis.md#ga8f23994b914214a2c83d2e9aa63f0cb5 "LOG_FRONTEND_STMESP_DEMUX_MAJOR_MAX").

## [◆ ](#aca85e1b671127e8803423f22b2d45a33)source\_id\_buf

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* log\_frontend\_stmesp\_demux\_config::source\_id\_buf |
| --- |

Buffer for storing source ID's.

Used for turbo logging.

## [◆ ](#a643b5bd780342bf1944e5a63274aa305)source\_id\_buf\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) log\_frontend\_stmesp\_demux\_config::source\_id\_buf\_len |
| --- |

It must be multiple of number of major ID's count.

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_frontend\_stmesp\_demux.h](log__frontend__stmesp__demux_8h_source.md)

- [log\_frontend\_stmesp\_demux\_config](structlog__frontend__stmesp__demux__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
