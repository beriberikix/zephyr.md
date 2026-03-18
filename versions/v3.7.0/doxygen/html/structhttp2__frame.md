---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structhttp2__frame.html
original_path: doxygen/html/structhttp2__frame.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http2\_frame Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [HTTP server API](group__http__server.md)

HTTP/2 frame representation.
[More...](#details)

`#include <[server.h](server_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [length](#ab626f6cca2d5a92ba8c6bbc24828b84a) |
|  | Frame payload length. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [stream\_identifier](#a0dfc83689ba3bdefe7bd27ab21bcd543) |
|  | Stream ID the frame belongs to. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a40d75871da54ad54c7e0038cb03afe59) |
|  | Frame type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a6d7bbf365456cba136bb523f513c515c) |
|  | Frame flags. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [padding\_len](#aa2124f60dc9ab2b692359fac07002528) |
|  | Frame padding length. |

## Detailed Description

HTTP/2 frame representation.

## Field Documentation

## [◆ ](#a6d7bbf365456cba136bb523f513c515c)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) http2\_frame::flags |
| --- |

Frame flags.

## [◆ ](#ab626f6cca2d5a92ba8c6bbc24828b84a)length

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) http2\_frame::length |
| --- |

Frame payload length.

## [◆ ](#aa2124f60dc9ab2b692359fac07002528)padding\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) http2\_frame::padding\_len |
| --- |

Frame padding length.

## [◆ ](#a0dfc83689ba3bdefe7bd27ab21bcd543)stream\_identifier

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) http2\_frame::stream\_identifier |
| --- |

Stream ID the frame belongs to.

## [◆ ](#a40d75871da54ad54c7e0038cb03afe59)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) http2\_frame::type |
| --- |

Frame type.

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[server.h](server_8h_source.md)

- [http2\_frame](structhttp2__frame.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
