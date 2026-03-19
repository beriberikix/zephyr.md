---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/unionlog__frontend__stmesp__demux__packet.html
original_path: doxygen/html/unionlog__frontend__stmesp__demux__packet.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp\_demux\_packet Union Reference

[Trace and Debug Domain APIs](group__log__frontend__stmesp__apis.md) » [Logging frontend STMESP Demultiplexer API](group__log__frontend__stpesp__demux__apis.md)

Union of all packet types.
[More...](#details)

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* | [rgeneric](#ac712f4dc2ca645e2ba6f6c638b41bf10) |
|  | Pointer to generic mpsc\_pbuf const packet. |
| union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* | [generic](#a71d8ecb5afa1ac2cd64aaf21916119c5) |
|  | Pointer to generic mpsc\_pbuf packet. |
| struct [log\_frontend\_stmesp\_demux\_log](structlog__frontend__stmesp__demux__log.md) \* | [log](#ac75deeb2f665aeb5dcfd94090aa1a1cf) |
|  | Pointer to the log message. |
| struct [log\_frontend\_stmesp\_demux\_trace\_point](structlog__frontend__stmesp__demux__trace__point.md) \* | [trace\_point](#aa68b1022f97c8806ee430a541190fc82) |
|  | Pointer to the trace point message. |
| struct [log\_frontend\_stmesp\_demux\_hw\_event](structlog__frontend__stmesp__demux__hw__event.md) \* | [hw\_event](#ae764f7a3b04e66af22c52aa1d52a441e) |
|  | Pointer to the HW event message. |
| struct [log\_frontend\_stmesp\_demux\_packet\_generic](structlog__frontend__stmesp__demux__packet__generic.md) \* | [generic\_packet](#a30d3cfc6071bebc1614f2f67c8a950c7) |
|  | Pointer to the generic log\_frontend\_stmesp\_demux packet. |

## Detailed Description

Union of all packet types.

## Field Documentation

## [◆ ](#a71d8ecb5afa1ac2cd64aaf21916119c5)generic

| union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md)\* log\_frontend\_stmesp\_demux\_packet::generic |
| --- |

Pointer to generic mpsc\_pbuf packet.

## [◆ ](#a30d3cfc6071bebc1614f2f67c8a950c7)generic\_packet

| struct [log\_frontend\_stmesp\_demux\_packet\_generic](structlog__frontend__stmesp__demux__packet__generic.md)\* log\_frontend\_stmesp\_demux\_packet::generic\_packet |
| --- |

Pointer to the generic log\_frontend\_stmesp\_demux packet.

## [◆ ](#ae764f7a3b04e66af22c52aa1d52a441e)hw\_event

| struct [log\_frontend\_stmesp\_demux\_hw\_event](structlog__frontend__stmesp__demux__hw__event.md)\* log\_frontend\_stmesp\_demux\_packet::hw\_event |
| --- |

Pointer to the HW event message.

## [◆ ](#ac75deeb2f665aeb5dcfd94090aa1a1cf)log

| struct [log\_frontend\_stmesp\_demux\_log](structlog__frontend__stmesp__demux__log.md)\* log\_frontend\_stmesp\_demux\_packet::log |
| --- |

Pointer to the log message.

## [◆ ](#ac712f4dc2ca645e2ba6f6c638b41bf10)rgeneric

| const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md)\* log\_frontend\_stmesp\_demux\_packet::rgeneric |
| --- |

Pointer to generic mpsc\_pbuf const packet.

## [◆ ](#aa68b1022f97c8806ee430a541190fc82)trace\_point

| struct [log\_frontend\_stmesp\_demux\_trace\_point](structlog__frontend__stmesp__demux__trace__point.md)\* log\_frontend\_stmesp\_demux\_packet::trace\_point |
| --- |

Pointer to the trace point message.

---

The documentation for this union was generated from the following file:

- zephyr/logging/[log\_frontend\_stmesp\_demux.h](log__frontend__stmesp__demux_8h_source.md)

- [log\_frontend\_stmesp\_demux\_packet](unionlog__frontend__stmesp__demux__packet.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
