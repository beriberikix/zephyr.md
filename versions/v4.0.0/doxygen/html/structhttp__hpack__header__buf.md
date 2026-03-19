---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structhttp__hpack__header__buf.html
original_path: doxygen/html/structhttp__hpack__header__buf.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_hpack\_header\_buf Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP HPACK](group__http__hpack.md)

HTTP2 header field with decoding buffer.
[More...](#details)

`#include <[hpack.h](hpack_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#ac0b781b733a16dc0c9e99753a4d2b25d) |
|  | A pointer to the decoded header field name. |
| const char \* | [value](#a957db215f89359b64a76e98e878e8c83) |
|  | A pointer to the decoded header field value. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [name\_len](#ad6079192782eec8e4a0c1d89018c6d7b) |
|  | Length of the decoded header field name. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [value\_len](#a48291a396efc761d85ffb5f46ddddf07) |
|  | Length of the decoded header field value. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [buf](#a6d1d09942d85f148e3979cf88f1cb87a) [HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE] |
|  | Encoding/Decoding buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [datalen](#a9d1c7d2daaf55f201c03e7438b033abf) |
|  | Length of the data in the decoding buffer. |

## Detailed Description

HTTP2 header field with decoding buffer.

## Field Documentation

## [◆ ](#a6d1d09942d85f148e3979cf88f1cb87a)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) http\_hpack\_header\_buf::buf[HTTP\_SERVER\_HUFFMAN\_DECODE\_BUFFER\_SIZE] |
| --- |

Encoding/Decoding buffer.

Used with Huffman encoding/decoding.

## [◆ ](#a9d1c7d2daaf55f201c03e7438b033abf)datalen

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_hpack\_header\_buf::datalen |
| --- |

Length of the data in the decoding buffer.

## [◆ ](#ac0b781b733a16dc0c9e99753a4d2b25d)name

| const char\* http\_hpack\_header\_buf::name |
| --- |

A pointer to the decoded header field name.

## [◆ ](#ad6079192782eec8e4a0c1d89018c6d7b)name\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_hpack\_header\_buf::name\_len |
| --- |

Length of the decoded header field name.

## [◆ ](#a957db215f89359b64a76e98e878e8c83)value

| const char\* http\_hpack\_header\_buf::value |
| --- |

A pointer to the decoded header field value.

## [◆ ](#a48291a396efc761d85ffb5f46ddddf07)value\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_hpack\_header\_buf::value\_len |
| --- |

Length of the decoded header field value.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[hpack.h](hpack_8h_source.md)

- [http\_hpack\_header\_buf](structhttp__hpack__header__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
