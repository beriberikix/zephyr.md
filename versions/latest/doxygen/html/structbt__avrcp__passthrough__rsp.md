---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__avrcp__passthrough__rsp.html
original_path: doxygen/html/structbt__avrcp__passthrough__rsp.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_avrcp\_passthrough\_rsp Struct Reference

`#include <[avrcp.h](avrcp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [response](#a90c8c59bf3f333fa06d2b49d6e58af19) |
|  | [bt\_avrcp\_rsp\_t](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326 "AV/C response codes.") |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [operation\_id](#a940eb51fabd1987016f6888d1b38c18e) |
|  | [bt\_avrcp\_opid\_t](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84 "AV/C operation ids used in AVRCP passthrough commands.") |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [state](#aaa4ab701c9dee8d2ce8b4676f3ae140b) |
|  | [bt\_avrcp\_button\_state\_t](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881 "AVRCP button state flag.") |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#ad657103f9c751ba1e5fb1d447aff1718) |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [payload](#a9bd874797764bafb73a5663ccbb30bf8) |

## Field Documentation

## [◆ ](#ad657103f9c751ba1e5fb1d447aff1718)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avrcp\_passthrough\_rsp::len |
| --- |

## [◆ ](#a940eb51fabd1987016f6888d1b38c18e)operation\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avrcp\_passthrough\_rsp::operation\_id |
| --- |

[bt\_avrcp\_opid\_t](avrcp_8h.md#a3c997d96028343a0a5a4948dabe19b84 "AV/C operation ids used in AVRCP passthrough commands.")

## [◆ ](#a9bd874797764bafb73a5663ccbb30bf8)payload

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_avrcp\_passthrough\_rsp::payload |
| --- |

## [◆ ](#a90c8c59bf3f333fa06d2b49d6e58af19)response

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avrcp\_passthrough\_rsp::response |
| --- |

[bt\_avrcp\_rsp\_t](avrcp_8h.md#aba2d8faec2c3baf7403199ea8a509326 "AV/C response codes.")

## [◆ ](#aaa4ab701c9dee8d2ce8b4676f3ae140b)state

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avrcp\_passthrough\_rsp::state |
| --- |

[bt\_avrcp\_button\_state\_t](avrcp_8h.md#a15f9f868b056f17ea12d96530b7da881 "AVRCP button state flag.")

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[avrcp.h](avrcp_8h_source.md)

- [bt\_avrcp\_passthrough\_rsp](structbt__avrcp__passthrough__rsp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
