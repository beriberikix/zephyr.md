---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__buf__simple__state.html
original_path: doxygen/html/structnet__buf__simple__state.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_buf\_simple\_state Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Buffer Library](group__net__buf.md)

Parsing state of a buffer.
[More...](#details)

`#include <[buf.h](net_2buf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [offset](#a4061f8e50e14289b1ec999ef490c8fbf) |
|  | Offset of the data pointer from the beginning of the storage. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#af0e544fe2b018a7ff0b30970e9de8253) |
|  | Length of data. |

## Detailed Description

Parsing state of a buffer.

This is used for temporarily storing the parsing state of a buffer while giving control of the parsing to a routine which we don't control.

## Field Documentation

## [◆ ](#af0e544fe2b018a7ff0b30970e9de8253)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_simple\_state::len |
| --- |

Length of data.

## [◆ ](#a4061f8e50e14289b1ec999ef490c8fbf)offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_simple\_state::offset |
| --- |

Offset of the data pointer from the beginning of the storage.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[buf.h](net_2buf_8h_source.md)

- [net\_buf\_simple\_state](structnet__buf__simple__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
